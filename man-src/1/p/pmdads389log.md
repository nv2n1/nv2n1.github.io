---
title: "pmdads389log(1)"
name: "pmdads389log"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdads389log/"
description: "pmdads389log – 389 Directory Server Log PMDA"
---

<h2>NAME</h2>
<p> <code>pmdads389log</code> &#8211; 389 Directory Server Log PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdads389log</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which extracts statistics from 389 Directory Server access log using the <code><a href="/docs/linux/man/1-logconv-pl/">logconv.pl</a></code>(1) utility.</p>
<h2>INSTALLATION</h2>
<p> <code>pmdads389log</code> uses a configuration file</p>
<dl>
<dt>&bull;</p>
<dd> <i>$PCP_PMDAS_DIR/ds389log/ds389log.conf</i></dl>
<p> This file can contain overridden values (Perl code) for the settings listed at the start of <i>pmdads389log.pl</i>, namely:</p>
<dl>
<dt>&bull;</p>
<dd> <code>logconv.pl</code> parameters</p>
<dt>&bull;</p>
<dd> minimal query interval</p>
<dt>&bull;</p>
<dd> 389 <font SIZE="-1">DS</font> access log to use</p>
<dt>&bull;</p>
<dd> 389 <font SIZE="-1">DS</font> log directory to use (used if no file specified)</p>
<dt>&bull;</p>
<dd> non-root user having read access to the access log file</dl>
<p> Once this is setup, you can access the names and values for the 389 DS performance metrics by doing the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/ds389log </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/ds389log </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdads389log</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/ds389log/ds389log.conf</code></p>
<dd> configuration file for the <code>pmdads389log</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/ds389log/Install</code></p>
<dd> installation script for the <code>pmdads389log</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/ds389log/Remove</code></p>
<dd> undo installation script for the <code>pmdads389log</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/ds389log.log</code></p>
<dd> default log file for error messages from <code>pmdads389log</code></p>
<dt><code>/var/log/dirsrv/slapd-&#8230;/access</code></p>
<dd> 389 Directory Server access log parsed by <code>logconv.pl</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-logconv-pl/">logconv.pl</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/1-pmdads389/">pmdads389</a></code>(1). </p>
<h2>Index</h2>
