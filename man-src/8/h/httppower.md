---
title: "httppower(8)"
name: "httppower"
section: "8"
letter: "h"
url: "/docs/linux/man/8-httppower/"
description: "httppower – communicate with HTTP based power distribution units"
---

<p>httppower &#8211; communicate with HTTP based power distribution units</p>
<h2>Synopsis</h2>
<p><code>httppower</code> <i>[&#8211;url URL]</i> </p>
<h2>Description</h2>
<p><code>httppower</code> is a helper program for <code>powerman</code> which enables it to communicate with HTTP based power distribution units. It is run interactively by the powerman daemon.</p>
<h2>Options</h2>
<dl>
<dt><i>-u, &#8211;url URL</i></p>
<dd>Set the base URL.</dl>
<h2>Interactive Commands</h2>
<p>The following commands are accepted at the httppower&gt; prompt:</p>
<dl>
<dt><i>auth user:pass</i></p>
<dd>Authenticate to the base URL with specified user and password, using &#8220;basic&#8221; HTTP authentication which sends the user and password over the network in plain text.</p>
<dt><i>seturl URL</i></p>
<dd>Set the base URL. Overrides the command line option.</p>
<dt><i>get [URL-suffix]</i></p>
<dd>Send an HTTP GET to the base URL with the optional URL-suffix appended.</p>
<dt><i>post [URL-suffix] key=val[&amp;key=val]&#8230;</i></p>
<dd>Send an HTTP POST to the base URL with the optional URL-suffix appended, and key-value pairs as argument. </p>
</dl>
<h2>Files</h2>
<p>/usr/sbin/httppower<br />
 /etc/powerman/powerman.conf</p>
<h2>Origin</h2>
<p>PowerMan was originally developed by Andrew Uselton on LLNL&#8217;s Linux clusters. This software is open source and distributed under the terms of the GNU GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-powerman/">powerman</a></code>(1), <code><a href="/docs/linux/man/8-powermand/">powermand</a></code>(8), <code><a href="/docs/linux/man/8-httppower/">httppower</a></code>(8), <code><a href="/docs/linux/man/8-plmpower/">plmpower</a></code>(8), <code><a href="/docs/linux/man/8-vpcd/">vpcd</a></code>(8), <code><a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a></code>(5), <code><a href="/docs/linux/man/5-powerman-dev/">powerman.dev</a></code>(5). <code><a rel="nofollow" href="http://code.google.com/p/powerman">http://code.google.com/p/powerman</a></code> </p>
