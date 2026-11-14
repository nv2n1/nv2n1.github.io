---
title: "dmlite_replica(3)"
name: "dmlite_replica"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmlite_replica/"
description: "dmlite_replica –"
---

<h2 class="name">NAME</h2>
<p> dmlite_replica &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;inode.h&gt;</p>
<h3>Data Fields</h3>
<p> int64_t <code>replicaid</code> </p>
<p> int64_t <code>fileid</code> </p>
<p> int64_t <code>nbaccesses</code> </p>
<p> time_t <code>atime</code> </p>
<p> time_t <code>ptime</code> </p>
<p> time_t <code>ltime</code> </p>
<p> enum <code>dmlite_replica_status</code> <code>status</code> </p>
<p> enum <code>dmlite_replica_type</code> <code>type</code> </p>
<p> char <code>server</code> [<code>HOST_NAME_MAX</code>] </p>
<p> char <code>rfn</code> [<code>URL_MAX</code>] </p>
<p> <code>dmlite_any_dict</code> * <code>extra</code><br />
 <i>If != NULL, additional metadata will be put here. </i></p>
<h2>Detailed Description</h2>
<p> A replica of a file</p>
<h2>Field Documentation</h2>
<h3>time_t atime</h3>
<h3><code>dmlite_any_dict</code>* extra</h3>
<p> If != NULL, additional metadata will be put here. Caller is generally responsible for allocating and freeing. Exception: when an array is allocated by the called method</p>
<h3>int64_t fileid</h3>
<h3>time_t ltime</h3>
<h3>int64_t nbaccesses</h3>
<h3>time_t ptime</h3>
<h3>int64_t replicaid</h3>
<h3>char rfn[<code>URL_MAX</code>]</h3>
<h3>char server[<code>HOST_NAME_MAX</code>]</h3>
<h3>enum <code>dmlite_replica_status</code> status</h3>
<h3>enum <code>dmlite_replica_type</code> type</h3>
<h2>Author</h2>
<p> Generated automatically by Doxygen for dmlite from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAR">Author</a></p>
<dd></dl>
