import kue from 'kue';

// Create queue
const queue = kue.createQueue();

// Create job
const job = queue.create('push_notification_code', {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account'
}).save((err) => {
    if (err) throw err;
    console.log(`Notification job created: ${job.id}`);
});

// Handle job events
job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', (error) => {
    console.log(`Notification job failed: ${error}`);
});
