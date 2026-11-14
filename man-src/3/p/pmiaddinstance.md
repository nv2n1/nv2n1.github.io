---
title: "pmiaddinstance(3)"
name: "pmiaddinstance"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmiaddinstance/"
description: "pmiAddInstance – add an element to an instance domain in a LOGIMPORT context"
---

<p><code>pmiAddInstance</code> &#8211; add an element to an instance domain in a LOGIMPORT context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiAddInstance(pmInDom </code><i>indom</i>, const char *<i>instance</i>, int <i>inst</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiAddInstance($</code><i>indom</i>, $<i>instance</i>, $<i>inst</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiAddInstance</code> adds a new element to the instance domain identified by <i>indom</i>. </p>
<p> <i>indom</i> would normally be constructed using the <code>pmInDom_build</code> macro, e.g. pmInDom_build(PMI_DOMAIN,0) for the first instance domain in the Performance Metrics Domain PMI_DOMAIN (which is the default for all meta data created by the LOGIMPORT library). </p>
<p> The new instance must have both an external name (<i>instance</i>) and an internal instance identifier (<i>inst</i>) that is unique across all instances in the <i>indom</i> instance domain. There is a special &#8220;uniqueness rule&#8221; for <i>instance</i> that is imposed by <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3), namely that the external instance name must be unique in the leading non-space characters, e.g. the instance names &#8220;foo&#8221; and &#8220;foo bar&#8221; are considered the same by this rule and not allowed in the same instance domain, but &#8220;foo&#8221; and &#8220;foobar&#8221; would be allowed. </p>
<p> Once defined, the external instance name can be used in calls to <code><a href="/docs/linux/man/3-pmigethandle/">pmiGetHandle</a></code>(3) and/or <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3) with the name of a metric defined over the same instance domain.</p>
<h2>Diagnostics</h2>
<p><code>pmiAddInstance</code> returns zero on success else a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmigethandle/">pmiGetHandle</a></code>(3), <code><a href="/docs/linux/man/3-pmiputvalue/">pmiPutValue</a></code>(3) and <code><a href="/docs/linux/man/3-pmlookupindom/">pmLookupInDom</a></code>(3). </p>
