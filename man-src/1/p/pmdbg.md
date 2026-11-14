---
title: "pmdbg(1)"
name: "pmdbg"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdbg/"
description: "pmdbg – translate Performance Co-Pilot debug control flags"
---

<h2>NAME</h2>
<p> <code>pmdbg</code> &#8211; translate Performance Co-Pilot debug control flags</p>
<h2>SYNOPSIS</h2>
<p> <code>pmdbg</code> <i>code</i> &#8230;<br />
 <code>pmdbg</code> <code>-l</code><br />
 <code>pmdbg</code> <code>-D</code> <i>name</i>[,<i>name</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The components of the Performance Co-Pilot (PCP) use a global vector of bit-fields to control diagnostic and debug output. </p>
<p> <code>pmdbg</code> with a <code>-l</code> argument prints out the mnemonic and decimal values of all the bit-fields in the debug control vector. </p>
<p> <code>pmdbg</code> with a <code>-D</code> argument parses the list of <i>names</i>(s) using <code><a href="/docs/linux/man/3-__pmparsedebug/">__pmParseDebug</a></code>(3) and reports the corresponding decimal value. This is most useful when debugging and wanting to set the internal value of the control vector (<code>pmDebug</code>) via a debugger, e.g. <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1). </p>
<p> In the alternative usage, the <i>code</i> arguments are values for the debug vector, and the bit-fields that are enabled by each of these values is listed. </p>
<p> Each <i>code</i> may be an integer, a hexadecimal value or a hexadecimal value prefixed by either &#8220;0x&#8221; or &#8220;0X&#8221;. </p>
<p> Most applications using the facilities of the PCP support a <code>-D</code><i>N</i> command-line syntax to enable debug control. <code>pmdbg</code> is designed to help choose an appropriate value for <i>N</i>. </p>
<p> Alternatively the initial value of the debug control flags may be set to a value <i>N</i> using the environment variable <code>$PCP_DEBUG</code>. If both mechanisms are used the effect is additive, so the resultant flags are those set via <code>$PCP_DEBUG</code> combined with those set via any <code>-D</code> command line options.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
