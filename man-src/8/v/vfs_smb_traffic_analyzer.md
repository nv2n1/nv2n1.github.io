---
title: "vfs_smb_traffic_analyzer(8)"
name: "vfs_smb_traffic_analyzer"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_smb_traffic_analyzer/"
description: "vfs_smb_traffic_analyzer – log Samba VFS read and write operations through a socket to a helper application"
---

<p>vfs_smb_traffic_analyzer &#8211; log Samba VFS read and write operations through a socket to a helper application</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = smb_traffic_analyzer</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_smb_traffic_analyzer VFS module logs client file operations on a Samba server and sends this data over a socket to a helper program (in the following the &quot;Receiver&quot;), which feeds a SQL database. More information on the helper programs can be obtained from the homepage of the project at: <a rel="nofollow" href="http://holger123.wordpress.com/smb-traffic-analyzer/">http://holger123.wordpress.com/smb-traffic-analyzer/</a> Since the VFS module depends on a receiver that is doing something with the data, it is evolving in it&#8217;s development. Therefore, the module works with different protocol versions, and the receiver has to be able to decode the protocol that is used. The protocol version 1 was introduced to Samba at September 25, 2008. It was a very simple protocol, supporting only a small list of VFS operations, and had several drawbacks. The protocol version 2 is a try to solve the problems version 1 had while at the same time adding new features. With the release of Samba 4.0.0, the module will run protocol version 2 by default.</p>
<h2>Protocol Version 1 Documentation</h2>
<p>vfs_smb_traffic_analyzer protocol version 1 is aware of the following VFS operations:</p>
<dl>
<dd>write</dl>
<dl>
<dd>pwrite</dl>
<dl>
<dd>read</dl>
<dl>
<dd>pread</dl>
<p> vfs_smb_traffic_analyzer sends the following data in a fixed format separated by a comma through either an internet or a unix domain socket: </p>
<dl>
<dd>
<pre> BYTES|USER|DOMAIN|READ/WRITE|SHARE|FILENAME|TIMESTAMP</pre>
</dl>
<p> Description of the records: </p>
<dl>
<dd>&bull; BYTES &#8211; the length in bytes of the VFS operation</dl>
<dl>
<dd>&bull; USER &#8211; the user who initiated the operation</dl>
<dl>
<dd>&bull; DOMAIN &#8211; the domain of the user</dl>
<dl>
<dd>&bull; READ/WRITE &#8211; either &quot;W&quot; for a write operation or &quot;R&quot; for read</dl>
<dl>
<dd>&bull; SHARE &#8211; the name of the share on which the VFS operation occurred</dl>
<dl>
<dd>&bull; FILENAME &#8211; the name of the file that was used by the VFS operation</dl>
<dl>
<dd>&bull; TIMESTAMP &#8211; a timestamp, formatted as &quot;yyyy-mm-dd hh-mm-ss.ms&quot; indicating when the VFS operation occurred</dl>
<dl>
<dd>&bull; IP &#8211; The IP Address (v4 or v6) of the client machine that initiated the VFS operation.</dl>
<p> This module is stackable.</p>
<h2>Drawbacks Of Protocol Version 1</h2>
<p>Several drawbacks have been seen with protocol version 1 over time. </p>
<dl>
<dd>&bull; Problematic parsing &#8211; Protocol version 1 uses hyphen and comma to separate blocks of data. Once there is a filename with a hyphen, you will run into problems because the receiver decodes the data in a wrong way.</dl>
<dl>
<dd>&bull; Insecure network transfer &#8211; Protocol version 1 sends all it&#8217;s data as plaintext over the network.</dl>
<dl>
<dd>&bull; Limited set of supported VFS operations &#8211; Protocol version 1 supports only four VFS operations.</dl>
<dl>
<dd>&bull; No subreleases of the protocol &#8211; Protocol version 1 is fixed on it&#8217;s version, making it unable to introduce new features or bugfixes through compatible sub-releases.</dl>
<h2>Version 2 Of The Protocol</h2>
<p>Protocol version 2 is an approach to solve the problems introduced with protcol v1. From the users perspective, the following changes are most prominent among other enhancements: </p>
<dl>
<dd>&bull; The data from the module may be send encrypted, with a key stored in secrets.tdb (or secrets.ntdb). The Receiver then has to use the same key. The module does AES block encryption over the data to send.</dl>
<dl>
<dd>&bull; The module now can identify itself against the receiver with a sub-release number, where the receiver may run with a different sub-release number than the module. However, as long as both run on the V2.x protocol, the receiver will not crash, even if the module uses features only implemented in the newer subrelease. Ultimately, if the module uses a new feature from a newer subrelease, and the receiver runs an older protocol, it is just ignoring the functionality. Of course it is best to have both the receiver and the module running the same subrelease of the protocol.</dl>
<dl>
<dd>&bull; The parsing problems of protocol V1 can no longer happen, because V2 is marshalling the data packages in a proper way.</dl>
<dl>
<dd>&bull; The module now potentially has the ability to create data on every VFS function. As of protocol V2.0, there is support for 8 VFS functions, namely write,read,pread,pwrite, rename,chdir,mkdir and rmdir. Supporting more VFS functions is one of the targets for the upcoming sub-releases.</dl>
<p> To enable protocol V2, the protocol_version vfs option has to be used (see OPTIONS).</p>
<h2>Options With Protocol V1 And V2.X</h2>
<p>smb_traffic_analyzer:mode = STRING</p>
<dl>
<dd>If STRING matches to &quot;unix_domain_socket&quot;, the module will use a unix domain socket located at /var/tmp/stadsocket, if STRING contains an different string or is not defined, the module will use an internet domain socket for data transfer.</dl>
<p> smb_traffic_analyzer:host = STRING</p>
<dl>
<dd>The module will send the data to the system named with the hostname STRING.</dl>
<p> smb_traffic_analyzer:port = STRING</p>
<dl>
<dd>The module will send the data using the TCP port given in STRING.</dl>
<p> smb_traffic_analyzer:anonymize_prefix = STRING</p>
<dl>
<dd>The module will replace the user names with a prefix given by STRING and a simple hash number. In version 2.x of the protocol, the users SID will also be anonymized.</dl>
<p> smb_traffic_analyzer:total_anonymization = STRING</p>
<dl>
<dd>If STRING matches to &#8216;yes&#8217;, the module will replace any user name with the string given by the option smb_traffic_analyzer:anonymize_prefix, without generating an additional hash number. This means that any transfer data will be mapped to a single user, leading to a total anonymization of user related data. In version 2.x of the protocol, the users SID will also be anonymized.</dl>
<p> smb_traffic_analyzer:protocol_version = STRING</p>
<dl>
<dd>If STRING matches to V1, the module will use version 1 of the protocol. If STRING is not given, the module will use version 2 of the protocol, which is the default.</dl>
<h2>Examples</h2>
<p>Running protocol V2 on share &quot;example_share&quot;, using an internet socket. </p>
<dl>
<dd>
<pre> <i>[example_share]</i>
 m[blue]<code>path = /data/example</code>m[]
 m[blue]<code>vfs_objects = smb_traffic_analyzer</code>m[]
 m[blue]<code>smb_traffic_analyzer:host = examplehost</code>m[]
 m[blue]<code>smb_traffic_analyzer:port = 3491</code>m[]</pre>
