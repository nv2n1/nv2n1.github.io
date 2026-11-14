---
title: "sane-as6e(5)"
name: "sane-as6e"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-as6e/"
description: "sane-as6e – SANE backend for using the Artec AS6E parallel port interface scanner."
---

<p>sane-as6e &#8211; SANE backend for using the Artec AS6E parallel port interface scanner.</p>
<h2>Description</h2>
<p>The <code>sane-as6e</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Artec AS6E flatbed scanner. It requires the <code>as6edriver</code> program in order to operate. The <code>as6edriver</code> program is not included with the SANE package. It can be found at <i><a rel="nofollow" href="http://as6edriver.sourceforge.net">http://as6edriver.sourceforge.net</a></i>. See the as6edriver documentation for technical information. The <code>as6edriver</code> program must be in the path for executables (<code>$PATH</code>). Especially if you run <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) (the SANE network scanning daemon), take care to setup the path for <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) or <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8) correctly or place the program in a directory that is in the path. </p>
<h2>Files</h2>
<p><code>as6edriver</code> &#8211; driver program that controls the scanner.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-as6edriver/">as6edriver</a></code>(5), <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8)<br />
 <i><a rel="nofollow" href="http://as6edriver.sourceforge.net">http://as6edriver.sourceforge.net</a></i> </p>
<h2>Author</h2>
<p>Eugene S. Weiss</p>
<h2>Email-Contact</h2>
<p><i>yossarian [at] users.sourceforge.net</i></p>
