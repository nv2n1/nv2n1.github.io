---
title: "chntpw(8)"
name: "chntpw"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chntpw/"
description: "chntpw – utility to overwrite passwords of Windows systems"
---

<p>chntpw &#8211; utility to overwrite passwords of Windows systems</p>
<h2>Synopsis</h2>
<p><code>chntpw</code> [<i>options</i>] &lt;<i>samfile</i>&gt; [<i>systemfile</i>] [<i>securityfile</i>] [<i>otherreghive</i>] [&#8230;]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>chntpw</code> command. This manual page was written for the Debian distribution because the original program does not have a manual page. <code>chntpw</code> is a utility to view some information and reset user passwords in a Windows NT/2000 SAM userdatabase file used by Microsoft Windows Operating System (in NT3.x and later versions). This file is usually located at \WINDOWS\system32\config\SAM on the Windows file system. It is not necessary to know the previous passwords to reset them. In addition it contains a simple registry editor and ahex-editor with which the information contained in a registry file can be browsed and modified. </p>
<p> This program should be able to handle both 32 and 64 bit Microsoft Windows and all versions from NT3.x up to Win8.1. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> <p> Show a summary of options. </p>
 </dd>
<dt><code>-u username</code></dt>
<dd> <p> Username or username ID (RID) to change. The default is &#8216;Administrator&#8217;. </p>
 </dd>
<dt><code>-l</code></dt>
<dd> <p> List all users in the SAM database and exit. </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> Interactive Menu system: list all users (as per -l option) and then ask for the user to change. </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> Registry editor with limited capabilities (but it does include write support). For a slightly more powerful editor see <code>reged</code> </p>
 </dd>
<dt><code>-d</code></dt>
<dd> <p> Use buffer debugger instead (hex editor) </p>
<p> <code>-L</code> Log all changed filenames to /tmp/changed. When this option is set the program automatically saves the changes in the hive files without prompting the user. </p>
<p> Be careful when using the <code>-L</code> option as a root user in a multiuser system. The filename is fixed and this can be used by malicious users (dropping a symlink with the same name) to overwrite system files. </p>
 </dd>
<dt><code>-N</code></dt>
<dd> <p> Do not allocate more information, only allow the editing of existing values with same size. </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> Do not expand the hive file (safe mode). </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Print verbose information and debug messages. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>ntfs-3g /dev/sda1 /media/win ; cd /media/win/WINDOWS/system32/config/</code></dt>
<dd> <p> Mount the Windows file system and enters the directory <code>\\WINDOWS\\system32\\config</code> where Windows stores the SAM database. </p>
 </dd>
<dt><code>chntpw SAM system</code></dt>
<dd> <p> Opens registry hives <code>SAM</code> and <code>system</code> and change administrator account. This will work even if the name has been changed or it has been localized (since different language versions of NT use different administrator names). </p>
 </dd>
<dt><code>chntpw -l SAM</code></dt>
<dd> <p> Lists the users defined in the <code>SAM</code> registry file. </p>
 </dd>
<dt><code>chntpw -u jabbathehutt SAM</code></dt>
<dd> <p> Prompts for password for <code>jabbathehutt</code> and changes it in the <code>SAM</code> registry file, if found (otherwise do nothing). </p>
 </dd></dl>
<h2>KNOWN BUGS</h2>
<p> This program uses undocumented structures in the SAM database. Use with caution (i.e. make sure you make a backup of the file before any changes are done). </p>
<p> Password changing is only possible if the program has been specifically compiled with some cryptographic functions. This feature, however, only works properly in Windows NT and Windows 2000 systems. It might not work properly in Windows XP, Vista, Win7, Win8 and later systems. </p>
<p> In the Debian distribution this feature is not enabled. </p>
<h2>SEE ALSO</h2>
<p> <code>reged, samusrgrp, sampasswd</code> </p>
<p> If you are looking for an automated procedure for password recovery, you might want to check the bootdisks (can be used in CD and USB drives) provided by the upstream author at <code><a rel="nofollow" href="http://pogostick.net/~pnh/ntpasswd/">http://pogostick.net/~pnh/ntpasswd/</a></code> </p>
<p> <br/>
 You will find more information available on how this program works, including in-depth details on how the registry works, in the text files <i>/usr/share/doc/chntpw/README.txt</i> and <i>/usr/share/doc/chntpw/MANUAL.txt</i> </p>
<h2>AUTHOR</h2>
<p> This program was written by Petter N Hagen. </p>
<p> This manual page was written by Javier Fernandez-Sanguino &lt;jfs [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
