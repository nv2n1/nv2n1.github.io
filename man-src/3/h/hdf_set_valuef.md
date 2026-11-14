---
title: "hdf_set_valuef(3)"
name: "hdf_set_valuef"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hdf_set_valuef/"
description: "hdf_set_valuef – Set the value of a named node"
---

<h2 class="name">NAME</h2>
<p> hdf_set_valuef &#8211; Set the value of a named node </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;util/neo_hdf.h&gt;
</code></pre>
<pre><code>
NEOERR *hdf_set_valuef(HDF *hdf, const char *fmt, ...)
    ATTRIBUTE_PRINTF(2, 3);
</code></pre>
<h2>ARGUMENTS</h2>
<p> hdf -&gt; the pointer to the hdf dataset<br />
 fmt -&gt; the name=value <a href="/docs/linux/man/3-printf/">printf</a>(3) format string </p>
<h2>DESCRIPTION</h2>
<p> hdf_set_valuef is a convenience function that wraps hdf_set_value. Due to limitations of C, the fmt is in the format &quot;name=value&quot;, where we will first format the entire string, and then break it at the first (from the left) equal sign (=) and use the left portion as the name and the right portion as the value. This function is somewhat inefficient in that it first allocates the full name=value, and then the call to hdf_set_value duplicates the value portion, and then we free the name=value. Currently, we don&#8217;t strip whitespace from the key or value. In the future, this function might work more like reading a single line of an HDF string or file, allowing for attributes and symlinks to be specified&#8230; maybe. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hdf_set_symlink/">hdf_set_symlink</a></code>(3), <a href="/docs/linux/man/3-hdf_get_valuef/">hdf_get_valuef</a><code>(3), compareFunc)</code>(3), <a href="/docs/linux/man/3-hdf_dump_str/">hdf_dump_str</a><code>(3), <a href="/docs/linux/man/3-hdf_get_int_value/">hdf_get_int_value</a></code>(3), <a href="/docs/linux/man/3-hdf_read_string_ignore/">hdf_read_string_ignore</a><code>(3), <a href="/docs/linux/man/3-hdf_copy/">hdf_copy</a></code>(3), <a href="/docs/linux/man/3-hdf_get_node/">hdf_get_node</a><code>(3), <a href="/docs/linux/man/3-hdf_set_value/">hdf_set_value</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_child/">hdf_obj_child</a><code>(3), <a href="/docs/linux/man/3-hdf_read_string/">hdf_read_string</a></code>(3), <a href="/docs/linux/man/3-hdf_set_buf/">hdf_set_buf</a><code>(3), <a href="/docs/linux/man/3-hdf_register_fileload/">hdf_register_fileload</a></code>(3), <a href="/docs/linux/man/3-hdf_get_obj/">hdf_get_obj</a><code>(3), <a href="/docs/linux/man/3-hdf_get_attr/">hdf_get_attr</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_top/">hdf_obj_top</a><code>(3), <a href="/docs/linux/man/3-hdf_dump_format/">hdf_dump_format</a></code>(3), <a href="/docs/linux/man/3-hdf_destroy/">hdf_destroy</a><code>(3), <a href="/docs/linux/man/3-hdf_init/">hdf_init</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_value/">hdf_obj_value</a><code>(3), <a href="/docs/linux/man/3-hdf_write_string/">hdf_write_string</a></code>(3), <a href="/docs/linux/man/3-hdf_set_valuevf/">hdf_set_valuevf</a><code>(3), <a href="/docs/linux/man/3-hdf_sort_obj/">hdf_sort_obj</a></code>(3), <a href="/docs/linux/man/3-hdf_write_file_atomic/">hdf_write_file_atomic</a><code>(3), <a href="/docs/linux/man/3-hdf_obj_attr/">hdf_obj_attr</a></code>(3), <a href="/docs/linux/man/3-hdf_set_valuef/">hdf_set_valuef</a><code>(3), <a href="/docs/linux/man/3-hdf_get_copy/">hdf_get_copy</a></code>(3), <a href="/docs/linux/man/3-hdf_write_file/">hdf_write_file</a><code>(3), <a href="/docs/linux/man/3-hdf_get_valuevf/">hdf_get_valuevf</a></code>(3), hdf_remove_tree </p>
<h2>Index</h2>
