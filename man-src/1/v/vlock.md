---
title: "vlock(1)"
name: "vlock"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vlock/"
description: "vlock – Virtual Console lock program"
---

<h2 class="name">NAME</h2>
<p> vlock &#8211; Virtual Console lock program </p>
<h2>SYNOPSIS</h2>
<p> <code>vlock [ -hv ]</code> </p>
<p> <code>vlock [ -acns ] [ -t &lt;timeout&gt; ] [ plugins&#8230; ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>vlock</code> is a program to lock one or more sessions on the Linux console. This is especially useful for Linux machines which have multiple users with access to the console. One user may lock his or her session(s) while still allowing other users to use the system on other virtual consoles. If desired, the entire console may be locked and virtual console switching disabled. </p>
<p> By default, only the current VC (virtual console) is locked. With the <code>-a,&#8211;all</code> option all VCs are locked. The locked VCs cannot be unlocked without the invoker&#8217;s password or the root password. The root password will always be able to unlock any or all sessions, unless disabled at compile time. </p>
<p> Please note that it is entirely possible to completely lock yourself out of the console with the <code>-a,&#8211;all</code> option if you cannot remember your password! Unless you are able to kill vlock by logging in remotely via a serial terminal or network, a hard reset is the only method of &#8220;unlocking&#8221; the display. </p>
<p> When locking the entire console display it is sometimes still possible to kill vlock using the Secure Access Key (SAK) or other commands that are available through the SysRq mechanism. When the <code>-s,&#8211;disable-sysrq</code> and <code>-a,&#8211;all</code> options are given the SysRq mechanism is disabled while vlock is running. See /usr/src/linux/Documentation/sysrq.txt for more details. </p>
<p> vlock works for console sessions primarily. To lock the entire console display from an X session use the <code>-n,&#8211;new</code> option. This will make vlock switch to an empty virtual console to lock the display. </p>
<p> The options <code>-n,&#8211;new</code>, <code>-s,&#8211;disable-sysrq</code>, and <code>-t,&#8211;timeout</code> only work if vlock is compiled with plugin support. See the PLUGINS section for more information.</p>
<h2>OPTIONS</h2>
<p> <code>-a,&#8211;all</code></p>
<dl>
<dt>
<dd> Lock all console sessions and disable VC switching.</dl>
<p> <code>-c,&#8211;current</code></p>
<dl>
<dt>
<dd> Lock the current session (this is the default).</dl>
<p> <code>-n,&#8211;new</code></p>
<dl>
<dt>
<dd> Switch to a new virtual console before locking all console sessions.</dl>
<p> <code>-s,&#8211;disable-sysrq</code></p>
<dl>
<dt>
<dd> Disable the SysRq mechanism while consoles are locked. This option only works if the <code>-a,&#8211;all</code> option given.</dl>
<p> <code>-t,&#8211;timeout &lt;seconds&gt;</code></p>
<dl>
<dt>
<dd> Specify the timeout for the screensaver plugins. See <a href="/docs/linux/man/5-vlock-plugins/">vlock-plugins</a>(5) for more information.</dl>
<p> <code>-h,&#8211;help</code></p>
<dl>
<dt>
<dd> Print a brief help message.</dl>
<p> <code>-v,&#8211;version</code></p>
<dl>
<dt>
<dd> Print the version number.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables can be used to change vlock&#8217;s behavior: </p>
<p> <code>USER</code></p>
<dl>
<dt>
<dd> If this variable is when <code>vlock</code> is run as root (uid 0) vlock locks the screen as this user instead of root. The root password will still be able to unlock the session, unless disabled at compile time.</dl>
<p> <code>VLOCK_ALL_MESSAGE</code></p>
<dl>
<dt>
<dd> If this variable is set and all consoles are locked its contents will be used as the locking message instead of the default message.</dl>
<p> <code>VLOCK_CURRENT_MESSAGE</code></p>
<dl>
<dt>
<dd> If this variable is set and only the current consoles is locked its contents will be used as the locking message instead of the default message.</dl>
<p> <code>VLOCK_MESSAGE</code></p>
<dl>
<dt>
<dd> If this variable is set its contents will be used as the locking message instead of the default. This overrides the former two variables.</dl>
<p> <code>VLOCK_PLUGINS</code></p>
<dl>
<dt>
<dd> If this variable is set it is interpreted as a space separated list of plugins that will be loaded when vlock starts additionally to the ones listed on the command line.</dl>
<p> <code>VLOCK_TIMEOUT</code></p>
<dl>
<dt>
<dd> Set this variable to specify the timeout (in seconds) after which the screen saver plugins (if any) will be invoked. If this variable is unset or set to an invalid value or 0 no timeout is used. See <a href="/docs/linux/man/5-vlock-plugins/">vlock-plugins</a>(5) for more information about plugins.</dl>
<p> <code>VLOCK_PROMPT_TIMEOUT</code></p>
<dl>
<dt>
<dd> Set this variable to specify the amount of time (in seconds) you will have to enter your password at the password prompt. If this variable is unset or set to an invalid value or 0 no timeout is used. <code>Warning</code>: If this value is too low, you may not be able to unlock your session.</dl>
<h2>FILES</h2>
<p> <code>~/.vlockrc</code></p>
<dl>
<dt>
<dd> This file is read by <code>vlock</code> on startup if it exists. All the variables mentioned above can be set here.</dl>
<h2>SECURITY</h2>
<p> See the SECURITY file in the <code>vlock</code> distribution for more information. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-vlock-main/">vlock-main</a></code>(8), <code><a href="/docs/linux/man/5-vlock-plugins/">vlock-plugins</a></code>(5)</p>
<h2>AUTHORS</h2>
<p> Michael K. Johnson &lt;<a rel="nofollow" href="http://danlj.org/mkj/">http://danlj.org/mkj/</a>&gt; </p>
<p> Frank Benkstein &lt;frank-vlock [at] benkstein.net&gt; </p>
<h2>Index</h2>
