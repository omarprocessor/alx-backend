import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

// Promisify Redis commands
const hsetAsync = promisify(client.hset).bind(client);
const hgetallAsync = promisify(client.hgetall).bind(client);

// Create hash
async function createHash() {
    const hashData = {
        Portland: '50',
        Seattle: '80',
        'New York': '20',
        Bogota: '20',
        Cali: '40',
        Paris: '2'
    };

    for (const [key, value] of Object.entries(hashData)) {
        await hsetAsync('ALX', key, value);
        console.log('Reply: 1'); // hset returns 1 for success
    }
}

// Display hash
async function displayHash() {
    const result = await hgetallAsync('ALX');
    console.log(result);
}

// Execute operations
createHash().then(() => displayHash());

// Keep the process running
process.on('SIGINT', () => {
    client.quit();
    process.exit(0);
});
