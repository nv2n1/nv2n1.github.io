---
title: "xl2tpd(5)"
name: "xl2tpd"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xl2tpd/"
description: "xl2tpd.conf – L2TPD configuration file"
---

<p>xl2tpd.conf &#8211; L2TPD configuration file</p>
<h2>Description</h2>
<p>The xl2tpd.conf file contains configuration information for xl2tpd, the implementation of l2tp protocol. </p>
<p> The configuration file is composed of sections and parameters. Each section has a given name which will be used when using the configuration FIFO (normaly /var/run/l2tp-control). See xl2tpd.8 for more details. </p>
<p> The specific given name <code>default</code> will specify parameters applicables for all the following sections.</p>
<h2>Global Section</h2>
<dl>
<dt><code>auth file</code></p>
<dd>Specify where to find the authentication file used to authenticate l2tp tunnels. The default is /etc/l2tpd/l2tp-secrets. </p>
<dt><code>ipsec saref</code></p>
<dd>Use IPsec Security Association trackinng. When this is enabled, packets received by xl2tpd should have to extra fields (refme and refhim) which allows tracking of multiple clients using the same internal NATed IP address, and allows tracking of multiple clients behind the same NAT router. This neds to be supported by the kernel. Currently, this only works with Openswan KLIPS in &quot;mast&quot; mode. (see <a rel="nofollow" href="http://www.openswan.org/)">http://www.openswan.org/)</a> </p>
<p> Set this to yes and the system will provide proper SAref values in the recvmsg() calls. </p>
<p> Values can be yes or no. The default is no. </p>
<dt><code>saref refinfo</code></p>
<dd>When using IPsec Security Association trackinng, a new setsockopt is used. Since this is not (yet?) an official Linux kernel option, we got bumped. Openswan upto 2.6.35 for linux kernels up to 2.6.35 used a saref num of 22. Linux 3.6.36+ uses 22 for IP_NODEFRAG. We moved our IP_IPSEC_REFINFO to 30. If not set, the default is to use 30. For older SAref patched kernels, use 22. </p>
<dt><code>listen-addr</code></p>
<dd>The IP address of the interface on which the daemon listens. By default, it listens on INADDR_ANY (0.0.0.0), meaning it listens on all interfaces. </p>
<dt><code>port</code></p>
<dd>Specify which UDP port xl2tpd should use. The default is 1701. </p>
<dt><code>access control</code></p>
<dd>If set to yes, the xl2tpd process will only accept connections from peers addresses specified in the following sections. The default is no. </p>
<dt><code>debug avp</code></p>
<dd>Set this to yes to enable syslog output of L2TP AVP debugging information. </p>
<dt><code>debug network</code></p>
<dd>Set this to yes to enable syslog output of network debugging information. </p>
<dt><code>debug packet</code></p>
<dd>Set this to yes to enable printing of L2TP packet debugging information. Note: Output goes to STDOUT, so use this only in conjunction with the <code>-D</code> command line option. </p>
<dt><code>debug state</code></p>
<dd>Set this to yes to enable syslog output of FSM debugging information. </p>
<dt><code>debug tunnel</code></p>
<dd>Set this to yes to enable syslog output of tunnel debugging information. </p>
</dl>
<h2>Lns Section</h2>
<dl>
<dt><code>exclusive</code></p>
<dd>If set to yes, only one control tunnel will be allowed to be built between 2 peers. CHECK </p>
<dt><code>(no) ip range</code></p>
<dd>Specify the range of ip addresses the LNS will assign to the connecting LAC PPP tunnels. Multiple ranges can be defined. Using the &#8216;no&#8217; statement disallows the use of that particular range. Ranges are defined using the format IP &#8211; IP (example: 1.1.1.1 &#8211; 1.1.1.10). Note that either at least one <code>ip range</code> option must be given, or you must set <code>assign ip</code> to no. </p>
<dt><code>assign ip</code></p>
<dd>Set this to no if xl2tpd should not assign IP addresses out of the pool defined with the <code>ip range </code> option. This can be useful if you have some other means to assign IP addresses, e. g. a pppd that supports RADIUS AAA. </p>
<dt><code>(no) lac</code></p>
<dd>Specify the ip addresses of LAC&#8217;s which are allowed to connect to xl2tpd acting as a LNS. The format is the same as the <code>ip range </code> option. </p>
<dt><code>hidden bit</code></p>
<dd>If set to yes, xl2tpd will use the AVP hiding feature of L2TP. To get more information about hidden AVP&#8217;s and AVP in general, refer to rfc2661 (add URL?) </p>
<dt><code>local ip</code></p>
<dd>Use the following IP as xl2tpd&#8217;s own ip address. </p>
<dt><code>length bit</code></p>
<dd>If set to yes, the length bit present in the l2tp packet payload will be used. </p>
<dt><code>(refuse | require) chap</code></p>
<dd>Will require or refuse the remote peer to get authenticated via CHAP for the ppp authentication. </p>
<dt><code>(refuse | require) pap</code></p>
<dd>Will require or refuse the remote peer to get authenticated via PAP for the ppp authentication. </p>
<dt><code>(refuse | require) authentication</code></p>
<dd>Will require or refuse the remote peer to authenticate itself. </p>
<dt><code>unix authentication</code></p>
<dd>If set to yes, /etc/passwd will be used for remote peer ppp authentication. </p>
<dt><code>hostname</code></p>
<dd>Will report this as the xl2tpd hostname in negociation. </p>
<dt><code>ppp debug</code></p>
<dd>This will enable the debug for pppd. </p>
<dt><code>pass peer</code></p>
<dd>Pass the peer&#8217;s IP address to pppd as ipparam. Enabled by default. </p>
<dt><code>pppoptfile</code></p>
<dd>Specify the path for a file which contains pppd configuration parameters to be used. </p>
<dt><code>call rws</code></p>
<dd>This option is deprecated and no longer functions. It used to be used to define the flow control window size for individual L2TP calls or sessions. The L2TP standard (RFC2661) no longer defines flow control or window sizes on calls or sessions. </p>
<dt><code>tunnel rws</code></p>
<dd>This defines the window size of the control channel. The window size is defined as the number of outstanding unacknowledged packets, not as a number of bytes. </p>
<dt><code>flow bits</code></p>
<dd>If set to yes, sequence numbers will be included in the communication. The feature to use sequence numbers in sessions is currently broken and does not function. </p>
<dt><code>challenge</code></p>
<dd>If set to yes, use challenge authentication to authenticate peer. </p>
<dt><code>rx bps</code></p>
<dd>If set, the receive bandwidth maximum will be set to this value </p>
<dt><code>tx bps</code></p>
<dd>If set, the transmit bandwidth maximum will be set to this value </p>
</dl>
<h2>Lac Section</h2>
<p>The following are LAC specific configuration flags. Most of those described in the LNS section may be used in a LAC context, where it make common sense (essentially l2tp procotols tuning flags and authentication / ppp related ones). </p>
<dl>
<dt><code>lns</code></p>
<dd>Set the dns name or ip address of the LNS to connect to. </p>
<dt><code>redial</code></p>
<dd>If set to yes, xl2tpd will attempts to redial if the call get disconected. Note that, if enabled, xl2tpd will keep passwords in memory: a potental security risk. </p>
<dt><code>redial timeout</code></p>
<dd>Wait X seconds before redial. The redial option must be set to yes to use this option. Defaults to 30 seconds. </p>
<dt><code>max redial </code></p>
<dd>Will give up redial tries after X attempts. </p>
</dl>
<h2>Files</h2>
<p>/etc/xl2tpd/xl2tpd.conf /etc/xl2tpd/l2tp-secrets /var/run/xl2tpd/l2tp-control</p>
<h2>Bugs</h2>
<p>Please address bugs and comment to xl2tpdv [at] lists.xelerance.com</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-xl2tpd/">xl2tpd</a>(8)</p>
<h2>Authors</h2>
<p>Forked from xl2tpd by Xelerance (<a rel="nofollow" href="http://www.xelerance.com/software/xl2tpd/">http://www.xelerance.com/software/xl2tpd/</a> </p>
<p> Michael Richardson &lt;mcr [at] xelerance.com&gt; Paul Wouters &lt;paul [at] xelerance.com&gt; </p>
<p> Many thanks to Jacco de Leeuw &lt;jacco2 [at] dds.nl&gt; for maintaining l2tpd. </p>
<p> Previous development was hosted at sourceforge (<a rel="nofollow" href="http://www.sourceforge.net/projects/l2tpd)">http://www.sourceforge.net/projects/l2tpd)</a> by: </p>
<p> Scott Balmos &lt;sbalmos [at] iglou.com&gt;<br />
 David Stipp &lt;dstipp [at] one.net&gt;<br />
 Jeff McAdams &lt;jeffm [at] iglou.com&gt; </p>
<p> Based off of l2tpd version 0.60<br />
 Copyright (C)1998 Adtran, Inc.<br />
 Mark Spencer &lt;markster [at] marko.net&gt;</p>
