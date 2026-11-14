---
title: "stdbinomial_distribution_param_type(3)"
name: "stdbinomial_distribution_param_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbinomial_distribution_param_type/"
description: "std::binomial_distribution< _IntType >::param_type –"
---

<p>std::binomial_distribution&lt; _IntType &gt;::param_type &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef <code>binomial_distribution</code><br />
 &lt; _IntType &gt; <code>distribution_type</code>&quot;</p>
<h3>Public Member Functions</h3>
<p><code>_M_p</code> (__p) </p>
<p> double <code>p</code> () const </p>
<p> _IntType <code>t</code> () const</p>
<h3>Public Attributes</h3>
<p><code>__pad0__</code>: _M_t(__t)</p>
<h3>Friends</h3>
<p>class <code>binomial_distribution&lt; _IntType &gt;</code> </p>
<p> bool <code>operator==</code> (const <code>param_type</code> &amp;__p1, const <code>param_type</code> &amp;__p2)</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _IntType = int&gt;struct std::binomial_distribution&lt; _IntType &gt;::param_type</h3>
<p>Parameter type. </p>
<p> Definition at line 3786 of file random.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
