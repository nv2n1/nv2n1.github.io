---
title: "nfdump(1)"
name: "nfdump"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfdump/"
description: "nfdump – netflow display and analyze program"
---

<h2>NAME</h2>
<p> nfdump &#8211; netflow display and analyze program</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nfdump [options] [filter]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>nfdump</code></p>
<dd>is the netflow display and analyzing program of the nfdump tool set. It reads the netflow data from files stored by nfcapd and processes the flows according the options given. The filter syntax is comparable to tcpdump and extended for netflow data. Nfdump can also display many different top N flow and flow element statistics. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r </code><i>inputfile</i></p>
<dd> Read input data from <i>inputfile</i>. Default is read from stdin.</p>
<dt><code>-R </code><i>expr</i></p>
<dd> Read input from a sequence of files in the same directory. <i>expr</i> may be one of:</p>
<dl>
<dt>
<dd> /any/<i>dir</i> Read recursively all files in directory <i>dir</i>. </p>
<p> /dir/<i>file</i> Read all files beginning with <i>file</i>. </p>
<p> /dir/<i>file1:file2</i> Read all files from <i>file1</i> to <i>file2</i>. </p>
<p> When using in combination with a sub hierarchy: </p>
<p> /dir/<i>sub1/sub2/file1:sub3/sub4/file2</i> </p>
<p> Read all files from <i>sub1/sub2/file1</i> <i>sub3/sub4/file2</i> iterating over all required hierarchy levels. </p>
<p> Note: files are read in alphabetical sequence.</dl>
<dt><code>-M </code><i>expr</i></p>
<dd> Read input from multiple directories. <i>expr</i> looks like: <i>/any/path/to/dir1:dir2:dir3</i> etc. and will be expanded to the directories: <i>/any/path/to/dir1</i>, <i>/any/path/to/dir2</i> and <i>/any/path/to/dir3</i> Any number of colon separated directories may be given. The files to read are specified by -r or -R and are expected to exist in all the given directories. The options -r and -R must not contain any directory part when used in conjunction with -M.</p>
<dt><code>-m</code></p>
<dd> depricated option. Use -O tstart instead.</p>
<dt><code>-O </code><i>order</i></p>
<dd> Set sort order to print flows or aggregated flows. <i>order</i> can be:</p>
<dl>
<dt>
<dd> flows Sort according the number of flows<br />
 packets Sort according to (in)packets<br />
 ipkg Same as packets<br />
 opkg Sort according to output packets<br />
 bytes Sort according to (in)bytes<br />
 ibyte Same as bytes<br />
 obyte Sort according to output bytes<br />
 pps Sort according to (in)packets per second<br />
 ipps Same as ipps<br />
 opps Sort according to out packets per second<br />
 bps Sort according to (in)bytes per second<br />
 ibps Same as bps<br />
 obps Sort according to output bytes per second<br />
 bpp Sort according to (in)bytes per packet<br />
 ibpp Same as bpp<br />
 obpp Sort according to output packets<br />
 tstart Sort according to start time of flow &#8211; former -m<br />
 tend&quot; Sort according to end time of flows</dl>
<dt><code>-w </code><i>outputfile</i></p>
<dd> If specified writes binary netflow records to <i>outputfile</i> ready to be processed again with nfdump. The default output is ASCII on stdout. In combination with options -m, -a, -b, and -B write aggregated and/or sorted flow cache in binary format to disk.</p>
<dt><code>-f </code><i>filterfile</i></p>
<dd> Reads the filter syntax from <i>filterfile</i>. Note: Any filter specified directly on the command line takes precedence over -f.</p>
<dt><code>-t </code><i>timewin</i></p>
<dd> Process only flows, which fall in the time window <i>timewin</i>, where <i>timewin</i> is YYYY/MM/dd.hh:mm:ss[-YYYY/MM/dd.hh:mm:ss]. Any parts of the time spec may be omitted e.g YYYY/MM/dd expands to YYYY/MM/dd.00:00:00-infinity and processes all flow from a given day onwards. The time window may also be specified as +/- n. In this case it is relativ to the beginning or end of all flows. +10 means the first 10 seconds of all flows, -10 means the last 10 seconds of all flows.</p>
<dt><code>-c </code><i>num</i></p>
<dd> Limit the number of records to read and process from file(es) to the first <i>num</i> flows.</p>
<dt><code>-a</code></p>
<dd> Aggregate netflow data. Automatically implies -a. Aggregation is done at connection level by taking the 5-tuple protocol, srcip, dstip, srcport and dstport.</p>
<dt><code>-A </code><i>aggregation </i></p>
<dd> Similar to Flexible Netflow (FNF), netflow records can be aggregated by any number of given v9 fields. <i>aggregation</i> is a &#8216;,&#8217; separated list of recognised tags of the following list:</p>
<dl>
<dt>
<dd> proto IP protocol<br />
 srcip Source IP address<br />
 dstip Destination IP address<br />
 srcip4/net IPv4 source IP address with applied netmask<br />
 srcip6/net IPv6 source IP address with applied netmask<br />
 dstip4/net IPv4 destination IP address with applied netmask<br />
 dstip6/net IPv6 destination IP address with applied netmask<br />
 srcnet Apply netmask srcmask in netflow record for source IP<br />
 dstnet Apply netmask dstmask in netflow record for dest IP<br />
 srcport Source port<br />
 dstport Destination port<br />
 srcmask Source mask<br />
 dstmask Destination mask<br />
 srcvlan Source vlan label<br />
 dstvlan Destination vlan label<br />
 srcas Source AS number<br />
 dstas Destination AS number<br />
 nextas BGP Next AS<br />
 prevas BGP Previous AS<br />
 inif SNMP input interface number<br />
 outif SNMP output interface number<br />
 next IP next hop<br />
 bgpnext BGP next hop<br />
 insrcmac In source MAC address<br />
 outdstmac out destination MAC address<br />
 indstmac In destintation MAC address<br />
 outsrcmac Out source MAC address<br />
 tos Source type of service<br />
 srctos Source type of Service<br />
 dsttos Destination type of Service<br />
 mpls1 MPLS label 1<br />
 mpls2 MPLS label 2<br />
 mpls3 MPLS label 3<br />
 mpls4 MPLS label 4<br />
 mpls5 MPLS label 5<br />
 mpls6 MPLS label 6<br />
 mpls7 MPLS label 7<br />
 mpls8 MPLS label 8<br />
 mpls9 MPLS label 9<br />
 mpls10 MPLS label 10<br />
 router Exporting router IP</dl>
