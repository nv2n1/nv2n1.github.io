---
title: "register_datafile_object(3)"
name: "register_datafile_object"
section: "3"
letter: "r"
url: "/docs/linux/man/3-register_datafile_object/"
description: "register_datafile_object – Registers load/destroy functions for custom object types. Allegro game programming library."
---

<p>register_datafile_object &#8211; Registers load/destroy functions for custom object types. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void register_datafile_object(int id, void *(*load)(PACKFILE *f, long size),

                              void (*destroy)(void *data));</code></pre>
<h2>Description</h2>
<p>Used to add custom object types, specifying functions to load and destroy objects of this type. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-load_datafile/">load_datafile</a></code>(3), <code><a href="/docs/linux/man/3-load_datafile_object/">load_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-dat_id/">DAT_ID</a></code>(3) </p>
