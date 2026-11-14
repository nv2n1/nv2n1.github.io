---
title: "pmgetpmnslocation(3)"
name: "pmgetpmnslocation"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmgetpmnslocation/"
description: "pmGetPMNSLocation – determine the location of the currently used PMNS"
---

<p><code>pmGetPMNSLocation</code> &#8211; determine the location of the currently used PMNS</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmGetPMNSLocation(void); </p>
<p> cc &#8230; -lpcp </code></p>
<h2>Description</h2>
<p>If an application needs to know where the Performance Metrics Name Space (PMNS) is coming from then <code>pmGetPMNSLocation</code> will return whether it is from an archive, <code>PMNS_ARCHIVE</code>, or from a local PMNS file, <code>PMNS_LOCAL</code>, or from a remote pmcd, <code>PMNS_REMOTE</code>. </p>
<p> This information may be useful in determining an appropriate error message depending on the PMNS&#8217; location.</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmtrimnamespace/">pmTrimNameSpace</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOPMNS</code></p>
<dd>If is not possible to determine where the location of the PMNS is. This could be due to problems with the current context or being unable to load a local PMNS. </p>
</dl>
