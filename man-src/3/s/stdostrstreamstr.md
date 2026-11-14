---
title: "stdostrstreamstr(3)"
name: "stdostrstreamstr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdostrstreamstr/"
---

std::ostrstream::str - std::ostrstream::str

<h2>Synopsis</h2>

<pre><code>char *str();</code></pre> 
Returns the pointer to the beginning of the buffer, after freezing it. Effectively calls rdbuf()-&gt;str() 

<h2>Notes</h2>

Before a call to str() that uses the result as a C string, the stream buffer must be null-terminated. Regular output such as with stream &lt;&lt; 1.2 does not store a null terminator, it must be appended explicitly, typically with the manipulator std::ends. 
After a call to str(), dynamic streams become frozen. A call to freeze(false) is required before exiting the scope in which this ostrstream object was created. otherwise the destructor will leak memory. Also, additional output to a frozen stream may be truncated once it reaches the end of the allocated buffer, which may leave the buffer not null-terminated. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Pointer to the beginning of the buffer in the associated std::strsteambuf or NULL if no buffer is available. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
int main()

{
    std::ostrstream dyn;     // dynamically-allocated output buffer
    dyn &lt;&lt; &quot;Test: &quot; &lt;&lt; 1.23; // not adding std::ends to demonstrate append behavior
    std::cout &lt;&lt; &quot;The output stream holds \&quot;&quot;;
    std::cout.write(dyn.str(), dyn.pcount()) &lt;&lt; &quot;\&quot;\n&quot;;
    // the stream is now frozen due to str()
    dyn &lt;&lt; &quot; More text&quot; &lt;&lt; std::ends;
    std::cout &lt;&lt; &quot;The output stream holds \&quot;&quot;;
    std::cout.write(dyn.str(), dyn.pcount()) &lt;&lt; &quot;\&quot;\n&quot;;
    dyn.freeze(false);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;The stream holds &quot;Test: 1.23&quot; 
&nbsp;<wbr>&nbsp;The stream holds &quot;Test: 1.23 More &quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;marks the buffer frozen and returns the beginning pointer of the input sequence 
str <i>(public member function of std::strstreambuf)</i> 
