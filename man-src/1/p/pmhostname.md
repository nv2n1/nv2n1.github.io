---
title: "pmhostname(1)"
name: "pmhostname"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmhostname/"
description: "pmhostname – report hostname"
---

<h2>NAME</h2>
<p> <code>pmhostname</code> &#8211; report hostname</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmhostname</code> [<i>hostname</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmhostname</code> reports the name of the host <i>hostname</i> as returned by <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3). </p>
<p> If <i>hostname</i> is not specified, then the local host name is retrieved using <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2) and this is than passed to <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3). </p>
<p> <code>pmhostname</code> provides a service for shell scripts that mimics the logic formerly used by Performance Co-Pilot applications when trying to determine the official name of a host. PCP applications no longer use DNS-based heuristics, and therefore this command is <i>deprecated</i>. </p>
<p> If <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) fails, the input host name (either <i>hostname</i> or the result from calling <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2)) is reported.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-named/">named</a></code>(1), <code><a href="/docs/linux/man/1-nsd/">nsd</a></code>(1), <code><a href="/docs/linux/man/1-nslookup/">nslookup</a></code>(1), <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2), <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/5-resolver/">resolver</a></code>(5). </p>
<h2>Index</h2>
