---
title: "attr_remove(3)"
name: "attr_remove"
section: "3"
letter: "a"
url: "/docs/linux/man/3-attr_remove/"
description: "attr_remove, attr_removef – remove a user attribute of a filesystem object"
---

<h2>NAME</h2>
<p> attr_remove, attr_removef &#8211; remove a user attribute of a filesystem object</p>
<h2>C SYNOPSIS</h2>
<pre><code>
#include &lt;attr/attributes.h&gt;
int attr_remove(const char *path, const char *attrname, int flags);
int attr_removef(int fd, const char *attrname, int flags);
[</code></pre>
<h2>DESCRIPTION</h2>
<p> ] The <code>attr_remove</code> and <code>attr_removef</code> functions provide a way to remove previously created attributes from filesystem objects. </p>
<p> <i>Path</i> points to a path name for a filesystem object, and <i>fd</i> refers to the file descriptor associated with a file. If the attribute <i>attrname</i> exists, the attribute name and value will be removed from the fileystem object. The <i>flags</i> argument can contain the following symbols bitwise OR&#8217;ed together:</p>
<dl>
<dt><font SIZE="-1">ATTR_ROOT</font></p>
<dd> Look for <i>attrname</i> in the <code>root</code> address space, not in the <code>user</code> address space. (limited to use by super-user only)</p>
<dt><font SIZE="-1">ATTR_DONTFOLLOW</font></p>
<dd> Do not follow symbolic links when resolving a <i>path</i> on an <code>attr_remove</code> function call. The default is to follow symbolic links.</dl>
<p> <code>attr_remove</code> will fail if one or more of the following are true:</p>
<dl>
<dt><font SIZE="-1">[ENOATTR]</font></p>
<dd> The attribute name given is not associated with the indicated filesystem object.</p>
<dt><font SIZE="-1">[ENOENT]</font></p>
<dd> The named file does not exist.</p>
<dt><font SIZE="-1">[EPERM]</font></p>
<dd> The effective user <font SIZE="-1">ID</font> does not match the owner of the file and the effective user <font SIZE="-1">ID</font> is not super-user.</p>
<dt><font SIZE="-1">[ENOTDIR]</font></p>
<dd> A component of the path prefix is not a directory.</p>
<dt><font SIZE="-1">[EACCES]</font></p>
<dd> Search permission is denied on a component of the path prefix.</p>
<dt><font SIZE="-1">[EINVAL]</font></p>
<dd> A bit was set in the <i>flag</i> argument that is not defined for this system call.</p>
<dt><font SIZE="-1">[EFAULT]</font></p>
<dd> <i>Path</i> points outside the allocated address space of the process.</p>
<dt><font SIZE="-1">[ELOOP]</font></p>
<dd> A path name lookup involved too many symbolic links.</p>
<dt><font SIZE="-1">[ENAMETOOLONG]</font></p>
<dd> The length of <i>path</i> exceeds <font SIZE="-1">{<i>MAXPATHLEN</i>}, </font> or a pathname component is longer than <font SIZE="-1">{<i>MAXNAMELEN</i>}. </font></dl>
<p> <code>attr_removef</code> will fail if:</p>
<dl>
<dt><font SIZE="-1">[ENOATTR]</font></p>
<dd> The attribute name given is not associated with the indicated filesystem object.</p>
<dt><font SIZE="-1">[EINVAL]</font></p>
<dd> A bit was set in the <i>flag</i> argument that is not defined for this system call, or <i>fd</i> refers to a socket, not a file.</p>
<dt><font SIZE="-1">[EFAULT]</font></p>
<dd> <i>Attrname</i> points outside the allocated address space of the process.</p>
<dt><font SIZE="-1">[EBADF]</font></p>
<dd> <i>Fd</i> does not refer to a valid descriptor.</dl>
<h2>DIAGNOSTICS</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-attr/">attr</a></code>(1), <code><a href="/docs/linux/man/3-attr_get/">attr_get</a></code>(3), <code><a href="/docs/linux/man/3-attr_list/">attr_list</a></code>(3), <code><a href="/docs/linux/man/3-attr_multi/">attr_multi</a></code>(3), and <code><a href="/docs/linux/man/3-attr_set/">attr_set</a></code>(3). </p>
<h2>Index</h2>
