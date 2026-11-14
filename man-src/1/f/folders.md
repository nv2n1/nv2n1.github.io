---
title: "folders(1)"
name: "folders"
section: "1"
letter: "f"
url: "/docs/linux/man/1-folders/"
description: "folder, folders – set/list current folder/message"
---

<h2 class="name">NAME</h2>
<p> folder, folders &#8211; set/list current folder/message </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>folder</code> [<i>+folder</i>] [<i>msg</i>] [<code>-all</code> | <code>-noall</code>] [<code>-create</code> | <code>-nocreate</code>] [<code>-fast</code> | <code>-nofast</code>] [<code>-header</code> | <code>-noheader</code>] [<code>-recurse</code> | <code>-norecurse</code>] [<code>-total</code> | <code>-nototal</code>] [<code>-list</code> | <code>-nolist</code>] [<code>-push</code> | <code>-pop</code>] [<code>-pack</code> | <code>-nopack</code>] [<code>-print</code>] [<code>-verbose</code> | <code>-noverbose</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<dl>
<dt> <code>folders</code></p>
<dd>is equivalent to <code>folder</code> <code>-all</code></dl>
<h2>DESCRIPTION</h2>
<p> Since the <code>nmh</code> environment is the shell, it is easy to lose track of the current folder from day to day. When <code>folder</code> is given the <code>-print</code> switch (the default), <code>folder</code> will list the current folder, the number of messages in it, the range of the messages (low-high), and the current message within the folder, and will flag extra files if they exist. An example of this summary is: </p>
<dl>
<dt>
<dd>
<pre><code>
inbox + has &amp;nbsp;
16 messages(&amp;nbsp; &amp;nbsp; 3 - 22);
cur = &amp;nbsp;
&amp;nbsp;
5.
</code></pre>
</dl>
<p> If a <i>+folder</i> and/or <i>msg</i> are specified, they will become the current folder and/or message. By comparison, when a <i>+folder</i> argument is given, this corresponds to a &#8220;cd&#8221; operation in the shell; when no <i>+folder</i> argument is given, this corresponds roughly to a &#8220;pwd&#8221; operation in the shell. </p>
<p> If the specified (or default) folder doesn&#8217;t exist, the default action is to query the user as to whether the folder should be created; when standard input is not a tty, the answer to the query is assumed to be &#8220;yes&#8221;. </p>
<p> Specifying <code>-create</code> will cause <code>folder</code> to create new folders without any query. (This is the easy way to create an empty folder for use later.) Specifying <code>-nocreate</code> will cause <code>folder</code> to exit without creating a non-existant folder. Specifying <code>-all</code> will produce a summary line for each top-level folder in the user&#8217;s nmh directory, sorted alphabetically. (If <code>folder</code> is invoked by a name ending with &#8220;s&#8221; (e.g. <code>folders</code>), <code>-all</code> is assumed). Specifying <code>-recurse</code> with <code>-all</code> will also produce a line for all sub-folders. These folders are all preceded by the read-only folders, which occur as &#8220;<i>atr-cur-</i>&#8221; entries in the user&#8217;s <code>nmh</code> context. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
FOLDER &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
#MESSAGES RANGE CUR(OTHERS) / var / work / folder has &amp;nbsp;
35 messages(&amp;nbsp; 1 - 35);
cur = 23. / usr / bugs / Mail has &amp; nbsp;
82 messages(&amp;nbsp; 1 - 108);
cur = 82. ff has &amp; nbsp;
no messages.inbox + has &amp;nbsp;
16 messages(&amp;nbsp; 3 - 22);
cur = &amp;nbsp;
5. mh has &amp;nbsp;
76 messages(15 - 76);
cur = 70. notes has &amp; nbsp;
&amp;nbsp;
2 messages(&amp;nbsp; 1 - &amp;nbsp; &amp;nbsp; 2);
cur = &amp;nbsp;
1. ucom has 124 messages(&amp;nbsp; 1 - 124);
cur = &amp;nbsp;
6;
(others).TOTAL = 339 messages in 7 folders
</code></pre>
</dl>
<p> The &#8220;+&#8221; after <i>inbox</i> indicates that it is the current folder. The &#8220;(others)&#8221; indicates that the folder <i>ucom</i> has files which aren&#8217;t messages. These files may either be sub-folders, or files that don&#8217;t belong under the nmh file naming scheme. </p>
<p> The header is output if either a <code>-all</code> or a <code>-header</code> switch is specified. It is suppressed by <code>-noheader</code>. </p>
<p> The folder and message totals are output if either a <code>-all</code> or a <code>-total</code> switch is specified. It is suppressed by <code>-nototal</code>. </p>
<p> If <code>-fast</code> is given, only the folder name (or names in the case of <code>-all</code>) will be listed. (This is faster because the folders need not be read.) </p>
<p> If a <i>+folder</i> is given along with the <code>-all</code> switch, <code>folder</code> will, in addition to setting the current folder, list the top-level subfolders for the current folder (with <code>-norecurse</code>) or list all sub-folders under the current folder recursively (with <code>-recurse</code>). </p>
<p> If <i>msg</i> is supplied, together with <i>+folder</i> or without <code>-all</code>, it will become the current message of <i>+folder</i> (if it had been supplied) or the current folder. </p>
<p> The <code>-recurse</code> switch lists each folder recursively, so use of this option effectively defeats the speed enhancement of the <code>-fast</code> option, since each folder must be searched for subfolders. Nevertheless, the combination of these options is useful. </p>
<h3>Compacting a Folder</h3>
<p> The <code>-pack</code> switch will compress the message names in the designated folders, removing holes in message numbering. The <code>-verbose</code> switch directs <code>folder</code> to tell the user the general actions that it is taking to compress the folder. </p>
<h3>The Folder Stack</h3>
<p> The <code>-push</code> switch directs <code>folder</code> to push the current folder onto the <i>folder-stack</i>, and make the <i>+folder</i> argument the current folder. If <i>+folder</i> is not given, the current folder and the top of the <i>folder-stack</i> are exchanged. This corresponds to the &#8220;pushd&#8221; operation in the shell. </p>
<p> The <code>-pop</code> switch directs <code>folder</code> to discard the top of the <i>folder-stack</i>, after setting the current folder to that value. No <i>+folder</i> argument is allowed. This corresponds to the &#8220;popd&#8221; operation in the shell. The <code>-push</code> switch and the <code>-pop</code> switch are mutually exclusive: the last occurrence of either one overrides any previous occurrence of the other. Both of these switches also set <code>-list</code> by default. </p>
<p> The <code>-list</code> switch directs <code>folder</code> to list the contents of the <i>folder-stack</i>. No <i>+folder</i> argument is allowed. After a successful <code>-push</code> or <code>-pop</code>, the <code>-list</code> action is taken, unless a <code>-nolist</code> switch follows them on the command line. This corresponds to the &#8220;dirs&#8221; operation in the shell. The <code>-push</code>, <code>-pop</code>, and <code>-list</code> switches turn off <code>-print</code>.</p>
<h2>FILES</h2>
<dl>
<dt>$HOME/.mh_profile</p>
<dd> The user&#8217;s profile.</dl>
<h2>PROFILE COMPONENTS</h2>
<dl>
<dt>Path:</p>
<dd> To determine the user&#8217;s nmh directory.</p>
<dt>Current-Folder:</p>
<dd> To find the default current folder.</p>
<dt>Folder-Protect:</p>
<dd> To set mode when creating a new folder.</p>
<dt>Folder-Stack:</p>
<dd> To determine the folder stack.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mhpath/">mhpath</a></i>(1), <i><a href="/docs/linux/man/1-refile/">refile</a></i>(1), <i><a href="/docs/linux/man/1-rmf/">rmf</a></i>(1)</p>
<h2>DEFAULTS</h2>
<dl>
<dt>+folder</p>
<dd> The current folder.</p>
<dt>msg</p>
<dd> &#8220;none&#8221;</p>
<dt>-nofast</p>
<dd>
<dt>-noheader</p>
<dd>
<dt>-nototal</p>
<dd>
<dt>-nopack</p>
<dd>
<dt>-norecurse</p>
<dd>
<dt>-noverbose</p>
<dd>
<dt>-print</p>
<dd> is the default if no <code>-list</code>, <code>-push</code>, or <code>-pop</code> is specified.</p>
<dt>-list</p>
<dd> is the default if <code>-push</code>, or <code>-pop</code> is specified.</dl>
<h2>CONTEXT</h2>
<p> If <i>+folder</i> and/or <i>msg</i> are given, they will become the current folder and/or message.</p>
<h2>BUGS</h2>
<p> There is no way to restore the default behavior (to ask the user whether to create a non-existant folder) after <code>-create</code> or <code>-nocreate</code> is given. </p>
<h2>Index</h2>
