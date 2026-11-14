---
title: "stdistrstreamistrstream(3)"
name: "stdistrstreamistrstream"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdistrstreamistrstream/"
---

std::istrstream::~istrstream - std::istrstream::~istrstream

<h2>Synopsis</h2>

<pre><code>virtual ~istrstream();</code></pre> 
Destroys a std::istrstream object, which also destroys the member std::strstreambuf. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Notes</h2>

The constructors of std::istrstream do not create the underlying std::strstreambuf in dynamically allocated mode, so the memory leaks that are possible with std::ostrstream::~ostrstream or std::strstream::~strstream do not apply. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;strstream&gt;

#include &lt;iostream&gt;
int main()

{
    {
        std::istrstream s(&quot;1.234&quot;);
        double d;
        s &gt;&gt; d;
        std::cout &lt;&lt; d &lt;&lt; '\n';
    } // destructor called
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1.234
