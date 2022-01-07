import React from "react";
import Linechart from "./Chartjs/Linechart";
import Dashboard from "./Dashboard/Dashboard";
import Login from "./Login/Login";
import LineChartG2 from "./G2plot/LineChartG2";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    // <LineChartG2></LineChartG2>
    <Router>
      {/* A <Routes> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
      <>
        <Dashboard />
        {/* <Routes>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/">
            <Dashboard />
          </Route>
        </Routes> */}
      </>
    </Router>
  );
}

export default App;
