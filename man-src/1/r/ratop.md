---
title: "ratop(1)"
name: "ratop"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ratop/"
description: "ratop – display and update sorted network flow data"
---

<h2>NAME</h2>
<p> <code>ratop</code> &#8211; display and update sorted network flow data</p>
<h2>SYNOPSIS</h2>
<p> <code>ratop [raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ratop</code> reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from an <i>argus-file</i>, or from a remote data source, and periodically displays a sorted list of network flow records. When read from a file, <code>ratop</code> displays the resulting flow caches when the file is completed, updating its status display line with each input. When reading from a live argus data stream, <code>ratop</code> will display data, asynchronously in realtime, as it is received from the source. </p>
<p> Flow data is aggregated as its read, (see <code>racluster.1</code>), resulting in a single line for each network transaction encountered in the data stream. The default sorting key is total packets per flow, but other keys can be used instead. Flow records that have been idle for more than the default 60s are removed. Various output options, such as the specific columns of data to display, the entry idle timeout value, the screen refresh rate, etc &#8230; are all configurable. </p>
<p> <code>ratop</code> uses <code>ncurses</code> and <code>readline.3</code>, when available, to provide a <code>vi.1</code> look and feel for displaying, navigating and modifying network flow data. </p>
<p> While running <code>ratop</code> a lot of help can be obtained from the on-line help system, using the &quot;:h&quot; command.<br />
&nbsp;<wbr></p>
<h2>OPTIONS</h2>
<p> Command line option specifications are processed from left to right. Options can be specified more than once. If conflicting options are specified, later specifications override earlier ones. This makes it viable to create a shell alias for <code>ratop</code> with preferred defaults specified, then override those preferred defaults as desired on the command line. </p>
<p> <code>ratop</code>, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression, and the ability to specify the output style, format and contents for printing data. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. <code><a href="/docs/linux/man/1-ratop/">ratop</a>(1)</code> specific options are: </p>
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
<dd> intermediate node origin AS number, if available. </p>
<dt></dl>
</dl>
<dd>
<dl>
<dt><code>-M</code><i> modes</i></p>
<dd> Supported modes are:</dl>
<dl>
<dt>
<dd>
<dl>
<dt><code>correct</code></p>
<dd> Attempt to correct the direction of flows by also searching the reverse flow key, if a match isn&#8217;t found in the cache. This mode is on by default when using the default full 5-tuple flow key definitions.</p>
<dt><code>nocorrect</code></p>
<dd> Turn off flow correction for direction. This mode is used by default if the flow key has been changed.</p>
<dt><code>preserve</code></p>
<dd> Preserve fields when aggregating matching flow data.</p>
<dt><code>nopreserve</code></p>
<dd> Do not preserve fields when aggregating matching flow data.</p>
<dt><code>norep</code></p>
<dd> Do not generate an aggregate statistic for each flow. This is used primarily when the output represents a single object. Primarily used when merging status records to generate single flows that represent single transactions.</p>
<dt><code>rmon</code></p>
<dd> Generate data suitable for producing RMON types of metrics.</p>
<dt><code>nocurses</code></p>
<dd> Do not use the curses interface to present data. This option is primarily used when debugging ratop, to get around the issues of screen maniuplation within a debugger like gdb or lldb.</dl>
</dl>
<h2>DISPLAY</h2>
<p> The first several lines of the <code>ratop</code> display show global state. The top line shows how ratop is running, with the list of command line options that are in effect. In the upper most right corner is the current time. The next line is the column title line, that labels each column. The bottom line is the command line, where you will see and prepare &#8216;:&#8217; commands. The line above the bottom line is the status line, showing the number of flows that are in the <code>ratop</code> process queue, display queue, the total number of flows read, the rate of flow records read, and the current status, whether it is Active, reading records, or Idle, when all input is complete. This line can be toggled on or off using ^G. </p>
<p> Flows caches are displayed one per row and are sorted by total pkts, by default. <code>ratop</code> sorting can be configured using the <i>rarc</i> variable RA_SORT_ALGORITHMS, or by using the &quot;:P&quot; command. </p>
<p> <code>ratop</code> supports 3 basic filters. Like all other ra* programs, <code>ratop</code> will send its command line filter to its remote argus data sources, to limit the load on the wire. This is the &quot;remote&quot; filter. Also, <code>ratop</code> supports a &quot;local&quot; filter, that is applied to flow record input. Normally this is used when the remote argus data source doesn&#8217;t support the syntax of the specific filter. <code>ratop</code> also support a &quot;display&quot; filter, that is used to select which flow records are to be displayed. This filter does not have any impact on the internal flow caches that <code>ratop</code> is tracking, so you can change the &quot;display&quot; filter at any time and see the current state of other flows. </p>
<h2>COLOR</h2>
<p> <code>ratop</code> supports color which is configured using the rarc file. The RA_COLOR_CONFIG file is a fall through specification of flow filters and field color definitions. For flows that match a filter, specific fields in the row will be painted the configured color. Because the filter specification supports the &quot; cont &quot; directive, a single row can be painted by any number of color definitions. </p>
<p> When color is enabled <code>ratop</code> will attempt to color IP addresses to indicate that local host address, and the local network. This is very helpful in mobile host installations, where you may not know what IP address has been assigned the localhost. <code>ratop</code> also supports coloring local addresses based on the RA_LOCAL rarc variable. </p>
<p> See racolor.conf.5. </p>
<h2>ARGUS EVENTS</h2>
<p> Introduced in argus-3.0.8, <code>ratop</code> supports correlating specific ARGUS_EVENT data with flow data, which can be turned on through the use of the RA_CORRELATE_EVENTS rarc variable. <code>ratop</code> will process argus-lsof event data generated by host bourne argi, and label flow data with user, pid and process name metadata. While experimental, it is production level functionality, and can be used with other ra* programs to enhance flow data with host os process information. See argus-3.0.8 documentation on ARGUS_EVENTS. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>ratop -r argus.file -s rank stime dur:14 saddr daddr proto pkts bytes</p>
<dd>
<p> Read the file argus.file, and display the resulting aggregated and sorted list of flow records, using the default sorting methods. </p>
<dt>ratop -S localhost</p>
<dd> Run ratop as a live display of realtime flow traffic. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-rarc/">rarc</a>(5) <a href="/docs/linux/man/1-racluster/">racluster</a>(1) <a href="/docs/linux/man/5-racluster-conf/">racluster.conf</a>(5) </p>
<h2>Index</h2>
