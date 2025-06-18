import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

// Function to set a new school
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) throw err;
        console.log('Reply:', reply);
    });
}

// Function to display school value
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) throw err;
        console.log(reply);
    });
}

// Test the functions
displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');

// Keep the process running
process.on('SIGINT', () => {
    client.quit();
    process.exit(0);
});
