---
title: "mpcd(8)"
name: "mpcd"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mpcd/"
description: "mpcd – ATM MPOA (Multi-Protocol Over ATM) client daemon"
---

<p>mpcd &#8211; ATM MPOA (Multi-Protocol Over ATM) client daemon</p>
<h2>Synopsis</h2>
<p><code>mpcd</code> <code>[ -s</code> <i>Control ATM address</i> <code>]</code> <code>[ -l</code> <i>Data ATM address</i> <code>]</code> <code>[ -c</code> <i>MPS control ATM address</i> <code>]</code> <code>[ -i</code> <i>Interface number</i> <code>]</code> <code>[ -m</code> <i>MPS MAC address</i> <code>]</code> <code>[ -L</code> <i>LEC address</i> <code>[ -n</code> <i>ELAN name</i> <code>]</code> <code>[ -C</code> <i>LECS Address</i> <code>]]</code></p>
<h2>Description</h2>
<p>MPOA client <font SIZE="-1">(MPC) is responsible for creating and receiving</font> internetwork layer shortcuts. Using these shortcuts MPCs forward unicast internetwork layer packets effectively over ATM without need for routing protocols. </p>
<p> <font SIZE="-1">MPC</font> has two roles; ingress and egress. In ingress role <font SIZE="-1">MPC</font> detects flows destined outside it&#8217;s own subnet and tries to establish shortcuts to those destinations. In egress role <font SIZE="-1">MPC</font> accepts shortcuts and packets arriving on those shortcuts. Maintaining shortcuts is done with the help of <font SIZE="-1">MPOA</font> server <font SIZE="-1">(MPS).</font> </p>
<p> Just as the Linux <font SIZE="-1">LAN</font> Emulation client, <font SIZE="-1">MPOA</font> client is also divided in two parts. The parts are kernel component and a daemon process. The daemon opens and receives data shortcuts and control connections with the kernel component. The kernel component tallies packets flowing out from the <font SIZE="-1">LANE</font> device and makes the decision if a packet should be forwarded using <font SIZE="-1">LANE</font> or <font SIZE="-1">MPOA</font> shortcuts. </p>
<p> If the daemon is killed with <code>SIGHUP</code> it will close all the open connections, purge ingress and egress cache entries, query <font SIZE="-1">LECS</font> if applicable and then restart itself. </p>
<p> Linux MPOA client only supports non-LLC-muxed shortcuts. The number of supported MPOA clients is unlimited.</p>
<h2>Options</h2>
<dl>
<dt>-s Control ATM address</p>
<dd>Local ATM address this MPC uses for MPOA control connections.</p>
<dt>-l Data ATM address</p>
<dd>Local ATM address from and to which MPOA shortcuts are established.</p>
<dt>-c MPS control ATM address</p>
<dd>ATM address of MPS. Only needed if MPS can not advertise it by itself.</p>
<dt>-i Interface number</p>
<dd>The interface number of LEC this MPC serves. E.g. 2 for &quot;lec2&quot;.</p>
<dt>-m MPS MAC address</p>
<dd>MAC address of default router where MPS recides. Only useful if the MPOA server fails to advertise itself.</p>
<dt>-L LEC address</p>
<dd>Listen address of the <font SIZE="-1">LANE</font> client zeppelin. mpcd uses this address as its own <font SIZE="-1">ATM</font> address when it queries <font SIZE="-1">LECS</font> for <font SIZE="-1">MPC</font> configuration parameters. If this option is not present then mpcd <code>will not</code> use <font SIZE="-1">LECS</font> to query for configuration parameters. This option is normally the same as zeppelin&#8217;s -l option.</p>
<dt>-n ELAN name</p>
<dd>Name of the <font SIZE="-1">ELAN</font> for which mpcd asks for parameters when it connects to <font SIZE="-1">LECS.</font> If this option is not given, <font SIZE="-1">LECS</font> should respond with parameters belonging to the default <font SIZE="-1">ELAN</font> if one exists. This option is normally the same as zeppelin&#8217;s -n option.</p>
<dt>-C LECS address</p>
<dd>ATM address of <font SIZE="-1">LECS</font> mpcd asks for parameters. If this option is left empty and -L is given, mpcd uses ATM Forum assigned Well-Known <font SIZE="-1">LECS</font> address. This option is normally the same as zeppelin&#8217;s -c option.</dl>
<h2>Examples</h2>
<p>This script snippet shows how to run LANE and MPOA. After UNI signalling and ILMI have been started LANE (zeppelin) and MPOA (mpcd) are started. The commented out line shows how to start mpcd so that it queries <font SIZE="-1">LECS</font> for <font SIZE="-1">MPC</font> parameters. </p>
<p> Arguments jaarli[1-3] are local ATM addresses listed in file <i>/etc/hosts.atm.</i> </p>
<p> ATM=/usr/src/atm<br />
 case &quot;$1&quot; in<br />
 start)<br />
&nbsp;<wbr>cd&nbsp;<wbr>$ATM<br />
&nbsp;<wbr>if&nbsp;<wbr>[&nbsp;<wbr>-x sigd/atmsigd&nbsp;<wbr>]&nbsp;<wbr>;&nbsp;<wbr>then</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>sigd/atmsigd -b&nbsp;<wbr></dl>
<p>&nbsp;<wbr>fi<br />
&nbsp;<wbr>if&nbsp;<wbr>[&nbsp;<wbr>-x ilmid/ilmid&nbsp;<wbr>]&nbsp;<wbr>;&nbsp;<wbr>then</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>ilmid/ilmid -b -x</dl>
<p>&nbsp;<wbr>fi<br />
&nbsp;<wbr>if&nbsp;<wbr>[&nbsp;<wbr>-x led/zeppelin&nbsp;<wbr>]&nbsp;<wbr>;&nbsp;<wbr>then</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>led/zeppelin -2 -n sampo -i2 -l jaarli3&nbsp;<wbr>&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>ifconfig lec2 10.10.10.208&nbsp;<wbr>\</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>netmask 255.255.255.192&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>broadcast 10.10.10.255</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>ifconfig lec2 up<br />
&nbsp;<wbr>&nbsp;<wbr>route add default gw 10.10.10.193</dl>
<p>&nbsp;<wbr>fi<br />
&nbsp;<wbr>if&nbsp;<wbr>[&nbsp;<wbr>-x mpoad/mpcd&nbsp;<wbr>]&nbsp;<wbr>;&nbsp;<wbr>then</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>mpoad/mpcd -i2 -s jaarli1 -l jaarli2&nbsp;<wbr>&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>#mpoad/mpcd -i2 -s jaarli1 -l jaarli2&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-L jaarli3 -n sampo&nbsp;<wbr>&amp;&nbsp;<wbr></dl>
<p>&nbsp;<wbr>fi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>;;<br />
 esac<br />
 exit 0</p>
<h2>Bugs</h2>
<p>Supports only Ethernet type of ELANs. Probably others too.</p>
<h2>Authors</h2>
<p>Heikki Vatiainen &lt;hessu [at] cs.tut.fi&gt;, Sampo Saaristo &lt;s156953 [at] cs.tut.fi&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-zeppelin/">zeppelin</a>(8),</code> <code><a href="/docs/linux/man/8-atmsigd/">atmsigd</a>(8)</code> </p>
