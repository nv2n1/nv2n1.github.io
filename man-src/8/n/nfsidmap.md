---
title: "nfsidmap(8)"
name: "nfsidmap"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfsidmap/"
description: "nfsidmap – The NFS idmapper upcall program"
---

<p>nfsidmap &#8211; The NFS idmapper upcall program</p>
<h2>Synopsis</h2>
<p><code>nfsidmap [-v] [-t timeout] key desc</code><br />
 <code>nfsidmap [-v] [-c]</code><br />
 <code>nfsidmap [-v] [-u|-g|-r user]</code><br />
 <code>nfsidmap -d</code><br />
 <code>nfsidmap -l</code><br />
 <code>nfsidmap -h</code></p>
<h2>Description</h2>
<p>The NFSv4 protocol represents the local system&#8217;s UID and GID values on the wire as strings of the form <i>user [at] domain</i>. The process of translating from UID to string and string to UID is referred to as &quot;ID mapping.&quot; </p>
<p> The system derives the <i>user</i> part of the string by performing a password or group lookup. The lookup mechanism is configured in <i>/etc/idmapd.conf</i>. </p>
<p> By default, the <i>domain</i> part of the string is the system&#8217;s DNS domain name. It can also be specified in <i>/etc/idmapd.conf</i> if the system is multi-homed, or if the system&#8217;s DNS domain name does not match the name of the system&#8217;s Kerberos realm. </p>
<p> The <i>/usr/sbin/nfsidmap</i> program performs translations on behalf of the kernel. The kernel uses the request-key mechanism to perform an upcall. <i>/usr/sbin/nfsidmap</i> is invoked by /sbin/request-key, performs the translation, and initializes a key with the resulting information. The kernel then caches the translation results in the key. </p>
<p> <i>nfsidmap</i> can also clear cached ID map results in the kernel, or revoke one particular key. An incorrect cached key can result in file and directory ownership reverting to &quot;nobody&quot; on NFSv4 mount points. </p>
<p> In addition, the <code>-d</code> and <code>-l</code> options are available to help diagnose misconfigurations. They have no effect on the keyring containing ID mapping results.</p>
<h2>Options</h2>
<dl>
<dt><code>-c </code></p>
<dd>Clear the keyring of all the keys.</p>
<dt><code>-d</code></p>
<dd>Display the system&#8217;s effective NFSv4 domain name on <i>stdout</i>.</p>
<dt><code>-g user</code></p>
<dd>Revoke the gid key of the given user.</p>
<dt><code>-h</code></p>
<dd>Display usage message.</p>
<dt><code>-l</code></p>
<dd>Display on <i>stdout</i> all keys currently in the keyring used to cache ID mapping results. These keys are visible only to the superuser.</p>
<dt><code>-r user</code></p>
<dd>Revoke both the uid and gid key of the given user.</p>
<dt><code>-t timeout</code></p>
<dd>Set the expiration timer, in seconds, on the key. The default is 600 seconds (10 mins).</p>
<dt><code>-u user</code></p>
<dd>Revoke the uid key of the given user.</p>
<dt><code>-v</code></p>
<dd>Increases the verbosity of the output to syslog (can be specified multiple times).</dl>
<h2>Configuring</h2>
<p>The file <i>/etc/request-key.conf</i> will need to be modified so <i>/sbin/request-key</i> can properly direct the upcall. The following line should be added before a call to keyctl negate: </p>
<p> create<tt>&nbsp;<wbr></tt>id_resolver<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/sbin/nfsidmap -t 600 %k %d </p>
<p> This will direct all id_resolver requests to the program <i>/usr/sbin/nfsidmap.</i> The <code>-t 600 </code> defines how many seconds into the future the key will expire. This is an optional parameter for <i>/usr/sbin/nfsidmap</i> and will default to 600 seconds when not specified. </p>
<p> The idmapper system uses four key descriptions: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> uid: Find the UID for the given user</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> gid: Find the GID for the given group</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> user: Find the user name for the given UID</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>group: Find the group name for the given GID</p>
<p> You can choose to handle any of these individually, rather than using the generic upcall program. If you would like to use your own program for a uid lookup then you would edit your request-key.conf so it looks similar to this: </p>
<p> create<tt>&nbsp;<wbr></tt>id_resolver<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>uid:*<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/some/other/program %k %d</p>
<p> create<tt>&nbsp;<wbr></tt>id_resolver<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/usr/sbin/nfsidmap %k %d</p>
<p> Notice that the new line was added above the line for the generic program. request-key will find the first matching line and run the corresponding program. In this case, /some/other/program will handle all uid lookups, and /usr/sbin/nfsidmap will handle gid, user, and group lookups.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/idmapd.conf</i></p>
<dd>ID mapping configuration file</p>
<dt><i>/etc/request-key.conf</i></p>
<dd>Request key configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-idmapd-conf/">idmapd.conf</a></code>(5), <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8)</p>
<h2>Author</h2>
<p>Bryan Schumaker, &lt;bjschuma [at] netapp.com&gt;</p>
