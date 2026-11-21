---
title: "pmdamysql(1)"
name: "pmdamysql"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdamysql/"
description: "pmdamysql – MySQL database PMDA"
---

<h2>NAME</h2>
<p> <code>pmdamysql</code> &#8211; MySQL database PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdamysql</code> is a Performance Co-Pilot <font SIZE="-1">PMDA</font> which extracts live performance data from a running MySQL database.</p>
<h2>INSTALLATION</h2>
<p> <code>pmdamysql</code> uses a configuration file from (in this order):</p>
<dl>
<dt>&bull;</dt>
<dd> /etc/pcpdbi.conf</dd>
<dt>&bull;</dt>
<dd> <tt>$PCP_PMDAS_DIR</tt>/mysql/mysql.conf</dd></dl>
<p> This file can contain overridden values (Perl code) for the settings listed at the start of pmdamysql.pl, namely:</p>
<dl>
<dt>&bull;</dt>
<dd> database name (see <font SIZE="-1"><i>DBI</i></font><i></i>(3) for details)</dd>
<dt>&bull;</dt>
<dd> database username</dd></dl>
<p> Once this is setup, you can access the names and values for the mysql performance metrics by doing the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/mysql </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/mysql </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdamysql</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>Binary Status values in text</h2>
<p> Some of the status values are in the form of <font SIZE="-1">YES/NO</font> or <font SIZE="-1">ON/OFF</font>. </p>
<p> Since these cannot be interpreted by tools like <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1), they have been duplicated with a _num extension and the values of 1 (<font SIZE="-1">YES/ON</font>) or 0 (<font SIZE="-1">NO/OFF</font>).</p>
<h3>Eg:</h3>
<dl>
<dt>&bull;</dt>
<dd> mysql.slave_status.slave_io_running</dd>
<dt>&bull;</dt>
<dd> mysql.slave_status.slave_io_running_num</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/pcpdbi.conf</code></dt>
<dd> configuration file for all <font SIZE="-1">PCP</font> database monitors</dd>
<dt><code>$PCP_PMDAS_DIR/mysql/mysql.conf</code></dt>
<dd> configuration file for <code>pmdamysql</code></dd>
<dt><code>$PCP_PMDAS_DIR/mysql/Install</code></dt>
<dd> installation script for the <code>pmdamysql</code> agent</dd>
<dt><code>$PCP_PMDAS_DIR/mysql/Remove</code></dt>
<dd> undo installation script for the <code>pmdamysql</code> agent</dd>
<dt><code>$PCP_LOG_DIR/pmcd/mysql.log</code></dt>
<dd> default log file for error messages from <code>pmdamysql</code></dd></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdadbping/">pmdadbping</a></code>(1), <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) and <code>DBI</code>(3). </p>
