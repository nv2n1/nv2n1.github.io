---
title: "qbarray-h(3)"
name: "qbarray-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbarray-h/"
description: "qbarray.h –"
---

<p>qbarray.h &#8211; </p>
<p> This is a dynamic array (it can grow, but without moving memory).</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;stdint.h&gt;

#include &lt;unistd.h&gt;

#include &lt;qb/qbdefs.h&gt;</code></pre>
<h3>Typedefs</h3>
<p>typedef struct qb_array <code>qb_array_t</code><br />
 <i>This is an opaque data type representing an instance of an array. </i><br />
 typedef void(* <code>qb_array_new_bin_cb_fn</code> )(<code>qb_array_t</code> *a, uint32_t bin)</p>
<h3>Functions</h3>
<p><code>qb_array_t</code> * <code>qb_array_create</code> (size_t max_elements, size_t element_size)<br />
 <i>Create an array with fixed sized elements. </i><br />
 <code>qb_array_t</code> * <code>qb_array_create_2</code> (size_t max_elements, size_t element_size, size_t autogrow_elements)<br />
 <i>Create an array with fixed sized elements. </i><br />
 int32_t <code>qb_array_index</code> (<code>qb_array_t</code> *a, int32_t idx, void **element_out)<br />
 <i>Get an element at a particular index. </i><br />
 int32_t <code>qb_array_grow</code> (<code>qb_array_t</code> *a, size_t max_elements)<br />
 <i>Grow the array. </i><br />
 size_t <code>qb_array_num_bins_get</code> (<code>qb_array_t</code> *a)<br />
 <i>Get the number of bins used or the array. </i><br />
 size_t <code>qb_array_elems_per_bin_get</code> (<code>qb_array_t</code> *a)<br />
 <i>Get the number of elements per bin. </i><br />
 int32_t <code>qb_array_new_bin_cb_set</code> (<code>qb_array_t</code> *a, <code>qb_array_new_bin_cb_fn</code> fn)<br />
 <i>Get a callback when a new bin is allocated. </i><br />
 void <code>qb_array_free</code> (<code>qb_array_t</code> *a)<br />
 <i>Free all the memory used by the array. </i></p>
<h2>Detailed Description</h2>
<p>This is a dynamic array (it can grow, but without moving memory). </p>
<pre>* arr = qb_array_create_2(64, sizeof(struct my_struct), 256);
* ...
* res = qb_array_index(arr, idx, (void**)&amp;my_ptr);
* if (res &lt; 0) {
* return res;
* }
* // use my_ptr, now even if there is a grow, this pointer will be valid.
* </pre>
<p>&nbsp;<wbr></p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* qb_array_new_bin_cb_fn)(<code>qb_array_t</code> *a, uint32_t bin)</h3>
<h3>typedef struct qb_array <code>qb_array_t</code></h3>
<p>This is an opaque data type representing an instance of an array.</p>
<h2>Function Documentation</h2>
<h3><code>qb_array_t</code>* qb_array_create (size_tmax_elements, size_telement_size)</h3>
<p>Create an array with fixed sized elements. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>max_elements</i> initial max elements.<br />
 <i>element_size</i> size of each element.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>array instance.</dl>
<h3><code>qb_array_t</code>* qb_array_create_2 (size_tmax_elements, size_telement_size, size_tautogrow_elements)</h3>
<p>Create an array with fixed sized elements. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>max_elements</i> initial max elements.<br />
 <i>element_size</i> size of each element.<br />
 <i>autogrow_elements</i> the number of elements to grow automatically by.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>array instance.</dl>
<h3>size_t qb_array_elems_per_bin_get (<code>qb_array_t</code> *a)</h3>
<p>Get the number of elements per bin.</p>
<h3>void qb_array_free (<code>qb_array_t</code> *a)</h3>
<p>Free all the memory used by the array. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>a</i> array instance.</dl>
<h3>int32_t qb_array_grow (<code>qb_array_t</code> *a, size_tmax_elements)</h3>
<p>Grow the array. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>a</i> array instance.<br />
 <i>max_elements</i> the new maximum size of the array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(0 == success, else -errno)</dl>
<h3>int32_t qb_array_index (<code>qb_array_t</code> *a, int32_tidx, void **element_out)</h3>
<p>Get an element at a particular index. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>a</i> array instance.<br />
 <i>idx</i> the index<br />
 <i>element_out</i> the pointer to the element data.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(0 == success, else -errno)</dl>
<h3>int32_t qb_array_new_bin_cb_set (<code>qb_array_t</code> *a, <code>qb_array_new_bin_cb_fn</code>fn)</h3>
<p>Get a callback when a new bin is allocated.</p>
<h3>size_t qb_array_num_bins_get (<code>qb_array_t</code> *a)</h3>
<p>Get the number of bins used or the array.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
