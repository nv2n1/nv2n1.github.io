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
<dt><code>-a </code><i>plaintext </i><code>| </code><i>otp </i><code>| </code><i>sasl</i></dt>
<dd>Tells which authentication mode is acceptable, <i>sasl</i> enables SASL (RFC2222), and <i>otp</i> enables OTP (RFC1938) authentication. Both disable plaintext passwords.</dd>
<dt><code>&#8211;address-log= file </code></dt>
<dd>Logs the addresses (along with a timestamp) of all clients to the specified file. This can be used to implement POP-before-SMTP authentication.</dd>
<dt><code>-d</code></dt>
<dd>Enables more verbose log messages.</dd>
<dt><code>-i</code></dt>
<dd>When not started by inetd, this flag tells that it has to create a socket by itself.</dd>
<dt><code>-k</code></dt>
<dd>Tells to use Kerberos for authentication. This is the traditional way of doing Kerberos authentication, and is normally done on a separate port (as it doesn&#8217;t follow RFC1939), and should be used instead of using SASL.</dd>
<dt><code>-p </code><i>port</i></dt>
<dd>Port to listen to, in combination with &#8211;<code>i</code></dd>
<dt><code>-t </code><i>file</i></dt>
<dd>Trace all commands to file.</dd>
<dt><code>-T </code><i>seconds</i></dt>
<dd>Set timeout to something other than the default of 120 seconds.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-push/">push</a>(8), movemail(8)</p>
<h2>Standards</h2>
<p>RFC1939 (Post Office Protocol &#8211; Version 3)</p>
<h2>Authors</h2>
<p>The server was initially developed at the University of California, Berkeley. </p>
<p> Many changes have been made as part of the KTH Kerberos distributions.</p>
