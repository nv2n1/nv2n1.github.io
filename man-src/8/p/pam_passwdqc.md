---
title: "pam_passwdqc(8)"
name: "pam_passwdqc"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_passwdqc/"
description: "pam_passwdqc – Password quality-control PAM module"
---

<p><code>pam_passwdqc</code> &#8211; Password quality-control PAM module</p>
<h2>Synopsis</h2>
<p>[<i>service-name</i> ] <i>module-type</i> <i>control-flag</i> pam_passwdqc [<i>options</i> ]</p>
<h2>Description</h2>
<p>The module is a simple password strength checking module for PAM. In addition to checking regular passwords, it offers support for passphrases and can provide randomly generated ones. </p>
<p> The module provides functionality for only one PAM management group: password changing. In terms of the <i>module-type</i> parameter, this is the &#8220;<code>password</code> &#8221; feature. </p>
<p> The Fn pam_chauthtok service function may ask the user for a new password, and verify that it meets certain minimum standards. If the chosen password is unsatisfactory, the service function returns <code>PAM_AUTHTOK_ERR</code> </p>
<p> The set of options that may be passed to the module is exactly the same as the set of options that may be specified in the /etc/passwdqc.conf file. These options are described in passwdqc.conf5.</p>
<h2>See Also</h2>
<p>pam.conf5, passwdqc.conf5, <a href="/docs/linux/man/8-pam/">pam</a>(8). </p>
<p> <a rel="nofollow" href="http://www.openwall.com/passwdqc/">http://www.openwall.com/passwdqc/</a></p>
<h2>Authors</h2>
<p>The module was written for Openwall GNU/*/Linux by An Solar Designer Aq solar at openwall.com . This manual page was written for the Fx Project by ThinkSec AS and NAI Labs, the Security Research Division of Network Associates, Inc. under DARPA/SPAWAR contract N66001-01-C-8035 (&#8220;CBOSS&#8221; ) as part of the DARPA CHATS research program. It has since been revised, most importantly to refer to passwdqc.conf5 instead of describing the options right on this page.</p>
