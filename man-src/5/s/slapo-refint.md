---
title: "slapo-refint(5)"
name: "slapo-refint"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-refint/"
description: "slapo-refint – Referential Integrity overlay to slapd"
---

<p>slapo-refint &#8211; Referential Integrity overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Referential Integrity overlay can be used with a backend database such as <code><a href="/docs/linux/man/5-slapd-bdb/">slapd-bdb</a></code>(5) to maintain the cohesiveness of a schema which utilizes reference attributes. </p>
<p> Integrity is maintained by updating database records which contain the named attributes to match the results of a <code>modrdn</code> or <code>delete</code> operation. For example, if the integrity attribute were configured as <code>manager</code>, deletion of the record &quot;uid=robert,ou=people,dc=example,dc=com&quot; would trigger a search for all other records which have a <code>manager</code> attribute containing that DN. Entries matching that search would have their <code>manager</code> attribute removed. Or, renaming the same record into &quot;uid=george,ou=people,dc=example,dc=com&quot; would trigger a search for all other records which have a <code>manager</code> attribute containing that DN. Entries matching that search would have their <code>manager</code> attribute deleted and replaced by the new DN. </p>
<p> <code>rootdn</code> must be set for the database. refint runs as the rootdn to gain access to make its updates. <code>rootpw</code> is not needed.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the Referential Integrity overlay. They should appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>refint_attributes &lt;attribute&gt; [&#8230;]</code></p>
<dd>Specify one or more attributes for which integrity will be maintained as described above.</p>
<dt><code>refint_nothing &lt;string&gt;</code></p>
<dd>Specify an arbitrary value to be used as a placeholder when the last value would otherwise be deleted from an attribute. This can be useful in cases where the schema requires the existence of an attribute for which referential integrity is enforced. The attempted deletion of a required attribute will otherwise result in an Object Class Violation, causing the request to fail. The string must be a valid DN.</p>
<dt><code>refint_modifiersname &lt;DN&gt;</code></p>
<dd>Specify the DN to be used as the modifiersName of the internal modifications performed by the overlay. It defaults to &quot;<i>cn=Referential Integrity Overlay</i>&quot;.</dl>
<p> Modifications performed by this overlay are not propagated during replication. This overlay must be configured identically on replication consumers in order to maintain full synchronization with the provider.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5).</p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
