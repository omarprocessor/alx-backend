import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();

// Parse JSON bodies
app.use(express.json());

// List of products
const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Promisify Redis commands
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Get product by ID
const getItemById = (id) => listProducts.find(item => item.id === id);

// Reserve stock
const reserveStockById = async (itemId, stock) => {
    await setAsync(`item.${itemId}`, stock);
};

// Get current reserved stock
const getCurrentReservedStockById = async (itemId) => {
    const stock = await getAsync(`item.${itemId}`);
    return stock ? parseInt(stock) : 0;
};

// Routes
app.get('/list_products', async (req, res) => {
    const products = listProducts.map(item => ({
        itemId: item.id,
        itemName: item.name,
        price: item.price,
        initialAvailableQuantity: item.stock
    }));
    res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    
    if (!item) {
        res.json({ status: 'Product not found' });
        return;
    }

    const currentStock = await getCurrentReservedStockById(itemId);
    res.json({
        itemId: item.id,
        itemName: item.name,
        price: item.price,
        initialAvailableQuantity: item.stock,
        currentQuantity: currentStock
    });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);

    if (!item) {
        res.json({ status: 'Product not found' });
        return;
    }

    const currentStock = await getCurrentReservedStockById(itemId);
    if (currentStock <= 0) {
        res.json({ status: 'Not enough stock available', itemId });
        return;
    }

    await reserveStockById(itemId, currentStock - 1);
    res.json({ status: 'Reservation confirmed', itemId });
});

// Start server
const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