<dl>
<dt>
<dd>
<p> nfdump automatically compiles an appropriate output format for the selected aggregation unless an explicit output format is given. The automatic output format is identical to <code>-o &#8216;fmt:%ts %td &lt;fields&gt; %pkt %byt %bps %bpp %fl&#8217;</code> where &lt;fields&gt; represents the selected aggregation tags. </p>
<p> Example:</p>
<dl>
<dt>
<dd> <code> -A proto,srcip,dstport</code> </p>
<p> <code> -A srcas,dstas</code> </p>
</dl>
</dl>
<dt><code>-b</code></p>
<dd> Aggregate netflow records as bidirectional flows. Automatically implies -a. Aggregation is done on connection level by taking the 5-tuple protocol, srcip, dstip, srcport and dstport, or the reverse order for the corresponding connection flow. Input and output packets/bytes are counted and reported separate. Both flows are merged into a single record. An appropriate output format is selected automatically, which may be overwritten by any -o format option.</p>
<dt><code>-B</code></p>
<dd> Like -b but automagically swaps flows, such that src port is &gt; 1024 and dst port is &lt; 1024 as some exporters do not care sending the flows in proper order. It&#8217;s considered to be a convenient option. If src and dst port are &gt; 1024 or &lt; 1024, the flows are taken as is.</p>
<dt><code>-I</code></p>
<dd> Print flow statistics from file specified by -r, or timeslot specified by -R/-M.</p>
<dt><code>-D </code><i>dns</i></p>
<dd> Set <i>dns</i> as nameserver to lookup hostnames.</p>
<dt><code>-s </code><i>statistic[:p][/orderby]</i></p>
<dd> Generate the Top N flow or flow element statistic. <i>statistic</i> can be:</p>
<dl>
<dt>
<dd> record Statistic about arregated netflow records.<br />
 srcip Statistic about source IP addresses<br />
 dstip Statistic about destination IP addresses<br />
 ip Statistic about any (source or destination) IP addresses<br />
 nhip Statistic about next hop IP addresses<br />
 nhbip Statistic about BGP next hop IP addresses<br />
 router Statistic about exporting router IP address<br />
 srcport Statistic about source ports<br />
 dstport Statistic about destination ports<br />
 port Statistic about any (source or destination) ports<br />
 tos Statistic about type of service &#8211; default src<br />
 srctos Statistic about src type of service<br />
 dsttos Statistic about dst type of service<br />
 dir Statistic about flow directions ingress/egress<br />
 srcas Statistic about source AS numbers<br />
 dstas Statistic about destination AS numbers<br />
 as Statistic about any (source or destination) AS numbers<br />
 inif Statistic about input interface<br />
 outif Statistic about output interface<br />
 if Statistic about any interface<br />
 srcmask Statistic about src mask<br />
 dstmask Statistic about dst mask<br />
 srcvlan Statistic about src vlan label<br />
 dstvlan Statistic about dst vlan label<br />
 vlan Statistic about any vlan label<br />
 insrcmac Statistic about input src MAC address<br />
 outdstmac Statistic about output dst MAC address<br />
 indstmac Statistic about input dst MAC address<br />
 outsrcmac Statistic about output src MAC address<br />
 srcmac Statistic about any src MAC address<br />
 dstmac Statistic about any dst MAC address<br />
 inmac Statistic about any input MAC address<br />
 outmac Statistic about any output MAC address<br />
 mask Statistic about any mask<br />
 proto Statistic about IP protocols<br />
 mpls1 Statistic about MPLS label 1<br />
 mpls2 Statistic about MPLS label 2<br />
 mpls3 Statistic about MPLS label 3<br />
 mpls4 Statistic about MPLS label 4<br />
 mpls5 Statistic about MPLS label 5<br />
 mpls6 Statistic about MPLS label 6<br />
 mpls7 Statistic about MPLS label 7<br />
 mpls8 Statistic about MPLS label 8<br />
 mpls9 Statistic about MPLS label 9<br />
 mpls10 Statistic about MPLS label 10<br />
 sysid Internal SysID of exporter </p>
<p> NSEL/ASA stats<br />
 event NSEL/ASA event<br />
 xevent NSEL/ASA extended event<br />
 xsrcip NSEL/ASA translated src IP address<br />
 xsrcport NSEL/ASA translated src port<br />
 xdstip NSEL/ASA translated dst IP address<br />
 xdstport NSEL/ASA translated dst port<br />
 iacl NSEL/ASA ingress ACL<br />
 iace NSEL/ASA ingress ACE<br />
 ixace NSEL/ASA ingress xACE<br />
 eacl NSEL/ASA egress ACL<br />
 eace NSEL/ASA egress ACE<br />
 exace NSEL/ASA egress xACE </p>
