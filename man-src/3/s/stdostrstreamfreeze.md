---
title: "stdostrstreamfreeze(3)"
name: "stdostrstreamfreeze"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdostrstreamfreeze/"
---

std::ostrstream::freeze - std::ostrstream::freeze

<h2>Synopsis</h2>

<pre><code>void freeze(bool flag = true);</code></pre> 
If the stream is using a dynamically-allocated array for output, disables (flag == true) or enables (flag == false) automatic allocation/deallocation of the buffer. Effectively calls rdbuf()-&gt;freeze(flag) 

<h2>Notes</h2>

After a call to str(), dynamic streams become frozen automatically. A call to freeze(false) is required before exiting the scope in which this ostrstream object was created. otherwise the destructor will leak memory. Also, additional output to a frozen stream may be truncated once it reaches the end of the allocated buffer. 

<h2>Parameters</h2>

flag - desired status

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
int main()

{
    std::ostrstream dyn;     // dynamically-allocated output buffer
    dyn &lt;&lt; &quot;Test: &quot; &lt;&lt; 1.23; // note: no std::ends to demonstrate appending
    std::cout &lt;&lt; &quot;The output stream contains \&quot;&quot;;
    std::cout.write(dyn.str(), dyn.pcount()) &lt;&lt; &quot;\&quot;\n&quot;;
    // the stream is now frozen due to str()
    dyn &lt;&lt; &quot; More text&quot;; // output to a frozen stream may be truncated
    std::cout &lt;&lt; &quot;The output stream contains \&quot;&quot;;
    std::cout.write(dyn.str(), dyn.pcount()) &lt;&lt; &quot;\&quot;\n&quot;;
    dyn.freeze(false);        // freeze(false) must be called or the  destructor will leak
    std::ostrstream dyn2;     // dynamically-allocated output buffer
    dyn2 &lt;&lt; &quot;Test: &quot; &lt;&lt; 1.23; // note: no std::ends
    std::cout &lt;&lt; &quot;The output stream contains \&quot;&quot;;
    std::cout.write(dyn2.str(), dyn2.pcount()) &lt;&lt; &quot;\&quot;\n&quot;;
    dyn2.freeze(false);                // unfreeze the stream after str()
    dyn2 &lt;&lt; &quot; More text&quot; &lt;&lt; std::ends; // output will not be truncated (buffer grows)
    std::cout &lt;&lt; &quot;The output stream contains \&quot;&quot; &lt;&lt; dyn2.str() &lt;&lt; &quot;\&quot;\n&quot;;
    dyn2.freeze(false); // freeze(false) must be called or the  destructor will leak
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;The output stream contains &quot;Test: 1.23&quot; 
&nbsp;<wbr>&nbsp;The output stream contains &quot;Test: 1.23 More &quot; 
&nbsp;<wbr>&nbsp;The output stream contains &quot;Test: 1.23&quot; 
&nbsp;<wbr>&nbsp;The output stream contains &quot;Test: 1.23 More text&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets/clears the frozen state of the buffer 
freeze <i>(public member function of std::strstreambuf)</i> 
