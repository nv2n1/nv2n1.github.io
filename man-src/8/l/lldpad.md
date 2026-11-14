---
title: "lldpad(8)"
name: "lldpad"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lldpad/"
description: "lldpad – Link Layer Discovery Protocol (LLDP) agent daemon"
---

<p>lldpad &#8211; Link Layer Discovery Protocol (LLDP) agent daemon</p>
<h2>Synopsis</h2>
<p><code>lldpad [-h]</code> <code>[-v]</code> <code>[-V</code><i> level</i><code>]</code> <code>[-d]</code> <code>[-k]</code> <code>[-p]</code> <code>[-s]</code> <code>[-t]</code> <code>[-f</code><i> filename</i><code>]</code></p>
<h2>Description</h2>
<p>Executes the LLDP protocol for supported network interfaces. The list of TLVs currently supported are:</p>
<dl>
<dt>&#8211;</p>
<dd>IEEE 802.1AB Mandatory TLVs</p>
<dt>&#8211;</p>
<dd>IEEE 802.1AB Basic Management TLVs</p>
<dt>&#8211;</p>
<dd>IEEE 802.3 Organizationally Specific TLVs</p>
<dt>&#8211;</p>
<dd>LLDP-MED Organizationally Specific TLVs</p>
<dt>&#8211;</p>
<dd>Data Center Bridging capabilities exchange protocol (DCBX) TLVs</p>
<dt>&#8211;</p>
<dd>Edge Virtual Bridging (EVB) TLVs
</dl>
<p> Capabilities of <code>lldpad</code> include:</p>
<dl>
<dt>&#8211;</p>
<dd>Transmission of LLDP PDUs containing enabled TLVs from enabled ports.</p>
<dt>&#8211;</p>
<dd>Reception of LLDP PDUs from enabled ports.</p>
<dt>&#8211;</p>
<dd>Operation of the DCBX protocol for interfaces which support the DCB rtnetlink interface. This includes operation of the DCBX state machines above LLDP and corresponding configuration of the DCB parameters of the network interface. Supported DCB features are: Extended Transmission Selection, Priority Flow Control and the FCoE application.</p>
<dt>&#8211;</p>
<dd>Configuring the DCB settings of the network driver based on the operation of DCBX.</p>
<dt>&#8211;</p>
<dd>Provides a multi-channel interface for client applications to query and configure features. Events are also generated on the client interface to inform clients of changes. The lldpad package includes two clients: lldptool for general LLDP agent management and dcbtool for DCB management.</dl>
<p> <code>lldpad</code> supports the versions of the DCB capabilities exchange (DCBX) protocol listed as follows:</p>
<dl>
<dt>version 1 &#8211; also known as CIN DCBX</p>
<dd>&lt;<a rel="nofollow" href="http://download.intel.com/technology/eedc/dcb_cep_spec.pdf">http://download.intel.com/technology/eedc/dcb_cep_spec.pdf</a>&gt;</dl>
<dl>
<dt>version 2 &#8211; also known as CEE DCBX</p>
<dd>&lt;<a rel="nofollow" href="http://www.ieee802.org/1/files/public/docs2008/az-wadekar-dcbx-capability-exchange-discovery-protocol-1108-v1.01.pdf">http://www.ieee802.org/1/files/public/docs2008/az-wadekar-dcbx-capability-exchange-discovery-protocol-1108-v1.01.pdf</a>&gt;</dl>
<dl>
<dt>IEEE DCBX</p>
<dd>See the IEEE 802.1Qaz-2011 specification for details.</dl>
<p> IEEE DCBX is the default DCBX mode for a DCB capable interface so the default and configured IEEE DCBX TLVs will be transmitted when the interface comes up. <code>lldpad</code> can be globally configured to support one of the legacy DCBX versions (CIN or CEE). If the remote LLDP agent does not transmit any IEEE DCBX TLVs and does transmit a legacy DCBX TLV which matches the configured legacy DCBX version, then the DCBX mode will drop back to legacy DCBX mode. It will not transition back to IEEE DCBX mode until the next link reset. If <code>lldpad</code> has dropped back to legacy DCBX mode for a given interface and the daemon is stopped and restarted, the legacy DCBX mode for that interface will be used instead of starting out in IEEE DCBX mode. This behavior only applies to the case where <code>lldpad</code> is restarted and is not persistent across a system reboot. See <code>dcbtool</code> for information on how to globally configure which legacy version of DCBX <code>lldpad</code> executes. See <code>lldptool</code> for information on how to reset the DCBX mode of an interface back to default (starts out in IEEE DCBX mode). <code>lldpad</code> also supports edge virtual bridging as currently under specification in the IEEE 802.1Qb working group. &lt;<a rel="nofollow" href="http://www.ieee802.org/1/pages/802.1bg.html">http://www.ieee802.org/1/pages/802.1bg.html</a>&gt; </p>
<h2>Options</h2>
<p><code>lldpad</code> has the following command line options:</p>
<dl>
<dt><code>-h</code></p>
<dd>show usage information</p>
<dt><code>-f</code><i> filename</i></p>
<dd>use the specified file as the configuration file instead of the default file: /var/lib/lldpad/lldpad.conf <code>lldpad</code> expects the directory of the configuration file to exist, but if the configuration file does not exist, then a default configuration file will be created. lldpad creates and maintains the contents of the configuration file. Configuration should be performed by using lldptool or dcbtool.</p>
<dt><code>-d</code></p>
<dd>run lldpad as a daemon</p>
<dt><code>-v</code></p>
<dd>show lldpad version</p>
<dt><code>-V</code><i> level</i></p>
<dd>set lldpad debugging level. Uses syslog debug levels see syslog.2 for details.</p>
<dt><code>-k</code></p>
<dd>used to terminate the first instance of lldpad that was started (e.g. from initrd). Once lldpad -k has been invoked and lldpad has been restarted, subsequent invocations of lldpad -k will not terminate lldpad. </p>
<dt><code>-s</code></p>
<dd>remove lldpad state records from shared memory</p>
<dt><code>-p</code></p>
<dd>do not create PID file /var/run/lldpad.pid on startup</p>
<dt><code>-t</code></p>
<dd>omit timestamps from logging messages</dl>
<h2>Note</h2>
<p>On termination, lldpad does not undo any of the configurations that it has set. This approach minimizes the risk of restarting the daemon to perform a software update, or of having storage issues during shutdown. Ongoing operation of network interfaces that had been controlled by lldpad may result in unexpected behavior.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dcbtool/">dcbtool</a></code>(8), <code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-dcbx/">lldptool-dcbx</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-ets/">lldptool-ets</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-pfc/">lldptool-pfc</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-app/">lldptool-app</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-med/">lldptool-med</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-vdp/">lldptool-vdp</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-evb/">lldptool-evb</a></code>(8) </p>
<h2>Copyright</h2>
<p>lldpad &#8211; LLDP agent daemon with DCBX support<br />
 Copyright(c) 2007-2012 Intel Corporation. Portions of lldpad are based on:</p>
<dl>
<dt>hostapd-0.5.7</p>
<dd>
<dt>Copyright</p>
<dd>(c) 2004-2008, Jouni Malinen &lt;j@w1.fi&gt;</dl>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms and conditions of the GNU General Public License, version 2, as published by the Free Software Foundation. </p>
<p> This program is distributed in the hope it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St &#8211; Fifth Floor, Boston, MA 02110-1301 USA. </p>
<p> The full GNU General Public License is included in this distribution in the file called &quot;COPYING&quot;.</p>
<h2>Support</h2>
<p>Contact Information: open-lldp Mailing List &lt;lldp-devel [at] open-lldp.org&gt;</p>
