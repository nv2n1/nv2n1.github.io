---
title: "pmgetconfig(3)"
name: "pmgetconfig"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmgetconfig/"
description: "pmGetConfig, pmGetOptionalConfig – return values for Performance Co-Pilot configuration variables"
---

<p><code>pmGetConfig</code>, <code>pmGetOptionalConfig</code> &#8211; return values for Performance Co-Pilot configuration variables</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 char *pmGetConfig(const char *</code><i>variable</i>);<br />
 char *pmGetOptionalConfig(const char *<i>variable</i>); </p>
<p> #include &lt;pcp/impl.h&gt;<br />
 char *__pmGetAPIConfig(const char *<i>feature</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The <code>pmGetConfig</code> and <code>pmGetOptionalConfig</code> functions search for <i>variable</i> first in the environment and then, if not found, in the Performance Co-Pilot (PCP) configuration file and returns the string result. If <i>variable</i> is not already in the environment, it is added with a call to <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3) before returning. </p>
<p> The <code>pmGetOptionalConfig</code> function allows for failures &#8211; either from <i>variable</i> not being set at all, or due to the configuration file being missing. <code>pmGetConfig</code> is less tolerant to a missing configuration file, which it treats as a critical PCP installation failure &#8211; see the &#8220;RETURN VALUE&#8221; section below for further details. </p>
<p> The default location of the PCP configuration file is <code>/etc/pcp.conf</code> but this may be changed by setting <code>PCP_CONF</code> in the environment to a new location, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). </p>
<p> The internal <code>__pmGetAPIConfig</code> function reports on features of the PCP library. It can be used to query support for multi-threading, security extensions, and other features. </p>
<p> The <code><a href="/docs/linux/man/1-pmconfig/">pmconfig</a></code>(1) utility provides command line access to both of these interfaces, and also provides a mechanism for listing all available <code>variables</code> and <code>features</code> that are valid arguments to these routines.</p>
<h2>Return Value</h2>
<p>If <i>variable</i> is not found in either the environment or the PCP configuration file, or if the configuration file is inaccessible, then <code>pmGetOptionalConfig </code> returns NULL. </p>
<p> If <i>variable</i> is found in neither the environment nor the PCP configuration file, then <code>pmGetConfig </code> returns an empty string. If the PCP configuration file is not found then a fatal error message is printed and the process will <code><a href="/docs/linux/man/2-exit/">exit</a></code>(2) &#8211; although this sounds drastic, it is the only course of action available because the PCP configuration/installation is deemed fatally flawed. </p>
<p> The <code>__pmGetAPIConfig</code> routine returns NULL on failure to lookup the requested <i>feature</i>. It does not modify the environment, and returns a pointer to a static read-only string. </p>
<p> The value returned by all of these routines is either a static pointer or pointer into the environment, and so changing it is a bad idea.</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmconfig/">pmconfig</a></code>(1), <code><a href="/docs/linux/man/3-pmgetversion/">pmGetVersion</a></code>(3), <code><a href="/docs/linux/man/2-exit/">exit</a></code>(2), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3), <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). </p>
