---
title: "find(1)"
name: "find"
section: "1"
letter: "f"
url: "/docs/linux/man/1-find/"
description: "find – search for files in a directory hierarchy"
---

<h2 class="name">NAME</h2>
<p> find &#8211; search for files in a directory hierarchy </p>
<h2>SYNOPSIS</h2>
<p> <code>find</code> [-H] [-L] [-P] [-D debugopts] [-Olevel] [starting-point&#8230;] [expression]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the GNU version of <code>find</code>. GNU <code>find</code> searches the directory tree rooted at each given starting-point by evaluating the given expression from left to right, according to the rules of precedence (see section OPERATORS), until the outcome is known (the left hand side is false for <i>and</i> operations, true for <i>or</i>), at which point <code>find</code> moves on to the next file name. If no starting-point is specified, `.&#8217; is assumed. </p>
<p> If you are using <code>find</code> in an environment where security is important (for example if you are using it to search directories that are writable by other users), you should read the `Security Considerations&#8217; chapter of the findutils documentation, which is called <code>Finding Files</code> and comes with findutils. That document also includes a lot more detail and discussion than this manual page, so you may find it a more useful source of information.</p>
<h2>OPTIONS</h2>
<p> The <code>-H</code>, <code>-L</code> and <code>-P</code> options control the treatment of symbolic links. Command-line arguments following these are taken to be names of files or directories to be examined, up to the first argument that begins with `-&#8216;, or the argument `(&#8216; or `!&#8217;. That argument and any following arguments are taken to be the expression describing what is to be searched for. If no paths are given, the current directory is used. If no expression is given, the expression <code>-print</code> is used (but you should probably consider using <code>-print0</code> instead, anyway). </p>
<p> This manual page talks about `options&#8217; within the expression list. These options control the behaviour of <code>find</code> but are specified immediately after the last path name. The five `real&#8217; options <code>-H</code>, <code>-L</code>, <code>-P</code>, <code>-D</code> and <code>-O</code> must appear before the first path name, if at all. A double dash <code>&#8212;</code> could theoretically be used to signal that any remaining arguments are not options, but this does not really work due to the way <code>find</code> determines the end of the following path arguments: it does that by reading until an expression argument comes (which also starts with a `-&#8216;). Now, if a path argument would start with a `-&#8216;, then <code>find</code> would treat it as expression argument instead. Thus, to ensure that all start points are taken as such, and especially to prevent that wildcard patterns expanded by the calling shell are not mistakenly treated as expression arguments, it is generally safer to prefix wildcards or dubious path names with either `./&#8217; or to use absolute path names starting with &#8216;/&#8217;.</p>
<dl>
<dt>-P</p>
<dd> Never follow symbolic links. This is the default behaviour. When <code>find</code> examines or prints information about files, and the file is a symbolic link, the information used shall be taken from the properties of the symbolic link itself. </p>
<dt>-L</p>
<dd> Follow symbolic links. When <code>find</code> examines or prints information about files, the information used shall be taken from the properties of the file to which the link points, not from the link itself (unless it is a broken symbolic link or <code>find</code> is unable to examine the file to which the link points). Use of this option implies <code>-noleaf</code>. If you later use the <code>-P</code> option, <code>-noleaf</code> will still be in effect. If <code>-L</code> is in effect and <code>find</code> discovers a symbolic link to a subdirectory during its search, the subdirectory pointed to by the symbolic link will be searched.</p>
<dt>
<dd> When the <code>-L</code> option is in effect, the <code>-type</code> predicate will always match against the type of the file that a symbolic link points to rather than the link itself (unless the symbolic link is broken). Actions that can cause symbolic links to become broken while <code>find</code> is executing (for example <code>-delete</code>) can give rise to confusing behaviour. Using <code>-L</code> causes the <code>-lname</code> and <code>-ilname</code> predicates always to return false. </p>
<dt>-H</p>
<dd> Do not follow symbolic links, except while processing the command line arguments. When <code>find</code> examines or prints information about files, the information used shall be taken from the properties of the symbolic link itself. The only exception to this behaviour is when a file specified on the command line is a symbolic link, and the link can be resolved. For that situation, the information used is taken from whatever the link points to (that is, the link is followed). The information about the link itself is used as a fallback if the file pointed to by the symbolic link cannot be examined. If <code>-H</code> is in effect and one of the paths specified on the command line is a symbolic link to a directory, the contents of that directory will be examined (though of course <code>-maxdepth 0</code> would prevent this).</dl>
<p> If more than one of <code>-H</code>, <code>-L</code> and <code>-P</code> is specified, each overrides the others; the last one appearing on the command line takes effect. Since it is the default, the <code>-P</code> option should be considered to be in effect unless either <code>-H</code> or <code>-L</code> is specified. </p>
<p> GNU <code>find</code> frequently stats files during the processing of the command line itself, before any searching has begun. These options also affect how those arguments are processed. Specifically, there are a number of tests that compare files listed on the command line against a file we are currently considering. In each case, the file specified on the command line will have been examined and some of its properties will have been saved. If the named file is in fact a symbolic link, and the <code>-P</code> option is in effect (or if neither <code>-H</code> nor <code>-L</code> were specified), the information used for the comparison will be taken from the properties of the symbolic link. Otherwise, it will be taken from the properties of the file the link points to. If <code>find</code> cannot follow the link (for example because it has insufficient privileges or the link points to a nonexistent file) the properties of the link itself will be used. </p>
<p> When the <code>-H</code> or <code>-L</code> options are in effect, any symbolic links listed as the argument of <code>-newer</code> will be dereferenced, and the timestamp will be taken from the file to which the symbolic link points. The same consideration applies to <code>-newerXY</code>, <code>-anewer</code> and <code>-cnewer</code>. </p>
<p> The <code>-follow</code> option has a similar effect to <code>-L</code>, though it takes effect at the point where it appears (that is, if <code>-L</code> is not used but <code>-follow</code> is, any symbolic links appearing after <code>-follow</code> on the command line will be dereferenced, and those before it will not). </p>
<dl>
<dt>-D debugopts</p>
<dd> Print diagnostic information; this can be helpful to diagnose problems with why <code>find</code> is not doing what you want. The list of debug options should be comma separated. Compatibility of the debug options is not guaranteed between releases of findutils. For a complete list of valid debug options, see the output of <code>find -D help</code>. Valid debug options include</p>
<dl>
<dt>
<dd>
<dl>
<dt>exec</p>
<dd> Show diagnostic information relating to -exec, -execdir, -ok and -okdir</p>
<dt>opt</p>
<dd> Prints diagnostic information relating to the optimisation of the expression tree; see the -O option.</p>
<dt>rates</p>
<dd> Prints a summary indicating how often each predicate succeeded or failed.</p>
<dt>search</p>
<dd> Navigate the directory tree verbosely.</p>
<dt>stat</p>
<dd> Print messages as files are examined with the <code>stat</code> and <code>lstat</code> system calls. The <code>find</code> program tries to minimise such calls.</p>
<dt>tree</p>
<dd> Show the expression tree in its original and optimised form.</p>
<dt>all</p>
<dd> Enable all of the other debug options (but <code>help</code>).</p>
<dt>help</p>
<dd> Explain the debugging options.</dl>
</dl>
<dt>-Olevel</p>
<dd> Enables query optimisation. The <code>find</code> program reorders tests to speed up execution while preserving the overall effect; that is, predicates with side effects are not reordered relative to each other. The optimisations performed at each optimisation level are as follows.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Equivalent to optimisation level 1.</p>
<dt>1</p>
<dd> This is the default optimisation level and corresponds to the traditional behaviour. Expressions are reordered so that tests based only on the names of files (for example <code>-name</code> and <code>-regex</code>) are performed first.</p>
<dt>2</p>
<dd> Any <code>-type</code> or <code>-xtype</code> tests are performed after any tests based only on the names of files, but before any tests that require information from the inode. On many modern versions of Unix, file types are returned by <code>readdir()</code> and so these predicates are faster to evaluate than predicates which need to stat the file first. If you use the <code>-fstype&nbsp;</code><i>FOO</i> predicate and specify a filesystem type <i>FOO</i> which is not known (that is, present in `/etc/mtab&#8217;) at the time <code>find</code> starts, that predicate is equivalent to <code>-false</code>.</p>
<dt>3</p>
<dd> At this optimisation level, the full cost-based query optimiser is enabled. The order of tests is modified so that cheap (i.e. fast) tests are performed first and more expensive ones are performed later, if necessary. Within each cost band, predicates are evaluated earlier or later according to whether they are likely to succeed or not. For <code>-o</code>, predicates which are likely to succeed are evaluated earlier, and for <code>-a</code>, predicates which are likely to fail are evaluated earlier.</dl>
</dl>
<dt>
<dd> The cost-based optimiser has a fixed idea of how likely any given test is to succeed. In some cases the probability takes account of the specific nature of the test (for example, <code>-type f</code> is assumed to be more likely to succeed than <code>-type c</code>). The cost-based optimiser is currently being evaluated. If it does not actually improve the performance of <code>find</code>, it will be removed again. Conversely, optimisations that prove to be reliable, robust and effective may be enabled at lower optimisation levels over time. However, the default behaviour (i.e. optimisation level 1) will not be changed in the 4.3.x release series. The findutils test suite runs all the tests on <code>find</code> at each optimisation level and ensures that the result is the same.</dl>
<h2>EXPRESSION</h2>
<p> The part of the command line after the list of starting points is the <i>expression</i>. This is a kind of query specification describing how we match files and what we do with the files that were matched. An expression is composed of a sequence of things: </p>
<dl>
<dt>Tests</p>
<dd> Tests return a true or false value, usually on the basis of some property of a file we are considering. The <code>-empty</code> test for example is true only when the current file is empty. </p>
<dt>Actions</p>
<dd> Actions have side effects (such as printing something on the standard output) and return either true or false, usually based on whether or not they are successful. The <code>-print</code> action for example prints the name of the current file on the standard output. </p>
<dt>Global options</p>
<dd> Global options affect the operation of tests and actions specified on any part of the command line. Global options always return true. The <code>-depth</code> option for example makes <code>find</code> traverse the file system in a depth-first order. </p>
<dt>Positional options</p>
<dd> Positional options affect only tests or actions which follow them. Positional options always return true. The <code>-regextype</code> option for example is positional, specifying the regular expression dialect for regular expressions occurring later on the command line. </p>
<dt>Operators</p>
<dd> Operators join together the other items within the expression. They include for example <code>-o</code> (meaning logical OR) and <code>-a</code> (meaning logical AND). Where an operator is missing, <code>-a</code> is assumed. </p>
</dl>
<p> The <code>-print</code> action is performed on all files for which the whole expression is true, unless it contains an action other than <code>-prune</code> or <code>-quit</code>. Actions which inhibit the default <code>-print</code> are <code>-delete</code>, <code>-exec</code>, <code>-execdir</code>, <code>-ok</code>, <code>-okdir</code>, <code>-fls</code>, <code>-fprint</code>, <code>-fprintf</code>, <code>-ls</code>, <code>-print</code> and <code>-printf</code>. </p>
<p> The <code>-delete</code> action also acts like an option (since it implies <code>-depth</code>). </p>
<h3>POSITIONAL OPTIONS</h3>
<p> Positional options always return true. They affect only tests occurring later on the command line. </p>
<dl>
<dt>-daystart</p>
<dd> Measure times (for <code>-amin</code>, <code>-atime</code>, <code>-cmin</code>, <code>-ctime</code>, <code>-mmin</code>, and <code>-mtime</code>) from the beginning of today rather than from 24 hours ago. This option only affects tests which appear later on the command line. </p>
<dt>-follow</p>
<dd> Deprecated; use the <code>-L</code> option instead. Dereference symbolic links. Implies <code>-noleaf</code>. The <code>-follow</code> option affects only those tests which appear after it on the command line. Unless the <code>-H</code> or <code>-L</code> option has been specified, the position of the <code>-follow</code> option changes the behaviour of the <code>-newer</code> predicate; any files listed as the argument of <code>-newer</code> will be dereferenced if they are symbolic links. The same consideration applies to <code>-newerXY</code>, <code>-anewer</code> and <code>-cnewer</code>. Similarly, the <code>-type</code> predicate will always match against the type of the file that a symbolic link points to rather than the link itself. Using <code>-follow</code> causes the <code>-lname and</code> <code>-ilname</code> predicates always to return false. </p>
<dt>-regextype <i>type</i></p>
<dd> Changes the regular expression syntax understood by <code>-regex</code> and <code>-iregex</code> tests which occur later on the command line. To see which regular expression types are known, use <code>-regextype help</code>. The Texinfo documentation (see <code>SEE</code> <code>ALSO</code>) explains the meaning of and differences between the various types of regular expression. </p>
<dt>-warn, -nowarn</p>
<dd> Turn warning messages on or off. These warnings apply only to the command line usage, not to any conditions that <code>find</code> might encounter when it searches directories. The default behaviour corresponds to <code>-warn</code> if standard input is a tty, and to <code>-nowarn</code> otherwise. If a warning message relating to command-line usage is produced, the exit status of <code>find</code> is not affected. If the POSIXLY_CORRECT environment variable is set, and <code>-warn</code> is also used, it is not specified which, if any, warnings will be active. </p>
</dl>
<h3>GLOBAL OPTIONS</h3>
<p> Global options always return true. Global options take effect even for tests which occur earlier on the command line. To prevent confusion, global options should specified on the command-line after the list of start points, just before the first test, positional option or action. If you specify a global option in some other place, <code>find</code> will issue a warning message explaining that this can be confusing. </p>
<p> The global options occur after the list of start points, and so are not the same kind of option as <code>-L</code>, for example. </p>
<dl>
<dt>-d</p>
<dd> A synonym for -depth, for compatibility with FreeBSD, NetBSD, MacOS X and OpenBSD. </p>
<dt>-depth</p>
<dd> Process each directory&#8217;s contents before the directory itself. The -delete action also implies <code>-depth</code>. </p>
<dt>-help, &#8211;help</p>
<dd> Print a summary of the command-line usage of <code>find</code> and exit. </p>
<dt>-ignore_readdir_race</p>
<dd> Normally, <code>find</code> will emit an error message when it fails to stat a file. If you give this option and a file is deleted between the time <code>find</code> reads the name of the file from the directory and the time it tries to stat the file, no error message will be issued. This also applies to files or directories whose names are given on the command line. This option takes effect at the time the command line is read, which means that you cannot search one part of the filesystem with this option on and part of it with this option off (if you need to do that, you will need to issue two <code>find</code> commands instead, one with the option and one without it). </p>
<p> Furthermore, <code>find</code> with the <code>-ignore_readdir_race</code> option will ignore errors of the <code>-delete</code> action in the case the file has disappeared since the parent directory was read: it will not output an error diagnostic, and the return code of the <code>-delete</code> action will be true. </p>
<dt>-maxdepth <i>levels</i></p>
<dd> Descend at most <i>levels</i> (a non-negative integer) levels of directories below the starting-points. Using <code>-maxdepth 0</code> means only apply the tests and actions to the starting-points themselves. </p>
<dt>-mindepth <i>levels</i></p>
<dd> Do not apply any tests or actions at levels less than <i>levels</i> (a non-negative integer). Using <code>-mindepth 1</code> means process all files except the starting-points. </p>
<dt>-mount</p>
<dd> Don&#8217;t descend directories on other filesystems. An alternate name for <code>-xdev</code>, for compatibility with some other versions of <code>find</code>. </p>
<dt>-noignore_readdir_race</p>
<dd> Turns off the effect of <code>-ignore_readdir_race</code>. </p>
<dt>-noleaf</p>
<dd> Do not optimize by assuming that directories contain 2 fewer subdirectories than their hard link count. This option is needed when searching filesystems that do not follow the Unix directory-link convention, such as CD-ROM or MS-DOS filesystems or AFS volume mount points. Each directory on a normal Unix filesystem has at least 2 hard links: its name and its `.&#8217; entry. Additionally, its subdirectories (if any) each have a `..&#8217; entry linked to that directory. When <code>find</code> is examining a directory, after it has statted 2 fewer subdirectories than the directory&#8217;s link count, it knows that the rest of the entries in the directory are non-directories (`leaf&#8217; files in the directory tree). If only the files&#8217; names need to be examined, there is no need to stat them; this gives a significant increase in search speed. </p>
<dt>-version, &#8211;version</p>
<dd> Print the <code>find</code> version number and exit. </p>
<dt>-xdev</p>
<dd> Don&#8217;t descend directories on other filesystems. </p>
</dl>
<h3>TESTS</h3>
<p> Some tests, for example <code>-newerXY</code> and <code>-samefile</code>, allow comparison between the file currently being examined and some reference file specified on the command line. When these tests are used, the interpretation of the reference file is determined by the options <code>-H</code>, <code>-L</code> and <code>-P</code> and any previous <code>-follow</code>, but the reference file is only examined once, at the time the command line is parsed. If the reference file cannot be examined (for example, the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) system call fails for it), an error message is issued, and <code>find</code> exits with a nonzero status. </p>
<p> A numeric argument <i>n</i> can be specified to tests (like <code>-amin</code>, <code>-mtime</code>, <code>-gid</code>, <code>-inum</code>, <code>-links</code>, <code>-size</code>, <code>-uid</code> and <code>-used</code>) as</p>
<dl>
<dt><i>+n</i></p>
<dd> for greater than <i>n</i>,</p>
<dt><i>-n</i></p>
<dd> for less than <i>n</i>,</p>
<dt><i>n</i></p>
<dd> for exactly <i>n</i>.</dl>
<p> Supported tests: </p>
<dl>
<dt>-amin <i>n</i></p>
<dd> File was last accessed less than, more than or exactly <i>n</i> minutes ago. </p>
<dt>-anewer <i>reference</i></p>
<dd> Time of the last access of the current file is more recent than that of the last data modification of the <i>reference</i> file. If <i>reference</i> is a symbolic link and the <code>-H</code> option or the <code>-L</code> option is in effect, then the time of the last data modification of the file it points to is always used. </p>
<dt>-atime <i>n</i></p>
<dd> File was last accessed less than, more than or exactly <i>n</i>*24 hours ago. When find figures out how many 24-hour periods ago the file was last accessed, any fractional part is ignored, so to match <code>-atime&nbsp;+1</code>, a file has to have been accessed at least <i>two</i> days ago. </p>
<dt>-cmin <i>n</i></p>
<dd> File&#8217;s status was last changed less than, more than or exactly <i>n</i> minutes ago. </p>
<dt>-cnewer <i>reference</i></p>
<dd> Time of the last status change of the current file is more recent than that of the last data modification of the <i>reference</i> file. If <i>reference</i> is a symbolic link and the <code>-H</code> option or the <code>-L</code> option is in effect, then the time of the last data modification of the file it points to is always used. </p>
<dt>-ctime <i>n</i></p>
<dd> File&#8217;s status was last changed less than, more than or exactly <i>n</i>*24 hours ago. See the comments for <code>-atime</code> to understand how rounding affects the interpretation of file status change times. </p>
<dt>-empty</p>
<dd> File is empty and is either a regular file or a directory. </p>
<dt>-executable</p>
<dd> Matches files which are executable and directories which are searchable (in a file name resolution sense) by the current user. This takes into account access control lists and other permissions artefacts which the <code>-perm</code> test ignores. This test makes use of the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) system call, and so can be fooled by NFS servers which do UID mapping (or root-squashing), since many systems implement <code><a href="/docs/linux/man/2-access/">access</a></code>(2) in the client&#8217;s kernel and so cannot make use of the UID mapping information held on the server. Because this test is based only on the result of the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) system call, there is no guarantee that a file for which this test succeeds can actually be executed. </p>
<dt>-false</p>
<dd> Always false. </p>
<dt>-fstype <i>type</i></p>
<dd> File is on a filesystem of type <i>type</i>. The valid filesystem types vary among different versions of Unix; an incomplete list of filesystem types that are accepted on some version of Unix or another is: ufs, 4.2, 4.3, nfs, tmp, mfs, S51K, S52K. You can use <code>-printf</code> with the %F directive to see the types of your filesystems. </p>
<dt>-gid <i>n</i></p>
<dd> File&#8217;s numeric group ID is less than, more than or exactly <i>n</i>. </p>
<dt>-group <i>gname</i></p>
<dd> File belongs to group <i>gname</i> (numeric group ID allowed). </p>
<dt>-ilname <i>pattern</i></p>
<dd> Like <code>-lname</code>, but the match is case insensitive. If the <code>-L</code> option or the <code>-follow</code> option is in effect, this test returns false unless the symbolic link is broken. </p>
<dt>-iname <i>pattern</i></p>
<dd> Like <code>-name</code>, but the match is case insensitive. For example, the patterns `fo*&#8217; and `F??&#8217; match the file names `Foo&#8217;, `FOO&#8217;, `foo&#8217;, `fOo&#8217;, etc. The pattern `*foo*` will also match a file called &#8216;.foobar&#8217;. </p>
<dt>-inum <i>n</i></p>
<dd> File has inode number smaller than, greater than or exactly <i>n</i>. It is normally easier to use the <code>-samefile</code> test instead. </p>
<dt>-ipath <i>pattern</i></p>
<dd> Like <code>-path</code>. but the match is case insensitive. </p>
<dt>-iregex <i>pattern</i></p>
<dd> Like <code>-regex</code>, but the match is case insensitive. </p>
<dt>-iwholename <i>pattern</i></p>
<dd> See -ipath. This alternative is less portable than <code>-ipath</code>. </p>
<dt>-links <i>n</i></p>
<dd> File has less than, more than or exactly <i>n</i> hard links. </p>
<dt>-lname <i>pattern</i></p>
<dd> File is a symbolic link whose contents match shell pattern <i>pattern</i>. The metacharacters do not treat `/&#8217; or `.&#8217; specially. If the <code>-L</code> option or the <code>-follow</code> option is in effect, this test returns false unless the symbolic link is broken. </p>
<dt>-mmin <i>n</i></p>
<dd> File&#8217;s data was last modified less than, more than or exactly <i>n</i> minutes ago. </p>
<dt>-mtime <i>n</i></p>
<dd> File&#8217;s data was last modified less than, more than or exactly <i>n</i>*24 hours ago. See the comments for <code>-atime</code> to understand how rounding affects the interpretation of file modification times. </p>
<dt>-name <i>pattern</i></p>
<dd> Base of file name (the path with the leading directories removed) matches shell pattern <i>pattern</i>. Because the leading directories are removed, the file names considered for a match with <code>-name</code> will never include a slash, so `-name a/b&#8217; will never match anything (you probably need to use <code>-path</code> instead). A warning is issued if you try to do this, unless the environment variable POSIXLY_CORRECT is set. The metacharacters (`*&#8217;, `?&#8217;, and `[]&#8217;) match a `.&#8217; at the start of the base name (this is a change in findutils-4.2.2; see section STANDARDS CONFORMANCE below). To ignore a directory and the files under it, use <code>-prune</code> rather than checking every file in the tree; see an example in the description of that action. Braces are not recognised as being special, despite the fact that some shells including Bash imbue braces with a special meaning in shell patterns. The filename matching is performed with the use of the <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3) library function. Don&#8217;t forget to enclose the pattern in quotes in order to protect it from expansion by the shell. </p>
<dt>-newer <i>reference</i></p>
<dd> Time of the last data modification of the current file is more recent than that of the last data modification of the <i>reference</i> file. If <i>reference</i> is a symbolic link and the <code>-H</code> option or the <code>-L</code> option is in effect, then the time of the last data modification of the file it points to is always used. </p>
<dt>-newerXY <i>reference</i></p>
<dd> Succeeds if timestamp <i>X</i> of the file being considered is newer than timestamp <i>Y</i> of the file <i>reference</i>. The letters <i>X</i> and <i>Y</i> can be any of the following letters: </p>
<table>
<tr VALIGN=top>
<td>a</td>
<td>The access time of the file <i>reference</i>
</td>
</tr>
<tr VALIGN=top>
<td>B</td>
<td>The birth time of the file <i>reference</i>
</td>
</tr>
<tr VALIGN=top>
<td>c</td>
<td>The inode status change time of <i>reference</i>
</td>
</tr>
<tr VALIGN=top>
<td>m</td>
<td>The modification time of the file <i>reference</i>
</td>
</tr>
<tr VALIGN=top>
<td>t</td>
<td><i>reference</i> is interpreted directly as a time
</td>
</tr>
</table>
<p> Some combinations are invalid; for example, it is invalid for <i>X</i> to be <i>t</i>. Some combinations are not implemented on all systems; for example <i>B</i> is not supported on all systems. If an invalid or unsupported combination of <i>XY</i> is specified, a fatal error results. Time specifications are interpreted as for the argument to the <code>-d</code> option of GNU <code>date</code>. If you try to use the birth time of a reference file, and the birth time cannot be determined, a fatal error message results. If you specify a test which refers to the birth time of files being examined, this test will fail for any files where the birth time is unknown. </p>
<dt>-nogroup</p>
<dd> No group corresponds to file&#8217;s numeric group ID. </p>
<dt>-nouser</p>
<dd> No user corresponds to file&#8217;s numeric user ID. </p>
<dt>-path <i>pattern</i></p>
<dd> File name matches shell pattern <i>pattern</i>. The metacharacters do not treat `/&#8217; or `.&#8217; specially; so, for example, </p>
<pre>
find . -path &quot;./sr*sc&quot;
</pre>
<p> will print an entry for a directory called <i>./src/misc</i> (if one exists). To ignore a whole directory tree, use <code>-prune</code> rather than checking every file in the tree. Note that the pattern match test applies to the whole file name, starting from one of the start points named on the command line. It would only make sense to use an absolute path name here if the relevant start point is also an absolute path. This means that this command will never match anything: </p>
<pre>
find bar -path /foo/bar/myfile -print
</pre>
<p> Find compares the <code>-path</code> argument with the concatenation of a directory name and the base name of the file it&#8217;s examining. Since the concatenation will never end with a slash, <code>-path</code> arguments ending in a slash will match nothing (except perhaps a start point specified on the command line). The predicate <code>-path</code> is also supported by HP-UX <code>find</code> and is part of the POSIX 2008 standard. </p>
<dt>-perm <i>mode</i></p>
<dd> File&#8217;s permission bits are exactly <i>mode</i> (octal or symbolic). Since an exact match is required, if you want to use this form for symbolic modes, you may have to specify a rather complex mode string. For example `-perm g=w&#8217; will only match files which have mode 0020 (that is, ones for which group write permission is the only permission set). It is more likely that you will want to use the `/&#8217; or `-&#8216; forms, for example `-perm -g=w&#8217;, which matches any file with group write permission. See the <code>EXAMPLES</code> section for some illustrative examples. </p>
<dt>-perm &#8211;<i>mode</i></p>
<dd> All of the permission bits <i>mode</i> are set for the file. Symbolic modes are accepted in this form, and this is usually the way in which you would want to use them. You must specify `u&#8217;, `g&#8217; or `o&#8217; if you use a symbolic mode. See the <code>EXAMPLES</code> section for some illustrative examples. </p>
<dt>-perm /<i>mode</i></p>
<dd> Any of the permission bits <i>mode</i> are set for the file. Symbolic modes are accepted in this form. You must specify `u&#8217;, `g&#8217; or `o&#8217; if you use a symbolic mode. See the <code>EXAMPLES</code> section for some illustrative examples. If no permission bits in <i>mode</i> are set, this test matches any file (the idea here is to be consistent with the behaviour of <code>-perm -000</code>). </p>
<dt>-perm +<i>mode</i></p>
<dd> This is no longer supported (and has been deprecated since 2005). Use <code>-perm /</code><i>mode</i> instead. </p>
<dt>-readable</p>
<dd> Matches files which are readable by the current user. This takes into account access control lists and other permissions artefacts which the <code>-perm</code> test ignores. This test makes use of the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) system call, and so can be fooled by NFS servers which do UID mapping (or root-squashing), since many systems implement <code><a href="/docs/linux/man/2-access/">access</a></code>(2) in the client&#8217;s kernel and so cannot make use of the UID mapping information held on the server. </p>
<dt>-regex <i>pattern</i></p>
<dd> File name matches regular expression <i>pattern</i>. This is a match on the whole path, not a search. For example, to match a file named <i>./fubar3,</i> you can use the regular expression `.*bar.&#8217; or `.*b.*3&#8242;, but not `f.*r3&#8242;. The regular expressions understood by <code>find</code> are by default Emacs Regular Expressions (except that `.&#8217; matches newline), but this can be changed with the <code>-regextype</code> option. </p>
<dt>-samefile <i>name</i></p>
<dd> File refers to the same inode as <i>name</i>. When <code>-L</code> is in effect, this can include symbolic links. </p>
<dt>-size <i>n</i>[cwbkMG]</p>
<dd> File uses less than, more than or exactly <i>n</i> units of space, rounding up. The following suffixes can be used:</p>
<dl>
<dt>
<dd>
<dl>
<dt>`b&#8217;</p>
<dd> for 512-byte blocks (this is the default if no suffix is used)</p>
<dt>`c&#8217;</p>
<dd> for bytes</p>
<dt>`w&#8217;</p>
<dd> for two-byte words</p>
<dt>`k&#8217;</p>
<dd> for kibibytes (KiB, units of 1024 bytes)</p>
<dt>`M&#8217;</p>
<dd> for mebibytes (MiB, units of 1024 * 1024 = 1048576 bytes)</p>
<dt>`G&#8217;</p>
<dd> for gibibytes (GiB, units of 1024 * 1024 * 1024 = 1073741824 bytes)</dl>
</dl>
<dt>
<dd> The size is simply the st_size member of the struct stat populated by the lstat (or stat) system call, rounded up as shown above. In other words, it&#8217;s consistent with the result you get for <code>ls -l</code>. Bear in mind that the `%k&#8217; and `%b&#8217; format specifiers of <code>-printf</code> handle sparse files differently. The `b&#8217; suffix always denotes 512-byte blocks and never 1024-byte blocks, which is different to the behaviour of <code>-ls</code>.</p>
<dt>
<dd> The + and &#8211; prefixes signify greater than and less than, as usual; i.e., an exact size of <i>n</i> units does not match. Bear in mind that the size is rounded up to the next unit. Therefore <code>-size -1M</code> is not equivalent to <code>-size -1048576c</code>. The former only matches empty files, the latter matches files from 0 to 1,048,575 bytes.</p>
<dt>-true</p>
<dd> Always true. </p>
<dt>-type <i>c</i></p>
<dd> File is of type <i>c</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>b</p>
<dd> block (buffered) special</p>
<dt>c</p>
<dd> character (unbuffered) special</p>
<dt>d</p>
<dd> directory</p>
<dt>p</p>
<dd> named pipe (FIFO)</p>
<dt>f</p>
<dd> regular file</p>
<dt>l</p>
<dd> symbolic link; this is never true if the <code>-L</code> option or the <code>-follow</code> option is in effect, unless the symbolic link is broken. If you want to search for symbolic links when <code>-L</code> is in effect, use <code>-xtype</code>.</p>
<dt>s</p>
<dd> socket</p>
<dt>D</p>
<dd> door (Solaris)</dl>
</dl>
<dt>
<dd> To search for more than one type at once, you can supply the combined list of type letters separated by a comma `,&#8217; (GNU extension).</p>
<dt>-uid <i>n</i></p>
<dd> File&#8217;s numeric user ID is less than, more than or exactly <i>n</i>. </p>
<dt>-used <i>n</i></p>
<dd> File was last accessed less than, more than or exactly <i>n</i> days after its status was last changed. </p>
<dt>-user <i>uname</i></p>
<dd> File is owned by user <i>uname</i> (numeric user ID allowed). </p>
<dt>-wholename <i>pattern</i></p>
<dd> See -path. This alternative is less portable than <code>-path</code>. </p>
<dt>-writable</p>
<dd> Matches files which are writable by the current user. This takes into account access control lists and other permissions artefacts which the <code>-perm</code> test ignores. This test makes use of the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) system call, and so can be fooled by NFS servers which do UID mapping (or root-squashing), since many systems implement <code><a href="/docs/linux/man/2-access/">access</a></code>(2) in the client&#8217;s kernel and so cannot make use of the UID mapping information held on the server. </p>
<dt>-xtype <i>c</i></p>
<dd> The same as <code>-type</code> unless the file is a symbolic link. For symbolic links: if the <code>-H</code> or <code>-P</code> option was specified, true if the file is a link to a file of type <i>c</i>; if the <code>-L</code> option has been given, true if <i>c</i> is `l&#8217;. In other words, for symbolic links, <code>-xtype</code> checks the type of the file that <code>-type</code> does not check.</p>
<dt>-context <i>pattern</i></p>
<dd> (SELinux only) Security context of the file matches glob <i>pattern</i>. </p>
</dl>
<h3>ACTIONS</h3>
<dl>
<dt>-delete</p>
<dd> Delete files; true if removal succeeded. If the removal failed, an error message is issued. If <code>-delete</code> fails, <code>find</code>&#8216;s exit status will be nonzero (when it eventually exits). Use of <code>-delete</code> automatically turns on the `<code>-depth</code>&#8216; option. </p>
<p> <code>Warnings</code>: Don&#8217;t forget that the find command line is evaluated as an expression, so putting <code>-delete</code> first will make <code>find</code> try to delete everything below the starting points you specified. When testing a <code>find</code> command line that you later intend to use with <code>-delete</code>, you should explicitly specify <code>-depth</code> in order to avoid later surprises. Because <code>-delete</code> implies <code>-depth</code>, you cannot usefully use <code>-prune</code> and <code>-delete</code> together. </p>
<p> Together with the <code>-ignore_readdir_race</code> option, <code>find</code> will ignore errors of the <code>-delete</code> action in the case the file has disappeared since the parent directory was read: it will not output an error diagnostic, and the return code of the <code>-delete</code> action will be true. </p>
<dt>-exec <i>command</i> ;</p>
<dd> Execute <i>command</i>; true if 0 status is returned. All following arguments to <code>find</code> are taken to be arguments to the command until an argument consisting of `;&#8217; is encountered. The string `{}&#8217; is replaced by the current file name being processed everywhere it occurs in the arguments to the command, not just in arguments where it is alone, as in some versions of <code>find</code>. Both of these constructions might need to be escaped (with a `\&#8217;) or quoted to protect them from expansion by the shell. See the <code>EXAMPLES</code> section for examples of the use of the <code>-exec</code> option. The specified command is run once for each matched file. The command is executed in the starting directory. There are unavoidable security problems surrounding use of the <code>-exec</code> action; you should use the <code>-execdir</code> option instead. </p>
<dt>-exec <i>command</i> {} +</p>
<dd> This variant of the <code>-exec</code> action runs the specified command on the selected files, but the command line is built by appending each selected file name at the end; the total number of invocations of the command will be much less than the number of matched files. The command line is built in much the same way that <code>xargs</code> builds its command lines. Only one instance of `{}&#8217; is allowed within the command, and it must appear at the end, immediately before the `+&#8217;; it needs to be escaped (with a `\&#8217;) or quoted to protect it from interpretation by the shell. The command is executed in the starting directory. If any invocation with the `+&#8217; form returns a non-zero value as exit status, then <code>find</code> returns a non-zero exit status. If <code>find</code> encounters an error, this can sometimes cause an immediate exit, so some pending commands may not be run at all. For this reason <code>-exec&nbsp;</code><i>my-command</i>&nbsp;&#8230;&nbsp;{}&nbsp;+&nbsp;-quit may not result in <i>my-command</i> actually being run. This variant of <code>-exec</code> always returns true. </p>
<dt>-execdir <i>command</i> ;</p>
<dd>
<dt>-execdir <i>command</i> {} +</p>
<dd> Like <code>-exec</code>, but the specified command is run from the subdirectory containing the matched file, which is not normally the directory in which you started <code>find</code>. As with -exec, the {} should be quoted if find is being invoked from a shell. This a much more secure method for invoking commands, as it avoids race conditions during resolution of the paths to the matched files. As with the <code>-exec</code> action, the `+&#8217; form of <code>-execdir</code> will build a command line to process more than one matched file, but any given invocation of <i>command</i> will only list files that exist in the same subdirectory. If you use this option, you must ensure that your <code>$PATH</code> environment variable does not reference `.&#8217;; otherwise, an attacker can run any commands they like by leaving an appropriately-named file in a directory in which you will run <code>-execdir</code>. The same applies to having entries in <code>$PATH</code> which are empty or which are not absolute directory names. If any invocation with the `+&#8217; form returns a non-zero value as exit status, then <code>find</code> returns a non-zero exit status. If <code>find</code> encounters an error, this can sometimes cause an immediate exit, so some pending commands may not be run at all. The result of the action depends on whether the <code>+</code> or the <code>;</code> variant is being used; <code>-execdir&nbsp;</code><i>command</i>&nbsp;{}&nbsp;+ always returns true, while <code>-execdir&nbsp;</code><i>command</i>&nbsp;{}&nbsp;; returns true only if <i>command</i> returns 0. </p>
<dt>-fls <i>file</i></p>
<dd> True; like <code>-ls</code> but write to <i>file</i> like <code>-fprint</code>. The output file is always created, even if the predicate is never matched. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
<dt>-fprint <i>file</i></p>
<dd> True; print the full file name into file <i>file</i>. If <i>file</i> does not exist when <code>find</code> is run, it is created; if it does exist, it is truncated. The file names <i>/dev/stdout</i> and <i>/dev/stderr</i> are handled specially; they refer to the standard output and standard error output, respectively. The output file is always created, even if the predicate is never matched. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
<dt>-fprint0 <i>file</i></p>
<dd> True; like <code>-print0</code> but write to <i>file</i> like <code>-fprint</code>. The output file is always created, even if the predicate is never matched. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
<dt>-fprintf <i>file</i> <i>format</i></p>
<dd> True; like <code>-printf</code> but write to <i>file</i> like <code>-fprint</code>. The output file is always created, even if the predicate is never matched. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
<dt>-ls</p>
<dd> True; list current file in <code>ls -dils</code> format on standard output. The block counts are of 1 KB blocks, unless the environment variable POSIXLY_CORRECT is set, in which case 512-byte blocks are used. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
<dt>-ok <i>command</i> ;</p>
<dd> Like <code>-exec</code> but ask the user first. If the user agrees, run the command. Otherwise just return false. If the command is run, its standard input is redirected from <i>/dev/null</i>. </p>
<dt>
<dd> The response to the prompt is matched against a pair of regular expressions to determine if it is an affirmative or negative response. This regular expression is obtained from the system if the `POSIXLY_CORRECT&#8217; environment variable is set, or otherwise from <code>find</code>&#8216;s message translations. If the system has no suitable definition, <code>find</code>&#8216;s own definition will be used. In either case, the interpretation of the regular expression itself will be affected by the environment variables &#8216;LC_CTYPE&#8217; (character classes) and &#8216;LC_COLLATE&#8217; (character ranges and equivalence classes). </p>
<dt>-okdir <i>command</i> ;</p>
<dd> Like <code>-execdir</code> but ask the user first in the same way as for <code>-ok</code>. If the user does not agree, just return false. If the command is run, its standard input is redirected from <i>/dev/null</i>. </p>
<dt>-print</p>
<dd> True; print the full file name on the standard output, followed by a newline. If you are piping the output of <code>find</code> into another program and there is the faintest possibility that the files which you are searching for might contain a newline, then you should seriously consider using the <code>-print0</code> option instead of <code>-print</code>. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
<dt>-print0</p>
<dd> True; print the full file name on the standard output, followed by a null character (instead of the newline character that <code>-print</code> uses). This allows file names that contain newlines or other types of white space to be correctly interpreted by programs that process the <code>find</code> output. This option corresponds to the <code>-0</code> option of <code>xargs</code>. </p>
<dt>-printf <i>format</i></p>
<dd> True; print <i>format</i> on the standard output, interpreting `\&#8217; escapes and `%&#8217; directives. Field widths and precisions can be specified as with the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) C function. Please note that many of the fields are printed as %s rather than %d, and this may mean that flags don&#8217;t work as you might expect. This also means that the `-&#8216; flag does work (it forces fields to be left-aligned). Unlike <code>-print</code>, <code>-printf</code> does not add a newline at the end of the string. The escapes and directives are:</p>
<dl>
<dt>
<dd>
<dl>
<dt></p>
<dd> Alarm bell.</p>
<dt></p>
<dd> Backspace.</p>
<dt>
