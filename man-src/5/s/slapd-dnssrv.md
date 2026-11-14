---
title: "slapd-dnssrv(5)"
name: "slapd-dnssrv"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-dnssrv/"
description: "slapd-dnssrv – DNS SRV referral backend to slapd"
---

<p>slapd-dnssrv &#8211; DNS SRV referral backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The DNSSRV backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) serves up referrals based upon SRV resource records held in the Domain Name System. </p>
<p> This backend is experimental.</p>
<h2>Configuration</h2>
<p>The DNSSRV backend has no backend nor database specific options. It is configured simply by &quot;database dnssrv&quot; followed a suffix directive, e.g. suffix &quot;&quot;.</p>
<h2>Access Control</h2>
<p>The <code>dnssrv</code> backend does not honor all ACL semantics as described in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5). In fact, this backend only implements the <code>search</code> operation when the <code>manageDSAit</code> control (RFC 3296) is used, otherwise for every operation a referral, whenever appropriate, or an error is returned. Currently, there is no means to condition the returning of the referral by means of ACLs; no access control is implemented, except for <code>read (=r)</code> access to the returned entries, which is actually provided by the frontend. Note, however, that the information returned by this backend is collected through the DNS, so it is public by definition.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file
</dl>
<h2>See Also</h2>
<p><code>&quot;OpenLDAP Root Service &#8211; An experimental LDAP referral service&quot;</code> [RFC 3088],<br />
 <code>&quot;OpenLDAP LDAP Root Service&quot;</code> &lt;<a rel="nofollow" href="http://www.openldap.org/faq/?file=393)">http://www.openldap.org/faq/?file=393)</a>&gt;,<br />
 <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) </p>
