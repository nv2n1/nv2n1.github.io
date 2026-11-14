---
title: "rawshark(1)"
name: "rawshark"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rawshark/"
description: "rawshark – Dump and analyze raw pcap data"
---

<h2 class="name">NAME</h2>
<p> rawshark &#8211; Dump and analyze raw pcap data </p>
<h2>SYNOPSIS</h2>
<p> <code>rawshark</code> [&nbsp;<wbr><code>-d</code>&nbsp;<wbr>&lt;encap:dlt&gt;|&lt;proto:protoname&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-F</code>&nbsp;<wbr>&lt;field to display&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-h</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-l</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-n</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-N</code>&nbsp;<wbr>&lt;name resolving flags&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-o</code>&nbsp;<wbr>&lt;preference setting&gt;&nbsp;<wbr>]&nbsp;<wbr>&#8230; [&nbsp;<wbr><code>-p</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-r</code>&nbsp;<wbr>&lt;pipe&gt;|-&nbsp;<wbr>] [&nbsp;<wbr><code>-R</code>&nbsp;<wbr>&lt;read&nbsp;<wbr>(display)&nbsp;<wbr>filter&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-s</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-S</code>&nbsp;<wbr>&lt;field format&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-t</code>&nbsp;<wbr>ad|a|r|d|e&nbsp;<wbr>] [&nbsp;<wbr><code>-v</code>&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rawshark</code> reads a stream of packets from a file or pipe, and prints a line describing its output, followed by a set of matching fields for each packet on stdout.</p>
<h2>INPUT</h2>
<p> Unlike <code>TShark</code>, <code>Rawshark</code> makes no assumptions about encapsulation or input. The <code>-d</code> and <code>-r</code> flags must be specified in order for it to run. One or more <code>-F</code> flags should be specified in order for the output to be useful. The other flags listed above follow the same conventions as <code>Wireshark</code> and <code>TShark</code>. </p>
<p> <code>Rawshark</code> expects input records with the following format by default. This matches the format of the packet header and packet data in a pcap-formatted file on disk. </p>
<pre><code>
struct rawshark_rec_s {
    uint32_t ts_sec;      /* Time stamp (seconds) */
    uint32_t ts_usec;     /* Time stamp (microseconds) */
    uint32_t caplen;      /* Length of the packet buffer */
    uint32_t len;         /* "On the wire" length of the packet */
    uint8_t data[caplen]; /* Packet data */
};
</code></pre>
<p> If <code>-p</code> is supplied <code>rawshark</code> expects the following format. This matches the <i>struct pcap_pkthdr</i> structure and packet data used in libpcap/WinPcap. This structure&#8217;s format is platform-dependent; the size of the <i>tv_sec</i> field in the <i>struct timeval</i> structure could be 32 bits or 64 bits. For <code>rawshark</code> to work, the layout of the structure in the input must match the layout of the structure in <code>rawshark</code>. Note that this format will probably be the same as the previous format if <code>rawshark</code> is a 32-bit program, but will not necessarily be the same if <code>rawshark</code> is a 64-bit program. </p>
<pre><code>
struct rawshark_rec_s {
    struct timeval ts;    /* Time stamp */
    uint32_t caplen;      /* Length of the packet buffer */
    uint32_t len;         /* "On the wire" length of the packet */
    uint8_t data[caplen]; /* Packet data */
};
</code></pre>
<p> In either case, the endianness (byte ordering) of each integer must match the system on which <code>rawshark</code> is running.</p>
<h2>OUTPUT</h2>
<p> If one or more fields are specified via the <code>-F</code> flag, <code>Rawshark</code> prints the number, field type, and display format for each field on the first line as &#8220;packet number&#8221; 0. For each record, the packet number, matching fields, and a &#8220;1&#8221; or &#8220;0&#8221; are printed to indicate if the field matched any supplied display filter. A &#8220;-&#8221; is used to signal the end of a field description and at the end of each packet line. For example, the flags <code>-F ip.src -F dns.qry.type</code> might generate the following output: </p>
<pre>
    0 FT_IPv4 BASE_NONE - 1 FT_UINT16 BASE_HEX -
    1 1=&quot;1&quot; 0=&quot;192.168.77.10&quot; 1 -
    2 1=&quot;1&quot; 0=&quot;192.168.77.250&quot; 1 -
    3 0=&quot;192.168.77.10&quot; 1 -
    4 0=&quot;74.125.19.104&quot; 1 -