<p> NAT stats<br />
 nevent NAT event<br />
 vrf/ivrf NAT ingress vrf<br />
 evrf NAT egress vrf<br />
 nsrcip NAT src IP address<br />
 nsrcport NAT src port<br />
 ndstip NAT dst IP address<br />
 ndstport NAT dst port
</dl>
<dl>
<dt>
<dd>
<p> By adding <i>:p</i> to the statistic name, the resulting statistic is split up into transport layer protocols. Default is transport protocol independent statistics. </p>
<p> <i>orderby</i> is optional and specifies the order by which the statistics is ordered and can be <i>flows</i>, <i>packets</i>, <i>bytes</i>, <i>pps</i>, <i>bps</i> or <i>bpp</i>. You may specify more than one <i>orderby</i> which results in the same statistic but ordered differently. If no <i>orderby</i> is given, statistics are ordered by <i>flows</i>. You can specify as many -s flow element statistics on the command line for the same run. </p>
<p> Example:</p>
<dl>
<dt>
<dd> <code>-s srcip -s ip/flows -s dstport/pps/packets/bytes -s record/bytes</code></dl>
</dl>
</dl>
<dl>
<dt><code>-O </code><i>orderby</i></p>
<dd> Specifies the default <i>orderby</i> for flow element statistics -s, which applies when no <i>orderby</i> is given at -s. <i>orderby</i> can be <i>flows</i>, <i>packets</i>, <i>bytes</i>, <i>pps</i>, <i>bps</i> or <i>bpp</i>. Defaults to <i>flows</i>.</p>
<dt><code>-l </code><i>[+/-]packet_num</i></p>
<dd> Limit statistics output to those records above or below the <i>packet_num</i> limit. <i>packet_num</i> accepts positive or negative numbers followed by &#8216;K&#8217; , &#8216;M&#8217; or &#8216;G&#8217; 10E3, 10E6 or 10E9 flows respectively. See also note at -L</p>
<dt><code>-L </code><i>[+/-]byte_num</i></p>
<dd> Limit statistics output to those records above or below the <i>byte_num</i> limit. <i>byte_num</i> accepts positive or negative numbers followed by &#8216;K&#8217; , &#8216;M&#8217; or &#8216;G&#8217; 10E3, 10E6 or 10E9 bytes respectively. <i>Note:</i> These limits only apply to the statistics and aggregated outputs generated with -a -s. To filter netflow records by packets and bytes, use the filter syntax &#8216;packets&#8217; and &#8216;bytes&#8217; described below.</p>
<dt><code>-n </code><i>num</i></p>
<dd> For record statistics (-s .. ): Define the number for the Top N. Defaults to 10. Use -n 0 to list all records.<br />
 For record sorting and aggregation (-a .. -O ..): Limit the records to the first top <i>num</i> sorted records. if not specified or -n 0 is given, all records are listed.</p>
<dt><code>-o </code><i>format</i></p>
<dd> Selects the output format to print flows or flow record statistics (-s record). The following formats are available:</p>
<dl>
<dt>
<dd> raw Print each file flow record on multiple lines.<br />
 line Print each flow on one line. Default format.<br />
 long Print each flow on one line with more details<br />
 biline Same as line, but for bidir flows<br />
 bilong Same as long, but for bidir flows<br />
 extended Print each flow on one line with even more details.<br />
 nsel Print each NSEL event on one line. Default if NSEL/ASA enabled.<br />
 nel Print each NAT event on one line. Default if NEL enabled.<br />
 csv Comma separated output for machine readable processing.<br />
 pipe Legacy machine readable format: fields &#8216;|&#8217; separated.<br />
 fmt:<i>format</i> User defined output format.</dl>
