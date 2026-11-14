---
title: "hdf_search_path(3)"
name: "hdf_search_path"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hdf_search_path/"
description: "hdf_search_path – Find a file given a search path in HDF"
---

<h2 class="name">NAME</h2>
<p> hdf_search_path &#8211; Find a file given a search path in HDF </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;util/neo_hdf.h&gt;
</code></pre>
<pre><code>
NEOERR *hdf_search_path(HDF *hdf, const char *path, char *full);
</code></pre>
<h2>ARGUMENTS</h2>
<p> hdf -&gt; the hdf dataset to use<br />
 path -&gt; the relative path<br />
 full -&gt; a pointer to a _POSIX_PATH_MAX buffer </p>
<h2>DESCRIPTION</h2>
<p> hdf_search_path is a convenience/utility function that searches for relative filenames in a search path. The search path is the list given by the children of hdf.loadpaths. </p>
<h2>RETURN VALUE</h2>
<p> full -&gt; the full path of the file </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hdf_set_symlink/">hdf_set_symlink</a></code>(3), <a href="/docs/linux/man/3-hdf_get_valuef/">hdf_get_valuef</a><code>(3), compareFunc)</code>(3), <a href="/docs/linux/man/3-hdf_dump_str/">hdf_dump_str</a><code>(3), <a href="/docs/linux/man/3-hdf_get_int_value/">hdf_get_int_value</a></code>(3), <a href="/docs/linux/man/3-hdf_read_string_ignore/">hdf_read_string_ignore</a><code>(3), <a href="/docs/linux/man/3-hdf_copy/">hdf_copy</a></code>(3), <a href="/docs/linux/man/3-hdf_get_node/">hdf_get_node</a><code>(3), <a href="/docs/linux/man/3-hdf_set_value/">hdf_set_value</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_child/">hdf_obj_child</a><code>(3), <a href="/docs/linux/man/3-hdf_read_string/">hdf_read_string</a></code>(3), <a href="/docs/linux/man/3-hdf_set_buf/">hdf_set_buf</a><code>(3), <a href="/docs/linux/man/3-hdf_register_fileload/">hdf_register_fileload</a></code>(3), <a href="/docs/linux/man/3-hdf_get_obj/">hdf_get_obj</a><code>(3), <a href="/docs/linux/man/3-hdf_get_attr/">hdf_get_attr</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_top/">hdf_obj_top</a><code>(3), <a href="/docs/linux/man/3-hdf_dump_format/">hdf_dump_format</a></code>(3), <a href="/docs/linux/man/3-hdf_destroy/">hdf_destroy</a><code>(3), <a href="/docs/linux/man/3-hdf_init/">hdf_init</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_value/">hdf_obj_value</a><code>(3), <a href="/docs/linux/man/3-hdf_write_string/">hdf_write_string</a></code>(3), <a href="/docs/linux/man/3-hdf_set_valuevf/">hdf_set_valuevf</a><code>(3), <a href="/docs/linux/man/3-hdf_sort_obj/">hdf_sort_obj</a></code>(3), <a href="/docs/linux/man/3-hdf_write_file_atomic/">hdf_write_file_atomic</a><code>(3), <a href="/docs/linux/man/3-hdf_obj_attr/">hdf_obj_attr</a></code>(3), <a href="/docs/linux/man/3-hdf_set_valuef/">hdf_set_valuef</a><code>(3), <a href="/docs/linux/man/3-hdf_get_copy/">hdf_get_copy</a></code>(3), <a href="/docs/linux/man/3-hdf_write_file/">hdf_write_file</a><code>(3), <a href="/docs/linux/man/3-hdf_get_valuevf/">hdf_get_valuevf</a></code>(3), hdf_remove_tree </p>
<h2>Index</h2>
