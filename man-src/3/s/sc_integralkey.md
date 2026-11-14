---
title: "sc_integralkey(3)"
name: "sc_integralkey"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_integralkey/"
description: "sc::IntegralKey –"
---

<p>sc::IntegralKey &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<p><code>IntegralKey</code> (int, int, int, int, int, int, int) </p>
<p> <code>IntegralKey</code> (const <code>IntegralKey</code> &amp;) </p>
<p> bool <code>operator==</code> (const <code>IntegralKey</code> &amp;k) const </p>
<p> bool <code>operator&lt;</code> (const <code>IntegralKey</code> &amp;k) const </p>
<p> int <code>sh0</code> () const </p>
<p> int <code>sh1</code> () const </p>
<p> int <code>p12</code> () const </p>
<p> int <code>p34</code> () const </p>
<p> int <code>sh2</code> () const </p>
<p> int <code>sh3</code> () const </p>
<p> int <code>p13p24</code> () const</p>
<h3>Public Attributes</h3>
<pre><code>unsigned int sh0_sh1_p12_p34



unsigned int sh2_sh3_p13p24
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
