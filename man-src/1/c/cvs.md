---
title: "cvs(1)"
name: "cvs"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cvs/"
description: "cvs – Concurrent Versions System"
---

<h2 class="name">NAME</h2>
<p> cvs &#8211; Concurrent Versions System </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>cvs</code> [ <i>cvs_options</i> ]</p>
<dd> <i>cvs_command</i> [ <i>command_options</i> ] [ <i>command_args</i> ]</dl>
<h2>NOTE</h2>
<p> This manpage is a summary of some of the features of <code>cvs</code>. It is auto-generated from an appendix of the CVS manual. For more in-depth documentation, please consult the Cederqvist manual (via the <code>info CVS</code> command or otherwise, as described in the SEE ALSO section of this manpage). Cross-references in this man page refer to nodes in the same.</p>
<h2>CVS commands</h2>
<h3>Guide to CVS commands</h3>
<p> This appendix describes the overall structure of <code>cvs</code> commands, and describes some commands in detail (others are described elsewhere; for a quick reference to <code>cvs</code> commands, see node `Invoking CVS&#8217; in the CVS manual). </p>
<h2>Structure</h2>
<h3>Overall structure of CVS commands</h3>
<p> The overall format of all <code>cvs</code> commands is: </p>
<dl>
<dt>
<dd> cvs [ cvs_options ] cvs_command [ command_options ] [ command_args ] </p>
<dt>
<dd>
<dt>
<dd> <code>cvs</code></p>
<dt>
<dd> The name of the <code>cvs</code> program. </p>
<dt>
<dd> <code>cvs_options</code></p>
<dt>
<dd> Some options that affect all sub-commands of <code>cvs</code>. These are described below. </p>
<dt>
<dd> <code>cvs_command</code></p>
<dt>
<dd> One of several different sub-commands. Some of the commands have aliases that can be used instead; those aliases are noted in the reference manual for that command. There are only two situations where you may omit <code>cvs_command</code>: <code>cvs -H</code> elicits a list of available commands, and <code>cvs -v</code> displays version information on <code>cvs</code> itself. </p>
<dt>
<dd> <code>command_options</code></p>
<dt>
<dd> Options that are specific for the command. </p>
<dt>
<dd> <code>command_args</code></p>
<dt>
<dd> Arguments to the commands. </p>
<p> There is unfortunately some confusion between <code>cvs_options</code> and <code>command_options</code>. When given as a <code>cvs_option</code>, some options only affect some of the commands. When given as a <code>command_option</code> it may have a different meaning, and be accepted by more commands. In other words, do not take the above categorization too seriously. Look at the documentation instead. </p>
</dl>
<h2>Exit status</h2>
<h3>CVS&#8217;s exit status</h3>
<p> <code>cvs</code> can indicate to the calling environment whether it succeeded or failed by setting its <i>exit status</i>. The exact way of testing the exit status will vary from one operating system to another. For example in a unix shell script the <code>$?</code> variable will be 0 if the last command returned a successful exit status, or greater than 0 if the exit status indicated failure. </p>
<p> If <code>cvs</code> is successful, it returns a successful status; if there is an error, it prints an error message and returns a failure status. The one exception to this is the <code>cvs diff</code> command. It will return a successful status if it found no differences, or a failure status if there were differences or if there was an error. Because this behavior provides no good way to detect errors, in the future it is possible that <code>cvs diff</code> will be changed to behave like the other <code>cvs</code> commands. </p>
<h2>~/.cvsrc</h2>
<h3>Default options and the ~/.cvsrc file</h3>
<p> There are some <code>command_options</code> that are used so often that you might have set up an alias or some other means to make sure you always specify that option. One example (the one that drove the implementation of the <code>.cvsrc</code> support, actually) is that many people find the default output of the <code>diff</code> command to be very hard to read, and that either context diffs or unidiffs are much easier to understand. </p>
<p> The <code>~/.cvsrc</code> file is a way that you can add default options to <code>cvs_commands</code> within cvs, instead of relying on aliases or other shell scripts. </p>
<p> The format of the <code>~/.cvsrc</code> file is simple. The file is searched for a line that begins with the same name as the <code>cvs_command</code> being executed. If a match is found, then the remainder of the line is split up (at whitespace characters) into separate options and added to the command arguments <i>before</i> any options from the command line. </p>
<p> If a command has two names (e.g., <code>checkout</code> and <code>co</code>), the official name, not necessarily the one used on the command line, will be used to match against the file. So if this is the contents of the user&#8217;s <code>~/.cvsrc</code> file: </p>
<dl>
<dt>
<dd> log -N</p>
<dt>
<dd> diff -uN</p>
<dt>
<dd> rdiff -u</p>
<dt>
<dd> update -Pd</p>
<dt>
<dd> checkout -P</p>
<dt>
<dd> release -d </p>
<dt>
<dd>
<p> the command <code>cvs checkout foo</code> would have the <code>-P</code> option added to the arguments, as well as <code>cvs co foo</code>. </p>
<p> With the example file above, the output from <code>cvs diff foobar</code> will be in unidiff format. <code>cvs diff -c foobar</code> will provide context diffs, as usual. Getting &quot;old&quot; format diffs would be slightly more complicated, because <code>diff</code> doesn&#8217;t have an option to specify use of the &quot;old&quot; format, so you would need <code>cvs -f diff foobar</code>. </p>
<p> In place of the command name you can use <code>cvs</code> to specify global options (see node `Global options&#8217; in the CVS manual). For example the following line in <code>.cvsrc</code> </p>
<dt>
<dd> cvs -z6 </p>
<dt>
<dd>
<p> causes <code>cvs</code> to use compression level 6. </p>
</dl>
<h2>Global options</h2>
<p> The available <code>cvs_options</code> (that are given to the left of <code>cvs_command</code>) are: </p>
<dl>
<dt>
<dd> <code>&#8211;allow-root=</code><i>rootdir</i></p>
<dt>
<dd> Specify legal <code>cvsroot</code> directory. See `Password authentication server&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-a</code></p>
<dt>
<dd> Authenticate all communication between the client and the server. Only has an effect on the <code>cvs</code> client. As of this writing, this is only implemented when using a GSSAPI connection (see node `GSSAPI authenticated&#8217; in the CVS manual). Authentication prevents certain sorts of attacks involving hijacking the active <code>tcp</code> connection. Enabling authentication does not enable encryption. </p>
<dt>
<dd> <code>-b </code><i>bindir</i></p>
<dt>
<dd> In <code>cvs</code> 1.9.18 and older, this specified that <code>rcs</code> programs are in the <i>bindir</i> directory. Current versions of <code>cvs</code> do not run <code>rcs</code> programs; for compatibility this option is accepted, but it does nothing. </p>
<dt>
<dd> <code>-T </code><i>tempdir</i></p>
<dt>
<dd> Use <i>tempdir</i> as the directory where temporary files are located. Overrides the setting of the <code>$TMPDIR</code> environment variable and any precompiled directory. This parameter should be specified as an absolute pathname. (When running client/server, <code>-T</code> affects only the local process; specifying <code>-T</code> for the client has no effect on the server and vice versa.) </p>
<dt>
<dd> <code>-d </code><i>cvs_root_directory</i></p>
<dt>
<dd> Use <i>cvs_root_directory</i> as the root directory pathname of the repository. Overrides the setting of the <code>$CVSROOT</code> environment variable. See `Repository&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-e </code><i>editor</i></p>
<dt>
<dd> Use <i>editor</i> to enter revision log information. Overrides the setting of the <code>$CVSEDITOR</code> and <code>$EDITOR</code> environment variables. For more information, see `Committing your changes&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-f</code></p>
<dt>
<dd> Do not read the <code>~/.cvsrc</code> file. This option is most often used because of the non-orthogonality of the <code>cvs</code> option set. For example, the <code>cvs log</code> option <code>-N</code> (turn off display of tag names) does not have a corresponding option to turn the display on. So if you have <code>-N</code> in the <code>~/.cvsrc</code> entry for <code>log</code>, you may need to use <code>-f</code> to show the tag names. </p>
<dt>
<dd> <code>-H</code></p>
<dt>
<dd>
<dt>
<dd> <code>&#8211;help</code></p>
<dt>
<dd> Display usage information about the specified <code>cvs_command</code> (but do not actually execute the command). If you don&#8217;t specify a command name, <code>cvs -H</code> displays overall help for <code>cvs</code>, including a list of other help options. </p>
<dt>
<dd> <code>-n</code></p>
<dt>
<dd> Do not change any files. Attempt to execute the <code>cvs_command</code>, but only to issue reports; do not remove, update, or merge any existing files, or create any new files. </p>
<p> Note that <code>cvs</code> will not necessarily produce exactly the same output as without <code>-n</code>. In some cases the output will be the same, but in other cases <code>cvs</code> will skip some of the processing that would have been required to produce the exact same output. </p>
<dt>
<dd> <code>-Q</code></p>
<dt>
<dd> Cause the command to be really quiet; the command will only generate output for serious problems. </p>
<dt>
<dd> <code>-q</code></p>
<dt>
<dd> Cause the command to be somewhat quiet; informational messages, such as reports of recursion through subdirectories, are suppressed. </p>
<dt>
<dd> <code>-r</code></p>
<dt>
<dd> Make new working files read-only. Same effect as if the <code>$CVSREAD</code> environment variable is set (see node `Environment variables&#8217; in the CVS manual). The default is to make working files writable, unless watches are on (see node `Watches&#8217; in the CVS manual). </p>
<dt>
<dd> <code>-s </code><i>variable</i><code>=</code><i>value</i></p>
<dt>
<dd> Set a user variable (see node `Variables&#8217; in the CVS manual). </p>
<dt>
<dd> <code>-t</code></p>
<dt>
<dd> Trace program execution; display messages showing the steps of <code>cvs</code> activity. Particularly useful with <code>-n</code> to explore the potential impact of an unfamiliar command. </p>
<dt>
<dd> <code>-v</code></p>
<dt>
<dd>
<dt>
<dd> <code>&#8211;version</code></p>
<dt>
<dd> Display version and copyright information for <code>cvs</code>. </p>
<dt>
<dd> <code>-w</code></p>
<dt>
<dd> Make new working files read-write. Overrides the setting of the <code>$CVSREAD</code> environment variable. Files are created read-write by default, unless <code>$CVSREAD</code> is set or <code>-r</code> is given. </p>
<dt>
<dd> <code>-x</code></p>
<dt>
<dd> Encrypt all communication between the client and the server. Only has an effect on the <code>cvs</code> client. As of this writing, this is only implemented when using a GSSAPI connection (see node `GSSAPI authenticated&#8217; in the CVS manual) or a Kerberos connection (see node `Kerberos authenticated&#8217; in the CVS manual). Enabling encryption implies that message traffic is also authenticated. Encryption support is not available by default; it must be enabled using a special configure option, <code>&#8211;enable-encryption</code>, when you build <code>cvs</code>. </p>
<dt>
<dd> <code>-z </code><i>gzip-level</i></p>
<dt>
<dd> Set the compression level. Valid levels are 1 (high speed, low compression) to 9 (low speed, high compression), or 0 to disable compression (the default). Only has an effect on the <code>cvs</code> client. </p>
</dl>
<h2>Common options</h2>
<h3>Common command options</h3>
<p> This section describes the <code>command_options</code> that are available across several <code>cvs</code> commands. These options are always given to the right of <code>cvs_command</code>. Not all commands support all of these options; each option is only supported for commands where it makes sense. However, when a command has one of these options you can almost always count on the same behavior of the option as in other commands. (Other command options, which are listed with the individual commands, may have different behavior from one <code>cvs</code> command to the other). </p>
<p> <code>The history command is an exception; it supports many options that conflict even with these standard options.</code> </p>
<dl>
<dt>
<dd> <code>-D </code><i>date_spec</i></p>
<dt>
<dd> Use the most recent revision no later than <i>date_spec</i>. <i>date_spec</i> is a single argument, a date description specifying a date in the past. </p>
<p> The specification is <i>sticky</i> when you use it to make a private copy of a source file; that is, when you get a working file using <code>-D</code>, <code>cvs</code> records the date you specified, so that further updates in the same directory will use the same date (for more information on sticky tags/dates, see node `Sticky tags&#8217; in the CVS manual). </p>
<p> <code>-D</code> is available with the <code>annotate</code>, <code>checkout</code>, <code>diff</code>, <code>export</code>, <code>history</code>, <code>rdiff</code>, <code>rtag</code>, and <code>update</code> commands. (The <code>history</code> command uses this option in a slightly different way; see node `history options&#8217; in the CVS manual). </p>
<p> A wide variety of date formats are supported by <code>cvs</code>. The most standard ones are ISO8601 (from the International Standards Organization) and the Internet e-mail standard (specified in RFC822 as amended by RFC1123). </p>
<p> ISO8601 dates have many variants but a few examples are: </p>
<dt>
<dd> 1972-09-24</p>
<dt>
<dd> 1972-09-24 20:05 </p>
<dt>
<dd>
<p> There are a lot more ISO8601 date formats, and <code>cvs</code> accepts many of them, but you probably don&#8217;t want to hear the <i>whole</i> long story :-). </p>
<p> In addition to the dates allowed in Internet e-mail itself, <code>cvs</code> also allows some of the fields to be omitted. For example: </p>
<dt>
<dd> 24 Sep 1972 20:05</p>
<dt>
<dd> 24 Sep </p>
<dt>
<dd>
<p> The date is interpreted as being in the local timezone, unless a specific timezone is specified. </p>
<p> These two date formats are preferred. However, <code>cvs</code> currently accepts a wide variety of other date formats. They are intentionally not documented here in any detail, and future versions of <code>cvs</code> might not accept all of them. </p>
<p> One such format is <i>month</i><code>/</code><i>day</i><code>/</code><i>year</i>. This may confuse people who are accustomed to having the month and day in the other order; <code>1/4/96</code> is January 4, not April 1. </p>
<p> Remember to quote the argument to the <code>-D</code> flag so that your shell doesn&#8217;t interpret spaces as argument separators. A command using the <code>-D</code> flag can look like this: </p>
<dt>
<dd> $ cvs diff -D &quot;1 hour ago&quot; cvs.texinfo </p>
<dt>
<dd>
<dt>
<dd> <code>-f</code></p>
<dt>
<dd> When you specify a particular date or tag to <code>cvs</code> commands, they normally ignore files that do not contain the tag (or did not exist prior to the date) that you specified. Use the <code>-f</code> option if you want files retrieved even when there is no match for the tag or date. (The most recent revision of the file will be used). </p>
<p> Note that even with <code>-f</code>, a tag that you specify must exist (that is, in some file, not necessary in every file). This is so that <code>cvs</code> will continue to give an error if you mistype a tag name. </p>
<p> <code>-f</code> is available with these commands: <code>annotate</code>, <code>checkout</code>, <code>export</code>, <code>rdiff</code>, <code>rtag</code>, and <code>update</code>. </p>
<p> <code>WARNING: The commit and remove commands also have a -f option, but it has a different behavior for those commands. See `commit options&#8217; in the CVS manual, and `Removing files&#8217; in the CVS manual.</code> </p>
<dt>
<dd> <code>-k </code><i>kflag</i></p>
<dt>
<dd> Alter the default processing of keywords. See `Keyword substitution&#8217; in the CVS manual, for the meaning of <i>kflag</i>. Your <i>kflag</i> specification is <i>sticky</i> when you use it to create a private copy of a source file; that is, when you use this option with the <code>checkout</code> or <code>update</code> commands, <code>cvs</code> associates your selected <i>kflag</i> with the file, and continues to use it with future update commands on the same file until you specify otherwise. </p>
<p> The <code>-k</code> option is available with the <code>add</code>, <code>checkout</code>, <code>diff</code>, <code>rdiff</code>, <code>import</code> and <code>update</code> commands. </p>
<dt>
<dd> <code>-l</code></p>
<dt>
<dd> Local; run only in current working directory, rather than recursing through subdirectories. </p>
<p> Available with the following commands: <code>annotate</code>, <code>checkout</code>, <code>commit</code>, <code>diff</code>, <code>edit</code>, <code>editors</code>, <code>export</code>, <code>log</code>, <code>rdiff</code>, <code>remove</code>, <code>rtag</code>, <code>status</code>, <code>tag</code>, <code>unedit</code>, <code>update</code>, <code>watch</code>, and <code>watchers</code>. </p>
<dt>
<dd> <code>-m </code><i>message</i></p>
<dt>
<dd> Use <i>message</i> as log information, instead of invoking an editor. </p>
<p> Available with the following commands: <code>add</code>, <code>commit</code> and <code>import</code>. </p>
<dt>
<dd> <code>-n</code></p>
<dt>
<dd> Do not run any tag program. (A program can be specified to run in the modules database (see node `modules&#8217; in the CVS manual); this option bypasses it). </p>
<p> <code>This is not the same as the cvs -n program option, which you can specify to the left of a cvs command!</code> </p>
<p> Available with the <code>checkout</code>, <code>export</code>, and <code>rtag</code> commands. </p>
<dt>
<dd> <code>-P</code></p>
<dt>
<dd> Prune empty directories. See `Removing directories&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-p</code></p>
<dt>
<dd> Pipe the files retrieved from the repository to standard output, rather than writing them in the current directory. Available with the <code>checkout</code> and <code>update</code> commands. </p>
<dt>
<dd> <code>-R</code></p>
<dt>
<dd> Process directories recursively. This is on by default. </p>
<p> Available with the following commands: <code>annotate</code>, <code>checkout</code>, <code>commit</code>, <code>diff</code>, <code>edit</code>, <code>editors</code>, <code>export</code>, <code>rdiff</code>, <code>remove</code>, <code>rtag</code>, <code>status</code>, <code>tag</code>, <code>unedit</code>, <code>update</code>, <code>watch</code>, and <code>watchers</code>. </p>
<dt>
<dd> <code>-r </code><i>tag</i></p>
<dt>
<dd> Use the revision specified by the <i>tag</i> argument instead of the default <i>head</i> revision. As well as arbitrary tags defined with the <code>tag</code> or <code>rtag</code> command, two special tags are always available: <code>HEAD</code> refers to the most recent version available in the repository, and <code>BASE</code> refers to the revision you last checked out into the current working directory. </p>
<p> The tag specification is sticky when you use this with <code>checkout</code> or <code>update</code> to make your own copy of a file: <code>cvs</code> remembers the tag and continues to use it on future update commands, until you specify otherwise (for more information on sticky tags/dates, see node `Sticky tags&#8217; in the CVS manual). </p>
<p> The tag can be either a symbolic or numeric tag, as described in `Tags&#8217; in the CVS manual, or the name of a branch, as described in `Branching and merging&#8217; in the CVS manual. When a command expects a specific revision, the name of a branch is interpreted as the most recent revision on that branch. </p>
<p> Specifying the <code>-q</code> global option along with the <code>-r</code> command option is often useful, to suppress the warning messages when the <code>rcs</code> file does not contain the specified tag. </p>
<p> <code>This is not the same as the overall cvs -r option, which you can specify to the left of a cvs command!</code> </p>
<p> <code>-r</code> is available with the <code>annotate</code>, <code>checkout</code>, <code>commit</code>, <code>diff</code>, <code>history</code>, <code>export</code>, <code>rdiff</code>, <code>rtag</code>, and <code>update</code> commands. </p>
<dt>
<dd> <code>-W</code></p>
<dt>
<dd> Specify file names that should be filtered. You can use this option repeatedly. The spec can be a file name pattern of the same type that you can specify in the <code>.cvswrappers</code> file. Available with the following commands: <code>import</code>, and <code>update</code>. </p>
</dl>
<h2>add</h2>
<h3>Add files and directories to the repository</h3>
<dl>
<dt>&bull;</p>
<dd> Synopsis: add [-k rcs-kflag] [-m message] files&#8230;</p>
<dt>&bull;</p>
<dd> Requires: repository, working directory.</p>
<dt>&bull;</p>
<dd> Changes: repository, working directory. </p>
<p> The <code>add</code> command is used to present new files and directories for addition into the <code>cvs</code> repository. When <code>add</code> is used on a directory, a new directory is created in the repository immediately. When used on a file, only the working directory is updated. Changes to the repository are not made until the <code>commit</code> command is used on the newly added file. </p>
<p> The <code>add</code> command also resurrects files that have been previously removed. This can be done before or after the <code>commit</code> command is used to finalize the removal of files. Resurrected files are restored into the working directory at the time the <code>add</code> command is executed. </p>
</dl>
<h2>add options</h2>
<p> These standard options are supported by <code>add</code> (see node `Common options&#8217; in the CVS manual, for a complete description of them): </p>
<dl>
<dt>
<dd> <code>-k </code><i>kflag</i></p>
<dt>
<dd> Process keywords according to <i>kflag</i>. See `Keyword substitution&#8217; in the CVS manual. This option is sticky; future updates of this file in this working directory will use the same <i>kflag</i>. The <code>status</code> command can be viewed to see the sticky options. For more information on the <code>status</code> command, see node `Invoking CVS&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-m </code><i>message</i></p>
<dt>
<dd> Use <i>message</i> as the log message, instead of invoking an editor. </p>
</dl>
<h2>add examples</h2>
<h3>Adding a directory</h3>
<dl>
<dt>
<dd> $ mkdir doc</p>
<dt>
<dd> $ cvs add doc</p>
<dt>
<dd> Directory /path/to/repository/doc added to the repository </p>
<dt>
<dd>
</dl>
<h3>Adding a file</h3>
<dl>
<dt>
<dd> $ &gt;TODO</p>
<dt>
<dd> $ cvs add TODO</p>
<dt>
<dd> cvs add: scheduling file `TODO&#8217; for addition</p>
<dt>
<dd> cvs add: use &#8216;cvs commit&#8217; to add this file permanently </p>
<dt>
<dd>
</dl>
<h3>Undoing a <code>remove</code> command</h3>
<dl>
<dt>
<dd> $ rm -f makefile</p>
<dt>
<dd> $ cvs remove makefile</p>
<dt>
<dd> cvs remove: scheduling `makefile&#8217; for removal</p>
<dt>
<dd> cvs remove: use &#8216;cvs commit&#8217; to remove this file permanently</p>
<dt>
<dd> $ cvs add makefile</p>
<dt>
<dd> U makefile</p>
<dt>
<dd> cvs add: makefile, version 1.2, resurrected </p>
<dt>
<dd>
</dl>
<h2>admin</h2>
<h3>Administration</h3>
<dl>
<dt>&bull;</p>
<dd> Requires: repository, working directory.</p>
<dt>&bull;</p>
<dd> Changes: repository.</p>
<dt>&bull;</p>
<dd> Synonym: rcs </p>
<p> This is the <code>cvs</code> interface to assorted administrative facilities. Some of them have questionable usefulness for <code>cvs</code> but exist for historical purposes. Some of the questionable options are likely to disappear in the future. This command <i>does</i> work recursively, so extreme care should be used. </p>
<p> On unix, if there is a group named <code>cvsadmin</code>, only members of that group can run <code>cvs admin</code> (except for the <code>cvs admin -k</code> command, which can be run by anybody). This group should exist on the server, or any system running the non-client/server <code>cvs</code>. To disallow <code>cvs admin</code> for all users, create a group with no users in it. On NT, the <code>cvsadmin</code> feature does not exist and all users can run <code>cvs admin</code>. </p>
</dl>
<h2>admin options</h2>
<p> Some of these options have questionable usefulness for <code>cvs</code> but exist for historical purposes. Some even make it impossible to use <code>cvs</code> until you undo the effect! </p>
<dl>
<dt>
<dd> <code>-A</code><i>oldfile</i></p>
<dt>
<dd> Might not work together with <code>cvs</code>. Append the access list of <i>oldfile</i> to the access list of the <code>rcs</code> file. </p>
<dt>
<dd> <code>-a</code><i>logins</i></p>
<dt>
<dd> Might not work together with <code>cvs</code>. Append the login names appearing in the comma-separated list <i>logins</i> to the access list of the <code>rcs</code> file. </p>
<dt>
<dd> <code>-b[</code><i>rev</i><code>]</code></p>
<dt>
<dd> Set the default branch to <i>rev</i>. In <code>cvs</code>, you normally do not manipulate default branches; sticky tags (see node `Sticky tags&#8217; in the CVS manual) are a better way to decide which branch you want to work on. There is one reason to run <code>cvs admin -b</code>: to revert to the vendor&#8217;s version when using vendor branches (see node `Reverting local changes&#8217; in the CVS manual). There can be no space between <code>-b</code> and its argument. </p>
<dt>
<dd> <code>-c</code><i>string</i></p>
<dt>
<dd> Sets the comment leader to <i>string</i>. The comment leader is not used by current versions of <code>cvs</code> or <code>rcs</code> 5.7. Therefore, you can almost surely not worry about it. See `Keyword substitution&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-e[</code><i>logins</i><code>]</code></p>
<dt>
<dd> Might not work together with <code>cvs</code>. Erase the login names appearing in the comma-separated list <i>logins</i> from the access list of the RCS file. If <i>logins</i> is omitted, erase the entire access list. There can be no space between <code>-e</code> and its argument. </p>
<dt>
<dd> <code>-I</code></p>
<dt>
<dd> Run interactively, even if the standard input is not a terminal. This option does not work with the client/server <code>cvs</code> and is likely to disappear in a future release of <code>cvs</code>. </p>
<dt>
<dd> <code>-i</code></p>
<dt>
<dd> Useless with <code>cvs</code>. This creates and initializes a new <code>rcs</code> file, without depositing a revision. With <code>cvs</code>, add files with the <code>cvs add</code> command (see node `Adding files&#8217; in the CVS manual). </p>
<dt>
<dd> <code>-k</code><i>subst</i></p>
<dt>
<dd> Set the default keyword substitution to <i>subst</i>. See `Keyword substitution&#8217; in the CVS manual. Giving an explicit <code>-k</code> option to <code>cvs update</code>, <code>cvs export</code>, or <code>cvs checkout</code> overrides this default. </p>
<dt>
<dd> <code>-l[</code><i>rev</i><code>]</code></p>
<dt>
<dd> Lock the revision with number <i>rev</i>. If a branch is given, lock the latest revision on that branch. If <i>rev</i> is omitted, lock the latest revision on the default branch. There can be no space between <code>-l</code> and its argument. </p>
<p> This can be used in conjunction with the <code>rcslock.pl</code> script in the <code>contrib</code> directory of the <code>cvs</code> source distribution to provide reserved checkouts (where only one user can be editing a given file at a time). See the comments in that file for details (and see the <code>README</code> file in that directory for disclaimers about the unsupported nature of contrib). According to comments in that file, locking must set to strict (which is the default). </p>
<dt>
<dd> <code>-L</code></p>
<dt>
<dd> Set locking to strict. Strict locking means that the owner of an RCS file is not exempt from locking for checkin. For use with <code>cvs</code>, strict locking must be set; see the discussion under the <code>-l</code> option above. </p>
<dt>
<dd> <code>-m</code><i>rev</i><code>:</code><i>msg</i></p>
<dt>
<dd> Replace the log message of revision <i>rev</i> with <i>msg</i>. </p>
<dt>
<dd> <code>-N</code><i>name</i><code>[:[</code><i>rev</i><code>]]</code></p>
<dt>
<dd> Act like <code>-n</code>, except override any previous assignment of <i>name</i>. For use with magic branches, see `Magic branch numbers&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-n</code><i>name</i><code>[:[</code><i>rev</i><code>]]</code></p>
<dt>
<dd> Associate the symbolic name <i>name</i> with the branch or revision <i>rev</i>. It is normally better to use <code>cvs tag</code> or <code>cvs rtag</code> instead. Delete the symbolic name if both <code>:</code> and <i>rev</i> are omitted; otherwise, print an error message if <i>name</i> is already associated with another number. If <i>rev</i> is symbolic, it is expanded before association. A <i>rev</i> consisting of a branch number followed by a <code>.</code> stands for the current latest revision in the branch. A <code>:</code> with an empty <i>rev</i> stands for the current latest revision on the default branch, normally the trunk. For example, <code>cvs admin -n</code><i>name</i><code>:</code> associates <i>name</i> with the current latest revision of all the RCS files; this contrasts with <code>cvs admin -n</code><i>name</i><code>:$</code> which associates <i>name</i> with the revision numbers extracted from keyword strings in the corresponding working files. </p>
<dt>
<dd> <code>-o</code><i>range</i></p>
<dt>
<dd> Deletes (<i>outdates</i>) the revisions given by <i>range</i>. </p>
<p> Note that this command can be quite dangerous unless you know <i>exactly</i> what you are doing (for example see the warnings below about how the <i>rev1</i>:<i>rev2</i> syntax is confusing). </p>
<p> If you are short on disc this option might help you. But think twice before using it&#8212;there is no way short of restoring the latest backup to undo this command! If you delete different revisions than you planned, either due to carelessness or (heaven forbid) a <code>cvs</code> bug, there is no opportunity to correct the error before the revisions are deleted. It probably would be a good idea to experiment on a copy of the repository first. </p>
<p> Specify <i>range</i> in one of the following ways: </p>
<dt>
<dd> <i>rev1</i><code>::</code><i>rev2</i></p>
<dt>
<dd> Collapse all revisions between rev1 and rev2, so that <code>cvs</code> only stores the differences associated with going from rev1 to rev2, not intermediate steps. For example, after <code>-o 1.3::1.5</code> one can retrieve revision 1.3, revision 1.5, or the differences to get from 1.3 to 1.5, but not the revision 1.4, or the differences between 1.3 and 1.4. Other examples: <code>-o 1.3::1.4</code> and <code>-o 1.3::1.3</code> have no effect, because there are no intermediate revisions to remove. </p>
<dt>
<dd> <code>::</code><i>rev</i></p>
<dt>
<dd> Collapse revisions between the beginning of the branch containing <i>rev</i> and <i>rev</i> itself. The branchpoint and <i>rev</i> are left intact. For example, <code>-o ::1.3.2.6</code> deletes revision 1.3.2.1, revision 1.3.2.5, and everything in between, but leaves 1.3 and 1.3.2.6 intact. </p>
<dt>
<dd> <i>rev</i><code>::</code></p>
<dt>
<dd> Collapse revisions between <i>rev</i> and the end of the branch containing <i>rev</i>. Revision <i>rev</i> is left intact but the head revision is deleted. </p>
<dt>
<dd> <i>rev</i></p>
<dt>
<dd> Delete the revision <i>rev</i>. For example, <code>-o 1.3</code> is equivalent to <code>-o 1.2::1.4</code>. </p>
<dt>
<dd> <i>rev1</i><code>:</code><i>rev2</i></p>
<dt>
<dd> Delete the revisions from <i>rev1</i> to <i>rev2</i>, inclusive, on the same branch. One will not be able to retrieve <i>rev1</i> or <i>rev2</i> or any of the revisions in between. For example, the command <code>cvs admin -oR_1_01:R_1_02 .</code> is rarely useful. It means to delete revisions up to, and including, the tag R_1_02. But beware! If there are files that have not changed between R_1_02 and R_1_03 the file will have <i>the same</i> numerical revision number assigned to the tags R_1_02 and R_1_03. So not only will it be impossible to retrieve R_1_02; R_1_03 will also have to be restored from the tapes! In most cases you want to specify <i>rev1</i>::<i>rev2</i> instead. </p>
<dt>
<dd> <code>:</code><i>rev</i></p>
<dt>
<dd> Delete revisions from the beginning of the branch containing <i>rev</i> up to and including <i>rev</i>. </p>
<dt>
<dd> <i>rev</i><code>:</code></p>
<dt>
<dd> Delete revisions from revision <i>rev</i>, including <i>rev</i> itself, to the end of the branch containing <i>rev</i>. </p>
<p> None of the revisions to be deleted may have branches or locks. </p>
<p> If any of the revisions to be deleted have symbolic names, and one specifies one of the <code>::</code> syntaxes, then <code>cvs</code> will give an error and not delete any revisions. If you really want to delete both the symbolic names and the revisions, first delete the symbolic names with <code>cvs tag -d</code>, then run <code>cvs admin -o</code>. If one specifies the non-<code>::</code> syntaxes, then <code>cvs</code> will delete the revisions but leave the symbolic names pointing to nonexistent revisions. This behavior is preserved for compatibility with previous versions of <code>cvs</code>, but because it isn&#8217;t very useful, in the future it may change to be like the <code>::</code> case. </p>
<p> Due to the way <code>cvs</code> handles branches <i>rev</i> cannot be specified symbolically if it is a branch. See `Magic branch numbers&#8217; in the CVS manual for an explanation. </p>
<p> Make sure that no-one has checked out a copy of the revision you outdate. Strange things will happen if he starts to edit it and tries to check it back in. For this reason, this option is not a good way to take back a bogus commit; commit a new revision undoing the bogus change instead (see node `Merging two revisions&#8217; in the CVS manual). </p>
<dt>
<dd> <code>-q</code></p>
<dt>
<dd> Run quietly; do not print diagnostics. </p>
<dt>
<dd> <code>-s</code><i>state</i><code>[:</code><i>rev</i><code>]</code></p>
<dt>
<dd> Useful with <code>cvs</code>. Set the state attribute of the revision <i>rev</i> to <i>state</i>. If <i>rev</i> is a branch number, assume the latest revision on that branch. If <i>rev</i> is omitted, assume the latest revision on the default branch. Any identifier is acceptable for <i>state</i>. A useful set of states is <code>Exp</code> (for experimental), <code>Stab</code> (for stable), and <code>Rel</code> (for released). By default, the state of a new revision is set to <code>Exp</code> when it is created. The state is visible in the output from <i>cvs log</i> (see node `log&#8217; in the CVS manual), and in the <code>$</code>Log$ and <code>$</code>State$ keywords (see node `Keyword substitution&#8217; in the CVS manual). Note that <code>cvs</code> uses the <code>dead</code> state for its own purposes (see node `Attic&#8217; in the CVS manual); to take a file to or from the <code>dead</code> state use commands like <code>cvs remove</code> and <code>cvs add</code> (see node `Adding and removing&#8217; in the CVS manual), not <code>cvs admin -s</code>. </p>
<dt>
<dd> <code>-t[</code><i>file</i><code>]</code></p>
<dt>
<dd> Useful with <code>cvs</code>. Write descriptive text from the contents of the named <i>file</i> into the RCS file, deleting the existing text. The <i>file</i> pathname may not begin with <code>&#8211;</code>. The descriptive text can be seen in the output from <code>cvs log</code> (see node `log&#8217; in the CVS manual). There can be no space between <code>-t</code> and its argument. </p>
<p> If <i>file</i> is omitted, obtain the text from standard input, terminated by end-of-file or by a line containing <code>.</code> by itself. Prompt for the text if interaction is possible; see <code>-I</code>. </p>
<dt>
<dd> <code>-t-</code><i>string</i></p>
<dt>
<dd> Similar to <code>-t</code><i>file</i>. Write descriptive text from the <i>string</i> into the <code>rcs</code> file, deleting the existing text. There can be no space between <code>-t</code> and its argument. </p>
<dt>
<dd> <code>-U</code></p>
<dt>
<dd> Set locking to non-strict. Non-strict locking means that the owner of a file need not lock a revision for checkin. For use with <code>cvs</code>, strict locking must be set; see the discussion under the <code>-l</code> option above. </p>
<dt>
<dd> <code>-u[</code><i>rev</i><code>]</code></p>
<dt>
<dd> See the option <code>-l</code> above, for a discussion of using this option with <code>cvs</code>. Unlock the revision with number <i>rev</i>. If a branch is given, unlock the latest revision on that branch. If <i>rev</i> is omitted, remove the latest lock held by the caller. Normally, only the locker of a revision may unlock it; somebody else unlocking a revision breaks the lock. This causes the original locker to be sent a <code>commit</code> notification (see node `Getting Notified&#8217; in the CVS manual). There can be no space between <code>-u</code> and its argument. </p>
<dt>
<dd> <code>-V</code><i>n</i></p>
<dt>
<dd> In previous versions of <code>cvs</code>, this option meant to write an <code>rcs</code> file which would be acceptable to <code>rcs</code> version <i>n</i>, but it is now obsolete and specifying it will produce an error. </p>
<dt>
<dd> <code>-x</code><i>suffixes</i></p>
<dt>
<dd> In previous versions of <code>cvs</code>, this was documented as a way of specifying the names of the <code>rcs</code> files. However, <code>cvs</code> has always required that the <code>rcs</code> files used by <code>cvs</code> end in <code>,v</code>, so this option has never done anything useful. </p>
</dl>
<h2>annotate</h2>
<h3>What revision modified each line of a file?</h3>
<dl>
<dt>&bull;</p>
<dd> Synopsis: annotate [options] files&#8230;</p>
<dt>&bull;</p>
<dd> Requires: repository.</p>
<dt>&bull;</p>
<dd> Synonym: blame</p>
<dt>&bull;</p>
<dd> Changes: nothing. </p>
<p> For each file in <i>files</i>, print the head revision of the trunk, together with information on the last modification for each line. </p>
</dl>
<h2>annotate options</h2>
<p> These standard options are supported by <code>annotate</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dt>
<dd> <code>-l</code></p>
<dt>
<dd> Local directory only, no recursion. </p>
<dt>
<dd> <code>-R</code></p>
<dt>
<dd> Process directories recursively. </p>
<dt>
<dd> <code>-f</code></p>
<dt>
<dd> Use head revision if tag/date not found. </p>
<dt>
<dd> <code>-F</code></p>
<dt>
<dd> Annotate binary files. </p>
<dt>
<dd> <code>-r </code><i>revision</i></p>
<dt>
<dd> Annotate file as of specified revision/tag. </p>
<dt>
<dd> <code>-D </code><i>date</i></p>
<dt>
<dd> Annotate file as of specified date. </p>
</dl>
<h2>annotate example</h2>
<p> For example: </p>
<dl>
<dt>
<dd> $ cvs annotate ssfile</p>
<dt>
<dd> Annotations for ssfile</p>
<dt>
<dd> ***************</p>
<dt>
<dd> 1.1 (mary 27-Mar-96): ssfile line 1</p>
<dt>
<dd> 1.2 (joe 28-Mar-96): ssfile line 2 </p>
<dt>
<dd>
<p> The file <code>ssfile</code> currently contains two lines. The <code>ssfile line 1</code> line was checked in by <code>mary</code> on March 27. Then, on March 28, <code>joe</code> added a line <code>ssfile line 2</code>, without modifying the <code>ssfile line 1</code> line. This report doesn&#8217;t tell you anything about lines which have been deleted or replaced; you need to use <code>cvs diff</code> for that (see node `diff&#8217; in the CVS manual). </p>
<p> The options to <code>cvs annotate</code> are listed in `Invoking CVS&#8217; in the CVS manual, and can be used to select the files and revisions to annotate. The options are described in more detail there and in `Common options&#8217; in the CVS manual. </p>
</dl>
<h2>checkout</h2>
<h3>Check out sources for editing</h3>
<dl>
<dt>&bull;</p>
<dd> Synopsis: checkout [options] modules&#8230;</p>
<dt>&bull;</p>
<dd> Requires: repository.</p>
<dt>&bull;</p>
<dd> Changes: working directory.</p>
<dt>&bull;</p>
<dd> Synonyms: co, get </p>
<p> Create or update a working directory containing copies of the source files specified by <i>modules</i>. You must execute <code>checkout</code> before using most of the other <code>cvs</code> commands, since most of them operate on your working directory. </p>
<p> The <i>modules</i> are either symbolic names for some collection of source directories and files, or paths to directories or files in the repository. The symbolic names are defined in the <code>modules</code> file. See `modules&#8217; in the CVS manual. </p>
<p> Depending on the modules you specify, <code>checkout</code> may recursively create directories and populate them with the appropriate source files. You can then edit these source files at any time (regardless of whether other software developers are editing their own copies of the sources); update them to include new changes applied by others to the source repository; or commit your work as a permanent change to the source repository. </p>
<p> Note that <code>checkout</code> is used to create directories. The top-level directory created is always added to the directory where <code>checkout</code> is invoked, and usually has the same name as the specified module. In the case of a module alias, the created sub-directory may have a different name, but you can be sure that it will be a sub-directory, and that <code>checkout</code> will show the relative path leading to each file as it is extracted into your private work area (unless you specify the <code>-Q</code> global option). </p>
<p> The files created by <code>checkout</code> are created read-write, unless the <code>-r</code> option to <code>cvs</code> (see node `Global options&#8217; in the CVS manual) is specified, the <code>CVSREAD</code> environment variable is specified (see node `Environment variables&#8217; in the CVS manual), or a watch is in effect for that file (see node `Watches&#8217; in the CVS manual). </p>
<p> Note that running <code>checkout</code> on a directory that was already built by a prior <code>checkout</code> is also permitted. This is similar to specifying the <code>-d</code> option to the <code>update</code> command in the sense that new directories that have been created in the repository will appear in your work area. However, <code>checkout</code> takes a module name whereas <code>update</code> takes a directory name. Also to use <code>checkout</code> this way it must be run from the top level directory (where you originally ran <code>checkout</code> from), so before you run <code>checkout</code> to update an existing directory, don&#8217;t forget to change your directory to the top level directory. </p>
<p> For the output produced by the <code>checkout</code> command, see node `update output&#8217; in the CVS manual. </p>
</dl>
<h2>checkout options</h2>
<p> These standard options are supported by <code>checkout</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dt>
<dd> <code>-D </code><i>date</i></p>
<dt>
<dd> Use the most recent revision no later than <i>date</i>. This option is sticky, and implies <code>-P</code>. See `Sticky tags&#8217; in the CVS manual for more information on sticky tags/dates. </p>
<dt>
<dd> <code>-f</code></p>
<dt>
<dd> Only useful with the <code>-D </code><i>date</i> or <code>-r </code><i>tag</i> flags. If no matching revision is found, retrieve the most recent revision (instead of ignoring the file). </p>
<dt>
<dd> <code>-k </code><i>kflag</i></p>
<dt>
<dd> Process keywords according to <i>kflag</i>. See `Keyword substitution&#8217; in the CVS manual. This option is sticky; future updates of this file in this working directory will use the same <i>kflag</i>. The <code>status</code> command can be viewed to see the sticky options. See `Invoking CVS&#8217; in the CVS manual for more information on the <code>status</code> command. </p>
<dt>
<dd> <code>-l</code></p>
<dt>
<dd> Local; run only in current working directory. </p>
<dt>
<dd> <code>-n</code></p>
<dt>
<dd> Do not run any checkout program (as specified with the <code>-o</code> option in the modules file; see node `modules&#8217; in the CVS manual). </p>
<dt>
<dd> <code>-P</code></p>
<dt>
<dd> Prune empty directories. See `Moving directories&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-p</code></p>
<dt>
<dd> Pipe files to the standard output. </p>
<dt>
<dd> <code>-R</code></p>
<dt>
<dd> Checkout directories recursively. This option is on by default. </p>
<dt>
<dd> <code>-r </code><i>tag</i></p>
<dt>
<dd> Use revision <i>tag</i>. This option is sticky, and implies <code>-P</code>. See `Sticky tags&#8217; in the CVS manual, for more information on sticky tags/dates. </p>
<p> In addition to those, you can use these special command options with <code>checkout</code>: </p>
<dt>
<dd> <code>-A</code></p>
<dt>
<dd> Reset any sticky tags, dates, or <code>-k</code> options. Does not reset sticky <code>-k</code> options on modified files. See `Sticky tags&#8217; in the CVS manual for more information on sticky tags/dates. </p>
<dt>
<dd> <code>-c</code></p>
<dt>
<dd> Copy the module file, sorted, to the standard output, instead of creating or modifying any files or directories in your working directory. </p>
<dt>
<dd> <code>-d </code><i>dir</i></p>
<dt>
<dd> Create a directory called <i>dir</i> for the working files, instead of using the module name. In general, using this flag is equivalent to using <code>mkdir </code><i>dir</i><code>; cd </code><i>dir</i> followed by the checkout command without the <code>-d</code> flag. </p>
<p> There is an important exception, however. It is very convenient when checking out a single item to have the output appear in a directory that doesn&#8217;t contain empty intermediate directories. In this case <i>only</i>, <code>cvs</code> tries to &#8220;shorten&#8221; pathnames to avoid those empty directories. </p>
<p> For example, given a module <code>foo</code> that contains the file <code>bar.c</code>, the command <code>cvs co -d dir foo</code> will create directory <code>dir</code> and place <code>bar.c</code> inside. Similarly, given a module <code>bar</code> which has subdirectory <code>baz</code> wherein there is a file <code>quux.c</code>, the command <code>cvs co -d dir bar/baz</code> will create directory <code>dir</code> and place <code>quux.c</code> inside. </p>
<p> Using the <code>-N</code> flag will defeat this behavior. Given the same module definitions above, <code>cvs co -N -d dir foo</code> will create directories <code>dir/foo</code> and place <code>bar.c</code> inside, while <code>cvs co -N -d dir bar/baz</code> will create directories <code>dir/bar/baz</code> and place <code>quux.c</code> inside. </p>
<dt>
<dd> <code>-j </code><i>tag</i></p>
<dt>
<dd> With two <code>-j</code> options, merge changes from the revision specified with the first <code>-j</code> option to the revision specified with the second <code>j</code> option, into the working directory. </p>
<p> With one <code>-j</code> option, merge changes from the ancestor revision to the revision specified with the <code>-j</code> option, into the working directory. The ancestor revision is the common ancestor of the revision which the working directory is based on, and the revision specified in the <code>-j</code> option. </p>
<p> In addition, each -j option can contain an optional date specification which, when used with branches, can limit the chosen revision to one within a specific date. An optional date is specified by adding a colon (:) to the tag: <code>-j</code><i>Symbolic_Tag</i><code>:</code><i>Date_Specifier</i>. </p>
<p> See `Branching and merging&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-N</code></p>
<dt>
<dd> Only useful together with <code>-d </code><i>dir</i>. With this option, <code>cvs</code> will not &#8220;shorten&#8221; module paths in your working directory when you check out a single module. See the <code>-d</code> flag for examples and a discussion. </p>
<dt>
<dd> <code>-s</code></p>
<dt>
<dd> Like <code>-c</code>, but include the status of all modules, and sort it by the status string. See `modules&#8217; in the CVS manual, for info about the <code>-s</code> option that is used inside the modules file to set the module status. </p>
</dl>
<h2>checkout examples</h2>
<p> Get a copy of the module <code>tc</code>: </p>
<dl>
<dt>
<dd> $ cvs checkout tc </p>
<dt>
<dd>
<p> Get a copy of the module <code>tc</code> as it looked one day ago: </p>
<dt>
<dd> $ cvs checkout -D yesterday tc </p>
<dt>
<dd>
</dl>
<h2>commit</h2>
<h3>Check files into the repository</h3>
<dl>
<dt>&bull;</p>
<dd> Synopsis: commit [-lRf] [-m &#8216;log_message&#8217; | -F file] [-r revision] [files&#8230;]</p>
<dt>&bull;</p>
<dd> Requires: working directory, repository.</p>
<dt>&bull;</p>
<dd> Changes: repository.</p>
<dt>&bull;</p>
<dd> Synonym: ci </p>
<p> Use <code>commit</code> when you want to incorporate changes from your working source files into the source repository. </p>
<p> If you don&#8217;t specify particular files to commit, all of the files in your working current directory are examined. <code>commit</code> is careful to change in the repository only those files that you have really changed. By default (or if you explicitly specify the <code>-R</code> option), files in subdirectories are also examined and committed if they have changed; you can use the <code>-l</code> option to limit <code>commit</code> to the current directory only. </p>
<p> <code>commit</code> verifies that the selected files are up to date with the current revisions in the source repository; it will notify you, and exit without committing, if any of the specified files must be made current first with <code>update</code> (see node `update&#8217; in the CVS manual). <code>commit</code> does not call the <code>update</code> command for you, but rather leaves that for you to do when the time is right. </p>
<p> When all is well, an editor is invoked to allow you to enter a log message that will be written to one or more logging programs (see node `modules&#8217; in the CVS manual, and see node `loginfo&#8217; in the CVS manual) and placed in the <code>rcs</code> file inside the repository. This log message can be retrieved with the <code>log</code> command; see node `log&#8217; in the CVS manual. You can specify the log message on the command line with the <code>-m </code><i>message</i> option, and thus avoid the editor invocation, or use the <code>-F </code><i>file</i> option to specify that the argument file contains the log message. </p>
</dl>
<h2>commit options</h2>
<p> These standard options are supported by <code>commit</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dt>
<dd> <code>-l</code></p>
<dt>
<dd> Local; run only in current working directory. </p>
<dt>
<dd> <code>-R</code></p>
<dt>
<dd> Commit directories recursively. This is on by default. </p>
<dt>
<dd> <code>-r </code><i>revision</i></p>
<dt>
<dd> Commit to <i>revision</i>. <i>revision</i> must be either a branch, or a revision on the main trunk that is higher than any existing revision number (see node `Assigning revisions&#8217; in the CVS manual). You cannot commit to a specific revision on a branch. </p>
<p> <code>commit</code> also supports these options: </p>
<dt>
<dd> <code>-F </code><i>file</i></p>
<dt>
<dd> Read the log message from <i>file</i>, instead of invoking an editor. </p>
<dt>
<dd> <code>-f</code></p>
<dt>
<dd> Note that this is not the standard behavior of the <code>-f</code> option as defined in `Common options&#8217; in the CVS manual. </p>
<p> Force <code>cvs</code> to commit a new revision even if you haven&#8217;t made any changes to the file. If the current revision of <i>file</i> is 1.7, then the following two commands are equivalent: </p>
<dt>
<dd> $ cvs commit -f <i>file</i></p>
<dt>
<dd> $ cvs commit -r 1.8 <i>file</i> </p>
<dt>
<dd>
<p> The <code>-f</code> option disables recursion (i.e., it implies <code>-l</code>). To force <code>cvs</code> to commit a new revision for all files in all subdirectories, you must use <code>-f -R</code>. </p>
<dt>
<dd> <code>-m </code><i>message</i></p>
<dt>
<dd> Use <i>message</i> as the log message, instead of invoking an editor. </p>
</dl>
<h2>commit examples</h2>
<h3>Committing to a branch</h3>
<p> You can commit to a branch revision (one that has an even number of dots) with the <code>-r</code> option. To create a branch revision, use the <code>-b</code> option of the <code>rtag</code> or <code>tag</code> commands (see node `Branching and merging&#8217; in the CVS manual). Then, either <code>checkout</code> or <code>update</code> can be used to base your sources on the newly created branch. From that point on, all <code>commit</code> changes made within these working sources will be automatically added to a branch revision, thereby not disturbing main-line development in any way. For example, if you had to create a patch to the 1.2 version of the product, even though the 2.0 version is already under development, you might do: </p>
<dl>
<dt>
<dd> $ cvs rtag -b -r FCS1_2 FCS1_2_Patch product_module</p>
<dt>
<dd> $ cvs checkout -r FCS1_2_Patch product_module</p>
<dt>
<dd> $ cd product_module</p>
<dt>
<dd> [[ hack away ]]</p>
<dt>
<dd> $ cvs commit </p>
<dt>
<dd>
<p> This works automatically since the <code>-r</code> option is sticky. </p>
</dl>
<h3>Creating the branch after editing</h3>
<p> Say you have been working on some extremely experimental software, based on whatever revision you happened to checkout last week. If others in your group would like to work on this software with you, but without disturbing main-line development, you could commit your change to a new branch. Others can then checkout your experimental stuff and utilize the full benefit of <code>cvs</code> conflict resolution. The scenario might look like: </p>
<dl>
<dt>
<dd> [[ hacked sources are present ]]</p>
<dt>
<dd> $ cvs tag -b EXPR1</p>
<dt>
<dd> $ cvs update -r EXPR1</p>
<dt>
<dd> $ cvs commit </p>
<dt>
<dd>
<p> The <code>update</code> command will make the <code>-r EXPR1</code> option sticky on all files. Note that your changes to the files will never be removed by the <code>update</code> command. The <code>commit</code> will automatically commit to the correct branch, because the <code>-r</code> is sticky. You could also do like this: </p>
<dt>
<dd> [[ hacked sources are present ]]</p>
<dt>
<dd> $ cvs tag -b EXPR1</p>
<dt>
<dd> $ cvs commit -r EXPR1 </p>
<dt>
<dd>
<p> but then, only those files that were changed by you will have the <code>-r EXPR1</code> sticky flag. If you hack away, and commit without specifying the <code>-r EXPR1</code> flag, some files may accidentally end up on the main trunk. </p>
<p> To work with you on the experimental change, others would simply do </p>
<dt>
<dd> $ cvs checkout -r EXPR1 whatever_module </p>
<dt>
<dd>
</dl>
<h2>diff</h2>
<h3>Show differences between revisions</h3>
<dl>
<dt>&bull;</p>
<dd> Synopsis: diff [-lR] [-k kflag] [format_options] [[-r rev1 | -D date1] [-r rev2 | -D date2]] [files&#8230;]</p>
<dt>&bull;</p>
<dd> Requires: working directory, repository.</p>
<dt>&bull;</p>
<dd> Changes: nothing. </p>
<p> The <code>diff</code> command is used to compare different revisions of files. The default action is to compare your working files with the revisions they were based on, and report any differences that are found. </p>
<p> If any file names are given, only those files are compared. If any directories are given, all files under them will be compared. </p>
<p> The exit status for diff is different than for other <code>cvs</code> commands; for details see node `Exit status&#8217; in the CVS manual. </p>
</dl>
<h2>diff options</h2>
<p> These standard options are supported by <code>diff</code> (see node `Common options&#8217; in the CVS manual for a complete description of them): </p>
<dl>
<dt>
<dd> <code>-D </code><i>date</i></p>
<dt>
<dd> Use the most recent revision no later than <i>date</i>. See <code>-r</code> for how this affects the comparison. </p>
<dt>
<dd> <code>-k </code><i>kflag</i></p>
<dt>
<dd> Process keywords according to <i>kflag</i>. See `Keyword substitution&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-l</code></p>
<dt>
<dd> Local; run only in current working directory. </p>
<dt>
<dd> <code>-R</code></p>
<dt>
<dd> Examine directories recursively. This option is on by default. </p>
<dt>
<dd> <code>-r </code><i>tag</i></p>
<dt>
<dd> Compare with revision <i>tag</i>. Zero, one or two <code>-r</code> options can be present. With no <code>-r</code> option, the working file will be compared with the revision it was based on. With one <code>-r</code>, that revision will be compared to your current working file. With two <code>-r</code> options those two revisions will be compared (and your working file will not affect the outcome in any way). </p>
<p> One or both <code>-r</code> options can be replaced by a <code>-D </code><i>date</i> option, described above. </p>
<p> The following options specify the format of the output. They have the same meaning as in GNU diff. Most options have two equivalent names, one of which is a single letter preceded by <code>&#8211;</code>, and the other of which is a long name preceded by <code>&#8212;</code>. </p>
<dt>
<dd> <code>&#8211;</code><i>lines</i></p>
<dt>
<dd> Show <i>lines</i> (an integer) lines of context. This option does not specify an output format by itself; it has no effect unless it is combined with <code>-c</code> or <code>-u</code>. This option is obsolete. For proper operation, <code>patch</code> typically needs at least two lines of context. </p>
<dt>
<dd> <code>-a</code></p>
<dt>
<dd> Treat all files as text and compare them line-by-line, even if they do not seem to be text. </p>
<dt>
<dd> <code>-b</code></p>
<dt>
<dd> Ignore trailing white space and consider all other sequences of one or more white space characters to be equivalent. </p>
<dt>
<dd> <code>-B</code></p>
<dt>
<dd> Ignore changes that just insert or delete blank lines. </p>
<dt>
<dd> <code>&#8211;binary</code></p>
<dt>
<dd> Read and write data in binary mode. </p>
<dt>
<dd> <code>&#8211;brief</code></p>
<dt>
<dd> Report only whether the files differ, not the details of the differences. </p>
<dt>
<dd> <code>-c</code></p>
<dt>
<dd> Use the context output format. </p>
<dt>
<dd> <code>-C </code><i>lines</i></p>
<dt>
<dd>
<dt>
<dd> <code>&#8211;context</code>[<code>=</code><i>lines</i>]</p>
<dt>
<dd> Use the context output format, showing <i>lines</i> (an integer) lines of context, or three if <i>lines</i> is not given. For proper operation, <code>patch</code> typically needs at least two lines of context. </p>
<dt>
<dd> <code>&#8211;changed-group-format=</code><i>format</i></p>
<dt>
<dd> Use <i>format</i> to output a line group containing differing lines from both files in if-then-else format. See `Line group formats&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-d</code></p>
<dt>
<dd> Change the algorithm to perhaps find a smaller set of changes. This makes <code>diff</code> slower (sometimes much slower). </p>
<dt>
<dd> <code>-e</code></p>
<dt>
<dd>
<dt>
<dd> <code>&#8211;ed</code></p>
<dt>
<dd> Make output that is a valid <code>ed</code> script. </p>
<dt>
<dd> <code>&#8211;expand-tabs</code></p>
<dt>
<dd> Expand tabs to spaces in the output, to preserve the alignment of tabs in the input files. </p>
<dt>
<dd> <code>-f</code></p>
<dt>
<dd> Make output that looks vaguely like an <code>ed</code> script but has changes in the order they appear in the file. </p>
<dt>
<dd> <code>-F </code><i>regexp</i></p>
<dt>
<dd> In context and unified format, for each hunk of differences, show some of the last preceding line that matches <i>regexp</i>. </p>
<dt>
<dd> <code>&#8211;forward-ed</code></p>
<dt>
<dd> Make output that looks vaguely like an <code>ed</code> script but has changes in the order they appear in the file. </p>
<dt>
<dd> <code>-H</code></p>
<dt>
<dd> Use heuristics to speed handling of large files that have numerous scattered small changes. </p>
<dt>
<dd> <code>&#8211;horizon-lines=</code><i>lines</i></p>
<dt>
<dd> Do not discard the last <i>lines</i> lines of the common prefix and the first <i>lines</i> lines of the common suffix. </p>
<dt>
<dd> <code>-i</code></p>
<dt>
<dd> Ignore changes in case; consider upper- and lower-case letters equivalent. </p>
<dt>
<dd> <code>-I </code><i>regexp</i></p>
<dt>
<dd> Ignore changes that just insert or delete lines that match <i>regexp</i>. </p>
<dt>
<dd> <code>&#8211;ifdef=</code><i>name</i></p>
<dt>
<dd> Make merged if-then-else output using <i>name</i>. </p>
<dt>
<dd> <code>&#8211;ignore-all-space</code></p>
<dt>
<dd> Ignore white space when comparing lines. </p>
<dt>
<dd> <code>&#8211;ignore-blank-lines</code></p>
<dt>
<dd> Ignore changes that just insert or delete blank lines. </p>
<dt>
<dd> <code>&#8211;ignore-case</code></p>
<dt>
<dd> Ignore changes in case; consider upper- and lower-case to be the same. </p>
<dt>
<dd> <code>&#8211;ignore-matching-lines=</code><i>regexp</i></p>
<dt>
<dd> Ignore changes that just insert or delete lines that match <i>regexp</i>. </p>
<dt>
<dd> <code>&#8211;ignore-space-change</code></p>
<dt>
<dd> Ignore trailing white space and consider all other sequences of one or more white space characters to be equivalent. </p>
<dt>
<dd> <code>&#8211;initial-tab</code></p>
<dt>
<dd> Output a tab rather than a space before the text of a line in normal or context format. This causes the alignment of tabs in the line to look normal. </p>
<dt>
<dd> <code>-L </code><i>label</i></p>
<dt>
<dd> Use <i>label</i> instead of the file name in the context format and unified format headers. </p>
<dt>
<dd> <code>&#8211;label=</code><i>label</i></p>
<dt>
<dd> Use <i>label</i> instead of the file name in the context format and unified format headers. </p>
<dt>
<dd> <code>&#8211;left-column</code></p>
<dt>
<dd> Print only the left column of two common lines in side by side format. </p>
<dt>
<dd> <code>&#8211;line-format=</code><i>format</i></p>
<dt>
<dd> Use <i>format</i> to output all input lines in if-then-else format. See `Line formats&#8217; in the CVS manual. </p>
<dt>
<dd> <code>&#8211;minimal</code></p>
<dt>
<dd> Change the algorithm to perhaps find a smaller set of changes. This makes <code>diff</code> slower (sometimes much slower). </p>
<dt>
<dd> <code>-n</code></p>
<dt>
<dd> Output RCS-format diffs; like <code>-f</code> except that each command specifies the number of lines affected. </p>
<dt>
<dd> <code>-N</code></p>
<dt>
<dd>
<dt>
<dd> <code>&#8211;new-file</code></p>
<dt>
<dd> In directory comparison, if a file is found in only one directory, treat it as present but empty in the other directory. </p>
<dt>
<dd> <code>&#8211;new-group-format=</code><i>format</i></p>
<dt>
<dd> Use <i>format</i> to output a group of lines taken from just the second file in if-then-else format. See `Line group formats&#8217; in the CVS manual. </p>
<dt>
<dd> <code>&#8211;new-line-format=</code><i>format</i></p>
<dt>
<dd> Use <i>format</i> to output a line taken from just the second file in if-then-else format. See `Line formats&#8217; in the CVS manual. </p>
<dt>
<dd> <code>&#8211;old-group-format=</code><i>format</i></p>
<dt>
<dd> Use <i>format</i> to output a group of lines taken from just the first file in if-then-else format. See `Line group formats&#8217; in the CVS manual. </p>
<dt>
<dd> <code>&#8211;old-line-format=</code><i>format</i></p>
<dt>
<dd> Use <i>format</i> to output a line taken from just the first file in if-then-else format. See `Line formats&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-p</code></p>
<dt>
<dd> Show which C function each change is in. </p>
<dt>
<dd> <code>&#8211;rcs</code></p>
<dt>
<dd> Output RCS-format diffs; like <code>-f</code> except that each command specifies the number of lines affected. </p>
<dt>
<dd> <code>&#8211;report-identical-files</code></p>
<dt>
<dd>
<dt>
<dd> <code>-s</code></p>
<dt>
<dd> Report when two files are the same. </p>
<dt>
<dd> <code>&#8211;show-c-function</code></p>
<dt>
<dd> Show which C function each change is in. </p>
<dt>
<dd> <code>&#8211;show-function-line=</code><i>regexp</i></p>
<dt>
<dd> In context and unified format, for each hunk of differences, show some of the last preceding line that matches <i>regexp</i>. </p>
<dt>
<dd> <code>&#8211;side-by-side</code></p>
<dt>
<dd> Use the side by side output format. </p>
<dt>
<dd> <code>&#8211;speed-large-files</code></p>
<dt>
<dd> Use heuristics to speed handling of large files that have numerous scattered small changes. </p>
<dt>
<dd> <code>&#8211;suppress-common-lines</code></p>
<dt>
<dd> Do not print common lines in side by side format. </p>
<dt>
<dd> <code>-t</code></p>
<dt>
<dd> Expand tabs to spaces in the output, to preserve the alignment of tabs in the input files. </p>
<dt>
<dd> <code>-T</code></p>
<dt>
<dd> Output a tab rather than a space before the text of a line in normal or context format. This causes the alignment of tabs in the line to look normal. </p>
<dt>
<dd> <code>&#8211;text</code></p>
<dt>
<dd> Treat all files as text and compare them line-by-line, even if they do not appear to be text. </p>
<dt>
<dd> <code>-u</code></p>
<dt>
<dd> Use the unified output format. </p>
<dt>
<dd> <code>&#8211;unchanged-group-format=</code><i>format</i></p>
<dt>
<dd> Use <i>format</i> to output a group of common lines taken from both files in if-then-else format. see node `Line group formats&#8217; in the CVS manual. </p>
<dt>
<dd> <code>&#8211;unchanged-line-format=</code><i>format</i></p>
<dt>
<dd> Use <i>format</i> to output a line common to both files in if-then-else format. see node `Line formats&#8217; in the CVS manual. </p>
<dt>
<dd> <code>-U </code><i>lines</i></p>
<dt>
<dd>
<dt>
<dd> <code>&#8211;unified</code>[<code>=</code><i>lines</i>]</p>
<dt>
<dd> Use the unified output format, showing <i>lines</i> (an integer) lines of context, or three if <i>lines</i> is not given. For proper operation, <code>patch</code> typically needs at least two lines of context. </p>
<dt>
<dd> <code>-w</code></p>
<dt>
<dd> Ignore white space when comparing lines. </p>
<dt>
<dd> <code>-W </code><i>columns</i></p>
<dt>
<dd>
<dt>
<dd> <code>&#8211;width=</code><i>columns</i></p>
<dt>
<dd> Use an output width of <i>columns</i> in side by side format. </p>
<dt>
<dd> <code>-y</code></p>
<dt>
<dd> Use the side by side output format. </p>
</dl>
<h2>Line group formats</h2>
<p> Line group formats let you specify formats suitable for many applications that allow if-then-else input, including programming languages and text formatting languages. A line group format specifies the output format for a contiguous group of similar lines. </p>
<p> For example, the following command compares the TeX file <code>myfile</code> with the original version from the repository, and outputs a merged file in which old regions are surrounded by <code>egin{em}</code>&#8211;<code>nd{em}</code> lines, and new regions are surrounded by <code>egin{bf}</code>&#8211;<code>nd{bf}</code> lines. </p>
<dl>
<dt>
<dd> cvs diff \</p>
<dt>
<dd>
&#8211;old-group-format=&#8217;egin{em}</p>
<dt>
<dd> %&lt;nd{em}</p>
<dt>
<dd> &#8216; \</p>
<dt>
<dd>
&#8211;new-group-format=&#8217;egin{bf}</p>
<dt>
<dd> %&gt;nd{bf}</p>
<dt>
<dd> &#8216; \</p>
<dt>
<dd>
myfile </p>
<dt>
<dd>
<p> The following command is equivalent to the above example, but it is a little more verbose, because it spells out the default line group formats. </p>
<dt>
<dd> cvs diff \</p>
<dt>
<dd>
&#8211;old-group-format=&#8217;egin{em}</p>
<dt>
<dd> %&lt;nd{em}</p>
<dt>
<dd> &#8216; \</p>
<dt>
<dd>
&#8211;new-group-format=&#8217;egin{bf}</p>
<dt>
<dd> %&gt;nd{bf}</p>
<dt>
<dd> &#8216; \</p>
<dt>
<dd>
&#8211;unchanged-group-format=&#8217;%=&#8217;&nbsp;<wbr>\</p>
<dt>
<dd>
&#8211;changed-group-format=&#8217;egin{em}</p>
<dt>
<dd> %&lt;nd{em}</p>
<dt>
<dd> egin{bf}</p>
<dt>
<dd> %&gt;nd{bf}</p>
<dt>
<dd> &#8216; \</p>
<dt>
<dd>
myfile </p>
<dt>
<dd>
<p> Here is a more advanced example, which outputs a diff listing with headers containing line numbers in a &#8220;plain English&#8221; style. </p>
<dt>
<dd> cvs diff \</p>
<dt>
<dd>
&#8211;unchanged-group-format=&#8221;&nbsp;<wbr>\</p>
<dt>
<dd>
&#8211;old-group-format=&#8217;&#8212;&#8212;&#8211;&nbsp;<wbr>%dn line%(n=1?:s)&nbsp;<wbr>deleted at&nbsp;<wbr>%df:</p>
<dt>
<dd> %&lt;&#8216; \</p>
<dt>
<dd>
&#8211;new-group-format=&#8217;&#8212;&#8212;&#8211;&nbsp;<wbr>%dN line%(N=1?:s)&nbsp;<wbr>added after&nbsp;<wbr>%de:</p>
<dt>
<dd> %&gt;&#8217; \</p>
<dt>
<dd>
&#8211;changed-group-format=&#8217;&#8212;&#8212;&#8211;&nbsp;<wbr>%dn line%(n=1?:s)&nbsp;<wbr>changed at&nbsp;<wbr>%df:</p>
<dt>
<dd> %&lt;&#8212;&#8212;&#8211; to:</p>
<dt>
<dd> %&gt;&#8217; \</p>
<dt>
<dd>
myfile </p>
<dt>
<dd>
<p> To specify a line group format, use one of the options listed below. You can specify up to four line group formats, one for each kind of line group. You should quote <i>format</i>, because it typically contains shell metacharacters. </p>
<dt>
<dd> <code>&#8211;old-group-format=</code><i>format</i></p>
<dt>
<dd> These line groups are hunks containing only lines from the first file. The default old group format is the same as the changed group format if it is specified; otherwise it is a format that outputs the line group as-is. </p>
<dt>
<dd> <code>&#8211;new-group-format=</code><i>format</i></p>
<dt>
<dd> These line groups are hunks containing only lines from the second file. The default new group format is same as the changed group format if it is specified; otherwise it is a format that outputs the line group as-is. </p>
<dt>
<dd> <code>&#8211;changed-group-format=</code><i>format</i></p>
<dt>
<dd> These line groups are hunks containing lines from both files. The default changed group format is the concatenation of the old and new group formats. </p>
<dt>
<dd> <code>&#8211;unchanged-group-format=</code><i>format</i></p>
<dt>
<dd> These line groups contain lines common to both files. The default unchanged group format is a format that outputs the line group as-is. </p>
<p> In a line group format, ordinary characters represent themselves; conversion specifications start with <code>%</code> and have one of the following forms. </p>
<dt>
<dd> <code>%&lt;</code></p>
<dt>
<dd> stands for the lines from the first file, including the trailing newline. Each line is formatted according to the old line format (see node `Line formats&#8217; in the CVS manual). </p>
<dt>
<dd> <code>%&gt;</code></p>
<dt>
<dd> stands for the lines from the second file, including the trailing newline. Each line is formatted according to the new line format. </p>
<dt>
<dd> <code>%=</code></p>
<dt>
<dd> stands for the lines common to both files, including the trailing newline. Each line is formatted according to the unchanged line format. </p>
<dt>
<dd> <code>%%</code></p>
<dt>
<dd> stands for <code>%</code>. </p>
<dt>
<dd> <code>%c&#8217;</code><i>C</i><code>&#8216;</code></p>
<dt>
<dd> where <i>C</i> is a single character, stands for <i>C</i>. <i>C</i> may not be a backslash or an apostrophe. For example, <code>%c&#8217;:&#8217;</code> stands for a colon, even inside the then-part of an if-then-else format, which a colon would normally terminate. </p>
<dt>
<dd> <code>%c&#8217;\</code><i>O</i><code>&#8216;</code></p>
<dt>
<dd> where <i>O</i> is a string of 1, 2, or 3 octal digits, stands for the character with octal code <i>O</i>. For example, <code>%c&#8217;
