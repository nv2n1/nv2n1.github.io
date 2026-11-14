---
title: "pmdatext(3)"
name: "pmdatext"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdatext/"
description: "pmdaText – extract metric help text for a PMDA"
---

<p><code>pmdaText</code> &#8211; extract metric help text for a PMDA</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaText(int </code><i>ident</i>, int <i>type</i>, char **<i>buffer</i>, pmdaExt *<i>pmda</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>As part of the Performance Metrics Domain Agent (PMDA) API (see <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)), <code>pmdaText</code> uses the standard <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) data structures to return the help text for metric <i>ident</i> in <i>buffer</i>. The help text must be located in help text files created with <code><a href="/docs/linux/man/1-newhelp/">newhelp</a></code>(1), and the associated files are automatically opened by <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3). </p>
<p> The path to the (basename of the) help text files can be set in the calls to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3) and overridden by the <code>-h</code> command line option in <code><a href="/docs/linux/man/3-pmdagetopt/">pmdaGetOpt</a></code>(3). </p>
<p> The encoding of <i>ident</i> follows the internal scheme used below the routines <code><a href="/docs/linux/man/3-pmlookuptext/">pmLookupText</a></code>(3) and <code><a href="/docs/linux/man/3-pmlookupindomtext/">pmLookupInDomText</a></code>(3), namely <i>ident</i> encodes either a metric identifier or an instance domain identifier, according to the value of <i>type</i>. </p>
<p> The <i>type</i> argument is a bit mask that encodes the interpretation of <i>ident</i> and the requested form of help text, as follows: either <code>PM_TEXT_PMID</code> if <i>ident</i> is a metric identifier, or <code>PM_TEXT_INDOM</code> if <i>ident</i> is an instance domain identifier, plus either <code>PM_TEXT_ONELINE</code> for the one line help text or <code>PM_TEXT_HELP</code> for the full help text. </p>
<p> The <i>buffer</i> is managed internally (usually it is cached), and it should <code>not</code> be released or freed by the caller of <code>pmdaText</code>.</p>
<h2>Diagnostics</h2>
<p>If the requested help text could not be obtained, <code>pmdaText</code> will return <code>PM_ERR_TEXT</code>.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_PROTOCOL_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-newhelp/">newhelp</a></code>(1), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3), <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindomtext/">pmLookupInDomText</a></code>(3) and <code><a href="/docs/linux/man/3-pmlookuptext/">pmLookupText</a></code>(3). </p>
