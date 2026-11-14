---
title: "pmdachildren(3)"
name: "pmdachildren"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdachildren/"
description: "pmdaChildren – translate a PMID to a set of dynamic performance metric names"
---

<p><code>pmdaChildren</code> &#8211; translate a PMID to a set of dynamic performance metric names</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaChildren(char *</code><i>name</i>, int <i>traverse</i>, char&nbsp;<wbr>***<i>offspring</i>, int&nbsp;<wbr>**<i>status</i>, pmdaExt&nbsp;<wbr>*<i>pmda</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>As part of the Performance Metrics Domain Agent (PMDA) API (see <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)), <code>pmdaChildren</code> is the generic callback for returning dynamic metric names (and their status) that are descendants of <i>name</i>. </p>
<p> Because implementing dynamic performance metrics requires specific PMDA support, and the facility is an optional component of a PMDA (most PMDAs do <code>not</code> support dynamic performance metrics), <code>pmdaChildren</code> is a skeleton implementation that returns <code>PM_ERR_NAME</code>. </p>
<p> A PMDA that supports dynamic performance metrics will provide a private callback that replaces <code>pmdaChildren</code> (by assignment to <i>version.four.children</i> of the <i>pmdaInterface</i> structure) and takes the initial metric <i>name</i> and returns names via <i>offspring</i>[] and the leaf or non-leaf status of each via <i>status</i>[]. </p>
<p> If <i>traverse</i> is 0, then the behaviour is akin to <code><a href="/docs/linux/man/3-pmgetchildren/">pmGetChildren</a></code>(3) and <i>offspring</i>[] contains the relative name component for the immediate descendants of <i>name.</i> </p>
<p> If <i>traverse</i> is 1, then the behaviour is akin to <code><a href="/docs/linux/man/3-pmtraversepmns/">pmTraversePMNS</a></code>(3) and <i>offspring</i>[] contains the absolute names of all dynamic metrics that are decedents of <i>name</i>. </p>
<p> The resulting list of pointers <i>offspring</i> <code>and</code> the values (the names) that the pointers reference will have been allocated by <code>pmdaChildren</code> with a single call to <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and the caller of <code>pmdaChildren</code> will call <code>free</code>(<i>offspring</i>) to release the space when it is no longer required. The same holds true for the <i>status</i> array.</p>
<h2>Diagnostics</h2>
<p><code>pmdaChildren</code> returns <code>PM_ERR_NAME</code> if the name is not recognized or cannot be translated, otherwise the number of descendent metric names found.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_PROTOCOL_4 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3), <code><a href="/docs/linux/man/3-pmdamain/">pmdaMain</a></code>(3), <code><a href="/docs/linux/man/3-pmgetchildren/">pmGetChildren</a></code>(3) and <code><a href="/docs/linux/man/3-pmtraversepmns/">pmTraversePMNS</a></code>(3). </p>
