---
title: "d_slider_proc(3)"
name: "d_slider_proc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-d_slider_proc/"
description: "d_slider_proc – Dialog procedure implementing a slider control object. Allegro game programming library."
---

<h2>NAME</h2>
<p> d_slider_proc &#8211; Dialog procedure implementing a slider control object. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int d_slider_proc(int msg, DIALOG *d, int c);</code></p>
<h2>DESCRIPTION</h2>
<p> A slider control object. This object holds a value in d2, in the range from 0 to d1. It will display as a vertical slider if h is greater than or equal to w, otherwise it will display as a horizontal slider. The dp field can contain an optional bitmap to use for the slider handle, and dp2 can contain an optional callback function, which is called each time d2 changes. The callback function should have the following prototype: </p>
<pre><code>
int function(void *dp3, int d2);
</code></pre>
<p> The d_slider_proc object will return the value of the callback function. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3) </p>
<h2>Index</h2>
