import './App.css';
import{ useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Stocks from "./navPages/stocks.js"
import Bonds from "./navPages/bonds.js"
import Funds from "./navPages/mutualFunds.js"
import CD from "./navPages/CD.js"

function App() {

  const [funds, setFunds] = useState(0);
  const [worth, setWorth] = useState(0);

  const [ newsData, setNewsData ] = useState([]);

    function getMarket() {
      fetch('http://localhost:1080/market/')
      .then(response => response.json())
      .then(data => console.log(data));
    }

    function getPortfolio() {
      fetch('http://localhost:1080/portfolio/')
      .then(response => response.json())
      .then(data => 
        {
          setFunds(data.funds);
          setWorth(data.worth);
        });
    }

    function wait(time) {
      fetch('http://localhost:1080/wait/' + time + '/')
      .then(response => response.json())
      .then(data => console.log(data));
    }

    function news() {
      fetch('http://localhost:1080/news/')
      .then(response => response.json())
      .then(data => {
        setNewsData(data);
      });
    }

  return <body>
    <button onClick={getMarket}>
      Get Market
    </button>
    <button onClick={getPortfolio}>
      Get Portfolio
    </button>
    <button onClick={() => wait(1)}>
      Wait 1
    </button>
    <button onClick={() => wait(2)}>
      Wait 2
    </button>
    <button onClick={news}>
      News
    </button>

    <div class="top">
      <div class="column1">
        <h1>Money: {funds}</h1>
        <h1>Net Worth: {worth}</h1>
      </div>
      <div class="column2">
        <h1>Stocks: </h1>
        <h1>Bonds: </h1>
        <h1>Certificate of Deposits (CDs): </h1>
        <h1>Mutual Funds: </h1>
      </div>
      <div class="column3">
        <h1>Year (Insert year) of 4</h1>
        <h1>Month (Insert Month)</h1>
      </div>
    </div>

    <div class = "news">
      <h1>News</h1>
      <div>
        {
        newsData.map((newsData) =>
          <div className= "newsData">
            <h1 className = "newsTitle"> {newsData.title}</h1>
            <h2 className = "newsDescription">{newsData.description}</h2>
          </div>
          )
        }
      </div>
    </div>

    <div class = "investments">
      <h1>Investments</h1>
      <Router>
        <Routes>
          <Route path="/stocks" element={<Stocks />} />
          <Route path="/bonds" element={<Bonds />} />
          <Route path="/mutualFunds" element={<Funds />} />
          <Route path="/CDs" element={<CD />} />
        </Routes>
      </Router>
    </div>
  </body>
}

export default App;