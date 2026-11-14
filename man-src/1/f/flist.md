---
title: "flist(1)"
name: "flist"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flist/"
description: "flist, flists – list the number of messages in given sequence(s)"
---

<h2 class="name">NAME</h2>
<p> flist, flists &#8211; list the number of messages in given sequence(s) </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flist</code> [<i>+folder1</i> [<i>+folder2</i> &#8230;]] [<code>-sequence</code> <i>name1</i> [<code>-sequence</code> <i>name2</i> &#8230;]] [<code>-all</code> | <code>-noall</code>] [<code>-showzero</code> | <code>-noshowzero</code>] [<code>-recurse</code> | <code>-norecurse</code>] [<code>-fast</code> | <code>-nofast</code>] [<code>-alpha</code> | <code>-noalpha</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<dl>
<dt> <code>flists</code></p>
<dd>is equivalent to <code>flist</code> <code>-all</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>Flist</code> is used to search a list of folders and display the number of messages in these folders that are in a given sequence or set of sequences (for example the &#8220;<i>unseen</i>&#8221; sequence). This is especially useful if you use some mechanism such as <code>slocal</code> or <code>procmail</code> (typically in conjunction with <code>rcvstore</code>) to pre-sort your mail into different folders before you view it. </p>
<p> By default, the command <code>flist</code> will search the current folder for the given sequence or sequences (usually &#8220;<i>unseen</i>&#8221;). If (possibly multiple) folders are specified on the command line with <i>+folder</i>, then all these folders are searched for the given sequence(s). <code>Flist</code> will display for each folder searched, the number of messages in each of the specified sequences, and the total number of messages. </p>
<p> The option <code>-sequence</code> is used to specify the name of a sequence in which to search for. This option may be used multiple times to specify multiple sequences. If this is not given, then the default is to search for all the sequences specified by the &#8220;<i>Unseen-Sequence</i>&#8221; profile component. For more details about sequences, read the <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5) man page. </p>
<p> Typically, <code>flist</code> will produce a line for each sequence, for every folder that is searched, even those which do not contain any messages in the given sequence. Specifying <code>-noshowzero</code> will cause <code>flist</code> to print only those folder/sequence combinations such the folder has a non-zero number of messages in the given specified sequence. </p>
<p> If <code>-recurse</code> is given, then for each folder that is search, <code>flist</code> will also recursively descend into those folders to search subfolders for the given sequence. </p>
<p> If <code>-fast</code> is given, only the names of the folders searched will be displayed, and <code>flist</code> will suppress all other output. If this option is used in conjunction with <code>-noshowzero</code>, then <code>flist</code> will only print the names of those folders searched that contain messages in in at least one of the specified sequences..SS &quot;Multiple Folders&quot; If the option <code>-all</code> is given (and no folders are specified with <i>+folder</i>), then <code>flist</code> will search all the folders in the top level of the users nmh directory. These folders are all preceded by the read-only folders, which occur as &#8220;<i>atr-cur-</i>&#8221; entries in the user&#8217;s <code>nmh</code> context. </p>
<p> An example of the output of <code>flist</code> <code>-all</code> is: </p>
<dl>
<dt>
<dd>
<pre><code>
/ work / Mail has 5 in sequence unseen(private);
out of 46 inbox + has 10 in sequence unseen;
out of 153 junklist has 0 in sequence unseen;
out of 63 postmaster has 1 in sequence unseen;
out of 3
</code></pre>
</dl>
<p> The &#8220;+&#8221; after <i>inbox</i> indicates that it is the current folder. </p>
<p> The &#8220;private&#8221; flag indicates that the given sequence for that folder is private. See the <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5) man page for details about private sequences. </p>
<p> If the option <code>-all</code> and <i>+folder</i> are both specified, then <code>flist</code> will search this folder, and all its first level subfolders for the given sequence. You may specify multiple folders in this way. </p>
<p> If <code>flist</code> is invoked by a name ending with &#8220;s&#8221; (e.g. <code>flists</code>), then the switch <code>-all</code> is assumed by default. </p>
<p> The sorting order for the listing is alphabetical (with <code>-alpha</code>), or in a priority order defined by the &#8220;<i>Flist-Order</i>&#8221; profile entry (with <code>-noalpha</code>). Each item in the &#8220;<i>Flist-Order</i>&#8221; is a folder name or a folder name pattern that uses * to match zero or more characters. Longer matching patterns have precedence over shorter matching patterns. For example: </p>
<dl>
<dt>
<dd>
<pre>
Flist-Order: personal petproject mh* * admin *junk
</pre>
</dl>
<p> This order puts a few interesting folders first, such as those with mail addressed to you personally, those about a pet project, and those about mh-related things. It places uninteresting folders at the end, and it puts everything else in the middle in alphabetical order.</p>
<h2>FILES</h2>
<dl>
<dt>$HOME/.mh_profile</p>
<dd> The user&#8217;s profile.</dl>
<h2>PROFILE COMPONENTS</h2>
<dl>
<dt>Path:</p>
<dd> To determine the user&#8217;s nmh directory.</p>
<dt>mh-sequences:</p>
<dd> File that contains public sequences.</p>
<dt>Unseen-Sequence:</p>
<dd> The name of the unseen message sequence.</p>
<dt>Flist-Order:</p>
<dd> To sort folders by priority.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-folder/">folder</a></i>(1), <i><a href="/docs/linux/man/1-rcvstore/">rcvstore</a></i>(1), <i><a href="/docs/linux/man/1-slocal/">slocal</a></i>(1), <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5)</p>
<h2>DEFAULTS</h2>
<dl>
<dt>-sequence</p>
<dd> The Unseen-Sequence profile entry.</p>
<dt>-showzero</p>
<dd>
<dt>-noall</p>
<dd>
<dt>-norecurse</p>
<dd>
<dt>-noalpha</p>
<dd>
<dt>-nofast</p>
<dd></dl>
<h2>CONTEXT</h2>
<p> If <i>+folder</i> is given, it will become the current folder. If multiple folders are given, the last one specified will become the current folder. </p>
<h2>Index</h2>
