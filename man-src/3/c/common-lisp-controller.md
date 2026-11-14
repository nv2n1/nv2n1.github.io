---
title: "common-lisp-controller(3)"
name: "common-lisp-controller"
section: "3"
letter: "c"
url: "/docs/linux/man/3-common-lisp-controller/"
description: "common-lisp-controller – Common Lisp system management tool"
---

<h2 class="name">NAME</h2>
<p> common-lisp-controller &#8211; Common Lisp system management tool</p>
<h2>DESCRIPTION</h2>
<p> The <i>common-lisp-controller</i> system will manage the installed Common Lisp <i>implementations</i> and <i>libraries</i> on the system. The main function is to enable every user to load any available <i>library</i> and to store the compiled files in a user and implementation specific cache directory. </p>
<p> On upgrades of either <i>implementations</i> or <i>libraries</i> these directories will be cleared so that no old fasl files will remain. </p>
<p> There are also options to add libraries by default to new images, see <i>/usr/share/doc/common-lisp-controller/README.Debian</i> , or to add user specific libraries to the management system, see <i>clc-register-user-package.</i><br />
&nbsp;<wbr></p>
<h2>EXAMPLES</h2>
<p> To load a clc library <i>:foo</i> on a clc enabled implementation simply do </p>
<p> <code>(clc:clc-require :foo)</code> </p>
<h2>FILES</h2>
<p> <i>/var/cache/common-lisp/</i> <i>&lt;uid&gt;</i> <i>/</i> <i>&lt;implementation-name&gt;</i> <i>/</i> <i>&lt;library&gt;</i> the cache directory for a library fir a given user with associated uid and a certain implementation. </p>
<p> <i>/usr/share/common-lisp/systems/ </i> the location of the libraries. </p>
<h2>BUGS</h2>
<p> Bug reports should be sent to the Debian BTS, preferably with reportbug. </p>
<h2>AUTHOR</h2>
<p> Peter Van Eynde (pvaneynd [at] debian.org) 2001-2006 </p>
<p> Kevin M. Rosenberg (kmr [at] debian.org) 2001-2004 </p>
<p> Ren&eacute; van Bevern 2005-2006 </p>
<p> Desmond O. Chang (dochang [at] gmail.com) 2010 </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-clc-register-user-package/">clc-register-user-package</a></code>(1), <code><a href="/docs/linux/man/1-clc-unregister-user-package/">clc-unregister-user-package</a></code>(1) <code><a href="/docs/linux/man/8-register-common-lisp-implementation/">register-common-lisp-implementation</a></code>(8) <code><a href="/docs/linux/man/8-register-common-lisp-source/">register-common-lisp-source</a></code>(8) <code>unregister-common-lisp-implementation|<a href="/docs/linux/man/8-source/">source</a></code>(8) <code><a href="/docs/linux/man/8-unregister-common-lisp-source/">unregister-common-lisp-source</a></code>(8) </p>
<h2>Index</h2>
