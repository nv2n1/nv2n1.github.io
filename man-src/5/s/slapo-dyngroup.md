---
title: "slapo-dyngroup(5)"
name: "slapo-dyngroup"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-dyngroup/"
description: "slapo-dyngroup – Dynamic Group overlay to slapd"
---

<p>slapo-dyngroup &#8211; Dynamic Group overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Dynamic Group overlay allows clients to use LDAP Compare operations to test the membership of a dynamic group the same way they would check against a static group. Compare operations targeting a group&#8217;s static member attribute will be intercepted and tested against the configured dynamic group&#8217;s URL attribute. </p>
<p> Note that this intercept only happens if the actual Compare operation does not return a LDAP_COMPARE_TRUE result. So if a group has both static and dynamic members, the static member list will be checked first.</p>
<h2>Configuration</h2>
<p>This <code>slapd.conf</code> option applies to the Dynamic Group overlay. It should appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>attrpair &lt;memberAttr&gt; &lt;URLattr&gt;</code></p>
<dd>Specify the attributes to be compared. A compare operation on the <i>memberAttr</i> will cause the <i>URLattr</i> to be evaluated for the result.</dl>
<h2>Examples</h2>
<pre> database bdb
 ...
 overlay dyngroup
 attrpair member memberURL</pre>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5).</p>
<h2>Author</h2>
<p>Howard Chu</p>
