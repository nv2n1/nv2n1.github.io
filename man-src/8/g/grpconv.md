---
title: "grpconv(8)"
name: "grpconv"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grpconv/"
description: "pwconv, pwunconv, grpconv, grpunconv – convert to and from shadow passwords and groups"
---

<p>pwconv, pwunconv, grpconv, grpunconv &#8211; convert to and from shadow passwords and groups</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pwconv</code> [<i>options</i>]</p>
<dt> <code>pwunconv</code> [<i>options</i>]</p>
<dt> <code>grpconv</code> [<i>options</i>]</p>
<dt> <code>grpunconv</code> [<i>options</i>]</dl>
<h2>Description</h2>
<dd>The <code>pwconv</code> command creates <i>shadow</i> from <i>passwd</i> and an optionally existing <i>shadow</i>. </p>
<p> The <code>pwunconv</code> command creates <i>passwd</i> from <i>passwd</i> and <i>shadow</i> and then removes <i>shadow</i>. </p>
<p> The <code>grpconv</code> command creates <i>gshadow</i> from <i>group</i> and an optionally existing <i>gshadow</i>. </p>
<p> The <code>grpunconv</code> command creates <i>group</i> from <i>group</i> and <i>gshadow</i> and then removes <i>gshadow</i>. </p>
<p> These four programs all operate on the normal and shadow password and group files: /etc/passwd, /etc/group, /etc/shadow, and /etc/gshadow. </p>
<p> Each program acquires the necessary locks before conversion. <code>pwconv</code> and <code>grpconv</code> are similar. First, entries in the shadowed file which don&#8217;t exist in the main file are removed. Then, shadowed entries which don&#8217;t have `x&#8217; as the password in the main file are updated. Any missing shadowed entries are added. Finally, passwords in the main file are replaced with `x&#8217;. These programs can be used for initial conversion as well to update the shadowed file if the main file is edited by hand. </p>
<p> <code>pwconv</code> will use the values of <i>PASS_MIN_DAYS</i>, <i>PASS_MAX_DAYS</i>, and <i>PASS_WARN_AGE</i> from /etc/login.defs when adding new entries to /etc/shadow. </p>
<p> Likewise <code>pwunconv</code> and <code>grpunconv</code> are similar. Passwords in the main file are updated from the shadowed file. Entries which exist in the main file but not in the shadowed file are left alone. Finally, the shadowed file is removed. Some password aging information is lost by <code>pwunconv</code>. It will convert what it can.</p>
<h2>Options</h2>
<p>The options which apply to the <code>pwconv</code>, <code>pwunconv</code>, <code>grpconv</code>, and <code>grpunconv</code> commands are: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dd>Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<h2>Bugs</h2>
<p>Errors in the password or group files (such as invalid or duplicate entries) may cause these programs to loop forever or fail in other strange ways. Please run <code>pwck</code> and <code>grpck</code> to correct any such errors before converting to or from shadow passwords or groups.</p>
<h2>Configuration</h2>
<p>The following configuration variable in /etc/login.defs changes the behavior of <code>grpconv</code> and <code>grpunconv</code>: </p>
<p> <code>MAX_MEMBERS_PER_GROUP</code> (number)</p>
<dl>
<dd>Maximum members per group entry. When the maximum is reached, a new group entry (line) is started in /etc/group (with the same name, same password, and same GID). </p>
<p> The default value is 0, meaning that there are no limits in the number of members in a group. </p>
<p> This feature (split group) permits to limit the length of lines in the group file. This is useful to make sure that lines for NIS groups are not larger than 1024 characters. </p>
<p> If you need to enforce such limit, you can use 25. </p>
<p> Note: split groups may not be supported by all tools (even in the Shadow toolsuite). You should not use this variable unless you really need it.</dl>
<p> The following configuration variables in /etc/login.defs change the behavior of <code>pwconv</code>: </p>
<p> <code>PASS_MAX_DAYS</code> (number)</p>
<dl>
<dd>The maximum number of days a password may be used. If the password is older than this, a password change will be forced. If not specified, -1 will be assumed (which disables the restriction).</dl>
<p> <code>PASS_MIN_DAYS</code> (number)</p>
<dl>
<dd>The minimum number of days allowed between password changes. Any password changes attempted sooner than this will be rejected. If not specified, -1 will be assumed (which disables the restriction).</dl>
<p> <code>PASS_WARN_AGE</code> (number)</p>
<dl>
<dd>The number of days warning given before a password expires. A zero means warning is given only upon the day of expiration, a negative value means no warning is given. If not specified, no warning will be provided.</dl>
<h2>Files</h2>
<p>/etc/login.defs</p>
<dl>
<dd>Shadow password suite configuration.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-grpck/">grpck</a></code>(8), <code><a href="/docs/linux/man/5-login-defs/">login.defs</a></code>(5), <code><a href="/docs/linux/man/8-pwck/">pwck</a></code>(8). </p>
