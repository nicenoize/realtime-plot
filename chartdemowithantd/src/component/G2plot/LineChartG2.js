import React, { useEffect, useState } from "react";
import * as G2PlotClient from "../../Client/G2PlotClient";
import { Line } from "@antv/g2plot";

const LineChartG2 = () => {
  const [chart, setChart] = useState();
  useEffect(() => {
    const test = async () => {
      G2PlotClient.getDataG2Plot().then((data) => {
        const line1 = new Line("container", {
          data,
          xField: "year",
          yField: "value",
        });
        const line = new Line("container", {
          data,
          padding: "auto",
          xField: "Secs",
          yField: "Value",
          xAxis: {
            tickCount: 5,
          },
          slider: {
            start: 0.35,
            end: 0.5,
          },
          responsive: true,
        });
        setChart(line);
      });
    };
    test();
  }, []);

  useEffect(() => {
    if (chart) {
      chart.render();
    }
  }, [chart]);
  return <div id="container"></div>;
};

export default LineChartG2;
