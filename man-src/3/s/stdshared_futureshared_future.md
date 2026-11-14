---
title: "stdshared_futureshared_future(3)"
name: "stdshared_futureshared_future"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_futureshared_future/"
---

std::shared_future&lt;T&gt;::~shared_future - std::shared_future&lt;T&gt;::~shared_future

<h2>Synopsis</h2>

~shared_future(); <i>(since C++11)</i> 
If *this is the last object referring to the shared state, destroys the shared state. Otherwise does nothing. 
