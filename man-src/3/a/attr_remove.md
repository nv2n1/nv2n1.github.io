---

title: "attr_remove(3)"
name: "attr_remove"
section: "3"
letter: "a"
url: "/docs/linux/man/3-attr_remove/"
description: "attr_remove, attr_removef – remove a user attribute of a filesystem object"
---

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
<dt>ATTR_ROOT</dt>
<dd> Look for <i>attrname</i> in the <code>root</code> address space, not in the <code>user</code> address space. (limited to use by super-user only)</dd>
<dt>ATTR_DONTFOLLOW</dt>
<dd> Do not follow symbolic links when resolving a <i>path</i> on an <code>attr_remove</code> function call. The default is to follow symbolic links.</dd></dl>
<p> <code>attr_remove</code> will fail if one or more of the following are true:</p>
<dl>
<dt>[ENOATTR]</dt>
<dd> The attribute name given is not associated with the indicated filesystem object.</dd>
<dt>[ENOENT]</dt>
<dd> The named file does not exist.</dd>
<dt>[EPERM]</dt>
<dd> The effective user ID does not match the owner of the file and the effective user ID is not super-user.</dd>
<dt>[ENOTDIR]</dt>
<dd> A component of the path prefix is not a directory.</dd>
<dt>[EACCES]</dt>
<dd> Search permission is denied on a component of the path prefix.</dd>
<dt>[EINVAL]</dt>
<dd> A bit was set in the <i>flag</i> argument that is not defined for this system call.</dd>
<dt>[EFAULT]</dt>
<dd> <i>Path</i> points outside the allocated address space of the process.</dd>
<dt>[ELOOP]</dt>
<dd> A path name lookup involved too many symbolic links.</dd>
<dt>[ENAMETOOLONG]</dt>
<dd> The length of <i>path</i> exceeds {<i>MAXPATHLEN</i>},  or a pathname component is longer than {<i>MAXNAMELEN</i>}. </dd></dl>
<p> <code>attr_removef</code> will fail if:</p>
<dl>
<dt>[ENOATTR]</dt>
<dd> The attribute name given is not associated with the indicated filesystem object.</dd>
<dt>[EINVAL]</dt>
<dd> A bit was set in the <i>flag</i> argument that is not defined for this system call, or <i>fd</i> refers to a socket, not a file.</dd>
<dt>[EFAULT]</dt>
<dd> <i>Attrname</i> points outside the allocated address space of the process.</dd>
<dt>[EBADF]</dt>
<dd> <i>Fd</i> does not refer to a valid descriptor.</dd></dl>
<h2>DIAGNOSTICS</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-attr/">attr</a></code>(1), <code><a href="/docs/linux/man/3-attr_get/">attr_get</a></code>(3), <code><a href="/docs/linux/man/3-attr_list/">attr_list</a></code>(3), <code><a href="/docs/linux/man/3-attr_multi/">attr_multi</a></code>(3), and <code><a href="/docs/linux/man/3-attr_set/">attr_set</a></code>(3). </p>
