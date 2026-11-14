---
title: "idmap_rfc2307(8)"
name: "idmap_rfc2307"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idmap_rfc2307/"
description: "idmap_rfc2307 – Samba’s idmap_rfc2307 Backend for Winbind"
---

<p>idmap_rfc2307 &#8211; Samba&#8217;s idmap_rfc2307 Backend for Winbind</p>
<h2>Description</h2>
<p>The idmap_rfc2307 plugin provides a way for winbind to read id mappings from records in an LDAP server as defined in RFC 2307. The LDAP server can be stand-alone or the LDAP server provided by the AD server. An AD server is always required to provide the mapping between name and SID, and the LDAP server is queried for the mapping between name and uid/gid. This module implements only the &quot;idmap&quot; API, and is READONLY. </p>
<p> Mappings must be provided in advance by the administrator by creating the user accounts in the Active Directory server and the posixAccount and posixGroup objects in the LDAP server. The names in the Active Directory server and in the LDAP server have to be the same. </p>
<p> This id mapping approach allows the reuse of existing LDAP authentication servers that store records in the RFC 2307 format. </p>
<p> When connecting to the LDAP server provided by an AD server, the parameter m[blue]<code>ldap ssl ads</code>m[] determines whether SSL should be used. When using a stand-alone LDAP server, m[blue]<code>ldap ssl</code>m[] applies.</p>
<h2>Idmap Options</h2>
<p>range = low &#8211; high</p>
<dl>
<dd>Defines the available matching UID and GID range for which the backend is authoritative. Note that the range acts as a filter. If specified any UID or GID stored in AD that fall outside the range is ignored and the corresponding map is discarded. It is intended as a way to avoid accidental UID/GID overlaps between local and remotely defined IDs.</dl>
<p> ldap_server = &lt;ad | stand-alone &gt;</p>
<dl>
<dd>Defines the type of LDAP server to use. This can either be the LDAP server provided by the Active Directory server (ad) or a stand-alone LDAP server.</dl>
<p> bind_path_user</p>
<dl>
<dd>Specifies the search base where user objects can be found in the LDAP server.</dl>
<p> bind_path_group</p>
<dl>
<dd>Specifies the search base where group objects can be found in the LDAP server.</dl>
<p> user_cn = &lt;yes | no&gt;</p>
<dl>
<dd>Query cn attribute instead of uid attribute for the user name in LDAP. This option is not required, the default is no.</dl>
<p> realm</p>
<dl>
<dd>Append @realm to cn for groups (and users if user_cn is set) in LDAP queries. This option is not required, the default is not to append the realm.</dl>
<p> ldap_domain</p>
<dl>
<dd>When using the LDAP server in the Active Directory server, this allows one to specify the domain where to access the Active Directory server. This allows using trust relationships while keeping all RFC 2307 records in one place. This parameter is optional, the default is to access the AD server in the current domain to query LDAP records.</dl>
<p> ldap_url</p>
<dl>
<dd>When using a stand-alone LDAP server, this parameter specifies the ldap URL for accessing the LDAP server.</dl>
<p> ldap_user_dn</p>
<dl>
<dd>Defines the user DN to be used for authentication. The secret for authenticating this user should be stored with net idmap secret (see <code><a href="/docs/linux/man/8-net/">net</a></code>(8)). If absent, an anonymous bind will be performed.</dl>
<h2>Examples</h2>
<p>The following example shows how to retrieve id mappings from a stand-alone LDAP server. This example also shows how to leave a small non conflicting range for local id allocation that may be used in internal backends like BUILTIN. </p>
<dl>
<dd>
<pre> [global]
 idmap config * : backend = tdb
 idmap config * : range = 1000000-1999999
 idmap config DOMAIN : backend = rfc2307
 idmap config DOMAIN : range = 2000000-2999999
 idmap config DOMAIN : ldap_server = stand-alone
 idmap config DOMAIN : ldap_url = <a href="ldap://ldap1.example.com">ldap://ldap1.example.com</a>
 idmap config DOMAIN : ldap_user_dn = cn=ldapmanager,dc=example,dc=com
 idmap config DOMAIN : bind_path_user = ou=People,dc=example,dc=com
 idmap config DOMAIN : bind_path_group = ou=Group,dc=example,dc=com</pre>
</dl>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
