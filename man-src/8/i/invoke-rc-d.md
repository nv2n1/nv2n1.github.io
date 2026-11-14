---
title: "invoke-rc-d(8)"
name: "invoke-rc-d"
section: "8"
letter: "i"
url: "/docs/linux/man/8-invoke-rc-d/"
description: "invoke-rc.d – executes System-V style init script actions"
---

<p>invoke-rc.d &#8211; executes System-V style init script actions</p>
<h2>Synopsis</h2>
<p><code>invoke-rc.d</code> [<i>&#8211;quiet</i>] [<i>&#8211;force</i>] [<i>&#8211;try-anyway</i>] [<i>&#8211;disclose-deny</i>] [<i>&#8211;query</i>] [<i>&#8211;no-fallback</i>] <i>name</i> <i>action</i> [<i>init script parameters&#8230;</i>] </p>
<p> <code>invoke-rc.d</code> [<i>&#8211;help</i>]</p>
<h2>Description</h2>
<p><code>invoke-rc.d</code> is a generic interface to execute System V style init script <code>/etc/init.d/</code><i>name</i> actions, obeying runlevel constraints as well as any local policies set by the system administrator. </p>
<p> All access to the init scripts by Debian packages&#8217; maintainer scripts should be done through <code>invoke-rc.d</code>. </p>
<p> This manpage documents only the usage and behavior of <code>invoke-rc.d</code>. For a discussion of the System V style init script arrangements please see <code><a href="/docs/linux/man/8-init/">init</a></code>(8). More information on invoke-rc.d can be found in the section on runlevels and init.d scripts of the <i>Debian Policy Manual</i>.</p>
<h2>Init Script Actions</h2>
<p>The standard actions are: <i>start</i>, <i>stop</i>, <i>force-stop</i>, <i>restart</i>, <i>try-restart</i>, <i>reload</i>, <i>force-reload</i>, and <i>status</i>. Other actions are accepted, but they can cause problems to <code>policy-rc.d</code> (see the <code>INIT SCRIPT POLICY</code> section), so warnings are generated if the policy layer is active. </p>
<p> Please note that not all init scripts will implement all the actions listed above, and that the policy layer may override an action to another action(s), or even deny it. </p>
<p> Any extra parameters will be passed to the init script(s) being executed. </p>
<p> If an action must be carried out regardless of any local policies, use the <i>&#8211;force</i> switch.</p>
<h2>Options</h2>
<dl>
<dt><i>&#8211;help</i></p>
<dd>Display usage help.</p>
<dt><i>&#8211;quiet</i></p>
<dd>Quiet mode, no error messages are generated.</p>
<dt><i>&#8211;force</i></p>
<dd>Tries to run the init script regardless of policy and init script subsystem errors. <code>Use of this option in Debian maintainer scripts is severely discouraged.</code></p>
<dt><i>&#8211;try-anyway</i></p>
<dd>Tries to run the init script if a non-fatal error is detected.</p>
<dt><i>&#8211;disclose-deny</i></p>
<dd>Return status code 101 instead of status code 0 if the init script action is denied by the policy layer.</p>
<dt><i>&#8211;query</i></p>
<dd>Returns one of the status codes 100-106. Does not run the init script, and implies <i>&#8211;disclose-deny</i> and <i>&#8211;no-fallback</i>.</p>
<dt><i>&#8211;no-fallback</i></p>
<dd>Ignores any fallback action requests by the policy layer. <code>Warning:</code> this is usually a very bad idea for any actions other than start.</p>
<dt><i>&#8211;skip-systemd-native</i></p>
<dd>Exits before doing anything if a systemd environment is detected and the requested service is a native systemd unit. This is useful for maintainer scripts that want to defer systemd actions to <code><a href="//www.systutorials.com/docs/linux/man/1p-deb-systemd-invoke/">deb-systemd-invoke</a></code>(1p)</dl>
<h2>Status Codes</h2>
<p>Should an init script be executed, <code>invoke-rc.d</code> always returns the status code returned by the init script. Init scripts should not return status codes in the 100+ range (which is reserved in Debian and by the LSB). The status codes returned by invoke-rc.d proper are:</p>
<dl>
<dt><code>0</code></p>
<dd><i>Success</i>. Either the init script was run and returned exit status 0 (note that a fallback action may have been run instead of the one given in the command line), or it was not run because of runlevel/local policy constrains and <code>&#8211;disclose-deny</code> is not in effect.</p>
<dt><code>1 &#8211; 99</code></p>
<dd>Reserved for init.d script, usually indicates a failure.</p>
<dt><code>100</code></p>
<dd><code>Init script ID (</code><i>name</i><code>) unknown.</code> This means the init script was not registered successfully through <code>update-rc.d</code> or that the init script does not exist.</p>
<dt><code>101</code></p>
<dd><code>Action not allowed</code>. The requested action will not be performed because of runlevel or local policy constraints.</p>
<dt><code>102</code></p>
<dd><code>Subsystem error</code>. Init script (or policy layer) subsystem malfunction. Also, forced init script execution due to <i>&#8211;try-anyway</i> or <i>&#8211;force</i> failed.</p>
<dt><code>103</code></p>
<dd><i>Syntax error.</i></p>
<dt><code>104</code></p>
<dd><i>Action allowed</i>. Init script would be run, but <code>&#8211;query</code> is in effect.</p>
<dt><code>105</code></p>
<dd><i>Behavior uncertain</i>. It cannot be determined if action should be carried out or not, and <code>&#8211;query</code> is in effect.</p>
<dt><code>106</code></p>
<dd><i>Fallback action requested</i>. The policy layer denied the requested action, and supplied an allowed fallback action to be used instead.</dl>
<h2>Init Script Policy</h2>
<p><code>invoke-rc.d</code> introduces the concept of a policy layer which is used to verify if an init script should be run or not, or if something else should be done instead. This layer has various uses, the most immediate ones being avoiding that package upgrades start daemons out-of-runlevel, and that a package starts or stops daemons while inside a chroot jail. </p>
<p> The policy layer has the following abilities: deny or approve the execution of an action; request that another action (called a <i>fallback</i>) is to be taken, instead of the action requested in invoke-rc.d&#8217;s command line; or request multiple actions to be tried in order, until one of them succeeds (a multiple <i>fallback</i>). </p>
<p> <code>invoke-rc.d</code> itself only pays attention to the current runlevel; it will block any attempts to start a service in a runlevel in which the service is disabled. Other policies are implemented with the use of the <code>policy-rc.d</code> helper, and are only available if <code>/usr/sbin/policy-rc.d</code> is installed in the system.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/init.d/*</code></p>
<dd>System V init scripts.</p>
<dt><code>/usr/sbin/policy-rc.d</code></p>
<dd>Init script policy layer helper (not required).</p>
<dt><code>/etc/rc?.d/*</code></p>
<dd>System V runlevel configuration.</dl>
<h2>Notes</h2>
<p><code>invoke-rc.d</code> special cases the <i>status</i> action, and returns exit status 4 instead of exit status 0 when it is denied.</p>
<h2>Bugs</h2>
<p>See <i><a rel="nofollow" href="http://bugs.debian.org/sysv-rc">http://bugs.debian.org/sysv-rc</a></i> and <i><a rel="nofollow" href="http://bugs.debian.org/init-system-helpers">http://bugs.debian.org/init-system-helpers</a></i>.</p>
<h2>See Also</h2>
<pre><i>Debian Policy manual</i>,
<code>/etc/init.d/skeleton</code>,
<code><a href="//www.systutorials.com/docs/linux/man/8-update-rc.d/">update-rc.d</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-init/">init</a></code>(8),
<code>/usr/share/doc/init-system-helpers/README.policy-rc.d.gz</code></pre>
<h2>Author</h2>
<p>Henrique de Moraes Holschuh </p>
<p> License: GNU General Public License v2 or Later (GPLv2+)</p>
<h2>Copyright</h2>
<p>2001 Henrique de Moraes Holschuh</p>
