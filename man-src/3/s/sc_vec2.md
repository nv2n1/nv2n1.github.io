---
title: "sc_vec2(3)"
name: "sc_vec2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_vec2/"
description: "sc::vec2 –"
---

<p>sc::vec2 &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>vec2 (const double x, const double y)



vec2 (const double d)



vec2 (const vec2 &amp;v)



vec2 (const vec3 &amp;v)



vec2 (const vec3 &amp;v, int dropAxis)



vec2 &amp; operator= (const vec2 &amp;v)



vec2 &amp; operator+= (const vec2 &amp;v)



vec2 &amp; operator-= (const vec2 &amp;v)



vec2 &amp; operator*= (const double d)



vec2 &amp; operator/= (const double d)



double &amp; operator[] (int i)



const double &amp; operator[] (int i) const



double length ()



double length2 ()



vec2 &amp; normalize ()



vec2 &amp; apply (V_FCT_PTR fct)



Protected Attributes
double n [2]



Friends</code></pre>
<p> class <code>vec3</code> </p>
<p> <code>vec2</code> <code>operator-</code> (const <code>vec2</code> &amp;v) </p>
<p> <code>vec2</code> <code>operator+</code> (const <code>vec2</code> &amp;a, const <code>vec2</code> &amp;b) </p>
<p> <code>vec2</code> <code>operator-</code> (const <code>vec2</code> &amp;a, const <code>vec2</code> &amp;b) </p>
<p> <code>vec2</code> <code>operator*</code> (const <code>vec2</code> &amp;a, const double d) </p>
<p> <code>vec2</code> <code>operator*</code> (const double d, const <code>vec2</code> &amp;a) </p>
<p> <code>vec2</code> <code>operator*</code> (const <code>mat3</code> &amp;a, const <code>vec2</code> &amp;v) </p>
<p> <code>vec2</code> <code>operator*</code> (const <code>vec2</code> &amp;v, <code>mat3</code> &amp;a) </p>
<p> double <code>operator*</code> (const <code>vec2</code> &amp;a, const <code>vec2</code> &amp;b) </p>
<p> <code>vec2</code> <code>operator/</code> (const <code>vec2</code> &amp;a, const double d) </p>
<p> <code>vec3</code> <code>operator^</code> (const <code>vec2</code> &amp;a, const <code>vec2</code> &amp;b) </p>
<p> int <code>operator==</code> (const <code>vec2</code> &amp;a, const <code>vec2</code> &amp;b) </p>
<p> int <code>operator!=</code> (const <code>vec2</code> &amp;a, const <code>vec2</code> &amp;b) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;s, <code>vec2</code> &amp;v) </p>
<p> std::istream &amp; <code>operator&gt;&gt;</code> (std::istream &amp;s, <code>vec2</code> &amp;v) </p>
<p> void <code>swap</code> (<code>vec2</code> &amp;a, <code>vec2</code> &amp;b) </p>
<p> <code>vec2</code> <code>min</code> (const <code>vec2</code> &amp;a, const <code>vec2</code> &amp;b) </p>
<p> <code>vec2</code> <code>max</code> (const <code>vec2</code> &amp;a, const <code>vec2</code> &amp;b) </p>
<p> <code>vec2</code> <code>prod</code> (const <code>vec2</code> &amp;a, const <code>vec2</code> &amp;b) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
