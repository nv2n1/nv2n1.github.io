---
title: "sc_mat3(3)"
name: "sc_mat3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mat3/"
description: "sc::mat3 –"
---

<p>sc::mat3 &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>mat3 (const vec3 &amp;v0, const vec3 &amp;v1, const vec3 &amp;v2)



mat3 (const double d)



mat3 (const mat3 &amp;m)



mat3 &amp; operator= (const mat3 &amp;m)



mat3 &amp; operator+= (const mat3 &amp;m)



mat3 &amp; operator-= (const mat3 &amp;m)



mat3 &amp; operator*= (const double d)



mat3 &amp; operator/= (const double d)



vec3 &amp; operator[] (int i)



const vec3 &amp; operator[] (int i) const



mat3 transpose () const



mat3 inverse ()



mat3 &amp; apply (V_FCT_PTR fct)



Protected Attributes</code></pre>
<p> <code>vec3</code> <code>v</code> [3]</p>
<h3>Friends</h3>
<p><code>mat3</code> <code>operator-</code> (const <code>mat3</code> &amp;a) </p>
<p> <code>mat3</code> <code>operator+</code> (const <code>mat3</code> &amp;a, const <code>mat3</code> &amp;b) </p>
<p> <code>mat3</code> <code>operator-</code> (const <code>mat3</code> &amp;a, const <code>mat3</code> &amp;b) </p>
<p> <code>mat3</code> <code>operator*</code> (const <code>mat3</code> &amp;a, const <code>mat3</code> &amp;b) </p>
<p> <code>mat3</code> <code>operator*</code> (const <code>mat3</code> &amp;a, const double d) </p>
<p> <code>mat3</code> <code>operator*</code> (const double d, const <code>mat3</code> &amp;a) </p>
<p> <code>mat3</code> <code>operator/</code> (const <code>mat3</code> &amp;a, const double d) </p>
<p> int <code>operator==</code> (const <code>mat3</code> &amp;a, const <code>mat3</code> &amp;b) </p>
<p> int <code>operator!=</code> (const <code>mat3</code> &amp;a, const <code>mat3</code> &amp;b) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;s, <code>mat3</code> &amp;m) </p>
<p> std::istream &amp; <code>operator&gt;&gt;</code> (std::istream &amp;s, <code>mat3</code> &amp;m) </p>
<p> void <code>swap</code> (<code>mat3</code> &amp;a, <code>mat3</code> &amp;b) </p>
<p> <code>vec3</code> <code>operator*</code> (const <code>mat3</code> &amp;a, const <code>vec3</code> &amp;v) </p>
<p> <code>vec2</code> <code>operator*</code> (const <code>mat3</code> &amp;a, const <code>vec2</code> &amp;v) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
