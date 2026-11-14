---
title: "geany(1)"
name: "geany"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geany/"
description: "Geany — a small and lightweight IDE"
---

<h2>NAME</h2>
<p> Geany &#8212; a small and lightweight IDE</p>
<h2>SYNOPSIS</h2>
<p> <code>geany</code> [<code>option</code>] [+number] [<code>files &#8230;</code>]</p>
<h2>DESCRIPTION</h2>
<p> Geany is a small and fast editor with basic features of an integrated development environment. </p>
<p> Some of its features: syntax highlighting, code completion, code folding, symbol/tag lists and many supported filetypes like C(++), Java, PHP, HTML, DocBook, Perl and more. </p>
<p> Homepage: <a rel="nofollow" href="http://www.geany.org/">http://www.geany.org/</a></p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>files &#8230;</code></p>
<dd> A space-separated list of filenames. Absolute and relative filenames can be used. Geany also recognises line and column information when appended to the filename with colons, e.g. &quot;geany foo.bar:10:5&quot; will open the file foo.bar and place the cursor in line 10 at column 5.</p>
<dt>
<dd> Projects can also be opened but a project file (*.geany) must be the first non-option argument. All additionally given files are ignored.</p>
<dt> <code>+number</code></p>
<dd> Set initial line <i>number</i> for the first opened file (same as &#8211;line, do not put a space between the + sign and the number). E.g. &quot;geany +7 foo.bar&quot; will open the file foo.bar and place the cursor in line 7.</p>
<dt> <code>&#8211;column</code></p>
<dd> Set initial column number for the first opened file (useful in conjunction with &#8211;line).</p>
<dt><code>-c</code>, <code>&#8211;config</code></p>
<dd> Use an alternate configuration directory. Default configuration directory is ~/.config/geany/ and there resides geany.conf and some template files.</p>
<dt> <code>&#8211;ft-names</code></p>
<dd> Print a list of Geany&#8217;s internal filetype names (useful snippets configuration).</p>
<dt><code>-g</code>, <code>&#8211;generate-tags</code></p>
<dd> Generate a global tags file (see documentation).</p>
<dt><code>-P</code>, <code>&#8211;no-preprocessing</code></p>
<dd> Don&#8217;t preprocess C/C++ files when generating tags.</p>
<dt><code>-i</code>, <code>&#8211;new-instance</code></p>
<dd> Don&#8217;t open files in a running instance, force opening a new instance. Only available if Geany was compiled with support for Sockets.</p>
<dt><code>-l</code>, <code>&#8211;line</code></p>
<dd> Set initial line number for the first opened file.</p>
<dt> <code>&#8211;list-documents</code></p>
<dd> Return a list of open documents in a running Geany instance. This can be used to read the currently opened documents in Geany from an external script or tool. The returned list is separated by newlines (LF) and consists of the full, UTF-8 encoded filenames of the documents. Only available if Geany was compiled with support for Sockets.</p>
<dt><code>-m</code>, <code>&#8211;no-msgwin</code></p>
<dd> Don&#8217;t show the message window. Use this option if you don&#8217;t need compiler messages or VTE support.</p>
<dt><code>-n</code>, <code>&#8211;no-ctags</code></p>
<dd> Don&#8217;t load symbol completion and call tip data. Use this option, if you don&#8217;t want to use them. For more information please see documentation.</p>
<dt><code>-p</code>, <code>&#8211;no-plugins</code></p>
<dd> Don&#8217;t load plugin support.</p>
<dt> <code>&#8211;print-prefix</code></p>
<dd> Print installation prefix, the data directory, the lib directory and the locale directory (in this order) to stdout, each per line. This is mainly intended for plugin authors to detect installation paths.</p>
<dt><code>-r</code>, <code>&#8211;read-only</code></p>
<dd> Open all files given on the command line in read-only mode. This only applies to files opened explicitly from the command line, so files from previous sessions or project files are unaffected.</p>
<dt><code>-s</code>, <code>&#8211;no-session</code></p>
<dd> Don&#8217;t load the previous session&#8217;s files.</p>
<dt><code>-t</code>, <code>&#8211;no-terminal</code></p>
<dd> Don&#8217;t load terminal support. Use this option, if you don&#8217;t want to load the virtual terminal emulator widget at startup. If you don&#8217;t have libvte.so.4 installed, then terminal-support is automatically disabled. Only available if Geany was compiled with support for VTE.</p>
<dt> <code>&#8211;socket-file</code></p>
<dd> Use this socket filename for communication with a running Geany instance</p>
<dt> <code>&#8211;vte-lib</code></p>
<dd> Specify explicitly the path including filename or only the filename to the VTE library, e.g. /usr/lib/libvte.so or libvte.so. This option is only needed, when the autodetection doesn&#8217;t work. Only available if Geany was compiled with support for VTE.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose (print useful status messages).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Show version information and exit.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show help information and exit.</dl>
<p> Geany supports all generic GTK options, a list is available on the help screen.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by the Geany developer team. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2. </p>
<p> The complete text of the GNU General Public License can be found in /usr/share/geany/GPL-2. </p>
<h2>Index</h2>
