---
title: "expect_kibitz(1)"
name: "expect_kibitz"
section: "1"
letter: "e"
url: "/docs/linux/man/1-expect_kibitz/"
description: "kibitz – allow two people to interact with one shell"
---

<h2 class="name">NAME</h2>
<p> kibitz &#8211; allow two people to interact with one shell </p>
<h2>SYNOPSIS</h2>
<p> <code>kibitz</code> [ <i>kibitz-args</i> ] <i>user</i> [ <i>program program-args&#8230;</i> ]<br />
 <code>kibitz</code> [ <i>kibitz-args</i> ] <i>user [at] host</i> [ <i>program program-args&#8230;</i> ]</p>
<h2>INTRODUCTION</h2>
<p> <code>kibitz</code> allows two (or more) people to interact with one shell (or any arbitrary program). Uses include:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A novice user can ask an expert user for help. Using <code>kibitz</code>, the expert can see what the user is doing, and offer advice or show how to do it right.</p>
<dt>&bull;</p>
<dd> By running <code>kibitz</code> and then starting a full-screen editor, people may carry out a conversation, retaining the ability to scroll backwards, save the entire conversation, or even edit it while in progress.</p>
<dt>&bull;</p>
<dd> People can team up on games, document editing, or other cooperative tasks where each person has strengths and weaknesses that complement one another.</dl>
</dl>
<h2>USAGE</h2>
<p> To start <code>kibitz</code>, user1 runs kibitz with the argument of the user to kibitz. For example: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>kibitz user2</p>
<p> <code>kibitz</code> starts a new shell (or another program, if given on the command line), while prompting user2 to run <code>kibitz</code>. If user2 runs <code>kibitz</code> as directed, the keystrokes of both users become the input of the shell. Similarly, both users receive the output from the shell. </p>
<p> To terminate <code>kibitz</code> it suffices to terminate the shell itself. For example, if either user types ^D (and the shell accepts this to be EOF), the shell terminates followed by <code>kibitz</code>. </p>
<p> Normally, all characters are passed uninterpreted. However, if the escape character (described when <code>kibitz</code> starts) is issued, the user may talk directly to the <code>kibitz</code> interpreter. Any <code><a href="/docs/linux/man/1-expect/">Expect</a></code>(1) or <code><a href="/docs/linux/man/3-tcl/">Tcl</a></code>(3) commands may be given. Also, job control may be used while in the interpreter, to, for example, suspend or restart <code>kibitz</code>. </p>
<p> Various processes can provide various effects. For example, you can emulate a two-way <a href="/docs/linux/man/1-write/">write</a>(1) session with the command: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>kibitz user2 sleep 1000000</p>
<h2>ARGUMENTS</h2>
<p> <code>kibitz</code> takes arguments, these should also be separated by whitespace. </p>
<p> The <code>-noproc</code> flag runs <code>kibitz</code> with no process underneath. Characters are passed to the other <code>kibitz</code>. This is particularly useful for connecting multiple interactive processes together. In this mode, characters are not echoed back to the typist. </p>
<p> <code>-noescape</code> disables the escape character. </p>
<p> <code>-escape</code><i> char</i> sets the escape character. The default escape character is ^]. </p>
<p> <code>-silent</code> turns off informational messages describing what kibitz is doing to initiate a connection. </p>
<p> <code>-tty</code><i> ttyname</i> defines the tty to which the invitation should be sent. </p>
<p> If you start <code>kibitz</code> to user2 on a remote computer, <code>kibitz</code> performs a <code>rlogin</code> to the remote computer with your current username. The flag <code>-proxy</code><i> username</i> causes <code>rlogin</code> to use <i>username</i> for the remote login (e.g. if your account on the remote computer has a different username). If the <code>-proxy</code> flag is not given, <code>kibitz</code> tries to determine your current username by (in that order) inspecting the environment variables USER and LOGNAME, then by using the commands <code>whoami</code> and <code>logname</code>. </p>
<p> The arguments <code>-noescape</code> and <code>-escape</code> can also be given by user2 when prompted to run <code>kibitz</code>. </p>
<h2>MORE THAN TWO USERS</h2>
<p> The current implementation of kibitz explicitly understands only two users, however, it is nonetheless possible to have a three (or more) -way kibitz, by kibitzing another <code>kibitz</code>. For example, the following command runs <code>kibitz</code> with the current user, user2, and user3: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>% kibitz user2 kibitz user3</p>
<p> Additional users may be added by simply appending more &quot;kibitz user&quot; commands. </p>
<p> The <code>xkibitz</code> script is similar to <code>kibitz</code> but supports the ability to add additional users (and drop them) dynamically.</p>
<h2>CAVEATS</h2>
<p> <code>kibitz</code> assumes the 2nd user has the same terminal type and size as the 1st user. If this assumption is incorrect, graphical programs may display oddly. </p>
<p> <code>kibitz</code> handles character graphics, but cannot handle bitmapped graphics. Thus, </p>
<pre>
        % xterm -e kibitz    will work
        % kibitz xterm       will not work
</pre>
<p> However, you can get the effect of the latter command by using <code>xkibitz </code> (see SEE ALSO below). <code>kibitz</code> uses the same permissions as used by rlogin, rsh, etc. Thus, you can only <code>kibitz</code> to users at hosts for which you can rlogin. Similarly, <code>kibitz</code> will prompt for a password on the remote host if rlogin would. </p>
<p> If you <code>kibitz</code> to users at remote hosts, <code>kibitz</code> needs to distinguish your prompt from other things that may precede it during login. (Ideally, the end of it is preferred but any part should suffice.) If you have an unusual prompt, set the environment variable EXPECT_PROMPT to an <a href="/docs/linux/man/1-egrep/">egrep</a>(1)-style regular expression. Brackets should be preceded with one backslash in ranges, and three backslashes for literal brackets. The default prompt r.e. is &quot;($|%|#)&nbsp;&quot;. </p>
<p> <code>kibitz</code> requires the <code>kibitz</code> program on both hosts. <code>kibitz</code> requires <code><a href="/docs/linux/man/1-expect/">expect</a></code>(1). </p>
<p> By comparison, the <code>xkibitz</code> script uses the X authorization mechanism for inter-host communication so it does not need to login, recognize your prompt, or require kibitz on the remote host. It does however need permission to access the other X servers.</p>
<h2>BUGS</h2>
<p> An early version of Sun&#8217;s tmpfs had a bug in it that causes <code>kibitz</code> to blow up. If <code>kibitz</code> reports &quot;error flushing &#8230;: Is a directory&quot; ask Sun for patch #100174. </p>
<p> If your Expect is not compiled with multiple-process support (i.e., you do not have a working select or poll), you will not be able to run kibitz.</p>
<h2>ENVIRONMENT</h2>
<p> The environment variable SHELL is used to determine the shell to start, if no other program is given on the command line. </p>
<p> If the environment variable EXPECT_PROMPT exists, it is taken as a regular expression which matches the end of your login prompt (but does not otherwise occur while logging in). See also CAVEATS above. </p>
<p> If the environment variables USER or LOGNAME are defined, they are used to determine the current user name for a <code>kibitz</code> to a remote computer. See description of the <code>-proxy</code> option in ARGUMENTS above.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-tcl/">Tcl</a></code>(3), <code><a href="/docs/linux/man/3-libexpect/">libexpect</a></code>(3), <code><a href="/docs/linux/man/1-xkibitz/">xkibitz</a></code>(1)<br />
 <i>&quot;Exploring Expect: A Tcl-Based Toolkit for Automating Interactive Programs&quot;</i> by Don Libes, O&#8217;Reilly and Associates, January 1995.<br />
 <i>&quot;Kibitz &#8211; Connecting Multiple Interactive Programs Together&quot;, </i>by Don Libes, Software &#8211; Practice &amp; Experience, John Wiley &amp; Sons, West Sussex, England, Vol. 23, No. 5, May, 1993.</p>
<h2>AUTHOR</h2>
<p> Don Libes, National Institute of Standards and Technology </p>
<p> <code>kibitz</code> is in the public domain. NIST and I would appreciate credit if this program or parts of it are used. </p>
<h2>Index</h2>
