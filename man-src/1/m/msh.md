---
title: "msh(1)"
name: "msh"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msh/"
description: "msh – nmh shell (and BBoard reader)"
---

<h2 class="name">NAME</h2>
<p> msh &#8211; nmh shell (and BBoard reader) </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>msh</code> [<code>-prompt</code> <i>string</i>] [<code>-scan</code> | <code>-noscan</code>] [<code>-topcur</code> | <code>-notopcur</code>] [<i>file</i>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>STATUS</h2>
<p> <code>msh is deprecated and will be removed from the next nmh release.</code></p>
<h2>DESCRIPTION</h2>
<p> <code>msh</code></p>
<dd>is an interactive program that implements a subset of the normal <code>nmh</code> commands operating on a single file in <code>mmdf</code> format. That is, <code>msh</code> is used to read a file that contains a number of messages, as opposed to the standard <code>nmh</code> style of reading a number of files, each file being a separate message in a folder. <code>msh</code>&#8216;s chief advantage is that the normal <code>nmh</code> style does not allow a file to have more than one message in it. Hence, <code>msh</code> is ideal for reading BBoards, as these files are delivered by the transport system in this format. In addition, <code>msh</code> can be used on other files, such as message archives which have been <code>pack</code>ed (see <i><a href="/docs/linux/man/1-packf/">packf</a></i>(1)). Finally, <code>msh</code> is an excellent <code>nmh</code> tutor. As the only commands available to the user are <code>nmh</code> commands, this allows <code>nmh</code> beginners to concentrate on how commands to <code>nmh</code> are formed and (more or less) what they mean. </p>
<p> When invoked, <code>msh</code> reads the named file, and enters a command loop. The user may type most of the normal <code>nmh</code> commands. The syntax and semantics of these commands typed to <code>msh</code> are identical to their <code>nmh</code> counterparts. In cases where the nature of <code>msh</code> would be inconsistent (e.g., specifying a <i>+folder</i> with some commands), <code>msh</code> will duly inform the user. The commands that <code>msh</code> currently supports (in some slightly modified or restricted forms) are: </p>
<dl>
<dt>
<dd>
<pre>
ali
burst
comp
dist
folder
forw
inc
mark
mhmail
mhn
msgchk
next
packf
pick
prev
refile
repl
rmm
scan
send
show
sortm
whatnow
whom
</pre>
</dl>
<p> In addition, <code>msh</code> has a <code>help</code> command which gives a brief overview. To terminate <code>msh</code>, type CTRL-D, or use the <code>quit</code> command. </p>
<p> If the file is writable and has been modified, then using <code>quit</code> will query the user if the file should be updated. </p>
<p> The <code>-prompt</code> <i>string</i> switch sets the prompting string for <code>msh</code>. </p>
<p> You may wish to use an alternate <code>nmh</code> profile for the commands that <code>msh</code> executes; see <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5) for details about the <code>$MH</code> environment variable. </p>
<p> The <code>exit</code> command is identical to the <code>quit</code> command in <code>msh</code>. </p>
<p> <code>msh</code> supports an output redirection facility. Commands may be followed by one of </p>
<dl>
<dt>
<dd>
<pre>
^&gt; <i>file</i>~^write output to <i>file</i>
^&gt;&gt; <i>file</i>~^append output to <i>file</i>
^| <i>command</i>~^pipe output to UNIX <i>command</i>
</pre>
</dl>
<p> If <i>file</i> starts with a &#8220;~&#8221; (tilde), then a <code>csh</code>-like expansion takes place. Note that <i>command</i> is interpreted by <code>sh</code>. Also note that <code>msh</code> does NOT support history substitutions, variable substitutions, or alias substitutions. </p>
<p> When parsing commands to the left of any redirection symbol, <code>msh</code> will honor `\&#8217; (backslash) as the quote next-character symbol, and &#8220;`&#8217; (double-quote) as quote-word delimiters. All other input tokens are separated by whitespace (spaces and tabs).</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
^/etc/nmh/mts.conf~^nmh mts configuration file
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Msg-Protect:~^To set mode when creating a new `file'
^fileproc:~^Program to file messages
^showproc:~^Program to show messages
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-packf/">packf</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>file</code>' defaults to ``./msgbox''
`<code>-prompt&nbsp;<wbr>(msh)&nbsp;<wbr>'</code>
`<code>-noscan</code>'
`<code>-notopcur</code>'
</pre>
<h2>CONTEXT</h2>
<p> None</p>
<h2>BUGS</h2>
<p> There is a strict limit of messages per file in <code>packf</code>&#8216;d format which <code>msh</code> can handle. Usually, this limit is 1000 messages. </p>
<p> Please remember that <code>msh</code> is not the C-Shell, and that a lot of the nice facilities provided by the latter are not present in the former. </p>
<p> In particular, <code>msh</code> does not understand backquoting, so the only effective way to use <code>pick</code> inside <code>msh</code> is to always use the <code>-seq</code> <i>select</i> switch. Clever users of <code>nmh</code> will put the line </p>
<dl>
<dt>
<dd> pick: -seq select -list</dl>
<p> in their <i>.mh_profile</i> file so that <code>pick</code> works equally well from both the shell and <code>msh</code>. </p>
<p> <code>sortm</code> always uses <code>-noverbose</code> and if <code>-textfield</code> <i>field</i> is used, <code>-limit</code> <i>0</i>. </p>
<p> The <code>msh</code> program inherits most (if not all) of the bugs from the <code>nmh</code> commands it implements. </p>
<h2>Index</h2>
