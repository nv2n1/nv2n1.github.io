---
title: "attr_list(3)"
name: "attr_list"
section: "3"
letter: "a"
url: "/docs/linux/man/3-attr_list/"
description: "attr_list, attr_listf – list the names of the user attributes of a filesystem object"
---

<h2>NAME</h2>
<p> attr_list, attr_listf &#8211; list the names of the user attributes of a filesystem object</p>
<h2>C SYNOPSIS</h2>
<pre><code>
#include &lt;sys/attributes.h&gt;
int attr_list(const char *path, char *buffer,
              const int buffersize, int flags,
              attrlist_cursor_t *cursor);
int attr_listf(int fd, char *buffer,
               const int buffersize, int flags,
               attrlist_cursor_t *cursor);
[</code></pre>
<h2>DESCRIPTION</h2>
<p> ] The <code>attr_list</code> and <code>attr_listf</code> functions provide a way to list the existing attributes of a filesystem object. </p>
<p> <i>Path</i> points to a path name for a filesystem object, and <i>fd</i> refers to the file descriptor associated with a file. The <i>buffer</i> will be filled with a structure describing at least a portion of the attributes associated with the given filesystem object. <i>Buffer</i> will be overwritten with an <tt>attrlist_t</tt> structure containing a list of the attributes associated with that filesystem object, up to a maximum of <i>buffersize</i> bytes. The <i>buffer</i> must be sufficiently large to hold the appropriate data structures plus at least one maximally sized attribute name, but cannot be more than ATTR_MAX_VALUELEN (currently 64KB) bytes in length. </p>
<p> [c p a] The contents of an <tt>attrlist_t</tt> structure include the following members: </p>
<dl>
<dt>
<dd>
<p>__int32_t al_count;     /* number of entries in attrlist */<br />
__int32_t al_more;      /* T/F: more attrs (do syscall again) */<br />
__int32_t al_offset[1]; /* byte offsets of attrs [var-sized] */
</dl>
<p> The <i>al_count</i> field shows the number of attributes represented in this buffer, which is also the number of elements in the <i>al_offset</i> array. The <i>al_more</i> field will be non-zero if another <code>attr_list</code> call would result in more attributes. The <i>al_offset</i> array contains the byte offset within the <i>buffer</i> of the structure describing each of the attributes, an <tt>attrlist_ent_t</tt> structure. The <tt>ATTR_ENTRY(buffer, index)</tt> macro will help with decoding the list. It takes a pointer to the <i>buffer</i> and an <i>index</i> into the <i>al_offset</i> array and returns a pointer to the corresponding <tt>attrlist_ent_t</tt> structure. </p>
<p> The contents of an <tt>attrlist_ent_t</tt> structure include the following members: </p>
<dl>
<dt>
<dd>
<pre><code>

u_int32_t a_valuelen; /* number bytes in value of attr */
char a_name[];        /* attr name (NULL terminated) */
</code></pre>
<p> [</dl>
<p> ] </p>
<p> The <i>a_valuelen</i> field shows the size in bytes of the value associated with the attribute whose name is stored in the <i>a_name</i> field. The name is a NULL terminated string. </p>
<p> Note that the value of the attribute cannot be obtained through this interface, the <code>attr_get</code> call should be used to get the value. The <code>attr_list</code> interface tells the calling process how large of a buffer it must have in order to get the attribute&#8217;s value. </p>
<p> The <i>flags</i> argument can contain the following symbols bitwise OR&#8217;ed together:</p>
<dl>
<dt><font SIZE="-1">ATTR_ROOT</font></p>
<dd> List the attributes that are in the <code>root</code> address space, not in the <code>user</code> address space. (limited to use by super-user only)</p>
<dt><font SIZE="-1">ATTR_DONTFOLLOW</font></p>
<dd> Do not follow symbolic links when resolving a <i>path</i> on an <code>attr_list</code> function call. The default is to follow symbolic links.</dl>
<p> The <i>cursor</i> argument is a pointer to an opaque data structure that the kernel uses to track the calling process&#8217;s position in the attribute list. The only valid operations on a <i>cursor</i> are to pass it into an <code>attr_list</code> function call or to zero it out. It should be zero&#8217;ed out before the first <code>attr_list</code> call. Note that multi-threaded applications may keep more than one <i>cursor</i> in order to serve multiple contexts, ie: the <code>attr_list</code> call is &quot;thread-safe&quot;. </p>
<p> <code>attr_list</code> will fail if one or more of the following are true:</p>
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
<dd> A bit was set in the <i>flag</i> argument that is not defined for this system call, or the buffer was too small or too large.</p>
<dt><font SIZE="-1">[EFAULT]</font></p>
<dd> Either <i>Path</i> or <i>buffer</i> points outside the allocated address space of the process, or <i>buffer</i> or <i>bufsize</i> are not 32bit aligned.</p>
<dt><font SIZE="-1">[ELOOP]</font></p>
<dd> A path name lookup involved too many symbolic links.</p>
<dt><font SIZE="-1">[ENAMETOOLONG]</font></p>
<dd> The length of <i>path</i> exceeds <font SIZE="-1">{<i>MAXPATHLEN</i>}, </font> or a pathname component is longer than <font SIZE="-1">{<i>MAXNAMELEN</i>}. </font></p>
<dt><font SIZE="-1">[ENOATTR]</font></p>
<dd> <i>attribute</i> does not exist for this file.</dl>
<p> <code>attr_listf</code> will fail if:</p>
<dl>
<dt><font SIZE="-1">[EINVAL]</font></p>
<dd> A bit was set in the <i>flag</i> argument that is not defined for this system call, or <i>fd</i> refers to a socket, not a file, or the buffer was too small or too large.</p>
<dt><font SIZE="-1">[EFAULT]</font></p>
<dd> Either <i>Path</i> or <i>buffer</i> points outside the allocated address space of the process, or <i>buffer</i> or <i>bufsize</i> are not 32bit aligned.</p>
<dt><font SIZE="-1">[EBADF]</font></p>
<dd> <i>Fd</i> does not refer to a valid descriptor.</dl>
<h2>DIAGNOSTICS</h2>
<p> Upon successful completion, a value of 0 is returned. Otherwise, a value of -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-attr/">attr</a></code>(1), <code><a href="/docs/linux/man/3-attr_multi/">attr_multi</a></code>(3), <code><a href="/docs/linux/man/3-attr_remove/">attr_remove</a></code>(3), and <code><a href="/docs/linux/man/3-attr_set/">attr_set</a></code>(3). </p>
<h2>Index</h2>
