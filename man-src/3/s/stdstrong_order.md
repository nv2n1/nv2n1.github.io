---
title: "stdstrong_order(3)"
name: "stdstrong_order"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrong_order/"
---

std::strong_order - std::strong_order

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;compare&gt;

    template &lt;class T&gt;
    (since C++ 20)

        constexpr std::strong_ordering strong_order(const T &amp;a, const T &amp;b);</code></pre> 
Compares two values using 3-way comparison and produces a result of type std::strong_ordering 
Specifically, 
* First, if std::numeric_limits&lt;T&gt;::is_iec559 is true, performs the ISO/IEC/IEEE 60559 totalOrder comparison of floating-point values and returns that result as a value of type std::strong_ordering (note: this comparison can distinguish between the positive and negative zero and between the NaNs with different representations) 
* Otherwise, if the expression a &lt;=&gt; b is well-formed and its result is convertible to std::strong_ordering, returns that result. 
* Otherwise, if the expression a &lt;=&gt; b is well-formed, but its result is not convertible to std::strong_ordering, then the function is defined as deleted. 
* Otherwise, if the expression a &lt;=&gt; b is ill-formed, but the expressions a == b and a &lt; b are both well-formed and convertible to bool, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if a == b is true, returns std::strong_ordering::equal 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* otherwise, if a &lt; b is true, returns std::strong_ordering::less 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* otherwise, returns std::strong_ordering::greater 
* Otherwise, the function is defined as deleted. 

<h2>Parameters</h2>

a, b - values to compare

<h2>Return value</h2>

A value of type std::strong_ordering, as described above. 

<h2>Notes</h2>



<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

strong_ordering the result type of 3-way comparison that supports all 6 operators and is substitutable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
weak_order performs 3-way comparison and produces a result of type std::weak_ordering 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
