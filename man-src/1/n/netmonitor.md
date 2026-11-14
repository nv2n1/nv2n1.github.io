---
title: "netmonitor(1)"
name: "netmonitor"
section: "1"
letter: "n"
url: "/docs/linux/man/1-netmonitor/"
description: "netmonitor – Network Bandwidth Monitor"
---

<h2>NAME</h2>
<p> netmonitor &#8211; Network Bandwidth Monitor</p>
<h2>SYNOPSIS</h2>
<p> <code>netmonitor</code> <i>[options&#8230;..]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>netmonitor </code> is a console application that monitors network interfaces. It displays the transfer rate (upload and download) for each device and the data consumed by each device. The main features of netmon are low resource usage, a simple yet effective design, and an easy to understand tabular output. It displays values whose units change dynamically to scale with the value. Its compact display fits in a 9&#215;66 size terminal window. </p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt>&#8211;config</p>
<dd> Starts the configuration program.</p>
<dt>&#8211;compact</p>
<dd> Removes the spacing lines between each devices.</p>
<dt>&#8211;help</p>
<dd> Displays the help menu. </p>
</dl>
<h2>FORCE UNIT OPTIONS</h2>
<dl>
<dt>&#8211;forceTKB</p>
<dd> Forces the total units to Kilobytes</p>
<dt>&#8211;forceTMB</p>
<dd> Forces the total units to Megabytes</p>
<dt>&#8211;forceTGB</p>
<dd> Forces the total units to Gigabytes</p>
<dt>&#8211;forceRKB</p>
<dd> Forces the data rate units to Kilobytes</p>
<dt>&#8211;forceRMB</p>
<dd> Forces the data rate units to Megabytes</p>
<dt>&#8211;forceRGB</p>
<dd> Forces the data rate units to Gigabytes </p>
</dl>
<h2>BUGS</h2>
<p> Forcing a data rate that is to low for the data values will cause destortion to the display. </p>
<h2>AUTHOR</h2>
<p> Dwayne Hoy &lt;hellcat82 at iprimus dot com dot au&gt; </p>
<h2>Index</h2>
