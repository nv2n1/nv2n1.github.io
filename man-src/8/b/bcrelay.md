---
title: "bcrelay(8)"
name: "bcrelay"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bcrelay/"
description: "bcrelay – a broadcast relay daemon"
---

<p><code>bcrelay</code> &#8211; a broadcast relay daemon</p>
<h2>Synopsis</h2>
<p><code>bcrelay</code> [<i>OPTION</i>]&#8230;</p>
<h2>Description</h2>
<p><code>bcrelay</code> simply plays as a broadcast repeater. When <code>bcrelay</code> receives packets from the incomming interface, it will then relay them to the outgoing interface. </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>,<code>&#8211;daemon</code></p>
<dd>Run <code>bcrelay</code> as a daemon.</p>
<dt><code>-h</code>,<code>&#8211;help</code></p>
<dd>Show help message.</p>
<dt><code>-i</code>,<code>&#8211;incoming</code> <i>interface-in</p>
<dd>Defines from which interface broadcasts will be read.</p>
<dt></i><code>-s</code>,<code>&#8211;outgoing</code> <i>interface-out</p>
<dd>Defines to which interface broadcasts will be relayed.</p>
<dt></i><code>-n</code>,<code>&#8211;nolog</code></p>
<dd>Disable any logging and tracing to /var/log/messages except fatal error messages.</p>
<dt><code>-s</code>,<code>&#8211;ipsec</code> <i>argument</i></p>
<dd>Defines an ipsec tunnel to be relayed to. Since ipsec tunnels terminate on the same interface, we need to define the broadcast address of the other end-point of the tunnel. This is done as ipsec0:x.x.x.255.</p>
<dt><code>-v</code>,<code>&#8211;version</code></p>
<dd>Show the version of <code>bcrelay</code>.</p>
<dt>Log messages and debugging information go to syslog as daemon.</p>
<dd>
<dt>Interfaces can be specified as regexpressions, ie. ppp[0-9]+.</p>
<dd></dl>
<h2>Authors</h2>
<p>Original <code>bcrelay</code> program was written by Luc Richards &lt;TheyCallMeLuc [at] yahoo.com.au&gt;. </p>
<p> <code>Bcrelay</code> was modified for <code>poptop</code> by Richard de Vroede &lt;r.devroede [at] linvision.com&gt; and rewritten by Norbert van Bolhuis &lt;norbert [at] vanbolhuis.demon.nl&gt; for version (v1.0+) of <code>bcrelay</code>. </p>
<p> This manual page was written by Nguyen Vinh for Debian GNU/Linux System (but may be used for others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License Version 2, and any later versions published by Free Software Foundation. There is no WARRANTY, to the extent permitted by the law.</p>
<h2>See Also</h2>
<p>For more detailed information about <code>bcrelay</code>, please read README. </p>
