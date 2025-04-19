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
    const admins = database.collection("admin");

    const user = await admins.findOne({ email: email, passwd: password });

    if (user) {
      var mess_of_admin = user.mess;
      var query = { current_mess : mess_of_admin};
      const students_registered_for_mess = await admins.find(query,{projection : { _id : 0,name : 1,current_mess : 1}}).toArray();

      
      res.json(students_registered_for_mess);
    } else {
      res.status(401).json({ message: 'Invalid email or password' });
    }
  } catch (err) {
    console.error('Database error:', err);
    res.status(500).json({ message: 'Server error' });
  } 
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'admin_login.html'));
  });
  
app.listen(PORT, () => {
  console.log(`Backend running at http://localhost:${PORT}`);
});


// const { useState } = React;

// function App() {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     const emailValue = email.trim();
//     const passwordValue = password.trim();

//     if (!emailValue) {
//       alert('Email is required');
//       return;
//     }

//     if (!passwordValue) {
//       alert('Password is required');
//       return;
//     }

//     try {
//       const response = await fetch('http://localhost:5500/login', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ email: emailValue, password: passwordValue }),
//       });

//       const data = await response.json();

//       if (response.ok) {
//         const student_details= data.details
//         localStorage.setItem('studentDetails',JSON.stringify(student_details) );
//         alert('Login successful!');
//         window.location.href = 'admin_dashboard.html';
//       } else {
//         alert(data.message || 'Invalid credentials');
//       }
//     } catch (error) {
//       console.error('Fetch error:', error);
//       alert('Server error. Please try again.');
//     }
//   };

//   return (
    
//     <>
    
//       <h2>Admin Login</h2>
//       <form onSubmit={handleSubmit}>
//         <div className="input-group">
//           <label>Email</label>
//           <input
//             type="email"
//             value={email}
//             onChange={(e) => setEmail(e.target.value)}
//             placeholder="Enter your email"
//           />
//         </div>
//         <div className="input-group">
//           <label>Password</label>
//           <input
//             type="password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//             placeholder="Enter your password"
//           />
//         </div>
//         <button type="submit" className="login-btn">Login</button>
//       </form>
//     </>
//   );
// }

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(<App />);