---
title: "trust(1)"
name: "trust"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trust/"
description: "trust – Tool for operating on the trust policy store"
---

<h2 class="name">NAME</h2>
<p> trust &#8211; Tool for operating on the trust policy store </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>trust list</code></p>
<dt> <code>trust extract</code> &#8211;filter=&lt;what&gt; &#8211;format=&lt;type&gt; /path/to/destination <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt></p>
<dt> <code>trust anchor</code> /path/to/certificate.crt <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt></p>
<dt> <code>trust dump</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>trust</code></p>
<dd>is a command line tool to examine and modify the shared trust policy store. </p>
<p> See the various sub commands below. The following global options can be used: </p>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> Run in verbose mode with debug output.</dl>
<p> <code>-q, &#8211;quiet</code></p>
<dl>
<dt>
<dd> Run in quiet mode without warning or failure messages.</dl>
<h2>LIST</h2>
<p> List trust policy store items. </p>
<dl>
<dt>
<dd>
<pre>
$ trust list
</pre>
</dl>
<p> List information about the various items in the trust policy store. Each item is listed with it&#8217;s PKCS#11 URI and some descriptive information. </p>
<p> You can specify the following options to control what to list. </p>
<p> <code>&#8211;filter=&lt;what&gt;</code></p>
<dl>
<dt>
<dd> Specifies what certificates to extract. You can specify the following values: </p>
<p> <code>ca-anchors</code></p>
<dl>
<dt>
<dd> Certificate anchors</dl>
<p> <code>trust-policy</code></p>
<dl>
<dt>
<dd> Anchors and blocklist (default)</dl>
<p> <code>blocklist</code></p>
<dl>
<dt>
<dd> Distrusted certificates</dl>
<p> <code>certificates</code></p>
<dl>
<dt>
<dd> All certificates</dl>
<p> <code>pkcs11:object=xx</code></p>
<dl>
<dt>
<dd> A PKCS#11 URI to filter with</dl>
<p> If an output format is chosen that cannot support type what has been specified by the filter, a message will be printed. </p>
<p> None of the available formats support storage of blocklist entries that do not contain a full certificate. Thus any certificates distrusted by their issuer and serial number alone, are not included in the extracted blocklist.</dl>
<p> <code>&#8211;purpose=&lt;usage&gt;</code></p>
<dl>
<dt>
<dd> Limit to certificates usable for the given purpose You can specify one of the following values: </p>
<p> <code>server-auth</code></p>
<dl>
<dt>
<dd> For authenticating servers</dl>
<p> <code>client-auth</code></p>
<dl>
<dt>
<dd> For authenticating clients</dl>
<p> <code>email</code></p>
<dl>
<dt>
<dd> For email protection</dl>
<p> <code>code-signing</code></p>
<dl>
<dt>
<dd> For authenticated signed code</dl>
<p> <code>1.2.3.4.5&#8230;</code></p>
<dl>
<dt>
<dd> An arbitrary purpose OID</dl>
</dl>
<h2>ANCHOR</h2>
<p> Store or remove trust anchors. </p>
<dl>
<dt>
<dd>
<pre>
$ trust anchor /path/to/certificate.crt
$ trust anchor --remove /path/to/certificate.crt
$ trust anchor --remove &quot;pkcs11:id=%AA%BB%CC%DD%EE;type=cert&quot;
</pre>
</dl>
<p> Store or remove trust anchors in the trust policy store. These are usually root certificate authorities. </p>
<p> Specify either the <code>&#8211;store</code> or <code>&#8211;remove</code> operations. If no operation is specified then <code>&#8211;store</code> is assumed. </p>
<p> When storing, one or more certificate files are expected on the command line. These are stored as anchors, unless they are already present. </p>
<p> When removing an anchor, either specify certificate files or PKCS#11 URI&#8217;s on the command line. Matching anchors will be removed. </p>
<p> It may be that this command needs to be run as root in order to modify the system trust policy store, if no user specific store is available. </p>
<p> You can specify the following options. </p>
<p> <code>&#8211;remove</code></p>
<dl>
<dt>
<dd> Remove one or more anchors from the trust policy store. Specify certificate files or PKCS#11 URI&#8217;s on the command line.</dl>
<p> <code>&#8211;store</code></p>
<dl>
<dt>
<dd> Store one or more anchors to the trust policy store. Specify certificate files on the command line.</dl>
<h2>EXTRACT</h2>
<p> Extract trust policy from the shared trust policy store. </p>
<dl>
<dt>
<dd>
<pre>
$ trust extract --format=x509-directory --filter=ca-anchors /path/to/directory
</pre>
</dl>
<p> You can specify the following options to control what to extract. The <code>&#8211;filter</code> and <code>&#8211;format</code> arguments should be specified. By default this command will not overwrite the destination file or directory. </p>
<p> <code>&#8211;comment</code></p>
<dl>
<dt>
<dd> Add identifying comments to PEM bundle output files before each certificate.</dl>
<p> <code>&#8211;filter=&lt;what&gt;</code></p>
<dl>
<dt>
<dd> Specifies what certificates to extract. You can specify the following values: </p>
<p> <code>ca-anchors</code></p>
<dl>
<dt>
<dd> Certificate anchors (default)</dl>
<p> <code>trust-policy</code></p>
<dl>
<dt>
<dd> Anchors and blocklist</dl>
<p> <code>blocklist</code></p>
<dl>
<dt>
<dd> Distrusted certificates</dl>
<p> <code>certificates</code></p>
<dl>
<dt>
<dd> All certificates</dl>
<p> <code>pkcs11:object=xx</code></p>
<dl>
<dt>
<dd> A PKCS#11 URI</dl>
<p> If an output format is chosen that cannot support type what has been specified by the filter, a message will be printed. </p>
<p> None of the available formats support storage of blocklist entries that do not contain a full certificate. Thus any certificates distrusted by their issuer and serial number alone, are not included in the extracted blocklist.</dl>
<p> <code>&#8211;format=&lt;type&gt;</code></p>
<dl>
<dt>
<dd> The format of the destination file or directory. You can specify one of the following values: </p>
<p> <code>x509-file</code></p>
<dl>
<dt>
<dd> DER X.509 certificate file</dl>
<p> <code>x509-directory</code></p>
<dl>
<dt>
<dd> directory of X.509 certificates</dl>
<p> <code>pem-bundle</code></p>
<dl>
<dt>
<dd> File containing one or more certificate PEM blocks</dl>
<p> <code>pem-directory</code></p>
<dl>
<dt>
<dd> Directory of PEM files each containing one certificate</dl>
<p> <code>pem-directory-hash</code></p>
<dl>
<dt>
<dd> Directory of PEM files each containing one certificate, with hash symlinks</dl>
<p> <code>openssl-bundle</code></p>
<dl>
<dt>
<dd> OpenSSL specific PEM bundle of certificates</dl>
<p> <code>openssl-directory</code></p>
<dl>
<dt>
<dd> Directory of OpenSSL specific PEM files</dl>
<p> <code>java-cacerts</code></p>
<dl>
<dt>
<dd> Java keystore &#8216;cacerts&#8217; certificate bundle</dl>
</dl>
<p> <code>&#8211;overwrite</code></p>
<dl>
<dt>
<dd> Overwrite output file or directory.</dl>
<p> <code>&#8211;purpose=&lt;usage&gt;</code></p>
<dl>
<dt>
<dd> Limit to certificates usable for the given purpose You can specify one of the following values: </p>
<p> <code>server-auth</code></p>
<dl>
<dt>
<dd> For authenticating servers</dl>
<p> <code>client-auth</code></p>
<dl>
<dt>
<dd> For authenticating clients</dl>
<p> <code>email</code></p>
<dl>
<dt>
<dd> For email protection</dl>
<p> <code>code-signing</code></p>
<dl>
<dt>
<dd> For authenticated signed code</dl>
<p> <code>1.2.3.4.5&#8230;</code></p>
<dl>
<dt>
<dd> An arbitrary purpose OID</dl>
</dl>
<h2>EXTRACT COMPAT</h2>
<p> Extract compatibility trust certificate bundles. </p>
<dl>
<dt>
<dd>
<pre>
$ trust extract-compat
</pre>
</dl>
<p> OpenSSL, Java and some versions of GnuTLS cannot currently read trust information directly from the trust policy store. This command extracts trust information such as certificate anchors for use by these libraries. </p>
<p> What this command does, and where it extracts the files is distribution or site specific. Packagers or administrators are expected customize this command.</p>
<h2>DUMP</h2>
<p> Dump PKCS#11 items in the various tokens. </p>
<dl>
<dt>
<dd>
<pre>
$ trust dump
</pre>
</dl>
<p> Dump information about the various PKCS#11 items in the tokens. Each item is dumped with it&#8217;s PKCS#11 URI and information in the .p11-kit persistence format. </p>
<p> You can specify the following options to control what to dump. </p>
<p> <code>&#8211;filter=&lt;what&gt;</code></p>
<dl>
<dt>
<dd> Specifies what certificates to extract. You can specify the following values: </p>
<p> <code>all</code></p>
<dl>
<dt>
<dd> All objects. This is the default</dl>
<p> <code>pkcs11:object=xx</code></p>
<dl>
<dt>
<dd> A PKCS#11 URI to filter with</dl>
</dl>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://github.com/p11-glue/p11-kit/issues/">https://github.com/p11-glue/p11-kit/issues/</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-p11-kit/">p11-kit</a></code>(8) </p>
<p> An explanatory document about storing trust policy: m[blue]<code><a rel="nofollow" href="https://p11-glue.github.io/p11-glue/doc/storing-trust-policy/">https://p11-glue.github.io/p11-glue/doc/storing-trust-policy/</a></code>m[] </p>
<p> Further details available in the p11-kit online documentation at m[blue]<code><a rel="nofollow" href="https://p11-glue.github.io/p11-glue/p11-kit/manual/">https://p11-glue.github.io/p11-glue/p11-kit/manual/</a></code>m[]. </p>
<h2>Index</h2>
