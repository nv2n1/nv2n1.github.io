---
title: "iftop(8)"
name: "iftop"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iftop/"
description: "iftop – display bandwidth usage on an interface by host"
---

<p>iftop &#8211; display bandwidth usage on an interface by host</p>
<h2>Synopsis</h2>
<p><code>iftop</code> <code>-h</code> | [<code>-nNpblBP</code>] [<code>-i</code> <i>interface</i>] [<code>-f</code> <i>filter code</i>] [<code>-F</code> <i>net</i>/<i>mask</i>] [<code>-G</code> <i>net6</i>/<i>mask6</i>]</p>
<h2>Description</h2>
<p><code>iftop</code> listens to network traffic on a named <i>interface</i>, or on the first interface it can find which looks like an external interface if none is specified, and displays a table of current bandwidth usage by pairs of hosts. <code>iftop</code> must be run with sufficient permissions to monitor all network traffic on the <i>interface</i>; see <code><a href="/docs/linux/man/3-pcap/">pcap</a></code>(3) for more information, but on most systems this means that it must be run as root. By default, <code>iftop</code> will look up the hostnames associated with addresses it finds in packets. This can cause substantial traffic of itself, and may result in a confusing display. You may wish to suppress display of DNS traffic by using filter code such as <code>not port domain</code>, or switch it off entirely, by using the <code>-n</code> option or by pressing <code>r</code> when the program is running. By default, <code>iftop</code> counts all IP packets that pass through the filter, and the direction of the packet is determined according to the direction the packet is moving across the interface. Using the <code>-F</code> option it is possible to get <code>iftop</code> to show packets entering and leaving a given network. For example, <code>iftop -F 10.0.0.0/255.0.0.0</code> will analyse packets flowing in and out of the 10.* network. Some other filter ideas:</p>
<dl>
<dt><code>not ether host ff:ff:ff:ff:ff:ff</code></p>
<dd>Ignore ethernet broadcast packets.</p>
<dt><code>port http and not host </code><i>webcache.example.com</i></p>
<dd>Count web traffic only, unless it is being directed through a local web cache.</p>
<dt><code>icmp</code></p>
<dd>How much bandwidth are users wasting trying to figure out why the network is slow? </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Print a summary of usage.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t do hostname lookups.</p>
<dt><code>-N</code></p>
<dd>Do not resolve port number to service names</p>
<dt><code>-p</code></p>
<dd>Run in promiscuous mode, so that traffic which does not pass directly through the specified interface is also counted.</p>
<dt><code>-P</code></p>
<dd>Turn on port display.</p>
<dt><code>-l</code></p>
<dd>Display and count datagrams addressed to or from link-local IPv6 addresses. The default is not to display that address category.</p>
<dt><code>-b</code></p>
<dd>Don&#8217;t display bar graphs of traffic.</p>
<dt><code>-m</code> <i>limit</i></p>
<dd>Set the upper limit for the bandwidth scale. Specified as a number with a &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; suffix.</p>
<dt><code>-B</code></p>
<dd>Display bandwidth rates in bytes/sec rather than bits/sec.</p>
<dt><code>-i</code> <i>interface</i></p>
<dd>Listen to packets on <i>interface</i>.</p>
<dt><code>-f</code> <i>filter code</i></p>
<dd>Use <i>filter code</i> to select the packets to count. Only IP packets are ever counted, so the specified code is evaluated as <code>(</code><i>filter code</i><code>) and ip</code>.</p>
<dt><code>-F</code> <i>net</i>/<i>mask</i></p>
<dd>Specifies an IPv4 network for traffic analysis. If specified, iftop will only include packets flowing in to or out of the given network, and packet direction is determined relative to the network boundary, rather than to the interface. You may specify <i>mask</i> as a dotted quad, such as /255.255.255.0, or as a single number specifying the number of bits set in the netmask, such as /24.</p>
<dt><code>-G</code> <i>net6</i>/<i>mask6</i></p>
<dd>Specifies an IPv6 network for traffic analysis. The value of <i>mask6</i> can be given as a prefix length or as a numerical address string for more compound bitmasking.</p>
<dt><code>-c</code> <i>config file</i></p>
<dd>Specifies an alternate config file. If not specified, iftop will use <code>~/.iftoprc</code> if it exists. See below for a description of config files</p>
<dt><code>-t</code> <i>text output mode</i></p>
<dd>Use text interface without ncurses and print the output to STDOUT. </p>
</dl>
<h2>Display</h2>
<p>When running, <code>iftop</code> uses the whole screen to display network usage. At the top of the display is a logarithmic scale for the bar graph which gives a visual indication of traffic. </p>
<p> The main part of the display lists, for each pair of hosts, the rate at which data has been sent and received over the preceding 2, 10 and 40 second intervals. The direction of data flow is indicated by arrows, &lt;= and =&gt;. For instance, </p>
<pre>foo.example.com =&gt; bar.example.com 1Kb 500b 100b
 &lt;= 2Mb 2Mb 2Mb</pre>
