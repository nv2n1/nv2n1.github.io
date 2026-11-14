---
title: "macchanger(1)"
name: "macchanger"
section: "1"
letter: "m"
url: "/docs/linux/man/1-macchanger/"
description: "macchanger – MAC Changer"
---

<h2 class="name">NAME</h2>
<p> macchanger &#8211; MAC Changer </p>
<h2>SYNOPSIS</h2>
<p> <code>macchanger </code> [<i>options</i>] device</p>
<h2>DESCRIPTION</h2>
<p> <code>macchanger</code> is a Linux utility for viewing/manipulating the MAC address for network interfaces.</p>
<h2>OPTIONS</h2>
<p> <code>macchanger</code> accepts the following options:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of program.</p>
<dt><code>-s, &#8211;show</code></p>
<dd> Prints the current MAC</p>
<dt><code>-e, &#8211;endding</code></p>
<dd> Don&#8217;t change the vendor bytes.</p>
<dt><code>-a, &#8211;another</code></p>
<dd> Set random vendor MAC of the same kind.</p>
<dt><code>-A</code></p>
<dd> Set random vendor MAC of any kind.</p>
<dt><code>-r, &#8211;random</code></p>
<dd> Set fully random MAC.</p>
<dt><code>-l, &#8211;list[=keyword]</code></p>
<dd> Print known vendors (with keyword in the vendor&#8217;s description string)</p>
<dt><code>-m, &#8211;mac=XX:XX:XX:XX:XX:XX</code></p>
<dd> Set the MAC XX:XX:XX:XX:XX:XX</dl>
<h2>EXAMPLE</h2>
<p> macchanger -A eth1</p>
<h2>SEE ALSO</h2>
<p> ifconfig (8)</p>
<h2>AUTHOR</h2>
<p> Alvaro Lopez Ortega &lt;alvaro [at] alobbs.com&gt;. </p>
<h2>Index</h2>
