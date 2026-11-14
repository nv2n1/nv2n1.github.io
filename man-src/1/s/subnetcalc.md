---
title: "subnetcalc(1)"
name: "subnetcalc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-subnetcalc/"
description: "subnetcalc – IPv4/IPv6 Subnet Calculator"
---

<h2 class="name">NAME</h2>
<p> <code>subnetcalc</code> &#8211; IPv4/IPv6 Subnet Calculator </p>
<h2>SYNOPSIS</h2>
<p> <code>subnetcalc</code> [Address] [Netmask/Prefix] [-<code>n</code> ] [-<code>uniquelocal</code> ] [-<code>uniquelocalhq</code> ] [-<code>nocolour|-nocolor</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>subnetcalc</code> is an IPv4/IPv6 subnet address calculator. For given IPv4 or IPv6 address and netmask or prefix length, it calculates network address, broadcast address, maximum number of hosts and host address range. Also, it prints the addresses in binary format for better understandability. Furthermore, it prints useful information on specific address types (e.g. type, scope, interface ID, etc.). </p>
<h2>ARGUMENTS</h2>
<p> The following arguments have to be provided:</p>
<dl>
<dt><code>Address</code></p>
<dd> The IP address. If a hostname is provided here, it is tried to resolve the address by a DNS server and the first returned address is used. Internationalized Domain Names (IDN) are supported.</p>
<dt><code>Netmask/Prefix</code></p>
<dd> The netmask or prefix length (0-32 for IPv4; 0-128 for IPv6).</p>
<dt><code>-n</code></p>
<dd> Skip trying a reverse DNS lookup.</p>
<dt><code>-uniquelocal</code></p>
<dd> Given an IPv6 address, the first 48 bits of the address are replaced by a randomly chosen IPv6 Unique Local prefix in fc00::/7 (see also RFC 4193). Under Linux, /dev/urandom is used for random number generation.</p>
<dt><code>-uniquelocalhq</code></p>
<dd> Like -uniquelocal, but using /dev/random instead on Linux systems for highest-quality random number generation. On other systems, this option is equal to -uniquelocal. Note, that reading from /dev/random may take some time. You can speed up this process by delivering random input e.g. by pressing keys or moving the mouse.</p>
<dt><code>-nocolour|-nocolor</code></p>
<dd> Turns colourised output off.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>subnetcalc 132.252.250.0 255.255.255.0</code></p>
<dd>
<dt><code>subnetcalc 132.252.250.0/255.255.255.0 -nocolor</code></p>
<dd>
<dt><code>subnetcalc 132.252.250.0 24</code></p>
<dd>
<dt><code>subnetcalc 132.252.250.0/24 -nocolour</code></p>
<dd>
<dt><code>subnetcalc fec0:2345:6789:1111:221:6aff:fe0b:2674 56</code></p>
<dd>
<dt><code>subnetcalc 2a00:1450:8007::69 64</code></p>
<dd>
<dt><code>subnetcalc ff08::1:2:3</code></p>
<dd>
<dt><code>subnetcalc 131.220.6.5/24</code></p>
<dd>
<dt><code>subnetcalc 132.252.181.87 -n</code></p>
<dd>
<dt><code>subnetcalc <a rel="nofollow" href="http://www.iem.uni-due.de">www.iem.uni-due.de</a> 24</code></p>
<dd>
<dt><code>subnetcalc <a rel="nofollow" href="http://www.six.heise.de">www.six.heise.de</a></code></p>
<dd>
<dt><code>subnetcalc fd00:: 64 -uniquelocal</code></p>
<dd>
<dt><code>subnetcalc fd00::9876:256:7bff:fe1b:3255 56 -uniquelocalhq</code></p>
<dd>
<dt><code>subnetcalc düsseldorf.de 28</code></p>
<dd>
<dt><code>subnetcalc <a rel="nofollow" href="http://www.k">www.k</a>öln.de</code></p>
<dd>
<dt><code>subnetcalc räksmörgås.josefsson.org 24</code></p>
<dd></dl>
<h2>AUTHORS</h2>
<p> Thomas Dreibholz<br />
 <a rel="nofollow" href="http://www.iem.uni-due.de/~dreibh/subnetcalc">http://www.iem.uni-due.de/~dreibh/subnetcalc</a><br />
 mailto://dreibh [at] iem.uni-due.de </p>
<h2>Index</h2>
