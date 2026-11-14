---
title: "pmconfig(1)"
name: "pmconfig"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmconfig/"
description: "pmconfig – Performance Co-Pilot configuration parameters"
---

<h2>NAME</h2>
<p> <code>pmconfig</code> &#8211; Performance Co-Pilot configuration parameters</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmconfig</code> [<code>-a</code>|<code>-l</code>] [<code>-L</code>] [<code>-s</code>] [<i>name &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmconfig</code> displays the values for some or all configuration parameters of the local Performance Co-Pilot toolkit installation. </p>
<p> The <code>-L</code> option may be used to change the default reporting mode so that the capabilities of the PCP library are reported, rather than the PCP environment. </p>
<p> An output format suitable for sourcing in shell scripts can be obtained using the <code>-s</code> option, which ensures configuration information is quoted and preceded by an export statement. When not reporting the library capabilities, this mode will produce a statement that does not override an existing setting in the environment for PCP configuration variables. </p>
<p> In the default operating mode, <code>pmconfig</code> is often used in conjunction with the <code>$PCP_DIR</code> environment variable to setup scripts running under the Windows operating system, where the filesystem hierarchy differs greatly to the of Linux/UNIX-based operating systems.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
