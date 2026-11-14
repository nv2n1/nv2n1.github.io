---
title: "pam_ssh_add(8)"
name: "pam_ssh_add"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_ssh_add/"
description: "pam_ssh_add – PAM module to auto load ssh keys into an agent"
---

<p>pam_ssh_add &#8211; PAM module to auto load ssh keys into an agent</p>
<h2>Description</h2>
<p>pam_ssh_add provides authentication and session modules that allow users to start their session with a running ssh-agent with as many ssh keys loaded as possible. </p>
<p> If used, the authentication module simply stores the authentication token for later use by the session module. Because this module performs no actual authentication it returns PAM_CRED_INSUFFICIENT on success and should always be accompanied by an actual authentication module in your pam configuration. </p>
<p> By default the session module will start a new ssh-agent and run ssh-add, loading any keys that exist in the default path for the newly logged in user. If any keys prompt for a password, and a authenication token was successfully stored, that token will be provided as the password.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>This option will turn on debug logging to syslog.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre> auth required pam_unix.so
 auth optional pam_ssh_add.so
 session optional pam_ssh_add.so</pre>
</dl>
<h2>Author</h2>
<p>Cockpit has been written by many m[blue]<code>contributors</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the m[blue]<code>upstream bug tracker</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>contributors</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/cockpit-project/cockpit/">https://github.com/cockpit-project/cockpit/</a></dl>
<dt> 2.</p>
<dd>upstream bug tracker</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/cockpit-project/cockpit/issues/new">https://github.com/cockpit-project/cockpit/issues/new</a></dl>
