---
title: "lslogins(1)"
name: "lslogins"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lslogins/"
description: "lslogins – display information about known users in the system"
---

<h2 class="name">NAME</h2>
<p> lslogins &#8211; display information about known users in the system </p>
<h2>SYNOPSIS</h2>
<p> <code>lslogins</code> [options] [<code>-s</code>|<code>-u</code>[=<i>UID</i>]] [<code>-g</code> <i>groups</i>] [<code>-l</code> <i>logins</i>] [<i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> Examine the wtmp and btmp logs, <i>/etc/shadow</i> (if necessary) and <i>/passwd</i> and output the desired data. </p>
<p> The optional argument <i>username</i> forces <code>lslogins</code> to print all available details about the specified user only. In this case the output format is different than in case of <code>-l</code> or <code>-g</code> and unknown is <i>username</i> reported as an error. </p>
<p> The default action is to list info about all the users in the system.</p>
<h2>OPTIONS</h2>
<p> Mandatory arguments to long options are mandatory for short options too. </p>
<p> <code>-a</code>, <code>&#8211;acc-expiration</code></p>
<dl>
<dt>
<dd> Display data about the date of last password change and the account expiration date (see <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5) for more info). (Requires root privileges.)</dl>
<p> <code>&#8211;btmp-file</code> <i>path</i></p>
<dl>
<dt>
<dd> Alternate path for btmp.</dl>
<p> <code>-c</code>, <code>&#8211;colon-separate</code></p>
<dl>
<dt>
<dd> Separate info about each user with a colon instead of a newline.</dl>
<p> <code>-e</code>, <code>&#8211;export</code></p>
<dl>
<dt>
<dd> Output data in the format of NAME=VALUE.</dl>
<p> <code>-f</code>, <code>&#8211;failed</code></p>
<dl>
<dt>
<dd> Display data about the users&#8217; last failed login attempts.</dl>
<p> <code>-G</code>, <code>&#8211;supp-groups</code></p>
<dl>
<dt>
<dd> Show information about supplementary groups.</dl>
<p> <code>-g</code>, <code>&#8211;groups</code>=<i>groups</i></p>
<dl>
<dt>
<dd> Only show data of users belonging to <i>groups</i>. More than one group may be specified; the list has to be comma-separated. Unknown group names are ignored. </p>
<p> Note that relation between user and group may be invisible for primary group if the user is not explicitly specify as group member (e.g., in <i>/etc/group</i>). If the command <code>lslogins</code> scans for groups than it uses groups database only, and user database with primary GID is not used at all.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help information and exit.</dl>
<p> <code>-L</code>, <code>&#8211;last</code></p>
<dl>
<dt>
<dd> Display data containing information about the users&#8217; last login sessions.</dl>
<p> <code>-l</code>, <code>&#8211;logins</code>=<i>logins</i></p>
<dl>
<dt>
<dd> Only show data of users with a login specified in <i>logins</i> (user names or user IDS). More than one login may be specified; the list has to be comma-separated. Unknown login names are ignored.</dl>
<p> <code>-n</code>, <code>&#8211;newline</code></p>
<dl>
<dt>
<dd> Display each piece of information on a separate line.</dl>
<p> <code>&#8211;noheadings</code></p>
<dl>
<dt>
<dd> Do not print a header line.</dl>
<p> <code>&#8211;notruncate</code></p>
<dl>
<dt>
<dd> Don&#8217;t truncate output.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dt>
<dd> Specify which output columns to print. The default list of columns may be extended if <i>list</i> is specified in the format <i>+list</i>.</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dt>
<dd> Output all available columns. <code>&#8211;help</code> to get a list of all supported columns.</dl>
<p> <code>-p</code>, <code>&#8211;pwd</code></p>
<dl>
<dt>
<dd> Display information related to login by password (see also <code>-afL).</code></dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dt>
<dd> Raw output (no columnation).</dl>
<p> <code>-s</code>, <code>&#8211;system-accs</code></p>
<dl>
<dt>
<dd> Show system accounts. These are by default all accounts with a UID between 101 and 999 (inclusive), with the exception of either nobody or nfsnobody (UID 65534). This hardcoded default may be overwritten by parameters SYS_UID_MIN and SYS_UID_MAX in the file <i>/etc/login.defs</i>.</dl>
<p> <code>&#8211;time-format</code> <i>type</i></p>
<dl>
<dt>
<dd> Display dates in short, full or iso format. The default is short, this time format is designed to be space efficient and human readable.</dl>
<p> <code>-u</code>, <code>&#8211;user-accs</code></p>
<dl>
<dt>
<dd> Show user accounts. These are by default all accounts with UID above 1000 (inclusive), with the exception of either nobody or nfsnobody (UID 65534). This hardcoded default maybe overwritten by parameters UID_MIN and UID_MAX in the file <i>/etc/login.defs</i>.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>&#8211;wtmp-file</code> <i>path</i></p>
<dl>
<dt>
<dd> Alternate path for wtmp.</dl>
<p> <code>&#8211;lastlog</code> <i>path</i></p>
<dl>
<dt>
<dd> Alternate path for <code><a href="/docs/linux/man/8-lastlog/">lastlog</a></code>(8).</dl>
<p> <code>-Z</code>, <code>&#8211;context</code></p>
<dl>
<dt>
<dd> Display the users&#8217; security context.</dl>
<p> <code>-z</code>, <code>&#8211;print0</code></p>
<dl>
<dt>
<dd> Delimit user entries with a nul character, instead of a newline.</dl>
<h2>EXIT STATUS</h2>
<p> 0</p>
<dl>
<dt>
<dd> if OK,</dl>
<p> 1</p>
<dl>
<dt>
<dd> if incorrect arguments specified,</dl>
<p> 2</p>
<dl>
<dt>
<dd> if a serious error occurs (e.g., a corrupt log).</dl>
<h2>NOTES</h2>
<p> The default UID thresholds are read from <i>/etc/login.defs</i>.</p>
<h2>HISTORY</h2>
<p> The <code>lslogins</code> utility is inspired by the <code>logins</code> utility, which first appeared in FreeBSD 4.10.</p>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-group/">group</a></code>(5), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5), <code><a href="/docs/linux/man/5-utmp/">utmp</a></code>(5)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>lslogins</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
