---
title: "idmap_hash(8)"
name: "idmap_hash"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idmap_hash/"
---

idmap_hash - DO NOT USE THIS BACKEND

<h2>Description</h2>

DO NOT USE THIS PLUGIN The idmap_hash plugin implements a hashing algorithm used to map SIDs for domain users and groups to 31-bit uids and gids, respectively. This plugin also implements the nss_info API and can be used to support a local name mapping files if enabled via the &quot;winbind normalize names&quot; and &quot;winbind nss info&quot; parameters in smb.conf. The module divides the range into subranges for each domain that is being handled by the idmap config. The module needs the complete UID and GID range to be able to map all SIDs. The lowest value for the range should be the smallest ID available in the system. This is normally 1000. The highest ID should be set to 2147483647. A smaller range will lead to issues because of the hashing algorithm used. The overall range to map all SIDs is 0 - 2147483647. Any range smaller than 0 - 2147483647 will filter some SIDs. As we can normally only start with 1000, we are not able to map 1000 SIDs. This already can lead to issues. The smaller the range the less SIDs can be mapped. We do not recommend to use this plugin. It will be removed in a future release of Samba.

<h2>Idmap Options</h2>

name_map
<dl><dd>Specifies the absolute path to the name mapping file used by the nss_info API. Entries in the file are of the form &quot;<i>unix name</i> = <i>qualified domain name</i>&quot;. Mapping of both user and group names is supported.</dl>

<h2>Examples</h2>

The following example utilizes the idmap_hash plugin for the idmap and nss_info information. 

<dl><dd><pre> [global]
 idmap config * : backend = hash
 idmap config * : range = 1000-2147483647
 winbind nss info = hash
 winbind normalize names = yes
 idmap_hash:name_map = /etc/samba/name_map.cfg</pre></dl>

<h2>Author</h2>

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
