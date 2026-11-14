---
title: "pam_console_apply(8)"
name: "pam_console_apply"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_console_apply/"
description: "pam_console_apply – set or revoke permissions for users at the system console"
---

<p>pam_console_apply &#8211; set or revoke permissions for users at the system console</p>
<h2>Synopsis</h2>
<p><code>pam_console_apply </code> [-f &lt;fstab file&gt;] [-c &lt;console.perms file&gt;] [-r] [-t &lt;tty&gt;] [-s] [-d] [&lt;device file&gt; &#8230;]</p>
<h2>Description</h2>
<p><code>pam_console_apply</code> is a helper executable which sets or resets permissions on device nodes.<br />
 If <i>/var/run/console.lock</i> exists, <code>pam_console_apply</code> will grant permissions to the user listed therein. If the lock file does not exist, permissions are reset according to defaults set in <i>console.perms</i> files, normally configured to set permissions on devices so that <code>root</code> owns them. </p>
<p> When initializing its configuration it first parses the <i>/etc/security/console.perms</i> file and then it searches for files ending with the <i>.perms</i> suffix in the <i>/etc/security/console.perms.d</i> directory. These files are parsed in the lexical order in &quot;C&quot; locale. Permission rules are appended to a global list, console and device class definitions override previous definitions of the same class.</p>
<h2>Arguments</h2>
<dl>
<dt>-c</p>
<dd>Load other console.perms file than the default one.</p>
<dt>-f</p>
<dd>Load other fstab file than the default one (<i>/etc/fstab</i>).</p>
<dt>-r</p>
<dd>Signals <code>pam_console_apply</code> to reset permissions. The default is to set permissions so that the user listed in <i>/var/run/console.lock</i> has access to the devices, and to reset permissions if no such file exists.</p>
<dt>-t</p>
<dd>Use &lt;tty&gt; to match console class in console.perms file. The default is tty0.</p>
<dt>-s</p>
<dd>Write error messages to the system log instead of stderr.</p>
<dt>-d</p>
<dd>Log/display messages useful for debugging.</dl>
<p> The optional &lt;device file&gt; arguments constrain what files should be affected by <code>pam_console_apply</code>. If they aren&#8217;t specified permissions are changed on all files specified in the <i>console.perms</i> file.</p>
<h2>Files</h2>
<p><i>/var/run/console.lock</i><br />
 <i>/etc/security/console.perms</i><br />
 <i>/etc/security/console.perms.d/50-default.perms</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_console/">pam_console</a>(8)</code><br />
 <code><a href="/docs/linux/man/5-console-perms/">console.perms</a>(5)</code></p>
<h2>Bugs</h2>
<p>Let&#8217;s hope not, but if you find any, please report them via the &quot;Bug Track&quot; link at <a rel="nofollow" href="http://bugzilla.redhat.com/bugzilla/">http://bugzilla.redhat.com/bugzilla/</a></p>
<h2>Authors</h2>
<p>Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;, using code shamelessly stolen from parts of pam_console.<br />
 Support of console.perms.d and other improvements by Tomas Mraz &lt;tmraz [at] redhat.com&gt;.</p>
