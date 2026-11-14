---
title: "register-common-lisp-implementation(8)"
name: "register-common-lisp-implementation"
section: "8"
letter: "r"
url: "/docs/linux/man/8-register-common-lisp-implementation/"
description: "(un)register-common-lisp-{implementation|source) – internal clc commands"
---

<p>(un)register-common-lisp-{implementation|source) &#8211; internal clc commands</p>
<h2>Synopsis</h2>
<p><code>register-common-lisp-implementation </code> <i>implementation</i> <code>unregister-common-lisp-implementation </code> <i>implementation</i> <code>register-common-lisp-source </code> <i>source-package</i> <code>unregister-common-lisp-source </code> <i>source-package</i> <code>clc-update-customized-images</code> <i>source-package</i> </p>
<h2>Description</h2>
<p>These are internal <i>common lisp controller</i> commands. Common lisp source and implementation packages use them to register themselves to the <i>common lisp controller</i> or to cause regeneration of implementation images if they were selected to be present in such. </p>
<h2>Bugs</h2>
<p>Bug reports should be sent to the debian BTS, preferably with reportbug. </p>
<h2>See Also</h2>
<dl>
<dt>The Common Lisp in Debian Manual at</p>
<dd><code><a rel="nofollow" href="http://cl-debian.alioth.debian.org/clid/clid.html/">http://cl-debian.alioth.debian.org/clid/clid.html/</a></code> </p>
<h2>Author</h2>
<p>Peter Van Eynde (pvaneynd [at] debian.org), Kevin M. Rosenberg (kmr [at] debian.org) and Ren&eacute; van Bevern (rvb [at] progn.org) 2001-2006</p>
