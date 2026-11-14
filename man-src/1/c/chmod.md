---
title: "chmod(1)"
name: "chmod"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chmod/"
description: "chmod – change file mode bits"
---

<h2 class="name">NAME</h2>
<p> chmod &#8211; change file mode bits </p>
<h2>SYNOPSIS</h2>
<p> <code>chmod</code> [<i>,OPTION/</i>]&#8230; <i>,MODE/</i>[<i>,,MODE/</i>]&#8230; <i>,FILE/</i>&#8230;<br />
 <code>chmod</code> [<i>,OPTION/</i>]&#8230; <i>,OCTAL-MODE FILE/</i>&#8230;<br />
 <code>chmod</code> [<i>,OPTION/</i>]&#8230; <i>,&#8211;reference=RFILE FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the GNU version of <code>chmod</code>. <code>chmod</code> changes the file mode bits of each given file according to <i>mode</i>, which can be either a symbolic representation of changes to make, or an octal number representing the bit pattern for the new mode bits. </p>
<p> The format of a symbolic mode is [<code>ugoa</code>&#8230;][[<code>-+=</code>][<i>perms</i>&#8230;]&#8230;], where <i>perms</i> is either zero or more letters from the set <code>rwxXst</code>, or a single letter from the set <code>ugo</code>. Multiple symbolic modes can be given, separated by commas. </p>
<p> A combination of the letters <code>ugoa</code> controls which users&#8217; access to the file will be changed: the user who owns it (<code>u</code>), other users in the file&#8217;s group (<code>g</code>), other users not in the file&#8217;s group (<code>o</code>), or all users (<code>a</code>). If none of these are given, the effect is as if (<code>a</code>) were given, but bits that are set in the umask are not affected. </p>
<p> The operator <code>+</code> causes the selected file mode bits to be added to the existing file mode bits of each file; <code>&#8211;</code> causes them to be removed; and <code>=</code> causes them to be added and causes unmentioned bits to be removed except that a directory&#8217;s unmentioned set user and group ID bits are not affected. </p>
<p> The letters <code>rwxXst</code> select file mode bits for the affected users: read (<code>r</code>), write (<code>w</code>), execute (or search for directories) (<code>x</code>), execute/search only if the file is a directory or already has execute permission for some user (<code>X</code>), set user or group ID on execution (<code>s</code>), restricted deletion flag or sticky bit (<code>t</code>). Instead of one or more of these letters, you can specify exactly one of the letters <code>ugo</code>: the permissions granted to the user who owns the file (<code>u</code>), the permissions granted to other users who are members of the file&#8217;s group (<code>g</code>), and the permissions granted to users that are in neither of the two preceding categories (<code>o</code>). </p>
<p> A numeric mode is from one to four octal digits (0-7), derived by adding up the bits with values 4, 2, and 1. Omitted digits are assumed to be leading zeros. The first digit selects the set user ID (4) and set group ID (2) and restricted deletion or sticky (1) attributes. The second digit selects permissions for the user who owns the file: read (4), write (2), and execute (1); the third selects permissions for other users in the file&#8217;s group, with the same values; and the fourth for other users not in the file&#8217;s group, with the same values. </p>
<p> <code>chmod</code> never changes the permissions of symbolic links; the <code>chmod</code> system call cannot change their permissions. This is not a problem since the permissions of symbolic links are never used. However, for each symbolic link listed on the command line, <code>chmod</code> changes the permissions of the pointed-to file. In contrast, <code>chmod</code> ignores symbolic links encountered during recursive directory traversals.</p>
<h2>SETUID AND SETGID BITS</h2>
<p> <code>chmod</code> clears the set-group-ID bit of a regular file if the file&#8217;s group ID does not match the user&#8217;s effective group ID or one of the user&#8217;s supplementary group IDs, unless the user has appropriate privileges. Additional restrictions may cause the set-user-ID and set-group-ID bits of <i>MODE</i> or <i>RFILE</i> to be ignored. This behavior depends on the policy and functionality of the underlying <code>chmod</code> system call. When in doubt, check the underlying system behavior. </p>
<p> For directories <code>chmod</code> preserves set-user-ID and set-group-ID bits unless you explicitly specify otherwise. You can set or clear the bits with symbolic modes like <code>u+s</code> and <code>g-s</code>. To clear these bits for directories with a numeric mode requires an additional leading zero, or leading = like <code>00755</code> , or <code>=755</code></p>
<h2>RESTRICTED DELETION FLAG OR STICKY BIT</h2>
<p> The restricted deletion flag or sticky bit is a single bit, whose interpretation depends on the file type. For directories, it prevents unprivileged users from removing or renaming a file in the directory unless they own the file or the directory; this is called the <i>restricted deletion flag</i> for the directory, and is commonly found on world-writable directories like <code>/tmp</code>. For regular files on some older systems, the bit saves the program&#8217;s text image on the swap device so it will load more quickly when run; this is called the <i>sticky bit</i>.</p>
<h2>OPTIONS</h2>
<p> Change the mode of each FILE to MODE. With <code>&#8211;reference</code>, change the mode of each FILE to that of RFILE.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;changes</code></p>
<dd> like verbose but report only when a change is made</p>
<dt><code>-f</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd> suppress most error messages</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> output a diagnostic for every file processed</p>
<dt><code>&#8211;no-preserve-root</code></p>
<dd> do not treat &#8216;/&#8217; specially (the default)</p>
<dt><code>&#8211;preserve-root</code></p>
<dd> fail to operate recursively on &#8216;/&#8217;</p>
<dt><code>&#8211;reference</code>=<i>,RFILE/</i></p>
<dd> use RFILE&#8217;s mode instead of MODE values</p>
<dt><code>-R</code>, <code>&#8211;recursive</code></p>
<dd> change files and directories recursively</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> Each MODE is of the form &#8216;[ugoa]*([-+=]([rwxXst]*|[ugo]))+|[-+=][0-7]+&#8217;.</p>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-chmod/">chmod</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/chmod">https://www.gnu.org/software/coreutils/chmod</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) chmod invocation&#8217; </p>
<h2>Index</h2>
