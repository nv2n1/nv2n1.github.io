---
title: "attr_multi(3)"
name: "attr_multi"
section: "3"
letter: "a"
url: "/docs/linux/man/3-attr_multi/"
description: "attr_multi, attr_multif – manipulate multiple user attributes on a filesystem object at once"
---

<h2>NAME</h2>
<p> attr_multi, attr_multif &#8211; manipulate multiple user attributes on a filesystem object at once</p>
<h2>C SYNOPSIS</h2>
<pre><code>
#include &lt;attr/attributes.h&gt;
int attr_multi(const char *path, attr_multiop_t *oplist,
               int count, int flags);
int attr_multif(int fd, attr_multiop_t *oplist,
                int count, int flags);
[</code></pre>
<h2>DESCRIPTION</h2>
<p> ] The <code>attr_multi</code> and <code>attr_multif</code> functions provide a way to operate on multiple attributes of a filesystem object at once. </p>
<p> <i>Path</i> points to a path name for a filesystem object, and <i>fd</i> refers to the file descriptor associated with a file. The <i>oplist</i> is an array of <tt>attr_multiop_t</tt> structures. Each element in that array describes a single attribute operation and provides all the information required to carry out that operation and to check for success or failure of that operation. <i>Count</i> tells how many elements are in the <i>oplist</i> array. </p>
<p> [c p a] The contents of an <tt>attr_multiop_t</tt> structure include the following members: </p>
<dl>
<dt>
<dd>
<pre><code>

