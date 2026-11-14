---
title: "tc-hfsc(8)"
name: "tc-hfsc"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-hfsc/"
description: "HFSC – Hierarchical Fair Service Curve’s control under linux"
---

<p>HFSC &#8211; Hierarchical Fair Service Curve&#8217;s control under linux</p>
<h2>Synopsis</h2>
<pre>tc qdisc add ... hfsc [ <code>default</code> CLASSID ]
tc class add ... hfsc [ [ <code>rt</code> SC ] [ <code>ls</code> SC ] | [ <code>sc</code> SC ] ] [ <code>ul</code> SC ]
<code>rt</code> : realtime service curve
<code>ls</code> : linkshare service curve
<code>sc</code> : rt+ls service curve
<code>ul</code> : upperlimit service curve
&bull; at least one of <code>rt</code>, <code>ls</code> or <code>sc</code> must be specified
&bull; <code>ul</code> can only be specified with <code>ls</code> or <code>sc</code>
<dl><dt>SC := [ [ <code>m1</code> BPS ] <code>d</code> SEC ] <code>m2</code> BPS<dd><code>m1</code> : slope of the first segment
<code>d</code> : x-coordinate of intersection
<code>m2</code> : slope of the second segment
</dl><dl><dt>SC := [ [ <code>umax</code> BYTE ] <code>dmax</code> SEC ] <code>rate</code> BPS<dd><code>umax</code> : maximum unit of work
<code>dmax</code> : maximum delay
<code>rate</code> : rate
</dl></pre>
<p>For description of BYTE, BPS and SEC &#8211; please see <code>UNITS</code> section of <code><a href="/docs/linux/man/8-tc/">tc</a></code>(8).</p>
<h2>DESCRIPTION (qdisc)</h2>
<p>HFSC qdisc has only one optional parameter &#8211; <code>default</code>. CLASSID specifies the minor part of the default classid, where packets not classified by other means (e.g. u32 filter, CLASSIFY target of iptables) will be enqueued. If <code>default</code> is not specified, unclassified packets will be dropped.</p>
<h2>DESCRIPTION (class)</h2>
<p>HFSC class is used to create a class hierarchy for HFSC scheduler. For explanation of the algorithm, and the meaning behind <code>rt</code>, <code>ls</code>, <code>sc</code> and <code>ul</code> service curves &#8211; please refer to <code><a href="/docs/linux/man/7-tc-hfsc/">tc-hfsc</a></code>(7). </p>
<p> As you can see in <code>SYNOPSIS</code>, service curve (SC) can be specified in two ways. Either as maximum delay for certain amount of work, or as a bandwidth assigned for certain amount of time. Obviously, <code>m1</code> is simply <code>umax</code>/<code>dmax</code>. </p>
<p> Both <code>m2</code> and <code>rate</code> are mandatory. If you omit other parameters, you will specify linear service curve.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/7-tc-hfsc/">tc-hfsc</a></code>(7), <code><a href="/docs/linux/man/8-tc-stab/">tc-stab</a></code>(8) </p>
<p> Please direct bugreports and patches to: &lt;netdev [at] vger.kernel.org&gt;</p>
<h2>Author</h2>
<p>Manpage created by Michal Soltys (soltys [at] ziu.info)</p>
