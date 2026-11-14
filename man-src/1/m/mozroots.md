---
title: "mozroots(1)"
name: "mozroots"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mozroots/"
description: "mozroots – Download and import trusted root certificates from Mozilla’s LXR into Mono’s certificate store"
---

<h2>NAME</h2>
<p> mozroots &#8211; Download and import trusted root certificates from Mozilla&#8217;s LXR into Mono&#8217;s certificate store</p>
<h2>SYNOPSIS</h2>
<p> <code>mozroots [&#8211;import [&#8211;machine] [&#8211;sync | &#8211;ask | &#8211;ask-add | &#8211;ask-remove]]</code></p>
<h2>DESCRIPTION</h2>
<p> This program downloads the trusted root certificates from the Mozilla LXR web site into the Mono certificate store. </p>
<p> Mono by default does not ship with any default certificates and allows the user to pick its trusted certificates. The mozroots command will bring the Mozilla certificates into your local machine.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;import</i></p>
<dd> Import the certificates into the trust store.</p>
<dt><i>&#8211;sync</i></p>
<dd> Synchronize (add/remove) the trust store with the certificates. Synchronize is useful for new Mono installations (no roots) and for automated updates (no user confirmation for addition or removal).</p>
<dt><i>&#8211;ask</i></p>
<dd> Always confirm before adding or removing trusted certificates. <code>Note:</code> The initial import will likely add about 100 new trusted root certificates into your store. You&#8217;ll have to answer <code>yes</code> to every one of them if this option is specified.</p>
<dt><i>&#8211;ask-add</i></p>
<dd> Always confirm before adding a new trusted certificate. <code>Note:</code> The initial import will likely add about 100 new trusted root certificates into your store. You&#8217;ll have to answer <code>yes</code> to every one of them if this option is specified.</p>
<dt><i>&#8211;ask-remove</i></p>
<dd> Always confirm before removing an existing trusted certificate.</dl>
<h2>ADVANCED OPTIONS</h2>
<dl>
<dt><i>&#8211;url url</i></p>
<dd> Specify an alternative URL for downloading the trusted certificates (LXR source format). This should only be useful for testing or if the Mozilla&#8217;s LXR web site address is changed. It can also be used to cache a local copy of the LXR file into your local intranet.</p>
<dt><i>&#8211;file name</i></p>
<dd> Do not download from LXR but use the specified file. This is useful if many computers have to download the same file from the Internet. This way you can keep a local copy on a file server (and minimize network traffic).</p>
<dt><i>&#8211;pkcs7 name</i></p>
<dd> Export the certificates into a PKCS#7 file. This is useful for debugging purpose or for re-importing the same list into other software.</p>
<dt><i>&#8211;machine</i></p>
<dd> Import the certificate in the machine trust store. The default is to import all trusted root certificates into the current user store.</p>
<dt><i>&#8211;quiet</i></p>
<dd> Limit console output to errors and confirmations messages. This is useful when scripting.</dl>
<h2>EXAMPLES</h2>
<p> After the initial Mono installation you&#8217;ll have no trusted roots certificates pre-installed. Neither will you have some root test certificates installed (your own or the ones provided by using <code>setreg</code> ). In this case the simplest thing to do, if you want to trust all those certificates, is to import and synchronize. </p>
<pre>
        $ mozroots --import --sync
        Mozilla Roots Importer - version 1.1.9.0
        Download and import trusted root certificates from Mozilla's LXR.
        Copyright 2002, 2003 Motus Technologies. Copyright 2004-2005 Novell. BSD licensed.
 
        Downloading from '<a rel="nofollow" href="http://lxr.mozilla.org/seamonkey/source/security/nss/lib/ckfw/builtins/certdata.txt'...">http://lxr.mozilla.org/seamonkey/source/security/nss/lib/ckfw/builtins/certdata.txt'...</a>
        Importing certificates into user store...
        93 new root certificates were added to your trust store.
        Import process completed.
</pre>
<p> If you created some test certificates (e.g. for using SSL/TLS with XSP) and/or if your enterprise requires some additional root certificates (e.g. intranet) then you may want to skip the removal part of the process. You can do this by asking for a removal confirmation (&#8211;ask-remove option) and answer no when prompted. </p>
<pre><code>
$ mozroots-- import-- ask - remove Mozilla Roots Importer - version 1.1.9.0 Download and import trusted root certificates from Mozilla's LXR. Copyright 2002, 2003 Motus Technologies.Copyright 2004 - 2005 Novell.BSD licensed.

                                                                                                                                                                                                       Downloading from 'http://lxr.mozilla.org/seamonkey/source/security/nss/lib/ckfw/builtins/certdata.txt' ... Importing certificates into user store... 93 new root certificates were added to your trust store.2 previously trusted certificates were not part of the update.Issuer : CN = Mono Test Root Agency
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Serial number : 69 -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                B0 - E1 - 4F - 88 - 6E-C7 - 85 - 48 - 0E-74 - 91 - 38 - 76 - F4 - 28 Valid from 9 / 1 / 2003 11 : 55 : 48 AM to 12 / 31 / 2039 1 : 59 : 59 PM Thumbprint SHA - 1 : EF - 26 - C2 - 28 - 11 - 3F - 79 - ED - 9D - EC - 3F - 3B - D5 - 7A - 26 - F2 - 7C - 9F - FA - 63 Thumbprint MD5 : AE - 19 - 3E-64 - 36 - 21 - F2 - A4 - 8B - 69 - 38 - CA - 64 - 4B - 2E-62 Are you sure you want to remove this certificate
                                                                                                                                                              ? no
                                                                                                                                                                    You can still use the synchronize option(--sync) if you have activated
                                                                                                                                                                        the default test roots certificate on your system.They will be removed
                                                                                                                                                                            at the end of the synchronization process but you can quickly add them
                                                                                                                                                                                back with the
                                                                                                                                                                                    setreg
                                                                                                                                                                                        tool.$ setreg 1 true
</code></pre>
<p> Another option to ease updates is to synchronize your machine trust store (using the &#8211;machine option) and keep your customized (test) certificates in your personal store (or vice versa). Note that every user on this computer will be trusting all the newly imported certificates. </p>
<pre>
        $ mozroots --import --machine --sync
        Mozilla Roots Importer - version 1.1.9.0
        Download and import trusted root certificates from Mozilla's LXR.
        Copyright 2002, 2003 Motus Technologies. Copyright 2004-2005 Novell. BSD licensed.
 
        Downloading from '<a rel="nofollow" href="http://lxr.mozilla.org/seamonkey/source/security/nss/lib/ckfw/builtins/certdata.txt'...">http://lxr.mozilla.org/seamonkey/source/security/nss/lib/ckfw/builtins/certdata.txt'...</a>
        Importing certificates into user store...
        94 new root certificates were added to your trust store.
        Import process completed.
</pre>
<p> Once the initial import is complete the number of changes (additions or removals) is generally very low. In this case it makes sense to know about any changes (i.e. ask for confirmation). No confirmation will be required if no changes are made to your trust store. </p>
<pre>
        $ mozroots --import --ask
        Mozilla Roots Importer - version 1.1.9.0
        Download and import trusted root certificates from Mozilla's LXR.
        Copyright 2002, 2003 Motus Technologies. Copyright 2004-2005 Novell. BSD licensed.
 
        Downloading from '<a rel="nofollow" href="http://lxr.mozilla.org/seamonkey/source/security/nss/lib/ckfw/builtins/certdata.txt'...">http://lxr.mozilla.org/seamonkey/source/security/nss/lib/ckfw/builtins/certdata.txt'...</a>
        Importing certificates into user store...
        Import process completed.
</pre>
<h2>FILES</h2>
<p> ~/.config/.mono/certs, /usr/share/.mono/certs </p>
<p> Contains Mono certificate stores for users / machine. See the <a href="/docs/linux/man/1-certmgr/">certmgr</a>(1) manual page for more information on managing certificate stores.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 Novell.</p>
<h2>MAILING LISTS</h2>
<p> Mailing lists are listed at the <a rel="nofollow" href="http://www.mono-project.com/community/help/mailing-lists/">http://www.mono-project.com/community/help/mailing-lists/</a></p>
<h2>WEB SITE</h2>
<p> <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a>(1),</code><a href="/docs/linux/man/1-certmgr/">certmgr</a>(1).<code><a href="/docs/linux/man/1-setreg/">setreg</a>(1)</code> </p>
<h2>Index</h2>
