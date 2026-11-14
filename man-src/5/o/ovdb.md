---
title: "ovdb(5)"
name: "ovdb"
section: "5"
letter: "o"
url: "/docs/linux/man/5-ovdb/"
description: "ovdb – Overview storage method for INN"
---

<p>ovdb &#8211; Overview storage method for INN</p>
<h2>Description</h2>
<p>Ovdb is a storage method that uses the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> library to store overview data. It requires version 4.4 or later of the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> library (4.7+ is recommended because older versions suffer from various issues). </p>
<p> Ovdb makes use of the full transaction/logging/locking functionality of the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> environment. Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> may be downloaded from <a rel="nofollow" href="http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/overview/index.html">http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/overview/index.html</a> &lt;<a href="http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/overview/index.html">http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/overview/index.html</a>&gt; and is needed to build the ovdb backend.</p>
<h2>Upgrading</h2>
<p>This is version 2 of ovdb. If you have a database created with a previous version of ovdb (such as the one shipped with <font SIZE="-1">INN</font>&nbsp;<wbr>2.3.0) your database will need to be upgraded using <i><a href="/docs/linux/man/8-ovdb_init/">ovdb_init</a></i>(8). See the man page <i><a href="/docs/linux/man/8-ovdb_init/">ovdb_init</a></i>(8) for upgrade instructions.</p>
<h2>Installation</h2>
<p>To build ovdb support into <font SIZE="-1">INN</font>, specify the option <code>&#8211;with-berkeleydb</code> when running the configure script. By default, configure will search for Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> in standard paths; there will be a message in the configure output indicating the pathname that will be used. </p>
<p> You can override this pathname by adding a path to the option, e.g., <code>&#8211;with-berkeleydb=/usr/BerkeleyDB.4.4</code>. This directory is expected to have subdirectories <i>include</i> and <i>lib</i>, containing <i>db.h</i>, and the library itself, respectively. </p>
<p> The ovdb database may take up more disk space for a given spool than the other overview methods. Plan on needing at least 1.1&nbsp;<wbr><font SIZE="-1">KB</font> for every article in your spool (not counting crossposts). So, if you have 5 million articles, you&#8217;ll need at least 5.5&nbsp;<wbr><font SIZE="-1">GB</font> of disk space for ovdb. With compression enabled, this estimate changes to 0.7&nbsp;<wbr><font SIZE="-1">KB</font> per article. See the <font SIZE="-1">COMPRESSION</font> section below. Plus, you&#8217;ll need additional space for transaction logs: at least 100&nbsp;<wbr><font SIZE="-1">MB</font>. By default the transaction logs go in the same directory as the database. To improve performance, they can be placed on a different disk &#8212; see the <font SIZE="-1">DB_CONFIG</font> section.</p>
<h2>Configuration</h2>
<p>To enable ovdb, set the <i>ovmethod</i> parameter in <i>inn.conf</i> to <tt>&quot;ovdb&quot;</tt>. The ovdb database is stored in the directory specified by the <i>pathoverview</i> parameter in <i>inn.conf</i>. This is the &#8220;<font SIZE="-1">DB_HOME</font>&#8221; directory. To start out, this directory should be empty (other than an optional <i></i><font SIZE="-1"><i>DB_CONFIG</i></font><i></i> file; see <font SIZE="-1">DB_CONFIG</font> for details) and <code>innd</code> (or <code>makehistory</code>) will create the files as necessary in that directory. Make sure the directory is owned by the news user. </p>
<p> Other parameters for configuring ovdb are in the <i><a href="/docs/linux/man/5-ovdb-conf/">ovdb.conf</a></i>(5) configuration file. See also the sample <i>ovdb.conf</i>.</p>
<dl>
<dt>cachesize</p>
<dd>Size of the memory pool cache, in kilobytes. The cache will have a backing store file in the <font SIZE="-1">DB</font> directory which will be at least as big. In general, the bigger the cache, the better. Use <tt>&quot;ovdb_stat -m&quot;</tt> to see cache hit percentages. To make a change of this parameter take effect, shut down and restart <font SIZE="-1">INN</font> (be sure to kill all of the nnrpds when shutting down). Default is 8000, which is adequate for small to medium sized servers. Large servers will probably need at least 20000.</p>
<dt>compress</p>
<dd>If <font SIZE="-1">INN</font> was compiled with zlib, and this compress parameter is true, <font SIZE="-1">OVDB</font> will compress overview records that are longer than 600 bytes. See the <font SIZE="-1">COMPRESSION</font> section below.</p>
<dt>numdbfiles</p>
<dd>Overview data is split between this many files. Currently, <code>innd</code> will keep all of the files open, so don&#8217;t set this too high or <code>innd</code> may run out of file descriptors. <code>nnrpd</code> only opens one at a time, regardless. May be set to one, or just a few, but only do that if your <font SIZE="-1">OS</font> supports large (&gt;2G) files. Changing this parameter has no effect on an already-established database. Default is 32.</p>
<dt>txn_nosync</p>
<dd>If txn_nosync is set to false, Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> flushes the log after every transaction. This minimizes the number of transactions that may be lost in the event of a crash, but results in significantly degraded performance. Default is true.</p>
<dt>useshm</p>
<dd>If useshm is set to true, Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> will use shared memory instead of mmap for its environment regions (cache, lock, etc). With some platforms, this may improve performance. Default is false.</p>
<dt>shmkey</p>
<dd>Sets the shared memory key used by Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> when &#8216;useshm&#8217; is true. Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> will create several (usually 5) shared memory segments, using sequentially numbered keys starting with &#8216;shmkey&#8217;. Choose a key that does not conflict with any existing shared memory segments on your system. Default is 6400.</p>
<dt>pagesize</p>
<dd>Sets the page size for the <font SIZE="-1">DB</font> files (in bytes). Must be a power of 2. Best choices are 4096 or 8192. The default is 8192. Changing this parameter has no effect on an already-established database.</p>
<dt>minkey</p>
<dd>Sets the minimum number of keys per page. See the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> documentation for more info. Default is based on page size and whether compression is enabled: </p>
<pre> default_minkey = MAX(2, pagesize / 2600) if compress is false
 default_minkey = MAX(2, pagesize / 1500) if compress is true</pre>
