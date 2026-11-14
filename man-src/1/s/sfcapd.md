---
title: "sfcapd(1)"
name: "sfcapd"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfcapd/"
description: "sfcapd – sflow capture daemon"
---

<h2>NAME</h2>
<p> sfcapd &#8211; sflow capture daemon</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>sfcapd [options]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>sfcapd</code></p>
<dd>is the sflow capture daemon of the nfdump tools. It reads sflow data from the network and stores it into nfcapd compatible files. The output file is automatically rotated and renamed every n minutes &#8211; typically 5 min &#8211; according the timestamp YYYYMMddhhmm of the interval e.g. nfcapd.200407110845 contains the data from July 11th 2004 08:45 onward. sfcapd supports sFlow version 4 and 5 datagrams. </p>
<p> Sflow is an industry standard developed by InMon Corporation. For more information see <a rel="nofollow" href="http://sflow.org.">http://sflow.org.</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p </code><i>portnum</i></p>
<dd> Specifies the port number to listen. Default port is 6343</p>
<dt><code>-b </code><i>bindhost</i></p>
<dd> Specifies the hostname/IPv4/IPv6 address to bind for listening. Can be an IP address or a hostname, resolving to an IP address attached to an interface. Defaults to any available IPv4 interface, if not specified.</p>
<dt><code>-4</code></p>
<dd> Forces sfcapd to listen on IPv4 addresses only. Can be used together with -b if a hostname has an IPv4 and IPv6 address record. Depending on the socket implementation -6 also accepts IPv4 data.</p>
<dt><code>-6</code></p>
<dd> Forces sfcapd to listen on IPv6 addresses only. Can be used together with -b if a hostname has an IPv4 and IPv6 address record.</p>
<dt><code>-j </code><i>MulticastGroup</i></p>
<dd> Join the specified IPv6 or IPv6 multicast group for listening.</p>
<dt><code>-R </code><i>host[/port}</i></p>
<dd> Enable packet repeater. Send all incoming packets to another <i>host</i> and <i>port</i>. <i>host</i> is either a valid IPv4/IPv6 address, or a valid simbolic hostname, which resolves to a IPv6 or IPv4 address. <i>port</i> may be ommited and defaults to port 6343. Note: Due to IPv4/IPv6 accepted addresses the port separator is &#8216;/&#8217;.</p>
<dt><code>-I </code><i>IdentString ( capital letter i )</i></p>
<dd> Specifies an ident string, which describes the source e.g. the name of the router. This string is put into the stat record to identify the source. Default is &#8216;none&#8217;. This is for compatibility with nfdump 1.5.x and used to specify a single sflow source. See <i>-n</p>
<dt></i><code>-l </code><i>base_directory ( letter ell )</i></p>
<dd> Specifies the base directory to store the output files. If a sub hierarchy is specified with -S the final directory is concatenated to <i>base_directory/sub_hierarchy</i>. This is for compatibility with nfdump 1.5.x and used to specify a single sflow source. See <i>-n</p>
<dt></i><code>-n </code><i>&lt;Ident,IP,base_directory&gt;</i></p>
<dd> Configures an sflow source named <i>Ident</i> and identified by source IP address <i>IP</i>. The base directory for the flow files is <i>base_directory</i>. If a sub hierarchy is specified with -S the final directory is concatenated to <i>base_directory/sub_hierarchy. Multiple netflow sources can be specified. All data is sent to the same port specified by -p</i>. Note: You must not mix -n option with -I and -l. Use either syntax.</p>
<dt><code>-f </code><i>&lt;pcap_file&gt;</i></p>
<dd> Read sflow packets from a give <i>pcap_file</i> instead of the network. This requires sfcapd to be compiled with the pcap option and is intended for debugging only.</p>
<dt><code>-S </code><i>&lt;num&gt;</i></p>
<dd> Allows to specify an additional directory sub hierarchy to store the data files. The default is 0, no sub hierarchy, which means the files go directly in the base directory (-l). The base directory (-l) is concatenated with the specified sub hierarchy format to form the final data directory. The following hierarchies are defined:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>0 default&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no hierarchy levels </p>
<p>&nbsp;<wbr>1&nbsp;<wbr>%Y/%m/%d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>year/month/day </p>
<p>&nbsp;<wbr>2&nbsp;<wbr>%Y/%m/%d/%H year/month/day/hour </p>
<p>&nbsp;<wbr>3&nbsp;<wbr>%Y/%W/%u&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>year/week_of_year/day_of_week </p>
<p>&nbsp;<wbr>4&nbsp;<wbr>%Y/%W/%u/%H year/week_of_year/day_of_week/hour </p>
<p>&nbsp;<wbr>5&nbsp;<wbr>%Y/%W/%u&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>year/week_of_year/day_of_week </p>
<p>&nbsp;<wbr>6&nbsp;<wbr>%Y/%W/%u/%H year/week_of_year/day_of_week/hour </p>
<p>&nbsp;<wbr>7&nbsp;<wbr>%Y/%j&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>year/day-of-year </p>
<p>&nbsp;<wbr>8&nbsp;<wbr>%Y/%j/%H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>year/day-of-year/hour </p>
<p>&nbsp;<wbr>9&nbsp;<wbr>%Y-%m-%d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>year-month-day </p>
<p> 10 %Y-%m-%d/%H year-month-day/hour</dl>
<dt><code>-T </code><i>&lt;extension list&gt;</i></p>
<dd> Specifies the list of extensions, to be stored in the flow file. Regardless of the extension list, the following sflow data is stored per record: first, last, fwd status, tcp flags, proto, (src)tos, src port, dst port, src ipaddr, dst ipaddr, in(packets), in(bytes). In addition sfcapd recognises the extensions as described below.</p>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Extensions:</p>
<dd>
<dl>
<dt>
<dd> sflow extensions: </p>
<p>&nbsp;<wbr>1 input/output interface SNMP numbers. </p>
<p>&nbsp;<wbr>2 src/dst AS numbers. </p>
<p>&nbsp;<wbr>3 src/dst mask,&nbsp;<wbr>(dst)TOS, direction,&nbsp;<wbr> </p>
<p>&nbsp;<wbr>4 Next hop IP addr </p>
<p>&nbsp;<wbr>5 BGP next hop IP addr </p>
<p>&nbsp;<wbr>6 src/dst vlan id labels </p>
<p> 10 in_src/out_dst MAC address </p>
<p> By default extension 1 and 2 are selected, which provides compatibility with earlier nfdump version. Extensions can be added/deleted by specifying a &#8216;,&#8217; separated list of extension ids. Each id may be prepended by an optional sign +/- to add or remove a given id from the extension list. The string &#8216;all&#8217; means all extensions. Extensions 7-9 are not available for sfcapd. </p>
<p> Examples: </p>
<p> -T all Enables all possible extensions. </p>
<p> -T +3,+4 Adds extensions 3 and 4 to the defaults 1 and 2. </p>
<p> -T all,-5,-6 Set all extensions but 5 and 6 </p>
<p> -T -1,4 Removes default extension 1 and adds extension 4 </p>
<p> Note: Extensions are shared with the netflow collector nfcapd. Sflow as well as netflow data is stored in the same type of extensions.</dl>
<dt><code>-t </code><i>interval</i></p>
<dd> Specifies the time interval in seconds to rotate files. The default value is 300s ( 5min ).</p>
<dt><code>-w</code></p>
<dd> Align file rotation with next n minute ( specified by -t ) interval. Example: If interval is 5 min, sync at 0,5,10&#8230; wall clock minutes Default: no alignment.</p>
<dt><code>-x </code><i>cmd</i></p>
<dd> Run command <i>cmd</i> at the end of every interval, when a new file becomes available. The following command expansion is available:</p>
<dl>
<dt>
<dd> %f<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Replaced by the file name e.g nfcapd.200407110845 inluding any</p>
<p>&nbsp;<wbr>&nbsp;<wbr>sub hierarchy.&nbsp;<wbr>(&nbsp;<wbr>2004/07/11/nfcapd.200407110845&nbsp;<wbr>) </p>
<p> %d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Replaced by the directory where the file is located.</p>
<p> %t<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Replaced by the time ISO format e.g. 200407110845.</p>
<p> %u<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Replaced by the UNIX time format.</p>
<p> %i<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Replaced ident string given by -I
</dl>
<dt><code>-e </code></p>
<dd> Auto expire files at every cycle. <i>max lifetime</i> and <i>max filesize</i> are defined using <a href="/docs/linux/man/1-nfexpire/">nfexpire</a>(1)</p>
<dt><code>-P </code><i>pidfile</i></p>
<dd> Specify name of pidfile. Default is no pidfile.</p>
<dt><code>-D</code></p>
<dd> Daemon mode: fork to background and detach from terminal. Nfcapd terminates on signal TERM, INT and HUP.</p>
<dt><code>-u </code><i>userid</i></p>
<dd> Change to the user <i>userid</i> as soon as possible. Only root is allowed to use this option.</p>
<dt><code>-g </code><i>groupid</i></p>
<dd> Change to the group <i>groupid</i> as soon as possible. Only root is allowed use this option.</p>
<dt><code>-B </code><i>bufflen</i></p>
<dd> Specifies the socket input buffer length in bytes. For high volume traffic ( near GB traffic ) it is recommended to set this value as high as possible ( typically &gt; 100k ), otherwise you risk to lose packets. The default is OS ( and kernel ) dependent.</p>
<dt><code>-E</code></p>
<dd> Print data records in nfdump raw format to stdout. This option is for debugging purpose only, to see how incoming sflow data is processed and stored.</p>
<dt><code>-j</code></p>
<dd> Compress flows. Use bz2 compression in output file. Note: not recommended while collecting</p>
<dt><code>-z</code></p>
<dd> Compress flows. Use fast LZO1X-1 compression in output file.</p>
<dt><code>-V</code></p>
<dd> Print sfcapd version and exit.</p>
<dt><code>-h</code></p>
<dd> Print help text to stdout with all options and exit.</dl>
<h2>RETURN VALUE</h2>
<p> Returns 0 on success, or 255 if initialization failed.</p>
<h2>LOGGING</h2>
<p> sfcapd logs to syslog with SYSLOG_FACILITY LOG_DAEMON For normal operation level &#8216;warning&#8217; should be fine. More information is reported at level &#8216;info&#8217; and &#8216;debug&#8217;. </p>
<p> A small statistic about the collected flows, as well as errors are reported at the end of every interval to syslog with level &#8216;info&#8217;.</p>
<h2>EXAMPLES</h2>
<p> Compatible with old sfcapd 1.5.x:</p>
<dl>
<dt>
<dd> <code>sfcapd -w -D -l /data/spool/router1 -p 6343 -B 128000 -I router1 -x &#8216;/path/some_app -r %d/%f&#8217; -P /var/run/sfcapd/sfcapd.router1</code></dl>
<p> Selectively enabled sender:</p>
<dl>
<dt>
<dd> <code>sfcapd -Tall -w -D -n router1,192.168.1.10,/data/spool/router1 -p 6343 -B 128000 -P /var/run/sfcapd/sfcapd.router1</code></dl>
<h2>NOTES</h2>
<p> sfcapd automatically scales the packets and bytes according the sampling rate. </p>
<p> Even with sflow version 4 and 5 support, not all available sflow elements are stored in the data files. As of this version, sfcpad supports the the same shared fields as extensions, as it&#8217;s netflow companion nfcapd for netflow version v9. See <a href="/docs/linux/man/1-nfcapd/">nfcapd</a>(1). More fields will be supported in future. </p>
<p> The format of the data files is version independent and compatible nfcapd collected data. </p>
<p> Socket buffer: Setting the socket buffer size is system dependent. When starting up, sfcapd returns the number of bytes the buffer was actually set. This is done by reading back the buffer size and may differ from what you requested.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nfcapd/">nfcapd</a>(1), <a href="/docs/linux/man/1-nfdump/">nfdump</a>(1), <a href="/docs/linux/man/1-nfprofile/">nfprofile</a>(1), <a href="/docs/linux/man/1-nfreplay/">nfreplay</a>(1) </p>
<h2>Index</h2>
