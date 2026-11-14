---
title: "mkfontscale(1)"
name: "mkfontscale"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkfontscale/"
description: "mkfontscale – create an index of scalable font files for X"
---

<h2 class="name">NAME</h2>
<p> mkfontscale &#8211; create an index of scalable font files for X </p>
<h2>SYNOPSIS</h2>
<p> <code>mkfontscale</code> [ <code>-b</code> ] [ <code>-s</code> ] [ <code>-o</code> <i>filename</i> ] [ <code>-x</code> <i>suffix</i> ] [ <code>-a</code> <i>encoding</i> ] &#8230; [ <code>-f</code> <i>fuzz</i> ] [ <code>-l</code> ] [ <code>-e</code> <i>directory</i> ] [ <code>-p</code> <i>prefix</i> ] [ <code>-r</code> <i>prefix</i> ] [ <code>-n</code> <i>prefix</i> ] [ <code>-u | -U</code> ] [ <code>-v</code> ] [ <code>&#8212;</code> ] [ <i>directory</i> ] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> For each directory argument, <i>mkfontscale</i> reads all of the scalable font files in the directory. For every font file found, an X11 font name (XLFD) is generated, and is written together with the file name to a file <code>fonts.scale</code> in the directory. </p>
<p> The resulting <code>fonts.scale</code> file should be checked and possibly manually edited before being used as input for the <code><a href="/docs/linux/man/1-mkfontdir/">mkfontdir</a></code>(1) program.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> read bitmap fonts. By default, bitmap fonts are ignored.</p>
<dt><code>-s</code></p>
<dd> ignore scalable fonts. By default, scalable fonts are read. If <code>-b</code> is set, this flag has the side effect of enabling the reading of <code>fonts.scale</code> files.</p>
<dt><code>-o</code><i> filename</i></p>
<dd> send program output to <i>filename</i>; default is <code>fonts.scale</code> if bitmap fonts are not being read, and <code>fonts.dir</code> if they are. If <i>filename</i> is relative, it is created in the directory being processed. If it is the special value <code>&#8211;</code>, output is written to standard output.</p>
<dt><code>-x</code><i> suffix</i></p>
<dd> exclude all files with the specified <i>suffix</i>.</p>
<dt><code>-a</code><i> encoding</i></p>
<dd> add <i>encoding</i> to the list of encodings searched for.</p>
<dt><code>-f</code><i> fuzz</i></p>
<dd> set the fraction of characters that may be missing in large encodings to <i>fuzz</i> percent. Defaults to 2%.</p>
<dt><code>-l</code></p>
<dd> Write <code>fonts.dir</code> files suitable for implementations that cannot reencode legacy fonts (BDF and PCF). By default, it is assumed that the implementation can reencode Unicode-encoded legacy fonts.</p>
<dt><code>-e</code></p>
<dd> specifies a directory with encoding files. Every such directory is scanned for encoding files, the list of which is then written to an &quot;encodings.dir&quot; file in every font directory.</p>
<dt><code>-p</code></p>
<dd> Specifies a prefix that is prepended to the encoding file path names when they are written to the &quot;encodings.dir&quot; file. The prefix is prepended literally: if a `/&#8217; is required between the prefix and the path names, it must be supplied explicitly as part of the prefix.</p>
<dt><code>-r</code></p>
<dd> Keep non-absolute encoding directories in their relative form when writing the &quot;encodings.dir&quot; file. The default is to convert relative encoding directories to absolute directories by prepending the current directory. The positioning of this options is significant, as this option only applies to subsequent <code>-e</code> options.</p>
<dt><code>-n</code></p>
<dd> do not scan for fonts, do not write font directory files. This option is useful when generating encoding directories only.</p>
<dt><code>-u, -U</code></p>
<dd> disable (<i>-u</i>) or enable (<i>-U</i>) indexing of ISO 10646:1 font encodings (default: enabled).</p>
<dt><code>-v</code></p>
<dd> print program version and exit.</p>
<dt><code>&#8212;</code></p>
<dd> end of options.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/1-mkfontdir/">mkfontdir</a>(1), <a href="/docs/linux/man/1-ttmkfdir/">ttmkfdir</a>(1), <a href="/docs/linux/man/1-xfs/">xfs</a>(1), <a href="/docs/linux/man/1-xset/">xset</a>(1)</p>
<h2>NOTES</h2>
<p> The format of the <code>fonts.scale</code>, <code>fonts.dir</code> and <code>encodings.dir</code> files is documented in the <a href="/docs/linux/man/1-mkfontdir/">mkfontdir</a>(1) manual page. </p>
<p> <code>Mkfontscale</code> will overwrite any <code>fonts.scale</code> file even if it has been hand-edited. </p>
<p> <code>mkfontscale -b -s -l</code> is equivalent to <code>mkfontdir</code>.</p>
<h2>AUTHOR</h2>
<p> The version of <code>mkfontscale</code> included in this X.Org Foundation release was originally written by Juliusz Chroboczek &lt;jch [at] freedesktop.org&gt; for the XFree86 project. The functionality of this program was inspired by the <code>ttmkfdir</code> utility by Joerg Pommnitz. </p>
<h2>Index</h2>
