---
title: "sc_parentclass(3)"
name: "sc_parentclass"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_parentclass/"
description: "sc::ParentClass –"
---

<p>sc::ParentClass &#8211; </p>
<p> Gives one parent class of a class.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;class.h&gt;

Public Types</code></pre>
<p> enum <code>Access</code> { <code>Private</code>, <code>Protected</code>, <code>Public</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>ParentClass (ClassDesc *, Access access=Private, int is_virtual=0)



ParentClass (const ParentClass &amp;)



int is_virtual () const



Access access () const



const ClassDesc * classdesc () const



void change_classdesc (ClassDesc *n)</code></pre>
<h2>Detailed Description</h2>
<p>Gives one parent class of a class.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