<dl>
<dt>
<dd> For each defined output format except -o fmt:&lt;format&gt; an IPv6 long output format exists. <code>line6, long6 and extended6</code>. See <i>output formats</i> below for more information.</dl>
<dt><code>-q</code></p>
<dd> Suppress the header line and the statistics at the bottom.</p>
<dt><code>-N</code></p>
<dd> Print plain numbers in output. Easier for post-parsing.</p>
<dt><code>-i </code><i>ident</i></p>
<dd> Change ident label in file, specified by -r to <i>ident</p>
<dt></i><code>-v </code><i>file</i></p>
<dd> Verify <i>file</i>. Print data file version, number of blocks and compression status.</p>
<dt><code>-E </code>file</p>
<dd> Print exporter/sampler list found in <i>file</i>. In case of a nfcapd collector file, an additional statistics per exporter is printed with number of flows, packets and sequence errors.</p>
<dt><code>-x </code>file</p>
<dd> Scan and print extension maps located in file file</p>
<dt><code>-j</code></p>
<dd> Compress flows. Use bz2 compression in output file. Space efficient method</p>
<dt><code>-z</code></p>
<dd> Compress flows. Use fast LZO1X-1 compression in output file. Time efficient method</p>
<dt><code>-J </code>num</p>
<dd> Change compression for file(s) given by -r &lt;file&gt; or -R &lt;dir&gt; num: 0 uncompress, 1: LZO1X-1 compression, 2: bz2 compression</p>
<dt><code>-Z</code></p>
<dd> Check filter syntax and exit. Sets the return value accordingly.</p>
<dt><code>-X</code></p>
<dd> Compiles the filer syntax and dumps the filter engine table to stdout. This is for debugging purpose only.</p>
<dt><code>-V</code></p>
<dd> Print nfdump version and exit.</p>
<dt><code>-h</code></p>
<dd> Print help text on stdout with all options and exit.</dl>
<h2>RETURN VALUE</h2>
<p> Returns</p>
<dl>
<dt>
<dd>
<p> 0 No error. </p>
<p> 255 Initialization failed. </p>
<p> 254 Error in filter syntax. </p>
<p> 250 Internal error.</dl>
<h2>OUTPUT FORMATS</h2>
<p> The output format <code>raw</code> prints each flow record on multiple lines, including all information available in the record. This is the most detailed view on a flow. </p>
<p> Other output formats print each flow on a single line. Predefined output formats are <code>line</code>, <code>long</code> and <code>extended</code> The output format <code>line</code> is the default output format when no format is specified. It limits the imformation to the connection details as well as number of packets, bytes and flows. </p>
<p> The output format <code>long</code> is identical to the format <code>line</code>, and includes additional information such as TCP flags and Type of Service. </p>
<p> The output format <code>extended</code> is identical to the format <code>long</code>, and includes additional computed information such as <code>pps</code>, <code>bps</code> and <code>bpp</code>. </p>
<p> <i>Fields:</i> </p>
<dl>
<dt>
<dd> <code>Date flow start:</code> Start time flow first seen. ISO 8601 format including miliseconds. </p>
<p> <code>Duration:</code> Duration of the flow in seconds and miliseconds. If flows are aggregated, <i>duration</i> is the time span over the entire periode of time from first seen to last seen. </p>
<p> <code>Proto:</code> Protocol used in the connection. </p>
<p> <code>Src IP Addr:Port:</code> Source IP address and source port. </p>
<p> <code>Dst IP Addr:Port:</code> Destination IP address and destination port. In case of ICMP, port is decodes as type.code. </p>
<p> <code>Flags:</code> TCP flags ORed of the connection. </p>
<p> <code>Tos:</code> Type of service. </p>
<p> <code>Packets:</code> The number of packets in this flow. If flows are aggregated, the packets are summed up. </p>
<p> <code>Bytes:</code> The number of bytes in this flow. If flows are aggregated, the bytes are summed up. </p>
<p> <code>pps:</code> The calculated packets per second: number of packets / duration. If flows are aggregated this results in the average pps during this periode of time. </p>
<p> <code>bps:</code> The calculated bits per second: 8 * number of bytes / duration. If flows are aggregated this results in the average bps during this periode of time. </p>
<p> <code>Bpp:</code> The calculated bytes per packet: number of bytes / number of packets. If flows are aggregated this results in the average bpp during this periode of time. </p>
<p> <code>Flows:</code> Number of flows. If flows are listed only, this number is always 1. If flows are aggregated, this shows the number of aggregated flows to one record.</dl>
<p> Numbers larger than 1&#8217;000&#8217;000 (1000*1000), are scaled to 4 digits and one decimal digit including the scaling factor <code>M</code>, <code>G</code> or <code>T</code> for cleaner output, e.g. <code>923.4 M</code> </p>
<p> To make the output more readable, IPv6 addresses are shrinked down to 16 characters. The seven most and seven least digits connected with two dots <code>&#8216;..&#8217;</code> are displayed in any normal output formats. To display the full IPv6 address, use the appropriate long format, which is the format name followed by a <code>6</code>. </p>
<p> Example: <code>-o line</code> displays an IPv6 address as <code>2001:23..80:d01e</code> where as the format <code>-o line6</code> displays the IPv6 address in full length <code>2001:234:aabb::211:24ff:fe80:d01e</code>. The combination of <code>-o line -6</code> is equivalent to <code>-o line6</code>. </p>
<p> The output format <code>fmt:&lt;format&gt;</code> allows you to define your own output format. A format description <code>format</code> consists of a single line containing arbitrary strings and format specifier as described below </p>
<dl>
<dt>
<dd> <code>%&lt;format&gt;</code> Inserts the predefined <code>format</code> at this position. e.g. <code>%line</code><br />
 <code>%ff</code> flow record flags in hex.<br />
 <code>%ts</code> Start Time &#8211; first seen<br />
 <code>%te</code> End Time &#8211; last seen<br />
 <code>%tr</code> Time the flow was received by the collector<br />
 <code>%td</code> Duration<br />
 <code>%pr</code> Protocol<br />
 <code>%exp</code> Exporter ID<br />
 <code>%eng</code> Engine Type/ID<br />
 <code>%sa</code> Source Address<br />
 <code>%da</code> Destination Address<br />
 <code>%sap</code> Source Address:Port<br />
 <code>%dap</code> Destination Address:Port<br />
 <code>%sp</code> Source Port<br />
 <code>%dp</code> Destination Port<br />
 <code>%sn</code> Source Network, mask applied<br />
 <code>%dn</code> Destination Network, mask applied<br />
 <code>%nh</code> Next-hop IP Address<br />
 <code>%nhb</code> BGP Next-hop IP Address<br />
 <code>%ra</code> Router IP Address<br />
 <code>%sas</code> Source AS<br />
 <code>%das</code> Destination AS<br />
 <code>%nas</code> Next AS<br />
 <code>%pas</code> Previous AS<br />
 <code>%in</code> Input Interface num<br />
 <code>%out</code> Output Interface num<br />
 <code>%pkt</code> Packets &#8211; default input<br />
 <code>%ipkt</code> Input Packets<br />
 <code>%opkt</code> Output Packets<br />
 <code>%byt</code> Bytes &#8211; default input<br />
 <code>%ibyt</code> Input Bytes<br />
 <code>%obyt</code> Output Bytes<br />
 <code>%fl</code> Flows<br />
 <code>%flg</code> TCP Flags<br />
 <code>%tos</code> Tos &#8211; default src<br />
 <code>%stos</code> Src Tos<br />
 <code>%dtos</code> Dst Tos<br />
 <code>%dir</code> Direction: ingress, egress<br />
 <code>%smk</code> Src mask<br />
 <code>%dmk</code> Dst mask<br />
 <code>%fwd</code> Forwarding Status<br />
 <code>%svln</code> Src vlan label<br />
 <code>%dvln</code> Dst vlan label<br />
 <code>%ismc</code> Input Src Mac Addr<br />
 <code>%odmc</code> Output Dst Mac Addr<br />
 <code>%idmc</code> Input Dst Mac Addr<br />
 <code>%osmc</code> Output Src Mac Addr<br />
 <code>%mpls1</code> MPLS label 1<br />
 <code>%mpls2</code> MPLS label 2<br />
 <code>%mpls3</code> MPLS label 3<br />
 <code>%mpls4</code> MPLS label 4<br />
 <code>%mpls5</code> MPLS label 5<br />
 <code>%mpls6</code> MPLS label 6<br />
 <code>%mpls7</code> MPLS label 7<br />
 <code>%mpls8</code> MPLS label 8<br />
 <code>%mpls9</code> MPLS label 9<br />
 <code>%mpls10</code> MPLS label 10<br />
 <code>%mpls</code> MPLS labels 1-10<br />
 <code>%bps</code> bps &#8211; bits per second<br />
 <code>%pps</code> pps &#8211; packets per second<br />
 <code>%bpp</code> bps &#8211; Bytes per package </p>
