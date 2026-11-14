---
title: "radlast(1)"
name: "radlast"
section: "1"
letter: "r"
url: "/docs/linux/man/1-radlast/"
description: "radlast – show \"last\" info from the radwtmp file"
---

<h2>NAME</h2>
<p> radlast &#8211; show &quot;last&quot; info from the radwtmp file</p>
<h2>SYNOPSIS</h2>
<p> <code>radlast</code> <i>[</i>options<i>]</i></p>
<h2>DESCRIPTION</h2>
<p> The FreeRADIUS server can write an accounting log in the <i>wtmp</i> format of the local system. <code>radlast</code> is a frontend for the systems <code>last</code> command &#8211; it just calls <code>last</code> with the <i>-f path_to_radwtmp_file</i> argument, and passes all options on the command line to the system <code>last</code> command.</p>
<h2>OPTIONS</h2>
<p> See the manpage of the system <code>last</code> command.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-radiusd/">radiusd</a>(8), <a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a>(5), <a href="/docs/linux/man/5-wtmp/">wtmp</a>(5), <a href="/docs/linux/man/1-last/">last</a>(1).</p>
<h2>AUTHOR</h2>
<p> Miquel van Smoorenburg, miquels [at] cistron.nl. </p>
<h2>Index</h2>
