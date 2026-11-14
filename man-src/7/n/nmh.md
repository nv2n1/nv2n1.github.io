---
title: "nmh(7)"
name: "nmh"
section: "7"
letter: "n"
url: "/docs/linux/man/7-nmh/"
description: "nmh – new MH message system"
---

<p>nmh &#8211; new MH message system</p>
<h2>Description</h2>
<p><code>nmh</code> is the name of a powerful message handling system. Rather than being a single comprehensive program, <code>nmh</code> consists of a collection of fairly simple single-purpose programs to send, retrieve, save, and manipulate messages. </p>
<p> Unlike most mail clients in UNIX, <code>nmh</code> is not a closed system which must be explicitly run, then exited when you wish to return to the shell. You may freely intersperse <code>nmh</code> commands with other shell commands, allowing you to read and answer your mail while you have (for example) a compilation running, or search for a file or run programs as needed to find the answer to someone&#8217;s question before answering their mail. </p>
<p> The rest of this manual entry is a quick tutorial which will teach you the basics of <code>nmh</code>. You should read the manual entries for the individual programs for complete documentation. </p>
<p> To get started using <code>nmh</code>, put the directory &#8220;/usr/bin&#8221; in your <code>$PATH</code>. Run the <code>install-mh</code> command. If you&#8217;ve never used <code>nmh</code> before, it will create the necessary default files and directories after asking you if you wish it to do so. </p>
<p> <code>inc</code> moves mail from your system maildrop into your <code>nmh</code> &#8220;+inbox&#8221; folder, breaking it up into separate files and converting it to <code>nmh</code> format as it goes. It prints one line for each message it processes, containing the from field, the subject field and as much of the first line of the message as will fit. It leaves the first message it processes as your current message. You&#8217;ll need to run <code>inc</code> each time you wish to incorporate new mail into your <code>nmh</code> file. </p>
<p> <code>scan</code> prints a list of the messages in your current folder. </p>
<p> The commands <code>show</code>, <code>next</code>, and <code>prev</code> are used to read specific messages from the current folder. <code>show</code> displays the current message, or a specific message, which may be specified by its number, which you pass as an argument to <code>show</code>. <code>next</code> and <code>prev</code> display, respectively, the message numerically after or before the current message. In all cases, the message displayed becomes the current message. If there is no current message, <code>show</code> may be called with an argument, or <code>next</code> may be used to advance to the first message. </p>
<p> <code>rmm</code> (remove message) deletes the current message. It may be called with message numbers passed as arguments, to delete specific messages. </p>
<p> <code>repl</code> is used to respond to the current message (by default). It places you in the editor with a prototype response form. While you&#8217;re in the editor, you may peruse the item you&#8217;re responding to by reading the file <code>@</code>. After completing your response, type &#8220;l&#8221; to <code>list</code> (review) it, or &#8220;s&#8221; to <code>send</code> it. </p>
<p> <code>comp</code> allows you to compose a message by putting you in the editor on a prototype message form, and then lets you send it via the <code>whatnow</code> command. <code>whatnow</code> also supports easy-to-use management of MIME attachments via its <code>attach</code> and related responses, as described in its man page. </p>
<p> <code>nmh</code> command arguments are usually called <i>switches</i>. Some switches have a corresponding &#8220;-no&#8221; switch, which negates all previous occurrences of that switch on the command line. This allows a user to conveniently override, on the command line, a switch in their profile. Switches may be abbreviated as long as there is no ambiguity with another switch of the same command. To avoid ambiguity with any switches that may be added in the future, it is recommended that full switch names be used in durable code such as shell scripts, functions, and aliases. </p>
<p> All the <code>nmh</code> commands may be run with the single switch <code>-help</code>, which causes them to print a list of the switches they may be invoked with and then exit. </p>
<p> All the <code>nmh</code> commands may be run with the single switch <code>-version</code>, which causes them to print the version number of the <code>nmh</code> distribution, and then exit. </p>
<p> Commands which take a message number as an argument (<code>scan</code>, <code>show</code>, <code>repl</code>, &#8230;) also take one of the words &#8220;first&#8221;, &#8220;prev&#8221;, &#8220;cur&#8221;, &#8220;next&#8221;, or &#8220;last&#8221; to indicate (respectively) the first, previous, current, next, or last message in the current folder (assuming they are defined). As a shorthand, &#8220;.&#8221; is equivalent to &#8220;cur&#8221;. </p>
<p> Commands which take a range of message numbers (<code>rmm</code>, <code>scan</code>, <code>show</code>, &#8230;) also take any of the abbreviations:</p>
<dl>
<dt><i>&lt;num1&gt;</i>&#8211;<i>&lt;num2&gt;</i></p>
<dd>Indicates all messages in the range &lt;num1&gt; to &lt;num2&gt;, inclusive. The range must be nonempty.</p>
<dt>all</p>
<dd>Indicates all messages, i.e., <i>first</i>&#8211;<i>last</i>.</p>
<dt><i>&lt;num&gt;</i>:+<i>N</i></p>
<dd>
<dt><i>&lt;num&gt;</i>:-N</p>
<dd>Up to <i>N</i> messages beginning with (or ending with) message <i>num</i>. <i>Num</i> may be any of the pre-defined symbols <code>first</code>, <code>prev</code>, <code>cur</code>, <code>next</code> or <code>last</code>.</p>
<dt>first:<i>N</i></p>
<dd>
<dt>prev:<i>N</i></p>
<dd>
<dt>next:<i>N</i></p>
<dd>
<dt>last:<i>N</i></p>
<dd>The first, previous, next or last messages, if they exist.</dl>
<p> Commands that take a folder name (<code>inc</code>, <code>refile</code>, <code>scan,</code> &#8230;) accept the folder name in two formats: &#8220;+folder&#8221; or &#8220;@folder&#8221;. In both cases, &#8220;folder&#8221; can be a &#8220;/&#8221;-separated path, e.g. &#8220;foo/bar&#8221;. &#8220;+folder&#8221; specifies a directory path to a folder. If &#8220;folder&#8221; starts with &#8220;/&#8221; then it&#8217;s an absolute path from the root directory. If it is &#8220;.&#8221; or &#8220;..&#8221;, or starts with &#8220;./&#8221; or &#8220;../&#8221;, then it&#8217;s relative to the current working directory. Otherwise it&#8217;s relative to <a href="/docs/linux/man/5-mh-profile/">mh-profile</a>(5)&#8217;s &#8220;<i>Path</i>&#8221;, i.e. as given by `<code>mhpath +</code>`. &#8220;@folder&#8221; is a shorthand for &#8220;+curfolder/folder&#8221;; it&#8217;s a relative path from the current folder. &#8220;curfolder&#8221; is given by `<code>mhpath</code>`. For example, assuming a <code>Path</code> profile component of Mail,</p>
<dl>
<dd><code>scan </code><i>+inbox</i> scans $HOME/Mail/inbox</p>
<dt><code>scan </code><i>+work/todo</i></p>
<dd>scans $HOME/Mail/work/todo</p>
<dt><code>scan </code><i>@todo</i></p>
<dd>scans $HOME/Mail/work/todo, if current folder is +work</p>
<dt><code>refile </code><i>@../done</i></p>
<dd>refiles to $HOME/Mail/work/done, if the current folder is +work/todo</p>
<dt><code>scan </code><i>+/tmp</i></p>
<dd>scans /tmp</p>
<dt><code>scan </code><i>+.</i></p>
<dd>scans the current directory</p>
<dt><code>refile </code><i>@.</i></p>
<dd>refiles current message to end of current folder.</dl>
<p> There are many other possibilities such as creating multiple folders for different topics, and automatically refiling messages according to subject, source, destination, or content. These are beyond the scope of this manual entry.</p>
<h2>Commands</h2>
<p>Following is a list of all the <code>nmh</code> commands, grouped loosely according to their role.</p>
<h3>Sending</h3>
<dl>
<dd><i><a href="/docs/linux/man/1-comp/">comp</a></i>(1) compose a message</p>
<dt><i><a href="/docs/linux/man/1-forw/">forw</a></i>(1)</p>
<dd>forward messages</p>
<dt><i><a href="/docs/linux/man/1-repl/">repl</a></i>(1)</p>
<dd>reply to a message</p>
<dt><i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1)</p>
<dd>prompting front-end for send</dl>
<p> Note that although <code>whatnow</code> provides much of the primary <code>nmh</code> user interface for sending mail, it is almost never invoked manually, but rather is invoked indirectly by one of the above commands, after you&#8217;ve composed a message in your editor, and before you&#8217;ve decided to send it. Here you can add attachments, check the recipient list, decide to quit and send it later, etc. </p>
<p> Related utilities:</p>
<dl>
<dd><i><a href="/docs/linux/man/1-ali/">ali</a></i>(1) list mail aliases</p>
<dt><i><a href="/docs/linux/man/1-anno/">anno</a></i>(1)</p>
<dd>annotate messages</p>
<dt><i><a href="/docs/linux/man/1-whom/">whom</a></i>(1)</p>
<dd>report to whom a message would go</p>
<dt><i><a href="/docs/linux/man/1-dist/">dist</a></i>(1)</p>
<dd>redistribute a message to additional addresses</dl>
<p> Advanced commands, only sometimes invoked directly:</p>
<dl>
<dd><i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1) translate MIME composition draft</p>
<dt><i><a href="/docs/linux/man/1-send/">send</a></i>(1)</p>
<dd>send a message</p>
<dt><i><a href="/docs/linux/man/1-sendfiles/">sendfiles</a></i>(1)</p>
<dd>send multiple files in a MIME message</dl>
<h3>Incorporating</h3>
<dl>
<dt><i><a href="/docs/linux/man/1-inc/">inc</a></i>(1)</p>
<dd>incorporate new mail</dl>
<p> Related utilities:</p>
<dl>
<dd><i><a href="/docs/linux/man/1-burst/">burst</a></i>(1) explode digests into messages</p>
<dt><i><a href="/docs/linux/man/1-msgchk/">msgchk</a></i>(1)</p>
<dd>check for messages</p>
<dt><i><a href="/docs/linux/man/1-rcvdist/">rcvdist</a></i>(1)</p>
<dd>asynchronously redistribute new mail</p>
<dt><i><a href="/docs/linux/man/1-rcvpack/">rcvpack</a></i>(1)</p>
<dd>append message to file</p>
<dt><i><a href="/docs/linux/man/1-rcvstore/">rcvstore</a></i>(1)</p>
<dd>asynchronously incorporate new mail</p>
<dt><i><a href="/docs/linux/man/1-slocal/">slocal</a></i>(1)</p>
<dd>asynchronously filter and deliver new mail</dl>
<h3>Viewing</h3>
<dl>
<dd><i><a href="/docs/linux/man/1-next/">next</a></i>(1) show the next message</p>
<dt><i><a href="/docs/linux/man/1-prev/">prev</a></i>(1)</p>
<dd>show the previous message</p>
<dt><i><a href="/docs/linux/man/1-show/">show</a></i>(1)</p>
<dd>show(display) messages</p>
<dt><i><a href="/docs/linux/man/1-scan/">scan</a></i>(1)</p>
<dd>produce a one line per message scan listing</p>
<dt><i><a href="/docs/linux/man/1-fnext/">fnext</a></i>(1)</p>
<dd>select the next folder with new messages</p>
<dt><i><a href="/docs/linux/man/1-fprev/">fprev</a></i>(1)</p>
<dd>select the previous folder with new messages</dl>
<p> Related utilities, only sometimes invoked directly:</p>
<dl>
<dd><i><a href="/docs/linux/man/1-mhl/">mhl</a></i>(1) produce formatted listings of nmh messages</p>
<dt><i><a href="/docs/linux/man/1-mhlist/">mhlist</a></i>(1)</p>
<dd>list information about content of MIME messages</p>
<dt><i><a href="/docs/linux/man/1-mhn/">mhn</a></i>(1)</p>
<dd>display/list/store/cache MIME messages</p>
<dt><i><a href="/docs/linux/man/1-mhshow/">mhshow</a></i>(1)</p>
<dd>display MIME messages</p>
<dt><i><a href="/docs/linux/man/1-mhstore/">mhstore</a></i>(1)</p>
<dd>store contents of MIME messages into files</dl>
<h3>Searching</h3>
<p>Within a folder:</p>
<dl>
<dt><i><a href="/docs/linux/man/1-pick/">pick</a></i>(1)</p>
<dd>select messages by content</dl>
<p> Across folders:</p>
<dl>
<dd><i><a href="/docs/linux/man/1-new/">new</a></i>(1) list folders with new messages</p>
<dt><i><a href="/docs/linux/man/1-unseen/">unseen</a></i>(1)</p>
<dd>list new messages in a give set of folders</p>
<dt><i><a href="/docs/linux/man/1-flist/">flist</a></i>(1)</p>
<dd>list folders with messages in given sequence(s)</p>
<dt><i><a href="/docs/linux/man/1-flists/">flists</a></i>(1)</p>
<dd>list all folders with messages in given sequence(s)</p>
<dt><i><a href="/docs/linux/man/1-folder/">folder</a></i>(1)</p>
<dd>set/list current folder/message</p>
<dt><i><a href="/docs/linux/man/1-folders/">folders</a></i>(1)</p>
<dd>list all folders</dl>
<h3>Organizing</h3>
<dl>
<dd><i><a href="/docs/linux/man/1-mark/">mark</a></i>(1) mark messages</p>
<dt><i><a href="/docs/linux/man/1-refile/">refile</a></i>(1)</p>
<dd>file messages in other folders</p>
<dt><i><a href="/docs/linux/man/1-rmf/">rmf</a></i>(1)</p>
<dd>remove folder</p>
<dt><i><a href="/docs/linux/man/1-rmm/">rmm</a></i>(1)</p>
<dd>remove messages</p>
<dt><i><a href="/docs/linux/man/1-sortm/">sortm</a></i>(1)</p>
<dd>sort messages</dl>
<h3>Convenience Wrappers</h3>
<dl>
<dd><i><a href="/docs/linux/man/1-mhmail/">mhmail</a></i>(1) send or read mail</p>
<dt><i><a href="/docs/linux/man/1-msh/">msh</a></i>(1)</p>
<dd>nmh shell</dl>
<h3>Utilities</h3>
<dl>
<dd><i><a href="/docs/linux/man/1-mhfixmsg/">mhfixmsg</a></i>(1) rewrite MIME messages with various transformations</p>
<dt><i><a href="/docs/linux/man/1-mhparam/">mhparam</a></i>(1)</p>
<dd>print nmh profile components</p>
<dt><i><a href="/docs/linux/man/1-mhpath/">mhpath</a></i>(1)</p>
<dd>print full pathnames of nmh messages and folders</p>
<dt><i><a href="/docs/linux/man/1-packf/">packf</a></i>(1)</p>
<dd>compress a folder into a single file</p>
<dt><i><a href="/docs/linux/man/1-prompter/">prompter</a></i>(1)</p>
<dd>prompting editor front end</p>
<dt><i><a href="/docs/linux/man/1-rcvtty/">rcvtty</a></i>(1)</p>
<dd>report new mail</dl>
<h3>Indirectly Invoked Commands</h3>
<dl>
<dd><i><a href="/docs/linux/man/8-ap/">ap</a></i>(8) parse addresses RFC 822-style</p>
<dt><i><a href="/docs/linux/man/8-conflict/">conflict</a></i>(8)</p>
<dd>search for alias/password conflicts</p>
<dt><i><a href="/docs/linux/man/8-dp/">dp</a></i>(8)</p>
<dd>parse dates RFC 822-style</p>
<dt><i><a href="/docs/linux/man/8-fmtdump/">fmtdump</a></i>(8)</p>
<dd>decode <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) files</p>
<dt><i><a href="/docs/linux/man/8-install-mh/">install-mh</a></i>(8)</p>
<dd>initialize the nmh environment</p>
<dt><i><a href="/docs/linux/man/8-post/">post</a></i>(8)</p>
<dd>deliver a message</dl>
<h3>Files Used by nmh Commands</h3>
<dl>
<dd><i><a href="/docs/linux/man/5-mh-alias/">mh-alias</a></i>(5) alias file for nmh message system</p>
<dt><i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5)</p>
<dd>format file for nmh message system</p>
<dt><i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5)</p>
<dd>user customization for nmh message system</p>
<dt><i><a href="/docs/linux/man/5-mh-tailor/">mh-tailor</a></i>(5)</p>
<dd>mail transport customization for nmh message system</dl>
<h3>Formats</h3>
<dl>
<dd><i><a href="/docs/linux/man/5-mh-draft/">mh-draft</a></i>(5) draft folder facility</p>
<dt><i><a href="/docs/linux/man/5-mh-folders/">mh-folders</a></i>(5)</p>
<dd>nmh message storage format specification</p>
<dt><i><a href="/docs/linux/man/5-mh-mail/">mh-mail</a></i>(5)</p>
<dd>message format for nmh message system</p>
<dt><i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5)</p>
<dd>sequence specification for nmh message system</dl>
<h2>Files</h2>
<dl>
<dt>/usr/bin</p>
<dd>contains <code>nmh</code> commands</p>
<dt>/etc/nmh</p>
<dd>contains <code>nmh</code> format files</p>
<dt>/usr/libexec/nmh</p>
<dd>contains <code>nmh</code> library commands</p>
<dt>$HOME/.mh-profile</p>
<dd>The user&#8217;s nmh profile</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-install-mh/">install-mh</a></i>(1), <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5), <i><a href="/docs/linux/man/7-mh-chart/">mh-chart</a></i>(7), <i><a href="/docs/linux/man/7-mh-mime/">mh-mime</a></i>(7)</p>
<h2>Bugs</h2>
<p>If problems are encountered with an <code>nmh</code> program, the problems should be reported to the local maintainers of <code>nmh</code>. When doing this, the name of the program should be reported, along with the version information for the program. To find out what version of an <code>nmh</code> program is being run, invoke the program with the <code>-version</code> switch. This prints the version of <code>nmh</code>, the host it was compiled on, and the date the program was linked. Send bug reports and suggestions to <i>nmh-workers [at] nongnu.org</i>. </p>
