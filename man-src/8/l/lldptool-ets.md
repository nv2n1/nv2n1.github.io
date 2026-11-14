---
title: "lldptool-ets(8)"
name: "lldptool-ets"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lldptool-ets/"
description: "ETS-{CFG|REC} – Show / manipulate ETS TLV configuration"
---

<p>ETS-{CFG|REC} &#8211; Show / manipulate ETS TLV configuration</p>
<h2>Synopsis</h2>
<p><code>lldptool -t -i ethx -V ETS-CFG</code> &lt;-c<i> </i>CONFIG_ARG<i> </i>&#8230;&gt; </p>
<pre><code>CONFIG_ARG := {

    enableTx | willing | tsa | up2tc | numtcs | tcbw }
</code></pre>
<p> CONFIG_ARG=value<i> </i>&#8230;<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>CONFIG_ARG</i> := <code>enableTx</code> = <code>{yes|no}</code> | <code>willing</code> = <code>{yes|no}</code> | <code>tsa</code> = <code>tc:{ets|strict|vendor},&#8230;</code> | <code>up2tc</code> = <code>priority:tc,&#8230;</code> | <code>tcbw</code> = <code>bw1,bw2,&#8230;</code> &lt;-c<i> </i>CONFIG_ARG<i> </i>&#8230;&gt; CONFIG_ARG=value<i> </i>&#8230;<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>CONFIG_ARG</i> := <code>enableTx</code> = <code>{yes|no}</code> | <code>tsa</code> = <code>tc:{ets|strict|vendor},&#8230;</code> | <code>up2tc</code> = <code>priority:tc,&#8230;</code> | <code>tcbw</code> = <code>bw1,bw2,&#8230;</code> </p>
<h2>Description</h2>
<p>The Enhanced Transmission Selection (ETS) feature has a recommendation TLV and a configuration TLV configured with ETS-REC and ETS-CFG respectively.</p>
<h2>Arguments</h2>
<dl>
<dt><code>enableTx</code></p>
<dd>Enables the ETS TLV to be transmitted</p>
<dt><code>willing</code></p>
<dd>Sets the ETS-CFG willing bit</p>
<dt><code>tsa </code></p>
<dd>Transmission selection algorithm, sets a comma separated list of traffic classes to the corresponding selection algorithm. Valid algorithms include &quot;ets&quot;, &quot;strict&quot; and &quot;vendor&quot;. </p>
<dt><code>up2tc</code></p>
<dd>Comma separated list mapping user priorities to traffic classes. </p>
<dt><code>tcbw</code></p>
<dd>Comma separated list of bandwidths for each traffic class the first value being assigned to traffic class 0 and the second to traffic class 1 and so on. Undefined bandwidths are presumed to be 0. </p>
<dt><code>numtcs</code></p>
<dd>Displays the number of ETS supported traffic classes. </p>
</dl>
<h2>Theory of Operations</h2>
<p>IEEE 802.1Qaz is enabled by default on hardware that supports this mode indicated by support for the DCBNL interface. Kernel config option CONFIG_DCB. The ETS-CFG TLV is advertised by default with the attributes indicated by querying the hardware for its current configuration. A valid configuration is to map all priorities to a single traffic class and use the link strict selection algorithm. This is equivalent to being in a non-DCB enabled mode. </p>
<p> To support legacy DCBX (CIN or CEE) the ETS-CFG and ETS-REC TLVs are disabled if a legacy DCBX TLV is received and no valid IEEE DCBX TLVs are received. The hardware DCBX mode will also be set to the legacy mode and IEEE mode is disabled. This allows switches to be configured and end nodes will then be configured accordingly without any configuration required on the end node. See <i><a href="/docs/linux/man/8-lldpad/">lldpad</a>(8)</i> for more information about the operation of the DCBX selection mechanism. </p>
<p> Mapping applications and protocols to traffic classes is required for ETS to be useful. User space programs can encode the priority of an application with the SO_PRIORITY option. The net_prio cgroup can be used to assign application traffic to specific priorities. See the kernel documentation and <i><a href="/docs/linux/man/8-cgdcbxd/">cgdcbxd</a>(8)</i> for net_prio cgroup information.</p>
<h2>EXAMPLE &amp; USAGE</h2>
<dl>
<dt>Configure willing bit for interface <i>eth2</i></p>
<dd><code>lldptool -T -i eth2 -V ETS-CFG willing=yes</code></p>
<dt>Configure traffic classes for ETS and strict priority on <i>eth2</i></p>
<dd><code>lldptool -T -i eth2 -V ETS-CFG tsa=0:ets,1:ets,2:ets,3:ets,4:strict,5:strict</code></p>
<dt>Configure 1:1 mapping from priority to traffic classes on <i>eth2</i></p>
<dd><code>lldptool -T -i eth2 -V ETS-CFG up2tc=0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7</code></p>
<dt>Display local configured ETS-CFG parameters for tcbw</p>
<dd><code>lldptool -t -i eth2 -V ETS-CFG -c tcbw</code></p>
<dt>Display last transmitted ETS-CFG TLV</p>
<dd><code>lldptool -t -i eth2 -V ETS-CFG</code></p>
<dt>Configure ETS-CFG and ETS-REC for default DCB on <i>eth2</i></p>
<dd><code>lldptool -T -i eth2 -V ETS-CFG tsa=0:ets,1:ets,2:ets,3:ets,4:ets,5:ets,6:ets,7:ets up2tc=0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7 tcbw=12,12,12,12,13,13,13,13</code> </p>
<p> <code>lldptool -T -i eth2 -V ETS-REC tsa=0:ets,1:ets,2:ets,3:ets,4:ets,5:ets,6:ets,7:ets up2tc=0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7 tcbw=12,12,12,12,13,13,13,13</code> </p>
</dl>
<h2>Source</h2>
<dl>
<dt>o</p>
<dd>IEEE 802.1Qaz (<a rel="nofollow" href="http://www.ieee802.org/1/pages/dcbridges.html)">http://www.ieee802.org/1/pages/dcbridges.html)</a> </p>
</dl>
<h2>Notes</h2>
<p>Support for tc-mqprio was added in 2.6.38 on older kernels other mechanisms may need to be used to map applications to traffic classes. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-app/">lldptool-app</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8), <code><a href="/docs/linux/man/8-tc-mqprio/">tc-mqprio</a></code>(8), </p>
<h2>Author</h2>
<p>John Fastabend</p>
