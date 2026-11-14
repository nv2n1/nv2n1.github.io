---
title: "set_display_switch_callback(3)"
name: "set_display_switch_callback"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_display_switch_callback/"
description: "set_display_switch_callback – Installs a switching notification callback. Allegro game programming library."
---

<p>set_display_switch_callback &#8211; Installs a switching notification callback. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int set_display_switch_callback(int dir, void (*cb)());</code></pre>
<h2>Description</h2>
<p>Installs a notification callback for the switching mode that was previously selected by calling set_display_switch_mode(). The direction parameter can either be SWITCH_IN or SWITCH_OUT, depending whether you want to be notified about switches away from your program or back to your program. You can sometimes install callbacks for both directions at the same time, but not every platform supports this. You can install several switch callbacks, but no more than eight on any platform.</p>
<h2>Return Value</h2>
<p>Returns zero on success, decreasing the number of empty callback slots by one. Returns -1 if the request is impossible for the current platform or you have reached the maximum number of allowed callbacks. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-remove_display_switch_callback/">remove_display_switch_callback</a></code>(3), <code><a href="/docs/linux/man/3-set_display_switch_mode/">set_display_switch_mode</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3) </p>
