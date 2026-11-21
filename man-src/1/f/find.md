---

title: "find(1)"
name: "find"
section: "1"
letter: "f"
url: "/docs/linux/man/1-find/"
description: "find – search for files in a directory hierarchy"
---

<p> find - search for files in a directory hierarchy </p>
<h2>SYNOPSIS</h2>
<p> <code>find</code> [-H] [-L] [-P] [-D debugopts] [-Olevel] [starting-point...] [expression]  </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the GNU version of <code>find</code>. GNU <code>find</code> searches the directory tree rooted at each given starting-point by evaluating the given expression from left to right, according to the rules of precedence (see section OPERATORS), until the outcome is known (the left hand side is false for <i>and</i> operations, true for <i>or</i>), at which point <code>find</code> moves on to the next file name. If no starting-point is specified, `.&#8216; is assumed. </p>
<p> If you are using <code>find</code> in an environment where security is important (for example if you are using it to search directories that are writable by other users), you should read the `Security Considerations&#8217; chapter of the findutils documentation, which is called <code>Finding Files</code> and comes with findutils. That document also includes a lot more detail and discussion than this manual page, so you may find it a more useful source of information.  </p>
<h2>OPTIONS</h2>
<p> The <code>-H</code>, <code>-L</code> and <code>-P</code> options control the treatment of symbolic links. Command-line arguments following these are taken to be names of files or directories to be examined, up to the first argument that begins with `-&#8216;, or the argument `(&#8216; or `!&#8216;. That argument and any following arguments are taken to be the expression describing what is to be searched for. If no paths are given, the current directory is used. If no expression is given, the expression <code>-print</code> is used (but you should probably consider using <code>-print0</code> instead, anyway). </p>
<p> This manual page talks about `options&#8217; within the expression list. These options control the behaviour of <code>find</code> but are specified immediately after the last path name. The five `real&#8217; options <code>-H</code>, <code>-L</code>, <code>-P</code>, <code>-D</code> and <code>-O</code> must appear before the first path name, if at all. A double dash <code>--</code> could theoretically be used to signal that any remaining arguments are not options, but this does not really work due to the way <code>find</code> determines the end of the following path arguments: it does that by reading until an expression argument comes (which also starts with a `-&#8216;). Now, if a path argument would start with a `-&#8216;, then <code>find</code> would treat it as expression argument instead. Thus, to ensure that all start points are taken as such, and especially to prevent that wildcard patterns expanded by the calling shell are not mistakenly treated as expression arguments, it is generally safer to prefix wildcards or dubious path names with either `./&#8216; or to use absolute path names starting with &#8216;/&#8216;. </p>
<dl>
<dt>-P</dt>
<dd> <p> Never follow symbolic links. This is the default behaviour. When <code>find</code> examines or prints information about files, and the file is a symbolic link, the information used shall be taken from the properties of the symbolic link itself. </p>
 </dd>
<dt>-L</dt>
<dd> <p> Follow symbolic links. When <code>find</code> examines or prints information about files, the information used shall be taken from the properties of the file to which the link points, not from the link itself (unless it is a broken symbolic link or <code>find</code> is unable to examine the file to which the link points). Use of this option implies <code>-noleaf</code>. If you later use the <code>-P</code> option, <code>-noleaf</code> will still be in effect. If <code>-L</code> is in effect and <code>find</code> discovers a symbolic link to a subdirectory during its search, the subdirectory pointed to by the symbolic link will be searched. </p>
 </dd>
<dd> <p> When the <code>-L</code> option is in effect, the <code>-type</code> predicate will always match against the type of the file that a symbolic link points to rather than the link itself (unless the symbolic link is broken). Actions that can cause symbolic links to become broken while <code>find</code> is executing (for example <code>-delete</code>) can give rise to confusing behaviour. Using <code>-L</code> causes the <code>-lname</code> and <code>-ilname</code> predicates always to return false. </p>
 </dd>
<dt>-H</dt>
<dd> <p> Do not follow symbolic links, except while processing the command line arguments. When <code>find</code> examines or prints information about files, the information used shall be taken from the properties of the symbolic link itself. The only exception to this behaviour is when a file specified on the command line is a symbolic link, and the link can be resolved. For that situation, the information used is taken from whatever the link points to (that is, the link is followed). The information about the link itself is used as a fallback if the file pointed to by the symbolic link cannot be examined. If <code>-H</code> is in effect and one of the paths specified on the command line is a symbolic link to a directory, the contents of that directory will be examined (though of course <code>-maxdepth 0</code> would prevent this). </p>
 </dd></dl>
<p> If more than one of <code>-H</code>, <code>-L</code> and <code>-P</code> is specified, each overrides the others; the last one appearing on the command line takes effect. Since it is the default, the <code>-P</code> option should be considered to be in effect unless either <code>-H</code> or <code>-L</code> is specified. </p>
<p> GNU <code>find</code> frequently stats files during the processing of the command line itself, before any searching has begun. These options also affect how those arguments are processed. Specifically, there are a number of tests that compare files listed on the command line against a file we are currently considering. In each case, the file specified on the command line will have been examined and some of its properties will have been saved. If the named file is in fact a symbolic link, and the <code>-P</code> option is in effect (or if neither <code>-H</code> nor <code>-L</code> were specified), the information used for the comparison will be taken from the properties of the symbolic link. Otherwise, it will be taken from the properties of the file the link points to. If <code>find</code> cannot follow the link (for example because it has insufficient privileges or the link points to a nonexistent file) the properties of the link itself will be used. </p>
<p> When the <code>-H</code> or <code>-L</code> options are in effect, any symbolic links listed as the argument of <code>-newer</code> will be dereferenced, and the timestamp will be taken from the file to which the symbolic link points. The same consideration applies to <code>-newerXY</code>, <code>-anewer</code> and <code>-cnewer</code>. </p>
<p> The <code>-follow</code> option has a similar effect to <code>-L</code>, though it takes effect at the point where it appears (that is, if <code>-L</code> is not used but <code>-follow</code> is, any symbolic links appearing after <code>-follow</code> on the command line will be dereferenced, and those before it will not). </p>
<dl>
<dt>-D debugopts</dt>
<dd> <p> Print diagnostic information; this can be helpful to diagnose problems with why <code>find</code> is not doing what you want. The list of debug options should be comma separated. Compatibility of the debug options is not guaranteed between releases of findutils. For a complete list of valid debug options, see the output of <code>find -D help</code>. Valid debug options include </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>exec</dt>
<dd> <p> Show diagnostic information relating to -exec, -execdir, -ok and -okdir </p>
 </dd>
<dt>opt</dt>
<dd> <p> Prints diagnostic information relating to the optimisation of the expression tree; see the -O option. </p>
 </dd>
<dt>rates</dt>
<dd> <p> Prints a summary indicating how often each predicate succeeded or failed. </p>
 </dd>
<dt>search</dt>
<dd> <p> Navigate the directory tree verbosely. </p>
 </dd>
<dt>stat</dt>
<dd> <p> Print messages as files are examined with the <code>stat</code> and <code>lstat</code> system calls. The <code>find</code> program tries to minimise such calls. </p>
 </dd>
<dt>tree</dt>
<dd> <p> Show the expression tree in its original and optimised form. </p>
 </dd>
<dt>all</dt>
<dd> <p> Enable all of the other debug options (but <code>help</code>). </p>
 </dd>
<dt>help</dt>
<dd> <p> Explain the debugging options. </p>
 </dd></dl>
</dl>
<dt>-Olevel</dt>
<dd> <p> Enables query optimisation. The <code>find</code> program reorders tests to speed up execution while preserving the overall effect; that is, predicates with side effects are not reordered relative to each other. The optimisations performed at each optimisation level are as follows. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>0</dt>
<dd> <p> Equivalent to optimisation level 1. </p>
 </dd>
<dt>1</dt>
<dd> <p> This is the default optimisation level and corresponds to the traditional behaviour. Expressions are reordered so that tests based only on the names of files (for example <code>-name</code> and <code>-regex</code>) are performed first. </p>
 </dd>
<dt>2</dt>
<dd> <p> Any <code>-type</code> or <code>-xtype</code> tests are performed after any tests based only on the names of files, but before any tests that require information from the inode. On many modern versions of Unix, file types are returned by <code>readdir()</code> and so these predicates are faster to evaluate than predicates which need to stat the file first. If you use the <code>-fstype&nbsp;</code><i>FOO</i> predicate and specify a filesystem type <i>FOO</i> which is not known (that is, present in `/etc/mtab&#8217;) at the time <code>find</code> starts, that predicate is equivalent to <code>-false</code>. </p>
 </dd>
<dt>3</dt>
<dd> <p> At this optimisation level, the full cost-based query optimiser is enabled. The order of tests is modified so that cheap (i.e. fast) tests are performed first and more expensive ones are performed later, if necessary. Within each cost band, predicates are evaluated earlier or later according to whether they are likely to succeed or not. For <code>-o</code>, predicates which are likely to succeed are evaluated earlier, and for <code>-a</code>, predicates which are likely to fail are evaluated earlier. </p>
 </dd></dl>
</dl>
<dd> <p> The cost-based optimiser has a fixed idea of how likely any given test is to succeed. In some cases the probability takes account of the specific nature of the test (for example, <code>-type f</code> is assumed to be more likely to succeed than <code>-type c</code>). The cost-based optimiser is currently being evaluated. If it does not actually improve the performance of <code>find</code>, it will be removed again. Conversely, optimisations that prove to be reliable, robust and effective may be enabled at lower optimisation levels over time. However, the default behaviour (i.e. optimisation level 1) will not be changed in the 4.3.x release series. The findutils test suite runs all the tests on <code>find</code> at each optimisation level and ensures that the result is the same. </p>
 </dd></dl>
<h2>EXPRESSION</h2>
<p> The part of the command line after the list of starting points is the <i>expression</i>. This is a kind of query specification describing how we match files and what we do with the files that were matched. An expression is composed of a sequence of things: </p>
<dl>
<dt>Tests</dt>
<dd> <p> Tests return a true or false value, usually on the basis of some property of a file we are considering. The <code>-empty</code> test for example is true only when the current file is empty. </p>
 </dd>
<dt>Actions</dt>
<dd> <p> Actions have side effects (such as printing something on the standard output) and return either true or false, usually based on whether or not they are successful. The <code>-print</code> action for example prints the name of the current file on the standard output. </p>
 </dd>
<dt>Global options</dt>
<dd> <p> Global options affect the operation of tests and actions specified on any part of the command line. Global options always return true. The <code>-depth</code> option for example makes <code>find</code> traverse the file system in a depth-first order. </p>
 </dd>
<dt>Positional options</dt>
<dd> <p> Positional options affect only tests or actions which follow them. Positional options always return true. The <code>-regextype</code> option for example is positional, specifying the regular expression dialect for regular expressions occurring later on the command line. </p>
 </dd>
<dt>Operators</dt>
<dd> <p> Operators join together the other items within the expression. They include for example <code>-o</code> (meaning logical OR) and <code>-a</code> (meaning logical AND). Where an operator is missing, <code>-a</code> is assumed. </p>
 </dd></dl>
<p> The <code>-print</code> action is performed on all files for which the whole expression is true, unless it contains an action other than <code>-prune</code> or <code>-quit</code>. Actions which inhibit the default <code>-print</code> are <code>-delete</code>, <code>-exec</code>, <code>-execdir</code>, <code>-ok</code>, <code>-okdir</code>, <code>-fls</code>, <code>-fprint</code>, <code>-fprintf</code>, <code>-ls</code>, <code>-print</code> and <code>-printf</code>. </p>
<p> The <code>-delete</code> action also acts like an option (since it implies <code>-depth</code>). </p>
<h3>POSITIONAL OPTIONS</h3>
<p> Positional options always return true. They affect only tests occurring later on the command line. </p>
<dl>
<dt>-daystart</dt>
<dd> <p> Measure times (for <code>-amin</code>, <code>-atime</code>, <code>-cmin</code>, <code>-ctime</code>, <code>-mmin</code>, and <code>-mtime</code>) from the beginning of today rather than from 24 hours ago. This option only affects tests which appear later on the command line. </p>
 </dd>
<dt>-follow</dt>
<dd> <p> Deprecated; use the <code>-L</code> option instead. Dereference symbolic links. Implies <code>-noleaf</code>. The <code>-follow</code> option affects only those tests which appear after it on the command line. Unless the <code>-H</code> or <code>-L</code> option has been specified, the position of the <code>-follow</code> option changes the behaviour of the <code>-newer</code> predicate; any files listed as the argument of <code>-newer</code> will be dereferenced if they are symbolic links. The same consideration applies to <code>-newerXY</code>, <code>-anewer</code> and <code>-cnewer</code>. Similarly, the <code>-type</code> predicate will always match against the type of the file that a symbolic link points to rather than the link itself. Using <code>-follow</code> causes the <code>-lname and</code> <code>-ilname</code> predicates always to return false. </p>
 </dd>
<dt>-regextype <i>type</i></dt>
<dd> <p> Changes the regular expression syntax understood by <code>-regex</code> and <code>-iregex</code> tests which occur later on the command line. To see which regular expression types are known, use <code>-regextype help</code>. The Texinfo documentation (see <code>SEE</code> <code>ALSO</code>) explains the meaning of and differences between the various types of regular expression. </p>
 </dd>
<dt>-warn, -nowarn</dt>
<dd> <p> Turn warning messages on or off. These warnings apply only to the command line usage, not to any conditions that <code>find</code> might encounter when it searches directories. The default behaviour corresponds to <code>-warn</code> if standard input is a tty, and to <code>-nowarn</code> otherwise. If a warning message relating to command-line usage is produced, the exit status of <code>find</code> is not affected. If the POSIXLY_CORRECT environment variable is set, and <code>-warn</code> is also used, it is not specified which, if any, warnings will be active. </p>
 </dd></dl>
<h3>GLOBAL OPTIONS</h3>
<p> Global options always return true. Global options take effect even for tests which occur earlier on the command line. To prevent confusion, global options should specified on the command-line after the list of start points, just before the first test, positional option or action. If you specify a global option in some other place, <code>find</code> will issue a warning message explaining that this can be confusing. </p>
<p> The global options occur after the list of start points, and so are not the same kind of option as <code>-L</code>, for example. </p>
<dl>
<dt>-d</dt>
<dd> <p> A synonym for -depth, for compatibility with FreeBSD, NetBSD, MacOS X and OpenBSD. </p>
 </dd>
<dt>-depth</dt>
<dd> <p> Process each directory&#8217;s contents before the directory itself. The -delete action also implies <code>-depth</code>. </p>
 </dd>
<dt>-help, --help</dt>
<dd> <p> Print a summary of the command-line usage of <code>find</code> and exit. </p>
 </dd>
<dt>-ignore_readdir_race</dt>
<dd> <p> Normally, <code>find</code> will emit an error message when it fails to stat a file. If you give this option and a file is deleted between the time <code>find</code> reads the name of the file from the directory and the time it tries to stat the file, no error message will be issued. This also applies to files or directories whose names are given on the command line. This option takes effect at the time the command line is read, which means that you cannot search one part of the filesystem with this option on and part of it with this option off (if you need to do that, you will need to issue two <code>find</code> commands instead, one with the option and one without it). </p>
<p> Furthermore, <code>find</code> with the <code>-ignore_readdir_race</code> option will ignore errors of the <code>-delete</code> action in the case the file has disappeared since the parent directory was read: it will not output an error diagnostic, and the return code of the <code>-delete</code> action will be true. </p>
 </dd>
<dt>-maxdepth <i>levels</i></dt>
<dd> <p> Descend at most <i>levels</i> (a non-negative integer) levels of directories below the starting-points. Using <code>-maxdepth 0</code> means only apply the tests and actions to the starting-points themselves. </p>
 </dd>
<dt>-mindepth <i>levels</i></dt>
<dd> <p> Do not apply any tests or actions at levels less than <i>levels</i> (a non-negative integer). Using <code>-mindepth 1</code> means process all files except the starting-points. </p>
 </dd>
<dt>-mount</dt>
<dd> <p> Don&#8217;t descend directories on other filesystems. An alternate name for <code>-xdev</code>, for compatibility with some other versions of <code>find</code>. </p>
 </dd>
<dt>-noignore_readdir_race</dt>
<dd> <p> Turns off the effect of <code>-ignore_readdir_race</code>. </p>
 </dd>
<dt>-noleaf</dt>
<dd> <p> Do not optimize by assuming that directories contain 2 fewer subdirectories than their hard link count. This option is needed when searching filesystems that do not follow the Unix directory-link convention, such as CD-ROM or MS-DOS filesystems or AFS volume mount points. Each directory on a normal Unix filesystem has at least 2 hard links: its name and its `.&#8216; entry. Additionally, its subdirectories (if any) each have a `..&#8216; entry linked to that directory. When <code>find</code> is examining a directory, after it has statted 2 fewer subdirectories than the directory&#8217;s link count, it knows that the rest of the entries in the directory are non-directories (`leaf&#8217; files in the directory tree). If only the files&#8217; names need to be examined, there is no need to stat them; this gives a significant increase in search speed. </p>
 </dd>
<dt>-version, --version</dt>
<dd> <p> Print the <code>find</code> version number and exit. </p>
 </dd>
<dt>-xdev</dt>
<dd> <p> Don&#8217;t descend directories on other filesystems. </p>
 </dd></dl>
<h3>TESTS</h3>
<p> Some tests, for example <code>-newerXY</code> and <code>-samefile</code>, allow comparison between the file currently being examined and some reference file specified on the command line. When these tests are used, the interpretation of the reference file is determined by the options <code>-H</code>, <code>-L</code> and <code>-P</code> and any previous <code>-follow</code>, but the reference file is only examined once, at the time the command line is parsed. If the reference file cannot be examined (for example, the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) system call fails for it), an error message is issued, and <code>find</code> exits with a nonzero status. </p>
<p> A numeric argument <i>n</i> can be specified to tests (like <code>-amin</code>, <code>-mtime</code>, <code>-gid</code>, <code>-inum</code>, <code>-links</code>, <code>-size</code>, <code>-uid</code> and <code>-used</code>) as </p>
<dl>
<dt><i>+n</i></dt>
<dd> <p> for greater than <i>n</i>, </p>
 </dd>
<dt><i>-n</i></dt>
<dd> <p> for less than <i>n</i>, </p>
 </dd>
<dt><i>n</i></dt>
<dd> <p> for exactly <i>n</i>. </p>
 </dd></dl>
<p> Supported tests: </p>
<dl>
<dt>-amin <i>n</i></dt>
<dd> <p> File was last accessed less than, more than or exactly <i>n</i> minutes ago. </p>
 </dd>
<dt>-anewer <i>reference</i></dt>
<dd> <p> Time of the last access of the current file is more recent than that of the last data modification of the <i>reference</i> file. If <i>reference</i> is a symbolic link and the <code>-H</code> option or the <code>-L</code> option is in effect, then the time of the last data modification of the file it points to is always used. </p>
 </dd>
<dt>-atime <i>n</i></dt>
<dd> <p> File was last accessed less than, more than or exactly <i>n</i>*24 hours ago. When find figures out how many 24-hour periods ago the file was last accessed, any fractional part is ignored, so to match <code>-atime&nbsp;+1</code>, a file has to have been accessed at least <i>two</i> days ago. </p>
 </dd>
<dt>-cmin <i>n</i></dt>
<dd> <p> File&#8217;s status was last changed less than, more than or exactly <i>n</i> minutes ago. </p>
 </dd>
<dt>-cnewer <i>reference</i></dt>
<dd> <p> Time of the last status change of the current file is more recent than that of the last data modification of the <i>reference</i> file. If <i>reference</i> is a symbolic link and the <code>-H</code> option or the <code>-L</code> option is in effect, then the time of the last data modification of the file it points to is always used. </p>
 </dd>
<dt>-ctime <i>n</i></dt>
<dd> <p> File&#8217;s status was last changed less than, more than or exactly <i>n</i>*24 hours ago. See the comments for <code>-atime</code> to understand how rounding affects the interpretation of file status change times. </p>
 </dd>
<dt>-empty</dt>
<dd> <p> File is empty and is either a regular file or a directory. </p>
 </dd>
<dt>-executable</dt>
<dd> <p> Matches files which are executable and directories which are searchable (in a file name resolution sense) by the current user. This takes into account access control lists and other permissions artefacts which the <code>-perm</code> test ignores. This test makes use of the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) system call, and so can be fooled by NFS servers which do UID mapping (or root-squashing), since many systems implement <code><a href="/docs/linux/man/2-access/">access</a></code>(2) in the client&#8217;s kernel and so cannot make use of the UID mapping information held on the server. Because this test is based only on the result of the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) system call, there is no guarantee that a file for which this test succeeds can actually be executed. </p>
 </dd>
