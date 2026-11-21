---

title: "slimlock(1)"
name: "slimlock"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slimlock/"
description: "slimlock – Unholy Screen Locker"
---

<p> <code>slimlock</code> &#8211; Unholy Screen Locker</p>
<h2>SYNOPSIS</h2>
<pre>
<code>slimlock</code> [-v]
</pre>
<h2>DESCRIPTION</h2>
<p> The Frankenstein&#8217;s monster of screen lockers. Grafting SLiM and slock together leads to blood, tears, and locked screens.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></dt>
<dd> display version information</dd></dl>
<h2>CONFIGURATION</h2>
<p> Slimlock reads the same configuration files you use for SLiM. It looks in <i>CFGDIR/slim.conf</i> and <i>CFGDIR/slimlock.conf</i>, where <i>CFGDIR</i> is defined in the makefile. The options that are read from slim.conf are hidecursor, current_theme, background_color, and background_style, screenshot_cmd, and welcome_msg. See the SLiM docs for more information. </p>
<p> slimlock.conf contains the following settings: </p>
<dl>
<dt><code>dpms_standby_timeout</code></dt>
<dd> number of seconds of inactivity before the screen blanks. <code>Default: </code><i>60</i></dd>
<dt><code>dpms_off_timeout</code></dt>
<dd> number of seconds of inactivity before the screen is turned off. <code>Default: </code><i>600</i></dd>
<dt><code>wrong_passwd_timeout</code></dt>
<dd> delay in seconds after an incorrect password is entered. <code>Default: </code><i>2</i></dd>
<dt><code>passwd_feedback_msg</code></dt>
<dd> message to display after a failed authentication attempt. <code>Default: </code><i>Authentication failed</i></dd>
<dt><code>passwd_feedback_capslock</code></dt>
<dd> message to display after a failed authentication attempt if the CapsLock is on. <code>Default: </code><i>Authentication failed (CapsLock is on)</i></dd>
<dt><code>show_username</code></dt>
<dd> 1 to show username on themes with single input field; 0 to disable. <code>Default: </code><i>1</i></dd>
<dt><code>show_welcome_msg</code></dt>
<dd> 1 to show SLiM&#8217;s welcome message; 0 to disable. <code>Default: </code><i>0</i></dd>
<dt><code>tty_lock</code></dt>
<dd> 1 to disallow virtual terminals switching; 0 to allow. <code>Default: </code><i>1</i></dd>
<dt><code>bell</code></dt>
<dd> 1 to enable the bell on authentication failure; 0 to disable. <code>Default: </code><i>1</i></dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-slim/">slim</a></code>(1) </p>
