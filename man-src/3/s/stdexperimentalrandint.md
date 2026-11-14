---
title: "stdexperimentalrandint(3)"
name: "stdexperimentalrandint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrandint/"
---

std::experimental::randint - std::experimental::randint

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/random&gt;

template &lt;class IntType&gt;                 (library fundamentals TS v2)

IntType randint(IntType a, IntType b);</code></pre> 
Generates a random integer in the closed interval [a, b]. 

<h2>Parameters</h2>

a, b - integer values specifying the range

<h2>Return value</h2>

A random integer i in the closed interval [a, b], produced using a thread-local instance of std::uniform_int_distribution&lt;IntType&gt; invoked with the per-thread_random_number_engine. 
Remarks 
If IntType is not one of short, int, long, long long, unsigned short, unsigned int, unsigned long, or unsigned long long, the program is ill-formed. 
The behavior is undefined if a &gt; b. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;experimental/random&gt;
int main()

{
    int random_number = std::experimental::randint(100, 999);
    std::cout &lt;&lt; &quot;random 3-digit number: &quot; &lt;&lt; random_number &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;random 3-digit number: 273

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reseeds the per-thread random engine 
reseed <i>(function)</i> 
