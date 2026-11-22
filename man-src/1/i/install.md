---

title: "install(1)"
name: "install"
section: "1"
letter: "i"
url: "/docs/linux/man/1-install/"
description: "install – copy files and set attributes"
---

<p> install &#8211; copy files and set attributes </p>
<h2>SYNOPSIS</h2>
<p> <code>install</code> [<i>,OPTION/</i>]&#8230; [<i>,-T/</i>] <i>,SOURCE DEST/</i><br/>
 <code>install</code> [<i>,OPTION/</i>]&#8230; <i>,SOURCE/</i>&#8230; <i>,DIRECTORY/</i><br/>
 <code>install</code> [<i>,OPTION/</i>]&#8230; <i>,-t DIRECTORY SOURCE/</i>&#8230;<br/>
 <code>install</code> [<i>,OPTION/</i>]&#8230; <i>,-d DIRECTORY/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This install program copies files (often just compiled) into destination locations you choose. If you want to download and install a ready-to-use package on a GNU/Linux system, you should instead be using a package manager like yum(1) or apt-get(1). </p>
<p> In the first three forms, copy SOURCE to DEST or multiple SOURCE(s) to the existing DIRECTORY, while setting permission modes and owner/group. In the 4th form, create all components of the given DIRECTORY(ies). </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>&#8211;backup</code>[=<i>,CONTROL/</i>]</dt>
<dd> make a backup of each existing destination file</dd>
<dt><code>-b</code></dt>
<dd> like <code>&#8211;backup</code> but does not accept an argument</dd>
<dt><code>-c</code></dt>
<dd> (ignored)</dd>
<dt><code>-C</code>, <code>&#8211;compare</code></dt>
<dd> compare each pair of source and destination files, and in some cases, do not modify the destination at all</dd>
<dt><code>-d</code>, <code>&#8211;directory</code></dt>
<dd> treat all arguments as directory names; create all components of the specified directories</dd>
<dt><code>-D</code></dt>
<dd> create all leading components of DEST except the last, or all components of <code>&#8211;target-directory</code>, then copy SOURCE to DEST</dd>
<dt><code>-g</code>, <code>&#8211;group</code>=<i>,GROUP/</i></dt>
<dd> set group ownership, instead of process&#8217; current group</dd>
<dt><code>-m</code>, <code>&#8211;mode</code>=<i>,MODE/</i></dt>
<dd> set permission mode (as in chmod), instead of rwxr-xr-x</dd>
<dt><code>-o</code>, <code>&#8211;owner</code>=<i>,OWNER/</i></dt>
<dd> set ownership (super-user only)</dd>
<dt><code>-p</code>, <code>&#8211;preserve-timestamps</code></dt>
<dd> apply access/modification times of SOURCE files to corresponding destination files</dd>
<dt><code>-s</code>, <code>&#8211;strip</code></dt>
<dd> strip symbol tables</dd>
<dt><code>&#8211;strip-program</code>=<i>,PROGRAM/</i></dt>
<dd> program used to strip binaries</dd>
<dt><code>-S</code>, <code>&#8211;suffix</code>=<i>,SUFFIX/</i></dt>
<dd> override the usual backup suffix</dd>
<dt><code>-t</code>, <code>&#8211;target-directory</code>=<i>,DIRECTORY/</i></dt>
<dd> copy all SOURCE arguments into DIRECTORY</dd>
<dt><code>-T</code>, <code>&#8211;no-target-directory</code></dt>
<dd> treat DEST as a normal file</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print the name of each directory as it is created</dd>
<dt><code>&#8211;preserve-context</code></dt>
<dd> preserve SELinux security context</dd>
<dt><code>-Z</code></dt>
<dd> set SELinux security context of destination file and each created directory to default type</dd>
<dt><code>&#8211;context</code>[=<i>,CTX/</i>]</dt>
<dd> like <code>-Z</code>, or if CTX is specified then set the SELinux or SMACK security context to CTX</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> The backup suffix is &#8216;~&#8217;, unless set with <code>&#8211;suffix</code> or SIMPLE_BACKUP_SUFFIX. The version control method may be selected via the <code>&#8211;backup</code> option or through the VERSION_CONTROL environment variable. Here are the values:</p>
<dl>
<dt>none, off</dt>
<dd> never make backups (even if <code>&#8211;backup</code> is given)</dd>
<dt>numbered, t</dt>
<dd> make numbered backups</dd>
<dt>existing, nil</dt>
<dd> numbered if numbered backups exist, simple otherwise</dd>
<dt>simple, never</dt>
<dd> always make simple backups</dd></dl>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br/>
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/install">https://www.gnu.org/software/coreutils/install</a>&gt;<br/>
 or available locally via: info &#8216;(coreutils) install invocation&#8217; </p>
