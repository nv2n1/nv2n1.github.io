---
title: "idmap_rid(8)"
name: "idmap_rid"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idmap_rid/"
---

idmap_rid - Samba's idmap_rid Backend for Winbind

<h2>Description</h2>

The idmap_rid backend provides a way to use an algorithmic mapping scheme to map UIDs/GIDs and SIDs. No database is required in this case as the mapping is deterministic. 

 Note that the idmap_rid module has changed considerably since Samba versions 3.0. and 3.2. Currently, there should to be an explicit idmap configuration for each domain that should use the idmap_rid backend, using disjoint ranges. One usually needs to define a writeable default idmap range, using a backend like <i>tdb</i> or <i>ldap</i> that can create unix ids, in order to be able to map the BUILTIN sids and other domains, and also in order to be able to create group mappings. See the example below. 

 Note that the old syntax <i>idmap backend = rid:&quot;DOM1=range DOM2=range2 ...&quot;</i> is not supported any more since Samba version 3.0.25.

<h2>Idmap Options</h2>

range = low - high
<dl><dd>Defines the available matching uid and gid range for which the backend is authoritative. Note that the range acts as a filter. If algorithmically determined UID or GID fall outside the range, they are ignored and the corresponding map is discarded. It is intended as a way to avoid accidental UID/GID overlaps between local and remotely defined IDs.</dl>
 

 base_rid = INTEGER
<dl><dd>Defines the base integer used to build SIDs out of a UID or a GID, and to rebase the UID or GID to be obtained from a SID. This means SIDs with a RID less than the base rid are filtered. The default is not to restrict the allowed rids at all, i.e. a base_rid value of 0. 

 Use of this parameter is deprecated.</dl>

<h2>The Mapping Formulas</h2>

The Unix ID for a RID is calculated this way: 

<dl><dd><pre> ID = RID - BASE_RID + LOW_RANGE_ID.</pre></dl>
 

 Correspondingly, the formula for calculating the RID for a given Unix ID is this: 

<dl><dd><pre> RID = ID + BASE_RID - LOW_RANGE_ID.</pre></dl>

<h2>Examples</h2>

This example shows how to configure two domains with idmap_rid, the principal domain and a trusted domain, leaving the default id mapping scheme at tdb. The example also demonstrates the use of the base_rid parameter for the trusted domain. 

<dl><dd><pre> [global]
 security = domain
 workgroup = MAIN
 idmap config * : backend = tdb
 idmap config * : range = 1000000-1999999
 idmap config MAIN : backend = rid
 idmap config MAIN : range = 10000 - 49999
 idmap config TRUSTED : backend = rid
 idmap config TRUSTED : range = 50000 - 99999</pre></dl>

<h2>Author</h2>

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
