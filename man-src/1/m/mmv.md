---
title: "mmv(1)"
name: "mmv"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mmv/"
description: "mmv – move/copy/append/link multiple files by wildcard patterns"
---

<h2>NAME</h2>
<p> mmv &#8211; move/copy/append/link multiple files by wildcard patterns</p>
<h2>SYNOPSIS</h2>
<p> <code>mmv</code> [<code>-h</code>] [<code>-d</code>|<code>p</code>] [<code>-g</code>|<code>t</code>] [<code>-v</code>|<code>n</code>] [<code>&#8212;</code>] [<code>from to</code>]</p>
<h2>EXAMPLES</h2>
<p> Rename all <i>*.jpeg</i> files in the current directory to <i>*.jpg</i>: </p>
<p> mmv &#8216;*.jpeg&#8217; &#8216;#1.jpg&#8217; </p>
<p> Replace the first occurrence of <i>abc</i> with <i>xyz</i> in all files in the current directory: </p>
<p> mmv &#8216;*abc*&#8217; &#8216;#1xyz#2&#8217; </p>
<p> Rename files ending in <i>.html.en</i>, <i>.html.de</i>, etc. to ending in <i>.en.html</i>, <i>.de.html</i>, etc. in the current directory: </p>
<p> mmv &#8216;*.html.??&#8217; &#8216;#1.#2#3.html&#8217; </p>
<p> Rename music files from <i>&lt;track no.&gt; &#8211; &lt;interpreter&gt; &#8211; &lt;song title&gt;.ogg</i> to <i>&lt;interpreter&gt; &#8211; &lt;track no.&gt; &#8211; &lt;song title&gt;.ogg</i> in the current directory: </p>
<p> mmv &#8216;* &#8211; * &#8211; *.ogg&#8217; &#8216;#2 &#8211; #1 &#8211; #3.ogg&#8217; </p>
<h2>DESCRIPTION</h2>
<p> <i>Mmv</i> moves (or copies, appends, or links, as specified) each source file matching a <i>from</i> pattern to the target name specified by the <i>to</i> pattern. This multiple action is performed safely, i.e. without any unexpected deletion of files due to collisions of target names with existing filenames or with other target names. Furthermore, before doing anything, <i>mmv</i> attempts to detect any errors that would result from the entire set of actions specified and gives the user the choice of either proceeding by avoiding the offending parts or aborting. <i>mmv</i> does support large files (LFS) but it does *NOT* support sparse files (i.e. it explodes them). </p>
<p> <center> The Task Options<br />
 </center> </p>
<p> Whether <i>mmv</i> moves, copies, appends, or links is governed by the first set of options given above. If none of these are specified, the task is given by the command name under which <i>mmv</i> was invoked (argv[0]): </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>command name<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>default task</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mmv<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-x</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mcp<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-c</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mad<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-a</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mln<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-l</p>
<p> The task option choices are:</p>
<dl>
<dt>-m :</p>
<dd> move source file to target name. Both must be on the same device. Will not move directories.</p>
<dt>-x :</p>
<dd> same as -m, except cross-device moves are done by copying, then deleting source. When copying, sets the permission bits and file modification time of the target file to that of the source file.</p>
<dt>-r :</p>
<dd> rename source file or directory to target name. The target name must not include a path: the file remains in the same directory in all cases. This option is the only way of renaming directories under <i>mmv</i>.</p>
<dt>-c :</p>
<dd> copy source file to target name. Sets the file modification time and permission bits of the target file to that of the source file, regardless of whether the target file already exists. Chains and cycles (to be explained below) are not allowed.</p>
<dt>-o :</p>
<dd> overwrite target name with source file. If target file exists, it is overwritten, keeping its original owner and permission bits. If it does not exist, it is created, with read-write permission bits set according to <i><a href="/docs/linux/man/1-umask/">umask</a></i>(1), and the execute permission bits copied from the source file. In either case, the file modification time is set to the current time.</p>
<dt>-a :</p>
<dd> append contents of source file to target name. Target file modification time is set to the current time. If target file does not exist, it is created with permission bits set as under -o. Unlike all other options, -a allows multiple source files to have the same target name, e.g. &quot;mmv -a \*.c big&quot; will append all &quot;.c&quot; files to &quot;big&quot;. Chains and cycles are also allowed, so &quot;mmv -a f f&quot; will double up &quot;f&quot;.</p>
<dt>-l :</p>
<dd> link target name to source file. Both must be on the same device, and the source must not be a directory. Chains and cycles are not allowed.</dl>
<p> Only one of these option may be given, and it applies to all matching files. Remaining options need not be given separately, i.e. &quot;mmv -mk&quot; is allowed. </p>
<p> <center> Multiple Pattern Pairs / Reading Patterns from STDIN<br />
 </center> </p>
<p> Multiple <i>from</i> &#8212; <i>to</i> pattern pairs may be specified by omitting the pattern pair on the command line, and entering them on the standard input, one pair per line. (If a pattern pair is given on the command line, the standard input is not read.) Thus, </p>
<p> mmv<br />
 a b<br />
 c d </p>
<p> would rename &quot;a&quot; to &quot;b&quot; and &quot;c&quot; to &quot;d&quot;. If a file can be matched to several of the given <i>from</i> patterns, the <i>to</i> pattern of the first matching pair is used. Thus, </p>
<p> mmv<br />
 a b<br />
 a c </p>
<p> would give the error message &quot;a -&gt; c : no match&quot; because file &quot;a&quot; (even if it exists) was already matched by the first pattern pair. </p>
<p> <code>WARNING:</code> This operation mode does <code>not</code> work if the patterns itself contain <code>spaces</code>. See <i><a rel="nofollow" href="http://bugs.debian.org/149873">http://bugs.debian.org/149873</a></i> for details. </p>
<p> <center> The <i>From</i> Pattern<br />
 </center> </p>
<p> The <i>from</i> pattern is a filename with embedded wildcards: &#8216;*&#8217;, &#8216;?&#8217;, &#8216;[&#8216;&#8230;&#8217;]&#8217;, and &#8216;;&#8217;. The first three have their usual <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1) meanings of, respectively, matching any string of characters, matching any single character, and matching any one of a set of characters. </p>
<p> Between the &#8216;[&#8216; and &#8216;]&#8217;, a range from character &#8216;a&#8217; through character &#8216;z&#8217; is specified with &quot;a-z&quot;. The set of matching characters can be negated by inserting a &#8216;^&#8217; after the &#8216;[&#8216;. Thus, &quot;[^b-e2-5_]&quot; will match any character but &#8216;b&#8217; through &#8216;e&#8217;, &#8216;2&#8217; through &#8216;5&#8217;, and &#8216;_&#8217;. </p>
<p> Note that paths are allowed in the patterns, and wildcards may be intermingled with slashes arbitrarily. The &#8216;;&#8217; wildcard is useful for matching files at any depth in the directory tree. It matches the same as &quot;*/&quot; repeated any number of times, including zero, and can only occur either at the beginning of the pattern or following a &#8216;/&#8217;. Thus &quot;;*.c&quot; will match all &quot;.c&quot; files in or below the current directory, while &quot;/;*.c&quot; will match them anywhere on the file system. </p>
<p> In addition, if the <i>from</i> pattern (or the <i>to</i> pattern) begins with &quot;~/&quot;, the &#8216;~&#8217; is replaced with the home directory name. (Note that the &quot;~user&quot; feature of <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) is not implemented.) However, the &#8216;~&#8217; is not treated as a wildcard, in the sense that it is not assigned a wildcard index (see below). </p>
<p> Since matching a directory under a task option other than -r or -s would result in an error, tasks other than -r and -s match directories only against completely explicit <i>from</i> patterns (i.e. not containing wildcards). Under -r and -s, this applies only to &quot;.&quot; and &quot;..&quot;. </p>
<p> Files beginning with &#8216;.&#8217; are only matched against <i>from</i> patterns that begin with an explicit &#8216;.&#8217;. However, if -h is specified, they are matched normally. </p>
<p> Warning: since the shell normally expands wildcards before passing the command-line arguments to <i>mmv</i>, it is usually necessary to enclose the command-line <i>from</i> and <i>to</i> patterns in quotes. </p>
<p> <center> The <i>To</i> Pattern<br />
 </center> </p>
<p> The <i>to</i> pattern is a filename with embedded <i>wildcard</i> <i>indexes</i>, where an index consists of the character &#8216;#&#8217; followed by a string of digits. When a source file matches a <i>from</i> pattern, a target name for the file is constructed out of the <i>to</i> pattern by replacing the wildcard indexes by the actual characters that matched the referenced wildcards in the source name. Thus, if the <i>from</i> pattern is &quot;abc*.*&quot; and the <i>to</i> pattern is &quot;xyz#2.#1&quot;, then &quot;abc.txt&quot; is targeted to &quot;xyztxt.&quot;. (The first &#8216;*&#8217; matched &quot;&quot;, and the second matched &quot;txt&quot;.) Similarly, for the pattern pair &quot;;*.[clp]&quot; -&gt; &quot;#1#3/#2&quot;, &quot;foo1/foo2/prog.c&quot; is targeted to &quot;foo1/foo2/c/prog&quot;. Note that there is no &#8216;/&#8217; following the &quot;#1&quot; in the <i>to</i> pattern, since the string matched by any &#8216;;&#8217; is always either empty or ends in a &#8216;/&#8217;. In this case, it matches &quot;foo1/foo2/&quot;. </p>
<p> To convert the string matched by a wildcard to either lowercase or uppercase before embedding it in the target name, insert &#8216;l&#8217; or &#8216;u&#8217;, respectively, between the &#8216;#&#8217; and the string of digits. </p>
<p> The <i>to</i> pattern, like the <i>from</i> pattern, can begin with a &quot;~/&quot; (see above). This does not necessitate enclosing the <i>to</i> pattern in quotes on the command line since <i><a href="/docs/linux/man/1-csh/">csh</a></i>(1) expands the &#8216;~&#8217; in the exact same manner as <i>mmv</i> (or, in the case of <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), does not expand it at all). </p>
<p> For all task options other than -r, if the target name is a directory, the real target name is formed by appending a &#8216;/&#8217; followed by the last component of the source file name. For example, &quot;mmv dir1/a dir2&quot; will, if &quot;dir2&quot; is indeed a directory, actually move &quot;dir1/a&quot; to &quot;dir2/a&quot;. However, if &quot;dir2/a&quot; already exists and is itself a directory, this is considered an error. </p>
<p> To strip any character (e.g. &#8216;*&#8217;, &#8216;?&#8217;, or &#8216;#&#8217;) of its special meaning to <i>mmv</i>, as when the actual replacement name must contain the character &#8216;#&#8217;, precede the special character with a &#8216;\&#8217; (and enclose the argument in quotes because of the shell). This also works to terminate a wildcard index when it has to be followed by a digit in the filename, e.g. &quot;a#11&quot;. </p>
<p> <center> Chains and Cycles<br />
 </center> </p>
<p> A chain is a sequence of specified actions where the target name of one action refers to the source file of another action. For example, </p>
<p> mmv<br />
 a b<br />
 b c </p>
<p> specifies the chain &quot;a&quot; -&gt; &quot;b&quot; -&gt; &quot;c&quot;. A cycle is a chain where the last target name refers back to the first source file, e.g. &quot;mmv a a&quot;. <i>Mmv</i> detects chains and cycles regardless of the order in which their constituent actions are actually given. Where allowed, i.e. in moving, renaming, and appending files, chains and cycles are handled gracefully, by performing them in the proper order. Cycles are broken by first renaming one of the files to a temporary name (or just remembering its original size when doing appends). </p>
<p> <center> Collisions and Deletions<br />
 </center> </p>
<p> When any two or more matching files would have to be moved, copied, or linked to the same target filename, <i>mmv</i> detects the condition as an error before performing any actions. Furthermore, <i>mmv</i> checks if any of its actions will result in the destruction of existing files. If the -d (delete) option is specified, all file deletions or overwrites are done silently. Under -p (protect), all deletions or overwrites (except those specified with &quot;(*)&quot; on the standard input, see below) are treated as errors. And if neither option is specified, the user is queried about each deletion or overwrite separately. (A new stream to &quot;/dev/tty&quot; is used for all interactive queries, not the standard input.) </p>
<p> <center> Error Handling<br />
 </center> </p>
<p> Whenever any error in the user&#8217;s action specifications is detected, an error message is given on the standard output, and <i>mmv</i> proceeds to check the rest of the specified actions. Once all errors are detected, <i>mmv</i> queries the user whether he wishes to continue by avoiding the erroneous actions or to abort altogether. This and all other queries may be avoided by specifying either the -g (go) or -t (terminate) option. The former will resolve all difficulties by avoiding the erroneous actions; the latter will abort <i>mmv</i> if any errors are detected. Specifying either of them defaults <i>mmv</i> to -p, unless -d is specified (see above). Thus, -g and -t are most useful when running <i>mmv</i> in the background or in a shell script, when interactive queries are undesirable. </p>
<p> <center> Reports<br />
 </center> </p>
<p> Once the actions to be performed are determined, <i>mmv</i> performs them silently, unless either the -v (verbose) or -n (no-execute) option is specified. The former causes <i>mmv</i> to report each performed action on the standard output as </p>
<p> a -&gt; b : done. </p>
<p> Here, &quot;a&quot; and &quot;b&quot; would be replaced by the source and target names, respectively. If the action deletes the old target, a &quot;(*)&quot; is inserted after the the target name. Also, the &quot;-&gt;&quot; symbol is modified when a cycle has to be broken: the &#8216;&gt;&#8217; is changed to a &#8216;^&#8217; on the action prior to which the old target is renamed to a temporary, and the &#8216;-&#8216; is changed to a &#8216;=&#8217; on the action where the temporary is used. </p>
<p> Under -n, none of the actions are performed, but messages like the above are printed on the standard output with the &quot;: done.&quot; omitted. </p>
<p> The output generated by -n can (after editing, if desired) be fed back to <i>mmv</i> on the standard input (by omitting the <i>from</i> &#8212; <i>to</i> pair on the <i>mmv</i> command line). To facilitate this, <i>mmv</i> ignores lines on the standard input that look like its own error and &quot;done&quot; messages, as well as all lines beginning with white space, and will accept pattern pairs with or without the intervening &quot;-&gt;&quot; (or &quot;-^&quot;, &quot;=&gt;&quot;, or &quot;=^&quot;). Lines with &quot;(*)&quot; after the target pattern have the effect of enabling -d for the files matching this pattern only, so that such deletions are done silently. </p>
<p> <code>WARNING:</code> This means that <code>unexpected things</code> may happen if <code>files</code> matched by the patterns contain <code>spaces</code>. See <i><a rel="nofollow" href="http://bugs.debian.org/149873">http://bugs.debian.org/149873</a></i> for details. </p>
<p> When feeding <i>mmv</i> its own output, one must remember to specify again the task option (if any) originally used to generate it. </p>
<p> Although <i>mmv</i> attempts to predict all mishaps prior to performing any specified actions, accidents may happen. For example, <i>mmv</i> does not check for adequate free space when copying. Thus, despite all efforts, it is still possible for an action to fail after some others have already been done. To make recovery as easy as possible, <i>mmv</i> reports which actions have already been done and which are still to be performed after such a failure occurs. It then aborts, not attempting to do anything else. Once the user has cleared up the problem, he can feed this report back to <i>mmv</i> on the standard input to have it complete the task. (The user is queried for a file name to dump this report if the standard output has not been redirected.)</p>
<h2>EXIT STATUS</h2>
<p> <i>Mmv</i> exits with status 1 if it aborts before doing anything, with status 2 if it aborts due to failure after completing some of the actions, and with status 0 otherwise.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mv/">mv</a>(1), <a href="/docs/linux/man/1-cp/">cp</a>(1), <a href="/docs/linux/man/1-ln/">ln</a>(1), <a href="/docs/linux/man/1-umask/">umask</a>(1)</p>
<h2>AUTHOR</h2>
<p> Vladimir Lanin<br />
 lanin [at] csd2.nyu.edu</p>
<h2>BUGS</h2>
<p> If the search pattern is not quoted, the shell expands the wildcards. <i>Mmv</i> then (usually) gives some error message, but can not determine that the lack of quotes is the cause. </p>
<p> To avoid difficulties in semantics and error checking, <i>mmv</i> refuses to move or create directories. </p>
<h2>Index</h2>
