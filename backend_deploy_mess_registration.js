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

app.post('/deploy', async (req, res) => {
  

  try {
    await client.connect();
    const database = client.db("mess");
    const students = database.collection("students");

    const allStudents = await students.find({}).toArray();

    for(let student of allStudents){
        const student_id = student._id;
        const current_mess_of_student = student.current_mess;
        const removed_mess = await students.updateOne({_id : student_id} , { $set : {previous_mess : current_mess_of_student , current_mess : ""}});
    }



    
    res.json({ message : "Successfully deployed"});

  } catch (err) {
    console.error('Database error:', err);
    res.status(500).json({ message: 'Server error' });
  } 
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'admin_dashboard.html'));
  });
  
app.listen(PORT, () => {
  console.log(`Backend running at http://localhost:${PORT}`);
});

