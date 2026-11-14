---
title: "pool-h(3)"
name: "pool-h"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pool-h/"
description: "pool.h –"
---

<p>pool.h &#8211; </p>
<p> C wrapper for DMLite Pool API.</p>
<h2>Synopsis</h2>
<pre><code>
#include 'dmlite.h'

#include 'any.h'

#include 'inode.h'

#include 'utils.h'</code></pre>
<h3>Data Structures</h3>
<pre><code>struct dmlite_pool


Pool data.


struct dmlite_chunk


Chunk of data.


struct dmlite_location


Collection of chunks that form a replica.



Macros
#define POOL_TYPE_MAX   16



#define POOL_MAX   16



Typedefs</code></pre>
<p> typedef struct <code>dmlite_pool</code> <code>dmlite_pool</code><br />
 <i>Pool data. </i><br />
 typedef struct <code>dmlite_chunk</code> <code>dmlite_chunk</code><br />
 <i>Chunk of data. </i><br />
 typedef struct <code>dmlite_location</code> <code>dmlite_location</code><br />
 <i>Collection of chunks that form a replica. </i></p>
<h3>Functions</h3>
<p>int <code>dmlite_getpools</code> (<code>dmlite_context</code> *context, unsigned *nPools, <code>dmlite_pool</code> **pools)<br />
 <i>Gets the list of pools. </i><br />
 int <code>dmlite_pools_free</code> (unsigned nPools, <code>dmlite_pool</code> *pools)<br />
 <i>Frees an array of pools. </i><br />
 <code>dmlite_location</code> * <code>dmlite_get</code> (<code>dmlite_context</code> *context, const char *path)<br />
 <i>Gets a single replica (synchronous). </i><br />
 <code>dmlite_location</code> * <code>dmlite_iget</code> (<code>dmlite_context</code> *context, ino_t inode)<br />
 <i>Gets a single replica (synchronous). </i><br />
 <code>dmlite_location</code> * <code>dmlite_getlocation</code> (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)<br />
 <i>Gets the location of a replica. </i><br />
 <code>dmlite_location</code> * <code>dmlite_put</code> (<code>dmlite_context</code> *context, const char *path)<br />
 <i>Puts a file (synchronous). </i><br />
 int <code>dmlite_put_abort</code> (<code>dmlite_context</code> *context, const <code>dmlite_location</code> *loc)<br />
 <i>Aborts a put request. </i><br />
 int <code>dmlite_location_free</code> (<code>dmlite_location</code> *loc)<br />
 <i>Frees a location struct. </i><br />
 int <code>dmlite_getdirspaces</code> (<code>dmlite_context</code> *context, const char *logicaldir, int64_t *freespace, int64_t *used)<br />
 <i>Get the estimation of the free/used space for writing into a directory. </i></p>
<h2>Detailed Description</h2>
<p>C wrapper for DMLite Pool API. </p>
<p> <code>Author:</code></p>
<dl>
<dd>Alejandro Álvarez Ayllon aalvarez [at] cern.ch</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define POOL_MAX 16</h3>
<h3>#define POOL_TYPE_MAX 16</h3>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>dmlite_chunk</code> <code>dmlite_chunk</code></h3>
<p>Chunk of data.</p>
<h3>typedef struct <code>dmlite_location</code> <code>dmlite_location</code></h3>
<p>Collection of chunks that form a replica. On read, there may be duplicated chunks.</p>
<h3>typedef struct <code>dmlite_pool</code> <code>dmlite_pool</code></h3>
<p>Pool data.</p>
<h2>Function Documentation</h2>
<h3><code>dmlite_location</code>* dmlite_get (<code>dmlite_context</code> *context, const char *path)</h3>
<p>Gets a single replica (synchronous). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical file name.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A pointer to a <code>dmlite_location</code> struct, or NULL on error.</dl>
<h3>int dmlite_getdirspaces (<code>dmlite_context</code> *context, const char *logicaldir, int64_t *freespace, int64_t *used)</h3>
<p>Get the estimation of the free/used space for writing into a directory. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>path</i> The path of the directory to query<br />
 <i>totalfree</i> The total number of free bytes (may not be contiguous)<br />
 <i>used</i> The total number of used bytes</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success, error code otherwise.</dl>
<h3><code>dmlite_location</code>* dmlite_getlocation (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)</h3>
<p>Gets the location of a replica. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The DM context.<br />
 <i>replica</i> The replica to translate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A pointer to a <code>dmlite_location</code> struct, or NULL on error.</dl>
<h3>int dmlite_getpools (<code>dmlite_context</code> *context, unsigned *nPools, <code>dmlite_pool</code> **pools)</h3>
<p>Gets the list of pools. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The DM context.<br />
 <i>nPools</i> The number of pools.<br />
 <i>pools</i> An array with the pools. <code>Use dmlite_freepools to free</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success, error code otherwise.</dl>
<h3><code>dmlite_location</code>* dmlite_iget (<code>dmlite_context</code> *context, ino_tinode)</h3>
<p>Gets a single replica (synchronous). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file inode.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A pointer to a <code>dmlite_location</code> struct, or NULL on error.</dl>
<h3>int dmlite_location_free (<code>dmlite_location</code> *loc)</h3>
<p>Frees a location struct. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>loc</i> The struct to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_pools_free (unsignednPools, <code>dmlite_pool</code> *pools)</h3>
<p>Frees an array of pools. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>nPools</i> The number of pools in the array.<br />
 <i>pools</i> The array to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success, error code otherwise.</dl>
<h3><code>dmlite_location</code>* dmlite_put (<code>dmlite_context</code> *context, const char *path)</h3>
<p>Puts a file (synchronous). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical file name to put.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A pointer to a <code>dmlite_location</code> struct, or NULL on error.</dl>
<h3>int dmlite_put_abort (<code>dmlite_context</code> *context, const <code>dmlite_location</code> *loc)</h3>
<p>Aborts a put request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The DM context.<br />
 <i>loc</i> As returned by dmlite_put.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success, error code otherwise.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for dmlite from the source code.</p>
