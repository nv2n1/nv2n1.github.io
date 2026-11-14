---
title: "symlinks(8)"
name: "symlinks"
section: "8"
letter: "s"
url: "/docs/linux/man/8-symlinks/"
description: "symlinks – symbolic link maintenance utility"
---

<p>symlinks &#8211; symbolic link maintenance utility</p>
<h2>Synopsis</h2>
<p><code>symlinks</code> [ <code>-cdorstv</code> ] dirlist</p>
<h2>Description</h2>
<p><code>symlinks</code> is a useful utility for maintainers of FTP sites, CDROMs, and Linux software distributions. It scans directories for symbolic links and lists them on stdout, often revealing flaws in the filesystem tree. Each link is output with a classification of <code>relative,</code> <code>absolute,</code> <code>dangling,</code> <code>messy,</code> <code>lengthy,</code> or <code>other_fs.</code> <code>relative</code> links are those expressed as paths relative to the directory in which the links reside, usually independent of the mount point of the filesystem. <code>absolute</code> links are those given as an absolute path from the root directory as indicated by a leading slash (/). <code>dangling</code> links are those for which the target of the link does not currently exist. This commonly occurs for <code>absolute</code> links when a filesystem is mounted at other than its customary mount point (such as when the normal root filesystem is mounted at /mnt after booting from alternative media). <code>messy</code> links are links which contain unnecessary slashes or dots in the path. These are cleaned up as well when <code>-c</code> is specified. <code>lengthy</code> links are links which use &quot;../&quot; more than necessary in the path (eg. /bin/vi -&gt; ../bin/vim) These are only detected when <code>-s</code> is specified, and are only cleaned up when <code>-c</code> is also specified. <code>other_fs</code> are those links whose target currently resides on a different filesystem from where symlinks was run (most useful with <code>-r</code> ). </p>
<h2>Options</h2>
<dl>
<dt><i>-c </i></p>
<dd>convert absolute links (within the same filesystem) to relative links. This permits links to maintain their validity regardless of the mount point used for the filesystem &#8212; a desirable setup in most cases. This option also causes any <code>messy</code> links to be cleaned up, and, if <code>-s</code> was also specified, then <code>lengthy</code> links are also shortened. Links affected by <code>-c</code> are prefixed with <code>changed</code> in the output.</p>
<dt><i>-d</i></p>
<dd>causes <code>dangling</code> links to be removed.</p>
<dt><i>-o </i></p>
<dd>fix links on other filesystems encountered while recursing. Normally, other filesystems encountered are not modified by symlinks.</p>
<dt><i>-r </i></p>
<dd>recursively operate on subdirectories within the same filesystem.</p>
<dt><i>-s</i></p>
<dd>causes <code>lengthy</code> links to be detected.</p>
<dt><i>-t</i></p>
<dd>is used to test for what <code>symlinks</code> would do if <code>-c</code> were specified, but without really changing anything.</p>
<dt><i>-v </i></p>
<dd>show all symbolic links. By default, <code>relative</code> links are not shown unless <code>-v</code> is specified.</dl>
<h2>Bugs</h2>
<p><code>symlinks</code> does not recurse or change links across filesystems. </p>
<h2>Author</h2>
<p><code>symlinks </code> has been written by Mark Lord &lt;mlord [at] pobox.com&gt;, the original developer and maintainer of the IDE Performance Package for linux, the Linux IDE Driver subsystem, hdparm, and a current day libata hacker.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2) </p>