<dt>-false</dt>
<dd> <p> Always false. </p>
 </dd>
<dt>-fstype <i>type</i></dt>
<dd> <p> File is on a filesystem of type <i>type</i>. The valid filesystem types vary among different versions of Unix; an incomplete list of filesystem types that are accepted on some version of Unix or another is: ufs, 4.2, 4.3, nfs, tmp, mfs, S51K, S52K. You can use <code>-printf</code> with the %F directive to see the types of your filesystems. </p>
 </dd>
<dt>-gid <i>n</i></dt>
<dd> <p> File&#8217;s numeric group ID is less than, more than or exactly <i>n</i>. </p>
 </dd>
<dt>-group <i>gname</i></dt>
<dd> <p> File belongs to group <i>gname</i> (numeric group ID allowed). </p>
 </dd>
<dt>-ilname <i>pattern</i></dt>
<dd> <p> Like <code>-lname</code>, but the match is case insensitive. If the <code>-L</code> option or the <code>-follow</code> option is in effect, this test returns false unless the symbolic link is broken. </p>
 </dd>
<dt>-iname <i>pattern</i></dt>
<dd> <p> Like <code>-name</code>, but the match is case insensitive. For example, the patterns `fo*&#8216; and `F??&#8216; match the file names `Foo&#8217;, `FOO&#8217;, `foo&#8217;, `fOo&#8217;, etc. The pattern `*foo*` will also match a file called &#8216;.foobar&#8217;. </p>
 </dd>
