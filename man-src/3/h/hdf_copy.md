---
title: "hdf_copy(3)"
name: "hdf_copy"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hdf_copy/"
description: "hdf_copy – copy part of an HDF dataset to another"
---

<h2 class="name">NAME</h2>
<p> hdf_copy &#8211; copy part of an HDF dataset to another </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;util/neo_hdf.h&gt;
</code></pre>
<pre><code>
NEOERR *hdf_copy(HDF *dest_hdf, const char *name, HDF *src);
</code></pre>
<h2>ARGUMENTS</h2>
<p> dest_hdf -&gt; the destination dataset<br />
 name -&gt; the name of the destination node<br />
 src -&gt; the hdf dataset to copy to the destination </p>
<h2>DESCRIPTION</h2>
<p> hdf_copy is a deep copy of an HDF tree pointed to by src to the named node of dest. dest and src need not be part of the same data set </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hdf_set_symlink/">hdf_set_symlink</a></code>(3), <a href="/docs/linux/man/3-hdf_get_valuef/">hdf_get_valuef</a><code>(3), compareFunc)</code>(3), <a href="/docs/linux/man/3-hdf_dump_str/">hdf_dump_str</a><code>(3), <a href="/docs/linux/man/3-hdf_get_int_value/">hdf_get_int_value</a></code>(3), <a href="/docs/linux/man/3-hdf_read_string_ignore/">hdf_read_string_ignore</a><code>(3), <a href="/docs/linux/man/3-hdf_copy/">hdf_copy</a></code>(3), <a href="/docs/linux/man/3-hdf_get_node/">hdf_get_node</a><code>(3), <a href="/docs/linux/man/3-hdf_set_value/">hdf_set_value</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_child/">hdf_obj_child</a><code>(3), <a href="/docs/linux/man/3-hdf_read_string/">hdf_read_string</a></code>(3), <a href="/docs/linux/man/3-hdf_set_buf/">hdf_set_buf</a><code>(3), <a href="/docs/linux/man/3-hdf_register_fileload/">hdf_register_fileload</a></code>(3), <a href="/docs/linux/man/3-hdf_get_obj/">hdf_get_obj</a><code>(3), <a href="/docs/linux/man/3-hdf_get_attr/">hdf_get_attr</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_top/">hdf_obj_top</a><code>(3), <a href="/docs/linux/man/3-hdf_dump_format/">hdf_dump_format</a></code>(3), <a href="/docs/linux/man/3-hdf_destroy/">hdf_destroy</a><code>(3), <a href="/docs/linux/man/3-hdf_init/">hdf_init</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_value/">hdf_obj_value</a><code>(3), <a href="/docs/linux/man/3-hdf_write_string/">hdf_write_string</a></code>(3), <a href="/docs/linux/man/3-hdf_set_valuevf/">hdf_set_valuevf</a><code>(3), <a href="/docs/linux/man/3-hdf_sort_obj/">hdf_sort_obj</a></code>(3), <a href="/docs/linux/man/3-hdf_write_file_atomic/">hdf_write_file_atomic</a><code>(3), <a href="/docs/linux/man/3-hdf_obj_attr/">hdf_obj_attr</a></code>(3), <a href="/docs/linux/man/3-hdf_set_valuef/">hdf_set_valuef</a><code>(3), <a href="/docs/linux/man/3-hdf_get_copy/">hdf_get_copy</a></code>(3), <a href="/docs/linux/man/3-hdf_write_file/">hdf_write_file</a><code>(3), <a href="/docs/linux/man/3-hdf_get_valuevf/">hdf_get_valuevf</a></code>(3), hdf_remove_tree </p>
<h2>Index</h2>
