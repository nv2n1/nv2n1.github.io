---
title: "idmap_tdb2(8)"
name: "idmap_tdb2"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idmap_tdb2/"
---

idmap_tdb2 - Samba's idmap_tdb2 Backend for Winbind

<h2>Description</h2>

The idmap_tdb2 plugin is a substitute for the default idmap_tdb backend used by winbindd for storing SID/uid/gid mapping tables in clustered environments with Samba and CTDB. 

 In contrast to read only backends like idmap_rid, it is an allocating backend: This means that it needs to allocate new user and group IDs in order to create new mappings.

<h2>Idmap Options</h2>

range = low - high
<dl><dd>Defines the available matching uid and gid range for which the backend is authoritative.</dl>
 

 script
<dl><dd>This option can be used to configure an external program for performing id mappings instead of using the tdb counter. The mappings are then stored int tdb2 idmap database. For details see the section on IDMAP SCRIPT below.</dl>

<h2>Idmap Script</h2>

The tdb2 idmap backend supports an external program for performing id mappings through the smb.conf option <i>idmap config * : script</i> or its deprecated legacy form <i>idmap : script</i>. 

 The mappings obtained by the script are then stored in the idmap tdb2 database instead of mappings created by the incrementing id counters. It is therefore important that the script covers the complete range of SIDs that can be passed in for SID to Unix ID mapping, since otherwise SIDs unmapped by the script might get mapped to IDs that had previously been mapped by the script. 

 The script should accept the following command line options. 

<dl><dd><pre> SIDTOID S-1-xxxx
 IDTOSID UID xxxx
 IDTOSID GID xxxx</pre></dl>
 

 And it should return one of the following responses as a single line of text. 

<dl><dd><pre> UID:yyyy
 GID:yyyy
 SID:yyyy
 ERR:yyyy</pre></dl>

<h2>Examples</h2>

This example shows how tdb2 is used as a the default idmap backend. 

<dl><dd><pre> [global]
 idmap config * : backend = tdb2
 idmap config * : range = 1000000-2000000</pre></dl>
 

 This example shows how tdb2 is used as a the default idmap backend using an external program via the script parameter: 

<dl><dd><pre> [global]
 idmap config * : backend = tdb2
 idmap config * : range = 1000000-2000000
 idmap config * : script = /usr/local/samba/bin/idmap_script.sh</pre></dl>

<h2>Author</h2>

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
