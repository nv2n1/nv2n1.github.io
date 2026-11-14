---
title: "stdistrstreamrdbuf(3)"
name: "stdistrstreamrdbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdistrstreamrdbuf/"
---

std::istrstream::rdbuf - std::istrstream::rdbuf

<h2>Synopsis</h2>

<pre><code>strstreambuf *rdbuf() const;</code></pre> 
Returns a pointer to the associated std::strstreambuf, casting away its constness (despite the const qualifier on the member function) 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Pointer to the associated std::strsteambuf, with constness cast away. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;strstream&gt;

int main()

{
    const std::istrstream buf(&quot;example&quot;);
    std::strstreambuf *ptr = buf.rdbuf();
}
</code></pre>
