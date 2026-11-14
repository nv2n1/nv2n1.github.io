---
title: "massagevendor(8)"
name: "massagevendor"
section: "8"
letter: "m"
url: "/docs/linux/man/8-massagevendor/"
description: "massagevendor – convert the ethernet vendor codes master list to arpwatch format"
---

<p>massagevendor &#8211; convert the ethernet vendor codes master list to arpwatch format</p>
<h2>Synopsis</h2>
<p>massagevendor <i>vendorfile</i></p>
<h2>Description</h2>
<p><code>massagevendor</code> is a program that converts a text file containing ethernet vendor codes into a format suitable for use by <code><a href="/docs/linux/man/8-arpwatch/">arpwatch</a>(8)</code> and <code><a href="/docs/linux/man/8-arpsnmp/">arpsnmp</a>(8).</code> The input <i>vendorfile</i> is a master text file containing vendor codes. The output is sent to <i>stdout.</i> Each line of the <i>vendorfile</i> is expected to have a six digit hexadecimal vendor code followed by spaces followed by the name of the manufacturer. </p>
<p> All ethernet devices have a unique identifier which includes a vendor code specifying the manufacturer of the device. In normal operation <code><a href="/docs/linux/man/8-arpwatch/">arpwatch</a>(8)</code> and <code><a href="/docs/linux/man/8-arpsnmp/">arpsnmp</a>(8)</code> use the file <i>ethercodes.dat</i> to report this vendor code. <code>massagevendor</code> is used to generate the <i>ethercodes.dat</i> file from text files containing these vendor codes. </p>
<p> Locations where an ethernet vendor codes master text file can be obtained are given below.</p>
<h2>Files</h2>
<pre>/var/lib/arpwatch - default location of the ethernet vendor list
ethercodes.dat - file containing the list of ethernet vendor codes</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-arpwatch/">arpwatch</a>(8),</code> <code><a href="/docs/linux/man/8-arpsnmp/">arpsnmp</a>(8)</code></p>
<h2>Notes</h2>
<p>Sources for ethernet vendor codes seen in the wild are </p>
<pre><dl><dt><dd><i><a rel="nofollow" href="http://map-ne.com/Ethernet/vendor.html">http://map-ne.com/Ethernet/vendor.html</a></i>
<i><a href="ftp://ftp.cavebear.com/pub/Ethernet.txt">ftp://ftp.cavebear.com/pub/Ethernet.txt</a></i>
<i><a rel="nofollow" href="http://www.cavebear.com/CaveBear/Ethernet/vendor.html">http://www.cavebear.com/CaveBear/Ethernet/vendor.html</a></i>
</dl>
Useful for comparison or completeness are the
ethernet vendor codes as assigned
by the IEEE which can be found at
<dl><dt><dd><i><a rel="nofollow" href="http://standards.ieee.org/regauth/oui/oui.txt">http://standards.ieee.org/regauth/oui/oui.txt</a></i>
</dl></pre>
<h2>Bugs</h2>
<p>Please send bug reports to arpwatch [at] ee.lbl.gov.</p>
<h2>Authors</h2>
<p>Craig Leres of the Lawrence Berkeley National Laboratory Network Research Group, University of California, Berkeley, CA. </p>
<p> The current version is available via anonymous ftp: </p>
<dl>
<dd><i><a href="ftp://ftp.ee.lbl.gov/arpwatch.tar.gz">ftp://ftp.ee.lbl.gov/arpwatch.tar.gz</a></i></dl>
<p> This manual page was contributed by Hugo Graumann.</p>
