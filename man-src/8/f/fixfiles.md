---
title: "fixfiles(8)"
name: "fixfiles"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fixfiles/"
description: "fixfiles – fix file SELinux security contexts."
---

<p>fixfiles &#8211; fix file SELinux security contexts. </p>
<h2>Synopsis</h2>
<p><code>fixfiles </code> <i>[-v] [-F] [-B] [ -N time ] [-l logfile ] { check | restore|[-f] relabel | verify } [[dir/file] &#8230; ]</i> <code>fixfiles </code> <i>[-v] [-F] [ -R rpmpackagename[,rpmpackagename&#8230;] ] [-l logfile ] { check | restore | verify }</i> <code>fixfiles </code> <i>[-v] [-F] -C PREVIOUS_FILECONTEXT [-l logfile ] { check | restore | verify }</i> <code>fixfiles [-F] [-B]</code> <i>onboot</i> </p>
<h2>Description</h2>
<p>This manual page describes the <code>fixfiles</code> script. This script is primarily used to correct the security context database (extended attributes) on filesystems. It can also be run at any time to relabel when adding support for new policy, or just check whether the file contexts are all as you expect. By default it will relabel all mounted ext2, ext3, xfs and jfs file systems as long as they do not have a security context mount option. You can use the -R flag to use rpmpackages as an alternative. The file /etc/selinux/fixfiles_exclude_dirs can contain a list of directories excluded from relabeling. <code>fixfiles onboot </code> will setup the machine to relabel on the next reboot. </p>
<h2>Options</h2>
<dl>
<dt><code>-B</code></p>
<dd>If specified with onboot, this fixfiles will record the current date in the /.autorelabel file, so that it can be used later to speed up labeling. If used with restore, the restore will only affect files that were modified today.</p>
<dt><code>-l logfile</code></p>
<dd>Save the output to the specified logfile</p>
<dt><code>-F</code></p>
<dd>Force reset of context to match file_context for customizable files </p>
<dt><code>-f</code></p>
<dd>Clear /tmp directory with out prompt for removal. </p>
<dt><code>-R rpmpackagename[,rpmpackagename&#8230;]</code></p>
<dd>Use the rpm database to discover all files within the specified packages and restore the file contexts. (-a will get all files in the RPM database).</p>
<dt><code>-C PREVIOUS_FILECONTEXT</code></p>
<dd>Run a diff on the PREVIOUS_FILECONTEXT file to the currently installed one, and restore the context of all affected files. </p>
<dt><code>-N time</code></p>
<dd>Only act on files created after the specified date. Date must be specified in &quot;YYYY-MM-DD HH:MM&quot; format. Date field will be passed to find &#8211;newermt command. </p>
<dt><code>-v</code></p>
<dd>Modify verbosity from progress to verbose. (Run restorecon with -v instead of -p) </p>
</dl>
<h2>Arguments</h2>
<p>One of:</p>
<dl>
<dt><code>check</code></p>
<dd>print any incorrect file context labels, showing old and new context, but do not change them.</p>
<dt><code>restore</code></p>
<dd>change any incorrect file context labels.</p>
<dt><code>relabel</code></p>
<dd>Prompt for removal of contents of /tmp directory and then change any incorrect file context labels to match the install file_contexts file.</p>
<dt><code>verify</code></p>
<dd>List out files with incorrect file context labels, but do not change them.</p>
<dt><code>[[dir/file] &#8230; ] </code></p>
<dd>List of files or directories trees that you wish to check file context on. </p>
</dl>
<h2>Author</h2>
<p>This man page was written by Richard Hally &lt;rhally [at] mindspring.com&gt;. The script was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-setfiles/">setfiles</a></code>(8),<code><a href="/docs/linux/man/8-restorecon/">restorecon</a>(8)</code> </p>
