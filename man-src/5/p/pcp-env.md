---
title: "pcp-env(5)"
name: "pcp-env"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pcp-env/"
description: "pcp.env – script to set Performance Co-Pilot run-time environment variables"
---

<p><code>pcp.env</code> &#8211; script to set Performance Co-Pilot run-time environment variables</p>
<h2>Synopsis</h2>
<p><i>/etc/pcp.env</i></p>
<h2>Description</h2>
<p>The <i>pcp.env</i> script is sourced by assorted Performance Co-Pilot (PCP) scripts and utilities to define the PCP operating environment variables. The conjugate for executable programs using the PCP libraries is the <i><a href="/docs/linux/man/3-__pmgetconfig/">__pmGetConfig</a></i>(3) function. Typical usage of <i>pcp.env </i> in a script is as follows :</p>
<dl>
<dd>&nbsp;<wbr>&nbsp;<wbr>#!&nbsp;<wbr>/bin/sh<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>source the PCP environment variables<br />
&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>/etc/pcp.env<br />
&nbsp;<wbr>&nbsp;<wbr>rest of script &#8230;  The full syntax and semantics of the <i>pcp.conf</i> file and the <i>__pmGetConfig</i> function are described in their respective reference pages. If the file <i>$HOME/.pcp/pcp.conf</i> exists then this will be processed after the system-wide <i>pcp.conf</i> file. This provides a mechanism to selectively modify or augment the environment settings for PCP scripts, which maybe useful if the scripts are run with <code><a href="/docs/linux/man/1-sudo/">sudo</a></code>(1) which cleans the environment of important settings that are required to ensure the correct execution of the PCP scripts, e.g. <code>$PATH</code> or <code>$PERL5LIB</code>.</p>
<h2>Environment</h2>
<p>The <code>PCP_CONF</code> environment variable specifies an alternative path to the <i>pcp.conf</i> file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-sudo/">sudo</a></code>(1), <code><a href="/docs/linux/man/3-pcpintro/">PCPIntro</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-__pmgetconfig/">__pmGetConfig</a></code>(3) and <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). </p>
