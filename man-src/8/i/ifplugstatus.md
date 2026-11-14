---
title: "ifplugstatus(8)"
name: "ifplugstatus"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifplugstatus/"
description: "ifplugstatus – A link beat detection tool"
---

<p>ifplugstatus &#8211; A link beat detection tool</p>
<h2>Synopsis</h2>
<p><code>ifplugstatus [</code><i>options</i><code>] [</code><i>INTERFACE</i><code>] </code></p>
<h2>Description</h2>
<p>ifplugstatus is an utility which may be used to detect the link status of a local Linux ethernet device, much in the same way mii-diag, mii-tool and ethtool work. In fact it supports all three different APIs these three tools use. In addition it supports link checking with the IFF_RUNNING interface flag, which most modern drivers (not only ethernet) support, and association status checking with the wireless extension API for WLAN devices. </p>
<p> The APIs are tried in the following order: </p>
<p> First the newest API: <i>SIOCETHTOOL</i> (aka ethtool API) </p>
<p> Second the next older API: <i>SIOCGMIIREG</i> (aka mii-diag API) </p>
<p> Than the WLAN API: <i>wireless extension</i> (aka iwconfig API) </p>
<p> Followed by the cleanest API: <i>IFF_RUNNING</i> (aka ifconfig API) </p>
<p> The oldest API (<i>SIOCPRIV</i> aka mii-tool API) is not tested since it is obsolete. </p>
<p> ifplugstatus may be used in shell script since it returns the current status as return value. It is especially useful to detect the available APIs on the used network driver. (Option <code>-v</code>)</p>
<h2>Options</h2>
<p>You may specify an ethernet device on the command line. Otherwise ifplugstatus will check all available network interfaces.</p>
<dl>
<dt><code>-a | &#8211;auto</code></p>
<dd>Enable interface automatically before querying (default: off)</p>
<dt><code>-h | &#8211;help</code></p>
<dd>Show help</p>
<dt><code>-q | &#8211;quiet</code></p>
<dd>Decrease verbosity by one. If the verbosity is &lt; 0, no text will be shown, only the return value is relevant; if the verbosity is = 0, a terse status will be shown; If the verbosity is &gt; 0, detailed information about the used API is returned. (By default the verbosity is 0)</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd>Increase verbosity by one. See option <code>-q</code>.</p>
<dt><code>-V | &#8211;version</code></p>
<dd>Show version</dl>
<h2>Return Values</h2>
<p><i>0</i> Success </p>
<p> <i>1</i> Failure </p>
<p> <i>2</i> Link beat detected (only available when an interface is specified) </p>
<p> <i>3</i> Unplugged (same here)</p>
<h2>Author</h2>
<p>ifplugd was written by Lennart Poettering &lt;mzvscyhtq (at) 0pointer (dot) de&gt;. ifplugd is available at <code><a rel="nofollow" href="http://0pointer.de/lennart/projects/ifplugd/">http://0pointer.de/lennart/projects/ifplugd/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mii-diag/">mii-diag</a>(8)</code>, <code><a href="/docs/linux/man/8-mii-tool/">mii-tool</a>(8)</code>, <code><a href="/docs/linux/man/8-ethtool/">ethtool</a>(8)</code>, <code><a href="/docs/linux/man/8-ifplugd/">ifplugd</a>(8)</code></p>
<h2>Comments</h2>
<p>This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth.</p>
