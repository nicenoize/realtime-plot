import { Line } from "@antv/g2plot";

//Constants
const jsonUrl =
  "http://aav.rz-berlin.mpg.de:17668/retrieval/data/getData.json?pv=FHIMP%3AHeDrop%3AForepressure_Droplet_Src";
const get = {
  method: "GET",
  mode: "cors",
};

export const getData = async () => {
  // const token= "";
  // const post = `${url}/${token}`;
  return fetch(jsonUrl, get)
    .then((response) => {
      return response.json();
    })
    .then((responseJson) => {
      let [data] = responseJson;
      console.log("[data]= responseJson");
      console.log("data.data");
      console.log(data.data);

      return data.data;
    })
    .then((data) => {
      const preData = data.map((object) => {
        const { secs, val } = object;
        return { Secs: secs, Value: val };
      });
      console.log("preData");
      console.log(preData);
      return preData;
    })
    .then((endData) => {
      const line = new Line("container", {
        endData,
        padding: "auto",
        xField: "Secs",
        yField: "Value",
        xAxis: {
          tickCount: 5,
        },
        slider: {
          start: 0.1,
          end: 0.5,
        },
      });
      Line.render();
    })
    .catch((error) => {
      console.error(error);
    });
};