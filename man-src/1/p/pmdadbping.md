---

title: "pmdadbping(1)"
name: "pmdadbping"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdadbping/"
description: "pmdadbping – database response time and availability PMDA"
---

<p> <code>pmdadbping</code> &#8211; database response time and availability PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdadbping</code> is a database response time measurement PMDA. </p>
<p> <code>pmdadbping</code> runs <code><a href="/docs/linux/man/1-dbprobe/">dbprobe</a></code>(1), and exports the performance measurements it makes available as PCP metrics. </p>
<p> <code><a href="/docs/linux/man/1-dbprobe/">dbprobe</a></code>(1) should be configured to use the type of DBI appropriate for the local database, which includes: RDBMS flavour, user/password, delay between &quot;ping&quot; requests, and the SQL statement to use.</p>
<h2>INSTALLATION</h2>
<p> Configure <code><a href="/docs/linux/man/1-dbprobe/">dbprobe</a></code>(1) &#8211; it uses a configuration file from (in this order):</p>
<dl>
<dt>&bull;</dt>
<dd> /etc/pcpdbi.conf</dd>
<dt>&bull;</dt>
<dd> <tt>$PCP_PMDAS_DIR</tt>/dbping/dbprobe.conf</dd></dl>
<p> This file can contain overridden values (Perl code) for the settings listed at the start of <i>dbprobe.pl</i>, namely:</p>
<dl>
<dt>&bull;</dt>
<dd> database name (see <code>DBI</code>(3) for details)</dd>
<dt>&bull;</dt>
<dd> database user name</dd>
<dt>&bull;</dt>
<dd> database pass word</dd>
<dt>&bull;</dt>
<dd> SQL statement to measure (probe)</dd>
<dt>&bull;</dt>
<dd> delay between probes</dd></dl>
<p> Once this is setup, you can access the names and values for the dbping performance metrics by doing the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/dbping </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/dbping </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdadbping</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/dbping/dbprobe.conf</code></dt>
<dd> probe configuration file for <i><a href="/docs/linux/man/1-dbprobe/">dbprobe</a></i>(1), used indirectly by <code>pmdadbping</code></dd>
<dt><code>$PCP_PMDAS_DIR/dbping/Install</code></dt>
<dd> installation script for the <code>pmdadbping</code> agent</dd>
<dt><code>$PCP_PMDAS_DIR/dbping/Remove</code></dt>
<dd> undo installation script for the <code>pmdadbping</code> agent</dd>
<dt><code>$PCP_LOG_DIR/pmcd/dbping.log</code></dt>
<dd> default log file for error messages from <code>pmdadbping</code></dd></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dbprobe/">dbprobe</a></code>(1) <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) and <code>DBI</code>(3). </p>
