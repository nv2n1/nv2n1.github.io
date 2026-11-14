---
title: "tc-tcindex(8)"
name: "tc-tcindex"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-tcindex/"
description: "tcindex – traffic control index filter"
---

<p>tcindex &#8211; traffic control index filter</p>
<h2>Synopsis</h2>
<p><code>tc</code> <code>filter</code> &#8230; <code>tcindex</code> [ <code>hash</code> <i>SIZE</i> ] [ <code>mask</code> <i>MASK</i> ] [ <code>shift</code> <i>SHIFT</i> ] [ <code>pass_on</code> | <code>fall_through</code> ] [ <code>classid</code> <i>CLASSID</i> ] [ <code>action</code> <code>ACTION_SPEC</code> ]</p>
<h2>Description</h2>
<p>This filter allows to match packets based on their <code>tcindex</code> field value, i.e. the combination of the DSCP and ECN fields as present in IPv4 and IPv6 headers.</p>
<h2>Options</h2>
<dl>
<dt><code>action</code><i> ACTION_SPEC</i></p>
<dd>Apply an action from the generic actions framework on matching packets.</p>
<dt><code>classid</code><i> CLASSID</i></p>
<dd>Push matching packets into the class identified by <i>CLASSID</i>.</p>
<dt><code>hash</code><i> SIZE</i></p>
<dd>Hash table size in entries to use. Defaults to 64.</p>
<dt><code>mask</code><i> MASK</i></p>
<dd>An optional bitmask to binary <code>AND</code> to the packet&#8217;s <code>tcindex</code> field before use.</p>
<dt><code>shift</code><i> SHIFT</i></p>
<dd>The number of bits to right-shift a packet&#8217;s <code>tcindex</code> value before use. If a <code>mask</code> has been set, masking is done before shifting.</p>
<dt><code>pass_on</code></p>
<dd>If this flag is set, failure to find a class for the resulting ID will make the filter fail and lead to the next filter being consulted.</p>
<dt><code>fall_through</code></p>
<dd>This is the opposite of <code>pass_on</code> and the default. The filter will classify the packet even if there is no class present for the resulting class ID. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) </p>
