---
title: "quota(8)"
name: "quota"
section: "8"
letter: "q"
url: "/docs/linux/man/8-quota/"
description: "quota – report and optionally fix quota usage"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>quota &#8211; report and optionally fix quota usage</p>
<h2>Synopsis</h2>
<p><code>quota</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-d</code> <i>domain</i> ] [ <code>-f</code> ] [ <i>mailbox-prefix</i>&#8230; ]</p>
<h2>Description</h2>
<p><i>Quota</i> generates a report listing quota roots, giving their limits and usage. If the <i>-f</i> option is given, <i>quota</i> first fixes any inconsistencies in the quota subsystem, such as mailboxes with the wrong quota root or quota roots with the wrong quota usage reported. If an optional <i>domain</i> is given, the quota listing (and inconsistency fixing) is performed in that domain rather than the default domain. If any optional <i>mailbox-prefix</i> arguments are given, the quota listing (and inconsistency fixing) is limited to quota roots with names that start with one of the given prefixes. </p>
<p> Running <i>quota</i> with both the <i>-f</i> option and <i>mailbox-prefix</i> arguments is not recommended. </p>
<p> <i>Quota</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-d</code><i> domain</i></p>
<dd>List/fix quotas in <i>domain</i>.</p>
<dt><code>-f</code></p>
<dd>Fix any inconsistencies in the quota subsystem before generating a report.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
