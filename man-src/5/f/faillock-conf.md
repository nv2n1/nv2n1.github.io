---
title: "faillock-conf(5)"
name: "faillock-conf"
section: "5"
letter: "f"
url: "/docs/linux/man/5-faillock-conf/"
description: "faillock.conf – pam_faillock configuration file"
---

<p>faillock.conf &#8211; pam_faillock configuration file</p>
<h2>Description</h2>
<p><code>faillock.conf</code> provides a way to configure the default settings for locking the user after multiple failed authentication attempts. This file is read by the <i>pam_faillock</i> module and is the preferred method over configuring <i>pam_faillock</i> directly. </p>
<p> The file has a very simple <i>name = value</i> format with possible comments starting with <i>#</i> character. The whitespace at the beginning of line, end of line, and around the <i>=</i> sign is ignored.</p>
<h2>Options</h2>
<p><code>dir=</code><i>/path/to/tally-directory</i></p>
<dl>
<dd>The directory where the user files with the failure records are kept. The default is /var/run/faillock.</dl>
<p> <code>audit</code></p>
<dl>
<dd>Will log the user name into the system log if the user is not found.</dl>
<p> <code>silent</code></p>
<dl>
<dd>Don&#8217;t print informative messages to the user. Please note that when this option is not used there will be difference in the authentication behavior for users which exist on the system and non-existing users.</dl>
<p> <code>no_log_info</code></p>
<dl>
<dd>Don&#8217;t log informative messages via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>local_users_only</code></p>
<dl>
<dd>Only track failed user authentications attempts for local users in /etc/passwd and ignore centralized (AD, IdM, LDAP, etc.) users. The <code><a href="/docs/linux/man/8-faillock/">faillock</a></code>(8) command will also no longer track user failed authentication attempts. Enabling this option will prevent a double-lockout scenario where a user is locked out locally and in the centralized mechanism.</dl>
<p> <code>deny=</code><i>n</i></p>
<dl>
<dd>Deny access if the number of consecutive authentication failures for this user during the recent interval exceeds <i>n</i>. The default is 3.</dl>
<p> <code>fail_interval=</code><i>n</i></p>
<dl>
<dd>The length of the interval during which the consecutive authentication failures must happen for the user account lock out is <i>n</i> seconds. The default is 900 (15 minutes).</dl>
<p> <code>unlock_time=</code><i>n</i></p>
<dl>
<dd>The access will be re-enabled after <i>n</i> seconds after the lock out. The value 0 has the same meaning as value <i>never</i> &#8211; the access will not be re-enabled without resetting the faillock entries by the <code><a href="/docs/linux/man/8-faillock/">faillock</a></code>(8) command. The default is 600 (10 minutes). </p>
<p> Note that the default directory that <i>pam_faillock</i> uses is usually cleared on system boot so the access will be also re-enabled after system reboot. If that is undesirable a different tally directory must be set with the <code>dir</code> option. </p>
<p> Also note that it is usually undesirable to permanently lock out users as they can become easily a target of denial of service attack unless the usernames are random and kept secret to potential attackers.</dl>
<p> <code>even_deny_root</code></p>
<dl>
<dd>Root account can become locked as well as regular accounts.</dl>
<p> <code>root_unlock_time=</code><i>n</i></p>
<dl>
<dd>This option implies <code>even_deny_root</code> option. Allow access after <i>n</i> seconds to root account after the account is locked. In case the option is not specified the value is the same as of the <code>unlock_time</code> option.</dl>
<p> <code>admin_group=</code><i>name</i></p>
<dl>
<dd>If a group name is specified with this option, members of the group will be handled by this module the same as the root account (the options <code>even_deny_root</code> and <code>root_unlock_time</code> will apply to them. By default the option is not set.</dl>
<h2>Examples</h2>
<p>/etc/security/faillock.conf file example: </p>
<dl>
<dd>
<pre>deny=4
unlock_time=1200
silent</pre>
</dl>
<h2>Files</h2>
<p>/etc/security/faillock.conf</p>
<dl>
<dd>the config file for custom options</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-faillock/">faillock</a></code>(8), <code><a href="/docs/linux/man/8-pam_faillock/">pam_faillock</a></code>(8), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Author</h2>
<p>pam_faillock was written by Tomas Mraz. The support for faillock.conf was written by Brian Ward.</p>
