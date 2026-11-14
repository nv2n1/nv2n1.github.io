---
title: "stddiscrete_distribution_param_type(3)"
name: "stddiscrete_distribution_param_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddiscrete_distribution_param_type/"
description: "std::discrete_distribution< _IntType >::param_type –"
---

<p>std::discrete_distribution&lt; _IntType &gt;::param_type &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef <code>discrete_distribution</code><br />
 &lt; _IntType &gt; <code>distribution_type</code>&quot;</p>
<h3>Public Member Functions</h3>
<pre><code>template&lt;typename _InputIterator &gt; param_type (_InputIterator __wbegin, _InputIterator __wend)



param_type (initializer_list&lt; double &gt; __wil)



template&lt;typename _Func &gt; param_type (size_t __nw, double __xmin, double __xmax, _Func __fw)



param_type (const param_type &amp;)=default



param_type &amp; operator= (const param_type &amp;)=default



std::vector&lt; double &gt; probabilities () const



Friends</code></pre>
<p> class <code>discrete_distribution&lt; _IntType &gt;</code> </p>
<p> bool <code>operator==</code> (const <code>param_type</code> &amp;__p1, const <code>param_type</code> &amp;__p2)</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _IntType = int&gt;struct std::discrete_distribution&lt; _IntType &gt;::param_type</h3>
<p>Parameter type. </p>
<p> Definition at line 5260 of file random.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
