---
title: "slapd-mdb(5)"
name: "slapd-mdb"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-mdb/"
description: "slapd-mdb – Memory-Mapped DB backend to slapd"
---

<p>slapd-mdb &#8211; Memory-Mapped DB backend to slapd</p>
<h2>Synopsis</h2>
<p><code>/etc/openldap/slapd.conf</code></p>
<h2>Description</h2>
<p>The <code>mdb</code> backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) uses OpenLDAP&#8217;s Lightning Memory-Mapped DB (LMDB) library to store data. It relies completely on the underlying operating system for memory management and does no caching of its own. It is the recommended primary database backend. </p>
<p> The <code>mdb</code> backend is similar to the <code>hdb</code> backend in that it uses a hierarchical database layout which supports subtree renames. It is both more space-efficient and more execution-efficient than the <code>bdb</code> backend, while being overall much simpler to manage.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the <code>mdb</code> backend database. That is, they must follow a &quot;database mdb&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page.</p>
<dl>
<dt><code>checkpoint</code><i>&nbsp;<wbr>&lt;kbyte&gt;&nbsp;<wbr>&lt;min&gt;</i></p>
<dd>Specify the frequency for flushing the database disk buffers. This setting is only needed if the <code>dbnosync</code> option is used. The checkpoint will occur if either <i>&lt;kbyte&gt;</i> data has been written or <i>&lt;min&gt;</i> minutes have passed since the last checkpoint. Both arguments default to zero, in which case they are ignored. When the <i>&lt;min&gt;</i> argument is non-zero, an internal task will run every <i>&lt;min&gt;</i> minutes to perform the checkpoint. Note: currently the <i>&lt;kbyte&gt;</i> setting is unimplemented.</p>
<dt><code>dbnosync</code></p>
<dd>Specify that on-disk database contents should not be immediately synchronized with in memory changes. Enabling this option may improve performance at the expense of data security. In particular, if the operating system crashes before changes are flushed, some number of transactions may be lost. By default, a full data flush/sync is performed when each transaction is committed.</p>
<dt><code>directory</code><i>&nbsp;<wbr>&lt;directory&gt;</i></p>
<dd>Specify the directory where the LMDB files containing this database and associated indexes live. A separate directory must be specified for each database. The default is <code>/var/openldap-data</code>.</p>
<dt><code>envflags </code>{<code>nosync</code>,<code>nometasync</code>,<code>writemap</code>,<code>mapasync</code>,<code>nordahead</code>}</p>
<dd>Specify flags for finer-grained control of the LMDB library&#8217;s operation.</p>
<dl>
<dd>
<dl>
<dt><code>nosync</code></p>
<dd>This is exactly the same as the <i>dbnosync</i> directive.</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>nometasync</code></p>
<dd>Flush the data on a commit, but skip the sync of the meta page. This mode is slightly faster than doing a full sync, but can potentially lose the last committed transaction if the operating system crashes. If both <i>nometasync</i> and <i>nosync</i> are set, the <i>nosync</i> flag takes precedence.</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>writemap</code></p>
<dd>Use a writable memory map instead of just read-only. This speeds up write operations but makes the database vulnerable to corruption in case any bugs in slapd cause stray writes into the mmap region.</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>mapasync</code></p>
<dd>When using a writable memory map and performing flushes on each commit, use an asynchronous flush instead of a synchronous flush (the default). This option has no effect if <i>writemap</i> has not been set. It also has no effect if <i>nosync</i> is set.</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>nordahead</code></p>
<dd>Turn off file readahead. Usually the OS performs readahead on every read request. This usually boosts read performance but can be harmful to random access read performance if the system&#8217;s memory is full and the DB is larger than RAM. This option is not implemented on Windows.</dl>
</dl>
<dt><code>index </code>{<i>&lt;attrlist&gt;</i>|<code>default</code>} [<code>pres</code>,<code>eq</code>,<code>approx</code>,<code>sub</code>,<i>&lt;special&gt;</i>]</p>
<dd>Specify the indexes to maintain for the given attribute (or list of attributes). Some attributes only support a subset of indexes. If only an <i>&lt;attr&gt;</i> is given, the indices specified for <code>default</code> are maintained. Note that setting a default does not imply that all attributes will be indexed. Also, for best performance, an <code>eq</code> index should always be configured for the <code>objectClass</code> attribute. </p>
<p> A number of special index parameters may be specified. The index type <code>sub</code> can be decomposed into <code>subinitial</code>, <code>subany</code>, and <code>subfinal</code> indices. The special type <code>nolang</code> may be specified to disallow use of this index by language subtypes. The special type <code>nosubtypes</code> may be specified to disallow use of this index by named subtypes. Note: changing <code>index</code> settings in <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) requires rebuilding indices, see <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8); changing <code>index</code> settings dynamically by LDAPModifying &quot;cn=config&quot; automatically causes rebuilding of the indices online in a background task.</p>
<dt><code>maxreaders</code><i>&nbsp;<wbr>&lt;integer&gt;</i></p>
<dd>Specify the maximum number of threads that may have concurrent read access to the database. Tools such as slapcat count as a single thread, in addition to threads in any active slapd processes. The default is 126.</p>
<dt><code>maxsize</code><i>&nbsp;<wbr>&lt;bytes&gt;</i></p>
<dd>Specify the maximum size of the database in bytes. A memory map of this size is allocated at startup time and the database will not be allowed to grow beyond this size. The default is 10485760 bytes. This setting may be changed upward if the configured limit needs to be increased. </p>
<p> Note: It is important to set this to as large a value as possible, (relative to anticipated growth of the actual data over time) since growing the size later may not be practical when the system is under heavy load.</p>
<dt><code>mode</code><i>&nbsp;<wbr>&lt;integer&gt;</i></p>
<dd>Specify the file protection mode that newly created database files should have. The default is 0600.</p>
<dt><code>searchstack</code><i>&nbsp;<wbr>&lt;depth&gt;</i></p>
<dd>Specify the depth of the stack used for search filter evaluation. Search filters are evaluated on a stack to accommodate nested AND / OR clauses. An individual stack is assigned to each server thread. The depth of the stack determines how complex a filter can be evaluated without requiring any additional memory allocation. Filters that are nested deeper than the search stack depth will cause a separate stack to be allocated for that particular search operation. These allocations can have a major negative impact on server performance, but specifying too much stack will also consume a great deal of memory. Each search stack uses 512K bytes per level. The default stack depth is 16, thus 8MB per thread is used.</dl>
<h2>Access Control</h2>
<p>The <code>mdb</code> backend honors access control semantics as indicated in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5).</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/openldap/slapd.conf</code></p>
<dd>default <code>slapd </code> configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8), <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8), OpenLDAP LMDB documentation.</p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. Written by Howard Chu.</p>
