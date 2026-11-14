---
title: "prunehistory(8)"
name: "prunehistory"
section: "8"
letter: "p"
url: "/docs/linux/man/8-prunehistory/"
description: "prunehistory – Remove tokens from Usenet history file"
---

<p>prunehistory &#8211; Remove tokens from Usenet history file</p>
<h2>Synopsis</h2>
<p><code>prunehistory</code> [<code>-p</code>] [<code>-f</code> <i>filename</i>]</p>
<h2>Description</h2>
<p><code>prunehistory</code> modifies a <i><a href="/docs/linux/man/5-history/">history</a></i>(5)-format text file to &#8220;remove&#8221; a set of tokens from it. The tokens are removed by overwriting them with spaces, so that the size and position of any following entries does not change. This has an effect similar to expiring the article, in that it is still mentioned in the history database but cannot be retrieved. </p>
<p> <code>prunehistory</code> reads the standard input. The input is taken as a set of lines. Blank lines and lines starting with a number sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines should consist of a message-ID followed by zero or more other fields (which are ignored). The message-ID is used as the <i><a href="/docs/linux/man/3-dbz/">dbz</a></i>(3) key to get an offset into the text file. Since <code>innd</code> only appends to the text file, <code>prunehistory</code> does not need to have any interaction with it.</p>
<h2>Options</h2>
<dl>
<dt><code>-p</code></p>
<dd><code>prunehistory</code> will normally complain about lines that do not follow the correct format. If the <code>-p</code> flag is used, then the program will silently print any invalid lines on its standard output. (Blank lines and comment lines are also passed through.)</p>
<dt><code>-f</code> <i>filename</i></p>
<dd>The default name of the <i>history</i> file is <i>pathdb</i>/history; to specify a different name, use the <code>-f</code> flag.</dl>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> prunehistory.pod 9448 2012-12-07 19:01:58Z eagle $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/3-dbz/">dbz</a></i>(3), <i><a href="/docs/linux/man/5-history/">history</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8). </p>
