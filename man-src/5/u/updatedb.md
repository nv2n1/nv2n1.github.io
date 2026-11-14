---
title: "updatedb(5)"
name: "updatedb"
section: "5"
letter: "u"
url: "/docs/linux/man/5-updatedb/"
description: "/etc/updatedb.conf – a configuration file for"
---

<p>/etc/updatedb.conf &#8211; a configuration file for </p>
<p><a href="/docs/linux/man/8-updatedb/">updatedb</a>(8) </p>
<h2>Description</h2>
<p><code>/etc/updatedb.conf</code> is a text file. Blank lines are ignored. A <code>#</code> character outside of a quoted string starts a comment extending until end of line. Other lines must be of the following form:</p>
<dl>
<dd><i>VARIABLE</i> <code>=</code> <code>&quot;</code><i>VALUE</i><code>&quot;</code></dl>
<p> White space between tokens is ignored. <i>VARIABLE</i> is an alphanumeric string which does not start with a digit. <i>VALUE</i> can contain any character except for <code>&quot;</code>. No escape mechanism is supported within <i>VALUE</i> and there is no way to write <i>VALUE</i> spanning more than one line. Unknown <i>VARIABLE</i> values are considered an error. The defined variables are:</p>
<dl>
<dt><code>PRUNEFS</code></p>
<dd>A whitespace-separated list of file system types (as used in <code>/etc/mtab</code>) which should not be scanned by <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8). The file system type matching is case-insensitive. By default, no file system types are skipped. When scanning a file system is skipped, all file systems mounted in the subtree are skipped too, even if their type does not match any entry in <code>PRUNEFS</code>.</p>
<dt><code>PRUNENAMES</code></p>
<dd>A whitespace-separated list of directory names (without paths) which should not be scanned by <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8). By default, no directory names are skipped. Note that only directories can be specified, and no pattern mechanism (e.g. globbing) is used.</p>
<dt><code>PRUNEPATHS</code></p>
<dd>A whitespace-separated list of path names of directories which should not be scanned by <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8). Each path name must be exactly in the form in which the directory would be reported by <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1). By default, no paths are skipped.</p>
<dt><code>PRUNE_BIND_MOUNTSFR</p>
<dd>One of the strings 0</code>, <code>no</code>, <code>1</code> or <code>yes</code>. If <code>PRUNE_BIND_MOUNTS</code> is <code>1</code> or <code>yes</code>, bind mounts are not scanned by <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8). All file systems mounted in the subtree of a bind mount are skipped as well, even if they are not bind mounts. As an exception, bind mounts of a directory on itself are not skipped. By default, bind mounts are not skipped. </p>
<h2>Notes</h2>
<p>When a directory is matched by <code>PRUNEFS</code>, <code>PRUNENAMES</code> or <code>PRUNEPATHS</code>, <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8) does not scan the contents of the directory. The path of the directory itself is, however, entered in the created database. For example, if <i>/tmp</i> is in <code>PRUNEPATHS</code>, <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1) will not show any files stored in <i>/tmp</i>, but it can show the <i>/tmp</i> directory. This behavior differs from traditional <code>locate</code> implementations. In some <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8) implementations <code>PRUNEPATHS</code> can be used to exclude non-directory files. This is not the case in this implementation. <code>/etc/updatedb.conf</code> is a shell script in some implementations, which allows much more flexibility in defining the variables. Equivalent functionality can be achieved by using the command-line options to <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8). </p>
<h2>Author</h2>
<p>Miloslav Trmac &lt;mitr [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-locate/">locate</a></code>(1), <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8) </p>
