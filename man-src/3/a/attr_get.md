---
title: "attr_get(3)"
name: "attr_get"
section: "3"
letter: "a"
url: "/docs/linux/man/3-attr_get/"
description: "attr_get, attr_getf – get the value of a user attribute of a filesystem object"
---

<h2>NAME</h2>
<p> attr_get, attr_getf &#8211; get the value of a user attribute of a filesystem object</p>
<h2>C SYNOPSIS</h2>
<pre><code>
#include &lt;attr/attributes.h&gt;
int attr_get(const char *path, const char *attrname,
             char *attrvalue, int *valuelength, int flags);
int attr_getf(int fd, const char *attrname,
              char *attrvalue, int *valuelength, int flags);
[</code></pre>
<h2>DESCRIPTION</h2>
<p> ] The <code>attr_get</code> and <code>attr_getf</code> functions provide a way to retrieve the value of an attribute. </p>
<p> <i>Path</i> points to a path name for a filesystem object, and <i>fd</i> refers to the file descriptor associated with a file. If the attribute <i>attrname</i> exists, the value associated with it will be copied into the <i>attrvalue</i> buffer. The <i>valuelength</i> argument is an input/output argument that on the call to <code>attr_get</code> should contain the maximum size of attribute value the process is willing to accept. On return, the <i>valuelength</i> will have been modified to show the actual size of the attribute value returned. The <i>flags</i> argument can contain the following symbols bitwise OR&#8217;ed together:</p>
<dl>
<dt><font SIZE="-1">ATTR_ROOT</font></p>
<dd> Look for <i>attrname</i> in the <code>root</code> address space, not in the <code>user</code> address space. (limited to use by super-user only)</p>
<dt><font SIZE="-1">ATTR_DONTFOLLOW</font></p>
<dd> Do not follow symbolic links when resolving a <i>path</i> on an <code>attr_get</code> function call. The default is to follow symbolic links.</dl>
<p> <code>attr_get</code> will fail if one or more of the following are true:</p>
<dl>
<dt><font SIZE="-1">[ENOATTR]</font></p>
<dd> The attribute name given is not associated with the indicated filesystem object.</p>
<dt><font SIZE="-1">[E2BIG]</font></p>
<dd> The value of the given attribute is too large to fit into the buffer. The integer that the <i>valuelength</i> argument points to has been modified to show the actual number of bytes that would be required to store the value of that attribute.</p>
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
<dd> <i>Path,</i> <i>attrname,</i> <i>attrvalue,</i> or <i>valuelength</i> points outside the allocated address space of the process.</p>
<dt><font SIZE="-1">[ELOOP]</font></p>
<dd> A path name lookup involved too many symbolic links.</p>
<dt><font SIZE="-1">[ENAMETOOLONG]</font></p>
<dd> The length of <i>path</i> exceeds <font SIZE="-1">{<i>MAXPATHLEN</i>}, </font> or a pathname component is longer than <font SIZE="-1">{<i>MAXNAMELEN</i>}. </font></dl>
<p> <code>attr_getf</code> will fail if:</p>
<dl>
<dt><font SIZE="-1">[ENOATTR]</font></p>
<dd> The attribute name given is not associated with the indicated filesystem object.</p>
<dt><font SIZE="-1">[E2BIG]</font></p>
<dd> The value of the given attribute is too large to fit into the buffer. The integer that the <i>valuelength</i> argument points to has been modified to show the actual numnber of bytes that would be required to store the value of that attribute.</p>
<dt><font SIZE="-1">[EINVAL]</font></p>
<dd> A bit was set in the <i>flag</i> argument that is not defined for this system call, or <i>fd</i> refers to a socket, not a file.</p>
<dt><font SIZE="-1">[EFAULT]</font></p>
<dd> <i>Attrname,</i> <i>attrvalue,</i> or <i>valuelength</i> points outside the allocated address space of the process.</p>
<dt><font SIZE="-1">[EBADF]</font></p>
<dd> <i>Fd</i> does not refer to a valid descriptor.</dl>
<h2>DIAGNOSTICS</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-attr/">attr</a></code>(1), <code><a href="/docs/linux/man/3-attr_list/">attr_list</a></code>(3), <code><a href="/docs/linux/man/3-attr_multi/">attr_multi</a></code>(3), <code><a href="/docs/linux/man/3-attr_remove/">attr_remove</a></code>(3), and <code><a href="/docs/linux/man/3-attr_set/">attr_set</a></code>(3). </p>
<h2>Index</h2>
