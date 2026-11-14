---
title: "pmgetcontexthostname(3)"
name: "pmgetcontexthostname"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmgetcontexthostname/"
description: "pmGetContextHostName, pmGetContextHostName_r – return the hostname associated with a Performance Co-Pilot context"
---

<p><code>pmGetContextHostName</code>, <code>pmGetContextHostName_r</code> &#8211; return the hostname associated with a Performance Co-Pilot context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> const char *pmGetContextHostName(int </code><i>id</i>);<br />
 char *pmGetContextHostName_r(int <i>id</i>, char *<i>buf</i>, int <i>buflen</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Given a valid PCP context identifier previously created with <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) or <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), the <code>pmGetContextHostName</code> function returns the hostname associated with <i>id</i>. The <code>pmGetContextHostName_r</code> function does the same, but stores the result in a user-supplied buffer <i>buf</i> of length <i>buflen</i>, which should have room for at least <code>MAXHOSTNAMELEN</code> bytes. </p>
<p> If the context <i>id</i> is associated with an archive source of data, the hostname returned is extracted from the archive label using <code><a href="/docs/linux/man/3-pmgetarchivelabel/">pmGetArchiveLabel</a></code>(3). </p>
<p> For live contexts, an attempt will first be made to retrieve the hostname from the PCP collector system using <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) with the <i>pmcd.hostname</i> metric. This allows client tools using this interface to retrieve an accurate host identifier even in the presence of port forwarding and tunnelled connections. </p>
<p> Should this not succeed, then a fallback method is used. For local contexts &#8211; with local meaning any of DSO, &#8220;localhost&#8221; or Unix domain socket connection &#8211; a hostname will be sought via <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3). For other contexts, the hostname extracted from the initial context host specification will be used.</p>
<h2>Return Value</h2>
<p>If <i>id</i> is not a valid PCP context identifier, the returned hostname is a zero length string.</p>
<h2>Notes</h2>
<p><code>pmGetContextHostName</code> returns a pointer to a static buffer, so the returned value is only valid until the next call to <code>pmGetContextHostName</code> and hence is not thread-safe. Multi-threaded applications should use <code>pmGetContextHostName_r</code> instead.</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3), <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3), <code><a href="/docs/linux/man/3-pmgetarchivelabel/">pmGetArchiveLabel</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
