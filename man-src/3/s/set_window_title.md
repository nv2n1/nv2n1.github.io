---
title: "set_window_title(3)"
name: "set_window_title"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_window_title/"
description: "set_window_title – Sets the window title of the Allegro program."
---

<p>set_window_title &#8211; Sets the window title of the Allegro program.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void set_window_title(const char *name);</code></p>
<h2>Description</h2>
<p> On platforms that are capable of it, this routine alters the window title for your Allegro program. Note that Allegro cannot set the window title when running in a DOS box under Windows. Example: </p>
<pre>
   set_window_title(&quot;Allegro rules!&quot;);
</pre>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-set_close_button_callback/">set_close_button_callback</a></code>(3), <code><a href="/docs/linux/man/3-set_uformat/">set_uformat</a></code>(3), <code><a href="/docs/linux/man/3-exunicod/">exunicod</a></code>(3)</p>
