---
title: "sc_transform(3)"
name: "sc_transform"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_transform/"
description: "sc::Transform –"
---

<p>sc::Transform &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DescribedClass</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Transform</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>mat4</code> &amp; <code>transform</code> () </p>
<p> void <code>translate</code> (double, double, double) </p>
<p> void <code>translate</code> (const <code>vec3</code> &amp;) </p>
<p> void <code>rotate</code> (const <code>vec3</code> &amp;, double angle_degrees) </p>
<p> void <code>scale</code> (double) </p>
<p> void <code>print</code> (std::ostream &amp;=ExEnv::out0()) const<br />
 <i>Print the object. </i> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
