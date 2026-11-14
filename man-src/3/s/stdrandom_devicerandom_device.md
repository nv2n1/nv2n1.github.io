---
title: "stdrandom_devicerandom_device(3)"
name: "stdrandom_devicerandom_device"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrandom_devicerandom_device/"
---

std::random_device::random_device - std::random_device::random_device

<h2>Synopsis</h2>

<pre><code>random_device()
    : random_device(/*implementation-defined*/){}(1)(since C++ 11)

          explicit random_device(const std::string &amp;token);
(2)(since C++ 11)

    random_device(const random_device &amp;) = delete;
(3)(since C++ 11)</code></pre> 
1) Default constructs a new std::random_device object with an implementation-defined token. 
2) Constructs a new std::random_device object, making use of the argument token in an implementation-defined manner. 
3) The copy constructor is deleted: std::random_device is not copyable nor movable. 

<h2>Exceptions</h2>

Throws an implementation-defined exceptions derived from std::exception on failure.

<h2>Notes</h2>

The implementations in libc++ and libstdc++ expect token to be the name of a character device that produces random numbers when read from, with the default value &quot;/dev/urandom&quot;, although where the CPU instruction RDRND is available, libstdc++ uses that as the default. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
P0935R0 C++11 default constructor was explicit made implicit 

<h2>Example</h2>

Demonstrates the two commonly available types of std::random_device on Linux 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;random&gt;
int main()

{
    std::uniform_int_distribution&lt;int&gt; d(0, 10);
    std::random_device rd1; // uses RDRND or /dev/urandom
    for (int n = 0; n &lt; 10; ++n)
        std::cout &lt;&lt; d(rd1) &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    std::random_device rd2(&quot;/dev/random&quot;); // much slower on Linux
    for (int n = 0; n &lt; 10; ++n)
        std::cout &lt;&lt; d(rd2) &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;7 10 7 0 4 4 6 9 4 7 
&nbsp;<wbr>&nbsp;2 4 10 6 3 2 0 6 3 7
