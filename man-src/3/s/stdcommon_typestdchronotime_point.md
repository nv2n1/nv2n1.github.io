---
title: "stdcommon_typestdchronotime_point(3)"
name: "stdcommon_typestdchronotime_point"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcommon_typestdchronotime_point/"
---

std::common_type(std::chrono::time_point) - std::common_type(std::chrono::time_point)

<h2>Synopsis</h2>

<pre><code>template &lt;class Clock, class Duration1, class Duration2&gt;

struct common_type&lt;std::chrono::time_point&lt;Clock, Duration1&gt;,

                   std::chrono::time_point&lt;Clock, Duration2&gt;&gt; {
    (since C++ 11)

        typedef std::chrono::time_point&lt;

            Clock, typename std::common_type&lt;Duration1, Duration2&gt;::type&gt; type;
};</code></pre> 
Exposes the type named type, which is the common type of two std::chrono::time_points. 

<h2>Notes</h2>

The common type of two std::chrono::time_point types is a std::chrono::time_point with the same clock as the two types and the std::common_type of their durations. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

common_type determines the common type of a group of types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
