---
title: "remove_display_switch_callback(3)"
name: "remove_display_switch_callback"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remove_display_switch_callback/"
description: "remove_display_switch_callback – Removes a switching notification callback. Allegro game programming library."
---

<p>remove_display_switch_callback &#8211; Removes a switching notification callback. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void remove_display_switch_callback(void (*cb)());</code></pre>
<h2>Description</h2>
<p>Removes a notification callback that was previously installed by calling set_display_switch_callback(). All the callbacks will automatically be removed when you call set_display_switch_mode(). You can safely call this function even if the callback you want to remove is not installed. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_display_switch_callback/">set_display_switch_callback</a></code>(3) </p>
