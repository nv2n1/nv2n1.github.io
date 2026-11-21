---

title: "mkfontscale(1)"
name: "mkfontscale"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkfontscale/"
description: "mkfontscale – create an index of scalable font files for X"
---

<p> <code>mkfontscale</code> [ <code>-b</code> ] [ <code>-s</code> ] [ <code>-o</code> <i>filename</i> ] [ <code>-x</code> <i>suffix</i> ] [ <code>-a</code> <i>encoding</i> ] &#8230; [ <code>-f</code> <i>fuzz</i> ] [ <code>-l</code> ] [ <code>-e</code> <i>directory</i> ] [ <code>-p</code> <i>prefix</i> ] [ <code>-r</code> <i>prefix</i> ] [ <code>-n</code> <i>prefix</i> ] [ <code>-u | -U</code> ] [ <code>-v</code> ] [ <code>&#8212;</code> ] [ <i>directory</i> ] &#8230;</p>
<p> For each directory argument, <i>mkfontscale</i> reads all of the scalable font files in the directory. For every font file found, an X11 font name (XLFD) is generated, and is written together with the file name to a file <code>fonts.scale</code> in the directory. </p>
<p> The resulting <code>fonts.scale</code> file should be checked and possibly manually edited before being used as input for the <code><a href="/docs/linux/man/1-mkfontdir/">mkfontdir</a></code>(1) program.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd> read bitmap fonts. By default, bitmap fonts are ignored.</dd>
<dt><code>-s</code></dt>
<dd> ignore scalable fonts. By default, scalable fonts are read. If <code>-b</code> is set, this flag has the side effect of enabling the reading of <code>fonts.scale</code> files.</dd>
<dt><code>-o</code><i> filename</i></dt>
<dd> send program output to <i>filename</i>; default is <code>fonts.scale</code> if bitmap fonts are not being read, and <code>fonts.dir</code> if they are. If <i>filename</i> is relative, it is created in the directory being processed. If it is the special value <code>&#8211;</code>, output is written to standard output.</dd>
<dt><code>-x</code><i> suffix</i></dt>
<dd> exclude all files with the specified <i>suffix</i>.</dd>
<dt><code>-a</code><i> encoding</i></dt>
<dd> add <i>encoding</i> to the list of encodings searched for.</dd>
<dt><code>-f</code><i> fuzz</i></dt>
<dd> set the fraction of characters that may be missing in large encodings to <i>fuzz</i> percent. Defaults to 2%.</dd>
<dt><code>-l</code></dt>
<dd> Write <code>fonts.dir</code> files suitable for implementations that cannot reencode legacy fonts (BDF and PCF). By default, it is assumed that the implementation can reencode Unicode-encoded legacy fonts.</dd>
<dt><code>-e</code></dt>
<dd> specifies a directory with encoding files. Every such directory is scanned for encoding files, the list of which is then written to an &quot;encodings.dir&quot; file in every font directory.</dd>
<dt><code>-p</code></dt>
<dd> Specifies a prefix that is prepended to the encoding file path names when they are written to the &quot;encodings.dir&quot; file. The prefix is prepended literally: if a `/&#8217; is required between the prefix and the path names, it must be supplied explicitly as part of the prefix.</dd>
<dt><code>-r</code></dt>
<dd> Keep non-absolute encoding directories in their relative form when writing the &quot;encodings.dir&quot; file. The default is to convert relative encoding directories to absolute directories by prepending the current directory. The positioning of this options is significant, as this option only applies to subsequent <code>-e</code> options.</dd>
<dt><code>-n</code></dt>
<dd> do not scan for fonts, do not write font directory files. This option is useful when generating encoding directories only.</dd>
<dt><code>-u, -U</code></dt>
<dd> disable (<i>-u</i>) or enable (<i>-U</i>) indexing of ISO 10646:1 font encodings (default: enabled).</dd>
<dt><code>-v</code></dt>
<dd> print program version and exit.</dd>
<dt><code>&#8212;</code></dt>
<dd> end of options.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/1-mkfontdir/">mkfontdir</a>(1), <a href="/docs/linux/man/1-ttmkfdir/">ttmkfdir</a>(1), xfs(1), <a href="/docs/linux/man/1-xset/">xset</a>(1)</p>
<h2>NOTES</h2>
<p> The format of the <code>fonts.scale</code>, <code>fonts.dir</code> and <code>encodings.dir</code> files is documented in the <a href="/docs/linux/man/1-mkfontdir/">mkfontdir</a>(1) manual page. </p>
<p> <code>Mkfontscale</code> will overwrite any <code>fonts.scale</code> file even if it has been hand-edited. </p>
<p> <code>mkfontscale -b -s -l</code> is equivalent to <code>mkfontdir</code>.</p>
<h2>AUTHOR</h2>
<p> The version of <code>mkfontscale</code> included in this X.Org Foundation release was originally written by Juliusz Chroboczek &lt;jch [at] freedesktop.org&gt; for the XFree86 project. The functionality of this program was inspired by the <code>ttmkfdir</code> utility by Joerg Pommnitz. </p>
