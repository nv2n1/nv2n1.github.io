---
title: "gssd(8)"
name: "gssd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gssd/"
description: "rpc.gssd – RPCSEC_GSS daemon"
---

<p>rpc.gssd &#8211; RPCSEC_GSS daemon</p>
<h2>Synopsis</h2>
<p><code>rpc.gssd</code> [<code>-DfMnlvr</code>] [<code>-k</code> <i>keytab</i>] [<code>-p</code> <i>pipefsdir</i>] [<code>-d</code> <i>ccachedir</i>] [<code>-t</code> <i>timeout</i>] [<code>-R</code> <i>realm</i>]</p>
<h2>Introduction</h2>
<p>The RPCSEC_GSS protocol, defined in RFC 5403, is used to provide strong security for RPC-based protocols such as NFS. </p>
<p> Before exchanging RPC requests using RPCSEC_GSS, an RPC client must establish a GSS <i>security context</i>. A security context is shared state on each end of a network transport that enables GSS-API security services. </p>
<p> Security contexts are established using <i>security credentials</i>. A credential grants temporary access to a secure network service, much as a railway ticket grants temporary access to use a rail service. </p>
<p> A user typically obtains a credential by providing a password to the <code><a href="/docs/linux/man/1-kinit/">kinit</a></code>(1) command, or via a PAM library at login time. A credential acquired with a <i>user principal</i> is known as a <i>user credential</i> (see <code><a href="/docs/linux/man/1-kerberos/">kerberos</a></code>(1) for more on principals). </p>
<p> For certain operations, a credential is required which represents no user, is otherwise unprivileged, and is always available. This is referred to as a <i>machine credential</i>. </p>
<p> Machine credentials are typically established using a <i>service principal</i>, whose encrypted password, called its <i>key</i>, is stored in a file, called a <i>keytab</i>, to avoid requiring a user prompt. A machine credential effectively does not expire because the system can renew it as needed without user intervention. </p>
<p> Once obtained, credentials are typically stored in local temporary files with well-known pathnames.</p>
<h2>Description</h2>
<p>To establish GSS security contexts using these credential files, the Linux kernel RPC client depends on a userspace daemon called <code>rpc.gssd</code>. The <code>rpc.gssd</code> daemon uses the rpc_pipefs filesystem to communicate with the kernel.</p>
<h3>User Credentials</h3>
<p>When a user authenticates using a command such as <code><a href="/docs/linux/man/1-kinit/">kinit</a></code>(1), the resulting credential is stored in a file with a well-known name constructed using the user&#8217;s UID. </p>
<p> To interact with an NFS server on behalf of a particular Kerberos-authenticated user, the Linux kernel RPC client requests that <code>rpc.gssd</code> initialize a security context with the credential in that user&#8217;s credential file. </p>
<p> Typically, credential files are placed in <i>/tmp</i>. However, <code>rpc.gssd</code> can search for credential files in more than one directory. See the description of the <code>-d</code> option for details.</p>
<h3>Machine Credentials</h3>
<p>A user credential is established by a user and is then shared with the kernel and <code>rpc.gssd</code>. A machine credential is established by <code>rpc.gssd</code> for the kernel when there is no user. Therefore <code>rpc.gssd</code> must already have the materials on hand to establish this credential without requiring user intervention. </p>
<p> <code>rpc.gssd</code> searches the local system&#8217;s keytab for a principal and key to use to establish the machine credential. By default, <code>rpc.gssd</code> assumes the file <i>/etc/krb5.keytab</i> contains principals and keys that can be used to obtain machine credentials. </p>
<p> <code>rpc.gssd</code> searches in the following order for a principal to use. The first matching credential is used. For the search, &lt;hostname&gt; and &lt;REALM&gt; are replaced with the local system&#8217;s hostname and Kerberos realm. </p>
<p>&lt;HOSTNAME&gt;$@&lt;REALM&gt; </p>
<p>root/&lt;hostname&gt;@&lt;REALM&gt; </p>
<p>nfs/&lt;hostname&gt;@&lt;REALM&gt; </p>
<p>host/&lt;hostname&gt;@&lt;REALM&gt; </p>
<p>root/&lt;anyname&gt;@&lt;REALM&gt; </p>
<p>nfs/&lt;anyname&gt;@&lt;REALM&gt; </p>
<p>host/&lt;anyname&gt;@&lt;REALM&gt; </p>
<p> The &lt;anyname&gt; entries match on the service name and realm, but ignore the hostname. These can be used if a principal matching the local host&#8217;s name is not found. </p>
<p> Note that the first principal in the search order is a user principal that enables Kerberized NFS when the local system is joined to an Active Directory domain using Samba. A password for this principal must be provided in the local system&#8217;s keytab. </p>
<p> You can specify another keytab by using the <code>-k</code> option if <i>/etc/krb5.keytab</i> does not exist or does not provide one of these principals.</p>
<h3>Credentials for UID 0</h3>
<p>UID 0 is a special case. By default <code>rpc.gssd</code> uses the system&#8217;s machine credentials for UID 0 accesses that require GSS authentication. This limits the privileges of the root user when accessing network resources that require authentication. </p>
<p> Specify the <code>-n</code> option when starting <code>rpc.gssd</code> if you&#8217;d like to force the root user to obtain a user credential rather than use the local system&#8217;s machine credential. </p>
<p> When <code>-n</code> is specified, the kernel continues to request a GSS context established with a machine credential for NFSv4 operations, such as SETCLIENTID or RENEW, that manage state. If <code>rpc.gssd</code> cannot obtain a machine credential (say, the local system has no keytab), NFSv4 operations that require machine credentials will fail.</p>
<h3>Encryption types</h3>
<p>A realm administrator can choose to add keys encoded in a number of different encryption types to the local system&#8217;s keytab. For instance, a host/ principal might have keys for the <code>aes256-cts-hmac-sha1-96</code>, <code>aes128-cts-hmac-sha1-96</code>, <code>des3-cbc-sha1</code>, and <code>arcfour-hmac</code> encryption types. This permits <code>rpc.gssd</code> to choose an appropriate encryption type that the target NFS server supports. </p>
<p> These encryption types are stronger than legacy single-DES encryption types. To interoperate in environments where servers support only weak encryption types, you can restrict your client to use only single-DES encryption types by specifying the <code>-l</code> option when starting <code>rpc.gssd</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-D</code></p>
<dd>The server name passed to GSSAPI for authentication is normally the name exactly as requested. e.g. for NFS it is the server name in the &quot;servername:/path&quot; mount request. Only if this servername appears to be an IP address (IPv4 or IPv6) or an unqualified name (no dots) will a reverse DNS lookup will be performed to get the canoncial server name. </p>
<p> If <code>-D</code> is present, a reverse DNS lookup will <i>always</i> be used, even if the server name looks like a canonical name. So it is needed if partially qualified, or non canonical names are regularly used. </p>
<p> Using <code>-D</code> can introduce a security vulnerability, so it is recommended that <code>-D</code> not be used, and that canonical names always be used when requesting services.</p>
<dt><code>-f</code></p>
<dd>Runs <code>rpc.gssd</code> in the foreground and sends output to stderr (as opposed to syslogd)</p>
<dt><code>-n</code></p>
<dd>When specified, UID 0 is forced to obtain user credentials which are used instead of the local system&#8217;s machine credentials.</p>
<dt><code>-k </code><i>keytab</i></p>
<dd>Tells <code>rpc.gssd</code> to use the keys found in <i>keytab</i> to obtain machine credentials. The default value is <i>/etc/krb5.keytab</i>.</p>
<dt><code>-l</code></p>
<dd>When specified, restricts <code>rpc.gssd</code> to sessions to weak encryption types such as <code>des-cbc-crc</code>. This option is available only when the local system&#8217;s Kerberos library supports settable encryption types.</p>
<dt><code>-p </code><i>path</i></p>
<dd>Tells <code>rpc.gssd</code> where to look for the rpc_pipefs filesystem. The default value is <i>/var/lib/nfs/rpc_pipefs</i>.</p>
<dt><code>-d </code><i>search-path</i></p>
<dd>This option specifies a colon separated list of directories that <code>rpc.gssd</code> searches for credential files. The default value is <i>/tmp:/run/user/%U</i>. The literal sequence &quot;%U&quot; can be specified to substitue the UID of the user for whom credentials are being searched.</p>
<dt><code>-M</code></p>
<dd>By default, machine credentials are stored in files in the first directory in the credential directory search path (see the <code>-d</code> option). When <code>-M</code> is set, <code>rpc.gssd</code> stores machine credentials in memory instead.</p>
<dt><code>-v</code></p>
<dd>Increases the verbosity of the output (can be specified multiple times).</p>
<dt><code>-r</code></p>
<dd>If the RPCSEC_GSS library supports setting debug level, increases the verbosity of the output (can be specified multiple times).</p>
<dt><code>-R </code><i>realm</i></p>
<dd>Kerberos tickets from this <i>realm</i> will be preferred when scanning available credentials cache files to be used to create a context. By default, the default realm, as configured in the Kerberos configuration file, is preferred.</p>
<dt><code>-t </code><i>timeout</i></p>
<dd>Timeout, in seconds, for kernel GSS contexts. This option allows you to force new kernel contexts to be negotiated after <i>timeout</i> seconds, which allows changing Kerberos tickets and identities frequently. The default is no explicit timeout, which means the kernel context will live the lifetime of the Kerberos service ticket used in its creation.</p>
<dt><code>-T timeout</code></p>
<dd>Timeout, in seconds, to create an RPC connection with a server while establishing an authenticated gss context for a user. The default timeout is set to 5 seconds. If you get messages like &quot;WARNING: can&#8217;t create tcp rpc_clnt to server %servername% for user with uid %uid%: RPC: Remote system error &#8211; Connection timed out&quot;, you should consider an increase of this timeout.</dl>
<h2>Configuration File</h2>
<p>Many of the options that can be set on the command line can also be controlled through values set in the <code>[gssd]</code> section of the <i>/etc/nfs.conf</i> configuration file. Values recognized include:</p>
<dl>
<dt><code>use-memcache</code></p>
<dd>A Boolean flag equivalent to <code>-M</code>.</p>
<dt><code>use-machine-creds</code></p>
<dd>A Boolean flag. Setting to <code>false</code> is equivalent to giving the <code>-n</code> flag.</p>
<dt><code>avoid-dns</code></p>
<dd>Setting to <code>false</code> is equivalent to providing the <code>-D</code> flag.</p>
<dt><code>limit-to-legacy-enctypes</code></p>
<dd>Equivalent to <code>-l</code>.</p>
<dt><code>context-timeout</code></p>
<dd>Equivalent to <code>-T</code>.</p>
<dt><code>rpc-timeout</code></p>
<dd>Equivalent to <code>-t</code>.</p>
<dt><code>pipefs-directory</code></p>
<dd>Equivalent to <code>-p</code>.</p>
<dt><code>keytab-file</code></p>
<dd>Equivalent to <code>-k</code>.</p>
<dt><code>cred-cache-directory</code></p>
<dd>Equivalent to <code>-d</code>.</p>
<dt><code>preferred-realm</code></p>
<dd>Equivalent to <code>-R</code>. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rpc-svcgssd/">rpc.svcgssd</a></code>(8), <code><a href="/docs/linux/man/1-kerberos/">kerberos</a></code>(1), <code><a href="/docs/linux/man/1-kinit/">kinit</a></code>(1), <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5)</p>
<h2>Authors</h2>
<p>Dug Song &lt;dugsong [at] umich.edu&gt;<br />
 Andy Adamson &lt;andros [at] umich.edu&gt;<br />
 Marius Aamodt Eriksen &lt;marius [at] umich.edu&gt;<br />
 J. Bruce Fields &lt;bfields [at] umich.edu&gt;</p>
