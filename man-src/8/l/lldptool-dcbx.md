---
title: "lldptool-dcbx(8)"
name: "lldptool-dcbx"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lldptool-dcbx/"
description: "DCBX – Show / manipulate DCBX configuration"
---

<p>DCBX &#8211; Show / manipulate DCBX configuration</p>
<h2>Synopsis</h2>
<p><code>lldptool -t -i ethx -V IEEE-DCBX -c [mode]</code> <code>lldptool -T -i ethx -V IEEE-DCBX mode=reset</code> <code>lldptool -t -i ethx -V &lt;CIN-DCBX|CEE-DCBX&gt; -c [enableTx]</code> <code>lldptool -T -i ethx -V &lt;CIN-DCBX|CEE-DCBX&gt; enableTx=&lt;yes|no&gt;</code> </p>
<h2>Description &#8211; Dcbx Mode</h2>
<p><code>lldpad</code> supports the following versions of the DCB capabilities exchange (DCBX) protocol:</p>
<dl>
<dt>CIN DCBX</p>
<dd>&lt;<a rel="nofollow" href="http://download.intel.com/technology/eedc/dcb_cep_spec.pdf">http://download.intel.com/technology/eedc/dcb_cep_spec.pdf</a>&gt;</p>
<dt>CEE DCBX</p>
<dd>&lt;<a rel="nofollow" href="http://www.ieee802.org/1/files/public/docs2008/az-wadekar-dcbx-capability-exchange-discovery-protocol-1108-v1.01.pdf">http://www.ieee802.org/1/files/public/docs2008/az-wadekar-dcbx-capability-exchange-discovery-protocol-1108-v1.01.pdf</a>&gt;</p>
<dt>IEEE DCBX</p>
<dd>See the IEEE 802.1Qaz-2011 specification for details.&quot;</dl>
<p> IEEE DCBX is the default DCBX mode for a DCB capable interface. Therefore the default and configured IEEE DCBX TLVs will be transmitted when the interface comes up. <code>lldpad</code> can be globally configured to support one of the legacy DCBX versions (CIN or CEE). If the remote LLDP agent does not transmit any IEEE DCBX TLVs and does transmit a legacy DCBX TLV which matches the configured legacy DCBX version, then the DCBX mode will drop back to legacy DCBX mode. It will not transition back to IEEE DCBX mode until the next link reset. If <code>lldpad</code> has dropped back to legacy DCBX mode for a given interface and the daemon is stopped and restarted, the legacy DCBX mode for that interface will be used instead of starting out in IEEE DCBX mode. This behavior only applies to the case where <code>lldpad</code> is restarted and is not persistent across a system reboot. </p>
<p> The DCBX mode can be queried and configured by using the special tlvid <code>IEEE-DCBX.</code> There is not an actual TLV which corresponds to this tlvid. Its use is to query and reset the IEEE DCBX mode. When queried, IEEE DCBX mode can take the following values: </p>
<p> <code>auto</code> &#8211; IEEE DCBX will be used (initially) if lldpad is restarted. An exception is if the DCBX mode has been forced to a legacy DCBX mode, then the specified legacy mode will be used. See information about the &#8216;dcbx&#8217; parameter in <a href="/docs/linux/man/8-dcbtool/">dcbtool</a>(8) for more information about this exception.&quot; </p>
<p> <code>CEE</code> &#8211; CEE DCBX will be used if lldpad is restarted </p>
<p> <code>CIN</code> &#8211; CIN DCBX will be used if lldpad is restarted </p>
<p> The IEEE DCBX mode can be reset to <code>auto</code> by setting the <code>mode</code> argument to the value <code>reset</code></p>
<h2>Description &#8211; Dcbx Configuration</h2>
<p>The detailed configuration of the IEEE DCBX TLVs can be found in related lldptool man pages for each IEEE DCBX TLV (see <a href="/docs/linux/man/8-lldptool-pfc/">lldptool-pfc</a>(8), <a href="/docs/linux/man/8-lldptool-ets/">lldptool-ets</a>(8) and <a href="/docs/linux/man/8-lldptool-app/">lldptool-app</a>(8)). </p>
<p> The detailed configuration of the CIN and CEE DCBX TLVs is performed using dcbtool (see <a href="/docs/linux/man/8-dcbtool/">dcbtool</a>(8)). However, lldptool can configure the enableTx parameter of the CIN and CEE DCBX TLVs (as it can with most other TLVs). Since lldpad only transmits TLVs for one version of DCBX on any given interface, the enableTx parameter for the CIN and CEE DCBX TLVs (and for the IEEE DCBX feature TLVs) takes effect only when the corresponding DCBX version is active.</p>
<h2>Arguments</h2>
<dl>
<dt><code>mode=reset</code></p>
<dd>Reset the DCBX mode that will be used if lldpad is restarted by setting the mode argument to reset using the special tlvid IEEE-DCBX.</p>
<dt><code>enableTx</code></p>
<dd>Enable the specified DCBX TLV (CIN-DCBX or CEE-DCBX) to be transmitted in the LLDPDU if that DCBX mode for the specified interface has been selected. </p>
</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<dl>
<dt>Query the current DCBX mode that will be used if lldpad is restarted. (this is not a persistent setting)</p>
<dd><code>lldptool -t -i eth3 -V IEEE-DCBX -c mode</code> </p>
<dt>Reset the DCBX mode to be &#8216;auto&#8217; (start in IEEE DCBX mode) after the next lldpad restart</p>
<dd><code>lldptool -T -i eth3 -V IEEE-DCBX mode=reset</code> </p>
<dt>Enable transmission of the CEE DCBX TLV</p>
<dd><code>lldptool -T -i eth3 -V CEE-DCBX enableTx=yes</code> </p>
<dt>Disable transmission of the CIN DCBX TLV</p>
<dd><code>lldptool -T -i eth3 -V CIN-DCBX enableTx=no</code> </p>
<dt>Query the configuration of enableTx for the CEE DCBX TLV</p>
<dd><code>lldptool -t -i eth3 -V CEE-DCBX -c enableTx</code> </p>
</dl>
<h2>Notes</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dcbtool/">dcbtool</a></code>(8), <code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-ets/">lldptool-ets</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-pfc/">lldptool-pfc</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-app/">lldptool-app</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) </p>
<h2>Author</h2>
<p>Eric Multanen</p>
