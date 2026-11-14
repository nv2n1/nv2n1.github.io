---
title: "stdstrstreamstrstream(3)"
name: "stdstrstreamstrstream"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrstreamstrstream/"
---

std::strstream::~strstream - std::strstream::~strstream

<h2>Synopsis</h2>

<pre><code>virtual ~strstream();</code></pre> 
Destroys a std::strstream object, which also destroys the member std::strstreambuf, which may call the deallocation function if the underlying buffer was dynamically-allocated and not frozen. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Notes</h2>

If str() was called on a dynamic strstream and freeze(false) was not called after that, this destructor leaks memory. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
int main()

{
    {
        std::ostrstream s; // dynamic buffer
        s &lt;&lt; 1.23 &lt;&lt; std::ends;
        std::cout &lt;&lt; s.str() &lt;&lt; '\n';
        s.freeze(false);
    } // destructor called, buffer deallocated
    {
        std::ostrstream s;
        s &lt;&lt; 1.23 &lt;&lt; std::ends;
        std::cout &lt;&lt; s.str() &lt;&lt; '\n';

        //        buf.freeze(false);
    } // destructor called, memory leaked
    {
        std::istrstream s(&quot;1.23&quot;); // constant buffer
        double d;
        s &gt;&gt; d;
        std::cout &lt;&lt; d &lt;&lt; '\n';
    } // destructor called, nothing to deallocate
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1.23 
&nbsp;<wbr>&nbsp;1.23 
&nbsp;<wbr>&nbsp;1.23
