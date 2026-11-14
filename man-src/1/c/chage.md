---
title: "chage(1)"
name: "chage"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chage/"
description: "chage – change user password expiry information"
---

<h2 class="name">NAME</h2>
<p> chage &#8211; change user password expiry information </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>chage</code> [<i>options</i>] <i>LOGIN</i></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>chage</code> command changes the number of days between password changes and the date of the last password change. This information is used by the system to determine when a user must change their password.</p>
<h2>OPTIONS</h2>
<p> The options which apply to the <code>chage</code> command are: </p>
<p> <code>-d</code>, <code>&#8211;lastday</code>&nbsp;<i>LAST_DAY</i></p>
<dl>
<dt>
<dd> Set the number of days since January 1st, 1970 when the password was last changed. The date may also be expressed in the format YYYY-MM-DD (or the format more commonly used in your area).</dl>
<p> <code>-E</code>, <code>&#8211;expiredate</code>&nbsp;<i>EXPIRE_DATE</i></p>
<dl>
<dt>
<dd> Set the date or number of days since January 1, 1970 on which the user&#8217;s account will no longer be accessible. The date may also be expressed in the format YYYY-MM-DD (or the format more commonly used in your area). A user whose account is locked must contact the system administrator before being able to use the system again. </p>
<p> Passing the number <i>-1</i> as the <i>EXPIRE_DATE</i> will remove an account expiration date.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help message and exit.</dl>
<p> <code>-i</code>, <code>&#8211;iso8601</code></p>
<dl>
<dt>
<dd> When printing dates, use YYYY-MM-DD format.</dl>
<p> <code>-I</code>, <code>&#8211;inactive</code>&nbsp;<i>INACTIVE</i></p>
<dl>
<dt>
<dd> Set the number of days of inactivity after a password has expired before the account is locked. The <i>INACTIVE</i> option is the number of days of inactivity. A user whose account is locked must contact the system administrator before being able to use the system again. </p>
<p> Passing the number <i>-1</i> as the <i>INACTIVE</i> will remove an account&#8217;s inactivity.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Show account aging information.</dl>
<p> <code>-m</code>, <code>&#8211;mindays</code>&nbsp;<i>MIN_DAYS</i></p>
<dl>
<dt>
<dd> Set the minimum number of days between password changes to <i>MIN_DAYS</i>. A value of zero for this field indicates that the user may change their password at any time.</dl>
<p> <code>-M</code>, <code>&#8211;maxdays</code>&nbsp;<i>MAX_DAYS</i></p>
<dl>
<dt>
<dd> Set the maximum number of days during which a password is valid. When <i>MAX_DAYS</i> plus <i>LAST_DAY</i> is less than the current day, the user will be required to change their password before being able to use their account. This occurrence can be planned for in advance by use of the <code>-W</code> option, which provides the user with advance warning. </p>
<p> Passing the number <i>-1</i> as <i>MAX_DAYS</i> will remove checking a password&#8217;s validity.</dl>
<p> <code>-R</code>, <code>&#8211;root</code>&nbsp;<i>CHROOT_DIR</i></p>
<dl>
<dt>
<dd> Apply changes in the <i>CHROOT_DIR</i> directory and use the configuration files from the <i>CHROOT_DIR</i> directory.</dl>
<p> <code>-W</code>, <code>&#8211;warndays</code>&nbsp;<i>WARN_DAYS</i></p>
<dl>
<dt>
<dd> Set the number of days of warning before a password change is required. The <i>WARN_DAYS</i> option is the number of days prior to the password expiring that a user will be warned their password is about to expire.</dl>
<p> If none of the options are selected, <code>chage</code> operates in an interactive fashion, prompting the user with the current values for all of the fields. Enter the new value to change the field, or leave the line blank to use the current value. The current value is displayed between a pair of <i>[ ]</i> marks.</p>
<h2>NOTE</h2>
<p> The <code>chage</code> program requires a shadow password file to be available. </p>
<p> The <code>chage</code> command is restricted to the root user, except for the <code>-l</code> option, which may be used by an unprivileged user to determine when their password or account is due to expire.</p>
<h2>CONFIGURATION</h2>
<p> The following configuration variables in /etc/login.defs change the behavior of this tool:</p>
<h2>FILES</h2>
<p> /etc/passwd</p>
<dl>
<dt>
<dd> User account information.</dl>
<p> /etc/shadow</p>
<dl>
<dt>
<dd> Secure user account information.</dl>
<h2>EXIT VALUES</h2>
<p> The <code>chage</code> command exits with the following values: </p>
<p> <i>0</i></p>
<dl>
<dt>
<dd> success</dl>
<p> <i>1</i></p>
<dl>
<dt>
<dd> permission denied</dl>
<p> <i>2</i></p>
<dl>
<dt>
<dd> invalid command syntax</dl>
<p> <i>15</i></p>
<dl>
<dt>
<dd> can&#8217;t find the shadow password file</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5). </p>
<h2>Index</h2>
