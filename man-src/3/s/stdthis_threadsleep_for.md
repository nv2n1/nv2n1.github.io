---
title: "stdthis_threadsleep_for(3)"
name: "stdthis_threadsleep_for"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthis_threadsleep_for/"
---

std::this_thread::sleep_for - std::this_thread::sleep_for

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;thread&gt;

    template &lt;class Rep, class Period&gt;
    (since C++ 11)

        void sleep_for(const std::chrono::duration&lt;Rep, Period&gt; &amp;sleep_duration);</code></pre> 
Blocks the execution of the current thread for at least the specified sleep_duration. 
This function may block for longer than sleep_duration due to scheduling or resource contention delays. 
The standard recommends that a steady clock is used to measure the duration. If an implementation uses a system clock instead, the wait time may also be sensitive to clock adjustments. 

<h2>Parameters</h2>

sleep_duration - time duration to sleep

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

Any exception thrown by clock, time_point, or duration during the execution (clocks, time points, and durations provided by the standard library never throw).

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;thread&gt;
int main()

{
    using namespace std::chrono_literals;
    std::cout &lt;&lt; &quot;Hello waiter\n&quot;
              &lt;&lt; std::flush;
    auto start = std::chrono::high_resolution_clock::now();
    std::this_thread::sleep_for(2s);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration&lt;double, std::milli&gt; elapsed = end - start;
    std::cout &lt;&lt; &quot;Waited &quot; &lt;&lt; elapsed.count() &lt;&lt; &quot; ms\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Hello waiter 
&nbsp;<wbr>&nbsp;Waited 2000.12 ms

<h2>See also</h2>

sleep_until stops the execution of the current thread until a specified time point 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
