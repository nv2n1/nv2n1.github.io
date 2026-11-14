---
title: "pmloadnamespace(3)"
name: "pmloadnamespace"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmloadnamespace/"
description: "pmLoadNameSpace – load a local PMNS for an application"
---

<p><code>pmLoadNameSpace</code> &#8211; load a local PMNS for an application</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmLoadNameSpace(const char *</code><i>filename</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>If the application wants to force using a local Performance Metrics Name Space (PMNS) instead of a distributed PMNS then it must load the PMNS using <code>pmLoadNameSpace</code> or <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3). If the application is to use a distributed PMNS, then it should NOT make a call to load the PMNS explicitly. </p>
<p> Most applications using a Performance Metrics Application Programming Interface (PMAPI) context (of any type, so PM_CONTEXT_HOST or PM_CONTEXT_ARCHIVE or PM_CONTEXT_LOCAL) should not need to call <code>pmLoadNameSpace</code>. </p>
<p> The <i>filename</i> argument designates the PMNS of interest. For applications not requiring a tailored PMNS, the special value <code>PM_NS_DEFAULT</code> may be used for <i>filename</i>, to force the default local PMNS to be loaded. </p>
<p> The default local PMNS is found in the file <i>$PCP_VAR_DIR/pmns/root</i> unless the environment variable <code>PMNS_DEFAULT</code> is set, in which case the value is assumed to be the pathname to the file containing the default local PMNS. </p>
<p> Externally a PMNS is stored in an ASCII format as described in <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). However, note that <code>pmLoadNameSpace</code> assumes <i>filename</i> does not contain any C-style comments, pre-processor directives or macros; if this is not the case, <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3) should be used instead. </p>
<p> As of Version 3.10.3 of PCP, by default, multiple names in the PMNS <code>are</code> allowed to be associated with a single Performance Metrics Identifier (PMID) and this is unconditionally allowed by <code>pmLoadNameSpace</code>. <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3) provides an alternative interface with user-defined control over the handling of duplicate names for the same PMID in the PMNS. </p>
<p> <code>pmLoadNameSpace</code> returns zero on success.</p>
<h2>Files</h2>
<dl>
<dt><i>$PCP_VAR_DIR/pmns/root</i></p>
<dd>the default local PMNS, when the environment variable <code>PMNS_DEFAULT</code> is unset</dl>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <i><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></i>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmtrimnamespace/">pmTrimNameSpace</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5).</p>
<h2>Diagnostics</h2>
<p>Syntax and other errors in the parsing of the PMNS are reported on <i>stderr</i> with a message of the form &#8220;Error Parsing ASCII PMNS: &#8230;&#8221;. </p>
<p> <code>PM_ERR_DUPPMNS</code></p>
<dl>
<dd>It is an error to try and load more than one PMNS, or to call either <code>pmLoadNameSpace</code> and/or <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3) more than once.</dl>
<p> <code>PM_ERR_PMNS</code></p>
<dl>
<dd>Syntax error in the PMNS file. </p>
</dl>
