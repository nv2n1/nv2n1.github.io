---
title: "install-docs(8)"
name: "install-docs"
section: "8"
letter: "i"
url: "/docs/linux/man/8-install-docs/"
description: "install-docs – manage online Debian documentation"
---

<p>install-docs &#8211; manage online Debian documentation</p>
<h2>Synopsis</h2>
<pre> install-docs [options] -i,--install | -r,--remove | -c,--check file [ file ... ]
 install-docs [options] -I,--install-all | -C,--install-changed | -R,--remove-all
 install-docs [options] -s,--status docid [ docid ... ]
 install-docs [options] --dump-db dbname
 install-docs -h,--help | -V,--version</pre>
<h2>Description</h2>
<p><code>install-docs</code> is a tool allow Debian package maintainers to register documentation to various documentation systems. It currently supports <code>dhelp</code>, <code>dwww</code>, <code>doc-central</code>, and <code>scrollkeeper</code> browsers. </p>
<p> This manual page provides a quick synopsis of <code>install-docs</code> usage. Full documentation can be found in the documentation, including a description of the control file syntax and grammar.</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Operate verbosely.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Print some debugging information.</p>
<dt><code>&#8211;no-update-menus</code></p>
<dd>Inhibit running <i><a href="/docs/linux/man/8-dwww-build-menu/">dwww-build-menu</a></i>(8), <i><a href="/docs/linux/man/8-dhelp_parse/">dhelp_parse</a></i>(8), and <i><a href="/docs/linux/man/8-scrollkeeper-update/">scrollkeeper-update</a></i>(8).</p>
<dt><code>&#8211;rootdir</code> <i>dir</i></p>
<dd>Set the root directory to <i>dir</i> instead of `<i>/</i>&#8216;. Useful and valid only with the <code>&#8211;check</code> action.</dl>
<h2>Actions</h2>
<p>Below is list of possible actions <code>install-docs</code> could handle. There can be only one action option passed to install-docs, moreover the action with its arguments must be the last option passed. </p>
<p> Each <i>file</i> argument should be the full path for the doc-base control file (i.e. `/usr/share/doc-base/some_file&#8217; or `/etc/doc-base/documents/some_file&#8217;), and each <i>docid</i> should be the document identifier (Document identifiers are set in the `Document&#8217; field of the control file, and usually correspond to the package name.) </p>
<p> If <i>file</i> or <i>docid</i> equals `<code>&#8211;</code>&#8216; (the minus sign), the list of arguments is read from the standard input (each file name or document id in separate line).</p>
<dl>
<dt><code>-i</code> <i>file</i> [<i>file</i> &#8230;], <code>&#8211;install</code> <i>file</i> [<i>file</i> &#8230;]</p>
<dd>Install the documentation described by the control file <i>file</i>.</p>
<dt><code>-r</code> <i>file</i> [<i>file</i> &#8230;], <code>&#8211;remove</code> <i>file</i> [<i>file</i> &#8230;]</p>
<dd>Remove the documentation identified by the control file <i>file</i>.</p>
<dt><code>-c</code> <i>file</i> [<i>file</i> &#8230;], <code>&#8211;check</code> <i>file</i> [<i>file</i> &#8230;]</p>
<dd>Check the control file <i>file</i> and display number of possible problems found. Use with <i>&#8211;verbose</i> to get the actual locations of errors and warnings. If <i>&#8211;rootdir</i> was also given, its argument will be prepended to names of the files given if the `Files&#8217; and `Index&#8217; fields of the <i>file</i>.</p>
<dt><code>-R</code>, <code>&#8211;remove-all</code></p>
<dd>De-register all registered documents.</p>
<dt><code>-I</code>, <code>&#8211;install-all</code></p>
<dd>(Re)register all documents from <i>/usr/share/doc-base</i> and <i>/etc/doc-base/documents</i>.</p>
<dt><code>-C</code>, <code>&#8211;install-changed</code></p>
<dd>Compare contents of <i>/usr/share/doc-base</i> and <i>/etc/doc-base/documents</i> directories with registered documents database and de-register any files that are missing and (re)register only changed or new files.</p>
<dt><code>-s</code> <i>docid</i> [<i>docid</i> &#8230;], <code>&#8211;status</code> <i>docid</i> [<i>docid</i> &#8230;]</p>
<dd>Display the status of the document identifier <i>docid</i>.</p>
<dt><code>-L</code> <i>docid</i> [<i>docid</i> &#8230;], <code>&#8211;listfiles</code> <i>docid</i> [<i>docid</i> &#8230;]</p>
<dd>Deprecated option. Does nothing.</p>
<dt><code>&#8211;dump-db</code> <i>dbname</i></p>
<dd>Dumps contents of internal databases, for debugging purposes. <i>dbname</i> can be either <code>files.db</code> or <code>status.db</code>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a short help message.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display version information.</dl>
<h2>Compatibility Issues</h2>
<p>The following features were added in version 0.8.4, please make sure to add proper `<i>Conflicts</i>&#8216; or `<i>Depends</i>&#8216; lines if you would like to use them in your package&#8217;s scripts:</p>
<dl>
<dt>&bull;</p>
<dd>support for passing more than one argument to the <code>-i</code> and <code>-r</code> actions,</p>
<dt>&bull;</p>
<dd>reading arguments from the standard input,</p>
<dt>&bull;</p>
<dd><code>-I</code>,<code>&#8211;install-all</code>, <code>-R</code>, <code>&#8212;remove-all</code>, <code>-c</code>, <code>&#8211;check</code> actions,</p>
<dt>&bull;</p>
<dd><code>-d</code>, <code>&#8211;debug</code>, <code>-h</code>, <code>&#8211;help</code> options.</dl>
<p> The <code>-C</code>, <code>&#8211;install-changed</code>, <code>&#8211;dump-db</code>, <code>-V</code>, <code>&#8211;version</code> options were added in 0.8.12.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/share/doc-base/</i></p>
<dd>The location of doc-base control files provided by various packages.</p>
<dt><i>/etc/doc-base/documents/</i></p>
<dd>The location of doc-base control files provided by local administrator.</p>
<dt><i>/var/lib/doc-base/info/documents/</i></p>
<dd>The location of registered control files.</p>
<dt><i>/var/lib/doc-base/info/status.db</i></p>
<dd>Statuses of registered documents.</p>
<dt><i>/var/lib/doc-base/info/files.db</i></p>
<dd>Timestamps and documents ids of registered doc-base files.</p>
<dt><i>/var/lib/doc-base/omf/</i></p>
<dd>The location of generated scrollkeeper <font SIZE="-1">OMF</font> files. Note: <i>/usr/share/omf/doc-base</i> should be a symbolic link pointing to the directory.</dl>
<h2>Bugs</h2>
<p>See <a rel="nofollow" href="http://bugs.debian.org/doc-base">http://bugs.debian.org/doc-base</a> &lt;<a href="http://bugs.debian.org/doc-base">http://bugs.debian.org/doc-base</a>&gt;.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-dhelp/">dhelp</a></i>(1), <i><a href="/docs/linux/man/1-doccentral/">doccentral</a></i>(1), <i><a href="/docs/linux/man/7-dwww/">dwww</a></i>(7), <i><a href="/docs/linux/man/7-scrollkeeper/">scrollkeeper</a></i>(7), Debian doc-base Manual <i>/usr/share/doc/doc-base/doc-base.html/index.html</i></p>
<h2>Author</h2>
<p>This program was originally written by Christian Schwarz &lt;schwarz [at] debian.org&gt;, for the Debian GNU/Linux system, and the next maintainer was Adam Di Carlo &lt;aph [at] debian.org&gt;. Robert Luberda &lt;robert [at] debian.org&gt; is currently maintaining and extending it. </p>
<p> This software was meant to be for the benefit of the entire Debian user and developer community. If you are interested in being involved with this software, please join the mailing list &lt;debian-doc [at] lists.debian.org&gt;.</p>
