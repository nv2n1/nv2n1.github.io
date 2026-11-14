---
title: "restorecon(8)"
name: "restorecon"
section: "8"
letter: "r"
url: "/docs/linux/man/8-restorecon/"
description: "restorecon – restore file(s) default SELinux security contexts."
---

<p>restorecon &#8211; restore file(s) default SELinux security contexts. </p>
<h2>Synopsis</h2>
<p><code>restorecon</code> <i>[-R] [-n] [-p] [-v] [-e directory] pathname&#8230;</i> <code>restorecon</code> <i>-f infilename [-e directory] [-R] [-n] [-p] [-v] [-F]</i> </p>
<h2>Description</h2>
<p>This manual page describes the <code>restorecon</code> program. This program is primarily used to set the security context (extended attributes) on one or more files. It can also be run at any other time to correct inconsistent labels, to add support for newly-installed policy or, by using the -n option, to passively check whether the file contexts are all set as specified by the active policy (default behavior). If a file object does not have a context, restorecon will write the default context to the file object&#8217;s extended attributes. If a file object has a context, restorecon will only modify the type portion of the security context. The -F option will force a replacement of the entire context. It is the same executable as <code>setfiles</code> but operates in a slightly different manner depending on its argv[0]. </p>
<h2>Options</h2>
<dl>
<dt><code>-e directory</code></p>
<dd>exclude a directory (repeat the option to exclude more than one directory, Requires full path).</p>
<dt><code>-f infilename</code></p>
<dd>infilename contains a list of files to be processed. Use &#8211; for stdin.</p>
<dt><code>-F</code></p>
<dd>Force reset of context to match file_context for customizable files, and the default file context, changing the user, role, range portion as well as the type.</p>
<dt><code>-h, -?</code></p>
<dd>display usage information and exit.</p>
<dt><code>-i</code></p>
<dd>ignore files that do not exist.</p>
<dt><code>-n</code></p>
<dd>don&#8217;t change any file labels (passive check). To display the files whose labels would be changed, add -v.</p>
<dt><code>-o outfilename</code></p>
<dd>Deprecated, SELinux policy will probably block this access. Use shell redirection to save list of files with incorrect context in filename.</p>
<dt><code>-p</code></p>
<dd>show progress by printing * every 1024 files. (If you relabel the entire OS, this will show you the percentage complete.)</p>
<dt><code>-R, -r</code></p>
<dd>change files and directories file labels recursively (descend directories).<br />
 <code>Note: restorecon reports warnings on paths without default labels only if called non-recursively or in verbose mode.</code></p>
<dt><code>-v</code></p>
<dd>show changes in file labels, if type or role are going to be changed.</p>
<dt><code>-0</code></p>
<dd>the separator for the input items is assumed to be the null character (instead of the white space). The quotes and the backslash characters are also treated as normal characters that can form valid input. This option finally also disables the end of file string, which is treated like any other argument. Useful when input items might contain white space, quote marks or backslashes. The <code>-print0</code> option of GNU <code>find</code> produces input suitable for this mode.</p>
<dt></dl>
<h2>Arguments</h2>
<dd><code>pathname&#8230;</code> The pathname for the file(s) to be relabeled.</p>
<h2>Note</h2>
<p>restorecon does not follow symbolic links and by default it does not operate recursively on directories.</p>
<h2>Author</h2>
<p>This man page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;. Some of the content of this man page was taken from the setfiles man page written by Russell Coker &lt;russell [at] coker.com.au&gt;. The program was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-setfiles/">setfiles</a></code>(8), <code><a href="/docs/linux/man/8-load_policy/">load_policy</a></code>(8), <code><a href="/docs/linux/man/8-checkpolicy/">checkpolicy</a></code>(8) </p>
