---
title: "get-oui(1)"
name: "get-oui"
section: "1"
letter: "g"
url: "/docs/linux/man/1-get-oui/"
description: "get-oui – Fetch the arp-scan OUI file from the IEEE website"
---

<h2 class="name">NAME</h2>
<p> get-oui &#8211; Fetch the arp-scan OUI file from the IEEE website </p>
<h2>SYNOPSIS</h2>
<p> <code>get-oui</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>get-oui</code> fetches the Ethernet OUI file from the IEEE website, and saves it in the format used by arp-scan. </p>
<p> The OUI file contains all of the OUIs (Organizationally Unique Identifiers) that have been registered with IEEE. Each OUI entry in the file specifies the first 24-bits of the 48-bit Ethernet hardware address, leaving the remaining 24-bits for use by the registering organisation. For example the OUI entry &quot;080020&quot;, registered to Sun Microsystems, applies to any Ethernet hardware address from <i>08:00:20:00:00:00</i> to <i>08:00:20:ff:ff:ff</i> inclusive. Each OUI assignment represents a total of 2^24 (16,777,216) Ethernet addresses. </p>
<p> Every major Ethernet hardware vendor registers an OUI for their equipment, and larger vendors will need to register more than one. For example, 3Com have a total of 37 OUI entries. Organisations that only produce a small number of Ethernet devices will often obtain an IAB registration instead. See <code><a href="/docs/linux/man/1-get-iab/">get-iab</a></code>(1) for details. </p>
<p> This script can be used to update the <code>arp-scan</code> OUI file from the latest data on the IEEE website. Most of the Ethernet addresses in use belong to an OUI registration, so this is the most important of the files that <code>arp-scan</code> uses to decode Ethernet hardware addresses. You should therefore run <code>get-oui</code> occasionally to keep the <code>arp-scan</code> OUI file up to date. </p>
<p> The OUI data is fetched from the URL <i><a rel="nofollow" href="http://standards.ieee.org/regauth/oui/oui.txt">http://standards.ieee.org/regauth/oui/oui.txt</a></i> and the output file is saved to the file <i>ieee-oui.txt</i> in the current directory. The URL to fetch the data from can be changed with the <code>-u</code> option, and the output file name can be changed with the <code>-f</code> option. </p>
<p> The <i>ieee-oui.txt</i> file that is produced by this script is used by <code>arp-scan</code> to determine the Ethernet card vendor from its hardware address. </p>
<p> The directory that <code>arp-scan</code> will look for the <i>ieee-oui.txt</i> file depends on the options used when it was built. If it was built using the default options, then it will look in <i>/usr/local/share/arp-scan</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display a brief usage message and exit.</p>
<dt><code>-f &lt;fn&gt;</code></p>
<dd> Write the output to the specified file instead of the default <i>ieee-oui.txt.</i></p>
<dt><code>-u &lt;URL&gt;</code></p>
<dd> Use the specified URL to fetch the raw OUI data from instead of the default <i><a rel="nofollow" href="http://standards.ieee.org/regauth/oui/oui.txt.">http://standards.ieee.org/regauth/oui/oui.txt.</a></i></p>
<dt><code>-v</code></p>
<dd> Display verbose progress messages.</dl>
<h2>FILES</h2>
<dl>
<dt><i>ieee-oui.txt</i></p>
<dd> The default output file.</dl>
<h2>EXAMPLES</h2>
<pre>
$ get-oui -v
Renaming ieee-oui.txt to ieee-oui.txt.bak
Fetching OUI data from <a rel="nofollow" href="http://standards.ieee.org/regauth/oui/oui.txt">http://standards.ieee.org/regauth/oui/oui.txt</a>
Fetched 1467278 bytes
Opening output file ieee-oui.txt
9274 OUI entries written to file ieee-oui.txt
</pre>
<h2>NOTES</h2>
<p> <code>get-oui</code> is implemented in Perl, so you need to have the Perl interpreter installed on your system to use it. </p>
<p> <code>get-oui</code> uses the <i>LWP::UserAgent</i> Perl module to fetch the data from the IEEE website. You must have this module installed on your system for it to work. This module is available on most distributions, often called <i>libwww-perl</i>. It is also available in source form from CPAN. </p>
<p> You can use a proxy server by defining the <i>http_proxy</i> environment variable.</p>
<h2>AUTHOR</h2>
<p> Roy Hills &lt;Roy.Hills [at] nta-monitor.com&gt;</p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-arp-scan/">arp-scan</a></code>(1)</p>
<dd>
<dt><code><a href="/docs/linux/man/1-get-iab/">get-iab</a></code>(1)</p>
<dd>
<dt><code><a href="/docs/linux/man/1-arp-fingerprint/">arp-fingerprint</a></code>(1)</p>
<dd></dl>
<p> <i><a rel="nofollow" href="http://www.nta-monitor.com/wiki/">http://www.nta-monitor.com/wiki/</a></i> The arp-scan wiki page. </p>
<h2>Index</h2>
