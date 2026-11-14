---
title: "pg_upgrade(1)"
name: "pg_upgrade"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pg_upgrade/"
description: "pg_upgrade – upgrade a PostgreSQL server instance"
---

<h2 class="name">NAME</h2>
<p> pg_upgrade &#8211; upgrade a PostgreSQL server instance </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pg_upgrade</code> <code>-b</code> <i>oldbindir</i> <code>-B</code> <i>newbindir</i> <code>-d</code> <i>olddatadir</i> <code>-D</code> <i>newdatadir</i> [<i>option</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>pg_upgrade (formerly called pg_migrator) allows data stored in PostgreSQL data files to be upgraded to a later PostgreSQL major version without the data dump/reload typically required for major version upgrades, e.g. from 8.4.7 to the current major release of PostgreSQL. It is not required for minor version upgrades, e.g. from 9.0.1 to 9.0.4. </p>
<p> Major PostgreSQL releases regularly add new features that often change the layout of the system tables, but the internal data storage format rarely changes. pg_upgrade uses this fact to perform rapid upgrades by creating new system tables and simply reusing the old user data files. If a future major release ever changes the data storage format in a way that makes the old data format unreadable, pg_upgrade will not be usable for such upgrades. (The community will attempt to avoid such situations.) </p>
<p> pg_upgrade does its best to make sure the old and new clusters are binary-compatible, e.g. by checking for compatible compile-time settings, including 32/64-bit binaries. It is important that any external modules are also binary compatible, though this cannot be checked by pg_upgrade. </p>
<p> pg_upgrade supports upgrades from 8.3.X and later to the current major release of PostgreSQL, including snapshot and alpha releases.</p>
<h2>OPTIONS</h2>
<p> pg_upgrade accepts the following command-line arguments: </p>
<p> <code>-b</code> <i>old_bindir</i>, <code>&#8211;old-bindir=</code><i>old_bindir</i></p>
<dl>
<dt>
<dd> the old cluster executable directory; environment variable <code>PGBINOLD</code></dl>
<p> <code>-B</code> <i>new_bindir</i>, <code>&#8211;new-bindir=</code><i>new_bindir</i></p>
<dl>
<dt>
<dd> the new cluster executable directory; environment variable <code>PGBINNEW</code></dl>
<p> <code>-c</code>, <code>&#8211;check</code></p>
<dl>
<dt>
<dd> check clusters only, don&#8217;t change any data</dl>
<p> <code>-d</code> <i>old_datadir</i>, <code>&#8211;old-datadir=</code><i>old_datadir</i></p>
<dl>
<dt>
<dd> the old cluster data directory; environment variable <code>PGDATAOLD</code></dl>
<p> <code>-D</code> <i>new_datadir</i>, <code>&#8211;new-datadir=</code><i>new_datadir</i></p>
<dl>
<dt>
<dd> the new cluster data directory; environment variable <code>PGDATANEW</code></dl>
<p> <code>-k</code>, <code>&#8211;link</code></p>
<dl>
<dt>
<dd> use hard links instead of copying files to the new cluster</dl>
<p> <code>-o</code> <i>options</i>, <code>&#8211;old-options</code> <i>options</i></p>
<dl>
<dt>
<dd> options to be passed directly to the old <code>postgres</code> command</dl>
<p> <code>-O</code> <i>options</i>, <code>&#8211;new-options</code> <i>options</i></p>
<dl>
<dt>
<dd> options to be passed directly to the new <code>postgres</code> command</dl>
<p> <code>-p</code> <i>old_port_number</i>, <code>&#8211;old-port=</code><i>old_portnum</i></p>
<dl>
<dt>
<dd> the old cluster port number; environment variable <code>PGPORTOLD</code></dl>
<p> <code>-P</code> <i>new_port_number</i>, <code>&#8211;new-port=</code><i>new_portnum</i></p>
<dl>
<dt>
<dd> the new cluster port number; environment variable <code>PGPORTNEW</code></dl>
<p> <code>-r</code>, <code>&#8211;retain</code></p>
<dl>
<dt>
<dd> retain SQL and log files even after successful completion</dl>
<p> <code>-u</code> <i>user_name</i>, <code>&#8211;user=</code><i>user_name</i></p>
<dl>
<dt>
<dd> cluster&#8217;s super user name; environment variable <code>PGUSER</code></dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> enable verbose internal logging</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> display version information, then exit</dl>
<p> <code>-?</code>, <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> show help, then exit</dl>
<h2>USAGE</h2>
<p> These are the steps to perform an upgrade with pg_upgrade: </p>
<dl>
<dt>
<dd> 1. Optionally move the old cluster: If you are using a version-specific installation directory, e.g. /opt/PostgreSQL/9.1, you do not need to move the old cluster. The graphical installers all use version-specific installation directories. </p>
<p> If your installation directory is not version-specific, e.g. /usr/local/pgsql, it is necessary to move the current PostgreSQL install directory so it does not interfere with the new PostgreSQL installation. Once the current PostgreSQL server is shut down, it is safe to rename the PostgreSQL installation directory; assuming the old directory is /usr/local/pgsql, you can do: </p>
<dl>
<dt>
<dd>
<pre>
mv /usr/local/pgsql /usr/local/pgsql.old
</pre>
</dl>
<p> to rename the directory.</dl>
<dl>
<dt>
<dd> 2. For source installs, build the new version: Build the new PostgreSQL source with <code>configure</code> flags that are compatible with the old cluster. pg_upgrade will check <code>pg_controldata</code> to make sure all settings are compatible before starting the upgrade.</dl>
<dl>
<dt>
<dd> 3. Install the new PostgreSQL binaries: Install the new server&#8217;s binaries and support files. </p>
<p> For source installs, if you wish to install the new server in a custom location, use the prefix variable: </p>
<dl>
<dt>
<dd>
<pre>
gmake prefix=/usr/local/pgsql.new install
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 4. Install pg_upgrade and pg_upgrade_support: Install the pg_upgrade binary and pg_upgrade_support library in the new PostgreSQL cluster.</dl>
<dl>
<dt>
<dd> 5. Initialize the new PostgreSQL cluster: Initialize the new cluster using <code>initdb</code>. Again, use compatible <code>initdb</code> flags that match the old cluster. Many prebuilt installers do this step automatically. There is no need to start the new cluster.</dl>
<dl>
<dt>
<dd> 6. Install custom shared object files: Install any custom shared object files (or DLLs) used by the old cluster into the new cluster, e.g. pgcrypto.so, whether they are from contrib or some other source. Do not install the schema definitions, e.g. pgcrypto.sql, because these will be upgraded from the old cluster.</dl>
<dl>
<dt>
<dd> 7. Adjust authentication: <code>pg_upgrade</code> will connect to the old and new servers several times, so you might want to set authentication to peer in pg_hba.conf or use a ~/.pgpass file (see Section 31.15, &#8220;The Password File&#8221;, in the documentation).</dl>
<dl>
<dt>
<dd> 8. Stop both servers: Make sure both database servers are stopped using, on Unix, e.g.: </p>
<dl>
<dt>
<dd>
<pre>
pg_ctl -D /opt/PostgreSQL/8.4 stop
pg_ctl -D /opt/PostgreSQL/9.0 stop
</pre>
</dl>
<p> or on Windows, using the proper service names: </p>
<dl>
<dt>
<dd>
<pre>
NET STOP postgresql-8.4
NET STOP postgresql-9.0
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
NET STOP pgsql-8.3  (PostgreSQL 8.3 and older used a different service name)
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 9. Run pg_upgrade: Always run the pg_upgrade binary of the new server, not the old one. pg_upgrade requires the specification of the old and new cluster&#8217;s data and executable (bin) directories. You can also specify user and port values, and whether you want the data linked instead of copied (the default). </p>
<p> If you use link mode, the upgrade will be much faster (no file copying), but you will not be able to access your old cluster once you start the new cluster after the upgrade. Link mode also requires that the old and new cluster data directories be in the same file system. See pg_upgrade &#8211;help for a full list of options. </p>
<p> For Windows users, you must be logged into an administrative account, and then start a shell as the postgres user and set the proper path: </p>
<dl>
<dt>
<dd>
<pre>
RUNAS /USER:postgres &quot;CMD.EXE&quot;
SET PATH=%PATH%;C:\Program Files\PostgreSQL\9.0in;
</pre>
</dl>
<p> and then run pg_upgrade with quoted directories, e.g.: </p>
<dl>
<dt>
<dd>
<pre><code>
pg_upgrade.exe-- old - datadir "C:/Program Files/PostgreSQL/8.4/data" --new - datadir "C:/Program Files/PostgreSQL/9.0/data" --old - bindir "C:/Program Files/PostgreSQL/8.4/bin" --new - bindir "C:/Program Files/PostgreSQL/9.0/bin"
</code></pre>
</dl>
<p> Once started, <code>pg_upgrade</code> will verify the two clusters are compatible and then do the upgrade. You can use <code>pg_upgrade &#8211;check</code> to perform only the checks, even if the old server is still running. <code>pg_upgrade &#8211;check</code> will also outline any manual adjustments you will need to make after the upgrade. If you are going to be using link mode, you should use the <code>&#8211;link</code> option with <code>&#8211;check</code> to enable link-mode-specific checks. <code>pg_upgrade</code> requires write permission in the current directory. </p>
<p> Obviously, no one should be accessing the clusters during the upgrade. pg_upgrade defaults to running servers on port 50432 to avoid unintended client connections. You can use the same port number for both clusters when doing an upgrade because the old and new clusters will not be running at the same time. However, when checking an old running server, the old and new port numbers must be different. </p>
<p> If an error occurs while restoring the database schema, <code>pg_upgrade</code> will exit and you will have to revert to the old cluster as outlined in Step 14 below. To try <code>pg_upgrade</code> again, you will need to modify the old cluster so the pg_upgrade schema restore succeeds. If the problem is a contrib module, you might need to uninstall the contrib module from the old cluster and install it in the new cluster after the upgrade, assuming the module is not being used to store user data.</dl>
<dl>
<dt>
<dd> 10. Restore pg_hba.conf: If you modified pg_hba.conf, restore its original settings. It might also be necessary to adjust other configuration files in the new cluster to match the old cluster, e.g. postgresql.conf.</dl>
<dl>
<dt>
<dd> 11. Post-Upgrade processing: If any post-upgrade processing is required, pg_upgrade will issue warnings as it completes. It will also generate script files that must be run by the administrator. The script files will connect to each database that needs post-upgrade processing. Each script should be run using: </p>
<dl>
<dt>
<dd>
<pre>
psql --username postgres --file script.sql postgres
</pre>
</dl>
<p> The scripts can be run in any order and can be deleted once they have been run. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Caution</code> </font><br />
 In general it is unsafe to access tables referenced in rebuild scripts until the rebuild scripts have run to completion; doing so could yield incorrect results or poor performance. Tables not referenced in rebuild scripts can be accessed immediately. </p>
</dl>
</dl>
<dl>
<dt>
<dd> 12. Statistics: Because optimizer statistics are not transferred by <code>pg_upgrade</code>, you will be instructed to run a command to regenerate that information at the end of the upgrade.</dl>
<dl>
<dt>
<dd> 13. Delete old cluster: Once you are satisfied with the upgrade, you can delete the old cluster&#8217;s data directories by running the script mentioned when <code>pg_upgrade</code> completes. You can also delete the old installation directories (e.g. bin, share).</dl>
<dl>
<dt>
<dd> 14. Reverting to old cluster: If, after running <code>pg_upgrade</code>, you wish to revert to the old cluster, there are several options: </p>
<dl>
<dt>
<dd> &bull; If you ran <code>pg_upgrade</code> with <code>&#8211;check</code>, no modifications were made to the old cluster and you can re-use it anytime.</dl>
<dl>
<dt>
<dd> &bull; If you ran <code>pg_upgrade</code> with <code>&#8211;link</code>, the data files are shared between the old and new cluster. If you started the new cluster, the new server has written to those shared files and it is unsafe to use the old cluster.</dl>
<dl>
<dt>
<dd> &bull; If you ran <code>pg_upgrade</code><i>without</i><code>&#8211;link</code> or did not start the new server, the old cluster was not modified except that, if linking started, a .old suffix was appended to $PGDATA/global/pg_control. To reuse the old cluster, possibly remove the .old suffix from $PGDATA/global/pg_control; you can then restart the old cluster.</dl>
</dl>
<h2>NOTES</h2>
<p> pg_upgrade does not support upgrading of databases containing these reg* OID-referencing system data types: regproc, regprocedure, regoper, regoperator, regconfig, and regdictionary. (regtype can be upgraded.) </p>
<p> All failure, rebuild, and reindex cases will be reported by pg_upgrade if they affect your installation; post-upgrade scripts to rebuild tables and indexes will be generated automatically. </p>
<p> For deployment testing, create a schema-only copy of the old cluster, insert dummy data, and upgrade that. </p>
<p> If you are upgrading a pre-PostgreSQL 9.2 cluster that uses a configuration-file-only directory, you must pass the real data directory location to pg_upgrade, and pass the configuration directory location to the server, e.g. -d /real-data-directory -o &#8216;-D /configuration-directory&#8217;. </p>
<p> If using a pre-9.1 old server that is using a non-default Unix-domain socket directory or a default that differs from the default of the new cluster, set <code>PGHOST</code> to point to the old server&#8217;s socket location. (This is not relevant on Windows.) </p>
<p> A Log-Shipping Standby Server (Section 25.2, &#8220;Log-Shipping Standby Servers&#8221;, in the documentation) cannot be upgraded because the server must allow writes. The simplest way is to upgrade the primary and use <code>rsync</code> to rebuild the standbys. You can run <code>rsync</code> while the primary is down, or as part of a base backup (Section 24.3.2, &#8220;Making a Base Backup&#8221;, in the documentation) which overwrites the old standby cluster. </p>
<p> If you want to use link mode and you do not want your old cluster to be modified when the new cluster is started, make a copy of the old cluster and upgrade that in link mode. To make a valid copy of the old cluster, use <code>rsync</code> to create a dirty copy of the old cluster while the server is running, then shut down the old server and run <code>rsync</code> again to update the copy with any changes to make it consistent. You might want to exclude some files, e.g. postmaster.pid, as documented in Section 24.3.3, &#8220;Making a Base Backup Using the Low Level API&#8221;, in the documentation.</p>
<h3>Limitations in Upgrading from PostgreSQL 8.3</h3>
<p> Upgrading <i>from</i> PostgreSQL 8.3 has additional restrictions not present when upgrading from later PostgreSQL releases. For example, pg_upgrade will not work for upgrading from 8.3 if a user column is defined as: </p>
<dl>
<dt>
<dd> &bull; a tsquery data type</dl>
<dl>
<dt>
<dd> &bull; data type name and is not the first column</dl>
<p> You must drop any such columns and upgrade them manually. </p>
<p> pg_upgrade will not work if the ltree contrib module is installed in a database. </p>
<p> pg_upgrade will require a table rebuild if: </p>
<dl>
<dt>
<dd> &bull; a user column is of data type tsvector</dl>
<p> pg_upgrade will require a reindex if: </p>
<dl>
<dt>
<dd> &bull; an index is of type hash or GIN</dl>
<dl>
<dt>
<dd> &bull; an index uses <code>bpchar_pattern_ops</code></dl>
<p> Also, the default datetime storage format changed to integer after PostgreSQL 8.3. pg_upgrade will check that the datetime storage format used by the old and new clusters match. Make sure your new cluster is built with the configure flag <code>&#8211;disable-integer-datetimes</code>. </p>
<p> For Windows users, note that due to different integer datetimes settings used by the graphical installer and the MSI installer, it is only possible to upgrade from version 8.3 of the installer distribution to version 8.4 or later of the installer distribution. It is not possible to upgrade from the MSI installer to the new graphical installer.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-initdb/">initdb</a></code>(1), <code><a href="/docs/linux/man/1-pg_ctl/">pg_ctl</a></code>(1), <code><a href="/docs/linux/man/1-pg_dump/">pg_dump</a></code>(1), <code><a href="/docs/linux/man/1-postgres/">postgres</a></code>(1) </p>
<h2>Index</h2>
