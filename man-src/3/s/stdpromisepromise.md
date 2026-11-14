---
title: "stdpromisepromise(3)"
name: "stdpromisepromise"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpromisepromise/"
---

std::promise&lt;R&gt;::~promise - std::promise&lt;R&gt;::~promise

<h2>Synopsis</h2>

~promise(); <i>(since C++11)</i> 
Abandons the shared state: 
* if the shared state is ready, releases it. 
* if the shared state is not ready, stores an exception object of type std::future_error with an error condition std::future_errc::broken_promise, makes the shared state ready and releases it. 
