---
title: "wireshark(1)"
name: "wireshark"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wireshark/"
description: "wireshark – Interactively dump and analyze network traffic"
---

<h2 class="name">NAME</h2>
<p> wireshark &#8211; Interactively dump and analyze network traffic </p>
<h2>SYNOPSIS</h2>
<p> <code>wireshark</code> [&nbsp;<wbr><code>-a</code>&nbsp;<wbr>&lt;capture autostop condition&gt;&nbsp;<wbr>]&nbsp;<wbr>&#8230; [&nbsp;<wbr><code>-b</code>&nbsp;<wbr>&lt;capture ring buffer option&gt;&nbsp;<wbr>]&nbsp;<wbr>&#8230; [&nbsp;<wbr><code>-B</code>&nbsp;<wbr>&lt;capture buffer size&gt;&nbsp;<wbr>]&nbsp;<wbr> [&nbsp;<wbr><code>-c</code>&nbsp;<wbr>&lt;capture packet count&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-C</code>&nbsp;<wbr>&lt;configuration profile&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-D</code>&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;display=</code>&lt;X display to use&gt;&nbsp;<wbr>]&nbsp;<wbr> [&nbsp;<wbr><code>-f</code>&nbsp;<wbr>&lt;capture filter&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-g</code>&nbsp;<wbr>&lt;packet number&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-h</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-H</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-i</code>&nbsp;<wbr>&lt;capture interface&gt;|-&nbsp;<wbr>] [&nbsp;<wbr><code>-I</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-j</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-J</code>&nbsp;<wbr>&lt;jump filter&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-k</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-K</code>&nbsp;<wbr>&lt;keytab&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-l</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-L</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-m</code>&nbsp;<wbr>&lt;font&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-n</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-N</code>&nbsp;<wbr>&lt;name resolving flags&gt;&nbsp;<wbr>]&nbsp;<wbr> [&nbsp;<wbr><code>-o</code>&nbsp;<wbr>&lt;preference/recent setting&gt;&nbsp;<wbr>]&nbsp;<wbr>&#8230; [&nbsp;<wbr><code>-p</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-P</code>&nbsp;<wbr>&lt;path setting&gt;] [&nbsp;<wbr><code>-r</code>&nbsp;<wbr>&lt;infile&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-R</code>&nbsp;<wbr>&lt;read&nbsp;<wbr>(display)&nbsp;<wbr>filter&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-s</code>&nbsp;<wbr>&lt;capture snaplen&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-S</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-t</code>&nbsp;<wbr>a|ad|d|dd|e|r|u|ud&nbsp;<wbr>] [&nbsp;<wbr><code>-v</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-w</code>&nbsp;<wbr>&lt;outfile&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-X</code>&nbsp;<wbr>&lt;eXtension option&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-y</code>&nbsp;<wbr>&lt;capture link type&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-Y</code>&nbsp;<wbr>&lt;displaY filter&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-z</code>&nbsp;<wbr>&lt;statistics&gt;&nbsp;<wbr>] [&nbsp;<wbr>&lt;infile&gt;&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Wireshark</code> is a <font SIZE="-1">GUI</font> network protocol analyzer. It lets you interactively browse packet data from a live network or from a previously saved capture file. <code>Wireshark</code>&#8216;s native capture file format is <code>pcap</code> format, which is also the format used by <code>tcpdump</code> and various other tools. </p>
<p> <code>Wireshark</code> can read / import the following file formats:</p>
<dl>
<dt>&bull;</p>
<dd> pcap &#8211; captures from <code>Wireshark</code>/<code>TShark</code>/<code>dumpcap</code>, <code>tcpdump</code>, and various other tools using libpcap&#8217;s/WinPcap&#8217;s/tcpdump&#8217;s/WinDump&#8217;s capture format</p>
<dt>&bull;</p>
<dd> pcap-ng &#8211; &#8220;next-generation&#8221; successor to pcap format</p>
<dt>&bull;</p>
<dd> <code>snoop</code> and <code>atmsnoop</code> captures</p>
<dt>&bull;</p>
<dd> Shomiti/Finisar <code>Surveyor</code> captures</p>
<dt>&bull;</p>
<dd> Novell <code>LANalyzer</code> captures</p>
<dt>&bull;</p>
<dd> Microsoft <code>Network Monitor</code> captures</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">AIX</font>&#8216;s <code>iptrace</code> captures</p>
<dt>&bull;</p>
<dd> Cinco Networks <code>NetXRay</code> captures</p>
<dt>&bull;</p>
<dd> Network Associates Windows-based <code>Sniffer</code> captures</p>
<dt>&bull;</p>
<dd> Network General/Network Associates DOS-based <code>Sniffer</code> (compressed or uncompressed) captures</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">AG</font> Group/WildPackets <code>EtherPeek</code>/<code>TokenPeek</code>/<code>AiroPeek</code>/<code>EtherHelp</code>/<code>PacketGrabber</code> captures</p>
<dt>&bull;</p>
<dd> <font SIZE="-1"><code>RADCOM</code></font>&#8216;s <font SIZE="-1">WAN/LAN</font> analyzer captures</p>
<dt>&bull;</p>
<dd> Network Instruments <code>Observer</code> version 9 captures</p>
<dt>&bull;</p>
<dd> <code>Lucent/Ascend</code> router debug output</p>
<dt>&bull;</p>
<dd> files from HP-UX&#8217;s <code>nettl</code></p>
<dt>&bull;</p>
<dd> <code>Toshiba&#8217;s</code> <font SIZE="-1">ISDN</font> routers dump output</p>
<dt>&bull;</p>
<dd> the output from <code>i4btrace</code> from the <font SIZE="-1">ISDN4BSD</font> project</p>
<dt>&bull;</p>
<dd> traces from the <code>EyeSDN</code> <font SIZE="-1">USB S0.</font></p>
<dt>&bull;</p>
<dd> the output in <code>IPLog</code> format from the Cisco Secure Intrusion Detection System</p>
<dt>&bull;</p>
<dd> <code>pppd logs</code> (pppdump format)</p>
<dt>&bull;</p>
<dd> the output from <font SIZE="-1">VMS</font>&#8216;s <code>TCPIPtrace</code>/<code>TCPtrace</code>/<font SIZE="-1"><code>UCX$TRACE</code></font> utilities</p>
<dt>&bull;</p>
<dd> the text output from the <font SIZE="-1"><code>DBS</code></font><code> Etherwatch</code> <font SIZE="-1">VMS</font> utility</p>
<dt>&bull;</p>
<dd> Visual Networks&#8217; <code>Visual UpTime</code> traffic capture</p>
<dt>&bull;</p>
<dd> the output from <code>CoSine</code> L2 debug</p>
<dt>&bull;</p>
<dd> the output from InfoVista&#8217;s <code>5View</code> <font SIZE="-1">LAN</font> agents</p>
<dt>&bull;</p>
<dd> Endace Measurement Systems&#8217; <font SIZE="-1">ERF</font> format captures</p>
<dt>&bull;</p>
<dd> Linux Bluez Bluetooth stack <code>hcidump -w</code> traces</p>
<dt>&bull;</p>
<dd> Catapult <font SIZE="-1">DCT2000 </font>.out files</p>
<dt>&bull;</p>
<dd> Gammu generated text output from Nokia <font SIZE="-1">DCT3</font> phones in Netmonitor mode</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">IBM</font> Series (<font SIZE="-1">OS/400</font>) Comm traces (<font SIZE="-1">ASCII &amp; UNICODE</font>)</p>
<dt>&bull;</p>
<dd> Juniper Netscreen snoop files</p>
<dt>&bull;</p>
<dd> Symbian <font SIZE="-1">OS</font> btsnoop files</p>
<dt>&bull;</p>
<dd> TamoSoft CommView files</p>
<dt>&bull;</p>
<dd> Textronix K12xx 32bit .rf5 format files</p>
<dt>&bull;</p>
<dd> Textronix K12 text file format captures</p>
<dt>&bull;</p>
<dd> Apple PacketLogger files</p>
<dt>&bull;</p>
<dd> Files from Aethra Telecommunications&#8217; <font SIZE="-1">PC108</font> software for their test instruments</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">MPEG-2</font> Transport Streams as defined in <font SIZE="-1">ISO/IEC 13818-1</font></p>
<dt>&bull;</p>
<dd> Rabbit Labs <font SIZE="-1">CAM</font> Inspector files</dl>
<p> There is no need to tell <code>Wireshark</code> what type of file you are reading; it will determine the file type by itself. <code>Wireshark</code> is also capable of reading any of these file formats if they are compressed using gzip. <code>Wireshark</code> recognizes this directly from the file; the &#8216;.gz&#8217; extension is not required for this purpose. </p>
<p> Like other protocol analyzers, <code>Wireshark</code>&#8216;s main window shows 3 views of a packet. It shows a summary line, briefly describing what the packet is. A packet details display is shown, allowing you to drill down to exact protocol or field that you interested in. Finally, a hex dump shows you exactly what the packet looks like when it goes over the wire. </p>
<p> In addition, <code>Wireshark</code> has some features that make it unique. It can assemble all the packets in a <font SIZE="-1">TCP</font> conversation and show you the <font SIZE="-1">ASCII </font>(or <font SIZE="-1">EBCDIC,</font> or hex) data in that conversation. Display filters in <code>Wireshark</code> are very powerful; more fields are filterable in <code>Wireshark</code> than in other protocol analyzers, and the syntax you can use to create your filters is richer. As <code>Wireshark</code> progresses, expect more and more protocol fields to be allowed in display filters. </p>
<p> Packet capturing is performed with the pcap library. The capture filter syntax follows the rules of the pcap library. This syntax is different from the display filter syntax. </p>
<p> Compressed file support uses (and therefore requires) the zlib library. If the zlib library is not present, <code>Wireshark</code> will compile, but will be unable to read compressed files. </p>
<p> The pathname of a capture file to be read can be specified with the <code>-r</code> option or can be specified as a command-line argument.</p>
<h2>OPTIONS</h2>
<p> Most users will want to start <code>Wireshark</code> without options and configure it from the menus instead. Those users may just skip this section.</p>
<dl>
<dt>-a &lt;capture autostop condition&gt;</p>
<dd> Specify a criterion that specifies when <code>Wireshark</code> is to stop writing to a capture file. The criterion is of the form <i>test</i><code>:</code><i>value</i>, where <i>test</i> is one of: </p>
<p> <code>duration</code>:<i>value</i> Stop writing to a capture file after <i>value</i> seconds have elapsed. </p>
<p> <code>filesize</code>:<i>value</i> Stop writing to a capture file after it reaches a size of <i>value</i> kB. If this option is used together with the -b option, Wireshark will stop writing to the current capture file and switch to the next one if filesize is reached. Note that the filesize is limited to a maximum value of 2 GiB. </p>
<p> <code>files</code>:<i>value</i> Stop writing to capture files after <i>value</i> number of files were written.</p>
<dt>-b &lt;capture ring buffer option&gt;</p>
<dd> Cause <code>Wireshark</code> to run in &#8220;multiple files&#8221; mode. In &#8220;multiple files&#8221; mode, <code>Wireshark</code> will write to several capture files. When the first capture file fills up, <code>Wireshark</code> will switch writing to the next file and so on. </p>
<p> The created filenames are based on the filename given with the <code>-w</code> flag, the number of the file and on the creation date and time, e.g. outfile_00001_20050604120117.pcap, outfile_00002_20050604120523.pcap, &#8230; </p>
<p> With the <i>files</i> option it&#8217;s also possible to form a &#8220;ring buffer&#8221;. This will fill up new files until the number of files specified, at which point <code>Wireshark</code> will discard the data in the first file and start writing to that file and so on. If the <i>files</i> option is not set, new files filled up until one of the capture stop conditions match (or until the disk is full). </p>
<p> The criterion is of the form <i>key</i><code>:</code><i>value</i>, where <i>key</i> is one of: </p>
<p> <code>duration</code>:<i>value</i> switch to the next file after <i>value</i> seconds have elapsed, even if the current file is not completely filled up. </p>
<p> <code>filesize</code>:<i>value</i> switch to the next file after it reaches a size of <i>value</i> kB. Note that the filesize is limited to a maximum value of 2 GiB. </p>
<p> <code>files</code>:<i>value</i> begin again with the first file after <i>value</i> number of files were written (form a ring buffer). This value must be less than 100000. Caution should be used when using large numbers of files: some filesystems do not handle many files in a single directory well. The <code>files</code> criterion requires either <code>duration</code> or <code>filesize</code> to be specified to control when to go to the next file. It should be noted that each <code>-b</code> parameter takes exactly one criterion; to specify two criterion, each must be preceded by the <code>-b</code> option. </p>
<p> Example: <code>-b filesize:1000 -b files:5</code> results in a ring buffer of five files of size one megabyte each.</p>
<dt>-B &lt;capture buffer size&gt;</p>
<dd> Set capture buffer size (in MiB, default is 2 MiB). This is used by the capture driver to buffer packet data until that data can be written to disk. If you encounter packet drops while capturing, try to increase this size. Note that, while <code>Wireshark</code> attempts to set the buffer size to 2 MiB by default, and can be told to set it to a larger value, the system or interface on which you&#8217;re capturing might silently limit the capture buffer size to a lower value or raise it to a higher value. </p>
<p> This is available on <font SIZE="-1">UNIX</font> systems with libpcap 1.0.0 or later and on Windows. It is not available on <font SIZE="-1">UNIX</font> systems with earlier versions of libpcap. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default capture buffer size. If used after an <code>-i</code> option, it sets the capture buffer size for the interface specified by the last <code>-i</code> option occurring before this option. If the capture buffer size is not set specifically, the default capture buffer size is used instead.</p>
<dt>-c &lt;capture packet count&gt;</p>
<dd> Set the maximum number of packets to read when capturing live data.</p>
<dt>-C &lt;configuration profile&gt;</p>
<dd> Start with the given configuration profile.</p>
<dt>-D</p>
<dd> Print a list of the interfaces on which <code>Wireshark</code> can capture, and exit. For each network interface, a number and an interface name, possibly followed by a text description of the interface, is printed. The interface name or the number can be supplied to the <code>-i</code> flag to specify an interface on which to capture. </p>
<p> This can be useful on systems that don&#8217;t have a command to list them (e.g., Windows systems, or <font SIZE="-1">UNIX</font> systems lacking <code>ifconfig -a</code>); the number can be useful on Windows 2000 and later systems, where the interface name is a somewhat complex string. </p>
<p> Note that &#8220;can capture&#8221; means that <code>Wireshark</code> was able to open that device to do a live capture; if, on your system, a program doing a network capture must be run from an account with special privileges (for example, as root), then, if <code>Wireshark</code> is run with the <code>-D</code> flag and is not run from such an account, it will not list any interfaces.</p>
<dt>&#8211;display=&lt;X display to use&gt;</p>
<dd> Specifies the X display to use. A hostname and screen (otherhost:0.0) or just a screen (:0.0) can be specified. This option is not available under Windows.</p>
<dt>-f &lt;capture filter&gt;</p>
<dd> Set the capture filter expression. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default capture filter expression. If used after an <code>-i</code> option, it sets the capture filter expression for the interface specified by the last <code>-i</code> option occurring before this option. If the capture filter expression is not set specifically, the default capture filter expression is used if provided.</p>
<dt>-g &lt;packet number&gt;</p>
<dd> After reading in a capture file using the <code>-r</code> flag, go to the given <i>packet number</i>.</p>
<dt>-h</p>
<dd> Print the version and options and exit.</p>
<dt>-H</p>
<dd> Hide the capture info dialog during live packet capture.</p>
<dt>-i &lt;capture interface&gt;|-</p>
<dd> Set the name of the network interface or pipe to use for live packet capture. </p>
<p> Network interface names should match one of the names listed in &quot;<code>wireshark -D</code>&#8220; (described above); a number, as reported by &#8221;<code>wireshark -D</code>&#8220;, can also be used. If you&#8217;re using <font SIZE="-1">UNIX, &#8221;</font><code>netstat -i</code>&#8220; or &#8221;<code>ifconfig -a</code>&quot; might also work to list interface names, although not all versions of <font SIZE="-1">UNIX</font> support the <code>-a</code> flag to <code>ifconfig</code>. </p>
<p> If no interface is specified, <code>Wireshark</code> searches the list of interfaces, choosing the first non-loopback interface if there are any non-loopback interfaces, and choosing the first loopback interface if there are no non-loopback interfaces. If there are no interfaces at all, <code>Wireshark</code> reports an error and doesn&#8217;t start the capture. </p>
<p> Pipe names should be either the name of a <font SIZE="-1">FIFO </font>(named pipe) or &#8220;-&#8221; to read data from the standard input. On Windows systems, pipe names must be of the form &#8220;\pipe\.\<code>pipename</code>&#8221;. Data read from pipes must be in standard pcap format. </p>
<p> This option can occur multiple times. When capturing from multiple interfaces, the capture file will be saved in pcap-ng format.</p>
<dt>-I</p>
<dd> Put the interface in &#8220;monitor mode&#8221;; this is supported only on <font SIZE="-1">IEEE 802.11</font> Wi-Fi interfaces, and supported only on some operating systems. </p>
<p> Note that in monitor mode the adapter might disassociate from the network with which it&#8217;s associated, so that you will not be able to use any wireless networks with that adapter. This could prevent accessing files on a network server, or resolving host names or network addresses, if you are capturing in monitor mode and are not connected to another network with another adapter. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it enables the monitor mode for all interfaces. If used after an <code>-i</code> option, it enables the monitor mode for the interface specified by the last <code>-i</code> option occurring before this option.</p>
<dt>-j</p>
<dd> Use after <code>-J</code> to change the behavior when no exact match is found for the filter. With this option select the first packet before.</p>
<dt>-J &lt;jump filter&gt;</p>
<dd> After reading in a capture file using the <code>-r</code> flag, jump to the packet matching the filter (display filter syntax). If no exact match is found the first packet after that is selected.</p>
<dt>-k</p>
<dd> Start the capture session immediately. If the <code>-i</code> flag was specified, the capture uses the specified interface. Otherwise, <code>Wireshark</code> searches the list of interfaces, choosing the first non-loopback interface if there are any non-loopback interfaces, and choosing the first loopback interface if there are no non-loopback interfaces; if there are no interfaces, <code>Wireshark</code> reports an error and doesn&#8217;t start the capture.</p>
<dt>-K &lt;keytab&gt;</p>
<dd> Load kerberos crypto keys from the specified keytab file. This option can be used multiple times to load keys from several files. </p>
<p> Example: <code>-K krb5.keytab</code></p>
<dt>-l</p>
<dd> Turn on automatic scrolling if the packet display is being updated automatically as packets arrive during a capture (as specified by the <code>-S</code> flag).</p>
<dt>-L</p>
<dd> List the data link types supported by the interface and exit.</p>
<dt>-m &lt;font&gt;</p>
<dd> Set the name of the font used by <code>Wireshark</code> for most text. <code>Wireshark</code> will construct the name of the bold font used for the data in the byte view pane that corresponds to the field selected in the packet details pane from the name of the main text font.</p>
<dt>-n</p>
<dd> Disable network object name resolution (such as hostname, <font SIZE="-1">TCP</font> and <font SIZE="-1">UDP</font> port names), the <code>-N</code> flag might override this one.</p>
<dt>-N &lt;name resolving flags&gt;</p>
<dd> Turn on name resolving only for particular types of addresses and port numbers, with name resolving for other types of addresses and port numbers turned off. This flag overrides <code>-n</code> if both <code>-N</code> and <code>-n</code> are present. If both <code>-N</code> and <code>-n</code> flags are not present, all name resolutions are turned on. </p>
<p> The argument is a string that may contain the letters: </p>
<p> <code>m</code> to enable <font SIZE="-1">MAC</font> address resolution </p>
<p> <code>n</code> to enable network address resolution </p>
<p> <code>N</code> to enable using external resolvers (e.g., <font SIZE="-1">DNS</font>) for network address resolution </p>
<p> <code>t</code> to enable transport-layer port number resolution </p>
<p> <code>C</code> to enable concurrent (asynchronous) <font SIZE="-1">DNS</font> lookups</p>
<dt>-o &lt;preference/recent setting&gt;</p>
<dd> Set a preference or recent value, overriding the default value and any value read from a preference/recent file. The argument to the flag is a string of the form <i>prefname</i><code>:</code><i>value</i>, where <i>prefname</i> is the name of the preference/recent value (which is the same name that would appear in the preference/recent file), and <i>value</i> is the value to which it should be set. Since <code>Ethereal</code> 0.10.12, the recent settings replaces the formerly used -B, -P and -T flags to manipulate the <font SIZE="-1">GUI</font> dimensions. </p>
<p> If <i>prefname</i> is &#8220;uat&#8221;, you can override settings in various user access tables using the form uat<code>:</code><i>uat filename</i>:<i>uat record</i>. <i>uat filename</i> must be the name of a <font SIZE="-1">UAT</font> file, e.g. <i>user_dlts</i>. <i>uat_record</i> must be in the form of a valid record for that file, including quotes. For instance, to specify a user <font SIZE="-1">DLT</font> from the command line, you would use </p>
<pre>
    -o &quot;uat:user_dlts:\&quot;User 0 (DLT=147)\&quot;,\&quot;cops\&quot;,\&quot;0\&quot;,\&quot;\&quot;,\&quot;0\&quot;,\&quot;\&quot;&quot;
