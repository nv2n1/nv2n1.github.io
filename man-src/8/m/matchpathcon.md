---
title: "matchpathcon(8)"
name: "matchpathcon"
section: "8"
letter: "m"
url: "/docs/linux/man/8-matchpathcon/"
description: "matchpathcon – get the default SELinux security context for the specified path from the file contexts configuration"
---

<p>matchpathcon &#8211; get the default SELinux security context for the specified path from the file contexts configuration</p>
<h2>Synopsis</h2>
<p><code>matchpathcon</code> [<code>-V</code>] [<code>-N</code>] [<code>-n</code>] [<code>-m</code> <i>type</i>] [<code>-f</code> <i>file_contexts_file</i>] [<code>-p</code> <i>prefix</i>] [<code>-P</code> <i>policy_root_path</i>] <i>filepath&#8230;</i></p>
<h2>Description</h2>
<p><code>matchpathcon</code> queries the system policy and outputs the default security context associated with the filepath. </p>
<p> <code>Note:</code> Identical paths can have different security contexts, depending on the file type (regular file, directory, link file, char file &#8230;). </p>
<p> <code>matchpathcon </code> will also take the file type into consideration in determining the default security context if the file exists. If the file does not exist, no file type matching will occur.</p>
<h2>Options</h2>
<dl>
<dt><code>-m</code><i> type</i></p>
<dd>Force file type for the lookup. Valid types are <code>file</code>, <code>dir</code>, pipe<code>, </code>chr_file<code>, </code>blk_file<code>, </code> <code>lnk_file</code>, <code>sock_file</code>.</p>
<dt><code>-n</code></p>
<dd>Do not display path.</p>
<dt><code>-N</code></p>
<dd>Do not use translations.</p>
<dt><code>-f</code><i> file_context_file</i></p>
<dd>Use alternate file_context file</p>
<dt><code>-p</code><i> prefix</i></p>
<dd>Use prefix to speed translations</p>
<dt><code>-P</code><i> policy_root_path</i></p>
<dd>Use alternate policy root path</p>
<dt><code>-V</code></p>
<dd>Verify file context on disk matches defaults</dl>
<h2>Author</h2>
<p>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-matchpathcon/">matchpathcon</a></code>(3) </p>
