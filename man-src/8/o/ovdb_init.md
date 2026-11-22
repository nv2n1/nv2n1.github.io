---
title: "ovdb_init(8)"
name: "ovdb_init"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovdb_init/"
description: "ovdb_init – Prepare ovdb database for use"
---

<p>ovdb_init &#8211; Prepare ovdb database for use</p>
<h2>Synopsis</h2>
<p>ovdb_init [<tt>&quot;-u&quot;</tt>|<tt>&quot;-r&quot;</tt>]</p>
<h2>Description</h2>
<p>This command must be run before any other process can access the overview database. It performs the following steps:</p>
<dl>
<dt>1.</dt>
<dd>Creates the database environment, if necessary</dd>
<dt>2.</dt>
<dd>If the database is idle (and if the <tt>&quot;-u&quot;</tt> option is not specified), it performs a normal recovery. The recovery will remove stale locks, recreate the memory pool cache, and repair any damage caused by a system crash or improper shutdown.</dd>
<dt>3.</dt>
<dd>If the <tt>&quot;-u&quot;</tt> option is specified, it performs any necessary upgrades to the database. See the UPGRADING section below.</dd>
<dt>4.</dt>
<dd>Starts the DB housekeeping processes (ovdb_monitor) if they&#8217;re not already running. (Unless the <tt>&quot;-r&quot;</tt> option is specified).</dd>
<dt>5.</dt>
<dd>Starts the ovdb readserver (ovdb_server) processes if <i>readserver</i> in <i>ovdb.conf</i> is true, and if they are not already running. (Unless the <tt>&quot;-r&quot;</tt> option is specified).</dd></dl>
<p> Returns exit status of 0 if all steps were completed successfully. In the event of an error, messages are written to syslog and/or stderr. </p>
<p> If a recovery was attempted but it failed, the database may be damaged beyond repair, requiring a rebuild with <i><a href="/docs/linux/man/8-makehistory/">makehistory</a></i>(8). </p>
<p> This command is normally invoked automatically by <i><a href="/docs/linux/man/8-rc-news/">rc.news</a></i>(8). </p>
<p> It is OK to run this command multiple times.</p>
<h2>Options</h2>
<dl>
<dt>&quot;-r&quot;</dt>
<dd>Perform recovery only. <tt>&quot;ovdb_monitor&quot;</tt> is not started.</dd>
<dt>&quot;-u&quot;</dt>
<dd>Perform any needed upgrades. Recovery is not attempted. <tt>&quot;ovdb_monitor&quot;</tt> is started if the upgrade succeeded.</dd></dl>
<h2>Upgrading</h2>
<p>There are two situations in which the database will need to be upgraded:</p>
<dl>
<dt>&bull;</dt>
<dd>You upgrade the Berkeley&nbsp;<wbr>DB library to a newer version, for example from 2.7.7 to 3.1.17. In this case, the Berkeley&nbsp;<wbr>DB db-&gt;<i>upgrade()</i> method is used.</dd>
<dt>&bull;</dt>
<dd>You upgrade ovdb to a newer major version; i.e., ovdb-1.0 to ovdb-2.0.</dd></dl>
<p> In both of these cases, the database is upgraded in-place; and the upgrade can not be undone. Do not interrupt the upgrade process once it has started, because there is a risk of irrepairable corruption. The upgrade may take several minutes to complete. If an upgrade does get interrupted, try running the upgrade again. </p>
<p> Here&#8217;s an example procedure to upgrade a database created with Berkeley&nbsp;<wbr>DB&nbsp;<wbr>2.7.7 to use Berkeley&nbsp;<wbr>DB&nbsp;<wbr>3.1.17:</p>
<dl>
<dt>1.</dt>
<dd>Build and install the Berkeley&nbsp;<wbr>DB&nbsp;<wbr>3.1.17;</dd>
<dt>2.</dt>
<dd>Run configure in the INN source tree and make sure it picks up the right Berkeley&nbsp;<wbr>DB directory (e.g., <i>/usr/local/BerkeleyDB.3.1</i>);</dd>
<dt>3.</dt>
<dd>Do a <tt>&quot;make&quot;</tt>;</dd>
<dt>4.</dt>
<dd>Shut down INN (e.g., with <tt>&quot;rc.news stop&quot;</tt>) and be sure to kill all instances of <code>nnrpd</code> as well;</dd>
<dt>5.</dt>
<dd>Do a <tt>&quot;make update&quot;</tt> to install the new binaries;</dd>
<dt>6.</dt>
<dd>Run <tt>&quot;ovdb_init -u&quot;</tt> as the news user;</dd>
<dt>7.</dt>
<dd>Start INN with <tt>&quot;rc.news&quot;</tt>.</dd></dl>
<p> It is OK to specify <tt>&quot;-u&quot;</tt> even if no upgrades are needed.</p>
<h2>History</h2>
<p>Written by Heath Kehoe &lt;hakehoe [at] avalon.net&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> ovdb_init.pod 9766 2014-12-07 21:08:08Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-ovdb/">ovdb</a></i>(5), <i><a href="/docs/linux/man/8-makehistory/">makehistory</a></i>(8) </p>
