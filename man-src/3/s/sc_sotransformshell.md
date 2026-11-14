---
title: "sc_sotransformshell(3)"
name: "sc_sotransformshell"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sotransformshell/"
description: "sc::SOTransformShell –"
---

<p>sc::SOTransformShell &#8211; </p>
<p> <code>SOTransformShell</code> maintains a list of AO functions contribute to an <code>SO</code> function in a particular <code>SO</code> shell.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;sobasis.h&gt;

Public Member Functions
void add_func (int irrep, double coef, int aofunc, int sofunc)


Add another function to the transform.



Public Attributes</code></pre>
<p> int <code>aoshell</code><br />
 <i>The number of the AO shell from which these functions come. </i><br />
 int <code>nfunc</code><br />
 <i>The number of AO/SO function pairs contributing. </i><br />
 <code>SOTransformFunction</code> * <code>func</code><br />
 <i>The array of </i><code>SOTransformFunction</code> objects describing the transform.</p>
<h2>Detailed Description</h2>
<p><code>SOTransformShell</code> maintains a list of AO functions contribute to an <code>SO</code> function in a particular <code>SO</code> shell. </p>
<p> The information is stored in objects of type <code>SOTransformFunction</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
