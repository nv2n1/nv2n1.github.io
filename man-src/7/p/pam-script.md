---
title: "pam-script(7)"
name: "pam-script"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pam-script/"
description: "pam-script – a PAM module that can invoke scripts within the PAM stack."
---

<p>pam-script &#8211; a PAM module that can invoke scripts within the PAM stack.</p>
<h2>Synopsis</h2>
<p><code>pam-script.so</code> [<i>onerr=(success|fail)</i>][<i>dir=/some/path/</i>] </p>
<h2>Description</h2>
<p><code>pam-script</code> allows you to execute scripts during authorization, passwd changes, and on session opening or closing. Such scripts can perform necessary tasks or influence the outcome of the PAM stack. For example, if the following entry was included in <i>pam.conf</i><br />
&nbsp;<wbr>&nbsp;<wbr>sshd<tt>&nbsp;<wbr>&nbsp;<wbr></tt>auth<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>required<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pam_script<br />
 then if the script, <i>pam_script_auth</i>, exits with a non-zero value this would cause the user to be denied SSH access to the machine. </p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>onerr=(success|fail)</code></p>
<dd>the default behavior if the module can not find or execute the script. The default is to fail if the option is not given.</p>
<dt><code>dir=/some/path/</code></p>
<dd>where to find the pam-scripts to invoke for each of the various module-types as described below. The default is dir=/etc if not given. </p>
<p> List of scripts</p>
<dt><code>pam_script_auth</code></p>
<dd>Executed under <i>auth</i> which handles the authentication stage of establishing the user via some challenge-response (i.e. username/password)</p>
<dt><code>pam_script_acct</code></p>
<dd>invoked under <i>account</i> module-type for non-authentication based account management.</p>
<dt><code>pam_script_passwd</code></p>
<dd>invoked under <i>passwd</i> for changing the password tokens.</p>
<dt><code>pam_script_ses_open</code></p>
<dd>invoked when a <i>session</i> is first opened.</p>
<dt><code>pam_script_ses_close</code></p>
<dd>run after a <i>session</i> is first closed. </p>
<p> All the scripts will be passed several environment variables: PAM_USER, PAM_RUSER, PAM_RHOST, PAM_SERVICE, PAM_AUTHTOK, PAM_TTY, and PAM_TYPE referring to the module-type. The pam_script.so arguments in the pam.conf will be passed on the command line, which can be used to modify the script behavior. </p>
</dl>
<h2>Files</h2>
<p><code>/lib64/security/pam_script.so</code> &#8211; the PAM module<br />
 <code>/etc</code> &#8211; where the scripts should be placed by default</p>
<h2>Version</h2>
<p>pam-script 1.1.8</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pam/">PAM</a></code>(7) and the PAM &quot;The System Administrators&#8217; Guide&quot;</p>
<h2>Author</h2>
<pre>pam-script was written by Jeroen Nijhof &lt;jeroen [at] jeroennijhof.nl&gt;
with some additions and modifications by R.K. Owen, Ph.D. &lt;rkowen [at] nersc.gov&gt;.
This manual page was written by R.K. Owen &lt;rkowen [at] nersc.gov&gt;,
for the Debian project (but may be used by others).</pre>
