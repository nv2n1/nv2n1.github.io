---
title: "pmtrimnamespace(3)"
name: "pmtrimnamespace"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmtrimnamespace/"
description: "pmTrimNameSpace – prune a performance metrics name space"
---

<p><code>pmTrimNameSpace</code> &#8211; prune a performance metrics name space</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmTrimNameSpace(void); </p>
<p> cc &#8230; -lpcp </code></p>
<h2>Description</h2>
<p>In some (rare) cases it is helpful to prune the Performance Metrics Name Space (PMNS) to match the available metrics. </p>
<p> The default PMNS that is accessible to a Performance Metrics Application Programming Interface (PMAPI) client is provided by the current PMAPI context:</p>
<dl>
<dt>&bull;</p>
<dd>for a PMAPI context of type <code>PM_CONTEXT_HOST</code> the PMNS is provided by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on the associated host and no pruning is required</p>
<dt>&bull;</p>
<dd>for a PMAPI context of type <code>PM_CONTEXT_ARCHIVE</code> the PMNS is stored within the associated Performance Co-Pilot (PCP) archive log and no pruning is required</p>
<dt>&bull;</p>
<dd>for a PMAPI context of type <code>PM_CONTEXT_LOCAL</code> at the first PMAPI call requiring access to the PMNS it is loaded from the default local location <code>$PCP_VAR_DIR/pmns/root</code> (or <code>$PMNS_DEFAULT</code>) and no pruning is required.</dl>
<p> If the default PMNS is in effect then calling <code>pmTrimNameSpace</code> is a no-op and returns zero with no change to the PMNS. </p>
<p> PMAPI clients also have the option of over-riding the default PMNS by loading a <i>local</i> PMNS from a file (see <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5) for the format) by calling <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3) or <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3) and this is when some PMNS pruning <i>may</i> be useful. </p>
<p> If a <i>local</i> PMNS is in effect when <code>pmTrimNameSpace</code> is called then the first action is to restore the PMNS to the state as of the completion of the last <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3) or <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3), so that the effects of consecutive calls to <code>pmTrimNameSpace</code> are <code>not</code> additive. </p>
<p> The subsequent actions of <code>pmTrimNameSpace</code> depend on the type of the current PMAPI context.</p>
<dl>
<dt>&bull;</p>
<dd>For a context of type <code>PM_CONTEXT_ARCHIVE</code> the <i>local</i> PMNS is trimmed to exclude metrics for which no description can be found in the PCP archive log. The PMNS is further trimmed to remove empty subtrees that do not contain any performance metric. Since PCP archives usually contain some subset of all metrics named in a PMNS, <code>pmTrimNameSpace</code> effectively prunes the application&#8217;s PMNS to contain only the names of the metrics in the archive.</p>
<dt>&bull;</p>
<dd>For a context of type <code>PM_CONTEXT_HOST</code> or <code>PM_CONTEXT_LOCAL</code> no further action is required.</dl>
<p> On success, <code>pmTrimNameSpace</code> returns zero.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_NOPMNS</code></p>
<dd>there has been some earlier problem with establishing the relevant PMNS</p>
<dt><code>PM_ERR_NOCONTEXT</code></p>
<dd>the current PMAPI context is invalid </p>
</dl>
