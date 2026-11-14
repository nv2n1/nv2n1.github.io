---
title: "stdpiecewise_constant_distribution_param_type(3)"
name: "stdpiecewise_constant_distribution_param_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpiecewise_constant_distribution_param_type/"
description: "std::piecewise_constant_distribution< _RealType >::param_type –"
---

<p>std::piecewise_constant_distribution&lt; _RealType &gt;::param_type &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef<br />
 <code>piecewise_constant_distribution</code><br />
 &lt; _RealType &gt; <code>distribution_type</code>&quot;</p>
<h3>Public Member Functions</h3>
<pre><code>template&lt;typename _InputIteratorB , typename _InputIteratorW &gt; param_type (_InputIteratorB __bfirst, _InputIteratorB __bend, _InputIteratorW __wbegin)



template&lt;typename _Func &gt; param_type (initializer_list&lt; _RealType &gt; __bi, _Func __fw)



template&lt;typename _Func &gt; param_type (size_t __nw, _RealType __xmin, _RealType __xmax, _Func __fw)



param_type (const param_type &amp;)=default



std::vector&lt; double &gt; densities () const



std::vector&lt; _RealType &gt; intervals () const



param_type &amp; operator= (const param_type &amp;)=default



Friends</code></pre>
<p> bool <code>operator==</code> (const <code>param_type</code> &amp;__p1, const <code>param_type</code> &amp;__p2) </p>
<p> class <code>piecewise_constant_distribution&lt; _RealType &gt;</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _RealType = double&gt;struct std::piecewise_constant_distribution&lt; _RealType &gt;::param_type</h3>
<p>Parameter type. </p>
<p> Definition at line 5490 of file random.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