<p> NSEL specific formats<br />
 <code>%nfc</code> NSEL connection ID<br />
 <code>%evt</code> NSEL event<br />
 <code>%xevt</code> NSEL extended event<br />
 <code>%msec</code> NSEL event time in msec<br />
 <code>%iacl</code> NSEL ingress ACL<br />
 <code>%eacl</code> NSEL egress ACL<br />
 <code>%xsa</code> NSEL XLATE src IP address<br />
 <code>%xda</code> NSEL XLATE dst IP address<br />
 <code>%xsp</code> NSEL XLATE src port<br />
 <code>%xdp</code> NSEL SLATE dst port<br />
 <code>%xsap</code> Xlate Source Address:Port<br />
 <code>%xdap</code> Xlate Destination Address:Port<br />
 <code>%uname</code> NSEL user name </p>
<p> NEL/NAT specific formats<br />
 <code>%nevt</code> NAT event &#8211; same as %evt<br />
 <code>%ivrf</code> NAT ingress VRF ID<br />
 <code>%evrf</code> NAT egress VRF ID<br />
 <code>%nsa</code> NAT src IP address<br />
 <code>%nda</code> NAT dst IP address<br />
 <code>%nsp</code> NAT src port<br />
 <code>%ndp</code> NAT dst port<br />
 <code>%pbstart</code> NAT pool block start<br />
 <code>%pbend</code> NAT pool block end<br />
 <code>%pbstep</code> NAT pool block step<br />
 <code>%pbsize</code> NAT pool block size </p>
<p> Nprobe formats<br />
 <code>%cl</code> Client latency<br />
 <code>%sl</code> Server latency<br />
 <code>%al</code> Application latency </p>
</dl>
<p> The &quot;flow flags&quot; format (%ff) prints the internal record flags as a single hexadecimal number, consisting of any of these flag values or-ed together: </p>
<dl>
<dt>
<dd>
 1 Record contains IPv6 addresses<br />
 2 Packet counters are 64-bit<br />
 4 Byte counters are 64-bit<br />
 8 IP next hop is an IPv6 address<br />
 16<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>BGP next hop is an IPv6 address</p>
<p> 32 Exporting router is an IPv6 address<br />
 64 Record is an EVENT record<br />
 128 Record is sampled</dl>
<p> Example: the standard output format <code>long</code> can be created as</p>
<dl>
<dt>
<dd> <code>-o &quot;fmt:%ts %td %pr %sap -&gt; %dap %flg %tos %pkt %byt %fl&quot;</code></dl>
<p> You may also define your own output format and have it compiled into nfdump. See nfdump.c section <code>Output Formats</code> for more details. </p>
<p> The <code>csv</code> output format is intended to be read by another program for further processing. As an example, see the parse_csv.pl Perl program. The cvs output format consists of one or more output blocks and one summary block. Each output block starts with a cvs index line followed by the cvs record lines. The index lines describes the order, how each following record is composed. </p>
<p> Example:</p>
<dl>
<dt>
<dd> Index line: ts,te,td,sa,da,sp,dp,pr,&#8230;<br />
 Record line: 2004-07-11 10:30:00,2004-07-11 10:30:10,10.010,&#8230;
