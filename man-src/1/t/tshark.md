---
title: "tshark(1)"
name: "tshark"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tshark/"
description: "tshark – Dump and analyze network traffic"
---

<h2 class="name">NAME</h2>
<p> tshark &#8211; Dump and analyze network traffic </p>
<h2>SYNOPSIS</h2>
<p> <code>tshark</code> [&nbsp;<wbr><code>-2</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-a</code>&nbsp;<wbr>&lt;capture autostop condition&gt;&nbsp;<wbr>]&nbsp;<wbr>&#8230; [&nbsp;<wbr><code>-b</code>&nbsp;<wbr>&lt;capture ring buffer option&gt;]&nbsp;<wbr>&#8230; [&nbsp;<wbr><code>-B</code>&nbsp;<wbr>&lt;capture buffer size&gt;&nbsp;<wbr>]&nbsp;<wbr> [&nbsp;<wbr><code>-c</code>&nbsp;<wbr>&lt;capture packet count&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-C</code>&nbsp;<wbr>&lt;configuration profile&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-d</code>&nbsp;<wbr>&lt;layer type&gt;==&lt;selector&gt;,&lt;decode-as protocol&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-D</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-e</code>&nbsp;<wbr>&lt;field&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-E</code>&nbsp;<wbr>&lt;field print option&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-f</code>&nbsp;<wbr>&lt;capture filter&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-F</code>&nbsp;<wbr>&lt;file format&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-g</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-h</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-H</code>&nbsp;<wbr>&lt;input hosts file&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-i</code>&nbsp;<wbr>&lt;capture interface&gt;|-&nbsp;<wbr>] [&nbsp;<wbr><code>-I</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-K</code>&nbsp;<wbr>&lt;keytab&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-l</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-L</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-n</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-N</code>&nbsp;<wbr>&lt;name resolving flags&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-o</code>&nbsp;<wbr>&lt;preference setting&gt;&nbsp;<wbr>]&nbsp;<wbr>&#8230; [&nbsp;<wbr><code>-O</code>&nbsp;<wbr>&lt;protocols&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-p</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-P</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-q</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-Q</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-r</code>&nbsp;<wbr>&lt;infile&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-R</code>&nbsp;<wbr>&lt;Read filter&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-Y</code>&nbsp;<wbr>&lt;displaY filter&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-s</code>&nbsp;<wbr>&lt;capture snaplen&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-S</code>&nbsp;<wbr>&lt;separator&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-t</code>&nbsp;<wbr>a|ad|d|dd|e|r|u|ud&nbsp;<wbr>] [&nbsp;<wbr><code>-T</code>&nbsp;<wbr>pdml|psml|ps|text|fields&nbsp;<wbr>] [&nbsp;<wbr><code>-v</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-V</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-w</code>&nbsp;<wbr>&lt;outfile&gt;|-&nbsp;<wbr>] [&nbsp;<wbr><code>-W</code>&nbsp;<wbr>&lt;file format option&gt;] [&nbsp;<wbr><code>-x</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-X</code>&nbsp;<wbr>&lt;eXtension option&gt;] [&nbsp;<wbr><code>-y</code>&nbsp;<wbr>&lt;capture link type&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-z</code>&nbsp;<wbr>&lt;statistics&gt;&nbsp;<wbr>] [&nbsp;<wbr>&lt;capture filter&gt;&nbsp;<wbr>] </p>
<p> <code>tshark</code> <code>-G</code> [fields|protocols|values|decodes|defaultprefs|currentprefs]</p>
<h2>DESCRIPTION</h2>
<p> <code>TShark</code> is a network protocol analyzer. It lets you capture packet data from a live network, or read packets from a previously saved capture file, either printing a decoded form of those packets to the standard output or writing the packets to a file. <code>TShark</code>&#8216;s native capture file format is <code>pcap</code> format, which is also the format used by <code>tcpdump</code> and various other tools. </p>
<p> Without any options set, <code>TShark</code> will work much like <code>tcpdump</code>. It will use the pcap library to capture traffic from the first available network interface and displays a summary line on stdout for each received packet. </p>
<p> <code>TShark</code> is able to detect, read and write the same capture files that are supported by <code>Wireshark</code>. The input file doesn&#8217;t need a specific filename extension; the file format and an optional gzip compression will be automatically detected. Near the beginning of the <font SIZE="-1">DESCRIPTION</font> section of <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1) or &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages/wireshark.html">http://www.wireshark.org/docs/man-pages/wireshark.html</a>&gt; is a detailed description of the way <code>Wireshark</code> handles this, which is the same way <code>Tshark</code> handles this. </p>
<p> Compressed file support uses (and therefore requires) the zlib library. If the zlib library is not present, <code>TShark</code> will compile, but will be unable to read compressed files. </p>
<p> If the <code>-w</code> option is not specified, <code>TShark</code> writes to the standard output the text of a decoded form of the packets it captures or reads. If the <code>-w</code> option is specified, <code>TShark</code> writes to the file specified by that option the raw data of the packets, along with the packets&#8217; time stamps. </p>
<p> When writing a decoded form of packets, <code>TShark</code> writes, by default, a summary line containing the fields specified by the preferences file (which are also the fields displayed in the packet list pane in <code>Wireshark</code>), although if it&#8217;s writing packets as it captures them, rather than writing packets from a saved capture file, it won&#8217;t show the &#8220;frame number&#8221; field. If the <code>-V</code> option is specified, it writes instead a view of the details of the packet, showing all the fields of all protocols in the packet. If the <code>-O</code> option is specified, it will only show the full protocols specified. Use the output of &quot;<code>tshark -G protocols</code>&quot; to find the abbreviations of the protocols you can specify. </p>
<p> If you want to write the decoded form of packets to a file, run <code>TShark</code> without the <code>-w</code> option, and redirect its standard output to the file (do <i>not</i> use the <code>-w</code> option). </p>
<p> When writing packets to a file, <code>TShark</code>, by default, writes the file in <code>pcap</code> format, and writes all of the packets it sees to the output file. The <code>-F</code> option can be used to specify the format in which to write the file. This list of available file formats is displayed by the <code>-F</code> flag without a value. However, you can&#8217;t specify a file format for a live capture. </p>
<p> Read filters in <code>TShark</code>, which allow you to select which packets are to be decoded or written to a file, are very powerful; more fields are filterable in <code>TShark</code> than in other protocol analyzers, and the syntax you can use to create your filters is richer. As <code>TShark</code> progresses, expect more and more protocol fields to be allowed in read filters. </p>
<p> Packet capturing is performed with the pcap library. The capture filter syntax follows the rules of the pcap library. This syntax is different from the read filter syntax. A read filter can also be specified when capturing, and only packets that pass the read filter will be displayed or saved to the output file; note, however, that capture filters are much more efficient than read filters, and it may be more difficult for <code>TShark</code> to keep up with a busy network if a read filter is specified for a live capture. </p>
<p> A capture or read filter can either be specified with the <code>-f</code> or <code>-R</code> option, respectively, in which case the entire filter expression must be specified as a single argument (which means that if it contains spaces, it must be quoted), or can be specified with command-line arguments after the option arguments, in which case all the arguments after the filter arguments are treated as a filter expression. Capture filters are supported only when doing a live capture; read filters are supported when doing a live capture and when reading a capture file, but require TShark to do more work when filtering, so you might be more likely to lose packets under heavy load if you&#8217;re using a read filter. If the filter is specified with command-line arguments after the option arguments, it&#8217;s a capture filter if a capture is being done (i.e., if no <code>-r</code> option was specified) and a read filter if a capture file is being read (i.e., if a <code>-r</code> option was specified). </p>
<p> The <code>-G</code> option is a special mode that simply causes <code>Tshark</code> to dump one of several types of internal glossaries and then exit.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-2</p>
<dd> Perform a two-pass analysis. This causes tshark to buffer output until the entire first pass is done, but allows it to fill in fields that require future knowledge, such as &#8216;response in frame #&#8217; fields. Also permits reassembly frame dependencies to be calculated correctly.</p>
<dt>-a &lt;capture autostop condition&gt;</p>
<dd> Specify a criterion that specifies when <code>TShark</code> is to stop writing to a capture file. The criterion is of the form <i>test</i><code>:</code><i>value</i>, where <i>test</i> is one of: </p>
<p> <code>duration</code>:<i>value</i> Stop writing to a capture file after <i>value</i> seconds have elapsed. </p>
<p> <code>filesize</code>:<i>value</i> Stop writing to a capture file after it reaches a size of <i>value</i> kB. If this option is used together with the -b option, <code>TShark</code> will stop writing to the current capture file and switch to the next one if filesize is reached. When reading a capture file, <code>TShark</code> will stop reading the file after the number of bytes read exceeds this number (the complete packet will be read, so more bytes than this number may be read). Note that the filesize is limited to a maximum value of 2 GiB. </p>
<p> <code>files</code>:<i>value</i> Stop writing to capture files after <i>value</i> number of files were written.</p>
<dt>-b &lt;capture ring buffer option&gt;</p>
<dd> Cause <code>TShark</code> to run in &#8220;multiple files&#8221; mode. In &#8220;multiple files&#8221; mode, <code>TShark</code> will write to several capture files. When the first capture file fills up, <code>TShark</code> will switch writing to the next file and so on. </p>
<p> The created filenames are based on the filename given with the <code>-w</code> option, the number of the file and on the creation date and time, e.g. outfile_00001_20050604120117.pcap, outfile_00002_20050604120523.pcap, &#8230; </p>
<p> With the <i>files</i> option it&#8217;s also possible to form a &#8220;ring buffer&#8221;. This will fill up new files until the number of files specified, at which point <code>TShark</code> will discard the data in the first file and start writing to that file and so on. If the <i>files</i> option is not set, new files filled up until one of the capture stop conditions match (or until the disk is full). </p>
<p> The criterion is of the form <i>key</i><code>:</code><i>value</i>, where <i>key</i> is one of: </p>
<p> <code>duration</code>:<i>value</i> switch to the next file after <i>value</i> seconds have elapsed, even if the current file is not completely filled up. </p>
<p> <code>filesize</code>:<i>value</i> switch to the next file after it reaches a size of <i>value</i> kB. Note that the filesize is limited to a maximum value of 2 GiB. </p>
<p> <code>files</code>:<i>value</i> begin again with the first file after <i>value</i> number of files were written (form a ring buffer). This value must be less than 100000. Caution should be used when using large numbers of files: some filesystems do not handle many files in a single directory well. The <code>files</code> criterion requires either <code>duration</code> or <code>filesize</code> to be specified to control when to go to the next file. It should be noted that each <code>-b</code> parameter takes exactly one criterion; to specify two criterion, each must be preceded by the <code>-b</code> option. </p>
<p> Example: <code>-b filesize:1000 -b files:5</code> results in a ring buffer of five files of size one megabyte each.</p>
<dt>-B &lt;capture buffer size&gt;</p>
<dd> Set capture buffer size (in MiB, default is 2 MiB). This is used by the capture driver to buffer packet data until that data can be written to disk. If you encounter packet drops while capturing, try to increase this size. Note that, while <code>Tshark</code> attempts to set the buffer size to 2 MiB by default, and can be told to set it to a larger value, the system or interface on which you&#8217;re capturing might silently limit the capture buffer size to a lower value or raise it to a higher value. </p>
<p> This is available on <font SIZE="-1">UNIX</font> systems with libpcap 1.0.0 or later and on Windows. It is not available on <font SIZE="-1">UNIX</font> systems with earlier versions of libpcap. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default capture buffer size. If used after an <code>-i</code> option, it sets the capture buffer size for the interface specified by the last <code>-i</code> option occurring before this option. If the capture buffer size is not set specifically, the default capture buffer size is used instead.</p>
<dt>-c &lt;capture packet count&gt;</p>
<dd> Set the maximum number of packets to read when capturing live data. If reading a capture file, set the maximum number of packets to read.</p>
<dt>-C &lt;configuration profile&gt;</p>
<dd> Run with the given configuration profile.</p>
<dt>-d &lt;layer type&gt;==&lt;selector&gt;,&lt;decode-as protocol&gt;</p>
<dd> Like Wireshark&#8217;s <code>Decode As&#8230;</code> feature, this lets you specify how a layer type should be dissected. If the layer type in question (for example, <code>tcp.port</code> or <code>udp.port</code> for a <font SIZE="-1">TCP</font> or <font SIZE="-1">UDP</font> port number) has the specified selector value, packets should be dissected as the specified protocol. </p>
<p> Example: <code>-d tcp.port==8888,http</code> will decode any traffic running over <font SIZE="-1">TCP</font> port 8888 as <font SIZE="-1">HTTP.</font> </p>
<p> Example: <code>-d tcp.port==8888:3,http</code> will decode any traffic running over <font SIZE="-1">TCP</font> ports 8888, 8889 or 8890 as <font SIZE="-1">HTTP.</font> </p>
<p> Example: <code>-d tcp.port==8888-8890,http</code> will decode any traffic running over <font SIZE="-1">TCP</font> ports 8888, 8889 or 8890 as <font SIZE="-1">HTTP.</font> </p>
<p> Using an invalid selector or protocol will print out a list of valid selectors and protocol names, respectively. </p>
<p> Example: <code>-d .</code> is a quick way to get a list of valid selectors. </p>
<p> Example: <code>-d ethertype==0x0800.</code> is a quick way to get a list of protocols that can be selected with an ethertype.</p>
<dt>-D</p>
<dd> Print a list of the interfaces on which <code>TShark</code> can capture, and exit. For each network interface, a number and an interface name, possibly followed by a text description of the interface, is printed. The interface name or the number can be supplied to the <code>-i</code> option to specify an interface on which to capture. </p>
<p> This can be useful on systems that don&#8217;t have a command to list them (e.g., Windows systems, or <font SIZE="-1">UNIX</font> systems lacking <code>ifconfig -a</code>); the number can be useful on Windows 2000 and later systems, where the interface name is a somewhat complex string. </p>
<p> Note that &#8220;can capture&#8221; means that <code>TShark</code> was able to open that device to do a live capture. Depending on your system you may need to run tshark from an account with special privileges (for example, as root) to be able to capture network traffic. If <code>TShark -D</code> is not run from such an account, it will not list any interfaces.</p>
<dt>-e &lt;field&gt;</p>
<dd> Add a field to the list of fields to display if <code>-T fields</code> is selected. This option can be used multiple times on the command line. At least one field must be provided if the <code>-T fields</code> option is selected. Column names may be used prefixed with &#8220;col.&#8221; </p>
<p> Example: <code>-e frame.number -e ip.addr -e udp -e col.info</code> </p>
<p> Giving a protocol rather than a single field will print multiple items of data about the protocol as a single field. Fields are separated by tab characters by default. <code>-E</code> controls the format of the printed fields.</p>
<dt>-E &lt;field print option&gt;</p>
<dd> Set an option controlling the printing of fields when <code>-T fields</code> is selected. </p>
<p> Options are: </p>
<p> <code>header=y|n</code> If <code>y</code>, print a list of the field names given using <code>-e</code> as the first line of the output; the field name will be separated using the same character as the field values. Defaults to <code>n</code>. </p>
<p> <code>separator=/t|/s|</code>&lt;character&gt; Set the separator character to use for fields. If <code>/t</code> tab will be used (this is the default), if <code>/s</code>, a single space will be used. Otherwise any character that can be accepted by the command line as part of the option may be used. </p>
<p> <code>occurrence=f|l|a</code> Select which occurrence to use for fields that have multiple occurrences. If <code>f</code> the first occurrence will be used, if <code>l</code> the last occurrence will be used and if <code>a</code> all occurrences will be used (this is the default). </p>
<p> <code>aggregator=,|/s|</code>&lt;character&gt; Set the aggregator character to use for fields that have multiple occurrences. If <code>,</code> a comma will be used (this is the default), if <code>/s</code>, a single space will be used. Otherwise any character that can be accepted by the command line as part of the option may be used. </p>
<p> <code>quote=d|s|n</code> Set the quote character to use to surround fields. <code>d</code> uses double-quotes, <code>s</code> single-quotes, <code>n</code> no quotes (the default).</p>
<dt>-f &lt;capture filter&gt;</p>
<dd> Set the capture filter expression. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default capture filter expression. If used after an <code>-i</code> option, it sets the capture filter expression for the interface specified by the last <code>-i</code> option occurring before this option. If the capture filter expression is not set specifically, the default capture filter expression is used if provided.</p>
<dt>-F &lt;file format&gt;</p>
<dd> Set the file format of the output capture file written using the <code>-w</code> option. The output written with the <code>-w</code> option is raw packet data, not text, so there is no <code>-F</code> option to request text output. The option <code>-F</code> without a value will list the available formats.</p>
<dt>-g</p>
<dd> This option causes the output file(s) to be created with group-read permission (meaning that the output file(s) can be read by other members of the calling user&#8217;s group).</p>
<dt>-G [fields|protocols|values|decodes|defaultprefs|currentprefs]</p>
<dd> The <code>-G</code> option will cause <code>Tshark</code> to dump one of several types of glossaries and then exit. If no specific glossary type is specified, then the <code>fields</code> report will be generated by default. </p>
<p> The available report types include: </p>
<p> <code>fields</code> Dumps the contents of the registration database to stdout. An independent program can take this output and format it into nice tables or <font SIZE="-1">HTML</font> or whatever. There is one record per line. Each record is either a protocol or a header field, differentiated by the first field. The fields are tab-delimited. </p>
<pre><code>
 * Protocols
 * ---------
 * Field 1 = 'P'
 * Field 2 = descriptive protocol name
 * Field 3 = protocol abbreviation
 *
 * Header Fields
 * -------------
 * Field 1 = 'F'
 * Field 2 = descriptive field name
 * Field 3 = field abbreviation
 * Field 4 = type ( textual representation of the ftenum type )
 * Field 5 = parent protocol abbreviation
 * Field 6 = base for display (for integer types); "parent bitfield width" for FT_BOOLEAN
 * Field 7 = bitmask: format: hex: 0x....
 * Field 8 = blurb describing field
</code></pre>
<p> <code>protocols</code> Dumps the protocols in the registration database to stdout. An independent program can take this output and format it into nice tables or <font SIZE="-1">HTML</font> or whatever. There is one record per line. The fields are tab-delimited. </p>
<pre>
 * Field 1 = protocol name
 * Field 2 = protocol short name
 * Field 3 = protocol filter name
</pre>
<p> <code>values</code> Dumps the value_strings, range_strings or true/false strings for fields that have them. There is one record per line. Fields are tab-delimited. There are three types of records: Value String, Range String and True/False String. The first field, &#8216;V&#8217;, &#8216;R&#8217; or &#8216;T&#8217;, indicates the type of record. </p>
<p>*Value Strings * &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -*Field 1 = &#8216;V&#8217; * Field 2 = field abbreviation to which this value string corresponds * Field 3 = Integer value * Field 4 = String *<br />
                                                                                                                                                               *Range Strings * &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -*Field 1 = &#8216;R&#8217; * Field 2 = field abbreviation to which this range string corresponds * Field 3 = Integer value : lower bound * Field 4 = Integer value : upper bound * Field 5 = String *<br />
                                                                                                                                                                                                                                                                                                                                                                                    *True / False Strings * &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;*Field 1 = &#8216;T&#8217; * Field 2 = field abbreviation to which this true / false string corresponds * Field 3 = True String * Field 4 = False String</p>
<p> <code>decodes</code> Dumps the &#8220;layer type&#8221;/&#8220;decode as&#8221; associations to stdout. There is one record per line. The fields are tab-delimited. </p>
<pre>
 * Field 1 = layer type, e.g. &quot;tcp.port&quot;
 * Field 2 = selector in decimal
 * Field 3 = &quot;decode as&quot; name, e.g. &quot;http&quot;
</pre>
<p> <code>defaultprefs</code> Dumps a default preferences file to stdout. </p>
<p> <code>currentprefs</code> Dumps a copy of the current preferences file to stdout.</p>
<dt>-h</p>
<dd> Print the version and options and exits.</p>
<dt>-H &lt;input hosts file&gt;</p>
<dd> Read a list of entries from a &#8220;hosts&#8221; file, which will then be written to a capture file. Implies <code>-W n</code>. Can be called multiple times. </p>
<p> The &#8220;hosts&#8221; file format is documented at &lt;<a rel="nofollow" href="http://en.wikipedia.org/wiki/Hosts_(file)">http://en.wikipedia.org/wiki/Hosts_(file)</a>&gt;.</p>
<dt>-i &lt;capture interface&gt; | &#8211;</p>
<dd> Set the name of the network interface or pipe to use for live packet capture. </p>
<p> Network interface names should match one of the names listed in &quot;<code>tshark -D</code>&#8220; (described above); a number, as reported by &#8221;<code>tshark -D</code>&#8220;, can also be used. If you&#8217;re using <font SIZE="-1">UNIX, &#8221;</font><code>netstat -i</code>&#8220; or &#8221;<code>ifconfig -a</code>&quot; might also work to list interface names, although not all versions of <font SIZE="-1">UNIX</font> support the <code>-a</code> option to <code>ifconfig</code>. </p>
<p> If no interface is specified, <code>TShark</code> searches the list of interfaces, choosing the first non-loopback interface if there are any non-loopback interfaces, and choosing the first loopback interface if there are no non-loopback interfaces. If there are no interfaces at all, <code>TShark</code> reports an error and doesn&#8217;t start the capture. </p>
<p> Pipe names should be either the name of a <font SIZE="-1">FIFO </font>(named pipe) or &#8220;-&#8221; to read data from the standard input. Data read from pipes must be in standard pcap format. </p>
<p> This option can occur multiple times. When capturing from multiple interfaces, the capture file will be saved in pcap-ng format. </p>
<p> Note: the Win32 version of <code>TShark</code> doesn&#8217;t support capturing from pipes!</p>
<dt>-I</p>
<dd> Put the interface in &#8220;monitor mode&#8221;; this is supported only on <font SIZE="-1">IEEE 802.11</font> Wi-Fi interfaces, and supported only on some operating systems. </p>
<p> Note that in monitor mode the adapter might disassociate from the network with which it&#8217;s associated, so that you will not be able to use any wireless networks with that adapter. This could prevent accessing files on a network server, or resolving host names or network addresses, if you are capturing in monitor mode and are not connected to another network with another adapter. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it enables the monitor mode for all interfaces. If used after an <code>-i</code> option, it enables the monitor mode for the interface specified by the last <code>-i</code> option occurring before this option.</p>
<dt>-K &lt;keytab&gt;</p>
<dd> Load kerberos crypto keys from the specified keytab file. This option can be used multiple times to load keys from several files. </p>
<p> Example: <code>-K krb5.keytab</code></p>
<dt>-l</p>
<dd> Flush the standard output after the information for each packet is printed. (This is not, strictly speaking, line-buffered if <code>-V</code> was specified; however, it is the same as line-buffered if <code>-V</code> wasn&#8217;t specified, as only one line is printed for each packet, and, as <code>-l</code> is normally used when piping a live capture to a program or script, so that output for a packet shows up as soon as the packet is seen and dissected, it should work just as well as true line-buffering. We do this as a workaround for a deficiency in the Microsoft Visual C<font SIZE="-2">++</font> C library.) </p>
<p> This may be useful when piping the output of <code>TShark</code> to another program, as it means that the program to which the output is piped will see the dissected data for a packet as soon as <code>TShark</code> sees the packet and generates that output, rather than seeing it only when the standard output buffer containing that data fills up.</p>
<dt>-L</p>
<dd> List the data link types supported by the interface and exit. The reported link types can be used for the <code>-y</code> option.</p>
<dt>-n</p>
<dd> Disable network object name resolution (such as hostname, <font SIZE="-1">TCP</font> and <font SIZE="-1">UDP</font> port names); the <code>-N</code> flag might override this one.</p>
<dt>-N &lt;name resolving flags&gt;</p>
<dd> Turn on name resolving only for particular types of addresses and port numbers, with name resolving for other types of addresses and port numbers turned off. This flag overrides <code>-n</code> if both <code>-N</code> and <code>-n</code> are present. If both <code>-N</code> and <code>-n</code> flags are not present, all name resolutions are turned on. </p>
<p> The argument is a string that may contain the letters: </p>
<p> <code>m</code> to enable <font SIZE="-1">MAC</font> address resolution </p>
<p> <code>n</code> to enable network address resolution </p>
<p> <code>N</code> to enable using external resolvers (e.g., <font SIZE="-1">DNS</font>) for network address resolution </p>
<p> <code>t</code> to enable transport-layer port number resolution </p>
<p> <code>C</code> to enable concurrent (asynchronous) <font SIZE="-1">DNS</font> lookups</p>
<dt>-o &lt;preference&gt;:&lt;value&gt;</p>
<dd> Set a preference value, overriding the default value and any value read from a preference file. The argument to the option is a string of the form <i>prefname</i><code>:</code><i>value</i>, where <i>prefname</i> is the name of the preference (which is the same name that would appear in the preference file), and <i>value</i> is the value to which it should be set.</p>
<dt>-O &lt;protocols&gt;</p>
<dd> Similar to the <code>-V</code> option, but causes <code>TShark</code> to only show a detailed view of the comma-separated list of <i>protocols</i> specified, rather than a detailed view of all protocols. Use the output of &quot;<code>tshark -G protocols</code>&quot; to find the abbreviations of the protocols you can specify.</p>
<dt>-p</p>
<dd> <i>Don&#8217;t</i> put the interface into promiscuous mode. Note that the interface might be in promiscuous mode for some other reason; hence, <code>-p</code> cannot be used to ensure that the only traffic that is captured is traffic sent to or from the machine on which <code>TShark</code> is running, broadcast traffic, and multicast traffic to addresses received by that machine. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, no interface will be put into the promiscuous mode. If used after an <code>-i</code> option, the interface specified by the last <code>-i</code> option occurring before this option will not be put into the promiscuous mode.</p>
<dt>-P</p>
<dd> Decode and display the packet summary, even if writing raw packet data using the <code>-w</code> option.</p>
<dt>-q</p>
<dd> When capturing packets, don&#8217;t display the continuous count of packets captured that is normally shown when saving a capture to a file; instead, just display, at the end of the capture, a count of packets captured. On systems that support the <font SIZE="-1">SIGINFO</font> signal, such as various BSDs, you can cause the current count to be displayed by typing your &#8220;status&#8221; character (typically control-T, although it might be set to &#8220;disabled&#8221; by default on at least some BSDs, so you&#8217;d have to explicitly set it to use it). </p>
<p> When reading a capture file, or when capturing and not saving to a file, don&#8217;t print packet information; this is useful if you&#8217;re using a <code>-z</code> option to calculate statistics and don&#8217;t want the packet information printed, just the statistics.</p>
<dt>-Q</p>
<dd> When capturing packets, only display true errors. This outputs less than the <code>-q</code> option, so the interface name and total packet count and the end of a capture are not sent to stderr.</p>
<dt>-r &lt;infile&gt;</p>
<dd> Read packet data from <i>infile</i>, can be any supported capture file format (including gzipped files). It&#8217;s <code>not</code> possible to use named pipes or stdin here!</p>
<dt>-R &lt;Read filter&gt;</p>
<dd> Cause the specified filter (which uses the syntax of read/display filters, rather than that of capture filters) to be applied during the first pass of analysis. Packets not matching the filter are not considered for future passes. Only makes sense with multiple passes, see -2. For regular filtering on single-pass dissect see -Y instead. </p>
<p> Note that forward-looking fields such as &#8216;response in frame #&#8217; cannot be used with this filter, since they will not have been calculate when this filter is applied.</p>
<dt>-Y &lt;displaY filter&gt;</p>
<dd> Cause the specified filter (which uses the syntax of read/display filters, rather than that of capture filters) to be applied before printing a decoded form of packets or writing packets to a file. Packets matching the filter are printed or written to file; packets that the matching packets depend upon (e.g., fragments), are not printed but are written to file; packets not matching the filter nor depended upon are discarded rather than being printed or written. </p>
<p> Use this instead of -R for filtering using single-pass analysis. If doing two-pass analysis (see -2) then only packets matching the read filter (if there is one) will be checked against this filter.</p>
<dt>-s &lt;capture snaplen&gt;</p>
<dd> Set the default snapshot length to use when capturing live data. No more than <i>snaplen</i> bytes of each network packet will be read into memory, or saved to disk. A value of 0 specifies a snapshot length of 65535, so that the full packet is captured; this is the default. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default snapshot length. If used after an <code>-i</code> option, it sets the snapshot length for the interface specified by the last <code>-i</code> option occurring before this option. If the snapshot length is not set specifically, the default snapshot length is used if provided.</p>
<dt>-S &lt;separator&gt;</p>
<dd> Set the line separator to be printed between packets.</p>
<dt>-t a|ad|d|dd|e|r|u|ud</p>
<dd> Set the format of the packet timestamp printed in summary lines. The format can be one of: </p>
<p> <code>a</code> absolute: The absolute time is the actual time the packet was captured, with no date displayed </p>
<p> <code>ad</code> absolute with date: The absolute date and time is the actual time and date the packet was captured </p>
<p> <code>d</code> delta: The delta time is the time since the previous packet was captured </p>
<p> <code>dd</code> delta_displayed: The delta_displayed time is the time since the previous displayed packet was captured </p>
<p> <code>e</code> epoch: The time in seconds since epoch (Jan 1, 1970 00:00:00) </p>
<p> <code>r</code> relative: The relative time is the time elapsed between the first packet and the current packet </p>
<p> <code>u</code> <font SIZE="-1">UTC:</font> The <font SIZE="-1">UTC</font> time is the actual time the packet was captured, with no date displayed </p>
<p> <code>ud</code> <font SIZE="-1">UTC</font> with date: The <font SIZE="-1">UTC</font> date and time is the actual time and date the packet was captured </p>
<p> The default format is relative.</p>
<dt>-T pdml|psml|ps|text|fields</p>
<dd> Set the format of the output when viewing decoded packet data. The options are one of: </p>
<p> <code>pdml</code> Packet Details Markup Language, an XML-based format for the details of a decoded packet. This information is equivalent to the packet details printed with the <code>-V</code> flag. </p>
<p> <code>psml</code> Packet Summary Markup Language, an XML-based format for the summary information of a decoded packet. This information is equivalent to the information shown in the one-line summary printed by default. </p>
<p> <code>ps</code> PostScript for a human-readable one-line summary of each of the packets, or a multi-line view of the details of each of the packets, depending on whether the <code>-V</code> flag was specified. </p>
<p> <code>text</code> Text of a human-readable one-line summary of each of the packets, or a multi-line view of the details of each of the packets, depending on whether the <code>-V</code> flag was specified. This is the default. </p>
<p> <code>fields</code> The values of fields specified with the <code>-e</code> option, in a form specified by the <code>-E</code> option. For example, </p>
<pre>
  -T fields -E separator=, -E quote=d
</pre>
<p> would generate comma-separated values (<font SIZE="-1">CSV</font>) output suitable for importing into your favorite spreadsheet program.</p>
<dt>-v</p>
<dd> Print the version and exit.</p>
<dt>-V</p>
<dd> Cause <code>TShark</code> to print a view of the packet details.</p>
<dt>-w &lt;outfile&gt; | &#8211;</p>
<dd> Write raw packet data to <i>outfile</i> or to the standard output if <i>outfile</i> is &#8216;-&#8216;. </p>
<p> <font SIZE="-1">NOTE:</font> -w provides raw packet data, not text. If you want text output you need to redirect stdout (e.g. using &#8216;&gt;&#8217;), don&#8217;t use the <code>-w</code> option for this.</p>
<dt>-W &lt;file format option&gt;</p>
<dd> Save extra information in the file if the format supports it. For example, </p>
<pre>
  -F pcapng -W n
</pre>
<p> will save host name resolution records along with captured packets. </p>
<p> Future versions of Wireshark may automatically change the capture format to <code>pcapng</code> as needed. </p>
<p> The argument is a string that may contain the following letter: </p>
<p> <code>n</code> write network address resolution information (pcapng only)</p>
<dt>-x</p>
<dd> Cause <code>TShark</code> to print a hex and <font SIZE="-1">ASCII</font> dump of the packet data after printing the summary and/or details, if either are also being displayed.</p>
<dt>-X &lt;eXtension options&gt;</p>
<dd> Specify an option to be passed to a <code>TShark</code> module. The eXtension option is in the form <i>extension_key</i><code>:</code><i>value</i>, where <i>extension_key</i> can be: </p>
<p> <code>lua_script</code>:<i>lua_script_filename</i> tells <code>Wireshark</code> to load the given script in addition to the default Lua scripts.</p>
<dt>-y &lt;capture link type&gt;</p>
<dd> Set the data link type to use while capturing packets. The values reported by <code>-L</code> are the values that can be used. </p>
<p> This option can occur multiple times. If used before the first occurrence of the <code>-i</code> option, it sets the default capture link type. If used after an <code>-i</code> option, it sets the capture link type for the interface specified by the last <code>-i</code> option occurring before this option. If the capture link type is not set specifically, the default capture link type is used if provided.</p>
<dt>-z &lt;statistics&gt;</p>
<dd> Get <code>TShark</code> to collect various types of statistics and display the result after finishing reading the capture file. Use the <code>-q</code> flag if you&#8217;re reading a capture file and only want the statistics printed, not any per-packet information. </p>
<p> Note that the <code>-z proto</code> option is different &#8211; it doesn&#8217;t cause statistics to be gathered and printed when the capture is complete, it modifies the regular packet summary output to include the values of fields specified with the option. Therefore you must not use the <code>-q</code> option, as that option would suppress the printing of the regular packet summary output, and must also not use the <code>-V</code> option, as that would cause packet detail information rather than packet summary information to be printed. </p>
<p> Currently implemented statistics are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-z help</code></p>
<dd> Display all possible values for <code>-z</code>.</p>
<dt><code>-z</code> afp,srt[,<i>filter</i>]</p>
<dd>
<dt><code>-z</code> camel,srt</p>
<dd>
<dt><code>-z</code> compare,<i>start</i>,<i>stop</i>,<i>ttl[0|1]</i>,<i>order[0|1]</i>,<i>variance</i>[,<i>filter</i>]</p>
<dd> If the optional <i>filter</i> is specified, only those packets that match the filter will be used in the calculations.</p>
<dt><code>-z</code> conv,<i>type</i>[,<i>filter</i>]</p>
<dd> Create a table that lists all conversations that could be seen in the capture. <i>type</i> specifies the conversation endpoint types for which we want to generate the statistics; currently the supported ones are: </p>
<pre>
  &quot;eth&quot;   Ethernet addresses
  &quot;fc&quot;    Fibre Channel addresses
  &quot;fddi&quot;  FDDI addresses
  &quot;ip&quot;    IPv4 addresses
  &quot;ipv6&quot;  IPv6 addresses
  &quot;ipx&quot;   IPX addresses
  &quot;tcp&quot;   TCP/IP socket pairs  Both IPv4 and IPv6 are supported
  &quot;tr&quot;    Token Ring addresses
  &quot;udp&quot;   UDP/IP socket pairs  Both IPv4 and IPv6 are supported
</pre>
<p> If the optional <i>filter</i> is specified, only those packets that match the filter will be used in the calculations. </p>
<p> The table is presented with one line for each conversation and displays the number of packets/bytes in each direction as well as the total number of packets/bytes. The table is sorted according to the total number of frames.</p>
<dt><code>-z</code> dcerpc,srt,<i>uuid</i>,<i>major</i>.<i>minor</i>[,<i>filter</i>]</p>
<dd> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">DCERPC</font> interface <i>uuid</i>, version <i>major</i>.<i>minor</i>. Data collected is the number of calls for each procedure, MinSRT, MaxSRT and AvgSRT. </p>
<p> Example: <code>-z dcerpc,srt,12345778-1234-abcd-ef00-0123456789ac,1.0</code> will collect data for the <font SIZE="-1">CIFS SAMR</font> Interface. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z dcerpc,srt,12345778-1234-abcd-ef00-0123456789ac,1.0,ip.addr==1.2.3.4</code> will collect <font SIZE="-1">SAMR SRT</font> statistics for a specific host.</p>
<dt><code>-z</code> diameter,avp[,<i>cmd.code</i>,<i>field</i>,<i>field</i>,<i>&#8230;</i>]</p>
<dd> This option enables extraction of most important diameter fields from large capture files. Exactly one text line for each diameter message with matched <code>diameter.cmd.code</code> will be printed. </p>
<p> Empty diameter command code or &#8216;*&#8217; can be specified to mach any <code>diameter.cmd.code</code> </p>
<p> Example: <code>-z diameter,avp</code> extract default field set from diameter messages. </p>
<p> Example: <code>-z diameter,avp,280</code> extract default field set from diameter <font SIZE="-1">DWR</font> messages. </p>
<p> Example: <code>-z diameter,avp,272</code> extract default field set from diameter <font SIZE="-1">CC</font> messages. </p>
<p> Extract most important fields from diameter <font SIZE="-1">CC</font> messages: </p>
<p> <code>tshark -r file.cap.gz -q -z diameter,avp,272,CC-Request-Type,CC-Request-Number,Session-Id,Subscription-Id-Data,Rating-Group,Result-Code</code> </p>
<p> Following fields will be printed out for each diameter message: </p>
<p>  &#8220;frame&#8221;        Frame number.<br />
  &#8220;time&#8221;         Unix time of the frame arrival.<br />
  &#8220;src&#8221;          Source address.<br />
  &#8220;srcport&#8221;      Source port.<br />
  &#8220;dst&#8221;          Destination address.<br />
  &#8220;dstport&#8221;      Destination port.<br />
  &#8220;proto&#8221;        Constant string &#8216;diameter&#8217;, which can be used for post processing of tshark output.  E.g. grep/sed/awk.<br />
  &#8220;msgnr&#8221;        seq. number of diameter message within the frame.  E.g. &#8216;2&#8217; for the third diameter message in the same frame.<br />
  &#8220;is_request&#8221;   &#8216;0&#8217; if message is a request, &#8216;1&#8217; if message is an answer.<br />
  &#8220;cmd&#8221;          diameter.cmd_code, E.g. &#8216;272&#8217; for credit control messages.<br />
  &#8220;req_frame&#8221;    Number of frame where matched request was found or &#8216;0&#8217;.<br />
  &#8220;ans_frame&#8221;    Number of frame where matched answer was found or &#8216;0&#8217;.<br />
  &#8220;resp_time&#8221;    response time in seconds, &#8216;0&#8217; in case if matched Request/Answer is not found in trace.  E.g. in the begin or end of capture.</p>
<p> <code>-z diameter,avp</code> option is much faster than <code>-V -T text</code> or <code>-T pdml</code> options. </p>
<p> <code>-z diameter,avp</code> option is more powerful than <code>-T field</code> and <code>-z proto,colinfo</code> options. </p>
<p> Multiple diameter messages in one frame are supported. </p>
<p> Several fields with same name within one diameter message are supported, e.g. <i>diameter.Subscription-Id-Data</i> or <i>diameter.Rating-Group</i>. </p>
<p> Note: <code>tshark -q</code> option is recommended to suppress default <code>tshark</code> output.</p>
<dt><code>-z</code> expert[<i>,error|,warn|,note|,chat</i>][<i>,filter</i>]</p>
<dd> Collects information about all expert info, and will display them in order, grouped by severity. </p>
<p> Example: <code>-z expert,sip</code> will show expert items of all severity for frames that match the sip protocol. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z &#8220;expert,note,tcp&#8221;</code> will only collect expert items for frames that include the tcp protocol, with a severity of note or higher.</p>
<dt><code>-z</code> follow,<i>prot</i>,<i>mode</i>,<i>filter</i>[<i>,range</i>]</p>
<dd> Displays the contents of a <font SIZE="-1">TCP</font> or <font SIZE="-1">UDP</font> stream between two nodes. The data sent by the second node is prefixed with a tab to differentiate it from the data sent by the first node. </p>
<p> <i>prot</i> specifies the transport protocol. It can be one of:<br />
&nbsp;<wbr>&nbsp;<wbr><code>tcp</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">TCP<br />
&nbsp;<wbr>&nbsp;<wbr></font><code>udp</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">UDP<br />
&nbsp;<wbr>&nbsp;<wbr></font><code>ssl</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">SSL</font> </p>
<p> <i>mode</i> specifies the output mode. It can be one of:<br />
&nbsp;<wbr>&nbsp;<wbr><code>ascii</code>&nbsp;<wbr><font SIZE="-1">ASCII</font>&nbsp;<wbr>output with dots for non-printable characters<br />
&nbsp;<wbr>&nbsp;<wbr><code>hex</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hexadecimal and&nbsp;<wbr><font SIZE="-1">ASCII</font>&nbsp;<wbr>data with offsets<br />
&nbsp;<wbr>&nbsp;<wbr><code>raw</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hexadecimal data </p>
<p> Since the output in <code>ascii</code> mode may contain newlines, the length of each section of output plus a newline precedes each section of output. </p>
<p> <i>filter</i> specifies the stream to be displayed. <font SIZE="-1">UDP</font> streams are selected with <font SIZE="-1">IP</font> address plus port pairs. <font SIZE="-1">TCP</font> streams are selected with either the stream index or <font SIZE="-1">IP</font> address plus port pairs. For example:<br />
&nbsp;<wbr>&nbsp;<wbr><code>ip-addr0</code>:<code>port0</code>,<code>ip-addr1</code>:<code>port1</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>tcp-stream-index</code> </p>
<p> <i>range</i> optionally specifies which &#8220;chunks&#8221; of the stream should be displayed. </p>
<p> Example: <code>-z &#8220;follow,tcp,hex,1&#8221;</code> will display the contents of the first <font SIZE="-1">TCP</font> stream in &#8220;hex&#8221; format. </p>
<p>== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =<br />
                                                                                                       Follow : tcp,<br />
                                                                                                hex<br />
                                                                                                    Filter : tcp.stream eq 1 Node 0 : 200.57.7.197 : 32891 Node 1 : 200.57.7.198 : 2906 00000000 00 00 00 22 00 00 00 07 00 0a 85 02 07 e9 00 02 &#8230; &#8220;&#8230;. &#8230;&#8230;..<br />
                                                                                                             00000010 07 e9 06 0f 00 0d 00 04 00 00 00 01 00 03 00 06 &#8230;&#8230;&#8230;&#8230;&#8230;.00000020 1f 00 06 04 00 00 &#8230;&#8230; 00000000 00 01 00 00 &#8230;.00000026 00 02 00 00</p>
<p> Example: <code>-z &#8220;follow,tcp,ascii,200.57.7.197:32891,200.57.7.198:2906&#8221;</code> will display the contents of a <font SIZE="-1">TCP</font> stream between 200.57.7.197 port 32891 and 200.57.7.98 port 2906. </p>
<p>  ===================================================================<br />
  Follow: tcp,ascii<br />
  Filter: (ommitted for readability)<br />
  Node 0: 200.57.7.197:32891<br />
  Node 1: 200.57.7.198:2906<br />
  38<br />
  &#8230;&#8221;&#8230;..<br />
  &#8230;&#8230;&#8230;&#8230;&#8230;.<br />
      4<br />
      &#8230;.</p>
<dt><code>-z</code> h225,counter[<i>,filter</i>]</p>
<dd> Count ITU-T H.225 messages and their reasons. In the first column you get a list of H.225 messages and H.225 message reasons, which occur in the current capture file. The number of occurrences of each message or reason is displayed in the second column. </p>
<p> Example: <code>-z h225,counter</code>. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. Example: use <code>-z &#8220;h225,counter,ip.addr==1.2.3.4&#8221;</code> to only collect stats for H.225 packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 . </p>
<p> This option can be used multiple times on the command line.</p>
<dt><code>-z</code> h225,srt[<i>,filter</i>]</p>
<dd> Collect requests/response <font SIZE="-1">SRT </font>(Service Response Time) data for ITU-T H.225 <font SIZE="-1">RAS.</font> Data collected is number of calls of each ITU-T H.225 <font SIZE="-1">RAS</font> Message Type, Minimum <font SIZE="-1">SRT,</font> Maximum <font SIZE="-1">SRT,</font> Average <font SIZE="-1">SRT,</font> Minimum in Packet, and Maximum in Packet. You will also get the number of Open Requests (Unresponded Requests), Discarded Responses (Responses without matching request) and Duplicate Messages. </p>
<p> Example: <code>-z h225,srt</code> </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z &#8220;h225,srt,ip.addr==1.2.3.4&#8221;</code> will only collect stats for ITU-T H.225 <font SIZE="-1">RAS</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 .</p>
<dt><code>-z</code> hosts[,ipv4][,ipv6]</p>
<dd> Dump any collected IPv4 and/or IPv6 addresses in &#8220;hosts&#8221; format. Both IPv4 and IPv6 addresses are dumped by default. </p>
<p> Addresses are collected from a number of sources, including standard &#8220;hosts&#8221; files and captured traffic.</p>
<dt><code>-z</code> http,stat,</p>
<dd> Calculate the <font SIZE="-1">HTTP</font> statistics distribution. Displayed values are the <font SIZE="-1">HTTP</font> status codes and the <font SIZE="-1">HTTP</font> request methods.</p>
<dt><code>-z</code> http,tree</p>
<dd> Calculate the <font SIZE="-1">HTTP</font> packet distribution. Displayed values are the <font SIZE="-1">HTTP</font> request modes and the <font SIZE="-1">HTTP</font> status codes.</p>
<dt><code>-z</code> http_req,tree</p>
<dd> Calculate the <font SIZE="-1">HTTP</font> requests by server. Displayed values are the server name and the <font SIZE="-1">URI</font> path.</p>
<dt><code>-z</code> http_srv,tree</p>
<dd> Calculate the <font SIZE="-1">HTTP</font> requests and responses by server. For the <font SIZE="-1">HTTP</font> requests, displayed values are the server <font SIZE="-1">IP</font> address and server hostname. For the <font SIZE="-1">HTTP</font> responses, displayed values are the server <font SIZE="-1">IP</font> address and status.</p>
<dt><code>-z</code> icmp,srt[,<i>filter</i>]</p>
<dd> Compute total <font SIZE="-1">ICMP</font> echo requests, replies, loss, and percent loss, as well as minimum, maximum, mean, median and sample standard deviation <font SIZE="-1">SRT</font> statistics typical of what ping provides. </p>
<p> Example: <code>-z icmp,srt,ip.src==1.2.3.4</code> will collect <font SIZE="-1">ICMP SRT</font> statistics for <font SIZE="-1">ICMP</font> echo request packets originating from a specific host. </p>
<p> This option can be used multiple times on the command line.</p>
<dt><code>-z</code> icmpv6,srt[,<i>filter</i>]</p>
<dd> Compute total ICMPv6 echo requests, replies, loss, and percent loss, as well as minimum, maximum, mean, median and sample standard deviation <font SIZE="-1">SRT</font> statistics typical of what ping provides. </p>
<p> Example: <code>-z icmpv6,srt,ipv6.src==fe80::1</code> will collect ICMPv6 <font SIZE="-1">SRT</font> statistics for ICMPv6 echo request packets originating from a specific host. </p>
<p> This option can be used multiple times on the command line.</p>
<dt><code>-z</code> io,phs[,<i>filter</i>]</p>
<dd> Create Protocol Hierarchy Statistics listing both number of packets and bytes. If no <i>filter</i> is specified the statistics will be calculated for all packets. If a <i>filter</i> is specified statistics will only be calculated for those packets that match the filter. </p>
<p> This option can be used multiple times on the command line.</p>
<dt><code>-z</code> io,stat,<i>interval</i>[,<i>filter</i>][,<i>filter</i>][,<i>filter</i>]&#8230;</p>
<dd> Collect packet/bytes statistics for the capture in intervals of <i>interval</i> seconds. <i>Interval</i> can be specified either as a whole or fractional second and can be specified with microsecond (us) resolution. If <i>interval</i> is 0, the statistics will be calculated over all packets. </p>
<p> If no <i>filter</i> is specified the statistics will be calculated for all packets. If one or more <i>filters</i> are specified statistics will be calculated for all filters and presented with one column of statistics for each filter. </p>
<p> This option can be used multiple times on the command line. </p>
<p> Example: <code>-z io,stat,1,ip.addr==1.2.3.4</code> will generate 1 second statistics for all traffic to/from host 1.2.3.4. </p>
<p> Example: <code>-z &#8220;io,stat,0.001,smb&amp;&amp;ip.addr==1.2.3.4&#8221;</code> will generate 1ms statistics for all <font SIZE="-1">SMB</font> packets to/from host 1.2.3.4. </p>
<p> The examples above all use the standard syntax for generating statistics which only calculates the number of packets and bytes in each interval. </p>
<p> <code>io,stat</code> can also do much more statistics and calculate <font SIZE="-1"><i>COUNT</i></font><i>()</i>, <font SIZE="-1"><i>SUM</i></font><i>()</i>, <font SIZE="-1"><i>MIN</i></font><i>()</i>, <font SIZE="-1"><i>MAX</i></font><i>()</i>, <font SIZE="-1"><i>AVG</i></font><i>()</i> and <font SIZE="-1"><i>LOAD</i></font><i>()</i> using a slightly different filter syntax:</p>
<dt>-z io,stat,<i>interval</i>,&quot;[COUNT|SUM|MIN|MAX|AVG|LOAD](<i>field</i>)<i>field</i> [and <i>filter</i>]&quot;</p>
<dd> <font SIZE="-1">NOTE:</font> One important thing to note here is that the field that the calculation is based on <font SIZE="-1">MUST</font> also be part of the filter string or else the calculation will fail. </p>
<p> So: <code>-z io,stat,0.010,AVG(smb.time)</code> does not work. Use <code>-z io,stat,0.010,AVG(smb.time)smb.time</code> instead. Also be aware that a field can exist multiple times inside the same packet and will then be counted multiple times in those packets. </p>
<p> <font SIZE="-1">NOTE: A</font> second important thing to note is that the system setting for decimal separator is set to &#8220;.&#8221;! If it is set to &#8220;,&#8221; the statistics will not be displayed per filter. </p>
<p> <font SIZE="-1"><code>COUNT</code></font><code>(</code>field<code>)</code>field<code> [and </code>filter<code>]</code> &#8211; Calculates the number of times that the field <i>name</i> (not its value) appears per interval in the filtered packet list. &#8221;<i>field</i>&#8221; can be any display filter name. </p>
<p> Example: <code>-z io,stat,0.010,&#8220;</code><font SIZE="-1"><code>COUNT</code></font><code>(smb.sid)smb.sid&#8221;</code> </p>
<p> This will count the total number of SIDs seen in each 10ms interval. </p>
<p> <font SIZE="-1"><code>SUM</code></font><code>(</code>field<code>)</code>field<code> [and </code>filter<code>]</code> &#8211; Unlike <font SIZE="-1">COUNT,</font> the <i>values</i> of the specified field are summed per time interval. &#8221;<i>field</i>&#8221; can only be a named integer, float, double or relative time field. </p>
<p> Example: <code>-z io,stat,0.010,&#8220;</code><font SIZE="-1"><code>SUM</code></font><code>(frame.len)frame.len&#8221;</code> </p>
<p> Reports the total number of bytes that were transmitted bidirectionally in all the packets within a 10 millisecond interval. </p>
<p> <font SIZE="-1"><code>MIN/MAX/AVG</code></font><code>(</code>field<code>)</code>field<code> [and </code>filter<code>]</code> &#8211; The minimum, maximum, or average field value in each interval is calculated. The specified field must be a named integer, float, double or relative time field. For relative time fields, the output is presented in seconds with six decimal digits of precision rounded to the nearest microsecond. </p>
<p> In the following example, the time of the first Read_AndX call, the last Read_AndX response values are displayed and the minimum, maximum, and average Read response times (SRTs) are calculated. <font SIZE="-1">NOTE:</font> If the <font SIZE="-1">DOS</font> command shell line continuation character, &#8221;^&#8221; is used, each line cannot end in a comma so it is placed at the beginning of each continuation line: </p>
<p>tshark &#8211; o tcp.desegment_tcp_streams : FALSE &#8211; n &#8211; q &#8211; r smb_reads.cap &#8211; z io, stat, 0,<br />
    &#8220;MIN(frame.time_relative)frame.time_relative and smb.cmd==0x2e and smb.flags.response==0&#8221;,<br />
    &#8220;MAX(frame.time_relative)frame.time_relative and smb.cmd==0x2e and smb.flags.response==1&#8221;,<br />
    &#8220;MIN(smb.time)smb.time and smb.cmd==0x2e&#8221;,<br />
    &#8220;MAX(smb.time)smb.time and smb.cmd==0x2e&#8221;,<br />
    &#8220;AVG(smb.time)smb.time and smb.cmd==0x2e&#8221; == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==<br />
            IO Statistics<br />
                Column #0 : MIN(frame.time_relative) frame.time_relative and smb.cmd<br />
            == 0x2e and<br />
        smb.flags.response == 0 Column #1 : MAX(frame.time_relative) frame.time_relative and smb.cmd == 0x2e and smb.flags.response == 1 Column #2 : MIN(smb.time) smb.time and smb.cmd == 0x2e Column #3 : MAX(smb.time) smb.time and smb.cmd == 0x2e Column #4 : AVG(smb.time) smb.time and smb.cmd == 0x2e | Column #0 | Column #1 | Column #2 | Column #3 | Column #4 | Time | MIN | MAX | MIN | MAX | AVG | 000.000 &#8211; 0.000000 7.704054 0.000072 0.005539 0.000295 == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==</p>
<p> The following command displays the average <font SIZE="-1">SMB</font> Read response <font SIZE="-1">PDU</font> size, the total number of read <font SIZE="-1">PDU</font> bytes, the average <font SIZE="-1">SMB</font> Write request <font SIZE="-1">PDU</font> size, and the total number of bytes transferred in <font SIZE="-1">SMB</font> Write PDUs: </p>
<p>tshark &#8211; n &#8211; q &#8211; r smb_reads_writes.cap &#8211; z io, stat, 0,<br />
    &#8220;AVG(smb.file.rw.length)smb.file.rw.length and smb.cmd==0x2e and smb.response_to&#8221;,<br />
    &#8220;SUM(smb.file.rw.length)smb.file.rw.length and smb.cmd==0x2e and smb.response_to&#8221;,<br />
    &#8220;AVG(smb.file.rw.length)smb.file.rw.length and smb.cmd==0x2f and not smb.response_to&#8221;,<br />
    &#8220;SUM(smb.file.rw.length)smb.file.rw.length and smb.cmd==0x2f and not smb.response_to&#8221; == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =<br />
                                                                                                                                                                                                                            IO Statistics<br />
                                                                                                                                                                                                                                Column #0 : AVG(smb.file.rw.length) smb.file.rw.length and<br />
                                                                                                                                                                                                                            smb.cmd == 0x2e and smb.response_to Column #1 : SUM(smb.file.rw.length) smb.file.rw.length and smb.cmd == 0x2e and smb.response_to Column #2 : AVG(smb.file.rw.length) smb.file.rw.length and smb.cmd == 0x2f and not smb.response_to Column #3 : SUM(smb.file.rw.length) smb.file.rw.length and smb.cmd == 0x2f and not smb.response_to | Column #0 | Column #1 | Column #2 | Column #3 | Time | AVG | SUM | AVG | SUM | 000.000 &#8211; 30018 28067522 72 3240 == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==<br />
    =</p>
<p> <font SIZE="-1"><code>LOAD</code></font><code>(</code>field<code>)</code>field<code> [and </code>filter<code>]</code> &#8211; The LOAD/Queue-Depth in each interval is calculated. The specified field must be a relative time field that represents a response time. For example smb.time. For each interval the Queue-Depth for the specified protocol is calculated. </p>
<p> The following command displays the average <font SIZE="-1">SMB LOAD. A</font> value of 1.0 represents one I/O in flight. </p>
<p>tshark &#8211; n &#8211; q &#8211; r smb_reads_writes.cap &#8211; z &#8220;io,stat,0.001,LOAD(smb.time)smb.time&#8221; == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==<br />
        IO Statistics<br />
            Interval : 0.001000 secs<br />
                Column #0 : LOAD(smb.time) smb.time<br />
    | Column #0 |<br />
    Time | LOAD |<br />
    0000.000000 &#8211; 0000.001000 1.000000 0000.001000 &#8211; 0000.002000 0.741000 0000.002000 &#8211; 0000.003000 0.000000 0000.003000 &#8211; 0000.004000 1.000000</p>
<p> <font SIZE="-1"><code>FRAMES</code></font><code> | BYTES[()</code>filter<code>]</code> &#8211; Displays the total number of frames or bytes. The filter field is optional but if included it must be prepended with &#8221;()&#8221;. </p>
<p> The following command displays five columns: the total number of frames and bytes (transferred bidirectionally) using a single comma, the same two stats using the <font SIZE="-1">FRAMES</font> and <font SIZE="-1">BYTES</font> subcommands, the total number of frames containing at least one <font SIZE="-1">SMB</font> Read response, and the total number of bytes transmitted to the client (unidirectionally) at <font SIZE="-1">IP</font> address 10.1.0.64. </p>
<pre><code>
tshark - o tcp.desegment_tcp_streams : FALSE - n - q - r smb_reads.cap - z io, stat, 0, , FRAMES, BYTES,
    "FRAMES()smb.cmd==0x2e and smb.response_to", "BYTES()ip.dst==10.1.0.64" == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = IO Statistics Column #0 : Column #1 : FRAMES Column #2 : BYTES Column #3 : FRAMES() smb.cmd == 0x2e and smb.response_to Column #4 : BYTES() ip.dst == 10.1.0.64 | Column #0 | Column #1 | Column #2 | Column #3 | Column #4 | Time | Frames | Bytes | FRAMES | BYTES | FRAMES | BYTES | 000.000 - 33576 29721685 33576 29721685 870 29004801 == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
</code></pre>
<dt><code>-z</code> mac-lte,stat[<i>,filter</i>]</p>
<dd> This option will activate a counter for <font SIZE="-1">LTE MAC</font> messages. You will get information about the maximum number of UEs/TTI, common messages and various counters for each <font SIZE="-1">UE</font> that appears in the log. </p>
<p> Example: <code>-z mac-lte,stat</code>. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated for those frames that match that filter. Example: <code>-z &quot;mac-lte,stat,mac-lte.rnti</code>3000&quot;&gt; will only collect stats for UEs with an assigned <font SIZE="-1">RNTI</font> whose value is more than 3000.</p>
<dt><code>-z</code> megaco,rtd[<i>,filter</i>]</p>
<dd> Collect requests/response <font SIZE="-1">RTD </font>(Response Time Delay) data for <font SIZE="-1">MEGACO. </font>(This is similar to <code>-z smb,srt</code>). Data collected is the number of calls for each known <font SIZE="-1">MEGACO</font> Type, MinRTD, MaxRTD and AvgRTD. Additionally you get the number of duplicate requests/responses, unresponded requests, responses, which don&#8217;t match with any request. Example: <code>-z megaco,rtd</code>. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. Example: <code>-z &#8220;megaco,rtd,ip.addr==1.2.3.4&#8221;</code> will only collect stats for <font SIZE="-1">MEGACO</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 . </p>
<p> This option can be used multiple times on the command line.</p>
<dt><code>-z</code> mgcp,rtd[<i>,filter</i>]</p>
<dd> Collect requests/response <font SIZE="-1">RTD </font>(Response Time Delay) data for <font SIZE="-1">MGCP. </font>(This is similar to <code>-z smb,srt</code>). Data collected is the number of calls for each known <font SIZE="-1">MGCP</font> Type, MinRTD, MaxRTD and AvgRTD. Additionally you get the number of duplicate requests/responses, unresponded requests, responses, which don&#8217;t match with any request. Example: <code>-z mgcp,rtd</code>. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. Example: <code>-z &#8220;mgcp,rtd,ip.addr==1.2.3.4&#8221;</code> will only collect stats for <font SIZE="-1">MGCP</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 .</p>
<dt><code>-z</code> proto,colinfo,<i>filter</i>,<i>field</i></p>
<dd> Append all <i>field</i> values for the packet to the Info column of the one-line summary output. This feature can be used to append arbitrary fields to the Info column in addition to the normal content of that column. <i>field</i> is the display-filter name of a field which value should be placed in the Info column. <i>filter</i> is a filter string that controls for which packets the field value will be presented in the info column. <i>field</i> will only be presented in the Info column for the packets which match <i>filter</i>. </p>
<p> <font SIZE="-1">NOTE:</font> In order for <code>TShark</code> to be able to extract the <i>field</i> value from the packet, <i>field</i> <font SIZE="-1">MUST</font> be part of the <i>filter</i> string. If not, <code>TShark</code> will not be able to extract its value. </p>
<p> For a simple example to add the &#8220;nfs.fh.hash&#8221; field to the Info column for all packets containing the &#8220;nfs.fh.hash&#8221; field, use </p>
<p> <code>-z proto,colinfo,nfs.fh.hash,nfs.fh.hash</code> </p>
<p> To put &#8220;nfs.fh.hash&#8221; in the Info column but only for packets coming from host 1.2.3.4 use: </p>
<p> <code>-z &#8220;proto,colinfo,nfs.fh.hash &amp;&amp; ip.src==1.2.3.4,nfs.fh.hash&#8221;</code> </p>
<p> This option can be used multiple times on the command line.</p>
<dt><code>-z</code> rlc-lte,stat[<i>,filter</i>]</p>
<dd> This option will activate a counter for <font SIZE="-1">LTE RLC</font> messages. You will get information about common messages and various counters for each <font SIZE="-1">UE</font> that appears in the log. </p>
<p> Example: <code>-z rlc-lte,stat</code>. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated for those frames that match that filter. Example: <code>-z &quot;rlc-lte,stat,rlc-lte.ueid</code>3000&quot;&gt; will only collect stats for UEs with a UEId of more than 3000.</p>
<dt><code>-z</code> rpc,programs</p>
<dd> Collect call/reply <font SIZE="-1">SRT</font> data for all known ONC-RPC programs/versions. Data collected is number of calls for each protocol/version, MinSRT, MaxSRT and AvgSRT. This option can only be used once on the command line.</p>
<dt><code>-z</code> rpc,srt,<i>program</i>,<i>version</i>[,<i>filter</i>]</p>
<dd> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <i>program</i>/<i>version</i>. Data collected is number of calls for each procedure, MinSRT, MaxSRT and AvgSRT. </p>
<p> Example: <code>-z rpc,srt,100003,3</code> will collect data for <font SIZE="-1">NFS</font> v3. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z rpc,srt,100003,3,nfs.fh.hash==0x12345678</code> will collect <font SIZE="-1">NFS</font> v3 <font SIZE="-1">SRT</font> statistics for a specific file.</p>
<dt><code>-z</code> rtp,streams</p>
<dd> Collect statistics for all <font SIZE="-1">RTP</font> streams and calculate max. delta, max. and mean jitter and packet loss percentages.</p>
<dt><code>-z</code> scsi,srt,<i>cmdset</i>[,<i>filter</i>]</p>
<dd> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">SCSI</font> commandset <i>cmdset</i>. </p>
<p> Commandsets are 0:SBC 1:SSC 5:MMC </p>
<p> Data collected is the number of calls for each procedure, MinSRT, MaxSRT and AvgSRT. </p>
<p> Example: <code>-z scsi,srt,0</code> will collect data for <font SIZE="-1">SCSI BLOCK COMMANDS </font>(<font SIZE="-1">SBC</font>). </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z scsi,srt,0,ip.addr==1.2.3.4</code> will collect <font SIZE="-1">SCSI SBC SRT</font> statistics for a specific iscsi/ifcp/fcip host.</p>
<dt><code>-z</code> sip,stat[<i>,filter</i>]</p>
<dd> This option will activate a counter for <font SIZE="-1">SIP</font> messages. You will get the number of occurrences of each <font SIZE="-1">SIP</font> Method and of each <font SIZE="-1">SIP</font> Status-Code. Additionally you also get the number of resent <font SIZE="-1">SIP</font> Messages (only for <font SIZE="-1">SIP</font> over <font SIZE="-1">UDP</font>). </p>
<p> Example: <code>-z sip,stat</code>. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. Example: <code>-z &#8220;sip,stat,ip.addr==1.2.3.4&#8221;</code> will only collect stats for <font SIZE="-1">SIP</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 .</p>
<dt><code>-z</code> smb,sids</p>
<dd> When this feature is used <code>TShark</code> will print a report with all the discovered <font SIZE="-1">SID</font> and account name mappings. Only those SIDs where the account name is known will be presented in the table. </p>
<p> For this feature to work you will need to either to enable &#8220;Edit/Preferences/Protocols/SMB/Snoop <font SIZE="-1">SID</font> to name mappings&#8221; in the preferences or you can override the preferences by specifying <code>-o&nbsp;<wbr>&#8220;smb.sid_name_snooping:TRUE&#8221;</code> on the <code>TShark</code> command line. </p>
<p> The current method used by <code>TShark</code> to find the <font SIZE="-1">SID-</font>&gt;name mapping is relatively restricted with a hope of future expansion.</p>
<dt><code>-z</code> smb,srt[,<i>filter</i>]</p>
<dd> Collect call/reply <font SIZE="-1">SRT </font>(Service Response Time) data for <font SIZE="-1">SMB. </font> Data collected is number of calls for each <font SIZE="-1">SMB</font> command, MinSRT, MaxSRT and AvgSRT. </p>
<p> Example: <code>-z smb,srt</code> </p>
<p> The data will be presented as separate tables for all normal <font SIZE="-1">SMB</font> commands, all Transaction2 commands and all <font SIZE="-1">NT</font> Transaction commands. Only those commands that are seen in the capture will have its stats displayed. Only the first command in a xAndX command chain will be used in the calculation. So for common SessionSetupAndX + TreeConnectAndX chains, only the SessionSetupAndX call will be used in the statistics. This is a flaw that might be fixed in the future. </p>
<p> This option can be used multiple times on the command line. </p>
<p> If the optional <i>filter</i> is provided, the stats will only be calculated on those calls that match that filter. </p>
<p> Example: <code>-z &#8220;smb,srt,ip.addr==1.2.3.4&#8221;</code> will only collect stats for <font SIZE="-1">SMB</font> packets exchanged by the host at <font SIZE="-1">IP</font> address 1.2.3.4 .</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>CAPTURE FILTER SYNTAX</h2>
<p> See the manual page of <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or, if that doesn&#8217;t exist, <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8), or, if that doesn&#8217;t exist, &lt;<a rel="nofollow" href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a>&gt;.</p>
<h2>READ FILTER SYNTAX</h2>
<p> For a complete table of protocol and protocol fields that are filterable in <code>TShark</code> see the <i><a href="/docs/linux/man/4-wireshark-filter/">wireshark-filter</a></i>(4) manual page.</p>
<h2>FILES</h2>
<p> These files contains various <code>Wireshark</code> configuration values.</p>
<dl>
<dt>Preferences</p>
<dd> The <i>preferences</i> files contain global (system-wide) and personal preference settings. If the system-wide preference file exists, it is read first, overriding the default settings. If the personal preferences file exists, it is read next, overriding any previous values. Note: If the command line option <code>-o</code> is used (possibly more than once), it will in turn override values from the preferences files. </p>
<p> The preferences settings are in the form <i>prefname</i><code>:</code><i>value</i>, one per line, where <i>prefname</i> is the name of the preference and <i>value</i> is the value to which it should be set; white space is allowed between <code>:</code> and <i>value</i>. A preference setting can be continued on subsequent lines by indenting the continuation lines with white space. A <code>#</code> character starts a comment that runs to the end of the line: </p>
<pre>
  # Capture in promiscuous mode?
  # TRUE or FALSE (case-insensitive).
  capture.prom_mode: TRUE
</pre>
<p> The global preferences file is looked for in the <i>wireshark</i> directory under the <i>share</i> subdirectory of the main installation directory (for example, <i>/usr/local/share/wireshark/preferences</i>) on UNIX-compatible systems, and in the main installation directory (for example, <i>C:\Program Files\Wireshark\preferences</i>) on Windows systems. </p>
<p> The personal preferences file is looked for in <i></i>$HOME<i>/.wireshark/preferences</i> on UNIX-compatible systems and <i></i>%APPDATA<i>%\Wireshark\preferences</i> (or, if <tt>%APPDATA</tt>% isn&#8217;t defined, <i></i>%USERPROFILE<i>%\Application Data\Wireshark\preferences</i>) on Windows systems.</p>
<dt>Disabled (Enabled) Protocols</p>
<dd> The <i>disabled_protos</i> files contain system-wide and personal lists of protocols that have been disabled, so that their dissectors are never called. The files contain protocol names, one per line, where the protocol name is the same name that would be used in a display filter for the protocol: </p>
<pre>
  http
  tcp     # a comment
</pre>
<p> The global <i>disabled_protos</i> file uses the same directory as the global preferences file. </p>
<p> The personal <i>disabled_protos</i> file uses the same directory as the personal preferences file.</p>
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
<dd> The <i>manuf</i> file is used to match the 3-byte vendor portion of a 6-byte hardware address with the manufacturer&#8217;s name; it can also contain well-known <font SIZE="-1">MAC</font> addresses and address ranges specified with a netmask. The format of the file is the same as the <i>ethers</i> files, except that entries of the form: </p>
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
<p> The personal <i>ipxnets</i> file is looked for in the same directory as the personal preferences file.</dl>
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
<dd> If this environment variable is set, <code>TShark</code> will call <i><a href="/docs/linux/man/3-abort/">abort</a></i>(3) when a dissector bug is encountered. <i><a href="/docs/linux/man/3-abort/">abort</a></i>(3) will cause the program to exit abnormally; if you are running <code>TShark</code> in a debugger, it should halt in the debugger and allow inspection of the process, and, if you are not running it in a debugger, it will, on some OSes, assuming your environment is configured correctly, generate a core dump file. This can be useful to developers attempting to troubleshoot a problem with a protocol dissector.</p>
<dt><font SIZE="-1">WIRESHARK_EP_VERIFY_POINTERS</font></p>
<dd> This environment variable, if present, causes certain uses of pointers to be audited to ensure they do not point to memory that is deallocated after each packet has been fully dissected. This can be useful to developers writing or auditing code.</p>
<dt><font SIZE="-1">WIRESHARK_SE_VERIFY_POINTERS</font></p>
<dd> This environment variable, if present, causes certain uses of pointers to be audited to ensure they do not point to memory that is deallocated after when a capture file is closed. This can be useful to developers writing or auditing code.</p>
<dt><font SIZE="-1">WIRESHARK_ABORT_ON_OUT_OF_MEMORY</font></p>
<dd> This environment variable, if present, causes <i><a href="/docs/linux/man/3-abort/">abort</a></i>(3) to be called if certain out-of-memory conditions (which normally result in an exception and an explanatory error message) are experienced. This can be useful to developers debugging out-of-memory conditions.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/4-wireshark-filter/">wireshark-filter</a></i>(4), <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1), <i><a href="/docs/linux/man/1-editcap/">editcap</a></i>(1), <i><a href="/docs/linux/man/3-pcap/">pcap</a></i>(3), <i><a href="/docs/linux/man/1-dumpcap/">dumpcap</a></i>(1), <i><a href="/docs/linux/man/1-text2pcap/">text2pcap</a></i>(1), <i><a href="/docs/linux/man/1-mergecap/">mergecap</a></i>(1), <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8)</p>
<h2>NOTES</h2>
<p> <code>TShark</code> is part of the <code>Wireshark</code> distribution. The latest version of <code>Wireshark</code> can be found at &lt;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&gt;. </p>
<p> <font SIZE="-1">HTML</font> versions of the Wireshark project man pages are available at: &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages">http://www.wireshark.org/docs/man-pages</a>&gt;.</p>
<h2>AUTHORS</h2>
<p> <code>TShark</code> uses the same packet dissection code that <code>Wireshark</code> does, as well as using many other modules from <code>Wireshark</code>; see the list of authors in the <code>Wireshark</code> man page for a list of authors of that code. </p>
<h2>Index</h2>
