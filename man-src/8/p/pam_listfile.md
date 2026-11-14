---
title: "pam_listfile(8)"
name: "pam_listfile"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_listfile/"
description: "pam_listfile – deny or allow services based on an arbitrary file"
---

<p>pam_listfile &#8211; deny or allow services based on an arbitrary file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_listfile.so</code> item=[tty|user|rhost|ruser|group|shell] sense=[allow|deny] file=<i>/path/filename</i> onerr=[succeed|fail] [apply=[<i>user</i>|<i>@group</i>]] [quiet]</dl>
<h2>Description</h2>
<dd>pam_listfile is a PAM module which provides a way to deny or allow services based on an arbitrary file. </p>
<p> The module gets the <code>item</code> of the type specified &#8212; <i>user</i> specifies the username, <i>PAM_USER</i>; tty specifies the name of the terminal over which the request has been made, <i>PAM_TTY</i>; rhost specifies the name of the remote host (if any) from which the request was made, <i>PAM_RHOST</i>; and ruser specifies the name of the remote user (if available) who made the request, <i>PAM_RUSER</i> &#8212; and looks for an instance of that item in the <code>file=</code><i>filename</i>. filename contains one line per item listed. If the item is found, then if <code>sense=</code><i>allow</i>, <i>PAM_SUCCESS</i> is returned, causing the authorization request to succeed; else if <code>sense=</code><i>deny</i>, <i>PAM_AUTH_ERR</i> is returned, causing the authorization request to fail. </p>
<p> If an error is encountered (for instance, if filename does not exist, or a poorly-constructed argument is encountered), then if <i>onerr=succeed</i>, <i>PAM_SUCCESS</i> is returned, otherwise if <i>onerr=fail</i>, <i>PAM_AUTH_ERR</i> or <i>PAM_SERVICE_ERR</i> (as appropriate) will be returned. </p>
<p> An additional argument, <code>apply=</code>, can be used to restrict the application of the above to a specific user (<code>apply=</code><i>username</i>) or a given group (<code>apply=</code><i>@groupname</i>). This added restriction is only meaningful when used with the <i>tty</i>, <i>rhost</i> and <i>shell</i> items. </p>
<p> Besides this last one, all arguments should be specified; do not count on any default behavior. </p>
<p> No credentials are awarded by this module.</p>
<h2>Options</h2>
<p><code>item=[tty|user|rhost|ruser|group|shell]</code></p>
<dl>
<dd>What is listed in the file and should be checked for.</dl>
<p> <code>sense=[allow|deny]</code></p>
<dl>
<dd>Action to take if found in file, if the item is NOT found in the file, then the opposite action is requested.</dl>
<p> <code>file=</code><i>/path/filename</i></p>
<dl>
<dd>File containing one item per line. The file needs to be a plain file and not world writable.</dl>
<p> <code>onerr=[succeed|fail]</code></p>
<dl>
<dd>What to do if something weird happens like being unable to open the file.</dl>
<p> <code>apply=[</code><i>user</i><code>|</code><i>@group</i><code>]</code></p>
<dl>
<dd>Restrict the user class for which the restriction apply. Note that with <code>item=[user|ruser|group]</code> this does not make sense, but for <code>item=[tty|rhost|shell]</code> it have a meaning.</dl>
<p> <code>quiet</code></p>
<dl>
<dd>Do not treat service refusals or missing list files as errors that need to be logged.</dl>
<h2>Module Types Provided</h2>
<p>All module types (<code>auth</code>, <code>account</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>Authentication failure.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>The rule does not apply to the <code>apply</code> option.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Error in service module.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Success.</dl>
<h2>Examples</h2>
<p>Classic &#8216;ftpusers&#8217; authentication can be implemented with this entry in /etc/pam.d/ftpd: </p>
<dl>
<dd>
<pre>#
# deny ftp-access to users listed in the /etc/ftpusers file
#
auth required pam_listfile.so \
 onerr=succeed item=user sense=deny file=/etc/ftpusers</pre>
</dl>
<p> Note, users listed in /etc/ftpusers file are (counterintuitively) <i>not</i> allowed access to the ftp service. </p>
<p> To allow login access only for certain users, you can use a /etc/pam.d/login entry like this: </p>
<dl>
<dd>
<pre>#
# permit login to users listed in /etc/loginusers
#
auth required pam_listfile.so \
 onerr=fail item=user sense=allow file=/etc/loginusers</pre>
</dl>
<p> For this example to work, all users who are allowed to use the login service should be listed in the file /etc/loginusers. Unless you are explicitly trying to lock out root, make sure that when you do this, you leave a way for root to log in, either by listing root in /etc/loginusers, or by listing a user who is able to <i>su</i> to the root account.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_listfile was written by Michael K. Johnson &lt;johnsonm [at] redhat.com&gt; and Elliot Lee &lt;sopwith [at] cuc.edu&gt;.</p>
