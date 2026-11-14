---
title: "unxrandr(1)"
name: "unxrandr"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unxrandr/"
description: "unxrandr – inverse tool of xrandr"
---

<h2>NAME</h2>
<p> unxrandr &#8211; inverse tool of xrandr</p>
<h2>SYNOPSIS</h2>
<p> <code>unxrandr</code></p>
<h2>DESCRIPTION</h2>
<p> <code>unxrandr</code> is a tool that queries the XRandR state using ARandR&#8217;s libraries and outputs an <code>xrandr</code> command line that reproduces the state (as far as it is supported by the library). </p>
<p> The command sh -c &quot;<i>unxrandr</i>&quot; </p>
<p> should never modify the configured state. </p>
<p> It takes no options apart from <code>&#8211;help</code> and <code>&#8211;version</code>.</p>
<h2>SEE ALSO</h2>
<p> <code>man 1 arandr</code></p>
<h2>AUTHOR</h2>
<p> chrysn &lt;chrysn [at] fsfe.org&gt; </p>
<h2>Index</h2>
