---
title: "mh-alias(5)"
name: "mh-alias"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mh-alias/"
description: "mh-alias – format of nmh alias files"
---

<p>mh-alias &#8211; format of nmh alias files</p>
<h2>Description</h2>
<p>Each line of an <code>nmh</code> alias file takes one of the following forms:</p>
<dl>
<dd><i>alias</i> <code>:</code> <i>address-group</i></dl>
<dl>
<dd><i>alias</i> <code>;</code> <i>address-group</i></dl>
<dl>
<dd><code>&lt;</code> <i>alias-file</i></dl>
<dl>
<dd><code>;</code> | <code>:</code> | <code>#</code> <i>comment</i></dl>
<p> where:</p>
<dl>
<dd>
<pre><i>address-group</i> := <i>address-list</i>
 | &lt; <i>file</i>
 | = <i>UNIX-group</i>
 | + <i>UNIX-group</i>
 | *
<i>address-list</i> := <i>address</i>
 | <i>address-list</i>, <i>address</i></pre>
</dl>
<p> Continuation lines end with &#8220;\&#8221; followed by a newline<br />
 character. This also applies to comment lines. Thus, the line following a &#8220;\&#8221;-terminated comment line is a continuation of that comment line. <i>Alias-file</i> and <i>file</i> are UNIX file names. <i>UNIX-group</i> is a group name or number from the system&#8217;s group database. Alias file contents are case-insensitive, with the exception of filesystem path names. If the line starts with a &#8220;&lt;&#8221;, the file named after the &#8220;&lt;&#8221; is read for more alias definitions. The reading is done recursively, so a &#8220;&lt;&#8221; may occur in the beginning of an alias file with the expected results. If the <i>address-group</i> starts with a &#8220;&lt;&#8221;, the file named after the &#8220;&lt;&#8221; is read and its contents are added to the <i>address-list</i> for the alias. If the <i>address-group</i> starts with an &#8220;=&#8221;, the system&#8217;s group database is consulted for the UNIX-group named after the &#8220;=&#8221;. Each login name occurring as a member of the group is added to the <i>address-list</i> for the alias. In contrast, if the <i>address-group</i> starts with a &#8220;+&#8221;, the system&#8217;s group database is consulted to determine the group-id of the UNIX-group named after the &#8220;+&#8221;. Each login name occurring in the system&#8217;s password database whose group-id is indicated by this group is added to the <i>address-list</i> for the alias. If the <i>address-group</i> is simply &#8220;*&#8221;, the system&#8217;s password database is consulted and all login names with a userid greater than some magic number (usually 200) are added to the <i>address-list</i> for the alias. <code>This feature is obsolescent and will be removed in a future release.</code> In match, a trailing &#8220;*&#8221; on an alias will match just about anything appropriate. An approximation of the way aliases are resolved at posting time is:</p>
<dl>
<dt>1)</p>
<dd>Build a list of all addresses from the message to be delivered, eliminating duplicate addresses.</p>
<dt>2)</p>
<dd>If this draft originated on the local host, then for those addresses in the message that have no host specified, perform alias resolution.</p>
<dt>3)</p>
<dd>For each line in the alias file, compare &#8220;alias&#8221; against all of the existing addresses. If a match, remove the matched &#8220;alias&#8221; from the address list, and add each new address in the address-group to the address list if it is not already on the list. The alias itself is not usually output, rather the address-group that the alias maps to is output instead. If &#8220;alias&#8221; is terminated with a &#8220;;&#8221; instead of a &#8220;:&#8221;, then both the &#8220;alias&#8221; and the address are output in the correct format (with the alias quoted if necessary and the address wrapped in &lt;&gt;).</dl>
<p> Since the <i>mh-alias</i> file is read line by line, forward references work, but backward references are not recognized.</p>
<h3>Example Alias File</h3>
<pre><code>&lt;/etc/nmh/BBoardAliases
fred: frated [at] UCI.example
sgroup: fred, fear, freida
b-people: Blind List: bill, betty
UNIX-committee: &lt;unix.aliases
staff: =staff
wheels: +wheel
news.*: news</code></pre>
<p> The first line says that more aliases should immediately be read from the file <code>/etc/nmh/BBoardAliases</code>. Following this, &#8220;fred&#8221; is defined as an alias for &#8220;frated [at] UCI.example&#8221;, and &#8220;sgroup&#8221; is defined as an alias for the three names &#8220;frated [at] UCI.example&#8221;, &#8221;fear&#8221;, and &#8221;freida&#8221;. The alias &#8220;b-people&#8221; is a blind list which includes the addresses &#8220;bill&#8221; and &#8220;betty&#8221;; the message will be delivered to those addresses, but the message header will show only &#8220;Blind List: ;&#8221; (not the addresses). The alias must not be terminated with, or contain, a semicolon. Note that blind lists are not supported with the <code>sendmail/pipe</code> mail transport method. Next, the definition of &#8220;UNIX-committee&#8221; is given by reading the file <i>unix.aliases</i> in the user&#8217;s <code>nmh</code> directory, &#8220;staff&#8221; is defined as all users who are listed as members of the group &#8220;staff&#8221; in the system&#8217;s group database, and &#8220;wheels&#8221; is defined as all users whose group-id in the system&#8217;s password database is equivalent to the &#8220;wheel&#8221; group.</p>
<h2>Profile Components</h2>
<dl>
<dt>Aliasfile:</p>
<dd>Default alias file.</dl>
<h2>Files</h2>
<dl>
<dt>/etc/nmh/MailAliases</p>
<dd>System-wide default alias file.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-ali/">ali</a></i>(1), <i><a href="/docs/linux/man/1-send/">send</a></i>(1), <i><a href="/docs/linux/man/1-whom/">whom</a></i>(1), <i><a href="/docs/linux/man/3-getgrent/">getgrent</a></i>(3), <i><a href="/docs/linux/man/3-getpwent/">getpwent</a></i>(3), <i><a href="/docs/linux/man/8-conflict/">conflict</a></i>(8), <i><a href="/docs/linux/man/8-post/">post</a></i>(8)</p>
<h2>Bugs</h2>
<p>Although the forward-referencing semantics of mh-alias files prevent recursion, the <code>alias-file</code> directive may defeat this. Since the number of file descriptors is finite, such infinite recursion will terminate with a meaningless diagnostic when all the fds are used up. Earlier versions of this man page showed a semicolon at the end of the blind list example. That caused the preceding alias to not be expanded. There must not be a semicolon at the end of, or within, the address group of a blind list. <code>post</code> will append the semicolon to the blind list name. </p>
