---
title: "spline(3)"
name: "spline"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spline/"
description: "spline – Draws a Bezier spline using four control points. Allegro game programming library."
---

<p>spline &#8211; Draws a Bezier spline using four control points. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void spline(BITMAP *bmp, const int points[8], int color);</code></pre>
<h2>Description</h2>
<p>Draws a Bezier spline using the four control points specified in the points array. Read the description of calc_spline() for information on how to build the points array. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-calc_spline/">calc_spline</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3) </p>