<dt>-inum <i>n</i></dt>
<dd> <p> File has inode number smaller than, greater than or exactly <i>n</i>. It is normally easier to use the <code>-samefile</code> test instead. </p>
 </dd>
<dt>-ipath <i>pattern</i></dt>
<dd> <p> Like <code>-path</code>. but the match is case insensitive. </p>
 </dd>
<dt>-iregex <i>pattern</i></dt>
<dd> <p> Like <code>-regex</code>, but the match is case insensitive. </p>
 </dd>
<dt>-iwholename <i>pattern</i></dt>
<dd> <p> See -ipath. This alternative is less portable than <code>-ipath</code>. </p>
 </dd>
<dt>-links <i>n</i></dt>
<dd> <p> File has less than, more than or exactly <i>n</i> hard links. </p>
 </dd>
<dt>-lname <i>pattern</i></dt>
<dd> <p> File is a symbolic link whose contents match shell pattern <i>pattern</i>. The metacharacters do not treat `/&#8216; or `.&#8216; specially. If the <code>-L</code> option or the <code>-follow</code> option is in effect, this test returns false unless the symbolic link is broken. </p>
 </dd>
<dt>-mmin <i>n</i></dt>
<dd> <p> File&#8217;s data was last modified less than, more than or exactly <i>n</i> minutes ago. </p>
 </dd>
<dt>-mtime <i>n</i></dt>
<dd> <p> File&#8217;s data was last modified less than, more than or exactly <i>n</i>*24 hours ago. See the comments for <code>-atime</code> to understand how rounding affects the interpretation of file modification times. </p>
 </dd>
<dt>-name <i>pattern</i></dt>
<dd> <p> Base of file name (the path with the leading directories removed) matches shell pattern <i>pattern</i>. Because the leading directories are removed, the file names considered for a match with <code>-name</code> will never include a slash, so `-name a/b&#8217; will never match anything (you probably need to use <code>-path</code> instead). A warning is issued if you try to do this, unless the environment variable POSIXLY_CORRECT is set. The metacharacters (`*&#8216;, `?&#8216;, and `[]&#8216;) match a `.&#8216; at the start of the base name (this is a change in findutils-4.2.2; see section STANDARDS CONFORMANCE below). To ignore a directory and the files under it, use <code>-prune</code> rather than checking every file in the tree; see an example in the description of that action. Braces are not recognised as being special, despite the fact that some shells including Bash imbue braces with a special meaning in shell patterns. The filename matching is performed with the use of the <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3) library function. Don&#8217;t forget to enclose the pattern in quotes in order to protect it from expansion by the shell. </p>
 </dd>
<dt>-newer <i>reference</i></dt>
<dd> <p> Time of the last data modification of the current file is more recent than that of the last data modification of the <i>reference</i> file. If <i>reference</i> is a symbolic link and the <code>-H</code> option or the <code>-L</code> option is in effect, then the time of the last data modification of the file it points to is always used. </p>
 </dd>
<dt>-newerXY <i>reference</i></dt>
<dd> <p> Succeeds if timestamp <i>X</i> of the file being considered is newer than timestamp <i>Y</i> of the file <i>reference</i>. The letters <i>X</i> and <i>Y</i> can be any of the following letters: </p>
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
 </dd>
<dt>-nogroup</dt>
<dd> <p> No group corresponds to file&#8217;s numeric group ID. </p>
 </dd>
<dt>-nouser</dt>
<dd> <p> No user corresponds to file&#8217;s numeric user ID. </p>
 </dd>
<dt>-path <i>pattern</i></dt>
<dd> <p> File name matches shell pattern <i>pattern</i>. The metacharacters do not treat `/&#8216; or `.&#8216; specially; so, for example, </p>
<pre><code>find . -path &quot;./sr*sc&quot;
</code></pre>
<p> will print an entry for a directory called <i>./src/misc</i> (if one exists). To ignore a whole directory tree, use <code>-prune</code> rather than checking every file in the tree. Note that the pattern match test applies to the whole file name, starting from one of the start points named on the command line. It would only make sense to use an absolute path name here if the relevant start point is also an absolute path. This means that this command will never match anything: <br />
 </p>
<pre><code>find bar -path /foo/bar/myfile -print
</code></pre>
<p> Find compares the <code>-path</code> argument with the concatenation of a directory name and the base name of the file it&#8217;s examining. Since the concatenation will never end with a slash, <code>-path</code> arguments ending in a slash will match nothing (except perhaps a start point specified on the command line). The predicate <code>-path</code> is also supported by HP-UX <code>find</code> and is part of the POSIX 2008 standard. </p>
 </dd>
<dt>-perm <i>mode</i></dt>
<dd> <p> File&#8217;s permission bits are exactly <i>mode</i> (octal or symbolic). Since an exact match is required, if you want to use this form for symbolic modes, you may have to specify a rather complex mode string. For example `-perm g=w&#8217; will only match files which have mode 0020 (that is, ones for which group write permission is the only permission set). It is more likely that you will want to use the `/&#8216; or `-&#8216; forms, for example `-perm -g=w&#8217;, which matches any file with group write permission. See the <code>EXAMPLES</code> section for some illustrative examples. </p>
 </dd>
<dt>-perm -<i>mode</i></dt>
<dd> <p> All of the permission bits <i>mode</i> are set for the file. Symbolic modes are accepted in this form, and this is usually the way in which you would want to use them. You must specify `u&#8217;, `g&#8217; or `o&#8217; if you use a symbolic mode. See the <code>EXAMPLES</code> section for some illustrative examples. </p>
 </dd>
<dt>-perm /<i>mode</i></dt>
<dd> <p> Any of the permission bits <i>mode</i> are set for the file. Symbolic modes are accepted in this form. You must specify `u&#8217;, `g&#8217; or `o&#8217; if you use a symbolic mode. See the <code>EXAMPLES</code> section for some illustrative examples. If no permission bits in <i>mode</i> are set, this test matches any file (the idea here is to be consistent with the behaviour of <code>-perm -000</code>). </p>
 </dd>
<dt>-perm +<i>mode</i></dt>
<dd> <p> This is no longer supported (and has been deprecated since 2005). Use <code>-perm /</code><i>mode</i> instead. </p>
 </dd>
<dt>-readable</dt>
<dd> <p> Matches files which are readable by the current user. This takes into account access control lists and other permissions artefacts which the <code>-perm</code> test ignores. This test makes use of the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) system call, and so can be fooled by NFS servers which do UID mapping (or root-squashing), since many systems implement <code><a href="/docs/linux/man/2-access/">access</a></code>(2) in the client&#8217;s kernel and so cannot make use of the UID mapping information held on the server. </p>
 </dd>
<dt>-regex <i>pattern</i></dt>
<dd> <p> File name matches regular expression <i>pattern</i>. This is a match on the whole path, not a search. For example, to match a file named <i>./fubar3,</i> you can use the regular expression `.*bar.&#8216; or `.*b.*3&#8217;, but not `f.*r3&#8217;. The regular expressions understood by <code>find</code> are by default Emacs Regular Expressions (except that `.&#8216; matches newline), but this can be changed with the <code>-regextype</code> option. </p>
 </dd>
<dt>-samefile <i>name</i></dt>
<dd> <p> File refers to the same inode as <i>name</i>. When <code>-L</code> is in effect, this can include symbolic links. </p>
 </dd>
<dt>-size <i>n</i>[cwbkMG]</dt>
<dd> <p> File uses less than, more than or exactly <i>n</i> units of space, rounding up. The following suffixes can be used: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>`b&#8217;</dt>
<dd> <p> for 512-byte blocks (this is the default if no suffix is used) </p>
 </dd>
<dt>`c&#8217;</dt>
<dd> <p> for bytes </p>
 </dd>
<dt>`w&#8217;</dt>
<dd> <p> for two-byte words </p>
 </dd>
<dt>`k&#8217;</dt>
<dd> <p> for kibibytes (KiB, units of 1024 bytes) </p>
 </dd>
<dt>`M&#8217;</dt>
<dd> <p> for mebibytes (MiB, units of 1024 * 1024 = 1048576 bytes) </p>
 </dd>
<dt>`G&#8217;</dt>
<dd> <p> for gibibytes (GiB, units of 1024 * 1024 * 1024 = 1073741824 bytes) </p>
 </dd></dl>
