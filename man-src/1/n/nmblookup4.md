---
title: "nmblookup4(1)"
name: "nmblookup4"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nmblookup4/"
description: "nmblookup4 – NetBIOS over TCP/IP client used to lookup NetBIOS names"
---

<h2 class="name">NAME</h2>
<p> nmblookup4 &#8211; NetBIOS over TCP/IP client used to lookup NetBIOS names </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nmblookup4</code> [-M] [-R] [-S] [-r] [-A] [-h] [-B&nbsp;<wbr>&lt;broadcast address&gt;] [-U&nbsp;<wbr>&lt;unicast address&gt;] [-d&nbsp;<wbr>&lt;debug level&gt;] [-s&nbsp;<wbr>&lt;smb config file&gt;] [-i&nbsp;<wbr>&lt;NetBIOS scope&gt;] [-T] [-f] {name}</dl>
<h2>DESCRIPTION</h2>
<dd>This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> <code>nmblookup4</code> is used to query NetBIOS names and map them to IP addresses in a network using NetBIOS over TCP/IP queries. The options allow the name queries to be directed at a particular IP broadcast area or to a particular machine. All queries are done over UDP.</p>
<h2>OPTIONS</h2>
<p> -M</p>
<dl>
<dt>
<dd> Searches for a master browser by looking up the NetBIOS <i>name</i> with a type of <code>0x1d</code>. If <i> name</i> is &quot;-&quot; then it does a lookup on the special name <code>__MSBROWSE__</code>. Please note that in order to use the name &quot;-&quot;, you need to make sure &quot;-&quot; isn&#8217;t parsed as an argument, e.g. use : <code>nmblookup4 -M &#8212; &#8211;</code>.</dl>
<p> -R</p>
<dl>
<dt>
<dd> Set the recursion desired bit in the packet to do a recursive lookup. This is used when sending a name query to a machine running a WINS server and the user wishes to query the names in the WINS server. If this bit is unset the normal (broadcast responding) NetBIOS processing code on a machine is used instead. See RFC1001, RFC1002 for details.</dl>
<p> -S</p>
<dl>
<dt>
<dd> Once the name query has returned an IP address then do a node status query as well. A node status query returns the NetBIOS names registered by a host.</dl>
<p> -r</p>
<dl>
<dt>
<dd> Try and bind to UDP port 137 to send and receive UDP datagrams. The reason for this option is a bug in Windows 95 where it ignores the source port of the requesting packet and only replies to UDP port 137. Unfortunately, on most UNIX systems root privilege is needed to bind to this port, and in addition, if the <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) daemon is running on this machine it also binds to this port.</dl>
<p> -A</p>
<dl>
<dt>
<dd> Interpret <i>name</i> as an IP Address and do a node status query on this address.</dl>
<p> -B &lt;broadcast address&gt;</p>
<dl>
<dt>
<dd> Send the query to the given broadcast address. Without this option the default behavior of nmblookup4 is to send the query to the broadcast address of the network interfaces as either auto-detected or defined in the m[blue]<i>interfaces</i>m[]<font SIZE="-2">[1]</font> parameter of the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file.</dl>
<p> -U &lt;unicast address&gt;</p>
<dl>
<dt>
<dd> Do a unicast query to the specified address or host <i>unicast address</i>. This option (along with the <i>-R</i> option) is needed to query a WINS server.</dl>
<p> -T</p>
<dl>
<dt>
<dd> This causes any IP addresses found in the lookup to be looked up via a reverse DNS lookup into a DNS name, and printed out before each </p>
<p> <i>IP address &#8230;. NetBIOS name</i> </p>
<p> pair that is the normal output.</dl>
<p> -f</p>
<dl>
<dt>
<dd> Show which flags apply to the name that has been looked up. Possible answers are zero or more of: Response, Authoritative, Truncated, Recursion_Desired, Recursion_Available, Broadcast.</dl>
<p> name</p>
<dl>
<dt>
<dd> This is the NetBIOS name being queried. Depending upon the previous options this may be a NetBIOS name or IP address. If a NetBIOS name then the different name types may be specified by appending &#8216;#&lt;type&gt;&#8217; to the name. This name may also be &#8216;*&#8217;, which will return all registered names within a broadcast area.</dl>
<h2>EXAMPLES</h2>
<p> <code>nmblookup4</code> can be used to query a WINS server (in the same way <code>nslookup</code> is used to query DNS servers). To query a WINS server, <code>nmblookup4</code> must be called like this: </p>
<p> <code>nmblookup4 -U server -R &#8216;name&#8217;</code> </p>
<p> For example, running : </p>
<p> <code>nmblookup4 -U samba.org -R &#8216;IRIX#1B&#8217;</code> </p>
<p> would query the WINS server samba.org for the domain master browser (1B name type) for the IRIX workgroup.</p>
<h2>VERSION</h2>
<p> This man page is correct for version 3 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8), <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7), and <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5).</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The original Samba man pages were written by Karl Auer. The man page sources were converted to YODL format (another excellent piece of Open Source software, available at m[blue]<code><a href="ftp://ftp.icce.rug.nl/pub/unix/">ftp://ftp.icce.rug.nl/pub/unix/</a></code>m[]<font SIZE="-2">[2]</font>) and updated for the Samba 2.0 release by Jeremy Allison. The conversion to DocBook for Samba 2.2 was done by Gerald Carter. The conversion to DocBook XML 4.2 for Samba 3.0 was done by Alexander Bokovoy.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> <i>interfaces</i> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/smb.conf.5.html#INTERFACES</dl>
<dt> 2.</p>
<dd> <a href="ftp://ftp.icce.rug.nl/pub/unix/">ftp://ftp.icce.rug.nl/pub/unix/</a></p>
<dl>
<dt>
<dd> <a href="ftp://ftp.icce.rug.nl/pub/unix/">ftp://ftp.icce.rug.nl/pub/unix/</a></dl>
</dl>
<h2>Index</h2>
