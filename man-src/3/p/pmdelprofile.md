---
title: "pmdelprofile(3)"
name: "pmdelprofile"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdelprofile/"
description: "pmDelProfile – delete instance(s) from the current PMAPI instance profile"
---

<p><code>pmDelProfile</code> &#8211; delete instance(s) from the current PMAPI instance profile</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmDelProfile(pmInDom </code><i>indom</i>, int <i>numinst</i>, int *<i>instlist</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The set of instances for performance metrics returned from a <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) call may be filtered or restricted using an instance profile. There is one instance profile for each context the application creates at the Performance Metrics Application Programming Interface (PMAPI), and each instance profile may include instances from one or more instance domains (see <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3)). </p>
<p> <code>pmDelProfile</code> may be used to delete instance specifications from the instance profile of the current PMAPI context. </p>
<p> In the simplest variant, the list of instances identified by the <i>instlist</i> argument for the <i>indom</i> instance domain are removed from the instance profile. The list of instance identifiers contains <i>numinst</i> values. </p>
<p> The <i>indom</i> value would normally be extracted from a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric, and the instances in <i>instlist</i> would typically be determined by calls to <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3) or <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3). </p>
<p> If <i>indom</i> equals <code>PM_INDOM_NULL</code> or <i>numinst</i> is zero, then all instance domains are selected for deletion. If <i>instlist</i> is <i>NULL</i>, then all instances in the selected domain(s) are removed from the profile. </p>
<p> To disable all available instances in all domains, use <i>pmDelProfile(PM_INDOM_NULL, 0, NULL)</i>. This is the only situation in which <i>indom</i> may be <code>PM_INDOM_NULL</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmaddprofile/">pmAddProfile</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmwhichcontext/">pmWhichContext</a></code>(3).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_PROFILESPEC</code></p>
<dd><i>indom</i> was <code>PM_INDOM_NULL</code> and <i>instlist</i> was not empty</dl>
<h2>Caveat</h2>
<p>It is possible to delete non-existent instance domains and non-existent instances from an instance profile. None of the routines that use the instance profile will ever issue an error if you do this. The cost of checking, when checking is possible, outweighs any benefits.</p>
