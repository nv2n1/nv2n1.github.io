---
title: "nmh(1)"
name: "nmh"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nmh/"
description: "nmh – new MH message system"
---

<h2>NAME</h2>
<p> nmh &#8211; new MH message system</p>
<h2>SYNOPSIS</h2>
<p> any <code>nmh</code> command</p>
<h2>DESCRIPTION</h2>
<p> <code>nmh</code> is the name of a powerful message handling system. Rather than being a single comprehensive program, <code>nmh</code> consists of a collection of fairly simple single-purpose programs to send, retrieve, save, and manipulate messages. </p>
<p> Unlike most mail clients in UNIX, <code>nmh</code> is not a closed system which must be explicitly run, then exited when you wish to return to the shell. You may freely intersperse <code>nmh</code> commands with other shell commands, allowing you to read and answer your mail while you have (for example) a compilation running, or search for a file or run programs as needed to find the answer to someone&#8217;s question before answering their mail. </p>
<p> The rest of this manual entry is a quick tutorial which will teach you the basics of <code>nmh</code>. You should read the manual entries for the individual programs for complete documentation. </p>
<p> To get started using <code>nmh</code>, put the directory <i>/usr/bin</i> on your <code>$PATH</code>. This is best done in one of the files: <i>.profile</i>, <i>.login</i>, <i>.bashrc</i>, or <i>.cshrc</i> in your home directory. (Check the manual entry for the shell you use, in case you don&#8217;t know how to do this.) Run the <code>install-mh</code> command. If you&#8217;ve never used <code>nmh</code> before, it will create the necessary default files and directories after asking you if you wish it to do so. </p>
<p> <code>inc</code> moves mail from your system maildrop into your <code>nmh</code> `+inbox&#8217; folder, breaking it up into separate files and converting it to <code>nmh</code> format as it goes. It prints one line for each message it processes, containing the from field, the subject field and as much of the first line of the message as will fit. It leaves the first message it processes as your current message. You&#8217;ll need to run <code>inc</code> each time you wish to incorporate new mail into your <code>nmh</code> file. </p>
<p> <code>scan</code> <code>prints a list of the messages in your current folder.</code> </p>
<p> The commands: <code>show</code>, <code>next</code>, and <code>prev</code> are used to read specific messages from the current folder. <code>show</code> displays the current message, or a specific message, which may be specified by its number, which you pass as an argument to <code>show</code>. <code>next</code> and <code>prev</code> display, respectively, the message numerically after or before the current message. In all cases, the message displayed becomes the current message. If there is no current message, <code>show</code> may be called with an argument, or <code>next</code> may be used to advance to the first message. </p>
<p> <code>rmm</code> (remove message) deletes the current message. It may be called with message numbers passed as arguments, to delete specific messages. </p>
<p> <code>repl</code> is used to respond to the current message (by default). It places you in the editor with a prototype response form. While you&#8217;re in the editor, you may peruse the item you&#8217;re responding to by reading the file <i>@</i>. After completing your response, type <code>l</code> to <code>list</code> (review) it, or <code>s</code> to <code>send</code> it. </p>
<p> <code>comp</code> allows you to compose a message by putting you in the editor on a prototype message form, and then lets you send it. </p>
<p> All the <code>nmh</code> commands may be run with the single argument: <code>-help</code>, which causes them to print a list of the arguments they may be invoked with and then exit. </p>
<p> All the <code>nmh</code> commands may be run with the single argument: <code>-version</code>, which cause them to print the version number of the <code>nmh</code> distribution, and then exit. </p>
<p> Commands which take a message number as an argument ( <code>scan</code>, <code>show</code>, <code>repl</code>, &#8230;) also take one of the words: &#8220;first&#8221;, &#8220;prev&#8221;, &#8220;cur&#8221;, &#8220;next&#8221;, or &#8220;last&#8221; to indicate (respectively) the first, previous, current, next, or last message in the current folder (assuming they are defined). </p>
<p> Commands which take a range of message numbers ( <code>rmm</code>, <code>scan</code>, <code>show</code>, &#8230;) also take any of the abbreviations: </p>
<dl>
<dt>
<dd>
<dl>
<dt><i>&lt;num1&gt;</i>&#8211;<i>&lt;num2&gt;</i></p>
<dd> Indicates all messages in the range &lt;num1&gt; to &lt;num2&gt;, inclusive. The range must be nonempty.</p>
<dt><i>&lt;num&gt;</i>:+<i>N</i></p>
<dd>
<dt><i>&lt;num&gt;</i>:-<i>N</i></p>
<dd> Up to <i>N</i> messages beginning with (or ending with) message <i>num</i>. <i>Num</i> may be any of the pre-defined symbols: <i>first</i>, <i>prev</i>, <i>cur</i>, <i>next</i> or <i>last</i>.</p>
<dt>first:<i>N</i></p>
<dd>
<dt>prev:<i>N</i></p>
<dd>
<dt>next:<i>N</i></p>
<dd>
<dt>last:<i>N</i></p>
<dd> The first, previous, next or last messages, if they exist.</dl>
</dl>
<p> There are many other possibilities such as creating multiple folders for different topics, and automatically refiling messages according to subject, source, destination, or content. These are beyond the scope of this manual entry. </p>
<p> Following is a list of all the <code>nmh</code> commands: </p>
<dl>
<dt>
<dd>
<pre><code>
^ali(1)~^- list mail aliases
^anno(1)~^- annotate messages
^burst(1)~^- explode digests into messages
^comp(1)~^- compose a message 
^dist(1)~^- redistribute a message to additional addresses
^flist(1)~^- list folders with messages in given sequence(s)
^flists(1)~^- list all folders with messages in given sequence(s)
^folder(1)~^- set/list current folder/message
^folders(1)~^- list all folders
^forw(1)~^- forward messages
^inc(1)~^- incorporate new mail
^mark(1)~^- mark messages
^mhbuild(1)~^- translate MIME composition draft
^mhl(1)~^- produce formatted listings of nmh messages
^mhlist(1)~^- list information about content of MIME messages
^mhmail(1)~^- send or read mail
^mhn(1)~^- display/list/store/cache MIME messages
^mhparam(1)~^- print nmh profile components
^mhpath(1)~^- print full pathnames of nmh messages and folders
^mhshow(1)~^- display MIME messages
^mhstore(1)~^- store contents of MIME messages into files
^msgchk(1)~^- check for messages
^msh(1)~^- nmh shell(and BBoard reader)
^next(1)~^- show the next message
^packf(1)~^- compress a folder into a single file
^pick(1)~^- select messages by content
^prev(1)~^- show the previous message
^prompter(1)~^- prompting editor front end
^rcvdist(1)~^- asynchronously redistribute new mail
^rcvpack(1)~^- append message to file
^rcvstore(1)~^- asynchronously incorporate new mail
^rcvtty(1)~^- report new mail
^refile(1)~^- file messages in other folders
^repl(1)~^- reply to a message
^rmf(1)~^- remove folder
^rmm(1)~^- remove messages
^scan(1)~^- produce a one line per message scan listing
^send(1)~^- send a message
^sendfiles(1)~^- send multiple files and directories in MIME message
^show(1)~^- show(display) messages
^slocal(1)~^- asynchronously filter and deliver new mail
^sortm(1)~^- sort messages
^whatnow(1)~^- prompting front-end for send
^whom(1)~^- report to whom a message would go
^mh-alias(5)~^- alias file for nmh message system
^mh-draft(5)~^- draft folder facility
^mh-format(5)~^- format file for nmh message system
^mh-mail(5)~^- message format for nmh message system
^mh-profile(5)~^- user customization for nmh message system
^mh-sequence(5)~^- sequence specification for nmh message system
^mh-tailor(5)~^- mail transport customization for nmh message system
^ap(8)~^- parse addresses 822-style
^conflict(8)~^- search for alias/password conflicts
^dp(8)~^- parse dates 822-style
^fmtdump(8)~^- decode nmh format files
^install-mh(8)~^- initialize the nmh environment
^post(8)~^- deliver a message
</code></pre>
</dl>
<h2>FILES</h2>
<pre>
^/usr/bin~^contains <i>nmh</i> commands
^/etc/nmh~^contains <i>nmh</i> format files
^/usr/libexec/nmh~^contains <i>nmh</i> library commands
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
</pre>
<h2>BUGS</h2>
<p> If problems are encountered with an <code>nmh</code> program, the problems should be reported to the local maintainers of <code>nmh</code>. When doing this, the name of the program should be reported, along with the version information for the program.<br />
 To find out what version of an <code>nmh</code> program is being run, invoke the program with the <code>-version</code> switch. This information includes the version of <code>nmh</code>, the host it was generated on, and the date the program was loaded. </p>
<p> Send bug reports and suggestions to <i>nmh-workers [at] nongnu.org</i>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mh-chart/">mh-chart</a>(1) </p>
<h2>Index</h2>
