---
title: "stdmask_arrayoperator(3)"
name: "stdmask_arrayoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmask_arrayoperator/"
---

std::mask_array&lt;T&gt;::operator= - std::mask_array&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>void operator=(const T &amp;value) const;
(1)

    void
    operator=(const std::valarray&lt;T&gt; &amp;val_arr) const;
(2)

    const mask_array &amp;
    operator=(const mask_array &amp;sl_arr) const;
(3)(since C++ 11)</code></pre> 
Assigns values to all referred elements. 
1) Assigns value to all of the elements. 
2) Assigns the elements of val_arr to the referred to elements of *this. 
3) Assigns the selected elements from sl_arr to the referred to elements of *this. 

<h2>Parameters</h2>

value - a value to assign to all of the referred elements 
val_arr - std::valarray to assign 
sl_arr - std::mask_array to assign

<h2>Return value</h2>

1-2) <i>(none)</i> 
3) *this 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
