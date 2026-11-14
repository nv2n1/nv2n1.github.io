---
title: "sc_renderedobject(3)"
name: "sc_renderedobject"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_renderedobject/"
description: "sc::RenderedObject –"
---

<p>sc::RenderedObject &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::RenderedMolecule</code>, <code>sc::RenderedObjectSet</code>, <code>sc::RenderedPolygons</code>, <code>sc::RenderedPolylines</code>, and <code>sc::RenderedSphere</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RenderedObject (const Ref&lt; Material &gt; &amp;=0)



RenderedObject (const Ref&lt; KeyVal &gt; &amp;)



const char * name () const



void set_name (const char *)



Ref&lt; Material &gt; material () const



Ref&lt; Appearance &gt; appearance () const



Ref&lt; Transform &gt; transform () const



void material (const Ref&lt; Material &gt; &amp;m)



void appearance (const Ref&lt; Appearance &gt; &amp;a)



void transform (const Ref&lt; Transform &gt; &amp;t)



virtual void print (std::ostream &amp;=ExEnv::out0()) const


Print the object.


virtual void render (const Ref&lt; Render &gt; &amp;)=0



Protected Attributes
char * name_



Ref&lt; Material &gt; material_



Ref&lt; Appearance &gt; appearance_



Ref&lt; Transform &gt; transform_



Friends</code></pre>
<p> class <code>Render</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
