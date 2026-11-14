---
title: "stdchronoclock_cast(3)"
name: "stdchronoclock_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoclock_cast/"
---

std::chrono::clock_cast - std::chrono::clock_cast

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;chrono&gt;

    template &lt;class Dest, class Source, class Duration&gt;
    (since C++ 20)

        auto clock_cast(const std::chrono::time_point&lt;Source, Duration&gt; &amp;t);</code></pre> 
Converts the time point t of a clock Source to an equivalent time point of the clock Dest, using std::chrono::system_clock and/or std::chrono::utc_clock as intermediaries if necessary. 
* If the expression std::chrono::clock_time_conversion&lt;Dest, Source&gt;{}(t) is well-formed, returns the result of that expression. 
* Otherwise, if at least one of the following two expressions are well-formed, then 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If both expression are well-formed, the conversion is ambiguous, and the program is ill-formed. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, exactly one of the two expressions is well-formed; the result of that expression is returned. 
1) std::chrono::clock_time_conversion&lt;Dest, std::chrono::system_clock&gt;{}( 
std::chrono::clock_time_conversion&lt;std::chrono::system_clock, Source&gt;{}(t)) 
2) std::chrono::clock_time_conversion&lt;Dest, std::chrono::utc_clock&gt;{}( 
std::chrono::clock_time_conversion&lt;std::chrono::utc_clock, Source&gt;{}(t)) 
* Otherwise, if at least one of the following two expressions are well-formed, then 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If both expression are well-formed, the conversion is ambiguous, and the program is ill-formed. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, exactly one of the two expressions is well-formed; the result of that expression is returned. 
1) std::chrono::clock_time_conversion&lt;Dest, std::chrono::utc_clock&gt;{}( 
std::chrono::clock_time_conversion&lt;std::chrono::utc_clock, std::chrono::system_clock&gt;{}( 
std::chrono::clock_time_conversion&lt;std::chrono::system_clock, Source&gt;{}(t))) 
2) std::chrono::clock_time_conversion&lt;Dest, std::chrono::system_clock&gt;{}( 
std::chrono::clock_time_conversion&lt;std::chrono::system_clock, std::chrono::utc_clock&gt;{}( 
std::chrono::clock_time_conversion&lt;std::chrono::utc_clock, Source&gt;{}(t))) 
* Otherwise, this function does not participate in overload resolution. 

<h2>Return value</h2>

The result of the conversion, determined as described above. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

clock_time_conversion traits class defining how to convert time points of one clock to another 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(C++20) 
