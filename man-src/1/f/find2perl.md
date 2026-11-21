---

title: "find2perl(1)"
name: "find2perl"
section: "1"
letter: "f"
url: "/docs/linux/man/1-find2perl/"
---

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
</dt><dd> Negate the sense of the following predicate. The <tt>&quot;!&quot;</tt> must be passed as a distinct argument, so it may need to be surrounded by whitespace and/or quoted from interpretation by the shell using a backslash (just as with using <tt><a HREF="/docs/linux/man/1-find/">find</a>(1)</tt>).
</dd><dt>&quot;( PREDICATES )&quot;
</dt><dd> Group the given <font SIZE="-1">PREDICATES</font>. The parentheses must be passed as distinct arguments, so they may need to be surrounded by whitespace and/or quoted from interpretation by the shell using a backslash (just as with using <tt><a HREF="/docs/linux/man/1-find/">find</a>(1)</tt>).
</dd><dt>&quot;PREDICATE1 PREDICATE2&quot;
</dt><dd> True if _both_ <font SIZE="-1">PREDICATE1</font> and <font SIZE="-1">PREDICATE2</font> are true; <font SIZE="-1">PREDICATE2</font> is not evaluated if <font SIZE="-1">PREDICATE1</font> is false.
</dd><dt>&quot;PREDICATE1 -o PREDICATE2&quot;
</dt><dd> True if either one of <font SIZE="-1">PREDICATE1</font> or <font SIZE="-1">PREDICATE2</font> is true; <font SIZE="-1">PREDICATE2</font> is not evaluated if <font SIZE="-1">PREDICATE1</font> is true.
</dd><dt>&quot;-follow&quot;
</dt><dd> Follow (dereference) symlinks. The checking of file attributes depends on the position of the <tt>&quot;-follow&quot;</tt> option. If it precedes the file check option, an <tt>&quot;stat&quot;</tt> is done which means the file check applies to the file the symbolic link is pointing to. If <tt>&quot;-follow&quot;</tt> option follows the file check option, this now applies to the symbolic link itself, i.e. an <tt>&quot;lstat&quot;</tt> is done.
</dd><dt>&quot;-depth&quot;
</dt><dd> Change directory traversal algorithm from breadth-first to depth-first.
</dd><dt>&quot;-prune&quot;
</dt><dd> Do not descend into the directory currently matched.
</dd><dt>&quot;-xdev&quot;
</dt><dd> Do not traverse mount points (prunes search at mount-point directories).
</dd><dt>&quot;-name GLOB&quot;
</dt><dd> File name matches specified <font SIZE="-1">GLOB</font> wildcard pattern. <font SIZE="-1">GLOB</font> may need to be quoted to avoid interpretation by the shell (just as with using <tt><a HREF="/docs/linux/man/1-find/">find</a>(1)</tt>).
</dd><dt>&quot;-iname GLOB&quot;
</dt><dd> Like <tt>&quot;-name&quot;</tt>, but the match is case insensitive.
</dd><dt>&quot;-path GLOB&quot;
</dt><dd> Path name matches specified <font SIZE="-1">GLOB</font> wildcard pattern.
</dd><dt>&quot;-ipath GLOB&quot;
</dt><dd> Like <tt>&quot;-path&quot;</tt>, but the match is case insensitive.
</dd><dt>&quot;-perm PERM&quot;
</dt><dd> Low-order 9 bits of permission match octal value <font SIZE="-1">PERM</font>.
</dd><dt>&quot;-perm -PERM&quot;
</dt><dd> The bits specified in <font SIZE="-1">PERM</font> are all set in file's permissions.
</dd><dt>&quot;-type X&quot;
</dt><dd> The file's type matches perl's <tt>&quot;-X&quot;</tt> operator.
</dd><dt>&quot;-fstype TYPE&quot;
</dt><dd> Filesystem of current path is of type <font SIZE="-1">TYPE</font> (only NFS/non-NFS distinction is implemented).
</dd><dt>&quot;-user USER&quot;
</dt><dd> True if <font SIZE="-1">USER</font> is owner of file.
</dd><dt>&quot;-group GROUP&quot;
</dt><dd> True if file's group is <font SIZE="-1">GROUP</font>.
</dd><dt>&quot;-nouser&quot;
</dt><dd> True if file's owner is not in password database.
</dd><dt>&quot;-nogroup&quot;
</dt><dd> True if file's group is not in group database.
</dd><dt>&quot;-inum INUM&quot;
</dt><dd> True file's inode number is <font SIZE="-1">INUM</font>.
</dd><dt>&quot;-links N&quot;
</dt><dd> True if (hard) link count of file matches N (see below).
</dd><dt>&quot;-size N&quot;
</dt><dd> True if file's size matches N (see below) N is normally counted in 512-byte blocks, but a suffix of ``c'' specifies that size should be counted in characters (bytes) and a suffix of ``k'' specifies that size should be counted in 1024-byte blocks.
</dd><dt>&quot;-atime N&quot;
</dt><dd> True if last-access time of file matches N (measured in days) (see below).
</dd><dt>&quot;-ctime N&quot;
</dt><dd> True if last-changed time of file's inode matches N (measured in days, see below).
</dd><dt>&quot;-mtime N&quot;
</dt><dd> True if last-modified time of file matches N (measured in days, see below).
</dd><dt>&quot;-newer FILE&quot;
</dt><dd> True if last-modified time of file matches N.
</dd><dt>&quot;-print&quot;
</dt><dd> Print out path of file (always true). If none of <tt>&quot;-exec&quot;</tt>, <tt>&quot;-ls&quot;</tt>, <tt>&quot;-print0&quot;</tt>, or <tt>&quot;-ok&quot;</tt> is specified, then <tt>&quot;-print&quot;</tt> will be added implicitly.
</dd><dt>&quot;-print0&quot;
</dt><dd> Like -print, but terminates with \0 instead of \n.
</dd><dt>&quot;-exec OPTIONS ;&quot;
</dt><dd> <i>exec()</i> the arguments in <font SIZE="-1">OPTIONS</font> in a subprocess; any occurrence of {} in <font SIZE="-1">OPTIONS</font> will first be substituted with the path of the current file. Note that the command ``rm'' has been special-cased to use perl's <i>unlink()</i> function instead (as an optimization). The <tt>&quot;;&quot;</tt> must be passed as a distinct argument, so it may need to be surrounded by whitespace and/or quoted from interpretation by the shell using a backslash (just as with using <tt><a HREF="/docs/linux/man/1-find/">find</a>(1)</tt>).
</dd><dt>&quot;-ok OPTIONS ;&quot;
</dt><dd> Like -exec, but first prompts user; if user's response does not begin with a y, skip the exec. The <tt>&quot;;&quot;</tt> must be passed as a distinct argument, so it may need to be surrounded by whitespace and/or quoted from interpretation by the shell using a backslash (just as with using <tt><a HREF="/docs/linux/man/1-find/">find</a>(1)</tt>).
</dd><dt>&quot;-eval EXPR&quot;
</dt><dd> Has the perl script <i>eval()</i> the <font SIZE="-1">EXPR</font>.
</dd><dt>&quot;-ls&quot;
</dt><dd> Simulates <tt>&quot;-exec ls -dils {} ;&quot;</tt>
</dd><dt>&quot;-tar FILE&quot;
</dt><dd> Adds current output to tar-format <font SIZE="-1">FILE</font>.
</dd><dt>&quot;-cpio FILE&quot;
</dt><dd> Adds current output to old-style cpio-format <font SIZE="-1">FILE</font>.
</dd><dt>&quot;-ncpio FILE&quot;
</dt><dd> Adds current output to ``new''-style cpio-format <font SIZE="-1">FILE</font>.</dd></dl>
 

 Predicates which take a numeric argument N can come in three forms: 

 <pre>
   * N is prefixed with a +: match values greater than N
   * N is prefixed with a -: match values less than N
   * N is not prefixed with either + or -: match only values equal to N
</pre>

<h2>SEE ALSO</h2>

 find, File::Find.
