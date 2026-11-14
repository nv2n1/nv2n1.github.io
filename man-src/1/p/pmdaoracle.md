---
title: "pmdaoracle(1)"
name: "pmdaoracle"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaoracle/"
description: "pmdaoracle – Oracle database PMDA"
---

<h2>NAME</h2>
<p> <code>pmdaoracle</code> &#8211; Oracle database PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdaoracle</code> is a Performance Co-Pilot <font SIZE="-1">PMDA</font> which extracts live performance data from a running Oracle database.</p>
<h2>INSTALLATION</h2>
<p> <code>pmdaoracle</code> uses a configuration file from (in this order):</p>
<dl>
<dt>&bull;</p>
<dd> /etc/pcpdbi.conf</p>
<dt>&bull;</p>
<dd> <tt>$PCP_PMDAS_DIR</tt>/oracle/oracle.conf</p>
<dt>&bull;</p>
<dd> ./oracle.conf</dl>
<p> This file can contain overridden values (Perl code) for the settings listed at the start of pmdaoracle.pl, for example:</p>
<dl>
<dt>&bull;</p>
<dd> $username &#8211; username to connect to the database [default: &#8216;SYSTEM&#8217;]</p>
<dt>&bull;</p>
<dd> $password &#8211; password to connect to the database [default: &#8216;manager&#8217;]</p>
<dt>&bull;</p>
<dd> $host &#8211; host the database is running on [default: &#8216;localhost&#8217;]</p>
<dt>&bull;</p>
<dd> $port &#8211; port the database is listening on [default: &#8216;1521&#8217;]</p>
<dt>&bull;</p>
<dd> $os_user &#8211; operating system username (PMDA will run with the corresponding user id) [default: oracle]</p>
<dt>&bull;</p>
<dd> @sids &#8211; an array of $ORACLE_SID database identifiers [default: (&#8216;master&#8217;)]</dl>
<p> In order to test your local settings, a simple script is provided that will connect and disconnect from the database &#8211; verifying fundamental configuration is in place before continuing on. If the <code>$PCP_PMDAS_DIR/oracle/connect.pl</code> script cannot connect, do not proceed with installation of the PMDA as it will be unsuccessful. Correct your local settings first. </p>
<p> Once this is setup, you can access the names and values for the oracle performance metrics by doing the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/oracle </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/oracle </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdaoracle</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>CONNECTION STATE</h2>
<p> By default, <code>pmdaoracle</code> will aggressively attempt to maintain persistent connections to Oracle to ensure timely responses to its queries, and will automatically re-connect if a connection drops. </p>
<p> However, in certain circumstances this may be undesirable, so a manual <code><a href="/docs/linux/man/3-pmstore/">pmStore</a></code>(3) mechanism is provided to explicitly control disconnecting and reconnecting to an Oracle instance. This can be used, for example, to ensure that <code>pmdaoracle</code> is not connected at shutdown, to ensure a clean Oracle shutdown process. </p>
<p> The <code>pmstore (1)</code> command can be used to disconnect and reconnect. Using the individual instances of the oracle.control.connected metric, one can set the connection state to either up (1) or down (0). Additionally, <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1) can report on the current status of Oracle connections. </p>
<pre><code>
#pminfo - f oracle.control.connected
oracle.control.connected
    inst[0 or "master"] value 1
#pmstore oracle.control.connected 0
    oracle.control.connected inst[0 or "master"] old value = 1 new value = 0
</code></pre>
<h2>FILES</h2>
<dl>
<dt><code>/etc/pcpdbi.conf</code></p>
<dd> configuration file for all <font SIZE="-1">PCP</font> database monitors</p>
<dt><code>$PCP_PMDAS_DIR/oracle/oracle.conf</code></p>
<dd> configuration file for <code>pmdaoracle</code></p>
<dt><code>$PCP_PMDAS_DIR/oracle/sample.conf</code></p>
<dd> example configuration file for <code>pmdaoracle</code> using $LD_LIBRARY_PATH</p>
<dt><code>$PCP_PMDAS_DIR/oracle/connect.pl</code></p>
<dd> configuration test script for <code>Oracle</code> database connectivity</p>
<dt><code>$PCP_PMDAS_DIR/oracle/Install</code></p>
<dd> installation script for the <code>pmdaoracle</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/oracle/Remove</code></p>
<dd> undo installation script for the <code>pmdaoracle</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/oracle.log</code></p>
<dd> default log file for error messages from <code>pmdaoracle</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmdadbping/">pmdadbping</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1), <code><a href="/docs/linux/man/3-dbi/">DBI</a></code>(3) and <code><a href="/docs/linux/man/3-pmstore/">pmStore</a></code>(3). </p>
<h2>Index</h2>
