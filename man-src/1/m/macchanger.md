---
title: "macchanger(1)"
name: "macchanger"
section: "1"
letter: "m"
url: "/docs/linux/man/1-macchanger/"
description: "macchanger – MAC Changer"
---

<h2>SYNOPSIS</h2>
<p> <code>macchanger </code> [<i>options</i>] device</p>
<h2>DESCRIPTION</h2>
<p> <code>macchanger</code> is a Linux utility for viewing/manipulating the MAC address for network interfaces.</p>
<h2>OPTIONS</h2>
<p> <code>macchanger</code> accepts the following options:</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Show version of program.</dd>
<dt><code>-s, &#8211;show</code></dt>
<dd> Prints the current MAC</dd>
<dt><code>-e, &#8211;endding</code></dt>
<dd> Don&#8217;t change the vendor bytes.</dd>
<dt><code>-a, &#8211;another</code></dt>
<dd> Set random vendor MAC of the same kind.</dd>
<dt><code>-A</code></dt>
<dd> Set random vendor MAC of any kind.</dd>
<dt><code>-r, &#8211;random</code></dt>
<dd> Set fully random MAC.</dd>
<dt><code>-l, &#8211;list[=keyword]</code></dt>
<dd> Print known vendors (with keyword in the vendor&#8217;s description string)</dd>
<dt><code>-m, &#8211;mac=XX:XX:XX:XX:XX:XX</code></dt>
<dd> Set the MAC XX:XX:XX:XX:XX:XX</dd></dl>
<h2>EXAMPLE</h2>
<p> macchanger -A eth1</p>
<h2>SEE ALSO</h2>
<p> ifconfig (8)</p>
<h2>AUTHOR</h2>
<p> Alvaro Lopez Ortega &lt;alvaro [at] alobbs.com&gt;. </p>
