---

title: "ratop(1)"
name: "ratop"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ratop/"
description: "ratop – display and update sorted network flow data"
---

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
<dt><code>-m</code><i> aggregation object</i></dt>
<dd> Supported aggregation objects are:</dd></dl>
<dl>
<dl>
<dt><code>none</code></dt>
<dd> use a null flow key.</dd>
<dt><code>srcid</code></dt>
<dd> argus source identifier.</dd>
<dt><code>smac</code></dt>
<dd> source mac(ether) addr.</dd>
<dt><code>dmac</code></dt>
<dd> destination mac(ether) addr.</dd>
<dt><code>soui</code></dt>
<dd> oui portion of the source mac(ether) addr.</dd>
<dt><code>doui</code></dt>
<dd> oui portion of the destination mac(ether) addr.</dd>
<dt><code>smpls</code></dt>
<dd> source mpls label.</dd>
<dt><code>dmpls</code></dt>
<dd> destination label addr.</dd>
<dt><code>svlan</code></dt>
<dd> source vlan label.</dd>
<dt><code>dvlan</code></dt>
<dd> destination vlan addr.</dd>
<dt><code>saddr/[l|m]</code></dt>
<dd> source IP addr/[cidr len | m.a.s.k].</dd>
<dt><code>daddr/[l|m]</code></dt>
<dd> destination IP addr/[cidr len | m.a.s.k].</dd>
<dt><code>matrix/l</code></dt>
<dd> sorted src and dst IP addr/cidr len.</dd>
<dt><code>proto</code></dt>
<dd> transaction protocol.</dd>
<dt><code>sport</code></dt>
<dd> source port number. Implies use of &#8216;proto&#8217;.</dd>
<dt><code>dport</code></dt>
<dd> destination port number. Implies use of &#8216;proto&#8217;.</dd>
<dt><code>stos</code></dt>
<dd> source TOS byte value.</dd>
<dt><code>dtos</code></dt>
<dd> destination TOS byte value.</dd>
<dt><code>sttl</code></dt>
<dd> src -&gt; dst TTL value.</dd>
<dt><code>dttl</code></dt>
<dd> dst -&gt; src TTL value.</dd>
<dt><code>stcpb</code></dt>
<dd> src -&gt; dst TCP base sequence number.</dd>
<dt><code>dtcpb</code></dt>
<dd> dst -&gt; src TCP base sequence number.</dd>
<dt><code>inode[/l|m]]</code></dt>
<dd> intermediate node IP addr/[cidr len | m.a.s.k], source of ICMP mapped events.</dd>
<dt><code>sco</code></dt>
<dd> source ARIN country code, if present.</dd>
<dt><code>dco</code></dt>
<dd> destination ARIN country code, if present.</dd>
<dt><code>sas</code></dt>
<dd> source node origin AS number, if available.</dd>
<dt><code>das</code></dt>
<dd> destination node origin AS number, if available.</dd>
<dt><code>ias</code></dt>
<dd> intermediate node origin AS number, if available. </dd>
<dt></dt></dl>
</dl>
<dd>
</dd><dl>
<dt><code>-M</code><i> modes</i></dt>
<dd> Supported modes are:</dd></dl>
<dl>
<dl>
<dt><code>correct</code></dt>
<dd> Attempt to correct the direction of flows by also searching the reverse flow key, if a match isn&#8217;t found in the cache. This mode is on by default when using the default full 5-tuple flow key definitions.</dd>
<dt><code>nocorrect</code></dt>
<dd> Turn off flow correction for direction. This mode is used by default if the flow key has been changed.</dd>
<dt><code>preserve</code></dt>
<dd> Preserve fields when aggregating matching flow data.</dd>
<dt><code>nopreserve</code></dt>
<dd> Do not preserve fields when aggregating matching flow data.</dd>
<dt><code>norep</code></dt>
<dd> Do not generate an aggregate statistic for each flow. This is used primarily when the output represents a single object. Primarily used when merging status records to generate single flows that represent single transactions.</dd>
<dt><code>rmon</code></dt>
<dd> Generate data suitable for producing RMON types of metrics.</dd>
<dt><code>nocurses</code></dt>
<dd> Do not use the curses interface to present data. This option is primarily used when debugging ratop, to get around the issues of screen maniuplation within a debugger like gdb or lldb.</dd></dl>
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
<dt>ratop -r argus.file -s rank stime dur:14 saddr daddr proto pkts bytes</dt>
<dd>
<p> Read the file argus.file, and display the resulting aggregated and sorted list of flow records, using the default sorting methods. </p>
</dd><dt>ratop -S localhost</dt>
<dd> Run ratop as a live display of realtime flow traffic. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-rarc/">rarc</a>(5) <a href="/docs/linux/man/1-racluster/">racluster</a>(1) racluster.conf(5) </p>
