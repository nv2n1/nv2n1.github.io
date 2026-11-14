---
title: "sc_vec3(3)"
name: "sc_vec3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_vec3/"
description: "sc::vec3 –"
---

<p>sc::vec3 &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>vec3 (const double x, const double y, const double z)



vec3 (const double d)



vec3 (const vec3 &amp;v)



vec3 (const vec2 &amp;v)



vec3 (const vec2 &amp;v, double d)



vec3 (const vec4 &amp;v)



vec3 (const vec4 &amp;v, int dropAxis)



vec3 &amp; operator= (const vec3 &amp;v)



vec3 &amp; operator+= (const vec3 &amp;v)



vec3 &amp; operator-= (const vec3 &amp;v)



vec3 &amp; operator*= (const double d)



vec3 &amp; operator/= (const double d)



double &amp; operator[] (int i)



const double &amp; operator[] (int i) const



double length ()



double length2 ()



vec3 &amp; normalize ()



vec3 &amp; apply (V_FCT_PTR fct)



Protected Attributes
double n [3]



Friends</code></pre>
<p> class <code>vec2</code> </p>
<p> class <code>vec4</code> </p>
<p> class <code>mat3</code> </p>
<p> <code>vec3</code> <code>operator-</code> (const <code>vec3</code> &amp;v) </p>
<p> <code>vec3</code> <code>operator+</code> (const <code>vec3</code> &amp;a, const <code>vec3</code> &amp;b) </p>
<p> <code>vec3</code> <code>operator-</code> (const <code>vec3</code> &amp;a, const <code>vec3</code> &amp;b) </p>
<p> <code>vec3</code> <code>operator*</code> (const <code>vec3</code> &amp;a, const double d) </p>
<p> <code>vec3</code> <code>operator*</code> (const double d, const <code>vec3</code> &amp;a) </p>
<p> <code>vec3</code> <code>operator*</code> (const <code>mat4</code> &amp;a, const <code>vec3</code> &amp;v) </p>
<p> <code>vec3</code> <code>operator*</code> (const <code>vec3</code> &amp;v, const <code>mat4</code> &amp;a) </p>
<p> double <code>operator*</code> (const <code>vec3</code> &amp;a, const <code>vec3</code> &amp;b) </p>
<p> <code>vec3</code> <code>operator/</code> (const <code>vec3</code> &amp;a, const double d) </p>
<p> <code>vec3</code> <code>operator^</code> (const <code>vec3</code> &amp;a, const <code>vec3</code> &amp;b) </p>
<p> int <code>operator==</code> (const <code>vec3</code> &amp;a, const <code>vec3</code> &amp;b) </p>
<p> int <code>operator!=</code> (const <code>vec3</code> &amp;a, const <code>vec3</code> &amp;b) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;s, <code>vec3</code> &amp;v) </p>
<p> std::istream &amp; <code>operator&gt;&gt;</code> (std::istream &amp;s, <code>vec3</code> &amp;v) </p>
<p> void <code>swap</code> (<code>vec3</code> &amp;a, <code>vec3</code> &amp;b) </p>
<p> <code>vec3</code> <code>min</code> (const <code>vec3</code> &amp;a, const <code>vec3</code> &amp;b) </p>
<p> <code>vec3</code> <code>max</code> (const <code>vec3</code> &amp;a, const <code>vec3</code> &amp;b) </p>
<p> <code>vec3</code> <code>prod</code> (const <code>vec3</code> &amp;a, const <code>vec3</code> &amp;b) </p>
<p> <code>vec2</code> <code>operator*</code> (const <code>mat3</code> &amp;a, const <code>vec2</code> &amp;v) </p>
<p> <code>mat3</code> <code>operator*</code> (const <code>mat3</code> &amp;a, const <code>mat3</code> &amp;b) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
