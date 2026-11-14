---
title: "stdexperimentalnullopt_t(3)"
name: "stdexperimentalnullopt_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalnullopt_t/"
---

std::experimental::nullopt_t - std::experimental::nullopt_t

<h2>Synopsis</h2>

Defined in header &lt;experimental/optional&gt; 
struct nullopt_t; (library fundamentals TS) 
std::experimental::nullopt_t is an empty class type used to indicate optional type with uninitialized state. In particular, std::experimental::optional has a constructor with nullopt_t as a single argument, which creates an optional that does not contain a value. 
std::experimental::nullopt_t must be a LiteralType and cannot have a default constructor. 
It must have a constexpr constructor that takes some implementation-defined literal type. 

<h2>Notes</h2>

<pre><code>nullopt_t is not DefaultConstructible to support both op = {};
and op = nullopt; as the syntax for disengaging an optional object.

A possible implementation of this class is
struct nullopt_t {
    constexpr nullopt_t(int)
    {
    }
};
</code></pre>

<h2>See also</h2>

nullopt an object of type nullopt_t 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(constant) 
<i>(C++17)</i> 
