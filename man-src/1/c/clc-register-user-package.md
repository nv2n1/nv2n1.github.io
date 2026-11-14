---
title: "clc-register-user-package(1)"
name: "clc-register-user-package"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clc-register-user-package/"
description: "clc-(un)register-user-package – registers a user asdf system"
---

<h2 class="name">NAME</h2>
<p> clc-(un)register-user-package &#8211; registers a user asdf system</p>
<h2>SYNOPSIS</h2>
<p> <code>clc-register-user-package</code> <i>package-file</i> </p>
<p> <code>clc-unregister-user-package</code> <i>package-file</i> </p>
<h2>DESCRIPTION</h2>
<p> Registers a user defined system into the <i>common lisp controller</i> system. This means that any Common Lisp implementation will know how to find the system. </p>
<p> The system file itself will be symlinked from the <i>~/.clc/systems</i> directory and the system will be recorded in the <i>~/.clc/user-packages.db</i> file. </p>
<p> No removal of old fasl files during upgrades of Common Lisp Implementations will be done, nor will the fasls of different implementations will be separated by <i>clc</i> , it is expected that the users who require this will create a full Debian package or create a symlink in <i>/usr/share/common-lisp/systems/</i> to the system file. </p>
<h2>BUGS</h2>
<p> Bug reports should be sent to the Debian BTS, preferably with reportbug. </p>
<h2>AUTHOR</h2>
<p> Peter Van Eynde (pvaneynd [at] debian.org) and Kevin M. Rosenberg (kmr [at] debian.org) 2001-2008. </p>
<h2>Index</h2>
