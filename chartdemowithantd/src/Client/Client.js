//this is the Api to the backend/JsonData dummy
const url = "https://reqres.in/api/users";
// {
//   "email": "eve.holt@reqres.in",
//   "password": "cityslicka"
// }

// {
//   "token": "QpwL5tke4Pnpja7X4"
// }
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
    .catch((error) => {
      console.error(error);
    });
};

export const getUser = async () => {
  return fetch(url, get)
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
    .catch((error) => {
      console.error(error);
    });
};
let client = () => {};
export default client;
