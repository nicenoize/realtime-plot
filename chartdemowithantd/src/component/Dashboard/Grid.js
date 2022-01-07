import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";
import _ from "lodash";
import { Responsive, WidthProvider } from "react-grid-layout";
// import Linechart from "../Chartjs/Linechart";
import ExampleChart from "../Chartjs/ExampleChart";
// import LineChartPlotty from "../ReactPlottyJs/LineChartplotty";
import LineChartPlotty from "../ReactPlottyJs/LineChartplotty";
const ResponsiveReactGridLayout = WidthProvider(Responsive);
const generateLayout = () => {
  return _.map(_.range(0, 25), (item, i) => {
    var y = Math.ceil(Math.random() * 4) + 1;
    return {
      x: (_.random(0, 5) * 2) % 12,
      y: Math.floor(i / 6) * y,
      w: 2,
      h: y,
      i: i.toString(),
      static: Math.random() < 0.05,
    };
  });
};
const layout = [
  { i: "a", x: 0, y: 0, w: 1, h: 2, static: true },
  { i: "b", x: 1, y: 0, w: 3, h: 2, minW: 2, maxW: 4 },
  { i: "c", x: 4, y: 0, w: 1, h: 2 },
  { i: "d", x: 0, y: 1, w: 10, h: 16 },
  // { i: "e", x: 0, y: 1, w: 10, h: 16 },
];
// d: [0, 1, 10, 16]

const Grid = (props) => {
  const [mounted, setMounted] = useState(false);
  const [state, setState] = useState({
    currentBreakpoint: "lg",
    compactType: "vertical",
    mounted: mounted,
    layouts: { lg: props.initialLayout },
  });
  let onBreakpointChange = (breakpoint) => {
    setState({
      ...state,
      currentBreakpoint: breakpoint,
    });
  };

  let onCompactTypeChange = () => {
    const { compactType: oldCompactType } = this.state;
    const compactType =
      oldCompactType === "horizontal"
        ? "vertical"
        : oldCompactType === "vertical"
        ? null
        : "horizontal";
    setState(...state, { compactType });
  };

  let onLayoutChange = (layout, layouts) => {
    props.onLayoutChange(layout, layouts);
  };

  let onNewLayout = () => {
    setState(...state, {
      layouts: { lg: generateLayout() },
    });
  };
  useEffect(() => {
    setState({
      currentBreakpoint: "lg",
      compactType: "vertical",
      mounted: true,
      layouts: { lg: props.initialLayout },
    });
  }, []);

  // layout is an array of objects, see the demo for more complete usage

  // generateDOM() {
  //   return _.map(this.state.layouts.lg, function(l, i) {
  //     return (
  //       <div key={i} className={l.static ? "static" : ""}>
  //         {l.static ? (
  //           <span
  //             className="text"
  //             title="This item is static and cannot be removed or resized."
  //           >
  //             Static - {i}
  //           </span>
  //         ) : (
  //           <span className="text">{i}</span>
  //         )}
  //       </div>
  //     );
  //   });
  // }

  // const onCompactTypeChange = () => {
  //   const { compactType: oldCompactType } = state;
  //   const compactType =
  //     oldCompactType === "horizontal"
  //       ? "vertical"
  //       : oldCompactType === "vertical"
  //       ? null
  //       : "horizontal";
  //   setState({ compactType });
  // };

  // const onNewLayout = () => {
  //   setState({
  //     layouts: { lg: generateLayout() },
  //   });
  // };
  return (
    <ResponsiveReactGridLayout
      {...props}
      // className="layout"
      layout={state.layouts}
      onBreakpointChange={onBreakpointChange}
      onLayoutChange={onLayoutChange}
      // isDraggable
      // isRearrangeable
      // isResizable
      // draggableHandle=".grid-item__title"
      // breakpoints={{ lg: 1280, md: 992, sm: 767, xs: 480, xxs: 0 }}
      // cols={{ lg: 12, md: 10, sm: 6, xs: 4, xxs: 2 }}
      // rowHeight={30}
      // width={1200}
      useCSSTransforms={state.mounted}
      compactType={state.compactType}
      preventCollision={!state.compactType}
    >
      <div className="layoutItem" key="a">
        a
      </div>
      <div className="layoutItem" key="b">
        b
      </div>
      <div className="layoutItem" key="c">
        c
      </div>
      <div className="layoutItem" key="d">
        {/* <Linechart></Linechart> */}
        <ExampleChart></ExampleChart>
      </div>
      <div className="layoutItem" key="e">
        {/* <Linechart></Linechart> */}
        <LineChartPlotty></LineChartPlotty>
      </div>
    </ResponsiveReactGridLayout>
  );
};

Grid.defaultProps = {
  className: "layout",
  rowHeight: 30,
  onLayoutChange: function () {},
  cols: { lg: 12, md: 10, sm: 6, xs: 4, xxs: 2 },
  initialLayout: layout,
  // initialLayout: generateLayout(),
};
export default Grid;
