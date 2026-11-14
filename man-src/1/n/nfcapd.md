---
title: "nfcapd(1)"
name: "nfcapd"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfcapd/"
description: "nfcapd – netflow capture daemon"
---

<h2>NAME</h2>
<p> nfcapd &#8211; netflow capture daemon</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nfcapd [options]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>nfcapd</code></p>
<dd>is the netflow capture daemon of the nfdump tools. It reads netflow data from the network and stores it into files. The output file is automatically rotated and renamed every n minutes &#8211; typically 5 min &#8211; according the timestamp YYYYMMddhhmm of the interval e.g. nfcapd.201107110845 contains the data from July 11th 2011 08:45 onward. </p>
<p> Netflow version v1, v5, v7 and v9 and IPFIX are transparently supported. </p>
<p> Extensions: nfcapd supports a large number of v9 tags. In order to optimise disk space and performance, v9 tags are grouped into a number of extensions which may or may not be stored into the data file. Therefore the v9 templates configured on the exporter may be tuned according the collector. Only those tags common to both are stored into the data files. </p>
<p> Sampling: By default, the sampling rate is set to 1 (unsampled) or to any given value specified by the -s cmd line option. If sampling information is found in the netflow stream, it overwrites the default value. Sampling is automatically recognised when announced in v9 option templates (tags #34, #35 or #48, #49, #50 ) or in the unofficial v5 header hack. Note: Not all platforms (or IOS/JunOS versions) support exporting sampling information in netflow data, even if sampling is configured. The number of bytes/packets in each netflow record is automatically multiplied by the sampling rate. The total number of flows is not changed as this is not accurate enough. (Small flows versus large flows) If the default sampling rate given by -s is negative, this will hard overwrite any device specific announced sampling rates. </p>
<p> NSEL/ASA Support: nfcapd can be compiled with NSEL/ASA support included. See notes on NSEL/ASA </p>
<p> NEL (NAT Event logging): nfcapd can be compiled with CISCO NEL support included. See notes on NEL. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p </code><i>portnum</i></p>
<dd> Specifies the port number to listen. Default port is 9995</p>
<dt><code>-b </code><i>bindhost</i></p>
<dd> Specifies the hostname/IPv4/IPv6 address to bind for listening. This can be an IP address or a hostname, resolving to an IP address attached to an interface. Defaults to any available IPv4 interface, if not specified.</p>
<dt><code>-4</code></p>
<dd> Forces nfcapd to listen on IPv4 addresses only. Can be used together with -b if a hostname has an IPv4 and IPv6 address record.</p>
<dt><code>-6</code></p>
<dd> Forces nfcapd to listen on IPv6 addresses only. Can be used together with -b if a hostname has an IPv4 and IPv6 address record. Depending on the socket implementation -6 also accepts IPv4 data.</p>
<dt><code>-J </code><i>MulticastGroup</i></p>
<dd> Join the specified IPv4 or IPv6 multicast group for listening.</p>
<dt><code>-R </code><i>host[/port}</i></p>
<dd> Enable packet repeater. Send all incoming packets to another <i>host</i> and <i>port</i>. <i>host</i> is either a valid IPv4/IPv6 address, or a valid symbolic hostname, which resolves to a IPv6 or IPv4 address. <i>port</i> may be ommited and defaults to port 9995. Note: Due to IPv4/IPv6 accepted addresses the port separator is &#8216;/&#8217;.</p>
<dt><code>-I </code><i>IdentString ( capital letter i )</i></p>
<dd> Specifies an ident string, which describes the source e.g. the name of the router. This string is put into the stat record to identify the source. Default is &#8216;none&#8217;. This is for compatibility with nfdump 1.5.x and used to specify a single netflow source. See <i>-n</p>
<dt></i><code>-l </code><i>base_directory ( letter ell )</i></p>
<dd> Specifies the base directory to store the output files. If a sub hierarchy is specified with -S the final directory is concatenated to <i>base_directory/sub_hierarchy</i>. This is for compatibility with nfdump 1.5.x and used to specify a single netflow source. See <i>-n</p>
<dt></i><code>-n </code><i>&lt;Ident,IP,base_directory&gt;</i></p>
<dd> Configures a netflow source named <i>Ident</i> and identified by source IP address <i>IP</i>. The base directory for the flow files is <i>base_directory</i>. If a sub hierarchy is specified with -S the final directory is concatenated to <i>base_directory/sub_hierarchy. Multiple netflow sources can be specified. All data is sent to the same port specified by -p</i>. Note: You must not mix -n option with -I and -l. Use either syntax.</p>
<dt><code>-f </code><i>&lt;pcap_file&gt;</i></p>
<dd> Read netflow packets from a give <i>pcap_file</i> instead of the network. This requires nfcapd to be compiled with the pcap option and is intended for debugging only.</p>
<dt><code>-s </code><i>&lt;rate&gt;</i></p>
<dd> Apply default sampling rate <i>rate</i> to all netflow records, unless the sampling rate is announced by the exporting device. In that case the announced sampling rate is applied. If &lt;rate&gt; is negative, this will hard overwrite any device specific announced sampling rates.</p>
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
<p>&nbsp;<wbr>5&nbsp;<wbr>%Y/%j&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>year/day-of-year </p>
<p>&nbsp;<wbr>6&nbsp;<wbr>%Y/%j/%H&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>year/day-of-year/hour </p>
<p>&nbsp;<wbr>7&nbsp;<wbr>%Y-%m-%d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>year-month-day </p>
<p>&nbsp;<wbr>8&nbsp;<wbr>%Y-%m-%d/%H year-month-day/hour</dl>
<dt><code>-T </code><i>&lt;extension list&gt;</i></p>
<dd> Specifies the list of extensions, to be stored in the netflow file. Regardless of the extension list, the following netflow data is stored per record: first, last, fwd status, tcp flags, proto, (src)tos, src port, dst port, src ipaddr, dst ipaddr, in(packets), in(bytes). In addition nfcapd recognises the extensions as described below. Some are valid for v5/v7/v9, but most of them make only sense for v9. Any specified extensions which do not exist in the input netflow records are ignored.</p>
<dt>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Extensions:</p>
<dd>
<dl>
<dt>
<dd> v5/v7/v9/IPFIX extensions: </p>
<p>&nbsp;<wbr>1 input/output interface SNMP numbers. </p>
<p>&nbsp;<wbr>2 src/dst AS numbers. </p>
<p>&nbsp;<wbr>3 src/dst mask,&nbsp;<wbr>(dst)TOS, direction. </p>
<p>&nbsp;<wbr>4 line Next hop IP addr line </p>
<p>&nbsp;<wbr>5 line BGP next hop IP addr line </p>
<p>&nbsp;<wbr>6 src/dst vlan id labels </p>
<p>&nbsp;<wbr>7 counter output packets </p>
<p>&nbsp;<wbr>8 counter output bytes </p>
<p>&nbsp;<wbr>9 counter aggregated flows </p>
<p> 10 in_src/out_dst MAC address </p>
<p> 11 in_dst/out_src MAC address </p>
<p> 12 MPLS labels 1-10 </p>
<p> 13 Exporting router IPv4/IPv6 address </p>
<p> 14 Exporting router ID </p>
<p> 15 BGP adjacent prev/next AS </p>
<p> 16 time stamp flow received by the collector </p>
<p> NSEL/ASA/NAT extensions </p>
<p> 26 NSEL ASA event, xtended event, ICMP type/code </p>
<p> 27 NSEL/NAT xlate ports </p>
<p> 28 NSEL/NAT xlate IPv4/IPv6 addr </p>
<p> 29 NSEL ASA ACL ingress/egress acl ID </p>
<p> 30 NSEL ASA username </p>
<p> NEL/NAT extensions </p>
<p> 31 NAT event, ingress egress vrfid </p>
<p> 32 NAT Block port allocation &#8211; block start, end step and size </p>
<p> nprobe extensions </p>
<p> 64 nprobe client/server/application latency&quot;}, </p>
<p> <code>IMPORTANT: </code> By default only extension 1 and 2 are selected Extensions can be added/deleted by specifying a &#8216;,&#8217; separated list of extension ids. Each id may be prepended by an optional sign +/- to add or remove a given id from the extension list. Shortcuts: The string &#8216;all&#8217; means all extensions. The strings<br />
&nbsp;<wbr>&#8216;nsel&#8217;&nbsp;<wbr>and&nbsp;<wbr>&#8216;nel&#8217;&nbsp;<wbr>enable all NSEL or NEL extensions respectively. </p>
<p> Examples: </p>
<p> -T all Enables all possible extensions. </p>
<p> -T +3,+4 Adds extensions 3 and 4 to the defaults 1 and 2. </p>
<p> -T all,-8,-9 Set all extensions but 8 and 9 </p>
<p> -T -1,4 Removes default extension 1 and adds extension 4 </p>
<p> -T nsel Enables all required ASA?NSEL extensions </p>
<p> -T nel Enables all required nell extensions </p>
<p> Note: Only those tags in common with the exporting device and enabled extensions at the collector side are stored into the data files. A detailed list which v9 tags are mapped into which extensions is given in the section <code>NOTES</code></dl>
<dt><code>-t </code><i>interval</i></p>
<dd> Specifies the time interval in seconds to rotate files. The default value is 300s ( 5min ).</p>
<dt><code>-w</code></p>
<dd> Align file rotation with next n minute ( specified by -t ) interval. Example: If interval is 5 min, sync at 0,5,10&#8230; wall clock minutes Default: no alignment.</p>
<dt><code>-x </code><i>cmd</i></p>
<dd> Run command <i>cmd</i> at the end of every interval, when a new file becomes available. The following command expansion is available:</p>
<dl>
<dt>
<dd> %f<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Replaced by the file name e.g nfcapd.200907110845 inluding any</p>
<p>&nbsp;<wbr>&nbsp;<wbr>sub hierarchy.&nbsp;<wbr>(&nbsp;<wbr>2009/07/11/nfcapd.200907110845&nbsp;<wbr>) </p>
<p> %d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Replaced by the directory where the file is located.</p>
<p> %t<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Replaced by the time ISO format e.g. 200907110845.</p>
<p> %u<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Replaced by the UNIX time format.</p>
<p> %i<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Replaced ident string given by -I
</dl>
<dt><code>-X</code></p>
<dd> Collect and embed extended statistics. Currently a port and bpp histogram is embeded. Mostly experimental for now</p>
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
<dd> Print netflow records in nfdump raw format to stdout. This option is for debugging purpose only, to see how incoming netflow data is processed and stored.</p>
<dt><code>-j</code></p>
<dd> Compress flows. Use bz2 compression in output file. Note: not recommended while collecting</p>
<dt><code>-z</code></p>
<dd> Compress flows. Use fast LZO1X-1 compression in output file.</p>
<dt><code>-V</code></p>
<dd> Print nfcapd version and exit.</p>
<dt><code>-h</code></p>
<dd> Print help text to stdout with all options and exit.</dl>
<h2>RETURN VALUE</h2>
<p> Returns 0 on success, or 255 if initialization failed.</p>
<h2>LOGGING</h2>
<p> nfcapd logs to syslog with SYSLOG_FACILITY LOG_DAEMON For normal operation level &#8216;warning&#8217; should be fine. More information is reported at level &#8216;info&#8217; and &#8216;debug&#8217;. </p>
<p> A small statistic about the collected flows, as well as errors are reported at the end of every interval to syslog with level &#8216;info&#8217;.</p>
<h2>EXAMPLES</h2>
<p> All flows are sent to port 9995 from all exporters and stored into a single file. All known v9 tags are taken.</p>
<dl>
<dt>
<dd> <code>nfcapd -z -w -D -T all -l /netflow/spool/allflows -I any -S 2 -P /var/run/nfcapd.allflows.pid</code></dl>
<p> All flows from 2 different exporters are sent to port 8877 and stored in separate directory trees. All known v9 tags are taken. Input buffer size is set to 128000 bytes</p>
<dl>
<dt>
<dd> <code>nfcapd -z -w -D -T all -p 8877 -n upstream,192.168.1.1,/netflow/spool/upstream -n peer,192.168.2.1,/netflow/spool/peer -S 2 -B 128000</code></dl>
<p> Only accept from from a single exporter and only extension 3,4 and 5 are accepted. Run a given command when files are rotated and automatically expire flows:</p>
<dl>
<dt>
<dd> <code>nfcapd -w -D -T 3,4,5 -n upstream,192.168.1.1,/netflow/spool/upstream -p 23456 -B 128000 -s 100 -x &#8216;/path/command -r %d/%f&#8217; -P /var/run/nfcapd/nfcapd.pid -e</code></dl>
<h2>NOTES</h2>
<p> Multiple netflow sources: </p>
<p> Netflow data may be sent from different exporters to a single nfcapd process. Use the -n option to separate each netflow source to a different data directory. For compatibility with nfdump 1.5.x, old style -l/-I options are still valid. In that case all flows from all sources are stored in a single file. For high volume netflow streams, it is still recommended to have a single nfcapd process per netflow source. </p>
<p> The current v9 implementation of nfdump supports the following v9 elements: fields:</p>
<dl>
<dt>
<dd>
<p> <code>v9 element</code> <code>v9 ID</code> <code>Extension</code> </p>
<p> NF9_LAST_SWITCHED 21 default </p>
<p> NF9_FIRST_SWITCHED 22 default </p>
<p> NF9_IN_BYTES 1 default </p>
<p> NF9_IN_PACKETS 2 default </p>
<p> NF9_IN_PROTOCOL 4 default </p>
<p> NF9_SRC_TOS 5 default </p>
<p> NF9_TCP_FLAGS 6 default </p>
<p> NF9_FORWARDING_STATUS 89 default </p>
<p> NF9_IPV4_SRC_ADDR 8 default </p>
<p> NF9_IPV4_DST_ADDR 12 default </p>
<p> NF9_IPV6_SRC_ADDR 27 default </p>
<p> NF9_IPV6_DST_ADDR 28 default </p>
<p> NF9_L4_SRC_PORT 7 default </p>
<p> NF9_L4_DST_PORT 11 default </p>
<p> NF9_ICMP_TYPE 32 default </p>
<p> NF9_INPUT_SNMP 10 1 </p>
<p> NF9_OUTPUT_SNMP 14 1 </p>
<p> NF9_SRC_AS 16 2 </p>
<p> NF9_DST_AS 17 2 </p>
<p> NF9_DST_TOS 55 3 </p>
<p> NF9_DIRECTION 61 3 </p>
<p> NF9_SRC_MASK 9 3 </p>
<p> NF9_DST_MASK 13 3 </p>
<p> NF9_IPV6_SRC_MASK 29 3 </p>
<p> NF9_IPV6_DST_MASK 30 3 </p>
<p> NF9_V4_NEXT_HOP 15 4 </p>
<p> NF9_V6_NEXT_HOP 62 4 </p>
<p> NF9_BGP_V4_NEXT_HOP 18 5 </p>
<p> NF9_BPG_V6_NEXT_HOP 63 5 </p>
<p> NF9_SRC_VLAN 58 6 </p>
<p> NF9_DST_VLAN 59 6 </p>
<p> NF9_OUT_PKTS 24 7 </p>
<p> NF9_OUT_BYTES 23 8 </p>
<p> NF9_FLOWS_AGGR 3 9 </p>
<p> NF9_IN_SRC_MAC 56 10 </p>
<p> NF9_OUT_DST_MAC 57 10 </p>
<p> NF9_IN_DST_MAC 80 11 </p>
<p> NF9_OUT_SRC_MAC 81 11 </p>
<p> NF9_MPLS_LABEL_1 70 12 </p>
<p> NF9_MPLS_LABEL_2 71 12 </p>
<p> NF9_MPLS_LABEL_3 72 12 </p>
<p> NF9_MPLS_LABEL_4 73 12 </p>
<p> NF9_MPLS_LABEL_5 74 12 </p>
<p> NF9_MPLS_LABEL_6 75 12 </p>
<p> NF9_MPLS_LABEL_7 76 12 </p>
<p> NF9_MPLS_LABEL_8 77 12 </p>
<p> NF9_MPLS_LABEL_9 78 12 </p>
<p> NF9_MPLS_LABEL_10 79 12 </p>
<p> NF9_SAMPLING_INTERVAL 34 Sampling </p>
<p> NF9_SAMPLING_ALGORITHM 35 Sampling </p>
<p> NF9_FLOW_SAMPLER_ID 48 Sampling </p>
<p> FLOW_SAMPLER_MODE 49 Sampling </p>
<p> NF9_FLOW_SAMPLER_RANDOM_INTERVAL 50 Sampling </p>
<p> IP addr of exporting router 13 </p>
<p> NF9_ENGINE_TYPE 38 14 </p>
<p> NF9_ENGINE_ID 39 14 </p>
<p> NF9_BGP_ADJ_NEXT_AS 128 15<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<p> NF9_BGP_ADJ_PREV_AS 129 15 </p>
<p> collector received timestamp 16</dl>
<p> 32 and 64 bit are supported for all counters. 32it AS numbers are supported. </p>
<p> IPFIX support is experimental. Due to lack of implementation of sampling in many IPFIX exporters, sampling for IPFIX is not yet supported. </p>
<p> The format of the data files is netflow version independent. </p>
<p> Socket buffer: Setting the socket buffer size is system dependent. When starting up, nfcapd returns the number of bytes the buffer was actually set. This is done by reading back the buffer size and may differ from what you requested.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nfdump/">nfdump</a>(1), <a href="/docs/linux/man/1-nfprofile/">nfprofile</a>(1), <a href="/docs/linux/man/1-nfreplay/">nfreplay</a>(1)</p>
<h2>BUGS</h2>
<p> No software without bugs! Please report any bugs back to me. </p>
<h2>Index</h2>
