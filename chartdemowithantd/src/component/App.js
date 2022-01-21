import React from "react";
import LineChart from "./Chartjs/Linechart";
import Dashboard from "./Dashboard/Dashboard";
import Login from "./Login/Login";
import LineChartG2 from "./G2plot/LineChartG2";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    // <LineChartG2></LineChartG2>
    <Routes>
      {/* A <Routes> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
      <>
        <Route path="/" element={<Dashboard />}></Route>
        <Route path="/login" element={<Login />}></Route>
        <Route path="/linechartg2" element={<LineChartG2 />}></Route>
        <Route path="/linechart" element={<LineChart />}></Route>
      </>
    </Routes>
  );
}

export default App;
