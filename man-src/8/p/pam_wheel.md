---
title: "pam_wheel(8)"
name: "pam_wheel"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_wheel/"
description: "pam_wheel – Only permit root access to members of group wheel"
---

<p>pam_wheel &#8211; Only permit root access to members of group wheel</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_wheel.so</code> [debug] [deny] [group=<i>name</i>] [root_only] [trust]</dl>
<h2>Description</h2>
<dd>The pam_wheel PAM module is used to enforce the so-called <i>wheel</i> group. By default it permits access to the target user if the applicant user is a member of the <i>wheel</i> group. If no group with this name exist, the module is using the group with the group-ID <code>0</code>.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>deny</code></p>
<dl>
<dd>Reverse the sense of the auth operation: if the user is trying to get UID 0 access and is a member of the wheel group (or the group of the <code>group</code> option), deny access. Conversely, if the user is not in the group, return PAM_IGNORE (unless <code>trust</code> was also specified, in which case we return PAM_SUCCESS).</dl>
<p> <code>group=</code><i>name</i></p>
<dl>
<dd>Instead of checking the wheel or GID 0 groups, use the <i>name</i> group to perform the authentication.</dl>
<p> <code>root_only</code></p>
<dl>
<dd>The check for wheel membership is done only when the target user UID is 0.</dl>
<p> <code>trust</code></p>
<dl>
<dd>The pam_wheel module will return PAM_SUCCESS instead of PAM_IGNORE if the user is a member of the wheel group (thus with a little play stacking the modules the wheel members may be able to su to root without being prompted for a passwd).</dl>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>account</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>Authentication failure.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>The return value should be ignored by PAM dispatch.</dl>
<p> PAM_PERM_DENY</p>
<dl>
<dd>Permission denied.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Cannot determine the user name.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Success.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known.</dl>
<h2>Examples</h2>
<p>The root account gains access by default (rootok), only wheel members can become root (wheel) but Unix authenticate non-root applicants.</p>
<dl>
<dd>
<pre>su auth sufficient pam_rootok.so
su auth required pam_wheel.so
su auth required pam_unix.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_wheel was written by Cristian Gafton &lt;gafton [at] redhat.com&gt;.</p>
