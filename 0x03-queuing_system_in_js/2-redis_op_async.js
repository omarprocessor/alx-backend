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
const getAsync = promisify(client.get).bind(client);

// Function to display school value with async/await
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.error(error);
    }
}

// Test the function
displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');

// Keep the process running
process.on('SIGINT', () => {
    client.quit();
    process.exit(0);
});
