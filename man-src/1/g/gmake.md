---
title: "gmake(1)"
name: "gmake"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmake/"
description: "make – GNU make utility to maintain groups of programs"
---

<h2 class="name">NAME</h2>
<p> make &#8211; GNU make utility to maintain groups of programs </p>
<h2>SYNOPSIS</h2>
<p> <code>make</code> [<i>OPTION</i>]&#8230; [<i>TARGET</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <i>make</i> utility will determine automatically which pieces of a large program need to be recompiled, and issue the commands to recompile them. The manual describes the GNU implementation of <code>make</code>, which was written by Richard Stallman and Roland McGrath, and is currently maintained by Paul Smith. Our examples show C programs, since they are very common, but you can use <code>make</code> with any programming language whose compiler can be run with a shell command. In fact, <code>make</code> is not limited to programs. You can use it to describe any task where some files must be updated automatically from others whenever the others change. </p>
<p> To prepare to use <code>make</code>, you must write a file called the <i>makefile</i> that describes the relationships among files in your program, and the states the commands for updating each file. In a program, typically the executable file is updated from object files, which are in turn made by compiling source files. </p>
<p> Once a suitable makefile exists, each time you change some source files, this simple shell command: </p>
<dl>
<dt>
<dd> <code>make</code></dl>
<p> suffices to perform all necessary recompilations. The <code>make</code> program uses the makefile description and the last-modification times of the files to decide which of the files need to be updated. For each of those files, it issues the commands recorded in the makefile. </p>
<p> <code>make</code> executes commands in the <i>makefile</i> to update one or more target <i>names</i>, where <i>name</i> is typically a program. If no <code>-f</code> option is present, <code>make</code> will look for the makefiles <i>GNUmakefile</i>, <i>makefile</i>, and <i>Makefile</i>, in that order. </p>
<p> Normally you should call your makefile either <i>makefile</i> or <i>Makefile</i>. (We recommend <i>Makefile</i> because it appears prominently near the beginning of a directory listing, right near other important files such as <i>README</i>.) The first name checked, <i>GNUmakefile</i>, is not recommended for most makefiles. You should use this name if you have a makefile that is specific to GNU <code>make</code>, and will not be understood by other versions of <code>make</code>. If <i>makefile</i> is &#8216;-&#8216;, the standard input is read. </p>
<p> <code>make</code> updates a target if it depends on prerequisite files that have been modified since the target was last modified, or if the target does not exist.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code>, <code>-m</code></p>
<dd> These options are ignored for compatibility with other versions of <code>make</code>.</p>
<dt><code>-B</code>, <code>&#8211;always-make</code></p>
<dd> Unconditionally make all targets.</p>
<dt><code>-C</code> <i>dir</i>, <code>&#8211;directory</code>=<i>dir</i></p>
<dd> Change to directory <i>dir</i> before reading the makefiles or doing anything else. If multiple <code>-C</code> options are specified, each is interpreted relative to the previous one: <code>-C </code>/ <code>-C </code>etc is equivalent to <code>-C </code>/etc. This is typically used with recursive invocations of <code>make</code>.</p>
<dt><code>-d</code></p>
<dd> Print debugging information in addition to normal processing. The debugging information says which files are being considered for remaking, which file-times are being compared and with what results, which files actually need to be remade, which implicit rules are considered and which are applied&#8212;everything interesting about how <code>make</code> decides what to do.</p>
<dt><code>&#8211;debug</code><i>[=FLAGS]</i></p>
<dd> Print debugging information in addition to normal processing. If the <i>FLAGS</i> are omitted, then the behavior is the same as if <code>-d</code> was specified. <i>FLAGS</i> may be <i>a</i> for all debugging output (same as using <code>-d</code>), <i>b</i> for basic debugging, <i>v</i> for more verbose basic debugging, <i>i</i> for showing implicit rules, <i>j</i> for details on invocation of commands, and <i>m</i> for debugging while remaking makefiles. Use <i>n</i> to disable all previous debugging flags.</p>
<dt><code>-e</code>, <code>&#8211;environment-overrides</code></p>
<dd> Give variables taken from the environment precedence over variables from makefiles.</p>
<dt><code>-f</code> <i>file</i>, <code>&#8211;file</code>=<i>file</i>, <code>&#8211;makefile</code>=<i>FILE</i></p>
<dd> Use <i>file</i> as a makefile.</p>
<dt><code>-i</code>, <code>&#8211;ignore-errors</code></p>
<dd> Ignore all errors in commands executed to remake files.</p>
<dt><code>-I</code> <i>dir</i>, <code>&#8211;include-dir</code>=<i>dir</i></p>
<dd> Specifies a directory <i>dir</i> to search for included makefiles. If several <code>-I</code> options are used to specify several directories, the directories are searched in the order specified. Unlike the arguments to other flags of <code>make</code>, directories given with <code>-I</code> flags may come directly after the flag: <code>-I</code><i>dir</i> is allowed, as well as <code>-I</code> <i>dir</i>. This syntax is allowed for compatibility with the C preprocessor&#8217;s <code>-I</code> flag.</p>
<dt><code>-j</code> [<i>jobs</i>], <code>&#8211;jobs</code>[=<i>jobs</i>]</p>
<dd> Specifies the number of <i>jobs</i> (commands) to run simultaneously. If there is more than one <code>-j</code> option, the last one is effective. If the <code>-j</code> option is given without an argument, <code>make</code> will not limit the number of jobs that can run simultaneously. When <code>make</code> invokes a <code>sub-make,</code> all instances of make will coordinate to run the specified number of jobs at a time; see the section <code>PARALLEL MAKE AND THE JOBSERVER</code> for details.</p>
<dt><code>&#8211;jobserver-fds</code> [<i>R,W</i>]</p>
<dd> Internal option <code>make</code> uses to pass the jobserver pipe read and write file descriptor numbers to <code>sub-makes;</code> see the section <code>PARALLEL MAKE AND THE JOBSERVER</code> for details</p>
<dt><code>-k</code>, <code>&#8211;keep-going</code></p>
<dd> Continue as much as possible after an error. While the target that failed, and those that depend on it, cannot be remade, the other dependencies of these targets can be processed all the same.</p>
<dt><code>-l</code> [<i>load</i>], <code>&#8211;load-average</code>[=<i>load</i>]</p>
<dd> Specifies that no new jobs (commands) should be started if there are others jobs running and the load average is at least <i>load</i> (a floating-point number). With no argument, removes a previous load limit.</p>
<dt><code>-L</code>, <code>&#8211;check-symlink-times</code></p>
<dd> Use the latest mtime between symlinks and target.</p>
<dt><code>-n</code>, <code>&#8211;just-print</code>, <code>&#8211;dry-run</code>, <code>&#8211;recon</code></p>
<dd> Print the commands that would be executed, but do not execute them (except in certain circumstances).</p>
<dt><code>-o</code> <i>file</i>, <code>&#8211;old-file</code>=<i>file</i>, <code>&#8211;assume-old</code>=<i>file</i></p>
<dd> Do not remake the file <i>file</i> even if it is older than its dependencies, and do not remake anything on account of changes in <i>file</i>. Essentially the file is treated as very old and its rules are ignored.</p>
<dt><code>-O</code>[<i>type</i>], <code>&#8211;output-sync</code>[=<i>type</i>]</p>
<dd> When running multiple jobs in parallel with <code>-j</code>, ensure the output of each job is collected together rather than interspersed with output from other jobs. If <i>type</i> is not specified or is <code>target</code> the output from the entire recipe for each target is grouped together. If <i>type</i> is <code>line</code> the output from each command line within a recipe is grouped together. If <i>type</i> is <code>recurse</code> output from an entire recursive make is grouped together. If <i>type</i> is <code>none</code> output synchronization is disabled.</p>
<dt><code>-p</code>, <code>&#8211;print-data-base</code></p>
<dd> Print the data base (rules and variable values) that results from reading the makefiles; then execute as usual or as otherwise specified. This also prints the version information given by the <code>-v</code> switch (see below). To print the data base without trying to remake any files, use <i>make -p -f/dev/null</i>.</p>
<dt><code>-q</code>, <code>&#8211;question</code></p>
<dd> &#8220;Question mode&#8221;. Do not run any commands, or print anything; just return an exit status that is zero if the specified targets are already up to date, nonzero otherwise.</p>
<dt><code>-r</code>, <code>&#8211;no-builtin-rules</code></p>
<dd> Eliminate use of the built-in implicit rules. Also clear out the default list of suffixes for suffix rules.</p>
<dt><code>-R</code>, <code>&#8211;no-builtin-variables</code></p>
<dd> Don&#8217;t define any built-in variables.</p>
<dt><code>-s</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd> Silent operation; do not print the commands as they are executed.</p>
<dt><code>-S</code>, <code>&#8211;no-keep-going</code>, <code>&#8211;stop</code></p>
<dd> Cancel the effect of the <code>-k</code> option. This is never necessary except in a recursive <code>make</code> where <code>-k</code> might be inherited from the top-level <code>make</code> via MAKEFLAGS or if you set <code>-k</code> in MAKEFLAGS in your environment.</p>
<dt><code>-t</code>, <code>&#8211;touch</code></p>
<dd> Touch files (mark them up to date without really changing them) instead of running their commands. This is used to pretend that the commands were done, in order to fool future invocations of <code>make</code>.</p>
<dt><code>&#8211;trace</code></p>
<dd> Information about the disposition of each target is printed (why the target is being rebuilt and what commands are run to rebuild it).</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print the version of the <code>make</code> program plus a copyright, a list of authors and a notice that there is no warranty.</p>
<dt><code>-w</code>, <code>&#8211;print-directory</code></p>
<dd> Print a message containing the working directory before and after other processing. This may be useful for tracking down errors from complicated nests of recursive <code>make</code> commands.</p>
<dt><code>&#8211;no-print-directory</code></p>
<dd> Turn off <code>-w</code>, even if it was turned on implicitly.</p>
<dt><code>-W</code> <i>file</i>, <code>&#8211;what-if</code>=<i>file</i>, <code>&#8211;new-file</code>=<i>file</i>, <code>&#8211;assume-new</code>=<i>file</i></p>
<dd> Pretend that the target <i>file</i> has just been modified. When used with the <code>-n</code> flag, this shows you what would happen if you were to modify that file. Without <code>-n</code>, it is almost the same as running a <i>touch</i> command on the given file before running <code>make</code>, except that the modification time is changed only in the imagination of <code>make</code>.</p>
<dt><code>&#8211;warn-undefined-variables</code></p>
<dd> Warn when an undefined variable is referenced.</dl>
<h2>EXIT STATUS</h2>
<p> GNU <code>make</code> exits with a status of zero if all makefiles were successfully parsed and no targets that were built failed. A status of one will be returned if the <code>-q</code> flag was used and <code>make</code> determines that a target needs to be rebuilt. A status of two will be returned if any errors were encountered.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>make</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>make</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info make</code></dl>
<p> should give you access to the complete manual. Additionally, the manual is also available online at <i><a rel="nofollow" href="https://www.gnu.org/software/make/manual/html_node/index.html">https://www.gnu.org/software/make/manual/html_node/index.html</a></i></p>
<h2>PARALLEL MAKE AND THE JOBSERVER</h2>
<p> Using the <i>-j</i> option, the user can instruct <code>make</code> to execute tasks in parallel. By specifying a numeric argument to <i>-j</i> the user may specify an upper limit of the number of parallel tasks to be run. </p>
<p> When the build environment is such that a top level <code>make</code> invokes <code>sub-makes</code> (for instance, a style in which each sub-directory contains its own <i>Makefile</i> ), no individual instance of <code>make</code> knows how many tasks are running in parallel, so keeping the number of tasks under the upper limit would be impossible without communication between all the <code>make</code> instances running. While solutions like having the top level <code>make</code> serve as a central controller are feasible, or using other synchronization mechanisms like shared memory or sockets can be created, the current implementation uses a simple shared pipe. </p>
<p> This pipe is created by the top-level <code>make</code> process, and passed on to all the <code>sub-makes.</code> The top level <code>make</code>process<code>writes</code> <code>N-1</code> one-byte tokens into the pipe (The top level <code>make</code> is assumed to reserve one token for itself). Whenever any of the <code>make</code> processes (including the top-level <code>make</code> ) needs to run a new task, it reads a byte from the shared pipe. If there are no tokens left, it must wait for a token to be written back to the pipe. Once the task is completed, the <code>make</code> process writes a token back to the pipe (and thus, if the tokens had been exhausted, unblocking the first <code>make</code> process that was waiting to read a token). Since only <code>N-1</code> tokens were written into the pipe, no more than <code>N</code> tasks can be running at any given time. </p>
<p> If the job to be run is not a <code>sub-make</code> then <code>make</code> will close the jobserver pipe file descriptors before invoking the commands, so that the command can not interfere with the <i>jobserver,</i> and the command does not find any unusual file descriptors.</p>
<h2>BUGS</h2>
<p> See the chapter &#8220;Problems and Bugs&#8221; in <i>The GNU Make Manual</i>.</p>
<h2>AUTHOR</h2>
<p> This manual page contributed by Dennis Morse of Stanford University. Further updates contributed by Mike Frysinger. It has been reworked by Roland McGrath. Maintained by Paul Smith.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1992-1993, 1996-2016 Free Software Foundation, Inc. This file is part of <i>GNU make</i>. </p>
<p> GNU Make is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> GNU Make is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program. If not, see <i><a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a></i>. </p>
<h2>Index</h2>
