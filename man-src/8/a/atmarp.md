---
title: "atmarp(8)"
name: "atmarp"
section: "8"
letter: "a"
url: "/docs/linux/man/8-atmarp/"
description: "atmarp – administer classical IP over ATM connections"
---

<p>atmarp &#8211; administer classical IP over ATM connections</p>
<h2>Synopsis</h2>
<p><code>atmarp</code> <code>-a</code><br/>
 <code>atmarp</code> <code>-c</code> [[atm]<i>number</i>]<br/>
 <code>atmarp</code> <code>-q</code> <i>ip_addr</i> [<code>qos&nbsp;<wbr></code><i>qos</i>] [<code>sndbuf&nbsp;<wbr></code><i>bytes</i>]<br/>
 <code>atmarp</code> <code>-s</code> <i>ip_addr</i> [<i>itf</i>.]<i>vpi</i>.<i>vci</i> [<code>qos&nbsp;<wbr></code><i>qos</i>] [<code>sndbuf&nbsp;<wbr></code><i>bytes</i>] [<code>temp</code>] [<code>pub</code>] [<code>null</code>]<br/>
 <code>atmarp</code> <code>-s</code> <i>ip_addr</i> <i>atm_addr</i> [<code>qos&nbsp;<wbr></code><i>qos</i>] [<code>sndbuf&nbsp;<wbr></code><i>bytes</i>] [<code>temp</code>] [<code>pub</code>] [<code>arpsrv</code>]<br/>
 <code>atmarp</code> <code>-d</code> <i>ip_addr</i> [<code>arpsrv</code>]<br/>
 <code>atmarp</code> <code>-V</code></p>
<h2>Description</h2>
<p><code>atmarp</code> is used to maintain the ATMARP table of the ATMARP demon. The table can be listed, new PVC and SVC entries can be added, and existing entries can be deleted. In addition to that, <code>atmarp</code> is also used to create new IP over ATM interfaces. </p>
<p> Note that the kernel has its own ATMARP table containing only entries for destinations to which a connection exists. The table of <code>atmarpd</code> can also contain currently unused entries.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></dt>
<dd>list the current ATMARP table.</dd>
<dt><code>-c</code></dt>
<dd>create the specified IP interface. If the interface number is omitted, the operating system assigns the next free number and <code>atmarp</code> prints the resulting interface name (e.g. `atm0&#8242;) on standard output.</dd>
<dt><code>-q</code></dt>
<dd>sets the QOS and the send buffer size to use as the default for all VCs generated for that IP network (<i>ip_addr</i> must be the address of the network).</dd>
<dt><code>-s</code></dt>
<dd>set up a PVC or create an SVC entry. The following options are recognized:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>qos</code>&nbsp;<wbr><i>qos</i></dt>
<dd>uses the specified quality of service (see <a href="/docs/linux/man/7-qos/">qos</a>(7) for the syntax). UBR at link speed is used by default.</dd>
<dt><code>sndbuf</code>&nbsp;<wbr><i>bytes</i></dt>
<dd>tries to set the send buffer to the specified number of bytes. A system default value is used if <code>sndbuf</code> is not specified.</dd>
<dt><code>temp</code></dt>
<dd>does not mark the entry as permanent, i.e. it will time out and then be removed.</dd>
<dt><code>pub</code></dt>
<dd>publishes the entry (only relevant for ATMARP server). ATMARP requests for entries not marked for publishing yield an ATMARP_NAK response.</dd>
<dt><code>null</code></dt>
<dd>uses NULL encapsulation instead of LLC/SNAP encapsulation on the PVC. This option is not available for SVCs, because the LLC/SNAP header is required to identify ATMARP packets. <code>null</code> also implies that the entry is permanent.</dd>
<dt><code>arpsrv</code></dt>
<dd>identifies the entry pointing to the ATMARP server. Note that the node acting as the ATMARP server must have no ATMARP server entry in its ATMARP table.</dd></dl>
</dl>
<dt><code>-d</code></dt>
<dd>delete the specified ARP entry. In order to prevent accidental deletion of the ATMARP server entry, the <code>arpsrv</code> flag must be specified when deleting it.</dd>
<dt><code>-V</code></dt>
<dd>print the version number of <code>atmarp</code> on standard output and exit.</dd></dl>
<h2>Files</h2>
<dl>
<dt><code>/var/run/atmarpd.table</code></dt>
<dd>ATMARP table</dd></dl>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;Werner.Almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-atmarpd/">atmarpd</a>(8), clip(8), <a href="/docs/linux/man/7-qos/">qos</a>(7) </p>
