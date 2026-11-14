---
title: "stdrandom_deviceentropy(3)"
name: "stdrandom_deviceentropy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrandom_deviceentropy/"
---

std::random_device::entropy - std::random_device::entropy

<h2>Synopsis</h2>

<pre><code>double entropy() const noexcept;
(since C++ 11)</code></pre> 
Obtains an estimate of the random number device entropy, which is a floating-point value between 0 and log 
2(max()+1) (which is equal to std::numeric_limits&lt;unsigned int&gt;::digits). If the device has n states whose individual probabilities are P 
0,...,P 
n-1, the device entropy S is defined as 
S = -Σn-1 
i=0P 
ilog(P 
i) 
A deterministic random number generator (e.g. a pseudo-random engine) has entropy zero. 

<h2>Return value</h2>

The value of the device entropy, or zero if not applicable. 

<h2>Notes</h2>

This function is not fully implemented in some standard libraries. For example, LLVM_libc++ always returns zero even though the device is non-deterministic. In comparison, Microsoft Visual C++ implementation always returns 32, and boost.random returns 10. 
The entropy of the Linux kernel device /dev/urandom may be obtained using ioctl_RNDGETENTCNT - that's what std::random_device::entropy() in GNU_libstdc++ uses as of version 8.1 

<h2>Example</h2>

Example output on one of the implementations 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;random&gt;
int main()

{
    std::random_device rd;
    std::cout &lt;&lt; rd.entropy() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;32
