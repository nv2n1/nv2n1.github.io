---
title: "pmdaclosehelp(3)"
name: "pmdaclosehelp"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdaclosehelp/"
description: "pmdaOpenHelp, pmdaGetHelp, pmdaGetInDomHelp, pmdaCloseHelp – help text support for a PMDA"
---

<p><code>pmdaOpenHelp</code>, <code>pmdaGetHelp</code>, <code>pmdaGetInDomHelp</code>, <code>pmdaCloseHelp</code> &#8211; help text support for a PMDA</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaOpenHelp(char *</code><i>fname</i>);<br />
 char *pmdaGetHelp(int <i>handle</i>, pmID <i>pmid</i>, int <i>type</i>);<br />
 char *pmdaGetInDomHelp(int <i>handle</i>, pmInDom <i>indom</i>, int <i>type</i>);<br />
 void pmdaCloseHelp(int <i>handle</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p>As part of the Performance Metrics Domain Agent (PMDA) API (see <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)), this group of routines is used to implement the processing of a PMDA&#8217;s metric help information. </p>
<p> These routines are really intended for internal use, and should not need to be called directly from any PMDA code. </p>
<p> Briefly, the base name of the help text file (as created by <code><a href="/docs/linux/man/1-newhelp/">newhelp</a></code>(1)) is passed in via a <code>-h</code> command line option for a daemon PMDA or as an argument to <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3). Then <code>pmdaOpenHelp</code> is called from <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3) and returns a <i>handle</i> that is used in subsequent calls to identify a particular help text collection (each PMDA typically has only one such collection). </p>
<p> Requests for help text are passed to <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3) which calls <code>pmdaGetHelp</code> or <code>pmdaGetInDomHelp</code> as required. </p>
<p> Other than error cases in <code>pmdaOpenHelp</code>, <code>pmdaCloseHelp</code> is not called.</p>
<h2>Diagnostics</h2>
<p><code>pmdaOpenHelp</code> returns a negative value for failure, suitable for decoding with <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3). <code>pmdaGetHelp</code> and <code>pmdaGetInDomHelp</code> return NULL if the corresponding help text does not exist.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_PROTOCOL_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-newhelp/">newhelp</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3), <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3), <code><a href="/docs/linux/man/3-pmdainit/">pmdaInit</a></code>(3), <code><a href="/docs/linux/man/3-pmdatext/">pmdaText</a></code>(3) and <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3). </p>
