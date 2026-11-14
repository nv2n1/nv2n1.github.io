---
title: "stdstudent_t_distribution_param_type(3)"
name: "stdstudent_t_distribution_param_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstudent_t_distribution_param_type/"
description: "std::student_t_distribution< _RealType >::param_type –"
---

<p>std::student_t_distribution&lt; _RealType &gt;::param_type &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef <code>student_t_distribution</code><br />
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
<h3>template&lt;typename _RealType = double&gt;struct std::student_t_distribution&lt; _RealType &gt;::param_type</h3>
<p>Parameter type. </p>
<p> Definition at line 3363 of file random.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
