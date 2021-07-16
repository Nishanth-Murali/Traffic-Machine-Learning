import './App.css';
import Chart from './Chart';
import Navbar from './Components/Navbar';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"; 
import Home from './Pages/Home';
import BarChart from './Pages/BarChart';
import LineChart from './Pages/LineChart';

function App() {
  return (
    <div className="App">
        <Router>
          <Navbar />
          <Switch>
            <Route path='/' exact component={Home}/>
            <Route path='/BarChart' component={BarChart}/>
            <Route path='/LineChart' component={LineChart}/>
          </Switch>
        </Router>
    </div>
  );
}

export default App;
