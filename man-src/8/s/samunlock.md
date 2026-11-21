---
title: "samunlock(8)"
name: "samunlock"
section: "8"
letter: "s"
url: "/docs/linux/man/8-samunlock/"
description: "samunlock – unlock users in the SAM user database"
---

<p>samunlock &#8211; unlock users in the SAM user database</p>
<h2>Synopsis</h2>
<p><code>samunlock</code> [<i>options</i>] -u<i>user</i> &lt;<i>samfile</i>&gt;</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>samunlock</code> command. <code>samunlock</code> is a non-interactive command line utility that can unlock a user and/or the user&#8217;s account bits from the SAM user database file of a Microsoft Windows system (Windows NT, 2000, XP, Vista, 7, 8.1, etc.). This file is usually located at \WINDOWS\system32\config\SAM on the file system of a Microsoft Windows Operating System </p>
<p> On success, the program does not output any informatin and the exit code is 0. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> <p> Show summary of options. </p>
 </dd>
<dt><code>-U</code></dt>
<dd> <p> Unlock the user. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Unlock all the users. If this option is used there is no need to specify the next option. </p>
 </dd>
<dt><code>-u &lt;user&gt;</code></dt>
<dd> <p> User to unlock. The user value can be provided as a username, or a RID number in hexadecimal (if the username is preceded with &#8216;0x&#8217;). Usernames including international characters will probably not work. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Lists the users in the SAM database. </p>
 </dd>
<dt><code>-H</code></dt>
<dd> <p> Output human readable output. The program by default will print a parsable table unless this option is used. </p>
 </dd>
<dt><code>-N</code></dt>
<dd> <p> Do not allocate more information, only allow the editing of existing values with same size. </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> Do not expand the hive file (safe mode). </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> Print debug information of allocated blocks. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Print verbose information and debug messages. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>samunlock -U -u theboss</code></dt>
<dd> <p> Unlock an user named &#8216;theboss&#8217;, if found. </p>
 </dd>
<dt><code>samunlock -U -u 0x3ea</code></dt>
<dd> <p> Unlock an user with RID &#8216;0x3a&#8217;. </p>
 </dd></dl>
<h2>KNOWN BUGS</h2>
<p> If the username includes international (non-ASCII) characters the program will not (usually) find it. Use the RID number instead. </p>
<h2>SEE ALSO</h2>
<p> <code>chntpwd, reged, samusrgrp</code> <br />
 You will find more information available on how this program works, in the text files <i>/usr/share/doc/chntpw/README.txt</i> and <i>/usr/share/doc/chntpw/MANUAL.txt</i> </p>
<p> More documentation is available at the non upstream&#8217;s author site: <code><a rel="nofollow" href="https://github.com/rescatux/chntpw">https://github.com/rescatux/chntpw</a></code> </p>
<h2>AUTHOR</h2>
<p> This program was written by Adrian Gibanel Lopez. </p>
<p> This manual page was written by Adrian Gibanel Lopez &lt;adrian15sgd [at] gmail.com&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
