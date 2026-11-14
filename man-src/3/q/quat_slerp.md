---
title: "quat_slerp(3)"
name: "quat_slerp"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quat_slerp/"
---

quat_slerp - Version of quat_interpolate() allowing control over the rotation. Allegro game programming library.

<h2>Synopsis</h2>

<pre><code>#include &lt;allegro.h&gt;

void quat_slerp(const QUAT *from, const QUAT *to, float t, QUAT *out, int how);</code></pre>

<h2>Description</h2>

The same as quat_interpolate(), but allows more control over how the rotation is done. The how parameter can be any one of the values: <pre> QUAT_SHORT - like quat_interpolate(), use shortest path
 QUAT_LONG - rotation will be greater than 180 degrees
 QUAT_CW - rotate clockwise when viewed from above
 QUAT_CCW - rotate counterclockwise when viewed from above
 QUAT_USER - the quaternions are interpolated exactly as
 given</pre>
