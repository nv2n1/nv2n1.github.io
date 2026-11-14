---
title: "lyx(1)"
name: "lyx"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lyx/"
description: "LyX – A Document Processor"
---

<h2>NAME</h2>
<p> LyX &#8211; A Document Processor</p>
<h2>SYNOPSIS</h2>
<p> <code>lyx</code> [ <i>command-line switches</i> ] [ <i>name[.lyx] &#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>LyX</code> is too complex to be described completely in the &quot;man&quot; page format. If your system is properly configured, you can access the full documentation within <code>LyX</code> under the Help menu. </p>
<p> <code>LyX</code> is a document preparation system. It excels at letting you create complex technical and scientific articles with mathematics, cross-references, bibliographies, indices, etc. It is very good at documents of any length in which the usual processing abilities are required: automatic sectioning and pagination, spellchecking, and so forth. It can also be used to write a letter to your mom, though granted, there are probably simpler programs available for that. It is definitely not the best tool for creating banners, flyers, or advertisements, though with some effort all these can be done, too. Some examples of what it is used for: memos, letters, dissertations and theses, lecture notes, seminar notebooks, conference proceedings, software documentation, books (on PostgreSQL, remote sensing, cryptology, fictional novels, poetry, and even a children&#8217;s book or two), articles in refereed scientific journals, scripts for plays and movies, business proposals&#8230; you get the idea. </p>
<p> Currently, <code>LyX</code> uses the Qt4 library as a toolkit. <code>LyX</code> should run everywhere, where this library runs. This is on all major Unix platforms as well as Windows and Mac OS X (which actually is a unix platform).</p>
<h2>OPTIONS</h2>
<p> <code>LyX</code> supports the following command-line switches.</p>
<dl>
<dt><code>-help</code></p>
<dd> summarizes LyX usage</p>
<dt><code>-version</code></p>
<dd> provides version information on the build of LyX.</p>
<dt><code>-sysdir</code><i> directory</i></p>
<dd> sets system directory. Normally not needed.</p>
<dt><code>-userdir</code><i> directory</i></p>
<dd> sets user directory. Needed if you want to use LyX with different lyxrc settings.</p>
<dt><code>-geometry</code><i> WxH+X+Y</i></p>
<dd> set geometry of the main window.</p>
<dt><code>-dbg</code><i> feature[,feature&#8230;]</i></p>
<dd> where feature is a name or number. Use &quot;<code>lyx -dbg</code>&quot; to see the list of available debug features.</p>
<dt><code> -x [&#8211;execute]</code> <i>command</p>
<dd> where command is a lyx command.</p>
<dt></i><code> -e [&#8211;export]</code> <i>fmt</p>
<dd> where fmt is the export format of choice (latex, pdflatex, luatex, xetex, xhtml, text, lyx, ps, pdf, &#8230;). Note that the order of -e and -x switches matters.</p>
<dt></i><code> -E [&#8211;export-to]</code> <i>fmt filename</p>
<dd> where fmt is the export format of choice (see &#8211;export), and filename is the destination filename. Note that any additional external file needed by filename (such as image files) will be exported as well to the folder containing filename (preserving the relative path embedded within the original LyX document, if any).</p>
<dt></i><code> -i [&#8211;import]</code> <i>fmt file.xxx</p>
<dd> where fmt is the import format of choice and file.xxx is the file to be imported.</p>
<dt></i><code> -f [&#8211;force-overwrite]</code> <i>what</p>
<dd> where what is is either &quot;</i><code>all</code>&quot;, &quot;<code>main</code>&quot; or &quot;<code>none</code>&quot;. Specify &quot;<code>all</code>&quot; to allow overwriting all files during a batch export, &quot;<code>main</code>&quot; to allow overwriting the main file only, or &quot;<code>none</code>&quot; to disallow overwriting any file. When this switch is followed by anything else other than &quot;<code>all</code>&quot;, &quot;<code>main</code>&quot; or &quot;<code>none</code>&quot;, the behavior is as if &quot;<code>all</code>&quot; was specified, but what follows is left on the command line for further processing.</p>
<dt><code> -n [&#8211;no-remote]</code></p>
<dd> open documents passed as arguments in a new instance, even if another instance of LyX is already running.</p>
<dt><code> -r [&#8211;remote]</code></p>
<dd> by using the lyxpipe, ask an already running instance of LyX to open the documents passed as arguments and then exit. If the lyxpipe is not set up or is not working, a new instance is created and execution continues normally.</p>
<dt><code>-batch</code></p>
<dd> causes LyX to run the given commands without opening a GUI window. Thus, something like: </p>
<p>&nbsp;<wbr>lyx -batch -x&nbsp;<wbr>&quot;buffer-print printer default dvips&quot;&nbsp;<wbr>myfile.lyx<br />
 will cause LyX to print myfile.lyx to the default printer, using dvips and the default print settings (which, of course, have to have been configured already). </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>LYX_DIR_21x</code></p>
<dd> can be used to specify which system directory to use.</dl>
<p> The system directory is determined by searching for the file &quot;chkconfig.ltx&quot;. Directories are searched in this order:<br />
 1) -sysdir command line parameter<br />
 2) LYX_DIR_21x environment variable<br />
 3) Maybe &lt;path of binary&gt;/TOP_SRCDIR/lib<br />
 4) &lt;path of binary&gt;/../share/&lt;name of binary&gt;/<br />
 5) hardcoded lyx_dir (at build time: /usr/share/lyx)</p>
<dl>
<dt><code>LYX_USERDIR_21x</code></p>
<dd> can be used to specify which user directory to use.</dl>
<p> The user directory is, in order of precedence:<br />
 1) -userdir command line parameter<br />
 2) LYX_USERDIR_21x environment variable<br />
 3) $HOME/.&lt;name of binary&gt; if no explicit setting is made </p>
<dl>
<dt><code>LYX_LOCALEDIR</code></p>
<dd> can be used to tell LyX where to look for the translations of its GUI strings in other languages. </p>
<dt><code>LYX_FORCE_OVERWRITE</code></p>
<dd> can be used to change the default behavior when exporting from command line.</dl>
<p> By default, LyX overwrites the main file when exporting from command line but not the ancillary files. This behavior can be changed by setting this environment variable, which relieves the need of using the -f switch. Allowed values are either &quot;<code>all</code>&quot;, &quot;<code>main</code>&quot; or &quot;<code>none</code>&quot;, with same meaning as for the -f switch.</p>
<h2>FILES</h2>
<pre>
~/.lyx/preferences      Personal configuration file
~/.lyx/lyxrc.defaults   Personal autodetected configuration file
<i>LIBDIR</i>/lyxrc.dist  System wide configuration file
<i>LIBDIR</i>/configure.py  Updates <code>LyX</code> if config has changed
<i>LIBDIR</i>/bind/      Keybindings
<i>LIBDIR</i>/clipart/   Clipart pictures
<i>LIBDIR</i>/doc/       Documentation in <code>LyX</code> format.
<i>LIBDIR</i>/examples/  Example documents
<i>LIBDIR</i>/images/    Images used as icons or in popups
<i>LIBDIR</i>/kbd/       Keyboard mappings
<i>LIBDIR</i>/layouts/   Layout descriptions
<i>LIBDIR</i>/templates/ Templates for documents
<i>LIBDIR</i>/tex/       Extra TeX files
</pre>
<p> <i>LIBDIR</i> is the system directory. This was at build time /usr/share/lyx.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tex2lyx/">tex2lyx</a>(1), <a href="/docs/linux/man/1-latex/">latex</a>(1). </p>
<p> Full documentation in either native <code>LyX</code> or postscript format.</p>
<h2>BUGS/LIMITATIONS</h2>
<p> There are still some bugs in <code>LyX</code>. To report one, read if possible the Introduction found under the Help menu in LyX. You&#8217;ll find detailed info on submitting bug reports there. If you can&#8217;t do that, send details to the LyX Developers mailing list lyx-devel [at] lists.lyx.org, or use the LyX bug tracker at <a rel="nofollow" href="http://www.lyx.org/trac/wiki/BugTrackerHome.">http://www.lyx.org/trac/wiki/BugTrackerHome.</a> Don&#8217;t forget to mention which version you are having problems with! </p>
<p> <code>LaTeX</code> import is still not perfect and may produce buggy *.lyx files. Consult the <code>tex2lyx</code> documentation. </p>
<h2>AUTHORS</h2>
<p> LyX is Copyright (C) 1995 by Matthias Ettrich, 1995-2010 LyX Team </p>
<h2>Index</h2>
