---
title: "cnid_dbd(8)"
name: "cnid_dbd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cnid_dbd/"
description: "cnid_dbd – implement access to CNID databases through a dedicated daemon process"
---

<p>cnid_dbd &#8211; implement access to CNID databases through a dedicated daemon process</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>cnid_dbd</code> <i>dbdir</i> <i>ctrlfd</i> <i>clntfd</i></dl>
<h2>Description</h2>
<p><code>cnid_dbd</code></p>
<dd>provides an interface for storage and retrieval of catalog node IDs (CNIDs) and related information to the <code>afpd</code> daemon. CNIDs are a component of Macintosh based file systems with semantics that map not easily onto Unix file systems. This makes separate storage in a database necessary. <code>cnid_dbd</code> is part of the <code>CNID backend</code> framework of <code>afpd</code> and implements the <code>dbd</code> backend. </p>
<p> <code>cnid_dbd</code> is never started via the command line or system startup scripts but only by the <code>cnid_metad</code> daemon. There is at most one instance of <code>cnid_dbd</code> per netatalk volume. </p>
<p> <code>cnid_dbd</code> uses the <code>Berkleley DB</code> database library and optionally supports transactionally protected updates if the netatalk package is compiled with the appropriate options. Using the <code>dbd</code> backend without transactions will protect the CNID database against unexpected crashes of the <code>afpd</code> daemon. Using the <code>dbd</code> backend with transactions will avoid corruption of the CNID database even if the system crashes unexpectedly. </p>
<p> <code>cnid_dbd</code> uses the same on-disk database format as the <code>cdb</code> backend. It is therefore possible to switch between the two backends as necessary. </p>
<p> <code>cnid_dbd</code> inherits the effective userid and groupid from <code>cnid_metad</code> on startup, which is normally caused by <code>afpd</code> serving a netatalk volume to a client. It changes to the <code>Berkleley DB</code> database home directory <i>dbdir</i> that is associated with the volume. If the userid inherited from <code>cnid_metad</code> is 0 (root), <code>cnid_dbd</code> will change userid and groupid to the owner and group of the database home directory. Otherwise, it will continue to use the inherited values. <code>cnid_dbd</code> will then attempt to open the database and start serving requests using filedescriptor <i>clntfd</i>. Subsequent instances of <code>afpd</code> that want to access the same volume are redirected to the running <code>cnid_dbd</code> process by <code>cnid_metad</code> via the filedescriptor <i>ctrlfd</i>. </p>
<p> <code>cnid_dbd</code> can be configured to run forever or to exit after a period of inactivity. If <code>cnid_dbd</code> receives a TERM or an INT signal it will exit cleanly after flushing dirty database buffers to disk and closing <code>Berkleley DB</code> database environments. It is safe to terminate <code>cnid_dbd</code> this way, it will be restarted when necessary. Other signals are not handled and will cause an immediate exit, possibly leaving the CNID database in an inconsistent state (no transactions) or losing recent updates during recovery (transactions). </p>
<p> If transactions are used the <code>Berkleley DB</code> database subsystem will create files named log.xxxxxxxxxx in the database home directory <i>dbdir</i>, where xxxxxxxxxx is a monotonically increasing integer. These files contain information to replay database changes and are not automatically removed, unless the <code>logfile_autoremove</code> option is specified in the <i>db_param</i> configuration file (see below). Please see the sections <code>Database and log file archival</code>, <code> Log file removal</code> and the documentation of the <code> db_archive</code> command line utility in the Berkeley DB Tutorial and Reference for information when and how it is safe to remove these files manually. </p>
<p> Do not use <code>cnid_dbd</code> for databases on NFS mounted file systems. It makes the whole point of securing database changes properly moot. Use the dbdir: Option in the appropriate <code>AppleVolumes</code> configuration file to put the database onto a local disk.</p>
<h2>Configuration</h2>
<p><code>cnid_dbd</code> reads configuration information from the file <i>db_param</i> in the database directory <i>dbdir</i> on startup. If the file does not exist or a parameter is not listed, suitable default values are used. The format for a single parameter is the parameter name, followed by one or more spaces, followed by the parameter value, followed by a newline. The following parameters are currently recognized: </p>
<p> <code>logfile_autoremove</code></p>
<dl>
<dd>This flag is ignored unless transactional support is enabled. If set to 1, unused Berkeley DB transactional logfiles (log.xxxxxxxxxx in the database home directory) are removed on startup of <code>cnid_dbd</code>. This is usually safe if the content of the database directory is backed up on a regular basis. Default: 0.</dl>
<p> <code>cachesize</code></p>
<dl>
<dd>Determines the size of the Berkeley DB cache in kilobytes. Default: 1024. Each <code>cnid_dbd</code> process grabs that much memory on top of its normal memory footprint. It can be used to tune database performance. The <code>db_stat</code> utility with the <code>-m</code> option that comes with Berkely DB can help you determine wether you need to change this value. The default is pretty conservative so that a large percentage of requests should be satisfied from the cache directly. If memory is not a bottleneck on your system you might want to leave it at that value. The <code>Berkeley DB Tutorial and Reference Guide</code> has a section <code>Selecting a cache size</code> that gives more detailed information.</dl>
<p> <code>nosync</code></p>
<dl>
<dd>This flag is ignored unless transactional support is enabled. If it is set to 1, transactional changes to the database are not synchronously written to disk when the transaction completes. This will increase performance considerably at the risk of recent changes getting lost in case of a crash. The database will still be consistent, though. See <code>Transaction Throughput</code> in the Berkeley DB Tutorial for more information. Default: 0.</dl>
<p> <code>flush_frequency</code>, <code>flush_interval</code></p>
<dl>
<dd><i>flush_frequency</i> (Default: 100) and <i>flush_interval</i> (Default: 30) control how often changes to the database are written to the underlying database files if no transactions are used or how often the transaction system is checkpointed for transactions. Both of these operations are performed if either i) more than <i>flush_frequency</i> requests have been received or ii) more than <i>flush_interval</i> seconds have elapsed since the last save/checkpoint. If you use transactions with <i>nosync</i> set to zero these parameters only influence how long recovery takes after a crash, there should never be any lost data. If <i>nosync</i> is 1, changes might be lost, but only since the last checkpoint. Be careful to check your harddisk configuration for on disk cache settings. Many IDE disks just cache writes as the default behaviour, so even flushing database files to disk will not have the desired effect.</dl>
<p> <code>fd_table_size</code></p>
<dl>
<dd>is the maximum number of connections (filedescriptors) that can be open for <code>afpd</code> client processes in <code>cnid_dbd.</code> Default: 16. If this number is exceeded, one of the existing connections is closed and reused. The affected <code>afpd</code> process will transparently reconnect later, which causes slight overhead. On the other hand, setting this parameter too high could affect performance in <code>cnid_dbd</code> since all descriptors have to be checked in a <code>select()</code> system call, or worse, you might exceed the per process limit of open file descriptors on your system. It is safe to set the value to 1 on volumes where only one <code>afpd</code> client process is expected to run, e.g. home directories.</dl>
<p> <code>idle_timeout</code></p>
<dl>
<dd>is the number of seconds of inactivity before an idle <code>cnid_dbd</code> exits. Default: 600. Set this to 0 to disable the timeout.</dl>
<p> <code>check</code></p>
<dl>
<dd>is a flag value. If set <code>cnid_dbd</code> will automatically check the database indexes. Default: 0. Set this to 1 to enable checking.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cnid_metad/">cnid_metad</a></code>(8), <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8) </p>
