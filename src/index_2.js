// import React from 'react';
// import ReactDOM from 'react-dom';
// import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();

import React from "react";
import ReactDOM from "react-dom";
import ShowcaseLayout from "./ShowcaseLayout";
import Dashboard from "./component/Dashboard/Dashboard";

class ExampleLayout extends React.Component {
  constructor(props) {
    super(props);
    this.state = { layout: [] };
    this.onLayoutChange = this.onLayoutChange.bind(this);
  }

  onLayoutChange(layout) {
    this.setState({ layout: layout });
  }

  stringifyLayout() {
    return this.state.layout.map(function (l) {
      return (
        <div className="layoutItem" key={l.i}>
          <b>{l.i}</b>: [{l.x}, {l.y}, {l.w}, {l.h}]
        </div>
      );
    });
  }

  render() {
    return (
      <div>
        <div className="layoutJSON">
          Displayed as <code>[x, y, w, h]</code>:
          <div className="columns">{this.stringifyLayout()}</div>
        </div>
        <ShowcaseLayout onLayoutChange={this.onLayoutChange} />
      </div>
    );
  }
}

const contentDiv = document.getElementById("root");
const gridProps = window.gridProps || {};
ReactDOM.render(React.createElement(ExampleLayout), contentDiv);
