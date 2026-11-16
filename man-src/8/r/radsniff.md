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
<dt>-c&nbsp;<wbr><i>count</i></dt>
<dd>Number of packets to capture.</dd>
<dt>-d&nbsp;<wbr><i>directory</i></dt>
<dd>Directory where the dictionaries are found.</dd>
<dt>-F</dt>
<dd>Filter PCAP file from stdin to stdout. Output file will contain RADIUS packets.</dd>
<dt>-f&nbsp;<wbr><i>filter</i></dt>
<dd>PCAP filter. (default is udp port 1812 or 1813)</dd>
<dt>-h</dt>
<dd>Print usage help information.</dd>
<dt>-i&nbsp;<wbr><i>interface</i></dt>
<dd>Interface to capture.</dd>
<dt>-I&nbsp;<wbr><i>filename</i></dt>
<dd>Read packets from filename.</dd>
<dt>-m</dt>
<dd>Print packet headers only, not contents.</dd>
<dt>-p&nbsp;<wbr><i>port</i></dt>
<dd>Listen for packets on port.</dd>
<dt>-r&nbsp;<wbr><i>filter</i></dt>
<dd>RADIUS attribute filter.</dd>
<dt>-s&nbsp;<wbr><i>secret</i></dt>
<dd>RADIUS secret.</dd>
<dt>-S</dt>
<dd>Sort attributes in the packet. Used to compare server results.</dd>
<dt>-w&nbsp;<wbr><i>file</i></dt>
<dd>Write output packets to file.</dd>
<dt>-x</dt>
<dd>Print out debugging information. </dd>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-radiusd/">radiusd</a>(8),pcap(3)</p>
<h2>Authors</h2>
<p>Nicolas Baradakis &lt;nicolas.baradakis [at] cegetel.net&gt;</p>
