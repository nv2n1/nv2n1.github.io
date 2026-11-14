---
title: "pmdapostgresql(1)"
name: "pmdapostgresql"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdapostgresql/"
description: "pmdapostgresql – PostgreSQL database PMDA"
---

<h2>NAME</h2>
<p> <code>pmdapostgresql</code> &#8211; PostgreSQL database PMDA</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdapostgresql</code> is a Performance Co-Pilot <font SIZE="-1">PMDA</font> which extracts live performance data from a running PostgreSQL database.</p>
<h2>INSTALLATION</h2>
<p> <code>pmdapostgresql</code> uses a configuration file from (in this order):</p>
<dl>
<dt>&bull;</p>
<dd> /etc/pcpdbi.conf</p>
<dt>&bull;</p>
<dd> <tt>$PCP_PMDAS_DIR</tt>/postgresql/postgresql.conf</p>
<dt>&bull;</p>
<dd> ./postgresql.conf</dl>
<p> This file can contain overridden values (Perl code) for the settings listed at the start of pmdapostgresql.pl, for example:</p>
<dl>
<dt>&bull;</p>
<dd> $database &#8211; database access method and database name, [default: &#8216;dbi:Pg:dbname=postgres&#8217;] (see <font SIZE="-1"><i><a href="/docs/linux/man/3-dbi/">DBI</a></i></font><i></i>(3) for details)</p>
<dt>&bull;</p>
<dd> $username &#8211; username to connect to the database [default: &#8216;postgres&#8217;]</p>
<dt>&bull;</p>
<dd> $password &#8211; password to connect to the database [default: &#8221;]</p>
<dt>&bull;</p>
<dd> $os_user &#8211; operating system username (PMDA will run with the corresponding user id) [default: $username]</dl>
<p> Once this is setup, you can access the names and values for the postgresql performance metrics by doing the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/postgresql </p>
<p>#&nbsp;<wbr>./Install </p>
<p> To uninstall, do the following as root: </p>
<p>#&nbsp;<wbr>cd&nbsp;<wbr>$PCP_PMDAS_DIR/postgresql </p>
<p>#&nbsp;<wbr>./Remove </p>
<p> <code>pmdapostgresql</code> is launched by <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) and should never be executed directly. The Install and Remove scripts notify <i><a href="/docs/linux/man/1-pmcd/">pmcd</a></i>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/pcpdbi.conf</code></p>
<dd> configuration file for all <font SIZE="-1">PCP</font> database monitors</p>
<dt><code>$PCP_PMDAS_DIR/postgresql/postgresql.conf</code></p>
<dd> configuration file for <code>pmdapostgresql</code></p>
<dt><code>$PCP_PMDAS_DIR/postgresql/Install</code></p>
<dd> installation script for the <code>pmdapostgresql</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/postgresql/Remove</code></p>
<dd> undo installation script for the <code>pmdapostgresql</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/postgresql.log</code></p>
<dd> default log file for error messages from <code>pmdapostgresql</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by <code>PCP</code>. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <i><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></i>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmdadbping/">pmdadbping</a></code>(1) and <code><a href="/docs/linux/man/3-dbi/">DBI</a></code>(3). </p>
<h2>Index</h2>
