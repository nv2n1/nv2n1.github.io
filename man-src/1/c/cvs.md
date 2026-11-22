---

title: "cvs(1)"
name: "cvs"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cvs/"
description: "cvs – Concurrent Versions System"
---

<p> cvs - Concurrent Versions System </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>cvs</code> [ <i>cvs_options</i> ]</dt>
<dd> <p> <i>cvs_command</i> [ <i>command_options</i> ] [ <i>command_args</i> ] </p>
 </dd></dl>
<h2>NOTE</h2>
<p> This manpage is a summary of some of the features of <code>cvs</code>. It is auto-generated from an appendix of the CVS manual. For more in-depth documentation, please consult the Cederqvist manual (via the <code>info CVS</code> command or otherwise, as described in the SEE ALSO section of this manpage). Cross-references in this man page refer to nodes in the same.  </p>
<h2>CVS commands</h2>
<h3>Guide to CVS commands</h3>
<p> This appendix describes the overall structure of <code>cvs</code> commands, and describes some commands in detail (others are described elsewhere; for a quick reference to <code>cvs</code> commands, see node `Invoking CVS&#8217; in the CVS manual). </p>
<h2>Structure</h2>
<h3>Overall structure of CVS commands</h3>
<p> The overall format of all <code>cvs</code> commands is: </p>
<dl>
<dd> <p> cvs [ cvs_options ] cvs_command [ command_options ] [ command_args ] </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>cvs</code> </p>
 </dd>
<dd> <p> The name of the <code>cvs</code> program. </p>
 </dd>
<dd> <p> <code>cvs_options</code> </p>
 </dd>
<dd> <p> Some options that affect all sub-commands of <code>cvs</code>. These are described below. </p>
 </dd>
<dd> <p> <code>cvs_command</code> </p>
 </dd>
<dd> <p> One of several different sub-commands. Some of the commands have aliases that can be used instead; those aliases are noted in the reference manual for that command. There are only two situations where you may omit <code>cvs_command</code>: <code>cvs -H</code> elicits a list of available commands, and <code>cvs -v</code> displays version information on <code>cvs</code> itself. </p>
 </dd>
<dd> <p> <code>command_options</code> </p>
 </dd>
<dd> <p> Options that are specific for the command. </p>
 </dd>
<dd> <p> <code>command_args</code> </p>
 </dd>
<dd> <p> Arguments to the commands. </p>
<p> There is unfortunately some confusion between <code>cvs_options</code> and <code>command_options</code>. When given as a <code>cvs_option</code>, some options only affect some of the commands. When given as a <code>command_option</code> it may have a different meaning, and be accepted by more commands. In other words, do not take the above categorization too seriously. Look at the documentation instead. </p>
 </dd></dl>
<h2>Exit status</h2>
<h3>CVS's exit status</h3>
<p> <code>cvs</code> can indicate to the calling environment whether it succeeded or failed by setting its <i>exit status</i>. The exact way of testing the exit status will vary from one operating system to another. For example in a unix shell script the <code>$?</code> variable will be 0 if the last command returned a successful exit status, or greater than 0 if the exit status indicated failure. </p>
<p> If <code>cvs</code> is successful, it returns a successful status; if there is an error, it prints an error message and returns a failure status. The one exception to this is the <code>cvs diff</code> command. It will return a successful status if it found no differences, or a failure status if there were differences or if there was an error. Because this behavior provides no good way to detect errors, in the future it is possible that <code>cvs diff</code> will be changed to behave like the other <code>cvs</code> commands. </p>
<h2>~/.cvsrc</h2>
<h3>Default options and the ~/.cvsrc file</h3>
<p> There are some <code>command_options</code> that are used so often that you might have set up an alias or some other means to make sure you always specify that option. One example (the one that drove the implementation of the <code>.cvsrc</code> support, actually) is that many people find the default output of the <code>diff</code> command to be very hard to read, and that either context diffs or unidiffs are much easier to understand. </p>
<p> The <code>~/.cvsrc</code> file is a way that you can add default options to <code>cvs_commands</code> within cvs, instead of relying on aliases or other shell scripts. </p>
<p> The format of the <code>~/.cvsrc</code> file is simple. The file is searched for a line that begins with the same name as the <code>cvs_command</code> being executed. If a match is found, then the remainder of the line is split up (at whitespace characters) into separate options and added to the command arguments <i>before</i> any options from the command line. </p>
<p> If a command has two names (e.g., <code>checkout</code> and <code>co</code>), the official name, not necessarily the one used on the command line, will be used to match against the file. So if this is the contents of the user&#8217;s <code>~/.cvsrc</code> file: </p>
<dl>
<dd> <p> log -N </p>
 </dd>
<dd> <p> diff -uN </p>
 </dd>
<dd> <p> rdiff -u </p>
 </dd>
<dd> <p> update -Pd </p>
 </dd>
<dd> <p> checkout -P </p>
 </dd>
<dd> <p> release -d </p>
 </dd>
<dd> <p> the command <code>cvs checkout foo</code> would have the <code>-P</code> option added to the arguments, as well as <code>cvs co foo</code>. </p>
<p> With the example file above, the output from <code>cvs diff foobar</code> will be in unidiff format. <code>cvs diff -c foobar</code> will provide context diffs, as usual. Getting &quot;old&quot; format diffs would be slightly more complicated, because <code>diff</code> doesn&#8217;t have an option to specify use of the &quot;old&quot; format, so you would need <code>cvs -f diff foobar</code>. </p>
<p> In place of the command name you can use <code>cvs</code> to specify global options (see node `Global options&#8217; in the CVS manual). For example the following line in <code>.cvsrc</code> </p>
 </dd>
<dd> <p> cvs -z6 </p>
 </dd>
<dd> <p> causes <code>cvs</code> to use compression level 6. </p>
 </dd></dl>
<h2>Global options</h2>
<p> The available <code>cvs_options</code> (that are given to the left of <code>cvs_command</code>) are: </p>
<dl>
<dd> <p> <code>--allow-root=</code><i>rootdir</i> </p>
 </dd>
<dd> <p> Specify legal <code>cvsroot</code> directory. See `Password authentication server&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-a</code> </p>
 </dd>
<dd> <p> Authenticate all communication between the client and the server. Only has an effect on the <code>cvs</code> client. As of this writing, this is only implemented when using a GSSAPI connection (see node `GSSAPI authenticated&#8217; in the CVS manual). Authentication prevents certain sorts of attacks involving hijacking the active <code>tcp</code> connection. Enabling authentication does not enable encryption. </p>
 </dd>
<dd> <p> <code>-b </code><i>bindir</i> </p>
 </dd>
<dd> <p> In <code>cvs</code> 1.9.18 and older, this specified that <code>rcs</code> programs are in the <i>bindir</i> directory. Current versions of <code>cvs</code> do not run <code>rcs</code> programs; for compatibility this option is accepted, but it does nothing. </p>
 </dd>
<dd> <p> <code>-T </code><i>tempdir</i> </p>
 </dd>
<dd> <p> Use <i>tempdir</i> as the directory where temporary files are located. Overrides the setting of the <code>$TMPDIR</code> environment variable and any precompiled directory. This parameter should be specified as an absolute pathname. (When running client/server, <code>-T</code> affects only the local process; specifying <code>-T</code> for the client has no effect on the server and vice versa.) </p>
 </dd>
<dd> <p> <code>-d </code><i>cvs_root_directory</i> </p>
 </dd>
<dd> <p> Use <i>cvs_root_directory</i> as the root directory pathname of the repository. Overrides the setting of the <code>$CVSROOT</code> environment variable. See `Repository&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-e </code><i>editor</i> </p>
 </dd>
<dd> <p> Use <i>editor</i> to enter revision log information. Overrides the setting of the <code>$CVSEDITOR</code> and <code>$EDITOR</code> environment variables. For more information, see `Committing your changes&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-f</code> </p>
 </dd>
<dd> <p> Do not read the <code>~/.cvsrc</code> file. This option is most often used because of the non-orthogonality of the <code>cvs</code> option set. For example, the <code>cvs log</code> option <code>-N</code> (turn off display of tag names) does not have a corresponding option to turn the display on. So if you have <code>-N</code> in the <code>~/.cvsrc</code> entry for <code>log</code>, you may need to use <code>-f</code> to show the tag names. </p>
 </dd>
<dd> <p> <code>-H</code> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>--help</code> </p>
 </dd>
<dd> <p> Display usage information about the specified <code>cvs_command</code> (but do not actually execute the command). If you don&#8217;t specify a command name, <code>cvs -H</code> displays overall help for <code>cvs</code>, including a list of other help options. </p>
 </dd>
<dd> <p> <code>-n</code> </p>
 </dd>
<dd> <p> Do not change any files. Attempt to execute the <code>cvs_command</code>, but only to issue reports; do not remove, update, or merge any existing files, or create any new files. </p>
<p> Note that <code>cvs</code> will not necessarily produce exactly the same output as without <code>-n</code>. In some cases the output will be the same, but in other cases <code>cvs</code> will skip some of the processing that would have been required to produce the exact same output. </p>
 </dd>
<dd> <p> <code>-Q</code> </p>
 </dd>
<dd> <p> Cause the command to be really quiet; the command will only generate output for serious problems. </p>
 </dd>
<dd> <p> <code>-q</code> </p>
 </dd>
<dd> <p> Cause the command to be somewhat quiet; informational messages, such as reports of recursion through subdirectories, are suppressed. </p>
 </dd>
<dd> <p> <code>-r</code> </p>
 </dd>
<dd> <p> Make new working files read-only. Same effect as if the <code>$CVSREAD</code> environment variable is set (see node `Environment variables&#8217; in the CVS manual). The default is to make working files writable, unless watches are on (see node `Watches&#8217; in the CVS manual). </p>
 </dd>
<dd> <p> <code>-s </code><i>variable</i><code>=</code><i>value</i> </p>
 </dd>
<dd> <p> Set a user variable (see node `Variables&#8217; in the CVS manual). </p>
 </dd>
<dd> <p> <code>-t</code> </p>
 </dd>
<dd> <p> Trace program execution; display messages showing the steps of <code>cvs</code> activity. Particularly useful with <code>-n</code> to explore the potential impact of an unfamiliar command. </p>
 </dd>
<dd> <p> <code>-v</code> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>--version</code> </p>
 </dd>
<dd> <p> Display version and copyright information for <code>cvs</code>. </p>
 </dd>
<dd> <p> <code>-w</code> </p>
 </dd>
<dd> <p> Make new working files read-write. Overrides the setting of the <code>$CVSREAD</code> environment variable. Files are created read-write by default, unless <code>$CVSREAD</code> is set or <code>-r</code> is given. </p>
 </dd>
<dd> <p> <code>-x</code> </p>
 </dd>
<dd> <p> Encrypt all communication between the client and the server. Only has an effect on the <code>cvs</code> client. As of this writing, this is only implemented when using a GSSAPI connection (see node `GSSAPI authenticated&#8217; in the CVS manual) or a Kerberos connection (see node `Kerberos authenticated&#8217; in the CVS manual). Enabling encryption implies that message traffic is also authenticated. Encryption support is not available by default; it must be enabled using a special configure option, <code>--enable-encryption</code>, when you build <code>cvs</code>. </p>
 </dd>
<dd> <p> <code>-z </code><i>gzip-level</i> </p>
 </dd>
<dd> <p> Set the compression level. Valid levels are 1 (high speed, low compression) to 9 (low speed, high compression), or 0 to disable compression (the default). Only has an effect on the <code>cvs</code> client. </p>
 </dd></dl>
<h2>Common options</h2>
<h3>Common command options</h3>
<p> This section describes the <code>command_options</code> that are available across several <code>cvs</code> commands. These options are always given to the right of <code>cvs_command</code>. Not all commands support all of these options; each option is only supported for commands where it makes sense. However, when a command has one of these options you can almost always count on the same behavior of the option as in other commands. (Other command options, which are listed with the individual commands, may have different behavior from one <code>cvs</code> command to the other). </p>
<p> <code>The history command is an exception; it supports many options that conflict even with these standard options.</code> </p>
<dl>
<dd> <p> <code>-D </code><i>date_spec</i> </p>
 </dd>
<dd> <p> Use the most recent revision no later than <i>date_spec</i>. <i>date_spec</i> is a single argument, a date description specifying a date in the past. </p>
<p> The specification is <i>sticky</i> when you use it to make a private copy of a source file; that is, when you get a working file using <code>-D</code>, <code>cvs</code> records the date you specified, so that further updates in the same directory will use the same date (for more information on sticky tags/dates, see node `Sticky tags&#8217; in the CVS manual). </p>
<p> <code>-D</code> is available with the <code>annotate</code>, <code>checkout</code>, <code>diff</code>, <code>export</code>, <code>history</code>, <code>rdiff</code>, <code>rtag</code>, and <code>update</code> commands. (The <code>history</code> command uses this option in a slightly different way; see node `history options&#8217; in the CVS manual). </p>
<p> A wide variety of date formats are supported by <code>cvs</code>. The most standard ones are ISO8601 (from the International Standards Organization) and the Internet e-mail standard (specified in RFC822 as amended by RFC1123). </p>
<p> ISO8601 dates have many variants but a few examples are: </p>
 </dd>
<dd> <p> 1972-09-24 </p>
 </dd>
<dd> <p> 1972-09-24 20:05 </p>
 </dd>
<dd> <p> There are a lot more ISO8601 date formats, and <code>cvs</code> accepts many of them, but you probably don&#8217;t want to hear the <i>whole</i> long story :-). </p>
<p> In addition to the dates allowed in Internet e-mail itself, <code>cvs</code> also allows some of the fields to be omitted. For example: </p>
 </dd>
<dd> <p> 24 Sep 1972 20:05 </p>
 </dd>
<dd> <p> 24 Sep </p>
 </dd>
<dd> <p> The date is interpreted as being in the local timezone, unless a specific timezone is specified. </p>
<p> These two date formats are preferred. However, <code>cvs</code> currently accepts a wide variety of other date formats. They are intentionally not documented here in any detail, and future versions of <code>cvs</code> might not accept all of them. </p>
<p> One such format is <i>month</i><code>/</code><i>day</i><code>/</code><i>year</i>. This may confuse people who are accustomed to having the month and day in the other order; <code>1/4/96</code> is January 4, not April 1. </p>
<p> Remember to quote the argument to the <code>-D</code> flag so that your shell doesn&#8217;t interpret spaces as argument separators. A command using the <code>-D</code> flag can look like this: </p>
 </dd>
<dd> <p> $ cvs diff -D &quot;1 hour ago&quot; cvs.texinfo </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>-f</code> </p>
 </dd>
<dd> <p> When you specify a particular date or tag to <code>cvs</code> commands, they normally ignore files that do not contain the tag (or did not exist prior to the date) that you specified. Use the <code>-f</code> option if you want files retrieved even when there is no match for the tag or date. (The most recent revision of the file will be used). </p>
<p> Note that even with <code>-f</code>, a tag that you specify must exist (that is, in some file, not necessary in every file). This is so that <code>cvs</code> will continue to give an error if you mistype a tag name. </p>
<p> <code>-f</code> is available with these commands: <code>annotate</code>, <code>checkout</code>, <code>export</code>, <code>rdiff</code>, <code>rtag</code>, and <code>update</code>. </p>
<p> <code>WARNING: The commit and remove commands also have a -f option, but it has a different behavior for those commands. See `commit options&#8217; in the CVS manual, and `Removing files&#8217; in the CVS manual.</code> </p>
 </dd>
<dd> <p> <code>-k </code><i>kflag</i> </p>
 </dd>
<dd> <p> Alter the default processing of keywords. See `Keyword substitution&#8217; in the CVS manual, for the meaning of <i>kflag</i>. Your <i>kflag</i> specification is <i>sticky</i> when you use it to create a private copy of a source file; that is, when you use this option with the <code>checkout</code> or <code>update</code> commands, <code>cvs</code> associates your selected <i>kflag</i> with the file, and continues to use it with future update commands on the same file until you specify otherwise. </p>
<p> The <code>-k</code> option is available with the <code>add</code>, <code>checkout</code>, <code>diff</code>, <code>rdiff</code>, <code>import</code> and <code>update</code> commands. </p>
 </dd>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Local; run only in current working directory, rather than recursing through subdirectories. </p>
<p> Available with the following commands: <code>annotate</code>, <code>checkout</code>, <code>commit</code>, <code>diff</code>, <code>edit</code>, <code>editors</code>, <code>export</code>, <code>log</code>, <code>rdiff</code>, <code>remove</code>, <code>rtag</code>, <code>status</code>, <code>tag</code>, <code>unedit</code>, <code>update</code>, <code>watch</code>, and <code>watchers</code>. </p>
 </dd>
<dd> <p> <code>-m </code><i>message</i> </p>
 </dd>
<dd> <p> Use <i>message</i> as log information, instead of invoking an editor. </p>
<p> Available with the following commands: <code>add</code>, <code>commit</code> and <code>import</code>. </p>
 </dd>
<dd> <p> <code>-n</code> </p>
 </dd>
<dd> <p> Do not run any tag program. (A program can be specified to run in the modules database (see node `modules&#8217; in the CVS manual); this option bypasses it). </p>
<p> <code>This is not the same as the cvs -n program option, which you can specify to the left of a cvs command!</code> </p>
<p> Available with the <code>checkout</code>, <code>export</code>, and <code>rtag</code> commands. </p>
 </dd>
<dd> <p> <code>-P</code> </p>
 </dd>
<dd> <p> Prune empty directories. See `Removing directories&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-p</code> </p>
 </dd>
<dd> <p> Pipe the files retrieved from the repository to standard output, rather than writing them in the current directory. Available with the <code>checkout</code> and <code>update</code> commands. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> Process directories recursively. This is on by default. </p>
<p> Available with the following commands: <code>annotate</code>, <code>checkout</code>, <code>commit</code>, <code>diff</code>, <code>edit</code>, <code>editors</code>, <code>export</code>, <code>rdiff</code>, <code>remove</code>, <code>rtag</code>, <code>status</code>, <code>tag</code>, <code>unedit</code>, <code>update</code>, <code>watch</code>, and <code>watchers</code>. </p>
 </dd>
<dd> <p> <code>-r </code><i>tag</i> </p>
 </dd>
<dd> <p> Use the revision specified by the <i>tag</i> argument instead of the default <i>head</i> revision. As well as arbitrary tags defined with the <code>tag</code> or <code>rtag</code> command, two special tags are always available: <code>HEAD</code> refers to the most recent version available in the repository, and <code>BASE</code> refers to the revision you last checked out into the current working directory. </p>
<p> The tag specification is sticky when you use this with <code>checkout</code> or <code>update</code> to make your own copy of a file: <code>cvs</code> remembers the tag and continues to use it on future update commands, until you specify otherwise (for more information on sticky tags/dates, see node `Sticky tags&#8217; in the CVS manual). </p>
<p> The tag can be either a symbolic or numeric tag, as described in `Tags&#8217; in the CVS manual, or the name of a branch, as described in `Branching and merging&#8217; in the CVS manual. When a command expects a specific revision, the name of a branch is interpreted as the most recent revision on that branch. </p>
<p> Specifying the <code>-q</code> global option along with the <code>-r</code> command option is often useful, to suppress the warning messages when the <code>rcs</code> file does not contain the specified tag. </p>
<p> <code>This is not the same as the overall cvs -r option, which you can specify to the left of a cvs command!</code> </p>
<p> <code>-r</code> is available with the <code>annotate</code>, <code>checkout</code>, <code>commit</code>, <code>diff</code>, <code>history</code>, <code>export</code>, <code>rdiff</code>, <code>rtag</code>, and <code>update</code> commands. </p>
 </dd>
<dd> <p> <code>-W</code> </p>
 </dd>
<dd> <p> Specify file names that should be filtered. You can use this option repeatedly. The spec can be a file name pattern of the same type that you can specify in the <code>.cvswrappers</code> file. Available with the following commands: <code>import</code>, and <code>update</code>. </p>
 </dd></dl>
<h2>add</h2>
<h3>Add files and directories to the repository</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Synopsis: add [-k rcs-kflag] [-m message] files... </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: repository, working directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: repository, working directory. </p>
<p> The <code>add</code> command is used to present new files and directories for addition into the <code>cvs</code> repository. When <code>add</code> is used on a directory, a new directory is created in the repository immediately. When used on a file, only the working directory is updated. Changes to the repository are not made until the <code>commit</code> command is used on the newly added file. </p>
<p> The <code>add</code> command also resurrects files that have been previously removed. This can be done before or after the <code>commit</code> command is used to finalize the removal of files. Resurrected files are restored into the working directory at the time the <code>add</code> command is executed. </p>
 </dd></dl>
<h2>add options</h2>
<p> These standard options are supported by <code>add</code> (see node `Common options&#8217; in the CVS manual, for a complete description of them): </p>
<dl>
<dd> <p> <code>-k </code><i>kflag</i> </p>
 </dd>
<dd> <p> Process keywords according to <i>kflag</i>. See `Keyword substitution&#8217; in the CVS manual. This option is sticky; future updates of this file in this working directory will use the same <i>kflag</i>. The <code>status</code> command can be viewed to see the sticky options. For more information on the <code>status</code> command, see node `Invoking CVS&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-m </code><i>message</i> </p>
 </dd>
<dd> <p> Use <i>message</i> as the log message, instead of invoking an editor. </p>
 </dd></dl>
<h2>add examples</h2>
<h3>Adding a directory</h3>
<dl>
<dd> <p> $ mkdir doc </p>
 </dd>
<dd> <p> $ cvs add doc </p>
 </dd>
<dd> <p> Directory /path/to/repository/doc added to the repository </p>
 </dd>
<dd>  </dd></dl>
<h3>Adding a file</h3>
<dl>
<dd> <p> $ &gt;TODO </p>
 </dd>
<dd> <p> $ cvs add TODO </p>
 </dd>
<dd> <p> cvs add: scheduling file `TODO&#8217; for addition </p>
 </dd>
<dd> <p> cvs add: use &#8216;cvs commit&#8217; to add this file permanently </p>
 </dd>
<dd>  </dd></dl>
<code></code><h3>Undoing a remove command</h3>
<dl>
<dd> <p> $ rm -f makefile </p>
 </dd>
<dd> <p> $ cvs remove makefile </p>
 </dd>
<dd> <p> cvs remove: scheduling `makefile&#8217; for removal </p>
 </dd>
<dd> <p> cvs remove: use &#8216;cvs commit&#8217; to remove this file permanently </p>
 </dd>
<dd> <p> $ cvs add makefile </p>
 </dd>
<dd> <p> U makefile </p>
 </dd>
<dd> <p> cvs add: makefile, version 1.2, resurrected </p>
 </dd>
<dd>  </dd></dl>
<h2>admin</h2>
<h3>Administration</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Requires: repository, working directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: repository. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Synonym: rcs </p>
<p> This is the <code>cvs</code> interface to assorted administrative facilities. Some of them have questionable usefulness for <code>cvs</code> but exist for historical purposes. Some of the questionable options are likely to disappear in the future. This command <i>does</i> work recursively, so extreme care should be used. </p>
<p> On unix, if there is a group named <code>cvsadmin</code>, only members of that group can run <code>cvs admin</code> (except for the <code>cvs admin -k</code> command, which can be run by anybody). This group should exist on the server, or any system running the non-client/server <code>cvs</code>. To disallow <code>cvs admin</code> for all users, create a group with no users in it. On NT, the <code>cvsadmin</code> feature does not exist and all users can run <code>cvs admin</code>. </p>
 </dd></dl>
<h2>admin options</h2>
<p> Some of these options have questionable usefulness for <code>cvs</code> but exist for historical purposes. Some even make it impossible to use <code>cvs</code> until you undo the effect! </p>
<dl>
<dd> <p> <code>-A</code><i>oldfile</i> </p>
 </dd>
<dd> <p> Might not work together with <code>cvs</code>. Append the access list of <i>oldfile</i> to the access list of the <code>rcs</code> file. </p>
 </dd>
<dd> <p> <code>-a</code><i>logins</i> </p>
 </dd>
<dd> <p> Might not work together with <code>cvs</code>. Append the login names appearing in the comma-separated list <i>logins</i> to the access list of the <code>rcs</code> file. </p>
 </dd>
<dd> <p> <code>-b[</code><i>rev</i><code>]</code> </p>
 </dd>
<dd> <p> Set the default branch to <i>rev</i>. In <code>cvs</code>, you normally do not manipulate default branches; sticky tags (see node `Sticky tags&#8217; in the CVS manual) are a better way to decide which branch you want to work on. There is one reason to run <code>cvs admin -b</code>: to revert to the vendor&#8217;s version when using vendor branches (see node `Reverting local changes&#8217; in the CVS manual). There can be no space between <code>-b</code> and its argument. </p>
 </dd>
<dd> <p> <code>-c</code><i>string</i> </p>
 </dd>
<dd> <p> Sets the comment leader to <i>string</i>. The comment leader is not used by current versions of <code>cvs</code> or <code>rcs</code> 5.7. Therefore, you can almost surely not worry about it. See `Keyword substitution&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-e[</code><i>logins</i><code>]</code> </p>
 </dd>
<dd> <p> Might not work together with <code>cvs</code>. Erase the login names appearing in the comma-separated list <i>logins</i> from the access list of the RCS file. If <i>logins</i> is omitted, erase the entire access list. There can be no space between <code>-e</code> and its argument. </p>
 </dd>
<dd> <p> <code>-I</code> </p>
 </dd>
<dd> <p> Run interactively, even if the standard input is not a terminal. This option does not work with the client/server <code>cvs</code> and is likely to disappear in a future release of <code>cvs</code>. </p>
 </dd>
<dd> <p> <code>-i</code> </p>
 </dd>
<dd> <p> Useless with <code>cvs</code>. This creates and initializes a new <code>rcs</code> file, without depositing a revision. With <code>cvs</code>, add files with the <code>cvs add</code> command (see node `Adding files&#8217; in the CVS manual). </p>
 </dd>
<dd> <p> <code>-k</code><i>subst</i> </p>
 </dd>
<dd> <p> Set the default keyword substitution to <i>subst</i>. See `Keyword substitution&#8217; in the CVS manual. Giving an explicit <code>-k</code> option to <code>cvs update</code>, <code>cvs export</code>, or <code>cvs checkout</code> overrides this default. </p>
 </dd>
<dd> <p> <code>-l[</code><i>rev</i><code>]</code> </p>
 </dd>
<dd> <p> Lock the revision with number <i>rev</i>. If a branch is given, lock the latest revision on that branch. If <i>rev</i> is omitted, lock the latest revision on the default branch. There can be no space between <code>-l</code> and its argument. </p>
<p> This can be used in conjunction with the <code>rcslock.pl</code> script in the <code>contrib</code> directory of the <code>cvs</code> source distribution to provide reserved checkouts (where only one user can be editing a given file at a time). See the comments in that file for details (and see the <code>README</code> file in that directory for disclaimers about the unsupported nature of contrib). According to comments in that file, locking must set to strict (which is the default). </p>
 </dd>
<dd> <p> <code>-L</code> </p>
 </dd>
<dd> <p> Set locking to strict. Strict locking means that the owner of an RCS file is not exempt from locking for checkin. For use with <code>cvs</code>, strict locking must be set; see the discussion under the <code>-l</code> option above. </p>
 </dd>
<dd> <p> <code>-m</code><i>rev</i><code>:</code><i>msg</i> </p>
 </dd>
<dd> <p> Replace the log message of revision <i>rev</i> with <i>msg</i>. </p>
 </dd>
<dd> <p> <code>-N</code><i>name</i><code>[:[</code><i>rev</i><code>]]</code> </p>
 </dd>
<dd> <p> Act like <code>-n</code>, except override any previous assignment of <i>name</i>. For use with magic branches, see `Magic branch numbers&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-n</code><i>name</i><code>[:[</code><i>rev</i><code>]]</code> </p>
 </dd>
<dd> <p> Associate the symbolic name <i>name</i> with the branch or revision <i>rev</i>. It is normally better to use <code>cvs tag</code> or <code>cvs rtag</code> instead. Delete the symbolic name if both <code>:</code> and <i>rev</i> are omitted; otherwise, print an error message if <i>name</i> is already associated with another number. If <i>rev</i> is symbolic, it is expanded before association. A <i>rev</i> consisting of a branch number followed by a <code>.</code> stands for the current latest revision in the branch. A <code>:</code> with an empty <i>rev</i> stands for the current latest revision on the default branch, normally the trunk. For example, <code>cvs admin -n</code><i>name</i><code>:</code> associates <i>name</i> with the current latest revision of all the RCS files; this contrasts with <code>cvs admin -n</code><i>name</i><code>:$</code> which associates <i>name</i> with the revision numbers extracted from keyword strings in the corresponding working files. </p>
 </dd>
<dd> <p> <code>-o</code><i>range</i> </p>
 </dd>
<dd> <p> Deletes (<i>outdates</i>) the revisions given by <i>range</i>. </p>
<p> Note that this command can be quite dangerous unless you know <i>exactly</i> what you are doing (for example see the warnings below about how the <i>rev1</i>:<i>rev2</i> syntax is confusing). </p>
<p> If you are short on disc this option might help you. But think twice before using it---there is no way short of restoring the latest backup to undo this command! If you delete different revisions than you planned, either due to carelessness or (heaven forbid) a <code>cvs</code> bug, there is no opportunity to correct the error before the revisions are deleted. It probably would be a good idea to experiment on a copy of the repository first. </p>
<p> Specify <i>range</i> in one of the following ways: </p>
 </dd>
<dd> <p> <i>rev1</i><code>::</code><i>rev2</i> </p>
 </dd>
<dd> <p> Collapse all revisions between rev1 and rev2, so that <code>cvs</code> only stores the differences associated with going from rev1 to rev2, not intermediate steps. For example, after <code>-o 1.3::1.5</code> one can retrieve revision 1.3, revision 1.5, or the differences to get from 1.3 to 1.5, but not the revision 1.4, or the differences between 1.3 and 1.4. Other examples: <code>-o 1.3::1.4</code> and <code>-o 1.3::1.3</code> have no effect, because there are no intermediate revisions to remove. </p>
 </dd>
<dd> <p> <code>::</code><i>rev</i> </p>
 </dd>
<dd> <p> Collapse revisions between the beginning of the branch containing <i>rev</i> and <i>rev</i> itself. The branchpoint and <i>rev</i> are left intact. For example, <code>-o ::1.3.2.6</code> deletes revision 1.3.2.1, revision 1.3.2.5, and everything in between, but leaves 1.3 and 1.3.2.6 intact. </p>
 </dd>
<dd> <p> <i>rev</i><code>::</code> </p>
 </dd>
<dd> <p> Collapse revisions between <i>rev</i> and the end of the branch containing <i>rev</i>. Revision <i>rev</i> is left intact but the head revision is deleted. </p>
 </dd>
<dd> <p> <i>rev</i> </p>
 </dd>
<dd> <p> Delete the revision <i>rev</i>. For example, <code>-o 1.3</code> is equivalent to <code>-o 1.2::1.4</code>. </p>
 </dd>
<dd> <p> <i>rev1</i><code>:</code><i>rev2</i> </p>
 </dd>
<dd> <p> Delete the revisions from <i>rev1</i> to <i>rev2</i>, inclusive, on the same branch. One will not be able to retrieve <i>rev1</i> or <i>rev2</i> or any of the revisions in between. For example, the command <code>cvs admin -oR_1_01:R_1_02 .</code> is rarely useful. It means to delete revisions up to, and including, the tag R_1_02. But beware! If there are files that have not changed between R_1_02 and R_1_03 the file will have <i>the same</i> numerical revision number assigned to the tags R_1_02 and R_1_03. So not only will it be impossible to retrieve R_1_02; R_1_03 will also have to be restored from the tapes! In most cases you want to specify <i>rev1</i>::<i>rev2</i> instead. </p>
 </dd>
<dd> <p> <code>:</code><i>rev</i> </p>
 </dd>
<dd> <p> Delete revisions from the beginning of the branch containing <i>rev</i> up to and including <i>rev</i>. </p>
 </dd>
<dd> <p> <i>rev</i><code>:</code> </p>
 </dd>
<dd> <p> Delete revisions from revision <i>rev</i>, including <i>rev</i> itself, to the end of the branch containing <i>rev</i>. </p>
<p> None of the revisions to be deleted may have branches or locks. </p>
<p> If any of the revisions to be deleted have symbolic names, and one specifies one of the <code>::</code> syntaxes, then <code>cvs</code> will give an error and not delete any revisions. If you really want to delete both the symbolic names and the revisions, first delete the symbolic names with <code>cvs tag -d</code>, then run <code>cvs admin -o</code>. If one specifies the non-<code>::</code> syntaxes, then <code>cvs</code> will delete the revisions but leave the symbolic names pointing to nonexistent revisions. This behavior is preserved for compatibility with previous versions of <code>cvs</code>, but because it isn&#8217;t very useful, in the future it may change to be like the <code>::</code> case. </p>
<p> Due to the way <code>cvs</code> handles branches <i>rev</i> cannot be specified symbolically if it is a branch. See `Magic branch numbers&#8217; in the CVS manual for an explanation. </p>
<p> Make sure that no-one has checked out a copy of the revision you outdate. Strange things will happen if he starts to edit it and tries to check it back in. For this reason, this option is not a good way to take back a bogus commit; commit a new revision undoing the bogus change instead (see node `Merging two revisions&#8217; in the CVS manual). </p>
 </dd>
<dd> <p> <code>-q</code> </p>
 </dd>
<dd> <p> Run quietly; do not print diagnostics. </p>
 </dd>
<dd> <p> <code>-s</code><i>state</i><code>[:</code><i>rev</i><code>]</code> </p>
 </dd>
<dd> <p> Useful with <code>cvs</code>. Set the state attribute of the revision <i>rev</i> to <i>state</i>. If <i>rev</i> is a branch number, assume the latest revision on that branch. If <i>rev</i> is omitted, assume the latest revision on the default branch. Any identifier is acceptable for <i>state</i>. A useful set of states is <code>Exp</code> (for experimental), <code>Stab</code> (for stable), and <code>Rel</code> (for released). By default, the state of a new revision is set to <code>Exp</code> when it is created. The state is visible in the output from <i>cvs log</i> (see node `log&#8217; in the CVS manual), and in the <code>$</code>Log$ and <code>$</code>State$ keywords (see node `Keyword substitution&#8217; in the CVS manual). Note that <code>cvs</code> uses the <code>dead</code> state for its own purposes (see node `Attic&#8217; in the CVS manual); to take a file to or from the <code>dead</code> state use commands like <code>cvs remove</code> and <code>cvs add</code> (see node `Adding and removing&#8217; in the CVS manual), not <code>cvs admin -s</code>. </p>
 </dd>
<dd> <p> <code>-t[</code><i>file</i><code>]</code> </p>
 </dd>
<dd> <p> Useful with <code>cvs</code>. Write descriptive text from the contents of the named <i>file</i> into the RCS file, deleting the existing text. The <i>file</i> pathname may not begin with <code>-</code>. The descriptive text can be seen in the output from <code>cvs log</code> (see node `log&#8217; in the CVS manual). There can be no space between <code>-t</code> and its argument. </p>
<p> If <i>file</i> is omitted, obtain the text from standard input, terminated by end-of-file or by a line containing <code>.</code> by itself. Prompt for the text if interaction is possible; see <code>-I</code>. </p>
 </dd>
<dd> <p> <code>-t-</code><i>string</i> </p>
 </dd>
<dd> <p> Similar to <code>-t</code><i>file</i>. Write descriptive text from the <i>string</i> into the <code>rcs</code> file, deleting the existing text. There can be no space between <code>-t</code> and its argument. </p>
 </dd>
<dd> <p> <code>-U</code> </p>
 </dd>
<dd> <p> Set locking to non-strict. Non-strict locking means that the owner of a file need not lock a revision for checkin. For use with <code>cvs</code>, strict locking must be set; see the discussion under the <code>-l</code> option above. </p>
 </dd>
<dd> <p> <code>-u[</code><i>rev</i><code>]</code> </p>
 </dd>
<dd> <p> See the option <code>-l</code> above, for a discussion of using this option with <code>cvs</code>. Unlock the revision with number <i>rev</i>. If a branch is given, unlock the latest revision on that branch. If <i>rev</i> is omitted, remove the latest lock held by the caller. Normally, only the locker of a revision may unlock it; somebody else unlocking a revision breaks the lock. This causes the original locker to be sent a <code>commit</code> notification (see node `Getting Notified&#8217; in the CVS manual). There can be no space between <code>-u</code> and its argument. </p>
 </dd>
<dd> <p> <code>-V</code><i>n</i> </p>
 </dd>
<dd> <p> In previous versions of <code>cvs</code>, this option meant to write an <code>rcs</code> file which would be acceptable to <code>rcs</code> version <i>n</i>, but it is now obsolete and specifying it will produce an error. </p>
 </dd>
<dd> <p> <code>-x</code><i>suffixes</i> </p>
 </dd>
<dd> <p> In previous versions of <code>cvs</code>, this was documented as a way of specifying the names of the <code>rcs</code> files. However, <code>cvs</code> has always required that the <code>rcs</code> files used by <code>cvs</code> end in <code>,v</code>, so this option has never done anything useful. </p>
 </dd></dl>
<h2>annotate</h2>
<h3>What revision modified each line of a file?</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Synopsis: annotate [options] files... </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: repository. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Synonym: blame </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: nothing. </p>
<p> For each file in <i>files</i>, print the head revision of the trunk, together with information on the last modification for each line. </p>
 </dd></dl>
<h2>annotate options</h2>
<p> These standard options are supported by <code>annotate</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Local directory only, no recursion. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> Process directories recursively. </p>
 </dd>
<dd> <p> <code>-f</code> </p>
 </dd>
<dd> <p> Use head revision if tag/date not found. </p>
 </dd>
<dd> <p> <code>-F</code> </p>
 </dd>
<dd> <p> Annotate binary files. </p>
 </dd>
<dd> <p> <code>-r </code><i>revision</i> </p>
 </dd>
<dd> <p> Annotate file as of specified revision/tag. </p>
 </dd>
<dd> <p> <code>-D </code><i>date</i> </p>
 </dd>
<dd> <p> Annotate file as of specified date. </p>
 </dd></dl>
<h2>annotate example</h2>
<p> For example: </p>
<dl>
<dd> <p> $ cvs annotate ssfile </p>
 </dd>
<dd> <p> Annotations for ssfile </p>
 </dd>
<dd> <p> *************** </p>
 </dd>
<dd> <p> 1.1 (mary 27-Mar-96): ssfile line 1 </p>
 </dd>
<dd> <p> 1.2 (joe 28-Mar-96): ssfile line 2 </p>
 </dd>
<dd> <p> The file <code>ssfile</code> currently contains two lines. The <code>ssfile line 1</code> line was checked in by <code>mary</code> on March 27. Then, on March 28, <code>joe</code> added a line <code>ssfile line 2</code>, without modifying the <code>ssfile line 1</code> line. This report doesn&#8217;t tell you anything about lines which have been deleted or replaced; you need to use <code>cvs diff</code> for that (see node `diff&#8217; in the CVS manual). </p>
<p> The options to <code>cvs annotate</code> are listed in `Invoking CVS&#8217; in the CVS manual, and can be used to select the files and revisions to annotate. The options are described in more detail there and in `Common options&#8217; in the CVS manual. </p>
 </dd></dl>
<h2>checkout</h2>
<h3>Check out sources for editing</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Synopsis: checkout [options] modules... </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: repository. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: working directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Synonyms: co, get </p>
<p> Create or update a working directory containing copies of the source files specified by <i>modules</i>. You must execute <code>checkout</code> before using most of the other <code>cvs</code> commands, since most of them operate on your working directory. </p>
<p> The <i>modules</i> are either symbolic names for some collection of source directories and files, or paths to directories or files in the repository. The symbolic names are defined in the <code>modules</code> file. See `modules&#8217; in the CVS manual. </p>
<p> Depending on the modules you specify, <code>checkout</code> may recursively create directories and populate them with the appropriate source files. You can then edit these source files at any time (regardless of whether other software developers are editing their own copies of the sources); update them to include new changes applied by others to the source repository; or commit your work as a permanent change to the source repository. </p>
<p> Note that <code>checkout</code> is used to create directories. The top-level directory created is always added to the directory where <code>checkout</code> is invoked, and usually has the same name as the specified module. In the case of a module alias, the created sub-directory may have a different name, but you can be sure that it will be a sub-directory, and that <code>checkout</code> will show the relative path leading to each file as it is extracted into your private work area (unless you specify the <code>-Q</code> global option). </p>
<p> The files created by <code>checkout</code> are created read-write, unless the <code>-r</code> option to <code>cvs</code> (see node `Global options&#8217; in the CVS manual) is specified, the <code>CVSREAD</code> environment variable is specified (see node `Environment variables&#8217; in the CVS manual), or a watch is in effect for that file (see node `Watches&#8217; in the CVS manual). </p>
<p> Note that running <code>checkout</code> on a directory that was already built by a prior <code>checkout</code> is also permitted. This is similar to specifying the <code>-d</code> option to the <code>update</code> command in the sense that new directories that have been created in the repository will appear in your work area. However, <code>checkout</code> takes a module name whereas <code>update</code> takes a directory name. Also to use <code>checkout</code> this way it must be run from the top level directory (where you originally ran <code>checkout</code> from), so before you run <code>checkout</code> to update an existing directory, don&#8217;t forget to change your directory to the top level directory. </p>
<p> For the output produced by the <code>checkout</code> command, see node `update output&#8217; in the CVS manual. </p>
 </dd></dl>
<h2>checkout options</h2>
<p> These standard options are supported by <code>checkout</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dd> <p> <code>-D </code><i>date</i> </p>
 </dd>
<dd> <p> Use the most recent revision no later than <i>date</i>. This option is sticky, and implies <code>-P</code>. See `Sticky tags&#8217; in the CVS manual for more information on sticky tags/dates. </p>
 </dd>
<dd> <p> <code>-f</code> </p>
 </dd>
<dd> <p> Only useful with the <code>-D </code><i>date</i> or <code>-r </code><i>tag</i> flags. If no matching revision is found, retrieve the most recent revision (instead of ignoring the file). </p>
 </dd>
<dd> <p> <code>-k </code><i>kflag</i> </p>
 </dd>
<dd> <p> Process keywords according to <i>kflag</i>. See `Keyword substitution&#8217; in the CVS manual. This option is sticky; future updates of this file in this working directory will use the same <i>kflag</i>. The <code>status</code> command can be viewed to see the sticky options. See `Invoking CVS&#8217; in the CVS manual for more information on the <code>status</code> command. </p>
 </dd>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Local; run only in current working directory. </p>
 </dd>
<dd> <p> <code>-n</code> </p>
 </dd>
<dd> <p> Do not run any checkout program (as specified with the <code>-o</code> option in the modules file; see node `modules&#8217; in the CVS manual). </p>
 </dd>
<dd> <p> <code>-P</code> </p>
 </dd>
<dd> <p> Prune empty directories. See `Moving directories&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-p</code> </p>
 </dd>
<dd> <p> Pipe files to the standard output. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> Checkout directories recursively. This option is on by default. </p>
 </dd>
<dd> <p> <code>-r </code><i>tag</i> </p>
 </dd>
<dd> <p> Use revision <i>tag</i>. This option is sticky, and implies <code>-P</code>. See `Sticky tags&#8217; in the CVS manual, for more information on sticky tags/dates. </p>
<p> In addition to those, you can use these special command options with <code>checkout</code>: </p>
 </dd>
<dd> <p> <code>-A</code> </p>
 </dd>
<dd> <p> Reset any sticky tags, dates, or <code>-k</code> options. Does not reset sticky <code>-k</code> options on modified files. See `Sticky tags&#8217; in the CVS manual for more information on sticky tags/dates. </p>
 </dd>
<dd> <p> <code>-c</code> </p>
 </dd>
<dd> <p> Copy the module file, sorted, to the standard output, instead of creating or modifying any files or directories in your working directory. </p>
 </dd>
<dd> <p> <code>-d </code><i>dir</i> </p>
 </dd>
<dd> <p> Create a directory called <i>dir</i> for the working files, instead of using the module name. In general, using this flag is equivalent to using <code>mkdir </code><i>dir</i><code>; cd </code><i>dir</i> followed by the checkout command without the <code>-d</code> flag. </p>
<p> There is an important exception, however. It is very convenient when checking out a single item to have the output appear in a directory that doesn&#8217;t contain empty intermediate directories. In this case <i>only</i>, <code>cvs</code> tries to ``shorten&#8217;&#8216; pathnames to avoid those empty directories. </p>
<p> For example, given a module <code>foo</code> that contains the file <code>bar.c</code>, the command <code>cvs co -d dir foo</code> will create directory <code>dir</code> and place <code>bar.c</code> inside. Similarly, given a module <code>bar</code> which has subdirectory <code>baz</code> wherein there is a file <code>quux.c</code>, the command <code>cvs co -d dir bar/baz</code> will create directory <code>dir</code> and place <code>quux.c</code> inside. </p>
<p> Using the <code>-N</code> flag will defeat this behavior. Given the same module definitions above, <code>cvs co -N -d dir foo</code> will create directories <code>dir/foo</code> and place <code>bar.c</code> inside, while <code>cvs co -N -d dir bar/baz</code> will create directories <code>dir/bar/baz</code> and place <code>quux.c</code> inside. </p>
 </dd>
<dd> <p> <code>-j </code><i>tag</i> </p>
 </dd>
<dd> <p> With two <code>-j</code> options, merge changes from the revision specified with the first <code>-j</code> option to the revision specified with the second <code>j</code> option, into the working directory. </p>
<p> With one <code>-j</code> option, merge changes from the ancestor revision to the revision specified with the <code>-j</code> option, into the working directory. The ancestor revision is the common ancestor of the revision which the working directory is based on, and the revision specified in the <code>-j</code> option. </p>
<p> In addition, each -j option can contain an optional date specification which, when used with branches, can limit the chosen revision to one within a specific date. An optional date is specified by adding a colon (:) to the tag: <code>-j</code><i>Symbolic_Tag</i><code>:</code><i>Date_Specifier</i>. </p>
<p> See `Branching and merging&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-N</code> </p>
 </dd>
<dd> <p> Only useful together with <code>-d </code><i>dir</i>. With this option, <code>cvs</code> will not ``shorten&#8217;&#8216; module paths in your working directory when you check out a single module. See the <code>-d</code> flag for examples and a discussion. </p>
 </dd>
<dd> <p> <code>-s</code> </p>
 </dd>
<dd> <p> Like <code>-c</code>, but include the status of all modules, and sort it by the status string. See `modules&#8217; in the CVS manual, for info about the <code>-s</code> option that is used inside the modules file to set the module status. </p>
 </dd></dl>
<h2>checkout examples</h2>
<p> Get a copy of the module <code>tc</code>: </p>
<dl>
<dd> <p> $ cvs checkout tc </p>
 </dd>
<dd> <p> Get a copy of the module <code>tc</code> as it looked one day ago: </p>
 </dd>
<dd> <p> $ cvs checkout -D yesterday tc </p>
 </dd>
<dd>  </dd></dl>
<h2>commit</h2>
<h3>Check files into the repository</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Synopsis: commit [-lRf] [-m &#8216;log_message&#8217; | -F file] [-r revision] [files...] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: working directory, repository. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: repository. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Synonym: ci </p>
<p> Use <code>commit</code> when you want to incorporate changes from your working source files into the source repository. </p>
<p> If you don&#8217;t specify particular files to commit, all of the files in your working current directory are examined. <code>commit</code> is careful to change in the repository only those files that you have really changed. By default (or if you explicitly specify the <code>-R</code> option), files in subdirectories are also examined and committed if they have changed; you can use the <code>-l</code> option to limit <code>commit</code> to the current directory only. </p>
<p> <code>commit</code> verifies that the selected files are up to date with the current revisions in the source repository; it will notify you, and exit without committing, if any of the specified files must be made current first with <code>update</code> (see node `update&#8217; in the CVS manual). <code>commit</code> does not call the <code>update</code> command for you, but rather leaves that for you to do when the time is right. </p>
<p> When all is well, an editor is invoked to allow you to enter a log message that will be written to one or more logging programs (see node `modules&#8217; in the CVS manual, and see node `loginfo&#8217; in the CVS manual) and placed in the <code>rcs</code> file inside the repository. This log message can be retrieved with the <code>log</code> command; see node `log&#8217; in the CVS manual. You can specify the log message on the command line with the <code>-m </code><i>message</i> option, and thus avoid the editor invocation, or use the <code>-F </code><i>file</i> option to specify that the argument file contains the log message. </p>
 </dd></dl>
<h2>commit options</h2>
<p> These standard options are supported by <code>commit</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Local; run only in current working directory. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> Commit directories recursively. This is on by default. </p>
 </dd>
<dd> <p> <code>-r </code><i>revision</i> </p>
 </dd>
<dd> <p> Commit to <i>revision</i>. <i>revision</i> must be either a branch, or a revision on the main trunk that is higher than any existing revision number (see node `Assigning revisions&#8217; in the CVS manual). You cannot commit to a specific revision on a branch. </p>
<p> <code>commit</code> also supports these options: </p>
 </dd>
<dd> <p> <code>-F </code><i>file</i> </p>
 </dd>
<dd> <p> Read the log message from <i>file</i>, instead of invoking an editor. </p>
 </dd>
<dd> <p> <code>-f</code> </p>
 </dd>
<dd> <p> Note that this is not the standard behavior of the <code>-f</code> option as defined in `Common options&#8217; in the CVS manual. </p>
<p> Force <code>cvs</code> to commit a new revision even if you haven&#8217;t made any changes to the file. If the current revision of <i>file</i> is 1.7, then the following two commands are equivalent: </p>
 </dd>
<dd> <p> $ cvs commit -f <i>file</i> </p>
 </dd>
<dd> <p> $ cvs commit -r 1.8 <i>file</i> </p>
 </dd>
<dd> <p> The <code>-f</code> option disables recursion (i.e., it implies <code>-l</code>). To force <code>cvs</code> to commit a new revision for all files in all subdirectories, you must use <code>-f -R</code>. </p>
 </dd>
<dd> <p> <code>-m </code><i>message</i> </p>
 </dd>
<dd> <p> Use <i>message</i> as the log message, instead of invoking an editor. </p>
 </dd></dl>
<h2>commit examples</h2>
<h3>Committing to a branch</h3>
<p> You can commit to a branch revision (one that has an even number of dots) with the <code>-r</code> option. To create a branch revision, use the <code>-b</code> option of the <code>rtag</code> or <code>tag</code> commands (see node `Branching and merging&#8217; in the CVS manual). Then, either <code>checkout</code> or <code>update</code> can be used to base your sources on the newly created branch. From that point on, all <code>commit</code> changes made within these working sources will be automatically added to a branch revision, thereby not disturbing main-line development in any way. For example, if you had to create a patch to the 1.2 version of the product, even though the 2.0 version is already under development, you might do: </p>
<dl>
<dd> <p> $ cvs rtag -b -r FCS1_2 FCS1_2_Patch product_module </p>
 </dd>
<dd> <p> $ cvs checkout -r FCS1_2_Patch product_module </p>
 </dd>
<dd> <p> $ cd product_module </p>
 </dd>
<dd> <p> [[ hack away ]] </p>
 </dd>
<dd> <p> $ cvs commit </p>
 </dd>
<dd> <p> This works automatically since the <code>-r</code> option is sticky. </p>
 </dd></dl>
<h3>Creating the branch after editing</h3>
<p> Say you have been working on some extremely experimental software, based on whatever revision you happened to checkout last week. If others in your group would like to work on this software with you, but without disturbing main-line development, you could commit your change to a new branch. Others can then checkout your experimental stuff and utilize the full benefit of <code>cvs</code> conflict resolution. The scenario might look like: </p>
<dl>
<dd> <p> [[ hacked sources are present ]] </p>
 </dd>
<dd> <p> $ cvs tag -b EXPR1 </p>
 </dd>
<dd> <p> $ cvs update -r EXPR1 </p>
 </dd>
<dd> <p> $ cvs commit </p>
 </dd>
<dd> <p> The <code>update</code> command will make the <code>-r EXPR1</code> option sticky on all files. Note that your changes to the files will never be removed by the <code>update</code> command. The <code>commit</code> will automatically commit to the correct branch, because the <code>-r</code> is sticky. You could also do like this: </p>
 </dd>
<dd> <p> [[ hacked sources are present ]] </p>
 </dd>
<dd> <p> $ cvs tag -b EXPR1 </p>
 </dd>
<dd> <p> $ cvs commit -r EXPR1 </p>
 </dd>
<dd> <p> but then, only those files that were changed by you will have the <code>-r EXPR1</code> sticky flag. If you hack away, and commit without specifying the <code>-r EXPR1</code> flag, some files may accidentally end up on the main trunk. </p>
<p> To work with you on the experimental change, others would simply do </p>
 </dd>
<dd> <p> $ cvs checkout -r EXPR1 whatever_module </p>
 </dd>
<dd>  </dd></dl>
<h2>diff</h2>
<h3>Show differences between revisions</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Synopsis: diff [-lR] [-k kflag] [format_options] [[-r rev1 | -D date1] [-r rev2 | -D date2]] [files...] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: working directory, repository. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: nothing. </p>
<p> The <code>diff</code> command is used to compare different revisions of files. The default action is to compare your working files with the revisions they were based on, and report any differences that are found. </p>
<p> If any file names are given, only those files are compared. If any directories are given, all files under them will be compared. </p>
<p> The exit status for diff is different than for other <code>cvs</code> commands; for details see node `Exit status&#8217; in the CVS manual. </p>
 </dd></dl>
<h2>diff options</h2>
<p> These standard options are supported by <code>diff</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dd> <p> <code>-D </code><i>date</i> </p>
 </dd>
<dd> <p> Use the most recent revision no later than <i>date</i>. See <code>-r</code> for how this affects the comparison. </p>
 </dd>
<dd> <p> <code>-k </code><i>kflag</i> </p>
 </dd>
<dd> <p> Process keywords according to <i>kflag</i>. See `Keyword substitution&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Local; run only in current working directory. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> Examine directories recursively. This option is on by default. </p>
 </dd>
<dd> <p> <code>-r </code><i>tag</i> </p>
 </dd>
<dd> <p> Compare with revision <i>tag</i>. Zero, one or two <code>-r</code> options can be present. With no <code>-r</code> option, the working file will be compared with the revision it was based on. With one <code>-r</code>, that revision will be compared to your current working file. With two <code>-r</code> options those two revisions will be compared (and your working file will not affect the outcome in any way). </p>
<p> One or both <code>-r</code> options can be replaced by a <code>-D </code><i>date</i> option, described above. </p>
<p> The following options specify the format of the output. They have the same meaning as in GNU diff. Most options have two equivalent names, one of which is a single letter preceded by <code>-</code>, and the other of which is a long name preceded by <code>--</code>. </p>
 </dd>
<dd> <p> <code>-</code><i>lines</i> </p>
 </dd>
<dd> <p> Show <i>lines</i> (an integer) lines of context. This option does not specify an output format by itself; it has no effect unless it is combined with <code>-c</code> or <code>-u</code>. This option is obsolete. For proper operation, <code>patch</code> typically needs at least two lines of context. </p>
 </dd>
<dd> <p> <code>-a</code> </p>
 </dd>
<dd> <p> Treat all files as text and compare them line-by-line, even if they do not seem to be text. </p>
 </dd>
<dd> <p> <code>-b</code> </p>
 </dd>
<dd> <p> Ignore trailing white space and consider all other sequences of one or more white space characters to be equivalent. </p>
 </dd>
<dd> <p> <code>-B</code> </p>
 </dd>
<dd> <p> Ignore changes that just insert or delete blank lines. </p>
 </dd>
<dd> <p> <code>--binary</code> </p>
 </dd>
<dd> <p> Read and write data in binary mode. </p>
 </dd>
<dd> <p> <code>--brief</code> </p>
 </dd>
<dd> <p> Report only whether the files differ, not the details of the differences. </p>
 </dd>
<dd> <p> <code>-c</code> </p>
 </dd>
<dd> <p> Use the context output format. </p>
 </dd>
<dd> <p> <code>-C </code><i>lines</i> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>--context</code>[<code>=</code><i>lines</i>] </p>
 </dd>
<dd> <p> Use the context output format, showing <i>lines</i> (an integer) lines of context, or three if <i>lines</i> is not given. For proper operation, <code>patch</code> typically needs at least two lines of context. </p>
 </dd>
<dd> <p> <code>--changed-group-format=</code><i>format</i> </p>
 </dd>
<dd> <p> Use <i>format</i> to output a line group containing differing lines from both files in if-then-else format. See `Line group formats&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-d</code> </p>
 </dd>
<dd> <p> Change the algorithm to perhaps find a smaller set of changes. This makes <code>diff</code> slower (sometimes much slower). </p>
 </dd>
<dd> <p> <code>-e</code> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>--ed</code> </p>
 </dd>
<dd> <p> Make output that is a valid <code>ed</code> script. </p>
 </dd>
<dd> <p> <code>--expand-tabs</code> </p>
 </dd>
<dd> <p> Expand tabs to spaces in the output, to preserve the alignment of tabs in the input files. </p>
 </dd>
<dd> <p> <code>-f</code> </p>
 </dd>
<dd> <p> Make output that looks vaguely like an <code>ed</code> script but has changes in the order they appear in the file. </p>
 </dd>
<dd> <p> <code>-F </code><i>regexp</i> </p>
 </dd>
<dd> <p> In context and unified format, for each hunk of differences, show some of the last preceding line that matches <i>regexp</i>. </p>
 </dd>
<dd> <p> <code>--forward-ed</code> </p>
 </dd>
<dd> <p> Make output that looks vaguely like an <code>ed</code> script but has changes in the order they appear in the file. </p>
 </dd>
<dd> <p> <code>-H</code> </p>
 </dd>
<dd> <p> Use heuristics to speed handling of large files that have numerous scattered small changes. </p>
 </dd>
<dd> <p> <code>--horizon-lines=</code><i>lines</i> </p>
 </dd>
<dd> <p> Do not discard the last <i>lines</i> lines of the common prefix and the first <i>lines</i> lines of the common suffix. </p>
 </dd>
<dd> <p> <code>-i</code> </p>
 </dd>
<dd> <p> Ignore changes in case; consider upper- and lower-case letters equivalent. </p>
 </dd>
<dd> <p> <code>-I </code><i>regexp</i> </p>
 </dd>
<dd> <p> Ignore changes that just insert or delete lines that match <i>regexp</i>. </p>
 </dd>
<dd> <p> <code>--ifdef=</code><i>name</i> </p>
 </dd>
<dd> <p> Make merged if-then-else output using <i>name</i>. </p>
 </dd>
<dd> <p> <code>--ignore-all-space</code> </p>
 </dd>
<dd> <p> Ignore white space when comparing lines. </p>
 </dd>
<dd> <p> <code>--ignore-blank-lines</code> </p>
 </dd>
<dd> <p> Ignore changes that just insert or delete blank lines. </p>
 </dd>
<dd> <p> <code>--ignore-case</code> </p>
 </dd>
<dd> <p> Ignore changes in case; consider upper- and lower-case to be the same. </p>
 </dd>
<dd> <p> <code>--ignore-matching-lines=</code><i>regexp</i> </p>
 </dd>
<dd> <p> Ignore changes that just insert or delete lines that match <i>regexp</i>. </p>
 </dd>
<dd> <p> <code>--ignore-space-change</code> </p>
 </dd>
<dd> <p> Ignore trailing white space and consider all other sequences of one or more white space characters to be equivalent. </p>
 </dd>
<dd> <p> <code>--initial-tab</code> </p>
 </dd>
<dd> <p> Output a tab rather than a space before the text of a line in normal or context format. This causes the alignment of tabs in the line to look normal. </p>
 </dd>
<dd> <p> <code>-L </code><i>label</i> </p>
 </dd>
<dd> <p> Use <i>label</i> instead of the file name in the context format and unified format headers. </p>
 </dd>
<dd> <p> <code>--label=</code><i>label</i> </p>
 </dd>
<dd> <p> Use <i>label</i> instead of the file name in the context format and unified format headers. </p>
 </dd>
<dd> <p> <code>--left-column</code> </p>
 </dd>
<dd> <p> Print only the left column of two common lines in side by side format. </p>
 </dd>
<dd> <p> <code>--line-format=</code><i>format</i> </p>
 </dd>
<dd> <p> Use <i>format</i> to output all input lines in if-then-else format. See `Line formats&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>--minimal</code> </p>
 </dd>
<dd> <p> Change the algorithm to perhaps find a smaller set of changes. This makes <code>diff</code> slower (sometimes much slower). </p>
 </dd>
<dd> <p> <code>-n</code> </p>
 </dd>
<dd> <p> Output RCS-format diffs; like <code>-f</code> except that each command specifies the number of lines affected. </p>
 </dd>
<dd> <p> <code>-N</code> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>--new-file</code> </p>
 </dd>
<dd> <p> In directory comparison, if a file is found in only one directory, treat it as present but empty in the other directory. </p>
 </dd>
<dd> <p> <code>--new-group-format=</code><i>format</i> </p>
 </dd>
<dd> <p> Use <i>format</i> to output a group of lines taken from just the second file in if-then-else format. See `Line group formats&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>--new-line-format=</code><i>format</i> </p>
 </dd>
<dd> <p> Use <i>format</i> to output a line taken from just the second file in if-then-else format. See `Line formats&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>--old-group-format=</code><i>format</i> </p>
 </dd>
<dd> <p> Use <i>format</i> to output a group of lines taken from just the first file in if-then-else format. See `Line group formats&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>--old-line-format=</code><i>format</i> </p>
 </dd>
<dd> <p> Use <i>format</i> to output a line taken from just the first file in if-then-else format. See `Line formats&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-p</code> </p>
 </dd>
<dd> <p> Show which C function each change is in. </p>
 </dd>
<dd> <p> <code>--rcs</code> </p>
 </dd>
<dd> <p> Output RCS-format diffs; like <code>-f</code> except that each command specifies the number of lines affected. </p>
 </dd>
<dd> <p> <code>--report-identical-files</code> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>-s</code> </p>
 </dd>
<dd> <p> Report when two files are the same. </p>
 </dd>
<dd> <p> <code>--show-c-function</code> </p>
 </dd>
<dd> <p> Show which C function each change is in. </p>
 </dd>
<dd> <p> <code>--show-function-line=</code><i>regexp</i> </p>
 </dd>
<dd> <p> In context and unified format, for each hunk of differences, show some of the last preceding line that matches <i>regexp</i>. </p>
 </dd>
<dd> <p> <code>--side-by-side</code> </p>
 </dd>
<dd> <p> Use the side by side output format. </p>
 </dd>
<dd> <p> <code>--speed-large-files</code> </p>
 </dd>
<dd> <p> Use heuristics to speed handling of large files that have numerous scattered small changes. </p>
 </dd>
<dd> <p> <code>--suppress-common-lines</code> </p>
 </dd>
<dd> <p> Do not print common lines in side by side format. </p>
 </dd>
<dd> <p> <code>-t</code> </p>
 </dd>
<dd> <p> Expand tabs to spaces in the output, to preserve the alignment of tabs in the input files. </p>
 </dd>
<dd> <p> <code>-T</code> </p>
 </dd>
<dd> <p> Output a tab rather than a space before the text of a line in normal or context format. This causes the alignment of tabs in the line to look normal. </p>
 </dd>
<dd> <p> <code>--text</code> </p>
 </dd>
<dd> <p> Treat all files as text and compare them line-by-line, even if they do not appear to be text. </p>
 </dd>
<dd> <p> <code>-u</code> </p>
 </dd>
<dd> <p> Use the unified output format. </p>
 </dd>
<dd> <p> <code>--unchanged-group-format=</code><i>format</i> </p>
 </dd>
<dd> <p> Use <i>format</i> to output a group of common lines taken from both files in if-then-else format. see node `Line group formats&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>--unchanged-line-format=</code><i>format</i> </p>
 </dd>
<dd> <p> Use <i>format</i> to output a line common to both files in if-then-else format. see node `Line formats&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-U </code><i>lines</i> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>--unified</code>[<code>=</code><i>lines</i>] </p>
 </dd>
<dd> <p> Use the unified output format, showing <i>lines</i> (an integer) lines of context, or three if <i>lines</i> is not given. For proper operation, <code>patch</code> typically needs at least two lines of context. </p>
 </dd>
<dd> <p> <code>-w</code> </p>
 </dd>
<dd> <p> Ignore white space when comparing lines. </p>
 </dd>
<dd> <p> <code>-W </code><i>columns</i> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>--width=</code><i>columns</i> </p>
 </dd>
<dd> <p> Use an output width of <i>columns</i> in side by side format. </p>
 </dd>
<dd> <p> <code>-y</code> </p>
 </dd>
<dd> <p> Use the side by side output format. </p>
 </dd></dl>
<h2>Line group formats</h2>
<p> Line group formats let you specify formats suitable for many applications that allow if-then-else input, including programming languages and text formatting languages. A line group format specifies the output format for a contiguous group of similar lines. </p>
<p> For example, the following command compares the TeX file <code>myfile</code> with the original version from the repository, and outputs a merged file in which old regions are surrounded by <code>\begin{em}</code>-<code>\end{em}</code> lines, and new regions are surrounded by <code>\begin{bf}</code>-<code>\end{bf}</code> lines. </p>
<dl>
<dd> <p> cvs diff \ </p>
 </dd>
<dd> <p> <br/>
--old-group-format=&#8216;\begin{em} </p>
 </dd>
<dd> <p> %&lt;\end{em} </p>
 </dd>
<dd> <p> &#8216; \ </p>
 </dd>
<dd> <p> <br/>
--new-group-format=&#8216;\begin{bf} </p>
 </dd>
<dd> <p> %&gt;\end{bf} </p>
 </dd>
<dd> <p> &#8216; \ </p>
 </dd>
<dd> <p> <br/>
myfile </p>
 </dd>
<dd> <p> The following command is equivalent to the above example, but it is a little more verbose, because it spells out the default line group formats. </p>
 </dd>
<dd> <p> cvs diff \ </p>
 </dd>
<dd> <p> <br/>
--old-group-format=&#8216;\begin{em} </p>
 </dd>
<dd> <p> %&lt;\end{em} </p>
 </dd>
<dd> <p> &#8216; \ </p>
 </dd>
<dd> <p> <br/>
--new-group-format=&#8216;\begin{bf} </p>
 </dd>
<dd> <p> %&gt;\end{bf} </p>
 </dd>
<dd> <p> &#8216; \ </p>
 </dd>
<dd> <p> <br/>
--unchanged-group-format=&#8216;%=&#8216;&nbsp;<wbr>\ </p>
 </dd>
<dd> <p> <br/>
--changed-group-format=&#8216;\begin{em} </p>
 </dd>
<dd> <p> %&lt;\end{em} </p>
 </dd>
<dd> <p> \begin{bf} </p>
 </dd>
<dd> <p> %&gt;\end{bf} </p>
 </dd>
<dd> <p> &#8216; \ </p>
 </dd>
<dd> <p> <br/>
myfile </p>
 </dd>
<dd> <p> Here is a more advanced example, which outputs a diff listing with headers containing line numbers in a ``plain English&#8217;&#8216; style. </p>
 </dd>
<dd> <p> cvs diff \ </p>
 </dd>
<dd> <p> <br/>
--unchanged-group-format=&#8216;&#8216;&nbsp;<wbr>\ </p>
 </dd>
<dd> <p> <br/>
--old-group-format=&#8216;--------&nbsp;<wbr>%dn line%(n=1?:s)&nbsp;<wbr>deleted at&nbsp;<wbr>%df: </p>
 </dd>
<dd> <p> %&lt;&#8216; \ </p>
 </dd>
<dd> <p> <br/>
--new-group-format=&#8216;--------&nbsp;<wbr>%dN line%(N=1?:s)&nbsp;<wbr>added after&nbsp;<wbr>%de: </p>
 </dd>
<dd> <p> %&gt;&#8216; \ </p>
 </dd>
<dd> <p> <br/>
--changed-group-format=&#8216;--------&nbsp;<wbr>%dn line%(n=1?:s)&nbsp;<wbr>changed at&nbsp;<wbr>%df: </p>
 </dd>
<dd> <p> %&lt;-------- to: </p>
 </dd>
<dd> <p> %&gt;&#8216; \ </p>
 </dd>
<dd> <p> <br/>
myfile </p>
 </dd>
<dd> <p> To specify a line group format, use one of the options listed below. You can specify up to four line group formats, one for each kind of line group. You should quote <i>format</i>, because it typically contains shell metacharacters. </p>
 </dd>
<dd> <p> <code>--old-group-format=</code><i>format</i> </p>
 </dd>
<dd> <p> These line groups are hunks containing only lines from the first file. The default old group format is the same as the changed group format if it is specified; otherwise it is a format that outputs the line group as-is. </p>
 </dd>
<dd> <p> <code>--new-group-format=</code><i>format</i> </p>
 </dd>
<dd> <p> These line groups are hunks containing only lines from the second file. The default new group format is same as the changed group format if it is specified; otherwise it is a format that outputs the line group as-is. </p>
 </dd>
<dd> <p> <code>--changed-group-format=</code><i>format</i> </p>
 </dd>
<dd> <p> These line groups are hunks containing lines from both files. The default changed group format is the concatenation of the old and new group formats. </p>
 </dd>
<dd> <p> <code>--unchanged-group-format=</code><i>format</i> </p>
 </dd>
<dd> <p> These line groups contain lines common to both files. The default unchanged group format is a format that outputs the line group as-is. </p>
<p> In a line group format, ordinary characters represent themselves; conversion specifications start with <code>%</code> and have one of the following forms. </p>
 </dd>
<dd> <p> <code>%&lt;</code> </p>
 </dd>
<dd> <p> stands for the lines from the first file, including the trailing newline. Each line is formatted according to the old line format (see node `Line formats&#8217; in the CVS manual). </p>
 </dd>
<dd> <p> <code>%&gt;</code> </p>
 </dd>
<dd> <p> stands for the lines from the second file, including the trailing newline. Each line is formatted according to the new line format. </p>
 </dd>
<dd> <p> <code>%=</code> </p>
 </dd>
<dd> <p> stands for the lines common to both files, including the trailing newline. Each line is formatted according to the unchanged line format. </p>
 </dd>
<dd> <p> <code>%%</code> </p>
 </dd>
<dd> <p> stands for <code>%</code>. </p>
 </dd>
<dd> <p> <code>%c&#8217;</code><i>C</i><code>&#8216;</code> </p>
 </dd>
<dd> <p> where <i>C</i> is a single character, stands for <i>C</i>. <i>C</i> may not be a backslash or an apostrophe. For example, <code>%c&#8217;:&#8216;</code> stands for a colon, even inside the then-part of an if-then-else format, which a colon would normally terminate. </p>
 </dd>
<dd> <p> <code>%c&#8217;\</code><i>O</i><code>&#8216;</code> </p>
 </dd>
<dd> <p> where <i>O</i> is a string of 1, 2, or 3 octal digits, stands for the character with octal code <i>O</i>. For example, <code>%c&#8217;\0&#8217;</code> stands for a null character. </p>
 </dd>
<dd> <p> <i>F</i><i>n</i> </p>
 </dd>
<dd> <p> where <i>F</i> is a <code>printf</code> conversion specification and <i>n</i> is one of the following letters, stands for <i>n</i>&#8216;s value formatted with <i>F</i>. </p>
 </dd>
<dd> <p> <code>e</code> </p>
 </dd>
<dd> <p> The line number of the line just before the group in the old file. </p>
 </dd>
<dd> <p> <code>f</code> </p>
 </dd>
<dd> <p> The line number of the first line in the group in the old file; equals <i>e</i> + 1. </p>
 </dd>
<dd> <p> <code>l</code> </p>
 </dd>
<dd> <p> The line number of the last line in the group in the old file. </p>
 </dd>
<dd> <p> <code>m</code> </p>
 </dd>
<dd> <p> The line number of the line just after the group in the old file; equals <i>l</i> + 1. </p>
 </dd>
<dd> <p> <code>n</code> </p>
 </dd>
<dd> <p> The number of lines in the group in the old file; equals <i>l</i> - <i>f</i> + 1. </p>
 </dd>
<dd> <p> <code>E, F, L, M, N</code> </p>
 </dd>
<dd> <p> Likewise, for lines in the new file. </p>
<p> The <code>printf</code> conversion specification can be <code>%d</code>, <code>%o</code>, <code>%x</code>, or <code>%X</code>, specifying decimal, octal, lower case hexadecimal, or upper case hexadecimal output respectively. After the <code>%</code> the following options can appear in sequence: a <code>-</code> specifying left-justification; an integer specifying the minimum field width; and a period followed by an optional integer specifying the minimum number of digits. For example, <code>%5dN</code> prints the number of new lines in the group in a field of width 5 characters, using the <code>printf</code> format <code>&quot;%5d&quot;</code>. </p>
 </dd>
<dd> <p> <code>(</code><i>A</i><code>=</code><i>B</i><code>?</code><i>T</i><code>:</code><i>E</i><code>)</code> </p>
 </dd>
<dd> <p> If <i>A</i> equals <i>B</i> then <i>T</i> else <i>E</i>. <i>A</i> and <i>B</i> are each either a decimal constant or a single letter interpreted as above. This format spec is equivalent to <i>T</i> if <i>A</i>&#8216;s value equals <i>B</i>&#8216;s; otherwise it is equivalent to <i>E</i>. </p>
<p> For example, <code>%(N=0?no:%dN) line%(N=1?:s)</code> is equivalent to <code>no lines</code> if <i>N</i> (the number of lines in the group in the new file) is 0, to <code>1 line</code> if <i>N</i> is 1, and to <code>%dN lines</code> otherwise. </p>
 </dd></dl>
<h2>Line formats</h2>
<p> Line formats control how each line taken from an input file is output as part of a line group in if-then-else format. </p>
<p> For example, the following command outputs text with a one-column change indicator to the left of the text. The first column of output is <code>-</code> for deleted lines, <code>|</code> for added lines, and a space for unchanged lines. The formats contain newline characters where newlines are desired on output. </p>
<dl>
<dd> <p> cvs diff \ </p>
 </dd>
<dd> <p> <br/>
--old-line-format=&#8216;-%l </p>
 </dd>
<dd> <p> &#8216; \ </p>
 </dd>
<dd> <p> <br/>
--new-line-format=&#8216;|%l </p>
 </dd>
<dd> <p> &#8216; \ </p>
 </dd>
<dd> <p> <br/>
--unchanged-line-format=&#8216;&nbsp;<wbr>%l </p>
 </dd>
<dd> <p> &#8216; \ </p>
 </dd>
<dd> <p> <br/>
myfile </p>
 </dd>
<dd> <p> To specify a line format, use one of the following options. You should quote <i>format</i>, since it often contains shell metacharacters. </p>
 </dd>
<dd> <p> <code>--old-line-format=</code><i>format</i> </p>
 </dd>
<dd> <p> formats lines just from the first file. </p>
 </dd>
<dd> <p> <code>--new-line-format=</code><i>format</i> </p>
 </dd>
<dd> <p> formats lines just from the second file. </p>
 </dd>
<dd> <p> <code>--unchanged-line-format=</code><i>format</i> </p>
 </dd>
<dd> <p> formats lines common to both files. </p>
 </dd>
<dd> <p> <code>--line-format=</code><i>format</i> </p>
 </dd>
<dd> <p> formats all lines; in effect, it sets all three above options simultaneously. </p>
<p> In a line format, ordinary characters represent themselves; conversion specifications start with <code>%</code> and have one of the following forms. </p>
 </dd>
<dd> <p> <code>%l</code> </p>
 </dd>
<dd> <p> stands for the contents of the line, not counting its trailing newline (if any). This format ignores whether the line is incomplete. </p>
 </dd>
<dd> <p> <code>%L</code> </p>
 </dd>
<dd> <p> stands for the contents of the line, including its trailing newline (if any). If a line is incomplete, this format preserves its incompleteness. </p>
 </dd>
<dd> <p> <code>%%</code> </p>
 </dd>
<dd> <p> stands for <code>%</code>. </p>
 </dd>
<dd> <p> <code>%c&#8217;</code><i>C</i><code>&#8216;</code> </p>
 </dd>
<dd> <p> where <i>C</i> is a single character, stands for <i>C</i>. <i>C</i> may not be a backslash or an apostrophe. For example, <code>%c&#8217;:&#8216;</code> stands for a colon. </p>
 </dd>
<dd> <p> <code>%c&#8217;\</code><i>O</i><code>&#8216;</code> </p>
 </dd>
<dd> <p> where <i>O</i> is a string of 1, 2, or 3 octal digits, stands for the character with octal code <i>O</i>. For example, <code>%c&#8217;\0&#8217;</code> stands for a null character. </p>
 </dd>
<dd> <p> <i>F</i><code>n</code> </p>
 </dd>
<dd> <p> where <i>F</i> is a <code>printf</code> conversion specification, stands for the line number formatted with <i>F</i>. For example, <code>%.5dn</code> prints the line number using the <code>printf</code> format <code>&quot;%.5d&quot;</code>. see node `Line group formats&#8217; in the CVS manual, for more about printf conversion specifications. </p>
<p> The default line format is <code>%l</code> followed by a newline character. </p>
<p> If the input contains tab characters and it is important that they line up on output, you should ensure that <code>%l</code> or <code>%L</code> in a line format is just after a tab stop (e.g. by preceding <code>%l</code> or <code>%L</code> with a tab character), or you should use the <code>-t</code> or <code>--expand-tabs</code> option. </p>
<p> Taken together, the line and line group formats let you specify many different formats. For example, the following command uses a format similar to <code>diff</code>&#8216;s normal format. You can tailor this command to get fine control over <code>diff</code>&#8216;s output. </p>
 </dd>
<dd> <p> cvs diff \ </p>
 </dd>
<dd> <p> <br/>
--old-line-format=&#8216;&lt;&nbsp;<wbr>%l </p>
 </dd>
<dd> <p> &#8216; \ </p>
 </dd>
<dd> <p> <br/>
--new-line-format=&#8216;&gt;&nbsp;<wbr>%l </p>
 </dd>
<dd> <p> &#8216; \ </p>
 </dd>
<dd> <p> <br/>
--old-group-format=&#8216;%df%(f=l?:,%dl)d%dE </p>
 </dd>
<dd> <p> %&lt;&#8216; \ </p>
 </dd>
<dd> <p> <br/>
--new-group-format=&#8216;%dea%dF%(F=L?:,%dL) </p>
 </dd>
<dd> <p> %&gt;&#8216; \ </p>
 </dd>
<dd> <p> <br/>
--changed-group-format=&#8216;%df%(f=l?:,%dl)c%dF%(F=L?:,%dL) </p>
 </dd>
<dd> <p> %&lt;--- </p>
 </dd>
<dd> <p> %&gt;&#8216; \ </p>
 </dd>
<dd> <p> <br/>
--unchanged-group-format=&#8216;&#8216;&nbsp;<wbr>\ </p>
 </dd>
<dd> <p> <br/>
myfile </p>
 </dd>
<dd>  </dd></dl>
<h2>diff examples</h2>
<p> The following line produces a Unidiff (<code>-u</code> flag) between revision 1.14 and 1.19 of <code>backend.c</code>. Due to the <code>-kk</code> flag no keywords are substituted, so differences that only depend on keyword substitution are ignored. </p>
<dl>
<dd> <p> $ cvs diff -kk -u -r 1.14 -r 1.19 backend.c </p>
 </dd>
<dd> <p> Suppose the experimental branch EXPR1 was based on a set of files tagged RELEASE_1_0. To see what has happened on that branch, the following can be used: </p>
 </dd>
<dd> <p> $ cvs diff -r RELEASE_1_0 -r EXPR1 </p>
 </dd>
<dd> <p> A command like this can be used to produce a context diff between two releases: </p>
 </dd>
<dd> <p> $ cvs diff -c -r RELEASE_1_0 -r RELEASE_1_1 &gt; diffs </p>
 </dd>
<dd> <p> If you are maintaining ChangeLogs, a command like the following just before you commit your changes may help you write the ChangeLog entry. All local modifications that have not yet been committed will be printed. </p>
 </dd>
<dd> <p> $ cvs diff -u | less </p>
 </dd>
<dd>  </dd></dl>
<h2>export</h2>
<h3>Export sources from CVS, similar to checkout</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Synopsis: export [-flNnR] [-r rev|-D date] [-k subst] [-d dir] module... </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: repository. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: current directory. </p>
<p> This command is a variant of <code>checkout</code>; use it when you want a copy of the source for module without the <code>cvs</code> administrative directories. For example, you might use <code>export</code> to prepare source for shipment off-site. This command requires that you specify a date or tag (with <code>-D</code> or <code>-r</code>), so that you can count on reproducing the source you ship to others (and thus it always prunes empty directories). </p>
<p> One often would like to use <code>-kv</code> with <code>cvs export</code>. This causes any keywords to be expanded such that an import done at some other site will not lose the keyword revision information. But be aware that doesn&#8217;t handle an export containing binary files correctly. Also be aware that after having used <code>-kv</code>, one can no longer use the <code>ident</code> command (which is part of the <code>rcs</code> suite---see <a href="/docs/linux/man/1-ident/">ident</a>(1)) which looks for keyword strings. If you want to be able to use <code>ident</code> you must not use <code>-kv</code>. </p>
 </dd></dl>
<h2>export options</h2>
<p> These standard options are supported by <code>export</code> (see node `Common options&#8217; in the CVS manual, for a complete description of them): </p>
<dl>
<dd> <p> <code>-D </code><i>date</i> </p>
 </dd>
<dd> <p> Use the most recent revision no later than <i>date</i>. </p>
 </dd>
<dd> <p> <code>-f</code> </p>
 </dd>
<dd> <p> If no matching revision is found, retrieve the most recent revision (instead of ignoring the file). </p>
 </dd>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Local; run only in current working directory. </p>
 </dd>
<dd> <p> <code>-n</code> </p>
 </dd>
<dd> <p> Do not run any checkout program. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> Export directories recursively. This is on by default. </p>
 </dd>
<dd> <p> <code>-r </code><i>tag</i> </p>
 </dd>
<dd> <p> Use revision <i>tag</i>. </p>
<p> In addition, these options (that are common to <code>checkout</code> and <code>export</code>) are also supported: </p>
 </dd>
<dd> <p> <code>-d </code><i>dir</i> </p>
 </dd>
<dd> <p> Create a directory called <i>dir</i> for the working files, instead of using the module name. See `checkout options&#8217; in the CVS manual for complete details on how <code>cvs</code> handles this flag. </p>
 </dd>
<dd> <p> <code>-k </code><i>subst</i> </p>
 </dd>
<dd> <p> Set keyword expansion mode (see node `Substitution modes&#8217; in the CVS manual). </p>
 </dd>
<dd> <p> <code>-N</code> </p>
 </dd>
<dd> <p> Only useful together with <code>-d </code><i>dir</i>. See `checkout options&#8217; in the CVS manual for complete details on how <code>cvs</code> handles this flag. </p>
 </dd></dl>
<h2>history</h2>
<h3>Show status of files and users</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Synopsis: history [-report] [-flags] [-options args] [files...] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: the file <code>$CVSROOT/CVSROOT/history</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: nothing. </p>
<p> <code>cvs</code> can keep a history file that tracks each use of the <code>checkout</code>, <code>commit</code>, <code>rtag</code>, <code>update</code>, and <code>release</code> commands. You can use <code>history</code> to display this information in various formats. </p>
<p> Logging must be enabled by creating the file <code>$CVSROOT/CVSROOT/history</code>. </p>
<p> <code>history uses -f, -l, -n, and -p in ways that conflict with the normal use inside cvs (see node `Common options&#8217; in the CVS manual).</code> </p>
 </dd></dl>
<h2>history options</h2>
<p> Several options (shown above as <code>-report</code>) control what kind of report is generated: </p>
<dl>
<dd> <p> <code>-c</code> </p>
 </dd>
<dd> <p> Report on each time commit was used (i.e., each time the repository was modified). </p>
 </dd>
<dd> <p> <code>-e</code> </p>
 </dd>
<dd> <p> Everything (all record types). Equivalent to specifying <code>-x</code> with all record types. Of course, <code>-e</code> will also include record types which are added in a future version of <code>cvs</code>; if you are writing a script which can only handle certain record types, you&#8217;ll want to specify <code>-x</code>. </p>
 </dd>
<dd> <p> <code>-m </code><i>module</i> </p>
 </dd>
<dd> <p> Report on a particular module. (You can meaningfully use <code>-m</code> more than once on the command line.) </p>
 </dd>
<dd> <p> <code>-o</code> </p>
 </dd>
<dd> <p> Report on checked-out modules. This is the default report type. </p>
 </dd>
<dd> <p> <code>-T</code> </p>
 </dd>
<dd> <p> Report on all tags. </p>
 </dd>
<dd> <p> <code>-x </code><i>type</i> </p>
 </dd>
<dd> <p> Extract a particular set of record types <i>type</i> from the <code>cvs</code> history. The types are indicated by single letters, which you may specify in combination. </p>
<p> Certain commands have a single record type: </p>
 </dd>
<dd> <p> <code>F</code> </p>
 </dd>
<dd> <p> release </p>
 </dd>
<dd> <p> <code>O</code> </p>
 </dd>
<dd> <p> checkout </p>
 </dd>
<dd> <p> <code>E</code> </p>
 </dd>
<dd> <p> export </p>
 </dd>
<dd> <p> <code>T</code> </p>
 </dd>
<dd> <p> rtag </p>
<p> One of five record types may result from an update: </p>
 </dd>
<dd> <p> <code>C</code> </p>
 </dd>
<dd> <p> A merge was necessary but collisions were detected (requiring manual merging). </p>
 </dd>
<dd> <p> <code>G</code> </p>
 </dd>
<dd> <p> A merge was necessary and it succeeded. </p>
 </dd>
<dd> <p> <code>U</code> </p>
 </dd>
<dd> <p> A working file was copied from the repository. </p>
 </dd>
<dd> <p> <code>P</code> </p>
 </dd>
<dd> <p> A working file was patched to match the repository. </p>
 </dd>
<dd> <p> <code>W</code> </p>
 </dd>
<dd> <p> The working copy of a file was deleted during update (because it was gone from the repository). </p>
<p> One of three record types results from commit: </p>
 </dd>
<dd> <p> <code>A</code> </p>
 </dd>
<dd> <p> A file was added for the first time. </p>
 </dd>
<dd> <p> <code>M</code> </p>
 </dd>
<dd> <p> A file was modified. </p>
 </dd>
<dd> <p> <code>R</code> </p>
 </dd>
<dd> <p> A file was removed. </p>
<p> The options shown as <code>-flags</code> constrain or expand the report without requiring option arguments: </p>
 </dd>
<dd> <p> <code>-a</code> </p>
 </dd>
<dd> <p> Show data for all users (the default is to show data only for the user executing <code>history</code>). </p>
 </dd>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Show last modification only. </p>
 </dd>
<dd> <p> <code>-w</code> </p>
 </dd>
<dd> <p> Show only the records for modifications done from the same working directory where <code>history</code> is executing. </p>
<p> The options shown as <code>-options </code><i>args</i> constrain the report based on an argument: </p>
 </dd>
<dd> <p> <code>-b </code><i>str</i> </p>
 </dd>
<dd> <p> Show data back to a record containing the string <i>str</i> in either the module name, the file name, or the repository path. </p>
 </dd>
<dd> <p> <code>-D </code><i>date</i> </p>
 </dd>
<dd> <p> Show data since <i>date</i>. This is slightly different from the normal use of <code>-D </code><i>date</i>, which selects the newest revision older than <i>date</i>. </p>
 </dd>
<dd> <p> <code>-f </code><i>file</i> </p>
 </dd>
<dd> <p> Show data for a particular file (you can specify several <code>-f</code> options on the same command line). This is equivalent to specifying the file on the command line. </p>
 </dd>
<dd> <p> <code>-n </code><i>module</i> </p>
 </dd>
<dd> <p> Show data for a particular module (you can specify several <code>-n</code> options on the same command line). </p>
 </dd>
<dd> <p> <code>-p </code><i>repository</i> </p>
 </dd>
<dd> <p> Show data for a particular source repository (you can specify several <code>-p</code> options on the same command line). </p>
 </dd>
<dd> <p> <code>-r </code><i>rev</i> </p>
 </dd>
<dd> <p> Show records referring to revisions since the revision or tag named <i>rev</i> appears in individual <code>rcs</code> files. Each <code>rcs</code> file is searched for the revision or tag. </p>
 </dd>
<dd> <p> <code>-t </code><i>tag</i> </p>
 </dd>
<dd> <p> Show records since tag <i>tag</i> was last added to the history file. This differs from the <code>-r</code> flag above in that it reads only the history file, not the <code>rcs</code> files, and is much faster. </p>
 </dd>
<dd> <p> <code>-u </code><i>name</i> </p>
 </dd>
<dd> <p> Show records for user <i>name</i>. </p>
 </dd>
<dd> <p> <code>-z </code><i>timezone</i> </p>
 </dd>
<dd> <p> Show times in the selected records using the specified time zone instead of UTC. </p>
 </dd></dl>
<h2>import</h2>
<h3>Import sources into CVS, using vendor branches</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Synopsis: import [-options] repository vendortag releasetag... </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: Repository, source distribution directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: repository. </p>
<p> Use <code>import</code> to incorporate an entire source distribution from an outside source (e.g., a source vendor) into your source repository directory. You can use this command both for initial creation of a repository, and for wholesale updates to the module from the outside source. See `Tracking sources&#8217; in the CVS manual for a discussion on this subject. </p>
<p> The <i>repository</i> argument gives a directory name (or a path to a directory) under the <code>cvs</code> root directory for repositories; if the directory did not exist, import creates it. </p>
<p> When you use import for updates to source that has been modified in your source repository (since a prior import), it will notify you of any files that conflict in the two branches of development; use <code>checkout -j</code> to reconcile the differences, as import instructs you to do. </p>
<p> If <code>cvs</code> decides a file should be ignored (see node `cvsignore&#8217; in the CVS manual), it does not import it and prints <code>I </code> followed by the filename (see node `import output&#8217; in the CVS manual for a complete description of the output). </p>
<p> If the file <code>$CVSROOT/CVSROOT/cvswrappers</code> exists, any file whose names match the specifications in that file will be treated as packages and the appropriate filtering will be performed on the file/directory before being imported. See `Wrappers&#8217; in the CVS manual. </p>
<p> The outside source is saved in a first-level branch, by default 1.1.1. Updates are leaves of this branch; for example, files from the first imported collection of source will be revision 1.1.1.1, then files from the first imported update will be revision 1.1.1.2, and so on. </p>
<p> At least three arguments are required. <i>repository</i> is needed to identify the collection of source. <i>vendortag</i> is a tag for the entire branch (e.g., for 1.1.1). You must also specify at least one <i>releasetag</i> to uniquely identify the files at the leaves created each time you execute <code>import</code>. The <i>releasetag</i> should be new, not previously existing in the repository file, and uniquely identify the imported release, </p>
<p> Note that <code>import</code> does <i>not</i> change the directory in which you invoke it. In particular, it does not set up that directory as a <code>cvs</code> working directory; if you want to work with the sources import them first and then check them out into a different directory (see node `Getting the source&#8217; in the CVS manual). </p>
 </dd></dl>
<h2>import options</h2>
<p> This standard option is supported by <code>import</code> (see node `Common options&#8217; in the CVS manual for a complete description): </p>
<dl>
<dd> <p> <code>-m </code><i>message</i> </p>
 </dd>
<dd> <p> Use <i>message</i> as log information, instead of invoking an editor. </p>
<p> There are the following additional special options. </p>
 </dd>
<dd> <p> <code>-b </code><i>branch</i> </p>
 </dd>
<dd> <p> See `Multiple vendor branches&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-d</code> </p>
 </dd>
<dd> <p> Use each file&#8217;s modification time as the time of import rather than the current time. </p>
 </dd>
<dd> <p> <code>-k </code><i>subst</i> </p>
 </dd>
<dd> <p> Indicate the keyword expansion mode desired. This setting will apply to all files created during the import, but not to any files that previously existed in the repository. See `Substitution modes&#8217; in the CVS manual for a list of valid <code>-k</code> settings. </p>
 </dd>
<dd> <p> <code>-I </code><i>name</i> </p>
 </dd>
<dd> <p> Specify file names that should be ignored during import. You can use this option repeatedly. To avoid ignoring any files at all (even those ignored by default), specify `-I !&#8216;. </p>
<p> <i>name</i> can be a file name pattern of the same type that you can specify in the <code>.cvsignore</code> file. See `cvsignore&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-W </code><i>spec</i> </p>
 </dd>
<dd> <p> Specify file names that should be filtered during import. You can use this option repeatedly. </p>
<p> <i>spec</i> can be a file name pattern of the same type that you can specify in the <code>.cvswrappers</code> file. see node `Wrappers&#8217; in the CVS manual. </p>
 </dd></dl>
<h2>import output</h2>
<p> <code>import</code> keeps you informed of its progress by printing a line for each file, preceded by one character indicating the status of the file: </p>
<dl>
<dd> <p> <code>U </code><i>file</i> </p>
 </dd>
<dd> <p> The file already exists in the repository and has not been locally modified; a new revision has been created (if necessary). </p>
 </dd>
<dd> <p> <code>N </code><i>file</i> </p>
 </dd>
<dd> <p> The file is a new file which has been added to the repository. </p>
 </dd>
<dd> <p> <code>C </code><i>file</i> </p>
 </dd>
<dd> <p> The file already exists in the repository but has been locally modified; you will have to merge the changes. </p>
 </dd>
<dd> <p> <code>I </code><i>file</i> </p>
 </dd>
<dd> <p> The file is being ignored (see node `cvsignore&#8217; in the CVS manual). </p>
 </dd>
<dd> <p> <code>L </code><i>file</i> </p>
 </dd>
<dd> <p> The file is a symbolic link; <code>cvs import</code> ignores symbolic links. People periodically suggest that this behavior should be changed, but if there is a consensus on what it should be changed to, it doesn&#8217;t seem to be apparent. (Various options in the <code>modules</code> file can be used to recreate symbolic links on checkout, update, etc.; see node `modules&#8217; in the CVS manual.) </p>
 </dd></dl>
<h2>import examples</h2>
<p> See `Tracking sources&#8217; in the CVS manual, and `From files&#8217; in the CVS manual. </p>
<h2>log</h2>
<h3>Print out log information for files</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Synopsis: log [options] [files...] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: repository, working directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: nothing. </p>
<p> Display log information for files. <code>log</code> used to call the <code>rcs</code> utility <code>rlog</code>. Although this is no longer true in the current sources, this history determines the format of the output and the options, which are not quite in the style of the other <code>cvs</code> commands. </p>
<p> The output includes the location of the <code>rcs</code> file, the <i>head</i> revision (the latest revision on the trunk), all symbolic names (tags) and some other things. For each revision, the revision number, the author, the number of lines added/deleted and the log message are printed. All times are displayed in Coordinated Universal Time (UTC). (Other parts of <code>cvs</code> print times in the local timezone). </p>
<p> <code>log uses -R in a way that conflicts with the normal use inside cvs (see node `Common options&#8217; in the CVS manual).</code> </p>
 </dd></dl>
<h2>log options</h2>
<p> By default, <code>log</code> prints all information that is available. All other options restrict the output. Note that the revision selection options (<code>-b</code>, <code>-d</code>, <code>-r</code>, <code>-s</code>, and <code>-w</code>) have no effect, other than possibly causing a search for files in Attic directories, when used in conjunction with the options that restrict the output to only <code>log</code> header fields (<code>-h</code>, <code>-R</code>, and <code>-t</code>) unless the <code>-S</code> option is also specified. </p>
<dl>
<dd> <p> <code>-b</code> </p>
 </dd>
<dd> <p> Print information about the revisions on the default branch, normally the highest branch on the trunk. </p>
 </dd>
<dd> <p> <code>-d </code><i>dates</i> </p>
 </dd>
<dd> <p> Print information about revisions with a checkin date/time in the range given by the semicolon-separated list of dates. The date formats accepted are those accepted by the <code>-D</code> option to many other <code>cvs</code> commands (see node `Common options&#8217; in the CVS manual). Dates can be combined into ranges as follows: </p>
 </dd>
<dd> <p> <i>d1</i><code>&lt;</code><i>d2</i> </p>
 </dd>
<dd>  </dd>
<dd> <p> <i>d2</i><code>&gt;</code><i>d1</i> </p>
 </dd>
<dd> <p> Select the revisions that were deposited between <i>d1</i> and <i>d2</i>. </p>
 </dd>
<dd> <p> <code>&lt;</code><i>d</i> </p>
 </dd>
<dd>  </dd>
<dd> <p> <i>d</i><code>&gt;</code> </p>
 </dd>
<dd> <p> Select all revisions dated <i>d</i> or earlier. </p>
 </dd>
<dd> <p> <i>d</i><code>&lt;</code> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>&gt;</code><i>d</i> </p>
 </dd>
<dd> <p> Select all revisions dated <i>d</i> or later. </p>
 </dd>
<dd> <p> <i>d</i> </p>
 </dd>
<dd> <p> Select the single, latest revision dated <i>d</i> or earlier. </p>
<p> The <code>&gt;</code> or <code>&lt;</code> characters may be followed by <code>=</code> to indicate an inclusive range rather than an exclusive one. </p>
<p> Note that the separator is a semicolon (;). </p>
 </dd>
<dd> <p> <code>-h</code> </p>
 </dd>
<dd> <p> Print only the name of the <code>rcs</code> file, name of the file in the working directory, head, default branch, access list, locks, symbolic names, and suffix. </p>
 </dd>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Local; run only in current working directory. (Default is to run recursively). </p>
 </dd>
<dd> <p> <code>-N</code> </p>
 </dd>
<dd> <p> Do not print the list of tags for this file. This option can be very useful when your site uses a lot of tags, so rather than &quot;more&quot;&#8216;ing over 3 pages of tag information, the log information is presented without tags at all. </p>
 </dd>
<dd> <p> <code>-n</code> </p>
 </dd>
<dd> <p> Print the list of tags for this file. This option can be very useful when your <code>.cvsrc</code> file has a <code>log -N</code> entry as a way to get a full list of all of the tags. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> Print only the name of the <code>rcs</code> file. </p>
 </dd>
<dd> <p> <code>-r</code><i>revisions</i> </p>
 </dd>
<dd> <p> Print information about revisions given in the comma-separated list <i>revisions</i> of revisions and ranges. The following table explains the available range formats: </p>
 </dd>
<dd> <p> <i>rev1</i><code>:</code><i>rev2</i> </p>
 </dd>
<dd> <p> Revisions <i>rev1</i> to <i>rev2</i> (which must be on the same branch). </p>
 </dd>
<dd> <p> <i>rev1</i><code>::</code><i>rev2</i> </p>
 </dd>
<dd> <p> The same, but excluding <i>rev1</i>. </p>
 </dd>
<dd> <p> <code>:</code><i>rev</i> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>::</code><i>rev</i> </p>
 </dd>
<dd> <p> Revisions from the beginning of the branch up to and including <i>rev</i>. </p>
 </dd>
<dd> <p> <i>rev</i><code>:</code> </p>
 </dd>
<dd> <p> Revisions starting with <i>rev</i> to the end of the branch containing <i>rev</i>. </p>
 </dd>
<dd> <p> <i>rev</i><code>::</code> </p>
 </dd>
<dd> <p> Revisions starting just after <i>rev</i> to the end of the branch containing <i>rev</i>. </p>
 </dd>
<dd> <p> <i>branch</i> </p>
 </dd>
<dd> <p> An argument that is a branch means all revisions on that branch. </p>
 </dd>
<dd> <p> <i>branch1</i><code>:</code><i>branch2</i> </p>
 </dd>
<dd>  </dd>
<dd> <p> <i>branch1</i><code>::</code><i>branch2</i> </p>
 </dd>
<dd> <p> A range of branches means all revisions on the branches in that range. </p>
 </dd>
<dd> <p> <i>branch</i><code>.</code> </p>
 </dd>
<dd> <p> The latest revision in <i>branch</i>. </p>
<p> A bare <code>-r</code> with no revisions means the latest revision on the default branch, normally the trunk. There can be no space between the <code>-r</code> option and its argument. </p>
 </dd>
<dd> <p> <code>-S</code> </p>
 </dd>
<dd> <p> Suppress the header if no revisions are selected. </p>
 </dd>
<dd> <p> <code>-s </code><i>states</i> </p>
 </dd>
<dd> <p> Print information about revisions whose state attributes match one of the states given in the comma-separated list <i>states</i>. Individual states may be any text string, though <code>cvs</code> commonly only uses two states, <code>Exp</code> and <code>dead</code>. See `admin options&#8217; in the CVS manual for more information. </p>
 </dd>
<dd> <p> <code>-t</code> </p>
 </dd>
<dd> <p> Print the same as <code>-h</code>, plus the descriptive text. </p>
 </dd>
<dd> <p> <code>-w</code><i>logins</i> </p>
 </dd>
<dd> <p> Print information about revisions checked in by users with login names appearing in the comma-separated list <i>logins</i>. If <i>logins</i> is omitted, the user&#8217;s login is assumed. There can be no space between the <code>-w</code> option and its argument. </p>
<p> <code>log</code> prints the intersection of the revisions selected with the options <code>-d</code>, <code>-s</code>, and <code>-w</code>, intersected with the union of the revisions selected by <code>-b</code> and <code>-r</code>. </p>
 </dd></dl>
<h2>log examples</h2>
<p> Contributed examples are gratefully accepted. </p>
<h2>rdiff</h2>
<h3>'patch' format diffs between releases</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> rdiff [-flags] [-V vn] [-r t|-D d [-r t2|-D d2]] modules... </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: repository. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: nothing. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Synonym: patch </p>
<p> Builds a Larry Wall format <a href="/docs/linux/man/1-patch/">patch</a>(1) file between two releases, that can be fed directly into the <code>patch</code> program to bring an old release up-to-date with the new release. (This is one of the few <code>cvs</code> commands that operates directly from the repository, and doesn&#8217;t require a prior checkout.) The diff output is sent to the standard output device. </p>
<p> You can specify (using the standard <code>-r</code> and <code>-D</code> options) any combination of one or two revisions or dates. If only one revision or date is specified, the patch file reflects differences between that revision or date and the current head revisions in the <code>rcs</code> file. </p>
<p> Note that if the software release affected is contained in more than one directory, then it may be necessary to specify the <code>-p</code> option to the <code>patch</code> command when patching the old sources, so that <code>patch</code> is able to find the files that are located in other directories. </p>
 </dd></dl>
<h2>rdiff options</h2>
<p> These standard options are supported by <code>rdiff</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dd> <p> <code>-D </code><i>date</i> </p>
 </dd>
<dd> <p> Use the most recent revision no later than <i>date</i>. </p>
 </dd>
<dd> <p> <code>-f</code> </p>
 </dd>
<dd> <p> If no matching revision is found, retrieve the most recent revision (instead of ignoring the file). </p>
 </dd>
<dd> <p> <code>-k </code><i>kflag</i> </p>
 </dd>
<dd> <p> Process keywords according to <i>kflag</i>. See `Keyword substitution&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Local; don&#8217;t descend subdirectories. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> Examine directories recursively. This option is on by default. </p>
 </dd>
<dd> <p> <code>-r </code><i>tag</i> </p>
 </dd>
<dd> <p> Use revision <i>tag</i>. </p>
<p> In addition to the above, these options are available: </p>
 </dd>
<dd> <p> <code>-c</code> </p>
 </dd>
<dd> <p> Use the context diff format. This is the default format. </p>
 </dd>
<dd> <p> <code>-s</code> </p>
 </dd>
<dd> <p> Create a summary change report instead of a patch. The summary includes information about files that were changed or added between the releases. It is sent to the standard output device. This is useful for finding out, for example, which files have changed between two dates or revisions. </p>
 </dd>
<dd> <p> <code>-t</code> </p>
 </dd>
<dd> <p> A diff of the top two revisions is sent to the standard output device. This is most useful for seeing what the last change to a file was. </p>
 </dd>
<dd> <p> <code>-u</code> </p>
 </dd>
<dd> <p> Use the unidiff format for the context diffs. Remember that old versions of the <code>patch</code> program can&#8217;t handle the unidiff format, so if you plan to post this patch to the net you should probably not use <code>-u</code>. </p>
 </dd>
<dd> <p> <code>-V </code><i>vn</i> </p>
 </dd>
<dd> <p> Expand keywords according to the rules current in <code>rcs</code> version <i>vn</i> (the expansion format changed with <code>rcs</code> version 5). Note that this option is no longer accepted. <code>cvs</code> will always expand keywords the way that <code>rcs</code> version 5 does. </p>
 </dd></dl>
<h2>rdiff examples</h2>
<p> Suppose you receive mail from foo [at] example.net asking for an update from release 1.2 to 1.4 of the tc compiler. You have no such patches on hand, but with <code>cvs</code> that can easily be fixed with a command such as this: </p>
<dl>
<dd> <p> $ cvs rdiff -c -r FOO1_2 -r FOO1_4 tc | \ </p>
 </dd>
<dd> <p> &gt; Mail -s &#8216;The patches you asked for&#8217; foo [at] example.net </p>
 </dd>
<dd> <p> Suppose you have made release 1.3, and forked a branch called <code>R_1_3fix</code> for bug fixes. <code>R_1_3_1</code> corresponds to release 1.3.1, which was made some time ago. Now, you want to see how much development has been done on the branch. This command can be used: </p>
 </dd>
<dd> <p> $ cvs patch -s -r R_1_3_1 -r R_1_3fix module-name </p>
 </dd>
<dd> <p> cvs rdiff: Diffing module-name </p>
 </dd>
<dd> <p> File ChangeLog,v changed from revision 1.52.2.5 to 1.52.2.6 </p>
 </dd>
<dd> <p> File foo.c,v changed from revision 1.52.2.3 to 1.52.2.4 </p>
 </dd>
<dd> <p> File bar.h,v changed from revision 1.29.2.1 to 1.2 </p>
 </dd>
<dd>  </dd></dl>
<h2>release</h2>
<h3>Indicate that a Module is no longer in use</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> release [-d] directories... </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: Working directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: Working directory, history log. </p>
<p> This command is meant to safely cancel the effect of <code>cvs checkout</code>. Since <code>cvs</code> doesn&#8217;t lock files, it isn&#8217;t strictly necessary to use this command. You can always simply delete your working directory, if you like; but you risk losing changes you may have forgotten, and you leave no trace in the <code>cvs</code> history file (see node `history file&#8217; in the CVS manual) that you&#8217;ve abandoned your checkout. </p>
<p> Use <code>cvs release</code> to avoid these problems. This command checks that no uncommitted changes are present; that you are executing it from immediately above a <code>cvs</code> working directory; and that the repository recorded for your files is the same as the repository defined in the module database. </p>
<p> If all these conditions are true, <code>cvs release</code> leaves a record of its execution (attesting to your intentionally abandoning your checkout) in the <code>cvs</code> history log. </p>
 </dd></dl>
<h2>release options</h2>
<p> The <code>release</code> command supports one command option: </p>
<dl>
<dd> <p> <code>-d</code> </p>
 </dd>
<dd> <p> Delete your working copy of the file if the release succeeds. If this flag is not given your files will remain in your working directory. </p>
<p> <code>WARNING: The release command deletes all directories and files recursively. This has the very serious side-effect that any directory created inside checked-out sources, and not added to the repository (using the add command; see node `Adding files&#8217; in the CVS manual) will be silently deleted---even if it is non-empty!</code> </p>
 </dd></dl>
<h2>release output</h2>
<p> Before <code>release</code> releases your sources it will print a one-line message for any file that is not up-to-date. </p>
<dl>
<dd> <p> <code>U </code><i>file</i> </p>
 </dd>
<dd>  </dd>
<dd> <p> <code>P </code><i>file</i> </p>
 </dd>
<dd> <p> There exists a newer revision of this file in the repository, and you have not modified your local copy of the file (<code>U</code> and <code>P</code> mean the same thing). </p>
 </dd>
<dd> <p> <code>A </code><i>file</i> </p>
 </dd>
<dd> <p> The file has been added to your private copy of the sources, but has not yet been committed to the repository. If you delete your copy of the sources this file will be lost. </p>
 </dd>
<dd> <p> <code>R </code><i>file</i> </p>
 </dd>
<dd> <p> The file has been removed from your private copy of the sources, but has not yet been removed from the repository, since you have not yet committed the removal. See `commit&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>M </code><i>file</i> </p>
 </dd>
<dd> <p> The file is modified in your working directory. There might also be a newer revision inside the repository. </p>
 </dd>
<dd> <p> <code>? </code><i>file</i> </p>
 </dd>
<dd> <p> <i>file</i> is in your working directory, but does not correspond to anything in the source repository, and is not in the list of files for <code>cvs</code> to ignore (see the description of the <code>-I</code> option, and see node `cvsignore&#8217; in the CVS manual). If you remove your working sources, this file will be lost. </p>
 </dd></dl>
<h2>release examples</h2>
<p> Release the <code>tc</code> directory, and delete your local working copy of the files. </p>
<dl>
<dd> <p> $ cd .. # You must stand immediately above the </p>
 </dd>
<dd> <p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sources when you issue&nbsp;<wbr><code>cvs release</code>. </p>
 </dd>
<dd> <p> $ cvs release -d tc </p>
 </dd>
<dd> <p> You have [0] altered files in this repository. </p>
 </dd>
<dd> <p> Are you sure you want to release (and delete) directory `tc&#8217;: y </p>
 </dd>
<dd> <p> $ </p>
 </dd>
<dd>  </dd></dl>
<h2>remove</h2>
<h3>Remove files from active use</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Synopsis: remove [-flR] [files...] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: repository, working directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: working directory. </p>
<p> The <code>remove</code> command is used to remove unwanted files from active use. The user normally deletes the files from the working directory prior to invocation of the <code>remove</code> command. Only the working directory is updated. Changes to the repository are not made until the <code>commit</code> command is run. </p>
<p> The <code>remove</code> command does not delete files from from the repository. <code>cvs</code> keeps all historical data in the repository so that it is possible to reconstruct previous states of the projects under revision control. </p>
<p> To undo <code>cvs</code> <code>remove</code> or to resurrect files that were previously removed, see node `add&#8217; in the CVS manual. </p>
 </dd></dl>
<h2>remove options</h2>
<p> These standard options are supported by <code>remove</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Local; run only in current working directory. See `Recursive behavior&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> Process directories recursively. See `Recursive behavior&#8217; in the CVS manual. </p>
<p> In addition, these options are also supported: </p>
 </dd>
<dd> <p> <code>-f</code> </p>
 </dd>
<dd> <p> Note that this is not the standard behavior of the <code>-f</code> option as defined in `Common options&#8217; in the CVS manual. </p>
<p> Delete files before removing them. </p>
<p> Entire directory hierarchies are easily removed using <code>-f</code>, but take note that it is not as easy to resurrect directory hierarchies as it is to remove them. </p>
 </dd></dl>
<h2>remove examples</h2>
<h3>Removing a file</h3>
<dl>
<dd> <p> $ cvs remove remove.me </p>
 </dd>
<dd> <p> cvs remove: file `remove.me&#8217; still in working directory </p>
 </dd>
<dd> <p> cvs remove: 1 file exists; remove it first </p>
 </dd>
<dd> <p> $ rm -f remove.me </p>
 </dd>
<dd> <p> $ cvs remove remove.me </p>
 </dd>
<dd> <p> cvs remove: scheduling `remove.me&#8217; for removal </p>
 </dd>
<dd> <p> cvs remove: use &#8216;cvs commit&#8217; to remove this file permanently </p>
 </dd>
<dd> <p> $ ls remove.it </p>
 </dd>
<dd> <p> remove.it </p>
 </dd>
<dd> <p> $ cvs remove -f remove.it </p>
 </dd>
<dd> <p> cvs remove: scheduling `remove.it&#8217; for removal </p>
 </dd>
<dd> <p> cvs remove: use &#8216;cvs commit&#8217; to remove this file permanently </p>
 </dd>
<dd>  </dd></dl>
<h3>Removing entire directories</h3>
<dl>
<dd> <p> $ tree -d a </p>
 </dd>
<dd> <p> a </p>
 </dd>
<dd> <p> |-- CVS </p>
 </dd>
<dd> <p> `-- b </p>
 </dd>
<dd> <p> <br/>
&nbsp;<wbr>`-- CVS </p>
 </dd>
<dd> <p> 3 directories </p>
 </dd>
<dd> <p> $ cvs remove -f a </p>
 </dd>
<dd> <p> cvs remove: Removing a </p>
 </dd>
<dd> <p> cvs remove: Removing a/b </p>
 </dd>
<dd> <p> cvs remove: scheduling `a/b/c&#8217; for removal </p>
 </dd>
<dd> <p> cvs remove: use &#8216;cvs commit&#8217; to remove this file permanently </p>
 </dd>
<dd>  </dd></dl>
<h2>update</h2>
<h3>Bring work tree in sync with repository</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> update [-ACdflPpR] [-I name] [-j rev [-j rev]] [-k kflag] [-r tag|-D date] [-W spec] files... </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Requires: repository, working directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes: working directory. </p>
<p> After you&#8217;ve run checkout to create your private copy of source from the common repository, other developers will continue changing the central source. From time to time, when it is convenient in your development process, you can use the <code>update</code> command from within your working directory to reconcile your work with any revisions applied to the source repository since your last checkout or update. </p>
 </dd></dl>
<h2>update options</h2>
<p> These standard options are available with <code>update</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dd> <p> <code>-D date</code> </p>
 </dd>
<dd> <p> Use the most recent revision no later than <i>date</i>. This option is sticky, and implies <code>-P</code>. See `Sticky tags&#8217; in the CVS manual for more information on sticky tags/dates. </p>
 </dd>
<dd> <p> <code>-f</code> </p>
 </dd>
<dd> <p> Only useful with the <code>-D </code><i>date</i> or <code>-r </code><i>tag</i> flags. If no matching revision is found, retrieve the most recent revision (instead of ignoring the file). </p>
 </dd>
<dd> <p> <code>-k </code><i>kflag</i> </p>
 </dd>
<dd> <p> Process keywords according to <i>kflag</i>. See `Keyword substitution&#8217; in the CVS manual. This option is sticky; future updates of this file in this working directory will use the same <i>kflag</i>. The <code>status</code> command can be viewed to see the sticky options. See `Invoking CVS&#8217; in the CVS manual for more information on the <code>status</code> command. </p>
 </dd>
<dd> <p> <code>-l</code> </p>
 </dd>
<dd> <p> Local; run only in current working directory. See `Recursive behavior&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-P</code> </p>
 </dd>
<dd> <p> Prune empty directories. See `Moving directories&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-p</code> </p>
 </dd>
<dd> <p> Pipe files to the standard output. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> Update directories recursively (default). See `Recursive behavior&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-r rev</code> </p>
 </dd>
<dd> <p> Retrieve revision/tag <i>rev</i>. This option is sticky, and implies <code>-P</code>. See `Sticky tags&#8217; in the CVS manual, for more information on sticky tags/dates. </p>
<p> These special options are also available with <code>update</code>. </p>
 </dd>
<dd> <p> <code>-A</code> </p>
 </dd>
<dd> <p> Reset any sticky tags, dates, or <code>-k</code> options. Does not reset sticky <code>-k</code> options on modified files. See `Sticky tags&#8217; in the CVS manual for more information on sticky tags/dates. </p>
 </dd>
<dd> <p> <code>-C</code> </p>
 </dd>
<dd> <p> Overwrite locally modified files with clean copies from the repository (the modified file is saved in <code>.#</code><i>file</i><code>.</code><i>revision</i>, however). </p>
 </dd>
<dd> <p> <code>-d</code> </p>
 </dd>
<dd> <p> Create any directories that exist in the repository if they&#8217;re missing from the working directory. Normally, <code>update</code> acts only on directories and files that were already enrolled in your working directory. </p>
<p> This is useful for updating directories that were created in the repository since the initial checkout; but it has an unfortunate side effect. If you deliberately avoided certain directories in the repository when you created your working directory (either through use of a module name or by listing explicitly the files and directories you wanted on the command line), then updating with <code>-d</code> will create those directories, which may not be what you want. </p>
 </dd>
<dd> <p> <code>-I </code><i>name</i> </p>
 </dd>
<dd> <p> Ignore files whose names match <i>name</i> (in your working directory) during the update. You can specify <code>-I</code> more than once on the command line to specify several files to ignore. Use <code>-I !</code> to avoid ignoring any files at all. See `cvsignore&#8217; in the CVS manual for other ways to make <code>cvs</code> ignore some files. </p>
 </dd>
<dd> <p> <code>-W</code><i>spec</i> </p>
 </dd>
<dd> <p> Specify file names that should be filtered during update. You can use this option repeatedly. </p>
<p> <i>spec</i> can be a file name pattern of the same type that you can specify in the <code>.cvswrappers</code> file. See `Wrappers&#8217; in the CVS manual. </p>
 </dd>
<dd> <p> <code>-j</code><i>revision</i> </p>
 </dd>
<dd> <p> With two <code>-j</code> options, merge changes from the revision specified with the first <code>-j</code> option to the revision specified with the second <code>j</code> option, into the working directory. </p>
<p> With one <code>-j</code> option, merge changes from the ancestor revision to the revision specified with the <code>-j</code> option, into the working directory. The ancestor revision is the common ancestor of the revision which the working directory is based on, and the revision specified in the <code>-j</code> option. </p>
<p> Note that using a single <code>-j </code><i>tagname</i> option rather than <code>-j </code><i>branchname</i> to merge changes from a branch will often not remove files which were removed on the branch. See `Merging adds and removals&#8217; in the CVS manual for more information. </p>
<p> In addition, each <code>-j</code> option can contain an optional date specification which, when used with branches, can limit the chosen revision to one within a specific date. An optional date is specified by adding a colon (:) to the tag: <code>-j</code><i>Symbolic_Tag</i><code>:</code><i>Date_Specifier</i>. </p>
<p> See `Branching and merging&#8217; in the CVS manual. </p>
 </dd></dl>
<h2>update output</h2>
<p> <code>update</code> and <code>checkout</code> keep you informed of their progress by printing a line for each file, preceded by one character indicating the status of the file: </p>
<dl>
<dd> <p> <code>U </code><i>file</i> </p>
 </dd>
<dd> <p> The file was brought up to date with respect to the repository. This is done for any file that exists in the repository but not in your working directory, and for files that you haven&#8217;t changed but are not the most recent versions available in the repository. </p>
 </dd>
<dd> <p> <code>P </code><i>file</i> </p>
 </dd>
<dd> <p> Like <code>U</code>, but the <code>cvs</code> server sends a patch instead of an entire file. This accomplishes the same thing as <code>U</code> using less bandwidth. </p>
 </dd>
<dd> <p> <code>A </code><i>file</i> </p>
 </dd>
<dd> <p> The file has been added to your private copy of the sources, and will be added to the source repository when you run <code>commit</code> on the file. This is a reminder to you that the file needs to be committed. </p>
 </dd>
<dd> <p> <code>R </code><i>file</i> </p>
 </dd>
<dd> <p> The file has been removed from your private copy of the sources, and will be removed from the source repository when you run <code>commit</code> on the file. This is a reminder to you that the file needs to be committed. </p>
 </dd>
<dd> <p> <code>M </code><i>file</i> </p>
 </dd>
<dd> <p> The file is modified in your working directory. </p>
<p> <code>M</code> can indicate one of two states for a file you&#8217;re working on: either there were no modifications to the same file in the repository, so that your file remains as you last saw it; or there were modifications in the repository as well as in your copy, but they were merged successfully, without conflict, in your working directory. </p>
<p> <code>cvs</code> will print some messages if it merges your work, and a backup copy of your working file (as it looked before you ran <code>update</code>) will be made. The exact name of that file is printed while <code>update</code> runs. </p>
 </dd>
<dd> <p> <code>C </code><i>file</i> </p>
 </dd>
<dd> <p> A conflict was detected while trying to merge your changes to <i>file</i> with changes from the source repository. <i>file</i> (the copy in your working directory) is now the result of attempting to merge the two revisions; an unmodified copy of your file is also in your working directory, with the name <code>.#</code><i>file</i><code>.</code><i>revision</i> where <i>revision</i> is the revision that your modified file started from. Resolve the conflict as described in `Conflicts example&#8217; in the CVS manual. (Note that some systems automatically purge files that begin with <code>.#</code> if they have not been accessed for a few days. If you intend to keep a copy of your original file, it is a very good idea to rename it.) Under <code>vms</code>, the file name starts with <code>__</code> rather than <code>.#</code>. </p>
 </dd>
<dd> <p> <code>? </code><i>file</i> </p>
 </dd>
<dd> <p> <i>file</i> is in your working directory, but does not correspond to anything in the source repository, and is not in the list of files for <code>cvs</code> to ignore (see the description of the <code>-I</code> option, and see node `cvsignore&#8217; in the CVS manual). </p>
 </dd></dl>
<h2>AUTHORS</h2>
<dl>
<dt>Dick Grune</dt>
<dd> <p> Original author of the <code>cvs</code> shell script version posted to <code>comp.sources.unix</code> in the volume6 release of December, 1986. Credited with much of the <code>cvs</code> conflict resolution algorithms. </p>
 </dd>
<dt>Brian Berliner</dt>
<dd> <p> Coder and designer of the <code>cvs</code> program itself in April, 1989, based on the original work done by Dick. </p>
 </dd>
<dt>Jeff Polk</dt>
<dd> <p> Helped Brian with the design of the <code>cvs</code> module and vendor branch support and author of the <code>checkin</code>(<code>1</code>) shell script (the ancestor of <code>cvs import</code>). </p>
 </dd>
<dt>Larry Jones, Derek R. Price, and Mark D. Baushke</dt>
<dd> <p> Have helped maintain <code>cvs</code> for many years. </p>
 </dd>
<dt>And many others too numerous to mention here.</dt>
<dd>  </dd></dl>
<h2>SEE ALSO</h2>
<p> The most comprehensive manual for CVS is Version Management with CVS by Per Cederqvist et al. Depending on your system, you may be able to get it with the <code>info CVS</code> command or it may be available as cvs.pdf (Portable Document Format), cvs.ps (PostScript), cvs.texinfo (Texinfo source), or cvs.html. </p>
<p> For CVS updates, more information on documentation, software related to CVS, development of CVS, and more, see: </p>
<dl>
<dd> <p> <code><a rel="nofollow" href="http://cvs.nongnu.org">http://cvs.nongnu.org</a></code> </p>
<p> <code>ci</code>(<code>1</code>), <code>co</code>(<code>1</code>), <code>cvs</code>(<code>5</code>), <code>cvsbug</code>(<code>8</code>), <code>diff</code>(<code>1</code>), <code>grep</code>(<code>1</code>), <code>patch</code>(<code>1</code>), <code>rcs</code>(<code>1</code>), <code>rcsdiff</code>(<code>1</code>), <code>rcsmerge</code>(<code>1</code>), <code>rlog</code>(<code>1</code>). </p>
 </dd></dl>
