---
title: "slapd-bdb(5)"
name: "slapd-bdb"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-bdb/"
description: "slapd-bdb, slapd-hdb – Berkeley DB backends to slapd"
---

<p>slapd-bdb, slapd-hdb &#8211; Berkeley DB backends to slapd</p>
<h2>Synopsis</h2>
<p><code>/etc/openldap/slapd.conf</code></p>
<h2>Description</h2>
<p>The <code>bdb</code> backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) uses the Oracle Berkeley DB (BDB) package to store data. It makes extensive use of indexing and caching to speed data access. </p>
<p> Note that BDB is deprecated and support will be dropped in future OpenLDAP releases. Installations should use the <code>mdb</code> backend instead. </p>
<p> <code>hdb</code> is a variant of the <code>bdb</code> backend that uses a hierarchical database layout which supports subtree renames. It is both more space-efficient and more execution-efficient than the <code>bdb</code> backend. It is otherwise identical to the <code>bdb</code> behavior, and all the same configuration options apply. </p>
<p> It is noted that these options are intended to complement Berkeley DB configuration options set in the environment&#8217;s <code>DB_CONFIG</code> file. See Berkeley DB documentation for details on <code>DB_CONFIG</code> configuration options. Where there is overlap, settings in <code>DB_CONFIG</code> take precedence.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the <code>bdb</code> and <code>hdb</code> backend database. That is, they must follow a &quot;database bdb&quot; or &quot;database hdb&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page.</p>
<dl>
<dt><code>cachesize</code><i>&nbsp;<wbr>&lt;integer&gt;</i></p>
<dd>Specify the size in entries of the in-memory entry cache maintained by the <code>bdb</code> or <code>hdb</code> backend database instance. The default is 1000 entries.</p>
<dt><code>cachefree</code><i>&nbsp;<wbr>&lt;integer&gt;</i></p>
<dd>Specify the number of entries to free from the entry cache when the cache reaches the <code>cachesize</code> limit. The default is 1 entry.</p>
<dt><code>checkpoint</code><i>&nbsp;<wbr>&lt;kbyte&gt;&nbsp;<wbr>&lt;min&gt;</i></p>
<dd>Specify the frequency for checkpointing the database transaction log. A checkpoint operation flushes the database buffers to disk and writes a checkpoint record in the log. The checkpoint will occur if either <i>&lt;kbyte&gt;</i> data has been written or <i>&lt;min&gt;</i> minutes have passed since the last checkpoint. Both arguments default to zero, in which case they are ignored. When the <i>&lt;min&gt;</i> argument is non-zero, an internal task will run every <i>&lt;min&gt;</i> minutes to perform the checkpoint. See the Berkeley DB reference guide for more details.</p>
<dt><code>checksum</code></p>
<dd>Enable checksum validation of DB pages whenever they are read from disk. This setting can only be configured before any database files are created.</p>
<dt><code>cryptfile</code><i>&nbsp;<wbr>&lt;file&gt;</i></p>
<dd>Specify the pathname of a file containing an encryption key to use for encrypting the database. Encryption is performed using Berkeley DB&#8217;s implementation of AES. Note that encryption can only be configured before any database files are created, and changing the key can only be done after destroying the current database and recreating it. Encryption is not enabled by default, and some distributions of Berkeley DB do not support encryption.</p>
<dt><code>cryptkey</code><i>&nbsp;<wbr>&lt;key&gt;</i></p>
<dd>Specify an encryption key to use for encrypting the database. This option may be used when a separate <i>cryptfile</i> is not desired. Only one of <code>cryptkey</code> or <code>cryptfile</code> may be configured.</p>
<dt><code>dbconfig</code><i>&nbsp;<wbr>&lt;Berkeley-DB-setting&gt;</i></p>
<dd>Specify a configuration directive to be placed in the <code>DB_CONFIG</code> file of the database directory. The <code>dbconfig</code> directive is just a convenience to allow all necessary configuration to be set in the <code>slapd.conf</code> file. The options set using this directive will only be written to the <code>DB_CONFIG</code> file if no such file existed at server startup time, otherwise they are completely ignored. This allows one to set initial values without overwriting/destroying a <code>DB_CONFIG </code> file that was already customized through other means. This directive may be specified multiple times, as needed. For example:</p>
<dl>
<dd>
<pre> dbconfig set_cachesize 0 1048576 0
 dbconfig set_lg_bsize 2097152</pre>
