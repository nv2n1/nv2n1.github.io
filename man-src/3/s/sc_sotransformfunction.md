---
title: "sc_sotransformfunction(3)"
name: "sc_sotransformfunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sotransformfunction/"
description: "sc::SOTransformFunction –"
---

<p>sc::SOTransformFunction &#8211; </p>
<p> <code>SOTransformShell</code> describes how an AO function contributes to an <code>SO</code> function in a particular <code>SO</code> shell.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;sobasis.h&gt;

Public Attributes</code></pre>
<p> double <code>coef</code><br />
 <i>The coefficient of the AO. </i><br />
 int <code>aofunc</code><br />
 <i>The AO function number. </i><br />
 int <code>sofunc</code><br />
 <i>The </i><code>SO</code> function number.<br />
 int <code>irrep</code><br />
 <i>The </i><code>SO</code> function&#8217;s irrep.</p>
<h2>Detailed Description</h2>
<p><code>SOTransformShell</code> describes how an AO function contributes to an <code>SO</code> function in a particular <code>SO</code> shell.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
