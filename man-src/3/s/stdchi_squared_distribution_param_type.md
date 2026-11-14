---
title: "stdchi_squared_distribution_param_type(3)"
name: "stdchi_squared_distribution_param_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchi_squared_distribution_param_type/"
description: "std::chi_squared_distribution< _RealType >::param_type –"
---

<p>std::chi_squared_distribution&lt; _RealType &gt;::param_type &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef<br />
 <code>chi_squared_distribution</code><br />
 &lt; _RealType &gt; <code>distribution_type</code>&quot;</p>
<h3>Public Attributes</h3>
<pre><code>__pad0__ : _M_n(__n)
{
}
_RealType n() const
{
    return _M_n

        Friends bool
        operator==(const param_type &amp;__p1, const param_type &amp;__p2)</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _RealType = double&gt;struct std::chi_squared_distribution&lt; _RealType &gt;::param_type</h3>
<p>Parameter type. </p>
<p> Definition at line 2728 of file random.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
