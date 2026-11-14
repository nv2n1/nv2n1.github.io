---
title: "bashdb(1)"
name: "bashdb"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bashdb/"
description: "bashdb – bash debugger script"
---

<h2 class="name">NAME</h2>
<p> bashdb &#8211; bash debugger script </p>
<h2>SYNOPSIS</h2>
<p> <code>bashdb</code> [<i>options</i>] [&#8211;] <i>script-name</i> [<i>script options</i>] </p>
<p> <code>bashdb</code> [<i>options</i>] -c <i>execution-string</i> </p>
<p> <code>bash &#8211;debugger</code> [<i>bash-options</i>&#8230;] <i>script-name</i> [<i>script options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;bashdb&quot;</tt> is a bash script to which arranges for another bash script to be debugged. The debugger has a similar command interface as <tt><a href="/docs/linux/man/1-gdb/">gdb</a>(1)</tt>. </p>
<p> The way this script arranges debugging to occur is by including (or actually &#8220;source&#8221;-ing) some debug-support code and then sourcing the given script or command string. </p>
<p> One problem with sourcing a debugged script is that the program name stored in <tt>$0</tt> will be <tt>&quot;bashdb&quot;</tt> rather than the name of the script to be debugged. The debugged script will appear in a call stack not as the top item but as the item below <tt>&quot;bashdb&quot;</tt>. If this is of concern, use the last form given above, <tt>&quot;bash --debugger&quot;</tt> <i>script-name</i> [<i>script-options</i>]. </p>
<p> If you used bashdb script and need to pass options to the script to be debugged, add <tt>&quot;--&quot;</tt> before the script name. That will tell bashdb not to try to process any further options. </p>
<p> See the reference manual &lt;<a rel="nofollow" href="http://bashdb.sourceforge.net/bashdb.html">http://bashdb.sourceforge.net/bashdb.html</a>&gt; for how to to call the debugger from inside your program or arrange for the debugger to get called when your program is sent a signal.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-h | &#8211;help</p>
<dd> Print a usage message on standard error and exit with a return code of 100. </p>
<dt>-A | &#8211;annotation <i>level</i></p>
<dd> Sets to output additional stack and status information which allows front-ends such as emacs to track what&#8217;s going on without polling. </p>
<p> This is needed in for regression testing. Using this option is equivalent to issuing: </p>
<pre>
  set annotation LEVEL
</pre>
<p> inside the debugger. </p>
<dt>-B | &#8211;basename</p>
<dd> In places where a filename appears in debugger output give just the basename only. This is needed in for regression testing. Using this option is equivalent to issuing: </p>
<pre>
  set basename on
</pre>
<p> inside the debugger. </p>
<dt>-n | nx</p>
<dd> Normally the debugger will read debugger commands in <tt>&quot;~/.bashdbinit&quot;</tt> if that file exists before accepting user interaction. <tt>&quot;.bashdbinit&quot;</tt> is analogus to Perl&#8217;s <tt>&quot;.perldb&quot;</tt> or <font SIZE="-1">GNU</font> gdb&#8217;s <tt>&quot;.gdbinit&quot;</tt>: a user might want to create such a debugger profile to add various user-specific customizations. </p>
<p> Using the <tt>&quot;-n&quot;</tt> option this initialization file will not be read. This is useful in regression testing or in tracking down a problem with one&#8217;s <tt>&quot;.bashdbinit&quot;</tt> profile. </p>
<dt>-c <i>command-string</i></p>
<dd> Instead of specifying the name of a script file, one can give an execution string that is to be debugged. Use this option to do that. </p>
<p> If you invoke the debugger via <tt>&quot;bash --debugger&quot;</tt>, the filename that will appear in source listing or in a call stack trace will be the artifical name *BOGUS*. </p>
<dt>-q | &#8211;quiet</p>
<dd> Do not print introductory version and copyright information. This is again useful in regression testing where we don&#8217;t want to include a changeable copyright date in the regression-test matching. </p>
<dt>-x <i>debugger-cmdfile</i></p>
<dd> Run the debugger commands <i>debugger-cmdfile</i> before accepting user input. These commands are read however after any <tt>&quot;.bashdbinit&quot;</tt> commands. Again this is useful running regression-testing debug scripts. </p>
<dt>-L | &#8211;library <i>debugger-library</i></p>
<dd> The debugger needs to source or include a number of functions and these reside in a library. If this option is not given the default location of library is relative to the installed bashdb script: <tt>&quot;../lib/bashdb&quot;</tt>. </p>
<dt>-T | &#8211;tempdir <i>temporary-file-directory</i></p>
<dd> The debugger needs to make use of some temporary filesystem storage to save persistent information across a subshell return or in order to evaluate an expression. The default directory is <tt>&quot;/tmp&quot;</tt> but you can use this option to set the directory where debugger temporary files will be created. </p>
<dt>-t | &#8211;tty <i>tty-name</i></p>
<dd> Debugger output usually goes to a terminal rather than stdout or stdin which the debugged program may use. Determination of the tty or pseudo-tty is normally done automatically. However if you want to control where the debugger output goes, use this option. </p>
<dt>-V | &#8211;version</p>
<dd> Show version number and no-warranty and exit with return code 1.</p>
<dt>-X | &#8211;trace</p>
<dd> Similar to &quot;<tt>&quot;set -x&quot;</tt>&quot; line tracing except that by default the location of each line, the bash level, and subshell level are printed. You might be able to get something roughly similar if you set <tt>&quot;PS4&quot;</tt> as follows </p>
<pre><code>
export PS4 = '(${BASH_SOURCE}:${LINENO}): ${FUNCNAME[0]}
'
</code></pre>
<p> In contrast however to &quot;<tt>&quot;set -x&quot;</tt>&quot; tracing, indentation of the original program is also preserved in the source output. And if you interrupt the program with a break (a <tt>&quot;SIGINT&quot;</tt> signal), you will go into the debugger (assuming your program doesn&#8217;t trap <tt>&quot;SIGINT&quot;</tt>). </p>
</dl>
<h2>BUGS</h2>
<p> The <tt>&quot;bashdb&quot;</tt> script and <tt>&quot;--debugger&quot;</tt> option assume a version of bash with debugging support. That is you can&#8217;t debug bash scripts using the standard-issue version 2.05b bash or earlier versions. In versions after 3.0, debugging should have been enabled when bash was built. (I think this is usually the case though.) If you try to run the bashdb script on such as shell, may get the message: </p>
<pre>
  Sorry, you need to use a debugger-enabled version of bash.
</pre>
<p> Debugging startup time can be slow especially on large bash scripts. Scripts created by <font SIZE="-1">GNU</font> autoconf are at thousands of lines line and it is not uncommon for them to be tens of thousands of lines. </p>
<p> There is a provision to address this problem by including a fast file-to-array read routine (readarray), but the bashdb package has to be compiled in a special way which needs access to the bash source code and objects. </p>
<p> Another reason of the debugger slowness is that the debugger has to intercept every line and check to see if some action is to be taken for this and this is all in bash code. A better and faster architecture would be for the debugger to register a list of conditions or stopping places inside the bash code itself and have it arrange to call the debugger only when a condition requiring the debugger arises. Checks would be faster as this would be done in C code and access to internal structures would make this more efficient.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>*</p>
<dd> &lt;<a rel="nofollow" href="http://bashdb.sourceforge.net/bashdb.html">http://bashdb.sourceforge.net/bashdb.html</a>&gt; &#8211; an extensive reference manual.</p>
<dt>*</p>
<dd> &lt;<a rel="nofollow" href="http://bashdb.sourceforge.net">http://bashdb.sourceforge.net</a>&gt; &#8211; the homepage for the project</p>
<dt>*</p>
<dd> &lt;<a rel="nofollow" href="http://www.gnu.org/software/bash/manual/bashref.html">http://www.gnu.org/software/bash/manual/bashref.html</a>&gt; &#8211; bash reference manual</dl>
<h2>AUTHOR</h2>
<p> The current version is maintained (or not) by Rocky Bernstein.</p>
<h2>COPYRIGHT</h2>
<pre><code>
Copyright(C) 2003, 2006, 2007 Rocky Bernstein This program is free software;
you can redistribute it and / or modify
                                     it under the terms of the GNU General Public License as published by
                                         the Free Software Foundation;
either version 2 of the License, or
                                     (at your option) any later version.This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  You should have received a copy of the GNU General Public License
  along with this program;
if
not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111 - 1307 USA
</code></pre>
<p> <i></i>$Id:<i> bashdb-man.pod,v 1.10 2009/06/22 22:41:10 rockyb Exp $</i> </p>
<h2>Index</h2>
