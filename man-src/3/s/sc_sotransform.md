---
title: "sc_sotransform(3)"
name: "sc_sotransform"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sotransform/"
description: "sc::SOTransform –"
---

<p>sc::SOTransform &#8211; </p>
<p> <code>SOTransform</code> maintains a list of AO shells that are be used to compute the <code>SO</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;sobasis.h&gt;

Public Member Functions
void set_naoshell (int n)



void add_transform (int aoshell, int irrep, double coef, int aofunc, int sofunc)


Adds another term to the transform.



Public Attributes
int naoshell_allocated



int naoshell


The number of AO shells that make up this SO shell.


SOTransformShell * aoshell


The SOTransformShell object for each AO.</code></pre>
<h2>Detailed Description</h2>
<p><code>SOTransform</code> maintains a list of AO shells that are be used to compute the <code>SO</code>. </p>
<p> The information is stored in objects of type <code>SOTransformShell</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
