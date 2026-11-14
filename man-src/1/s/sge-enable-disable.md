---
title: "sge-enable-disable(1)"
name: "sge-enable-disable"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sge-enable-disable/"
description: "sge-disable-submits, sge-enable-submits – Prevent/allow xxQS_NAMExx job submission by non-privileged users"
---

<h2 class="name">NAME</h2>
<p> sge-disable-submits, sge-enable-submits &#8211; Prevent/allow xxQS_NAMExx job submission by non-privileged users </p>
<h2>SYNOPSIS</h2>
<p> <code>sge-disable-submits</code> [<code>-h</code>|<code>&#8211;help</code>] </p>
<p> <code>sge-enable-submits</code> [<code>-h</code>|<code>&#8211;help</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>sge-disable-submits</code> Limits the xxQS_NAMExx global configuration to users in ACL &#8216;testing&#8217; to prevent normal users submitting further jobs. <code>sge-enable-submits</code> undoes the effect of <code>sge-disable-submits</code>, allowing normal users to submit jobs again. You must previously have created the &#8216;testing&#8217; ACL with </p>
<p> These operations are useful when you want to drain the xxQS_NAMExx installation completely of jobs, say around maintenance periods.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd> <code>-h</code>,<code>&#8211;help</code> Print usage information.</dl>
<h2>SEE ALSO</h2>
<h2>AUTHOR</h2>
<p> Dave Love &lt;d.love [at] liverpool.ac.uk&gt; </p>
<h2>Index</h2>
