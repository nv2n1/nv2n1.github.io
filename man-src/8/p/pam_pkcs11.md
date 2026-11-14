---
title: "pam_pkcs11(8)"
name: "pam_pkcs11"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_pkcs11/"
description: "pam_pkcs11 – PAM Authentication Module for PKCS#11 token libraries"
---

<p>pam_pkcs11 &#8211; PAM Authentication Module for PKCS#11 token libraries</p>
<h2>Synopsis</h2>
<p><code>pam_pkcs11.so</code> [<code>debug</code>] [<code>configfile=</code><i>&lt;configfile&gt;</i>]</p>
<h2>Description</h2>
<p>This Linux-PAM login module allows a X.509 certificate based user login. The certificate and its dedicated private key are thereby accessed by means of an appropriate PKCS #11 module. For the verification of the users&#8217; certificates, locally stored CA certificates as well as either online or locally accessible CRLs are used.</p>
<h2>Configuration</h2>
<p>The program that needs a PAM service should be configured in <i>/etc/pam.conf</i> or <i>/etc/pam.d/&lt;servicename&gt;</i>. </p>
<p> <code>pam_pkcs11</code> can be used in the &lt;auth&gt; PAM chain. </p>
<p> For details on how to configure PAM services, see the PAM documentation for your system. This manual does not cover PAM configuration details. The existing PAM service definitions for other applications on your system is also a good source for examples on how to configure a PAM service.</p>
<h2>Files</h2>
<p><i>/etc/pam_pkcs11/pam_pkcs11.conf</i><br />
 <i>/usr/lib/pam_pkcs11/*_mapper.so</i></p>
<h2>Author</h2>
<p>Original PAM-pkcs11 was written by Mario Strasser &lt;mast [at] gmx.net&gt;. Newer versions are from Juan Antonio Martinez &lt;jonsito [at] teleline.es&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs ideas, comments, bug-fixes and so to: <i>Juan Antonio Martinez &lt;jonsito [at] teleline.es&gt;</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam/">pam</a></code>(8), PAM Systems Administrator Guide (/usr/share/doc/pam_pkcs11-0.6.2/pam_pkcs11.htm l), <i>README.mappers</i> file, PAM-PKCS#11 User Manual. </p>