</dl>
<dt><code>dbnosync</code></p>
<dd>Specify that on-disk database contents should not be immediately synchronized with in memory changes. Enabling this option may improve performance at the expense of data security. See the Berkeley DB reference guide for more details.</p>
<dt><code>dbpagesize </code> <i>&lt;dbfile&gt; &lt;size&gt;</i></p>
<dd>Specify the page size to use for a particular database file, in units of 1024 bytes. The default for the <code>id2entry</code> file is 16, the default for all other files depends on the size of the underlying filesystem&#8217;s block size (typically 4 or 8). The maximum that BerkeleyDB supports is 64. This setting usually should not need to be changed, but if BerkeleyDB&#8217;s &quot;db_stat -d&quot; shows a large amount of overflow pages in use in a file, setting a larger size may increase performance at the expense of data integrity. This setting only takes effect when a database is being newly created. See the Berkeley DB reference guide for more details.</p>
<dt><code>directory</code><i>&nbsp;<wbr>&lt;directory&gt;</i></p>
<dd>Specify the directory where the BDB files containing this database and associated indexes live. A separate directory must be specified for each database. The default is <code>/var/openldap-data</code>.</p>
<dt><code>dirtyread</code></p>
<dd>Allow reads of modified but not yet committed data. Usually transactions are isolated to prevent other operations from accessing uncommitted data. This option may improve performance, but may also return inconsistent results if the data comes from a transaction that is later aborted. In this case, the modified data is discarded and a subsequent search will return a different result.</p>
<dt><code>dncachesize</code><i>&nbsp;<wbr>&lt;integer&gt;</i></p>
<dd>Specify the maximum number of DNs in the in-memory DN cache. Ideally this cache should be large enough to contain the DNs of every entry in the database. If set to a smaller value than the <code>cachesize</code> it will be silently increased to equal the <code>cachesize</code>. The default value is 0 which means unlimited, i.e. the DN cache will grow without bound. </p>
<p> It should be noted that the <code>DN cache</code> is allowed to temporarily grow beyond the configured size. It does this if many entries are locked when it tries to do a purge, because that means they&#8217;re legitimately in use. Also, the <code>DN cache</code> never purges entries that have cached children, so depending on the shape of the DIT, it could have lots of cached DNs over the defined limit.</p>
<dt><code>idlcachesize</code><i>&nbsp;<wbr>&lt;integer&gt;</i></p>
<dd>Specify the size of the in-memory index cache, in index slots. The default is zero. A larger value will speed up frequent searches of indexed entries. An <code>hdb</code> database needs a large <code>idlcachesize</code> for good search performance, typically three times the <code>cachesize</code> (entry cache size) or larger.</p>
<dt><code>index </code>{<i>&lt;attrlist&gt;</i>|<code>default</code>} [<code>pres</code>,<code>eq</code>,<code>approx</code>,<code>sub</code>,<i>&lt;special&gt;</i>]</p>
<dd>Specify the indexes to maintain for the given attribute (or list of attributes). Some attributes only support a subset of indexes. If only an <i>&lt;attr&gt;</i> is given, the indices specified for <code>default</code> are maintained. Note that setting a default does not imply that all attributes will be indexed. Also, for best performance, an <code>eq</code> index should always be configured for the <code>objectClass</code> attribute. </p>
<p> A number of special index parameters may be specified. The index type <code>sub</code> can be decomposed into <code>subinitial</code>, <code>subany</code>, and <code>subfinal</code> indices. The special type <code>nolang</code> may be specified to disallow use of this index by language subtypes. The special type <code>nosubtypes</code> may be specified to disallow use of this index by named subtypes. Note: changing <code>index</code> settings in <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) requires rebuilding indices, see <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8); changing <code>index</code> settings dynamically by LDAPModifying &quot;cn=config&quot; automatically causes rebuilding of the indices online in a background task.</p>
<dt><code>linearindex</code></p>
<dd>Tell <code>slapindex </code> to index one attribute at a time. By default, all indexed attributes in an entry are processed at the same time. With this option, each indexed attribute is processed individually, using multiple passes through the entire database. This option improves <code>slapindex </code> performance when the database size exceeds the <code>dbcache</code> size. When the <code>dbcache</code> is large enough, this option is not needed and will decrease performance. Also by default, <code>slapadd </code> performs full indexing and so a separate <code>slapindex</code> run is not needed. With this option, <code>slapadd </code> does no indexing and <code>slapindex</code> must be used.</p>
<dt><code>lockdetect</code>&nbsp;<wbr>{<code>oldest</code>|<code>youngest</code>|<code>fewest</code>|<code>random</code>|<code>default</code>}</p>
<dd>Specify which transaction to abort when a deadlock is detected. The default is <code>random</code>.</p>
<dt><code>mode</code><i>&nbsp;<wbr>&lt;integer&gt;</i></p>
<dd>Specify the file protection mode that newly created database index files should have. The default is 0600.</p>
<dt><code>searchstack</code><i>&nbsp;<wbr>&lt;depth&gt;</i></p>
<dd>Specify the depth of the stack used for search filter evaluation. Search filters are evaluated on a stack to accommodate nested AND / OR clauses. An individual stack is assigned to each server thread. The depth of the stack determines how complex a filter can be evaluated without requiring any additional memory allocation. Filters that are nested deeper than the search stack depth will cause a separate stack to be allocated for that particular search operation. These allocations can have a major negative impact on server performance, but specifying too much stack will also consume a great deal of memory. Each search stack uses 512K bytes per level. The default stack depth is 16, thus 8MB per thread is used.</p>
<dt><code>shm_key</code><i>&nbsp;<wbr>&lt;integer&gt;</i></p>
<dd>Specify a key for a shared memory BDB environment. By default the BDB environment uses memory mapped files. If a non-zero value is specified, it will be used as the key to identify a shared memory region that will house the environment.</dl>
<h2>Access Control</h2>
<p>The <code>bdb</code> and <code>hdb</code> backends honor access control semantics as indicated in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5).</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/openldap/slapd.conf</code></p>
<dd>default <code>slapd </code> configuration file</p>
<dt><code>DB_CONFIG</code></p>
<dd>Berkeley DB configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapd-mdb/">slapd-mdb</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8), <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8), Berkeley DB documentation.</p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. Originally begun by Kurt Zeilenga. Caching mechanisms originally designed by Jong-Hyuk Choi. Completion and subsequent work, as well as back-hdb, by Howard Chu.</p>
