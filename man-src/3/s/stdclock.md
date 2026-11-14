---
title: "stdclock(3)"
name: "stdclock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdclock/"
---

std::clock - std::clock

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ctime&gt;

std::clock_t clock();</code></pre> 
Returns the approximate processor time used by the process since the beginning of an implementation-defined era related to the program's execution. To convert result value to seconds divide it by CLOCKS_PER_SEC. 
Only the difference between two values returned by different calls to std::clock is meaningful, as the beginning of the std::clock era does not have to coincide with the start of the program. std::clock time may advance faster or slower than the wall clock, depending on the execution resources given to the program by the operating system. For example, if the CPU is shared by other processes, std::clock time may advance slower than wall clock. On the other hand, if the current process is multithreaded and more than one execution core is available, std::clock time may advance faster than wall clock. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Processor time used by the program so far or (clock_t)(-1) if that information is unavailable or its value cannot be represented. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

On POSIX-compatible systems, clock_gettime with clock id CLOCK_PROCESS_CPUTIME_ID offers better resolution. 
The value returned by clock() may wrap around on some implementations. For example, on a machine with 32-bit std::clock_t, it wraps after 2147 seconds or 36 minutes. 

<h2>Example</h2>

This example demonstrates the difference between clock() time and real time 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;chrono&gt;

#include &lt;ctime&gt;

#include &lt;thread&gt;
// the function f() does some time-consuming work

void f()

{
    volatile double d = 0;
    for (int n = 0; n &lt; 10000; ++n)
        for (int m = 0; m &lt; 10000; ++m)
            d += d * n * m;
}
int main()

{
    std::clock_t c_start = std::clock();
    auto t_start = std::chrono::high_resolution_clock::now();
    std::thread t1(f);
    std::thread t2(f); // f() is called on two threads
    t1.join();
    t2.join();
    std::clock_t c_end = std::clock();
    auto t_end = std::chrono::high_resolution_clock::now();
    std::cout &lt;&lt; std::fixed &lt;&lt; std::setprecision(2) &lt;&lt; &quot;CPU time used: &quot;
              &lt;&lt; 1000.0 * (c_end - c_start) / CLOCKS_PER_SEC &lt;&lt; &quot; ms\n&quot;
              &lt;&lt; &quot;Wall clock time passed: &quot;
              &lt;&lt; std::chrono::duration&lt;double, std::milli&gt;(t_end - t_start).count()
              &lt;&lt; &quot; ms\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;CPU time used: 1590.00 ms 
&nbsp;<wbr>&nbsp;Wall clock time passed: 808.23 ms

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a time_t object to a textual representation 
ctime <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the current time of the system as time since epoch 
time <i>(function)</i> 
