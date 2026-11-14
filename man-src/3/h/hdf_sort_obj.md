---
title: "hdf_sort_obj(3)"
name: "hdf_sort_obj"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hdf_sort_obj/"
description: "hdf_sort_obj – sort the children of an HDF node"
---

<h2 class="name">NAME</h2>
<p> hdf_sort_obj &#8211; sort the children of an HDF node </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;util/neo_hdf.h&gt;
</code></pre>
<pre>
hdf_sort_obj()
</pre>
<h2>ARGUMENTS</h2>
<p> h &#8211; HDF node<br />
 compareFunc &#8211; function which returns 1,0,-1 depending on some<br />
 criteria. The arguments to this sort function<br />
 are pointers to pointers to HDF elements. For<br />
 example:<br />
 int sortByName(const void *a, const void *b) {<br />
 HDF **ha = (HDF **)a;<br />
 HDF **hb = (HDF **)b;<br />
 *<br />
 return strcasecmp(hdf_obj_name(*ha), hdf_obj_name(*hb));<br />
 }<br />
 * </p>
<h2>DESCRIPTION</h2>
<p> hdf_sort_obj will sort the children of an HDF node, based on the given comparison function. This function works by creating an array of the pointers for each child object of h, using qsort to sort that array, and then re-ordering the linked list of children to the new order. The qsort compare function uses a pointer to the value in the array, which in our case is a pointer to an HDF struct, so your comparison function should work on HDF ** pointers. </p>
<h2>RETURN VALUE</h2>
<p> None (h children will be sorted) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hdf_set_symlink/">hdf_set_symlink</a></code>(3), <a href="/docs/linux/man/3-hdf_get_valuef/">hdf_get_valuef</a><code>(3), compareFunc)</code>(3), <a href="/docs/linux/man/3-hdf_dump_str/">hdf_dump_str</a><code>(3), <a href="/docs/linux/man/3-hdf_get_int_value/">hdf_get_int_value</a></code>(3), <a href="/docs/linux/man/3-hdf_read_string_ignore/">hdf_read_string_ignore</a><code>(3), <a href="/docs/linux/man/3-hdf_copy/">hdf_copy</a></code>(3), <a href="/docs/linux/man/3-hdf_get_node/">hdf_get_node</a><code>(3), <a href="/docs/linux/man/3-hdf_set_value/">hdf_set_value</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_child/">hdf_obj_child</a><code>(3), <a href="/docs/linux/man/3-hdf_read_string/">hdf_read_string</a></code>(3), <a href="/docs/linux/man/3-hdf_set_buf/">hdf_set_buf</a><code>(3), <a href="/docs/linux/man/3-hdf_register_fileload/">hdf_register_fileload</a></code>(3), <a href="/docs/linux/man/3-hdf_get_obj/">hdf_get_obj</a><code>(3), <a href="/docs/linux/man/3-hdf_get_attr/">hdf_get_attr</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_top/">hdf_obj_top</a><code>(3), <a href="/docs/linux/man/3-hdf_dump_format/">hdf_dump_format</a></code>(3), <a href="/docs/linux/man/3-hdf_destroy/">hdf_destroy</a><code>(3), <a href="/docs/linux/man/3-hdf_init/">hdf_init</a></code>(3), <a href="/docs/linux/man/3-hdf_obj_value/">hdf_obj_value</a><code>(3), <a href="/docs/linux/man/3-hdf_write_string/">hdf_write_string</a></code>(3), <a href="/docs/linux/man/3-hdf_set_valuevf/">hdf_set_valuevf</a><code>(3), <a href="/docs/linux/man/3-hdf_sort_obj/">hdf_sort_obj</a></code>(3), <a href="/docs/linux/man/3-hdf_write_file_atomic/">hdf_write_file_atomic</a><code>(3), <a href="/docs/linux/man/3-hdf_obj_attr/">hdf_obj_attr</a></code>(3), <a href="/docs/linux/man/3-hdf_set_valuef/">hdf_set_valuef</a><code>(3), <a href="/docs/linux/man/3-hdf_get_copy/">hdf_get_copy</a></code>(3), <a href="/docs/linux/man/3-hdf_write_file/">hdf_write_file</a><code>(3), <a href="/docs/linux/man/3-hdf_get_valuevf/">hdf_get_valuevf</a></code>(3), hdf_remove_tree </p>
<h2>Index</h2>
