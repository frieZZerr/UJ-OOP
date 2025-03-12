import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Products from './components/Products';
import Payments from './components/Payments';
import Cart from './components/Cart';

function App() {
  return (
    <Router>
      <header>
        <h1>4-Paws</h1>
        <nav>
          <ul>
            <li><Link to="/products">Products</Link></li>
            <li><Link to="/cart">Cart</Link></li>
            <li><Link to="/payments">Payments</Link></li>
          </ul>
        </nav>
      </header>
      <main>
        <div className="content">
          <Routes>
            <Route path="/products" element={<Products />} />
            <Route path="/cart" element={<Cart />} />
            <Route path="/payments" element={<Payments />} />
          </Routes>
        </div>
      </main>
    </Router>
  );
}

export default App;
