---
title: "glxheads(1)"
name: "glxheads"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glxheads/"
description: "glxheads – exercise multiple GLX connections"
---

<h2 class="name">NAME</h2>
<p> glxheads &#8211; exercise multiple GLX connections </p>
<h2>SYNOPSIS</h2>
<p> <code>glxheads</code> [<i>display</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <i>glxheads</i> program will try to open GLX connections on multiple X displays as specified on the command-line. If a connection can be made it will try to create a direct GLX context (and fallback to using indirect contexts if that fails) and open a window displaying a spinning green triangle. </p>
<p> If no display names are specified, <i>glxheads</i> will default to opening a single local connection on display 0.</p>
<h2>EXAMPLE</h2>
<p> To open a local connection on display 0 and two remote connections to the hosts <i>mars</i> (display 0) and <i>venus</i> (display 1), run glxheads with the following command-line: </p>
<dl>
<dt>
<dd>
<pre>
$ glxheads :0 mars:0 venus:1
</pre>
</dl>
<h2>AUTHOR</h2>
<p> glxheads was written by Brian Paul &lt;brian.paul [at] tungstengraphics.com&gt;. </p>
<p> This manual page was written by Thierry Reding &lt;thierry [at] gilfi.de&gt; for the Debian project (but may be used by others). </p>
<h2>Index</h2>
