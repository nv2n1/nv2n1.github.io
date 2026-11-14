---
title: "audisp-prelude(5)"
name: "audisp-prelude"
section: "5"
letter: "a"
url: "/docs/linux/man/5-audisp-prelude/"
description: "audisp-prelude.conf – the audisp-prelude configuration file"
---

<p>audisp-prelude.conf &#8211; the audisp-prelude configuration file</p>
<h2>Description</h2>
<p><code>audisp-prelude.conf</code> is the file that controls the configuration of the audit based intrusion detection system. There are 2 general kinds of configuration option types, enablers and actions. The enablers simply have <i>yes</i>/<i>no</i> as the only valid choices. </p>
<p> The action options currently allow <i>ignore</i>, and idmef<i></i> as its choices. The <i>ignore</i> option means that the IDS still detects events, but only logs the detection in response. The <i>idmef</i> option means that the IDS will send an IDMEF alert to the prelude manager upon detection. </p>
<p> The configuration options that are available are as follows: </p>
<dl>
<dt><i>profile</i></p>
<dd>This is a one word character string that is used to identify the profile name in the prelude reporting tools. The default is auditd.</p>
<dt><i>detect_avc</i></p>
<dd>This an enabler that determines if the IDS should be examining SE Linux AVC events. The default is <i>yes</i>.</p>
<dt><i>avc_action</i></p>
<dd>This is an action that determines what response should be taken whenever a SE Linux AVC is detected. The default is <i>idmef</i>.</p>
<dt><i>detect_login</i></p>
<dd>This is an enabler that determines if the IDS should be examining login events. The default is <i>yes</i>.</p>
<dt><i>login_action</i></p>
<dd>This is an action that determines what response should be taken whenever a login event is detected. The default is <i>idmef</i>.</p>
<dt><i>detect_login_fail_max</i></p>
<dd>This is an enabler that determines if the IDS should be looking for maximum number of failed logins for an account. The default is <i>yes</i>.</p>
<dt><i>login_fail_max_action</i></p>
<dd>This is an action that determines what response should be taken whenever the maximum number of failed logins for an account is detected. The default is <i>idmef</i>.</p>
<dt><i>detect_login_session_max</i></p>
<dd>This is an enabler that determines if the IDS should be looking for maximum concurrent sessions limit for an account. The default is <i>yes</i>.</p>
<dt><i>login_session_max_action</i></p>
<dd>This is an action that determines what response should be taken whenever the maximum concurrent sessions limit for an account is detected. The default is <i>idmef</i>.</p>
<dt><i>detect_login_location</i></p>
<dd>This is an enabler that determines if the IDS should be looking for logins being attempted from a forbidden location. The default is <i>yes</i>.</p>
<dt><i>login_location_action</i></p>
<dd>This is an action that determines what response should be taken whenever logins are attempted from a forbidden location. The default is <i>idmef</i>.</p>
<dt><i>detect_login_time_alerts</i></p>
<dd>This is an enabler that determines if the IDS should be looking for logins attempted during a forbidden time. The default is <i>yes</i>.</p>
<dt><i>login_time_action</i></p>
<dd>This is an action that determines what response should be taken whenever logins are attempted during a forbidden time. The default is <i>idmef</i>.</p>
<dt><i>detect_abend</i></p>
<dd>This is an enabler that determines if the IDS should be looking for programs terminating for an abnormal reason. The default is <i>yes</i>.</p>
<dt><i>abend_action</i></p>
<dd>This is an action that determines what response should be taken whenever programs terminate for an abnormal reason. The default is <i>idmef</i>.</p>
<dt><i>detect_promiscuous</i></p>
<dd>This is an enabler that determines if the IDS should be looking for promiscuous sockets being opened. The default is <i>yes</i>.</p>
<dt><i>promiscuous_action</i></p>
<dd>This is an action that determines what response should be taken whenever promiscuous sockets are detected open. The default is <i>idmef</i>.</p>
<dt><i>detect_mac_status</i></p>
<dd>This is an enabler that determines if the IDS should be detecting changes made to the SE Linux MAC enforcement. The default is <i>yes</i>.</p>
<dt><i>mac_status_action</i></p>
<dd>This is an action that determines what response should be taken whenever changes are made to the SE Linux MAC enforcement. The default is <i>idmef</i>.</p>
<dt><i>detect_group_auth</i></p>
<dd>This is an enabler that determines if the IDS should be detecting whenever a user fails in changing their default group. The default is <i>yes</i>.</p>
<dt><i>group_auth_act</i></p>
<dd>This is an action that determines what response should be taken whenever a user fails in changing their default group. The default is <i>idmef</i>.</p>
<dt><i>detect_watched_acct</i></p>
<dd>This is an enabler that determines if the IDS should be detecting a user attempting to login on an account that is being watched. The accounts to watch is set by the <i>watched_accounts</i> option. The default is <i>yes</i>.</p>
<dt><i>watched_acct_act</i></p>
<dd>This is an action that determines what response should be taken whenever a user attempts to login on an account that is being watched. The default is <i>idmef</i>.</p>
<dt><i>watched_accounts</i></p>
<dd>This option is a whitespace and comma separated list of accounts to watch. The accounts may be numeric or alphanumeric. If you want to include a range of accounts, separate them with a dash but no spaces. For example, to watch logins from bin to lp, use &quot;bin-lp&quot;. Only succesful logins logins are recorded.</p>
<dt><i>detect_watched_syscall</i></p>
<dd>This is an enabler that determines if the IDS should be detecting whenever a user runs a command that issues a syscall that is being watched. The default is <i>yes</i>.</p>
<dt><i>watched_syscall_act</i></p>
<dd>This is an action that determines what response should be taken whenever a user runs a command that issues a syscall that is being watched. The default is <i>idmef</i>.</p>
<dt><i>detect_watched_file</i></p>
<dd>This is an enabler that determines if the IDS should be detecting whenever a user accesses a file that is being watched. The default is <i>yes</i>.</p>
<dt><i>watched_file_act</i></p>
<dd>This is an action that determines what response should be taken whenever a user accesses a file that is being watched. The default is <i>idmef</i>.</p>
<dt><i>detect_watched_exec</i></p>
<dd>This is an enabler that determines if the IDS should be detecting whenever a user executes a program that is being watched. The default is <i>yes</i>.</p>
<dt><i>watched_exec_act</i></p>
<dd>This is an action that determines what response should be taken whenever a user executes a program that is being watched. The default is <i>idmef</i>.</p>
<dt><i>detect_watched_mk_exe</i></p>
<dd>This is an enabler that determines if the IDS should be detecting whenever a user creates a file that is executable. The default is <i>yes</i>.</p>
<dt><i>watched_mk_exe_act</i></p>
<dd>This is an action that determines what response should be taken whenever a user creates a file that is executable. The default is <i>idmef</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-audispd/">audispd</a></code>(8),<code><a href="/docs/linux/man/8-audisp-prelude/">audisp-prelude</a>(8),</code><a href="/docs/linux/man/1-prelude-manager/">prelude-manager</a><code>(1)</code></p>
<h2>Author</h2>
<p>Steve Grubb</p>
