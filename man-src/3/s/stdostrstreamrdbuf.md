---
title: "stdostrstreamrdbuf(3)"
name: "stdostrstreamrdbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdostrstreamrdbuf/"
---

std::ostrstream::rdbuf - std::ostrstream::rdbuf

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
    const std::ostrstream buf;
    std::strstreambuf *ptr = buf.rdbuf();
}
</code></pre>