</dl>
<dd> <p> The size is simply the st_size member of the struct stat populated by the lstat (or stat) system call, rounded up as shown above. In other words, it&#8217;s consistent with the result you get for <code>ls -l</code>. Bear in mind that the `%k&#8217; and `%b&#8217; format specifiers of <code>-printf</code> handle sparse files differently. The `b&#8217; suffix always denotes 512-byte blocks and never 1024-byte blocks, which is different to the behaviour of <code>-ls</code>. </p>
 </dd>
<dd> <p> The + and - prefixes signify greater than and less than, as usual; i.e., an exact size of <i>n</i> units does not match. Bear in mind that the size is rounded up to the next unit. Therefore <code>-size -1M</code> is not equivalent to <code>-size -1048576c</code>. The former only matches empty files, the latter matches files from 0 to 1,048,575 bytes. </p>
 </dd>
<dt>-true</dt>
<dd> <p> Always true. </p>
 </dd>
<dt>-type <i>c</i></dt>
<dd> <p> File is of type <i>c</i>: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>b</dt>
<dd> <p> block (buffered) special </p>
 </dd>
<dt>c</dt>
<dd> <p> character (unbuffered) special </p>
 </dd>
<dt>d</dt>
<dd> <p> directory </p>
 </dd>
<dt>p</dt>
<dd> <p> named pipe (FIFO) </p>
 </dd>
<dt>f</dt>
<dd> <p> regular file </p>
 </dd>
<dt>l</dt>
<dd> <p> symbolic link; this is never true if the <code>-L</code> option or the <code>-follow</code> option is in effect, unless the symbolic link is broken. If you want to search for symbolic links when <code>-L</code> is in effect, use <code>-xtype</code>. </p>
 </dd>
<dt>s</dt>
<dd> <p> socket </p>
 </dd>
<dt>D</dt>
<dd> <p> door (Solaris) </p>
 </dd></dl>
</dl>
<dd> <p> To search for more than one type at once, you can supply the combined list of type letters separated by a comma `,&#8216; (GNU extension). </p>
 </dd>
<dt>-uid <i>n</i></dt>
<dd> <p> File&#8217;s numeric user ID is less than, more than or exactly <i>n</i>. </p>
 </dd>
<dt>-used <i>n</i></dt>
<dd> <p> File was last accessed less than, more than or exactly <i>n</i> days after its status was last changed. </p>
 </dd>
<dt>-user <i>uname</i></dt>
<dd> <p> File is owned by user <i>uname</i> (numeric user ID allowed). </p>
 </dd>
<dt>-wholename <i>pattern</i></dt>
<dd> <p> See -path. This alternative is less portable than <code>-path</code>. </p>
 </dd>
<dt>-writable</dt>
<dd> <p> Matches files which are writable by the current user. This takes into account access control lists and other permissions artefacts which the <code>-perm</code> test ignores. This test makes use of the <code><a href="/docs/linux/man/2-access/">access</a></code>(2) system call, and so can be fooled by NFS servers which do UID mapping (or root-squashing), since many systems implement <code><a href="/docs/linux/man/2-access/">access</a></code>(2) in the client&#8217;s kernel and so cannot make use of the UID mapping information held on the server. </p>
 </dd>
<dt>-xtype <i>c</i></dt>
<dd> <p> The same as <code>-type</code> unless the file is a symbolic link. For symbolic links: if the <code>-H</code> or <code>-P</code> option was specified, true if the file is a link to a file of type <i>c</i>; if the <code>-L</code> option has been given, true if <i>c</i> is `l&#8217;. In other words, for symbolic links, <code>-xtype</code> checks the type of the file that <code>-type</code> does not check. </p>
 </dd>
<dt>-context <i>pattern</i></dt>
<dd> <p> (SELinux only) Security context of the file matches glob <i>pattern</i>. </p>
 </dd></dl>
<h3>ACTIONS</h3>
<dl>
<dt>-delete</dt>
<dd> <p> Delete files; true if removal succeeded. If the removal failed, an error message is issued. If <code>-delete</code> fails, <code>find</code>&#8216;s exit status will be nonzero (when it eventually exits). Use of <code>-delete</code> automatically turns on the `<code>-depth</code>&#8216; option. </p>
<p> <code>Warnings</code>: Don&#8217;t forget that the find command line is evaluated as an expression, so putting <code>-delete</code> first will make <code>find</code> try to delete everything below the starting points you specified. When testing a <code>find</code> command line that you later intend to use with <code>-delete</code>, you should explicitly specify <code>-depth</code> in order to avoid later surprises. Because <code>-delete</code> implies <code>-depth</code>, you cannot usefully use <code>-prune</code> and <code>-delete</code> together. </p>
<p> Together with the <code>-ignore_readdir_race</code> option, <code>find</code> will ignore errors of the <code>-delete</code> action in the case the file has disappeared since the parent directory was read: it will not output an error diagnostic, and the return code of the <code>-delete</code> action will be true. </p>
 </dd>
<dt>-exec <i>command</i> ;</dt>
<dd> <p> Execute <i>command</i>; true if 0 status is returned. All following arguments to <code>find</code> are taken to be arguments to the command until an argument consisting of `;&#8216; is encountered. The string `{}&#8216; is replaced by the current file name being processed everywhere it occurs in the arguments to the command, not just in arguments where it is alone, as in some versions of <code>find</code>. Both of these constructions might need to be escaped (with a `\&#8216;) or quoted to protect them from expansion by the shell. See the <code>EXAMPLES</code> section for examples of the use of the <code>-exec</code> option. The specified command is run once for each matched file. The command is executed in the starting directory. There are unavoidable security problems surrounding use of the <code>-exec</code> action; you should use the <code>-execdir</code> option instead. </p>
 </dd>
<dt>-exec <i>command</i> {} +</dt>
<dd> <p> This variant of the <code>-exec</code> action runs the specified command on the selected files, but the command line is built by appending each selected file name at the end; the total number of invocations of the command will be much less than the number of matched files. The command line is built in much the same way that <code>xargs</code> builds its command lines. Only one instance of `{}&#8216; is allowed within the command, and it must appear at the end, immediately before the `+&#8216;; it needs to be escaped (with a `\&#8216;) or quoted to protect it from interpretation by the shell. The command is executed in the starting directory. If any invocation with the `+&#8216; form returns a non-zero value as exit status, then <code>find</code> returns a non-zero exit status. If <code>find</code> encounters an error, this can sometimes cause an immediate exit, so some pending commands may not be run at all. For this reason <code>-exec&nbsp;</code><i>my-command</i>&nbsp;...&nbsp;{}&nbsp;+&nbsp;-quit may not result in <i>my-command</i> actually being run. This variant of <code>-exec</code> always returns true. </p>
 </dd>
<dt>-execdir <i>command</i> ;</dt>
<dd>  </dd>
<dt>-execdir <i>command</i> {} +</dt>
<dd> <p> Like <code>-exec</code>, but the specified command is run from the subdirectory containing the matched file, which is not normally the directory in which you started <code>find</code>. As with -exec, the {} should be quoted if find is being invoked from a shell. This a much more secure method for invoking commands, as it avoids race conditions during resolution of the paths to the matched files. As with the <code>-exec</code> action, the `+&#8216; form of <code>-execdir</code> will build a command line to process more than one matched file, but any given invocation of <i>command</i> will only list files that exist in the same subdirectory. If you use this option, you must ensure that your <code>$PATH</code> environment variable does not reference `.&#8216;; otherwise, an attacker can run any commands they like by leaving an appropriately-named file in a directory in which you will run <code>-execdir</code>. The same applies to having entries in <code>$PATH</code> which are empty or which are not absolute directory names. If any invocation with the `+&#8216; form returns a non-zero value as exit status, then <code>find</code> returns a non-zero exit status. If <code>find</code> encounters an error, this can sometimes cause an immediate exit, so some pending commands may not be run at all. The result of the action depends on whether the <code>+</code> or the <code>;</code> variant is being used; <code>-execdir&nbsp;</code><i>command</i>&nbsp;{}&nbsp;+ always returns true, while <code>-execdir&nbsp;</code><i>command</i>&nbsp;{}&nbsp;; returns true only if <i>command</i> returns 0. </p>
 </dd>
<dt>-fls <i>file</i></dt>
<dd> <p> True; like <code>-ls</code> but write to <i>file</i> like <code>-fprint</code>. The output file is always created, even if the predicate is never matched. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
 </dd>
<dt>-fprint <i>file</i></dt>
<dd> <p> True; print the full file name into file <i>file</i>. If <i>file</i> does not exist when <code>find</code> is run, it is created; if it does exist, it is truncated. The file names <i>/dev/stdout</i> and <i>/dev/stderr</i> are handled specially; they refer to the standard output and standard error output, respectively. The output file is always created, even if the predicate is never matched. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
 </dd>
<dt>-fprint0 <i>file</i></dt>
<dd> <p> True; like <code>-print0</code> but write to <i>file</i> like <code>-fprint</code>. The output file is always created, even if the predicate is never matched. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
 </dd>
<dt>-fprintf <i>file</i><i>format</i></dt>
<dd> <p> True; like <code>-printf</code> but write to <i>file</i> like <code>-fprint</code>. The output file is always created, even if the predicate is never matched. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
 </dd>
<dt>-ls</dt>
<dd> <p> True; list current file in <code>ls -dils</code> format on standard output. The block counts are of 1 KB blocks, unless the environment variable POSIXLY_CORRECT is set, in which case 512-byte blocks are used. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
 </dd>
<dt>-ok <i>command</i> ;</dt>
<dd> <p> Like <code>-exec</code> but ask the user first. If the user agrees, run the command. Otherwise just return false. If the command is run, its standard input is redirected from <i>/dev/null</i>. </p>
 </dd>
