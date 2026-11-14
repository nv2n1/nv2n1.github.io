---
title: "pmdapmid(3)"
name: "pmdapmid"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdapmid/"
description: "pmdaPMID – translate a dynamic performance metric name into a PMID"
---

<p><code>pmdaPMID</code> &#8211; translate a dynamic performance metric name into a PMID</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaPMID(char *</code><i>name</i>, pmID *<i>pmid</i>, pmdaExt *<i>pmda</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>As part of the Performance Metrics Domain Agent (PMDA) API (see <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)), <code>pmdaPMID</code> is the generic callback for translating a dynamic metric <i>name</i> into a PMID (<i>pmid</i>). </p>
<p> Because implementing dynamic performance metrics requires specific PMDA support, and the facility is an optional component of a PMDA (most PMDAs do <code>not</code> support dynamic performance metrics), <code>pmdaPMID</code> is a skeleton implementation that returns <code>PM_ERR_NAME</code>. </p>
<p> A PMDA that supports dynamic performance metrics will provide a private callback that replaces <code>pmdaPMID</code> (by assignment to <i>version.four.pmid</i> of the <i>pmdaInterface</i> structure) and implements the translation from a dynamic performance metric <i>name</i> into the associated <i>pmid</i>.</p>
<h2>Diagnostics</h2>
<p><code>pmdaPMID</code> returns <code>PM_ERR_NAME</code> if the name is not recognized or cannot be translated, else returns 0.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_PROTOCOL_4 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3), <code><a href="/docs/linux/man/3-pmdamain/">pmdaMain</a></code>(3) and <code><a href="/docs/linux/man/3-pmlookupname/">pmLookupName</a></code>(3). </p>
