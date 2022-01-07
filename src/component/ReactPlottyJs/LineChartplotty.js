import React from "react";
import Plotly from "plotly.js";
import createPlotlyComponent from "react-plotly.js/factory";
const Plot = createPlotlyComponent(Plotly);

const LineChartPlotty = () => {
  return (
    <Plot
      data={[
        {
          x: [1, 2, 3],
          y: [2, 6, 3],
          type: "scatter",
          mode: "lines+markers",
          marker: { color: "red" },
        },
        { type: "bar", x: [1, 2, 3], y: [2, 5, 3] },
      ]}
      layout={{ autosize: true, title: "A Fancy Plot" }}
      useResizeHandler={true}
      style={{ width: "100%", height: "100%" }}
    />
  );
};

export default LineChartPlotty;
