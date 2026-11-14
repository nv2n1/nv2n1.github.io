---
title: "pbmupc(1)"
name: "pbmupc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmupc/"
description: "pbmupc – create a Universal Product Code bitmap"
---

<h2 class="name">NAME</h2>
<p> pbmupc &#8211; create a Universal Product Code bitmap </p>
<h2>SYNOPSIS</h2>
<p> <code>pbmupc</code> [<code>-s1</code>|<code>-s2</code>] <i>type manufac product</i></p>
<h2>DESCRIPTION</h2>
<p> Generates a Universal Product Code symbol. The three arguments are: a one digit product type, a five digit manufacturer code, and a five digit product code. For example, &quot;0 72890 00011&quot; is the code for Heineken. </p>
<p> As presently configured, <i>pbmupc</i> produces a bitmap 230 bits wide and 175 bits high. The size can be altered by changing the defines at the beginning of the program, or by running the output through <i>pnmenlarge</i> or <i>pnmscale</i>.</p>
<h2>OPTIONS</h2>
<p> The <code>-s1</code> and <code>-s2</code> flags select the style of UPC to generate. The default, <code>-s1</code>, looks more or less like this: </p>
<pre><code>
|| || || || || || || ||
    || || || || || || || ||
    || || || || || || || ||
    || || || || || || || ||
    0 || 12345 || 67890 || 5
</code></pre>
<p> The other style, <code>-s2</code>, puts the product type digit higher up, and doesn&#8217;t display the checksum digit: </p>
<pre><code>
|| || || || || || || ||
    || || || || || || || ||
    0 || || || || || || || ||
    || || || || || || || ||
    || 12345 || 67890 ||
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
