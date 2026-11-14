---
title: "stdstrstreampcount(3)"
name: "stdstrstreampcount"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreampcount/"
---

std::strstream::pcount - std::strstream::pcount

<h2>Synopsis</h2>

<pre><code>int pcount() const;</code></pre> 
Returns the number of characters that were output in the put area of the associated std::strstreambuf. Effectively calls rdbuf()-&gt;pcount() 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The number of characters in the put area, or zero if nothing was output. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
int main()

{
    std::strstream dyn; // dynamically-allocated output buffer
    dyn &lt;&lt; &quot;Test: &quot; &lt;&lt; 1.23 &lt;&lt; std::ends;
    std::cout &lt;&lt; &quot;The size of the output is &quot; &lt;&lt; dyn.pcount()
              &lt;&lt; &quot; and it holds \&quot;&quot; &lt;&lt; dyn.str() &lt;&lt; &quot;\&quot;\n&quot;;
    dyn.freeze(false);
    char buf[10];
    std::strstream user(buf, 10); // user-provided output buffer
    user &lt;&lt; 1.23;                 // note: no std::ends
    std::cout.write(buf, user.pcount());
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The size of the output is 11 and it holds &quot;Test: 1.23&quot; 
&nbsp;<wbr>&nbsp;1.23

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the next pointer minus the beginning pointer in the output sequence: the number of characters written 
pcount <i>(public member function of std::strstreambuf)</i> 
