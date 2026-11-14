---
title: "gnome-text-editor(1)"
name: "gnome-text-editor"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-text-editor/"
description: "gedit – text editor for the GNOME Desktop"
---

<h2 class="name">NAME</h2>
<p> <code>gedit</code> &#8211; text editor for the GNOME Desktop</p>
<h2>SYNOPSIS</h2>
<p> <code>gedit</code> [<i>OPTION</i>&#8230;] [<i>FILE</i>&#8230;] [+<i>LINE</i>[:<i>COLUMN</i>]]<br />
 <code>gedit</code> [<i>OPTION</i>&#8230;] &#8211; </p>
<h2>DESCRIPTION</h2>
<p> <code>gedit</code> is the official text editor of the GNOME desktop environment. </p>
<p> While aiming at simplicity and ease of use, <code>gedit</code> is a powerful general purpose text editor. It can be used to create and edit all kinds of text files. </p>
<p> <code>gedit</code> features a flexible plugin system which can be used to dynamically add new advanced features to <code>gedit</code> itself. </p>
<h2>OPTIONS</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dl>
<dt><code>&#8211;encoding</code></p>
<dd> Set the character encoding to be used for opening the files listed on the command line.</p>
<dt><code>&#8211;list-encodings</code></p>
<dd> Display list of possible values for the encoding option and exit.</p>
<dt><code>&#8211;new-window</code></p>
<dd> Create a new toplevel window in an existing instance of <code>gedit.</code></p>
<dt><code>&#8211;new-document</code></p>
<dd> Create a new document in an existing instance of <code>gedit.</code></p>
<dt><code>-s, &#8211;standalone</code></p>
<dd> Run <code>gedit</code> in standalone mode.</p>
<dt><code>-w, &#8211;wait</code></p>
<dd> Open files and block the <code>gedit</code> process.</p>
<dt><code>&#8211;help</code></p>
<dd> Prints the command line options.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</p>
<dt><code>FILE</code></p>
<dd> Specifies the file to open when <code>gedit</code> starts. If this is not specified, <code>gedit</code> will load a blank file with an &quot;Unsaved Document&quot; label. Multiple files can be loaded if they are separated by spaces. <code>gedit</code> also supports handling of remote files. For example, you can pass the location of a webpage to <code>gedit</code> , like &quot;<a rel="nofollow" href="http://www.gnome.org">http://www.gnome.org</a>&quot;, or load a file from a FTP server, like &quot;<a href="ftp://ftp.gnome.org/robots.txt">ftp://ftp.gnome.org/robots.txt</a>&quot;.</p>
<dt><code>&#8211;</code></p>
<dd> <code>gedit will read from stdin</code></p>
<dt><code>+LINE</code></p>
<dd> For all the files specified on command line, go to the line specified by LINE (do not insert a space between the &quot;+&quot; sign and the number). If LINE is missing, go to the last line.</p>
<dt><code>COLUMN</code></p>
<dd> For all the files specified on command line, go to the column specified by COLUMN. If COLUMN is missing, go to the first column. </p>
</dl>
<h2>BUGS</h2>
<p> If you find a bug, please report it at the GNOME bug tracker. See <a rel="nofollow" href="https://wiki.gnome.org/Apps/Gedit/ReportingBugs.">https://wiki.gnome.org/Apps/Gedit/ReportingBugs.</a></p>
<h2>AUTHORS</h2>
<p> Paolo Maggi (paolo [at] gnome.org)</p>
<dl>
<dt>Paolo Borelli (pborelli [at] gnome.org)</p>
<dd>
<dt>Steve Frécinaux (code [at] istique.net)</p>
<dd>
<dt>Jesse van den Kieboom (jessevdk [at] gnome.org)</p>
<dd>
<dt>Ignacio Casal Quinteiro &lt;icq [at] gnome.org&gt;</p>
<dd>
<dt>James Willcox (jwillcox [at] gnome.org)</p>
<dd>
<dt>Federico Mena Quintero (federico [at] novell.com)</p>
<dd>
<dt>Chema Celorio</p>
<dd>
</dl>
<h2>Index</h2>
