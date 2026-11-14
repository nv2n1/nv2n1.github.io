---
title: "hdf_set_value(3)"
name: "hdf_set_value"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hdf_set_value/"
description: "hdf_set_value – Set the value of a named node"
---

<h2 class="name">NAME</h2>
<p> hdf_set_value &#8211; Set the value of a named node </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;util/neo_hdf.h&gt;
</code></pre>
<pre><code>
NEOERR *hdf_set_value(HDF *hdf, const char *name, const char *value);
</code></pre>
<h2>ARGUMENTS</h2>
<p> hdf -&gt; the pointer to the hdf dataset<br />
 name -&gt; the named node to walk to<br />
 value -&gt; the value to set the node to </p>
<h2>DESCRIPTION</h2>
<p> hdf_set_value will set the value of a named node. All of the interstitial nodes which don&#8217;t exist will be created with a value of NULL. Existing nodes are not modified. New nodes are created at the end of the list. If a list of nodes exceeds FORCE_HASH_AT, then a HASH will be created at that level and all of the nodes will be added to the hash for faster lookup times. The copy of the value will be made which the dataset will own. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hdf_set_symlink/">hdf_set_symlink</a></code>(3), <a href="/docs/linux/man/3-hdf_get_valuef/">hdf_get_valuef</a><code>(3), compareFunc)</code>(3), <a href="/docs/linux/man/3-hdf_dump_str/">hdf_dump_str</a><code>(3), <a href="/docs/linux/man/3-hdf_get_int_value/">hdf_get_int_value</a></code>(3), <a href="/docs/linux/man/3-hdf_read_string_ignore/">hdf_read_string_ignore</a><code>(3), <a href="/docs/linux/man/3-hdf_copy/">hdf_copy</a></code>(3), <a href="/docs/linux/man/3-hdf_get_node/">hdf_get_node</a><code>(3), <a href="/docs/linux/man/3-hdf_set_value/">hdf_set_value</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_child/">hdf_obj_child</a><code>(3), <a href="/docs/linux/man/3-hdf_read_string/">hdf_read_string</a></code>(3), <a href="/docs/linux/man/3-hdf_set_buf/">hdf_set_buf</a><code>(3), <a href="/docs/linux/man/3-hdf_register_fileload/">hdf_register_fileload</a></code>(3), <a href="/docs/linux/man/3-hdf_get_obj/">hdf_get_obj</a><code>(3), <a href="/docs/linux/man/3-hdf_get_attr/">hdf_get_attr</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_top/">hdf_obj_top</a><code>(3), <a href="/docs/linux/man/3-hdf_dump_format/">hdf_dump_format</a></code>(3), <a href="/docs/linux/man/3-hdf_destroy/">hdf_destroy</a><code>(3), <a href="/docs/linux/man/3-hdf_init/">hdf_init</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_value/">hdf_obj_value</a><code>(3), <a href="/docs/linux/man/3-hdf_write_string/">hdf_write_string</a></code>(3), <a href="/docs/linux/man/3-hdf_set_valuevf/">hdf_set_valuevf</a><code>(3), <a href="/docs/linux/man/3-hdf_sort_obj/">hdf_sort_obj</a></code>(3), <a href="/docs/linux/man/3-hdf_write_file_atomic/">hdf_write_file_atomic</a><code>(3), <a href="/docs/linux/man/3-hdf_obj_attr/">hdf_obj_attr</a></code>(3), <a href="/docs/linux/man/3-hdf_set_valuef/">hdf_set_valuef</a><code>(3), <a href="/docs/linux/man/3-hdf_get_copy/">hdf_get_copy</a></code>(3), <a href="/docs/linux/man/3-hdf_write_file/">hdf_write_file</a><code>(3), <a href="/docs/linux/man/3-hdf_get_valuevf/">hdf_get_valuevf</a></code>(3), hdf_remove_tree </p>
<h2>Index</h2>
