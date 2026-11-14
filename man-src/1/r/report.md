---
title: "report(1)"
name: "report"
section: "1"
letter: "r"
url: "/docs/linux/man/1-report/"
description: "report – uploads FILEs to specified ticket on TARGET."
---

<h2 class="name">NAME</h2>
<p> report &#8211; uploads FILEs to specified ticket on TARGET. </p>
<h2>SYNOPSIS</h2>
<p> <i>report</i> [-v] -T TARGET -t ID FILE&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This tool is provided to ease transition of users of report package to libreport. Recognized TARGETs are <i>strata</i> and <i>bugzilla</i>, first one invokes upload to RHTSupport and second &#8211; to Bugzilla. </p>
<p> Configuration (such as login data) can be supplied via files /etc/libreport/plugins/bugzilla.conf and /etc/libreport/plugins/rhtsupport.conf, or via environment variables &#8211; read documentation of reporter-bugzilla and reporter-rhtsupport tools.</p>
<h2>OPTIONS</h2>
<p> -T, &#8211;target</p>
<dl>
<dt>
<dd> &quot;strata&quot; or &quot;bugzilla&quot;</dl>
<p> -t, &#8211;ticket ID</p>
<dl>
<dt>
<dd> Ticket/case ID</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-reporter-bugzilla/">reporter-bugzilla</a></code>(1), <code><a href="/docs/linux/man/1-reporter-rhtsupport/">reporter-rhtsupport</a></code>(1)</p>
<h2>AUTHORS</h2>
<dl>
<dt>
<dd> &bull; ABRT team</dl>
<h2>Index</h2>
