---
title: "stdthreadhardware_concurrency(3)"
name: "stdthreadhardware_concurrency"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthreadhardware_concurrency/"
---

std::thread::hardware_concurrency - std::thread::hardware_concurrency

<h2>Synopsis</h2>

<pre><code>static unsigned int hardware_concurrency() noexcept;
(since C++ 11)</code></pre> 
Returns the number of concurrent threads supported by the implementation. The value should be considered only a hint. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Number of concurrent threads supported. If the value is not well defined or not computable, returns 0. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;thread&gt;
int main()
{
    unsigned int n = std::thread::hardware_concurrency();
    std::cout &lt;&lt; n &lt;&lt; &quot; concurrent threads are supported.\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;4 concurrent threads are supported.

<h2>See also</h2>

hardware_destructive_interference_size min offset to avoid false sharing 
hardware_constructive_interference_size max offset to promote true sharing 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(constant) 
<i>(C++17)</i> 