</dl>
<p> All records are in ASCII readable form. Numbers are not scaled, so each line can easily be parsed. </p>
<p> Indices used in nfdump 1.6: </p>
<dl>
<dt>
<dd> ts,te,td time records: t-start, t-end, duration<br />
 sa,da src dst address sp,dp src, dst port<br />
 pr protocol PF_INET or PF_INET6<br />
 flg TCP Flags: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>000001 FIN. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>000010 SYN </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>000100 RESET </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>001000 PUSH </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>010000 ACK </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>100000 URGENT </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e.g. 6&nbsp;<wbr>=&gt;&nbsp;<wbr>SYN&nbsp;<wbr>+&nbsp;<wbr>RESET<br />
 fwd forwarding status<br />
 stos src tos<br />
 ipkt,ibyt input packets/bytes<br />
 opkt,obyt output packets, bytes<br />
 in,out input/output interface SNMP number<br />
 sas,das src, dst AS<br />
 smk,dmk src, dst mask<br />
 dtos dst tos<br />
 dir direction<br />
 nh,nhb nethop IP address, bgp next hop IP<br />
 svln,dvln src, dst vlan id<br />
 ismc,odmc input src, output dst MAC<br />
 idmc,osmc input dst, output src MAC<br />
 mpls1,mpls2 MPLS label 1-10<br />
 mpls3,mpls4<br />
 mpls5,mpls6<br />
 mpls7,mpls8<br />
 mpls9,mpls10<br />
 ra router IP<br />
 eng router engine type/id
</dl>
<p> See parse_csv.pl for more details. </p>
<h2>FILTER</h2>
<p> The filter syntax is similar to the well known pcap library used by tcpdump. The filter can be either specified on the command line after all options or in a separate file. It can span several lines. Anything after a &#8216;#&#8217; is treated as a comment and ignored to the end of the line. There is virtually no limit in the length of the filter expression. All keywords are case independent. </p>
<p> Any filter consists of one or more expressions <i>expr</i>. Any number of <i>expr</i> can be linked together: </p>
<p> expr <code>and</code> expr, expr <code>or</code> expr, <code>not</code> expr and <code>(</code> expr <code>)</code>. </p>
<p> <i>Expr</i> can be one of the following filter primitives:</p>
<dl>
<dt><i>include</i></p>
<dd> <code>@include &lt;file&gt;</code><br />
 include the content of <i>&lt;file&gt;</i> into filter.</p>
<dt><i>ip version</i></p>
<dd> <code>inet</code> or <code>ipv4</code> for IPv4<br />
 <code>inet6</code> or <code>ipv6</code> for IPv6</p>
<dt><i>protocol</i></p>
<dd> <code>proto &lt;protocol&gt;</code><br />
 <code>proto &lt;number&gt;</code><br />
 where <code>&lt;protocol&gt;</code> is known protocol such as <code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmp6</code>, <code>gre</code>, <code>esp</code>, <code>ah</code>, etc. or a valid protocol number: <code>6</code>, <code>17</code> etc.</p>
