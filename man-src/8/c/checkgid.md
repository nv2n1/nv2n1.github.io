---
title: "checkgid(8)"
name: "checkgid"
section: "8"
letter: "c"
url: "/docs/linux/man/8-checkgid/"
description: "checkgid – checks the gid"
---

<p>checkgid &#8211; checks the gid</p>
<h2>Synopsis</h2>
<p><code>checkgid group </code></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>checkgid </code> command. </p>
<p> <code>checkgid</code> is a program that checks whether it can setgid to the group specified. This is to see if it is a valid group for apache2 to use at runtime. If the user (should be run as superuser) is in that group, or can setgid to it, it will return 0.</p>
<h2>Author</h2>
<p>This manual page was written by Daniel Stone &lt;daniel [at] sfarc.net&gt; for the Debian GNU/Linux distribution, as the original did not have a manpage.</p>
