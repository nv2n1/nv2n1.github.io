---
title: "faillock(8)"
name: "faillock"
section: "8"
letter: "f"
url: "/docs/linux/man/8-faillock/"
description: "faillock – Tool for displaying and modifying the authentication failure record files"
---

<p>faillock &#8211; Tool for displaying and modifying the authentication failure record files</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>faillock</code> [&#8211;dir&nbsp;<i>/path/to/tally-directory</i>] [&#8211;user&nbsp;<i>username</i>] [&#8211;reset]</dl>
<h2>Description</h2>
<dd>The <i>pam_faillock.so</i> module maintains a list of failed authentication attempts per user during a specified interval and locks the account in case there were more than <i>deny</i> consecutive failed authentications. It stores the failure records into per-user files in the tally directory. </p>
<p> The <code>faillock</code> command is an application which can be used to examine and modify the contents of the tally files. It can display the recent failed authentication attempts of the <i>username</i> or clear the tally files of all or individual <i>usernames</i>.</p>
<h2>Options</h2>
<p><code>&#8211;dir </code><i>/path/to/tally-directory</i></p>
<dl>
<dd>The directory where the user files with the failure records are kept. The default is /var/run/faillock.</dl>
<p> <code>&#8211;user </code><i>username</i></p>
<dl>
<dd>The user whose failure records should be displayed or cleared.</dl>
<p> <code>&#8211;reset</code></p>
<dl>
<dd>Instead of displaying the user&#8217;s failure records, clear them.</dl>
<h2>Files</h2>
<p>/var/run/faillock/*</p>
<dl>
<dd>the files logging the authentication failures for users</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_faillock/">pam_faillock</a></code>(8), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Author</h2>
<p>faillock was written by Tomas Mraz.</p>
