---
title: "idmap_nss(8)"
name: "idmap_nss"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idmap_nss/"
---

idmap_nss - Samba's idmap_nss Backend for Winbind

<h2>Description</h2>

The idmap_nss plugin provides a means to map Unix users and groups to Windows accounts and obsoletes the &quot;winbind trusted domains only&quot; smb.conf option. This provides a simple means of ensuring that the SID for a Unix user named jsmith is reported as the one assigned to DOMAIN\jsmith which is necessary for reporting ACLs on files and printers stored on a Samba member server.

<h2>Examples</h2>

This example shows how to use idmap_nss to check the local accounts for its own domain while using allocation to create new mappings for trusted domains 

<dl><dd><pre> [global]
 idmap config * : backend = tdb
 idmap config * : range = 1000000-1999999
 idmap config SAMBA : backend = nss
 idmap config SAMBA : range = 1000-999999</pre></dl>

<h2>Author</h2>

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
