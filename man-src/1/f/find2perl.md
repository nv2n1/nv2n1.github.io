---
title: "find2perl(1)"
name: "find2perl"
section: "1"
letter: "f"
url: "/docs/linux/man/1-find2perl/"
---

<h2 class="name">NAME</h2>
 

 find2perl - translate find command lines to Perl code 

<h2>SYNOPSIS</h2>

 <pre><code>
find2perl[paths][predicates] | perl
</code></pre>

<h2>DESCRIPTION</h2>

 find2perl is a little translator to convert find command lines to equivalent Perl code. The resulting code is typically faster than running find itself. 

 ``paths'' are a set of paths where find2perl will start its searches and ``predicates'' are taken from the following list.
<dl>
<dt>&quot;! PREDICATE&quot;
<dd> Negate the sense of the following predicate. The <tt>&quot;!&quot;</tt> must be passed as a distinct argument, so it may need to be surrounded by whitespace and/or quoted from interpretation by the shell using a backslash (just as with using <tt><a HREF="/docs/linux/man/1-find/">find</a>(1)</tt>).
<dt>&quot;( PREDICATES )&quot;
<dd> Group the given <font SIZE="-1">PREDICATES</font>. The parentheses must be passed as distinct arguments, so they may need to be surrounded by whitespace and/or quoted from interpretation by the shell using a backslash (just as with using <tt><a HREF="/docs/linux/man/1-find/">find</a>(1)</tt>).
<dt>&quot;PREDICATE1 PREDICATE2&quot;
<dd> True if _both_ <font SIZE="-1">PREDICATE1</font> and <font SIZE="-1">PREDICATE2</font> are true; <font SIZE="-1">PREDICATE2</font> is not evaluated if <font SIZE="-1">PREDICATE1</font> is false.
<dt>&quot;PREDICATE1 -o PREDICATE2&quot;
<dd> True if either one of <font SIZE="-1">PREDICATE1</font> or <font SIZE="-1">PREDICATE2</font> is true; <font SIZE="-1">PREDICATE2</font> is not evaluated if <font SIZE="-1">PREDICATE1</font> is true.
<dt>&quot;-follow&quot;
<dd> Follow (dereference) symlinks. The checking of file attributes depends on the position of the <tt>&quot;-follow&quot;</tt> option. If it precedes the file check option, an <tt>&quot;stat&quot;</tt> is done which means the file check applies to the file the symbolic link is pointing to. If <tt>&quot;-follow&quot;</tt> option follows the file check option, this now applies to the symbolic link itself, i.e. an <tt>&quot;lstat&quot;</tt> is done.
<dt>&quot;-depth&quot;
<dd> Change directory traversal algorithm from breadth-first to depth-first.
<dt>&quot;-prune&quot;
<dd> Do not descend into the directory currently matched.
<dt>&quot;-xdev&quot;
<dd> Do not traverse mount points (prunes search at mount-point directories).
<dt>&quot;-name GLOB&quot;
<dd> File name matches specified <font SIZE="-1">GLOB</font> wildcard pattern. <font SIZE="-1">GLOB</font> may need to be quoted to avoid interpretation by the shell (just as with using <tt><a HREF="/docs/linux/man/1-find/">find</a>(1)</tt>).
<dt>&quot;-iname GLOB&quot;
<dd> Like <tt>&quot;-name&quot;</tt>, but the match is case insensitive.
<dt>&quot;-path GLOB&quot;
<dd> Path name matches specified <font SIZE="-1">GLOB</font> wildcard pattern.
<dt>&quot;-ipath GLOB&quot;
<dd> Like <tt>&quot;-path&quot;</tt>, but the match is case insensitive.
<dt>&quot;-perm PERM&quot;
<dd> Low-order 9 bits of permission match octal value <font SIZE="-1">PERM</font>.
<dt>&quot;-perm -PERM&quot;
<dd> The bits specified in <font SIZE="-1">PERM</font> are all set in file's permissions.
<dt>&quot;-type X&quot;
<dd> The file's type matches perl's <tt>&quot;-X&quot;</tt> operator.
<dt>&quot;-fstype TYPE&quot;
<dd> Filesystem of current path is of type <font SIZE="-1">TYPE</font> (only NFS/non-NFS distinction is implemented).
<dt>&quot;-user USER&quot;
<dd> True if <font SIZE="-1">USER</font> is owner of file.
<dt>&quot;-group GROUP&quot;
<dd> True if file's group is <font SIZE="-1">GROUP</font>.
<dt>&quot;-nouser&quot;
<dd> True if file's owner is not in password database.
<dt>&quot;-nogroup&quot;
<dd> True if file's group is not in group database.
<dt>&quot;-inum INUM&quot;
<dd> True file's inode number is <font SIZE="-1">INUM</font>.
<dt>&quot;-links N&quot;
<dd> True if (hard) link count of file matches N (see below).
<dt>&quot;-size N&quot;
<dd> True if file's size matches N (see below) N is normally counted in 512-byte blocks, but a suffix of ``c'' specifies that size should be counted in characters (bytes) and a suffix of ``k'' specifies that size should be counted in 1024-byte blocks.
<dt>&quot;-atime N&quot;
<dd> True if last-access time of file matches N (measured in days) (see below).
<dt>&quot;-ctime N&quot;
<dd> True if last-changed time of file's inode matches N (measured in days, see below).
<dt>&quot;-mtime N&quot;
<dd> True if last-modified time of file matches N (measured in days, see below).
<dt>&quot;-newer FILE&quot;
<dd> True if last-modified time of file matches N.
<dt>&quot;-print&quot;
<dd> Print out path of file (always true). If none of <tt>&quot;-exec&quot;</tt>, <tt>&quot;-ls&quot;</tt>, <tt>&quot;-print0&quot;</tt>, or <tt>&quot;-ok&quot;</tt> is specified, then <tt>&quot;-print&quot;</tt> will be added implicitly.
<dt>&quot;-print0&quot;
<dd> Like -print, but terminates with \0 instead of \n.
<dt>&quot;-exec OPTIONS ;&quot;
<dd> <i>exec()</i> the arguments in <font SIZE="-1">OPTIONS</font> in a subprocess; any occurrence of {} in <font SIZE="-1">OPTIONS</font> will first be substituted with the path of the current file. Note that the command ``rm'' has been special-cased to use perl's <i>unlink()</i> function instead (as an optimization). The <tt>&quot;;&quot;</tt> must be passed as a distinct argument, so it may need to be surrounded by whitespace and/or quoted from interpretation by the shell using a backslash (just as with using <tt><a HREF="/docs/linux/man/1-find/">find</a>(1)</tt>).
<dt>&quot;-ok OPTIONS ;&quot;
<dd> Like -exec, but first prompts user; if user's response does not begin with a y, skip the exec. The <tt>&quot;;&quot;</tt> must be passed as a distinct argument, so it may need to be surrounded by whitespace and/or quoted from interpretation by the shell using a backslash (just as with using <tt><a HREF="/docs/linux/man/1-find/">find</a>(1)</tt>).
<dt>&quot;-eval EXPR&quot;
<dd> Has the perl script <i>eval()</i> the <font SIZE="-1">EXPR</font>.
<dt>&quot;-ls&quot;
<dd> Simulates <tt>&quot;-exec ls -dils {} ;&quot;</tt>
<dt>&quot;-tar FILE&quot;
<dd> Adds current output to tar-format <font SIZE="-1">FILE</font>.
<dt>&quot;-cpio FILE&quot;
<dd> Adds current output to old-style cpio-format <font SIZE="-1">FILE</font>.
<dt>&quot;-ncpio FILE&quot;
<dd> Adds current output to ``new''-style cpio-format <font SIZE="-1">FILE</font>.</dl>
 

 Predicates which take a numeric argument N can come in three forms: 

 <pre>
   * N is prefixed with a +: match values greater than N
   * N is prefixed with a -: match values less than N
   * N is not prefixed with either + or -: match only values equal to N
</pre>

<h2>SEE ALSO</h2>

 find, File::Find. 

<h2>Index</h2>


