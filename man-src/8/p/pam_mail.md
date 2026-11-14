---
title: "pam_mail(8)"
name: "pam_mail"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_mail/"
description: "pam_mail – Inform about available mail"
---

<p>pam_mail &#8211; Inform about available mail</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_mail.so</code> [close] [debug] [dir=<i>maildir</i>] [empty] [hash=<i>count</i>] [noenv] [nopen] [quiet] [standard]</dl>
<h2>Description</h2>
<dd>The pam_mail PAM module provides the &quot;you have new mail&quot; service to the user. It can be plugged into any application that has credential or session hooks. It gives a single message indicating the <i>newness</i> of any mail it finds in the user&#8217;s mail folder. This module also sets the PAM environment variable, <code>MAIL</code>, to the user&#8217;s mail directory. </p>
<p> If the mail spool file (be it /var/mail/$USER or a pathname given with the <code>dir=</code> parameter) is a directory then pam_mail assumes it is in the <i>Maildir</i> format.</p>
<h2>Options</h2>
<p><code>close</code></p>
<dl>
<dd>Indicate if the user has any mail also on logout.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>dir=</code><i>maildir</i></p>
<dl>
<dd>Look for the user&#8217;s mail in an alternative location defined by maildir/&lt;login&gt;. The default location for mail is /var/mail/&lt;login&gt;. Note, if the supplied maildir is prefixed by a &#8216;~&#8217;, the directory is interpreted as indicating a file in the user&#8217;s home directory.</dl>
<p> <code>empty</code></p>
<dl>
<dd>Also print message if user has no mail.</dl>
<p> <code>hash=</code><i>count</i></p>
<dl>
<dd>Mail directory hash depth. For example, a <i>hashcount</i> of 2 would make the mail file be /var/spool/mail/u/s/user.</dl>
<p> <code>noenv</code></p>
<dl>
<dd>Do not set the <code>MAIL</code> environment variable.</dl>
<p> <code>nopen</code></p>
<dl>
<dd>Don&#8217;t print any mail information on login. This flag is useful to get the <code>MAIL</code> environment variable set, but to not display any information about it.</dl>
<p> <code>quiet</code></p>
<dl>
<dd>Only report when there is new mail.</dl>
<p> <code>standard</code></p>
<dl>
<dd>Old style &quot;You have&#8230;&quot; format which doesn&#8217;t show the mail spool being used. This also implies &quot;empty&quot;.</dl>
<h2>Module Types Provided</h2>
<p>The <code>session</code> and <code>auth</code> (on establishment and deletion of credentials) module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Badly formed arguments.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Success.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known.</dl>
<h2>Examples</h2>
<p>Add the following line to /etc/pam.d/login to indicate that the user has new mail when they login to the system.</p>
<dl>
<dd>
<pre>session optional pam_mail.so standard</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_mail was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;.</p>
