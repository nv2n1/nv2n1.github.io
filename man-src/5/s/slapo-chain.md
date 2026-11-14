---
title: "slapo-chain(5)"
name: "slapo-chain"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-chain/"
description: "slapo-chain – chain overlay to slapd"
---

<p>slapo-chain &#8211; chain overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code>chain</code> overlay to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) allows automatic referral chasing. Any time a referral is returned (except for bind operations), it is chased by using an instance of the ldap backend. If operations are performed with an identity (i.e. after a bind), that identity can be asserted while chasing the referrals by means of the <i>identity assertion</i> feature of back-ldap (see <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5) for details), which is essentially based on the <code>proxied authorization</code> control [RFC 4370]. Referral chasing can be controlled by the client by issuing the <code>chaining</code> control (see <i>draft-sermersheim-ldap-chaining</i> for details.) The config directives that are specific to the <code>chain</code> overlay are prefixed by <code>chain-</code>, to avoid potential conflicts with directives specific to the underlying database or to other stacked overlays. There are very few chain overlay specific directives; however, directives related to the instances of the <i>ldap</i> backend that may be implicitly instantiated by the overlay may assume a special meaning when used in conjunction with this overlay. They are described in <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5), and they also need to be prefixed by <code>chain-</code>. Note: this overlay is built into the <i>ldap</i> backend; it is not a separate module. </p>
<pre><code>overlay chain


This directive adds the chain overlay to the current backend.
The chain overlay may be used with any backend, but it is mainly
intended for use with local storage backends that may return referrals.
It is useless in conjunction with the slapd-ldap and slapd-meta
backends because they already exploit the libldap specific referral chase
feature.
[Note: this may change in the future, as the ldap(5) and
meta(5) backends might no longer chase referrals on their own.]
chain-cache-uri {FALSE|true}


This directive instructs the chain overlay to cache
connections to URIs parsed out of referrals that are not predefined,
to be reused for later chaining.
These URIs inherit the properties configured for the underlying
slapd-ldap(5) before any occurrence of the chain-uri
directive; basically, they are chained anonymously.
chain-chaining [resolve=&lt;r&gt;] [continuation=&lt;c&gt;] [critical]


This directive enables the chaining control
(see draft-sermersheim-ldap-chaining for details)
with the desired resolve and continuation behaviors and criticality.
The resolve parameter refers to the behavior while discovering
a resource, namely when accessing the object indicated by the request DN;
the continuation parameter refers to the behavior while handling
intermediate responses, which is mostly significant for the search
operation, but may affect extended operations that return intermediate
responses.
The values r and c can be any of
chainingPreferred,

chainingRequired,

referralsPreferred,

referralsRequired.

If the critical flag affects the control criticality if provided.
[This control is experimental and its support may change in the future.]
chain-max-depth &lt;n&gt;


In case a referral is returned during referral chasing, further chasing
occurs at most &lt;n&gt; levels deep.  Set to 1 (the default)
to disable further referral chasing.
chain-return-error {FALSE|true}


In case referral chasing fails, the real error is returned instead
of the original referral.  In case multiple referral URIs are present,
only the first error is returned.  This behavior may not be always
appropriate nor desirable, since failures in referral chasing might be
better resolved by the client (e.g. when caused by distributed
authentication issues).
chain-uri &lt;ldapuri&gt;


This directive instantiates a new underlying ldap database
and instructs it about which URI to contact to chase referrals.
As opposed to what stated in slapd-ldap(5), only one URI
can appear after this directive;
all subsequent slapd - ldap(5) directives prefixed by chain - refer to this specific instance of a remote server.
</code></pre>
<p> Directives for configuring the underlying ldap database may also be required, as shown in this example: </p>
<pre><code>overlay                 chain
chain-rebind-as-user    FALSE

chain-uri               &quot;ldap://ldap1.example.com&quot;
chain-rebind-as-user    TRUE
chain-idassert-bind     bindmethod=&quot;simple&quot;
binddn=&quot;cn=Auth,dc=example,dc=com&quot;
credentials=&quot;secret&quot;
mode=&quot;self&quot;

chain-uri               &quot;ldap://ldap2.example.com&quot;
chain-idassert-bind     bindmethod=&quot;simple&quot;
binddn=&quot;cn=Auth,dc=example,dc=com&quot;
credentials=&quot;secret&quot;
mode=&quot;none&quot;</code></pre>
<p> Any valid directives for the ldap database may be used; see <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5) for details. Multiple occurrences of the <code>chain-uri</code> directive may appear, to define multiple &quot;trusted&quot; URIs where operations with <i>identity assertion</i> are chained. All URIs not listed in the configuration are chained anonymously. All <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5) directives appearing before the first occurrence of <code>chain-uri</code> are inherited by all URIs, unless specifically overridden inside each URI configuration.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8).</p>
<h2>Author</h2>
<p>Originally implemented by Howard Chu; extended by Pierangelo Masarati.</p>
