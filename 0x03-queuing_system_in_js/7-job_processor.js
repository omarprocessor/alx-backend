import kue from 'kue';

// Create queue
const queue = kue.createQueue();

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    
    if (blacklistedNumbers.includes(phoneNumber)) {
        done(new Error(`Phone number ${phoneNumber} is blacklisted`));
        return;
    }

    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

// Process jobs
queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});

// Keep the process running
process.on('SIGINT', () => {
    queue.shutdown(5000, (error) => {
        if (error) throw error;
        process.exit(0);
    });
});
