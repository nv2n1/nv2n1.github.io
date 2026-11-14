---
title: "sc_renderedobjectset(3)"
name: "sc_renderedobjectset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_renderedobjectset/"
description: "sc::RenderedObjectSet –"
---

<p>sc::RenderedObjectSet &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RenderedObject</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RenderedObjectSet (int capacity=10)



RenderedObjectSet (const Ref&lt; KeyVal &gt; &amp;)



int n () const



const Ref&lt; RenderedObject &gt; &amp; element (int i) const



virtual void add (const Ref&lt; RenderedObject &gt; &amp;)



Protected Member Functions
void render (const Ref&lt; Render &gt; &amp;)
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
