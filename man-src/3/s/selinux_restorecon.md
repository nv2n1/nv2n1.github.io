---
title: "selinux_restorecon(3)"
name: "selinux_restorecon"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_restorecon/"
description: "selinux_restorecon – restore file(s) default SELinux security contexts"
---

<p>selinux_restorecon &#8211; restore file(s) default SELinux security contexts</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/restorecon.h&gt;
int selinux_restorecon(const char *pathname,

                       unsigned int restorecon_flags);</code></pre>
<h2>Description</h2>
<p><code>selinux_restorecon</code>() restores file default security contexts on filesystems that support extended attributes (see <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7)), based on:</p>
<dl>
<dd><i>pathname</i> containing a directory or file to be relabeled.<br />
 If this is a directory and the <i>restorecon_flags</i> <code>SELINUX_RESTORECON_RECURSE</code> has been set (for descending through directories), then <code>selinux_restorecon</code>() will write an SHA1 digest of specfile entries calculated by <code><a href="/docs/linux/man/3-selabel_get_digests_all_partial_matches/">selabel_get_digests_all_partial_matches</a></code>(3) to an extended attribute of <i>security.sehash</i> once the relabeling has been completed successfully (see the <code>NOTES</code> section for details).<br />
 These digests will be checked should <code>selinux_restorecon</code>() be rerun with the <i>restorecon_flags</i> <code>SELINUX_RESTORECON_RECURSE</code> flag set. If any of the specfile entries had been updated, the digest will also be updated. However if the digest is the same, no relabeling checks will take place.<br />
 The <i>restorecon_flags</i> that can be used to manage the usage of the SHA1 digest are:</p>
<dl>
<dd><code>SELINUX_RESTORECON_SKIP_DIGEST</code><br />
 <code>SELINUX_RESTORECON_IGNORE_DIGEST</code></dl>
<p> <i>restorecon_flags</i> contains the labeling option/rules as follows:  <code>SELINUX_RESTORECON_SKIP_DIGEST</code> Do not check or update any extended attribute <i>security.sehash</i> entries. <code>SELINUX_RESTORECON_IGNORE_DIGEST</code> force the checking of labels even if the stored SHA1 digest matches the specfile entries SHA1 digest. The specfile entries digest will be written to the <i>security.sehash</i> extended attribute once relabeling has been completed successfully provided the <code>SELINUX_RESTORECON_NOCHANGE</code> flag has not been set. <code>SELINUX_RESTORECON_NOCHANGE</code> don&#8217;t change any file labels (passive check) or update the digest in the <i>security.sehash</i> extended attribute. <code>SELINUX_RESTORECON_SET_SPECFILE_CTX</code> If set, reset the files label to match the default specfile context. If not set only reset the files &quot;type&quot; component of the context to match the default specfile context. <code>SELINUX_RESTORECON_RECURSE</code> change file and directory labels recursively (descend directories) and if successful write an SHA1 digest of the specfile entries to an extended attribute as described in the <code>NOTES</code> section. <code>SELINUX_RESTORECON_VERBOSE</code> log file label changes.</p>
<dl>
<dd>Note that if <code>SELINUX_RESTORECON_VERBOSE</code> and <code>SELINUX_RESTORECON_PROGRESS</code> flags are set, then <code>SELINUX_RESTORECON_PROGRESS</code> will take precedence.</dl>
<p> <code>SELINUX_RESTORECON_PROGRESS</code> show progress by outputting the number of files in 1k blocks processed to stdout. If the <code>SELINUX_RESTORECON_MASS_RELABEL</code> flag is also set then the approximate percentage complete will be shown. <code>SELINUX_RESTORECON_MASS_RELABEL</code> generally set when relabeling the entire OS, that will then show the approximate percentage complete. The <code>SELINUX_RESTORECON_PROGRESS</code> flag must also be set. <code>SELINUX_RESTORECON_REALPATH</code> convert passed-in <i>pathname</i> to the canonical pathname using <code><a href="/docs/linux/man/3-realpath/">realpath</a></code>(3). <code>SELINUX_RESTORECON_XDEV</code> prevent descending into directories that have a different device number than the <i>pathname</i> entry from which the descent began. <code>SELINUX_RESTORECON_ADD_ASSOC</code> attempt to add an association between an inode and a specification. If there is already an association for the inode and it conflicts with the specification, then use the last matching specification. <code>SELINUX_RESTORECON_ABORT_ON_ERROR</code> abort on errors during the file tree walk. <code>SELINUX_RESTORECON_SYSLOG_CHANGES</code> log any label changes to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). <code>SELINUX_RESTORECON_LOG_MATCHES</code> log what specfile context matched each file. <code>SELINUX_RESTORECON_IGNORE_NOENTRY</code> ignore files that do not exist. <code>SELINUX_RESTORECON_IGNORE_MOUNTS</code> do not read <code>/proc/mounts</code> to obtain a list of non-seclabel mounts to be excluded from relabeling checks.<br />
 Setting <code>SELINUX_RESTORECON_IGNORE_MOUNTS</code> is useful where there is a non-seclabel fs mounted with a seclabel fs mounted on a directory below this.</dl>
