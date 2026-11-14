---
title: "slapo-memberof(5)"
name: "slapo-memberof"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-memberof/"
description: "slapo-memberof – Reverse Group Membership overlay to slapd"
---

<p>slapo-memberof &#8211; Reverse Group Membership overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code>memberof</code> overlay to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) allows automatic reverse group membership maintenance. Any time a group entry is modified, its members are modified as appropriate in order to keep a DN-valued &quot;is member of&quot; attribute updated with the DN of the group. </p>
<h2>Configuration</h2>
<p>The config directives that are specific to the <code>memberof</code> overlay must be prefixed by <code>memberof-</code>, to avoid potential conflicts with directives specific to the underlying database or to other stacked overlays. </p>
<dl>
<dt><code>overlay memberof</code></p>
<dd>This directive adds the memberof overlay to the current database; see <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details. </p>
</dl>
<p> The following <code>slapd.conf</code> configuration options are defined for the memberof overlay. </p>
<dl>
<dt><code>memberof-group-oc</code><i>&nbsp;<wbr>&lt;group-oc&gt;</i></p>
<dd>The value <i>&lt;group-oc&gt; </i> is the name of the objectClass that triggers the reverse group membership update. It defaults to <i>groupOfNames</i>. </p>
<dt><code>memberof-member-ad</code><i>&nbsp;<wbr>&lt;member-ad&gt;</i></p>
<dd>The value <i>&lt;member-ad&gt; </i> is the name of the attribute that contains the names of the members in the group objects; it must be DN-valued. It defaults to <i>member</i>. </p>
<dt><code>memberof-memberof-ad</code><i>&nbsp;<wbr>&lt;memberof-ad&gt;</i></p>
<dd>The value <i>&lt;memberof-ad&gt; </i> is the name of the attribute that contains the names of the groups an entry is member of; it must be DN-valued. Its contents are automatically updated by the overlay. It defaults to <i>memberOf</i>. </p>
<dt><code>memberof-dn</code><i>&nbsp;<wbr>&lt;dn&gt;</i></p>
<dd>The value <i>&lt;dn&gt; </i> contains the DN that is used as <i>modifiersName</i> for internal modifications performed to update the reverse group membership. It defaults to the <i>rootdn</i> of the underlying database. </p>
<dt><code>memberof-dangling {</code><i>ignore</i><code>, </code><i>drop</i><code>, </code><i>error</i><code>}</code></p>
<dd>This option determines the behavior of the overlay when, during a modification, it encounters dangling references. The default is <i>ignore</i>, which may leave dangling references. Other options are <i>drop</i>, which discards those modifications that would result in dangling references, and <i>error</i>, which causes modifications that would result in dangling references to fail. </p>
<dt><code>memberof-dangling-error</code><i>&nbsp;<wbr>&lt;error-code&gt;</i></p>
<dd>If <code>memberof-dangling</code> is set to <i>error</i>, this configuration parameter can be used to modify the response code returned in case of violation. It defaults to &quot;constraint violation&quot;, but other implementations are known to return &quot;no such object&quot; instead. </p>
<dt><code>memberof-refint {</code><i>true</i><code>|</code><i>FALSE</i><code>}</code></p>
<dd>This option determines whether the overlay will try to preserve referential integrity or not. If set to <i>TRUE</i>, when an entry containing values of the &quot;is member of&quot; attribute is modified, the corresponding groups are modified as well. </p>
</dl>
<p> The memberof overlay may be used with any backend that provides full read-write functionality, but it is mainly intended for use with local storage backends. The maintenance operations it performs are internal to the server on which the overlay is configured and are never replicated. Replica servers should be configured with their own instances of the memberOf overlay if it is desired to maintain these memberOf attributes on the replicas.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8). The <code><a href="/docs/linux/man/5-slapo-memberof/">slapo-memberof</a></code>(5) overlay supports dynamic configuration via <code>back-config</code>.</p>
<h2>Acknowledgements</h2>
<p>This module was written in 2005 by Pierangelo Masarati for SysNet s.n.c.</p>
