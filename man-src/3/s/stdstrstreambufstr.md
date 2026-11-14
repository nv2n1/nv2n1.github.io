---
title: "stdstrstreambufstr(3)"
name: "stdstrstreambufstr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreambufstr/"
---

std::strstreambuf::str - std::strstreambuf::str

<h2>Synopsis</h2>

<pre><code>char *str() const;</code></pre> 
Calls freeze(), then returns a copy of start pointer of the get area, std::streambuf::eback(). 
The start of the get area, for all writeable std::strstreambuf objects constructed through the interface provided by std::strstream, is also the start of the put area. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A copy of eback(), which may be a null pointer. 

<h2>Notes</h2>

This function is typically called through the std::strstream interface. 
The call to freeze() guarantees that the returned pointer remains valid until the next explicit call to freeze(false): otherwise (on a dynamic buffer) any output operation could trigger buffer reallocation which would invalidate the pointer. It also causes a memory leak in the destructor of std::strstreambuf, unless freeze(false) is called before the buffer (or, more commonly, the std::strstream that manages it) is destroyed. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
int main()

{
    std::strstream dyn; // dynamically-allocated read/write buffer
    dyn &lt;&lt; &quot;Test: &quot; &lt;&lt; 1.23 &lt;&lt; std::ends;
    std::strstreambuf *buf = dyn.rdbuf();
    std::cout &lt;&lt; &quot;R/W buffer holds \&quot;&quot; &lt;&lt; buf-&gt;str() // or dyn.str()
              &lt;&lt; &quot;\&quot;\n&quot;;
    dyn.freeze(false); // after calling .str() on a dynamic strstream
    char arr[10];
    std::ostrstream user(arr, 10); // fixed-size write-only buffer
    buf = user.rdbuf();
    user &lt;&lt; 1.23 &lt;&lt; std::ends;
    std::cout &lt;&lt; &quot;Write-only buffer holds \&quot;&quot; &lt;&lt; buf-&gt;str() // or user.str()
              &lt;&lt; &quot;\&quot;\n&quot;;
    std::istrstream lit(&quot;1 2 3&quot;); // fixed-size read-only buffer
    buf = lit.rdbuf();
    std::cout &lt;&lt; &quot;Read-only buffer holds \&quot;&quot; &lt;&lt; buf-&gt;str() // or lit.str()
              &lt;&lt; &quot;\&quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;R/W buffer holds &quot;Test: 1.23&quot; 
&nbsp;<wbr>&nbsp;Write-only buffer holds &quot;1.23&quot; 
&nbsp;<wbr>&nbsp;Read-only buffer holds &quot;1 2 31 2 3&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the output buffer 
str <i>(public member function of std::strstream)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the output buffer 
str <i>(public member function of std::ostrstream)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the output buffer 
str <i>(public member function of std::istrstream)</i> 
