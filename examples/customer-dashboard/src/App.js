import { useEffect, useState } from 'react';

function App() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    fetch('http://localhost:1234/api/customers')
      .then((resp) => resp.json())
      .then((data) => setCustomers(data));
  }, []);

  return (
    <>
      <div className='alert alert-primary'>
        <div className='container'>
          <h1>Customer Dashboard</h1>
        </div>
      </div>

      <div className='container'>
        <table className='table'>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>City</th>
              <th>Email</th>
            </tr>
          </thead>

          <tbody>
            {customers.map((c) => (
              <tr key={c.id}>
                <td>{c.id}</td>
                <td>{c.name}</td>
                <td>{c.city}</td>
                <td>{c.email}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default App;
