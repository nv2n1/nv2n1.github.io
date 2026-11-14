---
title: "cert8(5)"
name: "cert8"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cert8/"
---

cert8.db - Legacy NSS certificate database

<h2>Description</h2>

<i>cert8.db</i> is an NSS certificate database. 

 This certificate database is in the legacy database format. Consider migrating to cert9.db and key4.db which are the new sqlite-based shared database format with support for concurrent access.

<h2>Files</h2>

/etc/pki/nssdb/cert8.db

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-cert9-db/">cert9.db</a>(5), <a HREF="/docs/linux/man/5-key4-db/">key4.db</a>(5), <a HREF="/docs/linux/man/5-pkcs11-txt/">pkcs11.txt</a>(5),

<h2>Authors</h2>

The nss libraries were written and maintained by developers with Netscape, Red Hat, Sun, Oracle, Mozilla, and Google. 

 Authors: Elio Maldonado &lt;emaldona [at] redhat.com&gt;.

<h2>License</h2>

Licensed under the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a rel="nofollow" HREF="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a>
