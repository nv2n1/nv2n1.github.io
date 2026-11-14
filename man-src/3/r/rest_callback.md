---
title: "rest_callback(3)"
name: "rest_callback"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rest_callback/"
description: "rest_callback – Like rest(), but calls the callback during the wait. Allegro game programming library."
---

<p>rest_callback &#8211; Like rest(), but calls the callback during the wait. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>void rest_callback(long time, void (*callback)())</code></p>
<h2>Description</h2>
<p>Like rest(), but for non-zero values continually calls the specified function while it is waiting for the required time to elapse. If the provided `callback&#8217; parameter is NULL, this function does exactly the same thing as calling rest(). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-rest/">rest</a></code>(3) </p>
