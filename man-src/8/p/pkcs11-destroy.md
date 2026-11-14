---
title: "pkcs11-destroy(8)"
name: "pkcs11-destroy"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pkcs11-destroy/"
description: "pkcs11-destroy – destroy PKCS#11 objects"
---

<p>pkcs11-destroy &#8211; destroy PKCS#11 objects</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pkcs11-destroy</code> [<code>-m&nbsp;<wbr></code><i>module</i>] [<code>-s&nbsp;<wbr></code><i>slot</i>] {-i&nbsp;<wbr><i>ID</i> | -l&nbsp;<wbr><i>label</i>} [<code>-p&nbsp;<wbr></code><i>PIN</i>] [<code>-w&nbsp;<wbr></code><i>seconds</i>]</dl>
<h2>Description</h2>
<p><code>pkcs11-destroy</code></p>
<dd>destroys keys stored in a PKCS#11 device, identified by their <code>ID</code> or <code>label</code>. </p>
<p> Matching keys are displayed before being destroyed. By default, there is a five second delay to allow the user to interrupt the process before the destruction takes place.</p>
<h2>Arguments</h2>
<p>-m <i>module</i></p>
<dl>
<dd>Specify the PKCS#11 provider module. This must be the full path to a shared library object implementing the PKCS#11 API for the device.</dl>
<p> -s <i>slot</i></p>
<dl>
<dd>Open the session with the given PKCS#11 slot. The default is slot 0.</dl>
<p> -i <i>ID</i></p>
<dl>
<dd>Destroy keys with the given object ID.</dl>
<p> -l <i>label</i></p>
<dl>
<dd>Destroy keys with the given label.</dl>
<p> -p <i>PIN</i></p>
<dl>
<dd>Specify the PIN for the device. If no PIN is provided on the command line, <code>pkcs11-destroy</code> will prompt for it.</dl>
<p> -w <i>seconds</i></p>
<dl>
<dd>Specify how long to pause before carrying out key destruction. The default is five seconds. If set to 0, destruction will be immediate.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pkcs11-list/">pkcs11-list</a></code>(3), <code><a href="/docs/linux/man/3-pkcs11-keygen/">pkcs11-keygen</a></code>(3)</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
