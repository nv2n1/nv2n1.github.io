---
title: "pam_ftp(8)"
name: "pam_ftp"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_ftp/"
description: "pam_ftp – PAM module for anonymous access module"
---

<p>pam_ftp &#8211; PAM module for anonymous access module</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_<a href="ftp://ftp.so">ftp.so</a></code> [debug] [ignore] [users=<i>XXX,YYY,</i>&#8230;]</dl>
<h2>Description</h2>
<dd>pam_ftp is a PAM module which provides a pluggable anonymous ftp mode of access. </p>
<p> This module intercepts the user&#8217;s name and password. If the name is <i>ftp</i> or <i>anonymous</i>, the user&#8217;s password is broken up at the <i>@</i> delimiter into a <i>PAM_RUSER</i> and a <i>PAM_RHOST</i> part; these pam-items being set accordingly. The username (<i>PAM_USER</i>) is set to <i>ftp</i>. In this case the module succeeds. Alternatively, the module sets the <i>PAM_AUTHTOK</i> item with the entered password and fails. </p>
<p> This module is not safe and easily spoofable.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>ignore</code></p>
<dl>
<dd>Pay no attention to the email address of the user (if supplied).</dl>
<p> <code>ftp=</code><i>XXX,YYY,&#8230;</i></p>
<dl>
<dd>Instead of <i>ftp</i> or <i>anonymous</i>, provide anonymous login to the comma separated list of users: <i>XXX,YYY,&#8230;</i>. Should the applicant enter one of these usernames the returned username is set to the first in the list: <i>XXX</i>.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>auth</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The authentication was successful.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known.</dl>
<h2>Examples</h2>
<p>Add the following line to /etc/pam.d/ftpd to handle ftp style anonymous login:</p>
<dl>
<dd>
<pre>#
# ftpd; add ftp-specifics. These lines enable anonymous ftp over
# standard UN*X access (the listfile entry blocks access to
# users listed in /etc/ftpusers)
#
auth sufficient pam_<a href="ftp://ftp.so">ftp.so</a>
auth required pam_unix.so use_first_pass
auth required pam_listfile.so \
 onerr=succeed item=user sense=deny file=/etc/ftpusers</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_ftp was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;.</p>
