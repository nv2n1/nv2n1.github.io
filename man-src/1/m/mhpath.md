---
title: "mhpath(1)"
name: "mhpath"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mhpath/"
description: "mhpath – print full pathnames of nmh messages and folders"
---

<h2 class="name">NAME</h2>
<p> mhpath &#8211; print full pathnames of nmh messages and folders </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mhpath</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>mhpath</code></p>
<dd>expands and sorts the message list `msgs&#8217; and writes the full pathnames of the messages to the standard output separated by newlines. If no `msgs&#8217; are specified, <code>mhpath</code> outputs the current mail folder&#8217;s pathname instead. If the only argument is `+&#8217;, your <code>nmh</code> &#8220;Path&#8221; is output; this can be useful in shell scripts. </p>
<p> Contrasted with other <code>nmh</code> commands, a message argument to <code>mhpath</code> may often be intended for writing. Because of this: </p>
<dl>
<dt>1)</p>
<dd> the name &#8220;new&#8221; has been added to <code>mhpath</code>&#8216;s list of reserved message names (the others are &#8220;first&#8221;, &#8220;last&#8221;, &#8220;prev&#8221;, &#8220;next&#8221;, &#8220;cur&#8221;, and &#8220;all&#8221;). The new message is equivalent to the message after the last message in a folder (and equivalent to 1 in a folder without messages). The &#8220;new&#8221; message may not be used as part of a message range.</p>
<dt>2)</p>
<dd> Within a message list, the following designations may refer to messages that do not exist: a single numeric message name, the single message name &#8220;cur&#8221;, and (obviously) the single message name &#8220;new&#8221;. All other message designations must refer to at least one existing message, if the folder contains messages.</p>
<dt>3)</p>
<dd> An empty folder is not in itself an error.</dl>
<p> A message number less than that of the smallest existing message in a folder is treated as if the message already exists. A message number greater than that of the highest existing message in a folder causes an &#8220;out of range&#8221; error message to be displayed. </p>
<p> As part of a range designation that contains messages that do exist, message numbers less than the smallest, or greater than the highest, existing message in a folder are ignored. </p>
<p> Examples: The current folder foo contains messages 3 5 6. Cur is 4. </p>
<dl>
<dt>
<dd>
<pre>
% mhpath
/r/phyl/Mail/foo
% mhpath all
/r/phyl/Mail/foo/3
/r/phyl/Mail/foo/5
/r/phyl/Mail/foo/6
% mhpath 2001
mhpath: message 2001 out of range 1-6
% mhpath 1-2001
/r/phyl/Mail/foo/3
/r/phyl/Mail/foo/5
/r/phyl/Mail/foo/6
% mhpath new
/r/phyl/Mail/foo/7
% mhpath last new
/r/phyl/Mail/foo/6
/r/phyl/Mail/foo/7
% mhpath last-new
mhpath: bad message list last-new
% mhpath cur
/r/phyl/Mail/foo/4
% mhpath 1-2
mhpath: no messages in range 1-2
% mhpath first:2
/r/phyl/Mail/foo/3
/r/phyl/Mail/foo/5
% mhpath 1 2
/r/phyl/Mail/foo/1
/r/phyl/Mail/foo/2
</pre>
</dl>
<p> <code>mhpath</code> is also useful in backquoted operations: </p>
<dl>
<dt>
<dd>
<pre>
% cd `mhpath +inbox`
% echo `mhpath +`
/r/phyl/Mail
</pre>
</dl>
<p> Because <code>mhpath</code> expands and sorts [<i>msgs</i>]. the command </p>
<dl>
<dt>
<dd>
<pre>
mv `mhpath 501 500`
</pre>
</dl>
<p> to will not move 501 to 500. Quite the reverse. But </p>
<dl>
<dt>
<dd>
<pre>
mv `mhpath 501` `mhpath 500`
</pre>
</dl>
<p> will do the trick. </p>
<p> Out-of-range message 0 produces a different error message than large out-of-range message numbers. But both cause <code>mhpath</code> to exit with non-zero status.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-folder/">folder</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to none
</pre>
<h2>CONTEXT</h2>
<p> None </p>
<h2>Index</h2>
