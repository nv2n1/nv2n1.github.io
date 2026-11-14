---
title: "idmap_tdb(8)"
name: "idmap_tdb"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idmap_tdb/"
---

idmap_tdb - Samba's idmap_tdb Backend for Winbind

<h2>Description</h2>

The idmap_tdb plugin is the default backend used by winbindd for storing SID/uid/gid mapping tables. 

 In contrast to read only backends like idmap_rid, it is an allocating backend: This means that it needs to allocate new user and group IDs in order to create new mappings.

<h2>Idmap Options</h2>

range = low - high
<dl><dd>Defines the available matching uid and gid range for which the backend is authoritative.</dl>

<h2>Examples</h2>

This example shows how tdb is used as a the default idmap backend. This configured range is used for uid and gid allocation. 

<dl><dd><pre> [global]
 # &quot;backend = tdb&quot; is redundant here since it is the default
 idmap config * : backend = tdb
 idmap config * : range = 1000000-2000000</pre></dl>

<h2>Author</h2>

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
