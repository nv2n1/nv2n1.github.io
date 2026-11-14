---
title: "pam_sge-qrsh-setup(8)"
name: "pam_sge-qrsh-setup"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_sge-qrsh-setup/"
description: "pam_sge-qrsh-setup – PAM module for tight integration with xxQS_NAMExx"
---

<p>pam_sge-qrsh-setup &#8211; PAM module for tight integration with xxQS_NAMExx</p>
<h2>Synopsis</h2>
<p><code>pam_sge-qrsh-setup</code></p>
<h2>Description</h2>
<p>This PAM module provides tight integration of SSH communication into xxQS_NAMExx when is used with <code>qrsh</code> etc. It may also work with other communication methods that run daemons which use PAM. See It provides to the spawned processes the group id from <i>$SGE_ROOT</i><code>/default/spool/</code><i>hostname</i><code>/active_jobs/</code><i>job_id</i><code>/addgrpid</code> and the environment from <i>$SGE_ROOT</i><code>/default/spool/</code><i>hostname</i><code>/active_jobs/</code><i>job_id</i><code>/environment</code>. </p>
<p> It assumes the use of a wrapper for <code>rshd</code>. A suitable one is distributed as <code>util/resources/wrappers/rshd-wrapper</code> under the xxQS_NAMExx root directory.</p>
<h2>Options</h2>
<p>The module has no options.</p>
<h2>Example</h2>
<p>On a typical GNU/Linux system, add the following line to <code>/etc/pam.d/sshd</code>, e.g. at the top of the file. </p>
<dl>
<dd>&nbsp;auth required&nbsp;/opt/sge/lib/lx-amd64/pam_sge-qrsh-setup.so </p>
</dl>
<p> On some systems it might be necessary to copy pam_sge-qrsh-setup.so into, say, <code>/lib/security</code> and instead use it as </p>
<dl>
<dd>&nbsp;auth required pam_sge-qrsh-setup.so</dl>
<h2>Files</h2>
<p><code>/var/run/sge-qrsh-setup</code><br />
 <code>$SGE_ROOT/util/resources/wrappers/rshd-wrapper</code></p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Andreas Haupt, man page by Dave Love.</p>
