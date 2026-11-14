---
title: "slapo-pbind(5)"
name: "slapo-pbind"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-pbind/"
description: "slapo-pbind – proxy bind overlay to slapd"
---

<p>slapo-pbind &#8211; proxy bind overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code>pbind</code> overlay to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) forwards Simple Binds on a local database to a remote LDAP server instead of processing them locally. The remote connection is managed using an instance of the ldap backend. The <code>pbind</code> overlay uses a subset of the <i>ldap</i> backend&#8217;s config directives. They are described in more detail in <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5). Note: this overlay is built into the <i>ldap</i> backend; it is not a separate module.</p>
<dl>
<dt><code>overlay pbind</code></p>
<dd>This directive adds the proxy bind overlay to the current backend. The proxy bind overlay may be used with any backend, but it is mainly intended for use with local storage backends.</p>
<dt><code>uri &lt;ldapurl&gt;</code></p>
<dd>LDAP server to use.</p>
<dt><code>tls &lt;TLS parameters&gt;</code></p>
<dd>Specify the use of TLS.</p>
<dt><code>network-timeout &lt;time&gt;</code></p>
<dd>Set the network timeout.</p>
<dt><code>quarantine &lt;quarantine parameters&gt;</code></p>
<dd>Turns on quarantine of URIs that returned <i>LDAP_UNAVAILABLE</i>. </p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8).</p>
<h2>Author</h2>
<p>Howard Chu</p>
