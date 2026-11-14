---
title: "evince(1)"
name: "evince"
section: "1"
letter: "e"
url: "/docs/linux/man/1-evince/"
description: "evince – GNOME document viewer"
---

<h2 class="name">NAME</h2>
<p> <code>evince</code> &#8211; GNOME document viewer </p>
<p> The Evince Document Viewer application for the GNOME desktop environment</p>
<h2>SYNTAX</h2>
<p> <code>evince</code> [&#8211;help] [&#8211;page-label=PAGE | &#8211;page-index=NUMBER | &#8211;named-dest=DEST] [&#8211;fullscreen] [&#8211;presentation] [&#8211;preview] [&#8211;find=STRING] [filename(s)&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>evince</code> </p>
<p> Evince is a document viewer capable of displaying multiple and single page document formats like PDF and Postscript. For more general information about Evince please visit our website at <a rel="nofollow" href="http://www.gnome.org/projects/evince/">http://www.gnome.org/projects/evince/</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Prints the command line options.</p>
<dt><code>-p, &#8211;page-label=PAGE</code></p>
<dd> Open the document on the page with the specified page label (or page number).</p>
<dt><code>-i, &#8211;page-index=NUMBER</code></p>
<dd> Open the document on the page with the specified page index (this is the exact page number, not a page label).</p>
<dt><code>-n, &#8211;named-dest=DEST</code></p>
<dd> Open the document on the specified named destination.</p>
<dt><code>-f, &#8211;fullscreen</code></p>
<dd> Run evince in fullscreen mode.</p>
<dt><code>-s, &#8211;presentation</code></p>
<dd> Run evince in presentation mode.</p>
<dt><code>-l, &#8211;find=string</code></p>
<dd> You can pass a word or phrase here. If it exists, evince will display the document and the first match.</p>
<dt><code>filename(s)&#8230;</code></p>
<dd> Specifies the file to open when Evince starts. If this is not specified, Evince will open a blank window. Multiple files can be loaded if they are separated by spaces. Evince also supports handling of remote files. For example, you can pass the location on the web or load a file from a FTP server, like &quot;<a href="ftp://adobe.com/sample.pdf">ftp://adobe.com/sample.pdf</a>&quot;. </p>
</dl>
<h2>Print preview options</h2>
<p> These options are primarily intended for use with the GTK+ print preview function. For more information about these options see <a rel="nofollow" href="http://developer.gnome.org/gtk3/stable/GtkSettings.html#GtkSettings--gtk-print-preview-command">http://developer.gnome.org/gtk3/stable/GtkSettings.html#GtkSettings&#8211;gtk-print-preview-command</a></p>
<dl>
<dt><code>-w, &#8211;preview</code></p>
<dd> Run evince as a previewer.</p>
<dt><code>&#8211;unlink-temp-file</code></p>
<dd> If evince is run in preview mode, this will unlink the temporary file created by GTK+.</p>
<dt><code>&#8211;print-settings %s %f</p>
<dd> This sends the full path of the PDF file, f, and the settings of the print dialog, s, to evince. </p>
</dl>
<p> </code></p>
<h2>BUGS</h2>
<p> If you find a bug, please report it at <a rel="nofollow" href="https://gitlab.gnome.org/GNOME/evince/issues.">https://gitlab.gnome.org/GNOME/evince/issues.</a> </p>
<h2>Index</h2>
