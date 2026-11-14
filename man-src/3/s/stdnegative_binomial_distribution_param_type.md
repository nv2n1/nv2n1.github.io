---
title: "stdnegative_binomial_distribution_param_type(3)"
name: "stdnegative_binomial_distribution_param_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnegative_binomial_distribution_param_type/"
description: "std::negative_binomial_distribution< _IntType >::param_type –"
---

<p>std::negative_binomial_distribution&lt; _IntType &gt;::param_type &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef<br />
 <code>negative_binomial_distribution</code><br />
 &lt; _IntType &gt; <code>distribution_type</code>&quot;</p>
<h3>Public Member Functions</h3>
<pre><code>param_type (_IntType __k=1, double __p=0.5)



_IntType k () const



double p () const



Friends</code></pre>
<p> bool <code>operator==</code> (const <code>param_type</code> &amp;__p1, const <code>param_type</code> &amp;__p2)</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _IntType = int&gt;struct std::negative_binomial_distribution&lt; _IntType &gt;::param_type</h3>
<p>Parameter type. </p>
<p> Definition at line 4217 of file random.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
