---
title: "tcl_access(3)"
name: "tcl_access"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_access/"
description: "Tcl_Access, Tcl_Stat – check file permissions and other attributes"
---

<p>Tcl_Access, Tcl_Stat &#8211; check file permissions and other attributes </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_Access</code>(<i>path</i>, <i>mode</i>)
int
<code>Tcl_Stat</code>(<i>path</i>, <i>statPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>char <i>*path</i> (in) Native name of the file to check the attributes of.</p>
<dd>int <i>mode</i> (in) Mask consisting of one or more of R_OK, W_OK, X_OK and F_OK. R_OK, W_OK and X_OK request checking whether the file exists and has read, write and execute permissions, respectively. F_OK just requests checking for the existence of the file.</p>
<dd>struct stat <i>*statPtr</i> (out) The structure that contains the result. </p>
</dl>
<h2>Description</h2>
<p>As of Tcl 8.4, the object-based APIs <code>Tcl_FSAccess</code> and <code>Tcl_FSStat</code> should be used in preference to <code>Tcl_Access</code> and <code>Tcl_Stat</code>, wherever possible. </p>
<p> There are two reasons for calling <code>Tcl_Access</code> and <code>Tcl_Stat</code> rather than calling system level functions <code>access</code> and <code>stat</code> directly. First, the Windows implementation of both functions fixes some bugs in the system level calls. Second, both <code>Tcl_Access</code> and <code>Tcl_Stat</code> (as well as <code>Tcl_OpenFileChannelProc</code>) hook into a linked list of functions. This allows the possibility to reroute file access to alternative media or access methods. </p>
<p> <code>Tcl_Access</code> checks whether the process would be allowed to read, write or test for existence of the file (or other file system object) whose name is pathname. If pathname is a symbolic link on Unix, then permissions of the file referred by this symbolic link are tested. </p>
<p> On success (all requested permissions granted), zero is returned. On error (at least one bit in mode asked for a permission that is denied, or some other error occurred), -1 is returned. </p>
<p> <code>Tcl_Stat</code> fills the stat structure <i>statPtr</i> with information about the specified file. You do not need any access rights to the file to get this information but you need search rights to all directories named in the path leading to the file. The stat structure includes info regarding device, inode (always 0 on Windows), privilege mode, nlink (always 1 on Windows), user id (always 0 on Windows), group id (always 0 on Windows), rdev (same as device on Windows), size, last access time, last modification time, and creation time. </p>
<p> If <i>path</i> exists, <code>Tcl_Stat</code> returns 0 and the stat structure is filled with data. Otherwise, -1 is returned, and no stat info is given. </p>
<h2>Keywords</h2>
<p>stat, access</p>
