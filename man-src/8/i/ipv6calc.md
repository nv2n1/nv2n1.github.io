---
title: "ipv6calc(8)"
name: "ipv6calc"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipv6calc/"
description: "ipv6calc – format and calculate IPv6/IPv4/MAC"
---

<p>ipv6calc &#8211; format and calculate IPv6/IPv4/MAC</p>
<h2>Synopsis</h2>
<p>ipv6calc [<i>OPTIONS</i>] [<code>&lt;input data&gt;</code>] </p>
<h2>Description</h2>
<p>This program formats and calculates IPv6/IPv4/MAC addresses and can do many more tricky things, e.g. includes a pipe filter capability.</p>
<h2>Options</h2>
<p>If no data is presented as command-line arguments, data is read from standard input. </p>
<p> General options:</p>
<dl>
<dt><code>[-d|&#8211;debug </code><i>DEBUGVALUE</i><code>]</code></p>
<dd>debug value (bitwise like) can also be set by IPV6CALC_DEBUG environment value</p>
<dt><code>[-v|&#8211;version [-v [-v]]]</code></p>
<dd>version information (2 optional detail levels)</p>
<dt><code>[-v|&#8211;version -h]</code></p>
<dd>explanation of feature tokens</p>
<dt><code>[-V|&#8211;verbose]</code></p>
<dd>be more verbose</p>
<dt><code>[-h|&#8211;help|-?]</code></p>
<dd>this online help</dl>
<p> External database options (depending on compiled-in suppport):</p>
<dl>
<dt><code>[&#8211;db-ip2location-disable]</code></p>
<dd>IP2Location support disabled</p>
<dt><code>[&#8211;db-ip2location-dir</code> <i>DIRECTORY</i><code>]</code></p>
<dd>IP2Location database directory (default: /usr/share/IP2Location)</p>
<dt><code>[&#8211;db-geoip-disable]</code></p>
<dd>GeoIP support disabled</p>
<dt><code>[&#8211;db-geoip-dir</code> <i>DIRECTORY</i><code>]</code></p>
<dd>GeoIP database directory (default: /usr/share/GeoIP)</dl>
<p> Special options:</p>
<dl>
<dt><code>[-q|&#8211;quiet]</code></p>
<dd>be more quiet (auto-enabled in pipe mode)</p>
<dt><code>[-f|&#8211;flush]</code></p>
<dd>flush each line in pipe mode</dl>
<p> Usage with new style options:</p>
<dl>
<dt><code>[&#8211;in|-I</code> <i>INPUT-TYPE</i><code>]</code></p>
<dd>specify input type (default: autodetect)</p>
<dt><code>[&#8211;out|-O</code> <i>OUTPUT-TYPE</i><code>]</code></p>
<dd>specify output type (sometimes: autodetect)</p>
<dt><code>[&#8211;action|-A</code> <i>ACTION</i><code>]</code></p>
<dd>specify action (default: format conversion, sometimes: autodetect)</p>
<dt><code>[&lt;format option&gt; &#8230;]</code></p>
<dd>specify format options</p>
<dt><code>&lt;input data&gt; [&#8230;]</code></p>
<dd>input data</p>
<dl>
<dd>
<dl>
<dt>Available input types:</p>
<dd><code>[-m] -I|&#8211;in -?|-h|&#8211;help</code></p>
<dt>Available output types:</p>
<dd><code>[-m] -O|&#8211;out -?|-h|&#8211;help</code></p>
<dt>Available action types:</p>
<dd><code>[-m] -A|&#8211;action -?|-h|&#8211;help</code></dl>
</dl>
</dl>
<p>&nbsp;<wbr>Other usage:</p>
<dl>
<dt><code>&#8211;showinfo|-i [&#8211;machine_readable|-m]</code></p>
<dd>show information about input data</p>
<dt><code>&#8211;showinfo|-i &#8211;show_types</code></p>
<dd>show available types on &#8216;-m&#8217;</dl>
<p> Usage with shortcut options: &lt;shortcut option&gt; [&lt;format option&gt; &#8230;] &lt;input data&gt; </p>
<p> For more information and available format options use: &lt;shortcut option&gt; -?|-h|&#8211;help </p>
<p> <code>-r|&#8211;addr2ip6_int</code> (-O revnibbles.int) </p>
<p> <code>-r|&#8211;addr_to_ip6int</code> (-O revnibbles.int) </p>
<p> <code>-a|&#8211;addr2ip6_arpa</code> (-O revnibbles.arpa) </p>
<p> <code>-a|&#8211;addr_to_ip6arpa</code> (-O revnibbles.arpa) </p>
<p> <code>-b|&#8211;addr_to_bitstring</code> (-O bitstring) </p>
<p> <code> &#8211;addr2compaddr</code> (&#8211;printcompressed) </p>
<p> <code> &#8211;addr_to_compressed</code> (&#8211;printcompressed) </p>
<p> <code> &#8211;addr2uncompaddr</code> (&#8211;printuncompressed) </p>
<p> <code> &#8211;addr_to_uncompressed</code> (&#8211;printuncompressed) </p>
<p> <code> &#8211;addr_to_base85</code> (-I ipv6addr -O base85) </p>
<p> <code> &#8211;base85_to_addr</code> (-I base85 -O ipv6addr) </p>
<p> <code> &#8211;mac_to_eui64</code> (-I mac -O eui64) </p>
<p> <code> &#8211;addr2fulluncompaddr</code> (&#8211;printfulluncompressed) </p>
<p> <code> &#8211;addr_to_fulluncompressed</code> (&#8211;printfulluncompressed) </p>
<p> <code> &#8211;addr2if_inet6</code> (-I ipv6addr -O ifinet6) </p>
<p> <code> &#8211;addr_to_ifinet6</code> (-I ipv6addr -O ifinet6) </p>
<p> <code> &#8211;if_inet62addr</code> (-I ifinet6 -O ipv6addr &#8211;printcompressed) </p>
<p> <code> &#8211;ifinet6_to_compressed</code> (-I ifinet6 -O ipv6addr &#8211;printcompressed) </p>
<p> <code> &#8211;eui64_to_privacy</code> (-I iid_token -O iid_token -A genprivacyiid) </p>
<p> <code> &#8211;ipv4_to_6to4addr</code> (-I ipv4 -O ipv6addr -A conv6to4) </p>
<p> See inline help or documentation for more.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;ipv6calc [at] lists.deepspace6.net&gt; or to the authors.<br />
 Homepage: <a rel="nofollow" href="http://www.deepspace6.net/projects/ipv6calc.html">http://www.deepspace6.net/projects/ipv6calc.html</a></p>
<h2>Examples</h2>
<p>To run this program the standard way type: </p>
<p> ipv6calc &#8211;showinfo -i -m ::1 </p>
<p> ipv6calc &#8211;showinfo -m 127.0.0.1 </p>
<p> ipv6calc &#8211;showinfo &#8211;show_types </p>
<p> ipv6calc &#8211;ipv4_to_6to4addr 127.0.0.1 </p>
<p> ipv6calc &#8211;addr_to_uncompressed ::1 </p>
<p> Usage of filters in pipe mode:</p>
<dl>
<dd>cat &lt;Apache-Logfile&gt; | ipv6calc -E ipv6.db.cc=US,iid-random</dl>
<h2>Copyright</h2>
<p>GPLv2</p>
<h2>Authors</h2>
<p>Peter Bieringer &lt;pb [at] bieringer.de&gt;</p>
