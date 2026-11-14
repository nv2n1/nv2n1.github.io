---
title: "pmiestatus(1)"
name: "pmiestatus"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmiestatus/"
description: "pmiestatus – display information from pmie stats file"
---

<h2>NAME</h2>
<p> <code>pmiestatus</code> &#8211; display information from pmie stats file</p>
<h2>SYNOPSIS</h2>
<p> <code>pmiestatus</code> <i>statsfile</i> [<i>&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmiestatus</code> displays information used to identify a running <code>pmie</code> process. It is mostly used by <code>pmie_check</code> and <code>pmie_daily</code> when they hunt for instances of <code>pmie</code> to check against the control file.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_TMP_DIR/pmie/</code><i>*</i></p>
<dd> pmie stats files</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), <code><a href="/docs/linux/man/1-pmie_check/">pmie_check</a></code>(1), <code><a href="/docs/linux/man/1-pmie_daily/">pmie_daily</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