<p>The lowest allowed minkey is 2. Setting minkey higher than the default is not recommended, as it will cause the databases to have a lot of overflow pages. Changing this parameter has no effect on an already-established database.</p>
<dt>maxlocks</p>
<dd>Sets the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> &#8220;lk_max&#8221; parameter, which is the maximum number of locks that can exist in the database at the same time. Default is 4000.</p>
<dt>nocompact</p>
<dd>The nocompact parameter affects expireover&#8217;s behavior. The expireover function in ovdb can do its job in one of two ways: by simply deleting expired records from the database, or by re-writing the overview records into a different location leaving out the expired records. The first method is faster, but it leaves &#8216;holes&#8217; that result in space that can not immediately be reused. The second method &#8216;compacts&#8217; the records by rewriting them. </p>
<p> If this parameter is set to 0, expireover will compact all newsgroups; if set to 1, expireover will not compact any newsgroups; and if set to a value greater than one, expireover will only compact groups that have less than that number of articles. </p>
<p> Experience has shown that compacting has minimal effect (other than making expireover take longer) so the default is now 1. This parameter will probably be removed in the future.</p>
<dt>readserver</p>
<dd>Normally, each nnrpd process directly accesses the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> environment. The process of attaching to the database (and detaching when finished) is fairly expensive, and can result in high loads in situations when there are lots of reader connections of relatively short duration. </p>
<p> When the <i>readserver</i> parameter is true, the nnrpds will access overview via a helper server (<code>ovdb_server</code> &#8212; which is started by <code>ovdb_init</code>). This can also result in cleaner shutdowns for the database, improving stability and avoiding deadlocks and corrupted databases. If you are experiencing any instability in ovdb, try setting this parameter to true. Default is false.</p>
<dt>numrsprocs</p>
<dd>This parameter is only used when <i>readserver</i> is true. It sets the number of ovdb_server processes. As each ovdb_server can process only one transaction at a time, running more servers can improve reader response times. Default is 5.</p>
<dt>maxrsconn</p>
<dd>This parameter is only used when <i>readserver</i> is true. It sets a maximum number of readers that a given ovdb_server process will serve at one time. This means the maximum number of readers for all of the ovdb_server processes is (numrsprocs * maxrsconn). This does <code>not</code> limit the actual number of readers, since nnrpd will fall back to opening the database directly if it can&#8217;t connect to a readserver. Default is 0, which means an umlimited number of connections is allowed.</dl>
<h2>Compression</h2>
<p>New in this version of <font SIZE="-1">OVDB</font> is the ability to compress overview data before it is stored into the database. In addition to consuming less disk space, compression keeps the average size of the database keys smaller. This in turn increases the average number of keys per page, which can significantly improve performance and also helps keep the database more compact. This feature requires that <font SIZE="-1">INN</font> be built with zlib. Only records larger than 600 bytes get compressed, because that is the point at which compression starts to become significant. </p>
<p> If compression is not enabled (either from the <tt>&quot;compress&quot;</tt> option in <i>ovdb.conf</i> or <font SIZE="-1">INN</font> was not built from zlib), the database will be backward compatible with older versions of <font SIZE="-1">OVDB</font>. However, if compression is enabled, the database is marked with a newer version that will prevent older versions of <font SIZE="-1">OVDB</font> from opening the database. </p>
<p> You can upgrade an existing database to use compression simply by setting <i>compress</i> to true in <i>ovdb.conf</i>. Note that existing records in the database will remain uncompressed; only new records added after enabling compression will be compressed. </p>
<p> If you disable compression on a database that previously had it enabled, new records will be stored uncompressed, but the database will still be incompatible with older versions of <font SIZE="-1">OVDB</font> (and will also be incompatible with this version of <font SIZE="-1">OVDB</font> if it was not built with zlib). So to downgrade to a completely uncompressed database you will have to rebuild the database using makehistory.</p>
<h2>Db_Config</h2>
<p>A file called <i></i><font SIZE="-1"><i>DB_CONFIG</i></font><i></i> may be placed in the database directory to customize where the various database files and transaction logs are written. By default, all of the files are written in the &#8220;<font SIZE="-1">DB_HOME</font>&#8221; directory. One way to improve performance is to put the transaction logs on a different disk. To do this, put: </p>
<pre> DB_LOG_DIR /path/to/logs</pre>
<p>in the <i></i><font SIZE="-1"><i>DB_CONFIG</i></font><i></i> file. If the pathname you give starts with a /, it is treated as an absolute path; otherwise, it is relative to the &#8220;<font SIZE="-1">DB_HOME</font>&#8221; directory. Make sure that any directories you specify exist and have proper ownership/mode before starting <font SIZE="-1">INN</font>, because they won&#8217;t be created automatically. Also, don&#8217;t change the <font SIZE="-1">DB_CONFIG</font> file while anything that uses ovdb is running. </p>
<p> Another thing that you can do with this file is to split the overview database across multiple disks. In the <i></i><font SIZE="-1"><i>DB_CONFIG</i></font><i></i> file, you can list directories that Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> will search when it goes to open a database. </p>
<p> For example, let&#8217;s say that you have <i>pathoverview</i> set to <i>/mnt/overview</i> and you have four additional file systems created on <i>/mnt/ov?</i>. You would create a file &#8220;/mnt/overview/DB_CONFIG&#8221; containing the following lines: </p>
<pre> set_data_dir /mnt/overview
 set_data_dir /mnt/ov1
 set_data_dir /mnt/ov2
 set_data_dir /mnt/ov3
 set_data_dir /mnt/ov4</pre>
<p>Distribute your ovNNNNN files into the four filesystems. (say, 8 each). When called upon to open a database file, the db library will look for it in each of the specified directories (in order). If said file is not found, one will be created in the first of those directories. </p>
<p> Whenever you change <font SIZE="-1">DB_CONFIG</font> or move database files around, make sure all news processes that use the database are shut down first (including nnrpds). </p>
<p> The <font SIZE="-1">DB_CONFIG</font> functionality is part of Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> itself, rather than something provided by ovdb. See the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> documentation for complete details for the version of Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> that you&#8217;re running.</p>
<h2>Running</h2>
<p>When starting the news system, <code>rc.news</code> will invoke <code>ovdb_init</code>. <code>ovdb_init</code> must be run before using the database. It performs the following tasks:</p>
<dl>
<dt>&bull;</p>
<dd>Creates the database environment, if necessary.</p>
<dt>&bull;</p>
<dd>If the database is idle, it performs a normal recovery. The recovery will remove stale locks, recreate the memory pool cache, and repair any damage caused by a system crash or improper shutdown.</p>
<dt>&bull;</p>
<dd>Starts the <font SIZE="-1">DB</font> housekeeping processes (<code>ovdb_monitor</code>) if they&#8217;re not already running.</dl>
<p> And when stopping <font SIZE="-1">INN</font>, <code>rc.news</code> kills the ovdb_monitor processes after the other <font SIZE="-1">INN</font> processes have been shut down.</p>
<h2>Diagnostics</h2>
<p>Problems relating to ovdb are logged to news.err with &#8220;<font SIZE="-1">OVDB</font>&#8221; in the error message. </p>
<p> <font SIZE="-1">INN</font> programs that use overview will fail to start up if the ovdb_monitor processes aren&#8217;t running. Be sure to run <code>ovdb_init</code> before running anything that accesses overview. </p>
<p> Also, <font SIZE="-1">INN</font> programs that use overview will fail to start up if the user running them is not the &#8220;news&#8221; user. </p>
<p> If a program accessing the database crashes, or otherwise exits uncleanly, it might leave a stale lock in the database. This lock could cause other processes to deadlock on that stale lock. To fix this, shut down all news processes (using <tt>&quot;kill -9&quot;</tt> if necessary) and then restart. <code>ovdb_init</code> should perform a recovery operation which will remove the locks and repair damage caused by killing the deadlocked processes.</p>
<h2>Files</h2>
<dl>
<dt>inn.conf</p>
<dd>The <i>ovmethod</i> and <i>pathoverview</i> parameters are relevant to ovdb.</p>
<dt>ovdb.conf</p>
<dd>Optional configuration file for tuning. See <font SIZE="-1">CONFIGURATION</font> above.</p>
<dt><i>pathoverview</i></p>
<dd>Directory where the database goes. Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> calls it the &#8216;<font SIZE="-1">DB_HOME</font>&#8216; directory.</p>
<dt><i>pathoverview</i>/DB_CONFIG</p>
<dd>Optional file to configure the layout of the database files.</p>
<dt><i>pathrun</i>/ovdb.sem</p>
<dd>A file that gets locked by every process that is accessing the database. This is used by <code>ovdb_init</code> to determine whether the database is active or quiescent.</p>
<dt><i>pathrun</i>/ovdb_monitor.pid</p>
<dd>Contains the process <font SIZE="-1">ID</font> of <code>ovdb_monitor</code>.</dl>
<h2>To Do</h2>
<p>Implement a way to limit how many databases can be open at once (to reduce file descriptor usage); maybe using something similar to the cache code in ov3.c</p>
<h2>History</h2>
<p>Written by Heath Kehoe &lt;hakehoe [at] avalon.net&gt; for InterNetNews </p>
<p> <tt>$Id:</tt> ovdb.pod 9577 2013-12-06 03:54:44Z eagle $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/8-ovdb_init/">ovdb_init</a></i>(8), <i><a href="/docs/linux/man/8-ovdb_monitor/">ovdb_monitor</a></i>(8), <i><a href="/docs/linux/man/8-ovdb_stat/">ovdb_stat</a></i>(8) Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> documentation: in the <i>docs</i> directory of the Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> source distribution, or on the Oracle Berkeley&nbsp;<wbr><font SIZE="-1">DB</font> web page: <a rel="nofollow" href="http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/overview/index.html">http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/overview/index.html</a> &lt;<a href="http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/overview/index.html">http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/overview/index.html</a>&gt;. </p>
