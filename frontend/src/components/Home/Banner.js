import React, { useState, useEffect } from "react";
import agent from "../../agent";
import logo from "../../imgs/logo.png";

const Banner = (props) => {
  const [query, setQuery] = useState('');
  const [searching, setSearching] = useState(false);

  const changeHandler = (ev) => {
    setQuery(ev.target.value);
    if (ev.target.value.length === 0) {
      setSearching(false);
    }
    if (ev.target.value.length >= 3) {
      setSearching(true)
    }
  }

  useEffect( () => {
    if (searching) {
      props.onSearchQueryChange(
        query,
        (page) => agent.Items.search(query, page),
        agent.Items.search(query)
      );
    }
  }, [searching, query, props]);

  return (
    <div className="banner text-white">
      <div className="container p-4 text-center">
        <img src={logo} alt="banner" />
        <div>
          <form className="form-inline justify-content-center">
            <span>A place to </span>
            <span id="get-part" className="mx-1">get</span>
            <input
              id="search-box"
              type="text"
              className="form-control mx-1"
              placeholder="What is that you truly desire?"
              value={query}
              onChange={changeHandler}
            ></input>
            <span> the cool stuff.</span>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Banner;
