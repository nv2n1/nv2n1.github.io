---
title: "popper(8)"
name: "popper"
section: "8"
letter: "p"
url: "/docs/linux/man/8-popper/"
description: "popper – POP3 server"
---

<p><code>popper</code> &#8211; POP3 server</p>
<h2>Synopsis</h2>
<p>[-<code>k</code> ] [-<code>a </code><i>plaintext </i><code>| </code><i>otp </i><code>| </code><i>sasl</i> ] [-<code>t </code><i>file</i> ] [-<code>T </code><i>seconds</i> ] [-<code>d</code> ] [-<code>i</code> ] [-<code>p </code><i>port</i> ] [-<code>-address-log= file </code> ]</p>
<h2>Description</h2>
<p>serves mail via the Post Office Protocol. Supported options include:</p>
<dl>
<dt><code>-a </code><i>plaintext </i><code>| </code><i>otp </i><code>| </code><i>sasl</i></p>
<dd>Tells which authentication mode is acceptable, <i>sasl</i> enables SASL (RFC2222), and <i>otp</i> enables OTP (RFC1938) authentication. Both disable plaintext passwords.</p>
<dt><code>&#8211;address-log= file </code></p>
<dd>Logs the addresses (along with a timestamp) of all clients to the specified file. This can be used to implement POP-before-SMTP authentication.</p>
<dt><code>-d</code></p>
<dd>Enables more verbose log messages.</p>
<dt><code>-i</code></p>
<dd>When not started by inetd, this flag tells that it has to create a socket by itself.</p>
<dt><code>-k</code></p>
<dd>Tells to use Kerberos for authentication. This is the traditional way of doing Kerberos authentication, and is normally done on a separate port (as it doesn&#8217;t follow RFC1939), and should be used instead of using SASL.</p>
<dt><code>-p </code><i>port</i></p>
<dd>Port to listen to, in combination with &#8211;<code>i</code></p>
<dt><code>-t </code><i>file</i></p>
<dd>Trace all commands to file.</p>
<dt><code>-T </code><i>seconds</i></p>
<dd>Set timeout to something other than the default of 120 seconds.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-push/">push</a>(8), <a href="/docs/linux/man/8-movemail/">movemail</a>(8)</p>
<h2>Standards</h2>
<p>RFC1939 (Post Office Protocol &#8211; Version 3)</p>
<h2>Authors</h2>
<p>The server was initially developed at the University of California, Berkeley. </p>
<p> Many changes have been made as part of the KTH Kerberos distributions.</p>
