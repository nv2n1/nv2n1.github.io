---
title: "stdchronosteady_clocknow(3)"
name: "stdchronosteady_clocknow"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronosteady_clocknow/"
---

std::chrono::steady_clock::now - std::chrono::steady_clock::now

<h2>Synopsis</h2>

<pre><code>static std::chrono::time_point&lt;std::chrono::steady_clock&gt; now() noexcept;  (since C++11)</code></pre> 
Returns a time point representing the current point in time. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A time point representing the current time. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;numeric&gt;

#include &lt;chrono&gt;
volatile int sink;

int main()

{
    for (auto size = 1ull; size &lt; 1000000000ull; size *= 100) {
        // record start time
        auto start = std::chrono::steady_clock::now();
        // do some work
        std::vector&lt;int&gt; v(size, 42);
        sink = std::accumulate(v.begin(), v.end(), 0u); // make sure it's a side effect
        // record end time
        auto end = std::chrono::steady_clock::now();
        std::chrono::duration&lt;double&gt; diff = end - start;
        std::cout &lt;&lt; &quot;Time to fill and iterate a vector of &quot;
                  &lt;&lt; size &lt;&lt; &quot; ints : &quot; &lt;&lt; diff.count() &lt;&lt; &quot; s\n&quot;;
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Time to fill and iterate a vector of 1 ints : 2.43e-07 s 
&nbsp;<wbr>&nbsp;Time to fill and iterate a vector of 100 ints : 4.1e-07 s 
&nbsp;<wbr>&nbsp;Time to fill and iterate a vector of 10000 ints : 2.519e-05 s 
&nbsp;<wbr>&nbsp;Time to fill and iterate a vector of 1000000 ints : 0.00207669 s 
&nbsp;<wbr>&nbsp;Time to fill and iterate a vector of 100000000 ints : 0.423087 s
