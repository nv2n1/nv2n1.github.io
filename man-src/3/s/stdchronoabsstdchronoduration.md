---
title: "stdchronoabsstdchronoduration(3)"
name: "stdchronoabsstdchronoduration"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoabsstdchronoduration/"
---

std::chrono::abs(std::chrono::duration) - std::chrono::abs(std::chrono::duration)

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
template &lt;class Rep, class Period&gt; <i>(since C++17)</i> 
constexpr duration&lt;Rep, Period&gt; abs(duration&lt;Rep, Period&gt; d) 
Returns the absolute value of the duration d. Specifically, if d &gt;= d.zero(), return d, otherwise return -d. 
The function does not participate in the overload resolution unless std::numeric_limits&lt;Rep&gt;::is_signed is true. 

<h2>Parameters</h2>

d - duration

<h2>Return value</h2>

Absolute value of d 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template &lt;class Rep, class Period, class = std::enable_if_t&lt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::chrono::duration&lt;Rep, Period&gt;::min() &lt; std::chrono::duration&lt;Rep, Period&gt;::zero()&gt;&gt; 
&nbsp;<wbr>&nbsp;constexpr std::chrono::duration&lt;Rep, Period&gt; abs(duration&lt;Rep, Period&gt; d) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d &gt;= d.zero() ? d : -d; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implements unary + and unary - 
operator+ <i>(public member function)</i> 
operator- 
abs(int) 
labs 
llabs computes absolute value of an integral value (|x|) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
