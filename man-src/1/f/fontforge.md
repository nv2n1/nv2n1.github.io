---
title: "fontforge(1)"
name: "fontforge"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fontforge/"
description: "fontforge – create and modify PostScript, TrueType and SVG fonts"
---

<h2>NAME</h2>
<p> <code>fontforge &#8211; create and modify PostScript, TrueType and SVG fonts</code></p>
<h2>SYNOPSIS</h2>
<p> <code>fontforge</code> [<code>-c</code> <i>string</i>] [<code>-cmap</code> <i>maptype</i>] [<code>-depth</code> <i>pixeld</i>] [<code>-display</code> <i>str</i>] [<code>-lang=ff</code>] [<code>-lang=py</code>] [<code>-last</code>] [<code>-library-status</code>] [<code>-help</code>] [<code>-keyboard</code> <i>ktype</i>] [<code>-new</code>] [<code>-nosplash</code>] [<code>-recover</code> <i>mode</i>] [<code>-script</code> <i>file</i>] [<code>-sync</code>] [<code>-usage</code>] [<code>-vc</code> <i>vclass</i>] [<code>-version</code>] <i>fontfile &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The program <i>fontforge</i> allows you to create and modify font files, accepting input in the following formats (with associated file extensions appearing in parentheses):</p>
<dl>
<dt>Glyph Bitmap Distribution (.bdf)</p>
<dd>
<dt>Macintosh resource fonts (.dfont, .bin, .hqx)</p>
<dd>
<dt>OpenType (.otf)</p>
<dd>
<dt><i>fontforge</i> spline font database (.sfd)</p>
<dd>
<dt>P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font>, which includes:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>ASCII format (.pfa)</p>
<dd>
<dt>Binary format (.pfb)</p>
<dd>
<dt>CID-keyed fonts, Adobe convention used primarily for Asian characters (.cid, .otf)</p>
<dd>
<dt>P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> Type 0 (.ps)</p>
<dd>
<dt>P<font SIZE="-2">OST</font>S<font SIZE="-2">CRIPT</font> Type 3 (.ps)</p>
<dd></dl>
</dl>
<dt>Scaleable vector graphics fonts (.svg)</p>
<dd>
<dt>TeX bitmap (.pk)</p>
<dd>
<dt>TrueType (.ttf, .ttc)</p>
<dd>
<dt>X11 bitmap (.pcf)</p>
<dd></dl>
<p> If the argument list contains a font file name (or several), <i>fontforge</i> opens a <code>fontview</code> window for each font displaying the characters of the that font. In the absence of options or arguments, the program opens a file-picker window, allowing you to browse your disk to find a font file, or create a new one. </p>
<p> This manual page is intended only as a rudimentary overview; see the HTML Users Manual for more complete information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code><i> string</i></p>
<dd> Must be the first argument. Executes &quot;string&quot; as a set of scripting commands. Any additional arguments will be passed to the script.</p>
<dt><code>-cmap</code><i> maptype</i></p>
<dd> Employ the specified method to control 8-bit colormaps, where <i>maptype</i> assumes one of these three values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>current</code></p>
<dd> Attempt to allocate colors in the current (shared) colormap. The program will likely not find everything it requires.</p>
<dt><code>copy</code></p>
<dd> Allocate what can be allocated, then copy the current colormap; it can thus make use of cells other programs are using.</p>
<dt><code>private</code></p>
<dd> Create a new colormap and fill it with the required colors.</dl>
</dl>
<dt><code>-depth</code><i> pixeld</i></p>
<dd> Attempt to employ a visual that matches the specified pixel depth, <i>pixeld</i>.</p>
<dt><code>-display</code><i> str</i></p>
<dd> Employ the X display specified by the string <i>str</i> (for example: localhost:0).</p>
<dt><code>-help</code></p>
<dd> Display the usage description and start a web client displaying the online documentation.</p>
<dt><code>-keyboard</code><i> ktype</i></p>
<dd> Alter the displayed menus to employ modifier keys appropriate to the specified keyboard type, where <i>ktype</i> assumes one of the following four values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ibm</code></p>
<dd> IBM PC type keyboard.</p>
<dt><code>mac</code></p>
<dd> Apple Macintosh keyboard.</p>
<dt><code>sun</code></p>
<dd> Sun workstation keyboard.</p>
<dt><code>ppc</code></p>
<dd> Macintosh keyboard, but on a system running SuSe linux (the mappings differ from those used under MacOS X).</dl>
</dl>
<dt><code>-last</code></p>
<dd> Opens whatever font you last edited with <i>fontforge.</i> If you specify <i>n</i> <code>-last</code> <i>fontforge</i> will open the last <i>n</i> fonts.</p>
<dt><code>-lang=ff</code></p>
<dd> Interpret the script with the fontforge interpreter.</p>
<dt><code>-lang=py</code></p>
<dd> Interpret the script with the python interpreter.</p>
<dt><code>-library-status</code></p>
<dd> Prints information about optional libraries.</p>
<dt><code>-new</code></p>
<dd> Create a new font with the ISO 8859-1 encoding (the international encoding standard for western Europe, and the standard for most X fonts).</p>
<dt><code>-nosplash</code></p>
<dd> Suppress display of the splash screen.</p>
<dt><code>-recover</code><i> mode</i></p>
<dd> Control the crash recovery mechanism (helpful if crash recovery causes problems), where <i>mode</i> takes on one of three allowed settings:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> perform automatic recovery (default) if the program crashed before saving changes.</p>
<dt><code>clean</code></p>
<dd> Delete recovery information.</p>
<dt><code>none</code></p>
<dd> Suppress crash recovery.</dl>
</dl>
<dt><code>-script</code><i> file</i></p>
<dd> Execute the script named <i>file</i>. Does not open the X display. This must be the first argument passed to fontforge. Any other arguments are handled by the scriptfile itself. Any other command line arguments will be passed to the script. The program contains a command interpreter which allows access to most but not all of its interactive features. If a scriptfile is executable, and if its first line contains the string &quot;fontforge&quot;, then the argument <code>-script</code> may be omitted. This means that fontforge can be used as an interpreter.</p>
<dt><code>-sync</code></p>
<dd> Make X synchronous. Used primarily for debugging, this option slows X down.</p>
<dt><code>-usage</code></p>
<dd> Display the usage description.</p>
<dt><code>-vc vclass </code></p>
<dd> Attempt to use a visual that matches the class, <i>vclass</i>, specified as either the name of a visual class or an integer enumerating a visual class.</p>
<dt><code>-version</code></p>
<dd> Display the current version (a six digit string containing the date stamp of the source files).</dl>
<h2>ENVIRONMENT</h2>
<p> If any of the following environment variables exist, they are used:</p>
<dl>
<dt><code>BROWSER</code></p>
<dd> Specifies the name of a browser program for examining documentation.</p>
<dt><code>AUTOTRACE</code></p>
<dd> Specifies the location of the autotrace program (usually FontForge can figure this out without help, but not always).</p>
<dt><code>MF</code></p>
<dd> Specifies the location of the metafont program.</p>
<dt><code>FONTFORGE_VERBOSE</code></p>
<dd> Turns on verbose mode in scripting. Each statement is printed as it is executed.</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.FontForge/autosave/</code></p>
<dd> crash recovery directory</p>
<dt><code>/usr/local/share/fontforge/*.ui</code></p>
<dd> translations for the user interface</p>
<dt><code>/usr/local/share/doc/fontforge/*.html</code></p>
<dd> optional location for online documentation.</p>
<dt><code>/usr/local/share/fontforge/*.cidmap</code></p>
<dd> &quot;encoding&quot; files for Adobe&#8217;s cid formats from <a rel="nofollow" href="http://fontforge.sourceforge.net/cidmaps.tgz">http://fontforge.sourceforge.net/cidmaps.tgz</a></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sfddiff/">sfddiff</a></code>(1) </p>
<p> The HTML version of the <i>fontforge</i> manual, available online at:</p>
<dl>
<dt><a rel="nofollow" href="http://fontforge.sourceforge.net/">http://fontforge.sourceforge.net/</a></p>
<dd></dl>
<h2>NOTE</h2>
<p> <code>fontforge</code> used to be called <code>pfaedit.</code></p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2000-2007 by George Williams (gww [at] silcom.com). Original manual page by Tom Harvey, subsequently modified by George Williams. Heavily rewritten and modified to use standard <i>-man</i> (5) macros by R.P.C. Rodgers (rodgers [at] nlm.nih.gov), 23 October 2002.</p>
<h2>BUGS</h2>
<p> Undoubtedly many, but unknown and ever changing. See</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://fontforge.sourceforge.net/#known-bugs">http://fontforge.sourceforge.net/#known-bugs</a> for a current list. </p>
</dl>
<h2>Index</h2>
