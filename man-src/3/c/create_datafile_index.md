---
title: "create_datafile_index(3)"
name: "create_datafile_index"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_datafile_index/"
description: "create_datafile_index – Creates an index for a datafile. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_datafile_index &#8211; Creates an index for a datafile. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>DATAFILE_INDEX *create_datafile_index(const char *filename);</code></p>
<h2>DESCRIPTION</h2>
<p> Creates an index for a datafile, to speed up loading single objects out of it. This is mostly useful for big datafiles, which you don&#8217;t want to load as a whole. The index will store the offset of all objects inside the datafile, and then you can load it quickly with &quot;load_datafile_object_indexed&quot; later. Use destroy_datafile_index to free the memory used by it again. </p>
<p> Note: If the datafile uses global compression, there is no performance gain from using an index, because seeking to the offset still requires to uncompress the whole datafile up to that offset. Example: </p>
<pre><code>
DATAFILE_INDEX *index = create_datafile_index("huge.dat");
DATAFILE *object = load_datafile_object_indexed(index, 1234);
... unload_datafile_object(object);
destroy_datafile_index(index);
</code></pre>
<h2>RETURN VALUE</h2>
<p> A pointer value which you can pass to load_datafile_object_indexed. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-destroy_datafile_index/">destroy_datafile_index</a></code>(3), <code><a href="/docs/linux/man/3-load_datafile_object_indexed/">load_datafile_object_indexed</a></code>(3) </p>
<h2>Index</h2>
