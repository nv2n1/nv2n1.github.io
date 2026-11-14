---
title: "sc_mat4(3)"
name: "sc_mat4"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mat4/"
description: "sc::mat4 –"
---

<p>sc::mat4 &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>mat4 (const vec4 &amp;v0, const vec4 &amp;v1, const vec4 &amp;v2, const vec4 &amp;v3)



mat4 (const double d)



mat4 (const mat4 &amp;m)



mat4 &amp; operator= (const mat4 &amp;m)



mat4 &amp; operator+= (const mat4 &amp;m)



mat4 &amp; operator-= (const mat4 &amp;m)



mat4 &amp; operator*= (const double d)



mat4 &amp; operator/= (const double d)



vec4 &amp; operator[] (int i)



const vec4 &amp; operator[] (int i) const



mat4 transpose () const



mat4 inverse ()



mat4 &amp; apply (V_FCT_PTR fct)



Protected Attributes</code></pre>
<p> <code>vec4</code> <code>v</code> [4]</p>
<h3>Friends</h3>
<p><code>mat4</code> <code>operator-</code> (const <code>mat4</code> &amp;a) </p>
<p> <code>mat4</code> <code>operator+</code> (const <code>mat4</code> &amp;a, const <code>mat4</code> &amp;b) </p>
<p> <code>mat4</code> <code>operator-</code> (const <code>mat4</code> &amp;a, const <code>mat4</code> &amp;b) </p>
<p> <code>mat4</code> <code>operator*</code> (const <code>mat4</code> &amp;a, const <code>mat4</code> &amp;b) </p>
<p> <code>mat4</code> <code>operator*</code> (const <code>mat4</code> &amp;a, const double d) </p>
<p> <code>mat4</code> <code>operator*</code> (const double d, const <code>mat4</code> &amp;a) </p>
<p> <code>mat4</code> <code>operator/</code> (const <code>mat4</code> &amp;a, const double d) </p>
<p> int <code>operator==</code> (const <code>mat4</code> &amp;a, const <code>mat4</code> &amp;b) </p>
<p> int <code>operator!=</code> (const <code>mat4</code> &amp;a, const <code>mat4</code> &amp;b) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;s, <code>mat4</code> &amp;m) </p>
<p> std::istream &amp; <code>operator&gt;&gt;</code> (std::istream &amp;s, <code>mat4</code> &amp;m) </p>
<p> void <code>swap</code> (<code>mat4</code> &amp;a, <code>mat4</code> &amp;b) </p>
<p> <code>vec4</code> <code>operator*</code> (const <code>mat4</code> &amp;a, const <code>vec4</code> &amp;v) </p>
<p> <code>vec3</code> <code>operator*</code> (const <code>mat4</code> &amp;a, const <code>vec3</code> &amp;v) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
