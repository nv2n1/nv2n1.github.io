---
title: "stderror_categorymessage(3)"
name: "stderror_categorymessage"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_categorymessage/"
---

std::error_category::message - std::error_category::message

<h2>Synopsis</h2>

<pre><code>virtual std::string message(int condition) const = 0;
(since C++ 11)</code></pre> 
Returns a string describing the given error condition for the error category represented by *this. 

<h2>Parameters</h2>

condition - specifies the error condition to describe

<h2>Return value</h2>

A string describing the given error condition. 

<h2>Exceptions</h2>

<i>(none)</i>
