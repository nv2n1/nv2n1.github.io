---
title: "slapo-syncprov(5)"
name: "slapo-syncprov"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-syncprov/"
description: "slapo-syncprov – Sync Provider overlay to slapd"
---

<p>slapo-syncprov &#8211; Sync Provider overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Sync Provider overlay implements the provider-side support for the LDAP Content Synchronization (RFC4533) as well as syncrepl replication support. The overlay can be used with any backend that maintains entryCSN and entryUUID attributes for its entries. It also creates a contextCSN attribute in the root entry of the database. </p>
<p> The contextCSN is updated for every write operation performed against the database. To reduce database contention, the contextCSN is only updated in memory. The value is written to the database on server shutdown and read into memory on startup, and maintained in memory thereafter. Checkpoints may be configured to write the contextCSN into the underlying database to minimize recovery time after an unclean shutdown. </p>
<p> On databases that support inequality indexing, it is helpful to set an eq index on the entryCSN attribute when using this overlay.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the Sync Provider overlay. They should appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>syncprov-checkpoint &lt;ops&gt; &lt;minutes&gt;</code></p>
<dd>After a write operation has succeeded, write the contextCSN to the underlying database if <code>&lt;ops&gt;</code> write operations or more than <code>&lt;minutes&gt;</code> time have passed since the last checkpoint. Checkpointing is disabled by default.</p>
<dt><code>syncprov-sessionlog &lt;ops&gt;</code></p>
<dd>Configures an in-memory session log for recording information about write operations made on the database. The <code>&lt;ops&gt;</code> specifies the number of operations that are recorded in the log. All write operations (except Adds) are recorded in the log. When using the session log, it is helpful to set an eq index on the entryUUID attribute in the underlying database.</p>
<dt><code>syncprov-nopresent TRUE | FALSE</code></p>
<dd>Specify that the Present phase of refreshing should be skipped. This value should only be set TRUE for a syncprov instance on top of a log database (such as one managed by the accesslog overlay). The default is FALSE.</p>
<dt><code>syncprov-reloadhint TRUE | FALSE</code></p>
<dd>Specify that the overlay should honor the reloadHint flag in the Sync Control. In OpenLDAP releases 2.3.11 and earlier the syncrepl consumer did not properly set this flag, so the overlay must ignore it. This option should be set TRUE when working with newer releases that properly support this flag. It must be set TRUE when using the accesslog overlay for delta-based syncrepl replication support. The default is FALSE.</dl>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapo-accesslog/">slapo-accesslog</a></code>(5). OpenLDAP Administrator&#8217;s Guide.</p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
