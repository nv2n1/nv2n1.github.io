---
title: "pmpython(1)"
name: "pmpython"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmpython/"
description: "pmpython – run a python script using a preferred python variant"
---

<h2>NAME</h2>
<p> <code>pmpython</code> &#8211; run a python script using a preferred python variant</p>
<h2>SYNOPSIS</h2>
<p> <code>pmpython</code> [<i>python-args-and-script</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmpython</code> provides a way to run python scripts using a customisable python interpreter, rather than embedding the name of a particular version of python into each script. </p>
<p> This can be useful as it allows version-independent python code to be run anywhere. All python modules shipped with PCP support versions 2.6 and later (in the python2 series), and 3.3 and later (in the python3 release series). </p>
<p> Due to python monitoring and collecting scripts being relatively simple in PCP (not requiring new modules, language features, etc), it has been possible to ensure they work for all of the above python versions. </p>
<p> However, the name of the python interpreter is not always the same, thus, it is common for PCP python scripts to use a &#8220;shebang&#8221; line that launches the <code>python</code> interpreter indirectly as follows: </p>
<pre>
#!/usr/bin/env pmpython
</pre>
<p> <code><a href="/docs/linux/man/1-env/">env</a></code>(1) is used to find the correct path for the <code>pmpython</code> executable from the user&#8217;s <code>$PATH</code>. </p>
<p> By default the name of the python interpreter is found from the the value of <code>$PCP_PYTHON_PROG</code> from the environment (if set) else from <i>/etc/pcp.conf</i>. The latter is the more typical case where this value is based on some heuristics about the platform at the time the PCP packages were build and favour the use of <i>python3</i> in all recent releases of PCP (for those platforms that support it). </p>
<p> This allows an appropriate name to be used for the python interpreter instead of a hard-coded python version name, while still allowing the user to override the python interpreter as follows: </p>
<pre>
$ PCP_PYTHON_PROG=python3 pmpython --version
Python 3.4.2
$ PCP_PYTHON_PROG=python2 pmpython --version
Python 2.7.9
</pre>
<p> This is convenient for shipping identical scripts on multiple platforms, and for testing different python versions with the one script (e.g. in the case where multiple versions of python are installed, PCP_PYTHON_PROG can be set in the local environment to override the global setting). </p>
<p> <code>pmpython</code> is a replacement for an earlier tool with similar function, namely <code><a href="/docs/linux/man/1-pcp-python/">pcp-python</a></code>(1).</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-env/">env</a></code>(1), <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-pcp-python/">pcp-python</a></code>(1) and <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<h2>Index</h2>
