import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
    let queue;
    let jobs;

    beforeEach(() => {
        queue = kue.createQueue();
        jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            }
        ];
    });

    afterEach(() => {
        queue.testMode.enter();
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('should display an error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('not an array', queue)).toThrow('Jobs is not an array');
    });

    it('should create two new jobs to the queue', () => {
        const job1 = {
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
        };
        const job2 = {
            phoneNumber: '4153518781',
            message: 'This is the code 4562 to verify your account'
        };
        
        const testJobs = [job1, job2];
        createPushNotificationsJobs(testJobs, queue);

        expect(queue.testMode.jobs.length).toBe(2);
        expect(queue.testMode.jobs[0].data).toEqual(job1);
        expect(queue.testMode.jobs[1].data).toEqual(job2);
    });
});
