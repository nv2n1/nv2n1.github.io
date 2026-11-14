---
title: "l2ping(8)"
name: "l2ping"
section: "8"
letter: "l"
url: "/docs/linux/man/8-l2ping/"
description: "l2ping – Send L2CAP echo request and receive answer"
---

<p>l2ping &#8211; Send L2CAP echo request and receive answer</p>
<h2>Synopsis</h2>
<p><code>l2ping</code> [<code>-i</code> <i>&lt;hciX&gt;</i>] [<code>-s</code> <i>size</i>] [<code>-c</code> <i>count</i>] [<code>-t</code> <i>timeout</i>] [<code>-d</code> <i>delay</i>] [<code>-f</code>] [<code>-r</code>] [<code>-v</code>] <i>bd_addr</i> </p>
<h2>Description</h2>
<p>L2ping sends a L2CAP echo request to the Bluetooth MAC address <i>bd_addr</i> given in dotted hex notation.</p>
<h2>Options</h2>
<dl>
<dt><code>-i</code><i> &lt;hciX&gt;</i></p>
<dd>The command is applied to device hciX , which must be the name of an installed Bluetooth device (X = 0, 1, 2, &#8230;) If not specified, the command will be sent to the first available Bluetooth device.</p>
<dt><code>-s</code><i> size</i></p>
<dd>The <i>size</i> of the data packets to be sent.</p>
<dt><code>-c</code><i> count</i></p>
<dd>Send <i>count</i> number of packets then exit.</p>
<dt><code>-t</code><i> timeout</i></p>
<dd>Wait <i>timeout</i> seconds for the response.</p>
<dt><code>-d</code><i> delay</i></p>
<dd>Wait <i>delay</i> seconds between pings.</p>
<dt><code>-f</code></p>
<dd>Kind of flood ping. Use with care! It reduces the delay time between packets to 0.</p>
<dt><code>-r</code></p>
<dd>Reverse ping (gnip?). Send echo response instead of echo request.</p>
<dt><code>-v</code></p>
<dd>Verify response payload is identical to request payload. It is not required for remote stacks to return the request payload, but most stacks do (including Bluez).</p>
<dt><i>bd_addr</i></p>
<dd>The Bluetooth MAC address to be pinged in dotted hex notation like <code>01:02:03:ab:cd:ef</code> or <code>01:EF:cd:aB:02:03</code></dl>
<h2>Authors</h2>
<p>Written by Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt; and Marcel Holtmann &lt;marcel [at] holtmann.org&gt; </p>
<p> man page by Nils Faerber &lt;nils [at] kernelconcepts.de&gt;, Adam Laurie &lt;adam [at] algroup.co.uk&gt;.</p>
