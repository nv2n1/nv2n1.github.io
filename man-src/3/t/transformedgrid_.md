---
title: "transformedgrid_(3)"
name: "transformedgrid_"
section: "3"
letter: "t"
url: "/docs/linux/man/3-transformedgrid_/"
description: "QuantLib::TransformedGrid – transformed grid"
---

<p>QuantLib::TransformedGrid &#8211; transformed grid </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/math/transformedgrid.hpp&gt;</code></pre>
<p> Inherited by LogGrid.</p>
<h3>Public Member Functions</h3>
<p><code>TransformedGrid</code> (const <code>Array</code> &amp;grid) </p>
<p> template&lt;class T &gt; <code>TransformedGrid</code> (const <code>Array</code> &amp;grid, T func) </p>
<p> const <code>Array</code> &amp; <code>gridArray</code> () const </p>
<p> const <code>Array</code> &amp; <code>transformedGridArray</code> () const </p>
<p> const <code>Array</code> &amp; <code>dxmArray</code> () const </p>
<p> const <code>Array</code> &amp; <code>dxpArray</code> () const </p>
<p> const <code>Array</code> &amp; <code>dxArray</code> () const </p>
<p> <code>Real</code> <code>grid</code> (Size i) const </p>
<p> <code>Real</code> <code>transformedGrid</code> (Size i) const </p>
<p> <code>Real</code> <code>dxm</code> (Size i) const </p>
<p> <code>Real</code> <code>dxp</code> (Size i) const </p>
<p> <code>Real</code> <code>dx</code> (Size i) const </p>
<p> Size <code>size</code> () const</p>
<h3>Protected Attributes</h3>
<p><code>Array</code> <code>grid_</code> </p>
<p> <code>Array</code> <code>transformedGrid_</code> </p>
<p> <code>Array</code> <code>dxm_</code> </p>
<p> <code>Array</code> <code>dxp_</code> </p>
<p> <code>Array</code> <code>dx_</code></p>
<h2>Detailed Description</h2>
<p>transformed grid </p>
<p> This package encapuslates an array of grid points. It is used primarily in PDE calculations.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
