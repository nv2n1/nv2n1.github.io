---
title: "amservice(8)"
name: "amservice"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amservice/"
description: "amservice – run an amanda service on a client"
---

<p>amservice &#8211; run an amanda service on a client</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amservice</code> [-f&nbsp;<wbr><i>input_file</i>&nbsp;<wbr>[-s]] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] <i>hostname</i> <i>auth</i> <i>service</i></dl>
<h2>Description</h2>
<p><code>Amservice</code></p>
<dd>execute an Amanda service on a client. It can be used without amanda server configuration (amanda.conf and disklist). It can be used to check communication between a server and a client. Amservice reads stdin to capture the REQ packet to send to the client. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p><code>hostname</code></p>
<dl>
<dd>The hostname of the client.</dl>
<p> <code>auth</code></p>
<dl>
<dd>The auth to use, one of: bsd, bsdudp, bsdtcp, ssh, rsh or krb5. The client must be configured with this auth.</dl>
<p> <code>service</code></p>
<dl>
<dd>The amanda service to execute on the client. One of noop, selfcheck or sendsize.</dl>
<p> <code>-f input_file</code></p>
<dl>
<dd>Use the file input_file instead of stdin to read the REQ packet from.</dl>
<p> <code>-s</code></p>
<dl>
<dd>Redirect the first connected stream to stdin/stdout. The -f argument is required for the REQ packet, the REP packet is not printed on stdout.</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<h2>Example</h2>
<p>The noop service is easy to execute because it does not require a REQ packet: </p>
<pre>amservice hostname bsdtcp noop &lt; /dev/null</pre>
<p>The example executes the noop service on the client using bsdtcp auth. This is useful for debugging connection problems. It print an OPTIONS line upon success. </p>
<p> It is more difficult to execute the selfcheck or sendsize service, as these require a valid REQ packet. If you have already uccessfully run amanda, you can find valid REQ packets in the amandad.*.debug files.</p>
<h2>Exit Code</h2>
<p>The exit code of <code>amservice</code> is one of: </p>
<pre> 0 = success
 1 = error executing amandad on the client.</pre>
<p>As <code>amservice</code> doesn&#8217;t parse the REP packet, it can only detect failures in executing amandad on the client. <code>amservice</code> can exit with value 0 even if the user is not authorized to execute the service. An error message will be printed.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amcheck/">amcheck</a></code>(8), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8), <code><a href="/docs/linux/man/8-amadmin/">amadmin</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
