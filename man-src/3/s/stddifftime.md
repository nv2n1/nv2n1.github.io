---
title: "stddifftime(3)"
name: "stddifftime"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddifftime/"
---

std::difftime - std::difftime

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ctime&gt;

double difftime( std::time_t time_end, std::time_t time_beg );</code></pre> 
Computes difference between two calendar times as std::time_t objects (time_end - time_beg) in seconds. If time_end refers to time point before time_beg then the result is negative. 

<h2>Parameters</h2>

time_beg, time_end - times to compare

<h2>Return value</h2>

Difference between two times in seconds. 

<h2>Notes</h2>

On POSIX systems, std::time_t is measured in seconds, and difftime is equivalent to arithmetic subtraction, but C and C++ allow fractional units for time_t. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;ctime&gt;
int main()

{
    std::time_t start = std::time(nullptr);
    volatile double d;
    // some time-consuming operation
    for (int n = 0; n &lt; 10000; ++n) {
        for (int m = 0; m &lt; 100000; ++m) {
            d += d * n * m;
        }
    }
    std::cout &lt;&lt; &quot;Wall time passed: &quot;
              &lt;&lt; std::difftime(std::time(nullptr), start) &lt;&lt; &quot; s.\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Wall time passed: 7 s.

<h2>See also</h2>

duration a time interval 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
