---
title: "sc_animatedobject(3)"
name: "sc_animatedobject"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_animatedobject/"
description: "sc::AnimatedObject –"
---

<p>sc::AnimatedObject &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::MolFreqAnimate</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>AnimatedObject (const Ref&lt; KeyVal &gt; &amp;)



const char * name () const



void set_name (const char *name)



virtual int nobject ()=0



virtual Ref&lt; RenderedObject &gt; object (int iobject)=0



Protected Attributes
char * name_
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
