---
title: "stdchronotime_point(3)"
name: "stdchronotime_point"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotime_point/"
---

std::chrono::time_point&lt;Clock,Duration&gt;::time_since_epoch - std::chrono::time_point&lt;Clock,Duration&gt;::time_since_epoch

<h2>Synopsis</h2>

duration time_since_epoch() const; <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++14)</i> 
constexpr duration time_since_epoch() const; <i>(since C++14)</i> 
Returns a duration representing the amount of time between *this and the clock's epoch. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The amount of time between this time_point and the clock's epoch 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;ctime&gt;
int main()

{
    const auto p0 = std::chrono::time_point&lt;std::chrono::system_clock&gt;{};
    const auto p1 = std::chrono::system_clock::now();
    const auto p2 = p1 - std::chrono::hours(24);
    std::time_t epoch_time = std::chrono::system_clock::to_time_t(p0);
    std::cout &lt;&lt; &quot;epoch: &quot; &lt;&lt; std::ctime(&amp;epoch_time);
    std::time_t today_time = std::chrono::system_clock::to_time_t(p1);
    std::cout &lt;&lt; &quot;today: &quot; &lt;&lt; std::ctime(&amp;today_time);
    std::cout &lt;&lt; &quot;hours since epoch: &quot;
              &lt;&lt; std::chrono::duration_cast&lt;std::chrono::hours&gt;(
                     p1.time_since_epoch())
                     .count()
              &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;yesterday, hours since epoch: &quot;
              &lt;&lt; std::chrono::duration_cast&lt;std::chrono::hours&gt;(
                     p2.time_since_epoch())
                     .count()
              &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;epoch: Thu Jan 1 00:00:00 1970 
&nbsp;<wbr>&nbsp;today: Fri Jun 30 10:44:11 2017 
&nbsp;<wbr>&nbsp;hours since epoch: 416338 
&nbsp;<wbr>&nbsp;yesterday, hours since epoch: 416314
