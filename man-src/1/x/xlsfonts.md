---
title: "xlsfonts(1)"
name: "xlsfonts"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xlsfonts/"
description: "xlsfonts – server font list displayer for X"
---

<h2 class="name">NAME</h2>
<p> xlsfonts &#8211; server font list displayer for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xlsfonts</code> [<code>-display host:dpy</code>] [<code>-l</code>] [<code>-ll</code>] [<code>-lll</code>] [<code>-m</code>] [<code>-C</code>] [<code>-1</code>] [<code>-w width</code>] [<code>-n columns</code>] [<code>-u</code>] [<code>-o</code>] [<code>-fn pattern</code>] [<code>-v</code>]</p>
<h2>DESCRIPTION</h2>
<p> xlsfonts lists the fonts that match the given pattern. The wildcard character &quot;*&quot; may be used to match any sequence of characters (including none), and &quot;?&quot; to match any single character. If no pattern is given, &quot;*&quot; is assumed. </p>
<p> The &quot;*&quot; and &quot;?&quot; characters must be quoted to prevent them from being expanded by the shell.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>host:dpy</i></p>
<dd> This option specifies the X server to contact.</p>
<dt><code>-d </code><i>host:dpy</i></p>
<dd> Same as <code>-display </code><i>host:dpy</i>.</p>
<dt><code>-l</code></p>
<dd> Lists some attributes of the font on one line in addition to its name.</p>
<dt><code>-ll</code></p>
<dd> Lists font properties in addition to <code>-l</code> output.</p>
<dt><code>-lll</code></p>
<dd> Lists character metrics in addition to <code>-ll</code> output.</p>
<dt><code>-m</code></p>
<dd> This option indicates that long listings should also print the minimum and maximum bounds of each font.</p>
<dt><code>-C</code></p>
<dd> This option indicates that listings should use multiple columns. This is the same as <code>-n 0</code>.</p>
<dt><code>-1</code></p>
<dd> This option indicates that listings should use a single column. This is the same as <code>-n 1</code>.</p>
<dt><code>-w </code><i>width</i></p>
<dd> This option specifies the width in characters that should be used in figuring out how many columns to print. The default is 79.</p>
<dt><code>-n </code><i>columns</i></p>
<dd> This option specifies the number of columns to use in displaying the output. By default, it will attempt to fit as many columns of font names into the number of character specified by <code>-w</code> width.</p>
<dt><code>-u</code></p>
<dd> This option indicates that the output should be left unsorted.</p>
<dt><code>-o</code></p>
<dd> This option indicates that xlsfonts should do an OpenFont (and QueryFont, if appropriate) rather than a ListFonts. This is useful if ListFonts or ListFontsWithInfo fail to list a known font (as is the case with some scaled font systems).</p>
<dt><code>-fn </code><i>pattern</i></p>
<dd> This option specifies the font name pattern to match.</p>
<dt><code>-v</code></p>
<dd> This option indicates that xlsfonts should print out the program version and exit.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1), <code><a href="/docs/linux/man/1-xset/">xset</a></code>(1), <code><a href="/docs/linux/man/1-xfd/">xfd</a></code>(1), X Logical Font Description Conventions</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> <code>DISPLAY</code> must be set to get the default host and display to use.</dl>
<h2>BUGS</h2>
<p> Doing &#8220;xlsfonts -l&#8221; can tie up your server for a very long time. This is really a bug with single-threaded non-preemptable servers, not with this program.</p>
<h2>AUTHOR</h2>
<p> Mark Lillibridge </p>
<p> Jim Fulton </p>
<p> Phil Karlton </p>
<p> Roland Mainz </p>
<h2>Index</h2>
