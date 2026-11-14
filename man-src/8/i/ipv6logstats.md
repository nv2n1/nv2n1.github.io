---
title: "ipv6logstats(8)"
name: "ipv6logstats"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipv6logstats/"
description: "ipv6logstats – Takes http log data from stdin and print a statistics table on output"
---

<p>ipv6logstats &#8211; Takes http log data from stdin and print a statistics table on output</p>
<h2>Synopsis</h2>
<p>cat /var/log/httpd/access_log | <code>ipv6logstats</code> [<i>OPTIONS</i>]</p>
<h2>Syntax</h2>
<p>ipv6logstats [logfile]</p>
<h2>Description</h2>
<p>Takes web server log data (or any other data which has IPv4/v6 address in first column) from stdin and print statistics table/list (depending on option) to stdout</p>
<h2>Options</h2>
<p>General options:</p>
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
<dd>this online help</p>
<dt><code>[-q|&#8211;quiet]</code></p>
<dd>be more quiet</dl>
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
<dt><code>[-u|&#8211;unknown]</code></p>
<dd>print unknown IP addresses to stderr</p>
<dt><code>[-c|&#8211;columns]</code></p>
<dd>print statistics in columns (1)</p>
<dt><code>[-N|&#8211;column-numbers]</code></p>
<dd>print column numbers</p>
<dt><code>[-n|&#8211;noheader]</code></p>
<dd>don&#8217;t print header in columns mode (1)</p>
<dt><code>[-o|&#8211;onlyheader]</code></p>
<dd>print only header in columns mode (1)</p>
<dt><code>[-p|&#8211;prefix</code> <i>TOKEN</i><code>]</code></p>
<dd>print token as prefix (1)</p>
<dt><code>[-s|&#8211;simple]</code></p>
<dd>disable extended statistic (CountryCode/ASN)<br />
&nbsp;<wbr>(1)&nbsp;<wbr>unsupported for CountryCode&nbsp;<wbr>&amp;&nbsp;<wbr>ASN statistics </p>
</dl>
<h2>Examples</h2>
<p>Column mode: </p>
<p> echo &quot;2001:a60:1400:1201:221:70ff:fe01:2345&quot; | ./ipv6logstats -c -q </p>
<pre>ALL IPv4 IPv6 UNKNOWN IPv4/APNIC IPv4/ARIN IPv4/RIPE IPv4/LACNIC IPv4/AFRINIC IPv4/UNKNOWN IPv6/6bone IPv6/IANA IPv6/APNIC IPv6/ARIN IPv6/RIPE IPv6/LACNIC IPv6/AFRINIC IPv6/RESERVED IPv6/UNKNOWN IPv6/6to4/IANA IPv6/6to4/APNIC IPv6/6to4/ARIN IPv6/6to4/RIPE IPv6/6to4/LACNIC IPv6/6to4/AFRINIC IPv6/6to4/RESERVED IPv6/6to4/UNKNOWN IPv6/Teredo/IANA IPv6/Teredo/APNIC IPv6/Teredo/ARIN IPv6/Teredo/RIPE IPv6/Teredo/LACNIC IPv6/Teredo/AFRINIC IPv6/Teredo/RESERVED IPv6/Teredo/UNKNOWN IPv6/NAT64/IANA IPv6/NAT64/APNIC IPv6/NAT64/ARIN IPv6/NAT64/RIPE IPv6/NAT64/LACNIC IPv6/NAT64/AFRINIC IPv6/NAT64/RESERVED IPv6/NAT64/UNKNOWN IPv6/IID/Global IPv6/IID/Random IPv6/IID/Manual IPv6/IID/ISATAP IPv6/IID/Unknown #Version(4.0)
 
1 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 #4.0
Row mode:
echo &quot;2001:a60:1400:1201:221:70ff:fe01:2345&quot; | ./ipv6logstats -q 
*Version 4.0
*DateTime: 2014:07:23 19:59:56+0000 GMT
*UnixTime: 1406145596
ALL 1
IPv4 0
IPv6 1
IPv6/RIPE 1
IPv6/IID/Global 1
*3*CC-code-proto/DE/ALL 1
*3*CC-code-proto/DE/IPv4 0
*3*CC-code-proto/DE/IPv6 1
*3*CC-code-proto-list/DE 1 0 1
*3*CC-proto-code/ALL/DE 1
*3*CC-proto-code/IPv6/DE 1
*3*CC-proto-code-list/ALL 1 0 1
*3*AS-num-proto/8767/ALL 1
*3*AS-num-proto/8767/IPv4 0
*3*AS-num-proto/8767/IPv6 1
*3*AS-num-proto-list/8767 1 0 1
*3*AS-proto-num/ALL/8767 1
*3*AS-proto-num/IPv6/8767 1
*3*AS-proto-num-list/ALL 1 0 1</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipv6calc/">ipv6calc</a>(8)</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;ipv6calc [at] lists.deepspace6.net&gt; or to the authors. </p>
<p> Homepage: <a rel="nofollow" href="http://www.deepspace6.net/projects/ipv6calc.html">http://www.deepspace6.net/projects/ipv6calc.html</a></p>
<h2>Copyright</h2>
<p>GPLv2</p>
<h2>Authors</h2>
<p>Peter Bieringer &lt;pb [at] bieringer.de&gt;</p>
