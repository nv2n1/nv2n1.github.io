---
title: "sc_identity(3)"
name: "sc_identity"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_identity/"
description: "sc::Identity –"
---

<p>sc::Identity &#8211; </p>
<p> <code>Identity</code> gives objects a unique identity and ordering relationship relative to all other objects.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;identity.h&gt;</code></pre>
<p> Inherited by <code>sc::ClassDesc</code>, and <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Identifier</code> <code>identifier</code> ()<br />
 <i>Return the </i><code>Identifier</code> for this argument.</p>
<h2>Detailed Description</h2>
<p><code>Identity</code> gives objects a unique identity and ordering relationship relative to all other objects. </p>
<p> <code>Identity</code> must be virtually inherited if multiple inheritance is to be used.</p>
<h2>Member Function Documentation</h2>
<h3><code>Identifier</code> sc::Identity::identifier () [inline]</h3>
<p>Return the <code>Identifier</code> for this argument. Usually this is just the pointer to the object.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
