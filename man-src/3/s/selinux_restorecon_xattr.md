---
title: "selinux_restorecon_xattr(3)"
name: "selinux_restorecon_xattr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_restorecon_xattr/"
description: "selinux_restorecon_xattr – manage default security.sehash extended attribute entries added by"
---

<p>selinux_restorecon_xattr &#8211; manage default <i>security.sehash</i> extended attribute entries added by <code></p>
<p> <a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3), <code><a href="/docs/linux/man/8-setfiles/">setfiles</a></code>(8) or <code><a href="/docs/linux/man/8-restorecon/">restorecon</a></code>(8). </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/restorecon.h&gt;
int selinux_restorecon_xattr(const char *pathname,

                             unsigned int xattr_flags,

                             struct dir_xattr ***xattr_list);</code></pre>
<h2>Description</h2>
<p><code>selinux_restorecon_xattr</code>() returns a linked list of <code>dir_xattr</code> structures containing information described below based on:</p>
<dl>
<dd><i>pathname</i> containing a directory tree to be searched for <i>security.sehash</i> extended attribute entries. <i>xattr_flags</i> contains options as follows:  <code>SELINUX_RESTORECON_XATTR_RECURSE</code> recursively descend directories. <code>SELINUX_RESTORECON_XATTR_DELETE_NONMATCH_DIGESTS</code> delete non-matching digests from each directory in <i>pathname</i>. <code>SELINUX_RESTORECON_XATTR_DELETE_ALL_DIGESTS</code> delete all digests from each directory in <i>pathname</i>. <code>SELINUX_RESTORECON_XATTR_IGNORE_MOUNTS</code> do not read <code>/proc/mounts</code> to obtain a list of non-seclabel mounts to be excluded from the search.<br />
 Setting <code>SELINUX_RESTORECON_XATTR_IGNORE_MOUNTS</code> is useful where there is a non-seclabel fs mounted with a seclabel fs mounted on a directory below this.</dl>
<p> <i>xattr_list</i> is the returned pointer to a linked list of <code>dir_xattr</code> structures, each containing the following information: </p>
<pre><code>struct dir_xattr {
    char *directory;
    char *digest; /* Printable hex encoded string */
    enum digest_result result;
    struct dir_xattr *next;
};</code></pre>
<p> The <code>result</code> entry is enumerated as follows:</p>
<dl>
<dd>
<pre>enum digest_result {
 MATCH = 0,
 NOMATCH,
 DELETED_MATCH,
 DELETED_NOMATCH,
 ERROR
};</pre>
</dl>
<p> <i>xattr_list</i> must be set to <code>NULL</code> before calling <code><a href="/docs/linux/man/3-selinux_restorecon_xattr/">selinux_restorecon_xattr</a></code>(3). The caller is responsible for freeing the returned <i>xattr_list</i> entries in the linked list.</dl>
<p> See the <code>NOTES</code> section for more information. </p>
<h2>Return Value</h2>
<p>On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately. </p>
<h2>Notes</h2>
<dl>
<dt>1.</p>
<dd>By default <code><a href="/docs/linux/man/3-selinux_restorecon_xattr/">selinux_restorecon_xattr</a></code>(3) will use the default set of specfiles described in <code><a href="/docs/linux/man/5-files_contexts/">files_contexts</a></code>(5) to calculate the SHA1 digests to be used for comparison. To change this default behavior <code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3) must be called specifying the required <code>SELABEL_OPT_PATH</code> and setting the <code>SELABEL_OPT_DIGEST</code> option to a non-NULL value. <code><a href="/docs/linux/man/3-selinux_restorecon_set_sehandle/">selinux_restorecon_set_sehandle</a></code>(3) is then called to set the handle to be used by <code><a href="/docs/linux/man/3-selinux_restorecon_xattr/">selinux_restorecon_xattr</a></code>(3).</p>
<dt>2.</p>
<dd>By default <code><a href="/docs/linux/man/3-selinux_restorecon_xattr/">selinux_restorecon_xattr</a></code>(3) reads <code>/proc/mounts</code> to obtain a list of non-seclabel mounts to be excluded from searches unless the <code>SELINUX_RESTORECON_XATTR_IGNORE_MOUNTS</code> flag has been set.</p>
<dt>3.</p>
<dd><code>RAMFS</code> and <code>TMPFS</code> filesystems do not support the <i>security.sehash</i> extended attribute and are automatically excluded from searches.</p>
<dt>4.</p>
<dd>By default <code>stderr</code> is used to log output messages and errors. This may be changed by calling <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3) with the <code>SELINUX_CB_LOG</code> <i>type</i> option. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_sehandle/">selinux_restorecon_set_sehandle</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_default_handle/">selinux_restorecon_default_handle</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_exclude_list/">selinux_restorecon_set_exclude_list</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_alt_rootpath/">selinux_restorecon_set_alt_rootpath</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3) </p>
