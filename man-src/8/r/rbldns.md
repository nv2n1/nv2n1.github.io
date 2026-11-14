---
title: "rbldns(8)"
name: "rbldns"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rbldns/"
description: "rbldns – Real time Block List DNS server."
---

<p><code>rbldns</code> &#8211; Real time Block List DNS server.</p>
<h2>Synopsis</h2>
<p><code>rbldns</code> [<code>OPTIONS</code>] </p>
<h2>Description</h2>
<p><code>rbldns</code> is a Real time Block List DNS server. It accepts iterative DNS queries from clients seeking information about IP addresses. It provides responses showing whether the addresses are listed on the locally configured Real time Block List(RBL) or Dialup Users List(DUL). When invoked, <code>rbldns</code> reads from the configuration file and listens on UDP port 53 for the incoming requests. When the request is received, <code>rbldns</code> answers it by looking in the data.cdb file placed under the ROOT directory specified in the configuration file. </p>
<h2>Options</h2>
<dl>
<dt><code>-d &lt;value&gt;</code></p>
<dd>&nbsp;<wbr>print debug messages as per the debug level, 1, 2 or 3.</p>
<dt><code>-D</code></p>
<dd>&nbsp;<wbr>run as a daemon</p>
<dt><code>-h &#8211;help</code></p>
<dd>&nbsp;<wbr>print this help.</p>
<dt><code>-v &#8211;version</code></p>
<dd>&nbsp;<wbr>print version information. </p>
</dl>
<h2>Files</h2>
<p>&nbsp;<wbr>/etc/ndjbdns/rbldns.conf </p>
<p>&nbsp;<wbr>/var/log/rbldns.log</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>Author</h2>
<p>Prasad J Pandit</p>
