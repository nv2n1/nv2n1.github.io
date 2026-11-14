---
title: "pam_umask(8)"
name: "pam_umask"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_umask/"
description: "pam_umask – PAM module to set the file mode creation mask"
---

<p>pam_umask &#8211; PAM module to set the file mode creation mask</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_umask.so</code> [debug] [silent] [usergroups] [nousergroups] [umask=<i>mask</i>]</dl>
<h2>Description</h2>
<dd>pam_umask is a PAM module to set the file mode creation mask of the current environment. The umask affects the default permissions assigned to newly created files. </p>
<p> The PAM module tries to get the umask value from the following places in the following order: </p>
<dl>
<dd>&bull; umask= entry in the user&#8217;s GECOS field</dl>
<dl>
<dd>&bull; umask= argument</dl>
<dl>
<dd>&bull; UMASK entry from /etc/login.defs (influenced by USERGROUPS_ENAB in /etc/login.defs)</dl>
<dl>
<dd>&bull; UMASK= entry from /etc/default/login</dl>
<p> The GECOS field is split on comma &#8216;,&#8217; characters. The module also in addition to the umask= entry recognizes pri= entry, which sets the nice priority value for the session, and ulimit= entry, which sets the maximum size of files the processes in the session can create.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>silent</code></p>
<dl>
<dd>Don&#8217;t print informative messages.</dl>
<p> <code>usergroups</code></p>
<dl>
<dd>If the user is not root and the username is the same as primary group name, the umask group bits are set to be the same as owner bits (examples: 022 -&gt; 002, 077 -&gt; 007). Note that using this option explicitly is discouraged. pam_umask enables this functionality by default if /etc/login.defs enables USERGROUPS_ENAB, and the umask is not set explicitly in other places than /etc/login.defs (this is compatible with login&#8217;s behaviour without PAM).</dl>
<p> <code>nousergroups</code></p>
<dl>
<dd>This is the direct opposite of the usergroups option described above, which can be useful in case pam_umask has been compiled with usergroups enabled by default and you want to disable it at runtime.</dl>
<p> <code>umask=</code><i>mask</i></p>
<dl>
<dd>Sets the calling process&#8217;s file mode creation mask (umask) to <code>mask</code> &amp; 0777. The value is interpreted as Octal.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> type is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The new umask was set successfully.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>The conversation method supplied by the application failed to obtain the username.</dl>
<p> PAM_INCOMPLETE</p>
<dl>
<dd>The conversation method supplied by the application returned PAM_CONV_AGAIN.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>No username was given.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known.</dl>
<h2>Examples</h2>
<p>Add the following line to /etc/pam.d/login to set the user specific umask at login:</p>
<dl>
<dd>
<pre> session optional pam_umask.so umask=0022</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_umask was written by Thorsten Kukuk &lt;kukuk [at] thkukuk.de&gt;.</p>
