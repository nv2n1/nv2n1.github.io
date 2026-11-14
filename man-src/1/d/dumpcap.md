---
title: "dumpcap(1)"
name: "dumpcap"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dumpcap/"
description: "dumpcap – Dump network traffic"
---

<h2 class="name">NAME</h2>
<p> dumpcap &#8211; Dump network traffic </p>
<h2>SYNOPSIS</h2>
<p> <code>dumpcap</code> [&nbsp;<wbr><code>-a</code>&nbsp;<wbr>&lt;capture autostop condition&gt;&nbsp;<wbr>]&nbsp;<wbr>&#8230; [&nbsp;<wbr><code>-b</code>&nbsp;<wbr>&lt;capture ring buffer option&gt;]&nbsp;<wbr>&#8230; [&nbsp;<wbr><code>-B</code>&nbsp;<wbr>&lt;capture buffer size&gt;&nbsp;<wbr>]&nbsp;<wbr> [&nbsp;<wbr><code>-c</code>&nbsp;<wbr>&lt;capture packet count&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-C</code>&nbsp;<wbr>&lt;byte limit&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-d</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-D</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-f</code>&nbsp;<wbr>&lt;capture filter&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-g</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-h</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-i</code>&nbsp;<wbr>&lt;capture interface&gt;|rpcap://&lt;host&gt;/&lt;capture interface&gt;|TCP@&lt;host&gt;:&lt;port&gt;|-&nbsp;<wbr>] [&nbsp;<wbr><code>-I</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-L</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-M</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-n</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-N</code>&nbsp;<wbr>&lt;packet limit&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-p</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-P</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-q</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-s</code>&nbsp;<wbr>&lt;capture snaplen&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-S</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-t</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-v</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-w</code>&nbsp;<wbr>&lt;outfile&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-y</code>&nbsp;<wbr>&lt;capture link type&gt;&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Dumpcap</code> is a network traffic dump tool. It lets you capture packet data from a live network and write the packets to a file. <code>Dumpcap</code>&#8216;s default capture file format is <code>pcap-ng</code> format. When the <code>-P</code> option is specified, the output file is written in the <code>pcap</code> format. </p>
<p> Without any options set it will use the libpcap/WinPcap library to capture traffic from the first available network interface and writes the received raw packet data, along with the packets&#8217; time stamps into a pcap file. </p>
<p> If the <code>-w</code> option is not specified, <code>Dumpcap</code> writes to a newly created pcap file with a randomly chosen name. If the <code>-w</code> option is specified, <code>Dumpcap</code> writes to the file specified by that option. </p>
<p> Packet capturing is performed with the pcap library. The capture filter syntax follows the rules of the pcap library.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-a &lt;capture autostop condition&gt;</p>
<dd> Specify a criterion that specifies when <code>Dumpcap</code> is to stop writing to a capture file. The criterion is of the form <i>test</i><code>:</code><i>value</i>, where <i>test</i> is one of: </p>
<p> <code>duration</code>:<i>value</i> Stop writing to a capture file after <i>value</i> seconds have elapsed. </p>
<p> <code>filesize</code>:<i>value</i> Stop writing to a capture file after it reaches a size of <i>value</i> kB. If this option is used together with the -b option, dumpcap will stop writing to the current capture file and switch to the next one if filesize is reached. Note that the filesize is limited to a maximum value of 2 GiB. </p>
<p> <code>files</code>:<i>value</i> Stop writing to capture files after <i>value</i> number of files were written.</p>
<dt>-b &lt;capture ring buffer option&gt;</p>
<dd> Cause <code>Dumpcap</code> to run in &#8220;multiple files&#8221; mode. In &#8220;multiple files&#8221; mode, <code>Dumpcap</code> will write to several capture files. When the first capture file fills up, <code>Dumpcap</code> will switch writing to the next file and so on. </p>
<p> The created filenames are based on the filename given with the <code>-w</code> option, the number of the file and on the creation date and time, e.g. outfile_00001_20050604120117.pcap, outfile_00002_20050604120523.pcap, &#8230; </p>
<p> With the <i>files</i> option it&#8217;s also possible to form a &#8220;ring buffer&#8221;. This will fill up new files until the number of files specified, at which point <code>Dumpcap</code> will discard the data in the first file and start writing to that file and so on. If the <i>files</i> option is not set, new files filled up until one of the capture stop conditions match (or until the disk is full). </p>
<p> The criterion is of the form <i>key</i><code>:</code><i>value</i>, where <i>key</i> is one of: </p>
<p> <code>duration</code>:<i>value</i> switch to the next file after <i>value</i> seconds have elapsed, even if the current file is not completely filled up. </p>
<p> <code>filesize</code>:<i>value</i> switch to the next file after it reaches a size of <i>value</i> kB. Note that the filesize is limited to a maximum value of 2 GiB. </p>
<p> <code>files</code>:<i>value</i> begin again with the first file after <i>value</i> number of files were written (form a ring buffer). This value must be less than 100000. Caution should be used when using large numbers of files: some filesystems do not handle many files in a single directory well. The <code>files</code> criterion requires either <code>duration</code> or <code>filesize</code> to be specified to control when to go to the next file. It should be noted that each <code>-b</code> parameter takes exactly one criterion; to specify two criterion, each must be preceded by the <code>-b</code> option. </p>
<p> Example: <code>-b filesize:1000 -b files:5</code> results in a ring buffer of five files of size one megabyte each.</p>
<dt>-B &lt;capture buffer size&gt;</p>
<dd> Set capture buffer size (in MiB, default is 2 MiB). This is used by the capture driver to buffer packet data until that data can be written to disk. If you encounter packet drops while capturing, try to increase this size. Note that, while <code>Dumpcap</code> attempts to set the buffer size to 2 MiB by default, and can be told to set it to a larger value, the system or interface on which you&#8217;re capturing might silently limit the capture buffer size to a lower value or raise it to a higher value. </p>
<p> This is available on <font SIZE="-1">UNIX</font> systems with libpcap 1.0.0 or later and on Windows. It is not available on <font SIZE="-1">UNIX</font> systems with earlier versions of libpcap. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default capture buffer size. If used after an <code>-i</code> option, it sets the capture buffer size for the interface specified by the last <code>-i</code> option occurring before this option. If the capture buffer size is not set specifically, the default capture buffer size is used instead.</p>
<dt>-c &lt;capture packet count&gt;</p>
<dd> Set the maximum number of packets to read when capturing live data.</p>
<dt>-C &lt;byte limit&gt;</p>
<dd> Limit the amount of memory in bytes used for storing captured packets in memory while processing it. If used in combination with the <code>-N</code> option, both limits will apply. Setting this limit will enable the usage of the separate thread per interface.</p>
<dt>-d</p>
<dd> Dump the code generated for the capture filter in a human-readable form, and exit.</p>
<dt>-D</p>
<dd> Print a list of the interfaces on which <code>Dumpcap</code> can capture, and exit. For each network interface, a number and an interface name, possibly followed by a text description of the interface, is printed. The interface name or the number can be supplied to the <code>-i</code> option to specify an interface on which to capture. </p>
<p> This can be useful on systems that don&#8217;t have a command to list them (e.g., Windows systems, or <font SIZE="-1">UNIX</font> systems lacking <code>ifconfig -a</code>); the number can be useful on Windows 2000 and later systems, where the interface name is a somewhat complex string. </p>
<p> Note that &#8220;can capture&#8221; means that <code>Dumpcap</code> was able to open that device to do a live capture. Depending on your system you may need to run dumpcap from an account with special privileges (for example, as root) to be able to capture network traffic. If &quot;<code>dumpcap -D</code>&quot; is not run from such an account, it will not list any interfaces.</p>
<dt>-f &lt;capture filter&gt;</p>
<dd> Set the capture filter expression. </p>
<p> The entire filter expression must be specified as a single argument (which means that if it contains spaces, it must be quoted). </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default capture filter expression. If used after an <code>-i</code> option, it sets the capture filter expression for the interface specified by the last <code>-i</code> option occurring before this option. If the capture filter expression is not set specifically, the default capture filter expression is used if provided.</p>
<dt>-g</p>
<dd> This option causes the output file(s) to be created with group-read permission (meaning that the output file(s) can be read by other members of the calling user&#8217;s group).</p>
<dt>-h</p>
<dd> Print the version and options and exits.</p>
<dt>-i &lt;capture interface&gt;|rpcap://&lt;host&gt;/&lt;capture interface&gt;|TCP@&lt;host&gt;:&lt;port&gt;|-</p>
<dd> Set the name of the network interface or pipe to use for live packet capture. </p>
<p> Network interface names should match one of the names listed in &quot;<code>dumpcap -D</code>&#8220; (described above); a number, as reported by &#8221;<code>dumpcap -D</code>&#8220;, can also be used. If you&#8217;re using <font SIZE="-1">UNIX, &#8221;</font><code>netstat -i</code>&#8220; or &#8221;<code>ifconfig -a</code>&quot; might also work to list interface names, although not all versions of <font SIZE="-1">UNIX</font> support the <code>-a</code> option to <code>ifconfig</code>. </p>
<p> If no interface is specified, <code>Dumpcap</code> searches the list of interfaces, choosing the first non-loopback interface if there are any non-loopback interfaces, and choosing the first loopback interface if there are no non-loopback interfaces. If there are no interfaces at all, <code>Dumpcap</code> reports an error and doesn&#8217;t start the capture. </p>
<p> Pipe names should be either the name of a <font SIZE="-1">FIFO </font>(named pipe) or &#8220;-&#8221; to read data from the standard input. Data read from pipes must be in standard pcap format. </p>
<p> This option can occur multiple times. When capturing from multiple interfaces, the capture file will be saved in pcap-ng format. </p>
<p> Note: the Win32 version of <code>Dumpcap</code> doesn&#8217;t support capturing from pipes or stdin!</p>
<dt>-I</p>
<dd> Put the interface in &#8220;monitor mode&#8221;; this is supported only on <font SIZE="-1">IEEE 802.11</font> Wi-Fi interfaces, and supported only on some operating systems. </p>
<p> Note that in monitor mode the adapter might disassociate from the network with which it&#8217;s associated, so that you will not be able to use any wireless networks with that adapter. This could prevent accessing files on a network server, or resolving host names or network addresses, if you are capturing in monitor mode and are not connected to another network with another adapter. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it enables the monitor mode for all interfaces. If used after an <code>-i</code> option, it enables the monitor mode for the interface specified by the last <code>-i</code> option occurring before this option.</p>
<dt>-L</p>
<dd> List the data link types supported by the interface and exit. The reported link types can be used for the <code>-y</code> option.</p>
<dt>-M</p>
<dd> When used with <code>-D</code>, <code>-L</code> or <code>-S</code>, print machine-readable output. The machine-readable output is intended to be read by <code>Wireshark</code> and <code>TShark</code>; its format is subject to change from release to release.</p>
<dt>-n</p>
<dd> Save files as pcap-ng. This is the default.</p>
<dt>-N &lt;packet limit&gt;</p>
<dd> Limit the number of packets used for storing captured packets in memory while processing it. If used in combination with the <code>-C</code> option, both limits will apply. Setting this limit will enable the usage of the separate thread per interface.</p>
<dt>-p</p>
<dd> <i>Don&#8217;t</i> put the interface into promiscuous mode. Note that the interface might be in promiscuous mode for some other reason; hence, <code>-p</code> cannot be used to ensure that the only traffic that is captured is traffic sent to or from the machine on which <code>Dumpcap</code> is running, broadcast traffic, and multicast traffic to addresses received by that machine. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, no interface will be put into the promiscuous mode. If used after an <code>-i</code> option, the interface specified by the last <code>-i</code> option occurring before this option will not be put into the promiscuous mode.</p>
<dt>-P</p>
<dd> Save files as pcap instead of the default pcap-ng. In situations that require pcap-ng, such as capturing from multiple interfaces, this option will be overridden.</p>
<dt>-q</p>
<dd> When capturing packets, don&#8217;t display the continuous count of packets captured that is normally shown when saving a capture to a file; instead, just display, at the end of the capture, a count of packets captured. On systems that support the <font SIZE="-1">SIGINFO</font> signal, such as various BSDs, you can cause the current count to be displayed by typing your &#8220;status&#8221; character (typically control-T, although it might be set to &#8220;disabled&#8221; by default on at least some BSDs, so you&#8217;d have to explicitly set it to use it).</p>
<dt>-s &lt;capture snaplen&gt;</p>
<dd> Set the default snapshot length to use when capturing live data. No more than <i>snaplen</i> bytes of each network packet will be read into memory, or saved to disk. A value of 0 specifies a snapshot length of 65535, so that the full packet is captured; this is the default. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default snapshot length. If used after an <code>-i</code> option, it sets the snapshot length for the interface specified by the last <code>-i</code> option occurring before this option. If the snapshot length is not set specifically, the default snapshot length is used if provided.</p>
<dt>-S</p>
<dd> Print statistics for each interface once every second.</p>
<dt>-t</p>
<dd> Use a separate thread per interface.</p>
<dt>-v</p>
<dd> Print the version and exit.</p>
<dt>-w &lt;outfile&gt;</p>
<dd> Write raw packet data to <i>outfile</i>. </p>
<p> <font SIZE="-1">NOTE:</font> The usage of &#8220;-&#8221; for stdout is not allowed here!</p>
<dt>-y &lt;capture link type&gt;</p>
<dd> Set the data link type to use while capturing packets. The values reported by <code>-L</code> are the values that can be used. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default capture link type. If used after an <code>-i</code> option, it sets the capture link type for the interface specified by the last <code>-i</code> option occurring before this option. If the capture link type is not set specifically, the default capture link type is used if provided.</dl>
<h2>CAPTURE FILTER SYNTAX</h2>
<p> See the manual page of <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or, if that doesn&#8217;t exist, <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8), or, if that doesn&#8217;t exist, &lt;<a rel="nofollow" href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1), <i><a href="/docs/linux/man/1-tshark/">tshark</a></i>(1), <i><a href="/docs/linux/man/1-editcap/">editcap</a></i>(1), <i><a href="/docs/linux/man/1-mergecap/">mergecap</a></i>(1), <i><a href="/docs/linux/man/1-capinfos/">capinfos</a></i>(1), <i><a href="/docs/linux/man/3-pcap/">pcap</a></i>(3), <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8)</p>
<h2>NOTES</h2>
<p> <code>Dumpcap</code> is part of the <code>Wireshark</code> distribution. The latest version of <code>Wireshark</code> can be found at &lt;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&gt;. </p>
<p> <font SIZE="-1">HTML</font> versions of the Wireshark project man pages are available at: &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages">http://www.wireshark.org/docs/man-pages</a>&gt;.</p>
<h2>AUTHORS</h2>
<p> <code>Dumpcap</code> is derived from the <code>Wireshark</code> capturing engine code; see the list of authors in the <code>Wireshark</code> man page for a list of authors of that code. </p>
<h2>Index</h2>
