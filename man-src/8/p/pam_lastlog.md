---
title: "pam_lastlog(8)"
name: "pam_lastlog"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_lastlog/"
description: "pam_lastlog – PAM module to display date of last login and perform inactive account lock out"
---

<p>pam_lastlog &#8211; PAM module to display date of last login and perform inactive account lock out</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_lastlog.so</code> [debug] [silent] [never] [nodate] [nohost] [noterm] [nowtmp] [noupdate] [showfailed] [inactive=&lt;days&gt;] [unlimited]</dl>
<h2>Description</h2>
<dd>pam_lastlog is a PAM module to display a line of information about the last login of the user. In addition, the module maintains the /var/log/lastlog file. </p>
<p> Some applications may perform this function themselves. In such cases, this module is not necessary. </p>
<p> The module checks <code>LASTLOG_UID_MAX</code> option in /etc/login.defs and does not update or display last login records for users with UID higher than its value. If the option is not present or its value is invalid, no user ID limit is applied. </p>
<p> If the module is called in the auth or account phase, the accounts that were not used recently enough will be disallowed to log in. The check is not performed for the root account so the root is never locked out. It is also not performed for users with UID higher than the <code>LASTLOG_UID_MAX</code> value.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>silent</code></p>
<dl>
<dd>Don&#8217;t inform the user about any previous login, just update the /var/log/lastlog file. This option does not affect display of bad login attempts.</dl>
<p> <code>never</code></p>
<dl>
<dd>If the /var/log/lastlog file does not contain any old entries for the user, indicate that the user has never previously logged in with a welcome message.</dl>
<p> <code>nodate</code></p>
<dl>
<dd>Don&#8217;t display the date of the last login.</dl>
<p> <code>noterm</code></p>
<dl>
<dd>Don&#8217;t display the terminal name on which the last login was attempted.</dl>
<p> <code>nohost</code></p>
<dl>
<dd>Don&#8217;t indicate from which host the last login was attempted.</dl>
<p> <code>nowtmp</code></p>
<dl>
<dd>Don&#8217;t update the wtmp entry.</dl>
<p> <code>noupdate</code></p>
<dl>
<dd>Don&#8217;t update any file.</dl>
<p> <code>showfailed</code></p>
<dl>
<dd>Display number of failed login attempts and the date of the last failed attempt from btmp. The date is not displayed when <code>nodate</code> is specified.</dl>
<p> <code>inactive=&lt;days&gt;</code></p>
<dl>
<dd>This option is specific for the auth or account phase. It specifies the number of days after the last login of the user when the user will be locked out by the module. The default value is 90.</dl>
<p> <code>unlimited</code></p>
<dl>
<dd>If the <i>fsize</i> limit is set, this option can be used to override it, preventing failures on systems with large UID values that lead lastlog to become a huge sparse file.</dl>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>account</code> module type allows one to lock out users who did not login recently enough. The <code>session</code> module type is provided for displaying the information about the last login and/or updating the lastlog and wtmp files.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>Everything was successful.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Internal service module error.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known.</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>User locked out in the auth or account phase due to inactivity.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>There was an error during reading the lastlog file in the auth or account phase and thus inactivity of the user cannot be determined.</dl>
<h2>Examples</h2>
<p>Add the following line to /etc/pam.d/login to display the last login time of an user: </p>
<dl>
<dd>
<pre> session required pam_lastlog.so nowtmp</pre>
</dl>
<p> To reject the user if he did not login during the previous 50 days the following line can be used: </p>
<dl>
<dd>
<pre> auth required pam_lastlog.so inactive=50</pre>
</dl>
<h2>Files</h2>
<p>/var/log/lastlog</p>
<dl>
<dd>Lastlog logging file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-limits-conf/">limits.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_lastlog was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;. </p>
<p> Inactive account lock out added by Tomáš Mráz &lt;tm [at] t8m.info&gt;.</p>
