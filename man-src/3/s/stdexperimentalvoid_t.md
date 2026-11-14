---
title: "stdexperimentalvoid_t(3)"
name: "stdexperimentalvoid_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalvoid_t/"
---

std::experimental::void_t - std::experimental::void_t

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / type_traits&gt;

    template &lt;class...&gt;
    (library fundamentals TS v2)

        using void_t = void;</code></pre> 
A utility metafunction that maps a sequence of any types to the type void. 

<h2>Notes</h2>

This utility metafunction is used in template metaprogramming to detect ill-formed types in SFINAE context. First voted into C++17 as std::void_t, it was later added as well to the library fundamentals TS as std::experimental::void_t, because it is a dependency of the detection_idiom. 

<h2>See also</h2>

void_t void variadic alias template 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(alias template) 
<i>(C++17)</i> 
