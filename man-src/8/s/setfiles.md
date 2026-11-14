---
title: "setfiles(8)"
name: "setfiles"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setfiles/"
description: "setfiles – set SELinux file security contexts."
---

<p>setfiles &#8211; set SELinux file security contexts. </p>
<h2>Synopsis</h2>
<p><code>setfiles</code> <i>[-c policy] [-d] [-l] [-n] [-e directory] [-o filename] [-p] [-q] [-s] [-v] [-W] [-F] spec_file pathname&#8230;</i></p>
<h2>Description</h2>
<p>This manual page describes the <code>setfiles</code> program. </p>
<p> This program is primarily used to initialize the security context fields (extended attributes) on one or more filesystems (or parts of them). Usually it is initially run as part of the SELinux installation process (a step commonly known as labeling). </p>
<p> It can also be run at any other time to correct inconsistent labels, to add support for newly-installed policy or, by using the -n option, to passively check whether the file contexts are all set as specified by the active policy (default behavior) or by some other policy (see the -c option). </p>
<p> If a file object does not have a context, setfiles will write the default context to the file object&#8217;s extended attributes. If a file object has a context, setfiles will only modify the type portion of the security context. The -F option will force a replacement of the entire context.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>check the validity of the contexts against the specified binary policy.</p>
<dt><code>-d</code></p>
<dd>show what specification matched each file (do not abort validation after 10 errors).</p>
<dt><code>-e directory</code></p>
<dd>directory to exclude (repeat option for more than one directory).</p>
<dt><code>-f</code></p>
<dd>take a list of files to be processed from an input file.</p>
<dt><code>-F</code></p>
<dd>Force reset of context to match file_context for customizable files, and the default file context, changing the user, role, range portion as well as the type.</p>
<dt><code>-h, -?</code></p>
<dd>display usage information and exit.</p>
<dt><code>-i</code></p>
<dd>ignore files that do not exist.</p>
<dt><code>-l</code></p>
<dd>log changes in file labels to syslog.</p>
<dt><code>-n</code></p>
<dd>don&#8217;t change any file labels (passive check).</p>
<dt><code>-o filename</code></p>
<dd>Deprecated, SELinux policy will probably block this access. Use shell redirection to save list of files with incorrect context in filename.</p>
<dt><code>-p</code></p>
<dd>show progress by printing * every 1024 files. (If you relabel the entire OS, this will show you the percentage complete.)</p>
<dt><code>-q</code></p>
<dd>suppress non-error output.</p>
<dt><code>-r rootpath</code></p>
<dd>use an alternate root path.</p>
<dt><code>-s</code></p>
<dd>take a list of files from standard input instead of using a pathname from the command line (equivalent to -f -).</p>
<dt><code>-v</code></p>
<dd>show changes in file labels.</p>
<dt><code>-W</code></p>
<dd>display warnings about entries that had no matching files.</p>
<dt><code>-0</code></p>
<dd>the separator for the input items is assumed to be the null character (instead of the white space). The quotes and the backslash characters are also treated as normal characters that can form valid input. This option finally also disables the end of file string, which is treated like any other argument. Useful when input items might contain white space, quote marks or backslashes. The <code>-print0</code> option of GNU <code>find</code> produces input suitable for this mode. </p>
</dl>
<h2>Arguments</h2>
<p><code>spec_file</code> The specification file which contains lines of the following form<br />
 <code>regexp [ -type ] ( context | &lt;&lt;none&gt;&gt; )</code><br />
 The regular expression is anchored at both ends. The optional type field specifies the file type as shown in the mode field by the <code><a href="/docs/linux/man/1-ls/">ls</a>(1)</code> program, e.g. &#8212; to match only regular files or -d to match only directories. The context can be an ordinary security context or the string &lt;&lt;none&gt;&gt; to specify that the file is not to have its context changed.<br />
 The last matching specification is used. If there are multiple hard links to a file that match different specifications and those specifications indicate different security contexts, then a warning is displayed but the file is still labeled based on the last matching specification other than &lt;&lt;none&gt;&gt;.</p>
<dl>
<dt><code>pathname&#8230;</code></p>
<dd>The pathname for the root directory of each file system to be relabeled or a specific directory within a filesystem that should be recursively descended and relabeled or the pathname of a file that should be relabeled. Not used if the <code>-f</code> or the <code>-s</code> option is used. </p>
</dl>
<h2>Author</h2>
<p>This man page was written by Russell Coker &lt;russell [at] coker.com.au&gt;. The program was written by Stephen Smalley &lt;sds [at] epoch.ncsc.mil&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-restorecon/">restorecon</a></code>(8), <code><a href="/docs/linux/man/8-load_policy/">load_policy</a></code>(8), <code><a href="/docs/linux/man/8-checkpolicy/">checkpolicy</a></code>(8) </p>
