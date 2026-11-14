---
title: "pmaddprofile(3)"
name: "pmaddprofile"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmaddprofile/"
description: "pmAddProfile – add instance(s) to the current PMAPI instance profile"
---

<p><code>pmAddProfile</code> &#8211; add instance(s) to the current PMAPI instance profile</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmAddProfile(pmInDom </code><i>indom</i>, int <i>numinst</i>, int *<i>instlist</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The set of instances for performance metrics returned from a <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) call may be filtered or restricted using an instance profile. There is one instance profile for each context the application creates at the Performance Metrics Application Programming Interface (<code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3)), and each instance profile may include instances from one or more instance domains (see <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3)). </p>
<p> <code>pmAddProfile</code> may be used to add new instance specifications to the instance profile of the current PMAPI context. </p>
<p> In the simplest variant, the list of instances identified by the <i>instlist</i> argument for the <i>indom</i> instance domain are added to the instance profile. The list of instance identifiers contains <i>numinst</i> values. </p>
<p> The <i>indom</i> value would normally be extracted from a call to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a particular performance metric, and the instances in <i>instlist</i> would typically be determined by calls to <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3) or <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3). </p>
<p> To select all instances in all instance domains, use </p>
<pre>pmAddProfile(PM_INDOM_NULL, 0, (int *)0)</pre>
<p>This is the only case where <i>indom</i> may be equal to <code>PM_INDOM_NULL</code>. If <i>numinst</i> is zero, or <i>instlist</i> is NULL, then all instances in <i>indom</i> are selected.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmdelprofile/">pmDelProfile</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3), <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmwhichcontext/">pmWhichContext</a></code>(3).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>PM_ERR_PROFILESPEC</code></p>
<dd><i>indom</i> was <code>PM_INDOM_NULL</code> and <i>instlist</i> was not empty</dl>
<h2>Caveat</h2>
<p>It is possible to add non-existent instance domains and non-existent instances to an instance profile. None of the routines that use the instance profile will ever issue an error if you do this. The cost of checking, when checking is possible, outweighs any benefits.</p>
