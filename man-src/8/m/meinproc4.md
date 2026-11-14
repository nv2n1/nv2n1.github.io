---
title: "meinproc4(8)"
name: "meinproc4"
section: "8"
letter: "m"
url: "/docs/linux/man/8-meinproc4/"
description: "meinproc4 – KDE translator for XML"
---

<p>meinproc4 &#8211; KDE translator for XML</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>meinproc4</code> [&#8211;help] [Generic-options] [Qt-options] [KDE-options] [&#8211;cache<i>&nbsp;<wbr>file</i>] [&#8211;check] [&#8211;htdig] [&#8211;srcdir] [&#8211;param&nbsp;<wbr><i>key</i>=<i>value</i>] [[[-o] | [&#8211;output]]<i> file</i>] [&#8211;stdout] [&#8211;stylesheet<i>&nbsp;<wbr>xsl</i>] docbook_file</dl>
<h2>Description</h2>
<p><code>meinproc4</code></p>
<dd>converts DocBook files to HTML.</p>
<h2>Generic Options</h2>
<p><code>&#8211;author</code></p>
<dl>
<dd>Show author information.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Show help about options.</dl>
<p> <code>&#8211;help-all</code></p>
<dl>
<dd>Show all options.</dl>
<p> <code>&#8211;help-kde</code></p>
<dl>
<dd>Show KDE specific options.</dl>
<p> <code>&#8211;help-qt</code></p>
<dl>
<dd>Show Qt specific options.</dl>
<p> <code>&#8211;license</code></p>
<dl>
<dd>Show license information.</dl>
<p> <code>-v</code><code>&#8211;version</code></p>
<dl>
<dd>Show version information</dl>
<h2>Application Options</h2>
<p><code>&#8211;cache</code> <i>file</i></p>
<dl>
<dd>Create a cache file for the document</dl>
<p> <code>&#8211;check</code></p>
<dl>
<dd>Check the document for validity </p>
<dl>
<dd>
<pre>The output can be a bit daunting, since one small mistake can cause a cascade of errors. 
The trick is to look at the first error, fix that error, save the file, and run <code>meinproc4</code> again.</pre>
</dl>
</dl>
<p> <code>&#8211;htdig</code></p>
<dl>
<dd>Create a ht://dig compatible index</dl>
<p> <code>-o</code>, <code>&#8211;output</code><i> file</i></p>
<dl>
<dd>Output whole document to <i>file</i>.</dl>
<p> <code>&#8211;stdout</code></p>
<dl>
<dd>Output whole document to stdout.</dl>
<p> <code>&#8211;stylesheet</code> <i>xsl</i></p>
<dl>
<dd>Stylesheet to use</dl>
<p> <code>&#8211;srcdir</code> <i>dir</i></p>
<dl>
<dd>Set the root directory to look for kdelibs</dl>
<p> <code>&#8211;param</code> key=value</p>
<dl>
<dd>Set parameters to pass to the stylesheet.</dl>
<h2>Usage</h2>
<p>The most common way to run <code>meinproc4</code> is simply as </p>
<dl>
<dd>
<pre><code>meinproc4</code><i>docbook-file</i></pre>
</dl>
<p> where <i>docbook-file</i> is usually index.docbook. This command creates HTML pages from the DocBook file. Note that these pages are only viewable in KDE-based browsers (like Konqueror). </p>
<p> If you need to view the HTML output in another browser (for example, if you&#8217;re placing it on line), use </p>
<dl>
<dd>
<pre><code>meinproc4</code><code> --stylesheet </code><i>stylesheet-name</i><i>docbook-file</i></pre>
</dl>
<p> where <i>stylesheet-name</i> is the full path to one of the XSL stylesheets in $KDEDIR/share/apps/ksgmltools/customization. To produce output suitable for the web, you can use <code>kde-web.xsl</code> or <code>kde-chunk-online.xsl</code>. See the README file in that directory for more details.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-kdeoptions/">kdeoptions</a></i>(7), <i><a href="/docs/linux/man/7-qtoptions/">qtoptions</a></i>(7)</p>
<h2>Bugs</h2>
<p>There are probably tons of bugs. Use m[blue]<code>bugs.kde.org</code>m[]<font SIZE="-2">[1]</font> to report them.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>bugs.kde.org</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dl>
