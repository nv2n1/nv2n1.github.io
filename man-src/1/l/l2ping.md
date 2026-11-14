---
title: "l2ping(1)"
name: "l2ping"
section: "1"
letter: "l"
url: "/docs/linux/man/1-l2ping/"
description: "l2ping – Send L2CAP echo request and receive answer"
---

<h2 class="name">NAME</h2>
<p> l2ping &#8211; Send L2CAP echo request and receive answer </p>
<h2>SYNOPSIS</h2>
<p> <code>l2ping</code> [<i>OPTIONS</i>] <i>bd_addr</i></p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-l2ping/">l2ping</a>(1)</code> sends a L2CAP echo request to the Bluetooth MAC address bd_addr given in dotted hex notation.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code><i>&nbsp;&lt;hciX&gt;</i></p>
<dd> The command is applied to device <i>hciX</i>, which must be the name of an installed Bluetooth device (X = 0, 1, 2, &#8230;) If not specified, the command will be sent to the first available Bluetooth device.</p>
<dt><code>-s</code><i>&nbsp;size</i></p>
<dd> The size of the data packets to be sent.</p>
<dt><code>-c</code><i>&nbsp;count</i></p>
<dd> Send count number of packets then exit.</p>
<dt><code>-t</code><i>&nbsp;timeout</i></p>
<dd> Wait timeout seconds for the response.</p>
<dt><code>-d</code><i>&nbsp;delay</i></p>
<dd> Wait delay seconds between pings.</p>
<dt><code>-f</code></p>
<dd> Kind of flood ping. Use with care! It reduces the delay time between packets to 0.</p>
<dt><code>-r</code></p>
<dd> Reverse ping (gnip?). Send echo response instead of echo request.</p>
<dt><code>-v</code></p>
<dd> Verify response payload is identical to request payload. It is not required for remote stacks to return the request payload, but most stacks do (including Bluez).</p>
<dt><code>bd_addr</code></p>
<dd> The Bluetooth MAC address to be pinged in dotted hex notation like <code>01:02:03:ab:cd:ef</code> or <code>01:EF:cd:aB:02:03</code></dl>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>AUTHOR</h2>
<p> Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt;, Marcel Holtmann &lt;marcel [at] holtmann.org&gt;, Nils Faerber &lt;nils [at] kernelconcepts.de&gt;, Adam Laurie &lt;adam [at] algroup.co.uk&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
<h2>Index</h2>
