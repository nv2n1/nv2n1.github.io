---
title: "stduniform_real_distribution_param_type(3)"
name: "stduniform_real_distribution_param_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduniform_real_distribution_param_type/"
description: "std::uniform_real_distribution< _RealType >::param_type –"
---

<p>std::uniform_real_distribution&lt; _RealType &gt;::param_type &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef<br />
 <code>uniform_real_distribution</code><br />
 &lt; _RealType &gt; <code>distribution_type</code>&quot;</p>
<h3>Public Member Functions</h3>
<pre><code>param_type (_RealType __a=_RealType(0), _RealType __b=_RealType(1))



result_type a () const



result_type b () const



Friends</code></pre>
<p> bool <code>operator==</code> (const <code>param_type</code> &amp;__p1, const <code>param_type</code> &amp;__p2)</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _RealType = double&gt;struct std::uniform_real_distribution&lt; _RealType &gt;::param_type</h3>
<p>Parameter type. </p>
<p> Definition at line 1876 of file random.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
