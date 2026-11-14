---
title: "clc-clbuild(1)"
name: "clc-clbuild"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clc-clbuild/"
description: "clc-clbuild – clc enabled clbuild wrapper"
---

<h2 class="name">NAME</h2>
<p> clc-clbuild &#8211; clc enabled clbuild wrapper </p>
<h2>SYNOPSIS</h2>
<p> <code>clc-clbuild</code> <i>setup</i> </p>
<p> <code>clc-clbuild</code> <i>clbuild commands</i> </p>
<h2>DESCRIPTION</h2>
<p> This is a thin wrapper round <i>clbuild</i> for use with <i>common lisp controller.</i> You can use this to install and update <i>clbuild </i> enabled packages. </p>
<p> To use first do (as root) <code>clc-clbuild setup,</code> this will download and setup clbuild. Then you can use the normal <i>clbuild</i> commands. These will be ran as the user <i>cl-builder</i> and will setup a <i>clbuild </i> environment in <code>/usr/share/common-lisp/clbuild/</code> </p>
<p> For example running (as root again) </p>
<p> <code>clc-clbuild install cl-ppcre</code> </p>
<p> will download and install <i>cl-ppcre</i> from the appropriate libraries. Please see </p>
<p> <code>clc-clbuild help</code> </p>
<p> for more information. </p>
<h2>BUGS</h2>
<p> Bug reports should be sent to the debian BTS, preferably with reportbug. </p>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<p> Peter Van Eynde (pvaneynd [at] debian.org) </p>
<h2>Index</h2>
