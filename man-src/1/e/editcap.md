---
title: "editcap(1)"
name: "editcap"
section: "1"
letter: "e"
url: "/docs/linux/man/1-editcap/"
description: "editcap – Edit and/or translate the format of capture files"
---

<h2 class="name">NAME</h2>
<p> editcap &#8211; Edit and/or translate the format of capture files </p>
<h2>SYNOPSIS</h2>
<p> <code>editcap</code> [&nbsp;<wbr><code>-A</code>&nbsp;<wbr>&lt;start time&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-B</code>&nbsp;<wbr>&lt;stop time&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-c</code>&nbsp;<wbr>&lt;packets per file&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-C</code>&nbsp;<wbr>&lt;choplen&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-E</code>&nbsp;<wbr>&lt;error probability&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-F</code>&nbsp;<wbr>&lt;file format&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-h</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-i</code>&nbsp;<wbr>&lt;seconds per file&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-r</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-s</code>&nbsp;<wbr>&lt;snaplen&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-S</code>&nbsp;<wbr>&lt;strict time adjustment&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-t</code>&nbsp;<wbr>&lt;time adjustment&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-T</code>&nbsp;<wbr>&lt;encapsulation type&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-v</code>&nbsp;<wbr>] <i>infile</i> <i>outfile</i> [&nbsp;<wbr><i>packet#</i>[-<i>packet#</i>]&nbsp;<wbr>&#8230;&nbsp;<wbr>] </p>
<p> <code>editcap</code> &nbsp;<wbr><code>-d</code>&nbsp;<wbr> | &nbsp;<wbr><code>-D</code>&nbsp;<wbr>&lt;dup window&gt;&nbsp;<wbr> | &nbsp;<wbr><code>-w</code>&nbsp;<wbr>&lt;dup time window&gt;&nbsp;<wbr> [&nbsp;<wbr><code>-v</code>&nbsp;<wbr>] <i>infile</i> <i>outfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Editcap</code> is a program that reads some or all of the captured packets from the <i>infile</i>, optionally converts them in various ways and writes the resulting packets to the capture <i>outfile</i> (or outfiles). </p>
<p> By default, it reads all packets from the <i>infile</i> and writes them to the <i>outfile</i> in pcap file format. </p>
<p> An optional list of packet numbers can be specified on the command tail; individual packet numbers separated by whitespace and/or ranges of packet numbers can be specified as <i>start</i>&#8211;<i>end</i>, referring to all packets from <i>start</i> to <i>end</i>. By default the selected packets with those numbers will <i>not</i> be written to the capture file. If the <code>-r</code> flag is specified, the whole packet selection is reversed; in that case <i>only</i> the selected packets will be written to the capture file. </p>
<p> <code>Editcap</code> can also be used to remove duplicate packets. Several different options (<code>-d</code>, <code>-D</code> and <code>-w</code>) are used to control the packet window or relative time window to be used for duplicate comparison. </p>
<p> <code>Editcap</code> is able to detect, read and write the same capture files that are supported by <code>Wireshark</code>. The input file doesn&#8217;t need a specific filename extension; the file format and an optional gzip compression will be automatically detected. Near the beginning of the <font SIZE="-1">DESCRIPTION</font> section of <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1) or &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages/wireshark.html">http://www.wireshark.org/docs/man-pages/wireshark.html</a>&gt; is a detailed description of the way <code>Wireshark</code> handles this, which is the same way <code>Editcap</code> handles this. </p>
<p> <code>Editcap</code> can write the file in several output formats. The <code>-F</code> flag can be used to specify the format in which to write the capture file; <code>editcap -F</code> provides a list of the available output formats.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-A &lt;start time&gt;</p>
<dd> Saves only the packets whose timestamp is on or after start time. The time is given in the following format YYYY-MM-DD <font SIZE="-1">HH:MM:SS</font></p>
<dt>-B &lt;stop time&gt;</p>
<dd> Saves only the packets whose timestamp is before stop time. The time is given in the following format YYYY-MM-DD <font SIZE="-1">HH:MM:SS</font></p>
<dt>-c &lt;packets per file&gt;</p>
<dd> Splits the packet output to different files based on uniform packet counts with a maximum of &lt;packets per file&gt; each. Each output file will be created with a suffix -nnnnn, starting with 00000. If the specified number of packets is written to the output file, the next output file is opened. The default is to use a single output file.</p>
<dt>-C &lt;choplen&gt;</p>
<dd> Sets the chop length to use when writing the packet data. Each packet is chopped by a few &lt;choplen&gt; bytes of data. Positive values chop at the packet beginning while negative values chop at the packet end. </p>
<p> This is useful for chopping headers for decapsulation of an entire capture or in the rare case that the conversion between two file formats leaves some random bytes at the end of each packet.</p>
<dt>-d</p>
<dd> Attempts to remove duplicate packets. The length and <font SIZE="-1">MD5</font> hash of the current packet are compared to the previous four (4) packets. If a match is found, the current packet is skipped. This option is equivalent to using the option <code>-D 5</code>.</p>
<dt>-D &lt;dup window&gt;</p>
<dd> Attempts to remove duplicate packets. The length and <font SIZE="-1">MD5</font> hash of the current packet are compared to the previous &lt;dup window&gt; &#8211; 1 packets. If a match is found, the current packet is skipped. </p>
<p> The use of the option <code>-D 0</code> combined with the <code>-v</code> option is useful in that each packet&#8217;s Packet number, Len and <font SIZE="-1">MD5</font> Hash will be printed to standard out. This verbose output (specifically the <font SIZE="-1">MD5</font> hash strings) can be useful in scripts to identify duplicate packets across trace files. </p>
<p> The &lt;dup window&gt; is specified as an integer value between 0 and 1000000 (inclusive). </p>
<p> <font SIZE="-1">NOTE:</font> Specifying large &lt;dup window&gt; values with large tracefiles can result in very long processing times for <code>editcap</code>.</p>
<dt>-E &lt;error probability&gt;</p>
<dd> Sets the probability that bytes in the output file are randomly changed. <code>Editcap</code> uses that probability (between 0.0 and 1.0 inclusive) to apply errors to each data byte in the file. For instance, a probability of 0.02 means that each byte has a 2% chance of having an error. </p>
<p> This option is meant to be used for fuzz-testing protocol dissectors.</p>
<dt>-F &lt;file format&gt;</p>
<dd> Sets the file format of the output capture file. <code>Editcap</code> can write the file in several formats, <code>editcap -F</code> provides a list of the available output formats. The default is the <code>pcap</code> format.</p>
<dt>-h</p>
<dd> Prints the version and options and exits.</p>
<dt>-i &lt;seconds per file&gt;</p>
<dd> Splits the packet output to different files based on uniform time intervals using a maximum interval of &lt;seconds per file&gt; each. Each output file will be created with a suffix -nnnnn, starting with 00000. If packets for the specified time interval are written to the output file, the next output file is opened. The default is to use a single output file.</p>
<dt>-r</p>
<dd> Reverse the packet selection. Causes the packets whose packet numbers are specified on the command line to be written to the output capture file, instead of discarding them.</p>
<dt>-s &lt;snaplen&gt;</p>
<dd> Sets the snapshot length to use when writing the data. If the <code>-s</code> flag is used to specify a snapshot length, packets in the input file with more captured data than the specified snapshot length will have only the amount of data specified by the snapshot length written to the output file. </p>
<p> This may be useful if the program that is to read the output file cannot handle packets larger than a certain size (for example, the versions of snoop in Solaris 2.5.1 and Solaris 2.6 appear to reject Ethernet packets larger than the standard Ethernet <font SIZE="-1">MTU,</font> making them incapable of handling gigabit Ethernet captures if jumbo packets were used).</p>
<dt>-S &lt;strict time adjustment&gt;</p>
<dd> Time adjust selected packets to insure strict chronological order. </p>
<p> The &lt;strict time adjustment&gt; value represents relative seconds specified as [-]<i>seconds</i>[<i>.fractional seconds</i>]. </p>
<p> As the capture file is processed each packet&#8217;s absolute time is <i>possibly</i> adjusted to be equal to or greater than the previous packet&#8217;s absolute timestamp depending on the &lt;strict time adjustment&gt; value. </p>
<p> If &lt;strict time adjustment&gt; value is 0 or greater (e.g. 0.000001) then <code>only</code> packets with a timestamp less than the previous packet will adjusted. The adjusted timestamp value will be set to be equal to the timestamp value of the previous packet plus the value of the &lt;strict time adjustment&gt; value. A &lt;strict time adjustment&gt; value of 0 will adjust the minimum number of timestamp values necessary to insure that the resulting capture file is in strict chronological order. </p>
<p> If &lt;strict time adjustment&gt; value is specified as a negative value, then the timestamp values of <code>all</code> packets will be adjusted to be equal to the timestamp value of the previous packet plus the absolute value of the &lt;lt&gt;strict time adjustment&lt;gt&gt; value. A &lt;strict time adjustment&gt; value of -0 will result in all packets having the timestamp value of the first packet. </p>
<p> This feature is useful when the trace file has an occasional packet with a negative delta time relative to the previous packet.</p>
<dt>-t &lt;time adjustment&gt;</p>
<dd> Sets the time adjustment to use on selected packets. If the <code>-t</code> flag is used to specify a time adjustment, the specified adjustment will be applied to all selected packets in the capture file. The adjustment is specified as [-]<i>seconds</i>[<i>.fractional seconds</i>]. For example, <code>-t</code> 3600 advances the timestamp on selected packets by one hour while <code>-t</code> -0.5 reduces the timestamp on selected packets by one-half second. </p>
<p> This feature is useful when synchronizing dumps collected on different machines where the time difference between the two machines is known or can be estimated.</p>
<dt>-T &lt;encapsulation type&gt;</p>
<dd> Sets the packet encapsulation type of the output capture file. If the <code>-T</code> flag is used to specify an encapsulation type, the encapsulation type of the output capture file will be forced to the specified type. <code>editcap -T</code> provides a list of the available types. The default type is the one appropriate to the encapsulation type of the input capture file. </p>
<p> Note: this merely forces the encapsulation type of the output file to be the specified type; the packet headers of the packets will not be translated from the encapsulation type of the input capture file to the specified encapsulation type (for example, it will not translate an Ethernet capture to an <font SIZE="-1">FDDI</font> capture if an Ethernet capture is read and &#8216;<code>-T fddi</code>&#8216; is specified). If you need to remove/add headers from/to a packet, you will need <i><a href="/docs/linux/man/1-od/">od</a></i>(1)/<i><a href="/docs/linux/man/1-text2pcap/">text2pcap</a></i>(1).</p>
<dt>-v</p>
<dd> Causes <code>editcap</code> to print verbose messages while it&#8217;s working. </p>
<p> Use of <code>-v</code> with the de-duplication switches of <code>-d</code>, <code>-D</code> or <code>-w</code> will cause all <font SIZE="-1">MD5</font> hashes to be printed whether the packet is skipped or not.</p>
<dt>-w &lt;dup time window&gt;</p>
<dd> Attempts to remove duplicate packets. The current packet&#8217;s arrival time is compared with up to 1000000 previous packets. If the packet&#8217;s relative arrival time is <i>less than or equal to</i> the &lt;dup time window&gt; of a previous packet and the packet length and <font SIZE="-1">MD5</font> hash of the current packet are the same then the packet to skipped. The duplicate comparison test stops when the current packet&#8217;s relative arrival time is greater than &lt;dup time window&gt;. </p>
<p> The &lt;dup time window&gt; is specified as <i>seconds</i>[<i>.fractional seconds</i>]. </p>
<p> The [.fractional seconds] component can be specified to nine (9) decimal places (billionths of a second) but most typical trace files have resolution to six (6) decimal places (millionths of a second). </p>
<p> <font SIZE="-1">NOTE:</font> Specifying large &lt;dup time window&gt; values with large tracefiles can result in very long processing times for <code>editcap</code>. </p>
<p> <font SIZE="-1">NOTE:</font> The <code>-w</code> option assumes that the packets are in chronological order. If the packets are <font SIZE="-1">NOT</font> in chronological order then the <code>-w</code> duplication removal option may not identify some duplicates.</dl>
<h2>EXAMPLES</h2>
<p> To see more detailed description of the options use: </p>
<pre>
    editcap -h
</pre>
<p> To shrink the capture file by truncating the packets at 64 bytes and writing it as Sun snoop file use: </p>
<pre>
    editcap -s 64 -F snoop capture.pcap shortcapture.snoop
</pre>
<p> To delete packet 1000 from the capture file use: </p>
<pre>
    editcap capture.pcap sans1000.pcap 1000
</pre>
<p> To limit a capture file to packets from number 200 to 750 (inclusive) use: </p>
<pre>
    editcap -r capture.pcap small.pcap 200-750
</pre>
<p> To get all packets from number 1-500 (inclusive) use: </p>
<pre>
    editcap -r capture.pcap first500.pcap 1-500
</pre>
<p> or </p>
<pre>
    editcap capture.pcap first500.pcap 501-9999999
</pre>
<p> To exclude packets 1, 5, 10 to 20 and 30 to 40 from the new file use: </p>
<pre>
    editcap capture.pcap exclude.pcap 1 5 10-20 30-40
</pre>
<p> To select just packets 1, 5, 10 to 20 and 30 to 40 for the new file use: </p>
<pre>
    editcap -r capture.pcap select.pcap 1 5 10-20 30-40
</pre>
<p> To remove duplicate packets seen within the prior four frames use: </p>
<pre>
    editcap -d capture.pcap dedup.pcap
</pre>
<p> To remove duplicate packets seen within the prior 100 frames use: </p>
<pre>
    editcap -D 101 capture.pcap dedup.pcap
</pre>
<p> To remove duplicate packets seen <i>equal to or less than</i> 1/10th of a second: </p>
<pre>
    editcap -w 0.1 capture.pcap dedup.pcap
</pre>
<p> To display the <font SIZE="-1">MD5</font> hash for all of the packets (and <font SIZE="-1">NOT</font> generate any real output file): </p>
<pre>
    editcap -v -D 0 capture.pcap /dev/null
</pre>
<p> or on Windows systems </p>
<pre>
    editcap -v -D 0 capture.pcap NUL
</pre>
<p> To advance the timestamps of each packet forward by 3.0827 seconds: </p>
<pre>
    editcap -t 3.0827 capture.pcap adjusted.pcap
</pre>
<p> To insure all timestamps are in strict chronological order: </p>
<pre>
    editcap -S 0 capture.pcap adjusted.pcap
</pre>
<p> To introduce 5% random errors in a capture file use: </p>
<pre>
    editcap -E 0.05 capture.pcap capture_error.pcap
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-pcap/">pcap</a></i>(3), <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1), <i><a href="/docs/linux/man/1-tshark/">tshark</a></i>(1), <i><a href="/docs/linux/man/1-mergecap/">mergecap</a></i>(1), <i><a href="/docs/linux/man/1-dumpcap/">dumpcap</a></i>(1), <i><a href="/docs/linux/man/1-capinfos/">capinfos</a></i>(1), <i><a href="/docs/linux/man/1-text2pcap/">text2pcap</a></i>(1), <i><a href="/docs/linux/man/1-od/">od</a></i>(1), <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8)</p>
<h2>NOTES</h2>
<p> <code>Editcap</code> is part of the <code>Wireshark</code> distribution. The latest version of <code>Wireshark</code> can be found at &lt;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&gt;. </p>
<p> <font SIZE="-1">HTML</font> versions of the Wireshark project man pages are available at: &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages">http://www.wireshark.org/docs/man-pages</a>&gt;.</p>
<h2>AUTHORS</h2>
<pre><code>
Original Author-- -- -- -- -- -- --Richard Sharpe&lt;sharpe[AT] ns.aus.com&gt;
    Contributors-- -- -- -- -- --Guy Harris&lt;guy[AT] alum.mit.edu&gt;
        Ulf Lamping&lt;ulf.lamping[AT] web.de&gt;
</code></pre>
<h2>Index</h2>
