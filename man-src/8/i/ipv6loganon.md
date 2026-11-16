---
title: "ipv6loganon(8)"
name: "ipv6loganon"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipv6loganon/"
description: "ipv6loganon – HTTP server log file anonymizer"
---

<p>ipv6loganon &#8211; HTTP server log file anonymizer</p>
<h2>Synopsis</h2>
<p>cat /var/log/httpd/access_log | <code>ipv6loganon</code> [<i>OPTIONS</i>]</p>
<h2>Description</h2>
<p>This program anonymizes IPv4/IPv6 addresses in HTTP server log files Takes data from stdin, processes it to stdout. Depending on the anonymization method, address parts (prefix/interface identifier) are 1. simply <code>zeroized</code> by given masks. 2. <code>anonymized</code> by zeroizing only required bits (partially depending on specified masks). 3. anonymized by trying to keep for IPv4 and IPv6 addresses (<code>keep-type-asn-cc</code>) When zeroing only required bits (mode 2) the possibilities are</p>
<dl>
<dt>IID:</dt>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt>EUI-48/64:</dt>
<dd>serial number would be zero&#8217;ed, keeping OID ISATAP: client IPv4 address would be anonymized by given IPv4 mask TEREDO: client IPv4 address would be anonymized by given IPv4 mask, client port would be zero&#8217;ed</dd>
<dt>6to4(Microsoft):</dt>
<dd>client IPv4 address would be anonymized by given IPv4 mask</dd>
<dt>local:</dt>
<dd>whole IID would be zero&#8217;ed (except if privacy extension was detected, then replaced by a special token)</dd></dl>
</dl>
<dt>Prefix:</dt>
<dd>IPv6 addresses including IPv4 address of client will be anonymized by the given IPv4 mask  When anonymizing with keep (mode 3) the relevant fields are: <code>type</code> of address, Autonomous System Number (<code>ASN</code>), and Country Code (<code>CC</code>) This method requires an IPv4/IPv6 to Country Code and ASN resolution, provided by GeoIP Big advantage: <a href="/docs/linux/man/8-ipv6logstats/">ipv6logstats</a>(8) result should be the same as with raw data Anonymized IPv4 addresses are from experimental range <code>240.0.0.0/8</code> Anonymized IPv6 addresses are using (currently hijacked) prefix <code>a909::/16</code> Anonymized IPv6 IID is starting with <code>a9x9</code> (x = anonymized nibbles of SLA)</dd>
<h2>Options</h2>
<p>General options:</p>
<dl>
<dt><code>[-d|&#8211;debug </code><i>DEBUGVALUE</i><code>]</code></dt>
<dd>debug value (bitwise like) can also be set by IPV6CALC_DEBUG environment value</dd>
<dt><code>[-v|&#8211;version [-v [-v]]]</code></dt>
<dd>version information (2 optional detail levels)</dd>
<dt><code>[-v|&#8211;version -h]</code></dt>
<dd>explanation of feature tokens</dd>
<dt><code>[-V|&#8211;verbose]</code></dt>
<dd>be more verbose</dd>
<dt><code>[-h|&#8211;help|-?]</code></dt>
<dd>this online help</dd></dl>
<p> External database options (depending on compiled-in suppport):</p>
<dl>
<dt><code>[&#8211;db-ip2location-disable]</code></dt>
<dd>IP2Location support disabled</dd>
<dt><code>[&#8211;db-ip2location-dir</code> <i>DIRECTORY</i><code>]</code></dt>
<dd>IP2Location database directory (default: /usr/share/IP2Location)</dd>
<dt><code>[&#8211;db-geoip-disable]</code></dt>
<dd>GeoIP support disabled</dd>
<dt><code>[&#8211;db-geoip-dir</code> <i>DIRECTORY</i><code>]</code></dt>
<dd>GeoIP database directory (default: /usr/share/GeoIP)</dd></dl>
<p> Input/output options:</p>
<dl>
<dt><code>[-w|&#8211;write]</code></dt>
<dd>write output to file instead of stdout</dd>
<dt><code>[-a|&#8211;append]</code></dt>
<dd>append output to file instead of stdout</dd>
<dt><code>[-f|&#8211;flush]</code></dt>
<dd>flush output after each line</dd>
<dt><code>[-V|&#8211;verbose]</code></dt>
<dd>be verbose</dd></dl>
<p> Performance options:</p>
<dl>
<dt><code>[-n|&#8211;nocache]</code></dt>
<dd>disable caching</dd>
<dt><code>[-c|&#8211;cachelimit </code><i>VALUE</i><code>]</code></dt>
<dd>set cache limit. Default: <code>20</code>, maximum: <code>200</code>.</dd></dl>
<p> Processing options: </p>
<p> Shortcut for anonymization presets:</p>
<dl>
<dd>
</dd><dl>
<dd><code>&#8211;anonymize-standard</code> (default)</dd>
<dd><code>&#8211;anonymize-careful</code></dd>
<dd><code>&#8211;anonymize-paranoid</code></dd></dl>
</dl>
<p> Supported methods <code>[&#8211;anonymize-method </code><i>METHOD</i><code>]</code>:</p>
<dl>
<dt><code>anonymize</code></dt>
<dd>reliable anonymization, keep as much type information as possible</dd>
<dt><code>zeroize</code></dt>
<dd>simple zeroizing according to given masks, probably loose type information</dd>
<dt><code>keep-type-asn-cc</code> special reliable anonymization, keep type &amp;</dt>
<dd>Autonomous System Number and CountryCode. LP Available presets (shortcut names) [&#8211;anonymize-preset <i>PRESET-NAME</i>]:</dd>
<dt><code>anonymize-standard</code> (<code>as</code>):</dt>
<dd>mask-ipv6= 56 mask-ipv4=24 mask-eui64=40 mask-mac=24 mask-autoadjust=yes method=anonymize</dd>
<dt><code>anonymize-careful</code> (<code>ac</code>):</dt>
<dd>mask-ipv6= 48 mask-ipv4=20 mask-eui64=24 mask-mac=24 mask-autoadjust=yes method=anonymize</dd>
<dt><code>anonymize-paranoid</code> (<code>ap</code>):</dt>
<dd>mask-ipv6= 40 mask-ipv4=16 mask-eui64= 0 mask-mac=24 mask-autoadjust=no method=anonymize</dd>
<dt><code>zeroize-standard</code> (<code>zs</code>):</dt>
<dd>mask-ipv6= 56 mask-ipv4=24 mask-eui64=40 mask-mac=24 mask-autoadjust=yes method=zeroize</dd>
<dt><code>zeroize-careful</code> (<code>zc</code>):</dt>
<dd>mask-ipv6= 48 mask-ipv4=20 mask-eui64=24 mask-mac=24 mask-autoadjust=yes method=zeroize</dd>
<dt><code>zeroize-paranoid</code> (<code>zp</code>):</dt>
<dd>mask-ipv6= 40 mask-ipv4=16 mask-eui64= 0 mask-mac=24 mask-autoadjust=no method=zeroize</dd>
<dt><code>keep-type-asn-cc</code> (<code>kp</code>):</dt>
<dd>mask-ipv6= 56 mask-ipv4=24 mask-eui64=40 mask-mac=24 mask-autoadjust=yes method=keep-type-asn-cc</dd></dl>
<p> Custom control:</p>
<dl>
<dt><code>&#8211;mask-ipv4</code> <i>BITS</i></dt>
<dd>mask IPv4 address [0-32] (even if occurs in IPv6 address)</dd>
<dt><code>&#8211;mask-ipv6</code> <i>BITS</i></dt>
<dd>mask IPv6 prefix [0-64] (only applied to related address types)</dd>
<dt><code>&#8211;mask-eui64</code> <i>BITS</i></dt>
<dd>mask EUI-64 address or IPv6 interface identifier [0-64]</dd>
<dt><code>&#8211;mask-mac</code> <i>BITS</i></dt>
<dd>mask MAC address [0-48]</dd>
<dt><code>&#8211;mask-autoadjust yes|no</code></dt>
<dd>autoadjust mask to keep type/vendor information regardless of less given mask</dd></dl>
<h2>Examples</h2>
<p>Original lines (stdin): </p>
<p> 207.46.98.53 &#8211; &#8211; [01/Jan/2007:00:01:15 +0100] &quot;GET /Linux+IPv6-HOWTO/x1112.html HTTP/1.0&quot; 200 6162 &quot;-&quot; &quot;msnbot/1.0 (+<a rel="nofollow" href="http://search.msn.com/msnbot.htm)">http://search.msn.com/msnbot.htm)</a>&quot; 253 6334 </p>
<p> 2002:52b6:6b01:1:216:17ff:fe01:2345 &#8211; &#8211; [10/Jan/2007:15:04:28 +0100] &quot;GET /favicon.ico HTTP/1.1&quot; 200 4710 &quot;<a rel="nofollow" href="http://www.bieringer.de/linux/IPv6/">http://www.bieringer.de/linux/IPv6/</a>&quot; &quot;Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.9) Gecko/20061219 Fedora/1.5.0.9-1.fc6 Firefox/1.5.0.9 pango-text&quot; 413 5005 </p>
<p> Modified lines (stdout): </p>
<p> 207.46.98.0 &#8211; &#8211; [01/Jan/2007:00:01:15 +0100] &quot;GET /Linux+IPv6-HOWTO/x1112.html HTTP/1.0&quot; 200 6162 &quot;-&quot; &quot;msnbot/1.0 (+<a rel="nofollow" href="http://search.msn.com/msnbot.htm)">http://search.msn.com/msnbot.htm)</a>&quot; 253 6334 </p>
<p> 2002:52b6:6b00:0:216:17ff:fe00:0 &#8211; &#8211; [10/Jan/2007:15:04:28 +0100] &quot;GET /favicon.ico HTTP/1.1&quot; 200 4710 &quot;<a rel="nofollow" href="http://www.bieringer.de/linux/IPv6/">http://www.bieringer.de/linux/IPv6/</a>&quot; &quot;Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.9) Gecko/20061219 Fedora/1.5.0.9-1.fc6 Firefox/1.5.0.9 pango-text&quot; 413 5005 </p>
<p> Anonymization method: keep-type-asn-cc </p>
<p> echo &quot;1.2.3.4&quot; | ./ipv6loganon &#8211;anonymize-preset keep-type-asn-cc 246.24.59.65 </p>
<p> echo &quot;2001:a60:1400:1201:221:70ff:fe01:2345&quot; | ./ipv6loganon &#8211;anonymize-preset keep-type-asn-cc a909:16fa:9092:23ff:a909:4291:4022:1708</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipv6calc/">ipv6calc</a>(8), ipv6logstat(8)</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;ipv6calc [at] lists.deepspace6.net&gt; or to the authors. </p>
<p> Homepage: <a rel="nofollow" href="http://www.deepspace6.net/projects/ipv6calc.html">http://www.deepspace6.net/projects/ipv6calc.html</a></p>
<h2>License</h2>
<p>GPLv2</p>
<h2>Authors</h2>
<p>Peter Bieringer &lt;pb [at] bieringer.de&gt;</p>
</dl>