---
title: "datafile(3)"
name: "datafile"
section: "3"
letter: "d"
url: "/docs/linux/man/3-datafile/"
description: "DATAFILE – Stores an Allegro datafile in memory."
---

<p>DATAFILE &#8211; Stores an Allegro datafile in memory.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct DATAFILE</code></p>
<h2>Description</h2>
<pre> void *dat; - pointer to the actual data
 int type; - type of the data
 long size; - size of the data in bytes
 void *prop; - list of object properties</pre>
<p>Read chapter &quot;Datafile routines&quot;, section &quot;Using datafiles&quot; for a description on how to obtain/use this structure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-load_datafile/">load_datafile</a></code>(3), <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exdata/">exdata</a></code>(3), <code><a href="/docs/linux/man/3-exexedat/">exexedat</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3), <code><a href="/docs/linux/man/3-exunicod/">exunicod</a></code>(3)</p>
