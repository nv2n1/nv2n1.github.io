---

title: "fontforge(1)"
name: "fontforge"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fontforge/"
description: "fontforge – create and modify PostScript, TrueType and SVG fonts"
---

<p> <code>fontforge &#8211; create and modify PostScript, TrueType and SVG fonts</code></p>
<h2>SYNOPSIS</h2>
<p> <code>fontforge</code> [<code>-c</code> <i>string</i>] [<code>-cmap</code> <i>maptype</i>] [<code>-depth</code> <i>pixeld</i>] [<code>-display</code> <i>str</i>] [<code>-lang=ff</code>] [<code>-lang=py</code>] [<code>-last</code>] [<code>-library-status</code>] [<code>-help</code>] [<code>-keyboard</code> <i>ktype</i>] [<code>-new</code>] [<code>-nosplash</code>] [<code>-recover</code> <i>mode</i>] [<code>-script</code> <i>file</i>] [<code>-sync</code>] [<code>-usage</code>] [<code>-vc</code> <i>vclass</i>] [<code>-version</code>] <i>fontfile &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The program <i>fontforge</i> allows you to create and modify font files, accepting input in the following formats (with associated file extensions appearing in parentheses):</p>
<dl>
<dt>Glyph Bitmap Distribution (.bdf)</dt>
<dd>
</dd><dt>Macintosh resource fonts (.dfont, .bin, .hqx)</dt>
<dd>
</dd><dt>OpenType (.otf)</dt>
<dd>
</dd><dt><i>fontforge</i> spline font database (.sfd)</dt>
<dd>
</dd><dt>POSTSCRIPT, which includes:</dt>
<dd>
</dd><dl>
<dl>
<dt>ASCII format (.pfa)</dt>
<dd>
</dd><dt>Binary format (.pfb)</dt>
<dd>
</dd><dt>CID-keyed fonts, Adobe convention used primarily for Asian characters (.cid, .otf)</dt>
<dd>
</dd><dt>POSTSCRIPT Type 0 (.ps)</dt>
<dd>
</dd><dt>POSTSCRIPT Type 3 (.ps)</dt>
<dd></dd></dl>
</dl>
<dt>Scaleable vector graphics fonts (.svg)</dt>
<dd>
</dd><dt>TeX bitmap (.pk)</dt>
<dd>
</dd><dt>TrueType (.ttf, .ttc)</dt>
<dd>
</dd><dt>X11 bitmap (.pcf)</dt>
<dd></dd></dl>
<p> If the argument list contains a font file name (or several), <i>fontforge</i> opens a <code>fontview</code> window for each font displaying the characters of the that font. In the absence of options or arguments, the program opens a file-picker window, allowing you to browse your disk to find a font file, or create a new one. </p>
<p> This manual page is intended only as a rudimentary overview; see the HTML Users Manual for more complete information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code><i> string</i></dt>
<dd> Must be the first argument. Executes &quot;string&quot; as a set of scripting commands. Any additional arguments will be passed to the script.</dd>
<dt><code>-cmap</code><i> maptype</i></dt>
<dd> Employ the specified method to control 8-bit colormaps, where <i>maptype</i> assumes one of these three values:</dd>
<dl>
<dl>
<dt><code>current</code></dt>
<dd> Attempt to allocate colors in the current (shared) colormap. The program will likely not find everything it requires.</dd>
<dt><code>copy</code></dt>
<dd> Allocate what can be allocated, then copy the current colormap; it can thus make use of cells other programs are using.</dd>
<dt><code>private</code></dt>
<dd> Create a new colormap and fill it with the required colors.</dd></dl>
</dl>
<dt><code>-depth</code><i> pixeld</i></dt>
<dd> Attempt to employ a visual that matches the specified pixel depth, <i>pixeld</i>.</dd>
<dt><code>-display</code><i> str</i></dt>
<dd> Employ the X display specified by the string <i>str</i> (for example: localhost:0).</dd>
<dt><code>-help</code></dt>
<dd> Display the usage description and start a web client displaying the online documentation.</dd>
<dt><code>-keyboard</code><i> ktype</i></dt>
<dd> Alter the displayed menus to employ modifier keys appropriate to the specified keyboard type, where <i>ktype</i> assumes one of the following four values:</dd>
<dl>
<dl>
<dt><code>ibm</code></dt>
<dd> IBM PC type keyboard.</dd>
<dt><code>mac</code></dt>
<dd> Apple Macintosh keyboard.</dd>
<dt><code>sun</code></dt>
<dd> Sun workstation keyboard.</dd>
<dt><code>ppc</code></dt>
<dd> Macintosh keyboard, but on a system running SuSe linux (the mappings differ from those used under MacOS X).</dd></dl>
</dl>
<dt><code>-last</code></dt>
<dd> Opens whatever font you last edited with <i>fontforge.</i> If you specify <i>n</i> <code>-last</code> <i>fontforge</i> will open the last <i>n</i> fonts.</dd>
<dt><code>-lang=ff</code></dt>
<dd> Interpret the script with the fontforge interpreter.</dd>
<dt><code>-lang=py</code></dt>
<dd> Interpret the script with the python interpreter.</dd>
<dt><code>-library-status</code></dt>
<dd> Prints information about optional libraries.</dd>
<dt><code>-new</code></dt>
<dd> Create a new font with the ISO 8859-1 encoding (the international encoding standard for western Europe, and the standard for most X fonts).</dd>
<dt><code>-nosplash</code></dt>
<dd> Suppress display of the splash screen.</dd>
<dt><code>-recover</code><i> mode</i></dt>
<dd> Control the crash recovery mechanism (helpful if crash recovery causes problems), where <i>mode</i> takes on one of three allowed settings:</dd>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd> perform automatic recovery (default) if the program crashed before saving changes.</dd>
<dt><code>clean</code></dt>
<dd> Delete recovery information.</dd>
<dt><code>none</code></dt>
<dd> Suppress crash recovery.</dd></dl>
</dl>
<dt><code>-script</code><i> file</i></dt>
<dd> Execute the script named <i>file</i>. Does not open the X display. This must be the first argument passed to fontforge. Any other arguments are handled by the scriptfile itself. Any other command line arguments will be passed to the script. The program contains a command interpreter which allows access to most but not all of its interactive features. If a scriptfile is executable, and if its first line contains the string &quot;fontforge&quot;, then the argument <code>-script</code> may be omitted. This means that fontforge can be used as an interpreter.</dd>
<dt><code>-sync</code></dt>
<dd> Make X synchronous. Used primarily for debugging, this option slows X down.</dd>
<dt><code>-usage</code></dt>
<dd> Display the usage description.</dd>
<dt><code>-vc vclass </code></dt>
<dd> Attempt to use a visual that matches the class, <i>vclass</i>, specified as either the name of a visual class or an integer enumerating a visual class.</dd>
<dt><code>-version</code></dt>
<dd> Display the current version (a six digit string containing the date stamp of the source files).</dd></dl>
<h2>ENVIRONMENT</h2>
<p> If any of the following environment variables exist, they are used:</p>
<dl>
<dt><code>BROWSER</code></dt>
<dd> Specifies the name of a browser program for examining documentation.</dd>
<dt><code>AUTOTRACE</code></dt>
<dd> Specifies the location of the autotrace program (usually FontForge can figure this out without help, but not always).</dd>
<dt><code>MF</code></dt>
<dd> Specifies the location of the metafont program.</dd>
<dt><code>FONTFORGE_VERBOSE</code></dt>
<dd> Turns on verbose mode in scripting. Each statement is printed as it is executed.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.FontForge/autosave/</code></dt>
<dd> crash recovery directory</dd>
<dt><code>/usr/local/share/fontforge/*.ui</code></dt>
<dd> translations for the user interface</dd>
<dt><code>/usr/local/share/doc/fontforge/*.html</code></dt>
<dd> optional location for online documentation.</dd>
<dt><code>/usr/local/share/fontforge/*.cidmap</code></dt>
<dd> &quot;encoding&quot; files for Adobe&#8217;s cid formats from <a rel="nofollow" href="http://fontforge.sourceforge.net/cidmaps.tgz">http://fontforge.sourceforge.net/cidmaps.tgz</a></dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sfddiff/">sfddiff</a></code>(1) </p>
<p> The HTML version of the <i>fontforge</i> manual, available online at:</p>
<dl>
<dt><a rel="nofollow" href="http://fontforge.sourceforge.net/">http://fontforge.sourceforge.net/</a></dt>
<dd></dd></dl>
<h2>NOTE</h2>
<p> <code>fontforge</code> used to be called <code>pfaedit.</code></p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2000-2007 by George Williams (gww [at] silcom.com). Original manual page by Tom Harvey, subsequently modified by George Williams. Heavily rewritten and modified to use standard <i>-man</i> (5) macros by R.P.C. Rodgers (rodgers [at] nlm.nih.gov), 23 October 2002.</p>
<h2>BUGS</h2>
<p> Undoubtedly many, but unknown and ever changing. See</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://fontforge.sourceforge.net/#known-bugs">http://fontforge.sourceforge.net/#known-bugs</a> for a current list. </dd>
</dl>
