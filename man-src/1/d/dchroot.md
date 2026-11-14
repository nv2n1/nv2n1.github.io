---
title: "dchroot(1)"
name: "dchroot"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dchroot/"
description: "dchroot – enter a chroot environment"
---

<h2>NAME</h2>
<p> dchroot &#8211; enter a chroot environment</p>
<h2>SYNOPSIS</h2>
<p> <code>dchroot</code> [<code>-h</code>|<code>&#8211;help</code> | <code>-V</code>|<code>&#8211;version</code> | <code>-l</code>|<code>&#8211;list</code> | <code>-i</code>|<code>&#8211;info</code> | <code>&#8211;config</code> | <code>&#8211;location</code>] [<code>&#8211;directory=</code><i>directory</i>] [<code>-d</code>|<code>&#8211;preserve-environment</code>] [<code>-q</code>|<code>&#8211;quiet</code> | <code>-v</code>|<code>&#8211;verbose</code>] [<code>-c </code><i>chroot</i>|<code>&#8211;chroot=</code><i>chroot</i> | <code>&#8211;all</code>] [<code>COMMAND</code> [ <code>ARG1</code> [ <code>ARG2</code> [ <code>ARGn</code>]]]]</p>
<h2>DESCRIPTION</h2>
<p> <code>dchroot</code> allows the user to run a command or a login shell in a chroot environment. If no command is specified, a login shell will be started in the user&#8217;s home directory inside the chroot. </p>
<p> The command is one or more arguments which will be run in the user&#8217;s default shell using its <i>-c</i> option. As a result, shell code may be embedded in this argument. If multiple command options are used, they are concatenated together, separated by spaces. Users should be aware of the shell quoting issues this presents, and should use <code>schroot</code> if necessary, which does not have any quoting issues. </p>
<p> The directory the command or login shell is run in depends upon the context. See <i>&#8211;directory</i> option below for a complete description. </p>
<p> This version of dchroot is a compatibility wrapper around the <code><a href="/docs/linux/man/1-schroot/">schroot</a></code>(1) program. It is provided for backward compatibility with the dchroot command-line options, but schroot is recommended for future use. See the section &#8220;<i>Incompatibilities</i>&#8221; below for known incompatibilities with older versions of dchroot. </p>
<p> If no chroot is specified, the chroot name or alias &#8216;default&#8217; will be used as a fallback.</p>
<h2>OPTIONS</h2>
<p> <code>dchroot</code> accepts the following options:</p>
<h3>Basic options</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help summary.</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> Select all chroots.</p>
<dt><code>-c</code>, <code>&#8211;chroot=</code><i>chroot</i></p>
<dd> Specify a chroot to use. This option may be used multiple times to specify more than one chroot, in which case its effect is similar to <i>&#8211;all</i>.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> List all available chroots.</p>
<dt><code>-i</code>, <code>&#8211;info</code></p>
<dd> Print detailed information about the specified chroots. Note that earlier versions of dchroot did not include this option.</p>
<dt><code>-p</code>, <code>&#8211;path</code></p>
<dd> Print location (path) of the specified chroots.</p>
<dt><code>&#8211;config</code></p>
<dd> Print configuration of the specified chroots. This is useful for testing that the configuration in use is the same as the configuration file. Any comments in the original file will be missing. Note that earlier versions of dchroot did not include this option.</p>
<dt><code>&#8211;directory=</code><i>directory</i></p>
<dd> Change to <i>directory</i> inside the chroot before running the command or login shell. If <i>directory</i> is not available, dchroot will exit with an error status.</p>
<dt>
<dd> The default behaviour is as follows (all directory paths are inside the chroot). Unless the <i>&#8211;preserve-environment</i> option is used to preserve the environment, the login shell or command will run in the user&#8217;s home directory, or <i>/</i> if the home directory is not available. When the <i>&#8211;preserve-environment</i> option is used, it will attempt to use the current working directory, again falling back to <i>/</i> if it is not accessible. If none of the directories are available, dchroot will exit with an error status.</p>
<dt><code>-d</code>, <code>&#8211;preserve-environment</code></p>
<dd> Preserve the user&#8217;s environment inside the chroot environment. The default is to use a clean environment; this option copies the entire user environment and sets it in the session.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Print only essential messages.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print all messages. Note that earlier versions of dchroot did not include this option.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version information.</dl>
<p> Note that earlier versions of dchroot did not provide long options.</p>
<h2>INCOMPATIBILITIES</h2>
<h3>Debian dchroot prior to version 0.99.0</h3>
<dl>
<dt>&bull;</p>
<dd> Log messages are worded and formatted differently.</p>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/1-su/">su</a></code>(1) is no longer used to run commands in the chroot; this is done by dchroot internally. This change may cause subtle differences. If you find an incompatibility, please report it so it may be corrected.</p>
<dt>&bull;</p>
<dd> dchroot provides a restricted subset of the functionality implemented by <code>schroot</code>, but is still schroot underneath. Thus dchroot is still subject to schroot security checking, including PAM authentication and authorisation, and session management, for example, and hence may behave slightly differently to older dchroot versions in some circumstances.</dl>
<h3>Debian dchroot prior to version 1.5.1</h3>
<dl>
<dt>&bull;</p>
<dd> This version of dchroot uses <i>schroot.conf</i> to store the configuration for available chroots, rather than the <i>dchroot.conf</i> file used historically. dchroot supported automatic migration of <i>dchroot.conf</i> to the <i>schroot.conf</i> keyfile format with its <i>&#8211;config</i> option from versions 0.2.2 to 1.5.0; support for the old format is now no longer available.</dl>
<h3>DSA dchroot</h3>
<p> Machines run by the Debian System Administrators for the Debian Project have a <code>dchroot-dsa</code> package which provides an alternate dchroot implementation.</p>
<dl>
<dt>&bull;</p>
<dd> All the above incompatibilities apply.</p>
<dt>&bull;</p>
<dd> This version of dchroot has incompatible command-line options, and while some of those options are supported or have equivalent options by a different name, the <i>-c</i> option is not required to specify a chroot, and this version of dchroot cannot implement this behaviour in a backward-compatible manner (because if <i>-c</i> is omitted, the default chroot is used). DSA dchroot uses the first non-option as the chroot to use, only allowing one chroot to be used at once.</dl>
<h2>DIRECTORY FALLBACKS</h2>
<p> dchroot will select an appropriate directory to use within the chroot based upon whether the <i>&#8211;directory</i> or <i>&#8211;preserve-environment</i> options are used. When explicitly specifying a directory, only one directory will be used for safety and consistency, while for a login shell or command several possibilities may be tried. Note that due to multiple fallbacks being considered for commands, it is dangerous to run commands using dchroot; use schroot instead. The following subsections list the fallback sequence for each case. CWD is the current working directory, DIR is the directory specified with <i>&#8211;directory</i>.</p>
<h3>Login shell or command</h3>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td>Transition</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>(Host &rarr; Chroot)</td>
<td>Comment
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>CWD &rarr; passwd pw_dir</td>
<td> Normal behaviour (if &#8211;directory and <i>&#8211;preserve-environment</i> are not used)
</td>
</tr>
<tr VALIGN=top>
<td>CWD &rarr; /</td>
<td> If passwd pw_dir is nonexistent
</td>
</tr>
<tr VALIGN=top>
<td><code>FAIL</code></td>
<td> If / is nonexistent
</td>
</tr>
</table>
</table>
<h3>&#8211;preserve-environment used</h3>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td>Transition</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>(Host &rarr; Chroot)</td>
<td>Comment
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>CWD &rarr; CWD</td>
<td> Normal behaviour (if <i>&#8211;preserve-environment</i> used)
</td>
</tr>
<tr VALIGN=top>
<td>CWD &rarr; /</td>
<td> If CWD is nonexistent
</td>
</tr>
<tr VALIGN=top>
<td><code>FAIL</code></td>
<td> If / is nonexistent
</td>
</tr>
</table>
</table>
<h3>&#8211;directory used</h3>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td>Transition</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>(Host &rarr; Chroot)</td>
<td>Comment
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>CWD &rarr; DIR</td>
<td>Normal behaviour
</td>
</tr>
<tr VALIGN=top>
<td><code>FAIL</code></td>
<td>If DIR is nonexistent
</td>
</tr>
</table>
</table>
<p> No fallbacks should exist under any circumstances.</p>
<h3>Debugging</h3>
<p> Note that <i>&#8211;debug=notice</i> will show the internal fallback list computed for the session.</p>
<h2>EXAMPLES</h2>
<p> $ dchroot -l&#x240d; Available chroots: sarge [default], sid </p>
<p> $ dchroot -p sid&#x240d; /srv/chroot/sid </p>
<p> $ dchroot -q -c sid &#8212; uname -smr&#x240d; Linux 2.6.16.17 ppc $ dchroot -q -c sid &#8212; &quot;uname -smr&quot;&#x240d; Linux 2.6.16.17 ppc </p>
<p> $ dchroot -q -c sid &quot;ls -1 / | tac | head -n 4&quot;&#x240d; var usr tmp sys </p>
<p> $ dchroot -c sid&#x240d; I: [sid chroot] Running login shell: &#8220;/bin/bash&#8221; $ </p>
<p> Use <i>&#8212;</i> to allow options beginning with &#8216;-&#8216; or &#8216;&#8211;&#8216; in the command to run in the chroot. This prevents them being interpreted as options for dchroot itself. Note that the top line was echoed to standard error, and the remaining lines to standard output. This is intentional, so that program output from commands run in the chroot may be piped and redirected as required; the data will be the same as if the command was run directly on the host system.</p>
<h2>TROUBLESHOOTING</h2>
<p> If something is not working, and it&#8217;s not clear from the error messages what is wrong, try using the <code>&#8211;debug=</code><i>level</i> option to turn on debugging messages. This gives a great deal more information. Valid debug levels are &#8216;none&#8217;, and &#8216;notice&#8217;, &#8216;info&#8217;, &#8216;warning&#8217; and &#8216;critical&#8217; in order of increasing severity. The lower the severity level, the more output. </p>
<p> If you are still having trouble, the developers may be contacted on the mailing list:<br />
 Debian buildd-tools Developers<br />
 &lt;buildd-tools-devel [at] lists.alioth.debian.org&gt;</p>
<h2>BUGS</h2>
<p> On the <code>mips</code> and <code>mipsel</code> architectures, Linux kernels up to and including at least version 2.6.17 have broken <code><a href="/docs/linux/man/2-personality/">personality</a></code>(2) support, which results in a failure to set the personality. This will be seen as an &#8220;Operation not permitted&#8221; (EPERM) error. To work around this problem, set personality to &#8216;undefined&#8217;, or upgrade to a more recent kernel.</p>
<h2>FILES</h2>
<dl>
<dt>
<dd> The system-wide <code>schroot</code> definition file. This file must be owned by the root user, and not be writable by other.</dl>
<h2>AUTHORS</h2>
<p> Roger Leigh. </p>
<p> This implementation of dchroot uses the same command-line options as the original <code>dchroot</code> by David Kimdon &lt;dwhedon [at] debian.org&gt;, but is an independent implementation.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005-2012 Roger Leigh &lt;rleigh [at] debian.org&gt; </p>
<p> is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-schroot/">schroot</a></code>(1), <code><a href="/docs/linux/man/1-sbuild/">sbuild</a></code>(1), <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2), <code><a href="/docs/linux/man/5-schroot-setup/">schroot-setup</a></code>(5), <code><a href="/docs/linux/man/5-schroot-conf/">schroot.conf</a></code>(5). </p>
<h2>Index</h2>
