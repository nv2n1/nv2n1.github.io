---
title: "slapd-backends(5)"
name: "slapd-backends"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-backends/"
description: "slapd.backends – backends for slapd, the stand-alone LDAP daemon"
---

<p>slapd.backends &#8211; backends for slapd, the stand-alone LDAP daemon</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) daemon can use a variety of different backends for serving LDAP requests. Backends may be compiled statically into slapd, or when module support is enabled, they may be dynamically loaded. Multiple instances of a backend can be configured, to serve separate databases from the same slapd server. </p>
<p> Configuration options for each backend are documented separately in the corresponding <code>slapd-&lt;backend&gt;</code>(5) manual pages.</p>
<dl>
<dt><code>bdb</code></p>
<dd>This was the recommended primary backend through OpenLDAP 2.3, but it has since been superseded by the <code>hdb</code> backend. It takes care to configure it properly. It uses the transactional database interface of the Oracle Berkeley DB (BDB) package to store data.</p>
<dt><code>config</code></p>
<dd>This backend is used to manage the configuration of slapd at run-time. Unlike other backends, only a single instance of the <code>config</code> backend may be defined. It also instantiates itself automatically, so it is always present even if not explicitly defined in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file.</p>
<dt><code>dnssrv</code></p>
<dd>This backend is experimental. It serves up referrals based upon SRV resource records held in the Domain Name System.</p>
<dt><code>hdb</code></p>
<dd>This is the recommended primary backend for a normal slapd database. <code>hdb</code> is a variant of the <code>bdb</code> backend that uses a hierarchical database layout. This layout stores entry DNs more efficiently than the <code>bdb</code> backend, using less space and requiring less work to create, delete, and rename entries. It is also one of the few backends to support subtree renames.</p>
<dt><code>ldap</code></p>
<dd>This backend acts as a proxy to forward incoming requests to another LDAP server.</p>
<dt><code>ldif</code></p>
<dd>This database uses the filesystem to build the tree structure of the database, using plain ascii files to store data. Its usage should be limited to very simple databases, where performance is not a requirement. This backend also supports subtree renames.</p>
<dt><code>mdb</code></p>
<dd>This will soon be the recommended primary backend, superseding <code>hdb</code>. This backend uses OpenLDAP&#8217;s own MDB transactional database library. It is extremely compact and extremely efficient, delivering much higher performance than the Berkeley DB backends while using significantly less memory. Also, unlike Berkeley DB, MDB is crash proof, and requires no special tuning or maintenance. This backend also supports subtree renames.</p>
<dt><code>meta</code></p>
<dd>This backend performs basic LDAP proxying with respect to a set of remote LDAP servers. It is an enhancement of the <code>ldap</code> backend.</p>
<dt><code>monitor</code></p>
<dd>This backend provides information about the running status of the slapd daemon. Only a single instance of the <code>monitor</code> backend may be defined.</p>
<dt><code>ndb</code></p>
<dd>This backend is experimental. It uses the transactional database interface of the MySQL Cluster Engine (NDB) to store data. Note that Oracle, which now owns MySQL, has withdrawn support for NDB and this backend is unlikely to be developed any further.</p>
<dt><code>null</code></p>
<dd>Operations in this backend succeed but do nothing.</p>
<dt><code>passwd</code></p>
<dd>This backend is provided for demonstration purposes only. It serves up user account information from the system <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5) file.</p>
<dt><code>perl</code></p>
<dd>This backend embeds a <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) interpreter into slapd. It runs Perl subroutines to implement LDAP operations.</p>
<dt><code>relay</code></p>
<dd>This backend is experimental. It redirects LDAP operations to another database in the same server, based on the naming context of the request. Its use requires the <code>rwm</code> overlay (see <code><a href="/docs/linux/man/5-slapo-rwm/">slapo-rwm</a></code>(5) for details) to rewrite the naming context of the request. It is primarily intended to implement virtual views on databases that actually store data.</p>
<dt><code>shell</code></p>
<dd>This backend executes external programs to implement LDAP operations. It is primarily intended to be used in prototypes.</p>
<dt><code>sql</code></p>
<dd>This backend is experimental. It services LDAP requests from an SQL database.</dl>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</p>
<dt>/etc/openldap/slapd.d</p>
<dd>default slapd configuration directory</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/5-slapd-bdb/">slapd-bdb</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapd-dnssrv/">slapd-dnssrv</a></code>(5), <code><a href="/docs/linux/man/5-slapd-hdb/">slapd-hdb</a></code>(5), <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-slapd-ldif/">slapd-ldif</a></code>(5), <code><a href="/docs/linux/man/5-slapd-mdb/">slapd-mdb</a></code>(5), <code><a href="/docs/linux/man/5-slapd-meta/">slapd-meta</a></code>(5), <code><a href="/docs/linux/man/5-slapd-monitor/">slapd-monitor</a></code>(5), <code><a href="/docs/linux/man/5-slapd-ndb/">slapd-ndb</a></code>(5), <code><a href="/docs/linux/man/5-slapd-null/">slapd-null</a></code>(5), <code><a href="/docs/linux/man/5-slapd-passwd/">slapd-passwd</a></code>(5), <code><a href="/docs/linux/man/5-slapd-perl/">slapd-perl</a></code>(5), <code><a href="/docs/linux/man/5-slapd-relay/">slapd-relay</a></code>(5), <code><a href="/docs/linux/man/5-slapd-shell/">slapd-shell</a></code>(5), <code><a href="/docs/linux/man/5-slapd-sql/">slapd-sql</a></code>(5), <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-overlays/">slapd.overlays</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8). &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
