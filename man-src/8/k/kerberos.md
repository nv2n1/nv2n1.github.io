---
title: "kerberos(8)"
name: "kerberos"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kerberos/"
description: "kerberos – introduction to the Kerberos system"
---

<p><code>kerberos</code> &#8211; introduction to the Kerberos system</p>
<h2>Description</h2>
<p>Kerberos is a network authentication system. Its purpose is to securely authenticate users and services in an insecure network environment. </p>
<p> This is done with a Kerberos server acting as a trusted third party, keeping a database with secret keys for all users and services (collectively called <i>principals )</i> </p>
<p> Each principal belongs to exactly one <i>realm</i> which is the administrative domain in Kerberos. A realm usually corresponds to an organisation, and the realm should normally be derived from that organisation&#8217;s domain name. A realm is served by one or more Kerberos servers. </p>
<p> The authentication process involves exchange of `tickets&#8217; and `authenticators&#8217; which together prove the principal&#8217;s identity. </p>
<p> When you login to the Kerberos system, either through the normal system login or with the <a href="/docs/linux/man/1-kinit/">kinit</a>(1) program, you acquire a <i>ticket granting ticket</i> which allows you to get new tickets for other services, such as <code>telnet</code> or <code>ftp</code> without giving your password. </p>
<p> For more information on how Kerberos works, and other general Kerberos questions see the Kerberos FAQ at Lk <a rel="nofollow" href="http://www.cmf.nrl.navy.mil/krb/kerberos-faq.html">http://www.cmf.nrl.navy.mil/krb/kerberos-faq.html</a> . </p>
<p> For setup instructions see the Heimdal Texinfo manual.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ftp/">ftp</a>(1), <a href="/docs/linux/man/1-kdestroy/">kdestroy</a>(1), <a href="/docs/linux/man/1-kinit/">kinit</a>(1), <a href="/docs/linux/man/1-klist/">klist</a>(1), <a href="/docs/linux/man/1-kpasswd/">kpasswd</a>(1), <a href="/docs/linux/man/1-telnet/">telnet</a>(1), <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5.conf5, <a href="/docs/linux/man/8-kadmin/">kadmin</a>(8), <a href="/docs/linux/man/8-kdc/">kdc</a>(8), <a href="/docs/linux/man/8-ktutil/">ktutil</a>(8)</p>
<h2>History</h2>
<p>The Kerberos authentication system was developed in the late 1980&#8217;s as part of the Athena Project at the Massachusetts Institute of Technology. Versions one through three never reached outside MIT, but version 4 was (and still is) quite popular, especially in the academic community, but is also used in commercial products like the AFS filesystem. </p>
<p> The problems with version 4 are that it has many limitations, the code was not too well written (since it had been developed over a long time), and it has a number of known security problems. To resolve many of these issues work on version five started, and resulted in IETF RFC 1510 in 1993. IETF RFC 1510 was obsoleted in 2005 with IETF RFC 4120, also known as Kerberos clarifications. With the arrival of IETF RFC 4120, the work on adding extensibility and internationalization have started (Kerberos extensions), and a new RFC will hopefully appear soon. </p>
<p> This manual page is part of the <code>Heimdal</code> Kerberos 5 distribution, which has been in development at the Royal Institute of Technology in Stockholm, Sweden, since about 1997.</p>
