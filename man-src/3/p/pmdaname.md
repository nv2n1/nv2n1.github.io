---
title: "pmdaname(3)"
name: "pmdaname"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdaname/"
description: "pmdaName – translate a PMID to a set of dynamic performance metric names"
---

<p><code>pmdaName</code> &#8211; translate a PMID to a set of dynamic performance metric names</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaName(pmID </code><i>pmid</i>, char ***<i>nameset</i>, pmdaExt *<i>pmda</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>As part of the Performance Metrics Domain Agent (PMDA) API (see <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)), <code>pmdaName</code> is the generic callback for translating a <i>pmid</i> into one or more dynamic metric names (<i>nameset</i>). </p>
<p> Because implementing dynamic performance metrics requires specific PMDA support, and the facility is an optional component of a PMDA (most PMDAs do <code>not</code> support dynamic performance metrics), <code>pmdaName</code> is a skeleton implementation that returns <code>PM_ERR_NAME</code>. </p>
<p> A PMDA that supports dynamic performance metrics will provide a private callback that replaces <code>pmdaName</code> (by assignment to <i>version.four.name</i> of the <i>pmdaInterface</i> structure) and implements the translation from a <i>pmid</i> to a set of dynamic performance metric names returned via <i>nameset</i>. The behaviour, return values and memory allocation rules for <i>nameset</i> are the same as for <code><a href="/docs/linux/man/3-pmnameall/">pmNameAll</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>pmdaName</code> returns <code>PM_ERR_PMID</code> if the name is not recognized or cannot be translated, otherwise the number of metric names found (most commonly 1).</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_PROTOCOL_4 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3), <code><a href="/docs/linux/man/3-pmdamain/">pmdaMain</a></code>(3), <code><a href="/docs/linux/man/3-pmnameall/">pmNameAll</a></code>(3) and <code><a href="/docs/linux/man/3-pmnameid/">pmNameID</a></code>(3). </p>
