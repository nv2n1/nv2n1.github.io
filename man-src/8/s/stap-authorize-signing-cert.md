---
title: "stap-authorize-signing-cert(8)"
name: "stap-authorize-signing-cert"
section: "8"
letter: "s"
url: "/docs/linux/man/8-stap-authorize-signing-cert/"
description: "stap-authorize-signing-cert – systemtap signing authorization utility"
---

<p>stap-authorize-signing-cert &#8211; systemtap signing authorization utility </p>
<h2>Synopsis</h2>
<p><code>stap-authorize-signing-cert </code><i>CERTFILE</i> [ <i>DIRNAME</i> ] </p>
<h2>Description</h2>
<p>The <i>staprun</i> program will load modules for members of the group <i>stapusr</i> if they are signed by a trusted signer. A trusted signer is usually a <i>systemtap</i> compile server which signs modules when the client (<i>stap-client</i>) specifies the <code>&#8211;unprivileged</code> option. The trustworthiness of a given signer can not be determined automatically without a trusted certificate authority issuing systemtap signing certificates. This is not practical in everyday use and so, <i>staprun</i> must authenticate servers against its own database of trusted signers. In this context, establishing a given signer as trusted means adding that signer[aq]s certificate to <i>staprun</i>[aq]s database of trusted signers. The <i>stap-authorize-signing-cert</i> program adds the given signing certificate to the given certificate database, making that signer a trusted server for <i>staprun</i> when using that database. </p>
<h2>Arguments</h2>
<p>The <i>stap-authorize-signing-cert</i> program accepts two arguments: </p>
<dl>
<dt><code>CERTFILE</code></p>
<dd>This is the name of the file containing the certificate of the new trusted signer. For systemtap compile servers, this is the file named <i>stap.cert</i> which can be found in the server[aq]s certificate database. On the server host, for servers started by the <i>stap-server</i> service, this database can be found in <i>/var/lib/stap-server/.systemtap/ssl/server/</i>. For servers run by other non-root users, this database can be found in <i>$HOME/.systemtap/ssl/server/</i>. For root users (EUID=0), it can be found in the stappaths (7) manual page. </p>
<dt><code>DIRNAME</code></p>
<dd>This optional argument is the name of the directory containing the certificate database to which the certificate is to be added. If not specified, the default can be found in the stappaths (7) manual page. That is, the default result is that all users on the local host will trust this signer. Note that this default directory is only writable by root. </p>
</dl>
<h2>Safety And Security</h2>
<p>Systemtap is an administrative tool. It exposes kernel internal data structures and potentially private user information. See the <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) manual page for additional information on safety and security. </p>
<p> <i>Systemtap</i> uses Network Security Services (NSS) for module signing and verification. The NSS tool <i>certutil</i> is used for the generation of certificates. The related certificate databases must be protected in order to maintain the security of the system. Use of the utilities provided will help to ensure that the proper protection is maintained. <i>staprun</i> will check for proper access permissions before making use of any certificate database.</p>
<h2>Files</h2>
<dl>
<dt>/var/lib/stap-server/.systemtap/ssl/server/stap.cert</p>
<dd>Signing certificate for servers started by the <i>stap-server</i> service. </p>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-stap/">stap</a></i>(1), <i><a href="/docs/linux/man/7-stappathss/">stappathss</a></i>(7), <i><a href="/docs/linux/man/8-staprun/">staprun</a></i>(8), <i><a href="/docs/linux/man/8-stap-server/">stap-server</a></i>(8), <i><a href="/docs/linux/man/8-stap-client/">stap-client</a></i>(8), <i>NSS</i>, <i>certutil</i> </p>
<h2>Bugs</h2>
<p>Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sources.redhat.com/systemtap/">http://sources.redhat.com/systemtap/</a></code>, <code>&lt;systemtap [at] sources.redhat.com&gt;</code>. </p>
