---
title: "mac-vendor(5)"
name: "mac-vendor"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mac-vendor/"
description: "mac-vendor – Ethernet vendor file for arp-scan"
---

<p>mac-vendor &#8211; Ethernet vendor file for arp-scan</p>
<h2>Synopsis</h2>
<p><i>mac-vendor.txt</i></p>
<h2>Description</h2>
<p>The <i>mac-vendor.txt</i> contains Ethernet MAC to vendor string mappings for <code>arp-scan</code>. It is used in addition to the IEEE OUI and IAB listings in <i>ieee-oui.txt</i> and <i>ieee-iab.txt</i>. It is for MAC-vendor mappings that are not covered by the IEEE manufacturer listings. Each line in the <i>mac-vendor.txt</i> file contains a MAC-vendor mapping in the form: </p>
<pre><code>&lt;MAC-Prefix&gt;&lt;TAB&gt;&lt;Vendor&gt;</code></pre>
<p> Where &lt;MAC-Prefix&gt; is the prefix of the MAC address in hex, and &lt;Vendor&gt; is the name of the vendor. The prefix can be of any length from two hex digits (one octet) to twelve hex digits (six octets, the entire Ethernet hardware address). The alphabetic hex characters [A-F] must be entered in upper case. For example: </p>
<pre>012345 would match 01:23:45:xx:xx:xx, where xx represents any value;
0123456 would match 01:23:45:6x:xx:xx; and
01234567 would match 01:23:45:67:xx:xx.</pre>
<p>Blank lines and lines beginning with &quot;#&quot; are ignored. The order of entries in the file is not important. <code>arp-scan</code> will attempt to match larger prefixes before trying to match smaller ones, and will stop at the first match.</p>
<h2>Files</h2>
<p><i>/usr/local/share/arp-scan/mac-vendor.txt</i></p>
<h2>Example</h2>
<pre># From nmap Debian bug report #369681 dated 31 May 2006
525400 QEMU
B0C420 Bochs
# From RFC 2338: 00-00-5E-00-01-{VRID}
00005E0001 VRRP (last octet is VRID)
# Microsoft WLBS (Windows NT Load Balancing Service)
# <a rel="nofollow" href="http://www.microsoft.com/technet/prodtechnol/acs/reskit/acrkappb.mspx">http://www.microsoft.com/technet/prodtechnol/acs/reskit/acrkappb.mspx</a>
02BF Microsoft WLBS (last four octets are IP address)</pre>
<h2>Author</h2>
<p>Roy Hills &lt;Roy.Hills [at] nta-monitor.com&gt;</p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-arp-scan/">arp-scan</a></code>(1)</p>
<dd>
<dt><code><a href="/docs/linux/man/1-get-oui/">get-oui</a></code>(1)</p>
<dd>
<dt><code><a href="/docs/linux/man/1-get-iab/">get-iab</a></code>(1)</p>
<dd>
<dt><code><a href="/docs/linux/man/1-arp-fingerprint/">arp-fingerprint</a></code>(1)</p>
<dd></dl>
<p> <i><a rel="nofollow" href="http://www.nta-monitor.com/wiki/">http://www.nta-monitor.com/wiki/</a></i> The arp-scan wiki page. </p>
