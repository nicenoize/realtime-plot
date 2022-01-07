import React, { useState, useEffect } from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";
import * as Client from "../../Client/Client";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);
// const jsonLabels = ["Secs", "Val", "Nanos", "Severity", "Status"];

let Linechart = (props) => {
  const [dataToPass, setDataToPass] = useState();

  const options = {
    responsive: true,
    autoSkip: false,
    title: {
      display: true,
      text: "Chart Title",
    },
    scales: {
      y: {
        suggestedMin: 0.004,
        suggestedMax: 0.005,
      },
    },
  };

  useEffect(() => {
    const test = async () => {
      await Client.getData()
        .then((data) => {
          console.log("Labael");
          console.log(data);
          let longArrayinArrayKeys = data.map((object) => Object.keys(object));
          let arraySec = data.map((object) => {
            const { secs } = object;
            return secs;
          });
          let arrayVal = data.map((object) => {
            const { val } = object;
            return val;
          });
          console.log("arrayVal");
          console.log(arrayVal);
          // let arrayNanos = data.map((object) => {
          //   const { nanos } = object;
          //   return nanos;
          // });
          // let arrayServerity = data.map((object) => {
          //   const { severity } = object;
          //   return severity;
          // });
          // let arrayStatus = data.map((object) => {
          //   const { status } = object;
          //   return status;
          // });
          console.log("Secs");
          console.log(arraySec);
          let longArrayinArray = data.map((object) => Object.keys(object));
          let longKeysarrays = [].concat.apply([], longArrayinArrayKeys);
          let newLabels = [...new Set(longKeysarrays)];
          let newSecs = [...new Set(arraySec)];
          console.log("newSecs");
          console.log(newSecs);
          let newVal = [...new Set(arrayVal)];
          console.log("newVal");
          console.log(newVal);

          console.log("newLabels");
          console.log(newLabels);
          const dataPass = {
            labels: arraySec,
            datasets: [
              {
                label: "Dataset 1",
                // label: "Dataset1",
                data: arrayVal,
                fill: false,
                backgroundColor: "rgb(53, 162, 235)",
                borderColor: "rgb(53, 162, 235, 0.5)",
              },
            ],
          };
          setDataToPass(dataPass);
        })
        .catch((error) => {
          console.error(error);
        });
    };
    test();
  }, []);

  // const dataArray = getData();
  // console.log("dataArray1");
  // console.log(dataArray);
  // const labes = getData().then((data) => {
  //   console.log("Labael");
  //   console.log(data);
  //   const labels = data;
  //   const dataPass = {
  //     labels,
  //     datasets: [
  //       {
  //         label: "Dataset1",
  //         data: [labels.map],
  //         fill: false,
  //         backgroundColor: "rgb(255,99,132)",
  //         borderColor: "rgb(255,99,132,0.2),",
  //       },
  //     ],
  //   };
  // });
  // // const [jsonData] = dataArray;
  // const { data } = jsonData; // this is a array of objects!

  // const arrayInArrayDuplications = data.map((dataObject) => {
  //   Object.keys(dataObject);
  // });

  // let oneArray = [].concat.apply([], arrayInArrayDuplications);
  // let labels = [...new Set(oneArray)];
  // useEffect(() => {
  //   console.log("dataToPass");
  //   console.log(dataToPass);
  // }, [dataToPass]);
  return dataToPass ? <Line option={options} data={dataToPass} /> : [];
};

export default Linechart;
