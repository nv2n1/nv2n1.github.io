---
title: "qbhdb-h(3)"
name: "qbhdb-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbhdb-h/"
description: "qbhdb.h –"
---

<p>qbhdb.h &#8211; </p>
<p> The handle database is for reference counting objects.</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;stdlib.h&gt;

#include &lt;stdint.h&gt;

#include &lt;inttypes.h&gt;

#include &lt;qb/qbarray.h&gt;</code></pre>
<h3>Data Structures</h3>
<p>struct qb_hdb_handle</p>
<p>struct qb_hdb</p>
<p>Macros<br />
#define _GNU_SOURCE</p>
<p>#define QB_HDB_D_FORMAT   &#8216;%&#8217; PRIu64</p>
<p>#define QB_HDB_X_FORMAT   &#8216;%&#8217; PRIx64</p>
<p>#define QB_HDB_DECLARE(database_name, destructor_function)</p>
<p>Convience macro for declaring a file scoped handle database.</p>
<p>Typedefs<br />
 typedef uint64_t <code>qb_handle_t</code><br />
 <i>Generic handle type is 64 bits. </i></p>
<h3>Functions</h3>
<pre><code>void qb_hdb_create (struct qb_hdb *hdb)


Create a new database.


void qb_hdb_destroy (struct qb_hdb *hdb)


Destroy a handle database.


int32_t qb_hdb_handle_create (struct qb_hdb *hdb, int32_t instance_size, qb_handle_t *handle_id_out)


Create a new handle.


int32_t qb_hdb_handle_get (struct qb_hdb *hdb, qb_handle_t handle_in, void **instance)


Get the instance associated with this handle and increase it's refcount.


int32_t qb_hdb_handle_get_always (struct qb_hdb *hdb, qb_handle_t handle_in, void **instance)


Get the instance associated with this handle and increase it's refcount.


int32_t qb_hdb_handle_put (struct qb_hdb *hdb, qb_handle_t handle_in)


Put the instance associated with this handle and decrease it's refcount.


int32_t qb_hdb_handle_destroy (struct qb_hdb *hdb, qb_handle_t handle_in)


Request the destruction of the object.


int32_t qb_hdb_handle_refcount_get (struct qb_hdb *hdb, qb_handle_t handle_in)


Get the current refcount.


void qb_hdb_iterator_reset (struct qb_hdb *hdb)


Reset the iterator.


int32_t qb_hdb_iterator_next (struct qb_hdb *hdb, void **instance, qb_handle_t *handle)


Get the next object and increament it's refcount.


uint32_t qb_hdb_base_convert (qb_handle_t handle)



uint64_t qb_hdb_nocheck_convert (uint32_t handle)</code></pre>
<h2>Detailed Description</h2>
<p>The handle database is for reference counting objects.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define _GNU_SOURCE</h3>
<h3>#define QB_HDB_D_FORMAT &#8216;%&#8217; PRIu64</h3>
<h3>#define QB_HDB_DECLARE(database_name, destructor_function)</h3>
<p><code>Value:</code> </p>
<pre>static struct qb_hdb (database_name) = { .handle_count = 0, .handles = NULL, .iterator = 0, .destructor = destructor_function, .first_run = QB_TRUE }; </pre>
<p>Convience macro for declaring a file scoped handle database. </p>
<pre>* QB_HDB_DECLARE(my_handle_database, NULL);
* </pre>
<p>&nbsp;<wbr></p>
<h3>#define QB_HDB_X_FORMAT &#8216;%&#8217; PRIx64</h3>
<h2>Typedef Documentation</h2>
<h3>typedef uint64_t <code>qb_handle_t</code></h3>
<p>Generic handle type is 64 bits.</p>
<h2>Function Documentation</h2>
<h3>uint32_t qb_hdb_base_convert (<code>qb_handle_t</code>handle)</h3>
<h3>void qb_hdb_create (struct <code>qb_hdb</code> *hdb)</h3>
<p>Create a new database. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>hdb</i> the database to init.</dl>
<h3>void qb_hdb_destroy (struct <code>qb_hdb</code> *hdb)</h3>
<p>Destroy a handle database. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>hdb</i> the database to destroy.</dl>
<h3>int32_t qb_hdb_handle_create (struct <code>qb_hdb</code> *hdb, int32_tinstance_size, <code>qb_handle_t</code> *handle_id_out)</h3>
<p>Create a new handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>hdb</i> the database instance<br />
 <i>instance_size</i> size of the object to malloc<br />
 <i>handle_id_out</i> new handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(0 == ok, -errno faliure)</dl>
<h3>int32_t qb_hdb_handle_destroy (struct <code>qb_hdb</code> *hdb, <code>qb_handle_t</code>handle_in)</h3>
<p>Request the destruction of the object. When the refcount is 0, it will be destroyed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>handle_in</i> the handle<br />
 <i>hdb</i> the database instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(0 == ok, -errno faliure)</dl>
<h3>int32_t qb_hdb_handle_get (struct <code>qb_hdb</code> *hdb, <code>qb_handle_t</code>handle_in, void **instance)</h3>
<p>Get the instance associated with this handle and increase it&#8217;s refcount. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>handle_in</i> the handle<br />
 <i>hdb</i> the database instance<br />
 <i>instance</i> (out) pointer to the desired object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(0 == ok, -errno faliure)</dl>
<h3>int32_t qb_hdb_handle_get_always (struct <code>qb_hdb</code> *hdb, <code>qb_handle_t</code>handle_in, void **instance)</h3>
<p>Get the instance associated with this handle and increase it&#8217;s refcount. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>handle_in</i> the handle<br />
 <i>hdb</i> the database instance<br />
 <i>instance</i> (out) pointer to the desired object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(0 == ok, -errno faliure)</dl>
<h3>int32_t qb_hdb_handle_put (struct <code>qb_hdb</code> *hdb, <code>qb_handle_t</code>handle_in)</h3>
<p>Put the instance associated with this handle and decrease it&#8217;s refcount. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>handle_in</i> the handle<br />
 <i>hdb</i> the database instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(0 == ok, -errno faliure)</dl>
<h3>int32_t qb_hdb_handle_refcount_get (struct <code>qb_hdb</code> *hdb, <code>qb_handle_t</code>handle_in)</h3>
<p>Get the current refcount. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>handle_in</i> the handle<br />
 <i>hdb</i> the database instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(&gt;= 0 is the refcount, -errno faliure)</dl>
<h3>int32_t qb_hdb_iterator_next (struct <code>qb_hdb</code> *hdb, void **instance, <code>qb_handle_t</code> *handle)</h3>
<p>Get the next object and increament it&#8217;s refcount. Remember to call <code>qb_hdb_handle_put()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>hdb</i> the database instance<br />
 <i>handle</i> (out) the handle<br />
 <i>instance</i> (out) pointer to the desired object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(0 == ok, -errno faliure)</dl>
<h3>void qb_hdb_iterator_reset (struct <code>qb_hdb</code> *hdb)</h3>
<p>Reset the iterator. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>hdb</i> the database instance</dl>
<h3>uint64_t qb_hdb_nocheck_convert (uint32_thandle)</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
