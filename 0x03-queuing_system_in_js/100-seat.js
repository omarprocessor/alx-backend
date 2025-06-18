import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

// Promisify Redis commands
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Initialize seat reservation
const INITIAL_SEATS = 50;
let reservationEnabled = true;

// Initialize seats
setAsync('available_seats', INITIAL_SEATS);

// Routes
app.get('/available_seats', async (req, res) => {
    const seats = await getAsync('available_seats');
    res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        res.json({ status: 'Reservation are blocked' });
        return;
    }

    const job = queue.create('reserve_seat', {}).save((err) => {
        if (err) {
            res.json({ status: 'Reservation failed' });
            return;
        }
        console.log(`Seat reservation job ${job.id} in process`);
        res.json({ status: 'Reservation in process' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (error) => {
        console.log(`Seat reservation job ${job.id} failed: ${error}`);
    });
});

app.get('/process', async (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        try {
            const seats = await getAsync('available_seats');
            const currentSeats = parseInt(seats);

            if (currentSeats <= 0) {
                reservationEnabled = false;
                throw new Error('Not enough seats available');
            }

            await setAsync('available_seats', currentSeats - 1);
            done();
        } catch (error) {
            done(error);
        }
    });
});

// Start server
const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
