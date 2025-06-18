const redis = require('redis');

// Create Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

// Keep the process running
process.on('SIGINT', () => {
    client.quit();
    process.exit(0);
});
