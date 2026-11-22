---

title: "pmdads389(1)"
name: "pmdads389"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdads389/"
description: "pmdads389 – 389 Directory Server PMDA"
---

<p> <code>pmdads389</code> &#8211; 389 Directory Server PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdads389</code> is a Performance Metrics Domain Agent (PMDA) which extracts live performance data from a running 389 Directory Server instance. </p>
<p> See the Red Hat Directory Server Administration Guide for description for each metric. </p>
<h2>INSTALLATION</h2>
<p> <code>pmdads389</code> uses a configuration file</p>
<dl>
<dt>&bull;</dt>
<dd> <i>$PCP_PMDAS_DIR/ds389/ds389.conf</i></dd></dl>
<p> This file can contain overridden values (Perl code) for the settings listed at the start of <i>pmdads389.pl</i>, namely:</p>
<dl>
<dt>&bull;</dt>
<dd> LDAP server</dd>
<dt>&bull;</dt>
<dd> bind DN</dd>
<dt>&bull;</dt>
<dd> bind password</dd>
<dt>&bull;</dt>
<dd> search scope</dd>
<dt>&bull;</dt>
<dd> search base</dd>
<dt>&bull;</dt>
<dd> search filter</dd>
<dt>&bull;</dt>
<dd> query interval</dd></dl>
<p> Once this is setup, you can access the names and values for the 389 DS performance metrics by doing the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/ds389 </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/ds389 </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdads389</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/ds389/ds389.conf</code></dt>
<dd> configuration file for the <code>pmdads389</code> agent</dd>
<dt><code>$PCP_PMDAS_DIR/ds389/Install</code></dt>
<dd> installation script for the <code>pmdads389</code> agent</dd>
<dt><code>$PCP_PMDAS_DIR/ds389/Remove</code></dt>
<dd> undo installation script for the <code>pmdads389</code> agent</dd>
<dt><code>$PCP_LOG_DIR/pmcd/ds389.log</code></dt>
<dd> default log file for error messages from <code>pmdads389</code></dd></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/8-ns-slapd/">ns-slapd</a></code>(8). </p>
