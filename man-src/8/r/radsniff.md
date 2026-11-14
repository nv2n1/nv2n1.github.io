---
title: "radsniff(8)"
name: "radsniff"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radsniff/"
description: "radsniff – dump radius protocol"
---

<p>radsniff &#8211; dump radius protocol</p>
<h2>Synopsis</h2>
<p><code>radsniff</code> [<code>-c</code> <i>count</i>] [<code>-d</code> <i>directory</i>] [<code>-F</code>] [<code>-f</code> <i>filter</i>] [<code>-h</code>] [<code>-i</code> <i>interface</i>] [<code>-I</code> <i>filename</i>] [<code>-m</code>] [<code>-p</code> <i>port</i>] [<code>-r</code> <i>filter</i>] [<code>-s</code> <i>secret</i>] [<code>-S</code>] [<code>-w</code> <i>file</i>] [<code>-x</code>] </p>
<h2>Description</h2>
<p><code>radsniff</code> is a simple wrapper around libpcap. It can also print out the contents of RADIUS packets using the FreeRADIUS dictionaries. </p>
<h2>Options</h2>
<dl>
<dt>-c&nbsp;<wbr><i>count</i></p>
<dd>Number of packets to capture.</p>
<dt>-d&nbsp;<wbr><i>directory</i></p>
<dd>Directory where the dictionaries are found.</p>
<dt>-F</p>
<dd>Filter PCAP file from stdin to stdout. Output file will contain RADIUS packets.</p>
<dt>-f&nbsp;<wbr><i>filter</i></p>
<dd>PCAP filter. (default is udp port 1812 or 1813)</p>
<dt>-h</p>
<dd>Print usage help information.</p>
<dt>-i&nbsp;<wbr><i>interface</i></p>
<dd>Interface to capture.</p>
<dt>-I&nbsp;<wbr><i>filename</i></p>
<dd>Read packets from filename.</p>
<dt>-m</p>
<dd>Print packet headers only, not contents.</p>
<dt>-p&nbsp;<wbr><i>port</i></p>
<dd>Listen for packets on port.</p>
<dt>-r&nbsp;<wbr><i>filter</i></p>
<dd>RADIUS attribute filter.</p>
<dt>-s&nbsp;<wbr><i>secret</i></p>
<dd>RADIUS secret.</p>
<dt>-S</p>
<dd>Sort attributes in the packet. Used to compare server results.</p>
<dt>-w&nbsp;<wbr><i>file</i></p>
<dd>Write output packets to file.</p>
<dt>-x</p>
<dd>Print out debugging information. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-radiusd/">radiusd</a>(8),<a href="/docs/linux/man/3-pcap/">pcap</a>(3)</p>
<h2>Authors</h2>
<p>Nicolas Baradakis &lt;nicolas.baradakis [at] cegetel.net&gt;</p>
