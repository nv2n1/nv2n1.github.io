---
title: "mkfontdir(1)"
name: "mkfontdir"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkfontdir/"
description: "mkfontdir – create an index of X font files in a directory"
---

<h2 class="name">NAME</h2>
<p> mkfontdir &#8211; create an index of X font files in a directory </p>
<h2>SYNOPSIS</h2>
<p> <code>mkfontdir</code> [<code>-n</code>] [<code>-x</code> <i>suffix</i>] [<code>-r</code>] [<code>-p</code> <i>prefix</i>] [<code>-e</code> <i>encoding-directory-name</i>] &#8230; [<code>&#8212;</code>] [<i>directory-name</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> For each directory argument, <i>mkfontdir</i> reads all of the font files in the directory searching for properties named &quot;FONT&quot;, or (failing that) the name of the file stripped of its suffix. These are converted to lower case and used as font names, and, along with the name of the font file, are written out to the file &quot;fonts.dir&quot; in the directory. The X server and font server use &quot;fonts.dir&quot; to find font files. </p>
<p> The kinds of font files read by <i>mkfontdir</i> depend on configuration parameters, but typically include PCF (suffix &quot;.pcf&quot;), SNF (suffix &quot;.snf&quot;) and BDF (suffix &quot;.bdf&quot;). If a font exists in multiple formats, <i>mkfontdir</i> will first choose PCF, then SNF and finally BDF. </p>
<p> The first line of fonts.dir gives the number of fonts in the file. The remaining lines list the fonts themselves, one per line, in two fields. First is the name of the font file, followed by a space and the name of the font.</p>
<h2>SCALABLE FONTS</h2>
<p> Because scalable font files do not usually include the X font name, the file &quot;fonts.scale&quot; can be used to name the scalable fonts in the directory. The fonts listed in it are copied to fonts.dir by <i>mkfontdir</i>. &quot;fonts.scale&quot; has the same format as the &quot;fonts.dir&quot; file, and can be created with the <i><a href="/docs/linux/man/1-mkfontscale/">mkfontscale</a></i>(1) program.</p>
<h2>FONT NAME ALIASES</h2>
<p> The file &quot;fonts.alias&quot;, which can be put in any directory of the font-path, is used to map new names to existing fonts, and should be edited by hand. The format is two white-space separated columns, the first containing aliases and the second containing font-name patterns. Lines beginning with &quot;!&quot; are comment lines and are ignored. </p>
<p> If neither the alias nor the value specifies the size fields of the font name, this is a scalable alias. A font name of any size that matches this alias will be mapped to the same size of the font that the alias resolves to. </p>
<p> When a font alias is used, the name it references is searched for in the normal manner, looking through each font directory in turn. This means that the aliases need not mention fonts in the same directory as the alias file. </p>
<p> To embed white space in either name, simply enclose it in double-quote marks; to embed double-quote marks (or any other character), precede them with back-slash: </p>
<pre>
&quot;magic-alias with spaces&quot;       &quot;\&quot;font name\&quot; with quotes&quot;
regular-alias                   fixed
</pre>
<p> If the string &quot;FILE_NAMES_ALIASES&quot; stands alone on a line, each file-name in the directory (stripped of its suffix) will be used as an alias for that font.</p>
<h2>ENCODING FILES</h2>
<p> The option <code>-e</code> can be used to specify a directory with encoding files. Every such directory is scanned for encoding files, the list of which is then written to an &quot;encodings.dir&quot; file in every font directory. The &quot;encodings.dir&quot; file is used by the server to find encoding information. </p>
<p> The &quot;encodings.dir&quot; file has the same format as &quot;fonts.dir&quot;. It maps encoding names (strings of the form <code>CHARSET_REGISTRY</code><i>&#8211;</i><code>CHARSET_ENCODING</code> ) to encoding file names.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-e</code></p>
<dd> Specify a directory containing encoding files. The <code>-e</code> option may be specified multiple times, and all the specified directories will be read. The order of the entries is significant, as encodings found in earlier directories override those in later ones; encoding files in the same directory are discriminated by preferring compressed versions.</p>
<dt><code>-n</code></p>
<dd> do not scan for fonts, do not write font directory files. This option is useful when generating encoding directories only.</p>
<dt><code>-p</code></p>
<dd> Specify a prefix that is prepended to the encoding file path names when they are written to the &quot;encodings.dir&quot; file. The prefix is prepended as-is. If a `/&#8217; is required between the prefix and the path names, it must be supplied explicitly as part of the prefix.</p>
<dt><code>-r</code></p>
<dd> Keep non-absolute encoding directories in their relative form when writing the &quot;encodings.dir&quot; file. The default is to convert relative encoding directories to absolute directories by prepending the current directory. The positioning of this options is significant, as this option only applies to subsequent <code>-e</code> options.</p>
<dt><code>-x </code><i>suffix</i></p>
<dd> Ignore fonts files of type <i>suffix</i>.</p>
<dt><code>&#8212;</code></p>
<dd> End options.</dl>
<h2>FILES</h2>
<dl>
<dt><code>fonts.dir</code></p>
<dd> List of fonts in the directory and the files they are stored in. Created by <i>mkfontdir</i>. Read by the X server and font server each time the font path is set (see <a href="/docs/linux/man/1-xset/">xset</a>(1)).</p>
<dt><code>fonts.scale</code></p>
<dd> List of scalable fonts in the directory. Contents are copied to fonts.dir by <i>mkfontdir</i>. Can be created with <i><a href="/docs/linux/man/1-mkfontscale/">mkfontscale</a></i>(1).</p>
<dt><code>fonts.alias</code></p>
<dd> List of font name aliases. Read by the X server and font server each time the font path is set (see <a href="/docs/linux/man/1-xset/">xset</a>(1)).</p>
<dt><code>encodings.dir</code></p>
<dd> List of known encodings and the files they are stored in. Created by <i>mkfontdir</i>. Read by the X server and font server each time a font with an unknown charset is opened.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/1-mkfontscale/">mkfontscale</a>(1), <a href="/docs/linux/man/1-xfs/">xfs</a>(1), <a href="/docs/linux/man/1-xset/">xset</a>(1) </p>
<h2>Index</h2>
