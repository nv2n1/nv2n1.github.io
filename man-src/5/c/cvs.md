---
title: "cvs(5)"
name: "cvs"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cvs/"
description: "cvs – Concurrent Versions System support files"
---

<p>cvs &#8211; Concurrent Versions System support files</p>
<h2>Note</h2>
<p>This documentation may no longer be up to date. Please consult the Cederqvist (CVS Manual) as specified in <code>cvs</code>(<code>1</code>).</p>
<h2>Synopsis</h2>
<dl>
<dt><code>$CVSROOT/CVSROOT/commitinfo,v</code></p>
<dd>
<dt><code>$CVSROOT/CVSROOT/cvsignore,v</code></p>
<dd>
<dt><code>$CVSROOT/CVSROOT/cvswrappers,v</code></p>
<dd>
<dt><code>$CVSROOT/CVSROOT/editinfo,v</code></p>
<dd>
<dt><code>$CVSROOT/CVSROOT/history</code></p>
<dd>
<dt><code>$CVSROOT/CVSROOT/loginfo,v</code></p>
<dd>
<dt><code>$CVSROOT/CVSROOT/modules,v</code></p>
<dd>
<dt><code>$CVSROOT/CVSROOT/rcsinfo,v</code></p>
<dd>
<dt><code>$CVSROOT/CVSROOT/taginfo,v</code></p>
<dd></dl>
<h2>Description</h2>
<p><code>cvs</code> is a system for providing source control to hierarchical collections of source directories. Commands and procedures for using <code>cvs</code> are described in <code>cvs</code>(<code>1</code>). </p>
<p> <code>cvs</code> manages <i>source repositories</i>, the directories containing master copies of the revision-controlled files, by copying particular revisions of the files to (and modifications back from) developers&#8217; private <i>working directories</i>. In terms of file structure, each individual source repository is an immediate subdirectory of <code>$CVSROOT</code>. </p>
<p> The files described here are supporting files; they do not have to exist for <code>cvs</code> to operate, but they allow you to make <code>cvs</code> operation more flexible. </p>
<p> You can use the `modules&#8217; file to define symbolic names for collections of source maintained with <code>cvs</code>. If there is no `modules&#8217; file, developers must specify complete path names (absolute, or relative to <code>$CVSROOT</code>) for the files they wish to manage with <code>cvs</code> commands. </p>
<p> You can use the `commitinfo&#8217; file to define programs to execute whenever `<code>cvs commit</code>&#8216; is about to execute. These programs are used for &#8220;pre-commit&#8221; checking to verify that the modified, added, and removed files are really ready to be committed. Some uses for this check might be to turn off a portion (or all) of the source repository from a particular person or group. Or, perhaps, to verify that the changed files conform to the site&#8217;s standards for coding practice. </p>
<p> You can use the `cvswrappers&#8217; file to record <code>cvs</code> wrapper commands to be used when checking files into and out of the repository. Wrappers allow the file or directory to be processed on the way in and out of CVS. The intended uses are many, one possible use would be to reformat a C file before the file is checked in, so all of the code in the repository looks the same. </p>
<p> You can use the `loginfo&#8217; file to define programs to execute after any <code>commit</code>, which writes a log entry for changes in the repository. These logging programs might be used to append the log message to a file. Or send the log message through electronic mail to a group of developers. Or, perhaps, post the log message to a particular newsgroup. </p>
<p> You can use the `taginfo&#8217; file to define programs to execute after any <code>tag</code>or<code>rtag</code> operation. These programs might be used to append a message to a file listing the new tag name and the programmer who created it, or send mail to a group of developers, or, perhaps, post a message to a particular newsgroup. </p>
<p> You can use the `rcsinfo&#8217; file to define forms for log messages. </p>
<p> You can use the `editinfo&#8217; file to define a program to execute for editing/validating `<code>cvs commit</code>&#8216; log entries. This is most useful when used with a `rcsinfo&#8217; forms specification, as it can verify that the proper fields of the form have been filled in by the user committing the change. </p>
<p> You can use the `cvsignore&#8217; file to specify the default list of files to ignore during <code>update</code>. </p>
<p> You can use the `history&#8217; file to record the <code>cvs</code> commands that affect the repository. The creation of this file enables history logging.</p>
<h2>Files</h2>
<dl>
<dt><code>modules</code></p>
<dd>The `modules&#8217; file records your definitions of names for collections of source code. <code>cvs</code> will use these definitions if you use <code>cvs</code> to check in a file with the right format to `<code>$CVSROOT/CVSROOT/modules,v</code>&#8216;. </p>
<p> The `modules&#8217; file may contain blank lines and comments (lines beginning with `<code>#</code>&#8216;) as well as module definitions. Long lines can be continued on the next line by specifying a backslash (&#8220;\&#8221;) as the last character on the line. </p>
<p> A <i>module definition</i> is a single line of the `modules&#8217; file, in either of two formats. In both cases, <i>mname</i> represents the symbolic module name, and the remainder of the line is its definition. </p>
<p> <i>mname</i> <code>-a</code> <i>aliases</i>&#8230;<br />
 This represents the simplest way of defining a module <i>mname</i>. The `<code>-a</code>&#8216; flags the definition as a simple alias: <code>cvs</code> will treat any use of <i>mname</i> (as a command argument) as if the list of names <i>aliases</i> had been specified instead. <i>aliases</i> may contain either other module names or paths. When you use paths in <i>aliases</i>, `<code>cvs checkout</code>&#8216; creates all intermediate directories in the working directory, just as if the path had been specified explicitly in the <code>cvs</code> arguments. </p>
