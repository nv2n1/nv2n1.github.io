---
title: "finger(1)"
name: "finger"
section: "1"
letter: "f"
url: "/docs/linux/man/1-finger/"
description: "finger – user information lookup program"
---

<h2 class="name">NAME</h2>
<p> <code>finger</code> &#8211; user information lookup program </p>
<h2>SYNOPSIS</h2>
<p> <code>finger</code> [-<code>lmsp</code> ] [<i>user &#8230;</i> ] [<i>user [at] host &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>finger</code> displays information about the system users. </p>
<p> Options are:</p>
<dl>
<dt><code>-s</code></p>
<dd> <code>Finger</code> displays the user&#8217;s login name, real name, terminal name and write status (as a &#8220;*&#8221; after the terminal name if write permission is denied), idle time, login time, office location and office phone number. </p>
<p> Login time is displayed as month, day, hours and minutes, unless more than six months ago, in which case the year is displayed rather than the hours and minutes. </p>
<p> Unknown devices as well as nonexistent idle and login times are displayed as single asterisks. </p>
<dt><code>-l</code></p>
<dd> Produces a multi-line format displaying all of the information described for the &#8211;<code>s</code> option as well as the user&#8217;s home directory, home phone number, login shell, mail status, and the contents of the files &#8220;.plan &#8221; &#8220;.project &#8221; &#8220;.pgpkey &#8221; and &#8220;.forward &#8221; from the user&#8217;s home directory. </p>
<p> Phone numbers specified as eleven digits are printed as &#8220;+N-NNN-NNN-NNNN&#8221;. Numbers specified as ten or seven digits are printed as the appropriate subset of that string. Numbers specified as five digits are printed as &#8220;xN-NNNN&#8221;. Numbers specified as four digits are printed as &#8220;xNNNN&#8221;. </p>
<p> If write permission is denied to the device, the phrase &#8220;(messages off)&#8221; is appended to the line containing the device name. One entry per user is displayed with the &#8211;<code>l</code> option; if a user is logged on multiple times, terminal information is repeated once per login. </p>
<p> Mail status is shown as &#8220;No Mail.&#8221; if there is no mail at all, &#8220;Mail last read DDD MMM ## HH:MM YYYY (TZ)&#8221; if the person has looked at their mailbox since new mail arriving, or &#8220;New mail received &#8230;&#8221;, &#8220; Unread since &#8230;&#8221; if they have new mail. </p>
<dt><code>-p</code></p>
<dd> Prevents the &#8211;<code>l</code> option of <code>finger</code> from displaying the contents of the &#8220;.plan &#8221; &#8220;.project &#8221; and &#8220;.pgpkey &#8221; files.</p>
<dt><code>-m</code></p>
<dd> Prevent matching of <i>user</i> names. <i>User</i> is usually a login name; however, matching will also be done on the users&#8217; real names, unless the &#8211;<code>m</code> option is supplied. All name matching performed by <code>finger</code> is case insensitive.</dl>
<p> If no options are specified, <code>finger</code> defaults to the &#8211;<code>l</code> style output if operands are provided, otherwise to the &#8211;<code>s</code> style. Note that some fields may be missing, in either format, if information is not available for them. </p>
<p> If no arguments are specified, <code>finger</code> will print an entry for each user currently logged into the system. </p>
<p> <code>Finger</code> may be used to look up users on a remote machine. The format is to specify a <i>user</i> as &#8220;<code>user [at] host</code> &#8221; or &#8220;<code>@host</code> &#8221; where the default output format for the former is the &#8211;<code>l</code> style, and the default output format for the latter is the &#8211;<code>s</code> style. The &#8211;<code>l</code> option is the only option that may be passed to a remote machine. </p>
<p> If standard output is a socket, <code>finger</code> will emit a carriage return (^M) before every linefeed (^J). This is for processing remote finger requests when invoked by <a href="/docs/linux/man/8-fingerd/">fingerd</a>(8).</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.nofinger </code></p>
<dd> If finger finds this file in a user&#8217;s home directory, it will, for finger requests originating outside the local host, firmly deny the existence of that user. For this to work, the finger program, as started by <a href="/docs/linux/man/8-fingerd/">fingerd</a>(8), must be able to see the .nofinger file. This generally means that the home directory containing the file must have the other-users-execute bit set (o+x). See <a href="/docs/linux/man/1-chmod/">chmod</a>(1). If you use this feature for privacy, please test it with &#8220;finger @localhost&#8221; before relying on it, just in case.</p>
<dt><code>~/.plan</code></p>
<dd>
<dt><code>~/.project</code></p>
<dd>
<dt><code>~/.pgpkey</code></p>
<dd> These files are printed as part of a long-format request. The .project file is limited to one line; the .plan file may be arbitrarily long.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-chfn/">chfn</a>(1), <a href="/docs/linux/man/1-passwd/">passwd</a>(1), <a href="/docs/linux/man/1-w/">w</a>(1), <a href="/docs/linux/man/1-who/">who</a>(1)</p>
<h2>HISTORY</h2>
<p> The <code>finger</code> command appeared in BSD 3.0 </p>
<h2>Index</h2>