</pre>
<p> Note that packets 1 and 2 are <font SIZE="-1">DNS</font> queries, and 3 and 4 are not. Adding <code>-R &#8220;not dns&#8221;</code> still prints each line, but there&#8217;s an indication that packets 1 and 2 didn&#8217;t pass the filter: </p>
<pre>
    0 FT_IPv4 BASE_NONE - 1 FT_UINT16 BASE_HEX -
    1 1=&quot;1&quot; 0=&quot;192.168.77.10&quot; 0 -
    2 1=&quot;1&quot; 0=&quot;192.168.77.250&quot; 0 -
    3 0=&quot;192.168.77.10&quot; 1 -
    4 0=&quot;74.125.19.104&quot; 1 -
</pre>
<p> Also note that the output may be in any order, and that multiple matching fields might be displayed.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-d &lt;encapsulation&gt;</p>
<dd> Specify how the packet data should be dissected. The encapsulation is of the form <i>type</i><code>:</code><i>value</i>, where <i>type</i> is one of: </p>
<p> <code>encap</code>:<i>name</i> Packet data should be dissected using the libpcap/WinPcap data link type (<font SIZE="-1">DLT</font>) <i>name</i>, e.g. <code>encap:EN10MB</code> for Ethernet. Names are converted using <i>pcap_datalink_name_to_val()</i>. A complete list of DLTs can be found at &lt;<a rel="nofollow" href="http://www.tcpdump.org/linktypes.html">http://www.tcpdump.org/linktypes.html</a>&gt;. </p>
<p> <code>encap</code>:<i>number</i> Packet data should be dissected using the libpcap/WinPcap <font SIZE="-1">DLT </font><i>number</i>, e.g. <code>encap:105</code> for raw <font SIZE="-1">IEEE 802.11. </font> </p>
<p> <code>proto</code>:<i>protocol</i> Packet data should be passed to the specified Wireshark protocol dissector, e.g. <code>proto:http</code> for <font SIZE="-1">HTTP</font> data.</p>
<dt>-F &lt;field to display&gt;</p>
<dd> Add the matching field to the output. Fields are any valid display filter field. More than one <code>-F</code> flag may be specified, and each field can match multiple times in a given packet. A single field may be specified per <code>-F</code> flag. If you want to apply a display filter, use the <code>-R</code> flag.</p>
<dt>-h</p>
<dd> Print the version and options and exits.</p>
<dt>-l</p>
<dd> Flush the standard output after the information for each packet is printed. (This is not, strictly speaking, line-buffered if <code>-V</code> was specified; however, it is the same as line-buffered if <code>-V</code> wasn&#8217;t specified, as only one line is printed for each packet, and, as <code>-l</code> is normally used when piping a live capture to a program or script, so that output for a packet shows up as soon as the packet is seen and dissected, it should work just as well as true line-buffering. We do this as a workaround for a deficiency in the Microsoft Visual C<font SIZE="-2">++</font> C library.) </p>
<p> This may be useful when piping the output of <code>TShark</code> to another program, as it means that the program to which the output is piped will see the dissected data for a packet as soon as <code>TShark</code> sees the packet and generates that output, rather than seeing it only when the standard output buffer containing that data fills up.</p>
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
<dt>-o &lt;preference&gt;:&lt;value&gt;</p>
<dd> Set a preference value, overriding the default value and any value read from a preference file. The argument to the option is a string of the form <i>prefname</i><code>:</code><i>value</i>, where <i>prefname</i> is the name of the preference (which is the same name that would appear in the preference file), and <i>value</i> is the value to which it should be set.</p>
<dt>-p</p>
<dd> Assume that packet data is preceded by a pcap_pkthdr struct as defined in pcap.h. On some systems the size of the timestamp data will be different from the data written to disk. On other systems they are identical and this flag has no effect.</p>
<dt>-r &lt;pipe&gt;|-</p>
<dd> Read packet data from <i>input source</i>. It can be either the name of a <font SIZE="-1">FIFO </font>(named pipe) or &#8220;-&#8221; to read data from the standard input, and must have the record format specified above.</p>
<dt>-R &lt;read (display) filter&gt;</p>
<dd> Cause the specified filter (which uses the syntax of read/display filters, rather than that of capture filters) to be applied before printing the output.</p>
<dt>-s</p>
<dd> Allows standard pcap files to be used as input, by skipping over the 24 byte pcap file header.</p>
<dt>-S</p>
<dd> Use the specified format string to print each field. The following formats are supported: </p>
<p> %D Field name or description, e.g. &#8220;Type&#8221; for dns.qry.type </p>
<p> %N Base 10 numeric value of the field. </p>
<p> %S String value of the field. </p>
<p> For something similar to Wireshark&#8217;s standard display (&#8220;Type: A (1)&#8221;) you could use %D:%S<code> (%N)</code>.</p>
<dt>-t ad|a|r|d|e</p>
<dd> Set the format of the packet timestamp printed in summary lines, the default is relative. The format can be one of: </p>
<p> <code>ad</code> absolute with date: The absolute date and time is the actual time and date the packet was captured </p>
<p> <code>a</code> absolute: The absolute time is the actual time the packet was captured, with no date displayed </p>
<p> <code>r</code> relative: The relative time is the time elapsed between the first packet and the current packet </p>
<p> <code>d</code> delta: The delta time is the time since the previous packet was captured </p>
<p> <code>e</code> epoch: The time in seconds since epoch (Jan 1, 1970 00:00:00)</p>
<dt>-v</p>
<dd> Print the version and exit.</dl>
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
<dd> If this environment variable is set, <code>Rawshark</code> will call <i><a href="/docs/linux/man/3-abort/">abort</a></i>(3) when a dissector bug is encountered. <i><a href="/docs/linux/man/3-abort/">abort</a></i>(3) will cause the program to exit abnormally; if you are running <code>Rawshark</code> in a debugger, it should halt in the debugger and allow inspection of the process, and, if you are not running it in a debugger, it will, on some OSes, assuming your environment is configured correctly, generate a core dump file. This can be useful to developers attempting to troubleshoot a problem with a protocol dissector.</p>
<dt><font SIZE="-1">WIRESHARK_EP_VERIFY_POINTERS</font></p>
<dd> This environment variable, if set, causes certain uses of pointers to be audited to ensure they do not point to memory that is deallocated after each packet has been fully dissected. This can be useful to developers writing or auditing code.</p>
<dt><font SIZE="-1">WIRESHARK_SE_VERIFY_POINTERS</font></p>
<dd> This environment variable, if set, causes certain uses of pointers to be audited to ensure they do not point to memory that is deallocated after when a capture file is closed. This can be useful to developers writing or auditing code.</p>
<dt><font SIZE="-1">WIRESHARK_ABORT_ON_OUT_OF_MEMORY</font></p>
<dd> This environment variable, if present, causes <i><a href="/docs/linux/man/3-abort/">abort</a></i>(3) to be called if certain out-of-memory conditions (which normally result in an exception and an explanatory error message) are experienced. This can be useful to developers debugging out-of-memory conditions.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/4-wireshark-filter/">wireshark-filter</a></i>(4), <i><a href="/docs/linux/man/1-wireshark/">wireshark</a></i>(1), <i><a href="/docs/linux/man/1-tshark/">tshark</a></i>(1), <i><a href="/docs/linux/man/1-editcap/">editcap</a></i>(1), <i><a href="/docs/linux/man/3-pcap/">pcap</a></i>(3), <i><a href="/docs/linux/man/1-dumpcap/">dumpcap</a></i>(1), <i><a href="/docs/linux/man/1-text2pcap/">text2pcap</a></i>(1), <i><a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a></i>(7) or <i><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></i>(8)</p>
<h2>NOTES</h2>
<p> <code>Rawshark</code> is part of the <code>Wireshark</code> distribution. The latest version of <code>Wireshark</code> can be found at &lt;<a rel="nofollow" href="http://www.wireshark.org">http://www.wireshark.org</a>&gt;. </p>
<p> <font SIZE="-1">HTML</font> versions of the Wireshark project man pages are available at: &lt;<a rel="nofollow" href="http://www.wireshark.org/docs/man-pages">http://www.wireshark.org/docs/man-pages</a>&gt;.</p>
<h2>AUTHORS</h2>
<p> <code>Rawshark</code> uses the same packet dissection code that <code>Wireshark</code> does, as well as using many other modules from <code>Wireshark</code>; see the list of authors in the <code>Wireshark</code> man page for a list of authors of that code. </p>
<h2>Index</h2>
