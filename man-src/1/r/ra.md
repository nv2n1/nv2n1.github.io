---
title: "ra(1)"
name: "ra"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ra/"
description: "ra – read argus(8) data."
---

<h2>NAME</h2>
<p> <code>ra</code> &#8211; read <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data.</p>
<h2>SYNOPSIS</h2>
<p> <code>ra [raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ra</code> reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from either <i>stdin</i>, an <i>argus-file</i>, or from a remote data source, which can either be an <i>argus-server</i>, or a netflow data server, filters the records it encounters based on an optional <i>filter-expression</i> and either prints the contents of the <code><a href="/docs/linux/man/5-argus/">argus</a>(5)</code> records that it encounters to <code>stdout</code> or appends them into an <code><a href="/docs/linux/man/5-argus/">argus</a>(5)</code> datafile. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Print aggregate statistics for the input stream on termination.</p>
<dt><code>-b</code></p>
<dd> Dump the compiled transaction-matching code to standard output and stop. This is useful for debugging filter expressions.</p>
<dt><code>-c &lt;char&gt;</code></p>
<dd> Specify a delimiter character for output columns (default is &#8216; &#8216;).</p>
<dt><code>-C &lt;[host]:portnum&gt; (deprecated)</code></p>
<dd> Specify a source of Netflow data. The optional host is the local interface address where Netflow Cisco records are going to be read. If absent, then it is implied that the interface address is AF_ANY. This option is deprecated and the &#8216;-S <a href="cisco://address:port'">cisco://address:port&#8217;</a> is now the recommended option.</p>
<dt><code>-D &lt;level&gt;</code></p>
<dd> Print debug information corresponding to <code>&lt;level&gt;</code> to stderr, if program compiled to support debug printing. As the level increases, so does the amount of debug information <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> will print. Values range from 1-8.</p>
<dt><code>-d</code></p>
<dd> Toggle whether to run this program as a daemon.</p>
<dt><code>-e &lt;regex&gt;</code></p>
<dd> Match regular expression in flow user data fields. Prepend the regex with either &quot;s:&quot; or &quot;d:&quot; to limit the match to either the source or destination user data fields. At this time null bytes in the user data buffer terminate search. Examples include: </p>
<pre>
   &quot;^SSH-&quot;           - Look for ssh connections on any port.
   &quot;s:^GET&quot;          - Look for HTTP GET requests in the source buffer.
   &quot;d:^HTTP.*Unauth&quot; - Find unauthorized http response.
</pre>
<p> Depending on the regular expression library that the system supports, you will be able to match many types of binary, octal and hex expressions. See regex.3, pcre.3 and the web for examples. </p>
<dt><code>-E &lt;file&gt;</code></p>
<dd> When using a filter expression at the end of the command, this option will cause <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> to append the records that are rejected by the filter into <code>&lt;file&gt;</code></p>
<dt><code>-F &lt;conffile&gt;</code></p>
<dd> Use <code>&lt;conffile&gt;</code> as a source of configuration information. The format of this file is identical to <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5)</code>. The data read from <code>&lt;conffile&gt;</code> overrides any prior configuration information.</p>
<dt><code>-h</code></p>
<dd> Print an explanation of all the arguments.</p>
<dt><code>-H</code></p>
<dd> Abbreviate numeric metrics, to make reading large values easier. Use the <code>-p &lt;num&gt;</code> option to specify the precision right of the decimal. </p>
<dt><code>-L &lt;n&gt;</code></p>
<dd> Specify how <code>ra</code> will print header labels for the output. </p>
<pre><code>
   Supported values are:
      -1  Don't print header labels.
       0  Print the header labels only once, as the beginning of output.
     &gt; 0  Print the header labels every n lines of output.
-M &lt;mode [mode ...]&gt;
Provide addition mode operators.  These are generally specific to the
individual ra* program, or a specific function. Available modes for ra()
are:
   disa             - interpret DSCodepoints using the US DISA encodings
   dsrs=dsrlist     - process these dsrs
      Where a dsrlist has the format:
         [+/-]dsr[,[+/-]dsr]
 
         Supported dsrs are:
           trans    transport information, such as source id and seq number.
           flow     flow key data (proto, saddr, sport, dir, daddr, dport)
   time time stamp fields(stime, ltime).metric basic([s | d] bytes, [s | d] pkts, [s | d] rate, [s | d] load) agr aggregation stats(trans, avgdur, mindur, maxdur, stdev).net network objects(tcp, esp, rtp, icmp data).vlan VLAN tag data mpls MPLS label data jitter Jitter data([s | d] jit, [s | d] intpkt) ipattr IP attributes([s | d] ipid, [s | d] tos, [s | d] dsb, [s | d] ttl) psize packet size information mac MAC addresses(smac, dmac)
   icmp ICMP specific data(icmpmap, inode)
   encaps Flow encapsulation type indications
           behavior Behavioral metrics and data
               tadj Time adjustment data
                   cor Multi -
       probe correlation data
           cocode Country Codes
               asn Autonomous System Number data
                   suser src user captured data
                   bytes(suser)
   duser dst captured user data bytes(duser)

      Examples are:
         -M dsrs=time,flow,metric
         -M dsrs=-suser,-duser
   label="regex"    - match flow label with regex(3) regular expression.
   man              - print management records
   noman            - do not print management records
   oui              - print oui labels in mac addresses
   printer="format" - specify printer formats for printing user data.
      Supported formats are:
           ascii      print user buffer as ascii string. use '.' for unprintable chars.
           obfuscate  ascii printer with password obfuscation.
           hex        print hex dump of user buffer on separate lines.
           encode32   print user buffer as 32-bit chars.
           encode64   print user buffer using 64-bit chars.
   poll             - successfully attach to remote data source and then exit
   rmon             - modify data to support unidiretional RMON stat reporting
   rtime:factor     - read data from a file, clocking records in as if they
                      being read in realtime.  Factor provides an opportunity
                      to specify a multiplication factor, enabling you to
                      read records in a fraction of real time, slowing down
                      reading considerably, or a factor of time, enabling
                      controlled speedup of the reading rate.
   saslmech="mech"  - specify a mandatory SASL mech
   sql="select"     - use "select" as select clause in mysql calls when supported.
   TZ="tzset"       - specify a tzset(3) time zone specification
   uni              - generate unidirectional flow data
   xml              - print output in xml format.
</code></pre>
<p> Illegal modes are not detectable by the standard library, and so unexpected results in command line parsing may occur if care is not taken with use of this option.</p>
<dt><code>-n</code></p>
<dd> Modify number to name converstion. This flag supports 4 states, specified by the modulus of the number of -n flags set. By default ra* programs do not provide hostname lookups, but they do lookup port and protocol names. The first <code>-n</code> will suppress port number to service conversion, <code>-nn</code> will suppress translation of protocol numbers to names (no lookups). <code>-nnn</code> will return you to full conversion, translating hostnames, port and protocol names, and <code>-nnnn</code> will return you to the default behavior. Because this indicator can be set in the .rarc file, multiple <code>-n</code> flags progress through the cycle.</p>
<dt><code>-N [io]&lt;num&gt;, [io]&lt;start-end&gt;, [io]&lt;start+num&gt;</code></p>
<dd> Process the first <code>&lt;num&gt;</code> records, the inclusive range <code>&lt;start &#8211; end&gt;</code>, or process &lt;num + 1&gt; records starting at index number <code>&lt;start&gt;</code>. The optional 1st character indicates whether the specification is applied to the input or the output stream of records, the default is input. If applied to the input, these are the range of records that match the input filter.</p>
<dt><code>-p &lt;digits&gt;</code></p>
<dd> Print <code>&lt;digits&gt;</code> number of units of precision for floating point values.</p>
<dt><code>-q</code></p>
<dd> Run in quiet mode. Configure Ra to not print out the contents of records. This can be used for a number of maintenance tasks, where you would be interested in the outcome of a program, or its progress, say with the -D option, without printing each input record.</p>
<dt><code>-r [- | &lt;[type:]file[::soffset[:eoffset]] &#8230;&gt;]</code></p>
<dd> Read <code>&lt;type&gt;</code> data from <code>&lt;files&gt;</code> in the order presented on the commandline. &#8216;<code>&#8211;</code>&#8216; denotes stdin. Ra supports reading <code>argus</code> type data (default), <code>cisco</code> and <code>ft</code>, flow-tools type data. If you want to read a set of files and then, when done, read stdin, use multiple occurences of the <i>-r</i> option. Ra can read <code><a href="/docs/linux/man/1-gzip/">gzip</a>(1)</code>, <code><a href="/docs/linux/man/1-bzip2/">bzip2</a>(1)</code>, <code><a href="/docs/linux/man/1-xz/">xz</a>(1)</code> and <code><a href="/docs/linux/man/1-compress/">compress</a>(1)</code> compressed data files. Byte offset values allow the specification of a range of records within an uncompressed file. Byte offsets must be aligned to record boundaries. Valid record offsets can be obtained using +offset as an output field even from compressed files. </p>
<p> Examples are: </p>
<pre>
   -r file1 file2              read argus records from file1, then file2.
   -r file::34876              read argus records starting at byte offset 34876 
   -r file::34876:35846        read argus records starting at byte offset 34876 and ending at 35846 
   -r cisco:file               read cisco netflow records from file
   -r ft:file                  read flow-tools based records
</pre>
<dt><code>-R &lt;dir dir &#8230;&gt;</code></p>
<dd> Recursively decend the directory and process all the regular files that are encountered. The function does not decend to links, or directories that begin with &#8216;.&#8217;. The feature, like the -r command, does not do any file type checking.</p>
<dt><code>-s &lt;[-][[+[#]]field[:len[:format]] &#8230;&gt;</code></p>
<dd> Specify the <code>fields</code> to print. <code>ra.1</code> gets the field print list either from its rarc configuration files or from the command-line. In the case where there is no configuration given <code>ra.1</code> uses a default printing field list, with default field lengths. By specifying a space separated list of fields, this option provides a means to completely redefine the list from the command line. Using the optional &#8216;-&#8216; and &#8216;+[#]&#8217; prepended to the field list, you can add or subtract fields from the configured list. Field lengths are hard constraints, and field output that exceeds the field length will be truncated, and a &#8216;*&#8217; will be inserted as the last character. When you see this, add more to the length specification for that specific field. Field lengths (len) less than 1, are not permitted and will generate an error. The optional &#8216;format&#8217; specification, uses <code>sprintf.1</code> syntax to format the value. The available fields to print are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>srcid</code></p>
<dd> argus source identifier.</p>
<dt><code>rank</code></p>
<dd> Ordinal value of this output flow record i.e. sequence number.</p>
<dt><code>stime</code></p>
<dd> record start time</p>
<dt><code>ltime</code></p>
<dd> record last time.</p>
<dt><code>trans</code></p>
<dd> aggregation record count.</p>
<dt><code>flgs</code></p>
<dd> flow state flags seen in transaction.</p>
<dt><code>seq</code></p>
<dd> argus sequence number.</p>
<dt><code>dur</code></p>
<dd> record total duration.</p>
<dt><code>runtime</code></p>
<dd> total active flow run time. This value is generated through aggregation, and is the sum of the records duration.</p>
<dt><code>idle</code></p>
<dd> time since the last packet activity. This value is useful in real-time processing, and is the current time &#8211; last time.</p>
<dt><code>mean</code></p>
<dd> average duration of aggregated records.</p>
<dt><code>stddev</code></p>
<dd> standard deviation of aggregated duration times.</p>
<dt><code>sum</code></p>
<dd> total accumulated durations of aggregated records.</p>
<dt><code>min</code></p>
<dd> minimum duration of aggregated records.</p>
<dt><code>max</code></p>
<dd> maximum duration of aggregated records.</p>
<dt><code>smac</code></p>
<dd> source MAC addr.</p>
<dt><code>dmac</code></p>
<dd> destination MAC addr.</p>
<dt><code>soui</code></p>
<dd> oui portion of the source MAC addr.</p>
<dt><code>doui</code></p>
<dd> oui portion of the destination MAC addr.</p>
<dt><code>saddr</code></p>
<dd> source IP addr.</p>
<dt><code>daddr</code></p>
<dd> destination IP addr.</p>
<dt><code>proto</code></p>
<dd> transaction protocol.</p>
<dt><code>sport</code></p>
<dd> source port number.</p>
<dt><code>dport</code></p>
<dd> destination port number.</p>
<dt><code>stos</code></p>
<dd> source TOS byte value.</p>
<dt><code>dtos</code></p>
<dd> destination TOS byte value.</p>
<dt><code>sdsb</code></p>
<dd> source diff serve byte value.</p>
<dt><code>ddsb</code></p>
<dd> destination diff serve byte value.</p>
<dt><code>sco</code></p>
<dd> source IP address country code.</p>
<dt><code>dco</code></p>
<dd> destination IP address country code.</p>
<dt><code>sttl</code></p>
<dd> src -&gt; dst TTL value.</p>
<dt><code>dttl</code></p>
<dd> dst -&gt; src TTL value.</p>
<dt><code>shops</code></p>
<dd> estimate of number of IP hops from src to this point.</p>
<dt><code>dhops</code></p>
<dd> estimate of number of IP hops from dst to this point.</p>
<dt><code>sipid</code></p>
<dd> source IP identifier.</p>
<dt><code>dipid</code></p>
<dd> destination IP identifier.</p>
<dt><code>smpls</code></p>
<dd> source MPLS identifier.</p>
<dt><code>dmpls</code></p>
<dd> destination MPLS identifier.</p>
<dt><code>autoid</code></p>
<dd> Auto generated identifier (mysql).</p>
<dt><code>sas</code></p>
<dd> Src origin AS</p>
<dt><code>das</code></p>
<dd> Dst origin AS</p>
<dt><code>ias</code></p>
<dd> Intermediate origin AS, AS of ICMP generator</p>
<dt><code>cause</code></p>
<dd> Argus record cause code. Valid values are Start, Status, Stop, Close, Error</p>
<dt><code>nstroke</code></p>
<dd> Number of observed keystrokes.</p>
<dt><code>snstroke</code></p>
<dd> Number of observed keystrokes from initiator (src) to target (dst).</p>
<dt><code>dnstroke</code></p>
<dd> Number of observed keystrokes from target (dst) to initiator (src).</p>
<dt><code>pkts</code></p>
<dd> total transaction packet count.</p>
<dt><code>spkts</code></p>
<dd> src -&gt; dst packet count.</p>
<dt><code>dpkts</code></p>
<dd> dst -&gt; src packet count.</p>
<dt><code>bytes</code></p>
<dd> total transaction bytes.</p>
<dt><code>sbytes</code></p>
<dd> src -&gt; dst transaction bytes.</p>
<dt><code>dbytes</code></p>
<dd> dst -&gt; src transaction bytes.</p>
<dt><code>appbytes</code></p>
<dd> total application bytes.</p>
<dt><code>sappbytes</code></p>
<dd> src -&gt; dst application bytes.</p>
<dt><code>dappbytes</code></p>
<dd> dst -&gt; src application bytes.</p>
<dt><code>pcr</code></p>
<dd> producer consumer ratio.</p>
<dt><code>load</code></p>
<dd> bits per second.</p>
<dt><code>sload</code></p>
<dd> source bits per second.</p>
<dt><code>dload</code></p>
<dd> destination bits per second.</p>
<dt><code>loss</code></p>
<dd> pkts retransmitted or dropped.</p>
<dt><code>sloss</code></p>
<dd> source pkts retransmitted or dropped.</p>
<dt><code>dloss</code></p>
<dd> destination pkts retransmitted or dropped.</p>
<dt><code>ploss</code></p>
<dd> percent pkts retransmitted or dropped.</p>
<dt><code>psloss</code></p>
<dd> percent source pkts retransmitted or dropped.</p>
<dt><code>pdloss</code></p>
<dd> percent destination pkts retransmitted or dropped.</p>
<dt><code>retrans</code></p>
<dd> pkts retransmitted.</p>
<dt><code>sretrans</code></p>
<dd> source pkts retransmitted.</p>
<dt><code>dretrans</code></p>
<dd> destination pkts retransmitted.</p>
<dt><code>pretrans</code></p>
<dd> percent pkts retransmitted.</p>
<dt><code>psretrans</code></p>
<dd> percent source pkts retransmitted.</p>
<dt><code>pdretrans</code></p>
<dd> percent destination pkts retransmitted.</p>
<dt><code>sgap</code></p>
<dd> source bytes missing in the data stream. Available after argus-3.0.4</p>
<dt><code>dgap</code></p>
<dd> destination bytes missing in the data stream. Available after argus-3.0.4</p>
<dt><code>rate</code></p>
<dd> pkts per second.</p>
<dt><code>srate</code></p>
<dd> source pkts per second.</p>
<dt><code>drate</code></p>
<dd> destination pkts per second.</p>
<dt><code>dir</code></p>
<dd> direction of transaction</p>
<dt><code>sintpkt</code></p>
<dd> source interpacket arrival time (mSec)</p>
<dt><code>sintdist</code></p>
<dd> source interpacket arrival time distribution</p>
<dt><code>sintpktact</code></p>
<dd> source active interpacket arrival time (mSec)</p>
<dt><code>sintdistact</code></p>
<dd> source active interpacket arrival time (mSec)</p>
<dt><code>sintpktidl</code></p>
<dd> source idle interpacket arrival time (mSec)</p>
<dt><code>sintdistidl</code></p>
<dd> source idle interpacket arrival time (mSec)</p>
<dt><code>dintpkt</code></p>
<dd> destination interpacket arrival time (mSec)</p>
<dt><code>dintdist</code></p>
<dd> destination interpacket arrival time distribution</p>
<dt><code>dintpktact</code></p>
<dd> destination active interpacket arrival time (mSec)</p>
<dt><code>dintdistact</code></p>
<dd> destination active interpacket arrival time distribution (mSec)</p>
<dt><code>dintpktidl</code></p>
<dd> destination idle interpacket arrival time (mSec)</p>
<dt><code>dintdistidl</code></p>
<dd> destination idle interpacket arrival time distribution</p>
<dt><code>sjit</code></p>
<dd> source jitter (mSec).</p>
<dt><code>sjitact</code></p>
<dd> source active jitter (mSec).</p>
<dt><code>sjitidle</code></p>
<dd> source idle jitter (mSec).</p>
<dt><code>djit</code></p>
<dd> destination jitter (mSec).</p>
<dt><code>djitact</code></p>
<dd> destination active jitter (mSec).</p>
<dt><code>djitidle</code></p>
<dd> destination idle jitter (mSec).</p>
<dt><code>state</code></p>
<dd> transaction state</p>
<dt><code>label</code></p>
<dd> Metadata label.</p>
<dt><code>suser</code></p>
<dd> source user data buffer.</p>
<dt><code>duser</code></p>
<dd> destination user data buffer.</p>
<dt><code>swin</code></p>
<dd> source TCP window advertisement.</p>
<dt><code>dwin</code></p>
<dd> destination TCP window advertisement.</p>
<dt><code>svlan</code></p>
<dd> source VLAN identifier.</p>
<dt><code>dvlan</code></p>
<dd> destination VLAN identifier.</p>
<dt><code>svid</code></p>
<dd> source VLAN identifier.</p>
<dt><code>dvid</code></p>
<dd> destination VLAN identifier.</p>
<dt><code>svpri</code></p>
<dd> source VLAN priority.</p>
<dt><code>dvpri</code></p>
<dd> destination VLAN priority.</p>
<dt><code>srng</code></p>
<dd> start time for the filter timerange.</p>
<dt><code>erng</code></p>
<dd> end time for the filter timerange.</p>
<dt><code>stcpb</code></p>
<dd> source TCP base sequence number</p>
<dt><code>dtcpb</code></p>
<dd> destination TCP base sequence number</p>
<dt><code>tcprtt</code></p>
<dd> TCP connection setup round-trip time, the sum of &#8216;synack&#8217; and &#8216;ackdat&#8217;.</p>
<dt><code>synack</code></p>
<dd> TCP connection setup time, the time between the SYN and the SYN_ACK packets.</p>
<dt><code>ackdat</code></p>
<dd> TCP connection setup time, the time between the SYN_ACK and the ACK packets.</p>
<dt><code>tcpopt</code></p>
<dd> The TCP connection options seen at initiation. The <i>tcpopt</i> indicator consists of a fixed length field, that reports presence of any of the TCP options that argus tracks The format is:<br />
 M            &#8211;  Maxiumum Segment Size<br />
  w           &#8211;  Window Scale<br />
   s          &#8211;  Selective ACK OK<br />
    S         &#8211;  Selective ACK<br />
     e        &#8211;  TCP Echo<br />
      E       &#8211;  TCP Echo Reply<br />
       T      &#8211;  TCP Timestamp<br />
        c     &#8211;  TCP CC<br />
         N    &#8211;  TCP CC New<br />
          O   &#8211;  TCP CC Echo<br />
           S  &#8211;  Source Explicit Congestion Notification<br />
            D &#8211;  Destination Explicit Congestion Notification<br />
inode<br />
ICMP intermediate node.<br />
offset<br />
record byte offset in file or stream.<br />
smeansz<br />
Mean of the flow packet size transmitted by the src (initiator).<br />
dmeansz<br />
Mean of the flow packet size transmitted by the dst (target).<br />
spktsz<br />
histogram for the src packet size distribution<br />
smaxsz<br />
maximum packet size for traffic transmitted by the src.<br />
dpktsz<br />
histogram for the dst packet size distribution<br />
dmaxsz<br />
maximum packet size for traffic transmitted by the dst.<br />
sminsz<br />
minimum packet size for traffic transmitted by the src.<br />
dminsz<br />
minimum packet size for traffic transmitted by the dst.<br />
dminsz<br />
minimum packet size for traffic transmitted by the dst.</p>
<p>Examles are:<br />
   -s saddr      print only the source address.<br />
   -s -bytes     removes the bytes field from list.<br />
   -s +2srcid    adds the source identifier as the 2nd field.<br />
   -s spkts:18   prints src pkt count with a column width of 18.<br />
   -s smpls      print the local mpls label in the flow.
</dl>
<dt><code>-S &lt;[URI://][user[:pass]@]host[:portnum]&gt;</code></p>
<dd> Specify a remote source of flow data. Read flow data from various data format and transport strategies, using the URI format to indicate the type of flow data record of interest (argus-tcp, argus-udp, cisco, jflow, sflow) and the source, as a name or an addresss, providing an option user and password for protected access. Use the optional &#8216;:portnum&#8217; to specify a port number other than the default; 561. </p>
<p> Examles are:<br />
&#8211; S localhost request remote argus records from localhost, using default methods.- S user[at] localhost request argus records from localhost, as &#8216;user&#8217;.- S user:pass[at] localhost request argus records from localhost, as &#8216;user&#8217;, with &#8216;pass&#8217; password.- S 192.168.0.4:12345 request via TCP argus records from 192.168.0.4, port 12345. &#8211; S argus: // user@anubis       request argus records from anubis, via TCP port 561, as &#8216;user&#8217;.<br />
                                                                                                                                                                                                                                                                                                                                                    -S argus &#8211;<br />
                                                                                                                                                             tcp: // thoth:12345   request argus records via TCP from thoth, port 12345.<br />
                                                                                                                                                                 -S argus &#8211;<br />
                                                                                                                                                             udp: // set:12345     request argus records via UDP from set, port 12345.<br />
                                                                                                                                                                 -S<br />
                                                                                                                                                           cisco: // any:9996          read cisco netflow records from AF_ANY, on port 9996.<br />
                                                                                                                                                               -S<br />
                                                                                                                                                           jflow: // 10.0.0.2:9898     read jflow records sent to 10.0.0.2, on port 9898.<br />
                                                                                                                                                               -S<br />
                                                                                                                                                           sflow: // localhost:6343    read sflow records sent to localhost interface, port 6343.</p>
<dt><code>-t &lt;timerange&gt;</code></p>
<dd> Specify the <code>&lt;time range&gt;</code> for matching <code><a href="/docs/linux/man/5-argus/">argus</a>(5)</code> records. This option supports a high degree of flexibility in specifing explicit and relative time ranges with support for time field wildcarding. </p>
<p> The syntax for the <code>&lt;time range&gt;</code> is: </p>
<pre><code>
[timeComparisonInd] timeSpecification[-timeSpecification] timeComparisonInd : [x] i | n | c(default = i) x negation reverses the result of the time comparison i intersects match records that were active during this time period n includes match records that start before and end after the period c contained match records that start and end during the period timeSpecification : [[[yyyy / ] mm / ] dd.] HH[:MM[:SS]]
    [yyyy / ] mm / dd yyyy
    % d{ymdHMS} seconds{+ | -} % d{ymdHMS} where '*' can be used as a wildcard.
</code></pre>
<p> Examples are: </p>
<pre>
   -t 14              specify the time range 2pm-3pm for today
   -t 15-23           specify the time range 3pm-11pm for today
   -t 2011            all records in the year 2011
   -t 2011/08         all records in Aug of the year 2011
   -t 2011/08-2011/10 all records in Aug, Sept, and Oct of the year 2011
   -t **.14           specify 2pm-3pm, every day this month
   -t 1270616652+2s   all records that span 10/04/07.01:04:12 EDT.
   -t 1999y1m23d10h   matches 10-11am on Jan, 23, 1999
   -t 10d*h*m15s      matches records that intersect the 15 sec,
                      any minute, any hour, on the 10th of this month
   -t ****/11/23      all records in Nov 23rd, any year
   -t 23.11:10-14     11:10:00 - 2pm on the 23rd of this month
   -t -10m            matches 10 minutes before, to the present
   -t -1M+1d          matches the first day of the this month.
   -t -2h5m+5m        matches records that start before and end
                      after the range starting 2 hours 5 minutes
                      prior to the present, and lasting 5 minutes.
</pre>
<p> Time is compared using basic intersection operations. A record <code>iPntersects a specified time range if there is any intersection between the time range of the record and the comparison time range. This is the default behavior. A record i</code>ncludes the comparison time range if the intersection of the two ranges equals the comparison time, and a record is <code>c</code>ontained when the intersection equals the duration of the record. The comparison indicator is the first character of the range specification, without spaces. </p>
<p> Examples are: </p>
<pre>
   -t n14:10:15-14:10:19  records include these 4s.
   -t c14:10-14:10:10     record starts and ends within these 10s.
   -t xi-5s+25s           record starts or ends 5 seconds earlier and
                          20 seconds after 'now'.
</pre>
<dt><code>-T &lt;secs&gt;</code></p>
<dd> Read <code><a href="/docs/linux/man/5-argus/">argus</a>(5)</code> from remote server for <code>&lt;secs&gt;</code> of time.</p>
<dt><code>-u</code></p>
<dd> Print time values using Unix time format (seconds from the Epoch).</p>
<dt><code>-w &lt;file&gt; [filter-expression]</code></p>
<dd> Append matching data to <code>&lt;file&gt;</code>, in <code>argus</code> file format. An <i>output-file</i> of &#8216;-&#8216; directs <code>ra</code> to write the <code><a href="/docs/linux/man/5-argus/">argus</a>(5)</code> records to stdout, allowing for &quot;chaining&quot; <code>ra*</code> style commands together. The optional filter-expression can be used to select specific output.</p>
<dt><code>-X</code></p>
<dd> Resets all options to their default values and overrides the rarc file contents (Use as the first option.)</p>
<dt><code>-z</code></p>
<dd> Modify status field to represent TCP state changes. The values of the status field when this is enabled are: </p>
<pre>
  's' - Syn Transmitted
  'S' - Syn Acknowledged
  'E' - TCP Established
  'f' - Fin Transmitted  (FIN Wait State 1)
  'F' - Fin Acknowledged (FIN Wait State 2)
  'R' - TCP Reset
</pre>
<dt><code>-Z &lt;s|d|b&gt;</code></p>
<dd> Modify status field to reprsent actual TCP flag values. &lt;&#8216;s&#8217;rc | &#8216;d&#8217;st | &#8216;b&#8217;oth&gt;. The characters that can be present in the status field when this is enabled are: </p>
<pre>
  'F' - Fin
  'S' - Syn
  'R' - Reset
  'P' - Push
  'A' - Ack
  'U' - Urgent Pointer
  '7' - Undefined 7th bit set
  '8' - Undefined 8th bit set
</pre>
</dl>
<h2>RETURN VALUES</h2>
<p> <code>ra</code> exits with one of the following values: </p>
<pre>
   0  Records matched condition, considering the options provided.  
   1  No records matched the condition, or the source was not an argus stream.
 &gt; 1  An error occurred.
</pre>
<h2>FILTER EXPRESSION</h2>
<p> If arguments remain after option processing, the collection is interpreted as a single filter <code>expression</code>. In order to indicate the end of arguments, a &#8216;&#8211;&#8216; (double dash) is required before the filter expression is added to the command line. Historically, a &#8216;-&#8216; (single dash) was used to separate the filter <code>expression</code> from the command line options, but newer versions of <code>getopt.1</code> now require the &#8216;&#8211;&#8216; (double dash). </p>
<p> The filter expression specifies which <code><a href="/docs/linux/man/5-argus/">argus</a>(5)</code> records will be selected for processing. If no <i>expression</i> is given, all records are selected, otherwise, only those records for which <i>expression</i> is `true&#8217; will be printed. </p>
<p> The syntax is very similar to the expression syntax for <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1)</code>, as the tcpdump compiler was a starting point for the <code><a href="/docs/linux/man/5-argus/">argus</a>(5)</code> filter expression compiler. However, the semantics for <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1)&#8217;s</code> packet filter expressions are different when applied to transaction record filtering, so there are some major differences. </p>
<p> When attached to a remote argus, <code>ra</code> will send the filter to the argus process, which compiles the filter, and uses it to select which argus records will be transmitted to the <code>ra</code> application. If you do not want to send a filter to the remote argus, prepend the filter with the keyword &quot;local&quot;, to indicate that the filtering will be done within the local <code>ra</code> process. </p>
<p> The <i>expression</i> consists of one or more <i>primitives.</i> Primitives usually consist of an <i>id</i> (name or number) preceded by one or more qualifiers. There are three different kinds of qualifier:</p>
<dl>
<dt><i>type</i></p>
<dd> qualifiers say what kind of thing the id name or number refers to. Possible types are <code>srcid,</code> <code>encaps,</code> <code>ether,</code> <code>host,</code> <code>net,</code> <code>co,</code> <code>port,</code> <code>tos,</code> <code>ttl,</code> <code>ptks,</code> <code>bytes,</code> <code>appbytes,</code> <code>pcr,</code> <code>data,</code> <code>rate,</code> <code>load,</code> <code>loss,</code> <code>ploss,</code> <code>vid,</code> <code>vpri,</code> and <code>mid.</code> </p>
<p> E.g., `srcid isis`, `encaps gre&#8217;, `host sphynx&#8217;, `net 192.168.0.0/16&#8242;, `port domain&#8217;, `ttl 1&#8242;, &#8216;ptks gt 2&#8217;, &#8216;ploss lt 5&#8217;. If there is no type qualifier, <code>host</code> is assumed.</p>
<dt><i>dir</i></p>
<dd> qualifiers specify a particular transfer direction to and/or from <i>an id.</i> Possible directions are <code>src</code>, <code>dst</code>, <code>src or dst</code> and <code>src and dst</code>. E.g., `src sphynx&#8217;, `dst net 192.168.0.0/24&#8242;, `src or dst port ftp&#8217;, `src and dst tos 0x0a&#8217;, `src or dst vid 0x12`, `dst vpri 0x02` . If there is no dir qualifier, <code>src or dst</code> is assumed.</p>
<dt><i>proto</i></p>
<dd> qualifiers restrict the match to a particular protocol. Possible values are those specified in the <code>/etc/protocols</code> system file and a small number of extensions, (that should be defined but aren&#8217;t). Specific extended values are <code>&#8216;ipv4&#8217;</code>, (to specify just ip version 4), in contrast to the defined proto <code>&#8216;ipv6&#8217;</code>. The defined proto <code>&#8216;ip&#8217;</code> reduces to the filter &#8216;ipv4 or ipv6&#8217;. </p>
<p> When preceeded by <i>ether</i>, the protocol names and numbers that are valid are specified in ./include/ethernames.h.</dl>
<p> In addition to the above, there are some special `primitive&#8217; keywords that don&#8217;t follow the pattern: <code>gateway</code>, <code>multicast</code>, and <code>broadcast</code>. All of these are described below. </p>
<p> More complex filter expressions are built up by using the words <code>and</code>, <code>or</code> and <code>not</code> to combine primitives. E.g., `host foo and not port ftp and not port ftp-data&#8217;. To save typing, identical qualifier lists can be omitted. E.g., `tcp dst port ftp or ftp-data or domain&#8217; is exactly the same as `tcp dst port ftp or tcp dst port ftp-data or tcp dst port domain&#8217;. </p>
<p> Allowable primitives are:</p>
<dl>
<dt><code>srcid </code><i>argusid</i></p>
<dd> True if the argus identifier field in the Argus record is <i>srcid</i>, which may be an IP address, a name or a decimal/hexidecimal number.</p>
<dt><code>seq [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if the transport sequence number in the Argus record matches the <i>sequence number expression</i>.</p>
<dt><code>encaps </code><i>type</i></p>
<dd> True if the encapsulation used by the flow in the Argus record includes the <i>type</i>. The list of valid encapsulation types is: </p>
<pre>
   eth, mpls, 802q, llc, pppoe, isl, gre, erspan, ah, ipnip, ipnip6, hdlc, chdlc,
   atm, sll, fddi, slip, arc, wlan, prism, avs, lrh, grh, teredo, udt, ipsec, juniper
<dt><code>dst host </code><i>host</i><dd>True if the IP destination field in the Argus record is <i>host</i>,
which may be either an address or a name.
<dt><code>src host </code><i>host</i><dd>True if the IP source field in the Argus record is <i>host</i>.
<dt><code>host </code><i>host</i><dd>True if either the IP source or destination in the Argus record is <i>host</i>.
Any of the above host expressions can be prepended with the keywords
<code>ip</code>, <code>arp</code>, or <code>rarp</code> as in:
<code>ip</code> host <i>host</i>
</pre>
<p> which is equivalent to: </p>
<pre>
<code>ether proto ip</code> and host <i>host</i>
</pre>
<p> If <i>host</i> is a name with multiple IP addresses, each address will be checked for a match.</p>
<dt><code>ether dst </code><i>ehost</i></p>
<dd> True if the ethernet destination address is <i>ehost</i>. <i>Ehost</i> may be either a name from /etc/ethers or a number (see <i><a href="//www.systutorials.com/docs/linux/man/3N-ethers/">ethers</a></i>(3N) for numeric format).</p>
<dt><code>ether src </code><i>ehost</i></p>
<dd> True if the ethernet source address is <i>ehost</i>.</p>
<dt><code>ether host </code><i>ehost</i></p>
<dd> True if either the ethernet source or destination address is <i>ehost</i>.</p>
<dt><code>gateway</code> <i>host</i></p>
<dd> True if the transaction used <i>host</i> as a gateway. I.e., the ethernet source or destination address was <i>host</i> but neither the IP source nor the IP destination was <i>host</i>. <i>Host</i> must be a name and must be found in both /etc/hosts and /etc/ethers. (An equivalent expression is </p>
<pre>
<code>ether host </code><i>ehost </i><code>and not host </code><i>host</i>
</pre>
<p> which can be used with either names or numbers for <i>host / ehost</i>.)</p>
<dt><code>dst net </code><i>cidr</i></p>
<dd> True if the IP destination address in the Argus record matches the <i>cidr</i> address.</p>
<dt><code>src net </code><i>cidr</i></p>
<dd> True if the IP source address in the Argus record matches the <i>cidr</i> address.</p>
<dt><code>net </code><i>cidr</i></p>
<dd> True if either the IP source or destination address in the Argus record matches <i>cidr</i> address.</p>
<dt><code>dst port </code><i>port</i></p>
<dd> True if the network transaction is IP based, using either the TCP or UDP transport protocols, and a destination port value of <i>port</i>. The <i>port</i> can be a number or a name as configured in the /etc/services file.(see <i><a href="//www.systutorials.com/docs/linux/man/4P-tcp/">tcp</a></i>(4P) and <i><a href="//www.systutorials.com/docs/linux/man/4P-udp/">udp</a></i>(4P)). If a name is used, both the protocol number and port number, are checked. If a number or ambiguous name is used, the port number is checked for both UDP and TCP protocols (e.g., <code>dst port 513</code> will print both tcp/login traffic and udp/who traffic, and <code>port domain</code> will match both tcp/domain and udp/domain traffic). Port ranges can be specified using numeric values, such as <code>port 53-215</code>. </p>
<dt><code>src port </code><i>port</i></p>
<dd> True if the network transaction has a source port value of <i>port</i>.</p>
<dt><code>port </code><i>port</i></p>
<dd> True if either the source or destination port in the Argus record is <i>port</i>. Any of the above port expressions can be prepended with the keywords, <code>tcp</code> or <code>udp</code>, as in: </p>
<pre>
<code>tcp src port </code><i>port</i>
</pre>
<p> which matches only tcp connections.</p>
<dt><code>ip proto </code><i>protocol</i></p>
<dd> True if the Argus record is an ip transaction (see <i><a href="//www.systutorials.com/docs/linux/man/4P-ip/">ip</a></i>(4P)) of protocol type <i>protocol</i>. <i>Protocol</i> can be a number or any of the string values found in <i>/etc/protocols</i>.</p>
<dt><code>multicast</code></p>
<dd> True if the network transaction involved an ip multicast address. By specifing ether multicast, you can select argus records that involve an ethernet multicast address.</p>
<dt><code>broadcast</code></p>
<dd> True if the network transaction involved an ip broadcast address. By specifing ether broadcast, you can select argus records that involve an ethernet broadcast address.</p>
<dt><code>ether proto </code><i>protocol</i></p>
<dd> True if the Argus record is of ether type <i>protocol</i>. <i>Protocol</i> can be a number or a name like <i>ip</i>, <i>arp</i>, or <i>rarp</i>.</p>
<dt><code>[src | dst] ttl [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if the TTL in the Argus record equals <i>number</i>.</p>
<dt><code>[src | dst] tos [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if the TOS in the Argus record (default) equals <i>number</i>.</p>
<dt><code>[src | dst] vid [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if th VLAN id in the Argus record (default) equals <i>number</i>.</p>
<dt><code>[src | dst] vpri [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if the VLAN priority in the Argus record (default) equals <i>number</i>.</p>
<dt><code>[src | dst] mid [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if the MPLS Label in the Argus record (default) equals <i>number</i>.</p>
<dt><code>[src | dst] pkts [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if the packet count in the Argus record (default) equals <i>number</i>.</p>
<dt><code>[src | dst] bytes [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if the byte count in the Argus record (default) equals <i>number</i>.</p>
<dt><code>[src | dst] appbytes [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if the application byte count in the Argus record (default) equals <i>number</i>.</p>
<dt><code>[src | dst] rate [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if the rate in the Argus record (default) equals <i>number</i>.</p>
<dt><code>[src | dst] load [gt | gte | lt | lte | eq] </code><i>number</i></p>
<dd> True if the load in the Argus record (default) equals <i>number</i>. </p>
</dl>
<p> Ra filter expressions support primitives that are specific to flow states and can be used to select flow records that were in these states at the time they were generated. <i>normal</i>, <i>wait</i>, <i>timeout</i>, <i>est</i> or <i>con</i> </p>
<p> Primitives that select flows that experienced fragmentation. <i>frag</i> and <i>fragonly</i> </p>
<p> Support for selecting flows that used multiple pairs of MAC addresses during their lifetime. <i>multipath</i> </p>
<p> Primitives specific to TCP flows are supported. <i>syn</i>, <i>synack</i>, <i>ecn</i>, <i>fin</i>, <i>finack</i>, <i>reset</i>, <i>retrans</i>, <i>outoforder</i> and <i>winshut</i> </p>
<p> Primitives specific to TCP options are supported. <i>tcpopt</i>, <i>mss</i>, <i>wscale</i>, <i>selackok</i>, <i>selack</i>, <i>tcpecho</i>, <i>tcpechoreply</i>, <i>tcptimestamp</i>, <i>tcpcc</i>, <i>tcpccnew</i>, <i>tcpccecho</i>, <i>secn</i> and <i>decn</i> </p>
<p> Primitives specific to ICMP flows are supported. <i>echo</i>, <i>unreach</i>, <i>redirect</i> and <i>timexed</i> </p>
<p> For some primitives, a direction qualifier is appropriate. These are <i>frag</i>, <i>reset</i>, <i>retrans</i>, <i>outoforder</i> and <i>winshut</i> </p>
<p> Primitives may be combined using:</p>
<dl>
<dt>
<dd> A parenthesized group of primitives and operators (parentheses are special to the Shell and must be escaped).</p>
<dt>
<dd> Negation (`<code>!</code>&#8216; or `<code>not</code>&#8216;).</p>
<dt>
<dd> Concatenation (`<code>and</code>&#8216;).</p>
<dt>
<dd> Alternation (`<code>or</code>&#8216;).</dl>
<p> Negation has highest precedence. Alternation and concatenation have equal precedence and associate left to right. Note that explicit <code>and</code> tokens, not juxtaposition, are now required for concatenation. </p>
<p> If an identifier is given without a keyword, the most recent keyword is assumed. For example, </p>
<pre>
<code>not host sphynx and anubis</code>
</pre>
<p> is short for </p>
<pre>
<code>not host sphynx and host anubis</code>
</pre>
<p> which should not be confused with </p>
<pre>
<code>not ( host sphynx or anubis )</code>
</pre>
<p> Expression arguments can be passed to <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> as either a single argument or as multiple arguments, whichever is more convenient. Generally, if the expression contains Shell metacharacters, it is easier to pass it as a single, quoted argument. Multiple arguments are concatenated with spaces before being parsed. </p>
<h3>Startup Processing</h3>
<p> <code>Ra</code> begins by searching for the configuration file <code>.rarc</code> first in the directory, <code>$ARGUSHOME</code> and then <code>$HOME</code>. If a <code>.rarc</code> is found, all variables specified in the file are set. </p>
<p> <code>Ra</code> then parses its command line options and set its internal variables accordingly. </p>
<p> If a configuration file is specified on the command-line, using the &quot;-f &lt;confile&gt;&quot; option, the values in this .rarc formatted file superceed all other values. </p>
<h2>EXAMPLES</h2>
<p> To report all TCP transactions from and to host &#8216;narly.wave.com&#8217;, reading transaction data from <i>argus-file</i> argus.data:</p>
<dl>
<dt>
<dd>
<pre>
<code>ra -r argus.data - tcp and host narly.wave.com</code>
</pre>
</dl>
<p> To report all UDP based DNS traffic, reading transaction data from the remote <i>argus.server</i>:</p>
<dl>
<dt>
<dd>
<pre>
<code>ra -S argus.server - udp port domain
</code></pre>
</dl>
<p> To report all UDP transactions seen by the remote <i>argus.server</i> on the port range 53-256, but not sending the filter to the remote argus process:</p>
<dl>
<dt>
<dd>
<pre>
<code>ra -S argus.server - local udp port 53-256
</code></pre>
</dl>
<p> Create the <i>argus-file</i> icmp.log with all ICMP events involving the host nimrod, using data from <i>argus-file</i>, but reading the transaction data from <i>stdin</i>:</p>
<dl>
<dt>
<dd>
<pre>
<code>cat </code><i>argus-file</i> | ra -r - -w icmp.log - icmp and host nimrod
</pre>
</dl>
<p> Read an <i>argus-file</i> at twice normal speed.</p>
<dl>
<dt>
<dd>
<pre>
<code>ra -r argus.file -M rtime:2
</code></pre>
</dl>
<h2>OUTPUT FORMAT</h2>
<p> The following is a brief description of the default output of .B ra. While this is by no means the &#8216;preferred&#8217; set of data that one should generate, it represents a starting point for using flow data in general. This also looks pretty good on 80 column terminals. The format is:</p>
<dl>
<dt>
<dd>
<pre>
<i>  time  flgs proto  shost  dir  daddr metrics state</i>
</pre>
</dl>
<dl>
<dt><code>time</code></p>
<dd> The format of the <i>time</i> field is specified by the .rarc file, using syntax supported by the routine <code><a href="//www.systutorials.com/docs/linux/man/3V-strftime/">strftime</a>(3V).</code> The default is &#8216;%T&#8217;. <code>Argus</code> transactional data contains both starting and ending transaction times, with precision to the microsecond. However, <code>ra</code> by default prints out the &#8216;stime&#8217; field, the records starting time.</p>
<dt><code>flgs</code></p>
<dd> The <i>flgs</i> indicator consists of a fixed length field. That reports various flow record and protocol identifiers, states and attributes. The format is: </p>
<pre>
 T        -  Time Corrected/Adjusted
 N        -  Netflow Originated Data
  *       -  Multiple sub-IP encapsulations
  e       -  Ethernet encapsulated flow
  E       -  ERSPAN encapsulation
  M       -  Multiple mac addresses seen
  m       -  MPLS encapsulated flow
  l       -  LLC encapsulated flow
  v       -  802.1Q encapsulations/tags
  w       -  802.11 wireless encapsulation
  p       -  PPP over Enternet encapsulated flow
  i       -  ISL encapsulated flow
  G       -  GRE encapsulation
  a       -  AH encapsulation
  P       -  IP tunnel encapsulation
  6       -  IPv6 tunnel encapsulation
  H       -  HDLC encapsulation
  C       -  Cisco HDLC encapsulation
  A       -  ATM encapsulation
  S       -  SLL encapsulation
  F       -  FDDI encapsulation
  s       -  SLIP encapsulation
  R       -  ARCNET encapsulation
   I      -  ICMP events mapped to this flow
   U      -  ICMP Unreachable event mapped to this flow
   R      -  ICMP Redirect event mapped to this flow
   T      -  ICMP Time Exceeded mapped to this flow
    *     -  Both Src and Dst loss/retransmission
    s     -  Src loss/retransmissions
    d     -  Dst loss/retransmissions
    g     -  Gaps in sequence numbers were observed
    &amp;     -  Both Src and Dst packet out of order
    i     -  Src packets out of order
    r     -  Dst packets out of order
     @    -  Both Src and Dst Window Closure
     S    -  Src TCP Window Closure
     D    -  Dst TCP Window Closure
     *    -  Silence suppression used by both src and dst (RTP)
     s    -  Silence suppression used by src
     d    -  Silence suppression used by dst
      E   -  Both Src and Dst ECN
      x   -  Src Explicit Congestion Notification
      t   -  Dst ECN
       V  -  Fragment overlap seen (if fragments seen)
       f  -  Partial Fragment (if fragments seen)
       F  -  Fragments seen
        O  -  multiple IP options set
        S  -  IP option Strict Source Route
        L  -  IP option Loose Source Route
        T  -  IP option Time Stamp
        +  -  IP option Security
        R  -  IP option Record Route
        A  -  IP option Router Alert
        U  -  unknown IP options set
</pre>
<dt><code>proto</code></p>
<dd> The proto field indicates the upper protocol used in the transaction. This field will contain the first 4 characters of the official name for the protocol used, as defined in RFC-1700, and configured using the /etc/protocols file. Argus attempts to discovery the Realtime Transport Protocol (rtp), when it is being used. When it encounters rtp, it will indicate its use in this field, with the string &#8216;rtp&#8217;. Use of the <code>-n</code> option, twice (-nn), will cause the actual protocol number to be displayed.</p>
<dt><code>shost</code></p>
<dd> The <i>shost</i> field is meant to convey the originator of the data in the flow. This field is protocol dependent, and for IP protocols will contain the src IP address/name. For TCP and UDP, the field will also contain the port number/name, separated by a period. </p>
<p> The &#8216;src&#8217; is generally the entity that first transmits a packet that is a part of a flow. However, the assignment of &#8216;src&#8217; and &#8216;dst&#8217; semantics is somewhat complicated by the notion of loss, or half-duplex monitoring, especially when connection-oriented protocol , such as TCP, are reported. In this case the &#8216;src&#8217; is the entity that initiated the flow.</p>
<dt><code>dir</code></p>
<dd> The <i>dir</i> field will have the direction of the transaction, as can be best determined from the datum, and is used to indicate which hosts are transmitting. For TCP, the dir field indicates the actual source of the TCP connection, and the center character indicating the state of the transaction.</p>
<dl>
<dt>
<dd>
<pre>
     -  - transaction was NORMAL
     |  - transaction was RESET
     o  - transaction TIMED OUT.
     ?  - direction of transaction is unknown.
</pre>
</dl>
<dt><code>daddr</code></p>
<dd> The <i>daddr</i> field is meant to convey the recipient of the data in the flow. Like the shost field, this field is protocol dependent, and for IP protocols will contain the dst IP address/name, and optionally the DSAP. </p>
<dt><code>metrics</code></p>
<dd> <i>metrics</i> represent the general sets of fields that reflect the activity of the flow. In the default output, there are 4 fields. The first 2 are the packet counts and the last 2 are the byte counts for the specific transaction. The fields are paired with the previous host fields, and represent the packets transmitted by the respective host.</p>
<dt><code>state</code></p>
<dd> The <i>state</i> field indicates the principle state for the transaction report, and is protocol dependent. For all the protocols, except ICMP, this field reports on the basic state of a transaction.</p>
<dt>
<dd> <code>REQ|INT (requested|initial)</code> This indicates that this is the <i>initial</i> state report for a transaction and is seen only when the <i>argus-server</i> is in DETAIL mode. For TCP connections this is <code>REQ</code>, indicating that a connection is being requested. For the connectionless protocols, such as UDP, this is <code>INT</code>.</p>
<dt>
<dd> <code>ACC (accepted)</code> This indicates that a request/response condition has occurred, and that a transaction has been detected between two hosts. For TCP, this indicates that a connection request has been answered, and the connection will be accepted. This is only seen when the <i>argus-server</i> is in DETAIL mode. For the connectionless protocols, this state indicates that there has been a single packet exchange between two hosts, and could qualify as a request/response transaction.</p>
<dt>
<dd> <code>EST|CON (established|connected)</code> This record type indicates that the reported transaction is active, and has been established or is continuing. This should be interpreted as a state report of a currently active transaction. For TCP, the EST state is only seen in DETAIL mode, and indicates that the three way handshake has been completed for a connection.</p>
<dt>
<dd> <code>CLO (closed) </code> TCP specific, this record type indicates that the TCP connection has closed normally.</p>
<dt>
<dd> <code>TIM (timeout)</code> Activity was not seen relating to this transaction, during the <code>argus</code> server&#8217;s timeout period for this protocol. This state is seen only when there were packets recorded since the last report for this transaction. </p>
</dl>
<p> For the ICMP and ICMPv6 protocols, the <i>state</i> field displays specific aspects of the ICMP type. ICMP state can have the values: </p>
<pre>
<code>ECO</code>     Echo Request
<code>ECR</code>     Echo Reply
<code>SRC</code>     Source Quench
<code>RED</code>     Redirect
<code>RTA</code>     Router Advertisement
<code>RTS</code>     Router Solicitation
<code>TXD</code>     Time Exceeded
<code>PAR</code>     Parameter Problem
<code>TST</code>     Time Stamp Request
<code>TSR</code>     Time Stamp Reply
<code>IRQ</code>     Information Request
<code>IRR</code>     Information Reply
<code>MAS</code>     Mask Request
<code>MSR</code>     Mask Reply
<code>URN</code>     Unreachable network
<code>URH</code>     Unreachable host
<code>URP</code>     Unreachable port
<code>URF</code>     Unreachable need fragmentation
<code>URS</code>     Unreachable source failed
<code>URNU</code>    Unreachable dst network unknown
<code>URHU</code>    Unreachable dst host unknown
<code>URISO</code>   Unreachable source host isolated
<code>URNPRO</code>  Unreachable network administrative prohibited
<code>URHPRO</code>  Unreachable host administrative prohibited
<code>URNTOS</code>  Unreachable network TOS prohibited
<code>URHTOS</code>  Unreachable host TOS prohibited
<code>URFIL</code>   Unreachable administrative filter
<code>URPRE</code>   Unreachable precedence violation
<code>URCUT</code>   Unreachable precedence cutoff
<code>MRQ</code>     Membership Query
<code>MHR</code>     Membership Report
<code>NRS</code>     Neighbor Discovery Router Solicit
<code>NRA</code>     Neighbor Discovery Router Advertisement
<code>NNS</code>     Neighbor Discovery Neighbor Solicit
<code>NNA</code>     Neighbor Discovery Neighbor Advertisement
<code>PTB</code>     Packet Too Big
</pre>
<h2>OUTPUT EXAMPLES</h2>
<p> These examples show typical <code>ra</code> output, and demonstrates a number of variations seen in <code>argus</code> data. This <code>ra</code> output was generated using the <code>-n</code> option to suppress number translation. </p>
<pre>
Thu 12/29 06:40:32   S tcp  132.3.31.15.6439   -&gt; 12.23.14.77.23   CLO
</pre>
<p> This is a normal tcp transaction to the telnet port on host 12.23.14.77. The IP Option strict source route was seen. </p>
<pre>
Thu 12/29 06:40:32     tcp  132.3.31.15.6200  &lt;|  12.23.14.77.25   RST
</pre>
<p> This tcp transaction from the smtp port of host 12.23.14.77 was <code>RESET</code>. In many cases this indicates that the transaction was rejected, however some os&#8217;s will use RST to close an active TCP. Use either the -z or -Zb options to specify exactly what conditions existed during the connection. </p>
<pre>
Thu 12/29 03:39:05  M  igmp 12.88.14.10       &lt;-&gt; 128.2.2.10       CON
</pre>
<p> This is an igmp transaction state report, usually seen with MBONE traffic. There was more than one source and destination MAC address pair used to support the transaction, suggesting a possible routing loop. </p>
<pre>
Thu 12/29 06:40:05 *   tcp  12.23.14.23.1043  &lt;-&gt; 12.23.14.27.6000 TIM
</pre>
<p> This is an X-windows transaction, that has <code>TIMEDOUT</code>. Packets were retransmitted during the connection. </p>
<pre>
Thu 12/29 07:42:09     udp   12.9.1.115.2262   -&gt; 28.12.141.6.139  INT
</pre>
<p> This is an initial netbios UDP transaction state report, indicating that this is the first datagram encountered for this transaction. </p>
<pre>
Thu 12/29 06:42:09     icmp  12.9.1.115       &lt;-&gt; 12.68.5.127      ECO
</pre>
<p> This example represents a &quot;ping&quot; of host 12.9.1.115, and its response. </p>
<p> This next example shows the <code>ra</code> output of a complete TCP transaction, with the preceeding Arp and DNS requests, while reading from a remote <i>argus-server</i>. The &#8216;*&#8217; in the CLO report indicates that at least one TCP packet was retransmitted during the transaction. The hostnames in this example are ficticious. </p>
<pre>
% ra -S argus-tcp://<i>argus-server</i> and host i.qosient.com
ra: Trying argus-server port 561
ra: connected Argus Version 3.0
Sat 12/03 15:29:38     arp  i.qosient.com     who-has  dsn.qosient.com  INT
Sat 12/03 15:29:39     udp  i.qosient.com.1542  &lt;-&gt;    dns.qosient.53   INT
Sat 12/03 15:29:39     arp  i.qosient.com     who-has  qosient.com      INT
Sat 12/03 15:29:39 *   tcp  i.qosient.com.1543   -&gt;    qosient.com.smtp CLO
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>FILES</h2>
<p> <code>/etc/ra.conf</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-rarc/">rarc</a></code>(5) <code><a href="/docs/linux/man/8-argus/">argus</a></code>(8) </p>
<p> Postel, Jon, <i>Internet Protocol,</i> <font SIZE="-1">RFC</font> 791, Network Information Center, <font SIZE="-1">SRI</font> International, Menlo Park, Calif., May 1981. </p>
<p> Postel, Jon, <i>Internet Control Message Protocol</i>, <font SIZE="-1">RFC</font> 792, Network Information Center, SRI International, Menlo Park, Calif., May 1981. </p>
<p> Postel, Jon, <i>Transmission Control Protocol</i>, <font SIZE="-1">RFC</font> 793, Network Information Center, SRI International, Menlo Park, Calif., May 1981. </p>
<p> Postel, Jon, <i>User Datagram Protocol</i>, <font SIZE="-1">RFC</font> 768, Network Information Center, SRI International, Menlo Park, Calif., May 1980. </p>
<p> McCanne, Steven, and Van Jacobson, <i>The BSD Packet Filter: A New Architecture for User-level Capture</i>, Lawrwnce Berkeley Laboratory, One Cyclotron Road, Berkeley, Calif., 94720, December 1992. </p>
<h2>Index</h2>
