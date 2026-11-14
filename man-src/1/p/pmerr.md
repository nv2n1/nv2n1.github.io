---
title: "pmerr(1)"
name: "pmerr"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmerr/"
description: "pmerr – translate Performance Co-Pilot error codes into error messages"
---

<h2>NAME</h2>
<p> <code>pmerr</code> &#8211; translate Performance Co-Pilot error codes into error messages</p>
<h2>SYNOPSIS</h2>
<p> <code>pmerr</code> <i>code</i> &#8230;<br />
 <code>pmerr</code> <code>-l</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pmerr</code> accepts standard Performance Co-Pilot (PCP) error codes via the <i>code</i> argument(s) and generates the corresponding error text. </p>
<p> Each <i>code</i> may be an integer, a hexadecimal value or a hexadecimal value prefixed by either &#8220;0x&#8221; or &#8220;0X&#8221;. </p>
<p> Error codes must be less than zero, so if <i>code</i> is a positive number, a warning message is produced, and the negated value is used. </p>
<p> The alternative use of the <code>-l</code> option causes all known error codes to be listed, along with their symbolic names and error text.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
