---
title: "sc_vertex(3)"
name: "sc_vertex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_vertex/"
description: "sc::Vertex –"
---

<p>sc::Vertex &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>Vertex (const SCVector3 &amp;point, const SCVector3 &amp;normal)



Vertex (const SCVector3 &amp;point)



const SCVector3 &amp; point () const



int has_normal () const



const SCVector3 &amp; normal () const



void set_point (const SCVector3 &amp;p)



void set_normal (const SCVector3 &amp;p)



operator SCVector3 &amp; ()



void print (std::ostream &amp;o=ExEnv::out0())
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
