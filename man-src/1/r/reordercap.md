---
title: "reordercap(1)"
name: "reordercap"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reordercap/"
description: "reordercap – Reorder input file by timestamp into output file"
---

<h2 class="name">NAME</h2>
<p> reordercap &#8211; Reorder input file by timestamp into output file </p>
<h2>SYNOPSIS</h2>
<p> <code>reordercap</code> [&nbsp;<wbr><code>-n</code>&nbsp;<wbr>] &lt;<i>infile</i>&gt; &lt;<i>outfile</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>Reordercap</code> is a program that reads an input capture file and rewrites the frames to an output capture file, but with the frames sorted by increasing timestamp. </p>
<p> This functionality may be useful when capture files have been created by combining frames from more than one well-synchronised source, but the frames have not been combined in strict time order. </p>
<p> <code>Reordercap</code> writes the output capture file in the same format as the input capture file. </p>
<p> <code>Reordercap</code> is able to detect, read and write the same capture files that are supported by <code>Wireshark</code>. The input file doesn&#8217;t need a specific filename extension; the file format and an optional gzip compression will be detected automatically. Near the beginning of the <font SIZE="-1">DESCRIPTION</font> section of <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1) or &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages/wireshark.html">http://www.wireshark.org/docs/man-pages/wireshark.html</a>&gt; is a detailed description of the way <code>Wireshark</code> handles this, which is the same way <code>reordercap</code> handles this.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-n</p>
<dd> When the <code>-n</code> option is used, <code>reordercap</code> will not write out the output file if it finds that the input file is already in order.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-pcap/">pcap</a></i>(3), <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1), <i><a href="/docs/linux/man/1-tshark/">tshark</a></i>(1), <i><a href="/docs/linux/man/1-dumpcap/">dumpcap</a></i>(1), <i><a href="/docs/linux/man/1-editcap/">editcap</a></i>(1), <i><a href="/docs/linux/man/1-mergecap/">mergecap</a></i>(1), <i><a href="/docs/linux/man/1-text2pcap/">text2pcap</a></i>(1), <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8)</p>
<h2>NOTES</h2>
<p> <code>Reordercap</code> is part of the <code>Wireshark</code> distribution. The latest version of <code>Wireshark</code> can be found at &lt;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&gt;. </p>
<p> It may make sense to move this functionality into <code>editcap</code>, or perhaps <code>mergecap</code>, in which case <code>reordercap</code> could be retired. </p>
<p> <font SIZE="-1">HTML</font> versions of the Wireshark project man pages are available at: &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages">http://www.wireshark.org/docs/man-pages</a>&gt;.</p>
<h2>AUTHORS</h2>
<pre><code>
Original Author-- -- -- -- -- -- --Martin Mathieson&lt;martin.r.mathieson[AT] googlemail.com&gt;
</code></pre>
<h2>Index</h2>
