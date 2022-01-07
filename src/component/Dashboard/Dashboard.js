import React, { useState } from "react";
import ReactDOM from "react-dom";
import { Layout, Menu } from "antd";
import SideNav from "./SideNav";
import Grid from "./Grid";
import "./index.css";

const { Header, Content, Footer } = Layout;
const gridProps = window.gridProps || {};
let Dashboard = (props) => {
  const [state, setState] = useState({ layout: [] });

  const onLayoutChange = (layout) => {
    setState({ layout: layout });
  };
  const stringifyLayout = () => {
    return state.layout.map((l) => {
      return (
        <div className="layoutItem" key={l.i}>
          <b>{l.i}</b>: [{l.x}, {l.y}, {l.w}, {l.h}]
        </div>
      );
    });
  };

  return (
    <>
      <Layout>
        <SideNav></SideNav>
        <Layout>
          <Header
            className="site-layout-sub-header-background"
            style={{ padding: 0 }}
          />
          <Content style={{ margin: "24px 16px 0" }}>
            <div
              className="site-layout-background"
              style={{ padding: 24, minHeight: 360 }}
            >
              <div className="layoutJSON">
                Displayed as <code>[x, y, w, h]</code>:
                <div className="columns">{stringifyLayout()}</div>
              </div>
              <Grid onLayoutChange={onLayoutChange}></Grid>
            </div>
          </Content>
          <Footer style={{ textAlign: "center" }}>
            Emil Steinkopf ©2021 Created with Ant UED
          </Footer>
        </Layout>
      </Layout>
    </>
  );
};
export default Dashboard;
