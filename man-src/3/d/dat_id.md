---
title: "dat_id(3)"
name: "dat_id"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dat_id/"
description: "DAT_ID – Makes an ID value from four letters. Allegro game programming library."
---

<p>DAT_ID &#8211; Makes an ID value from four letters. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Macro DAT_ID(a, b, c, d);</code></p>
<h2>Description</h2>
<p>Every object or property in a datafile is identified by a 4 letter ID, which can be created with this macro. For example, to access the NAME property of a datafile object, you could use: </p>
<pre> get_datafile_property(datob, DAT_ID('N','A','M','E'));</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-register_datafile_object/">register_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-get_datafile_property/">get_datafile_property</a></code>(3)</p>
