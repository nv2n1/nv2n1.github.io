---
title: "sc_shellextent(3)"
name: "sc_shellextent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_shellextent/"
description: "sc::ShellExtent –"
---

<p>sc::ShellExtent &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>void init (const Ref&lt; GaussianBasisSet &gt; &amp;, double resolution=1.0, double tolerance=DBL_EPSILON)



const std::vector&lt; ExtentData &gt; &amp; contributing_shells (int x, int y, int z)


Returns the shells that are nonzero at coordinates x, y, z.


const std::vector&lt; ExtentData &gt; &amp; contributing_shells (double x, double y, double z)



void print (std::ostream &amp;o=ExEnv::out0())



const int * n () const



int n (int ixyz) const



double lower (int ixyz) const



double upper (int ixyz) const



double resolution () const</code></pre>
<h2>Member Function Documentation</h2>
<h3>const std::vector&lt;<code>ExtentData</code>&gt;&amp; sc::ShellExtent::contributing_shells (int x, int y, int z) [inline]</h3>
<p>Returns the shells that are nonzero at coordinates x, y, z. The shells numbers are in ascending order.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
