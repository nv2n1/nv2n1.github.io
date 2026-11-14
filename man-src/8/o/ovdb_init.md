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
<dt>1.</p>
<dd>Creates the database environment, if necessary</p>
<dt>2.</p>
<dd>If the database is idle (and if the <tt>&quot;-u&quot;</tt> option is not specified), it performs a normal recovery. The recovery will remove stale locks, recreate the memory pool cache, and repair any damage caused by a system crash or improper shutdown.</p>
<dt>3.</p>
<dd>If the <tt>&quot;-u&quot;</tt> option is specified, it performs any necessary upgrades to the database. See the <font SIZE="-1">UPGRADING</font> section below.</p>
<dt>4.</p>
<dd>Starts the <font SIZE="-1">DB</font> housekeeping processes (ovdb_monitor) if they&#8217;re not already running. (Unless the <tt>&quot;-r&quot;</tt> option is specified).</p>
<dt>5.</p>
<dd>Starts the ovdb readserver (ovdb_server) processes if <i>readserver</i> in <i>ovdb.conf</i> is true, and if they are not already running. (Unless the <tt>&quot;-r&quot;</tt> option is specified).</dl>
<p> Returns exit status of 0 if all steps were completed successfully. In the event of an error, messages are written to syslog and/or stderr. </p>
<p> If a recovery was attempted but it failed, the database may be damaged beyond repair, requiring a rebuild with <i><a href="/docs/linux/man/8-makehistory/">makehistory</a></i>(8). </p>
<p> This command is normally invoked automatically by <i><a href="/docs/linux/man/8-rc-news/">rc.news</a></i>(8). </p>
<p> It is <font SIZE="-1">OK</font> to run this command multiple times.</p>
<h2>Options</h2>
<dl>
<dt>&quot;-r&quot;</p>
<dd>Perform recovery only. <tt>&quot;ovdb_monitor&quot;</tt> is not started.</p>
<dt>&quot;-u&quot;</p>
<dd>Perform any needed upgrades. Recovery is not attempted. <tt>&quot;ovdb_monitor&quot;</tt> is started if the upgrade succeeded.</dl>
<h2>Upgrading</h2>
<p>There are two situations in which the database will need to be upgraded:</p>
<dl>
<dt>&bull;</p>
<dd>You upgrade the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> library to a newer version, for example from 2.7.7 to 3.1.17. In this case, the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> db-&gt;<i>upgrade()</i> method is used.</p>
<dt>&bull;</p>
<dd>You upgrade ovdb to a newer major version; i.e., ovdb-1.0 to ovdb-2.0.</dl>
<p> In both of these cases, the database is upgraded in-place; and the upgrade can not be undone. Do not interrupt the upgrade process once it has started, because there is a risk of irrepairable corruption. The upgrade may take several minutes to complete. If an upgrade does get interrupted, try running the upgrade again. </p>
<p> Here&#8217;s an example procedure to upgrade a database created with Berkeley&nbsp;<wbr><font SIZE="-1">DB</font>&nbsp;<wbr>2.7.7 to use Berkeley&nbsp;<wbr><font SIZE="-1">DB</font>&nbsp;<wbr>3.1.17:</p>
<dl>
<dt>1.</p>
<dd>Build and install the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font>&nbsp;<wbr>3.1.17;</p>
<dt>2.</p>
<dd>Run configure in the <font SIZE="-1">INN</font> source tree and make sure it picks up the right Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> directory (e.g., <i>/usr/local/BerkeleyDB.3.1</i>);</p>
<dt>3.</p>
<dd>Do a <tt>&quot;make&quot;</tt>;</p>
<dt>4.</p>
<dd>Shut down <font SIZE="-1">INN</font> (e.g., with <tt>&quot;rc.news stop&quot;</tt>) and be sure to kill all instances of <code>nnrpd</code> as well;</p>
<dt>5.</p>
<dd>Do a <tt>&quot;make update&quot;</tt> to install the new binaries;</p>
<dt>6.</p>
<dd>Run <tt>&quot;ovdb_init -u&quot;</tt> as the news user;</p>
<dt>7.</p>
<dd>Start <font SIZE="-1">INN</font> with <tt>&quot;rc.news&quot;</tt>.</dl>
<p> It is <font SIZE="-1">OK</font> to specify <tt>&quot;-u&quot;</tt> even if no upgrades are needed.</p>
<h2>History</h2>
<p>Written by Heath Kehoe &lt;hakehoe [at] avalon.net&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> ovdb_init.pod 9766 2014-12-07 21:08:08Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-ovdb/">ovdb</a></i>(5), <i><a href="/docs/linux/man/8-makehistory/">makehistory</a></i>(8) </p>
