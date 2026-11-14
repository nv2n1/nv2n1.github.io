---
title: "rabins(1)"
name: "rabins"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rabins/"
description: "rabins – process argus(8) data within specified bins."
---

<h2>NAME</h2>
<p> <code>rabins</code> &#8211; process <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data within specified bins.</p>
<h2>SYNOPSIS</h2>
<p> <code>rabins</code> <code>[-B </code><i>secs</i><code>] -M</code> <i>splitmode</i> [<i>options</i>]] [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rabins</code> reads <code>argus</code> data from an <i>argus-data</i> source, and adjusts the data so that it is aligned to a set of bins, or slots, that are based on either time, input size, or count. The resulting output is split, modified, and optionally aggregated so that the data fits to the constraints of the specified bins. <code>rabins</code> is designed to be a combination of <code>rasplit</code> and <code>racluster</code>, acting on multiple contexts of argus data. </p>
<p> The principal function of <code>rabins</code> is to align input data to a series of bins, and then process the data within the context of each bin. This is the basis for real-time stream block processing. Time series stream block processing is cricital for flow data graphing, comparing, analyzing, and correlation. Fixed load stream block processing, based on the number of argus data records (&#8216;count&#8217;), or a fixed volume of data (&#8216;size&#8217;) allows for control of resources in processing. While load based options are very useful, they are rather esoteric. See the online examples and rasplit.1 for examples of using these modes of operation. </p>
<h2>Time Series Bins</h2>
<p> Time series bin&#8217;ing is specified using the <code>-M</code> <i>time</i> option. Time bins are specified by the size and granularity of the time bin. The granularity, &#8216;s&#8217;econds, &#8216;m&#8217;inutes, &#8216;h&#8217;ours, &#8216;d&#8217;ays, &#8216;w&#8217;eeks, &#8216;M&#8217;onths, and &#8216;y&#8217;ears, dictates where the bin boundaries lie. To ensure that 0.5d and 12h start on the same point in time, second, minute, hour, and day based bins start at midnight, Jan 1st of the year of processing. Week, month and year bins all start on natural time boundaries, for the period. </p>
<p> <code>rabins</code> provides a separate processing context for each bin, so that aggregation and sorting occur only within the context of each time period. Records are placed into bins based on load or time. For load based bins, input records are processed in received order and are not modified. When using time based bins, records are placed into bins based on the starting time of the record. By default, records that span a time boundary are split into as many records as needed to fit the record into appropriate bin sizes, using the algorithms used by <code>rasplit.1</code>. Metrics are distributed uniformly within all the appropriate bins. The result is a series of data and/or fragments that are time aligned, appropriate for time seried analysis, and visualization. </p>
<p> When a record is split to conform to a time series bin, the resulting starting and ending timestamps may or may not coincide with the timestamps of the bins themselves. For some applications, this treatment is critical to the analytics that are working on the resulting data, such as transaction duration, and flow traffic burst behavior. However, for other analytics, like average load, and rate analysis and reporting, the timestamps need to be modified so that they reflect the time range of the actual time bin boundaries. Rabins supports the optional <code>hard</code> option to specify that timestamps should conform to bin boundaries. One of the results of this is that all durations in the reported records will be the bin duration. This is extremely important when processing certain time series metrics, like load. </p>
<h2>Load Based Bins</h2>
<p> Load based bin&#8217;ing is specified using the <code>-M size</code> or <code>-M count</code> options. Load bins are used to constrain the resource used in bin processing. So much load is input, aggregation is performed on the input load, and when a threshold is reached, the entire aggregation cache is dumped, reinitiallized, and reused. These can be used effectively to provide realtime data reduction, but within a fixed amount of memory. </p>
<h2>Output Processing</h2>
<p> <code>rabins</code> has two basic modes of output, the default holds all output in main memory until EOF is encountered on input, where each sorted bin is written out. The second output mode, has <code>rabins</code> writing out the contents of individual sorted bins, periodically based on a holding time, specified using the <i>-B secs</i> option. The <i>secs</i> value should be chosen such that <code>rabins</code> will have seen all the appropriate incoming data for that time period. This is determined by the ARGUS_FLOW_STATUS_INTERVAL used by the collection of argus data sources in the input data stream, as well as any time drift that may exist amoung argus data processin elements. When there is good time sync, and with an ARGUS_FLOW_STATUS_INTERVAL of 5 seconds, appropriate <i>secs</i> values are between 5-15 seconds. </p>
<p> The output of <code>rabins</code> when using the <i>-B secs</i> option, is appropriate to drive a number of processing elements, such as near real-time visualizations and alarm and reporting. </p>
<h2>Output Stream</h2>
<p> Like all <code>ra.1</code> client programs, the output of <code>rabins.1</code> is an argus data stream, that can be written as binary data to a file or standard output, or can be printed. <code>rabins</code> supports all the output functions provided by <code>rasplit.1</code>. </p>
<p> The output files name consists of a prefix, which is specified using the <i>-w</i> <i>ra option</i>, and for all modes except <code>time</code> mode, a suffix, which is created for each resulting file. If no prefix is provided, then <code>rabins</code> will use &#8216;x&#8217; as the default prefix. The suffix that is used is determined by the mode of operation. When <code>rabins</code> is using the default count mode or the size mode, the suffix is a group of letters &#8216;aa&#8217;, &#8216;ab&#8217;, and so on, such that concatenating the output files in sorted order by file name produces the original input file. If <code>rabins</code> will need to create more output files than are allowed by the default suffix strategy, more letters will be added, in order to accomodate the needed files. </p>
<p> When <code>rabins</code> is spliting based on time, <code>rabins</code> uses a default extension of %Y.%m.%d.%h.%m.%s. This default can be overrided by adding a &#8216;%&#8217; extension to the name provided using the <i>-w</i> option. </p>
<p> When standard out is specified, using <i>-w &#8211;</i>, <code>rabins</code> will output a single <code>argus-stream</code> with START and STOP argus management records inserted appropriately to indicate where the output is split. See <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> for more information on output stream formats. </p>
<p> When <code>rabins</code> is spliting on output record count (the default), the number of records is specified as an ordinal counter, the default is 1000 records. When <code>rabins</code> is spliting based on the maximum output file size, the size is specified as bytes. The scale of the bytes can be specified by appending &#8216;b&#8217;, &#8216;k&#8217; and &#8216;m&#8217; to the number provided. </p>
<p> When <code>rabins</code> is spliting base on time, the time period is specified with the option, and can be any period based in seconds (s), minutes (m), hours (h), days (d), weeks (w), months (M) or years (y). <code>Rabins</code> will create and modify records as required to split on prescribed time boundaries. If any record spans a time boundary, the record is split and the metrics are adjusted using a uniform distribution model to distribute the statistics between the two records. </p>
<p> See <code>rasplit.1</code> for specifics. </p>
<h2>RABINS SPECIFIC OPTIONS</h2>
<p> <code>rabins</code>, like all ra based clients, supports a number of <code>ra options</code> including remote data access, reading from multiple files and filtering of input argus records through a terminating filter expression. Rabins also provides all the functions of <code>racluster.1</code> and <code>rasplit.1</code>, for processing and outputing data. <code>rabins</code> specific options are: </p>
<dl>
<dt><code>-B</code><i> secs</i></p>
<dd> Holding time in seconds before closing a bin and outputing its contents.</dl>
<dl>
<dt><code>-M</code><i> splitmode</i></p>
<dd> Supported spliting modes are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>time &lt;n[smhdwMy]&gt;</code></p>
<dd> bin records into time slots of n size. This is used for time series analytics, especially graphing. Records, by default are split, so that their timestamps do not span the time range specified. Metrics are uniformly distributed among the resulting records.</p>
<dt><code>count &lt;n[kmb]&gt;</code></p>
<dd> bin records into chunks based on the number of records. This is used for archive management and parallel processing analytics, to limit the size of data processing to fixed numbers of records.</p>
<dt><code>size &lt;n[kmb]&gt;</code></p>
<dd> bin records into chunks based on the number of total bytes. This is used for archive management and parallel processing analytics, to limit the size of data processing to fixed byte limitations.</dl>
</dl>
<dl>
<dt><code>-M</code><i> modes</i></p>
<dd> Supported processing modes are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>hard</code></p>
<dd> split on hard time boundaries. Each flow records start and stop times will be the time boundary times. The default is to use the original start and stop timestamps from the records that make up the resulting aggregation.</p>
<dt><code>nomodify</code></p>
<dd> Do not split the record when including it into a time bin. This allows a time bin to represent times outside of its defintion. This option should not be used with the &#8216;hard&#8217; option, as you will modify metrics and semantics.</dl>
</dl>
<dl>
<dt><code>-m</code><i> aggregation object</i></p>
<dd> Supported aggregation objects are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> use a null flow key.</p>
<dt><code>srcid</code></p>
<dd> argus source identifier.</p>
<dt><code>smac</code></p>
<dd> source mac(ether) addr.</p>
<dt><code>dmac</code></p>
<dd> destination mac(ether) addr.</p>
<dt><code>soui</code></p>
<dd> oui portion of the source mac(ether) addr.</p>
<dt><code>doui</code></p>
<dd> oui portion of the destination mac(ether) addr.</p>
<dt><code>smpls</code></p>
<dd> source mpls label.</p>
<dt><code>dmpls</code></p>
<dd> destination label addr.</p>
<dt><code>svlan</code></p>
<dd> source vlan label.</p>
<dt><code>dvlan</code></p>
<dd> destination vlan addr.</p>
<dt><code>saddr/[l|m]</code></p>
<dd> source IP addr/[cidr len | m.a.s.k].</p>
<dt><code>daddr/[l|m]</code></p>
<dd> destination IP addr/[cidr len | m.a.s.k].</p>
<dt><code>matrix/l</code></p>
<dd> sorted src and dst IP addr/cidr len.</p>
<dt><code>proto</code></p>
<dd> transaction protocol.</p>
<dt><code>sport</code></p>
<dd> source port number. Implies use of &#8216;proto&#8217;.</p>
<dt><code>dport</code></p>
<dd> destination port number. Implies use of &#8216;proto&#8217;.</p>
<dt><code>stos</code></p>
<dd> source TOS byte value.</p>
<dt><code>dtos</code></p>
<dd> destination TOS byte value.</p>
<dt><code>sttl</code></p>
<dd> src -&gt; dst TTL value.</p>
<dt><code>dttl</code></p>
<dd> dst -&gt; src TTL value.</p>
<dt><code>stcpb</code></p>
<dd> src -&gt; dst TCP base sequence number.</p>
<dt><code>dtcpb</code></p>
<dd> dst -&gt; src TCP base sequence number.</p>
<dt><code>inode[/l|m]]</code></p>
<dd> intermediate node IP addr/[cidr len | m.a.s.k], source of ICMP mapped events.</p>
<dt><code>sco</code></p>
<dd> source ARIN country code, if present.</p>
<dt><code>dco</code></p>
<dd> destination ARIN country code, if present.</p>
<dt><code>sas</code></p>
<dd> source node origin AS number, if available.</p>
<dt><code>das</code></p>
<dd> destination node origin AS number, if available.</p>
<dt><code>ias</code></p>
<dd> intermediate node origin AS number, if available.</dl>
</dl>
<dl>
<dt><code>-P</code><i> sort field</i></p>
<dd> <code>Rabins</code> can sort its output based on a sort field specification. Because the <code>-m</code> option is used for aggregation fields, <code>-P</code> is used to specify the print priority order. See <code><a href="/docs/linux/man/1-rasort/">rasort</a>(1)</code> for the list of sortable fields. </p>
<dt><code>-w</code><i> filename</i></p>
<dd> <code>Rabins</code> supports an extended <i>-w</i> option that allows for output record contents to be inserted into the output filename. Specified using &#8216;$&#8217; (dollar) notation, any printable field can be used. Care should be taken to honor any shell escape requirements when specifying on the command line. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for the list of printable fields. </p>
<p> Another extended feature, when using <code>time</code> mode, <code>rabins</code> will process the supplied filename using <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</code>, so that time fields can be inserted into the resulting output filename. </p>
</dl>
<h2>INVOCATION</h2>
<p> This invocation aggregates <code>inputfile</code> based on 10 minute time boundaries. Input is split to fit within a 10 minute time boundary, and within those boundaries, argus records are aggregated. The resulting output its streamed to a single file. </p>
<pre>
   
   <code>rabins</code> -r * -M time 10m -w outputfile
  
</pre>
<p> This next invocation aggregates <code>inputfiles</code> based on 5 minute time boundaries, and the output is written to 5 minute files. Input is split such that all records conform to hard 10 minute time boundaries, and within those boundaries, argus records are aggregated, in this case, based on IP address matrix. </p>
<p> The resulting output its streamed to files that are named relative to the records output content, a prefix of <i>/matrix/%Y/%m/%d/argus.</i> and the suffixes <i>%H.%M.%S</i>. </p>
<pre>
   
   <code>rabins</code> -r * -M hard time 5m -m matrix -w &quot;/matrix/%Y/%m/%d/argus.%H.%M.%S&quot;
  
</pre>
<p> This next invocation aggregates <code>input.stream</code> based on matrix/24 into 10 second time boundaries, holds the data for an additional 5 seconds after the time boundary has passed, and then prints the complete sorted contents of each bin to standard output. The output is printed at 10 second intervals, and the output is the content of the previous 10 sec time bin. This example is meant to provide, every 10 seconds, the summary of all Class C subnet activity seen. It is intended to run indefinately printing out aggregated summary records. By modifying the aggregation model, using the &quot;-f racluster.conf&quot; option, you can achieve a great deal of data reduction with a lot of semantic reporting. </p>
<pre><code>

% rabins - S localhost - m matrix / 24 - B 5s - M hard time 10s - p0 - s + 1trans - ipv4 StartTime Trans Proto SrcAddr Dir DstAddr SrcPkts DstPkts SrcBytes DstBytes State 2012 / 02 / 15.13 : 37 : 00 5 ip 192.168.0.0 / 24 &lt;-&gt;192.168.0.0 / 24 41 40 2860 12122 CON 2012 / 02 / 15.13 : 37 : 00 2 ip 192.168.0.0 / 24-&gt;224.0.0.0 / 24 2 0 319 0 INT[10 seconds pass] 2012 / 02 / 15.13 : 37 : 10 13 ip 192.168.0.0 / 24 &lt;-&gt;208.59.201.0 / 24 269 351 97886 398700 CON 2012 / 02 / 15.13 : 37 : 10 14 ip 192.168.0.0 / 24 &lt;-&gt;192.168.0.0 / 24 86 92 7814 46800 CON 2012 / 02 / 15.13 : 37 : 10 1 ip 17.172.224.0 / 24 &lt;-&gt;192.168.0.0 / 24 52 37 68125 4372 CON 2012 / 02 / 15.13 : 37 : 10 1 ip 192.168.0.0 / 24 &lt;-&gt;199.7.55.0 / 24 7 7 784 2566 CON 2012 / 02 / 15.13 : 37 : 10 1 ip 184.85.13.0 / 24 &lt;-&gt;192.168.0.0 / 24 6 5 3952 2204 CON 2012 / 02 / 15.13 : 37 : 10 2 ip 66.235.132.0 / 24 &lt;-&gt;192.168.0.0 / 24 5 6 915 3732 CON 2012 / 02 / 15.13 : 37 : 10 1 ip 74.125.226.0 / 24 &lt;-&gt;192.168.0.0 / 24 3 4 709 888 CON 2012 / 02 / 15.13 : 37 : 10 3 ip 66.39.3.0 / 24 &lt;-&gt;192.168.0.0 / 24 3 3 369 198 CON 2012 / 02 / 15.13 : 37 : 10 1 ip 192.168.0.0 / 24 &lt;-&gt;205.188.1.0 / 24 1 1 54 356 CON[10 seconds pass] 2012 / 02 / 15.13 : 37 : 20 6 ip 192.168.0.0 / 24 &lt;-&gt;208.59.201.0 / 24 392 461 60531 623894 CON 2012 / 02 / 15.13 : 37 : 20 8 ip 192.168.0.0 / 24 &lt;-&gt;192.168.0.0 / 24 95 111 6948 93536 CON 2012 / 02 / 15.13 : 37 : 20 3 ip 72.14.204.0 / 24 &lt;-&gt;192.168.0.0 / 24 38 32 38568 4414 CON 2012 / 02 / 15.13 : 37 : 20 1 ip 17.112.156.0 / 24 &lt;-&gt;192.168.0.0 / 24 26 13 21798 7116 CON 2012 / 02 / 15.13 : 37 : 20 2 ip 66.235.132.0 / 24 &lt;-&gt;192.168.0.0 / 24 6 3 1232 4450 CON 2012 / 02 / 15.13 : 37 : 20 1 ip 66.235.133.0 / 24 &lt;-&gt;192.168.0.0 / 24 1 2 82 132 CON[10 seconds pass] 2012 / 02 / 15.13 : 37 : 30 117 ip 192.168.0.0 / 24 &lt;-&gt;208.59.201.0 / 24 697 663 369769 134382 CON 2012 / 02 / 15.13 : 37 : 30 11 ip 192.168.0.0 / 24 &lt;-&gt;192.168.0.0 / 24 147 187 11210 193253 CON 2012 / 02 / 15.13 : 37 : 30 1 ip 184.85.13.0 / 24 &lt;-&gt;192.168.0.0 / 24 13 9 13408 9031 CON 2012 / 02 / 15.13 : 37 : 30 2 ip 66.235.132.0 / 24 &lt;-&gt;192.168.0.0 / 24 8 7 1920 11563 CON 2012 / 02 / 15.13 : 37 : 30 1 ip 192.168.0.0 / 24 &lt;-&gt;207.46.193.0 / 24 5 3 802 562 CON 2012 / 02 / 15.13 : 37 : 30 1 ip 17.112.156.0 / 24 &lt;-&gt;192.168.0.0 / 24 5 2 646 3684 CON 2012 / 02 / 15.13 : 37 : 30 2 ip 192.168.0.0 / 24-&gt;224.0.0.0 / 24 2 0 382 0 REQ[10 seconds pass]
</code></pre>
<p> This next invocation reads IP <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and processes, the <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data stream based on input byte size of no greater than 1 Megabyte. The resulting output stream is written to a single <i>argus.out</i> data file. </p>
<pre>
 
   <code>rabins</code> -r argusfile -M size 1m -s +1dur -m proto -w argus.out - ip
 
</pre>
<p> This invocation reads IP <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>inputfile</code> and aggregates the <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data stream based on input file size of no greater than 1K flows. The resulting output stream is printed to the screen as standard argus records. </p>
<pre>
   <code>rabins</code> -r argusfile -M count 1k -m proto -s stime dur proto spkts dpkts - ip
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/1-racluster/">racluster</a>(1),</code> <code><a href="/docs/linux/man/1-rasplit/">rasplit</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code> </p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>Index</h2>
