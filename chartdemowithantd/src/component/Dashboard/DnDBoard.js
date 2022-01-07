import React from "react";
import Grid from "./Grid";
const DnDBoard = () => {
  return (
    <div
      className="site-layout-background"
      style={{ padding: 24, minHeight: 360 }}
    >
      <div className="layoutJSON">
        Displayed as <code>[x, y, w, h]</code>:
        {/* <div className="columns">{stringifyLayout()}</div> */}
      </div>
      {/* <Grid onLayoutChange={onLayoutChange}></Grid> */}
    </div>
  );
};
export default DnDBoard;
