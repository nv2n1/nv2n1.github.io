---
title: "pmdainstance(3)"
name: "pmdainstance"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdainstance/"
description: "pmdaInstance – return instance descriptions for a PMDA"
---

<p><code>pmdaInstance</code> &#8211; return instance descriptions for a PMDA</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/pmda.h&gt; </p>
<p> int pmdaInstance(pmInDom </code><i>indom</i>, int <i>inst</i>, char *<i>name</i>, __pmInResult&nbsp;<wbr>**<i>result</i>, pmdaExt&nbsp;<wbr>*<i>pmda</i>); </p>
<p> cc &#8230; -lpcp_pmda -lpcp</p>
<h2>Description</h2>
<p><code>pmdaInstance</code> uses the standard <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) data structures to return information concerning the instance domain <i>indom</i>. </p>
<p> The <i>result</i> structure is constructed by <code>pmdaInstance</code> and will contain one or more instance names and/or identifiers as specified by the <i>inst</i> and <i>name</i> arguments. </p>
<p> If <i>inst</i> has the value <code>PM_IN_NULL</code> and <i>name</i> is a null string, <i>result</i> will contain all the instances names and identifiers in the instance domain. </p>
<p> If <i>inst</i> is <code>PM_IN_NULL</code> but <i>name</i> is the name of an instance in the instance domain <i>indom</i>, then <i>result</i> will contain the instance identifier for instance <i>name</i>. Note that if <i>name </i> contains no spaces, partial matching up to the first space in the instance name is performed, i.e. &#8220;<code>1</code>&#8221; will match instance name &#8220;<code>1</code> <code>minute</code>&#8221;. If <i>name</i> contains an embedded space, then no partial matching is performed and <i>name</i> should match one of the instance names exactly. </p>
<p> If <i>name</i> is a null string but <i>inst</i> is an instance identifier in the instance domain <i>indom</i>, then <i>result</i> will contain the name for instance <i>inst</i>. The <i>result</i> structure is allocated with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) and should be released by the caller with <code><a href="/docs/linux/man/3-free/">free</a></code>(3).</p>
<h2>Diagnostics</h2>
<p>If any errors occur during the execution of <code>pmdaInstance</code>, the <i>result</i> structure is deallocated. If the instance domain <i>indom</i> is not supported by the PMDA, <code>pmdaInstance</code> will return <code>PM_ERR_INDOM</code>. </p>
<p> If the <i>inst</i> or <i>name</i> does not correspond to any instances in the <i>indom</i> domain, <code>pmdaInstance</code> will return <code>PM_ERR_INST</code>.</p>
<h2>Caveat</h2>
<p>The PMDA must be using <code>PMDA_INTERFACE_2 </code> or later, as specified in the call to <code><a href="/docs/linux/man/3-pmdadso/">pmdaDSO</a></code>(3) or <code><a href="/docs/linux/man/3-pmdadaemon/">pmdaDaemon</a></code>(3). </p>
<p> Because of optional partial matching up to the first space in the instance name, the <code>PMDA</code> developer should ensure that if instance names are allowed to have spaces, the names are unique up to the first space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) and <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3). </p>
