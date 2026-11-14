---
title: "etherape(1)"
name: "etherape"
section: "1"
letter: "e"
url: "/docs/linux/man/1-etherape/"
description: "etherape – graphical network traffic browser"
---

<h2>NAME</h2>
<p> etherape &#8211; graphical network traffic browser</p>
<h2>SYNOPSIS</h2>
<p> <code>etherape</code> [ <code>-m</code> operating mode ] [ <code>-i</code> interface ] [ <code>-f</code> filter ] [ <code>-r</code> inputfile ] [ <code>-n</code> ] [ <code>-d</code> ] [ <code>-F</code> ] [ <code>-N</code> color ] [ <code>-L</code> color ] [ <code>-T</code> color ] <code>-z ]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>etherape</code> is a network traffic browser. It displays network activity graphically. It uses GNOME libraries as its user interface, and libpcap, a packet capture and filtering library.</p>
<h2>OPTIONS</h2>
<p> These options can be supplied to the command:</p>
<dl>
<dt><code>-m, &#8211;mode </code>&lt;ethernet|fddi|ip|tcp&gt;</p>
<dd> set mode of operation (default is lowest level for current device)</p>
<dt><code>-i, &#8211;interface </code>&lt;interface name&gt;</p>
<dd> set interface to listen to</p>
<dt><code>-f, &#8211;filter </code>&lt;capture filter&gt;</p>
<dd> set capture filter</p>
<dt><code>-r, &#8211;infile </code>&lt;file name&gt;</p>
<dd> set input file</p>
<dt><code>-n, &#8211;numeric</code></p>
<dd> don&#8217;t convert addresses to names</p>
<dt><code>-d, &#8211;diagram-only</code></p>
<dd> don&#8217;t display any node text identification</p>
<dt><code>-F, &#8211;no-fade</code></p>
<dd> do not fade old links</p>
<dt><code>-N, &#8211;node-color </code>&lt;color&gt;</p>
<dd> set the node color</p>
<dt><code>-L, &#8211;link-color </code>&lt;color&gt;</p>
<dd> set the link color</p>
<dt><code>-T, &#8211;text-color </code>&lt;color&gt;</p>
<dd> set the text color</p>
<dt><code>-z, &#8211;zero-delay </code></p>
<dd> ignores timestamps when replaying a capture file.</p>
<dt><code>-?, &#8211;help</code></p>
<dd> show a brief help message</dl>
<h2>FILES</h2>
<p> Etherape will use <i>/etc/ethers</i> if there is one. If not, it will try to reverse lookup the ip address. </p>
<p> <code>IMPORTANT!</code> It is particularly important when running in ethernet mode to have the ethernet address of your router in /etc/ethers. If not, your router will have as name whatever IP address it was forwarding traffic from when it was first heard. </p>
<h2>SEE ALSO</h2>
<p> The etherape webpage is at <a rel="nofollow" href="http://etherape.sourceforge.net/">http://etherape.sourceforge.net/</a> </p>
<h2>AUTHOR</h2>
<p> Juan Toledo &lt;toledo [at] users.sourceforge.net&gt; </p>
<h2>Index</h2>
