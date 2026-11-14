---
title: "pam_sge_authorize(8)"
name: "pam_sge_authorize"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_sge_authorize/"
description: "pam_sge_authorize – PAM module to control access to SGE hosts"
---

<p>pam_sge_authorize &#8211; PAM module to control access to SGE hosts</p>
<h2>Synopsis</h2>
<p><code>pam_sge_authorize</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>This PAM module limits access via etc. to xxQS_NAMExx hosts only to users who currently have a job running on the host. The expectation is that this limits their impact on any other users of the host.</p>
<h2>Options</h2>
<p><code>execd_spool_dir=</code><i>dir</i></p>
<dl>
<dd>Specify the spool directory in which to find the <code>active_jobs</code> directory as <i>dir</i><code>/</code><i>hostname</i><code>/active_jobs</code>. Default: <code>/opt/sge/default/spool</code>.</dl>
<p> <code>bypass_users=</code><i>user_list</i></p>
<dl>
<dd>The module ignores access by users with unames in the comma-separated <i>user_list</i>. There is a limit of 30 users. root is always allowed access.</dl>
<p> <code>max_sleep=</code><i>max_sleep</i></p>
<dl>
<dd>A non-zero <i>max_sleep</i> allows desynchronization of accesses to the spool directory. The module sleeps for a random period <i>t</i>, where 0&lt;=<i>t</i>&lt;=<i>max_sleep</i> microseconds before accessing the spool directory. This probably isn&#8217;t useful. Default: 0.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Send debugging information to syslog.</dl>
<p> <code>active</code></p>
<dl>
<dd>Require an active job, i.e. a running shepherd on the host. This can be used to enforce tight integration for distributed jobs, i.e. direct access to other nodes of the job is prevented via SSH, rather than <code>qrsh -inherit</code>.</dl>
<h2>Example</h2>
<p>On a typical GNU/Linux system, add something like the following to <code>/etc/pam.d/sshd</code>, e.g. at the top.</p>
<dl>
<dd>
<pre>account required /opt/sge/lib/lx-amd64/pam_sge_authorize.so \
 bypass_users=foo,bar,baz,qux spool_dir=/opt/sge/execd_spool</pre>
</dl>
<p> On some systems it might be necessary to copy pam_sge_authorize.so into, say, <code>/lib/security</code>, and instead use it as</p>
<dl>
<dd>auth required pam_sge_authorize.so</dl>
<h2>See Also</h2>
<h2>Author</h2>
<p>TACC. Man page by Dave Love, based on material from Bill Barth, TACC.</p>