<dd> <p> The response to the prompt is matched against a pair of regular expressions to determine if it is an affirmative or negative response. This regular expression is obtained from the system if the `POSIXLY_CORRECT&#8217; environment variable is set, or otherwise from <code>find</code>&#8216;s message translations. If the system has no suitable definition, <code>find</code>&#8216;s own definition will be used. In either case, the interpretation of the regular expression itself will be affected by the environment variables &#8216;LC_CTYPE&#8217; (character classes) and &#8216;LC_COLLATE&#8217; (character ranges and equivalence classes). </p>
 </dd>
<dt>-okdir <i>command</i> ;</dt>
<dd> <p> Like <code>-execdir</code> but ask the user first in the same way as for <code>-ok</code>. If the user does not agree, just return false. If the command is run, its standard input is redirected from <i>/dev/null</i>. </p>
 </dd>
<dt>-print</dt>
<dd> <p> True; print the full file name on the standard output, followed by a newline. If you are piping the output of <code>find</code> into another program and there is the faintest possibility that the files which you are searching for might contain a newline, then you should seriously consider using the <code>-print0</code> option instead of <code>-print</code>. See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
 </dd>
<dt>-print0</dt>
<dd> <p> True; print the full file name on the standard output, followed by a null character (instead of the newline character that <code>-print</code> uses). This allows file names that contain newlines or other types of white space to be correctly interpreted by programs that process the <code>find</code> output. This option corresponds to the <code>-0</code> option of <code>xargs</code>. </p>
 </dd>
<dt>-printf <i>format</i></dt>
<dd> <p> True; print <i>format</i> on the standard output, interpreting `\&#8216; escapes and `%&#8216; directives. Field widths and precisions can be specified as with the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) C function. Please note that many of the fields are printed as %s rather than %d, and this may mean that flags don&#8217;t work as you might expect. This also means that the `-&#8216; flag does work (it forces fields to be left-aligned). Unlike <code>-print</code>, <code>-printf</code> does not add a newline at the end of the string. The escapes and directives are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>\a</dt>
<dd> <p> Alarm bell. </p>
 </dd>
<dt>\b</dt>
<dd> <p> Backspace. </p>
 </dd>
<dt>\c</dt>
<dd> <p> Stop printing from this format immediately and flush the output. </p>
 </dd>
<dt>\f</dt>
<dd> <p> Form feed. </p>
 </dd>
<dt>\n</dt>
<dd> <p> Newline. </p>
 </dd>
<dt>\r</dt>
<dd> <p> Carriage return. </p>
 </dd>
<dt>\t</dt>
<dd> <p> Horizontal tab. </p>
 </dd>
<dt>\v</dt>
<dd> <p> Vertical tab. </p>
 </dd>
<dt>\0</dt>
<dd> <p> ASCII NUL. </p>
 </dd>
