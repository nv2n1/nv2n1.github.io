---
title: "stdfuturefuture(3)"
name: "stdfuturefuture"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfuturefuture/"
---

std::future&lt;T&gt;::~future - std::future&lt;T&gt;::~future

<h2>Synopsis</h2>

~future(); <i>(since C++11)</i> 
Releases any shared state. This means <pre><code>*if the return object or provider holds the last reference to its shared state, the shared state is destroyed;
and

    *the return object or
    provider gives up its reference to its shared state;
and
</code></pre> 
* these actions will not block for the shared state to become ready, except that it may block if all of the following are true: the shared state was created by a call to std::async, the shared state is not yet ready, and this was the last reference to the shared state. <i>(since C++14)</i> 
