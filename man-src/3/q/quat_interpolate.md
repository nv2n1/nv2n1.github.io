---
title: "quat_interpolate(3)"
name: "quat_interpolate"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quat_interpolate/"
description: "quat_interpolate – Constructs a quaternion representing a rotation between from and to. Allegro game programming library."
---

<p>quat_interpolate &#8211; Constructs a quaternion representing a rotation between from and to. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void quat_interpolate(const QUAT *from, const QUAT *to, float t, QUAT *out);</code></pre>
<h2>Description</h2>
<p>Constructs a quaternion that represents a rotation between from and to. The argument t can be anything between 0 and 1 and represents where between from and to the result will be. 0 returns from, 1 returns to, and 0.5 will return a rotation exactly in between. The result is copied to out. This function will create the short rotation (less than 180 degrees) between from and to. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-exquat/">exquat</a></code>(3) </p>
