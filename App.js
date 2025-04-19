const { useState } = React;

function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const emailValue = email.trim();
    const passwordValue = password.trim();

    if (!emailValue) {
      alert('Email is required');
      return;
    }

    if (!passwordValue) {
      alert('Password is required');
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: emailValue, password: passwordValue }),
      });

      const data = await response.json();

      if (response.ok) {
        alert('Login successful!');
        // window.location.href = 'dashboard.html';
      } else {
        alert(data.message || 'Invalid credentials');
      }
    } catch (error) {
      console.error('Fetch error:', error);
      alert('Server error. Please try again.');
    }
  };

  return (
    
    <>
    
      <h2>Mess Student Login</h2>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label>Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
          />
        </div>
        <div className="input-group">
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
          />
        </div>
        <button type="submit" className="login-btn">Login</button>
        <div className="links">
          <a href="https://reset.iith.ac.in/ldap/" target="_blank">Forgot Password?</a><br />
          <a href="admin_login.html">Mess Office/Admin Login</a>
        </div>
      </form>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);