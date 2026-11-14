---
title: "fslsfonts(1)"
name: "fslsfonts"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fslsfonts/"
description: "fslsfonts – list fonts served by X font server"
---

<h2 class="name">NAME</h2>
<p> fslsfonts &#8211; list fonts served by X font server </p>
<h2>SYNOPSIS</h2>
<p> <code>fslsfonts</code> [-options &#8230;] [-fn pattern]</p>
<h2>DESCRIPTION</h2>
<p> <i>fslsfonts</i> lists the fonts that match the given <i>pattern</i>. The wildcard character &quot;*&quot; may be used to match any sequence of characters (including none), and &quot;?&quot; to match any single character. If no pattern is given, &quot;*&quot; is assumed. </p>
<p> The &quot;*&quot; and &quot;?&quot; characters must be quoted to prevent them from being expanded by the shell.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-server </code><i>servername</i></p>
<dd> This option specifies the X font server to contact. <i>servername</i> must be specified in one of the formats defined in the <i>Font Server Names</i> section of <a href="/docs/linux/man/7-x/">X</a>(7). If not specified, the server name in the <code>FONTSERVER</code> environment variable is used.</dl>
<dl>
<dt><code>-l</code></p>
<dd> Lists some attributes of the font on one line in addition to its name.</p>
<dt><code>-ll</code></p>
<dd> Lists font properties in addition to <code>-l</code> output.</p>
<dt><code>-lll</code></p>
<dd> Supported for compatibility with <i>xlsfonts</i>, but output is the same as for <code>-ll</code>.</p>
<dt><code>-m</code></p>
<dd> This option indicates that long listings should also print the minimum and maximum bounds of each font.</p>
<dt><code>-C</code></p>
<dd> This option indicates that listings should use multiple columns. This is the same as <code>-n 0</code>.</p>
<dt><code>-1</code></p>
<dd> This option indicates that listings should use a single column. This is the same as <code>-n 1</code>.</p>
<dt><code>-w </code><i>width</i></p>
<dd> This option specifies the width in characters that should be used in figuring out how many columns to print. The default is 79.</p>
<dt><code>-n </code><i>columns</i></p>
<dd> This option specifies the number of columns to use in displaying the output. The default is 0, which will attempt to fit as many columns of font names into the number of character specified by <code>-w</code> <i>width</i>.</p>
<dt><code>-u</code></p>
<dd> This option indicates that the output should be left unsorted.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>FONTSERVER</code></p>
<dd> To get the default fontserver. The server name must be specified in one of the formats defined in the <i>Font Server Names</i> section of <a href="/docs/linux/man/7-x/">X</a>(7).</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xfs/">xfs</a>(1), <a href="/docs/linux/man/1-showfont/">showfont</a>(1), <a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<h2>BUGS</h2>
<p> Doing &#8220;fslsfonts -l&#8221; can tie up your server for a very long time. This is really a bug with single-threaded non-preemptable servers, not with this program.</p>
<h2>AUTHOR</h2>
<p> Dave Lemke, Network Computing Devices, Inc </p>
<h2>Index</h2>
