---
title: "atril(1)"
name: "atril"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atril/"
description: "Atril – The MATE Document Viewer"
---

<h2 class="name">NAME</h2>
<p> Atril &#8211; The MATE Document Viewer </p>
<h2>SYNTAX</h2>
<p> <code>atril [OPTIONS&#8230;] [FILES&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> Atril is the official Document Viewer of the MATE Desktop Environment, it is a simple multi-page document viewer. It can display and print PostScript (PS), Encapsulated PostScript (EPS), DJVU, DVI, XPS and Portable Document Format (PDF) files.</p>
<dl>
<dt>When supported by the document, it also allows searching for text, copying text to the clipboard, hypertext navigation, and table-of-contents bookmarks.</p>
<dd>
<dt>This manual page briefly documents the <code>atril</code> command.</p>
<dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>filename(s)&#8230;</code></p>
<dd> Specifies the file to open when <code>atril</code> starts. If this is not specified, <code>atril</code> will start with a blank window and you may open a file from the menu or by using the shortcut CTRL+O. Multiple files can be loaded if they are separated by spaces. <code>atril</code> also supports handling of remote files.</p>
<dt><code>-p, &#8211;page-label=PAGE</code></p>
<dd> Here you can specify a page label, this page will be selected in the document if it exists.</p>
<dt><code>-i, &#8211;page-index=NUMBER</code></p>
<dd> Here you can specify a page number, this page will be selected in the document if it exists.</p>
<dt><code>-f, &#8211;fullscreen</code></p>
<dd> Start <code>atril</code> in fullscreen mode. You must specify a document to start in fullscreen mode.</p>
<dt><code>-s, &#8211;presentation</code></p>
<dd> Start <code>atril</code> in presentation mode. You must specify a document to start in presentation mode.</p>
<dt><code>-w, &#8211;preview</code></p>
<dd> Start <code>atril</code> in preview mode. You must specify a document to start in preview mode.</p>
<dt><code>&#8211;display=DISPLAY</code></p>
<dd> X display to use.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</p>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Print standard command line options.</p>
<dt><code>&#8211;help-all</code></p>
<dd> Print all command line options.</dl>
<p> This program also accepts the standard GTK options. </p>
<h2>EXAMPLES</h2>
<p> <code>atril &#8211;preview ~/Desktop/stuff.ps</code></p>
<dl>
<dt>
<dd> Open stuff.ps from the current users desktop, in preview mode.</dl>
<p> <code>atril -i 2 -s ./document.pdf</code></p>
<dl>
<dt>
<dd> Open document.pdf from the current working directory, on page 2 in presentation mode. </p>
</dl>
<h2>BUGS</h2>
<h3>Should you encounter any bugs, they may be reported at:</h3>
<p> <a rel="nofollow" href="http://github.com/mate-desktop/atril/issues">http://github.com/mate-desktop/atril/issues</a></p>
<h2>AUTHORS</h2>
<h3>This Man Page has been written for the MATE Desktop Environment by:</h3>
<p> Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014)</p>
<h2>SEE ALSO</h2>
<h3>Atril documentation can be found from the Help menu, or by pressing the F1 key.</h3>
<p> Further information may also be available at: <a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a> </p>
<h2>Index</h2>
