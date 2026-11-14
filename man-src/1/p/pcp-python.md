---
title: "pcp-python(1)"
name: "pcp-python"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-python/"
description: "pcp-python – run a python script using a preferred python variant"
---

<h2>NAME</h2>
<p> <code>pcp-python</code> &#8211; run a python script using a preferred python variant</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp python</code> [<i>SCRIPT</i> [<i>ARG</i>]&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pcp-python</code> has been replaced by <code><a href="/docs/linux/man/1-pmpython/">pmpython</a></code>(1) which is preferred, however <code>pcp-python</code> is still installed to provided backwards compatibility. </p>
<p> <code>pcp-python</code> provides a way to run python scripts using a customisable python binary, rather than embedding any particular version of python into each script. </p>
<p> This can be useful as it allows version-independent python code to be run anywhere. All python modules shipped with PCP support versions 2.6 and later (in the python2 series), and 3.3 and later (in the python3 release series). </p>
<p> Due to python monitoring and collecting scripts being relatively simple in PCP (not requiring new modules, language features, etc), it has been possible to ensure they work for all of the above python versions. Thus, it is common for PCP python scripts to use a &quot;shebang&quot; line that invokes <code>pcp-python</code> as follows: </p>
<pre>
<i>#!/usr/bin/pcp python</i>
</pre>
<p> This allows the custom setting to be injected instead of a hard-coded python version, while still allowing the user to override the python version as follows: </p>
<pre>
<code>$ PCP_PYTHON_PROG=python3 /usr/bin/pcp python --version</code>
Python 3.3.2
<code>$ PCP_PYTHON_PROG=python2 /usr/bin/pcp python --version</code>
Python 2.7.5
</pre>
<p> This is convenient for shipping identical scripts on multiple platforms, and for testing different python versions with the one script (e.g. in the case where multiple versions of python are installed, PCP_PYTHON_PROG can be set in the local environment to override the global setting). </p>
<p> By default, the value of PCP_PYTHON_PROG from <i>/etc/pcp.conf</i> will be used. The default value of this configuration parameter is set depending on some heuristics about the target build platform. These heuristics favour the use of <i>python3</i> in all recent releases of PCP, for those platforms that support it.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1) and <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<h2>Index</h2>
