---
title: "pmdads389(1)"
name: "pmdads389"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdads389/"
description: "pmdads389 – 389 Directory Server PMDA"
---

<h2>NAME</h2>
<p> <code>pmdads389</code> &#8211; 389 Directory Server PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdads389</code> is a Performance Metrics Domain Agent (<font SIZE="-1">PMDA</font>) which extracts live performance data from a running 389 Directory Server instance. </p>
<p> See the Red Hat Directory Server Administration Guide for description for each metric. </p>
<h2>INSTALLATION</h2>
<p> <code>pmdads389</code> uses a configuration file</p>
<dl>
<dt>&bull;</p>
<dd> <i>$PCP_PMDAS_DIR/ds389/ds389.conf</i></dl>
<p> This file can contain overridden values (Perl code) for the settings listed at the start of <i>pmdads389.pl</i>, namely:</p>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">LDAP</font> server</p>
<dt>&bull;</p>
<dd> bind <font SIZE="-1">DN</font></p>
<dt>&bull;</p>
<dd> bind password</p>
<dt>&bull;</p>
<dd> search scope</p>
<dt>&bull;</p>
<dd> search base</p>
<dt>&bull;</p>
<dd> search filter</p>
<dt>&bull;</p>
<dd> query interval</dl>
<p> Once this is setup, you can access the names and values for the 389 DS performance metrics by doing the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/ds389 </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/ds389 </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdads389</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/ds389/ds389.conf</code></p>
<dd> configuration file for the <code>pmdads389</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/ds389/Install</code></p>
<dd> installation script for the <code>pmdads389</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/ds389/Remove</code></p>
<dd> undo installation script for the <code>pmdads389</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/ds389.log</code></p>
<dd> default log file for error messages from <code>pmdads389</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/8-ns-slapd/">ns-slapd</a></code>(8). </p>
<h2>Index</h2>
