---
title: "stdchronoclock_time_conversion(3)"
name: "stdchronoclock_time_conversion"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoclock_time_conversion/"
description: "std::chrono::clock_time_conversion – std::chrono::clock_time_conversion"
---

<p>std::chrono::clock_time_conversion &#8211; std::chrono::clock_time_conversion</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;chrono&gt;<br />
template&lt;class Dest, class Source&gt; struct clock_time_conversion { }; <i>(since C++20)</i><br />
std::chrono::clock_time_conversion is a trait that specifies how to convert a std::chrono::time_point of the Source clock to that of the Dest clock. It does so by providing an const-callable operator() that accepts an argument of type std::chrono::time_point&lt;Source, Duration&gt; and returns a std::chrono::time_point&lt;Dest, OtherDuration&gt; that represents an equivalent point in time. The duration of the returned time point is computed from the source duration in a manner that varies for each specialization. clock_time_conversion is normally only used indirectly, via std::chrono::clock_cast.<br />
A program may specialize clock_time_conversion if at least one of the template parameters is a user-defined clock type.<br />
The primary template is an empty struct. The standard defines the following specializations:<br />
template&lt;class Clock&gt; struct clock_time_conversion&lt;Clock, Clock&gt;; <code>(1)</code> <i>(since C++20)</i><br />
template&lt;&gt; struct clock_time_conversion&lt;std::chrono::system_clock, std::chrono::system_clock&gt;; <code>(2)</code> <i>(since C++20)</i><br />
template&lt;&gt; struct clock_time_conversion&lt;std::chrono::utc_clock, std::chrono::utc_clock&gt;; <code>(3)</code> <i>(since C++20)</i><br />
template&lt;&gt; struct clock_time_conversion&lt;std::chrono::system_clock, std::chrono::utc_clock&gt;; <code>(4)</code> <i>(since C++20)</i><br />
template&lt;&gt; struct clock_time_conversion&lt;std::chrono::utc_clock, std::chrono::system_clock&gt;; <code>(5)</code> <i>(since C++20)</i><br />
template&lt;class Clock&gt; struct clock_time_conversion&lt;Clock, std::chrono::system_clock&gt;; <code>(6)</code> <i>(since C++20)</i><br />
template&lt;class Clock&gt; struct clock_time_conversion&lt;std::chrono::system_clock, Clock&gt;; <code>(7)</code> <i>(since C++20)</i><br />
template&lt;class Clock&gt; struct clock_time_conversion&lt;Clock, std::chrono::utc_clock&gt;; <code>(8)</code> <i>(since C++20)</i><br />
template&lt;class Clock&gt; struct clock_time_conversion&lt;std::chrono::utc_clock, Clock&gt;; <code>(9)</code> <i>(since C++20)</i><br />
1-3) Identity conversion: operator() returns a copy of the argument.<br />
4-5) Conversions between std::chrono::sys_time and std::chrono::utc_time: operator() calls std::chrono::utc_clock::to_sys and std::chrono::utc_clock::from_sys, respectively.<br />
6-7) Conversions to and from std::chrono::sys_time when Clock supports from_sys and to_sys: operator() calls Clock::to_sys and Clock::from_sys, respectively.<br />
8-9) Conversions to and from std::chrono::utc_time when Clock supports from_utc and to_utc: operator() calls Clock::to_utc and Clock::from_utc, respectively. </p>
<h2>Member functions</h2>
<p>Each specialization has an implicitly-declared default constructor, copy constructor, move constructor, copy assignment operator, move assignment operator, and destructor. </p>
<p>&nbsp;std::chrono::clock_time_conversion::operator() </p>
<p>template &lt;class Duration&gt;<br />
std::chrono::time_point&lt;Clock, Duration&gt; <code>(1)</code> (member of specialization (1))<br />
operator()(const std::chrono::time_point&lt;Clock, Duration&gt;&amp; t) const;<br />
template &lt;class Duration&gt;<br />
std::chrono::sys_time&lt;Duration&gt; <code>(2)</code> (member of specialization (2))<br />
operator()(const std::chrono::sys_time&lt;Duration&gt; &amp; t) const;<br />
template &lt;class Duration&gt;<br />
std::chrono::utc_time&lt;Duration&gt; <code>(3)</code> (member of specialization (3))<br />
operator()(const std::chrono::utc_time&lt;Duration&gt;&amp; t) const;<br />
template &lt;class Duration&gt;<br />
std::chrono::sys_time&lt;Duration&gt; <code>(4)</code> (member of specialization (4))<br />
operator()(const std::chrono::utc_time&lt;Duration&gt;&amp; t) const;<br />
template &lt;class Duration&gt;<br />
std::chrono::utc_time&lt;Duration&gt; <code>(5)</code> (member of specialization (5))<br />
operator()(const std::chrono::sys_time&lt;Duration&gt;&amp; t) const;<br />
template &lt;class Duration&gt;<br />
auto operator()(const std::chrono::sys_time&lt;Duration&gt;&amp; t) const <code>(6)</code> (member of specialization (6))<br />
-&gt; decltype(Clock::from_sys(t));<br />
template &lt;class Duration&gt;<br />
auto operator()(const std::chrono::time_point&lt;SourceClock, Duration&gt;&amp; t) const <code>(7)</code> (member of specialization (7))<br />
-&gt; decltype(Clock::to_sys(t));<br />
template &lt;class Duration&gt;<br />
auto operator()(const std::chrono::utc_time&lt;Duration&gt;&amp; t) const <code>(8)</code> (member of specialization (8))<br />
-&gt; decltype(Clock::from_utc(t));<br />
template &lt;class Duration&gt;<br />
auto operator()(const std::chrono::time_point&lt;Clock, Duration&gt;&amp; t) const <code>(9)</code> (member of specialization (9))<br />
-&gt; decltype(Clock::to_utc(t)); </p>
<p>Converts the argument std::chrono::time_point to the destination clock.<br />
1-3) Identity conversion. Returns t unchanged.<br />
4) Returns std::chrono::utc_clock::to_sys(t).<br />
5) Returns std::chrono::utc_clock::from_sys(t).<br />
6) Returns Clock::from_sys(t). This overload only participates in overload resolution if the expression Clock::from_sys(t) is well-formed. The program is ill-formed if Clock::from_sys(t) does not return std::chrono::time_point&lt;Clock, Duration&gt; where Duration is some valid specialization of std::chrono::duration.<br />
7) Returns Clock::to_sys(t). This overload only participates in overload resolution if the expression Clock::to_sys(t) is well-formed. The program is ill-formed if Clock::to_sys(t) does not return std::chrono::sys_time&lt;Duration&gt; where Duration is some valid specialization of std::chrono::duration.<br />
8) Returns Clock::from_utc(t). This overload only participates in overload resolution if the expression Clock::from_utc(t) is well-formed. The program is ill-formed if Clock::from_utc(t) does not return std::chrono::time_point&lt;Clock, Duration&gt; where Duration is some valid specialization of std::chrono::duration.<br />
9) Returns Clock::to_utc(t). This overload only participates in overload resolution if the expression Clock::to_utc(t) is well-formed. The program is ill-formed if Clock::to_utc(t) does not return std::chrono::utc_time&lt;Duration&gt; where Duration is some valid specialization of std::chrono::duration.</p>
<h2>Parameters</h2>
<p>t &#8211; time point to convert</p>
<h2>Return value</h2>
<p>The result of the conversion as described above:<br />
1-3) t.<br />
4) std::chrono::utc_clock::to_sys(t).<br />
5) std::chrono::utc_clock::from_sys(t).<br />
6) Clock::from_sys(t).<br />
7) Clock::to_sys(t).<br />
8) Clock::from_utc(t).<br />
9) Clock::to_utc(t). </p>
<h2>See also</h2>
<p>clock_cast convert time points of one clock to another<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
