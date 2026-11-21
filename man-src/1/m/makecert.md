---
title: "makecert(1)"
name: "makecert"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makecert/"
description: "MakeCert – Create X.509 certificates for test purposes"
---

<h2>NAME</h2>
<p> MakeCert &#8211; Create X.509 certificates for test purposes</p>
<h2>SYNOPSIS</h2>
<p> <code>makecert [options] certificate</code></p>
<h2>DESCRIPTION</h2>
<p> Create an X.509 certificate using the provided informations. This is useful for testing Authenticode signatures, SSL and S/MIME technologies.</p>
<h2>PARAMETERS</h2>
<dl>
<dt><i>-# num</i></dt>
<dd> Specify the certificate serial number.</dd>
<dt><i>-n dn</i></dt>
<dd> Specify the subject Distinguished Name (DN).</dd>
<dt><i>-in dn</i></dt>
<dd> Specify the issuer Distinguished Name (DN).</dd>
<dt><i>-r</i></dt>
<dd> Create a self-signed, also called root, certificate.</dd>
<dt><i>-iv pvkfile</i></dt>
<dd> Specify the private key file (.PVK) for the issuer. The private key in the specified file will be used to sign the new certificate.</dd>
<dt><i>-ic certfile</i></dt>
<dd> Extract the issuer&#8217;s name from the specified certificate file &#8211; i.e. the subject name of the specified certificate becomes the issuer name of the new certificate.</dd>
<dt><i>-in name</i></dt>
<dd> Use the issuer&#8217;s name from the specified parameter.</dd>
<dt><i>-ik container</i></dt>
<dd> Specify the key container name to be used for the issuer.</dd>
<dt><i>-iky [signature | exchange | #]</i></dt>
<dd> Specify the key number to be used in the provider (when used with -ik).</dd>
<dt><i>-ip provider</i></dt>
<dd> Specify the cryptographic provider to be used for the issuer.</dd>
<dt><i>-ir [localmachine | currentuser]</i></dt>
<dd> Specify the provider will search the user or the machine keys containers for the issuer.</dd>
<dt><i>-iy number</i></dt>
<dd> Specify the provider type to be used for the issuer.</dd>
<dt><i>-sv pkvfile</i></dt>
<dd> Specify the private key file (.PVK) for the subject. The public part of the key will be inserted into the created certificate. If non-existant the specified file will be created with a new key pair (default to 1024 bits RSA key pair).</dd>
<dt><i>-sk container</i></dt>
<dd> Specify the key container name to be used for the subject.</dd>
<dt><i>-sky [signature | exchange | #]</i></dt>
<dd> Specify the key number to be used in the provider (when used with -sk).</dd>
<dt><i>-sp provider</i></dt>
<dd> Specify the cryptographic provider to be used for the subject.</dd>
<dt><i>-sr [localmachine | currentuser]</i></dt>
<dd> Specify the provider will search the user or the machine keys containers for the subject.</dd>
<dt><i>-sy number</i></dt>
<dd> Specify the provider type to be used for the issuer.</dd>
<dt><i>-a hash</i></dt>
<dd> Select hash algorithm. Only MD5 and SHA1 algorithms are supported.</dd>
<dt><i>-b date</i></dt>
<dd> The date since when the certificate is valid (notBefore).</dd>
<dt><i>-e date</i></dt>
<dd> The date until when the certificate is valid (notAfter).</dd>
<dt><i>-m number</i></dt>
<dd> Specify the certificate validity period in months. This is added to the notBefore validity date which can be set with -b or will default to the current date/time.</dd>
<dt><i>-cy [authority|end]</i></dt>
<dd> Basic constraints. Select Authority or End-Entity certificate. Only Authority certificates can be used to sign other certificates (-ic). End-Entity can be used by clients (e.g. Authenticode, S/MIME) or servers (e.g. SSL).</dd>
<dt><i>-h number</i></dt>
<dd> Add a path length restriction to the certificate chain. This is only applicable for certificates that have BasicConstraint set to Authority (-cy authority). This is used to limit the chain of certificates than can be issued under this authority.</dd>
<dt><i>-alt filename</i></dt>
<dd> Add a subjectAltName extension to the certificate. Each line from &#8216;filename&#8217; will be added as a DNS entry of the extension. This option is useful if you want to create a single SSL certificate to work on several hosts that do not share a common domain name (i.e. CN=*.domain.com would not work).</dd>
<dt><i>-eku oid[,oid]</i></dt>
<dd> Add some extended key usage OID to the certificate.</dd>
<dt><i>-p12 pkcs12file password</i></dt>
<dd> Create a new PKCS#12 file containing both the certificates (the subject and possibly the issuer&#8217;s) and the private key. The PKCS#12 file is protected with the specified password. This option is <code>mono exclusive.</code></dd>
<dt><i>-?</i></dt>
<dd> Help (display this help message)</dd>
<dt><i>-!</i></dt>
<dd> Extended help (for advanced options)</dd></dl>
<h2>EXAMPLES</h2>
<p> To create a SSL test (i.e. non trusted) certificate is easy once your know your host&#8217;s name. The following command will create a test certificate for an SSL server: </p>
<pre>
        $ hostname 
        pollux
        $ makecert -r -eku 1.3.6.1.5.5.7.3.1 -n &quot;CN=pollux&quot; -sv pollux.pvk pollux.cer
        Success
</pre>
<p> In particular in the above example, the parameters used to build this test certificate were:</p>
<dl>
<dt><i>-r</i></dt>
<dd> Create a self-signed certificate (i.e. without an hierarchy).</dd>
<dt><i>-eku 1.3.6.1.5.5.7.3.1</i></dt>
<dd> Optional (as sadly most client don&#8217;t require it). This indicates that your certificate is intended for server-side authentication.</dd>
<dt><i>-n Common Name (CN) = Host name. This is verified the SSL client and must</i></dt>
<dd> match the connected host (or else you&#8217;ll get a warning or error or *gasp* nothing).</dd>
<dt><i>-sv private.key</i></dt>
<dd> The private key file. The key (1024 bits RSA key pair) will be automatically generated if the specified file isn&#8217;t present.</dd>
<dt><i>pollux.cer</i></dt>
<dd> The SSL certificate to be created for your host.</dd></dl>
<h2>KNOWN RESTRICTIONS</h2>
<p> Compared to the Windows version some options aren&#8217;t supported (-$, -d, -l, -nscp, -is, -sc, -ss). Also PVK files with passwords aren&#8217;t supported.</p>
<h2>AUTHOR</h2>
<p> Written by Sebastien Pouliot</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003 Motus Technologies. Copyright (C) 2004-2005 Novell. Released under BSD license.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-signcode/">signcode</a>(1)</code> </p>