</dl>
<p> The module running on share &quot;example_share&quot;, using a unix domain socket </p>
<dl>
<dd>
<pre> <i>[example_share]</i>
 m[blue]<code>path = /data/example</code>m[]
 m[blue]<code>vfs objects = smb_traffic_analyzer</code>m[]
 m[blue]<code>smb_traffic_analyzer:mode = unix_domain_socket</code>m[]</pre>
</dl>
<p> The module running on share &quot;example_share&quot;, using an internet socket, connecting to host &quot;examplehost&quot; on port 3491. </p>
<dl>
<dd>
<pre> <i>[example_share]</i>
 m[blue]<code>path = /data/example</code>m[]
 m[blue]<code>vfs objects = smb_traffic_analyzer</code>m[]
 m[blue]<code>smb_traffic_analyzer:host = examplehost</code>m[]
 m[blue]<code>smb_traffic_analyzer:port = 3491</code>m[]</pre>
</dl>
<p> The module running on share &quot;example_share&quot;, using an internet socket, connecting to host &quot;examplehost&quot; on port 3491, anonymizing user names with the prefix &quot;User&quot;. </p>
<dl>
<dd>
<pre> <i>[example_share]</i>
 m[blue]<code>path = /data/example</code>m[]
 m[blue]<code>vfs objects = smb_traffic_analyzer</code>m[]
 m[blue]<code>smb_traffic_analyzer:host = examplehost</code>m[]
 m[blue]<code>smb_traffic_analyzer:port = 3491</code>m[]
 m[blue]<code>smb_traffic_analyzer:anonymize_prefix = User</code>m[]</pre>
</dl>
<h2>Version</h2>
<p>This man page is correct for version 3.3 of the Samba suite.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The original version of the VFS module and the helper tools were created by Holger Hetterich.</p>
