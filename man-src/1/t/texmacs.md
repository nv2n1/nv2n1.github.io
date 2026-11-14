---
title: "texmacs(1)"
name: "texmacs"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texmacs/"
description: "GNU TeXmacs – a WYSIWYG mathematical text editor"
---

<h2>NAME</h2>
<p> GNU TeXmacs &#8211; a WYSIWYG mathematical text editor </p>
<h2>SYNOPSIS</h2>
<p> texmacs [<i>OPTION</i>]&#8230; [<i>SOURCE</i>]&#8230; </p>
<h2>INTRODUCTION</h2>
<p> GNU TeXmacs is a free scientific text editor, which was both inspired by TeX and GNU Emacs. The editor allows you to write structured documents via a wysiwyg (what-you-see-is-what-you-get) and user friendly interface. New styles may be created by the user. The program implements high-quality typesetting algorithms and TeX fonts, which help you to produce professionally looking documents. </p>
<p> The high typesetting quality still goes through for automatically generated formulas, which makes TeXmacs suitable as an interface for computer algebra systems. TeXmacs also supports the Guile/Scheme extension language, so that you may customize the interface and write your own extensions to the editor. </p>
<p> TeXmacs currently runs on PC&#8217;s and PPC&#8217;s under Gnu/linux (a &gt;200MHz processor and &gt;32Mb of memory are recommended) and on sun computers. Converters exist for TeX/LaTeX and they are under development for Html/Mathml/Xml. In the future, TeXmacs is planned to evoluate towards a complete scientific office suite, with spreadsheet capacities, a technical drawing editor and a presentation mode. </p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>-b [file]</code>, <code>&#8211;initialize-buffer [file]</code></p>
<dd> Uses [file] as a guile/scheme initialization file for TeXmacs buffers.</p>
<dt><code>-c [in] [out]</code>, <code>&#8211;convert [in] [out]</code></p>
<dd> Convert input file [in] into output file [out]. The file formats are determined automatically from the suffixes and as a function of the contents of [in]. The argument list may contain several conversion instructions and you will usually want to use this option in combination with &#8211;quit.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Display most important debugging information.</p>
<dt><code>&#8211;debug-events</code></p>
<dd> Display all widget events.</p>
<dt><code>&#8211;debug-io</code></p>
<dd> Display all communicated data between TeXmacs and extern systems.</p>
<dt><code>&#8211;debug-all</code></p>
<dd> Turn all debugging flags on.</p>
<dt><code>&#8211;delete-cache</code></p>
<dd> This option deletes all files in the TeXmacs cache. TeXmacs uses several caches for speeding up font, file, directory and style file loading. However, these optimizations may be incorrect when the user manually changes files in the TeXmacs distribution or when new fonts are added. This is rarely the case for normal users, but sometimes necessary for TeXmacs developers.</p>
<dt><code>&#8211;delete-doc-cache</code></p>
<dd> This option is similar to &#8211;delete-cache, but only deletes the cache for accelerated help file loading.</p>
<dt><code>&#8211;delete-file-cache</code></p>
<dd> This option is similar to &#8211;delete-cache, but only deletes the cache for accelerated file loading.</p>
<dt><code>&#8211;delete-font-cache</code></p>
<dd> This option is similar to &#8211;delete-cache, but only deletes the cache for accelerated font loading.</p>
<dt><code>&#8211;delete-style-cache</code></p>
<dd> This option is similar to &#8211;delete-cache, but only deletes the cache for accelerated style file loading.</p>
<dt><code>-fn [font]</code>, <code>&#8211;font [font]</code></p>
<dd> Sets the default TeX fonts for menus and so to [font]. The [font] is of the form [name], [name][size] or [name][size]@[dpi]. For instance, ecss11@400 would give a sans serif font at 400 dpi. By default, the [size] is 11 and the [dpi] 300.</p>
<dt><code>-g [geom]</code>, <code>&#8211;geometry [geom]</code></p>
<dd> Suggested geometry for TeXmacs windows. Here [geom] may be a size [width x height] in pixels, like in `texmacs -g 600&#215;480&#8242;. It may also take the form [width x height [+|-] xoff [+|-] yoff], like in `texmacs -g 800&#215;600-100+100&#8242;.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a help message, which lists the command line options of TeXmacs.</p>
<dt><code>-i [file]</code>, <code>&#8211;initialize [file]</code></p>
<dd> Uses [file] as a guile/scheme initialization file for TeXmacs.</p>
<dt><code>-Oc</code>, <code>&#8211;no-char-clipping</code></p>
<dd> Faster but less perfect displaying of anti-aliased fonts.</p>
<dt><code>+Oc</code>, <code>&#8211;char-clipping</code></p>
<dd> High quality displaying of anti-aliased fonts (default).</p>
<dt><code>-p</code>, <code>&#8211;path</code></p>
<dd> Echo the TeXmacs path.</p>
<dt><code>-q</code>, <code>&#8211;quit</code></p>
<dd> Shortcut for the option -x &quot;(quit-TeXmacs)&quot;.</p>
<dt><code>-r</code>, <code>&#8211;reverse</code></p>
<dd> Reverse video mode. This mode inverts and weakens the intensity of all colors. This option is only available as a global start-up option. You cannot change it while running TeXmacs.</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> Silent execution: less messages to standard output.</p>
<dt><code>-S</code>, <code>&#8211;setup</code></p>
<dd> Rerun the setup program before starting TeXmacs. The setup program analyzes your TeX/LaTeX distribution and the plugins which are installed on your system.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display the current TeXmacs version.</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Display some informative messages.</p>
<dt><code>-x</code>, <code>&#8211;execute [cmd]</code></p>
<dd> Execute the scheme command [cmd] just after startup. If you specify several -x options, then the corresponding scheme commands are executed in the same order.</dl>
<h2>AUTHOR</h2>
<p> Written by Joris van der Hoeven</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] texmacs.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1999-2005 Joris van der Hoeven<br />
 This is free software; see the source for copying conditions. GNU TeXmacs comes with NO WARRANTY WHATSOEVER; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for GNU TeXmacs can be accessed through the help menu when starting up the editor. You may also access the online documentation from inside the editor. The TeXmacs website at &lt;<a rel="nofollow" href="http://www.texmacs.org">http://www.texmacs.org</a>&gt; can be consulted for additional information. The TeXmacs web pages are also available at &lt;<a rel="nofollow" href="http://www.gnu.org/software/texmacs">http://www.gnu.org/software/texmacs</a>&gt;. </p>
<h2>Index</h2>