<dt>\\</dt>
<dd> <p> A literal backslash (`\&#8216;). </p>
 </dd>
<dt>\NNN</dt>
<dd> <p> The character whose ASCII code is NNN (octal). </p>
 </dd></dl>
<p> A `\&#8216; character followed by any other character is treated as an ordinary character, so they both are printed. </p>
<dl>
<dt>%%</dt>
<dd> <p> A literal percent sign. </p>
 </dd>
<dt>%a</dt>
<dd> <p> File&#8217;s last access time in the format returned by the C <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) function. </p>
 </dd>
<dt>%A <i>k</i></dt>
<dd> <p> File&#8217;s last access time in the format specified by <i>k</i>, which is either `@&#8216; or a directive for the C <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) function. The following shows an incomplete list of possible values for <i>k</i>. Please refer to the documentation of <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) for the full list. Some of the conversion specification characters might not be available on all systems, due to differences in the implementation of the <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) library function. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>@</dt>
<dd> <p> seconds since Jan. 1, 1970, 00:00 GMT, with fractional part. </p>
 </dd></dl>
<p> Time fields: </p>
<dl>
<dt>H</dt>
<dd> <p> hour (00..23) </p>
 </dd>
<dt>I</dt>
<dd> <p> hour (01..12) </p>
 </dd>
<dt>k</dt>
<dd> <p> hour ( 0..23) </p>
 </dd>
<dt>l</dt>
<dd> <p> hour ( 1..12) </p>
 </dd>
<dt>M</dt>
<dd> <p> minute (00..59) </p>
 </dd>
<dt>p</dt>
<dd> <p> locale&#8217;s AM or PM </p>
 </dd>
<dt>r</dt>
<dd> <p> time, 12-hour (hh:mm:ss [AP]M) </p>
 </dd>
<dt>S</dt>
<dd> <p> Second (00.00 .. 61.00). There is a fractional part. </p>
 </dd>
<dt>T</dt>
<dd> <p> time, 24-hour (hh:mm:ss.xxxxxxxxxx) </p>
 </dd>
<dt>+</dt>
<dd> <p> Date and time, separated by `+&#8216;, for example `2004-04-28+22:22:05.0&#8217;. This is a GNU extension. The time is given in the current timezone (which may be affected by setting the TZ environment variable). The seconds field includes a fractional part. </p>
 </dd>
<dt>X</dt>
<dd> <p> locale&#8217;s time representation (H:M:S). The seconds field includes a fractional part. </p>
 </dd>
<dt>Z</dt>
<dd> <p> time zone (e.g., EDT), or nothing if no time zone is determinable </p>
 </dd></dl>
<p> Date fields: </p>
<dl>
<dt>a</dt>
<dd> <p> locale&#8217;s abbreviated weekday name (Sun..Sat) </p>
 </dd>
<dt>A</dt>
<dd> <p> locale&#8217;s full weekday name, variable length (Sunday..Saturday) </p>
 </dd>
<dt>b</dt>
<dd> <p> locale&#8217;s abbreviated month name (Jan..Dec) </p>
 </dd>
<dt>B</dt>
<dd> <p> locale&#8217;s full month name, variable length (January..December) </p>
 </dd>
<dt>c</dt>
<dd> <p> locale&#8217;s date and time (Sat Nov 04 12:02:33 EST 1989). The format is the same as for <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) and so to preserve compatibility with that format, there is no fractional part in the seconds field. </p>
 </dd>
<dt>d</dt>
<dd> <p> day of month (01..31) </p>
 </dd>
<dt>D</dt>
<dd> <p> date (mm/dd/yy) </p>
 </dd>
<dt>F</dt>
<dd> <p> date (yyyy-mm-dd) </p>
 </dd>
<dt>h</dt>
<dd> <p> same as b </p>
 </dd>
<dt>j</dt>
<dd> <p> day of year (001..366) </p>
 </dd>
<dt>m</dt>
<dd> <p> month (01..12) </p>
 </dd>
<dt>U</dt>
<dd> <p> week number of year with Sunday as first day of week (00..53) </p>
 </dd>
<dt>w</dt>
<dd> <p> day of week (0..6) </p>
 </dd>
<dt>W</dt>
<dd> <p> week number of year with Monday as first day of week (00..53) </p>
 </dd>
<dt>x</dt>
<dd> <p> locale&#8217;s date representation (mm/dd/yy) </p>
 </dd>
<dt>y</dt>
<dd> <p> last two digits of year (00..99) </p>
 </dd>
<dt>Y</dt>
<dd> <p> year (1970...) </p>
 </dd></dl>
</dl>
<dt>%b</dt>
<dd> <p> The amount of disk space used for this file in 512-byte blocks. Since disk space is allocated in multiples of the filesystem block size this is usually greater than %s/512, but it can also be smaller if the file is a sparse file. </p>
 </dd>
<dt>%c</dt>
<dd> <p> File&#8217;s last status change time in the format returned by the C <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) function. </p>
 </dd>
<dt>%C <i>k</i></dt>
<dd> <p> File&#8217;s last status change time in the format specified by <i>k</i>, which is the same as for %A. </p>
 </dd>
<dt>%d</dt>
<dd> <p> File&#8217;s depth in the directory tree; 0 means the file is a starting-point. </p>
 </dd>
<dt>%D</dt>
<dd> <p> The device number on which the file exists (the st_dev field of struct stat), in decimal. </p>
 </dd>
<dt>%f</dt>
<dd> <p> Print the basename; the file&#8217;s name with any leading directories removed (only the last element). For <code>/</code>, the result is `/&#8216;. See the <code>EXAMPLES</code> section for an example. </p>
 </dd>
<dt>%F</dt>
<dd> <p> Type of the filesystem the file is on; this value can be used for -fstype. </p>
 </dd>
<dt>%g</dt>
<dd> <p> File&#8217;s group name, or numeric group ID if the group has no name. </p>
 </dd>
<dt>%G</dt>
<dd> <p> File&#8217;s numeric group ID. </p>
 </dd>
<dt>%h</dt>
<dd> <p> Dirname; the Leading directories of the file&#8217;s name (all but the last element). If the file name contains no slashes (since it is in the current directory) the %h specifier expands to `.&#8216;. For files which are themselves directories and contain a slash (including <code>/</code>), %h expands to the empty string. See the <code>EXAMPLES</code> section for an example. </p>
 </dd>
<dt>%H</dt>
<dd> <p> Starting-point under which file was found. </p>
 </dd>
<dt>%i</dt>
<dd> <p> File&#8217;s inode number (in decimal). </p>
 </dd>
<dt>%k</dt>
<dd> <p> The amount of disk space used for this file in 1 KB blocks. Since disk space is allocated in multiples of the filesystem block size this is usually greater than %s/1024, but it can also be smaller if the file is a sparse file. </p>
 </dd>
<dt>%l</dt>
<dd> <p> Object of symbolic link (empty string if file is not a symbolic link). </p>
 </dd>
<dt>%m</dt>
<dd> <p> File&#8217;s permission bits (in octal). This option uses the `traditional&#8217; numbers which most Unix implementations use, but if your particular implementation uses an unusual ordering of octal permissions bits, you will see a difference between the actual value of the file&#8217;s mode and the output of %m. Normally you will want to have a leading zero on this number, and to do this, you should use the <code>#</code> flag (as in, for example, `%#m&#8217;). </p>
 </dd>
<dt>%M</dt>
<dd> <p> File&#8217;s permissions (in symbolic form, as for <code>ls</code>). This directive is supported in findutils 4.2.5 and later. </p>
 </dd>
<dt>%n</dt>
<dd> <p> Number of hard links to file. </p>
 </dd>
<dt>%p</dt>
<dd> <p> File&#8217;s name. </p>
 </dd>
<dt>%P</dt>
<dd> <p> File&#8217;s name with the name of the starting-point under which it was found removed. </p>
 </dd>
<dt>%s</dt>
<dd> <p> File&#8217;s size in bytes. </p>
 </dd>
<dt>%S</dt>
<dd> <p> File&#8217;s sparseness. This is calculated as (BLOCKSIZE*st_blocks / st_size). The exact value you will get for an ordinary file of a certain length is system-dependent. However, normally sparse files will have values less than 1.0, and files which use indirect blocks may have a value which is greater than 1.0. In general the number of blocks used by a file is file system dependent. The value used for BLOCKSIZE is system-dependent, but is usually 512 bytes. If the file size is zero, the value printed is undefined. On systems which lack support for st_blocks, a file&#8217;s sparseness is assumed to be 1.0. </p>
 </dd>
<dt>%t</dt>
<dd> <p> File&#8217;s last modification time in the format returned by the C <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) function. </p>
 </dd>
<dt>%T <i>k</i></dt>
<dd> <p> File&#8217;s last modification time in the format specified by <i>k</i>, which is the same as for %A. </p>
 </dd>
<dt>%u</dt>
<dd> <p> File&#8217;s user name, or numeric user ID if the user has no name. </p>
 </dd>
<dt>%U</dt>
<dd> <p> File&#8217;s numeric user ID. </p>
 </dd>
<dt>%y</dt>
<dd> <p> File&#8217;s type (like in <code>ls -l</code>), U=unknown type (shouldn&#8217;t happen) </p>
 </dd>
<dt>%Y</dt>
<dd> <p> File&#8217;s type (like %y), plus follow symbolic links: `L&#8217;=loop, `N&#8217;=nonexistent, `?&#8216; for any other error when determining the type of the target of a symbolic link. </p>
 </dd>
<dt>%Z</dt>
<dd> <p> (SELinux only) file&#8217;s security context. </p>
 </dd>
<dt>%{ %[ %(</dt>
<dd> <p> Reserved for future use. </p>
 </dd></dl>
<p> A `%&#8216; character followed by any other character is discarded, but the other character is printed (don&#8217;t rely on this, as further format characters may be introduced). A `%&#8216; at the end of the format argument causes undefined behaviour since there is no following character. In some locales, it may hide your door keys, while in others it may remove the final page from the novel you are reading. </p>
<p> The %m and %d directives support the <code>#</code>, <code>0</code> and <code>+</code> flags, but the other directives do not, even if they print numbers. Numeric directives that do not support these flags include <code>G</code>, <code>U</code>, <code>b</code>, <code>D</code>, <code>k</code> and <code>n</code>. The `-&#8216; format flag is supported and changes the alignment of a field from right-justified (which is the default) to left-justified. </p>
<p> See the <code>UNUSUAL FILENAMES</code> section for information about how unusual characters in filenames are handled. </p>
<dt>-prune</dt>
<dd> <p> True; if the file is a directory, do not descend into it. If <code>-depth</code> is given, then <code>-prune</code> has no effect. Because <code>-delete</code> implies <code>-depth</code>, you cannot usefully use <code>-prune</code> and <code>-delete</code> together. For example, to skip the directory <i>src/emacs</i> and all files and directories under it, and print the names of the other files found, do something like this: </p>
<pre><code>find . -path ./src/emacs -prune -o -print
</code></pre>
 </dd>
<dt>-quit</dt>
<dd> <p> Exit immediately (with return value zero if no errors have occurred). This is different to <code>-prune</code> because <code>-prune</code> only applies to the contents of pruned directories, while <code>-quit</code> simply makes <code>find</code> stop immediately. No child processes will be left running. Any command lines which have been built by <code>-exec ...&nbsp;+</code> or <code>-execdir ...&nbsp;+</code> are invoked before the program is exited. After <code>-quit</code> is executed, no more files specified on the command line will be processed. For example, `<code>find&nbsp;</code><i>/tmp/foo</i>&nbsp;<i>/tmp/bar</i>&nbsp;-print -quit` will print only `/tmp/foo`. <br />
 One common use of <code>-quit</code> is to stop searching the file system once we have found what we want. For example, if we want to find just a single file we can do this: </p>
<pre><code>find / -name needle -print -quit
</code></pre>
 </dd></dl>
<h3>OPERATORS</h3>
<p> Listed in order of decreasing precedence: </p>
<dl>
<dt>( <i>expr</i> )</dt>
<dd> <p> Force precedence. Since parentheses are special to the shell, you will normally need to quote them. Many of the examples in this manual page use backslashes for this purpose: `\(...\)&#8216; instead of `(...)&#8216;. </p>
 </dd>
<dt>! <i>expr</i></dt>
<dd> <p> True if <i>expr</i> is false. This character will also usually need protection from interpretation by the shell. </p>
 </dd>
<dt>-not <i>expr</i></dt>
<dd> <p> Same as ! <i>expr</i>, but not POSIX compliant. </p>
 </dd>
<dt><i>expr1 expr2</i></dt>
<dd> <p> Two expressions in a row are taken to be joined with an implied <code>-a</code>; <i>expr2</i> is not evaluated if <i>expr1</i> is false. </p>
 </dd>
<dt><i>expr1</i> -a <i>expr2</i></dt>
<dd> <p> Same as <i>expr1 expr2</i>. </p>
 </dd>
<dt><i>expr1</i> -and <i>expr2</i></dt>
<dd> <p> Same as <i>expr1 expr2</i>, but not POSIX compliant. </p>
 </dd>
<dt><i>expr1</i> -o <i>expr2</i></dt>
<dd> <p> Or; <i>expr2</i> is not evaluated if <i>expr1</i> is true. </p>
 </dd>
<dt><i>expr1</i> -or <i>expr2</i></dt>
<dd> <p> Same as <i>expr1</i> <code>-o</code> <i>expr2</i>, but not POSIX compliant. </p>
 </dd>
<dt><i>expr1</i> , <i>expr2</i></dt>
<dd> <p> List; both <i>expr1</i> and <i>expr2</i> are always evaluated. The value of <i>expr1</i> is discarded; the value of the list is the value of <i>expr2</i>. The comma operator can be useful for searching for several different types of thing, but traversing the filesystem hierarchy only once. The <code>-fprintf</code> action can be used to list the various matched items into several different output files. </p>
 </dd></dl>
<p> Please note that <code>-a</code> when specified implicitly (for example by two tests appearing without an explicit operator between them) or explicitly has higher precedence than <code>-o</code>. This means that <code>find . -name afile -o -name bfile -print</code> will never print <i>afile</i>.  </p>
<h2>UNUSUAL FILENAMES</h2>
<p> Many of the actions of <code>find</code> result in the printing of data which is under the control of other users. This includes file names, sizes, modification times and so forth. File names are a potential problem since they can contain any character except `\0&#8217; and `/&#8216;. Unusual characters in file names can do unexpected and often undesirable things to your terminal (for example, changing the settings of your function keys on some terminals). Unusual characters are handled differently by various actions, as described below. </p>
<dl>
<dt>-print0, -fprint0</dt>
<dd> <p> Always print the exact filename, unchanged, even if the output is going to a terminal. </p>
 </dd>
<dt>-ls, -fls</dt>
<dd> <p> Unusual characters are always escaped. White space, backslash, and double quote characters are printed using C-style escaping (for example `\f&#8217;, `\&quot;&#8216;). Other unusual characters are printed using an octal escape. Other printable characters (for <code>-ls</code> and <code>-fls</code> these are the characters between octal 041 and 0176) are printed as-is. </p>
 </dd>
<dt>-printf, -fprintf</dt>
<dd> <p> If the output is not going to a terminal, it is printed as-is. Otherwise, the result depends on which directive is in use. The directives %D, %F, %g, %G, %H, %Y, and %y expand to values which are not under control of files&#8217; owners, and so are printed as-is. The directives %a, %b, %c, %d, %i, %k, %m, %M, %n, %s, %t, %u and %U have values which are under the control of files&#8217; owners but which cannot be used to send arbitrary data to the terminal, and so these are printed as-is. The directives %f, %h, %l, %p and %P are quoted. This quoting is performed in the same way as for GNU <code>ls</code>. This is not the same quoting mechanism as the one used for <code>-ls</code> and <code>-fls</code>. If you are able to decide what format to use for the output of <code>find</code> then it is normally better to use `\0&#8217; as a terminator than to use newline, as file names can contain white space and newline characters. The setting of the `LC_CTYPE&#8217; environment variable is used to determine which characters need to be quoted. </p>
 </dd>
<dt>-print, -fprint</dt>
<dd> <p> Quoting is handled in the same way as for <code>-printf</code> and <code>-fprintf</code>. If you are using <code>find</code> in a script or in a situation where the matched files might have arbitrary names, you should consider using <code>-print0</code> instead of <code>-print</code>. </p>
 </dd></dl>
<p> The <code>-ok</code> and <code>-okdir</code> actions print the current filename as-is. This may change in a future release.  </p>
<h2>STANDARDS CONFORMANCE</h2>
<p> For closest compliance to the POSIX standard, you should set the POSIXLY_CORRECT environment variable. The following options are specified in the POSIX standard (IEEE Std 1003.1-2008, 2016 Edition): </p>
<dl>
<dt><code>-H</code></dt>
<dd> <p> This option is supported. </p>
 </dd>
<dt><code>-L</code></dt>
<dd> <p> This option is supported. </p>
 </dd>
<dt><code>-name</code></dt>
<dd> <p> This option is supported, but POSIX conformance depends on the POSIX conformance of the system&#8217;s <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3) library function. As of findutils-4.2.2, shell metacharacters (`*&#8216;, `?&#8216; or `[]&#8216; for example) match a leading `.&#8216;, because IEEE PASC interpretation 126 requires this. This is a change from previous versions of findutils. </p>
 </dd>
<dt><code>-type</code></dt>
<dd> <p> Supported. POSIX specifies `b&#8217;, `c&#8217;, `d&#8217;, `l&#8217;, `p&#8217;, `f&#8217; and `s&#8217;. GNU find also supports `D&#8217;, representing a Door, where the OS provides these. Furthermore, GNU find allows multiple types to be specified at once in a comma-separated list. </p>
 </dd>
<dt><code>-ok</code></dt>
<dd> <p> Supported. Interpretation of the response is according to the `yes&#8217; and `no&#8217; patterns selected by setting the `LC_MESSAGES&#8217; environment variable. When the `POSIXLY_CORRECT&#8217; environment variable is set, these patterns are taken system&#8217;s definition of a positive (yes) or negative (no) response. See the system&#8217;s documentation for <code><a href="/docs/linux/man/3-nl_langinfo/">nl_langinfo</a></code>(3), in particular YESEXPR and NOEXPR. When `POSIXLY_CORRECT&#8217; is not set, the patterns are instead taken from <code>find</code>&#8216;s own message catalogue. </p>
 </dd>
<dt><code>-newer</code></dt>
<dd> <p> Supported. If the file specified is a symbolic link, it is always dereferenced. This is a change from previous behaviour, which used to take the relevant time from the symbolic link; see the HISTORY section below. </p>
 </dd>
<dt><code>-perm</code></dt>
<dd> <p> Supported. If the POSIXLY_CORRECT environment variable is not set, some mode arguments (for example +a+x) which are not valid in POSIX are supported for backward-compatibility. </p>
 </dd>
<dt>Other primaries</dt>
<dd> <p> The primaries <code>-atime</code>, <code>-ctime</code>, <code>-depth</code>, <code>-exec</code>, <code>-group</code>, <code>-links</code>, <code>-mtime</code>, <code>-nogroup</code>, <code>-nouser</code>, <code>-ok</code>, <code>-path</code>, <code>-print</code>, <code>-prune</code>, <code>-size</code>, <code>-user</code> and <code>-xdev</code> are all supported. </p>
 </dd></dl>
<p> The POSIX standard specifies parentheses `(&#8216;, `)&#8216;, negation `!&#8216; and the logical AND/OR operators <code>-a</code> and <code>-o</code>. </p>
<p> All other options, predicates, expressions and so forth are extensions beyond the POSIX standard. Many of these extensions are not unique to GNU find, however. </p>
<p> The POSIX standard requires that <code>find</code> detects loops: </p>
<dl>
<dd> <p> The <code>find</code> utility shall detect infinite loops; that is, entering a previously visited directory that is an ancestor of the last file encountered. When it detects an infinite loop, find shall write a diagnostic message to standard error and shall either recover its position in the hierarchy or terminate. </p>
 </dd></dl>
<p> GNU <code>find</code> complies with these requirements. The link count of directories which contain entries which are hard links to an ancestor will often be lower than they otherwise should be. This can mean that GNU find will sometimes optimise away the visiting of a subdirectory which is actually a link to an ancestor. Since <code>find</code> does not actually enter such a subdirectory, it is allowed to avoid emitting a diagnostic message. Although this behaviour may be somewhat confusing, it is unlikely that anybody actually depends on this behaviour. If the leaf optimisation has been turned off with <code>-noleaf</code>, the directory entry will always be examined and the diagnostic message will be issued where it is appropriate. Symbolic links cannot be used to create filesystem cycles as such, but if the <code>-L</code> option or the <code>-follow</code> option is in use, a diagnostic message is issued when <code>find</code> encounters a loop of symbolic links. As with loops containing hard links, the leaf optimisation will often mean that <code>find</code> knows that it doesn&#8217;t need to call <i>stat()</i> or <i>chdir()</i> on the symbolic link, so this diagnostic is frequently not necessary. </p>
<p> The <code>-d</code> option is supported for compatibility with various BSD systems, but you should use the POSIX-compliant option <code>-depth</code> instead. </p>
<p> The POSIXLY_CORRECT environment variable does not affect the behaviour of the <code>-regex</code> or <code>-iregex</code> tests because those tests aren&#8217;t specified in the POSIX standard.  </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>LANG</dt>
<dd> <p> Provides a default value for the internationalization variables that are unset or null. </p>
 </dd>
<dt>LC_ALL</dt>
<dd> <p> If set to a non-empty string value, override the values of all the other internationalization variables. </p>
 </dd>
<dt>LC_COLLATE</dt>
<dd> <p> The POSIX standard specifies that this variable affects the pattern matching to be used for the <code>-name</code> option. GNU find uses the <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3) library function, and so support for `LC_COLLATE&#8217; depends on the system library. This variable also affects the interpretation of the response to <code>-ok</code>; while the `LC_MESSAGES&#8217; variable selects the actual pattern used to interpret the response to <code>-ok</code>, the interpretation of any bracket expressions in the pattern will be affected by `LC_COLLATE&#8217;. </p>
 </dd>
<dt>LC_CTYPE</dt>
<dd> <p> This variable affects the treatment of character classes used in regular expressions and also with the <code>-name</code> test, if the system&#8217;s <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3) library function supports this. This variable also affects the interpretation of any character classes in the regular expressions used to interpret the response to the prompt issued by <code>-ok</code>. The `LC_CTYPE&#8217; environment variable will also affect which characters are considered to be unprintable when filenames are printed; see the section UNUSUAL FILENAMES. </p>
 </dd>
<dt>LC_MESSAGES</dt>
<dd> <p> Determines the locale to be used for internationalised messages. If the `POSIXLY_CORRECT&#8217; environment variable is set, this also determines the interpretation of the response to the prompt made by the <code>-ok</code> action. </p>
 </dd>
<dt>NLSPATH</dt>
<dd> <p> Determines the location of the internationalisation message catalogues. </p>
 </dd>
<dt>PATH</dt>
<dd> <p> Affects the directories which are searched to find the executables invoked by <code>-exec</code>, <code>-execdir</code>, <code>-ok</code> and <code>-okdir</code>. </p>
 </dd>
<dt>POSIXLY_CORRECT</dt>
<dd> <p> Determines the block size used by <code>-ls</code> and <code>-fls</code>. If <code>POSIXLY_CORRECT</code> is set, blocks are units of 512 bytes. Otherwise they are units of 1024 bytes. </p>
 </dd>
<dd> <p> Setting this variable also turns off warning messages (that is, implies <code>-nowarn</code>) by default, because POSIX requires that apart from the output for <code>-ok</code>, all messages printed on stderr are diagnostics and must result in a non-zero exit status. </p>
 </dd>
<dd> <p> When POSIXLY_CORRECT is not set, <code>-perm </code><i>+zzz</i> is treated just like <code>-perm </code><i>/zzz</i> if <i>+zzz</i> is not a valid symbolic mode. When POSIXLY_CORRECT is set, such constructs are treated as an error. </p>
 </dd>
<dd> <p> When POSIXLY_CORRECT is set, the response to the prompt made by the <code>-ok</code> action is interpreted according to the system&#8217;s message catalogue, as opposed to according to <code>find</code>&#8216;s own message translations. </p>
 </dd>
<dt>TZ</dt>
<dd> <p> Affects the time zone used for some of the time-related format directives of <code>-printf</code> and <code>-fprintf</code>. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<h3>Simple `find|xargs` approach</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Find files named <i>core</i> in or below the directory <i>/tmp</i> and delete them. </p>
<pre><code>
 $ find /tmp -name core -type f -print | xargs /bin/rm -f 
</code></pre>
<p> Note that this will work incorrectly if there are any filenames containing newlines, single or double quotes, or spaces. </p>
 </dd></dl>
<h3>Safer `find -print0 | xargs -0` approach</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Find files named <i>core</i> in or below the directory <i>/tmp</i> and delete them, processing filenames in such a way that file or directory names containing single or double quotes, spaces or newlines are correctly handled. </p>
<pre><code>
 $ find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f 
</code></pre>
<p> The <code>-name</code> test comes before the <code>-type</code> test in order to avoid having to call <code><a href="/docs/linux/man/2-stat/">stat</a>(2)</code> on every file. </p>
 </dd></dl>
<p> Note that there is still a race between the time <code>find</code> traverses the hierarchy printing the matching filenames, and the time the process executed by <code>xargs</code> works with that file. </p>
<h3>Executing a command for each file</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Run <i>file</i> on every file in or below the current directory. </p>
<pre><code>
 $ find . -type f -exec file '{}' \; 
</code></pre>
<p> Notice that the braces are enclosed in single quote marks to protect them from interpretation as shell script punctuation. The semicolon is similarly protected by the use of a backslash, though single quotes could have been used in that case also. </p>
 </dd></dl>
<p> In many cases, one might prefer the <code>`-exec ...&nbsp;+`</code> or better the <code>`-execdir ...&nbsp;+`</code> syntax for performance and security reasons.  </p>
<h3>Traversing the filesystem just once - for 2 different actions</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Traverse the filesystem just once, listing set-user-ID files and directories into <i>/root/suid.txt</i> and large files into <i>/root/big.txt</i>. </p>
<pre><code>
 $ find / \ 
 \( -perm -4000 -fprintf /root/suid.txt '%#m %u %p\n' \) , \ 


 \( -size +100M -fprintf /root/big.txt '%-10s %p\n' \) 
</code></pre>
<p> This example uses the line-continuation character &#8216;\&#8216; on the first two lines to instruct the shell to continue reading the command on the next line. </p>
 </dd></dl>
<h3>Searching files by age</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Search for files in your home directory which have been modified in the last twenty-four hours. </p>
<pre><code>
 $ find $HOME -mtime 0 
</code></pre>
<p> This command works this way because the time since each file was last modified is divided by 24 hours and any remainder is discarded. That means that to match <code>-mtime</code> <code>0</code>, a file will have to have a modification in the past which is less than 24 hours ago. </p>
 </dd></dl>
<h3>Searching files by permissions</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Search for files which are executable but not readable. </p>
<pre><code>
 $ find /sbin /usr/sbin -executable \! -readable -print 
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Search for files which have read and write permission for their owner, and group, but which other users can read but not write to. </p>
<pre><code>
 $ find . -perm 664 
</code></pre>
<p> Files which meet these criteria but have other permissions bits set (for example if someone can execute the file) will not be matched. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Search for files which have read and write permission for their owner and group, and which other users can read, without regard to the presence of any extra permission bits (for example the executable bit). </p>
<pre><code>
 $ find . -perm -664 
</code></pre>
<p> This will match a file which has mode <i>0777</i>, for example. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Search for files which are writable by somebody (their owner, or their group, or anybody else). </p>
<pre><code>
 $ find . -perm /222 
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Search for files which are writable by either their owner or their group. </p>
<pre><code>
 $ find . -perm /220 
 $ find . -perm /u+w,g+w 
 $ find . -perm /u=w,g=w 
</code></pre>
<p> All three of these commands do the same thing, but the first one uses the octal representation of the file mode, and the other two use the symbolic form. The files don&#8217;t have to be writable by both the owner and group to be matched; either will do. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Search for files which are writable by both their owner and their group. </p>
<pre><code>
 $ find . -perm -220 
 $ find . -perm -g+w,u+w 
</code></pre>
<p> Both these commands do the same thing. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A more elaborate search on permissions. </p>
<pre><code>
 $ find . -perm -444 -perm /222 \! -perm /111 
 $ find . -perm -a+r -perm /a+w \! -perm /a+x 
</code></pre>
<p> These two commands both search for files that are readable for everybody (<code>-perm -444</code> or <code>-perm -a+r</code>), have at least one write bit set (<code>-perm /222</code> or <code>-perm /a+w</code>) but are not executable for anybody (<code>! -perm /111</code> or <code>! -perm /a+x</code> respectively). </p>
 </dd></dl>
<h3>Pruning - omitting files and subdirectories</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Copy the contents of <i>/source-dir</i> to <i>/dest-dir</i>, but omit files and directories named <i>.snapshot</i> (and anything in them). It also omits files or directories whose name ends in <i>&#8216;~&#8216;</i>, but not their contents. </p>
<pre><code>
 $ cd /source-dir 
 $ find . -name .snapshot -prune -o \( \! -name '*~' -print0 \) \ 


 | cpio -pmd0 /dest-dir 
</code></pre>
<p> The construct <code>-prune -o&nbsp;\(&nbsp;... -print0&nbsp;\)</code> is quite common. The idea here is that the expression before <code>-prune</code> matches things which are to be pruned. However, the <code>-prune</code> action itself returns true, so the following <code>-o</code> ensures that the right hand side is evaluated only for those directories which didn&#8217;t get pruned (the contents of the pruned directories are not even visited, so their contents are irrelevant). The expression on the right hand side of the <code>-o</code> is in parentheses only for clarity. It emphasises that the <code>-print0</code> action takes place only for things that didn&#8217;t have <code>-prune</code> applied to them. Because the default `and&#8217; condition between tests binds more tightly than <code>-o</code>, this is the default anyway, but the parentheses help to show what is going on. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Given the following directory of projects and their associated SCM administrative directories, perform an efficient search for the projects&#8217; roots: </p>
<pre><code>
 $ find repo/ \ 
 \( -exec test -d '{}/.svn' \; \ 
 -or -exec test -d '{}/.git' \; \ 
 -or -exec test -d '{}/CVS' \; \ 
 \) -print -prune 
</code></pre>
<p> Sample output: </p>
<pre><code>
 repo/project1/CVS 
 repo/gnu/project2/.svn 
 repo/gnu/project3/.svn 
 repo/gnu/project3/src/.svn 
 repo/project4/.git 
</code></pre>
<p> In this example, <code>-prune</code> prevents unnecessary descent into directories that have already been discovered (for example we do not search <i>project3/src</i> because we already found <i>project3/.svn</i>), but ensures sibling directories (<i>project2</i> and <i>project3</i>) are found. </p>
 </dd></dl>
<h3>Other useful examples</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Search for several file types. </p>
<pre><code>
 $ find /tmp -type f,d,l 
</code></pre>
<p> Search for files, directories, and symbolic links in the directory <i>/tmp</i> passing these types as a comma-separated list (GNU extension), which is otherwise equivalent to the longer, yet more portable: </p>
<pre><code>
 $ find /tmp \( -type f -o -type d -o -type l \) 
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Search for files with the particular name <i>needle</i> and stop immediately when we find the first one. </p>
<pre><code>
 $ find / -name needle -print -quit 
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Demonstrate the interpretation of the <code>%f</code> and <code>%h</code> format directives of the <code>-printf</code> action for some corner-cases. Here is an example including some output. </p>
<pre><code>
 $ find . .. / /tmp /tmp/TRACE compile compile/64/tests/find -maxdepth 0 -printf '[%h][%f]\n' 
 [.][.] 
 [.][..] 
 [][/] 
 [][tmp] 
 [/tmp][TRACE] 
 [.][compile] 
 [compile/64/tests][find] 
</code></pre>
 </dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>find</code> exits with status 0 if all files are processed successfully, greater than 0 if errors occur. This is deliberately a very broad description, but if the return value is non-zero, you should not rely on the correctness of the results of <code>find</code>. </p>
<p> When some error occurs, <code>find</code> may stop immediately, without completing all the actions specified. For example, some starting points may not have been examined or some pending program invocations for <code>-exec ...&nbsp;{}&nbsp;+</code> or <code>-execdir ...&nbsp;{}&nbsp;+</code> may not have been performed.  </p>
<h2>HISTORY</h2>
<p> As of findutils-4.2.2, shell metacharacters (`*&#8216;, `?&#8216; or `[]&#8216; for example) used in filename patterns match a leading `.&#8216;, because IEEE POSIX interpretation 126 requires this. </p>
<p> As of findutils-4.3.3, <code>-perm&nbsp;/000</code> now matches all files instead of none. </p>
<p> Nanosecond-resolution timestamps were implemented in findutils-4.3.3. </p>
<p> As of findutils-4.3.11, the <code>-delete</code> action sets <code>find</code>&#8216;s exit status to a nonzero value when it fails. However, <code>find</code> will not exit immediately. Previously, <code>find</code>&#8216;s exit status was unaffected by the failure of <code>-delete</code>. </p>
<table>
<tr VALIGN=top>
<td>Feature</td>
<td>Added in</td>
<td>Also occurs in
</td>
</tr>
<tr VALIGN=top>
<td>-newerXY</td>
<td>4.3.3</td>
<td>BSD
</td>
</tr>
<tr VALIGN=top>
<td>-D</td>
<td>4.3.1</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-O</td>
<td>4.3.1</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-readable</td>
<td>4.3.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-writable</td>
<td>4.3.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-executable</td>
<td>4.3.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-regextype</td>
<td>4.2.24</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-exec ... +</td>
<td>4.2.12</td>
<td>POSIX
</td>
</tr>
<tr VALIGN=top>
<td>-execdir</td>
<td>4.2.12</td>
<td>BSD
</td>
</tr>
<tr VALIGN=top>
<td>-okdir</td>
<td>4.2.12</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-samefile</td>
<td>4.2.11</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-H</td>
<td>4.2.5</td>
<td>POSIX
</td>
</tr>
<tr VALIGN=top>
<td>-L</td>
<td>4.2.5</td>
<td>POSIX
</td>
</tr>
<tr VALIGN=top>
<td>-P</td>
<td>4.2.5</td>
<td>BSD
</td>
</tr>
<tr VALIGN=top>
<td>-delete</td>
<td>4.2.3</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-quit</td>
<td>4.2.3</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-d</td>
<td>4.2.3</td>
<td>BSD
</td>
</tr>
<tr VALIGN=top>
<td>-wholename</td>
<td>4.2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-iwholename</td>
<td>4.2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-ignore_readdir_race</td>
<td>4.2.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-fls</td>
<td>4.0</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-ilname</td>
<td>3.8</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-iname</td>
<td>3.8</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-ipath</td>
<td>3.8</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>-iregex</td>
<td>3.8</td>
<td>
</td>
</tr>
</table>
<p> The syntax .B -perm +MODE was removed in findutils-4.5.12, in favour of .B -perm <code>/MODE</code>. The <code>+MODE</code> syntax had been deprecated since findutils-4.2.21 which was released in 2005.  </p>
<h2>NON-BUGS</h2>
<h3>Operator precedence surprises</h3>
<p> The command <code>find . -name afile -o -name bfile -print</code> will never print <i>afile</i> because this is actually equivalent to <code>find . -name afile -o \( -name bfile -a -print \)</code>. Remember that the precedence of <code>-a</code> is higher than that of <code>-o</code> and when there is no operator specified between tests, <code>-a</code> is assumed.  </p>
<h3>"paths must precede expression" error message</h3>
<pre><code>
 $ find . -name *.c -print find: paths must precede expression
find: possible unquoted pattern after predicate `-name'?
</code></pre>
<p> This happens when the shell could expand the pattern <i>*.c</i> to more than one file name existing in the current directory, and passing the resulting file names in the command line to <code>find</code> like this: </p>
<pre><code>
 find . -name frcode.c locate.c word_io.c -print 
</code></pre>
<p> That command is of course not going to work, because the <code>-name</code> predicate allows exactly only one pattern as argument. Instead of doing things this way, you should enclose the pattern in quotes or escape the wildcard, thus allowing <code>find</code> to use the pattern with the wildcard during the search for file name matching instead of file names expanded by the parent shell: </p>
<pre><code>
 $ find . -name '*.c' -print 
 $ find . -name \*.c -print 
</code></pre>
<h2>BUGS</h2>
<p> There are security problems inherent in the behaviour that the POSIX standard specifies for <code>find</code>, which therefore cannot be fixed. For example, the <code>-exec</code> action is inherently insecure, and <code>-execdir</code> should be used instead. </p>
<p> The environment variable <code>LC_COLLATE</code> has no effect on the <code>-ok</code> action.  </p>
<h2>REPORTING BUGS</h2>
<p> GNU findutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/findutils/#get-help">https://www.gnu.org/software/findutils/#get-help</a>&gt; <br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt; </p>
<p> Report any other issue via the form at the GNU Savannah bug tracker: </p>
<dl>
<dd> <p> &lt;<a rel="nofollow" href="https://savannah.gnu.org/bugs/?group=findutils">https://savannah.gnu.org/bugs/?group=findutils</a>&gt; </p>
 </dd></dl>
<p> General topics about the GNU findutils package are discussed at the <i>bug-findutils</i> mailing list: </p>
<dl>
<dd> <p> &lt;<a rel="nofollow" href="https://lists.gnu.org/mailman/listinfo/bug-findutils">https://lists.gnu.org/mailman/listinfo/bug-findutils</a>&gt; </p>
 </dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1990-2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;. <br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1), <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code>updatedb</code>(1), <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1), <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code>locatedb</code>(5), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/findutils/find">https://www.gnu.org/software/findutils/find</a>&gt; <br />
 or available locally via: <code>info find</code> </p>
