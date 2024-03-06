import { createClient } from 'redis';

const redisClient = createClient();

redisClient = createClient();
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});
redisClient.on('connect', () => console.log('Redis client connected to the server'));
