---
title: "cgdcbxd(8)"
name: "cgdcbxd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cgdcbxd/"
description: "cgdcbxd – control group dcb event net_prio daemon"
---

<p>cgdcbxd &#8211; control group dcb event net_prio daemon </p>
<h2>Synopsis</h2>
<p><code>cgdcbxd</code> [options] </p>
<h2>Description</h2>
<p><code>cgdcbxd</code> is a daemon used to monitor DCB netlink events and manage the net_prio control group subsystem. The daemon keeps the hierarchy and priority mappings in sync with DCBX Application events. When a DCB netlink event is received <code>cgdcbxd</code> parses the application TLV and identifies new, updated, and deleted application tuples. The DCBX application TLV uses the selector, protocol ID and priority fields to identify and set application priority. The <code>selector</code> field specifies the protocol ID type supported types are <code>Ethertype =</code> 1 <code>TCP or SCTP =</code> 2 <code>UDP or DCCP =</code> 3 <code>TCP, SCTP UDP, and DCCP =</code> 4 The <code>protocol ID</code> field specifies the port or ethertype depending on the selector field and the <code>priority</code> gives a priority value (0-7). Used to set the net_prio.ifpriomap. When a new application tuple is identified <code>cgdcbxd</code> creates a control group under the net_prio subsystem using the directory <code>cgdcbx-&lt;selector&gt;-&lt;protocolID&gt;</code>. The <code>&lt;selector&gt;</code> field uses the IEEE selector values listed above for both CEE DCBX and IEEE DCBX versions. This control group will be managed by <code>cgdcbx</code> and the <code>ifpriomap</code> will be kept in sync with the application TLV. If a DCB netlink event removes the application selector-protocolID tuple then <code>cgdcbx</code> removes the control group. This may be used with <code>cgrulesengd</code> to create configuration rules that map applications and users to DCBX selector-protocolID tuples. Note protocol ID and selector values use the well-known protocol type and port or ethertype defined by the IANA (Internet Assigned Numbers Authority) the application are not required to use the well-known ports this is only used to identify the application. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Display help.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t fork the daemon, stay in the foreground.</p>
<dt><code>-v</code></p>
<dd>Show version</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/cgrules.conf</code></p>
<dd>
<dt>the default libcgroup configuration file</p>
<dd></dl>
<h2>Sources</h2>
<dl>
<dt>o</p>
<dd>IEEE 802.1Qaz (<a rel="nofollow" href="http://www.ieee802.org/1/pages/dcbridges.html)">http://www.ieee802.org/1/pages/dcbridges.html)</a> o IANA (<a rel="nofollow" href="http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml)">http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml)</a> </p>
</dl>
<h2>Notes</h2>
<p>Support for the net_prio subsystem was added in the 3.3 Linux kernel. </p>
<h2>Signals</h2>
<p><code>SIGUSR1</code> dumps list of managed interfaces and control groups with priomaps.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cgrulesengd/">cgrulesengd</a></code>(8), <code><a href="/docs/linux/man/5-cgrules-conf/">cgrules.conf</a></code>(5) <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8), <code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), </p>
<h2>Author</h2>
<p>John Fastabend &lt;john.r.fastabend [at] intel.com&gt;</p>
