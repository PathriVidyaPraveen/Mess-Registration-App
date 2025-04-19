const express = require('express');
const cors = require('cors');
const { MongoClient } = require('mongodb');

const path = require('path');
const app = express();

const PORT = 5500;

const url = "mongodb+srv://dinesh_23:tc97386@cluster0.7a7ovpk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
const client = new MongoClient(url);

app.use(cors());
app.use(express.json());
app.use(express.static(__dirname)); 

app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  try {
    await client.connect();
    const database = client.db("mess");
    const students = database.collection("students");

    const user = await students.findOne({ email: email, passwd: password });
    

    if (user) {
      const current_mess_of_student = user.current_mess;
      const previous_mess_of_student = user.previous_mess;

      res.json({ message: 'Login successful' , current_mess: current_mess_of_student, previous_mess: previous_mess_of_student});
    } else {
      res.status(401).json({ message: 'Invalid email or password' });
    }
  } catch (err) {
    console.error('Database error:', err);
    res.status(500).json({ message: 'Server error' });
  } 
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'messregistration.html'));
  });
  
app.listen(PORT, () => {
  console.log(`Backend running at http://localhost:${PORT}`);
});


