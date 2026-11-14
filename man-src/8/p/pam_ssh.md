---
title: "pam_ssh(8)"
name: "pam_ssh"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_ssh/"
description: "pam_ssh – authentication and session management with SSH private keys"
---

<p><code>pam_ssh</code> &#8211; authentication and session management with SSH private keys</p>
<h2>Synopsis</h2>
<p>[<i>service-name</i> ] <i>module-type</i> <i>control-flag</i> pam_ssh [<i>options</i> ]</p>
<h2>Description</h2>
<p>The SSH authentication service module for PAM, provides functionality for two PAM categories: authentication and session management. In terms of the <i>module-type</i> parameter, they are the &#8220;<code>auth</code> &#8221; and &#8220;<code>session</code> &#8221; features. It also provides null functions for the remaining categories.</p>
<h3>SSH Authentication Module</h3>
<p>The SSH authentication component provides a function to verify the identity of a user (Fn pam_sm_authenticate ) by prompting the user for a passphrase and verifying that it can decrypt the target user&#8217;s SSH key using that passphrase. The following options may be passed to the authentication module:</p>
<dl>
<dt><code>debug</code></p>
<dd><a href="/docs/linux/man/3-syslog/">syslog</a>(3) debugging information at <code>LOG_DEBUG</code> level.</p>
<dt><code>use_first_pass</code></p>
<dd>If the authentication module is not the first in the stack, and a previous module obtained the user&#8217;s password, that password is used to authenticate the user. If this fails, the authentication module returns failure without prompting the user for a password. This option has no effect if the authentication module is the first in the stack, or if no previous modules obtained the user&#8217;s password.</p>
<dt><code>try_first_pass</code></p>
<dd>This option is similar to the <code>use_first_pass</code> option, except that if the previously obtained password fails, the user is prompted for another password.</p>
<dt><code>keyfiles</code></p>
<dd>Specify the comma-separated list of files in $HOME/.ssh to check for SSH keys. The default is &#8220;id_dsa,id_rsa,identity&#8221;</p>
<dt><code>nullok</code></p>
<dd>Allow empty passphrases.</dl>
<h3>SSH Session Management Module</h3>
<p>The SSH session management component provides functions to initiate (Fn pam_sm_open_session ) and terminate (Fn pam_sm_close_session ) sessions. The Fn pam_sm_open_session function starts an SSH agent, passing it any private keys it decrypted during the authentication phase, and sets the environment variables the agent specifies. The Fn pam_sm_close_session function kills the previously started SSH agent by sending it a <code>SIGTERM</code> The following options may be passed to the session management module:</p>
<dl>
<dt><code>debug</code></p>
<dd><a href="/docs/linux/man/3-syslog/">syslog</a>(3) debugging information at <code>LOG_DEBUG</code> level.</dl>
<h2>Files</h2>
<dl>
<dt><code>$HOME/.ssh/identity </code></p>
<dd>SSH1/OpenSSH RSA key</p>
<dt><code>$HOME/.ssh/id_dsa </code></p>
<dd>OpenSSH DSA key</p>
<dt><code>$HOME/.ssh2/id_rsa_* </code></p>
<dd>SSH2 RSA keys</p>
<dt><code>$HOME/.ssh2/id_dsa_* </code></p>
<dd>SSH2 DSA keys</p>
<dt><code>/var/run/pam_ssh/&lt;user&gt;* </code></p>
<dd>ssh-agent environment information. The files are owned by the superuser but readable by the users. The location is Fedora specific, in the original package these files are in $HOME/.ssh/agent-*</dl>
<h2>See Also</h2>
<p>ssh-agent1, <a href="/docs/linux/man/3-syslog/">syslog</a>(3), pam.conf5, <a href="/docs/linux/man/8-pam/">pam</a>(8)</p>
<h2>Authors</h2>
<p>An -nosplit An Andrew J. Korty Aq ajk [at] iu.edu wrote <code>.</code> An Dag-Erling Smorgrav wrote the original OpenPAM support code. An Mark R V Murray wrote the original version of this manual page.</p>
