---
title: "secmod-db(5)"
name: "secmod-db"
section: "5"
letter: "s"
url: "/docs/linux/man/5-secmod-db/"
---

secmod.db - Legacy NSS security modules database

<h2>Description</h2>

<i>secmod.db</i> is an NSS security modules database. 

 The security modules database is used to keep track of the NSS security modules. The NSS security modules export their services via the PKCS #11 API which NSS uses as its Services Provider Interface. 

 The command line utility <i>modutil</i> is used for managing PKCS #11 module information both within secmod.db files and within hardware tokens. 

 For new applications the recommended way of tracking security modules is via the pkcs11.txt configuration file used in conjunction the new sqlite-based shared database format for certificate and key databases.

<h2>Files</h2>

/etc/pki/nssdb/secmod.db

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-modutil/">modutil</a>(1), <a HREF="/docs/linux/man/5-cert8-db/">cert8.db</a>(5), <a HREF="/docs/linux/man/5-cert9-db/">cert9.db</a>(5), <a HREF="/docs/linux/man/5-key3-db/">key3.db</a>(5), <a HREF="/docs/linux/man/5-key4-db/">key4.db</a>(5), <a HREF="/docs/linux/man/5-pkcs11-txt/">pkcs11.txt</a>(5)

<h2>Authors</h2>

The nss libraries were written and maintained by developers with Netscape, Red Hat, Sun, Oracle, Mozilla, and Google. 

 Authors: Elio Maldonado &lt;emaldona [at] redhat.com&gt;.

<h2>License</h2>

Licensed under the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a rel="nofollow" HREF="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a>
