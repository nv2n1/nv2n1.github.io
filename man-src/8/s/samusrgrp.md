---
title: "samusrgrp(8)"
name: "samusrgrp"
section: "8"
letter: "s"
url: "/docs/linux/man/8-samusrgrp/"
description: "samusrgrp – add or remove users from groups in SAM database files"
---

<p>samusrgrp &#8211; add or remove users from groups in SAM database files</p>
<h2>Synopsis</h2>
<p><code>samusrgrp</code> [<i>options</i>] &lt;<i>samfile</i>&gt;</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>samusrgrp</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page. <code>samusrgrp</code> is a non-interactive command line utility that can add or remove a user from a local group that exists in the SAM user database of a Microsoft Windows system (Windows NT, 2000, XP, Vista, 7, 8.1, etc.). This file is usually located at \WINDOWS\system32\config\SAM on the file system of a Microsoft Windows Operating System </p>
<p> On success, the program does not output any informatin and the exit code is 0. </p>
<p> The binary program supports multiple names. If it is called named <code>samusrtogrp</code> it will assume <code>-a</code> mode (add user). If it is called named <code>samusrfromgrp</code> it will assume <code>-r</code> mode (remove user). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> <p> Show summary of options. </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> The user is added to the group. This option has to be followed by -u and -g . </p>
 </dd>
<dt><code>-r</code></dt>
<dd> <p> The user is removed from the group. This option has to be followed by -u and -g . </p>
 </dd>
<dt><code>-u &lt;user&gt;</code></dt>
<dd> <p> User to change. The user value can be provided as a username, or a RID number in hexadecimal (if the username is preceded with &#8216;0x&#8217;). Usernames including international characters will probably not work. </p>
 </dd>
<dt><code>-g &lt;group&gt;</code></dt>
<dd> <p> Group to change. The group can only be given as a group number, in hexadecimal, preceded with with &#8216;0x&#8217;. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> Lists the groups in the SAM database. </p>
 </dd>
<dt><code>-L</code></dt>
<dd> <p> Lists the groups in the SAM database as well as their members. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Print the machine SID. </p>
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
<dt><code>samusrgrp -a -u theboss -g 0x220 SAMFILE</code></dt>
<dd> <p> Adds a user named &#8216;theboss&#8217; to the group 0x220 (Administrators) </p>
 </dd>
<dt><code>samusrgrp -a -u 0x3ea -g 0x221 SAMFILE</code></dt>
<dd> <p> Adds a user with the id &#8216;0x3aa&#8217; to the group 0x221 (Users) </p>
 </dd>
<dt><code>samusrgrp -r -u 0x3ff -g 0x221 SAMFILE</code></dt>
<dd> <p> Remove a user with the id &#8216;0x3ff&#8217; from the group 0x221 (Users) </p>
 </dd></dl>
<h2>KNOWN BUGS</h2>
<p> If the username includes international (non-ASCII) characters the program will not (usually) find it. Use the RID number instead. </p>
<h2>SEE ALSO</h2>
<p> <code>chntpwd, reged, sampasswd</code> <br/>
 You will find more information available on how this program works, in the text files <i>/usr/share/doc/chntpw/README.txt</i> and <i>/usr/share/doc/chntpw/MANUAL.txt</i> </p>
<p> More documentation is available at the upstream&#8217;s author site: <code><a rel="nofollow" href="http://pogostick.net/~pnh/ntpasswd/">http://pogostick.net/~pnh/ntpasswd/</a></code> </p>
<h2>AUTHOR</h2>
<p> This program was written by Petter N Hagen. </p>
<p> This manual page was written by Javier Fernandez-Sanguino &lt;jfs [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
