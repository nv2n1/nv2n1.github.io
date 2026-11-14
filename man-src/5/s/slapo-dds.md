---
title: "slapo-dds(5)"
name: "slapo-dds"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-dds/"
description: "slapo-dds – Dynamic Directory Services overlay to slapd"
---

<p>slapo-dds &#8211; Dynamic Directory Services overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code>dds</code> overlay to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) implements dynamic objects as per RFC 2589. The name <code>dds</code> stands for Dynamic Directory Services. It allows to define dynamic objects, characterized by the <code>dynamicObject</code> objectClass. Dynamic objects have a limited lifetime, determined by a time-to-live (TTL) that can be refreshed by means of a specific <code>refresh</code> extended operation. This operation allows to set the Client Refresh Period (CRP), namely the period between refreshes that is required to preserve the dynamic object from expiration. The expiration time is computed by adding the requested TTL to the current time. When dynamic objects reach the end of their lifetime without being further refreshed, they are automatically deleted. There is no guarantee of immediate deletion, so clients should not count on it. Dynamic objects can have subordinates, provided these also are dynamic objects. RFC 2589 does not specify what the behavior of a dynamic directory service should be when a dynamic object with (dynamic) subordinates expires. In this implementation, the lifetime of dynamic objects with subordinates is prolonged until all the dynamic subordinates expire. This <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) directive adds the <code>dds</code> overlay to the current database:</p>
<dl>
<dt><code>overlay dds</code></p>
<dd> The database must have a <code>rootdn</code> specified, otherwise, the <code>dds</code> overlay will not be able to delete expired objects. The <code>dds</code> overlay may be used with any backend that implements the <code>add</code>, <code>modify</code>, <code>search</code>, and <code>delete</code> operations. Since its use may result in many internal entry lookups, adds and deletes, it should be best used in conjunction with backends that have reasonably good write performances. The config directives that are specific to the <code>dds</code> overlay are prefixed by <code>dds-</code>, to avoid potential conflicts with directives specific to the underlying database or to other stacked overlays.</p>
<dl>
<dt><code>dds-max-ttl &lt;ttl&gt;</code></p>
<dd>Specifies the max TTL value. This is also the default TTL newly created dynamic objects receive, unless <code>dds-default-ttl</code> is set. When the client with a refresh extended operation requests a TTL higher than it, sizeLimitExceeded is returned. This value must be between 86400 (1 day, the default) and 31557600 (1 year plus 6 hours, as per RFC 2589).</p>
<dt><code>dds-min-ttl &lt;ttl&gt;</code></p>
<dd>Specifies the min TTL value; clients requesting a lower TTL by means of the refresh extended operation actually obtain this value as CRP. If set to 0 (the default), no lower limit is set.</p>
<dt><code>dds-default-ttl &lt;ttl&gt;</code></p>
<dd>Specifies the default TTL value that newly created dynamic objects get. If set to 0 (the default), the <code>dds-max-ttl</code> is used.</p>
<dt><code>dds-interval &lt;ttl&gt;</code></p>
<dd>Specifies the interval between expiration checks; defaults to 1 hour.</p>
<dt><code>dds-tolerance &lt;ttl&gt;</code></p>
<dd>Specifies an extra time that is added to the timer that actually wakes up the thread that will delete an expired dynamic object. So the nominal lifetime of the entry is that specified in the <code>entryTtl</code> attribute, but its lifetime will actually be <code>entryTtl + tolerance</code>. Note that there is no guarantee that the lifetime of a dynamic object will be <i>exactly</i> the requested TTL; due to implementation details, it may be longer, which is allowed by RFC 2589. By default, tolerance is 0.</p>
<dt><code>dds-max-dynamicObjects &lt;num&gt;</code></p>
<dd>Specifies the maximum number of dynamic objects that can simultaneously exist within a naming context. This allows to limit the amount of resources (mostly in terms of run-queue size) that are used by dynamic objects. By default, no limit is set.</p>
<dt><code>dds-state {TRUE|false}</code></p>
<dd>Specifies if the Dynamic Directory Services feature is enabled or not. By default it is; however, a proxy does not need to keep track of dynamic objects itself, it only needs to inform the frontend that support for dynamic objects is available. </p>
<h2>Access Control</h2>
<p>The <code>dds</code> overlay restricts the refresh operation by requiring <code>manage</code> access to the <code>entryTtl</code> attribute (see <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5) for details about the <code>manage</code> access privilege). Since the <code>entryTtl</code> is an operational, NO-USER-MODIFICATION attribute, no direct write access to it is possible. So the <code>dds</code> overlay turns refresh extended operation into an internal modification to the value of the <code>entryTtl</code> attribute with the <code>relax</code> control set. </p>
<p> RFC 2589 recommends that anonymous clients should not be allowed to refresh a dynamic object. This can be implemented by appropriately crafting access control to obtain the desired effect. </p>
<p> Example: restrict refresh to authenticated clients </p>
<dl>
<dd>
<pre>access to attrs=entryTtl
 by users manage
 by * read</pre>
</dl>
<p> Example: restrict refresh to the creator of the dynamic object </p>
<dl>
<dd>
<pre>access to attrs=entryTtl
 by dnattr=creatorsName manage
 by * read</pre>
</dl>
<p> Another suggested usage of dynamic objects is to implement dynamic meetings; in this case, all the participants to the meeting are allowed to refresh the meeting object, but only the creator can delete it (otherwise it will be deleted when the TTL expires) </p>
<p> Example: assuming <i>participant</i> is a valid DN-valued attribute, allow users to start a meeting and to join it; restrict refresh to the participants; restrict delete to the creator </p>
<dl>
<dd>
<pre>access to dn.base=&quot;cn=Meetings&quot;
 attrs=children
 by users write
access to dn.onelevel=&quot;cn=Meetings&quot;
 attrs=entry
 by dnattr=creatorsName write
 by * read
access to dn.onelevel=&quot;cn=Meetings&quot;
 attrs=participant
 by dnattr=creatorsName write
 by users selfwrite
 by * read
access to dn.onelevel=&quot;cn=Meetings&quot;
 attrs=entryTtl
 by dnattr=participant manage
 by * read</pre>
</dl>
<h2>Replication</h2>
<p>This implementation of RFC 2589 provides a restricted interpretation of how dynamic objects replicate. Only the master takes care of handling dynamic object expiration, while replicas simply see the dynamic object as a plain object. </p>
<p> When replicating these objects, one needs to explicitly exclude the <code>dynamicObject</code> class and the <code>entryTtl</code> attribute. This implementation of RFC 2589 introduces a new operational attribute, <code>entryExpireTimestamp</code>, that contains the expiration timestamp. This must be excluded from replication as well. </p>
<p> The quick and dirty solution is to set <code>schemacheck=off</code> in the syncrepl configuration and, optionally, exclude the operational attributes from replication, using </p>
<dl>
<dd>
<pre>syncrepl ...
 exattrs=entryTtl,entryExpireTimestamp</pre>
</dl>
<p> In any case the overlay must be either statically built in or run-time loaded by the consumer, so that it is aware of the <code>entryExpireTimestamp</code> operational attribute; however, it must not be configured in the shadow database. Currently, there is no means to remove the <code>dynamicObject</code> class from the entry; this may be seen as a feature, since it allows to see the dynamic properties of the object.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8).</p>
<h2>Author</h2>
<p>Implemented by Pierangelo Masarati.</p>
