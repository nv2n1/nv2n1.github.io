---
title: "p11-kit(8)"
name: "p11-kit"
section: "8"
letter: "p"
url: "/docs/linux/man/8-p11-kit/"
description: "p11-kit – Tool for operating on configured PKCS#11 modules"
---

<p>p11-kit &#8211; Tool for operating on configured PKCS#11 modules</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>p11-kit list-modules</code></p>
<dt> <code>p11-kit extract</code> &#8230; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt></p>
<dt> <code>p11-kit server</code> &#8230; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>
</dl>
<h2>Description</h2>
<p><code>p11-kit</code></p>
<dd>is a command line tool that can be used to perform operations on PKCS#11 modules configured on the system. </p>
<p> See the various sub commands below. The following global options can be used: </p>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dd>Run in verbose mode with debug output.</dl>
<p> <code>-q, &#8211;quiet</code></p>
<dl>
<dd>Run in quiet mode without warning or failure messages.</dl>
<h2>List Modules</h2>
<p>List system configured PKCS#11 modules. </p>
<dl>
<dd>
<pre>$ p11-kit list-modules</pre>
</dl>
<p> The modules, information about them and the tokens present in the PKCS#11 modules will be displayed.</p>
<h2>Extract</h2>
<p>Extract certificates from configured PKCS#11 modules. </p>
<p> This operation has been moved to a separate command <code>trust extract</code>. See <code><a href="/docs/linux/man/1-trust/">trust</a></code>(1) for more information</p>
<h2>Server</h2>
<p>Run a server process that exposes PKCS#11 module remotely. </p>
<dl>
<dd>
<pre>$ p11-kit server pkcs11:token1 pkcs11:token2 ...
$ p11-kit server --provider /path/to/pkcs11-module.so pkcs11:token1 pkcs11:token2 ...</pre>
</dl>
<p> This launches a server that exposes the given PKCS#11 tokens on a local socket. The tokens must belong to the same module. To access the socket, use p11-kit-client.so module. The server address and PID are printed as a shell-script snippet which sets the appropriate environment variable: P11_KIT_SERVER_ADDRESS and P11_KIT_SERVER_PID.</p>
<h2>Extract Trust</h2>
<p>Extract standard trust information files. </p>
<p> This operation has been moved to a separate command <code>trust extract-compat</code>. See <code><a href="/docs/linux/man/1-trust/">trust</a></code>(1) for more information</p>
<h2>Remote</h2>
<p>Run a PKCS#11 module remotely. </p>
<dl>
<dd>
<pre>$ p11-kit remote /path/to/pkcs11-module.so
$ p11-kit remote pkcs11:token1 pkcs11:token2 ...</pre>
</dl>
<p> This is not meant to be run directly from a terminal. But rather in a <code>remote</code> option in a <code><a href="/docs/linux/man/5-pkcs11-conf/">pkcs11.conf</a></code>(5) file. </p>
<p> This exposes the given PKCS#11 module or tokens over standard input and output. Those two forms, whether to expose a module or tokens, are mutually exclusive and if the second form is used, the tokens must belong to the same module.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://github.com/p11-glue/p11-kit/issues/">https://github.com/p11-glue/p11-kit/issues/</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pkcs11-conf/">pkcs11.conf</a></code>(5) Further details available in the p11-kit online documentation at m[blue]<code><a rel="nofollow" href="https://p11-glue.github.io/p11-glue/p11-kit/manual/">https://p11-glue.github.io/p11-glue/p11-kit/manual/</a></code>m[]. </p>
