---
title: "genresscript(1)"
name: "genresscript"
section: "1"
letter: "g"
url: "/docs/linux/man/1-genresscript/"
description: "genresscript – generate resource script from PE and NE binaries"
---

<h2 class="name">NAME</h2>
<p> genresscript &#8211; generate resource script from PE and NE binaries </p>
<h2>SYNOPSIS</h2>
<p> <code>genresscript</code> [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>genresscript</code> command. This manual page was written for the Debian GNU distribution because the original program does not have a manual page. </p>
<p> Genresscript takes any number of PE or NE binaries, and outputs a resource script with all resources from the binaries listed. (Everything but the destination filename will be filled in in the script.) This is useful when you already have extracted images and want to create a resource script of them.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;type=ID</code></p>
<dd> list resources of this type instead of group_icon</p>
<dt><code>-b</code></p>
<dd>
<dt><code>&#8211;base=PATH</code></p>
<dd> the default extraction name of all resources</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;sort</code></p>
<dd> sort alphabetically instead of using order in binary</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-extresso/">extresso</a></code>(1), <code><a href="/docs/linux/man/1-icotool/">icotool</a></code>(1), <code><a href="/docs/linux/man/1-wrestool/">wrestool</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Colin Watson &lt;cjwatson [at] debian.org&gt; and Oskar Liljeblad &lt;oskar [at] osk.mine.nu&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Colin Watson </p>
<p> Copyright &#169; 2001 Oskar Liljeblad </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
