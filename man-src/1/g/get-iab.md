---
title: "get-iab(1)"
name: "get-iab"
section: "1"
letter: "g"
url: "/docs/linux/man/1-get-iab/"
description: "get-iab – Fetch the arp-scan IAB file from the IEEE website"
---

<h2 class="name">NAME</h2>
<p> get-iab &#8211; Fetch the arp-scan IAB file from the IEEE website </p>
<h2>SYNOPSIS</h2>
<p> <code>get-iab</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>get-iab</code> fetches the Ethernet IAB file from the IEEE website, and saves it in the format used by arp-scan. </p>
<p> The IAB file contains all of the IABs (Individual Address Blocks) that have been registered with IEEE. Each IAB entry in the file specifies the first 36-bits of the 48-bit Ethernet hardware address, leaving the remaining 12-bits for use by the registering organisation. For example the IAB entry &quot;0050C2003&quot;, registered to Microsoft, applies to any Ethernet hardware address from <i>00:50:c2:00:30:00</i> to <i>00:50:c2:00:3f:ff</i> inclusive. Each IAB assignment represents a total of 2^12 (4,096) Ethernet addresses. </p>
<p> Major Ethernet hardware vendors typically use an OUI registration rather than an IAB registration. See <code><a href="/docs/linux/man/1-get-oui/">get-oui</a></code>(1) for details. </p>
<p> This script can be used to update the <code>arp-scan</code> IAB file from the latest data on the IEEE website. It is relatively rare to see Ethernet addresses from IAB registrations, so the IAB file is not as important as the OUI file. </p>
<p> The IAB data is fetched from the URL <i><a rel="nofollow" href="http://standards.ieee.org/regauth/oui/iab.txt">http://standards.ieee.org/regauth/oui/iab.txt</a></i> and the output file is saved to the file <i>ieee-iab.txt</i> in the current directory. The URL to fetch the data from can be changed with the <code>-u</code> option, and the output file name can be changed with the <code>-f</code> option. </p>
<p> The <i>ieee-iab.txt</i> file that is produced by this script is used by <code>arp-scan</code> to determine the Ethernet card vendor from its hardware address. </p>
<p> The directory that <code>arp-scan</code> will look for the <i>ieee-iab.txt</i> file depends on the options used when it was built. If it was built using the default options, then it will look in <i>/usr/local/share/arp-scan</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display a brief usage message and exit.</p>
<dt><code>-f &lt;fn&gt;</code></p>
<dd> Write the output to the specified file instead of the default <i>ieee-iab.txt.</i></p>
<dt><code>-u &lt;URL&gt;</code></p>
<dd> Use the specified URL to fetch the raw IAB data from instead of the default <i><a rel="nofollow" href="http://standards.ieee.org/regauth/oui/iab.txt">http://standards.ieee.org/regauth/oui/iab.txt</a></i></p>
<dt><code>-v</code></p>
<dd> Display verbose progress messages.</dl>
<h2>FILES</h2>
<dl>
<dt><i>ieee-iab.txt</i></p>
<dd> The default output file.</dl>
<h2>EXAMPLES</h2>
<pre>
$ get-iab -v
Renaming ieee-iab.txt to ieee-iab.txt.bak
Fetching IAB data from <a rel="nofollow" href="http://standards.ieee.org/regauth/oui/iab.txt">http://standards.ieee.org/regauth/oui/iab.txt</a>
Fetched 230786 bytes
Opening output file ieee-iab.txt
1535 IAB entries written to file ieee-iab.txt
</pre>
<h2>NOTES</h2>
<p> <code>get-iab</code> is implemented in Perl, so you need to have the Perl interpreter installed on your system to use it. </p>
<p> <code>get-iab</code> uses the <i>LWP::UserAgent</i> Perl module to fetch the data from the IEEE website. You must have this module installed on your system for it to work. This module is available on most distributions, often called <i>libwww-perl</i>. It is also available in source form from CPAN. </p>
<p> You can use a proxy server by defining the <i>http_proxy</i> environment variable.</p>
<h2>AUTHOR</h2>
<p> Roy Hills &lt;Roy.Hills [at] nta-monitor.com&gt;</p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-arp-scan/">arp-scan</a></code>(1)</p>
<dd>
<dt><code><a href="/docs/linux/man/1-get-oui/">get-oui</a></code>(1)</p>
<dd>
<dt><code><a href="/docs/linux/man/1-arp-fingerprint/">arp-fingerprint</a></code>(1)</p>
<dd></dl>
<p> <i><a rel="nofollow" href="http://www.nta-monitor.com/wiki/">http://www.nta-monitor.com/wiki/</a></i> The arp-scan wiki page. </p>
<h2>Index</h2>
