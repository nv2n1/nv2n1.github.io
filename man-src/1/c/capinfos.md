---
title: "capinfos(1)"
name: "capinfos"
section: "1"
letter: "c"
url: "/docs/linux/man/1-capinfos/"
description: "capinfos – Prints information about capture files"
---

<h2 class="name">NAME</h2>
<p> capinfos &#8211; Prints information about capture files </p>
<h2>SYNOPSIS</h2>
<p> <code>capinfos</code> [&nbsp;<wbr><code>-a</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-A</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-b</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-B</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-c</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-C</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-d</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-e</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-E</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-h</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-H</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-i</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-l</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-L</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-m</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-M</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-N</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-o</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-q</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-Q</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-r</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-R</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-s</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-S</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-t</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-T</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-u</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-x</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-y</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-z</code>&nbsp;<wbr>] &lt;<i>infile</i>&gt; <i>&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Capinfos</code> is a program that reads one or more capture files and returns some or all available statistics (infos) of each &lt;<i>infile</i>&gt; in one of two types of output formats: long or table. </p>
<p> The long output is suitable for a human to read. The table output is useful for generating a report that can be easily imported into a spreadsheet or database. </p>
<p> The user specifies what type of output (long or table) and which statistics to display by specifying flags (options) that corresponding to the report type and desired infos. If no options are specified, <code>Capinfos</code> will report all statistics available in &#8220;long&#8221; format. </p>
<p> Options are processed from left to right order with later options superseding or adding to earlier options. </p>
<p> <code>Capinfos</code> is able to detect and read the same capture files that are supported by <code>Wireshark</code>. The input files don&#8217;t need a specific filename extension; the file format and an optional gzip compression will be automatically detected. Near the beginning of the <font SIZE="-1">DESCRIPTION</font> section of <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1) or &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages/wireshark.html">http://www.wireshark.org/docs/man-pages/wireshark.html</a>&gt; is a detailed description of the way <code>Wireshark</code> handles this, which is the same way <code>Capinfos</code> handles this.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-a</p>
<dd> Displays the start time of the capture. <code>Capinfos</code> considers the earliest timestamp seen to be the start time, so the first packet in the capture is not necessarily the earliest &#8211; if packets exist &#8220;out-of-order&#8221;, time-wise, in the capture, <code>Capinfos</code> detects this.</p>
<dt>-A</p>
<dd> Generate all infos. By default capinfos will display all infos values for each input file, but enabling any of the individual display infos options will disable the generate all option.</p>
<dt>-b</p>
<dd> Separate infos with <font SIZE="-1">ASCII SPACE </font>(0x20) characters. This option is only useful when generating a table style report (-T). The various info values will be separated (delimited) from one another with a single <font SIZE="-1">ASCII SPACE</font> character. </p>
<p> <font SIZE="-1">NOTE:</font> Since some of the header labels as well as some of the value fields contain <font SIZE="-1">SPACE</font> characters. This option is of limited value unless one of the quoting options (-q or -Q) is also specified.</p>
<dt>-B</p>
<dd> Separate the infos with <font SIZE="-1">ASCII TAB</font> characters. This option is only useful when generating a table style report (-T). The various info values will be separated (delimited) from one another with a single <font SIZE="-1">ASCII TAB</font> character. The <font SIZE="-1">TAB</font> character is the default delimiter when -T style report is enabled.</p>
<dt>-c</p>
<dd> Displays the number of packets in the capture file.</p>
<dt>-C</p>
<dd> Cancel processing any additional files if and when capinfos should fail to open an input file. By default capinfos will attempt to open each and every file name argument. </p>
<p> Note: An error message will be written to stderr whenever capinfos fails to open a file regardless of whether the -C option is specified or not. Upon exit, capinfos will return an error status if any errors occurred during processing.</p>
<dt>-d</p>
<dd> Displays the total length of all packets in the file, in bytes. This counts the size of the packets as they appeared in their original form, not as they appear in this file. For example, if a packet was originally 1514 bytes and only 256 of those bytes were saved to the capture file (if packets were captured with a snaplen or other slicing option), <code>Capinfos</code> will consider the packet to have been 1514 bytes.</p>
<dt>-e</p>
<dd> Displays the end time of the capture. <code>Capinfos</code> considers the latest timestamp seen to be the end time, so the last packet in the capture is not necessarily the latest &#8211; if packets exist &#8220;out-of-order&#8221;, time-wise, in the capture, <code>Capinfos</code> detects this.</p>
<dt>-E</p>
<dd> Displays the per-file encapsulation of the capture file.</p>
<dt>-h</p>
<dd> Prints the help listing and exits.</p>
<dt>-H</p>
<dd> Displays the <font SIZE="-1">SHA1, RIPEMD160,</font> and <font SIZE="-1">MD5</font> hashes for the file.</p>
<dt>-i</p>
<dd> Displays the average data rate, in bits/sec</p>
<dt>-k</p>
<dd> Displays the capture comment. For pcapng files, this is the comment from the section header block.</p>
<dt>-l</p>
<dd> Display the snaplen (if any) for a file. snaplen (if available) is determined from the capture file header and by looking for truncated records in the capture file.</p>
<dt>-L</p>
<dd> Generate long report. Capinfos can generate two different styles of reports. The &#8220;long&#8221; report is the default style of output and is suitable for a human to use.</p>
<dt>-m</p>
<dd> Separate the infos with comma (,) characters. This option is only useful when generating a table style report (-T). The various info values will be separated (delimited) from one another with a single comma &#8220;,&#8221; character.</p>
<dt>-M</p>
<dd> Print raw (machine readable) numeric values in long reports. By default capinfos prints human-readable values with <font SIZE="-1">SI</font> suffixes. Table reports (-T) always print raw values.</p>
<dt>-N</p>
<dd> Do not quote the infos. This option is only useful when generating a table style report (-T). Excluding any quoting characters around the various values and using a <font SIZE="-1">TAB</font> delimiter produces a very &#8220;clean&#8221; table report that is easily parsed with <font SIZE="-1">CLI</font> tools. By default infos are <font SIZE="-1"><code>NOT</code></font> quoted.</p>
<dt>-o</p>
<dd> Displays &#8220;True&#8221; if packets exist in strict chronological order or &#8220;False&#8221; if one or more packets in the capture exists &#8220;out-of-order&#8221; time-wise.</p>
<dt>-q</p>
<dd> Quote infos with single quotes (&#8216;). This option is only useful when generating a table style report (-T). When this option is enabled, each value will be encapsulated within a pair of single quote (&#8216;) characters. This option (when used with the -m option) is useful for generating one type of <font SIZE="-1">CSV</font> style file report.</p>
<dt>-Q</p>
<dd> Quote infos with double quotes (&#8220;). This option is only useful when generating a table style report (-T). When this option is enabled, each value will be encapsulated within a pair of double quote (&#8221;) characters. This option (when used with the -m option) is useful for generating the most common type of <font SIZE="-1">CSV</font> style file report.</p>
<dt>-r</p>
<dd> Do not generate header record. This option is only useful when generating a table style report (-T). If this option is specified then <code>no</code> header record will be generated within the table report.</p>
<dt>-R</p>
<dd> Generate header record. This option is only useful when generating a table style report (-T). A header is generated by default. A header record (if generated) is the first line of data reported and includes labels for all the columns included within the table report.</p>
<dt>-s</p>
<dd> Displays the size of the file, in bytes. This reports the size of the capture file itself.</p>
<dt>-S</p>
<dd> Display the start and end times as seconds since January 1, 1970. Handy for synchronizing dumps using <code>editcap -t</code>.</p>
<dt>-t</p>
<dd> Displays the capture type of the capture file.</p>
<dt>-T</p>
<dd> Generate a table report. A table report is a text file that is suitable for importing into a spreadsheet or database. Capinfos can build a tab delimited text file (the default) or several variations on Comma-separated values (<font SIZE="-1">CSV</font>) files.</p>
<dt>-u</p>
<dd> Displays the capture duration, in seconds. This is the difference in time between the earliest packet seen and latest packet seen.</p>
<dt>-x</p>
<dd> Displays the average packet rate, in packets/sec</p>
<dt>-y</p>
<dd> Displays the average data rate, in bytes/sec</p>
<dt>-z</p>
<dd> Displays the average packet size, in bytes</dl>
<h2>EXAMPLES</h2>
<p> To see a description of the capinfos options use: </p>
<pre>
    capinfos -h
</pre>
<p> To generate a long form report for the capture file mycapture.pcap use: </p>
<pre>
    capinfos mycapture.pcap
</pre>
<p> To generate a <font SIZE="-1">TAB</font> delimited table form report for the capture file mycapture.pcap use: </p>
<pre>
    capinfos -T mycapture.pcap
</pre>
<p> To generate a <font SIZE="-1">CSV</font> style table form report for the capture file mycapture.pcap use: </p>
<pre>
    capinfos -T -m -Q mycapture.pcap
</pre>
<p> or </p>
<pre>
    capinfos -TmQ mycapture.pcap
</pre>
<p> To generate a <font SIZE="-1">TAB</font> delimited table style report with just the filenames, capture type, capture encapsulation type and packet count for all the pcap files in the current directory use: </p>
<pre>
    capinfos -T -t -E -c *.pcap
</pre>
<p> or </p>
<pre>
    capinfos -TtEs *.pcap
</pre>
<p> Note: The ability to use of filename globbing characters are a feature of *nix style command shells. </p>
<p> To generate a <font SIZE="-1">CSV</font> delimited table style report of all infos for all pcap files in the current directory and write it to a text file called mycaptures.csv use: </p>
<pre>
    capinfos -TmQ *.pcap &gt;mycaptures.csv
</pre>
<p> The resulting mycaptures.csv file can be easily imported into spreadsheet applications.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-pcap/">pcap</a></i>(3), <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1), <i><a href="/docs/linux/man/1-mergecap/">mergecap</a></i>(1), <i><a href="/docs/linux/man/1-editcap/">editcap</a></i>(1), <i><a href="/docs/linux/man/1-tshark/">tshark</a></i>(1), <i><a href="/docs/linux/man/1-dumpcap/">dumpcap</a></i>(1), <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8)</p>
<h2>NOTES</h2>
<p> <code>Capinfos</code> is part of the <code>Wireshark</code> distribution. The latest version of <code>Wireshark</code> can be found at &lt;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&gt;. </p>
<p> <font SIZE="-1">HTML</font> versions of the Wireshark project man pages are available at: &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages">http://www.wireshark.org/docs/man-pages</a>&gt;.</p>
<h2>AUTHORS</h2>
<pre><code>
Original Author-- -- -- -- -- -- --Ian Schorr&lt;ian[AT] ianschorr.com&gt;
    Contributors-- -- -- -- -- --Gerald Combs&lt;gerald[AT] wireshark.org&gt;
        Jim Young&lt;jyoung[AT] gsu.edu&gt;
</code></pre>
<h2>Index</h2>
