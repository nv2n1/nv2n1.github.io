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
<dt><code>-B</code></dt>
<dd>If specified with onboot, this fixfiles will record the current date in the /.autorelabel file, so that it can be used later to speed up labeling. If used with restore, the restore will only affect files that were modified today.</dd>
<dt><code>-l logfile</code></dt>
<dd>Save the output to the specified logfile</dd>
<dt><code>-F</code></dt>
<dd>Force reset of context to match file_context for customizable files </dd>
<dt><code>-f</code></dt>
<dd>Clear /tmp directory with out prompt for removal. </dd>
<dt><code>-R rpmpackagename[,rpmpackagename&#8230;]</code></dt>
<dd>Use the rpm database to discover all files within the specified packages and restore the file contexts. (-a will get all files in the RPM database).</dd>
<dt><code>-C PREVIOUS_FILECONTEXT</code></dt>
<dd>Run a diff on the PREVIOUS_FILECONTEXT file to the currently installed one, and restore the context of all affected files. </dd>
<dt><code>-N time</code></dt>
<dd>Only act on files created after the specified date. Date must be specified in &quot;YYYY-MM-DD HH:MM&quot; format. Date field will be passed to find &#8211;newermt command. </dd>
<dt><code>-v</code></dt>
<dd>Modify verbosity from progress to verbose. (Run restorecon with -v instead of -p) </dd>
</dl>
<h2>Arguments</h2>
<p>One of:</p>
<dl>
<dt><code>check</code></dt>
<dd>print any incorrect file context labels, showing old and new context, but do not change them.</dd>
<dt><code>restore</code></dt>
<dd>change any incorrect file context labels.</dd>
<dt><code>relabel</code></dt>
<dd>Prompt for removal of contents of /tmp directory and then change any incorrect file context labels to match the install file_contexts file.</dd>
<dt><code>verify</code></dt>
<dd>List out files with incorrect file context labels, but do not change them.</dd>
<dt><code>[[dir/file] &#8230; ] </code></dt>
<dd>List of files or directories trees that you wish to check file context on. </dd>
</dl>
<h2>Author</h2>
<p>This man page was written by Richard Hally &lt;rhally [at] mindspring.com&gt;. The script was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-setfiles/">setfiles</a></code>(8),<code><a href="/docs/linux/man/8-restorecon/">restorecon</a>(8)</code> </p>
