---
title: "stdnullopt_t(3)"
name: "stdnullopt_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnullopt_t/"
---

std::nullopt_t - std::nullopt_t

<h2>Synopsis</h2>

Defined in header &lt;optional&gt; 
struct nullopt_t; <i>(since C++17)</i> 
std::nullopt_t is an empty class type used to indicate optional type with uninitialized state. In particular, std::optional has a constructor with nullopt_t as a single argument, which creates an optional that does not contain a value. 
std::nullopt_t must be a non-aggregate LiteralType and cannot have a default constructor or an initializer-list constructor. 
It must have a constexpr constructor that takes some implementation-defined literal type. 

<h2>Notes</h2>

The constraints on nullopt_t's constructors exist to support both op = {}; and op = nullopt; as the syntax for disengaging an optional object. 
A possible implementation of this class is <pre><code>struct nullopt_t {
    explicit constexpr nullopt_t(int)
    {
    }
};
</code></pre>

<h2>See also</h2>

nullopt an object of type nullopt_t 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(constant) 
<i>(C++17)</i> 
