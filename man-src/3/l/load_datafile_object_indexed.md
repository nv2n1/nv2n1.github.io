---
title: "load_datafile_object_indexed(3)"
name: "load_datafile_object_indexed"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_datafile_object_indexed/"
description: "load_datafile_object_indexed – Loads a single object from a datafile index. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_datafile_object_indexed &#8211; Loads a single object from a datafile index. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>DATAFILE *load_datafile_object_indexed(const DATAFILE_INDEX *index, int item)</code></p>
<h2>DESCRIPTION</h2>
<p> This loads a single object, using the index created previously with create_datafile_index. See create_datafile_index for an example.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to a single DATAFILE element whose &quot;dat&quot; member points to the object, or NULL if the object could not be loaded. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_datafile_index/">create_datafile_index</a></code>(3), <code><a href="/docs/linux/man/3-load_datafile_object/">load_datafile_object</a></code>(3), <code><a href="/docs/linux/man/3-unload_datafile_object/">unload_datafile_object</a></code>(3) </p>
<h2>Index</h2>
