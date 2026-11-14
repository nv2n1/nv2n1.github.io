---
title: "stdchronotime_point_cast(3)"
name: "stdchronotime_point_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotime_point_cast/"
---

std::chrono::time_point_cast - std::chrono::time_point_cast

<h2>Synopsis</h2>

<pre><code>template &lt;class ToDuration, class Clock, class Duration&gt;
(since C++ 11)

    time_point&lt;Clock, ToDuration&gt; time_point_cast((until C++ 14)

                                                      const time_point&lt;Clock, Duration&gt; &amp;t);

template &lt;class ToDuration, class Clock, class Duration&gt;

constexpr time_point&lt;Clock, ToDuration&gt; time_point_cast((since C++ 14)

                                                            const time_point&lt;Clock, Duration&gt; &amp;t);</code></pre> 
Converts a std::chrono::time_point from one duration to another. 

<h2>Parameters</h2>

t - time_point to convert from

<h2>Return value</h2>

std::chrono::time_point&lt;Clock, ToDuration&gt;(std::chrono::duration_cast&lt;ToDuration&gt;(t.time_since_epoch())) 

<h2>Notes</h2>

time_point_cast will only participate in overload resolution if ToDuration is an instantiation of duration. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;
using Clock = std::chrono::high_resolution_clock;

using Ms = std::chrono::milliseconds;

using Sec = std::chrono::seconds;
template &lt;class Duration&gt;

using TimePoint = std::chrono::time_point&lt;Clock, Duration&gt;;
inline void print_ms(const TimePoint&lt;Ms&gt; &amp;time_point)

{
    std::cout &lt;&lt; time_point.time_since_epoch().count() &lt;&lt; &quot; ms\n&quot;;
}
int main()

{
    TimePoint&lt;Sec&gt; time_point_sec(Sec(4));
    // implicit cast, no precision loss
    TimePoint&lt;Ms&gt; time_point_ms(time_point_sec);
    print_ms(time_point_ms); // 4000 ms
    time_point_ms = TimePoint&lt;Ms&gt;(Ms(5756));
    // explicit cast, need when precision loss may happens
    // 5756 truncated to 5000
    time_point_sec = std::chrono::time_point_cast&lt;Sec&gt;(time_point_ms);
    print_ms(time_point_sec); // 5000 ms
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;4000 ms 
&nbsp;<wbr>&nbsp;5000 ms
