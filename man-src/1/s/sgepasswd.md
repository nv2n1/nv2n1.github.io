---
title: "sgepasswd(1)"
name: "sgepasswd"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgepasswd/"
description: "sgepasswd – Modify the xxQS_NAMExx password file of xxQS_NAMExx"
---

<h2 class="name">NAME</h2>
<p> sgepasswd &#8211; Modify the xxQS_NAMExx password file of xxQS_NAMExx </p>
<h2>SYNTAX</h2>
<p> <code>sgepasswd</code> [[ <code>-D domain</code> ] <code>-d user</code> ] </p>
<p> <code>sgepasswd</code> [ <code>-D domain</code> ] [ <code>user</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>sgepasswd</i> modifies the xxQS_NAMExx password file </p>
<p> This file contains a list of usernames and their Microsoft Windows password in encrypted form. and on hosts running Microsoft Windows as operating systems use this information to start jobs for a certain user. </p>
<p> Each user can use the <i>sgepasswd</i> application to add a new entry for their own user account. (In fact, normal users can create an entry for any account, so the entry should be made initially, when the account is created.) It is also possible to change the stored password with <i>sgepasswd</i> if the user knows the old one. </p>
<p> The root user additionally has permission to change the password entries for other user accounts. Root can also delete existing entries. </p>
<p> The <i>sgepasswd</i> binary is only available on non-Windows hosts. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-D domain</code></p>
<dd> By default <i>sgepasswd</i> will add/modify the current Unix username without a domain specification. This switch can be used to add a domain specification in front of the current user name. Consult your Microsoft Windows documentation to get more information about domain users.</p>
<dt><code>-d user</code></p>
<dd> Only root can use this parameter to delete entries from the file.</p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</dl>
<h2>NOTE</h2>
<p> Prevent relevant jobs running before a password is changed both with <i>sgepasswd</i> and in the Windows domain. Otherwise, if multiple jobs try to run on a Windows host as the user concerned, and are unable to access the right password, Windows&#8217; intrusion detection system may disable the account. <i>sgepasswd</i> and in the Windows domain.</p>
<h2>SECURITY</h2>
<p> This is a non-trivial program which needs to be setuid root, operating with various user-supplied input. It probably shouldn&#8217;t be installed setuid if it is not needed to support Windows hosts. </p>
<p> See above concerning making initial entries.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>SGE_CERTFILE</code></p>
<dd> Specifies the location of the public key file. By default <i>sgepasswd</i> will use $SGE_ROOT/$SGE_CELL/common/sgeCA/certs/cert.pem.</p>
<dt><code>SGE_KEYFILE</code></p>
<dd> If set, specifies the location of the private key file. Default is /var/lib/sgeCA/port$SGE_QMASTER_PORT/$SGE_CELL/private/key.pem.</p>
<dt><code>SGE_RANDFILE</code></p>
<dd> If set, specifies the location of the seed used to create encrypted versions of user passwords. Default is /var/lib/sgeCA/port${SGE_QMASTER_PORT}/${SGE_CELL}/private/rand.seed.</dl>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
