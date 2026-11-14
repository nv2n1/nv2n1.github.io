---
title: "extresso(1)"
name: "extresso"
section: "1"
letter: "e"
url: "/docs/linux/man/1-extresso/"
description: "extresso – wrapper for wrestool and icotool"
---

<h2 class="name">NAME</h2>
<p> extresso &#8211; wrapper for wrestool and icotool </p>
<h2>SYNOPSIS</h2>
<p> <code>extresso</code> [<i>OPTIONS</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>extresso</code> command. This manual page was written for the Debian GNU distribution because the original program does not have a manual page. </p>
<p> Extresso reads resource scripts, and uses wrestool to extract the listed resources and icotool to convert them (if necessary).</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;).</p>
<dl>
<dt><code>-o,</code>&#8211;output=DIR</p>
<dd> Where to place extracted files (default `.&#8217;).</p>
<dt><code>&#8211;format=FORMAT</code></p>
<dd> Extraction format of icon resources, passed to icotool.</p>
<dt><code>-b,</code>&#8211;base=DIR</p>
<dd> Base directory of local files in scripts. (This will be appended to &#8220;file&#8221; lines in the scripts.)</p>
<dt><code>-i,</code>&#8211;interactive</p>
<dd> Prompt before extraction.</p>
<dt><code>-v,</code>&#8211;verbose</p>
<dd> Explain what is being done.</p>
<dt><code>&#8211;help</code></p>
<dd> Display a help message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</dl>
<h2>EXAMPLES</h2>
<p> Extract all resources from shell32.dll using the resource script &#8220;win98_shell32&#8221;, assuming it is available in &#8220;/windows/windows/system/shell32.dll&#8221;, and placing output in &#8220;out/&#8221;: </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;extresso ../data/resscripts/win98_shell32 &#8211;base=/windows/windows &#8211;output=out/<br />
&nbsp;<wbr>&nbsp;$&nbsp;find out/&nbsp;-type f | wc -l<br />
&nbsp;<wbr>&nbsp;339<br />
&nbsp;<wbr>&nbsp;$</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-genresscript/">genresscript</a></code>(1), <code><a href="/docs/linux/man/1-icotool/">icotool</a></code>(1), <code><a href="/docs/linux/man/1-wrestool/">wrestool</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Colin Watson &lt;cjwatson [at] debian.org&gt; and Oskar Liljeblad &lt;oskar [at] osk.mine.nu&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Colin Watson </p>
<p> Copyright &#169; 2001 Oskar Liljeblad </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
