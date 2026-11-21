---

title: "evince(1)"
name: "evince"
section: "1"
letter: "e"
url: "/docs/linux/man/1-evince/"
description: "evince – GNOME document viewer"
---

<p> <code>evince</code> &#8211; GNOME document viewer </p>
<p> The Evince Document Viewer application for the GNOME desktop environment</p>
<h2>SYNTAX</h2>
<p> <code>evince</code> [&#8211;help] [&#8211;page-label=PAGE | &#8211;page-index=NUMBER | &#8211;named-dest=DEST] [&#8211;fullscreen] [&#8211;presentation] [&#8211;preview] [&#8211;find=STRING] [filename(s)&#8230;]</p>
<p> <code>evince</code> </p>
<p> Evince is a document viewer capable of displaying multiple and single page document formats like PDF and Postscript. For more general information about Evince please visit our website at <a rel="nofollow" href="http://www.gnome.org/projects/evince/">http://www.gnome.org/projects/evince/</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, -h, &#8211;help</code></dt>
<dd> Prints the command line options.</dd>
<dt><code>-p, &#8211;page-label=PAGE</code></dt>
<dd> Open the document on the page with the specified page label (or page number).</dd>
<dt><code>-i, &#8211;page-index=NUMBER</code></dt>
<dd> Open the document on the page with the specified page index (this is the exact page number, not a page label).</dd>
<dt><code>-n, &#8211;named-dest=DEST</code></dt>
<dd> Open the document on the specified named destination.</dd>
<dt><code>-f, &#8211;fullscreen</code></dt>
<dd> Run evince in fullscreen mode.</dd>
<dt><code>-s, &#8211;presentation</code></dt>
<dd> Run evince in presentation mode.</dd>
<dt><code>-l, &#8211;find=string</code></dt>
<dd> You can pass a word or phrase here. If it exists, evince will display the document and the first match.</dd>
<dt><code>filename(s)&#8230;</code></dt>
<dd> Specifies the file to open when Evince starts. If this is not specified, Evince will open a blank window. Multiple files can be loaded if they are separated by spaces. Evince also supports handling of remote files. For example, you can pass the location on the web or load a file from a FTP server, like &quot;<a href="ftp://adobe.com/sample.pdf">ftp://adobe.com/sample.pdf</a>&quot;. </dd>
</dl>
<h2>Print preview options</h2>
<p> These options are primarily intended for use with the GTK+ print preview function. For more information about these options see <a rel="nofollow" href="http://developer.gnome.org/gtk3/stable/GtkSettings.html#GtkSettings--gtk-print-preview-command">http://developer.gnome.org/gtk3/stable/GtkSettings.html#GtkSettings&#8211;gtk-print-preview-command</a></p>
<dl>
<dt><code>-w, &#8211;preview</code></dt>
<dd> Run evince as a previewer.</dd>
<dt><code>&#8211;unlink-temp-file</code></dt>
<dd> If evince is run in preview mode, this will unlink the temporary file created by GTK+.</dd>
<dt><code>&#8211;print-settings %s %f</dt>
<dd> This sends the full path of the PDF file, f, and the settings of the print dialog, s, to evince. </dd>
</dl>
<p> </code></p>
<h2>BUGS</h2>
<p> If you find a bug, please report it at <a rel="nofollow" href="https://gitlab.gnome.org/GNOME/evince/issues.">https://gitlab.gnome.org/GNOME/evince/issues.</a> </p>
