---
title: "pcp-conf(5)"
name: "pcp-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pcp-conf/"
description: "pcp.conf – the Performance Co-Pilot configuration and environment file"
---

<p><code>pcp.conf</code> &#8211; the Performance Co-Pilot configuration and environment file</p>
<h2>Synopsis</h2>
<p><i>/etc/pcp.conf</i></p>
<h2>Description</h2>
<p>When using Performance Co-Pilot (PCP) tools and utilities and when calling PCP library functions, a standard set of environment variables are defined in <i>/etc/pcp.conf</i>. These variables are generally used to specify the location of various PCP pieces in the file system and may be loaded into shell scripts by sourcing the <i>/etc/<a href="/docs/linux/man/5-pcp-env/">pcp.env</a></i>(5) shell script and queried by C/C++ programs using the <i><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></i>(3) library function. If a variable is already defined in the environment, the values in <i>pcp.conf</i> do <code>not</code> override those values, i.e. the values in <i>pcp.conf</i> serve as installation defaults only. </p>
<p> Both the <i>pcp.env</i> and <i>pcp.conf</i> files are expected to be found in <i>/etc</i> by default. If required, the <i>pcp.conf</i> file may be relocated and <code>PCP_CONF</code> set in the environment to specify the full path to the new location. The <i>pcp.env</i> file can not be relocated (this is the only hard coded path required by PCP). </p>
<p> The syntax rules for <i>pcp.conf</i> are as follows :</p>
<dl>
<dt>1.</p>
<dd>the general syntax is<br />
 <center> <code>PCP_VARIABLE_NAME=variable value to end of line</code><br />
 </center></p>
<dt>2.</p>
<dd>lines that begin with <code>#</code> and all blank lines are ignored.</p>
<dt>3.</p>
<dd>all variables must be prefixed with <code>PCP_</code>. This is a security issue &#8211; variables that do not have this prefix will be silently ignored.</p>
<dt>4.</p>
<dd>there should be no space between the variable name and the literal <code>=</code> and no space between the <code>= </code> and the variable value (unless the value actually starts with a space). This is required because the <i>pcp.conf</i> file may be sourced directly by Makefiles as well as interpreted by the <i>pcp.env</i> script and the <i>pmGetConfig</i> function.</p>
<dt>5.</p>
<dd>variable values may contain spaces and should <code>not</code> be quoted. The <i>pcp.env</i> script automatically quotes all variable values from the character immediately following the <code>=</code> through to the end of the line.</dl>
<p> For further details and an explanation of the use of each variable, see the comments in the <i>/etc/pcp.conf</i> file itself.</p>
<h2>Environment</h2>
<p>The <code>PCP_CONF</code> environment variable specifies an alternative path to the <i>pcp.conf</i> file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmconfig/">pmconfig</a></code>(1), <code><a href="/docs/linux/man/3-pcpintro/">PCPIntro</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
