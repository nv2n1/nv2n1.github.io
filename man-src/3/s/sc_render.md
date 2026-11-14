---
title: "sc_render(3)"
name: "sc_render"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_render/"
description: "sc::Render –"
---

<p>sc::Render &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::FileRender</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>Render (const Ref&lt; KeyVal &gt; &amp;)



Ref&lt; Material &gt; default_material ()



Ref&lt; Appearance &gt; default_appearance ()



Ref&lt; Transform &gt; default_transform ()



void default_material (const Ref&lt; Material &gt; &amp;m)



void default_appearance (const Ref&lt; Appearance &gt; &amp;a)



void default_transform (const Ref&lt; Transform &gt; &amp;t)



virtual void clear ()=0



virtual void render (const Ref&lt; RenderedObject &gt; &amp;)



virtual void animate (const Ref&lt; AnimatedObject &gt; &amp;)



virtual void set (const Ref&lt; RenderedObjectSet &gt; &amp;)



virtual void sphere (const Ref&lt; RenderedSphere &gt; &amp;)



virtual void polygons (const Ref&lt; RenderedPolygons &gt; &amp;)=0



virtual void polylines (const Ref&lt; RenderedPolylines &gt; &amp;)=0



Protected Member Functions</code></pre>
<p> virtual void <code>push_material</code> (const <code>Ref</code>&lt; <code>Material</code> &gt; &amp;m) </p>
<p> virtual void <code>push_appearance</code> (const <code>Ref</code>&lt; <code>Appearance</code> &gt; &amp;a) </p>
<p> virtual void <code>push_transform</code> (const <code>Ref</code>&lt; <code>Transform</code> &gt; &amp;t) </p>
<p> virtual <code>Ref</code>&lt; <code>Material</code> &gt; <code>pop_material</code> () </p>
<p> virtual <code>Ref</code>&lt; <code>Appearance</code> &gt; <code>pop_appearance</code> () </p>
<p> virtual <code>Ref</code>&lt; <code>Transform</code> &gt; <code>pop_transform</code> ()</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Material</code> &gt; <code>default_material_</code> </p>
<p> <code>Ref</code>&lt; <code>Appearance</code> &gt; <code>default_appearance_</code> </p>
<p> <code>Ref</code>&lt; <code>Transform</code> &gt; <code>default_transform_</code> </p>
<p> <code>Stack</code>&lt; <code>Ref</code>&lt; <code>Material</code> &gt; &gt; <code>material_stack_</code> </p>
<p> <code>Stack</code>&lt; <code>Ref</code>&lt; <code>Appearance</code> &gt; &gt; <code>appearance_stack_</code> </p>
<p> <code>Stack</code>&lt; <code>Ref</code>&lt; <code>Transform</code> &gt; &gt; <code>transform_stack_</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
