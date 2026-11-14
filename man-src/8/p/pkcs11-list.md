---
title: "pkcs11-list(8)"
name: "pkcs11-list"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pkcs11-list/"
description: "pkcs11-list – list PKCS#11 objects"
---

<p>pkcs11-list &#8211; list PKCS#11 objects</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pkcs11-list</code> [<code>-P</code>] [<code>-m&nbsp;<wbr></code><i>module</i>] [<code>-s&nbsp;<wbr></code><i>slot</i>] [-i&nbsp;<wbr><i>ID</i>] [-l&nbsp;<wbr><i>label</i>] [<code>-p&nbsp;<wbr></code><i>PIN</i>]</dl>
<h2>Description</h2>
<p><code>pkcs11-list</code></p>
<dd>lists the PKCS#11 objects with <code>ID</code> or <code>label</code> or by default all objects.</p>
<h2>Arguments</h2>
<p>-P</p>
<dl>
<dd>List only the public objects. (Note that on some PKCS#11 devices, all objects are private.)</dl>
<p> -m <i>module</i></p>
<dl>
<dd>Specify the PKCS#11 provider module. This must be the full path to a shared library object implementing the PKCS#11 API for the device.</dl>
<p> -s <i>slot</i></p>
<dl>
<dd>Open the session with the given PKCS#11 slot. The default is slot 0.</dl>
<p> -i <i>ID</i></p>
<dl>
<dd>List only key objects with the given object ID.</dl>
<p> -l <i>label</i></p>
<dl>
<dd>List only key objects with the given label.</dl>
<p> -p <i>PIN</i></p>
<dl>
<dd>Specify the PIN for the device. If no PIN is provided on the command line, <code>pkcs11-list</code> will prompt for it.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pkcs11-keygen/">pkcs11-keygen</a></code>(3), <code><a href="/docs/linux/man/3-pkcs11-destroy/">pkcs11-destroy</a></code>(3)</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
