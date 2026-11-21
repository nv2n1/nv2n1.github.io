---
title: "sampasswd(8)"
name: "sampasswd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sampasswd/"
description: "sampasswd – reset passwords of users in the SAM user database"
---

<p>sampasswd &#8211; reset passwords of users in the SAM user database</p>
<h2>Synopsis</h2>
<p><code>sampasswd</code> [<i>options</i>] -u<i>user</i> &lt;<i>samfile</i>&gt;</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>sampasswd</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page. <code>sampasswd</code> is a non-interactive command line utility that can reset a user&#8217;s password and/or the user&#8217;s account bits from the SAM user database file of a Microsoft Windows system (Windows NT, 2000, XP, Vista, 7, 8.1, etc.). This file is usually located at \WINDOWS\system32\config\SAM on the file system of a Microsoft Windows Operating System </p>
<p> On success, the program does not output any informatin and the exit code is 0. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> <p> Show summary of options. </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> Reset the user&#8217;s password. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> Reset all the users. If this option is used there is no need to specify the next option. </p>
 </dd>
<dt><code>-u &lt;user&gt;</code></dt>
<dd> <p> User to change. The user value can be provided as a username, or a RID number in hexadecimal (if the username is preceded with &#8216;0x&#8217;). Usernames including international characters will probably not work. </p>
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
<dt><code>sampasswd -r -u theboss</code></dt>
<dd> <p> Reset the password of a user named &#8216;theboss&#8217;, if found. </p>
 </dd>
<dt><code>sampasswd -r -u 0x3ea</code></dt>
<dd> <p> Reset the password of the user with RID &#8216;0x3a&#8217;. </p>
 </dd>
<dt><code>samusrgrp -r -a</code></dt>
<dd> <p> Reset the password of all the users in the Administrator&#8217;s group (0x220) </p>
 </dd>
<dt><code>samusrgrp -r -f</code></dt>
<dd> <p> Reset the password of the administrative users with the lowest RID number. This does not include the built-in administrator (0x1f4) unless no other administrative user can be found in the database file. </p>
 </dd></dl>
<h2>KNOWN BUGS</h2>
<p> If the username includes international (non-ASCII) characters the program will not (usually) find it. Use the RID number instead. </p>
<h2>SEE ALSO</h2>
<p> <code>chntpwd, reged, samusrgrp</code> <br />
 You will find more information available on how this program works, in the text files <i>/usr/share/doc/chntpw/README.txt</i> and <i>/usr/share/doc/chntpw/MANUAL.txt</i> </p>
<p> More documentation is available at the upstream&#8217;s author site: <code><a rel="nofollow" href="http://pogostick.net/~pnh/ntpasswd/">http://pogostick.net/~pnh/ntpasswd/</a></code> </p>
<h2>AUTHOR</h2>
<p> This program was written by Petter N Hagen. </p>
<p> This manual page was written by Javier Fernandez-Sanguino &lt;jfs [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
