---
title: "isogmt(1)"
name: "isogmt"
section: "1"
letter: "i"
url: "/docs/linux/man/1-isogmt/"
description: "isogmt – Run GMT command or script in isolation mode"
---

<h2>NAME</h2>
<p> isogmt &#8211; Run GMT command or script in isolation mode</p>
<h2>SYNOPSIS</h2>
<p> <code>isogmt</code> <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> <code>isogmt</code> runs a single GMT command or shell script in <code>isolation mode</code>. This means that the files <i>gmt.history</i> and <i>gmt.conf</i> will be read from the usual locations (current directory, <i>~/.gmt</i>, or home directory), but changes will only be written in a temporary directory, which will be removed after execution. The name of the temporary directory will be available to the command or script as the environment variable GMT_TMPDIR.</p>
<h2>EXAMPLES</h2>
<p> Run the shell script <i>script.gmt</i> in isolation mode isogmt sh script.gmt</p>
<h2>SEE ALSO</h2>
<p> <code>gmt</code>, <code>gmt.conf</code></p>
<h2>COPYRIGHT</h2>
<p> 2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe </p>
<h2>Index</h2>