<pre><i>mname</i> [ <i>options</i> ] <i>dir</i> [ <i>files</i>... ] [ <code>&amp;</code><i>module</i>... ]</pre>
<p>In the simplest case, this form of module definition reduces to `<i>mname dir</i>&#8216;. This defines all the files in directory <i>dir</i> as module <i>mname</i>. <i>dir</i> is a relative path (from <code>$CVSROOT</code>) to a directory of source in one of the source repositories. In this case, on <code>checkout</code>, a single directory called <i>mname</i> is created as a working directory; no intermediate directory levels are used by default, even if <i>dir</i> was a path involving several directory levels. </p>
<p> By explicitly specifying <i>files</i> in the module definition after <i>dir</i>, you can select particular files from directory <i>dir</i>. The sample definition for <code>modules</code> is an example of a module defined with a single file from a particular directory. Here is another example: </p>
<pre><code>m4test unsupported/gnu/m4 foreach.m4 forloop.m4
</code></pre>
<p>With this definition, executing `<code>cvs checkout m4test</code>&#8216; will create a single working directory `m4test&#8217; containing the two files listed, which both come from a common directory several levels deep in the <code>cvs</code> source repository. </p>
<p> A module definition can refer to other modules by including `<code>&amp;</code><i>module</i>&#8216; in its definition. <code>checkout</code> creates a subdirectory for each such <i>module</i>, in your working directory.<br />
 <i>New in </i><code>cvs</code> 1.3; avoid this feature if sharing module definitions with older versions of <code>cvs</code>. </p>
<p> Finally, you can use one or more of the following <i>options</i> in module definitions: </p>
<p> `<code>-d</code> <i>name</i>&#8216;, to name the working directory something other than the module name.<br />
 <i>New in </i><code>cvs</code> 1.3; avoid this feature if sharing module definitions with older versions of <code>cvs</code>. </p>
