---
title: "ipa-rmkeytab(1)"
name: "ipa-rmkeytab"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-rmkeytab/"
description: "ipa-rmkeytab – Remove a kerberos principal from a keytab"
---

<h2>NAME</h2>
<p> ipa-rmkeytab &#8211; Remove a kerberos principal from a keytab</p>
<h2>SYNOPSIS</h2>
<p> ipa-rmkeytab [ <code>-p</code> principal-name ] [ <code>-k</code> keytab-file ] [ <code>-r</code> realm ] [ <code>-d</code> ] </p>
<h2>DESCRIPTION</h2>
<p> Removes a kerberos principal from a <i>keytab</i>. </p>
<p> Kerberos keytabs are used for services (like sshd) to perform kerberos authentication. A keytab is a file with one or more secrets (or keys) for a kerberos principal. </p>
<p> A kerberos service principal is a kerberos identity that can be used for authentication. Service principals contain the name of the service, the hostname of the server, and the realm name. </p>
<p> ipa-rmkeytab provides two ways to remove principals. A specific principal can be removed or all principals for a given realm can be removed. </p>
<p> All encryption types and versions of a principal are removed. </p>
<p> The realm may be included when removing a specific principal but it is not required. </p>
<p> <code>NOTE:</code> removing a principal from the keytab does not affect the Kerberos principal stored in the IPA server. It merely removes the entry from the local keytab.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p principal-name</code></p>
<dd> The non-realm part of the full principal name.</p>
<dt><code>-k keytab-file</code></p>
<dd> The keytab file to remove the principal(s) from.</p>
<dt><code>-r realm</code></p>
<dd> A realm to remove all principals for.</p>
<dt><code>-d</code></p>
<dd> Debug mode. Additional information is displayed.</dl>
<h2>EXAMPLES</h2>
<p> Remove the NFS service principal on the host foo.example.com from /tmp/nfs.keytab. </p>
<p>#&nbsp;<wbr>ipa-rmkeytab -p nfs/foo.example.com -k&nbsp;<wbr>/tmp/nfs.keytab </p>
<p> Remove the ldap service principal on the host foo.example.com from /etc/krb5.keytab. </p>
<p>#&nbsp;<wbr>ipa-rmkeytab -p ldap/foo.example.com -k&nbsp;<wbr>/etc/krb5.keytab </p>
<p> Remove all principals for the realm EXAMPLE.COM. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>ipa-rmkeytab -r EXAMPLE.COM -k&nbsp;<wbr>/etc/krb5.keytab</p>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<p> 1 Kerberos initialization failed </p>
<p> 2 Memory allocation error </p>
<p> 3 Unable to open keytab </p>
<p> 4 Unable to parse the principal name </p>
<p> 5 Principal name or realm not found in keytab </p>
<p> 6 Unable to remove principal from keytab </p>
<h2>Index</h2>
