---
title: "sc_ooglrender(3)"
name: "sc_ooglrender"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_ooglrender/"
description: "sc::OOGLRender –"
---

<p>sc::OOGLRender &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::FileRender</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>OOGLRender (const char *filename)



OOGLRender (std::ostream &amp;o=ExEnv::out0())



OOGLRender (const Ref&lt; KeyVal &gt; &amp;)



void render (const Ref&lt; RenderedObject &gt; &amp;)



void animate (const Ref&lt; AnimatedObject &gt; &amp;)



const char * file_extension ()



void set (const Ref&lt; RenderedObjectSet &gt; &amp;)



void sphere (const Ref&lt; RenderedSphere &gt; &amp;)



void polygons (const Ref&lt; RenderedPolygons &gt; &amp;)



void polylines (const Ref&lt; RenderedPolylines &gt; &amp;)
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
