---
title: "stdstrstreambufpcount(3)"
name: "stdstrstreambufpcount"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreambufpcount/"
---

std::strstreambuf::pcount - std::strstreambuf::pcount

<h2>Synopsis</h2>

<pre><code>int pcount() const;
</code></pre> 
Returns the number of characters written to the output sequence. 
If the next pointer for the put area (std::streambuf::pptr()) is a null pointer, returns zero. 
Otherwise, returns the next pointer in the put area minus the beginning pointer in the put area, that is pptr() - pbase() 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The number of characters written to the put area. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
int main()

{
    std::strstream dyn; // dynamically-allocated output buffer
    dyn &lt;&lt; &quot;Test: &quot; &lt;&lt; 1.23 &lt;&lt; std::ends;
    std::strstreambuf *buf = dyn.rdbuf();
    std::cout &lt;&lt; &quot;The size of the output is &quot;
              &lt;&lt; buf-&gt;pcount() // or just buf.pcount()
              &lt;&lt; &quot; and it holds \&quot;&quot; &lt;&lt; dyn.str() &lt;&lt; &quot;\&quot;\n&quot;;
    dyn.freeze(false); // after calling .str() on a dynamic strstream
    char arr[10];
    std::ostrstream user(arr, 10); // user-provided output buffer
    buf = user.rdbuf();
    user &lt;&lt; 1.23;                        // note: no std::ends
    std::cout.write(arr, buf-&gt;pcount()); // or just user.pcount()
    std::cout &lt;&lt; '\n';
    std::istrstream lit(&quot;1 2 3&quot;); // read-only fixed-size buffer
    buf = lit.rdbuf();
    // istrstream has no member pcount(), so lit.pcount() won't work
    std::cout &lt;&lt; &quot;Input-only pcount() = &quot; &lt;&lt; buf-&gt;pcount() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The size of the output is 11 and it holds &quot;Test: 1.23&quot; 
&nbsp;<wbr>&nbsp;1.23 
&nbsp;<wbr>&nbsp;Input-only pcount() = 0

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the number of characters written 
pcount <i>(public member function of std::strstream)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the number of characters written 
pcount <i>(public member function of std::ostrstream)</i> 