<p>shows, on the first line, traffic from <code>foo.example.com</code> to <code>bar.example.com</code>; in the preceding 2 seconds, this averaged 1Kbit/s, around half that amount over the preceding 10s, and a fifth of that over the whole of the last 40s. During each of those intervals, the data sent in the other direction was about 2Mbit/s. On the actual display, part of each line is inverted to give a visual indication of the 10s average of traffic. You might expect to see something like this where host <code>foo</code> is making repeated HTTP requests to <code>bar</code>, which is sending data back which saturates a 2Mbit/s link. </p>
<p> By default, the pairs of hosts responsible for the most traffic (10 second average) are displayed at the top of the list. </p>
<p> At the bottom of the display, various totals are shown, including peak traffic over the last 40s, total traffic transferred (after filtering), and total transfer rates averaged over 2s, 10s and 40s.</p>
<h2>Source / Dest Aggregation</h2>
<p>By pressing <code>s</code> or <code>d</code> while <code>iftop</code> is running, all traffic for each source or destination will be aggregated together. This is most useful when <code>iftop</code> is run in promiscuous mode, or is run on a gateway machine.</p>
<h2>Port Display</h2>
<p><code>S</code> or <code>D</code> toggle the display of source and destination ports respectively. <code>p</code> will toggle port display on/off.</p>
<h2>Display Type</h2>
<p><code>t</code> cycles through the four line display modes; the default 2-line display, with sent and received traffic on separate lines, and 3 1-line displays, with sent, received, or total traffic shown.</p>
<h2>Display Order</h2>
<p>By default, the display is ordered according to the 10s average (2nd column). By pressing <code>1</code>, <code>2</code> or <code>3</code> it is possible to sort by the 1st, 2nd or 3rd column. By pressing <code>&lt;</code> or <code>&gt;</code> the display will be sorted by source or destination hostname respectively.</p>
<h2>Display Filtering</h2>
<p><code>l</code> allows you to enter a POSIX extended regular expression that will be used to filter hostnames shown in the display. This is a good way to quickly limit what is shown on the display. Note that this happens at a much later stage than filter code, and does not affect what is actually captured. Display filters DO NOT affect the totals at the bottom of the screen.</p>
<h2>Pause Display / Freeze Order</h2>
<p><code>P</code> will pause the current display. </p>
<p> <code>o</code> will freeze the current screen order. This has the side effect that traffic between hosts not shown on the screen at the time will not be shown at all, although it will be included in the totals at the bottom of the screen.</p>
<h2>Scroll Display</h2>
<p><code>j</code> and <code>k</code> will scroll the display of hosts. This feature is most useful when the display order is frozen (see above).</p>
<h2>Filter Code</h2>
<p><code>f</code> allows you to edit the filter code whilst iftop running. This can lead to some unexpected behaviour.</p>
<h2>Config File</h2>
<p>iftop can read its configuration from a config file. If the <code>-c</code> option is not specified, iftop will attempt to read its configuration from <code>~/.iftoprc</code>, if it exists. Any command line options specified will override settings in the config file. </p>
<p> The config file consists of one configuration directive per line. Each directive is a name value pair, for example: </p>
<pre>interface: eth0</pre>
<p>sets the network interface. The following config directives are supported: </p>
<dl>
<dt><code>interface:</code> <i>if</i></p>
<dd>Sets the network interface to <i>if</i>.</p>
<dt><code>dns-resolution:</code> <i>(yes|no)</i></p>
<dd>Controls reverse lookup of IP addresses.</p>
<dt><code>port-resolution:</code> <i>(yes|no)</i></p>
<dd>Controls conversion of port numbers to service names.</p>
<dt><code>filter-code:</code> <i>bpf</i></p>
<dd>Sets the filter code to <i>bpf</i>.</p>
<dt><code>show-bars:</code> <i>(yes|no)</i></p>
<dd>Controls display of bar graphs.</p>
<dt><code>promiscuous:</code> <i>(yes|no)</i></p>
<dd>Puts the interface into promiscuous mode.</p>
<dt><code>port-display:</code> <i>(off|source-only|destination-only|on)</i></p>
<dd>Controls display of port numbers.</p>
<dt><code>link-local:</code> <i>(yes|no)</i></p>
<dd>Determines displaying of link-local IPv6 addresses.</p>
<dt><code>hide-source:</code> <i>(yes|no)</i></p>
<dd>Hides source host names.</p>
<dt><code>hide-destination:</code> <i>(yes|no)</i></p>
<dd>Hides destination host names.</p>
<dt><code>use-bytes:</code> <i>(yes|no)</i></p>
<dd>Use bytes for bandwidth display, rather than bits.</p>
<dt><code>sort:</code> <i>(2s|10s|40s|source|destination)</i></p>
<dd>Sets which column is used to sort the display.</p>
<dt><code>line-display:</code> <i>(two-line|one-line-both|one-line-sent|one-line-received)</i></p>
<dd>Controls the appearance of each item in the display.</p>
<dt><code>show-totals:</code> <i>(yes|no)</i></p>
<dd>Shows cumulative total for each item.</p>
<dt><code>log-scale:</code> <i>(yes|no)</i></p>
<dd>Use a logarithmic scale for bar graphs.</p>
<dt><code>max-bandwidth:</code> <i>bw</i></p>
<dd>Fixes the maximum for the bar graph scale to <i>bw</i>, e.g. &quot;10M&quot;. Note that the value has to always be in bits, regardless if the option to display in bytes has been chosen.</p>
<dt><code>net-filter:</code> <i>net/mask</i></p>
<dd>Defines an IP network boundary for determining packet direction.</p>
<dt><code>net-filter6:</code> <i>net6/mask6</i></p>
<dd>Defines an IPv6 network boundary for determining packet direction.</p>
<dt><code>screen-filter:</code> <i>regexp</i></p>
<dd>Sets a regular expression to filter screen output. </p>
</dl>
<h2>QUIRKS (aka they&#8217;re features, not bugs)</h2>
<p>There are some circumstances in which iftop may not do what you expect. In most cases what it is doing is logical, and we believe it is correct behaviour, although I&#8217;m happy to hear reasoned arguments for alternative behaviour. </p>
<p> <code>Totals don&#8217;t add up</code> </p>
<p> There are several reasons why the totals may not appear to add up. The most obvious is having a screen filter in effect, or screen ordering frozen. In this case some captured information is not being shown to you, but is included in the totals. </p>
<p> A more subtle explanation comes about when running in promiscuous mode without specifying a <code>-F</code> option. In this case there is no easy way to assign the direction of traffic between two third parties. For the purposes of the main display this is done in an arbitrary fashion (by ordering of IP addresses), but for the sake of totals all traffic between other hosts is accounted as incoming, because that&#8217;s what it is from the point of view of your interface. The <code>-F</code> option allows you to specify an arbitrary network boundary, and to show traffic flowing across it. </p>
<p> <code>Peak totals don&#8217;t add up</code> </p>
<p> Again, this is a feature. The peak sent and peak received didn&#8217;t necessarily happen at the same time. The peak total is the maximum of sent plus received in each captured time division. </p>
<p> <code>Changing the filter code doesn&#8217;t seem to work</code> </p>
<p> Give it time. Changing the filter code affects what is captured from the time that you entered it, but most of what is on the display is based on some fraction of the last 40s window of capturing. After changing the filter there may be entries on the display that are disallowed by the current filter for up to 40s. DISPLAY FILTERING has immediate effect and does not affect what is captured.</p>
<h2>Files</h2>
<dl>
<dt><code>~/.iftoprc</code></p>
<dd>Configuration file for iftop. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></code>(8), <code><a href="/docs/linux/man/3-pcap/">pcap</a></code>(3), <code><a href="/docs/linux/man/1-driftnet/">driftnet</a></code>(1). </p>
<h2>Author</h2>
<p>Paul Warren &lt;pdw [at] ex-parrot.com&gt;</p>
<h2>Version</h2>
<p>$Id: iftop.8,v 1.31 2014/01/05 17:22:39 pdw Exp $</p>
<h2>Copying</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.</p>
