---
title: "certmgr(1)"
name: "certmgr"
section: "1"
letter: "c"
url: "/docs/linux/man/1-certmgr/"
description: "certmgr – Mono Certificate Manager (CLI version)"
---

<h2>NAME</h2>
<p> certmgr &#8211; Mono Certificate Manager (CLI version)</p>
<h2>SYNOPSIS</h2>
<p> <code>certmgr [action] [object type] [options] store [filename]</code> or <code>certmgr -ssl [options] url</code></p>
<h2>DESCRIPTION</h2>
<p> This tool allow to list, add, remove or extract certificates, certificate revocation lists (CRL) or certificate trust lists (CTL) to/from a certificate store. Certificate stores are used to build and validate certificate chains for Authenticode(r) code signing validation and SSL server certificates.</p>
<h2>STORES</h2>
<p> The <i>store</i> represents the certificate store to use. It can be one of the following:</p>
<dl>
<dt><i>My</i></p>
<dd> This is the personal certificate store.</p>
<dt><i>AddressBook</i></p>
<dd> This is the store for other people.</p>
<dt><i>CA</i></p>
<dd> This is a store for intermediate certificate authorities.</p>
<dt><i>Trust</i></p>
<dd> This is for trusted roots.</p>
<dt><i>Disallowed</i></p>
<dd> This is for untrusted roots</dl>
<h2>ACTIONS</h2>
<dl>
<dt><i>-list</i></p>
<dd> List the certificates, CTL or CTL in the specified store.</p>
<dt><i>-add</i></p>
<dd> Add a certificate, CRL or CTL to specified store. If filename it&#8217;s a pkcs12 or pfx file, and it contains a private key, it will be imported to local key pair container.</p>
<dt><i>-del</i></p>
<dd> Remove a certificate, CRL or CTL from specified store. You must specify the object to be removed with it&#8217;s hash value (and not a filename). This hash value is shown when doing a <code>-list</code> on the store.</p>
<dt><i>-put</i></p>
<dd> Copy a certificate, CRL or CTL from a store to a file.</p>
<dt><i>-ssl</i></p>
<dd> Download and add the certificates from a SSL session. You&#8217;ll be asked to confirm the addition of every certificate received from the server. Note that SSL/TLS protocols do not requires a server to send the root certificate. This action assume an certificate (-c) object type and will import the certificates in appropriate stores (i.e. server certificate in the OtherPeople store, the root certificate in the Trust store, any other intermediate certificates in the IntermediateCA store).</p>
<dt><i>-importKey</i></p>
<dd> Allows importing a private key from a pkcs12 file into a local key pair store. (Usefull when you already have the key&#8217;s corresponding certificate installed at the specific store.) </p>
</dl>
<h2>OBJECT TYPES</h2>
<dl>
<dt><i>-c, -cert, -certificate</i></p>
<dd> Add, Delete or Put certificates. That is the specified file must/will contains X.509 certificates in DER binary encoding.</p>
<dt><i>-crl</i></p>
<dd> Add, Delete or Put certificate revocation lists (CRL). That is the specified file must/will contains X.509 CRL in DER binary encoding.</p>
<dt><i>-ctl</i></p>
<dd> Add, Delete or Put certificate trust lists (CRL). UNSUPPORTED. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>-m</i></p>
<dd> Use the machine&#8217;s certificate stores (instead of the default user&#8217;s stores).</p>
<dt><i>-v</i></p>
<dd> More details displayed on the console.</p>
<dt><i>-p password</i></p>
<dd> Use the specify password when accessing a pkcs12 file.</p>
<dt><i>-help, -h, -?, /?</i></p>
<dd> Display help about this tool. </p>
</dl>
<h2>FILES</h2>
<p> <code>WARNING: This details the current behavior of Mono and could change between releases.</code> The only safe way to interact with certificate stores is to use the certmgr tool. The current releases of Mono keeps all the user certificate stores in separates directories under <i>~/.config/.mono/certs/</i></p>
<dl>
<dt>For example the trusted root certificates for a user would be kept under</p>
<dd> <i>~/.config/.mono/certs/Trust/</i></p>
<dt>Certificates files are kept in DER (binary) format (extension .cer).</p>
<dd>
<dt>The filenames either starts with</p>
<dd> <i>tbp </i> (thumbprint) or <i>ski</i> (subject key identifier).</p>
<dt>The rest of the filename is the base64-encoded value (tbp or ski).</p>
<dd>
<dt>Private key data is stored under</p>
<dd> <i>~/.config/.mono/keypairs/</i> </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>mono certmgr.exe -list -c -m Trust</code></p>
<dd> List all certificates in the machine Trust store. This will display the hash value for each certificate. This value can be used to identify uniquely a certificate for some operations (e.g. delete). E.g. <code>Unique Hash: FFA3AC0084DA1673B5A031EBB2156B3E8FBBF6D8</code></p>
<dt><code>mono certmgr.exe -del -c -m Trust FFA3AC0084DA1673B5A031EBB2156B3E8FBBF6D8</code></p>
<dd> Remove the certificate, represented by the hash value, from the machine Trust store. Note that the machine store is normally restricted. The following error message will appear if the current user doesn&#8217;t have the minimum access rights to remove the certificate: <code>Access to the machine &#8216;Trust&#8217; certificate store has been denied.</code></p>
<dt><code>certmgr -ssl <a rel="nofollow" href="https://www.verisign.com">https://www.verisign.com</a></code></p>
<dd> Import certificates from <a rel="nofollow" href="http://www.verisign.com">www.verisign.com</a> used for HTTP over SSL. See KNOWN ISSUES (MD2) if you&#8217;re downloading from <a rel="nofollow" href="http://www.verisign.com">www.verisign.com</a>.</p>
<dt><code>certmgr -ssl <a href="ldaps://www.nldap.com:636">ldaps://www.nldap.com:636</a></code></p>
<dd> Import the certificates from <a rel="nofollow" href="http://www.nldap.com">www.nldap.com</a> used for secure LDAP. This works even if we don&#8217;t know how to speak LDAP because we stop the communication shortly after the SSL handshake (which gives us the certificate). </p>
</dl>
<h2>KNOWN ISSUES</h2>
<dl>
<dt><code>MD2</code></p>
<dd> Some Certificate Authorities (CA) old root certificates use the MD2 hash algorithm. MD2 is old enough not to be part of the standard .NET framework. This makes it impossible to validate a digital signature made with MD2. For this reason MD2 is included in the Mono.Security.dll assembly. However the machine.config file must be updated so the OID for MD2 is known at runtime. </p>
<p> To correct this insert the following XML snippet inside the &lt;configuration&gt; element of your machine.config file.<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;mscorlib&gt;<br />
&nbsp;<wbr>&lt;cryptographySettings&gt;<br />
&lt;cryptoNameMapping&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;cryptoClasses&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;cryptoClass monoMD2=&quot;Mono.Security.Cryptography.MD2Managed, Mono.Security, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=0738eb9f132ed756&quot;&nbsp;<wbr>/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/cryptoClasses&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;nameEntry name=&quot;MD2&quot;&nbsp;<wbr>class=&quot;monoMD2&quot;&nbsp;<wbr>/&gt;<br />
&lt;/cryptoNameMapping&gt;<br />
&lt;oidMap&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;oidEntry OID=&quot;1.2.840.113549.2.2&quot;&nbsp;<wbr>name=&quot;MD2&quot;&nbsp;<wbr>/&gt;<br />
&lt;/oidMap&gt;<br />
&nbsp;<wbr>&lt;/cryptographySettings&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/mscorlib&gt; </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by Sebastien Pouliot </p>
<p> Minor additions by Pablo Ruiz García</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2004-2005 Novell.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-list">http://lists.ximian.com/mailman/listinfo/mono-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-makecert/">makecert</a>(1),</code><a href="/docs/linux/man/1-setreg/">setreg</a>(1) </p>
<h2>Index</h2>
