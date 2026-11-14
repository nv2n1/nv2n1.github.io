---
title: "dmlite_xstat(3)"
name: "dmlite_xstat"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmlite_xstat/"
description: "dmlite_xstat –"
---

<h2 class="name">NAME</h2>
<p> dmlite_xstat &#8211; </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;inode.h&gt;</p>
<h3>Data Fields</h3>
<p> ino_t <code>parent</code> </p>
<p> struct stat <code>stat</code> </p>
<p> enum <code>dmlite_file_status</code> <code>status</code> </p>
<p> char <code>name</code> [NAME_MAX] </p>
<p> char <code>guid</code> [<code>GUID_MAX</code>] </p>
<p> char <code>csumtype</code> [<code>CSUMTYPE_MAX</code>] </p>
<p> char <code>csumvalue</code> [<code>CSUMVALUE_MAX</code>] </p>
<p> char <code>acl</code> [<code>ACL_ENTRIES_MAX</code> *<code>ACL_SIZE</code>] </p>
<p> <code>dmlite_any_dict</code> * <code>extra</code><br />
 <i>If != NULL, additional metadata will be put here. </i></p>
<h2>Detailed Description</h2>
<p> File metadata</p>
<h2>Field Documentation</h2>
<h3>char acl[<code>ACL_ENTRIES_MAX</code> *<code>ACL_SIZE</code>]</h3>
<h3>char csumtype[<code>CSUMTYPE_MAX</code>]</h3>
<h3>char csumvalue[<code>CSUMVALUE_MAX</code>]</h3>
<h3><code>dmlite_any_dict</code>* extra</h3>
<p> If != NULL, additional metadata will be put here. Caller is responsible for allocating and freeing</p>
<h3>char guid[<code>GUID_MAX</code>]</h3>
<h3>char name[NAME_MAX]</h3>
<h3>ino_t parent</h3>
<h3>struct stat stat</h3>
<h3>enum <code>dmlite_file_status</code> status</h3>
<h2>Author</h2>
<p> Generated automatically by Doxygen for dmlite from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAP">Author</a></p>
<dd></dl>
