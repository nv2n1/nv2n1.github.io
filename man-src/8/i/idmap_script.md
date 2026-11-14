---
title: "idmap_script(8)"
name: "idmap_script"
section: "8"
letter: "i"
url: "/docs/linux/man/8-idmap_script/"
---

idmap_script - Samba's idmap_script Backend for Winbind

<h2>Description</h2>

The idmap_script plugin is a substitute for the idmap_tdb2 backend used by winbindd for storing SID/uid/gid mapping tables in clustered environments with Samba and CTDB. It is a read only backend that uses a script to perform mapping. 

 It was developed out of the idmap_tdb2 back end and does not store SID/uid/gid mappings in a TDB, since the winbind_cache tdb will store the mappings once they are provided.

<h2>Idmap Options</h2>

range = low - high
<dl><dd>Defines the available matching uid and gid range for which the backend is authoritative.</dl>
 

 script
<dl><dd>This option can be used to configure an external program for performing id mappings.</dl>

<h2>Idmap Script</h2>

The tdb2 idmap backend supports an external program for performing id mappings through the smb.conf option <i>idmap config * : script</i> or its deprecated legacy form <i>idmap : script</i>. 

 The mappings obtained by the script are then stored in the idmap tdb2 database instead of mappings created by the incrementing id counters. It is therefore important that the script covers the complete range of SIDs that can be passed in for SID to Unix ID mapping, since otherwise SIDs unmapped by the script might get mapped to IDs that had previously been mapped by the script. 

 The script should accept the following command line options. 

<dl><dd><pre> SIDTOID S-1-xxxx
 IDTOSID UID xxxx
 IDTOSID GID xxxx
 IDTOSID XID xxxx</pre></dl>
 

 And it should return one of the following responses as a single line of text. 

<dl><dd><pre> UID:yyyy
 GID:yyyy
 XID:yyyy
 SID:ssss
 ERR:yyyy</pre></dl>
 

 XID indicates that the ID returned should be both a UID and a GID. That is, it requests an ID_TYPE_BOTH, but it is ultimately up to the script whether or not it can honor that request. It can choose to return a UID or a GID mapping only.

<h2>Examples</h2>

This example shows how script is used as a the default idmap backend using an external program via the script parameter: 

<dl><dd><pre> [global]
 idmap config * : backend = script
 idmap config * : range = 1000000-2000000
 idmap config * : script = /usr/local/samba/bin/idmap_script.sh</pre></dl>
 

 This shows a simple script to partially perform the task: 

<dl><dd><pre> #!/bin/sh
 #
 # Uncomment this if you want some logging
 #echo $@ &gt;&gt; /tmp/idmap.sh.log
 if [ &quot;$1&quot; == &quot;SIDTOID&quot; ]
 then
 # Note. The number returned has to be within the range defined
 #echo &quot;Sending UID:1000005&quot; &gt;&gt; /tmp/idmap.sh.log
 echo &quot;UID:1000005&quot;
 exit 0
 else
 #echo &quot;Sending ERR: No idea what to do&quot; &gt;&gt; /tmp/idmap.sh.log
 echo &quot;ERR: No idea what to do&quot;
 exit 1
 fi</pre></dl>
 

 Clearly, this script is not enough, as it should probably use wbinfo to determine if an incoming SID is a user or group SID and then look up the mapping in a table or use some other mechanism for mapping SIDs to UIDs and etc. 

 Please be aware that the script is called with the _NO_WINBINDD environment variable set to 1. This prevents recursive calls into winbind from the script both via explicit calls to wbinfo and via implicit calls via nss_winbind. For example a call to ls -l could trigger such an infinite recursion. 

 It is safe to call wbinfo -n and wbinfo -s from within an idmap script. To do so, the script must unset the _NO_WINBINDD environment variable right before the call to wbinfo and set it to 1 again right after wbinfo has returned to protect against the recursion.

<h2>Author</h2>

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
