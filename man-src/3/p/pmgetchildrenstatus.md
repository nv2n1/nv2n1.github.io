---
title: "pmgetchildrenstatus(3)"
name: "pmgetchildrenstatus"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmgetchildrenstatus/"
description: "pmGetChildrenStatus – return the descendent nodes of a PMNS node and their respective status"
---

<p><code>pmGetChildrenStatus</code> &#8211; return the descendent nodes of a PMNS node and their respective status</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmGetChildrenStatus(const char *</code><i>name</i>, char ***<i>offspring</i>, int&nbsp;<wbr>**<i>status</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Given a fully qualified pathname to a node in the current Performance Metrics Name Space (PMNS), as identified by <i>name</i>, <code>pmGetChildrenStatus</code> returns via <i>offspring</i> a list of the relative names of all of the immediate descendent nodes of <i>name</i> in the current PMNS. </p>
<p> As a special case, if <i>name</i> is an empty string (i.e.<code>&quot;&quot;</code>), the immediate descendants of the root node in the PMNS will be returned. </p>
<p> If <i>status</i> is not NULL, then <code>pmGetChildrenStatus</code> will also return the status of each child via <i>status.</i> The status will refer to either a leaf node (with value <code>PMNS_LEAF_STATUS</code> ) or a non-leaf node (with value <code>PMNS_NONLEAF_STATUS</code> ). </p>
<p> Normally, <code>pmGetChildrenStatus</code> will return the number of descendent names discovered, else a value less than zero for an error. The value zero indicates that <i>name</i> is a valid metric name, i.e. is associated with a leaf node in the PMNS. </p>
<p> The resulting list of pointers <i>offspring</i> <code>and</code> the values (the relative names) that the pointers reference will have been allocated by <code>pmGetChildrenStatus</code> with a single call to <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and it is the responsibility of the <code>pmGetChildrenStatus</code> caller to <code>free</code>(<i>offspring</i>) to release the space when it is no longer required. The same holds true for the <i>status</i> array. </p>
<p> When an error occurs, or <i>name </i> is a leaf node (i.e. the result of <code>pmGetChildrenStatus</code> is less than one), both <i>offspring</i> and <i>status</i> are undefined (no space will have been allocated, and so calling <code><a href="/docs/linux/man/3-free/">free</a></code>(3) is a singularly bad idea).</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetchildren/">pmGetChildren</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3), <code><a href="/docs/linux/man/3-pmnameid/">pmNameID</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOPMNS</code></p>
<dd>Failed to access a PMNS for operation. Note that if the application hasn&#8217;t a priori called <a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a>(3) and wants to use the distributed PMNS, then a call to <code>pmGetChildrenStatus</code> must be made inside a current context.</p>
<dt><code>PM_ERR_NAME</code></p>
<dd>The pathname <i>name</i> is not valid in the current PMNS</p>
<dt><code>PM_ERR_*</code></p>
<dd>Other diagnostics are for protocol failures when accessing the distributed PMNS. </p>
</dl>