<p> The behavior regarding the checking and updating of the SHA1 digest described above is the default behavior. It is possible to change this by first calling <code><a href="/docs/linux/man/3-selabel_open/">selabel_open</a></code>(3) and not enabling the <code>SELABEL_OPT_DIGEST</code> option, then calling <code><a href="/docs/linux/man/3-selinux_restorecon_set_sehandle/">selinux_restorecon_set_sehandle</a></code>(3) to set the handle to be used by <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3). If the <i>pathname</i> is a directory path, then it is possible to set directories to be excluded from the path by calling <code><a href="/docs/linux/man/3-selinux_restorecon_set_exclude_list/">selinux_restorecon_set_exclude_list</a></code>(3) with a <code>NULL</code> terminated list before calling <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3). By default <code><a href="/docs/linux/man/3-selinux_restorecon/">selinux_restorecon</a></code>(3) reads <code>/proc/mounts</code> to obtain a list of non-seclabel mounts to be excluded from relabeling checks unless the <code>SELINUX_RESTORECON_IGNORE_MOUNTS</code> flag has been set.</dl>
<h2>Return Value</h2>
<p>On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>Notes</h2>
<dl>
<dt>1.</p>
<dd>To improve performance when relabeling file systems recursively (e.g. the <i>restorecon_flags</i> <code>SELINUX_RESTORECON_RECURSE</code> flag is set) <code>selinux_restorecon</code>() will write a calculated SHA1 digest of the specfile entries returned by <code><a href="/docs/linux/man/3-selabel_get_digests_all_partial_matches/">selabel_get_digests_all_partial_matches</a></code>(3) to an extended attribute named <i>security.sehash</i> for each directory in the <i>pathname</i> path.</p>
<dt>2.</p>
<dd>To check the extended attribute entry use <code><a href="/docs/linux/man/1-getfattr/">getfattr</a></code>(1)<code>,</code> for example: </p>
<dl>
<dd>
<dl>
<dd>getfattr -e hex -n security.sehash /</dl>
</dl>
<dt>3.</p>
<dd>Should any of the specfile entries have changed, then when <code>selinux_restorecon</code>() is run again with the <code>SELINUX_RESTORECON_RECURSE</code> flag set, new SHA1 digests will be calculated and all files automatically relabeled depending on the settings of the <code>SELINUX_RESTORECON_SET_SPECFILE_CTX</code> flag (provided <code>SELINUX_RESTORECON_NOCHANGE</code> is not set).</p>
<dt>4.</p>
<dd><code>/sys</code> and in-memory filesystems do not support the <i>security.sehash</i> extended attribute and are automatically excluded from any relabeling checks.</p>
<dt>5.</p>
<dd>By default <code>stderr</code> is used to log output messages and errors. This may be changed by calling <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3) with the <code>SELINUX_CB_LOG</code> <i>type</i> option.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selabel_get_digests_all_partial_matches/">selabel_get_digests_all_partial_matches</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_sehandle/">selinux_restorecon_set_sehandle</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_default_handle/">selinux_restorecon_default_handle</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_exclude_list/">selinux_restorecon_set_exclude_list</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_set_alt_rootpath/">selinux_restorecon_set_alt_rootpath</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_restorecon_xattr/">selinux_restorecon_xattr</a></code>(3),<br />
 <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3) </p>
