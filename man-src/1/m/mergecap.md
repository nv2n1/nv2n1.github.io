---
title: "mergecap(1)"
name: "mergecap"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mergecap/"
description: "mergecap – Merges two or more capture files into one"
---

<h2 class="name">NAME</h2>
<p> mergecap &#8211; Merges two or more capture files into one </p>
<h2>SYNOPSIS</h2>
<p> <code>mergecap</code> [&nbsp;<wbr><code>-a</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-F</code>&nbsp;<wbr>&lt;<i>file format</i>&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-h</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-s</code>&nbsp;<wbr>&lt;<i>snaplen</i>&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-T</code>&nbsp;<wbr>&lt;<i>encapsulation type</i>&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-v</code>&nbsp;<wbr>] <code>-w</code>&nbsp;<wbr>&lt;<i>outfile</i>&gt;|- &lt;<i>infile</i>&gt; [&lt;<i>infile</i>&gt; <i>&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Mergecap</code> is a program that combines multiple saved capture files into a single output file specified by the <code>-w</code> argument. <code>Mergecap</code> knows how to read <code>pcap</code> capture files, including those of <code>tcpdump</code>, <code>Wireshark</code>, and other tools that write captures in that format. </p>
<p> By default, <code>Mergecap</code> writes the capture file in <code>pcap</code> format, and writes all of the packets from the input capture files to the output file. </p>
<p> <code>Mergecap</code> is able to detect, read and write the same capture files that are supported by <code>Wireshark</code>. The input files don&#8217;t need a specific filename extension; the file format and an optional gzip compression will be automatically detected. Near the beginning of the <font SIZE="-1">DESCRIPTION</font> section of <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1) or &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages/wireshark.html">http://www.wireshark.org/docs/man-pages/wireshark.html</a>&gt; is a detailed description of the way <code>Wireshark</code> handles this, which is the same way <code>Mergecap</code> handles this. </p>
<p> <code>Mergecap</code> can write the file in several output formats. The <code>-F</code> flag can be used to specify the format in which to write the capture file, <code>mergecap -F</code> provides a list of the available output formats. </p>
<p> Packets from the input files are merged in chronological order based on each frame&#8217;s timestamp, unless the <code>-a</code> flag is specified. <code>Mergecap</code> assumes that frames within a single capture file are already stored in chronological order. When the <code>-a</code> flag is specified, packets are copied directly from each input file to the output file, independent of each frame&#8217;s timestamp. </p>
<p> The output file frame encapsulation type is set to the type of the input files if all input files have the same type. If not all of the input files have the same frame encapsulation type, the output file type is set to <font SIZE="-1">WTAP_ENCAP_PER_PACKET. </font> Note that some capture file formats, most notably <code>pcap</code>, do not currently support <font SIZE="-1">WTAP_ENCAP_PER_PACKET.</font> This combination will cause the output file creation to fail.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-a</p>
<dd> Causes the frame timestamps to be ignored, writing all packets from the first input file followed by all packets from the second input file. By default, when <code>-a</code> is not specified, the contents of the input files are merged in chronological order based on each frame&#8217;s timestamp. </p>
<p> Note: when merging, <code>mergecap</code> assumes that packets within a capture file are already in chronological order.</p>
<dt>-F &lt;file format&gt;</p>
<dd> Sets the file format of the output capture file. <code>Mergecap</code> can write the file in several formats; <code>mergecap -F</code> provides a list of the available output formats. The default is to use the file format of the first input file.</p>
<dt>-h</p>
<dd> Prints the version and options and exits.</p>
<dt>-s &lt;snaplen&gt;</p>
<dd> Sets the snapshot length to use when writing the data. If the <code>-s</code> flag is used to specify a snapshot length, frames in the input file with more captured data than the specified snapshot length will have only the amount of data specified by the snapshot length written to the output file. This may be useful if the program that is to read the output file cannot handle packets larger than a certain size (for example, the versions of snoop in Solaris 2.5.1 and Solaris 2.6 appear to reject Ethernet frames larger than the standard Ethernet <font SIZE="-1">MTU,</font> making them incapable of handling gigabit Ethernet captures if jumbo frames were used).</p>
<dt>-T &lt;encapsulation type&gt;</p>
<dd> Sets the packet encapsulation type of the output capture file. If the <code>-T</code> flag is used to specify a frame encapsulation type, the encapsulation type of the output capture file will be forced to the specified type, rather than being the type appropriate to the encapsulation type of the input capture files. </p>
<p> Note that this merely forces the encapsulation type of the output file to be the specified type; the packet headers of the packets will not be translated from the encapsulation type of the input capture file to the specified encapsulation type (for example, it will not translate an Ethernet capture to an <font SIZE="-1">FDDI</font> capture if an Ethernet capture is read and &#8216;<code>-T fddi</code>&#8216; is specified).</p>
<dt>-v</p>
<dd> Causes <code>mergecap</code> to print a number of messages while it&#8217;s working.</p>
<dt>-w &lt;outfile&gt;|-</p>
<dd> Sets the output filename. If the name is &#8216;<code>&#8211;</code>&#8216;, stdout will be used. This setting is mandatory.</dl>
<h2>EXAMPLES</h2>
<p> To merge two capture files together, 100 seconds apart use: </p>
<pre>
    capinfos -aeS a.pcap b.pcap
</pre>
<p> (Let&#8217;s suppose a.pcap starts at 1009932757 and b.pcap ends at 873660281. 1009932757 &#8211; 873660281 &#8211; 100 = 136272376 seconds.) </p>
<pre>
    editcap -t 136272376 b.pcap b-shifted.pcap
    mergecap -w compare.pcap a.pcap b-shifted.pcap
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-pcap/">pcap</a></i>(3), <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1), <i><a href="/docs/linux/man/1-tshark/">tshark</a></i>(1), <i><a href="/docs/linux/man/1-dumpcap/">dumpcap</a></i>(1), <i><a href="/docs/linux/man/1-editcap/">editcap</a></i>(1), <i><a href="/docs/linux/man/1-text2pcap/">text2pcap</a></i>(1), <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8)</p>
<h2>NOTES</h2>
<p> <code>Mergecap</code> is based heavily upon <code>editcap</code> by Richard Sharpe &lt;sharpe[<font SIZE="-1">AT</font>]ns.aus.com&gt; and Guy Harris &lt;guy[<font SIZE="-1">AT</font>]alum.mit.edu&gt;. </p>
<p> <code>Mergecap</code> is part of the <code>Wireshark</code> distribution. The latest version of <code>Wireshark</code> can be found at &lt;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&gt;. </p>
<p> <font SIZE="-1">HTML</font> versions of the Wireshark project man pages are available at: &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages">http://www.wireshark.org/docs/man-pages</a>&gt;.</p>
<h2>AUTHORS</h2>
<pre><code>
Original Author-- -- -- -- -- -- --Scott Renfro&lt;scott[AT] renfro.org&gt;
    Contributors-- -- -- -- -- --Bill Guyton&lt;guyton[AT] bguyton.com&gt;
</code></pre>
<h2>Index</h2>
