---
title: "kgrantpty(7)"
name: "kgrantpty"
section: "7"
letter: "k"
url: "/docs/linux/man/7-kgrantpty/"
description: "kgrantpty – konsole uses this to securely open a slave pty"
---

<p>kgrantpty &#8211; konsole uses this to securely open a slave pty</p>
<h2>Synopsis</h2>
<pre><code>kgrantpty</code> [<code>OPTION</code>] [<code>FILE</code>]</pre>
<h2>Description</h2>
<p><code>kgrantpty</code> is only intended to be used internally by konsole to open a slave pty securely. It performs a setuid chmod and chown on the slave pty device. Eavesdropping is prevented with the usage of a file handle as an argument. KPty automatically calls this tool, and it is not intended to be called from the command line.</p>
<h2>Options</h2>
<dl>
<dd><code>&#8211;grant</code> grant secure setuid root chmod and chown to the file descriptor</p>
<dd><code>&#8211;revoke</code> revoke the secure setuid root chmod and chown from the file descriptor</dl>
<h2>Security</h2>
<p><code>kgrantpty</code> must be used as setuid root.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ttyname/">ttyname</a></code>(3), <code><a href="/docs/linux/man/3-forkpty/">forkpty</a></code>(3), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7)</p>
<h2>Author</h2>
<p>Manpage written by Rodrigo Rubira Branco &lt;rrbranco [at] br.ibm.com&gt;</p>
