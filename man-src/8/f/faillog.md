---
title: "faillog(8)"
name: "faillog"
section: "8"
letter: "f"
url: "/docs/linux/man/8-faillog/"
description: "faillog – display faillog records or set login failure limits"
---

<p>faillog &#8211; display faillog records or set login failure limits</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>faillog</code> [<i>options</i>]</dl>
<h2>Description</h2>
<p><code>faillog</code></p>
<dd>displays the contents of the failure log database (/var/log/faillog). It can also set the failure counters and limits. When <code>faillog</code> is run without arguments, it only displays the faillog records of the users who had a login failure.</p>
<h2>Options</h2>
<p>The options which apply to the <code>faillog</code> command are: </p>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dd>Display (or act on) faillog records for all users having an entry in the faillog database. </p>
<p> The range of users can be restricted with the <code>-u</code> option. </p>
<p> In display mode, this is still restricted to existing users but forces the display of the faillog entries even if they are empty. </p>
<p> With the <code>-l</code>, <code>-m</code>, <code>-r</code>, <code>-t</code> options, the users&#8217; records are changed, even if the user does not exist on the system. This is useful to reset records of users that have been deleted or to set a policy in advance for a range of users.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-l</code>, <code>&#8211;lock-secs</code>&nbsp;<i>SEC</i></p>
<dl>
<dd>Lock account for <i>SEC</i> seconds after failed login. </p>
<p> Write access to /var/log/faillog is required for this option.</dl>
<p> <code>-m</code>, <code>&#8211;maximum</code>&nbsp;<i>MAX</i></p>
<dl>
<dd>Set the maximum number of login failures after the account is disabled to <i>MAX</i>. </p>
<p> Selecting a <i>MAX</i> value of 0 has the effect of not placing a limit on the number of failed logins. </p>
<p> The maximum failure count should always be 0 for <i>root</i> to prevent a denial of services attack against the system. </p>
<p> Write access to /var/log/faillog is required for this option.</dl>
<p> <code>-r</code>, <code>&#8211;reset</code></p>
<dl>
<dd>Reset the counters of login failures. </p>
<p> Write access to /var/log/faillog is required for this option.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-t</code>, <code>&#8211;time</code>&nbsp;<i>DAYS</i></p>
<dl>
<dd>Display faillog records more recent than <i>DAYS</i>.</dl>
<p> <code>-u</code>, <code>&#8211;user</code>&nbsp;<i>LOGIN</i>|<i>RANGE</i></p>
<dl>
<dd>Display faillog record or maintains failure counters and limits (if used with <code>-l</code>, <code>-m</code> or <code>-r</code> options) only for the specified user(s). </p>
<p> The users can be specified by a login name, a numerical user ID, or a <i>RANGE</i> of users. This <i>RANGE</i> of users can be specified with a min and max values (<i>UID_MIN-UID_MAX</i>), a max value (<i>-UID_MAX</i>), or a min value (<i>UID_MIN-</i>).</dl>
<p> When none of the <code>-l</code>, <code>-m</code>, or <code>-r</code> options are used, <code>faillog</code> displays the faillog record of the specified user(s).</p>
<h2>Caveats</h2>
<p><code>faillog</code> only prints out users with no successful login since the last failure. To print out a user who has had a successful login since their last failure, you must explicitly request the user with the <code>-u</code> flag, or print out all users with the <code>-a</code> flag.</p>
<h2>Files</h2>
<p>/var/log/faillog</p>
<dl>
<dd>Failure logging file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/5-faillog/">faillog</a></code>(5). </p>
