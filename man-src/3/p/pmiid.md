---
title: "pmiid(3)"
name: "pmiid"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmiid/"
description: "pmiUnits, pmiID, pmiInDom – construct core metric data structures"
---

<p><code>pmiUnits</code>, <code>pmiID</code>, <code>pmiInDom</code> &#8211; construct core metric data structures</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> pmID pmiID(int </code><i>domain</i>, int <i>cluster</i>, int <i>item</i>);<br />
 pmInDom pmiInDom(int <i>domain</i>, int <i>serial</i>);<br />
 pmUnits pmiUnits(int <i>dimSpace</i>, int <i>dimTime</i>, int <i>dimCount</i>, int&nbsp;<wbr><i>scaleSpace</i>, int&nbsp;<wbr><i>scaleTime</i>, int&nbsp;<wbr><i>scaleCount</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> $pmid = pmiID($</code><i>domain</i>, $<i>cluster</i>, $<i>item</i>);<br />
 $indom = pmiInDom($<i>domain</i>, $<i>serial</i>);<br />
 $units = pmiUnits($<i>dimSpace</i>, $<i>dimTime</i>, $<i>dimCount</i>, $<i>scaleSpace</i>, $<i>scaleTime</i>, $<i>scaleCount</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), these routines provide convenience methods (especially for script use) for constructing <code>pmID</code>, <code>pmInDom</code> and <code>pmUnits</code> structures respectively, to be used in subsequent calls to <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3) and <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3). </p>
<p> Refer to <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for a complete description of the values and semantics of the components of a <code>pmUnits</code> structure, and hence the valid argument values for <code>pmiUnits</code>.</p>
<h2>Diagnostics</h2>
<p>None.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddmetric/">pmiAddMetric</a></code>(3), <code><a href="/docs/linux/man/3-pmiaddinstance/">pmiAddInstance</a></code>(3) and <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3). </p>
