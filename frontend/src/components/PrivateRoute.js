// import React from "react";
import { Route, Redirect } from "react-router-dom";

class PrivateRoute extends Route {
    render() {
        return this.props.currentUser ? (
            <Route {...this.props} /> 
        ) : (
            <Redirect to="/" />
        );
    }
}

export default PrivateRoute;