<p> `<code>-i</code> <i>prog</i>&#8216; allows you to specify a program <i>prog</i> to run whenever files in a module are committed. <i>prog</i> runs with a single argument, the full pathname of the affected directory in a source repository. The `commitinfo&#8217;, `loginfo&#8217;, and `editinfo&#8217; files provide other ways to call a program on <code>commit</code>. </p>
<p> `<code>-o</code> <i>prog</i>&#8216; allows you to specify a program <i>prog</i> to run whenever files in a module are checked out. <i>prog</i> runs with a single argument, the module name. </p>
<p> `<code>-e</code> <i>prog</i>&#8216; allows you to specify a program <i>prog</i> to run whenever files in a module are exported. <i>prog</i> runs with a single argument, the module name. </p>
<p> `<code>-t</code> <i>prog</i>&#8216; allows you to specify a program <i>prog</i> to run whenever files in a module are tagged. <i>prog</i> runs with two arguments: the module name and the symbolic tag specified to <code>rtag</code>. </p>
<p> `<code>-u</code> <i>prog</i>&#8216; allows you to specify a program <i>prog</i> to run whenever `<code>cvs update</code>&#8216; is executed from the top-level directory of the checked-out module. <i>prog</i> runs with a single argument, the full path to the source repository for this module.</p>
<dt><code>commitinfo</code>, <code>loginfo</code>, <code>rcsinfo</code>, <code>editinfo</code></p>
<dd>These files all specify programs to call at different points in the `<code>cvs commit</code>&#8216; process. They have a common structure. Each line is a pair of fields: a regular expression, separated by whitespace from a filename or command-line template. Whenever one of the regular expression matches a directory name in the repository, the rest of the line is used. If the line begins with a <code>#</code> character, the entire line is considered a comment and is ignored. Whitespace between the fields is also ignored. </p>
<p> For `loginfo&#8217;, the rest of the line is a command-line template to execute. The templates can include not only a program name, but whatever list of arguments you wish. If you write `<code>%s</code>&#8216; somewhere on the argument list, <code>cvs</code> supplies, at that point, the list of files affected by the <code>commit</code>. The first entry in the list is the relative path within the source repository where the change is being made. The remaining arguments list the files that are being modified, added, or removed by this <code>commit</code> invocation. </p>
<p> For `taginfo&#8217;, the rest of the line is a command-line template to execute. The arguments passed to the command are, in order, the <i>tagname ,</i> <i>operation</i> (i.e. <code>add</code> for `tag&#8217;, <code>mov</code> for `tag -F&#8217;, and <code>del</code> for `tag -d`), <i>repository ,</i> and any remaining are pairs of <code>filename revision .</code> A non-zero exit of the filter program will cause the tag to be aborted. </p>
<p> For `commitinfo&#8217;, the rest of the line is a command-line template to execute. The template can include not only a program name, but whatever list of arguments you wish. The full path to the current source repository is appended to the template, followed by the file names of any files involved in the commit (added, removed, and modified files). </p>
<p> For `rcsinfo&#8217;, the rest of the line is the full path to a file that should be loaded into the log message template. </p>
<p> For `editinfo&#8217;, the rest of the line is a command-line template to execute. The template can include not only a program name, but whatever list of arguments you wish. The full path to the current log message template file is appended to the template. </p>
<p> You can use one of two special strings instead of a regular expression: `<code>ALL</code>&#8216; specifies a command line template that must always be executed, and `<code>DEFAULT</code>&#8216; specifies a command line template to use if no regular expression is a match. </p>
<p> The `commitinfo&#8217; file contains commands to execute <i>before</i> any other <code>commit</code> activity, to allow you to check any conditions that must be satisfied before <code>commit</code> can proceed. The rest of the <code>commit</code> will execute only if all selected commands from this file exit with exit status <code>0</code>. </p>
<p> The `rcsinfo&#8217; file allows you to specify <i>log templates</i> for the <code>commit</code> logging session; you can use this to provide a form to edit when filling out the <code>commit</code> log. The field after the regular expression, in this file, contains filenames (of files containing the logging forms) rather than command templates. </p>
<p> The `editinfo&#8217; file allows you to execute a script <i>before the commit starts</i>, but after the log information is recorded. These &quot;edit&quot; scripts can verify information recorded in the log file. If the edit script exits with a non-zero exit status, the commit is aborted. </p>
<p> The `loginfo&#8217; file contains commands to execute <i>at the end</i> of a commit. The text specified as a commit log message is piped through the command; typical uses include sending mail, filing an article in a newsgroup, or appending to a central file.</p>
<dt><code>cvsignore</code>, <code>.cvsignore</code></p>
<dd>The default list of files (or <code>sh</code>(<code>1</code>) file name patterns) to ignore during `<code>cvs update</code>&#8216;. At startup time, <code>cvs</code> loads the compiled in default list of file name patterns (see <code>cvs</code>(<code>1</code>)). Then the per-repository list included in <code>$CVSROOT/CVSROOT/cvsignore</code> is loaded, if it exists. Then the per-user list is loaded from `$HOME/.cvsignore&#8217;. Finally, as <code>cvs</code> traverses through your directories, it will load any per-directory `.cvsignore&#8217; files whenever it finds one. These per-directory files are only valid for exactly the directory that contains them, not for any sub-directories.</p>
<dt><code>history</code></p>
<dd>Create this file in <code>$CVSROOT/CVSROOT</code> to enable history logging (see the description of `<code>cvs history</code>&#8216;).</dl>
<h2>See Also</h2>
<p><code>cvs</code>(<code>1</code>),</p>
<h2>Copying</h2>
<p>Copyright &#169; 1992 Cygnus Support, Brian Berliner, and Jeff Polk </p>
<p> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual into another language, under the above conditions for modified versions, except that this permission notice may be included in translations approved by the Free Software Foundation instead of in the original English.</p>
