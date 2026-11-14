---
title: "gstream-restore(3)"
name: "gstream-restore"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-restore/"
description: "restore"
---

<h2>NAME</h2>
<p> restore</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void restore();</code></p>
<h2>DESCRIPTION</h2>
<p> When you have activated a tabulator stop (by using the &#8216;	&#8217; character), it might change the colour or the font depending on what or what not you have told it to do. To get the original settings back you can call this function. </p>
<p> It is automatically called when a newline (&#8216;
&#8217;) is encountered, and in a few other situations. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-set_tab/">gstream-set_tab</a></code>(3), <code><a href="/docs/linux/man/3-gstream-remove_tab/">gstream-remove_tab</a></code>(3), <code><a href="/docs/linux/man/3-gstream-remove_all_tabs/">gstream-remove_all_tabs</a></code>(3) </p>
<h2>Index</h2>