</pre>
<dt>-p</p>
<dd> <i>Don&#8217;t</i> put the interface into promiscuous mode. Note that the interface might be in promiscuous mode for some other reason; hence, <code>-p</code> cannot be used to ensure that the only traffic that is captured is traffic sent to or from the machine on which <code>Wireshark</code> is running, broadcast traffic, and multicast traffic to addresses received by that machine. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, no interface will be put into the promiscuous mode. If used after an <code>-i</code> option, the interface specified by the last <code>-i</code> option occurring before this option will not be put into the promiscuous mode.</p>
<dt>-P &lt;path setting&gt;</p>
<dd> Special path settings usually detected automatically. This is used for special cases, e.g. starting Wireshark from a known location on an <font SIZE="-1">USB</font> stick. </p>
<p> The criterion is of the form <i>key</i><code>:</code><i>path</i>, where <i>key</i> is one of: </p>
<p> <code>persconf</code>:<i>path</i> path of personal configuration files, like the preferences files. </p>
<p> <code>persdata</code>:<i>path</i> path of personal data files, it&#8217;s the folder initially opened. After the very first initialization, the recent file will keep the folder last used.</p>
<dt>-r &lt;infile&gt;</p>
<dd> Read packet data from <i>infile</i>, can be any supported capture file format (including gzipped files). It&#8217;s not possible to use named pipes or stdin here! To capture from a pipe or from stdin use <code>-i &#8211;</code></p>
<dt>-R &lt;read (display) filter&gt;</p>
<dd> When reading a capture file specified with the <code>-r</code> flag, causes the specified filter (which uses the syntax of display filters, rather than that of capture filters) to be applied to all packets read from the capture file; packets not matching the filter are discarded.</p>
<dt>-s &lt;capture snaplen&gt;</p>
<dd> Set the default snapshot length to use when capturing live data. No more than <i>snaplen</i> bytes of each network packet will be read into memory, or saved to disk. A value of 0 specifies a snapshot length of 65535, so that the full packet is captured; this is the default. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default snapshot length. If used after an <code>-i</code> option, it sets the snapshot length for the interface specified by the last <code>-i</code> option occurring before this option. If the snapshot length is not set specifically, the default snapshot length is used if provided.</p>
<dt>-S</p>
<dd> Automatically update the packet display as packets are coming in.</p>
<dt>-t a|ad|d|dd|e|r|u|ud</p>
<dd> Set the format of the packet timestamp displayed in the packet list window. The format can be one of: </p>
<p> <code>a</code> absolute: The absolute time is the actual time the packet was captured, with no date displayed </p>
<p> <code>ad</code> absolute with date: The absolute date and time is the actual time and date the packet was captured </p>
<p> <code>d</code> delta: The delta time is the time since the previous packet was captured </p>
<p> <code>dd</code> delta_displayed: The delta_displayed time is the time since the previous displayed packet was captured </p>
<p> <code>e</code> epoch: The time in seconds since epoch (Jan 1, 1970 00:00:00) </p>
<p> <code>r</code> relative: The relative time is the time elapsed between the first packet and the current packet </p>
<p> <code>u</code> <font SIZE="-1">UTC:</font> The <font SIZE="-1">UTC</font> time is the actual time the packet was captured, with no date displayed </p>
<p> <code>ud</code> <font SIZE="-1">UTC</font> with date: The <font SIZE="-1">UTC</font> date and time is the actual time and date the packet was captured </p>
<p> The default format is relative.</p>
<dt>-v</p>
<dd> Print the version and exit.</p>
<dt>-w &lt;outfile&gt;</p>
<dd> Set the default capture file name.</p>
<dt>-X &lt;eXtension options&gt;</p>
<dd> Specify an option to be passed to an <code>Wireshark</code> module. The eXtension option is in the form <i>extension_key</i><code>:</code><i>value</i>, where <i>extension_key</i> can be: </p>
<p> <code>lua_script</code>:<i>lua_script_filename</i> tells <code>Wireshark</code> to load the given script in addition to the default Lua scripts. </p>
<p> <code>stdin_descr</code>:<i>description</i> tells <code>Wireshark</code> to use the given description when capturing from standard input (<code>-i &#8211;</code>).</p>
<dt>-y &lt;capture link type&gt;</p>
<dd> If a capture is started from the command line with <code>-k</code>, set the data link type to use while capturing packets. The values reported by <code>-L</code> are the values that can be used. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default capture link type. If used after an <code>-i</code> option, it sets the capture link type for the interface specified by the last <code>-i</code> option occurring before this option. If the capture link type is not set specifically, the default capture link type is used if provided.</p>
<dt>-Y &lt;displaY filter&gt;</p>
<dd> Start with the given display filter.</p>
<dt>-z &lt;statistics&gt;</p>
<dd> Get <code>Wireshark</code> to collect various types of statistics and display the result in a window that updates in semi-real time. </p>
<p> Currently implemented statistics are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-z</code> conv,<i>type</i>[,<i>filter</i>]</p>
<dd> Create a table that lists all conversations that could be seen in the capture. <i>type</i> specifies the conversation endpoint types for which we want to generate the statistics; currently the supported ones are: </p>
<pre>
  &quot;eth&quot;   Ethernet addresses
  &quot;fc&quot;    Fibre Channel addresses
  &quot;fddi&quot;  FDDI addresses
  &quot;ip&quot;    IPv4 addresses
  &quot;ipv6&quot;  IPv6 addresses
  &quot;ipx&quot;   IPX addresses
  &quot;tcp&quot;   TCP/IP socket pairs   Both IPv4 and IPv6 are supported
  &quot;tr&quot;    Token Ring addresses
  &quot;udp&quot;   UDP/IP socket pairs   Both IPv4 and IPv6 are supported
</pre>
<p> If the optional <i>filter</i> is specified, only those packets that match the filter will be used in the calculations. </p>
<p> The table is presented with one line for each conversation and displays the number of packets/bytes in each direction as well as the total number of packets/bytes. By default, the table is sorted according to the total number of packets. </p>
<p> These tables can also be generated at runtime by selecting the appropriate conversation type from the menu &#8220;Tools/Statistics/Conversation List/&#8221;.</p>
<dt><code>-z</code> dcerpc,srt,<i>uuid</i>,<i>major</i>.<i>minor</i>[,<i>filter</i>]</p>
<dd> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">DCERPC</font> interface <i>uuid</i>, version <i>major</i>.<i>minor</i>. Data collected is the number of calls for each procedure, MinSRT, MaxSRT and AvgSRT. </p>
<p> Example: <code>-z dcerpc,srt,12345778-1234-abcd-ef00-0123456789ac,1.0</code> will collect data for the <font SIZE="-1">CIFS SAMR</font> Interface. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z dcerpc,srt,12345778-1234-abcd-ef00-0123456789ac,1.0,ip.addr==1.2.3.4</code> will collect <font SIZE="-1">SAMR SRT</font> statistics for a specific host.</p>
<dt><code>-z</code> fc,srt[,<i>filter</i>]</p>
<dd> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">FC. </font> Data collected is the number of calls for each Fibre Channel command, MinSRT, MaxSRT and AvgSRT. </p>
<p> Example: <code>-z fc,srt</code> will calculate the Service Response Time as the time delta between the First packet of the exchange and the Last packet of the exchange. </p>
<p> The data will be presented as separate tables for all normal <font SIZE="-1">FC</font> commands, Only those commands that are seen in the capture will have its stats displayed. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z &#8220;fc,srt,fc.id==01.02.03&#8221;</code> will collect stats only for <font SIZE="-1">FC</font> packets exchanged by the host at <font SIZE="-1">FC</font> address 01.02.03 .</p>
<dt><code>-z</code> h225,counter[<i>,filter</i>]</p>
<dd> Count ITU-T H.225 messages and their reasons. In the first column you get a list of H.225 messages and H.225 message reasons which occur in the current capture file. The number of occurrences of each message or reason is displayed in the second column. </p>
<p> Example: <code>-z h225,counter</code> </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z &#8220;h225,counter,ip.addr==1.2.3.4&#8221;</code> will collect stats only for H.225 packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 .</p>
<dt><code>-z</code> h225,srt[<i>,filter</i>]</p>
<dd> Collect request/response <font SIZE="-1">SRT </font>(Service Response Time) data for ITU-T H.225 <font SIZE="-1">RAS.</font> Data collected is the number of calls of each ITU-T H.225 <font SIZE="-1">RAS</font> Message Type, Minimum <font SIZE="-1">SRT,</font> Maximum <font SIZE="-1">SRT,</font> Average <font SIZE="-1">SRT,</font> Minimum in Packet, and Maximum in Packet. You will also get the number of Open Requests (Unresponded Requests), Discarded Responses (Responses without matching request) and Duplicate Messages. </p>
<p> Example: <code>-z h225,srt</code> </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z &#8220;h225,srt,ip.addr==1.2.3.4&#8221;</code> will collect stats only for ITU-T H.225 <font SIZE="-1">RAS</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 .</p>
<dt><code>-z</code> io,stat</p>
<dd> Collect packet/bytes statistics for the capture in intervals of 1 second. This option will open a window with up to 5 color-coded graphs where number-of-packets-per-second or number-of-bytes-per-second statistics can be calculated and displayed. </p>
<p> This option can be used multiple times on the command line. </p>
<p> This graph window can also be opened from the Analyze:Statistics:Traffic:IO-Stat menu item.</p>
<dt><code>-z</code> ldap,srt[,<i>filter</i>]</p>
<dd> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">LDAP. </font> Data collected is the number of calls for each implemented <font SIZE="-1">LDAP</font> command, MinSRT, MaxSRT and AvgSRT. </p>
<p> Example: <code>-z ldap,srt</code> will calculate the Service Response Time as the time delta between the Request and the Response. </p>
<p> The data will be presented as separate tables for all implemented <font SIZE="-1">LDAP</font> commands, Only those commands that are seen in the capture will have its stats displayed. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: use <code>-z &#8220;ldap,srt,ip.addr==10.1.1.1&#8221;</code> will collect stats only for <font SIZE="-1">LDAP</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 10.1.1.1 . </p>
<p> The only <font SIZE="-1">LDAP</font> commands that are currently implemented and for which the stats will be available are: <font SIZE="-1">BIND SEARCH MODIFY ADD DELETE MODRDN COMPARE EXTENDED</font></p>
<dt><code>-z</code> megaco,srt[<i>,filter</i>]</p>
<dd> Collect request/response <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">MEGACO. </font>(This is similar to <code>-z smb,srt</code>). Data collected is the number of calls for each known <font SIZE="-1">MEGACO</font> Command, Minimum <font SIZE="-1">SRT,</font> Maximum <font SIZE="-1">SRT</font> and Average <font SIZE="-1">SRT.</font> </p>
<p> Example: <code>-z megaco,srt</code> </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z &#8220;megaco,srt,ip.addr==1.2.3.4&#8221;</code> will collect stats only for <font SIZE="-1">MEGACO</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 .</p>
<dt><code>-z</code> mgcp,srt[<i>,filter</i>]</p>
<dd> Collect request/response <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">MGCP. </font>(This is similar to <code>-z smb,srt</code>). Data collected is the number of calls for each known <font SIZE="-1">MGCP</font> Type, Minimum <font SIZE="-1">SRT,</font> Maximum <font SIZE="-1">SRT</font> and Average <font SIZE="-1">SRT.</font> </p>
<p> Example: <code>-z mgcp,srt</code> </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z &#8220;mgcp,srt,ip.addr==1.2.3.4&#8221;</code> will collect stats only for <font SIZE="-1">MGCP</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 .</p>
<dt><code>-z</code> rpc,programs</p>
<dd> Collect call/reply <font SIZE="-1">SRT</font> data for all known ONC-RPC programs/versions. Data collected is the number of calls for each protocol/version, MinSRT, MaxSRT and AvgSRT.</p>
<dt><code>-z</code> rpc,srt,<i>program</i>,<i>version</i>[,&lt;filter&gt;]</p>
<dd> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <i>program</i>/<i>version</i>. Data collected is the number of calls for each procedure, MinSRT, MaxSRT and AvgSRT. </p>
<p> Example: <code>-z rpc,srt,100003,3</code> will collect data for <font SIZE="-1">NFS</font> v3. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z rpc,srt,100003,3,nfs.fh.hash==0x12345678</code> will collect <font SIZE="-1">NFS</font> v3 <font SIZE="-1">SRT</font> statistics for a specific file.</p>
<dt><code>-z</code> scsi,srt,<i>cmdset</i>[,&lt;filter&gt;]</p>
<dd> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">SCSI</font> commandset &lt;cmdset&gt;. </p>
<p> Commandsets are 0:SBC 1:SSC 5:MMC </p>
<p> Data collected is the number of calls for each procedure, MinSRT, MaxSRT and AvgSRT. </p>
<p> Example: <code>-z scsi,srt,0</code> will collect data for <font SIZE="-1">SCSI BLOCK COMMANDS </font>(<font SIZE="-1">SBC</font>). </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z scsi,srt,0,ip.addr==1.2.3.4</code> will collect <font SIZE="-1">SCSI SBC SRT</font> statistics for a specific iscsi/ifcp/fcip host.</p>
<dt><code>-z</code> sip,stat[<i>,filter</i>]</p>
<dd> This option will activate a counter for <font SIZE="-1">SIP</font> messages. You will get the number of occurrences of each <font SIZE="-1">SIP</font> Method and of each <font SIZE="-1">SIP</font> Status-Code. Additionally you also get the number of resent <font SIZE="-1">SIP</font> Messages (only for <font SIZE="-1">SIP</font> over <font SIZE="-1">UDP</font>). </p>
<p> Example: <code>-z sip,stat</code> </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z &#8220;sip,stat,ip.addr==1.2.3.4&#8221;</code> will collect stats only for <font SIZE="-1">SIP</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 .</p>
<dt><code>-z</code> smb,srt[,<i>filter</i>]</p>
<dd> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">SMB. </font> Data collected is the number of calls for each <font SIZE="-1">SMB</font> command, MinSRT, MaxSRT and AvgSRT. </p>
<p> Example: <code>-z smb,srt</code> </p>
<p> The data will be presented as separate tables for all normal <font SIZE="-1">SMB</font> commands, all Transaction2 commands and all <font SIZE="-1">NT</font> Transaction commands. Only those commands that are seen in the capture will have their stats displayed. Only the first command in a xAndX command chain will be used in the calculation. So for common SessionSetupAndX + TreeConnectAndX chains, only the SessionSetupAndX call will be used in the statistics. This is a flaw that might be fixed in the future. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z &#8220;smb,srt,ip.addr==1.2.3.4&#8221;</code> will collect stats only for <font SIZE="-1">SMB</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 .</p>
<dt><code>-z</code> voip,calls</p>
<dd> This option will show a window that shows VoIP calls found in the capture file. This is the same window shown as when you go to the Statistics Menu and choose VoIP Calls. </p>
<p> Example: <code>-z voip,calls</code></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>INTERFACE</h2>
<h3><font SIZE="-1">MENU ITEMS</font></h3>
<dl>
<dt>File:Open</p>
<dd>
<dt>File:Open Recent</p>
<dd>
<dt>File:Merge</p>
<dd> Merge another capture file to the currently loaded one. The <i>File:Merge</i> dialog box allows the merge &#8220;Prepended&#8221;, &#8220;Chronologically&#8221; or &#8220;Appended&#8221;, relative to the already loaded one.</p>
<dt>File:Close</p>
<dd> Open or close a capture file. The <i>File:Open</i> dialog box allows a filter to be specified; when the capture file is read, the filter is applied to all packets read from the file, and packets not matching the filter are discarded. The <i>File:Open Recent</i> is a submenu and will show a list of previously opened files.</p>
<dt>File:Save</p>
<dd>
<dt>File:Save As</p>
<dd> Save the current capture, or the packets currently displayed from that capture, to a file. Check boxes let you select whether to save all packets, or just those that have passed the current display filter and/or those that are currently marked, and an option menu lets you select (from a list of file formats in which at particular capture, or the packets currently displayed from that capture, can be saved), a file format in which to save it.</p>
<dt>File:File Set:List Files</p>
<dd> Show a dialog box that lists all files of the file set matching the currently loaded file. A file set is a compound of files resulting from a capture using the &#8220;multiple files&#8221; / &#8220;ringbuffer&#8221; mode, recognizable by the filename pattern, e.g.: Filename_00001_20050604101530.pcap.</p>
<dt>File:File Set:Next File</p>
<dd>
<dt>File:File Set:Previous File</p>
<dd> If the currently loaded file is part of a file set (see above), open the next / previous file in that set.</p>
<dt>File:Export</p>
<dd> Export captured data into an external format. Note: the data cannot be imported back into Wireshark, so be sure to keep the capture file.</p>
<dt>File:Print</p>
<dd> Print packet data from the current capture. You can select the range of packets to be printed (which packets are printed), and the output format of each packet (how each packet is printed). The output format will be similar to the displayed values, so a summary line, the packet details view, and/or the hex dump of the packet can be printed. </p>
<p> Printing options can be set with the <i>Edit:Preferences</i> menu item, or in the dialog box popped up by this menu item.</p>
<dt>File:Quit</p>
<dd> Exit the application.</p>
<dt>Edit:Copy:Description</p>
<dd> Copies the description of the selected field in the protocol tree to the clipboard.</p>
<dt>Edit:Copy:Fieldname</p>
<dd> Copies the fieldname of the selected field in the protocol tree to the clipboard.</p>
<dt>Edit:Copy:Value</p>
<dd> Copies the value of the selected field in the protocol tree to the clipboard.</p>
<dt>Edit:Copy:As Filter</p>
<dd> Create a display filter based on the data currently highlighted in the packet details and copy that filter to the clipboard. </p>
<p> If that data is a field that can be tested in a display filter expression, the display filter will test that field; otherwise, the display filter will be based on the absolute offset within the packet. Therefore it could be unreliable if the packet contains protocols with variable-length headers, such as a source-routed token-ring packet.</p>
<dt>Edit:Find Packet</p>
<dd> Search forward or backward, starting with the currently selected packet (or the most recently selected packet, if no packet is selected). Search criteria can be a display filter expression, a string of hexadecimal digits, or a text string. </p>
<p> When searching for a text string, you can search the packet data, or you can search the text in the Info column in the packet list pane or in the packet details pane. </p>
<p> Hexadecimal digits can be separated by colons, periods, or dashes. Text string searches can be <font SIZE="-1">ASCII</font> or Unicode (or both), and may be case insensitive.</p>
<dt>Edit:Find Next</p>
<dd>
<dt>Edit:Find Previous</p>
<dd> Search forward / backward for a packet matching the filter from the previous search, starting with the currently selected packet (or the most recently selected packet, if no packet is selected).</p>
<dt>Edit:Mark Packet (toggle)</p>
<dd> Mark (or unmark if currently marked) the selected packet. The field &#8220;frame.marked&#8221; is set for packets that are marked, so that, for example, a display filters can be used to display only marked packets, and so that the &#8220;Edit:Find Packet&#8221; dialog can be used to find the next or previous marked packet.</p>
<dt>Edit:Find Next Mark</p>
<dd>
<dt>Edit:Find Previous Mark</p>
<dd> Find next/previous marked packet.</p>
<dt>Edit:Mark All Packets</p>
<dd>
<dt>Edit:Unmark All Packets</p>
<dd> Mark / Unmark all packets that are currently displayed.</p>
<dt>Edit:Time Reference:Set Time Reference (toggle)</p>
<dd> Set (or unset if currently set) the selected packet as a Time Reference packet. When a packet is set as a Time Reference packet, the timestamps in the packet list pane will be replaced with the string &#8220;*REF*&#8221;. The relative time timestamp in later packets will then be calculated relative to the timestamp of this Time Reference packet and not the first packet in the capture. </p>
<p> Packets that have been selected as Time Reference packets will always be displayed in the packet list pane. Display filters will not affect or hide these packets. </p>
<p> If there is a column displayed for &#8220;Cumulative Bytes&#8221; this counter will be reset at every Time Reference packet.</p>
<dt>Edit:Time Reference:Find Next</p>
<dd>
<dt>Edit:Time Reference:Find Previous</p>
<dd> Search forward / backward for a time referenced packet.</p>
<dt>Edit:Configuration Profiles</p>
<dd> Manage configuration profiles to be able to use more than one set of preferences and configurations.</p>
<dt>Edit:Preferences</p>
<dd> Set the <font SIZE="-1">GUI,</font> capture, printing and protocol options (see &#8220;Preferences&#8221; dialog below).</p>
<dt>View:Main Toolbar</p>
<dd>
<dt>View:Filter Toolbar</p>
<dd>
<dt>View:Statusbar</p>
<dd> Show or hide the main window controls.</p>
<dt>View:Packet List</p>
<dd>
<dt>View:Packet Details</p>
<dd>
<dt>View:Packet Bytes</p>
<dd> Show or hide the main window panes.</p>
<dt>View:Time Display Format</p>
<dd> Set the format of the packet timestamp displayed in the packet list window.</p>
<dt>View:Name Resolution:Resolve Name</p>
<dd> Try to resolve a name for the currently selected item.</p>
<dt>View:Name Resolution:Enable for &#8230; Layer</p>
<dd> Enable or disable translation of addresses to names in the display.</p>
<dt>View:Colorize Packet List</p>
<dd> Enable or disable the coloring rules. Disabling will improve performance.</p>
<dt>View:Auto Scroll in Live Capture</p>
<dd> Enable or disable the automatic scrolling of the packet list while a live capture is in progress.</p>
<dt>View:Zoom In</p>
<dd>
<dt>View:Zoom Out</p>
<dd> Zoom into / out of the main window data (by changing the font size).</p>
<dt>View:Normal Size</p>
<dd> Reset the zoom factor of zoom in / zoom out back to normal font size.</p>
<dt>View:Resize All Columns</p>
<dd> Resize all columns to best fit the current packet display.</p>
<dt>View:Expand Subtrees</p>
<dd> Expands the currently selected item and it&#8217;s subtrees in the packet details.</p>
<dt>View:Expand All</p>
<dd>
<dt>View:Collapse All</p>
<dd> Expand / Collapse all branches of the packet details.</p>
<dt>View:Colorize Conversation</p>
<dd> Select color for a conversation.</p>
<dt>View:Reset Coloring 1-10</p>
<dd> Reset Color for a conversation.</p>
<dt>View:Coloring Rules</p>
<dd> Change the foreground and background colors of the packet information in the list of packets, based upon display filters. The list of display filters is applied to each packet sequentially. After the first display filter matches a packet, any additional display filters in the list are ignored. Therefore, if you are filtering on the existence of protocols, you should list the higher-level protocols first, and the lower-level protocols last.</p>
<dl>
<dt>
<dd>
<dl>
<dt>How Colorization Works</p>
<dd> Packets are colored according to a list of color filters. Each filter consists of a name, a filter expression and a coloration. A packet is colored according to the first filter that it matches. Color filter expressions use exactly the same syntax as display filter expressions. </p>
<p> When Wireshark starts, the color filters are loaded from:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> The user&#8217;s personal color filters file or, if that does not exist,</p>
<dt>2.</p>
<dd> The global color filters file.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If neither of these exist then the packets will not be colored.</dl>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>View:Show Packet In New Window</p>
<dd> Create a new window containing a packet details view and a hex dump window of the currently selected packet; this window will continue to display that packet&#8217;s details and data even if another packet is selected.</p>
<dt>View:Reload</p>
<dd> Reload a capture file. Same as <i>File:Close</i> and <i>File:Open</i> the same file again.</p>
<dt>Go:Back</p>
<dd> Go back in previously visited packets history.</p>
<dt>Go:Forward</p>
<dd> Go forward in previously visited packets history.</p>
<dt>Go:Go To Packet</p>
<dd> Go to a particular numbered packet.</p>
<dt>Go:Go To Corresponding Packet</p>
<dd> If a field in the packet details pane containing a packet number is selected, go to the packet number specified by that field. (This works only if the dissector that put that entry into the packet details put it into the details as a filterable field rather than just as text.) This can be used, for example, to go to the packet for the request corresponding to a reply, or the reply corresponding to a request, if that packet number has been put into the packet details.</p>
<dt>Go:Previous Packet</p>
<dd>
<dt>Go:Next Packet</p>
<dd>
<dt>Go:First Packet</p>
<dd>
<dt>Go:Last Packet</p>
<dd> Go to the previous / next / first / last packet in the capture.</p>
<dt>Go:Previous Packet In Conversation</p>
<dd>
<dt>Go:Next Packet In Conversation</p>
<dd> Go to the previous / next packet of the conversation (<font SIZE="-1">TCP, UDP</font> or <font SIZE="-1">IP</font>)</p>
<dt>Capture:Interfaces</p>
<dd> Shows a dialog box with all currently known interfaces and displaying the current network traffic amount. Capture sessions can be started from here. Beware: keeping this box open results in high system load!</p>
<dt>Capture:Options</p>
<dd> Initiate a live packet capture (see &#8220;Capture Options Dialog&#8221; below). If no filename is specified, a temporary file will be created to hold the capture. The location of the file can be chosen by setting your <font SIZE="-1">TMPDIR</font> environment variable before starting <code>Wireshark</code>. Otherwise, the default <font SIZE="-1">TMPDIR</font> location is system-dependent, but is likely either <i>/var/tmp</i> or <i>/tmp</i>.</p>
<dt>Capture:Start</p>
<dd> Start a live packet capture with the previously selected options. This won&#8217;t open the options dialog box, and can be convenient for repeatedly capturing with the same options.</p>
<dt>Capture:Stop</p>
<dd> Stop a running live capture.</p>
<dt>Capture:Restart</p>
<dd> While a live capture is running, stop it and restart with the same options again. This can be convenient to remove irrelevant packets, if no valuable packets were captured so far.</p>
<dt>Capture:Capture Filters</p>
<dd> Edit the saved list of capture filters, allowing filters to be added, changed, or deleted.</p>
<dt>Analyze:Display Filters</p>
<dd> Edit the saved list of display filters, allowing filters to be added, changed, or deleted.</p>
<dt>Analyze:Display Filter Macros</p>
<dd> Create shortcuts for complex macros</p>
<dt>Analyze:Apply as Filter</p>
<dd> Create a display filter based on the data currently highlighted in the packet details and apply the filter. </p>
<p> If that data is a field that can be tested in a display filter expression, the display filter will test that field; otherwise, the display filter will be based on the absolute offset within the packet. Therefore it could be unreliable if the packet contains protocols with variable-length headers, such as a source-routed token-ring packet. </p>
<p> The <code>Selected</code> option creates a display filter that tests for a match of the data; the <code>Not Selected</code> option creates a display filter that tests for a non-match of the data. The <code>And Selected</code>, <code>Or Selected</code>, <code>And Not Selected</code>, and <code>Or Not Selected</code> options add to the end of the display filter in the strip at the top (or bottom) an <font SIZE="-1">AND</font> or <font SIZE="-1">OR</font> operator followed by the new display filter expression.</p>
<dt>Analyze:Prepare a Filter</p>
<dd> Create a display filter based on the data currently highlighted in the packet details. The filter strip at the top (or bottom) is updated but it is not yet applied.</p>
<dt>Analyze:Enabled Protocols</p>
<dd> Allow protocol dissection to be enabled or disabled for a specific protocol. Individual protocols can be enabled or disabled by clicking on them in the list or by highlighting them and pressing the space bar. The entire list can be enabled, disabled, or inverted using the buttons below the list. </p>
<p> When a protocol is disabled, dissection in a particular packet stops when that protocol is reached, and Wireshark moves on to the next packet. Any higher-layer protocols that would otherwise have been processed will not be displayed. For example, disabling <font SIZE="-1">TCP</font> will prevent the dissection and display of <font SIZE="-1">TCP, HTTP, SMTP,</font> Telnet, and any other protocol exclusively dependent on <font SIZE="-1">TCP.</font> </p>
<p> The list of protocols can be saved, so that Wireshark will start up with the protocols in that list disabled.</p>
<dt>Analyze:Decode As</p>
<dd> If you have a packet selected, present a dialog allowing you to change which dissectors are used to decode this packet. The dialog has one panel each for the link layer, network layer and transport layer protocol/port numbers, and will allow each of these to be changed independently. For example, if the selected packet is a <font SIZE="-1">TCP</font> packet to port 12345, using this dialog you can instruct Wireshark to decode all packets to or from that <font SIZE="-1">TCP</font> port as <font SIZE="-1">HTTP</font> packets.</p>
<dt>Analyze:User Specified Decodes</p>
<dd> Create a new window showing whether any protocol <font SIZE="-1">ID</font> to dissector mappings have been changed by the user. This window also allows the user to reset all decodes to their default values.</p>
<dt>Analyze:Follow <font SIZE="-1">TCP</font> Stream</p>
<dd> If you have a <font SIZE="-1">TCP</font> packet selected, display the contents of the data stream for the <font SIZE="-1">TCP</font> connection to which that packet belongs, as text, in a separate window, and leave the list of packets in a filtered state, with only those packets that are part of that <font SIZE="-1">TCP</font> connection being displayed. You can revert to your old view by pressing <font SIZE="-1">ENTER</font> in the display filter text box, thereby invoking your old display filter (or resetting it back to no display filter). </p>
<p> The window in which the data stream is displayed lets you select:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> whether to display the entire conversation, or one or the other side of it;</p>
<dt>&bull;</p>
<dd> whether the data being displayed is to be treated as <font SIZE="-1">ASCII</font> or <font SIZE="-1">EBCDIC</font> text or as raw hex data;</dl>
</dl>
<dl>
<dt>
<dd>
<p> and lets you print what&#8217;s currently being displayed, using the same print options that are used for the <i>File:Print Packet</i> menu item, or save it as text to a file.</dl>
<dt>Analyze:Follow <font SIZE="-1">UDP</font> Stream</p>
<dd>
<dt>Analyze:Follow <font SIZE="-1">SSL</font> Stream</p>
<dd> (Similar to Analyze:Follow <font SIZE="-1">TCP</font> Stream)</p>
<dt>Analyze:Expert Info</p>
<dd>
<dt>Analyze:Expert Info Composite</p>
<dd> (Kind of) a log of anomalies found by Wireshark in a capture file.</p>
<dt>Analyze:Conversation Filter</p>
<dd>
<dt>Statistics:Summary</p>
<dd> Show summary information about the capture, including elapsed time, packet counts, byte counts, and the like. If a display filter is in effect, summary information will be shown about the capture and about the packets currently being displayed.</p>
<dt>Statistics:Protocol Hierarchy</p>
<dd> Show the number of packets, and the number of bytes in those packets, for each protocol in the trace. It organizes the protocols in the same hierarchy in which they were found in the trace. Besides counting the packets in which the protocol exists, a count is also made for packets in which the protocol is the last protocol in the stack. These last-protocol counts show you how many packets (and the byte count associated with those packets) <code>ended</code> in a particular protocol. In the table, they are listed under &#8220;End Packets&#8221; and &#8220;End Bytes&#8221;.</p>
<dt>Statistics:Conversations</p>
<dd> Lists of conversations; selectable by protocol. See Statistics:Conversation List below.</p>
<dt>Statistics:End Points</p>
<dd> List of End Point Addresses by protocol with packets/bytes/&#8230;. counts.</p>
<dt>Statistics:Packet Lengths</p>
<dd> Grouped counts of packet lengths (0-19 bytes, 20-39 bytes, &#8230;)</p>
<dt>Statistics:IO Graphs</p>
<dd> Open a window where up to 5 graphs in different colors can be displayed to indicate number of packets or number of bytes per second for all packets matching the specified filter. By default only one graph will be displayed showing number of packets per second. </p>
<p> The top part of the window contains the graphs and scales for the X and Y axis. If the graph is too long to fit inside the window there is a horizontal scrollbar below the drawing area that can scroll the graphs to the left or the right. The horizontal axis displays the time into the capture and the vertical axis will display the measured quantity at that time. </p>
<p> Below the drawing area and the scrollbar are the controls. On the bottom left there will be five similar sets of controls to control each individual graph such as &#8220;Display:&lt;button&gt;&#8221; which button will toggle that individual graph on/off. If &lt;button&gt; is ticked, the graph will be displayed. &#8220;Color:&lt;color&gt;&#8221; which is just a button to show which color will be used to draw that graph (color is only available in Gtk2 version) and finally &#8220;Filter:&lt;filter-text&gt;&#8221; which can be used to specify a display filter for that particular graph. </p>
<p> If filter-text is empty then all packets will be used to calculate the quantity for that graph. If filter-text is specified only those packets that match that display filter will be considered in the calculation of quantity. </p>
<p> To the right of the 5 graph controls there are four menus to control global aspects of the draw area and graphs. The &#8220;Unit:&#8221; menu is used to control what to measure; &#8220;packets/tick&#8221;, &#8220;bytes/tick&#8221; or &#8220;advanced&#8230;&#8221; </p>
<p> packets/tick will measure the number of packets matching the (if specified) display filter for the graph in each measurement interval. </p>
<p> bytes/tick will measure the total number of bytes in all packets matching the (if specified) display filter for the graph in each measurement interval. </p>
<p> advanced&#8230; see below </p>
<p> &#8220;Tick interval:&#8221; specifies what measurement intervals to use. The default is 1 second and means that the data will be counted over 1 second intervals. </p>
<p> &#8220;Pixels per tick:&#8221; specifies how many pixels wide each measurement interval will be in the drawing area. The default is 5 pixels per tick. </p>
<p> &#8220;Y-scale:&#8221; controls the max value for the y-axis. Default value is &#8220;auto&#8221; which means that <code>Wireshark</code> will try to adjust the maxvalue automatically. </p>
<p> &#8220;advanced&#8230;&#8221; If Unit:advanced&#8230; is selected the window will display two more controls for each of the five graphs. One control will be a menu where the type of calculation can be selected from <font SIZE="-1">SUM,COUNT,MAX,MIN,AVG</font> and <font SIZE="-1">LOAD,</font> and one control, textbox, where the name of a single display filter field can be specified. </p>
<p> The following restrictions apply to type and field combinations: </p>
<p> <font SIZE="-1">SUM:</font> available for all types of integers and will calculate the <font SIZE="-1">SUM</font> of all occurrences of this field in the measurement interval. Note that some field can occur multiple times in the same packet and then all instances will be summed up. Example: &#8216;tcp.len&#8217; which will count the amount of payload data transferred across <font SIZE="-1">TCP</font> in each interval. </p>
<p> <font SIZE="-1">COUNT:</font> available for all field types. This will <font SIZE="-1">COUNT</font> the number of times certain field occurs in each interval. Note that some fields may occur multiple times in each packet and if that is the case then each instance will be counted independently and <font SIZE="-1">COUNT</font> will be greater than the number of packets. </p>
<p> <font SIZE="-1">MAX:</font> available for all integer and relative time fields. This will calculate the max seen integer/time value seen for the field during the interval. Example: &#8216;smb.time&#8217; which will plot the maximum <font SIZE="-1">SMB</font> response time. </p>
<p> <font SIZE="-1">MIN:</font> available for all integer and relative time fields. This will calculate the min seen integer/time value seen for the field during the interval. Example: &#8216;smb.time&#8217; which will plot the minimum <font SIZE="-1">SMB</font> response time. </p>
<p> <font SIZE="-1">AVG:</font> available for all integer and relative time fields.This will calculate the average seen integer/time value seen for the field during the interval. Example: &#8216;smb.time&#8217; which will plot the average <font SIZE="-1">SMB</font> response time. </p>
<p> <font SIZE="-1">LOAD:</font> available only for relative time fields (response times). </p>
<p> Example of advanced: Display how <font SIZE="-1">NFS</font> response time <font SIZE="-1">MAX/MIN/AVG</font> changes over time: </p>
<p> Set first graph to: </p>
<pre>
   filter:nfs&amp;&amp;rpc.time
   Calc:MAX rpc.time
</pre>
<p> Set second graph to </p>
<pre>
   filter:nfs&amp;&amp;rpc.time
   Calc:AVG rpc.time
</pre>
<p> Set third graph to </p>
<pre>
   filter:nfs&amp;&amp;rpc.time
   Calc:MIN rpc.time
</pre>
<p> Example of advanced: Display how the average packet size from host a.b.c.d changes over time. </p>
<p> Set first graph to </p>
<pre>
   filter:ip.addr==a.b.c.d&amp;&amp;frame.pkt_len
   Calc:AVG frame.pkt_len
</pre>
<p> <font SIZE="-1">LOAD:</font> The <font SIZE="-1">LOAD</font> io-stat type is very different from anything you have ever seen before! While the response times themselves as plotted by <font SIZE="-1">MIN,MAX,AVG</font> are indications on the Server load (which affects the Server response time), the <font SIZE="-1">LOAD</font> measurement measures the Client <font SIZE="-1">LOAD.</font> What this measures is how much workload the client generates, i.e. how fast will the client issue new commands when the previous ones completed. i.e. the level of concurrency the client can maintain. The higher the number, the more and faster is the client issuing new commands. When the <font SIZE="-1">LOAD</font> goes down, it may be due to client load making the client slower in issuing new commands (there may be other reasons as well, maybe the client just doesn&#8217;t have any commands it wants to issue right then). </p>
<p> Load is measured in concurrency/number of overlapping i/o and the value 1000 means there is a constant load of one i/o. </p>
<p> In each tick interval the amount of overlap is measured. See the graph below containing three commands: Below the graph are the <font SIZE="-1">LOAD</font> values for each interval that would be calculated. </p>
<pre><code>
| | | | | | | | |
    | | | | | | | | |
    | | o == ==
    = * | | | | | |
      | | | | | | | | |
      | o == == == == * | o == == == == == == * | | |
      | | | | | | | | |
      -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- &gt; Time 500 1500 500 750 1000 500 0 0
</code></pre>
<dt>Statistics:Conversation List</p>
<dd> This option will open a new window that displays a list of all conversations between two endpoints. The list has one row for each unique conversation and displays total number of packets/bytes seen as well as number of packets/bytes in each direction. </p>
<p> By default the list is sorted according to the number of packets but by clicking on the column header; it is possible to re-sort the list in ascending or descending order by any column. </p>
<p> By first selecting a conversation by clicking on it and then using the right mouse button (on those platforms that have a right mouse button) wireshark will display a popup menu offering several different filter operations to apply to the capture. </p>
<p> These statistics windows can also be invoked from the Wireshark command line using the <code>-z conv</code> argument.</p>
<dt>Statistics:Service Response Time</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">AFP</font></p>
<dt>&bull;</p>
<dd> <font SIZE="-1">CAMEL</font></p>
<dt>&bull;</p>
<dd> DCE-RPC </p>
<p> Open a window to display Service Response Time statistics for an arbitrary DCE-RPC program interface and display <code>Procedure</code>, <code>Number of Calls</code>, <code>Minimum </code><font SIZE="-1"><code>SRT</code></font>, <code>Maximum </code><font SIZE="-1"><code>SRT</code></font> and <code>Average </code><font SIZE="-1"><code>SRT</code></font> for all procedures for that program/version. These windows opened will update in semi-real time to reflect changes when doing live captures or when reading new capture files into <code>Wireshark</code>. </p>
<p> This dialog will also allow an optional filter string to be used. If an optional filter string is used only such DCE-RPC request/response pairs that match that filter will be used to calculate the statistics. If no filter string is specified all request/response pairs will be used.</p>
<dt>&bull;</p>
<dd> Diameter</p>
<dt>&bull;</p>
<dd> Fibre Channel </p>
<p> Open a window to display Service Response Time statistics for Fibre Channel and display <font SIZE="-1"><code>FC</code></font><code> Type</code>, <code>Number of Calls</code>, <code>Minimum </code><font SIZE="-1"><code>SRT</code></font>, <code>Maximum </code><font SIZE="-1"><code>SRT</code></font> and <code>Average </code><font SIZE="-1"><code>SRT</code></font> for all <font SIZE="-1">FC</font> types. These windows opened will update in semi-real time to reflect changes when doing live captures or when reading new capture files into <code>Wireshark</code>. The Service Response Time is calculated as the time delta between the First packet of the exchange and the Last packet of the exchange. </p>
<p> This dialog will also allow an optional filter string to be used. If an optional filter string is used only such <font SIZE="-1">FC</font> first/last exchange pairs that match that filter will be used to calculate the statistics. If no filter string is specified all request/response pairs will be used.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">GTP</font></p>
<dt>&bull;</p>
<dd> H.225 <font SIZE="-1">RAS</font> </p>
<p> Collect requests/response <font SIZE="-1">SRT </font>(Service Response Time) data for ITU-T H.225 <font SIZE="-1">RAS.</font> Data collected is <code>number of calls</code> for each known ITU-T H.225 <font SIZE="-1">RAS</font> Message Type, <code>Minimum </code><font SIZE="-1"><code>SRT</code></font>, <code>Maximum </code><font SIZE="-1"><code>SRT</code></font>, <code>Average </code><font SIZE="-1"><code>SRT</code></font>, <code>Minimum in Packet</code>, and <code>Maximum in Packet</code>. You will also get the number of <code>Open Requests</code> (Unresponded Requests), <code>Discarded Responses</code> (Responses without matching request) and Duplicate Messages. These windows opened will update in semi-real time to reflect changes when doing live captures or when reading new capture files into <code>Wireshark</code>. </p>
<p> You can apply an optional filter string in a dialog box, before starting the calculation. The statistics will only be calculated on those calls matching that filter.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">LDAP</font></p>
<dt>&bull;</p>
<dd> <font SIZE="-1">MEGACO</font></p>
<dt>&bull;</p>
<dd> <font SIZE="-1">MGCP</font> </p>
<p> Collect requests/response <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">MGCP.</font> Data collected is <code>number of calls</code> for each known <font SIZE="-1">MGCP</font> Type, <code>Minimum </code><font SIZE="-1"><code>SRT</code></font>, <code>Maximum </code><font SIZE="-1"><code>SRT</code></font>, <code>Average </code><font SIZE="-1"><code>SRT</code></font>, <code>Minimum in Packet</code>, and <code>Maximum in Packet</code>. These windows opened will update in semi-real time to reflect changes when doing live captures or when reading new capture files into <code>Wireshark</code>. </p>
<p> You can apply an optional filter string in a dialog box, before starting the calculation. The statistics will only be calculated on those calls matching that filter.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">NCP</font></p>
<dt>&bull;</p>
<dd> ONC-RPC </p>
<p> Open a window to display statistics for an arbitrary ONC-RPC program interface and display <code>Procedure</code>, <code>Number of Calls</code>, <code>Minimum </code><font SIZE="-1"><code>SRT</code></font>, <code>Maximum </code><font SIZE="-1"><code>SRT</code></font> and <code>Average </code><font SIZE="-1"><code>SRT</code></font> for all procedures for that program/version. These windows opened will update in semi-real time to reflect changes when doing live captures or when reading new capture files into <code>Wireshark</code>. </p>
<p> This dialog will also allow an optional filter string to be used. If an optional filter string is used only such ONC-RPC request/response pairs that match that filter will be used to calculate the statistics. If no filter string is specified all request/response pairs will be used. </p>
<p> By first selecting a conversation by clicking on it and then using the right mouse button (on those platforms that have a right mouse button) wireshark will display a popup menu offering several different filter operations to apply to the capture.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">RADIUS</font></p>
<dt>&bull;</p>
<dd> <font SIZE="-1">SCSI</font></p>
<dt>&bull;</p>
<dd> <font SIZE="-1">SMB</font> </p>
<p> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">SMB. </font> Data collected is the number of calls for each <font SIZE="-1">SMB</font> command, MinSRT, MaxSRT and AvgSRT. </p>
<p> The data will be presented as separate tables for all normal <font SIZE="-1">SMB</font> commands, all Transaction2 commands and all <font SIZE="-1">NT</font> Transaction commands. Only those commands that are seen in the capture will have its stats displayed. Only the first command in a xAndX command chain will be used in the calculation. So for common SessionSetupAndX + TreeConnectAndX chains, only the SessionSetupAndX call will be used in the statistics. This is a flaw that might be fixed in the future. </p>
<p> You can apply an optional filter string in a dialog box, before starting the calculation. The stats will only be calculated on those calls matching that filter. </p>
<p> By first selecting a conversation by clicking on it and then using the right mouse button (on those platforms that have a right mouse button) wireshark will display a popup menu offering several different filter operations to apply to the capture.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">SMB2</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Statistics:BOOTP-DHCP</p>
<dd>
<dt>Statistics:Compare</p>
<dd> Compare two Capture Files</p>
<dt>Statistics:Flow Graph</p>
<dd> Flow Graph: General/TCP</p>
<dt>Statistics:HTTP</p>
<dd> <font SIZE="-1">HTTP</font> Load Distribution, Packet Counter &amp; Requests</p>
<dt>Statistics:IP Addresses</p>
<dd> Count/Rate/Percent by <font SIZE="-1">IP</font> Address</p>
<dt>Statistics:IP Destinations</p>
<dd> Count/Rate/Percent by <font SIZE="-1">IP</font> Address/protocol/port</p>
<dt>Statistics:IP Protocol Types</p>
<dd> Count/Rate/Percent by <font SIZE="-1">IP</font> Protocol Types</p>
<dt>Statistics:ONC-RPC Programs</p>
<dd> This dialog will open a window showing aggregated <font SIZE="-1">SRT</font> statistics for all ONC-RPC Programs/versions that exist in the capture file.</p>
<dt>Statistics:TCP Stream Graph</p>
<dd> Graphs: Round Trip; Throughput; Time-Sequence (Stevens); Time-Sequence (tcptrace)</p>
<dt>Statistics:UDP Multicast streams</p>
<dd> Multicast Streams Counts/Rates/&#8230; by Source/Destination Address/Port pairs</p>
<dt>Statistics:WLAN Traffic</p>
<dd> <font SIZE="-1">WLAN</font> Traffic Statistics</p>
<dt>Telephony:ITU-T H.225</p>
<dd> Count ITU-T H.225 messages and their reasons. In the first column you get a list of H.225 messages and H.225 message reasons, which occur in the current capture file. The number of occurrences of each message or reason will be displayed in the second column. This window opened will update in semi-real time to reflect changes when doing live captures or when reading new capture files into <code>Wireshark</code>. </p>
<p> You can apply an optional filter string in a dialog box, before starting the counter. The statistics will only be calculated on those calls matching that filter.</p>
<dt>Telephony:SIP</p>
<dd> Activate a counter for <font SIZE="-1">SIP</font> messages. You will get the number of occurrences of each <font SIZE="-1">SIP</font> Method and of each <font SIZE="-1">SIP</font> Status-Code. Additionally you also get the number of resent <font SIZE="-1">SIP</font> Messages (only for <font SIZE="-1">SIP</font> over <font SIZE="-1">UDP</font>). </p>
<p> This window opened will update in semi-real time to reflect changes when doing live captures or when reading new capture files into <code>Wireshark</code>. </p>
<p> You can apply an optional filter string in a dialog box, before starting the counter. The statistics will only be calculated on those calls matching that filter.</p>
<dt>Tools:Firewall <font SIZE="-1">ACL</font> Rules</p>
<dd>
<dt>Help:Contents</p>
<dd> Some help texts.</p>
<dt>Help:Supported Protocols</p>
<dd> List of supported protocols and display filter protocol fields.</p>
<dt>Help:Manual Pages</p>
<dd> Display locally installed <font SIZE="-1">HTML</font> versions of these manual pages in a web browser.</p>
<dt>Help:Wireshark Online</p>
<dd> Various links to online resources to be open in a web browser, like &lt;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&gt;.</p>
<dt>Help:About Wireshark</p>
<dd> See various information about Wireshark (see &#8220;About&#8221; dialog below), like the version, the folders used, the available plugins, &#8230;</dl>
<h3><font SIZE="-1">WINDOWS</font></h3>
<dl>
<dt>Main Window</p>
<dd> The main window contains the usual things like the menu, some toolbars, the main area and a statusbar. The main area is split into three panes, you can resize each pane using a &#8220;thumb&#8221; at the right end of each divider line. </p>
<p> The main window is much more flexible than before. The layout of the main window can be customized by the <i>Layout</i> page in the dialog box popped up by <i>Edit:Preferences</i>, the following will describe the layout with the default settings.</p>
<dl>
<dt>
<dd>
<dl>
<dt>Main Toolbar</p>
<dd> Some menu items are available for quick access here. There is no way to customize the items in the toolbar, however the toolbar can be hidden by <i>View:Main Toolbar</i>.</p>
<dt>Filter Toolbar</p>
<dd> A display filter can be entered into the filter toolbar. A filter for <font SIZE="-1">HTTP, HTTPS,</font> and <font SIZE="-1">DNS</font> traffic might look like this: </p>
<p>tcp.port == 80 || tcp.port == 443 || tcp.port == 53</p>
<p> Selecting the <i>Filter:</i> button lets you choose from a list of named filters that you can optionally save. Pressing the Return or Enter keys, or selecting the <i>Apply</i> button, will cause the filter to be applied to the current list of packets. Selecting the <i>Reset</i> button clears the display filter so that all packets are displayed (again). </p>
<p> There is no way to customize the items in the toolbar, however the toolbar can be hidden by <i>View:Filter Toolbar</i>.</p>
<dt>Packet List Pane</p>
<dd> The top pane contains the list of network packets that you can scroll through and select. By default, the packet number, packet timestamp, source and destination addresses, protocol, and description are displayed for each packet; the <i>Columns</i> page in the dialog box popped up by <i>Edit:Preferences</i> lets you change this (although, unfortunately, you currently have to save the preferences, and exit and restart Wireshark, for those changes to take effect). </p>
<p> If you click on the heading for a column, the display will be sorted by that column; clicking on the heading again will reverse the sort order for that column. </p>
<p> An effort is made to display information as high up the protocol stack as possible, e.g. <font SIZE="-1">IP</font> addresses are displayed for <font SIZE="-1">IP</font> packets, but the <font SIZE="-1">MAC</font> layer address is displayed for unknown packet types. </p>
<p> The right mouse button can be used to pop up a menu of operations. </p>
<p> The middle mouse button can be used to mark a packet.</p>
<dt>Packet Details Pane</p>
<dd> The middle pane contains a display of the details of the currently-selected packet. The display shows each field and its value in each protocol header in the stack. The right mouse button can be used to pop up a menu of operations.</p>
<dt>Packet Bytes Pane</p>
<dd> The lowest pane contains a hex and <font SIZE="-1">ASCII</font> dump of the actual packet data. Selecting a field in the packet details highlights the corresponding bytes in this section. </p>
<p> The right mouse button can be used to pop up a menu of operations.</p>
<dt>Statusbar</p>
<dd> The statusbar is divided into three parts, on the left some context dependent things are shown, like information about the loaded file, in the center the number of packets are displayed, and on the right the current configuration profile. </p>
<p> The statusbar can be hidden by <i>View:Statusbar</i>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Preferences</p>
<dd> The <i>Preferences</i> dialog lets you control various personal preferences for the behavior of <code>Wireshark</code>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>User Interface Preferences</p>
<dd> The <i>User Interface</i> page is used to modify small aspects of the <font SIZE="-1">GUI</font> to your own personal taste:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Selection Bars</p>
<dd> The selection bar in the packet list and packet details can have either a &#8220;browse&#8221; or &#8220;select&#8221; behavior. If the selection bar has a &#8220;browse&#8221; behavior, the arrow keys will move an outline of the selection bar, allowing you to browse the rest of the list or details without changing the selection until you press the space bar. If the selection bar has a &#8220;select&#8221; behavior, the arrow keys will move the selection bar and change the selection to the new item in the packet list or packet details.</p>
<dt>Save Window Position</p>
<dd> If this item is selected, the position of the main Wireshark window will be saved when Wireshark exits, and used when Wireshark is started again.</p>
<dt>Save Window Size</p>
<dd> If this item is selected, the size of the main Wireshark window will be saved when Wireshark exits, and used when Wireshark is started again.</p>
<dt>Save Window Maximized state</p>
<dd> If this item is selected the maximize state of the main Wireshark window will be saved when Wireshark exists, and used when Wireshark is started again.</p>
<dt>File Open Dialog Behavior</p>
<dd> This item allows the user to select how Wireshark handles the listing of the &#8220;File Open&#8221; Dialog when opening trace files. &#8220;Remember Last Directory&#8221; causes Wireshark to automatically position the dialog in the directory of the most recently opened file, even between launches of Wireshark. &#8220;Always Open in Directory&#8221; allows the user to define a persistent directory that the dialog will always default to.</p>
<dt>Directory</p>
<dd> Allows the user to specify a persistent File Open directory. Trailing slashes or backslashes will automatically be added.</p>
<dt>File Open Preview timeout</p>
<dd> This items allows the user to define how much time is spend reading the capture file to present preview data in the File Open dialog.</p>
<dt>Open Recent maximum list entries</p>
<dd> The File menu supports a recent file list. This items allows the user to specify how many files are kept track of in this list.</p>
<dt>Ask for unsaved capture files</p>
<dd> When closing a capture file or Wireshark itself if the file isn&#8217;t saved yet the user is presented the option to save the file when this item is set.</p>
<dt>Wrap during find</p>
<dd> This items determines the behavior when reaching the beginning or the end of a capture file. When set the search wraps around and continues, otherwise it stops.</p>
<dt>Settings dialogs show a save button</p>
<dd> This item determines if the various dialogs sport an explicit Save button or that save is implicit in <font SIZE="-1">OK /</font> Apply.</p>
<dt>Web browser command</p>
<dd> This entry specifies the command line to launch a web browser. It is used to access online content, like the Wiki and user guide. Use &#8216;%s&#8217; to place the request <font SIZE="-1">URL</font> in the command line.</p>
<dt>Display LEDs in the Expert Infos dialog tab labels</p>
<dd> This item determines if LED-like colored images are displayed in the Expert Infos dialog tab labels.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Layout Preferences</p>
<dd> The <i>Layout</i> page lets you specify the general layout of the main window. You can choose from six different layouts and fill the three panes with the contents you like.</p>
<dl>
<dt>
<dd>
<dl>
<dt>Scrollbars</p>
<dd> The vertical scrollbars in the three panes can be set to be either on the left or the right.</p>
<dt>Alternating row colors</p>
<dd>
<dt>Hex Display</p>
<dd> The highlight method in the hex dump display for the selected protocol item can be set to use either inverse video, or bold characters.</p>
<dt>Toolbar style</p>
<dd>
<dt>Filter toolbar placement</p>
<dd>
<dt>Custom window title</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Column Preferences</p>
<dd> The <i>Columns</i> page lets you specify the number, title, and format of each column in the packet list. </p>
<p> The <i>Column title</i> entry is used to specify the title of the column displayed at the top of the packet list. The type of data that the column displays can be specified using the <i>Column format</i> option menu. The row of buttons on the left perform the following actions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>New</p>
<dd> Adds a new column to the list.</p>
<dt>Delete</p>
<dd> Deletes the currently selected list item.</p>
<dt>Up / Down</p>
<dd> Moves the selected list item up or down one position.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Font Preferences</p>
<dd> The <i>Font</i> page lets you select the font to be used for most text.</p>
<dt>Color Preferences</p>
<dd> The <i>Colors</i> page can be used to change the color of the text displayed in the <font SIZE="-1">TCP</font> stream window and for marked packets. To change a color, simply select an attribute from the &#8220;Set:&#8221; menu and use the color selector to get the desired color. The new text colors are displayed as a sample text.</p>
<dt>Capture Preferences</p>
<dd> The <i>Capture</i> page lets you specify various parameters for capturing live packet data; these are used the first time a capture is started. </p>
<p> The <i>Interface:</i> combo box lets you specify the interface from which to capture packet data, or the name of a <font SIZE="-1">FIFO</font> from which to get the packet data. </p>
<p> The <i>Data link type:</i> option menu lets you, for some interfaces, select the data link header you want to see on the packets you capture. For example, in some OSes and with some versions of libpcap, you can choose, on an 802.11 interface, whether the packets should appear as Ethernet packets (with a fake Ethernet header) or as 802.11 packets. </p>
<p> The <i>Limit each packet to &#8230; bytes</i> check box lets you set the snapshot length to use when capturing live data; turn on the check box, and then set the number of bytes to use as the snapshot length. </p>
<p> The <i>Filter:</i> text entry lets you set a capture filter expression to be used when capturing. </p>
<p> If any of the environment variables <font SIZE="-1">SSH_CONNECTION, SSH_CLIENT, REMOTEHOST, DISPLAY,</font> or <font SIZE="-1">SESSIONNAME</font> are set, Wireshark will create a default capture filter that excludes traffic from the hosts and ports defined in those variables. </p>
<p> The <i>Capture packets in promiscuous mode</i> check box lets you specify whether to put the interface in promiscuous mode when capturing. </p>
<p> The <i>Update list of packets in real time</i> check box lets you specify that the display should be updated as packets are seen. </p>
<p> The <i>Automatic scrolling in live capture</i> check box lets you specify whether, in an &#8220;Update list of packets in real time&#8221; capture, the packet list pane should automatically scroll to show the most recently captured packets.</p>
<dt>Printing Preferences</p>
<dd> The radio buttons at the top of the <i>Printing</i> page allow you choose between printing packets with the <i>File:Print Packet</i> menu item as text or PostScript, and sending the output directly to a command or saving it to a file. The <i>Command:</i> text entry box, on UNIX-compatible systems, is the command to send files to (usually <code>lpr</code>), and the <i>File:</i> entry box lets you enter the name of the file you wish to save to. Additionally, you can select the <i>File:</i> button to browse the file system for a particular save file.</p>
<dt>Name Resolution Preferences</p>
<dd> The <i>Enable </i><font SIZE="-1"><i>MAC</i></font><i> name resolution</i>, <i>Enable network name resolution</i> and <i>Enable transport name resolution</i> check boxes let you specify whether <font SIZE="-1">MAC</font> addresses, network addresses, and transport-layer port numbers should be translated to names. </p>
<p> The <i>Enable concurrent </i><font SIZE="-1"><i>DNS</i></font><i> name resolution</i> allows Wireshark to send out multiple name resolution requests and not wait for the result before continuing dissection. This speeds up dissection with network name resolution but initially may miss resolutions. The number of concurrent requests can be set here as well. </p>
<p> <i></i><font SIZE="-1"><i>SMI</i></font><i> paths</i> </p>
<p> <i></i><font SIZE="-1"><i>SMI</i></font><i> modules</i></p>
<dt><font SIZE="-1">RTP</font> Player Preferences</p>
<dd> This page allows you to select the number of channels visible in the <font SIZE="-1">RTP</font> player window. It determines the height of the window, more channels are possible and visible by means of a scroll bar.</p>
<dt>Protocol Preferences</p>
<dd> There are also pages for various protocols that Wireshark dissects, controlling the way Wireshark handles those protocols.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Edit Capture Filter List</p>
<dd>
<dt>Edit Display Filter List</p>
<dd>
<dt>Capture Filter</p>
<dd>
<dt>Display Filter</p>
<dd>
<dt>Read Filter</p>
<dd>
<dt>Search Filter</p>
<dd> The <i>Edit Capture Filter List</i> dialog lets you create, modify, and delete capture filters, and the <i>Edit Display Filter List</i> dialog lets you create, modify, and delete display filters. </p>
<p> The <i>Capture Filter</i> dialog lets you do all of the editing operations listed, and also lets you choose or construct a filter to be used when capturing packets. </p>
<p> The <i>Display Filter</i> dialog lets you do all of the editing operations listed, and also lets you choose or construct a filter to be used to filter the current capture being viewed. </p>
<p> The <i>Read Filter</i> dialog lets you do all of the editing operations listed, and also lets you choose or construct a filter to be used to as a read filter for a capture file you open. </p>
<p> The <i>Search Filter</i> dialog lets you do all of the editing operations listed, and also lets you choose or construct a filter expression to be used in a find operation. </p>
<p> In all of those dialogs, the <i>Filter name</i> entry specifies a descriptive name for a filter, e.g. <code>Web and </code><font SIZE="-1"><code>DNS</code></font><code> traffic</code>. The <i>Filter string</i> entry is the text that actually describes the filtering action to take, as described above.The dialog buttons perform the following actions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>New</p>
<dd> If there is text in the two entry boxes, creates a new associated list item.</p>
<dt>Edit</p>
<dd> Modifies the currently selected list item to match what&#8217;s in the entry boxes.</p>
<dt>Delete</p>
<dd> Deletes the currently selected list item.</p>
<dt>Add Expression&#8230;</p>
<dd> For display filter expressions, pops up a dialog box to allow you to construct a filter expression to test a particular field; it offers lists of field names, and, when appropriate, lists from which to select tests to perform on the field and values with which to compare it. In that dialog box, the <font SIZE="-1">OK</font> button will cause the filter expression you constructed to be entered into the <i>Filter string</i> entry at the current cursor position.</p>
<dt><font SIZE="-1">OK</font></p>
<dd> In the <i>Capture Filter</i> dialog, closes the dialog box and makes the filter in the <i>Filter string</i> entry the filter in the <i>Capture Preferences</i> dialog. In the <i>Display Filter</i> dialog, closes the dialog box and makes the filter in the <i>Filter string</i> entry the current display filter, and applies it to the current capture. In the <i>Read Filter</i> dialog, closes the dialog box and makes the filter in the <i>Filter string</i> entry the filter in the <i>Open Capture File</i> dialog. In the <i>Search Filter</i> dialog, closes the dialog box and makes the filter in the <i>Filter string</i> entry the filter in the <i>Find Packet</i> dialog.</p>
<dt>Apply</p>
<dd> Makes the filter in the <i>Filter string</i> entry the current display filter, and applies it to the current capture.</p>
<dt>Save</p>
<dd> If the list of filters being edited is the list of capture filters, saves the current filter list to the personal capture filters file, and if the list of filters being edited is the list of display filters, saves the current filter list to the personal display filters file.</p>
<dt>Close</p>
<dd> Closes the dialog without doing anything with the filter in the <i>Filter string</i> entry.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>The Color Filters Dialog</p>
<dd> This dialog displays a list of color filters and allows it to be modified.</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">THE FILTER LIST</font></p>
<dd> Single rows may be selected by clicking. Multiple rows may be selected by using the ctrl and shift keys in combination with the mouse button.</p>
<dt><font SIZE="-1">NEW</font></p>
<dd> Adds a new filter at the bottom of the list and opens the Edit Color Filter dialog box. You will have to alter the filter expression at least before the filter will be accepted. The format of color filter expressions is identical to that of display filters. The new filter is selected, so it may immediately be moved up and down, deleted or edited. To avoid confusion all filters are unselected before the new filter is created.</p>
<dt><font SIZE="-1">EDIT</font></p>
<dd> Opens the Edit Color Filter dialog box for the selected filter. (If this button is disabled you may have more than one filter selected, making it ambiguous which is to be edited.)</p>
<dt><font SIZE="-1">ENABLE</font></p>
<dd> Enables the selected color filter(s).</p>
<dt><font SIZE="-1">DISABLE</font></p>
<dd> Disables the selected color filter(s).</p>
<dt><font SIZE="-1">DELETE</font></p>
<dd> Deletes the selected color filter(s).</p>
<dt><font SIZE="-1">EXPORT</font></p>
<dd> Allows you to choose a file in which to save the current list of color filters. You may also choose to save only the selected filters. A button is provided to save the filters in the global color filters file (you must have sufficient permissions to write this file, of course).</p>
<dt><font SIZE="-1">IMPORT</font></p>
<dd> Allows you to choose a file containing color filters which are then added to the bottom of the current list. All the added filters are selected, so they may be moved to the correct position in the list as a group. To avoid confusion, all filters are unselected before the new filters are imported. A button is provided to load the filters from the global color filters file.</p>
<dt><font SIZE="-1">CLEAR</font></p>
<dd> Deletes your personal color filters file, reloads the global color filters file, if any, and closes the dialog.</p>
<dt><font SIZE="-1">UP</font></p>
<dd> Moves the selected filter(s) up the list, making it more likely that they will be used to color packets.</p>
<dt><font SIZE="-1">DOWN</font></p>
<dd> Moves the selected filter(s) down the list, making it less likely that they will be used to color packets.</p>
<dt><font SIZE="-1">OK</font></p>
<dd> Closes the dialog and uses the color filters as they stand.</p>
<dt><font SIZE="-1">APPLY</font></p>
<dd> Colors the packets according to the current list of color filters, but does not close the dialog.</p>
<dt><font SIZE="-1">SAVE</font></p>
<dd> Saves the current list of color filters in your personal color filters file. Unless you do this they will not be used the next time you start Wireshark.</p>
<dt><font SIZE="-1">CLOSE</font></p>
<dd> Closes the dialog without changing the coloration of the packets. Note that changes you have made to the current list of color filters are not undone.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Capture Options Dialog</p>
<dd> The <i>Capture Options Dialog</i> lets you specify various parameters for capturing live packet data. </p>
<p> The <i>Interface:</i> field lets you specify the interface from which to capture packet data or a command from which to get the packet data via a pipe. </p>
<p> The <i>Link layer header type:</i> field lets you specify the interfaces link layer header type. This field is usually disabled, as most interface have only one header type. </p>
<p> The <i>Capture packets in promiscuous mode</i> check box lets you specify whether the interface should be put into promiscuous mode when capturing. </p>
<p> The <i>Limit each packet to &#8230; bytes</i> check box and field lets you specify a maximum number of bytes per packet to capture and save; if the check box is not checked, the limit will be 65535 bytes. </p>
<p> The <i>Capture Filter:</i> entry lets you specify the capture filter using a tcpdump-style filter string as described above. </p>
<p> The <i>File:</i> entry lets you specify the file into which captured packets should be saved, as in the <i>Printer Options</i> dialog above. If not specified, the captured packets will be saved in a temporary file; you can save those packets to a file with the <i>File:Save As</i> menu item. </p>
<p> The <i>Use multiple files</i> check box lets you specify that the capture should be done in &#8220;multiple files&#8221; mode. This option is disabled, if the <i>Update list of packets in real time</i> option is checked. </p>
<p> The <i>Next file every &#8230; megabyte(s)</i> check box and fields lets you specify that a switch to a next file should be done if the specified filesize is reached. You can also select the appropriate unit, but beware that the filesize has a maximum of 2 GiB. The check box is forced to be checked, as &#8220;multiple files&#8221; mode requires a file size to be specified. </p>
<p> The <i>Next file every &#8230; minute(s)</i> check box and fields lets you specify that the switch to a next file should be done after the specified time has elapsed, even if the specified capture size is not reached. </p>
<p> The <i>Ring buffer with &#8230; files</i> field lets you specify the number of files of a ring buffer. This feature will capture into the first file again, after the specified number of files have been used. </p>
<p> The <i>Stop capture after &#8230; files</i> field lets you specify the number of capture files used, until the capture is stopped. </p>
<p> The <i>Stop capture after &#8230; packet(s)</i> check box and field let you specify that Wireshark should stop capturing after having captured some number of packets; if the check box is not checked, Wireshark will not stop capturing at some fixed number of captured packets. </p>
<p> The <i>Stop capture after &#8230; megabyte(s)</i> check box and field lets you specify that Wireshark should stop capturing after the file to which captured packets are being saved grows as large as or larger than some specified number of megabytes. If the check box is not checked, Wireshark will not stop capturing at some capture file size (although the operating system on which Wireshark is running, or the available disk space, may still limit the maximum size of a capture file). This option is disabled, if &#8220;multiple files&#8221; mode is used, </p>
<p> The <i>Stop capture after &#8230; second(s)</i> check box and field let you specify that Wireshark should stop capturing after it has been capturing for some number of seconds; if the check box is not checked, Wireshark will not stop capturing after some fixed time has elapsed. </p>
<p> The <i>Update list of packets in real time</i> check box lets you specify whether the display should be updated as packets are captured and, if you specify that, the <i>Automatic scrolling in live capture</i> check box lets you specify the packet list pane should automatically scroll to show the most recently captured packets as new packets arrive. </p>
<p> The <i>Enable </i><font SIZE="-1"><i>MAC</i></font><i> name resolution</i>, <i>Enable network name resolution</i> and <i>Enable transport name resolution</i> check boxes let you specify whether <font SIZE="-1">MAC</font> addresses, network addresses, and transport-layer port numbers should be translated to names.</p>
<dt>About</p>
<dd> The <i>About</i> dialog lets you view various information about Wireshark.</p>
<dt>About:Wireshark</p>
<dd> The <i>Wireshark</i> page lets you view general information about Wireshark, like the installed version, licensing information and such.</p>
<dt>About:Authors</p>
<dd> The <i>Authors</i> page shows the author and all contributors.</p>
<dt>About:Folders</p>
<dd> The <i>Folders</i> page lets you view the directory names where Wireshark is searching it&#8217;s various configuration and other files.</p>
<dt>About:Plugins</p>
<dd> The <i>Plugins</i> page lets you view the dissector plugin modules available on your system. </p>
<p> The <i>Plugins List</i> shows the name and version of each dissector plugin module found on your system. </p>
<p> On Unix-compatible systems, the plugins are looked for in the following directories: the <i>lib/wireshark/plugins/$VERSION</i> directory under the main installation directory (for example, <i>/usr/local/lib/wireshark/plugins/$VERSION</i>), and then <i></i>$HOME<i>/.wireshark/plugins</i>. </p>
<p> On Windows systems, the plugins are looked for in the following directories: <i>plugins\$VERSION</i> directory under the main installation directory (for example, <i>C:\Program Files\Wireshark\plugins\$VERSION</i>), and then <i></i>%APPDATA<i>%\Wireshark\plugins\$VERSION</i> (or, if <tt>%APPDATA</tt>% isn&#8217;t defined, <i></i>%USERPROFILE<i>%\Application Data\Wireshark\plugins\$VERSION</i>). </p>
<p> <tt>$VERSION</tt> is the version number of the plugin interface, which is typically the version number of Wireshark. Note that a dissector plugin module may support more than one protocol; there is not necessarily a one-to-one correspondence between dissector plugin modules and protocols. Protocols supported by a dissector plugin module are enabled and disabled using the <i>Edit:Protocols</i> dialog box, just as protocols built into Wireshark are.</dl>
<h2>CAPTURE FILTER SYNTAX</h2>
<p> See the manual page of <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or, if that doesn&#8217;t exist, <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8), or, if that doesn&#8217;t exist, &lt;<a rel="nofollow" href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a>&gt;.</p>
<h2>DISPLAY FILTER SYNTAX</h2>
<p> For a complete table of protocol and protocol fields that are filterable in <code>Wireshark</code> see the <i><a href="/docs/linux/man/4-wireshark-filter/">wireshark-filter</a></i>(4) manual page.</p>
<h2>FILES</h2>
<p> These files contains various <code>Wireshark</code> configuration settings.</p>
<dl>
<dt>Preferences</p>
<dd> The <i>preferences</i> files contain global (system-wide) and personal preference settings. If the system-wide preference file exists, it is read first, overriding the default settings. If the personal preferences file exists, it is read next, overriding any previous values. Note: If the command line flag <code>-o</code> is used (possibly more than once), it will in turn override values from the preferences files. </p>
<p> The preferences settings are in the form <i>prefname</i><code>:</code><i>value</i>, one per line, where <i>prefname</i> is the name of the preference and <i>value</i> is the value to which it should be set; white space is allowed between <code>:</code> and <i>value</i>. A preference setting can be continued on subsequent lines by indenting the continuation lines with white space. A <code>#</code> character starts a comment that runs to the end of the line: </p>
<pre>
  # Vertical scrollbars should be on right side?
  # TRUE or FALSE (case-insensitive).
  gui.scrollbar_on_right: TRUE
</pre>
<p> The global preferences file is looked for in the <i>wireshark</i> directory under the <i>share</i> subdirectory of the main installation directory (for example, <i>/usr/local/share/wireshark/preferences</i>) on UNIX-compatible systems, and in the main installation directory (for example, <i>C:\Program Files\Wireshark\preferences</i>) on Windows systems. </p>
<p> The personal preferences file is looked for in <i></i>$HOME<i>/.wireshark/preferences</i> on UNIX-compatible systems and <i></i>%APPDATA<i>%\Wireshark\preferences</i> (or, if <tt>%APPDATA</tt>% isn&#8217;t defined, <i></i>%USERPROFILE<i>%\Application Data\Wireshark\preferences</i>) on Windows systems. </p>
<p> Note: Whenever the preferences are saved by using the <i>Save</i> button in the <i>Edit:Preferences</i> dialog box, your personal preferences file will be overwritten with the new settings, destroying any comments and unknown/obsolete settings that were in the file.</p>
<dt>Recent</p>
<dd> The <i>recent</i> file contains personal settings (mostly <font SIZE="-1">GUI</font> related) such as the current <code>Wireshark</code> window size. The file is saved at program exit and read in at program start automatically. Note: The command line flag <code>-o</code> may be used to override settings from this file. </p>
<p> The settings in this file have the same format as in the <i>preferences</i> files, and the same directory as for the personal preferences file is used. </p>
<p> Note: Whenever Wireshark is closed, your recent file will be overwritten with the new settings, destroying any comments and unknown/obsolete settings that were in the file.</p>
<dt>Disabled (Enabled) Protocols</p>
<dd> The <i>disabled_protos</i> files contain system-wide and personal lists of protocols that have been disabled, so that their dissectors are never called. The files contain protocol names, one per line, where the protocol name is the same name that would be used in a display filter for the protocol: </p>
<pre>
  http
  tcp     # a comment
</pre>
<p> If a protocol is listed in the global <i>disabled_protos</i> file, it is not displayed in the <i>Analyze:Enabled Protocols</i> dialog box, and so cannot be enabled by the user. </p>
<p> The global <i>disabled_protos</i> file uses the same directory as the global preferences file. </p>
<p> The personal <i>disabled_protos</i> file uses the same directory as the personal preferences file. </p>
<p> Note: Whenever the disabled protocols list is saved by using the <i>Save</i> button in the <i>Analyze:Enabled Protocols</i> dialog box, your personal disabled protocols file will be overwritten with the new settings, destroying any comments that were in the file.</p>
<dt>Name Resolution (hosts)</p>
<dd> If the personal <i>hosts</i> file exists, it is used to resolve IPv4 and IPv6 addresses before any other attempts are made to resolve them. The file has the standard <i>hosts</i> file syntax; each line contains one <font SIZE="-1">IP</font> address and name, separated by whitespace. The same directory as for the personal preferences file is used. </p>
<p> Capture filter name resolution is handled by libpcap on UNIX-compatible systems and WinPcap on Windows. As such the Wireshark personal <i>hosts</i> file will not be consulted for capture filter name resolution.</p>
<dt>Name Resolution (ethers)</p>
<dd> The <i>ethers</i> files are consulted to correlate 6-byte hardware addresses to names. First the personal <i>ethers</i> file is tried and if an address is not found there the global <i>ethers</i> file is tried next. </p>
<p> Each line contains one hardware address and name, separated by whitespace. The digits of the hardware address are separated by colons (:), dashes (-) or periods (.). The same separator character must be used consistently in an address. The following three lines are valid lines of an <i>ethers</i> file: </p>
<pre>
  ff:ff:ff:ff:ff:ff          Broadcast
  c0-00-ff-ff-ff-ff          TR_broadcast
  00.00.00.00.00.00          Zero_broadcast
</pre>
<p> The global <i>ethers</i> file is looked for in the <i>/etc</i> directory on UNIX-compatible systems, and in the main installation directory (for example, <i>C:\Program Files\Wireshark</i>) on Windows systems. </p>
<p> The personal <i>ethers</i> file is looked for in the same directory as the personal preferences file. </p>
<p> Capture filter name resolution is handled by libpcap on UNIX-compatible systems and WinPcap on Windows. As such the Wireshark personal <i>ethers</i> file will not be consulted for capture filter name resolution.</p>
<dt>Name Resolution (manuf)</p>
<dd> The <i>manuf</i> file is used to match the 3-byte vendor portion of a 6-byte hardware address with the manufacturer&#8217;s name; it can also contain well-known <font SIZE="-1">MAC</font> addresses and address ranges specified with a netmask. The format of the file is the same as the <i>ethers</i> files, except that entries such as: </p>
<pre>
  00:00:0C      Cisco
</pre>
<p> can be provided, with the 3-byte <font SIZE="-1">OUI</font> and the name for a vendor, and entries such as: </p>
<pre>
  00-00-0C-07-AC/40     All-HSRP-routers
</pre>
<p> can be specified, with a <font SIZE="-1">MAC</font> address and a mask indicating how many bits of the address must match. The above entry, for example, has 40 significant bits, or 5 bytes, and would match addresses from 00-00-0C-07-AC-00 through 00-00-0C-07-AC-FF. The mask need not be a multiple of 8. </p>
<p> The <i>manuf</i> file is looked for in the same directory as the global preferences file.</p>
<dt>Name Resolution (ipxnets)</p>
<dd> The <i>ipxnets</i> files are used to correlate 4-byte <font SIZE="-1">IPX</font> network numbers to names. First the global <i>ipxnets</i> file is tried and if that address is not found there the personal one is tried next. </p>
<p> The format is the same as the <i>ethers</i> file, except that each address is four bytes instead of six. Additionally, the address can be represented as a single hexadecimal number, as is more common in the <font SIZE="-1">IPX</font> world, rather than four hex octets. For example, these four lines are valid lines of an <i>ipxnets</i> file: </p>
<pre>
  C0.A8.2C.00              HR
  c0-a8-1c-00              CEO
  00:00:BE:EF              IT_Server1
  110f                     FileServer3
</pre>
<p> The global <i>ipxnets</i> file is looked for in the <i>/etc</i> directory on UNIX-compatible systems, and in the main installation directory (for example, <i>C:\Program Files\Wireshark</i>) on Windows systems. </p>
<p> The personal <i>ipxnets</i> file is looked for in the same directory as the personal preferences file.</p>
<dt>Capture Filters</p>
<dd> The <i>cfilters</i> files contain system-wide and personal capture filters. Each line contains one filter, starting with the string displayed in the dialog box in quotation marks, followed by the filter string itself: </p>
<pre>
  &quot;HTTP&quot; port 80
  &quot;DCERPC&quot; port 135
</pre>
<p> The global <i>cfilters</i> file uses the same directory as the global preferences file. </p>
<p> The personal <i>cfilters</i> file uses the same directory as the personal preferences file. It is written through the Capture:Capture Filters dialog. </p>
<p> If the global <i>cfilters</i> file exists, it is used only if the personal <i>cfilters</i> file does not exist; global and personal capture filters are not merged.</p>
<dt>Display Filters</p>
<dd> The <i>dfilters</i> files contain system-wide and personal display filters. Each line contains one filter, starting with the string displayed in the dialog box in quotation marks, followed by the filter string itself: </p>
<pre>
  &quot;HTTP&quot; http
  &quot;DCERPC&quot; dcerpc
</pre>
<p> The global <i>dfilters</i> file uses the same directory as the global preferences file. </p>
<p> The personal <i>dfilters</i> file uses the same directory as the personal preferences file. It is written through the Analyze:Display Filters dialog. </p>
<p> If the global <i>dfilters</i> file exists, it is used only if the personal <i>dfilters</i> file does not exist; global and personal display filters are not merged.</p>
<dt>Color Filters (Coloring Rules)</p>
<dd> The <i>colorfilters</i> files contain system-wide and personal color filters. Each line contains one filter, starting with the string displayed in the dialog box, followed by the corresponding display filter. Then the background and foreground colors are appended: </p>
<p>#a comment<br />
@tcp @tcp @[ 59345, 58980, 65534 ][0, 0, 0]<br />
    @udp @udp @[ 28834, 57427, 65533 ][0, 0, 0]</p>
<p> The global <i>colorfilters</i> file uses the same directory as the global preferences file. </p>
<p> The personal <i>colorfilters</i> file uses the same directory as the personal preferences file. It is written through the View:Coloring Rules dialog. </p>
<p> If the global <i>colorfilters</i> file exists, it is used only if the personal <i>colorfilters</i> file does not exist; global and personal color filters are not merged.</p>
<dt><font SIZE="-1">GTK</font> rc files</p>
<dd> The <i>gtkrc</i> files contain system-wide and personal <font SIZE="-1">GTK</font> theme settings. </p>
<p> The global <i>gtkrc</i> file uses the same directory as the global preferences file. </p>
<p> The personal <i>gtkrc</i> file uses the same directory as the personal preferences file.</p>
<dt>Plugins</p>
<dd> See above in the description of the About:Plugins page.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><font SIZE="-1">WIRESHARK_DEBUG_EP_NO_CHUNKS</font></p>
<dd> Normally per-packet memory is allocated in large &#8220;chunks.&#8221; This behavior doesn&#8217;t work well with debugging tools such as Valgrind or ElectricFence. Export this environment variable to force individual allocations. Note: disabling chunks also disables canaries (see below).</p>
<dt><font SIZE="-1">WIRESHARK_DEBUG_SE_NO_CHUNKS</font></p>
<dd> Normally per-file memory is allocated in large &#8220;chunks.&#8221; This behavior doesn&#8217;t work well with debugging tools such as Valgrind or ElectricFence. Export this environment variable to force individual allocations. Note: disabling chunks also disables canaries (see below).</p>
<dt><font SIZE="-1">WIRESHARK_DEBUG_EP_NO_CANARY</font></p>
<dd> Normally per-packet memory allocations are separated by &#8220;canaries&#8221; which allow detection of memory overruns. This comes at the expense of some extra memory usage. Exporting this environment variable disables these canaries.</p>
<dt><font SIZE="-1">WIRESHARK_DEBUG_SE_USE_CANARY</font></p>
<dd> Exporting this environment variable causes per-file memory allocations to be protected with &#8220;canaries&#8221; which allow for detection of memory overruns. This comes at the expense of significant extra memory usage.</p>
<dt><font SIZE="-1">WIRESHARK_DEBUG_SCRUB_MEMORY</font></p>
<dd> If this environment variable is set, the contents of per-packet and per-file memory is initialized to 0xBADDCAFE when the memory is allocated and is reset to 0xDEADBEEF when the memory is freed. This functionality is useful mainly to developers looking for bugs in the way memory is handled.</p>
<dt><font SIZE="-1">WIRESHARK_DEBUG_WMEM_OVERRIDE</font></p>
<dd> Setting this environment variable forces the wmem framework to use the specified allocator backend for *all* allocations, regardless of which backend is normally specified by the code. This is mainly useful to developers when testing or debugging. See <i></i><font SIZE="-1"><i>README</i></font><i>.wmem</i> in the source distribution for details.</p>
<dt><font SIZE="-1">WIRESHARK_RUN_FROM_BUILD_DIRECTORY</font></p>
<dd> This environment variable causes the plugins and other data files to be loaded from the build directory (where the program was compiled) rather than from the standard locations. It has no effect when the program in question is running with root (or setuid) permissions on *NIX.</p>
<dt><font SIZE="-1">WIRESHARK_DATA_DIR</font></p>
<dd> This environment variable causes the various data files to be loaded from a directory other than the standard locations. It has no effect when the program in question is running with root (or setuid) permissions on *NIX.</p>
<dt><font SIZE="-1">WIRESHARK_PYTHON_DIR</font></p>
<dd> This environment variable points to an alternate location for Python. It has no effect when the program in question is running with root (or setuid) permissions on *NIX.</p>
<dt><font SIZE="-1">ERF_RECORDS_TO_CHECK</font></p>
<dd> This environment variable controls the number of <font SIZE="-1">ERF</font> records checked when deciding if a file really is in the <font SIZE="-1">ERF</font> format. Setting this environment variable a number higher than the default (20) would make false positives less likely.</p>
<dt><font SIZE="-1">IPFIX_RECORDS_TO_CHECK</font></p>
<dd> This environment variable controls the number of <font SIZE="-1">IPFIX</font> records checked when deciding if a file really is in the <font SIZE="-1">IPFIX</font> format. Setting this environment variable a number higher than the default (20) would make false positives less likely.</p>
<dt><font SIZE="-1">WIRESHARK_ABORT_ON_DISSECTOR_BUG</font></p>
<dd> If this environment variable is set, <code>Wireshark</code> will call <i><a href="/docs/linux/man/3-abort/">abort</a></i>(3) when a dissector bug is encountered. <i><a href="/docs/linux/man/3-abort/">abort</a></i>(3) will cause the program to exit abnormally; if you are running <code>Wireshark</code> in a debugger, it should halt in the debugger and allow inspection of the process, and, if you are not running it in a debugger, it will, on some OSes, assuming your environment is configured correctly, generate a core dump file. This can be useful to developers attempting to troubleshoot a problem with a protocol dissector.</p>
<dt><font SIZE="-1">WIRESHARK_EP_VERIFY_POINTERS</font></p>
<dd> This environment variable, if set, causes certain uses of pointers to be audited to ensure they do not point to memory that is deallocated after each packet has been fully dissected. This can be useful to developers writing or auditing code.</p>
<dt><font SIZE="-1">WIRESHARK_SE_VERIFY_POINTERS</font></p>
<dd> This environment variable, if set, causes certain uses of pointers to be audited to ensure they do not point to memory that is deallocated after when a capture file is closed. This can be useful to developers writing or auditing code.</p>
<dt><font SIZE="-1">WIRESHARK_QUIT_AFTER_CAPTURE</font></p>
<dd> Cause <code>Wireshark</code> to exit after the end of the capture session. This doesn&#8217;t automatically start a capture; you must still use <code>-k</code> to do that. You must also specify an autostop condition, e.g. <code>-c</code> or <code>-a duration:&#8230;</code>. This means that you will not be able to see the results of the capture after it stops; it&#8217;s primarily useful for testing.</p>
<dt><font SIZE="-1">WIRESHARK_ABORT_ON_OUT_OF_MEMORY</font></p>
<dd> This environment variable, if present, causes <i><a href="/docs/linux/man/3-abort/">abort</a></i>(3) to be called if certain out-of-memory conditions (which normally result in an exception and an explanatory error message) are experienced. This can be useful to developers debugging out-of-memory conditions.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/4-wireshark-filter/">wireshark-filter</a></i>(4), <i><a href="/docs/linux/man/1-tshark/">tshark</a></i>(1), <i><a href="/docs/linux/man/1-editcap/">editcap</a></i>(1), <i><a href="/docs/linux/man/3-pcap/">pcap</a></i>(3), <i><a href="/docs/linux/man/1-dumpcap/">dumpcap</a></i>(1), <i><a href="/docs/linux/man/1-mergecap/">mergecap</a></i>(1), <i><a href="/docs/linux/man/1-text2pcap/">text2pcap</a></i>(1), <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8)</p>
<h2>NOTES</h2>
<p> The latest version of <code>Wireshark</code> can be found at &lt;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&gt;. </p>
<p> <font SIZE="-1">HTML</font> versions of the Wireshark project man pages are available at: &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages">http://www.wireshark.org/docs/man-pages</a>&gt;.</p>
<h2>AUTHORS</h2>
<pre><code>
Original Author-- -- -- -- -- -- --Gerald Combs&lt;gerald[AT] wireshark.org&gt;
            Contributors-- -- -- -- -- --Gilbert Ramirez&lt;gram[AT] alumni.rice.edu&gt;
                Thomas Bottom&lt;tom.bottom[AT] labxtechnologies.com&gt;
                    Chris Pane&lt;chris.pane[AT] labxtechnologies.com&gt;
                        Hannes R.Boehm&lt;hannes[AT] boehm.org&gt;
                            Mike Hall&lt;mike[AT] hallzone.net&gt;
                                Bobo Rajec&lt;bobo[AT] bsp - consulting.sk&gt;
                                    Laurent Deniel&lt;laurent.deniel[AT] free.fr&gt;
                                        Don Lafontaine&lt;lafont02[AT] cn.ca&gt;
                                            Guy Harris&lt;guy[AT] alum.mit.edu&gt;
                                                Simon Wilkinson&lt;sxw[AT] dcs.ed.ac.uk&gt;
                                                    Jo.rg Mayer&lt;jmayer[AT] loplof.de&gt;
                                                        Martin Maciaszek&lt;fastjack[AT] i - s - o.net&gt;
                                                            Didier Jorand&lt;Didier.Jorand[AT] alcatel.fr&gt;
                                                                Jun -
        ichiro itojun Hagino&lt;itojun[AT] itojun.org&gt;
            Richard Sharpe&lt;sharpe[AT] ns.aus.com&gt;
                John McDermott&lt;jjm[AT] jkintl.com&gt;
                    Jeff Jahr&lt;jjahr[AT] shastanets.com&gt;
                        Brad Robel - Forrest&lt;bradr[AT] watchguard.com&gt; Ashok Narayanan&lt;ashokn[AT] cisco.com&gt; Aaron Hillegass&lt;aaron[AT] classmax.com&gt; Jason Lango&lt;jal[AT] netapp.com&gt; Johan Feyaerts&lt;Johan.Feyaerts[AT] siemens.com&gt; Olivier Abad&lt;oabad[AT] noos.fr&gt; Thierry Andry&lt;Thierry.Andry[AT] advalvas.be&gt; Jeff Foster&lt;jfoste[AT] woodward.com&gt; Peter Torvals&lt;petertv[AT] xoommail.com&gt; Christophe Tronche&lt;ch.tronche[AT] computer.org&gt; Nathan Neulinger&lt;nneul[AT] umr.edu&gt; Tomislav Vujec&lt;tvujec[AT] carnet.hr&gt; Kojak&lt;kojak[AT] bigwig.net&gt; Uwe Girlich&lt;Uwe.Girlich[AT] philosys.de&gt; Warren Young&lt;tangent[AT] mail.com&gt; Heikki Vatiainen&lt;hessu[AT] cs.tut.fi&gt; Greg Hankins&lt;gregh[AT] twoguys.org&gt; Jerry Talkington&lt;jtalkington[AT] users.sourceforge.net&gt; Dave Chapeskie&lt;dchapes[AT] ddm.on.ca&gt; James Coe&lt;jammer[AT] cin.net&gt; Bert Driehuis&lt;driehuis[AT] playbeing.org&gt; Stuart Stanley&lt;stuarts[AT] mxmail.net&gt; John Thomes&lt;john[AT] ensemblecom.com&gt; Laurent Cazalet&lt;laurent.cazalet[AT] mailclub.net&gt; Thomas Parvais&lt;thomas.parvais[AT] advalvas.be&gt; Gerrit Gehnen&lt;G.Gehnen[AT] atrie.de&gt; Craig Newell&lt;craign[AT] cheque.uq.edu.au&gt; Ed Meaney&lt;emeaney[AT] cisco.com&gt; Dietmar Petras&lt;DPetras[AT] ELSA.de&gt; Fred Reimer&lt;fwr[AT] ga.prestige.net&gt; Florian Lohoff&lt;flo[AT] rfc822.org&gt; Jochen Friedrich&lt;jochen + ethereal[AT] scram.de&gt; Paul Welchinski&lt;paul.welchinski[AT] telusplanet.net&gt; Doug Nazar&lt;nazard[AT] dragoninc.on.ca&gt; Andreas Sikkema&lt;h323[AT] ramdyne.nl&gt; Mark Muhlestein&lt;mmm[AT] netapp.com&gt; Graham Bloice&lt;graham.bloice[AT] trihedral.com&gt; Ralf Schneider&lt;ralf.schneider[AT] alcatel.se&gt; Yaniv Kaul&lt;mykaul[AT] gmail.com&gt; Paul Ionescu&lt;paul[AT] acorp.ro&gt; Mark Burton&lt;markb[AT] ordern.com&gt; Stefan Raab&lt;sraab[AT] cisco.com&gt; Mark Clayton&lt;clayton[AT] shore.net&gt; Michael Rozhavsky&lt;mike[AT] tochna.technion.ac.il&gt; Dug Song&lt;dugsong[AT] monkey.org&gt; Michael Tu.xen&lt;tuexen[AT] fh - muenster.de&gt; Bruce Korb&lt;bkorb[AT] sco.com&gt; Jose Pedro Oliveira&lt;jpo[AT] di.uminho.pt&gt; David Frascone&lt;dave[AT] frascone.com&gt; Peter Kjellerstedt&lt;pkj[AT] axis.com&gt; Phil Techau&lt;phil_t[AT] altavista.net&gt; Wes Hardaker&lt;hardaker[AT] users.sourceforge.net&gt; Robert Tsai&lt;rtsai[AT] netapp.com&gt; Craig Metz&lt;cmetz[AT] inner.net&gt; Per Flock&lt;per.flock[AT] axis.com&gt; Jack Keane&lt;jkeane[AT] OpenReach.com&gt; Brian Wellington&lt;bwelling[AT] xbill.org&gt; Santeri Paavolainen&lt;santtu[AT] ssh.com&gt; Ulrich Kiermayr&lt;uk[AT] ap.univie.ac.at&gt; Neil Hunter&lt;neil.hunter[AT] energis - squared.com&gt; Ralf Holzer&lt;ralf[AT] well.com&gt; Craig Rodrigues&lt;rodrigc[AT] attbi.com&gt; Ed Warnicke&lt;hagbard[AT] physics.rutgers.edu&gt; Johan Jorgensen&lt;johan.jorgensen[AT] axis.com&gt; Frank Singleton&lt;frank.singleton[AT] ericsson.com&gt; Kevin Shi&lt;techishi[AT] ms22.hinet.net&gt; Mike Frisch&lt;mfrisch[AT] isurfer.ca&gt; Burke Lau&lt;burke_lau[AT] agilent.com&gt; Martti Kuparinen&lt;martti.kuparinen[AT] iki.fi&gt; David Hampton&lt;dhampton[AT] mac.com&gt; Kent Engstro.m&lt;kent[AT] unit.liu.se&gt; Ronnie Sahlberg&lt;ronnie_sahlberg[AT] ozemail.com.au&gt; Borosa Tomislav&lt;tomislav.borosa[AT] SIEMENS.HR&gt; Alexandre P.Ferreira&lt;alexandref[AT] tcoip.com.br&gt; Simharajan Srishylam&lt;Simharajan.Srishylam[AT] netapp.com&gt; Greg Kilfoyle&lt;gregk[AT] redback.com&gt; James E.Flemer&lt;jflemer[AT] acm.jhu.edu&gt; Peter Lei&lt;peterlei[AT] cisco.com&gt; Thomas Gimpel&lt;thomas.gimpel[AT] ferrari.de&gt; Albert Chin&lt;china[AT] thewrittenword.com&gt; Charles Levert&lt;charles[AT] comm.polymtl.ca&gt; Todd Sabin&lt;tas[AT] webspan.net&gt; Eduardo Perez Ureta&lt;eperez[AT] dei.inf.uc3m.es&gt; Martin Thomas&lt;martin_a_thomas[AT] yahoo.com&gt; Hartmut Mueller&lt;hartmut[AT] wendolene.ping.de&gt; Michal Melerowicz&lt;Michal.Melerowicz[AT] nokia.com&gt; Hannes Gredler&lt;hannes[AT] juniper.net&gt; Inoue&lt;inoue[AT] ainet.or.jp&gt; Olivier Biot&lt;obiot.ethereal[AT] gmail.com&gt; Patrick Wolfe&lt;pjw[AT] zocalo.cellular.ameritech.com&gt; Martin Held&lt;Martin.Held[AT] icn.siemens.de&gt; Riaan Swart&lt;rswart[AT] cs.sun.ac.za&gt; Christian Lacunza&lt;celacunza[AT] gmx.net&gt; Scott Renfro&lt;scott[AT] renfro.org&gt; Juan Toledo&lt;toledo[AT] users.sourceforge.net&gt; Jean - Christian Pennetier&lt;jeanchristian.pennetier[AT] rd.francetelecom.fr&gt; Jian Yu&lt;bgp4news[AT] yahoo.com&gt; Eran Mann&lt;emann[AT] opticalaccess.com&gt; Andy Hood&lt;ajhood[AT] fl.net.au&gt; Randy McEoin&lt;rmceoin[AT] ahbelo.com&gt; Edgar Iglesias&lt;edgar.iglesias[AT] axis.com&gt; Martina Obermeier&lt;Martina.Obermeier[AT] icn.siemens.de&gt; Javier Achirica&lt;achirica[AT] ttd.net&gt; B.Johannessen&lt;bob[AT] havoq.com&gt; Thierry Pelle&lt;thierry.pelle[AT] laposte.net&gt; Francisco Javier Cabello&lt;fjcabello[AT] vtools.es&gt; Laurent Rabret&lt;laurent.rabret[AT] rd.francetelecom.fr&gt; nuf si&lt;gnippiks[AT] yahoo.com&gt; Jeff Morriss&lt;jeff.morriss.ws[AT] gmail.com&gt; Aamer Akhter&lt;aakhter[AT] cisco.com&gt; Pekka Savola&lt;pekkas[AT] netcore.fi&gt; David Eisner&lt;cradle[AT] Glue.umd.edu&gt; Steve Dickson&lt;steved[AT] talarian.com&gt; Markus Seehofer&lt;Markus.Seehofer[AT] hirschmann.de&gt; Lee Berger&lt;lberger[AT] roy.org&gt; Motonori Shindo&lt;motonori[AT] shin.do&gt; Terje Krogdahl&lt;tekr[AT] nextra.com&gt; Jean - Francois Mule&lt;jfm[AT] cablelabs.com&gt; Thomas Wittwer&lt;thomas.wittwer[AT] iclip.ch&gt; Matthias Nyffenegger&lt;matthias.nyffenegger[AT] iclip.ch&gt; Palle Lyckegaard&lt;Palle[AT] lyckegaard.dk&gt; Nicolas Balkota&lt;balkota[AT] mac.com&gt; Tom Uijldert&lt;Tom.Uijldert[AT] cmg.nl&gt; Akira Endoh&lt;endoh[AT] netmarks.co.jp&gt; Graeme Hewson&lt;graeme.hewson[AT] oracle.com&gt; Pasi Eronen&lt;pe[AT] iki.fi&gt; Georg von Zezschwitz&lt;gvz[AT] 2scale.net&gt; Steffen Weinreich&lt;steve[AT] weinreich.org&gt; Marc Milgram&lt;ethereal[AT] mmilgram.NOSPAMmail.net&gt; Gordon McKinney&lt;gordon[AT] night - ray.com&gt; Pavel Novotny&lt;Pavel.Novotny[AT] icn.siemens.de&gt; Shinsuke Suzuki&lt;suz[AT] kame.net&gt; Andrew C.Feren&lt;acferen[AT] yahoo.com&gt; Tomas Kukosa&lt;tomas.kukosa[AT] siemens.com&gt; Andreas Stockmeier&lt;a.stockmeier[AT] avm.de&gt; Pekka Nikander&lt;pekka.nikander[AT] nomadiclab.com&gt; Hamish Moffatt&lt;hamish[AT] cloud.net.au&gt; Kazushi Sugyo&lt;k - sugyou[AT] nwsl.mesh.ad.jp&gt; Tim Potter&lt;tpot[AT] samba.org&gt; Raghu Angadi&lt;rangadi[AT] inktomi.com&gt; Taisuke Sasaki&lt;sasaki[AT] soft.net.fujitsu.co.jp&gt; Tim Newsham&lt;newsham[AT] lava.net&gt; Tom Nisbet&lt;Tnisbet[AT] VisualNetworks.com&gt; Darren New&lt;dnew[AT] san.rr.com&gt; Pavel Mores&lt;pvl[AT] uh.cz&gt; Bernd Becker&lt;bb[AT] bernd - becker.de&gt; Heinz Prantner&lt;Heinz.Prantner[AT] radisys.com&gt; Irfan Khan&lt;ikhan[AT] qualcomm.com&gt; Jayaram V.R&lt;vjayar[AT] cisco.com&gt; Dinesh Dutt&lt;ddutt[AT] cisco.com&gt; Nagarjuna Venna&lt;nvenna[AT] Brixnet.com&gt; Jirka Novak&lt;j.novak[AT] netsystem.cz&gt; Ricardo Barroetaven ~a&lt;rbarroetavena[AT] veufort.com&gt; Alan Harrison&lt;alanharrison[AT] mail.com&gt; Mike Frantzen&lt;frantzen[AT] w4g.org&gt; Charlie Duke&lt;cduke[AT] fvc.com&gt; Alfred Arnold&lt;Alfred.Arnold[AT] elsa.de&gt; Dermot Bradley&lt;dermot.bradley[AT] openwave.com&gt; Adam Sulmicki&lt;adam[AT] cfar.umd.edu&gt; Kari Tiirikainen&lt;kari.tiirikainen[AT] nokia.com&gt; John Mackenzie&lt;John.A.Mackenzie[AT] t - online.de&gt; Peter Valchev&lt;pvalchev[AT] openbsd.org&gt; Alex Rozin&lt;Arozin[AT] mrv.com&gt; Jouni Malinen&lt;jkmaline[AT] cc.hut.fi&gt; Paul E.Erkkila&lt;pee[AT] erkkila.org&gt; Jakob Schlyter&lt;jakob[AT] openbsd.org&gt; Jim Sienicki&lt;sienicki[AT] issanni.com&gt; Steven French&lt;sfrench[AT] us.ibm.com&gt; Diana Eichert&lt;deicher[AT] sandia.gov&gt; Blair Cooper&lt;blair[AT] teamon.com&gt; Kikuchi Ayamura&lt;ayamura[AT] ayamura.org&gt; Didier Gautheron&lt;dgautheron[AT] magic.fr&gt; Phil Williams&lt;csypbw[AT] comp.leeds.ac.uk&gt; Kevin Humphries&lt;khumphries[AT] networld.com&gt; Erik Nordstro.m&lt;erik.nordstrom[AT] it.uu.se&gt; Devin Heitmueller&lt;dheitmueller[AT] netilla.com&gt; Chenjiang Hu&lt;chu[AT] chiaro.com&gt; Kan Sasaki&lt;sasaki[AT] fcc.ad.jp&gt; Stefan Wenk&lt;stefan.wenk[AT] gmx.at&gt; Ruud Linders&lt;ruud[AT] lucent.com&gt; Andrew Esh&lt;Andrew.Esh[AT] tricord.com&gt; Greg Morris&lt;GMORRIS[AT] novell.com&gt; Dirk Steinberg&lt;dws[AT] dirksteinberg.de&gt; Kari Heikkila&lt;kari.o.heikkila[AT] nokia.com&gt; Olivier Dreux&lt;Olivier.Dreux[AT] alcatel.fr&gt; Michael Stiller&lt;ms[AT] 2scale.net&gt; Antti Tuominen&lt;ajtuomin[AT] tml.hut.fi&gt; Martin Gignac&lt;lmcgign[AT] mobilitylab.net&gt; John Wells&lt;wells[AT] ieee.org&gt; Loic Tortay&lt;tortay[AT] cc.in2p3.fr&gt; Steve Housley&lt;Steve_Housley[AT] eur .3com.com&gt; Peter Hawkins&lt;peter[AT] hawkins.emu.id.au&gt; Bill Fumerola&lt;billf[AT] FreeBSD.org&gt; Chris Waters&lt;chris[AT] waters.co.nz&gt; Solomon Peachy&lt;pizza[AT] shaftnet.org&gt; Jaime Fournier&lt;Jaime.Fournier[AT] hush.com&gt; Markus Steinmann&lt;ms[AT] seh.de&gt; Tsutomu Mieno&lt;iitom[AT] utouto.com&gt; Yasuhiro Shirasaki&lt;yasuhiro[AT] gnome.gr.jp&gt; Anand V.Narwani&lt;anand[AT] narwani.org&gt; Christopher K.St.John&lt;cks[AT] distributopia.com&gt; Nix&lt;nix[AT] esperi.demon.co.uk&gt; Liviu Daia&lt;Liviu.Daia[AT] imar.ro&gt; Richard Urwin&lt;richard[AT] soronlin.org.uk&gt; Prabhakar Krishnan&lt;Prabhakar.Krishnan[AT] netapp.com&gt; Jim McDonough&lt;jmcd[AT] us.ibm.com&gt; Sergei Shokhor&lt;sshokhor[AT] uroam.com&gt; Hidetaka Ogawa&lt;ogawa[AT] bs2.qnes.nec.co.jp&gt; Jan Kratochvil&lt;short[AT] ucw.cz&gt; Alfred Koebler&lt;ak[AT] icon - sult.de&gt; Vassilii Khachaturov&lt;Vassilii.Khachaturov[AT] comverse.com&gt; Bill Studenmund&lt;wrstuden[AT] wasabisystems.com&gt; Brian Bruns&lt;camber[AT] ais.org&gt; Flavio Poletti&lt;flavio[AT] polettix.it&gt; Marcus Haebler&lt;haeblerm[AT] yahoo.com&gt; Ulf Lamping&lt;ulf.lamping[AT] web.de&gt; Matthew Smart&lt;smart[AT] monkey.org&gt; Luke Howard&lt;lukeh[AT] au.padl.com&gt; PC Drew&lt;drewpc[AT] ibsncentral.com&gt; Renzo Tomas&lt;renzo.toma[AT] xs4all.nl&gt; Clive A.Stubbings&lt;eth[AT] vjet.demon.co.uk&gt; Steve Langasek&lt;vorlon[AT] netexpress.net&gt; Brad Hards&lt;bhards[AT] bigpond.net.au&gt; cjs 2895 &lt;
    cjs2895[AT] hotmail.com &gt;
    Lutz Jaenicke&lt;Lutz.Jaenicke[AT] aet.TU - Cottbus.DE&gt;
            Senthil Kumar Nagappan&lt;sknagappan[AT] yahoo.com&gt;
                Jason House&lt;jhouse[AT] mitre.org&gt;
                    Peter Fales&lt;psfales[AT] lucent.com&gt;
                        Fritz Budiyanto&lt;fritzb88[AT] yahoo.com&gt;
                            Jean - Baptiste Marchand&lt;Jean - Baptiste.Marchand[AT] hsc.fr&gt; Andreas Trauer&lt;andreas.trauer[AT] siemens.com&gt; Ronald Henderson&lt;Ronald.Henderson[AT] CognicaseUSA.com&gt; Brian Ginsbach&lt;ginsbach[AT] cray.com&gt; Dave Richards&lt;d_m_richards[AT] comcast.net&gt; Martin Regner&lt;martin.regner[AT] chello.se&gt; Jason Greene&lt;jason[AT] inetgurus.net&gt; Marco Molteni&lt;mmolteni[AT] cisco.com&gt; James Harris&lt;jharris[AT] fourhorsemen.org&gt; rmkml&lt;rmkml[AT] wanadoo.fr&gt; Anders Broman&lt;anders.broman[AT] ericsson.com&gt; Christian Falckenberg&lt;christian.falckenberg[AT] nortelnetworks.com&gt; Huagang Xie&lt;xie[AT] lids.org&gt; Pasi Kovanen&lt;Pasi.Kovanen[AT] tahoenetworks.fi&gt; Teemu Rinta - aho&lt;teemu.rinta - aho[AT] nomadiclab.com&gt; Martijn Schipper&lt;mschipper[AT] globespanvirata.com&gt; Wayne Parrott&lt;wayne_p[AT] pacific.net.au&gt; Laurent Meyer&lt;laurent.meyer6[AT] wanadoo.fr&gt; Lars Roland&lt;Lars.Roland[AT] gmx.net&gt; Miha Jemec&lt;m.jemec[AT] iskratel.si&gt; Markus Friedl&lt;markus[AT] openbsd.org&gt; Todd Montgomery&lt;tmontgom[AT] tibco.com&gt; emre&lt;emre[AT] flash.net&gt; Stephen Shelley&lt;steve.shelley[AT] attbi.com&gt; Erwin Rol&lt;erwin[AT] erwinrol.com&gt; Duncan Laurie&lt;duncan[AT] sun.com&gt; Tony Schene&lt;schene[AT] pcisys.net&gt; Matthijs Melchior&lt;mmelchior[AT] xs4all.nl&gt; Garth Bushell&lt;gbushell[AT] elipsan.com&gt; Mark C.Brown&lt;mbrown[AT] hp.com&gt; Can Erkin Acar&lt;canacar[AT] eee.metu.edu.tr&gt; Martin Warnes&lt;martin.warnes[AT] ntlworld.com&gt; J Bruce Fields&lt;bfields[AT] fieldses.org&gt; tz&lt;tz1[AT] mac.com&gt; Jeff Liu&lt;jqliu[AT] broadcom.com&gt; Niels Koot&lt;Niels.Koot[AT] logicacmg.com&gt; Lionel Ains&lt;lains[AT] gmx.net&gt; Joakim Wiberg&lt;jow[AT] hms - networks.com&gt; Jeff Rizzo&lt;riz[AT] boogers.sf.ca.us&gt; Christoph Wiest&lt;ch.wiest[AT] tesionmail.de&gt; Xuan Zhang&lt;xz[AT] aemail4u.com&gt; Thierry Martin&lt;thierry.martin[AT] accellent - group.com&gt; Oleg Terletsky&lt;oleg.terletsky[AT] comverse.com&gt; Michael Lum&lt;mlum[AT] telostech.com&gt; Shiang - Ming Huang&lt;smhuang[AT] pcs.csie.nctu.edu.tw&gt; Tony Lindstrom&lt;tony.lindstrom[AT] ericsson.com&gt; Niklas Ogren&lt;niklas.ogren[AT] 71.se&gt; Jesper Peterson&lt;jesper[AT] endace.com&gt; Giles Scott&lt;gscott[AT] arubanetworks.com&gt; Vincent Jardin&lt;vincent.jardin[AT] 6wind.com&gt; Jean - Michel Fayard&lt;jean - michel.fayard[AT] moufrei.de&gt; Josef Korelus&lt;jkor[AT] quick.cz&gt; Brian K.Teravskis&lt;Brian_Teravskis[AT] Cargill.com&gt; Nathan Jennings&lt;njgm890[AT] gmail.com&gt; Hans Viens&lt;hviens[AT] mediatrix.com&gt; Kevin A.Noll&lt;kevin.noll[AT] versatile.com&gt; Emanuele Caratti&lt;wiz[AT] libero.it&gt; Graeme Reid&lt;graeme.reid[AT] norwoodsystems.com&gt; Lars Ruoff&lt;lars.ruoff[AT] sxb.bsf.alcatel.fr&gt; Samuel Qu&lt;samuel.qu[AT] utstar.com&gt; Baktha Muralitharan&lt;muralidb[AT] cisco.com&gt; Loi.c Minier&lt;lool[AT] dooz.org&gt; Marcel Holtmann&lt;marcel[AT] holtmann.org&gt; Scott Emberley&lt;scotte[AT] netinst.com&gt; Brian Fundakowski Feldman&lt;bfeldman[AT] fla.fujitsu.com&gt; Yuriy Sidelnikov&lt;ysidelnikov[AT] hotmail.com&gt; Matthias Drochner&lt;M.Drochner[AT] fz - juelich.de&gt; Dave Sclarsky&lt;dave_sclarsky[AT] cnt.com&gt; Scott Hovis&lt;scott.hovis[AT] ums.msfc.nasa.gov&gt; David Fort&lt;david.fort[AT] irisa.fr&gt; Felix Fei&lt;felix.fei[AT] utstar.com&gt; Christoph Neusch&lt;christoph.neusch[AT] nortelnetworks.com&gt; Jan Kiszka&lt;jan.kiszka[AT] web.de&gt; Joshua Craig Douglas&lt;jdouglas[AT] enterasys.com&gt; Dick Gooris&lt;gooris[AT] alcatel - lucent.com&gt; Michael Shuldman&lt;michaels[AT] inet.no&gt; Tadaaki Nagao&lt;nagao[AT] iij.ad.jp&gt; Aaron Woo&lt;woo[AT] itd.nrl.navy.mil&gt; Chris Wilson&lt;chris[AT] mxtelecom.com&gt; Rolf Fiedler&lt;Rolf.Fiedler[AT] Innoventif.com&gt; Alastair Maw&lt;ethereal[AT] almaw.com&gt; Sam Leffler&lt;sam[AT] errno.com&gt; Martin Mathieson&lt;martin.r.mathieson[AT] googlemail.com&gt; Christian Wagner&lt;Christian.Wagner[AT] stud.uni - karlsruhe.de&gt; Edwin Calo&lt;calo[AT] fusemail.com&gt; Ian Schorr&lt;ischorr[AT] comcast.net&gt; Rowan McFarland&lt;rmcfarla[AT] cisco.com&gt; John Engelhart&lt;johne[AT] zang.com&gt; Ryuji Somegawa&lt;ryuji - so[AT] is.aist - nara.ac.jp&gt; metatech&lt;metatechbe[AT] gmail.com&gt; Brian Wheeler&lt;Brian.Wheeler[AT] arrisi.com&gt; Josh Bailey&lt;joshbailey[AT] lucent.com&gt; Jelmer Vernooij&lt;jelmer[AT] samba.org&gt; Duncan Sargeant&lt;dunc - ethereal - dev[AT] rcpt.to&gt; Love Ho.rnquist A &amp;#176;
strand&lt;lha[AT] it.su.se&gt;
        Lukas Pokorny&lt;maskis[AT] seznam.cz&gt;
            Carlos Pignataro&lt;cpignata[AT] cisco.com&gt;
                Thomas Anders&lt;thomas.anders[AT] blue - cable.de&gt;
                    Rich Coe&lt;Richard.Coe[AT] med.ge.com&gt;
                        Dominic Bechaz&lt;bdo[AT] zhwin.ch&gt;
                            Richard van der Hoff&lt;richardv[AT] mxtelecom.com&gt;
                                Shaun Jackman&lt;sjackman[AT] gmail.com&gt;
                                    Jon Oberheide&lt;jon[AT] oberheide.org&gt;
                                        Henry Ptasinski&lt;henryp[AT] broadcom.com&gt;
                                            Roberto Morro&lt;roberto.morro[AT] telecomitalia.it&gt;
                                                Chris Maynard&lt;Christopher.Maynard[AT] GTECH.COM&gt;
                                                    SEKINE Hideki&lt;sekineh[AT] gf7.so - net.ne.jp&gt;
                                                        Jeff Connelly&lt;shellreef + mp2p[AT] gmail.com&gt;
                                                            Irene Ru.ngeler &lt; i.ruengeler[AT] fh - muenster.de M.Ortega y Strupp&lt;moys[AT] loplof.de&gt; Kelly Byrd&lt;kbyrd - ethereal[AT] memcpy.com&gt; Luis Ontanon&lt;luis.ontanon[AT] gmail.com&gt; Luca Deri&lt;deri[AT] ntop.org&gt; Viorel Suman&lt;vsuman[AT] avmob.ro&gt; Alejandro Vaquero&lt;alejandro.vaquero[AT] verso.com&gt; Francesco Fondelli&lt;francesco.fondelli[AT] gmail.com&gt; Artem Tamazov&lt;artem.tamazov[AT] tellabs.com&gt; Dmitry Trebich&lt;dmitry.trebich[AT] gmail.com&gt; Bill Meier&lt;wmeier[AT] newsguy.com&gt; Susanne Edlund&lt;Susanne.Edlund[AT] ericsson.com&gt; Victor Stratan&lt;hidralisk[AT] yahoo.com&gt; Peter Johansson&lt;PeterJohansson73[AT] gmail.com&gt; Stefan Metzmacher&lt;metze[AT] samba.org&gt; Abhijit Menon - Sen&lt;ams[AT] oryx.com&gt; James Fields&lt;jvfields[AT] tds.net&gt; Kevin Johnson&lt;kjohnson[AT] secureideas.net&gt; Mike Duigou&lt;bondolo[AT] dev.java.net&gt; Deepak Jain&lt;jain1971[AT] yahoo.com&gt; Stefano Pettini&lt;spettini[AT] users.sourceforge.net&gt; Jon Ringle&lt;ml - ethereal[AT] ringle.org&gt; Tim Endean&lt;endeant[AT] hotmail.com&gt; Charlie Lenahan&lt;clenahan[AT] fortresstech.com&gt; Takeshi Nakashima&lt;T.Nakashima[AT] jp.yokogawa.com&gt; Shoichi Sakane&lt;sakane[AT] tanu.org&gt; Michael Richardson&lt;Michael.Richardson[AT] protiviti.com&gt; Olivier Jacques&lt;olivier.jacques[AT] hp.com&gt; Francisco Alcoba&lt;francisco.alcoba[AT] ericsson.com&gt; Nils O.Sela &amp;#176;
sdal&lt;noselasd[AT] asgaard.homelinux.org&gt;
        Guillaume Chazarain&lt;guichaz[AT] yahoo.fr&gt;
            Angelo Bannack&lt;angelo.bannack[AT] siemens.com&gt;
                Paolo Frigo&lt;paolofrigo[AT] gmail.com&gt;
                    Jeremy J Ouellette&lt;jouellet[AT] scires.com&gt;
                        Aboo Valappil&lt;valappil_aboo[AT] emc.com&gt;
                            Fred Hoekstra&lt;fred.hoekstra[AT] philips.com&gt;
                                Ankur Aggarwal&lt;ankur[AT] in.athenasemi.com&gt;
                                    Lucian Piros&lt;lpiros[AT] avmob.ro&gt;
                                        Juan Gonzalez&lt;juan.gonzalez[AT] pikatech.com&gt;
                                            Brian Bogora&lt;brian_bogora[AT] mitel.com&gt;
                                                Jim Young&lt;sysjhy[AT] langate.gsu.edu&gt;
                                                    Jeff Snyder&lt;jeff[AT] mxtelecom.com&gt;
                                                        William Fiveash&lt;William.Fiveash[AT] sun.com&gt;
                                                            Graeme Lunt&lt;graeme.lunt[AT] smhs.co.uk&gt;
                                                                Menno Andriesse&lt;s5066[AT] nc3a.nato.int&gt;
                                                                    Stig Bjorlykke&lt;stig[AT] bjorlykke.org&gt;
                                                                        Kyle J.Harms&lt;kyle.j.harms[AT] boeing.com&gt;
                                                                            Eric Wedel&lt;ewedel[AT] bluearc.com&gt;
                                                                                Secfire&lt;secfire[AT] gmail.com&gt;
                                                                                    Eric Hultin&lt;Eric.Hultin[AT] arrisi.com&gt;
                                                                                        Paolo Abeni&lt;paolo.abeni[AT] email.it&gt;
                                                                                            W.Borgert&lt;debacle[AT] debian.org&gt;
                                                                                                Frederic Roudaut&lt;frederic.roudaut[AT] irisa.fr&gt;
                                                                                                    Christoph Scholz&lt;scholz_ch[AT] web.de&gt;
                                                                                                        Wolfgang Hansmann&lt;hansmann[AT] cs.uni - bonn.de&gt;
                                                                                                            Kees Cook&lt;kees[AT] outflux.net&gt;
                                                                                                                Thomas Dreibholz&lt;dreibh[AT] iem.uni - due.de&gt;
                                                                                                                    Authesserre Samuel&lt;sauthess[AT] gmail.com&gt;
                                                                                                                        Balint Reczey&lt;balint[AT] balintreczey.hu&gt;
                                                                                                                            Stephen Fisher&lt;stephenfisher - wireshark[AT] outlook.com&gt;
                                                                                                                                Krzysztof Burghardt&lt;krzysztof[AT] burghardt.pl&gt;
                                                                                                                                    Peter Racz&lt;racz[AT] ifi.unizh.ch&gt;
                                                                                                                                        Jakob Bratkovic&lt;j.bratkovic[AT] iskratel.si&gt;
                                                                                                                                            Mark Lewis&lt;mlewis[AT] altera.com&gt;
                                                                                                                                                David Buechi&lt;bhd[AT] zhwin.ch&gt;
                                                                                                                                                    Bill Florac&lt;bill.florac[AT] etcconnect.com&gt;
                                                                                                                                                        Alex Burlyga&lt;Alex.Burlyga[AT] netapp.com&gt;
                                                                                                                                                            Douglas Pratley&lt;Douglas.pratley[AT] detica.com&gt;
                                                                                                                                                                Giorgio Tino&lt;giorgio.tino[AT] cacetech.com&gt;
                                                                                                                                                                    Davide Schiera&lt;davide.schiera[AT] riverbed.com&gt;
                                                                                                                                                                        Sebastien Tandel&lt;sebastien[AT] tandel.be&gt;
                                                                                                                                                                            Clay Jones&lt;clay.jones[AT] email.com&gt;
                                                                                                                                                                                Kriang Lerdsuwanakij&lt;lerdsuwa[AT] users.sourceforge.net&gt;
                                                                                                                                                                                    Abhik Sarkar&lt;sarkar.abhik[AT] gmail.com&gt;
                                                                                                                                                                                        Robin Seggelmann&lt;seggelmann[AT] fh - muenster.de&gt;
                                                                                                                                                                                            Chris Bontje&lt;cbontje[AT] gmail.com&gt;
                                                                                                                                                                                                Ryan Wamsley&lt;wamslers[AT] sbcglobal.net&gt;
                                                                                                                                                                                                    Dave Butt&lt;davidbutt[AT] mxtelecom.com&gt;
                                                                                                                                                                                                        Julian Cable&lt;julian_cable[AT] yahoo.com&gt;
                                                                                                                                                                                                            Joost Yervante Damad&lt;joost[AT] teluna.org&gt;
                                                                                                                                                                                                                Martin Sustrik&lt;sustrik[AT] imatix.com&gt;
                                                                                                                                                                                                                    Jon Smirl&lt;jonsmirl[AT] gmail.com&gt;
                                                                                                                                                                                                                        David Kennedy&lt;sgsguy[AT] gmail.com&gt;
                                                                                                                                                                                                                            Matthijs Mekking&lt;matthijs[AT] mlnetlabs.nl&gt;
                                                                                                                                                                                                                                Dustin Johnson&lt;dustin[AT] dustinj.us&gt;
                                                                                                                                                                                                                                    Victor Fajardo&lt;vfajardo[AT] tari.toshiba.com&gt;
                                                                                                                                                                                                                                        Tamas Regos&lt;tamas.regos[AT] ericsson.com&gt;
                                                                                                                                                                                                                                            Moshe van der Sterre&lt;moshevds[AT] gmail.com&gt;
                                                                                                                                                                                                                                                Rob Casey&lt;rcasey[AT] gmail.com&gt;
                                                                                                                                                                                                                                                    Ted Percival&lt;ted[AT] midg3t.net&gt;
                                                                                                                                                                                                                                                        Marc Petit -
    Huguenin&lt;marc[AT] petit - huguenin.org&gt;
        Florent Drouin&lt;florent.drouin[AT] alcatel - lucent.fr&gt;
            Karen Feng&lt;kfeng[AT] fas.harvard.edu&gt;
                Stephen Croll&lt;croll[AT] mobilemetrics.net&gt;
                    Jens Bra.uer&lt;jensb[AT] cs.tu - berlin.de&gt;
                        Sake Blok&lt;sake[AT] euronet.nl&gt;
                            Fulko Hew&lt;fulko.hew[AT] gmail.com&gt;
                                Yukiyo Akisada&lt;Yukiyo.Akisada[AT] jp.yokogawa.com&gt;
                                    Andy Chu&lt;chu.dev[AT] gmail.com&gt;
                                        Shane Kearns&lt;shane.kearns[AT] symbian.com&gt;
                                            Loris Degioanni&lt;loris.degioanni[AT] riverbed.com&gt;
                                                Sven Meier&lt;msv[AT] zhwin.ch&gt;
                                                    Holger Pfrommer&lt;hpfrommer[AT] hilscher.com&gt;
                                                        Hariharan Ananthakrishnan&lt;hariharan.a[AT] gmail.com&gt;
                                                            Hannes Ka.lber&lt;hannes.kaelber-- - wireshark[AT] x2e.de&gt;
                                                                Stephen Donnelly&lt;stephen[AT] endace.com&gt;
                                                                    Philip Frey&lt;frey.philip[AT] gmail.com&gt;
                                                                        Yves Geissbuehler&lt;yves.geissbuehler[AT] gmail.com&gt;
                                                                            Shigeo Nakamura&lt;naka_shigeo[AT] yahoo.co.jp&gt;
                                                                                Sven Eckelmann&lt;sven[AT] narfation.org&gt;
                                                                                    Edward J.Paradise&lt;pdice[AT] cisco.com&gt;
                                                                                        Brian Stormont&lt;nospam[AT] stormyprods.com&gt;
                                                                                            Vincent Helfre&lt;vincent.helfre[AT] ericsson.com&gt;
                                                                                                Brooss&lt;brooss.teambb[AT] gmail.com&gt;
                                                                                                    Joan Ramio&lt;joan[AT] ramio.cat&gt;
                                                                                                        David Castleford&lt;david.castleford[AT] orange - ftgroup.com&gt;
                                                                                                            Peter Harris&lt;pharris[AT] opentext.com&gt;
                                                                                                                Martin Lutz&lt;MartinL[AT] copadata.at&gt;
                                                                                                                    Johnny Mitrevski&lt;mitrevj[AT] hotmail.com&gt;
                                                                                                                        Neil Horman&lt;nhorman[AT] tuxdriver.com&gt;
                                                                                                                            Andreas Schuler&lt;krater[AT] badterrorist.com&gt;
                                                                                                                                Matthias Wenzel&lt;dect[AT] mazzoo.de&gt;
                                                                                                                                    Christian Durrer&lt;christian.durrer[AT] sensemail.ch&gt;
                                                                                                                                        Naoyoshi Ueda&lt;piyomaru3141[AT] gmail.com&gt;
                                                                                                                                            Javier Cardona&lt;javier[AT] cozybit.com&gt;
                                                                                                                                                Jens Steinhauser&lt;jens.steinhauser[AT] omicron.at&gt;
                                                                                                                                                    Julien Kerihuel&lt;j.kerihuel[AT] openchange.org&gt;
                                                                                                                                                        Vincenzo Condoleo&lt;vcondole[AT] hsr.ch&gt;
                                                                                                                                                            Mohammad Ebrahim Mohammadi Panah&lt;mebrahim[AT] gmail.com&gt;
                                                                                                                                                                Greg Schwendimann&lt;gregs[AT] iol.unh.edu&gt;
                                                                                                                                                                    Nick Lewis&lt;nick.lewis[AT] atltelecom.com&gt;
                                                                                                                                                                        Fred Fierling&lt;fff[AT] exegin.com&gt;
                                                                                                                                                                            Samu Varjonen&lt;samu.varjonen[AT] hiit.fi&gt;
                                                                                                                                                                                Alexis La Goutte&lt;alexis.lagoutte[AT] gmail.com&gt;
                                                                                                                                                                                    Varun Notibala&lt;nbvarun[AT] gmail.com&gt;
                                                                                                                                                                                        Nathan Hartwell&lt;nhartwell[AT] gmail.com&gt;
                                                                                                                                                                                            Don Chirieleison&lt;donc[AT] mitre.org&gt;
                                                                                                                                                                                                Harald Welte&lt;laforge[AT] gnumonks.org&gt;
                                                                                                                                                                                                    Chris Costa&lt;chcosta75[AT] hotmail.com&gt;
                                                                                                                                                                                                        Bruno Premont&lt;bonbons[AT] linux - vserver.org&gt;
                                                                                                                                                                                                            Florian Forster&lt;octo[AT] verplant.org&gt;
                                                                                                                                                                                                                Ivan Sy Jr.&lt;ivan_jr[AT] yahoo.com&gt;Matthieu Patou&lt;mat[AT] matws.net&gt;
                                                                                                                                                                                                                    Kovarththanan Rajaratnam&lt;kovarththanan.rajaratnam[AT] gmail.com&gt;
                                                                                                                                                                                                                        Matt Watchinski&lt;mwatchinski[AT] sourcefire.com&gt;
                                                                                                                                                                                                                            Ravi Kondamuru&lt;Ravi.Kondamuru[AT] citrix.com&gt;
                                                                                                                                                                                                                                Jan Gerbecks&lt;jan.gerbecks[AT] stud.uni - due.de&gt;
                                                                                                                                                                                                                                    Vladimir Smrekar&lt;vladimir.smrekar[AT] gmail.com&gt;
                                                                                                                                                                                                                                        Tobias Erichsen&lt;t.erichsen[AT] gmx.de&gt;
                                                                                                                                                                                                                                            Erwin van Eijk&lt;erwin.vaneijk[AT] gmail.com&gt;
                                                                                                                                                                                                                                                Venkateshwaran Dorai&lt;venkateshwaran.d[AT] gmail.com&gt;
                                                                                                                                                                                                                                                    Ben Greear&lt;greearb[AT] candelatech.com&gt;
                                                                                                                                                                                                                                                        Richard Ku.mmel&lt;r.kuemmel[AT] beckhoff.de&gt;
                                                                                                                                                                                                                                                            Yi Yu&lt;yiyu.inbox[AT] gmail.com&gt;
                                                                                                                                                                                                                                                                Aniruddha A&lt;aniruddha.a[AT] gmail.com&gt;
                                                                                                                                                                                                                                                                    David Aggeler&lt;david_aggeler[AT] hispeed.ch&gt;
                                                                                                                                                                                                                                                                        Jens Kilian&lt;jjk[AT] acm.org&gt;
                                                                                                                                                                                                                                                                            David Bond&lt;mokon[AT] mokon.net&gt;
                                                                                                                                                                                                                                                                                Paul J.Metzger&lt;pjm[AT] ll.mit.edu&gt;
                                                                                                                                                                                                                                                                                    Robert Hogan&lt;robert[AT] roberthogan.net&gt;
                                                                                                                                                                                                                                                                                        Torrey Atcitty&lt;torrey.atcitty[AT] harman.com&gt;
                                                                                                                                                                                                                                                                                            Dave Olsen&lt;dave.olsen[AT] harman.com&gt;
                                                                                                                                                                                                                                                                                                Craig Gunther&lt;craig.gunther[AT] harman.com&gt;
                                                                                                                                                                                                                                                                                                    Levi Pearson&lt;levi.pearson[AT] harman.com&gt;
                                                                                                                                                                                                                                                                                                        Allan M.Madsen&lt;allan.m[AT] madsen.dk&gt;
                                                                                                                                                                                                                                                                                                            Slava&lt;slavak[AT] gmail.com&gt;
                                                                                                                                                                                                                                                                                                                H.sivank&lt;hsivank[AT] gmail.com&gt;
                                                                                                                                                                                                                                                                                                                    Edgar Gladkich&lt;edgar.gladkich[AT] inacon.de&gt;
                                                                                                                                                                                                                                                                                                                        Michael Bernhard&lt;michael.bernhard[AT] bfh.ch&gt;
                                                                                                                                                                                                                                                                                                                            Holger Hans Peter Freyther&lt;zecke[AT] selfish.org&gt;
                                                                                                                                                                                                                                                                                                                                Jose Pico&lt;jose[AT] taddong.com&gt;
                                                                                                                                                                                                                                                                                                                                    David Perez&lt;david[AT] taddong.com&gt;
                                                                                                                                                                                                                                                                                                                                        Ha &amp;#176;
kon Nessjoen&lt;haakon.nessjoen[AT] gmail.com&gt;
        Herbert Lischka&lt;herbert[AT] lischka - berlin.de&gt;
            Felix Kra.mer&lt;sauter - cumulus[AT] de.sauter - bc.com&gt;
                Tom Hughes&lt;tom[AT] compton.nu&gt;
                    Owen Kirby&lt;osk[AT] exegin.com&gt;
                        Colin O'Flynn           &lt;coflynn[AT]newae.com&gt;  Juha Siltanen&lt;juha.siltanen[AT] nsn.com&gt;
                            Cal Turney&lt;turney_cal[AT] emc.com&gt;
                                Lukasz Kotasa&lt;lukasz.kotasa[AT] tieto.com&gt;
                                    Jason Masker&lt;jason[AT] masker.net&gt;
                                        Giuliano Fabris&lt;giuliano.fabris[AT] appeartv.com&gt;
                                            Alexander Koeppe&lt;format_c[AT] online.de&gt;
                                                Holger Grandy&lt;Holger.Grandy[AT] bmw - carit.de&gt;
                                                    Hadriel Kaplan&lt;hadrielk[AT] yahoo.com&gt;
                                                        Srinivasa Pradeep&lt;sippyemail - wireshark[AT] yahoo.com&gt;
                                                            Lori Tribble&lt;ljtconsulting[AT] gmail.com&gt;
                                                                Thomas Boehne&lt;TBoehne[AT] ADwin.de&gt;
                                                                    Gerhard Gappmeier&lt;gerhard.gappmeier[AT] ascolab.com&gt;
                                                                        David Katz&lt;dkatz[AT] airspan.com&gt;
                                                                            Toralf Fo.rster&lt;toralf.foerster[AT] gmx.de&gt;
                                                                                Stephane Bryant&lt;stephane[AT] glycon.org&gt;
                                                                                    Emil Wojak&lt;emil[AT] wojak.eu&gt;
                                                                                        Steve Huston&lt;shuston[AT] riverace.com&gt;
                                                                                            Lorand Jakab&lt;ljakab[AT] ac.upc.edu&gt;
                                                                                                Grzegorz Szczytowski&lt;Grzegorz.Szczytowski[AT] gmail.com&gt;
                                                                                                    Martin Kaiser&lt;martin[AT] kaiser.cx&gt;
                                                                                                        Jakub Zawadzki&lt;darkjames - ws[AT] darkjames.pl&gt;
                                                                                                            Roland Knall&lt;rknall[AT] gmail.com&gt;
                                                                                                                Xiao Xiangquan&lt;xiaoxiangquan[AT] gmail.com&gt;
                                                                                                                    Hans -
    Christoph Schemmel&lt;hans - christoph.schemmel[AT] cinterion.com&gt;
        Tyson Key&lt;tyson.key[AT] gmail.com&gt;
            Johannes Jochen&lt;johannes.jochen[AT] belden.com&gt;
                Florian Fainelli&lt;florian[AT] openwrt.org&gt;
                    Daniel Willmann&lt;daniel[AT] totalueberwachung.de&gt;
                        Brian Cavagnolo&lt;brian[AT] cozybit.com&gt;
                            Allison&lt;aobourn[AT] isilon.com&gt;
                                Edwin Groothuis&lt;wireshark[AT] mavetju.org&gt;
                                    Andrew Kampjes&lt;andrew.kampjes[AT] endace.com&gt;
                                        Kurnia Hendrawan&lt;kurnia.hendrawan[AT] consistec.de&gt;
                                            Leonard Tracy&lt;letracy[AT] cisco.com&gt;
                                                Elliott Aldrich&lt;elliott[AT] aldrichart.com&gt;
                                                    Glenn Matthews&lt;glenn.matthews[AT] cisco.com&gt;
                                                        Donnie Savage&lt;dsavage[AT] cisco.com&gt;
                                                            Spenser Sheng&lt;spenser.sheng[AT] ericsson.com&gt;
                                                                Benjamin Stocks&lt;bmstocks[AT] ra.rockwell.com&gt;
                                                                    Florian Reichert&lt;refl[AT] zhaw.ch&gt;
                                                                        Martin Renold&lt;reld[AT] zhaw.ch&gt;
                                                                            Iain Arnell&lt;iarnell[AT] epo.org&gt;
                                                                                Mariusz Okroj&lt;okrojmariusz[AT] gmail.com&gt;
                                                                                    Ivan Lawrow&lt;ivan.lawrow[AT] jennic.com&gt;
                                                                                        Kari Vatjus - Anttila&lt;kari.vatjus - anttila[AT] cie.fi&gt; Shobhank Sharma&lt;ssharma5[AT] ncsu.edu&gt; Salil Kanitkar&lt;sskanitk[AT] ncsu.edu&gt; Michael Sakaluk&lt;mdsakalu[AT] ncsu.edu&gt; Mayuresh Raut&lt;msraut[AT] ncsu.edu&gt; Sheetal Kshirsagar&lt;sdkshirs[AT] ncsu.edu&gt; Andrew Williams&lt;anwilli5[AT] ncsu.edu&gt; Per Liedberg&lt;per.liedberg[AT] ericsson.com&gt; Gaurav Tungatkar&lt;gauravstt[AT] gmail.com&gt; Bill Schiller&lt;bill.schiller[AT] emerson.com&gt; Aditya Ambadkar&lt;arambadk[AT] ncsu.edu&gt; Diana Chris&lt;dvchris[AT] ncsu.edu&gt; Guy Martin&lt;gmsoft[AT] tuxicoman.be&gt; Deepti Ragha&lt;dlragha[AT] ncsu.edu&gt; Niels de Vos&lt;ndevos[AT] redhat.com&gt; Clement Marrast&lt;clement.marrast[AT] molex.com&gt; Jacob Nordgren&lt;jnordgren[AT] gmail.com&gt; Rishie Sharma&lt;rishie[AT] kth.se&gt; Richard Stearn&lt;richard[AT] rns - stearn.demon.co.uk&gt; Tobias Rutz&lt;tobias.rutz[AT] work - microwave.de&gt; Michal Labedzki&lt;michal.labedzki[AT] tieto.com&gt; Wido Kelling&lt;kellingwido[AT] aol.com&gt; Kaushal Shah&lt;kshah3[AT] ncsu.edu&gt; Subramanian Ramachandran&lt;sramach6[AT] ncsu.edu&gt; Manuel Hofer&lt;manuel[At] mnlhfr.at&gt; Gaurav Patwardhan&lt;gspatwar[AT] ncsu.edu&gt; Peter Hatina&lt;phatina[AT] redhat.com&gt; Tomasz MoX&lt;desowin[AT] gmail.com&gt; and by : Georgi Guninski&lt;guninski[AT] guninski.com&gt; Jason Copenhaver&lt;jcopenha[AT] typedef.org&gt; Eric Perie&lt;eric.perie[AT] colubris.com&gt; David Yon&lt;yon[AT] tacticalsoftware.com&gt; Marcio Franco&lt;franco.marcio[AT] rd.francetelecom.fr&gt; Kaloian Stoilov&lt;kalkata[AT] yahoo.com&gt; Steven Lass&lt;stevenlass[AT] mail.com&gt; Gregory Stark&lt;gsstark[AT] mit.edu&gt; Darren Steele&lt;steeley[AT] steeley.co.uk&gt; Michael Kopp&lt;michael.kopp[AT] isarnet.de&gt; Bernd Leibing&lt;bernd.leibing[AT] kiz.uni - ulm.de&gt; Chris Heath&lt;chris[AT] heathens.co.nz&gt; Gisle Vanem&lt;gvanem[AT] broadpark.no&gt; Ritchie&lt;ritchie[AT] tipsybottle.com&gt; Aki Immonen&lt;aki.immonen[AT] golftalma.fi&gt; David E.Weekly&lt;david[AT] weekly.org&gt; Steve Ford&lt;sford[AT] geeky - boy.com&gt; Masaki Chikama&lt;masaki - c[AT] is.aist - nara.ac.jp&gt; Mohammad Hanif&lt;mhanif[AT] nexthop.com&gt; Reinhard Speyerer&lt;rspmn[AT] arcor.de&gt; Patrick Kursawe&lt;phosphan[AT] gentoo.org&gt; Arsen Chaloyan&lt;achaloyan[AT] yahoo.com&gt;&lt;melerski[AT] poczta.onet.pl&gt; Arnaud Jacques&lt;webmaster[AT] securiteinfo.com&gt; D.Manzella&lt;manzella[AT] lucent.com&gt; Jari Mustajarvi&lt;jari.mustajarvi[AT] nokia.com&gt; Pierre Juhen&lt;pierre.juhen[AT] wanadoo.fr&gt; David Richards&lt;drichards[AT] alum.mit.edu&gt; Shusaku Ueda&lt;ueda[AT] sra.co.jp&gt; Jonathan Perkins&lt;jonathan.perkins[AT] ipaccess.com&gt; Holger Schurig&lt;h.schurig[AT] mn - logistik.de&gt; Peter J.Creath&lt;peter - ethereal[AT] creath.net&gt; Magnus Hansson&lt;mah[AT] hms.se&gt; Pavel Kankovsky&lt;kan[AT] dcit.cz&gt; Nick Black&lt;dank[AT] reflexsecurity.com&gt; Bill Guyton&lt;guyton[AT] bguyton.com&gt; Chernishov Yury&lt;Chernishov[AT] iskrauraltel.ru&gt; Thomas Palmer&lt;Thomas.Palmer[AT] Gunter.AF.mil&gt; Clinton Work&lt;clinton[AT] scripty.com&gt; Joe Marcus Clarke&lt;marcus[AT] marcuscom.com&gt; Kendy Kutzner&lt;kutzner[AT] tm.uka.de&gt; James H.Cloos Jr.&lt;cloos[AT] jhcloos.com&gt;Tim Farley&lt;tfarley[AT] iss.net&gt; Daniel Thompson&lt;daniel.thompson[AT] st.com&gt; Chris Jepeway&lt;thai - dragon[AT] eleven29.com&gt; Matthew Bradley&lt;matthew.bradley[AT] cnsonline.net&gt; Nathan Alger&lt;nathan[AT] wasted.com&gt; Stas Grabois&lt;sagig[AT] radware.com&gt; Ainsley Pereira&lt;APereira[AT] Witness.com&gt; Philippe Mazeau&lt;philippe.mazeau[AT] swissvoice.net&gt; Carles Kishimoto&lt;ckishimo[AT] ac.upc.es&gt; Dennis Lim&lt;Dennis.Lim[AT] motorola.com&gt;&lt;postadal[AT] suse.cz&gt; Martin van der Werff&lt;martin[AT] vanderwerff.org&gt; Marco van den Bovenkamp&lt;marco[AT] linuxgoeroe.dhs.org&gt; Ming Zhang&lt;mingz[AT] ele.uri.edu&gt; Neil Piercy&lt;Neil.Piercy[AT] ipaccess.com&gt; Remi Denis - Courmont&lt;courmisch[AT] via.ecp.fr&gt; Thomas Palmer&lt;tpalmer[AT] elmore.rr.com&gt; Ma &amp;#176;rten Svantesson    &lt;f95-msv[AT]f.kth.se&gt;
Steve Sommars           (e-mail address removed at contributor's request)
Kestutis Kupciunas      &lt;kesha[AT]soften.ktu.lt&gt;
Rene Pilz               &lt;rene.pilz[AT]ftw.at&gt;
Laurent Constantin      &lt;laurent.constantin[AT]aql.fr&gt;
Martin Pichlmaier       &lt;martin.pichlmaier[AT]siemens.com&gt;
Mark Phillips           &lt;msp[AT]nortelnetworks.com&gt;
Nils Ohlmeier           &lt;lists[AT]ohlmeier.org&gt;
Ignacio Goyret          &lt;igoyret[AT]lucent.com&gt;
Bart Braem              &lt;bart.braem[AT]gmail.com&gt;
Shingo Horisawa         &lt;name4n5[AT]hotmail.com&gt;
Lane Hu                 &lt;lane.hu[AT]utstar.com&gt;
Marc Poulhies           &lt;marc.poulhies[AT]epfl.ch&gt;
Tomasz Mrugalski        &lt;thomson[AT]klub.com.pl&gt;
Brett Kuskie            &lt;mstrprgmmr[AT]chek.com&gt;
Brian Caswell           &lt;bmc[AT]sourcefire.com&gt;
Yann                    &lt;yann_eads[AT]hotmail.com&gt;
Julien Leproust         &lt;julien[AT]via.ecp.fr&gt;
Mutsuya Irie            &lt;irie[AT]sakura-catv.ne.jp&gt;
Yoshihiro Oyama         &lt;y.oyama[AT]netagent.co.jp&gt;
Chris Eagle             &lt;cseagle[AT]nps.edu&gt;
Dominique Bastien       &lt;dbastien[AT]accedian.com&gt;
Nicolas Dichtel         &lt;nicolas.dichtel[AT]6wind.com&gt;
Ricardo Muggli          &lt;ricardo.muggli[AT]mnsu.edu&gt;
Vladimir Kondratiev     &lt;vladimir.kondratiev[AT]gmail.com&gt;
Jaap Keuter             &lt;jaap.keuter[AT]xs4all.nl&gt;
Frederic Peters         &lt;fpeters[AT]debian.org&gt;
Anton Ivanov            &lt;anthony_johnson[AT]mail.ru&gt;
Ilya Konstantinov       &lt;future[AT]shiny.co.il&gt;
Neil Kettle             &lt;mu-b[AT]65535.com&gt;
Steve Karg              &lt;skarg[AT]users.sourceforge.net&gt;
Javier Acuna            &lt;javier.acuna[AT]sixbell.cl&gt;
Miklos Szurdi           &lt;szurdimiklos[AT]yahoo.com&gt;
Cvetan Ivanov           &lt;zezo[AT]spnet.net&gt;
Vasanth Manickam        &lt;vasanth.manickam[AT]bt.com&gt;
Julian Onions           &lt;julian.onions[AT]gmail.com&gt;
Samuel Thibault         &lt;samuel.thibault[AT]ens-lyon.org&gt;
Peter KovaX             &lt;peter.kovar[AT]gmail.com&gt;
Paul Ollis              &lt;paul.ollis[AT]roke.co.uk&gt;
Dominik Kuhlen          &lt;dkuhlen[AT]gmx.net&gt;
Karl Knoebl             &lt;karl.knoebl[AT]siemens.com&gt;
Maria-Luiza Crivat      &lt;luizacri[AT]gmail.com&gt;
Brice Augustin          &lt;bricecotte[AT]gmail.com&gt;
Matt Thornton           &lt;MATT_THORNTON[AT]appsig.com&gt;
Timo Metsala            &lt;timo.metsala[AT]gmail.com&gt;
Tomer Shani             &lt;thetour[AT]japan.com&gt;
Manu Pathak             &lt;mapathak[AT]cisco.com&gt;
John Sullivan           &lt;john[AT]kanargh.force9.co.uk&gt;
Martin Andre            &lt;andre[AT]clarinet.u-strasbg.fr&gt;
Andrei Emeltchenko      &lt;Andrei.Emeltchenko[AT]nokia.com&gt;
Kirby Files             &lt;kfiles[AT]masergy.com&gt;
Ravi Valmikam           &lt;rvalmikam[AT]airvananet.com&gt;
Diego Petteno           &lt;flameeyes[AT]gentoo.org&gt;
Daniel Black            &lt;dragonheart[AT]gentoo.org&gt;
Christoph Werle         &lt;Christoph.Werle[AT]ira.uka.de&gt;
Aaron Christensen       &lt;aaronmf[AT]gmail.com&gt;
Ian Abel                &lt;ianabel[AT]mxtelecom.com&gt;
Bryant Eastham          &lt;beastham[AT]slc.mew.com&gt;
Taner Kurtulus          &lt;taner.kurtulus[AT]tubitak.gov.tr&gt;
Joe Breher              &lt;linux[AT]q-music.com&gt;
Patrick vd Lageweg      &lt;patrick[AT]bitwizard.nl&gt;
Thomas Sillaber         &lt;Thomas.Sillaber[AT]gmx.de&gt;
Mike Davies             &lt;m.davies[AT]btinternet.com&gt;
Boris Misenov           &lt;Boris.Misenov[AT]oktelabs.ru&gt;
Joe McEachern           &lt;joe[AT]qacafe.com&gt;
Charles Lepple          &lt;clepple[AT]gmail.com&gt;
Tuomas Maattanen        &lt;maattanen[AT]iki.fi&gt;
Joe Eykholt             &lt;joe[AT]nuovasystems.com&gt;
Ian Brumby              &lt;ian.brumby[AT]baesystems.com&gt;
Todd J Martin           &lt;todd.martin[AT]acm.org&gt;
Scott Robinson          &lt;scott.robinson[AT]flukenetworks.com&gt;
Martin Peylo            &lt;wireshark[AT]izac.de&gt;
Stephane Loeuillet      &lt;leroutier[AT]gmail.com&gt;
Andrei Rubaniuk         &lt;rubaniuk[AT]mail.ru&gt;
Mikael Magnusson        &lt;mikma264[AT]gmail.com&gt;
Timo Tera.s                &lt;timo.teras[AT]iki.fi&gt;
Marton Nemeth           &lt;nm127[AT]freemail.hu&gt;
Kai Blin                &lt;kai[AT]samba.org&gt;
Olivier Montanuy        &lt;olivier.montanuy[AT]orange-ftgroup.com&gt;
Thomas Morin            &lt;thomas.morin[AT]orange-ftgroup.com&gt;
Jesus Roman             &lt;jroman[AT]teldat.com&gt;
Giodi Giorgi            &lt;g.giorgi[AT]gmail.com&gt;
Peter Hertting          &lt;Peter.Hertting[AT]gmx.net&gt;
Jess Balint             &lt;jbalint[AT]gmail.com&gt;
Bahaa Naamneh           &lt;b.naamneh[AT]gmail.com&gt;
Magnus So.rman             &lt;magnus.sorman[AT]ericsson.com
Pascal Quantin          &lt;pascal.quantin[AT]gmail.com&gt;
Roy Marples             &lt;roy[AT]marples.name&gt;
Ward van Wanrooij       &lt;ward[AT]ward.nu&gt;
Federico Mena Quintero  &lt;federico[AT]novell.com&gt;
Andreas Heise           &lt;andreas.heise[AT]nextiraone.de&gt;
Alex Lindberg           &lt;alindber[AT]yahoo.com&gt;
Rama Chitta             &lt;rama[AT]gear6.com&gt;
Roberto Mariani         &lt;jelot-wireshark[AT]jelot.it&gt;
Sandhya Gopinath        &lt;Sandhya.Gopinath[AT]citrix.com&gt;
Raghav SN               &lt;Raghav.SN[AT]citrix.com&gt;
Murali Raja             &lt;Murali.Raja[AT]citrix.com&gt;
Devesh Prakash          &lt;Devesh.Prakash[AT]citrix.com&gt;
Darryl Champagne        &lt;dchampagne[AT]sta.samsung.com&gt;
Michael Speck           &lt;Michael.Speck[AT]avl.com&gt;
Gerasimos Dimitriadis   &lt;dimeg[AT]intracom.gr&gt;
Robert Simac            &lt;rsimac[AT]cronsult.com&gt;
Johanna Sochos          &lt;johanna.sochos[AT]swissqual.com&gt;
Felix Obenhuber         &lt;felix[AT]obenhuber.de&gt;
Hilko Bengen            &lt;bengen---wireshark[AT]hilluzination.de&gt;
Hadar Shoham            &lt;hadar[AT]ti.com&gt;
Robert Bullen           &lt;robert[AT]bitcricket.com&gt;
Chuck Kristofek         &lt;chuck.kristofek[AT]ngc.com&gt;
Markus Renz             &lt;Markus.Renz[AT]hirschmann.de&gt;
Toshihiro Kataoka       &lt;kataoka.toshihiro[AT]gmail.com&gt;
Petr Lautrbach          &lt;plautrba[AT]redhat.com&gt;
Frank Lahm              &lt;franklahm[AT]googlemail.com&gt;
Jon Ellch               &lt;jellch[AT]harris.com&gt;
Alex Badea              &lt;vamposdecampos[AT]gmail.com&gt;
Dirk Jagdmann           &lt;doj[AT]cubic.org&gt;
RSA                     &lt;ryazanov.s.a[AT]gmail.com&gt;
Juliusz Chroboczek      &lt;jch[AT]pps.jussieu.fr&gt;
Vladimir Kazansky       &lt;vovjo[AT]yandex.ru&gt;
Peter Paluch            &lt;peter.paluch[AT]fri.uniza.sk&gt;
Tom Brezinski           &lt;tombr[AT]netinst.com&gt;
Nick Glass              &lt;nick.glass[AT]lycos.com&gt;
Michael Mann            &lt;mmann78[AT]netscape.net&gt;
Romain Fliedel          &lt;romain.fliedel+wireshark[AT]gmail.com&gt;
Michael Chen            &lt;michaelc[AT]idssoftware.com&gt;
Paul Stath              &lt;pstath[AT]axxcelera.com&gt;
DeCount                 &lt;aatrade[AT]libero.it&gt;
Andras Veres-Szentkiralyi       &lt;vsza[AT]vsza.hu&gt;
Jakob Hirsch            &lt;jh.wireshark-bugzilla[AT]plonk.de&gt;
XXXXX XXXXXXXX          &lt;DXDragon[AT]yandex.ru&gt;
                        &lt;billyjeans[AT]gmail.com&gt;
Evan Huus               &lt;eapache[AT]gmail.com&gt;
Tom Cook                &lt;tcook[AT]ixiacom.com&gt;
Tom Alexander           &lt;talexander[AT]ixiacom.com&gt;
Klaus Heckelmann        &lt;klaus.heckelmann[AT]nashtech.com&gt;
Ben Bowen               &lt;bbowen[AT]godaddy.com&gt;
Bodo Petermann          &lt;bp245[AT]hotmail.com&gt;
Martin Kupec            &lt;martin.kupec[AT]kupson.cz&gt;
Litao Gao               &lt;ltgao[AT]juniper.net&gt;
Niels Widger            &lt;niels[AT]qacafe.com&gt;
Pontus Fuchs            &lt;pontus.fuchs[AT]gmail.com&gt;
Bill Parker             &lt;wp02855[AT]gmail.com&gt;
Tomofumi Hayashi        &lt;s1061123[AT]gmail.com&gt;
Tim Hentenaar           &lt;tim.hentenaar[AT]gmail.com&gt;
Krishnamurthy Mayya     &lt;krishnamurthymayya[AT]gmail.com&gt;
Nikitha Malgi           &lt;nikitha01[AT]gmail.com&gt;
Adam Butcher            &lt;adam[AT]jessamine.co.uk&gt;
Hendrik Uhlmann         &lt;Hendrik.Uhlmann[AT]rheinmetall.com&gt;
Alex Gaertner           &lt;gaertner.alex[AT]gmx.de&gt;
Sebastiano Di Paola     &lt;sebastiano.dipaola[AT]gmail.com&gt;
Steven J. Magnani       &lt;steve[AT]digidescorp.com&gt;
David Arnold            &lt;davida[AT]pobox.com&gt;
Dario Lombardo          &lt;lomato[AT]gmail.com&gt;
Alexander Chemeris      &lt;alexander.chemeris[AT]gmail.com&gt;
Ivan Klyuchnikov        &lt;kluchnikovi[AT]gmail.com&gt;
Max Baker               &lt;max[AT]warped.org&gt;
Mike Garratt            &lt;mg.wireshark[AT]evn.co.nz&gt;
Bart Van Assche         &lt;bvanassche[AT]acm.org&gt;
Karl Beldan                     &lt;karl.beldan[AT]gmail.com&gt;
Masayuki Takemura       &lt;masayuki.takemura[AT]gmail.com&gt;
Dan Lasley &lt;dlasley[AT]promus.com&gt; gave permission for his
dumpit() hex-dump routine to be used.
Mattia Cazzola &lt;mattiac[AT]alinet.it&gt; provided a patch to the
hex dump display routine.
We use the exception module from Kazlib, a C library written by
Kaz Kylheku &lt;kaz[AT]ashi.footprints.net&gt;. Thanks go to him for
his well-written library. The Kazlib home page can be found at
http://users.footprints.net/~kaz/kazlib.html
We use Lua BitOp, written by Mike Pall, for bitwise operations
on numbers in Lua. The Lua BitOp home page can be found at
http://bitop.luajit.org/
Henrik Brix Andersen &lt;brix[AT]gimp.org&gt; gave permission for his
webbrowser calling routine to be used.
Christophe Devine &lt;c.devine[AT]cr0.net&gt; gave permission for his
SHA1 routines to be used.
snax &lt;snax[AT]shmoo.com&gt; gave permission to use his(?) weak key
detection code from Airsnort.
IANA gave permission for their port-numbers file to be used.
</code></pre>
<h2>Index</h2>
<dt><a href="#lbAI">CAPTURE FILTER SYNTAX</a></p>
<dd>
<dt><a href="#lbAJ">DISPLAY FILTER SYNTAX</a></p>
<dd>
<dt><a href="#lbAK">FILES</a></p>
<dd>
<dt><a href="#lbAL">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAM">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAN">NOTES</a></p>
<dd>
<dt><a href="#lbAO">AUTHORS</a></p>
<dd></dl>
