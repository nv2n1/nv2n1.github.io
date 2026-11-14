---
title: "tmpfiles(5)"
name: "tmpfiles"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tmpfiles/"
description: "tmpfiles.d – Configuration for creation, deletion and cleaning of volatile and temporary files"
---

<p>tmpfiles.d &#8211; Configuration for creation, deletion and cleaning of volatile and temporary files</p>
<h2>Synopsis</h2>
<p>/etc/tmpfiles.d/*.conf </p>
<p> /run/tmpfiles.d/*.conf </p>
<p> /usr/lib/tmpfiles.d/*.conf</p>
<h2>Description</h2>
<p><code>systemd-tmpfiles</code> uses the configuration files from the above directories to describe the creation, cleaning and removal of volatile and temporary files and directories which usually reside in directories such as /run or /tmp. </p>
<p> Volatile and temporary files and directories are those located in /run (and its alias /var/run), /tmp, /var/tmp, the API file systems such as /sys or /proc, as well as some other directories below /var. </p>
<p> System daemons frequently require private runtime directories below /run to place communication sockets and similar in. For these, consider declaring them in their unit files using <i>RuntimeDirectory=</i> (see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details), if this is feasible.</p>
<h2>Configuration Format</h2>
<p>Each configuration file shall be named in the style of <i>package</i>.conf or <i>package</i>&#8211;<i>part</i>.conf. The second variant should be used when it is desirable to make it easy to override just this part of configuration. </p>
<p> Files in /etc/tmpfiles.d override files with the same name in /usr/lib/tmpfiles.d and /run/tmpfiles.d. Files in /run/tmpfiles.d override files with the same name in /usr/lib/tmpfiles.d. Packages should install their configuration files in /usr/lib/tmpfiles.d. Files in /etc/tmpfiles.d are reserved for the local administrator, who may use this logic to override the configuration files installed by vendor packages. All configuration files are sorted by their filename in lexicographic order, regardless of which of the directories they reside in. If multiple files specify the same path, the entry in the file with the lexicographically earliest name will be applied, all all other conflicting entries will be logged as errors. When two lines are prefix and suffix of each other, then the prefix is always processed first, the suffix later. Otherwise, the files/directories are processed in the order they are listed. </p>
<p> If the administrator wants to disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in /etc/tmpfiles.d/ bearing the same filename. </p>
<p> The configuration format is one line per path containing type, path, mode, ownership, age, and argument fields: </p>
<dl>
<dd>
<pre>#Type Path Mode UID GID Age Argument
d /run/user 0755 root root 10d -
L /tmp/foobar - - - - /dev/null</pre>
</dl>
<h3>Type</h3>
<p>The type consists of a single letter and optionally an exclamation mark. </p>
<p> The following line types are understood: </p>
<p> <i>f</i></p>
<dl>
<dd>Create a file if it does not exist yet. If the argument parameter is given, it will be written to the file.</dl>
<p> <i>F</i></p>
<dl>
<dd>Create or truncate a file. If the argument parameter is given, it will be written to the file.</dl>
<p> <i>w</i></p>
<dl>
<dd>Write the argument parameter to a file, if the file exists. Lines of this type accept shell-style globs in place of normal path names. The argument parameter will be written without a trailing newline. C-style backslash escapes are interpreted.</dl>
<p> <i>d</i></p>
<dl>
<dd>Create a directory if it does not exist yet.</dl>
<p> <i>D</i></p>
<dl>
<dd>Create or empty a directory.</dl>
<p> <i>p</i>, <i>p+</i></p>
<dl>
<dd>Create a named pipe (FIFO) if it does not exist yet. If suffixed with <i>+</i> and a file already exists where the pipe is to be created, it will be removed and be replaced by the pipe.</dl>
<p> <i>L</i>, <i>L+</i></p>
<dl>
<dd>Create a symlink if it does not exist yet. If suffixed with <i>+</i> and a file already exists where the symlink is to be created, it will be removed and be replaced by the symlink. If the argument is omitted, symlinks to files with the same name residing in the directory /usr/share/factory/ are created.</dl>
<p> <i>c</i>, <i>c+</i></p>
<dl>
<dd>Create a character device node if it does not exist yet. If suffixed with <i>+</i> and a file already exists where the device node is to be created, it will be removed and be replaced by the device node. It is recommended to suffix this entry with an exclamation mark to only create static device nodes at boot, as udev will not manage static device nodes that are created at runtime.</dl>
<p> <i>b</i>, <i>b+</i></p>
<dl>
<dd>Create a block device node if it does not exist yet. If suffixed with <i>+</i> and a file already exists where the device node is to be created, it will be removed and be replaced by the device node. It is recommended to suffix this entry with an exclamation mark to only create static device nodes at boot, as udev will not manage static device nodes that are created at runtime.</dl>
<p> <i>C</i></p>
<dl>
<dd>Recursively copy a file or directory, if the destination files or directories do not exist yet. Note that this command will not descend into subdirectories if the destination directory already exists. Instead, the entire copy operation is skipped. If the argument is omitted, files from the source directory /usr/share/factory/ with the same name are copied.</dl>
<p> <i>x</i></p>
<dl>
<dd>Ignore a path during cleaning. Use this type to exclude paths from clean-up as controlled with the Age parameter. Note that lines of this type do not influence the effect of <i>r</i> or <i>R</i> lines. Lines of this type accept shell-style globs in place of normal path names.</dl>
<p> <i>X</i></p>
<dl>
<dd>Ignore a path during cleaning. Use this type to exclude paths from clean-up as controlled with the Age parameter. Unlike <i>x</i>, this parameter will not exclude the content if path is a directory, but only directory itself. Note that lines of this type do not influence the effect of <i>r</i> or <i>R</i> lines. Lines of this type accept shell-style globs in place of normal path names.</dl>
<p> <i>r</i></p>
<dl>
<dd>Remove a file or directory if it exists. This may not be used to remove non-empty directories, use <i>R</i> for that. Lines of this type accept shell-style globs in place of normal path names.</dl>
<p> <i>R</i></p>
<dl>
<dd>Recursively remove a path and all its subdirectories (if it is a directory). Lines of this type accept shell-style globs in place of normal path names.</dl>
<p> <i>z</i></p>
<dl>
<dd>Adjust the access mode, group and user, and restore the SELinux security context of a file or directory, if it exists. Lines of this type accept shell-style globs in place of normal path names.</dl>
<p> <i>Z</i></p>
<dl>
<dd>Recursively set the access mode, group and user, and restore the SELinux security context of a file or directory if it exists, as well as of its subdirectories and the files contained therein (if applicable). Lines of this type accept shell-style globs in place of normal path names.</dl>
<p> If the exclamation mark is used, this line is only safe of execute during boot, and can break a running system. Lines without the exclamation mark are presumed to be safe to execute at any time, e.g. on package upgrades. <code>systemd-tmpfiles</code> will execute line with an exclamation mark only if option <code>&#8211;boot</code> is given. </p>
<p> For example: </p>
<dl>
<dd>
<pre># Make sure these are created by default so that nobody else can
d /tmp/.X11-unix 1777 root root 10d
# Unlink the X11 lock files
r! /tmp/.X[0-9]*-lock</pre>
</dl>
<p> The second line in contrast to the first one would break a running system, and will only be executed with <code>&#8211;boot</code>.</p>
<h3>Path</h3>
<p>The file system path specification supports simple specifier expansion. The following expansions are understood: </p>
<p> <code>Table 1. Specifiers available</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Specifier </code></td>
<td><code> Meaning </code></td>
<td><code> Details </code>
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%m&quot; </td>
<td> Machine ID </td>
<td> The machine ID of the running system, formatted as string. See <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%b&quot; </td>
<td> Boot ID </td>
<td> The boot ID of the running system, formatted as string. See <code><a href="/docs/linux/man/4-random/">random</a></code>(4) for more information.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%H&quot; </td>
<td> Host name </td>
<td> The hostname of the running system.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%v&quot; </td>
<td> Kernel release </td>
<td> Identical to <code>uname -r</code> output.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;%%&quot; </td>
<td> Escaped % </td>
<td> Single percent sign.
</td>
</tr>
</table>
<h3>Mode</h3>
<p>The file access mode to use when creating this file or directory. If omitted or when set to -, the default is used: 0755 for directories, 0644 for all other file objects. For <i>z</i>, <i>Z</i> lines, if omitted or when set to &quot;-&quot;, the file access mode will not be modified. This parameter is ignored for <i>x</i>, <i>r</i>, <i>R</i>, <i>L</i> lines. </p>
<p> Optionally, if prefixed with &quot;~&quot;, the access mode is masked based on the already set access bits for existing file or directories: if the existing file has all executable bits unset, all executable bits are removed from the new access mode, too. Similarly, if all read bits are removed from the old access mode, they will be removed from the new access mode too, and if all write bits are removed, they will be removed from the new access mode too. In addition, the sticky/SUID/SGID bit is removed unless applied to a directory. This functionality is particularly useful in conjunction with <i>Z</i>.</p>
<h3>Uid, Gid</h3>
<p>The user and group to use for this file or directory. This may either be a numeric user/group ID or a user or group name. If omitted or when set to &quot;-&quot;, the default 0 (root) is used. For <i>z</i>, <i>Z</i> lines, when omitted or when set to -, the file ownership will not be modified. These parameters are ignored for <i>x</i>, <i>r</i>, <i>R</i>, <i>L</i> lines.</p>
<h3>Age</h3>
<p>The date field, when set, is used to decide what files to delete when cleaning. If a file or directory is older than the current time minus the age field, it is deleted. The field format is a series of integers each followed by one of the following postfixes for the respective time units: </p>
<p> <i>s</i>, <i>min</i>, <i>h</i>, <i>d</i>, <i>w</i>, <i>ms</i>, <i>m</i>, <i>us</i></p>
<dl>
<dd></dl>
<p> If multiple integers and units are specified, the time values are summed up. If an integer is given without a unit, s is assumed. </p>
<p> When the age is set to zero, the files are cleaned unconditionally. </p>
<p> The age field only applies to lines starting with <i>d</i>, <i>D</i>, and <i>x</i>. If omitted or set to &quot;-&quot;, no automatic clean-up is done. </p>
<p> If the age field starts with a tilde character &quot;~&quot;, the clean-up is only applied to files and directories one level inside the directory specified, but not the files and directories immediately inside it.</p>
<h3>Argument</h3>
<p>For <i>L</i> lines determines the destination path of the symlink. For <i>c</i>, <i>b</i> determines the major/minor of the device node, with major and minor formatted as integers, separated by &quot;:&quot;, e.g. &quot;1:3&quot;. For <i>f</i>, <i>F</i>, and <i>w</i> may be used to specify a short string that is written to the file, suffixed by a newline. For <i>C</i>, specifies the source file or directory. Ignored for all other lines.</p>
<h2>Example</h2>
<p><code>Example 1.&nbsp;<wbr>/etc/tmpfiles.d/screen.conf example</code> </p>
<p> <code>screen</code> needs two directories created at boot with specific modes and ownership. </p>
<dl>
<dd>
<pre>d /run/screens 1777 root root 10d
d /run/uscreens 0755 root root 10d12h</pre>
</dl>
<p> <code>Example 2.&nbsp;<wbr>/etc/tmpfiles.d/abrt.conf example</code> </p>
<p> <code>abrt</code> needs a directory created at boot with specific mode and ownership and its content should be preserved. </p>
<dl>
<dd>
<pre>d /var/tmp/abrt 0755 abrt abrt
x /var/tmp/abrt/*</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-tmpfiles/">systemd-tmpfiles</a></code>(8), <code><a href="/docs/linux/man/1-systemd-delta/">systemd-delta</a></code>(1), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) </p>
