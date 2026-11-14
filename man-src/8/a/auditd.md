---
title: "auditd(8)"
name: "auditd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-auditd/"
description: "auditd – The Linux Audit daemon"
---

<p>auditd &#8211; The Linux Audit daemon</p>
<h2>Synopsis</h2>
<p><code>auditd</code> [<code>-f</code>]&nbsp;<wbr>[<code>-l</code>]&nbsp;<wbr>[<code>-n</code>]&nbsp;<wbr>[<code>-s disable|enable|nochange</code>]</p>
<h2>Description</h2>
<p><code>auditd</code> is the userspace component to the Linux Auditing System. It&#8217;s responsible for writing audit records to the disk. Viewing the logs is done with the <code>ausearch</code> or <code>aureport</code> utilities. Configuring the audit system or loading rules is done with the <code>auditctl</code> utility. During startup, the rules in <i>/etc/audit/audit.rules</i> are read by <code>auditctl</code> and loaded into the kernel. Alternately, there is also an <code>augenrules</code> program that reads rules located in <i>/etc/audit/rules.d/</i> and compiles them into an audit.rules file. The audit daemon itself has some configuration options that the admin may wish to customize. They are found in the <code>auditd.conf</code> file.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>leave the audit daemon in the foreground for debugging. Messages also go to stderr rather than the audit log.</p>
<dt><code>-l</code></p>
<dd>allow the audit daemon to follow symlinks for config files.</p>
<dt><code>-n</code></p>
<dd>no fork. This is useful for running off of inittab or systemd.</p>
<dt><code>-s=</code><i>ENABLE_STATE</i></p>
<dd>specify when starting if auditd should change the current value for the kernel enabled flag. Valid values for ENABLE_STATE are &quot;disable&quot;, &quot;enable&quot; or &quot;nochange&quot;. The default is to enable (and disable when auditd terminates). The value of the enabled flag may be changed during the lifetime of auditd using &#8216;auditctl -e&#8217;.</dl>
<h2>Signals</h2>
<dl>
<dt>SIGHUP</p>
<dd>causes auditd to reconfigure. This means that auditd re-reads the configuration file. If there are no syntax errors, it will proceed to implement the requested changes. If the reconfigure is successful, a DAEMON_CONFIG event is recorded in the logs. If not successful, error handling is controlled by space_left_action, admin_space_left_action, disk_full_action, and disk_error_action parameters in auditd.conf. </p>
<dt>SIGTERM</p>
<dd>caused auditd to discontinue processing audit events, write a shutdown audit event, and exit. </p>
<dt>SIGUSR1</p>
<dd>causes auditd to immediately rotate the logs. It will consult the max_log_file_action to see if it should keep the logs or not. </p>
<dt>SIGUSR2</p>
<dd>causes auditd to attempt to resume logging. This is usually needed after logging has been suspended. </p>
</dl>
<h2>Files</h2>
<p><code>/etc/audit/auditd.conf</code> &#8211; configuration file for audit daemon </p>
<p> <code>/etc/audit/audit.rules</code> &#8211; audit rules to be loaded at startup </p>
<p> <code>/etc/audit/rules.d/</code> &#8211; directory holding individual sets of rules to be compiled into one file by augenrules.</p>
<h2>Notes</h2>
<p>A boot param of audit=1 should be added to ensure that all processes that run before the audit daemon starts is marked as auditable by the kernel. Not doing that will make a few processes impossible to properly audit. The audit daemon can receive audit events from other audit daemons via the audisp-remote audispd plugin. The audit daemon may be linked with tcp_wrappers to control which machines can connect. If this is the case, you can add an entry to hosts.allow and deny. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-auditd-conf/">auditd.conf</a></code>(5), <code><a href="/docs/linux/man/8-audispd/">audispd</a></code>(8), <code><a href="/docs/linux/man/8-ausearch/">ausearch</a></code>(8), <code><a href="/docs/linux/man/8-aureport/">aureport</a></code>(8), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8), <code><a href="/docs/linux/man/8-augenrules/">augenrules</a></code>(8), <code><a href="/docs/linux/man/7-audit-rules/">audit.rules</a></code>(7). </p>
<h2>Author</h2>
<p>Steve Grubb</p>