<dt><i>IP address</i></p>
<dd>
<dl>
<dt>
<dd> <code>[src|dst] ip &lt;ipaddr&gt;</code><br />
 <code>[src|dst] host &lt;ipaddr&gt;</code><br />
 with <i>&lt;ipaddr&gt;</i> as any valid IPv4, IPv6 address, or a full qualified hostname. In case of a hostname, the IP address is looked up in DNS. If more than a single IP address is found, all IP addresses are chained together. <code>(ip1 or ip2 or ip3 &#8230; )</code> </p>
<p> To check if an IP address is in a known IP list, use<br />
 <code>[src|dst] ip in [ &lt;iplist&gt; ] </code><br />
 <code>[src|dst] host in [ &lt;iplist&gt; ] </code><br />
 <i>&lt;iplist&gt;</i> is a space or comma separated list of individual <code>&lt;ipaddr&gt;</code> or full qualified hostnames, which are looked up in DNS. If more than a single IP address is found, all IP addresses are put into the list.</dl>
<dt><i>[src|dst]</i></p>
<dd> IP addresses, networks, ports, AS number etc. can be specifically selected by using a direction qualifier, such as src or <code>dst</code>. They can also be used in combination with <code>and</code> and <code>or</code>. such as <code>src and dst ip ..</code>.</p>
<dt><i>network</i></p>
<dd> <code>[src|dst] net a.b.c.d m.n.r.s</code><br />
 Select the IPv4 network <i>a.b.c.d</i> with netmask <i>m.n.r.s</i>. </p>
<p> <code>[src|dst] net &lt;net&gt;/&lt;num&gt;</code><br />
 with <i>&lt;net&gt;</i> as a valid IPv4 or IPv6 network and <i>&lt;num&gt;</i> as maskbits. The number of mask bits must match the appropriate address familiy in IPv4 or IPv6. Networks may be abreviated such as 172.16/16 if they are unambiguous.</p>
<dt><i>Port</i></p>
<dd>
<dl>
<dt>
<dd> <code>[src|dst] port [comp] &lt;num&gt;</code><br />
 with <i>&lt;num&gt;</i> as any valid port number. If <i>comp</i> is omitted,<br />
&nbsp;<wbr>&#8216;=&#8217;&nbsp;<wbr>is assumed.&nbsp;<wbr><i>comp</i>&nbsp;<wbr>is explained more detailed below.<br />
 <code>[src|dst] port in [ &lt;portlist&gt; ] </code><br />
 A port can be compared against a know list, where <code>&lt;portlist&gt;</code> is a space separated list of individual port numbers.</dl>
<dt><i>ICMP</i></p>
<dd>
<dl>
<dt>
<dd> <code>icmp-type &lt;num&gt;</code><br />
 <code>icmp-code &lt;num&gt;</code><br />
 with <i>&lt;num&gt;</i> as a valid icmp type/code. This automatically implies <code>proto icmp</code>.</dl>
<dt><i>Router ID</i></p>
<dd>
<dl>
<dt>
<dd> <code>engine-type &lt;num&gt;</code><br />
 <code>engine-id &lt;num&gt;</code><br />
 <code>sysid &lt;num&gt;</code><br />
 with <i>&lt;num&gt;</i> as a valid router engine type/id or exporter ID(0..255).</dl>
<dt><i>Interface</i></p>
<dd> <code>[in|out] if &lt;num&gt;</code><br />
 Select input or output or either interface ID, with <i>num</i> as the SNMP interface number.<br />
 Example: <code>in if 3</code></p>
<dt><i>AS numbers</i></p>
<dd> <code>[src|dst|prev|next] as [comp] &lt;num&gt;</code><br />
 Selects source, dstination, previous, next or any AS number with <i>&lt;num&gt;</i> as any valid as number. 32bit AS numbers are suported. If <i>comp</i> is omitted, &#8216;=&#8217; is assumed. <i>comp</i> is explained more detailed below. </p>
<p> <code>[src|dst|prev|next] as in [ &lt;ASlist&gt; ] </code><br />
 An AS number can be compared against a know list, where <code>&lt;ASlist&gt;</code> is a space or comma separated list of individual AS numbers.</p>
<dt><i>Prefix mask bits </i></p>
<dd> <code>[src|dst] mask &lt;bits&gt;</code><br />
 with <i>&lt;bits&gt;</i> as any valid prefix mask bit value.</p>
<dt><i>Vlan labels</i></p>
<dd> <code>[src|dst] vlan &lt;num&gt;</code><br />
 with <i>&lt;num&gt;</i> as any valid vlan label.</p>
<dt><i>Flags</i></p>
<dd> <code>flags &lt;tcpflags&gt;</code><br />
 with <i>&lt;tcpflags&gt;</i> as a combination of:</p>
<dl>
<dt>
<dd> A ACK.<br />
 S SYN.<br />
 F FIN.<br />
 R Reset.<br />
 P Push.<br />
 U Urgent.<br />
 X All flags on.</dl>
<p> The ordering of the flags is not relevant. Flags not mentioned are treated as don&#8217;t care. In order to get those flows with only the SYN flag set, use the syntax &#8216;<code>flags S and not flags AFRPU</code>&#8216;.</p>
<dt><i>Next hop IP</i></p>
<dd> <code>next ip &lt;ipaddr&gt;</code><br />
 with <i>&lt;ipaddr&gt;</i> as IPv4/IPv6 IP address of next hop router.</p>
<dt><i>Next-hop router&#8217;s IP in the BGP domain</i></p>
<dd> <code>bgpnext ip &lt;ipaddr&gt;</code><br />
 with <i>&lt;ipaddr&gt;</i> as IPv4/IPv6 next-hop router&#8217;s IP in the BGP domain. ( v9 #18 )</p>
<dt><i>Router IP</i></p>
<dd>
 <code>router ip &lt;ipaddr&gt;</code><br />
 Filter the flows according the IP address of the exporting router.</p>
<dt><i>MAC addresses</i></p>
<dd> <code>[InOutSrcDst] mac &lt;addr&gt;</code><br />
 With <i>&lt;addr&gt;</i> any valid MAC address. <code>mac</code> can be more specific specified by using any combination of a direction specifier as defined by CISCO v9. <code>in src</code>, <code>in dst</code>, <code>out src</code>, <code>out dst</code>.</p>
<dt><i>MPLS labels</i></p>
<dd> <code>mpls label&lt;n&gt; [comp] &lt;num&gt;</code><br />
 With <i>&lt;n&gt;</i> as any mpls label number 1..10. Filters exactly specified label&lt;n&gt;.<br />
 <code>mpls eos [comp] &lt;num&gt;</code> </p>
<p> Filters End of Stack label for a given value <i>&lt;num&gt;</i>.<br />
 <code>mpls exp&lt;n&gt; [comp] &lt;bits&gt;</code><br />
 Filters experimental bits of label <i>&lt;n&gt;</i> with <i>&lt;bits&gt;</i> 0..7.</p>
<dt><i>Packets</i></p>
<dd> <code>packets [comp] &lt;num&gt; [scale]</code><br />
 To filter for netflow records with a specific packet count.<br />
 Example: <code>packets &gt; 1k</code></p>
<dt><i>Bytes</i></p>
<dd> <code>bytes [comp] &lt;num&gt; [scale]</code><br />
 To filter for netflow records with a specific byte count.<br />
 Example: <code>bytes 46</code> filters all empty IPv4 packets</p>
<dt><i>Aggregated flows</i></p>
<dd> <code>flows [comp] &lt;num&gt; [scale]</code><br />
 To filter for netflow records with a specific number of aggregated flows.</p>
<dt><i>Type of Service (TOS)</i></p>
<dd> <i>[SourceDestination]</i> <code>tos &lt;num&gt;</code><br />
 With <i>&lt;num&gt;</i> 0..255. For compatibility with nfump 1.5.x: <code>tos &lt;num&gt;</code> is equivalent with <code>src tos &lt;num&gt;</code></p>
<dt><i>Packets per second: Calculated value.</i></p>
<dd> <code>pps</code> <i>[comp]</i> <i>num</i> <i>[scale]</i><br />
 To filter for flows with specific packets per second.</p>
<dt><i>Duration: Calculated value</i></p>
<dd> <code>duration</code> <i>[comp]</i> <i>num</i><br />
 To filter for flows with specific duration in miliseconds.</p>
<dt><i>Bits per second: Calculated value.</i></p>
<dd> <code>bps</code> <i>[comp]</i> <i>num</i> <i>[scale]</i><br />
 To filter for flows with specific bytes per second.</p>
<dt><i>Bytes per packet: Calculated value.</i></p>
<dd> <code>bpp</code> <i>[comp]</i> <i>num</i> <i>[scale]</i><br />
 To filter for flows with specific bytes per packet.</p>
<dt><i>scale</i> scaling factor. Maybe <i>k</i> <i>m</i> <i>g</i>. Factor is 1000</p>
<dd>
<dt><i>comp</i> The following comparators are supported:</p>
<dd> <code>=, ==, &gt;, &lt;, EQ, LT, GT .</code> If <i>comp</i> is omitted, &#8216;=&#8217; is assumed.</dl>
<dl>
<dt><code>NSEL/ASA specific filters:</code></p>
<dd></dl>
<p> <i>NSEL/ASA Event</i></p>
<dl>
<dt>
<dd> <code>asa event &lt;ignore|create|term|delete|deny&gt;</code><br />
 <code>asa event [comp] &lt;number&gt;</code><br />
 select NSEL/ASA event by name or number. If given as number it can be compared with a number
</dl>
<dl>
<dt><i>NSEL/ASA denied reason</i></p>
<dd>
<dl>
<dt>
<dd> <code>asa event denied &lt;ingress|egress|interface|nosyn&gt;</code><br />
 Select a NSEL/ASA denied event by type</dl>
<dt><i>NSEL/ASA extended events</i></p>
<dd>
<dl>
<dt>
<dd> <code>asa xevent [comp] &lt;num&gt;</code><br />
 Select an extended NSELL ASA event by number, or optionally compared by a number.</dl>
<dt><i>X-late IP addresses and ports</i></p>
<dd>
<dl>
<dt>
<dd> <code>[src|dst] xip &lt;ip&gt;</code><br />
 Select the translated IP address </p>
<p> <code>[src|dst] xnet &lt;net&gt;/&lt;num&gt;</code><br />
 with <i>&lt;net&gt;</i> as a valid translated IPv4 or IPv6 network and <i>&lt;num&gt;</i> as maskbits. The number of mask bits must match the appropriate address familiy in IPv4 or IPv6. Networks may be abreviated such as 172.16/16 if they are unambiguous. </p>
<p> <code>[src|dst] xport &lt;port&gt;</code><br />
 Select the translated port</dl>
<dt><i>NSEL/ASA ingress/egress</i></p>
<dd>
<dl>
<dt>
<dd> <code>ingress &lt;ACL|ACE|XACE&gt; [comp] number<br />
 Select/compare an ingress ACL </p>
<p> egress ACL [comp] &lt;number&gt;</code><br />
 Select/compare an egress ACL </p>
</dl>
<dt><code>NEL specific NAT filters:</code></p>
<dd></dl>
<p> <i>NAT Event</i></p>
<dl>
<dt>
<dd> <code>nat event &lt;add|delete&gt;</code><br />
 <code>nat event [comp] &lt;number&gt;</code><br />
 select NEL NAT event by name or number. If given as number it can be compared with a number
</dl>
<dl>
<dt><i>NEL NAT ip addresses and ports</i></p>
<dd>
<dl>
<dt>
<dd> <code>[src|dst] nip &lt;ip&gt;<br />
 Select the NAT IP address </p>
<p> [src|dst] nport &lt;port&gt;<br />
 Select the NAT port</dl>
<dt></code><i>NEL NAT vrf</i></p>
<dd> <code>ingress vrf &lt;num&gt;</code> Select the vrf </p>
</dl>
<h2>EXAMPLES</h2>
<p> <code>nfdump -r /and/dir/nfcapd.201107110845 -c 100 &#8216;proto tcp and ( src ip 172.16.17.18 or dst ip 172.16.17.19 )&#8217;</code> Dumps the first 100 netflow records which match the given filter: </p>
<p> <code>nfdump -r /and/dir/nfcapd.201107110845 -B</code> Map matching flows as bin-directional single flow. </p>
<p> <code>nfdump -R /and/dir/nfcapd.201107110845:nfcapd.200407110945 &#8216;host 192.168.1.2&#8217;</code> Dumps all netflow records of host 192.168.1.2 from July 11 08:45 &#8211; 09:45 </p>
<p> <code>nfdump -M /to/and/dir1:dir2 -R nfcapd.200407110845:nfcapd.200407110945 -s record -n 20</code> Generates the Top 20 statistics from 08:45 to 09:45 from 3 sources </p>
<p> <code>nfdump -r /and/dir/nfcapd.201107110845 -s record -n 20 -o extended</code> Generates the Top 20 statistics, extended output format </p>
<p> <code>nfdump -r /and/dir/nfcapd.201107110845 -s record -n 20 &#8216;in if 5 and bps &gt; 10k&#8217;</code> Generates the Top 20 statistics from flows comming from interface 5 </p>
<p> <code>nfdump -r /and/dir/nfcapd.201107110845 &#8216;inet6 and proto tcp and ( src port &gt; 1024 and dst port 80 )</code> Dumps all port 80 IPv6 connections to any web server.</p>
<h2>NOTES</h2>
<p> Generating the statistics for data files of a few hundred MB is no problem. However be careful if you want to create statistics of several GB of data. This may consume a lot of memory and can take a while. Flow anonymization has moved into nfanon.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-nfcapd/">nfcapd</a>(1), <a href="/docs/linux/man/1-nfanon/">nfanon</a>(1), <a href="/docs/linux/man/1-nfprofile/">nfprofile</a>(1), <a href="/docs/linux/man/1-nfreplay/">nfreplay</a>(1)</p>
<h2>BUGS</h2>
<p> There is still the famous last bug. Please report them &#8211; all the last bugs &#8211; back to me. </p>
<h2>Index</h2>
