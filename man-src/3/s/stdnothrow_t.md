---
title: "stdnothrow_t(3)"
name: "stdnothrow_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnothrow_t/"
---

std::nothrow_t - std::nothrow_t

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;new&gt;

    struct nothrow_t {
};
(until C++ 17)

    struct nothrow_t {
    explicit nothrow_t() = default;
};
(since C++ 17)</code></pre> 
std::nothrow_t is an empty class type used to disambiguate the overloads of throwing and non-throwing allocation_functions. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;an object of type nothrow_t used to select an non-throwing allocation function 
nothrow (constant) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions 
operator_new <i>(function)</i> 
operator_new[] 
