---
title: "kate(1)"
name: "kate"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kate/"
description: "kate – Advanced text editor for KDE"
---

<h2 class="name">NAME</h2>
<p> kate &#8211; Advanced text editor for KDE </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kate</code> [<code>-s, &#8211;start</code><i></p>
<dd>name</i>] [<code>&#8211;startanon</code>] [<code>-n, &#8211;new</code>] [<code>-b, &#8211;block</code>] [<code>-p, &#8211;pid</code><i> pid</i>] [<code>-e, &#8211;encoding</code><i> name</i>] [<code>-l, &#8211;line</code><i> line</i>] [<code>-c, &#8211;column</code><i> column</i>] [<code>-i, &#8211;stdin</code>] [<code>-u, &#8211;use</code>] [KDE Generic Options] [Qt Generic Options]</dl>
<h2>DESCRIPTION</h2>
<p> Kate is the KDE Advanced Text Editor. </p>
<p> Kate also provides the editor part for various applications, under the name KWrite. </p>
<p> Some of Kate&#8217;s many features include configurable syntax highlighting for languages ranging from C and C++ to HTML to bash scripts, the ability to create and maintain projects, a multiple document interface (MDI), and a self-contained terminal emulator. </p>
<p> But Kate is more than a programmer&#8217;s editor. Its ability to open several files at once makes it ideal for editing UNIX&#174;&#8217;s many configuration files. This document was written in Kate.</p>
<h2>OPTIONS</h2>
<p> <code>-s</code>, <code>&#8211;start</code> <i>name</i></p>
<dl>
<dt>
<dd> Start Kate with a given session.</dl>
<p> <code>&#8211;startanon</code></p>
<dl>
<dt>
<dd> Start Kate with a new anonymous session, implies <code>-n</code>.</dl>
<p> <code>-n</code>, <code>&#8211;new</code></p>
<dl>
<dt>
<dd> Force start of a new Kate instance (is ignored if <code>start</code> is used and another Kate instance already has the given session opened), forced if no parameters and no URLs are given at all.</dl>
<p> <code>-b</code>, <code>&#8211;block</code></p>
<dl>
<dt>
<dd> If using an already running Kate instance, block until it exits, if URLs given to open.</dl>
<p> <code>-p, &#8211;pid</code> <i> pid</i></p>
<dl>
<dt>
<dd> Only try to reuse kate instance with this <i>pid</i> (is ignored if <code>start</code> is used and another Kate instance already has the given session opened).</dl>
<p> <code>-e, &#8211;encoding</code> <i> name</i></p>
<dl>
<dt>
<dd> Set encoding for the file to open </p>
<p> You can use this to force a file opened in utf-8 format, for instance. (The command <code>iconv -l</code> provides a list of encodings, which may be helpful to you.)</dl>
<p> <code>-l, &#8211;line</code> <i> line</i></p>
<dl>
<dt>
<dd> Navigate to this line</dl>
<p> <code>-c, &#8211;column</code> <i> column</i></p>
<dl>
<dt>
<dd> Navigate to this column</dl>
<p> <code>-i, &#8211;stdin</code></p>
<dl>
<dt>
<dd> Read the contents of stdin</dl>
<p> <code>-u, &#8211;use</code></p>
<dl>
<dt>
<dd> Use an already running Kate instance; default, only for compatibility</dl>
<h2>SEE ALSO</h2>
<p> More detailed user documentation is available from m[blue]<code>help:/kate</code>m[] (either enter this URL into Konqueror, or run <code>khelpcenter</code><i>help:/kate</i>). </p>
<p> There is also further information available at m[blue]<code>the Kate website</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>EXAMPLES</h2>
<p> To open a file named source.cpp at column 15, line 25, in an existing Kate window, you could use: </p>
<dl>
<dt>
<dd>
<pre>
<code>kate</code><code>-c 15</code><code>-l
25</code><code>-u</code><code>source.cpp</code> 
</pre>
</dl>
<p> If you have an active internet connection, you can take advantage of KDE&#8217;s network transparency to open a file from an ftp site. If you do not have write permission on the remote server, the file will be opened read only and you will be prompted for a local filename to save to if you make changes. If you do have write permission, changes will be saved transparently over the network. </p>
<dl>
<dt>
<dd>
<pre>
<code>kate</code><i><a href="ftp://ftp.kde.org/pub/kde/README">ftp://ftp.kde.org/pub/kde/README</a></i>
</pre>
</dl>
<h2>AUTHORS</h2>
<p> The maintainer of Kate is Christoph Cullmann&lt;cullmann [at] kde.org&gt;. A comprehensive list of authors and contributors is available in the complete user manual mentioned above.</p>
<h2>AUTHOR</h2>
<p> <code>Lauri Watts</code> &lt;lauri [at] kde.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> the Kate website</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://kate-editor.org/">http://kate-editor.org/</a></dl>
</dl>
<h2>Index</h2>
