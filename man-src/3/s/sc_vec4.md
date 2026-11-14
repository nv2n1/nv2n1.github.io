---
title: "sc_vec4(3)"
name: "sc_vec4"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_vec4/"
description: "sc::vec4 –"
---

<p>sc::vec4 &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>vec4 (const double x, const double y, const double z, const double w)



vec4 (const double d)



vec4 (const vec4 &amp;v)



vec4 (const vec3 &amp;v)



vec4 (const vec3 &amp;v, const double d)



vec4 &amp; operator= (const vec4 &amp;v)



vec4 &amp; operator+= (const vec4 &amp;v)



vec4 &amp; operator-= (const vec4 &amp;v)



vec4 &amp; operator*= (const double d)



vec4 &amp; operator/= (const double d)



double &amp; operator[] (int i)



const double &amp; operator[] (int i) const



double length ()



double length2 ()



vec4 &amp; normalize ()



vec4 &amp; apply (V_FCT_PTR fct)



Protected Attributes
double n [4]



Friends</code></pre>
<p> class <code>vec3</code> </p>
<p> class <code>mat4</code> </p>
<p> <code>vec4</code> <code>operator-</code> (const <code>vec4</code> &amp;v) </p>
<p> <code>vec4</code> <code>operator+</code> (const <code>vec4</code> &amp;a, const <code>vec4</code> &amp;b) </p>
<p> <code>vec4</code> <code>operator-</code> (const <code>vec4</code> &amp;a, const <code>vec4</code> &amp;b) </p>
<p> <code>vec4</code> <code>operator*</code> (const <code>vec4</code> &amp;a, const double d) </p>
<p> <code>vec4</code> <code>operator*</code> (const double d, const <code>vec4</code> &amp;a) </p>
<p> <code>vec4</code> <code>operator*</code> (const <code>mat4</code> &amp;a, const <code>vec4</code> &amp;v) </p>
<p> <code>vec4</code> <code>operator*</code> (const <code>vec4</code> &amp;v, const <code>mat4</code> &amp;a) </p>
<p> double <code>operator*</code> (const <code>vec4</code> &amp;a, const <code>vec4</code> &amp;b) </p>
<p> <code>vec4</code> <code>operator/</code> (const <code>vec4</code> &amp;a, const double d) </p>
<p> int <code>operator==</code> (const <code>vec4</code> &amp;a, const <code>vec4</code> &amp;b) </p>
<p> int <code>operator!=</code> (const <code>vec4</code> &amp;a, const <code>vec4</code> &amp;b) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;s, <code>vec4</code> &amp;v) </p>
<p> std::istream &amp; <code>operator&gt;&gt;</code> (std::istream &amp;s, <code>vec4</code> &amp;v) </p>
<p> void <code>swap</code> (<code>vec4</code> &amp;a, <code>vec4</code> &amp;b) </p>
<p> <code>vec4</code> <code>min</code> (const <code>vec4</code> &amp;a, const <code>vec4</code> &amp;b) </p>
<p> <code>vec4</code> <code>max</code> (const <code>vec4</code> &amp;a, const <code>vec4</code> &amp;b) </p>
<p> <code>vec4</code> <code>prod</code> (const <code>vec4</code> &amp;a, const <code>vec4</code> &amp;b) </p>
<p> <code>vec3</code> <code>operator*</code> (const <code>mat4</code> &amp;a, const <code>vec3</code> &amp;v) </p>
<p> <code>mat4</code> <code>operator*</code> (const <code>mat4</code> &amp;a, const <code>mat4</code> &amp;b) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
