---
title: "stdchronoduration_cast(3)"
name: "stdchronoduration_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoduration_cast/"
---

std::chrono::duration_cast - std::chrono::duration_cast

<h2>Synopsis</h2>

<pre><code>template &lt;class ToDuration, class Rep, class Period&gt;
(since C++ 11)

    constexpr ToDuration duration_cast(const duration&lt;Rep, Period&gt; &amp;d);</code></pre> 
Converts a std::chrono::duration to a duration of different type ToDuration. 
No implicit conversions are used. Multiplications and divisions are avoided where possible, if it is known at compile time that one or more parameters are 1. Computations are done in the widest type available and converted, as if by static_cast, to the result type only when finished. 

<h2>Parameters</h2>

d - duration to convert

<h2>Return value</h2>

d converted to a duration of type ToDuration. 

<h2>Notes</h2>

The function does not participate in overload resolution unless ToDuration is an instance of std::chrono::duration. 
Casting between integer durations where the source period is exactly divisible by the target period (e.g. hours to minutes) or between floating-point durations can be performed with ordinary casts or implicitly via std::chrono::duration_constructors, no duration_cast is needed. 
Casting from a floating-point duration to an integer duration is subject_to_undefined_behavior when the floating-point value is NaN, infinity, or too large to be representable by the target's integer type. Otherwise, casting to an integer duration is subject to truncation as with any static_cast to an integer type. 

<h2>Example</h2>

This example measures the execution time of a function 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;ratio&gt;

#include &lt;thread&gt;
void f()

{
    std::this_thread::sleep_for(std::chrono::seconds(1));
}
int main()

{
    auto t1 = std::chrono::high_resolution_clock::now();
    f();
    auto t2 = std::chrono::high_resolution_clock::now();
    // floating-point duration: no duration_cast needed
    std::chrono::duration&lt;double, std::milli&gt; fp_ms = t2 - t1;
    // integral duration: requires duration_cast
    auto int_ms = std::chrono::duration_cast&lt;std::chrono::milliseconds&gt;(t2 - t1);
    // converting integral duration to integral duration of shorter divisible time unit:
    // no duration_cast needed
    std::chrono::duration&lt;long, std::micro&gt; int_usec = int_ms;
    std::cout &lt;&lt; &quot;f() took &quot; &lt;&lt; fp_ms.count() &lt;&lt; &quot; ms, &quot;
              &lt;&lt; &quot;or &quot; &lt;&lt; int_ms.count() &lt;&lt; &quot; whole milliseconds &quot;
              &lt;&lt; &quot;(which is &quot; &lt;&lt; int_usec.count() &lt;&lt; &quot; whole microseconds)&quot; &lt;&lt; std::endl;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;f() took 1000.23 ms, or 1000 whole milliseconds (which is 1000000 whole microseconds)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a time point to another time point on the same clock, with a different duration 
time_point_cast <i>(function template)</i> 
floor(std::chrono::duration) converts a duration to another, rounding down 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
ceil(std::chrono::duration) converts a duration to another, rounding up 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
round(std::chrono::duration) converts a duration to another, rounding to nearest, ties to even 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
