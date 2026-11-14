---
title: "vpcd(8)"
name: "vpcd"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vpcd/"
description: "vpcd – virtual power control daemon"
---

<p>vpcd &#8211; virtual power control daemon</p>
<h2>Synopsis</h2>
<p><code>vpcd</code> <i>[&#8211;port PORT]</i> </p>
<h2>Description</h2>
<p><code>vpcd</code> is a test program for PowerMan which emulates a remote power control device. It can be run interactively by the powerman daemon, or it can listen on a port of your choosing.</p>
<h2>Options</h2>
<dl>
<dt><i>-p, &#8211;port PORT</i></p>
<dd>Instructs <code>vpcd</code> to listen for connections on the specified port instead of using stdin/stdout. Only one connection will be accepted.</dl>
<h2>Interactive Commands</h2>
<p>The following commands are available at the vpcd&gt; prompt:</p>
<dl>
<dt><i>login</i></p>
<dd>The login command must br run before any of the other commands will work. No username or password is required.</p>
<dt><i>logoff</i></p>
<dd>Return <code>vpcd</code> to the initial state.</p>
<dt><i>stat PLUG|*</i></p>
<dd>Show the power status of PLUG. If PLUG is &#8220;*&#8221;, perform this action on all plugs.</p>
<dt><i>beacon PLUG|*</i></p>
<dd>Show the beacon status of PLUG. If PLUG is &#8220;*&#8221;, perform this action on all plugs.</p>
<dt><i>temp PLUG|*</i></p>
<dd>Show the temperature of the node attached to PLUG. If PLUG is &#8220;*&#8221;, perform this action on all plugs.</p>
<dt><i>spew COUNT</i></p>
<dd>Print COUNT 80-char lines. This is the basis of a buffer handling test.</p>
<dt><i>on PLUG|*</i></p>
<dd>Turn on PLUG. If PLUG is &#8220;*&#8221;, perform this action on all plugs.</p>
<dt><i>off PLUG|*</i></p>
<dd>Turn off PLUG. If PLUG is &#8220;*&#8221;, perform this action on all plugs.</p>
<dt><i>flash PLUG|*</i></p>
<dd>Light the beacon on PLUG. If PLUG is &#8220;*&#8221;, perform this action on all plugs.</p>
<dt><i>unflash PLUG|*</i></p>
<dd>Unlight the beacon on PLUG. If PLUG is &#8220;*&#8221;, perform this action on all plugs.</p>
<dt><i>reset PLUG|*</i></p>
<dd>Reset the node attached to PLUG. If PLUG is &#8220;*&#8221;, perform this action on all plugs. </p>
</dl>
<h2>Files</h2>
<p>/usr/sbin/vpcd</p>
<h2>Origin</h2>
<p>PowerMan was originally developed by Andrew Uselton on LLNL&#8217;s Linux clusters. This software is open source and distributed under the terms of the GNU GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-powerman/">powerman</a></code>(1), <code><a href="/docs/linux/man/8-powermand/">powermand</a></code>(8), <code><a href="/docs/linux/man/8-httppower/">httppower</a></code>(8), <code><a href="/docs/linux/man/8-plmpower/">plmpower</a></code>(8), <code><a href="/docs/linux/man/8-vpcd/">vpcd</a></code>(8), <code><a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a></code>(5), <code><a href="/docs/linux/man/5-powerman-dev/">powerman.dev</a></code>(5). <code><a rel="nofollow" href="http://code.google.com/p/powerman">http://code.google.com/p/powerman</a></code> </p>
