---
title: "tcpdump(8)"
name: "tcpdump"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcpdump/"
description: "tcpdump – dump traffic on a network"
---

<p>tcpdump &#8211; dump traffic on a network</p>
<h2>Synopsis</h2>
<p><code>tcpdump</code> [ <code>-AbdDefhHIJKlLnNOpqStuUvxX#</code> ] [ <code>-B</code> <i>buffer_size</i> ] </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <code>-c</code> <i>count</i> ] [ <code>&#8211;count</code> ] [ <code>-C</code> <i>file_size</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <code>-E</code> <i>spi [at] ipaddr algo:secret,&#8230;</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <code>-F</code> <i>file</i> ] [ <code>-G</code> <i>rotate_seconds</i> ] [ <code>-i</code> <i>interface</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <code>&#8211;immediate-mode</code> ] [ <code>-j</code> <i>tstamp_type</i> ] [ <code>-m</code> <i>module</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <code>-M</code> <i>secret</i> ] [ <code>&#8211;number</code> ] [ <code>&#8211;print</code> ] [ <code>-Q</code> <i>in|out|inout</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <code>-r</code> <i>file</i> ] [ <code>-s</code> <i>snaplen</i> ] [ <code>-T</code> <i>type</i> ] [ <code>&#8211;version</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <code>-V</code> <i>file</i> ] [ <code>-w</code> <i>file</i> ] [ <code>-W</code> <i>filecount</i> ] [ <code>-y</code> <i>datalinktype</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <code>-z</code> <i>postrotate-command</i> ] [ <code>-Z</code> <i>user</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <code>&#8211;time-stamp-precision=</code><i>tstamp_precision</i> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <code>&#8211;micro</code> ] [ <code>&#8211;nano</code> ]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [ <i>expression</i> ]</p>
<h2>Description</h2>
<p><i>Tcpdump</i> prints out a description of the contents of packets on a network interface that match the Boolean <i>expression</i>; the description is preceded by a time stamp, printed, by default, as hours, minutes, seconds, and fractions of a second since midnight. It can also be run with the <code>-w</code> flag, which causes it to save the packet data to a file for later analysis, and/or with the <code>-r</code> flag, which causes it to read from a saved packet file rather than to read packets from a network interface. It can also be run with the <code>-V</code> flag, which causes it to read a list of saved packet files. In all cases, only packets that match <i>expression</i> will be processed by <i>tcpdump</i>. </p>
<p> <i>Tcpdump</i> will, if not run with the <code>-c</code> flag, continue capturing packets until it is interrupted by a SIGINT signal (generated, for example, by typing your interrupt character, typically control-C) or a SIGTERM signal (typically generated with the <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1) command); if run with the <code>-c</code> flag, it will capture packets until it is interrupted by a SIGINT or SIGTERM signal or the specified number of packets have been processed. </p>
<p> When <i>tcpdump</i> finishes capturing packets, it will report counts of:</p>
<dl>
<dd>packets &#8220;captured&#8221; (this is the number of packets that <i>tcpdump</i> has received and processed);</p>
<dd>packets &#8220;received by filter&#8221; (the meaning of this depends on the OS on which you&#8217;re running <i>tcpdump</i>, and possibly on the way the OS was configured &#8211; if a filter was specified on the command line, on some OSes it counts packets regardless of whether they were matched by the filter expression and, even if they were matched by the filter expression, regardless of whether <i>tcpdump</i> has read and processed them yet, on other OSes it counts only packets that were matched by the filter expression regardless of whether <i>tcpdump</i> has read and processed them yet, and on other OSes it counts only packets that were matched by the filter expression and were processed by <i>tcpdump</i>);</p>
<dd>packets &#8220;dropped by kernel&#8221; (this is the number of packets that were dropped, due to a lack of buffer space, by the packet capture mechanism in the OS on which <i>tcpdump</i> is running, if the OS reports that information to applications; if not, it will be reported as 0).</dl>
<p> On platforms that support the SIGINFO signal, such as most BSDs (including macOS) and Digital/Tru64 UNIX, it will report those counts when it receives a SIGINFO signal (generated, for example, by typing your &#8220;status&#8221; character, typically control-T, although on some platforms, such as macOS, the &#8220;status&#8221; character is not set by default, so you must set it with <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1) in order to use it) and will continue capturing packets. On platforms that do not support the SIGINFO signal, the same can be achieved by using the SIGUSR1 signal. </p>
<p> Using the SIGUSR2 signal along with the <code>-w</code> flag will forcibly flush the packet buffer into the output file. </p>
<p> Reading packets from a network interface may require that you have special privileges; see the <code>pcap</code>(3PCAP) man page for details. Reading a saved packet file doesn&#8217;t require special privileges.</p>
<h2>Options</h2>
<dl>
<dt><code>-A</code></p>
<dd>Print each packet (minus its link level header) in ASCII. Handy for capturing web pages.</p>
<dt><code>-b</code></p>
<dd>Print the AS number in BGP packets in ASDOT notation rather than ASPLAIN notation.</p>
<dt><code>-B</code><i> buffer_size</i></p>
<dd>
<dt><code>&#8211;buffer-size=</code><i>buffer_size</i></p>
<dd>Set the operating system capture buffer size to <i>buffer_size</i>, in units of KiB (1024 bytes).</p>
<dt><code>-c</code><i> count</i></p>
<dd>Exit after receiving <i>count</i> packets.</p>
<dt><code>&#8211;count</code></p>
<dd>Print only on stderr the packet count when reading capture file(s) instead of parsing/printing the packets. If a filter is specified on the command line, <i>tcpdump</i> counts only packets that were matched by the filter expression.</p>
<dt><code>-C</code><i> file_size</i></p>
<dd>Before writing a raw packet to a savefile, check whether the file is currently larger than <i>file_size</i> and, if so, close the current savefile and open a new one. Savefiles after the first savefile will have the name specified with the <code>-w</code> flag, with a number after it, starting at 1 and continuing upward. The units of <i>file_size</i> are millions of bytes (1,000,000 bytes, not 1,048,576 bytes). </p>
<p> Note that when used with <code>-Z</code> option (enabled by default), privileges are dropped before opening first savefile.</p>
<dt><code>-d</code></p>
<dd>Dump the compiled packet-matching code in a human readable form to standard output and stop.</p>
<dd>Please mind that although code compilation is always DLT-specific, typically it is impossible (and unnecessary) to specify which DLT to use for the dump because <i>tcpdump</i> uses either the DLT of the input pcap file specified with <code>-r</code>, or the default DLT of the network interface specified with <code>-i</code>, or the particular DLT of the network interface specified with <code>-y</code> and <code>-i</code> respectively. In these cases the dump shows the same exact code that would filter the input file or the network interface without <code>-d</code>.</p>
<dd>However, when neither <code>-r</code> nor <code>-i</code> is specified, specifying <code>-d</code> prevents <i>tcpdump</i> from guessing a suitable network interface (see <code>-i</code>). In this case the DLT defaults to EN10MB and can be set to another valid value manually with <code>-y</code>.</p>
<dt><code>-dd</code></p>
<dd>Dump packet-matching code as a <code>C</code> program fragment.</p>
<dt><code>-ddd</code></p>
<dd>Dump packet-matching code as decimal numbers (preceded with a count).</p>
<dt><code>-D</code></p>
<dd>
<dt><code>&#8211;list-interfaces</code></p>
<dd>Print the list of the network interfaces available on the system and on which <i>tcpdump</i> can capture packets. For each network interface, a number and an interface name, possibly followed by a text description of the interface, are printed. The interface name or the number can be supplied to the <code>-i</code> flag to specify an interface on which to capture.</p>
<dd>This can be useful on systems that don&#8217;t have a command to list them (e.g., Windows systems, or UNIX systems lacking <code>ifconfig -a</code>); the number can be useful on Windows 2000 and later systems, where the interface name is a somewhat complex string.</p>
<dd>The <code>-D</code> flag will not be supported if <i>tcpdump</i> was built with an older version of <i>libpcap</i> that lacks the <code>pcap_findalldevs(3PCAP)</code> function.</p>
<dt><code>-e</code></p>
<dd>Print the link-level header on each dump line. This can be used, for example, to print MAC layer addresses for protocols such as Ethernet and IEEE 802.11.</p>
<dt><code>-E</code></p>
<dd>Use <i>spi [at] ipaddr algo:secret</i> for decrypting IPsec ESP packets that are addressed to <i>addr</i> and contain Security Parameter Index value <i>spi</i>. This combination may be repeated with comma or newline separation.</p>
<dd>Note that setting the secret for IPv4 ESP packets is supported at this time.</p>
<dd>Algorithms may be <code>des-cbc</code>, <code>3des-cbc</code>, <code>blowfish-cbc</code>, <code>rc3-cbc</code>, <code>cast128-cbc</code>, or <code>none</code>. The default is <code>des-cbc</code>. The ability to decrypt packets is only present if <i>tcpdump</i> was compiled with cryptography enabled.</p>
<dd><i>secret</i> is the ASCII text for ESP secret key. If preceded by 0x, then a hex value will be read.</p>
<dd>The option assumes RFC2406 ESP, not RFC1827 ESP. The option is only for debugging purposes, and the use of this option with a true `secret&#8217; key is discouraged. By presenting IPsec secret key onto command line you make it visible to others, via <i><a href="/docs/linux/man/1-ps/">ps</a></i>(1) and other occasions.</p>
<dd>In addition to the above syntax, the syntax <i>file name</i> may be used to have tcpdump read the provided file in. The file is opened upon receiving the first ESP packet, so any special permissions that tcpdump may have been given should already have been given up.</p>
<dt><code>-f</code></p>
<dd>Print `foreign&#8217; IPv4 addresses numerically rather than symbolically (this option is intended to get around serious brain damage in Sun&#8217;s NIS server &#8212; usually it hangs forever translating non-local internet numbers).</p>
<dd>The test for `foreign&#8217; IPv4 addresses is done using the IPv4 address and netmask of the interface on which capture is being done. If that address or netmask are not available, available, either because the interface on which capture is being done has no address or netmask or because the capture is being done on the Linux &quot;any&quot; interface, which can capture on more than one interface, this option will not work correctly.</p>
<dt><code>-F</code><i> file</i></p>
<dd>Use <i>file</i> as input for the filter expression. An additional expression given on the command line is ignored.</p>
<dt><code>-G</code><i> rotate_seconds</i></p>
<dd>If specified, rotates the dump file specified with the <code>-w</code> option every <i>rotate_seconds</i> seconds. Savefiles will have the name specified by <code>-w</code> which should include a time format as defined by <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). If no time format is specified, each new file will overwrite the previous. Whenever a generated filename is not unique, tcpdump will overwrite the pre-existing data; providing a time specification that is coarser than the capture period is therefore not advised.</p>
<dd>If used in conjunction with the <code>-C</code> option, filenames will take the form of `<i>file</i>&lt;count&gt;&#8217;.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>Print the tcpdump and libpcap version strings, print a usage message, and exit.</p>
<dt><code>&#8211;version</code></p>
<dd>Print the tcpdump and libpcap version strings and exit.</p>
<dt><code>-H</code></p>
<dd>Attempt to detect 802.11s draft mesh headers.</p>
<dt><code>-i</code><i> interface</i></p>
<dd>
<dt><code>&#8211;interface=</code><i>interface</i></p>
<dd>Listen, report the list of link-layer types, report the list of time stamp types, or report the results of compiling a filter expression on <i>interface</i>. If unspecified and if the <code>-d</code> flag is not given, <i>tcpdump</i> searches the system interface list for the lowest numbered, configured up interface (excluding loopback), which may turn out to be, for example, &#8220;eth0&#8221;.</p>
<dd>On Linux systems with 2.2 or later kernels, an <i>interface</i> argument of &#8220;any&#8221; can be used to capture packets from all interfaces. Note that captures on the &#8220;any&#8221; device will not be done in promiscuous mode.</p>
<dd>If the <code>-D</code> flag is supported, an interface number as printed by that flag can be used as the <i>interface</i> argument, if no interface on the system has that number as a name.</p>
<dt><code>-I</code></p>
<dd>
<dt><code>&#8211;monitor-mode</code></p>
<dd>Put the interface in &quot;monitor mode&quot;; this is supported only on IEEE 802.11 Wi-Fi interfaces, and supported only on some operating systems.</p>
<dd>Note that in monitor mode the adapter might disassociate from the network with which it&#8217;s associated, so that you will not be able to use any wireless networks with that adapter. This could prevent accessing files on a network server, or resolving host names or network addresses, if you are capturing in monitor mode and are not connected to another network with another adapter.</p>
<dd>This flag will affect the output of the <code>-L</code> flag. If <code>-I</code> isn&#8217;t specified, only those link-layer types available when not in monitor mode will be shown; if <code>-I</code> is specified, only those link-layer types available when in monitor mode will be shown.</p>
<dt><code>&#8211;immediate-mode</code></p>
<dd>Capture in &quot;immediate mode&quot;. In this mode, packets are delivered to tcpdump as soon as they arrive, rather than being buffered for efficiency. This is the default when printing packets rather than saving packets to a &#8220;savefile&#8221; if the packets are being printed to a terminal rather than to a file or pipe.</p>
<dt><code>-j</code><i> tstamp_type</i></p>
<dd>
<dt><code>&#8211;time-stamp-type=</code><i>tstamp_type</i></p>
<dd>Set the time stamp type for the capture to <i>tstamp_type</i>. The names to use for the time stamp types are given in <code><a href="/docs/linux/man/7-pcap-tstamp/">pcap-tstamp</a></code>(7); not all the types listed there will necessarily be valid for any given interface.</p>
<dt><code>-J</code></p>
<dd>
<dt><code>&#8211;list-time-stamp-types</code></p>
<dd>List the supported time stamp types for the interface and exit. If the time stamp type cannot be set for the interface, no time stamp types are listed.</p>
<dt><code>&#8211;time-stamp-precision=</code><i>tstamp_precision</i></p>
<dd>When capturing, set the time stamp precision for the capture to <i>tstamp_precision</i>. Note that availability of high precision time stamps (nanoseconds) and their actual accuracy is platform and hardware dependent. Also note that when writing captures made with nanosecond accuracy to a savefile, the time stamps are written with nanosecond resolution, and the file is written with a different magic number, to indicate that the time stamps are in seconds and nanoseconds; not all programs that read pcap savefiles will be able to read those captures.</p>
<dd>When reading a savefile, convert time stamps to the precision specified by <i>timestamp_precision</i>, and display them with that resolution. If the precision specified is less than the precision of time stamps in the file, the conversion will lose precision.</p>
<dd>The supported values for <i>timestamp_precision</i> are <code>micro</code> for microsecond resolution and <code>nano</code> for nanosecond resolution. The default is microsecond resolution.</p>
<dt><code>&#8211;micro</code></p>
<dd>
<dt><code>&#8211;nano</code></p>
<dd>Shorthands for <code>&#8211;time-stamp-precision=micro</code> or <code>&#8211;time-stamp-precision=nano</code>, adjusting the time stamp precision accordingly. When reading packets from a savefile, using <code>&#8211;micro</code> truncates time stamps if the savefile was created with nanosecond precision. In contrast, a savefile created with microsecond precision will have trailing zeroes added to the time stamp when <code>&#8211;nano</code> is used.</p>
<dt><code>-K</code></p>
<dd>
<dt><code>&#8211;dont-verify-checksums</code></p>
<dd>Don&#8217;t attempt to verify IP, TCP, or UDP checksums. This is useful for interfaces that perform some or all of those checksum calculation in hardware; otherwise, all outgoing TCP checksums will be flagged as bad.</p>
<dt><code>-l</code></p>
<dd>Make stdout line buffered. Useful if you want to see the data while capturing it. E.g.,</p>
<dd>
<dl>
<dd>
<dl>
<dd>
<pre><code>tcpdump -l | tee dat</code></pre>
</dl>
</dl>
<dd>or</p>
<dd>
<dl>
<dd>
<dl>
<dd>
<pre><code>tcpdump -l &gt; dat &amp; tail -f dat</code></pre>
</dl>
</dl>
<dd>Note that on Windows,&#8220;line buffered&#8221; means &#8220;unbuffered&#8221;, so that WinDump will write each character individually if <code>-l</code> is specified.</p>
<dd><code>-U</code> is similar to <code>-l</code> in its behavior, but it will cause output to be &#8220;packet-buffered&#8221;, so that the output is written to stdout at the end of each packet rather than at the end of each line; this is buffered on all platforms, including Windows.</p>
<dt><code>-L</code></p>
<dd>
<dt><code>&#8211;list-data-link-types</code></p>
<dd>List the known data link types for the interface, in the specified mode, and exit. The list of known data link types may be dependent on the specified mode; for example, on some platforms, a Wi-Fi interface might support one set of data link types when not in monitor mode (for example, it might support only fake Ethernet headers, or might support 802.11 headers but not support 802.11 headers with radio information) and another set of data link types when in monitor mode (for example, it might support 802.11 headers, or 802.11 headers with radio information, only in monitor mode).</p>
<dt><code>-m</code><i> module</i></p>
<dd>Load SMI MIB module definitions from file <i>module</i>. This option can be used several times to load several MIB modules into <i>tcpdump</i>.</p>
<dt><code>-M</code><i> secret</i></p>
<dd>Use <i>secret</i> as a shared secret for validating the digests found in TCP segments with the TCP-MD5 option (RFC 2385), if present.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t convert addresses (i.e., host addresses, port numbers, etc.) to names.</p>
<dt><code>-N</code></p>
<dd>Don&#8217;t print domain name qualification of host names. E.g., if you give this flag then <i>tcpdump</i> will print &#8220;nic&#8221; instead of &#8220;nic.ddn.mil&#8221;.</p>
<dt><code>-#</code></p>
<dd>
<dt><code>&#8211;number</code></p>
<dd>Print an optional packet number at the beginning of the line.</p>
<dt><code>-O</code></p>
<dd>
<dt><code>&#8211;no-optimize</code></p>
<dd>Do not run the packet-matching code optimizer. This is useful only if you suspect a bug in the optimizer.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;no-promiscuous-mode</code></p>
<dd><i>Don&#8217;t</i> put the interface into promiscuous mode. Note that the interface might be in promiscuous mode for some other reason; hence, `-p&#8217; cannot be used as an abbreviation for `ether host {local-hw-addr} or ether broadcast&#8217;.</p>
<dt><code>&#8211;print</code></p>
<dd>Print parsed packet output, even if the raw packets are being saved to a file with the <code>-w</code> flag.</p>
<dt><code>-Q</code><i> direction</i></p>
<dd>
<dt><code>&#8211;direction=</code><i>direction</i></p>
<dd>Choose send/receive direction <i>direction</i> for which packets should be captured. Possible values are `in&#8217;, `out&#8217; and `inout&#8217;. Not available on all platforms.</p>
<dt><code>-q</code></p>
<dd>Quick (quiet?) output. Print less protocol information so output lines are shorter.</p>
<dt><code>-r</code><i> file</i></p>
<dd>Read packets from <i>file</i> (which was created with the <code>-w</code> option or by other tools that write pcap or pcapng files). Standard input is used if <i>file</i> is &#8220;-&#8221;.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;absolute-tcp-sequence-numbers</code></p>
<dd>Print absolute, rather than relative, TCP sequence numbers.</p>
<dt><code>-s</code><i> snaplen</i></p>
<dd>
<dt><code>&#8211;snapshot-length=</code><i>snaplen</i></p>
<dd>Snarf <i>snaplen</i> bytes of data from each packet rather than the default of 262144 bytes. Packets truncated because of a limited snapshot are indicated in the output with &#8220;[|<i>proto</i>]&#8221;, where <i>proto</i> is the name of the protocol level at which the truncation has occurred.</p>
<dd>Note that taking larger snapshots both increases the amount of time it takes to process packets and, effectively, decreases the amount of packet buffering. This may cause packets to be lost. Note also that taking smaller snapshots will discard data from protocols above the transport layer, which loses information that may be important. NFS and AFS requests and replies, for example, are very large, and much of the detail won&#8217;t be available if a too-short snapshot length is selected.</p>
<dd>If you need to reduce the snapshot size below the default, you should limit <i>snaplen</i> to the smallest number that will capture the protocol information you&#8217;re interested in. Setting <i>snaplen</i> to 0 sets it to the default of 262144, for backwards compatibility with recent older versions of <i>tcpdump</i>.</p>
<dt><code>-T</code><i> type</i></p>
<dd>Force packets selected by &quot;<i>expression</i>&quot; to be interpreted the specified <i>type</i>. Currently known types are <code>aodv</code> (Ad-hoc On-demand Distance Vector protocol), <code>carp</code> (Common Address Redundancy Protocol), <code>cnfp</code> (Cisco NetFlow protocol), <code>domain</code> (Domain Name System), <code>lmp</code> (Link Management Protocol), <code>pgm</code> (Pragmatic General Multicast), <code>pgm_zmtp1</code> (ZMTP/1.0 inside PGM/EPGM), <code>ptp</code> (Precision Time Protocol), <code>radius</code> (RADIUS), <code>resp</code> (REdis Serialization Protocol), <code>rpc</code> (Remote Procedure Call), <code>rtcp</code> (Real-Time Applications control protocol), <code>rtp</code> (Real-Time Applications protocol), <code>snmp</code> (Simple Network Management Protocol), <code>someip</code> (SOME/IP), <code>tftp</code> (Trivial File Transfer Protocol), <code>vat</code> (Visual Audio Tool), <code>vxlan</code> (Virtual eXtensible Local Area Network), <code>wb</code> (distributed White Board) and <code>zmtp1</code> (ZeroMQ Message Transport Protocol 1.0).</p>
<dd>Note that the <code>pgm</code> type above affects UDP interpretation only, the native PGM is always recognised as IP protocol 113 regardless. UDP-encapsulated PGM is often called &quot;EPGM&quot; or &quot;PGM/UDP&quot;.</p>
<dd>Note that the <code>pgm_zmtp1</code> type above affects interpretation of both native PGM and UDP at once. During the native PGM decoding the application data of an ODATA/RDATA packet would be decoded as a ZeroMQ datagram with ZMTP/1.0 frames. During the UDP decoding in addition to that any UDP packet would be treated as an encapsulated PGM packet.</p>
<dt><code>-t</code></p>
<dd><i>Don&#8217;t</i> print a timestamp on each dump line.</p>
<dt><code>-tt</code></p>
<dd>Print the timestamp, as seconds since January 1, 1970, 00:00:00, UTC, and fractions of a second since that time, on each dump line.</p>
<dt><code>-ttt</code></p>
<dd>Print a delta (microsecond or nanosecond resolution depending on the <code>&#8211;time-stamp-precision</code> option) between current and previous line on each dump line. The default is microsecond resolution.</p>
<dt><code>-tttt</code></p>
<dd>Print a timestamp, as hours, minutes, seconds, and fractions of a second since midnight, preceded by the date, on each dump line.</p>
<dt><code>-ttttt</code></p>
<dd>Print a delta (microsecond or nanosecond resolution depending on the <code>&#8211;time-stamp-precision</code> option) between current and first line on each dump line. The default is microsecond resolution.</p>
<dt><code>-u</code></p>
<dd>Print undecoded NFS handles.</p>
<dt><code>-U</code></p>
<dd>
<dt><code>&#8211;packet-buffered</code></p>
<dd>If the <code>-w</code> option is not specified, or if it is specified but the <code>&#8211;print</code> flag is also specified, make the printed packet output &#8220;packet-buffered&#8221;; i.e., as the description of the contents of each packet is printed, it will be written to the standard output, rather than, when not writing to a terminal, being written only when the output buffer fills.</p>
<dd>If the <code>-w</code> option is specified, make the saved raw packet output &#8220;packet-buffered&#8221;; i.e., as each packet is saved, it will be written to the output file, rather than being written only when the output buffer fills.</p>
<dd>The <code>-U</code> flag will not be supported if <i>tcpdump</i> was built with an older version of <i>libpcap</i> that lacks the <code>pcap_dump_flush(3PCAP)</code> function.</p>
<dt><code>-v</code></p>
<dd>When parsing and printing, produce (slightly more) verbose output. For example, the time to live, identification, total length and options in an IP packet are printed. Also enables additional packet integrity checks such as verifying the IP and ICMP header checksum.</p>
<dd>When writing to a file with the <code>-w</code> option and at the same time not reading from a file with the <code>-r</code> option, report to stderr, once per second, the number of packets captured. In Solaris, FreeBSD and possibly other operating systems this periodic update currently can cause loss of captured packets on their way from the kernel to tcpdump.</p>
<dt><code>-vv</code></p>
<dd>Even more verbose output. For example, additional fields are printed from NFS reply packets, and SMB packets are fully decoded.</p>
<dt><code>-vvv</code></p>
<dd>Even more verbose output. For example, telnet <code>SB</code> &#8230; <code>SE</code> options are printed in full. With <code>-X</code> Telnet options are printed in hex as well.</p>
<dt><code>-V</code><i> file</i></p>
<dd>Read a list of filenames from <i>file</i>. Standard input is used if <i>file</i> is &#8220;-&#8221;.</p>
<dt><code>-w</code><i> file</i></p>
<dd>Write the raw packets to <i>file</i> rather than parsing and printing them out. They can later be printed with the -r option. Standard output is used if <i>file</i> is &#8220;-&#8221;.</p>
<dd>This output will be buffered if written to a file or pipe, so a program reading from the file or pipe may not see packets for an arbitrary amount of time after they are received. Use the <code>-U</code> flag to cause packets to be written as soon as they are received.</p>
<dd>The MIME type <i>application/vnd.tcpdump.pcap</i> has been registered with IANA for <i>pcap</i> files. The filename extension <i>.pcap</i> appears to be the most commonly used along with <i>.cap</i> and <i>.dmp</i>. <i>Tcpdump</i> itself doesn&#8217;t check the extension when reading capture files and doesn&#8217;t add an extension when writing them (it uses magic numbers in the file header instead). However, many operating systems and applications will use the extension if it is present and adding one (e.g. .pcap) is recommended.</p>
<dd>See <code><a href="/docs/linux/man/5-pcap-savefile/">pcap-savefile</a></code>(5) for a description of the file format.</p>
<dt><code>-W</code><i> filecount</i></p>
<dd>Used in conjunction with the <code>-C</code> option, this will limit the number of files created to the specified number, and begin overwriting files from the beginning, thus creating a &#8216;rotating&#8217; buffer. In addition, it will name the files with enough leading 0s to support the maximum number of files, allowing them to sort correctly.</p>
<dd>Used in conjunction with the <code>-G</code> option, this will limit the number of rotated dump files that get created, exiting with status 0 when reaching the limit.</p>
<dd>If used in conjunction with both <code>-C</code> and <code>-G,</code> the <code>-W</code> option will currently be ignored, and will only affect the file name.</p>
<dt><code>-x</code></p>
<dd>When parsing and printing, in addition to printing the headers of each packet, print the data of each packet (minus its link level header) in hex. The smaller of the entire packet or <i>snaplen</i> bytes will be printed. Note that this is the entire link-layer packet, so for link layers that pad (e.g. Ethernet), the padding bytes will also be printed when the higher layer packet is shorter than the required padding. In the current implementation this flag may have the same effect as <code>-xx</code> if the packet is truncated.</p>
<dt><code>-xx</code></p>
<dd>When parsing and printing, in addition to printing the headers of each packet, print the data of each packet, <i>including</i> its link level header, in hex.</p>
<dt><code>-X</code></p>
<dd>When parsing and printing, in addition to printing the headers of each packet, print the data of each packet (minus its link level header) in hex and ASCII. This is very handy for analysing new protocols. In the current implementation this flag may have the same effect as <code>-XX</code> if the packet is truncated.</p>
<dt><code>-XX</code></p>
<dd>When parsing and printing, in addition to printing the headers of each packet, print the data of each packet, <i>including</i> its link level header, in hex and ASCII.</p>
<dt><code>-y</code><i> datalinktype</i></p>
<dd>
<dt><code>&#8211;linktype=</code><i>datalinktype</i></p>
<dd>Set the data link type to use while capturing packets (see <code>-L</code>) or just compiling and dumping packet-matching code (see <code>-d</code>) to <i>datalinktype</i>.</p>
<dt><code>-z</code><i> postrotate-command</i></p>
<dd>Used in conjunction with the <code>-C</code> or <code>-G</code> options, this will make <i>tcpdump</i> run &quot; <i>postrotate-command file</i> &quot; where <i>file</i> is the savefile being closed after each rotation. For example, specifying <code>-z gzip</code> or <code>-z bzip2</code> will compress each savefile using gzip or bzip2.</p>
<dd>Note that tcpdump will run the command in parallel to the capture, using the lowest priority so that this doesn&#8217;t disturb the capture process.</p>
<dd>And in case you would like to use a command that itself takes flags or different arguments, you can always write a shell script that will take the savefile name as the only argument, make the flags &amp; arguments arrangements and execute the command that you want.</p>
<dt><code>-Z</code><i> user</i></p>
<dd>
<dt><code>&#8211;relinquish-privileges=</code><i>user</i></p>
<dd>If <i>tcpdump</i> is running as root, after opening the capture device or input savefile, change the user ID to <i>user</i> and the group ID to the primary group of <i>user</i>.</p>
<dd>This behavior is enabled by default (<code>-Z tcpdump</code>), and can be disabled by <code>-Z root</code>. </p>
<dt><i> expression</i></p>
<dd>
<dl>
<dd>selects which packets will be dumped. If no <i>expression</i> is given, all packets on the net will be dumped. Otherwise, only packets for which <i>expression</i> is `true&#8217; will be dumped. </p>
<p> For the <i>expression</i> syntax, see <code><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></code>(7). </p>
<p> The <i>expression</i> argument can be passed to <i>tcpdump</i> as either a single Shell argument, or as multiple Shell arguments, whichever is more convenient. Generally, if the expression contains Shell metacharacters, such as backslashes used to escape protocol names, it is easier to pass it as a single, quoted argument rather than to escape the Shell metacharacters. Multiple arguments are concatenated with spaces before being parsed.</dl>
</dl>
<h2>Examples</h2>
<p>To print all packets arriving at or departing from <i>sundown</i>:</p>
<dl>
<dd>
<pre><code>tcpdump host sundown</code></pre>
</dl>
<p> To print traffic between <i>helios</i> and either <i>hot</i> or <i>ace</i>:</p>
<dl>
<dd>
<pre><code>tcpdump host helios and \( hot or ace \)</code></pre>
</dl>
<p> To print all IP packets between <i>ace</i> and any host except <i>helios</i>:</p>
<dl>
<dd>
<pre><code>tcpdump ip host ace and not helios</code></pre>
</dl>
<p> To print all traffic between local hosts and hosts at Berkeley:</p>
<dl>
<dd>
<pre><code>tcpdump net ucb-ether</code></pre>
</dl>
<p> To print all ftp traffic through internet gateway <i>snup</i>: (note that the expression is quoted to prevent the shell from (mis-)interpreting the parentheses):</p>
<dl>
<dd>
<pre><code>tcpdump 'gateway snup and (port ftp or ftp-data)'</code></pre>
</dl>
<p> To print traffic neither sourced from nor destined for local hosts (if you gateway to one other net, this stuff should never make it onto your local net).</p>
<dl>
<dd>
<pre><code>tcpdump ip and not net </code><i>localnet</i></pre>
</dl>
<p> To print the start and end packets (the SYN and FIN packets) of each TCP conversation that involves a non-local host.</p>
<dl>
<dd>
<pre><code>tcpdump 'tcp[tcpflags] &amp; (tcp-syn|tcp-fin) != 0 and not src and dst net </code><i>localnet</i>'</pre>
</dl>
<p> To print the TCP packets with flags RST and ACK both set. (i.e. select only the RST and ACK flags in the flags field, and if the result is &quot;RST and ACK both set&quot;, match)</p>
<dl>
<dd>
<pre><code>tcpdump 'tcp[tcpflags] &amp; (tcp-rst|tcp-ack) == (tcp-rst|tcp-ack)'</code></pre>
</dl>
<p> To print all IPv4 HTTP packets to and from port 80, i.e. print only packets that contain data, not, for example, SYN and FIN packets and ACK-only packets. (IPv6 is left as an exercise for the reader.)</p>
<dl>
<dd>
<pre><code>tcpdump 'tcp port 80 and (((ip[2:2] - ((ip[0]&amp;0xf)&lt;&lt;2)) - ((tcp[12]&amp;0xf0)&gt;&gt;2)) != 0)'</code></pre>
</dl>
<p> To print IP packets longer than 576 bytes sent through gateway <i>snup</i>:</p>
<dl>
<dd>
<pre><code>tcpdump 'gateway snup and ip[2:2] &gt; 576'</code></pre>
</dl>
<p> To print IP broadcast or multicast packets that were <i>not</i> sent via Ethernet broadcast or multicast:</p>
<dl>
<dd>
<pre><code>tcpdump 'ether[0] &amp; 1 = 0 and ip[16] &gt;= 224'</code></pre>
</dl>
<p> To print all ICMP packets that are not echo requests/replies (i.e., not ping packets):</p>
<dl>
<dd>
<pre><code>tcpdump 'icmp[icmptype] != icmp-echo and icmp[icmptype] != icmp-echoreply'</code></pre>
</dl>
<h2>Output Format</h2>
<p>The output of <i>tcpdump</i> is protocol dependent. The following gives a brief description and examples of most of the formats. </p>
<p> Timestamps </p>
<p> By default, all output lines are preceded by a timestamp. The timestamp is the current clock time in the form</p>
<dl>
<dd>
<pre><i>hh:mm:ss.frac</i></pre>
</dl>
<p> and is as accurate as the kernel&#8217;s clock. The timestamp reflects the time the kernel applied a time stamp to the packet. No attempt is made to account for the time lag between when the network interface finished receiving the packet from the network and when the kernel applied a time stamp to the packet; that time lag could include a delay between the time when the network interface finished receiving a packet from the network and the time when an interrupt was delivered to the kernel to get it to read the packet and a delay between the time when the kernel serviced the `new packet&#8217; interrupt and the time when it applied a time stamp to the packet. </p>
<p> Link Level Headers </p>
<p> If the &#8216;-e&#8217; option is given, the link level header is printed out. On Ethernets, the source and destination addresses, protocol, and packet length are printed. </p>
<p> On FDDI networks, the &#8216;-e&#8217; option causes <i>tcpdump</i> to print the `frame control&#8217; field, the source and destination addresses, and the packet length. (The `frame control&#8217; field governs the interpretation of the rest of the packet. Normal packets (such as those containing IP datagrams) are `async&#8217; packets, with a priority value between 0 and 7; for example, `<code>async4</code>&#8216;. Such packets are assumed to contain an 802.2 Logical Link Control (LLC) packet; the LLC header is printed if it is <i>not</i> an ISO datagram or a so-called SNAP packet. </p>
<p> On Token Ring networks, the &#8216;-e&#8217; option causes <i>tcpdump</i> to print the `access control&#8217; and `frame control&#8217; fields, the source and destination addresses, and the packet length. As on FDDI networks, packets are assumed to contain an LLC packet. Regardless of whether the &#8216;-e&#8217; option is specified or not, the source routing information is printed for source-routed packets. </p>
<p> On 802.11 networks, the &#8216;-e&#8217; option causes <i>tcpdump</i> to print the `frame control&#8217; fields, all of the addresses in the 802.11 header, and the packet length. As on FDDI networks, packets are assumed to contain an LLC packet. </p>
<p> <i>(N.B.: The following description assumes familiarity with the SLIP compression algorithm described in RFC-1144.)</i> </p>
<p> On SLIP links, a direction indicator (&#8220;I&#8221; for inbound, &#8220;O&#8221; for outbound), packet type, and compression information are printed out. The packet type is printed first. The three types are <i>ip</i>, <i>utcp</i>, and <i>ctcp</i>. No further link information is printed for <i>ip</i> packets. For TCP packets, the connection identifier is printed following the type. If the packet is compressed, its encoded header is printed out. The special cases are printed out as <code>*S+</code><i>n</i> and <code>*SA+</code><i>n</i>, where <i>n</i> is the amount by which the sequence number (or sequence number and ack) has changed. If it is not a special case, zero or more changes are printed. A change is indicated by U (urgent pointer), W (window), A (ack), S (sequence number), and I (packet ID), followed by a delta (+n or -n), or a new value (=n). Finally, the amount of data in the packet and compressed header length are printed. </p>
<p> For example, the following line shows an outbound compressed TCP packet, with an implicit connection identifier; the ack has changed by 6, the sequence number by 49, and the packet ID by 6; there are 3 bytes of data and 6 bytes of compressed header:</p>
<dl>
<dd>
<pre><code>O ctcp * A+6 S+49 I+6 3 (6)</code></pre>
</dl>
<p> ARP/RARP Packets </p>
<p> ARP/RARP output shows the type of request and its arguments. The format is intended to be self explanatory. Here is a short sample taken from the start of an `rlogin&#8217; from host <i>rtsg</i> to host <i>csam</i>:</p>
<dl>
<dd>
<pre><tt>arp who-has csam tell rtsg
arp reply csam is-at CSAM</tt></pre>
</dl>
<p> The first line says that rtsg sent an ARP packet asking for the Ethernet address of internet host csam. Csam replies with its Ethernet address (in this example, Ethernet addresses are in caps and internet addresses in lower case). </p>
<p> This would look less redundant if we had done <i>tcpdump -n</i>:</p>
<dl>
<dd>
<pre><tt>arp who-has 128.3.254.6 tell 128.3.254.68
arp reply 128.3.254.6 is-at 02:07:01:00:01:c4</tt></pre>
</dl>
<p> If we had done <i>tcpdump -e</i>, the fact that the first packet is broadcast and the second is point-to-point would be visible:</p>
<dl>
<dd>
<pre><tt>RTSG Broadcast 0806 64: arp who-has csam tell rtsg
CSAM RTSG 0806 64: arp reply csam is-at CSAM</tt></pre>
</dl>
<p> For the first packet this says the Ethernet source address is RTSG, the destination is the Ethernet broadcast address, the type field contained hex 0806 (type ETHER_ARP) and the total length was 64 bytes. </p>
<p> IPv4 Packets </p>
<p> If the link-layer header is not being printed, for IPv4 packets, <code>IP</code> is printed after the time stamp. </p>
<p> If the <code>-v</code> flag is specified, information from the IPv4 header is shown in parentheses after the <code>IP</code> or the link-layer header. The general format of this information is:</p>
<dl>
<dd>
<pre>tos <i>tos</i>, ttl <i>ttl</i>, id <i>id</i>, offset <i>offset</i>, flags [<i>flags</i>], proto <i>proto</i>, length <i>length</i>, options (<i>options</i>)</pre>
</dl>
<p> <i>tos</i> is the type of service field; if the ECN bits are non-zero, those are reported as <code><a href="/docs/linux/man/1-ect/">ECT</a>(1)</code>, <code>ECT(0)</code>, or <code>CE</code>. <i>ttl</i> is the time-to-live; it is not reported if it is zero. <i>id</i> is the IP identification field. <i>offset</i> is the fragment offset field; it is printed whether this is part of a fragmented datagram or not. <i>flags</i> are the MF and DF flags; <code>+</code> is reported if MF is set, and <code>DF</code> is reported if F is set. If neither are set, <code>.</code> is reported. <i>proto</i> is the protocol ID field. <i>length</i> is the total length field. <i>options</i> are the IP options, if any. </p>
<p> Next, for TCP and UDP packets, the source and destination IP addresses and TCP or UDP ports, with a dot between each IP address and its corresponding port, will be printed, with a &gt; separating the source and destination. For other protocols, the addresses will be printed, with a &gt; separating the source and destination. Higher level protocol information, if any, will be printed after that. </p>
<p> For fragmented IP datagrams, the first fragment contains the higher level protocol header; fragments after the first contain no higher level protocol header. Fragmentation information will be printed only with the <code>-v</code> flag, in the IP header information, as described above. </p>
<p> TCP Packets </p>
<p> <i>(N.B.:The following description assumes familiarity with the TCP protocol described in RFC-793. If you are not familiar with the protocol, this description will not be of much use to you.)</i> </p>
<p> The general format of a TCP protocol line is:</p>
<dl>
<dd>
<pre><i>src</i> &gt; <i>dst</i>: Flags [<i>tcpflags</i>], seq <i>data-seqno</i>, ack <i>ackno</i>, win <i>window</i>, urg <i>urgent</i>, options [<i>opts</i>], length <i>len</i></pre>
</dl>
<p> <i>Src</i> and <i>dst</i> are the source and destination IP addresses and ports. <i>Tcpflags</i> are some combination of S (SYN), F (FIN), P (PUSH), R (RST), U (URG), W (ECN CWR), E (ECN-Echo) or `.&#8217; (ACK), or `none&#8217; if no flags are set. <i>Data-seqno</i> describes the portion of sequence space covered by the data in this packet (see example below). <i>Ackno</i> is sequence number of the next data expected the other direction on this connection. <i>Window</i> is the number of bytes of receive buffer space available the other direction on this connection. <i>Urg</i> indicates there is `urgent&#8217; data in the packet. <i>Opts</i> are TCP options (e.g., mss 1024). <i>Len</i> is the length of payload data. </p>
<p> <i>Iptype</i>, <i>Src</i>, <i>dst</i>, and <i>flags</i> are always present. The other fields depend on the contents of the packet&#8217;s TCP protocol header and are output only if appropriate. </p>
<p> Here is the opening portion of an rlogin from host <i>rtsg</i> to host <i>csam</i>.</p>
<dl>
<dd>
<pre><tt>IP rtsg.1023 &gt; csam.login: Flags [S], seq 768512:768512, win 4096, opts [mss 1024]
IP csam.login &gt; rtsg.1023: Flags [S.], seq, 947648:947648, ack 768513, win 4096, opts [mss 1024]
IP rtsg.1023 &gt; csam.login: Flags [.], ack 1, win 4096
IP rtsg.1023 &gt; csam.login: Flags [P.], seq 1:2, ack 1, win 4096, length 1
IP csam.login &gt; rtsg.1023: Flags [.], ack 2, win 4096
IP rtsg.1023 &gt; csam.login: Flags [P.], seq 2:21, ack 1, win 4096, length 19
IP csam.login &gt; rtsg.1023: Flags [P.], seq 1:2, ack 21, win 4077, length 1
IP csam.login &gt; rtsg.1023: Flags [P.], seq 2:3, ack 21, win 4077, urg 1, length 1
IP csam.login &gt; rtsg.1023: Flags [P.], seq 3:4, ack 21, win 4077, urg 1, length 1</tt></pre>
</dl>
<p> The first line says that TCP port 1023 on rtsg sent a packet to port <i>login</i> on csam. The <code>S</code> indicates that the <i>SYN</i> flag was set. The packet sequence number was 768512 and it contained no data. (The notation is `first:last&#8217; which means `sequence numbers <i>first</i> up to but not including <i>last</i>&#8216;.) There was no piggy-backed ACK, the available receive window was 4096 bytes and there was a max-segment-size option requesting an MSS of 1024 bytes. </p>
<p> Csam replies with a similar packet except it includes a piggy-backed ACK for rtsg&#8217;s SYN. Rtsg then ACKs csam&#8217;s SYN. The `.&#8217; means the ACK flag was set. The packet contained no data so there is no data sequence number or length. Note that the ACK sequence number is a small integer (1). The first time <i>tcpdump</i> sees a TCP `conversation&#8217;, it prints the sequence number from the packet. On subsequent packets of the conversation, the difference between the current packet&#8217;s sequence number and this initial sequence number is printed. This means that sequence numbers after the first can be interpreted as relative byte positions in the conversation&#8217;s data stream (with the first data byte each direction being `1&#8242;). `-S&#8217; will override this feature, causing the original sequence numbers to be output. </p>
<p> On the 6th line, rtsg sends csam 19 bytes of data (bytes 2 through 20 in the rtsg &rarr; csam side of the conversation). The PUSH flag is set in the packet. On the 7th line, csam says it&#8217;s received data sent by rtsg up to but not including byte 21. Most of this data is apparently sitting in the socket buffer since csam&#8217;s receive window has gotten 19 bytes smaller. Csam also sends one byte of data to rtsg in this packet. On the 8th and 9th lines, csam sends two bytes of urgent, pushed data to rtsg. </p>
<p> If the snapshot was small enough that <i>tcpdump</i> didn&#8217;t capture the full TCP header, it interprets as much of the header as it can and then reports &#8220;[|<i>tcp</i>]&#8221; to indicate the remainder could not be interpreted. If the header contains a bogus option (one with a length that&#8217;s either too small or beyond the end of the header), <i>tcpdump</i> reports it as &#8220;[<i>bad opt</i>]&#8221; and does not interpret any further options (since it&#8217;s impossible to tell where they start). If the header length indicates options are present but the IP datagram length is not long enough for the options to actually be there, <i>tcpdump</i> reports it as &#8220;[<i>bad hdr length</i>]&#8221;. </p>
<p> <code>Capturing TCP packets with particular flag combinations (SYN-ACK, URG-ACK, etc.)</code> </p>
<p> There are 8 bits in the control bits section of the TCP header:</p>
<dl>
<dd><i>CWR | ECE | URG | ACK | PSH | RST | SYN | FIN</i></dl>
<p> Let&#8217;s assume that we want to watch packets used in establishing a TCP connection. Recall that TCP uses a 3-way handshake protocol when it initializes a new connection; the connection sequence with regard to the TCP control bits is </p>
<dl>
<dd>1) Caller sends SYN</dl>
<dl>
<dd>2) Recipient responds with SYN, ACK</dl>
<dl>
<dd>3) Caller sends ACK</dl>
<p> Now we&#8217;re interested in capturing packets that have only the SYN bit set (Step 1). Note that we don&#8217;t want packets from step 2 (SYN-ACK), just a plain initial SYN. What we need is a correct filter expression for <i>tcpdump</i>. </p>
<p> Recall the structure of a TCP header without options: </p>
<pre> 0 15 31
-----------------------------------------------------------------
| source port | destination port |
-----------------------------------------------------------------
| sequence number |
-----------------------------------------------------------------
| acknowledgment number |
-----------------------------------------------------------------
| HL | rsvd |C|E|U|A|P|R|S|F| window size |
-----------------------------------------------------------------
| TCP checksum | urgent pointer |
-----------------------------------------------------------------</pre>
<p>A TCP header usually holds 20 octets of data, unless options are present. The first line of the graph contains octets 0 &#8211; 3, the second line shows octets 4 &#8211; 7 etc. </p>
<p> Starting to count with 0, the relevant TCP control bits are contained in octet 13: </p>
<pre> 0 7| 15| 23| 31
----------------|---------------|---------------|----------------
| HL | rsvd |C|E|U|A|P|R|S|F| window size |
----------------|---------------|---------------|----------------
| | 13th octet | | |</pre>
<p>Let&#8217;s have a closer look at octet no. 13: </p>
<pre> | |
 |---------------|
 |C|E|U|A|P|R|S|F|
 |---------------|
 |7 5 3 0|</pre>
<p>These are the TCP control bits we are interested in. We have numbered the bits in this octet from 0 to 7, right to left, so the PSH bit is bit number 3, while the URG bit is number 5. </p>
<p> Recall that we want to capture packets with only SYN set. Let&#8217;s see what happens to octet 13 if a TCP datagram arrives with the SYN bit set in its header: </p>
<pre> |C|E|U|A|P|R|S|F|
 |---------------|
 |0 0 0 0 0 0 1 0|
 |---------------|
 |7 6 5 4 3 2 1 0|</pre>
<p>Looking at the control bits section we see that only bit number 1 (SYN) is set. </p>
<p> Assuming that octet number 13 is an 8-bit unsigned integer in network byte order, the binary value of this octet is</p>
<dl>
<dd>00000010</dl>
<p> and its decimal representation is </p>
<pre> 7 6 5 4 3 2 1 0
0*2 + 0*2 + 0*2 + 0*2 + 0*2 + 0*2 + 1*2 + 0*2 = 2</pre>
<p>We&#8217;re almost done, because now we know that if only SYN is set, the value of the 13th octet in the TCP header, when interpreted as a 8-bit unsigned integer in network byte order, must be exactly 2. </p>
<p> This relationship can be expressed as</p>
<dl>
<dd><code>tcp[13] == 2</code></dl>
<p> We can use this expression as the filter for <i>tcpdump</i> in order to watch packets which have only SYN set:</p>
<dl>
<dd><code>tcpdump -i xl0 tcp[13] == 2</code></dl>
<p> The expression says &quot;let the 13th octet of a TCP datagram have the decimal value 2&quot;, which is exactly what we want. </p>
<p> Now, let&#8217;s assume that we need to capture SYN packets, but we don&#8217;t care if ACK or any other TCP control bit is set at the same time. Let&#8217;s see what happens to octet 13 when a TCP datagram with SYN-ACK set arrives: </p>
<pre> |C|E|U|A|P|R|S|F|
 |---------------|
 |0 0 0 1 0 0 1 0|
 |---------------|
 |7 6 5 4 3 2 1 0|</pre>
<p>Now bits 1 and 4 are set in the 13th octet. The binary value of octet 13 is</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;00010010</dl>
<p> which translates to decimal </p>
<pre> 7 6 5 4 3 2 1 0
0*2 + 0*2 + 0*2 + 1*2 + 0*2 + 0*2 + 1*2 + 0*2 = 18</pre>
<p>Now we can&#8217;t just use &#8216;tcp[13] == 18&#8217; in the <i>tcpdump</i> filter expression, because that would select only those packets that have SYN-ACK set, but not those with only SYN set. Remember that we don&#8217;t care if ACK or any other control bit is set as long as SYN is set. </p>
<p> In order to achieve our goal, we need to logically AND the binary value of octet 13 with some other value to preserve the SYN bit. We know that we want SYN to be set in any case, so we&#8217;ll logically AND the value in the 13th octet with the binary value of a SYN: </p>
<pre> 00010010 SYN-ACK 00000010 SYN
 AND 00000010 (we want SYN) AND 00000010 (we want SYN)
 -------- --------
 = 00000010 = 00000010</pre>
<p>We see that this AND operation delivers the same result regardless whether ACK or another TCP control bit is set. The decimal representation of the AND value as well as the result of this operation is 2 (binary 00000010), so we know that for packets with SYN set the following relation must hold true:</p>
<dl>
<dd>( ( value of octet 13 ) AND ( 2 ) ) == ( 2 )</dl>
<p> This points us to the <i>tcpdump</i> filter expression</p>
<dl>
<dd><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tcpdump -i xl0&nbsp;&#8216;tcp[13]&nbsp;&amp;&nbsp;2&nbsp;==&nbsp;2&#8217;</code></dl>
<p> Some offsets and field values may be expressed as names rather than as numeric values. For example tcp[13] may be replaced with tcp[tcpflags]. The following TCP flag field values are also available: tcp-fin, tcp-syn, tcp-rst, tcp-push, tcp-ack, tcp-urg. </p>
<p> This can be demonstrated as:</p>
<dl>
<dd><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tcpdump -i xl0&nbsp;&#8216;tcp[tcpflags]&nbsp;&amp;&nbsp;tcp-push&nbsp;!=&nbsp;0&#8217;</code></dl>
<p> Note that you should use single quotes or a backslash in the expression to hide the AND (&#8216;&amp;&#8217;) special character from the shell. </p>
<p> <code>UDP Packets</code> </p>
<p> UDP format is illustrated by this rwho packet:</p>
<dl>
<dd>
<pre><tt>actinide.who &gt; broadcast.who: udp 84</tt></pre>
</dl>
<p> This says that port <i>who</i> on host <i>actinide</i> sent a UDP datagram to port <i>who</i> on host <i>broadcast</i>, the Internet broadcast address. The packet contained 84 bytes of user data. </p>
<p> Some UDP services are recognized (from the source or destination port number) and the higher level protocol information printed. In particular, Domain Name service requests (RFC-1034/1035) and Sun RPC calls (RFC-1050) to NFS. </p>
<p> TCP or UDP Name Server Requests </p>
<p> <i>(N.B.:The following description assumes familiarity with the Domain Service protocol described in RFC-1035. If you are not familiar with the protocol, the following description will appear to be written in Greek.)</i> </p>
<p> Name server requests are formatted as</p>
<dl>
<dd>
<pre><i>src &gt; dst: id op? flags qtype qclass name (len)</i>
<tt>h2opolo.1538 &gt; helios.domain: 3+ A? ucbvax.berkeley.edu. (37)</tt></pre>
</dl>
<p> Host <i>h2opolo</i> asked the domain server on <i>helios</i> for an address record (qtype=A) associated with the name <i>ucbvax.berkeley.edu.</i> The query id was `3&#8242;. The `+&#8217; indicates the <i>recursion desired</i> flag was set. The query length was 37 bytes, excluding the TCP or UDP and IP protocol headers. The query operation was the normal one, <i>Query</i>, so the op field was omitted. If the op had been anything else, it would have been printed between the `3&#8242; and the `+&#8217;. Similarly, the qclass was the normal one, <i>C_IN</i>, and omitted. Any other qclass would have been printed immediately after the `A&#8217;. </p>
<p> A few anomalies are checked and may result in extra fields enclosed in square brackets: If a query contains an answer, authority records or additional records section, <i>ancount</i>, <i>nscount</i>, or <i>arcount</i> are printed as `[<i>n</i>a]&#8217;, `[<i>n</i>n]&#8217; or `[<i>n</i>au]&#8217; where <i>n</i> is the appropriate count. If any of the response bits are set (AA, RA or rcode) or any of the `must be zero&#8217; bits are set in bytes two and three, `[b2&amp;3=<i>x</i>]&#8217; is printed, where <i>x</i> is the hex value of header bytes two and three. </p>
<p> TCP or UDP Name Server Responses </p>
<p> Name server responses are formatted as</p>
<dl>
<dd>
<pre><i>src &gt; dst: id op rcode flags a/n/au type class data (len)</i>
<tt>helios.domain &gt; h2opolo.1538: 3 3/3/7 A 128.32.137.3 (273)
helios.domain &gt; h2opolo.1537: 2 NXDomain* 0/1/0 (97)</tt></pre>
</dl>
<p> In the first example, <i>helios</i> responds to query id 3 from <i>h2opolo</i> with 3 answer records, 3 name server records and 7 additional records. The first answer record is type A (address) and its data is internet address 128.32.137.3. The total size of the response was 273 bytes, excluding TCP or UDP and IP headers. The op (Query) and response code (NoError) were omitted, as was the class (C_IN) of the A record. </p>
<p> In the second example, <i>helios</i> responds to query 2 with a response code of non-existent domain (NXDomain) with no answers, one name server and no authority records. The `*&#8217; indicates that the <i>authoritative answer</i> bit was set. Since there were no answers, no type, class or data were printed. </p>
<p> Other flag characters that might appear are `-&#8216; (recursion available, RA, <i>not</i> set) and `|&#8217; (truncated message, TC, set). If the `question&#8217; section doesn&#8217;t contain exactly one entry, `[<i>n</i>q]&#8217; is printed. </p>
<p> SMB/CIFS decoding </p>
<p> <i>tcpdump</i> now includes fairly extensive SMB/CIFS/NBT decoding for data on UDP/137, UDP/138 and TCP/139. Some primitive decoding of IPX and NetBEUI SMB data is also done. </p>
<p> By default a fairly minimal decode is done, with a much more detailed decode done if -v is used. Be warned that with -v a single SMB packet may take up a page or more, so only use -v if you really want all the gory details. </p>
<p> For information on SMB packet formats and what all the fields mean see <a rel="nofollow" href="https://download.samba.org/pub/samba/specs/">https://download.samba.org/pub/samba/specs/</a> and other online resources. The SMB patches were written by Andrew Tridgell (tridge [at] samba.org). </p>
<p> NFS Requests and Replies </p>
<p> Sun NFS (Network File System) requests and replies are printed as:</p>
<dl>
<dd>
<pre><i>src.sport &gt; dst.nfs: NFS request xid xid len op args</i>
<i>src.nfs &gt; dst.dport: NFS reply xid xid reply stat len op results</i>
<tt>
sushi.1023 &gt; wrl.nfs: NFS request xid 26377
 112 readlink fh 21,24/10.73165
wrl.nfs &gt; sushi.1023: NFS reply xid 26377
 reply ok 40 readlink &quot;../var&quot;
sushi.1022 &gt; wrl.nfs: NFS request xid 8219
 144 lookup fh 9,74/4096.6878 &quot;xcolors&quot;
wrl.nfs &gt; sushi.1022: NFS reply xid 8219
 reply ok 128 lookup fh 9,74/4134.3150
</tt></pre>
</dl>
<p> In the first line, host <i>sushi</i> sends a transaction with id <i>26377</i> to <i>wrl</i>. The request was 112 bytes, excluding the UDP and IP headers. The operation was a <i>readlink</i> (read symbolic link) on file handle (<i>fh</i>) 21,24/10.731657119. (If one is lucky, as in this case, the file handle can be interpreted as a major,minor device number pair, followed by the inode number and generation number.) In the second line, <i>wrl</i> replies `ok&#8217; with the same transaction id and the contents of the link. </p>
<p> In the third line, <i>sushi</i> asks (using a new transaction id) <i>wrl</i> to lookup the name `<i>xcolors</i>&#8216; in directory file 9,74/4096.6878. In the fourth line, <i>wrl</i> sends a reply with the respective transaction id. </p>
<p> Note that the data printed depends on the operation type. The format is intended to be self explanatory if read in conjunction with an NFS protocol spec. Also note that older versions of tcpdump printed NFS packets in a slightly different format: the transaction id (xid) would be printed instead of the non-NFS port number of the packet. </p>
<p> If the -v (verbose) flag is given, additional information is printed. For example:</p>
<dl>
<dd>
<pre><tt>
sushi.1023 &gt; wrl.nfs: NFS request xid 79658
 148 read fh 21,11/12.195 8192 bytes @ 24576
wrl.nfs &gt; sushi.1023: NFS reply xid 79658
 reply ok 1472 read REG 100664 ids 417/0 sz 29388
</tt></pre>
</dl>
<p> (-v also prints the IP header TTL, ID, length, and fragmentation fields, which have been omitted from this example.) In the first line, <i>sushi</i> asks <i>wrl</i> to read 8192 bytes from file 21,11/12.195, at byte offset 24576. <i>Wrl</i> replies `ok&#8217;; the packet shown on the second line is the first fragment of the reply, and hence is only 1472 bytes long (the other bytes will follow in subsequent fragments, but these fragments do not have NFS or even UDP headers and so might not be printed, depending on the filter expression used). Because the -v flag is given, some of the file attributes (which are returned in addition to the file data) are printed: the file type (&#8220;REG&#8221;, for regular file), the file mode (in octal), the UID and GID, and the file size. </p>
<p> If the -v flag is given more than once, even more details are printed. </p>
<p> NFS reply packets do not explicitly identify the RPC operation. Instead, <i>tcpdump</i> keeps track of &#8220;recent&#8221; requests, and matches them to the replies using the transaction ID. If a reply does not closely follow the corresponding request, it might not be parsable. </p>
<p> AFS Requests and Replies </p>
<p> Transarc AFS (Andrew File System) requests and replies are printed as: </p>
<dl>
<dd>
<pre><i>src.sport &gt; dst.dport: rx packet-type</i>
<i>src.sport &gt; dst.dport: rx packet-type service call call-name args</i>
<i>src.sport &gt; dst.dport: rx packet-type service reply call-name args</i>
<tt>
elvis.7001 &gt; pike.afsfs:
 rx data fs call rename old fid 536876964/1/1 &quot;.newsrc.new&quot;
 new fid 536876964/1/1 &quot;.newsrc&quot;
pike.afsfs &gt; elvis.7001: rx data fs reply rename
</tt></pre>
</dl>
<p> In the first line, host elvis sends a RX packet to pike. This was a RX data packet to the fs (fileserver) service, and is the start of an RPC call. The RPC call was a rename, with the old directory file id of 536876964/1/1 and an old filename of `.newsrc.new&#8217;, and a new directory file id of 536876964/1/1 and a new filename of `.newsrc&#8217;. The host pike responds with a RPC reply to the rename call (which was successful, because it was a data packet and not an abort packet). </p>
<p> In general, all AFS RPCs are decoded at least by RPC call name. Most AFS RPCs have at least some of the arguments decoded (generally only the `interesting&#8217; arguments, for some definition of interesting). </p>
<p> The format is intended to be self-describing, but it will probably not be useful to people who are not familiar with the workings of AFS and RX. </p>
<p> If the -v (verbose) flag is given twice, acknowledgement packets and additional header information is printed, such as the RX call ID, call number, sequence number, serial number, and the RX packet flags. </p>
<p> If the -v flag is given twice, additional information is printed, such as the RX call ID, serial number, and the RX packet flags. The MTU negotiation information is also printed from RX ack packets. </p>
<p> If the -v flag is given three times, the security index and service id are printed. </p>
<p> Error codes are printed for abort packets, with the exception of Ubik beacon packets (because abort packets are used to signify a yes vote for the Ubik protocol). </p>
<p> AFS reply packets do not explicitly identify the RPC operation. Instead, <i>tcpdump</i> keeps track of &#8220;recent&#8221; requests, and matches them to the replies using the call number and service ID. If a reply does not closely follow the corresponding request, it might not be parsable. </p>
<p> KIP AppleTalk (DDP in UDP) </p>
<p> AppleTalk DDP packets encapsulated in UDP datagrams are de-encapsulated and dumped as DDP packets (i.e., all the UDP header information is discarded). The file <i>/etc/atalk.names</i> is used to translate AppleTalk net and node numbers to names. Lines in this file have the form</p>
<dl>
<dd>
<pre><i>number name</i>
<tt>1.254 ether
16.1 icsd-net
1.254.110 ace</tt></pre>
</dl>
<p> The first two lines give the names of AppleTalk networks. The third line gives the name of a particular host (a host is distinguished from a net by the 3rd octet in the number &#8211; a net number <i>must</i> have two octets and a host number <i>must</i> have three octets.) The number and name should be separated by whitespace (blanks or tabs). The <i>/etc/atalk.names</i> file may contain blank lines or comment lines (lines starting with a `#&#8217;). </p>
<p> AppleTalk addresses are printed in the form</p>
<dl>
<dd>
<pre><i>net.host.port</i>
<tt>144.1.209.2 &gt; icsd-net.112.220
office.2 &gt; icsd-net.112.220
jssmag.149.235 &gt; icsd-net.2</tt></pre>
</dl>
<p> (If the <i>/etc/atalk.names</i> doesn&#8217;t exist or doesn&#8217;t contain an entry for some AppleTalk host/net number, addresses are printed in numeric form.) In the first example, NBP (DDP port 2) on net 144.1 node 209 is sending to whatever is listening on port 220 of net icsd node 112. The second line is the same except the full name of the source node is known (`office&#8217;). The third line is a send from port 235 on net jssmag node 149 to broadcast on the icsd-net NBP port (note that the broadcast address (255) is indicated by a net name with no host number &#8211; for this reason it&#8217;s a good idea to keep node names and net names distinct in /etc/atalk.names). </p>
<p> NBP (name binding protocol) and ATP (AppleTalk transaction protocol) packets have their contents interpreted. Other protocols just dump the protocol name (or number if no name is registered for the protocol) and packet size. </p>
<p> <code>NBP packets</code> are formatted like the following examples:</p>
<dl>
<dd>
<pre><tt>icsd-net.112.220 &gt; jssmag.2: nbp-lkup 190: &quot;=:LaserWriter@*&quot;
jssmag.209.2 &gt; icsd-net.112.220: nbp-reply 190: &quot;RM1140:LaserWriter@*&quot; 250
techpit.2 &gt; icsd-net.112.220: nbp-reply 190: &quot;techpit:LaserWriter@*&quot; 186</tt></pre>
</dl>
<p> The first line is a name lookup request for laserwriters sent by net icsd host 112 and broadcast on net jssmag. The nbp id for the lookup is 190. The second line shows a reply for this request (note that it has the same id) from host jssmag.209 saying that it has a laserwriter resource named &quot;RM1140&quot; registered on port 250. The third line is another reply to the same request saying host techpit has laserwriter &quot;techpit&quot; registered on port 186. </p>
<p> <code>ATP packet</code> formatting is demonstrated by the following example:</p>
<dl>
<dd>
<pre><tt>jssmag.209.165 &gt; helios.132: atp-req 12266&lt;0-7&gt; 0xae030001
helios.132 &gt; jssmag.209.165: atp-resp 12266:0 (512) 0xae040000
helios.132 &gt; jssmag.209.165: atp-resp 12266:1 (512) 0xae040000
helios.132 &gt; jssmag.209.165: atp-resp 12266:2 (512) 0xae040000
helios.132 &gt; jssmag.209.165: atp-resp 12266:3 (512) 0xae040000
helios.132 &gt; jssmag.209.165: atp-resp 12266:4 (512) 0xae040000
helios.132 &gt; jssmag.209.165: atp-resp 12266:5 (512) 0xae040000
helios.132 &gt; jssmag.209.165: atp-resp 12266:6 (512) 0xae040000
helios.132 &gt; jssmag.209.165: atp-resp*12266:7 (512) 0xae040000
jssmag.209.165 &gt; helios.132: atp-req 12266&lt;3,5&gt; 0xae030001
helios.132 &gt; jssmag.209.165: atp-resp 12266:3 (512) 0xae040000
helios.132 &gt; jssmag.209.165: atp-resp 12266:5 (512) 0xae040000
jssmag.209.165 &gt; helios.132: atp-rel 12266&lt;0-7&gt; 0xae030001
jssmag.209.133 &gt; helios.132: atp-req* 12267&lt;0-7&gt; 0xae030002</tt></pre>
</dl>
<p> Jssmag.209 initiates transaction id 12266 with host helios by requesting up to 8 packets (the `&lt;0-7&gt;&#8217;). The hex number at the end of the line is the value of the `userdata&#8217; field in the request. </p>
<p> Helios responds with 8 512-byte packets. The `:digit&#8217; following the transaction id gives the packet sequence number in the transaction and the number in parens is the amount of data in the packet, excluding the ATP header. The `*&#8217; on packet 7 indicates that the EOM bit was set. </p>
<p> Jssmag.209 then requests that packets 3 &amp; 5 be retransmitted. Helios resends them then jssmag.209 releases the transaction. Finally, jssmag.209 initiates the next request. The `*&#8217; on the request indicates that XO (`exactly once&#8217;) was <i>not</i> set.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code>pcap</code>(3PCAP), <code><a href="/docs/linux/man/4-bpf/">bpf</a></code>(4), <code><a href="//www.systutorials.com/docs/linux/man/4P-nit/">nit</a></code>(4P), <code><a href="/docs/linux/man/5-pcap-savefile/">pcap-savefile</a></code>(5), <code><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></code>(7), <code><a href="/docs/linux/man/7-pcap-tstamp/">pcap-tstamp</a></code>(7)</p>
<dl>
<dd><i><a rel="nofollow" href="https://www.iana.org/assignments/media-types/application/vnd.tcpdump.pcap">https://www.iana.org/assignments/media-types/application/vnd.tcpdump.pcap</a></i></dl>
<h2>Authors</h2>
<p>The original authors are: </p>
<p> Van Jacobson, Craig Leres and Steven McCanne, all of the Lawrence Berkeley National Laboratory, University of California, Berkeley, CA. </p>
<p> It is currently being maintained by tcpdump.org. </p>
<p> The current version is available via HTTPS: </p>
<dl>
<dd><i><a rel="nofollow" href="https://www.tcpdump.org/">https://www.tcpdump.org/</a></i></dl>
<p> The original distribution is available via anonymous ftp: </p>
<dl>
<dd><i><a href="ftp://ftp.ee.lbl.gov/old/tcpdump.tar.Z">ftp://ftp.ee.lbl.gov/old/tcpdump.tar.Z</a></i></dl>
<p> IPv6/IPsec support is added by WIDE/KAME project. This program uses OpenSSL/LibreSSL, under specific configurations.</p>
<h2>Bugs</h2>
<p>To report a security issue please send an e-mail to security [at] tcpdump.org. To report bugs and other problems, contribute patches, request a feature, provide generic feedback etc. please see the file <i>CONTRIBUTING</i> in the tcpdump source tree root. NIT doesn&#8217;t let you watch your own outbound traffic, BPF will. We recommend that you use the latter. On Linux systems with 2.0[.x] kernels:</p>
<dl>
<dd>packets on the loopback device will be seen twice;</p>
<dd>packet filtering cannot be done in the kernel, so that all packets must be copied from the kernel in order to be filtered in user mode;</p>
<dd>all of a packet, not just the part that&#8217;s within the snapshot length, will be copied from the kernel (the 2.0[.x] packet capture mechanism, if asked to copy only part of a packet to userspace, will not report the true length of the packet; this would cause most IP packets to get an error from <code>tcpdump</code>);</p>
<dd>capturing on some PPP devices won&#8217;t work correctly.</dl>
<p> We recommend that you upgrade to a 2.2 or later kernel. Some attempt should be made to reassemble IP fragments or, at least to compute the right length for the higher level protocol. Name server inverse queries are not dumped correctly: the (empty) question section is printed rather than real query in the answer section. Some believe that inverse queries are themselves a bug and prefer to fix the program generating them rather than <i>tcpdump</i>. A packet trace that crosses a daylight savings time change will give skewed time stamps (the time change is ignored). Filter expressions on fields other than those in Token Ring headers will not correctly handle source-routed Token Ring packets. Filter expressions on fields other than those in 802.11 headers will not correctly handle 802.11 data packets with both To DS and From DS set. <code>ip6 proto</code> should chase header chain, but at this moment it does not. <code>ip6 protochain</code> is supplied for this behavior. Arithmetic expression against transport layer headers, like <code>tcp[0]</code>, does not work against IPv6 packets. It only looks at IPv4 packets. </p>
