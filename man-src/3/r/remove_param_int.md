---
title: "remove_param_int(3)"
name: "remove_param_int"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remove_param_int/"
description: "remove_param_int – Removes a timer with a customizable parameter. Allegro game programming library."
---

<p>remove_param_int &#8211; Removes a timer with a customizable parameter. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void remove_param_int(void (*proc)(void *), void *param);</code></pre>
<h2>Description</h2>
<p>Like remove_int(), but for use with timer callbacks that have parameter values. If there is more than one copy of the same callback active at a time, it identifies which one to remove by checking the parameter value (so you can&#8217;t have more than one copy of a handler using an identical parameter). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_param_int/">install_param_int</a></code>(3), <code><a href="/docs/linux/man/3-install_param_int_ex/">install_param_int_ex</a></code>(3), <code><a href="/docs/linux/man/3-remove_int/">remove_int</a></code>(3) </p>