int am_opcode;      /* which operation to perform (see below) */
int am_error;       /* [out arg] result of this sub-op (an errno) */
char *am_attrname;  /* attribute name to work with */
char *am_attrvalue; /* [in/out arg] attribute value (raw bytes) */
int am_length;      /* [in/out arg] length of value */
int am_flags;       /* flags (bit-wise OR of #defines below) */
</code></pre>
</dl>
<p> The <i>am_opcode</i> field defines how the remaining fields are to be interpreted and can take on one of the following values: </p>
<dl>
<dt>
<dd>
<pre>
<tt>
ATTR_OP_GET /* return the indicated attr's value */
ATTR_OP_SET /* set/create the indicated attr/value pair */
ATTR_OP_REMOVE /* remove the indicated attr */
</tt></pre>
</dl>
<p> The <i>am_error</i> field will contain the appropriate error result code if that sub-operation fails. The result codes for a given sub-operation are a subset of the result codes that are possible from the corresponding single-attribute function call. For example, the result code possible from an <tt>ATTR_OP_GET</tt> sub-operation are a subset of those that can be returned from an <code>attr_get</code> function call. </p>
<p> The <i>am_attrname</i> field is a pointer to a NULL terminated string giving the attribute name that the sub-operation should operate on. </p>
<p> The <i>am_attrvalue,</i> <i>am_length</i> and <i>am_flags</i> fields are used to store the value of the named attribute, and some control flags for that sub-operation, respectively. Their use varies depending on the value of the <i>am_opcode</i> field.</p>
<dl>
<dt><font SIZE="-1"><code>ATTR_OP_GET</code> </font></p>
<dd> The <i>am_attrvalue</i> field is a pointer to a empty buffer that will be overwritten with the value of the named attribute. The <i>am_length</i> field is initially the total size of the memory buffer that the <i>am_attrvalue</i> field points to. After the operation, the <i>am_length</i> field contains the actual size of the attribute&#8217;s value. The <i>am_flags</i> field may be set to the <tt>ATTR_ROOT</tt> flag. If the process has appropriate priviledges, the ROOT namespace will be searched for the named attribute, otherwise the USER namespace will be searched.</p>
<dt><font SIZE="-1"><code>ATTR_OP_SET</code> </font></p>
<dd> The <i>am_attrvalue</i> and <i>am_length</i> fields contain the new value for the given attribute name and its length. The <tt>ATTR_ROOT</tt> flag may be set in the <i>am_flags</i> field. If the process has appropriate priviledges, the ROOT namespace will be searched for the named attribute, otherwise the USER namespace will be searched. The <tt>ATTR_CREATE</tt> and the <tt>ATTR_REPLACE</tt> flags may also be set in the <i>am_flags</i> field (but not simultaneously). If the <tt>ATTR_CREATE</tt> flag is set, the sub-operation will set the <i>am_error</i> field to EEXIST if the named attribute already exists. If the <tt>ATTR_REPLACE</tt> flag is set, the sub-operation will set the <i>am_error</i> field to ENOATTR if the named attribute does not already exist. If neither of those two flags are set and the attribute does not exist, then the attribute will be created with the given value. If neither of those two flags are set and the attribute already exists, then the value will be replaced with the given value.</p>
<dt><font SIZE="-1"><code>ATTR_OP_REMOVE</code> </font></p>
<dd> The <i>am_attrvalue</i> and <i>am_length</i> fields are not used and are ignored. The <i>am_flags</i> field may be set to the <tt>ATTR_ROOT</tt> flag. If the process has appropriate priviledges, the ROOT namespace will be searched for the named attribute, otherwise the USER namespace will be searched.</dl>
<p> The <i>flags</i> argument to the <code>attr_multi</code> call is used to control following of symbolic links in the <i>path</i> argument. The default is to follow symbolic links, <i>flags</i> should be set to ATTR_DONTFOLLOW to not follow symbolic links. </p>
<p> <code>attr_multi</code> will fail if one or more of the following are true:</p>
<dl>
<dt><font SIZE="-1">[ENOENT]</font></p>
<dd> The named file does not exist.</p>
<dt><font SIZE="-1">[EPERM]</font></p>
<dd> The effective user <font SIZE="-1">ID</font> does not match the owner of the file and the effective user <font SIZE="-1">ID</font> is not super-user.</p>
<dt><font SIZE="-1">[ENOTDIR]</font></p>
<dd> A component of the path prefix is not a directory.</p>
<dt><font SIZE="-1">[EACCES]</font></p>
<dd> Search permission is denied on a component of the path prefix.</p>
<dt><font SIZE="-1">[EINVAL]</font></p>
<dd> A bit other than ATTR_DONTFOLLOW was set in the <i>flag</i> argument.</p>
<dt><font SIZE="-1">[EFAULT]</font></p>
<dd> <i>Path,</i> or <i>oplist</i> points outside the allocated address space of the process.</p>
<dt><font SIZE="-1">[ELOOP]</font></p>
<dd> A path name lookup involved too many symbolic links.</p>
<dt><font SIZE="-1">[ENAMETOOLONG]</font></p>
<dd> The length of <i>path</i> exceeds <font SIZE="-1">{<i>MAXPATHLEN</i>}, </font> or a pathname component is longer than <font SIZE="-1">{<i>MAXNAMELEN</i>}. </font></dl>
<p> <code>attr_multif</code> will fail if:</p>
<dl>
<dt><font SIZE="-1">[EINVAL]</font></p>
<dd> A bit was set in the <i>flag</i> argument, or <i>fd</i> refers to a socket, not a file.</p>
<dt><font SIZE="-1">[EFAULT]</font></p>
<dd> <i>Oplist</i> points outside the allocated address space of the process.</p>
<dt><font SIZE="-1">[EBADF]</font></p>
<dd> <i>Fd</i> does not refer to a valid descriptor.</dl>
<h2>DIAGNOSTICS</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately. Note that the individual operations listed in the <i>oplist</i> array each have their own error return fields. The <i>errno</i> variable only records the result of the <i>attr_multi</i> call itself, not the result of any of the sub-operations.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-attr/">attr</a></code>(1), <code><a href="/docs/linux/man/3-attr_get/">attr_get</a></code>(3), <code><a href="/docs/linux/man/3-attr_list/">attr_list</a></code>(3), <code><a href="/docs/linux/man/3-attr_remove/">attr_remove</a></code>(3), and <code><a href="/docs/linux/man/3-attr_set/">attr_set</a></code>(3). </p>
<h2>Index</h2>
