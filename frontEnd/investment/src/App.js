function App() {


    function getMarket() {
      fetch('http://localhost:1080/market/')
      .then(response => response.json())
      .then(data => console.log(data));
    }

    function getPortfolio() {
      fetch('http://localhost:1080/portfolio/')
      .then(response => response.json())
      .then(data => console.log(data));
    }

    function wait(time) {
      fetch('http://localhost:1080/wait/' + time + '/')
      .then(response => response.json())
      .then(data => console.log(data));
    }

    function news() {
      fetch('http://localhost:1080/news/')
      .then(response => response.json())
      .then(data => console.log(data));
    }

  return <top>
    {/* <div1>
      <h1>Money: </h1>
      <h1>Net Worth: </h1>
    </div1>
    <div2>
      <h1>Stocks: </h1>
      <h1>Bonds: </h1>
      <h1>Certificate of Deposits (CDs): </h1>
      <h1>Mutual Funds: </h1>
    </div2>
    <div3>
      <h1>Year (Insert year) of 4</h1>
      <h1>Month (Insert Month)</h1>
    </div3> */}
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

    <div class="row">
      <div class="column">
        <h1>Money: </h1>
        <h1>Net Worth: </h1>
      </div>
      <div class="column">
        <h1>Stocks: </h1>
        <h1>Bonds: </h1>
        <h1>Certificate of Deposits (CDs) ikjdflasjdfl;asdlfkjs: </h1>
        <h1>Mutual Funds: </h1>
      </div>
      <div class="column">
        <h1>Year (Insert year) of 4</h1>
        <h1>Month (Insert Month)</h1>
      </div>
    </div>
  </top>;
}

export default App;