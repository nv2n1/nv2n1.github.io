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
<dt>&bull;</p>
<dd> /etc/pcpdbi.conf</p>
<dt>&bull;</p>
<dd> <tt>$PCP_PMDAS_DIR</tt>/mysql/mysql.conf</dl>
<p> This file can contain overridden values (Perl code) for the settings listed at the start of pmdamysql.pl, namely:</p>
<dl>
<dt>&bull;</p>
<dd> database name (see <font SIZE="-1"><i><a href="/docs/linux/man/3-dbi/">DBI</a></i></font><i></i>(3) for details)</p>
<dt>&bull;</p>
<dd> database username</dl>
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
<dt>&bull;</p>
<dd> mysql.slave_status.slave_io_running</p>
<dt>&bull;</p>
<dd> mysql.slave_status.slave_io_running_num</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/pcpdbi.conf</code></p>
<dd> configuration file for all <font SIZE="-1">PCP</font> database monitors</p>
<dt><code>$PCP_PMDAS_DIR/mysql/mysql.conf</code></p>
<dd> configuration file for <code>pmdamysql</code></p>
<dt><code>$PCP_PMDAS_DIR/mysql/Install</code></p>
<dd> installation script for the <code>pmdamysql</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/mysql/Remove</code></p>
<dd> undo installation script for the <code>pmdamysql</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/mysql.log</code></p>
<dd> default log file for error messages from <code>pmdamysql</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdadbping/">pmdadbping</a></code>(1), <code><a href="/docs/linux/man/1-pmie/">pmie</a></code>(1) and <code><a href="/docs/linux/man/3-dbi/">DBI</a></code>(3). </p>
<h2>Index</h2>
