import kue from 'kue';

// Create queue
const queue = kue.createQueue();

// Function to send notification
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs
queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done();
});

// Keep the process running
process.on('SIGINT', () => {
    queue.shutdown(5000, (error) => {
        if (error) throw error;
        process.exit(0);
    });
});
