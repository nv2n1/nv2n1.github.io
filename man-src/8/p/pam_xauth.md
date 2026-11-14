---
title: "pam_xauth(8)"
name: "pam_xauth"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_xauth/"
description: "pam_xauth – PAM module to forward xauth keys between users"
---

<p>pam_xauth &#8211; PAM module to forward xauth keys between users</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_xauth.so</code> [debug] [xauthpath=<i>/path/to/xauth</i>] [systemuser=<i>UID</i>] [targetuser=<i>UID</i>]</dl>
<h2>Description</h2>
<dd>The pam_xauth PAM module is designed to forward xauth keys (sometimes referred to as &quot;cookies&quot;) between users. </p>
<p> Without pam_xauth, when xauth is enabled and a user uses the <code><a href="/docs/linux/man/1-su/">su</a></code>(1) command to assume another user&#8217;s privileges, that user is no longer able to access the original user&#8217;s X display because the new user does not have the key needed to access the display. pam_xauth solves the problem by forwarding the key from the user running su (the source user) to the user whose identity the source user is assuming (the target user) when the session is created, and destroying the key when the session is torn down. </p>
<p> This means, for example, that when you run <code><a href="/docs/linux/man/1-su/">su</a></code>(1) from an xterm session, you will be able to run X programs without explicitly dealing with the <code><a href="/docs/linux/man/1-xauth/">xauth</a></code>(1) xauth command or ~/.Xauthority files. </p>
<p> pam_xauth will only forward keys if xauth can list a key connected to the $DISPLAY environment variable. </p>
<p> Primitive access control is provided by ~/.xauth/export in the invoking user&#8217;s home directory and ~/.xauth/import in the target user&#8217;s home directory. </p>
<p> If a user has a ~/.xauth/import file, the user will only receive cookies from users listed in the file. If there is no ~/.xauth/import file, the user will accept cookies from any other user. </p>
<p> If a user has a .xauth/export file, the user will only forward cookies to users listed in the file. If there is no ~/.xauth/export file, and the invoking user is not <code>root</code>, the user will forward cookies to any other user. If there is no ~/.xauth/export file, and the invoking user is <code>root</code>, the user will <i>not</i> forward cookies to other users. </p>
<p> Both the import and export files support wildcards (such as <i>*</i>). Both the import and export files can be empty, signifying that no users are allowed.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>xauthpath=</code><i>/path/to/xauth</i></p>
<dl>
<dd>Specify the path the xauth program (it is expected in /usr/X11R6/bin/xauth, /usr/bin/xauth, or /usr/bin/X11/xauth by default).</dl>
<p> <code>systemuser=</code><i>UID</i></p>
<dl>
<dd>Specify the highest UID which will be assumed to belong to a &quot;system&quot; user. pam_xauth will refuse to forward credentials to users with UID less than or equal to this number, except for root and the &quot;targetuser&quot;, if specified.</dl>
<p> <code>targetuser=</code><i>UID</i></p>
<dl>
<dd>Specify a single target UID which is exempt from the systemuser check.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> type is provided.</p>
<h2>Return Values</h2>
<p>PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>Permission denied by import/export file.</dl>
<p> PAM_SESSION_ERR</p>
<dl>
<dd>Cannot determine user name, UID or access users home directory.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Success.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known.</dl>
<h2>Examples</h2>
<p>Add the following line to /etc/pam.d/su to forward xauth keys between users when calling su:</p>
<dl>
<dd>
<pre>session optional pam_xauth.so</pre>
</dl>
<h2>Implementation Details</h2>
<p>pam_xauth will work <i>only</i> if it is used from a setuid application in which the <code>getuid</code>() call returns the id of the user running the application, and for which PAM can supply the name of the account that the user is attempting to assume. The typical application of this type is <code><a href="/docs/linux/man/1-su/">su</a></code>(1). The application must call both <code>pam_open_session</code>() and <code>pam_close_session</code>() with the ruid set to the uid of the calling user and the euid set to root, and must have provided as the PAM_USER item the name of the target user. </p>
<p> pam_xauth calls <code><a href="/docs/linux/man/1-xauth/">xauth</a></code>(1) as the source user to extract the key for $DISPLAY, then calls xauth as the target user to merge the key into the a temporary database and later remove the database. </p>
<p> pam_xauth cannot be told to not remove the keys when the session is closed.</p>
<h2>Files</h2>
<p>~/.xauth/import</p>
<dl>
<dd>XXX</dl>
<p> ~/.xauth/export</p>
<dl>
<dd>XXX</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_xauth was written by Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;, based on original version by Michael K. Johnson &lt;johnsonm [at] redhat.com&gt;.</p>
