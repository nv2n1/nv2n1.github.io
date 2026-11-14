---
title: "pam_exec(8)"
name: "pam_exec"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_exec/"
description: "pam_exec – PAM module which calls an external command"
---

<p>pam_exec &#8211; PAM module which calls an external command</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_exec.so</code> [debug] [expose_authtok] [seteuid] [quiet] [stdout] [log=<i>file</i>] [type=<i>type</i>] <i>command</i> [<i>&#8230;</i>]</dl>
<h2>Description</h2>
<dd>pam_exec is a PAM module that can be used to run an external command. </p>
<p> The child&#8217;s environment is set to the current PAM environment list, as returned by <code><a href="/docs/linux/man/3-pam_getenvlist/">pam_getenvlist</a></code>(3) In addition, the following PAM items are exported as environment variables: <i>PAM_RHOST</i>, <i>PAM_RUSER</i>, <i>PAM_SERVICE</i>, <i>PAM_TTY</i>, <i>PAM_USER</i> and <i>PAM_TYPE</i>, which contains one of the module types: <code>account</code>, <code>auth</code>, <code>password</code>, <code>open_session</code> and <code>close_session</code>. </p>
<p> Commands called by pam_exec need to be aware of that the user can have control over the environment.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>expose_authtok</code></p>
<dl>
<dd>During authentication the calling command can read the password from <code><a href="/docs/linux/man/3-stdin/">stdin</a></code>(3). Only first <i>PAM_MAX_RESP_SIZE</i> bytes of a password are provided to the command.</dl>
<p> <code>log=</code><i>file</i></p>
<dl>
<dd>The output of the command is appended to file</dl>
<p> <code>type=</code><i>type</i></p>
<dl>
<dd>Only run the command if the module type matches the given type.</dl>
<p> <code>stdout</code></p>
<dl>
<dd>Per default the output of the executed command is written to /dev/null. With this option, the stdout output of the executed command is redirected to the calling application. It&#8217;s in the responsibility of this application what happens with the output. The <code>log</code> option is ignored.</dl>
<p> <code>quiet</code></p>
<dl>
<dd>Per default pam_exec.so will echo the exit status of the external command if it fails. Specifying this option will suppress the message.</dl>
<p> <code>seteuid</code></p>
<dl>
<dd>Per default pam_exec.so will execute the external command with the real user ID of the calling process. Specifying this option means the command is run with the effective user ID.</dl>
<h2>Module Types Provided</h2>
<p>All module types (<code>auth</code>, <code>account</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>The external command was run successfully.</dl>
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
<dd>No argument or a wrong number of arguments were given.</dl>
<p> PAM_SYSTEM_ERR</p>
<dl>
<dd>A system error occurred or the command to execute failed.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd><code>pam_setcred</code> was called, which does not execute the command. Or, the value given for the type= parameter did not match the module type.</dl>
<h2>Examples</h2>
<p>Add the following line to /etc/pam.d/passwd to rebuild the NIS database after each local password change: </p>
<dl>
<dd>
<pre> password optional pam_exec.so seteuid /usr/bin/make -C /var/yp</pre>
</dl>
<p> This will execute the command </p>
<dl>
<dd>
<pre>make -C /var/yp</pre>
</dl>
<p> with effective user ID.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_exec was written by Thorsten Kukuk &lt;kukuk [at] thkukuk.de&gt; and Josh Triplett &lt;josh [at] joshtriplett.org&gt;.</p>
