---
title: "dmi_walk(9)"
name: "dmi_walk"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dmi_walk/"
---

dmi_walk - Walk the DMI table and get called back for every record

<h2>Synopsis</h2>

<pre><code>int dmi_walk(void (*decode)(const struct dmi_header *, void *), void *private_data);</code></pre>

<h2>Arguments</h2>

<i>decode</i>
<dl><dd><dd>Callback function</dl>
 

 <i>private_data</i>
<dl><dd>Private data to be passed to the callback function</dl>

<h2>Description</h2>

Returns -1 when the DMI table can't be reached, 0 on success.

<h2>Copyright</h2>


