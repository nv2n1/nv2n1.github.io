---
title: "maildirmake(1)"
name: "maildirmake"
section: "1"
letter: "m"
url: "/docs/linux/man/1-maildirmake/"
description: "maildirmake – create maildirs and maildir folders"
---

<h2 class="name">NAME</h2>
<p> maildirmake &#8211; create maildirs and maildir folders </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>maildirmake</code> [options&#8230;] {<i>maildir</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>maildirmake</code> command creates maildirs, and maildir folders. This documentation describes the <code>maildirmake</code> command from the Courier mail server, which creates an extended form of maildirs that implements additional extensions beyond the basic maildir properties that were first implemented in the Qmail mail server.</p>
<h2>OPTIONS</h2>
<p> -S</p>
<dl>
<dt>
<dd> create a &quot;sharable&quot; maildir. A sharable maildir has slightly different permissions which allows creation of publicly-shared folders.</dl>
<p> -q <i>quota</i></p>
<dl>
<dt>
<dd> install a quota on the maildir. See m[blue]<code><a href="/docs/linux/man/7-maildirquota/">maildirquota</a></code>(7)m[]<font SIZE="-2">[1]</font>, below.</dl>
<p> -f <i>folder</i></p>
<dl>
<dt>
<dd> do not create a maildir, but create a folder in an existing maildir.</dl>
<p> -F <i>folder</i></p>
<dl>
<dt>
<dd> Like the -f option, except that the folder&#8217;s name is given using the system locale&#8217;s character set. Non-Latin characters in the folder&#8217;s name must be given to the -f option using IMAP&#8217;s modified-UTF7 encoding. The -F option takes the folder name specified using the console&#8217;s character set..</dl>
<p> -s <i>mode</i></p>
<dl>
<dt>
<dd> create a publicly accessible folder in an existing sharable maildir. First, use the <code>-S</code> option to create a sharable maildir. Then, run <code>maildirmake</code> again with the <code>-s</code> option to create publicly accessible folders. <i>mode</i> is a comma-separated list of the following keywords: read &#8211; readonly folder, only you can write messages to this folder; write &#8211; anyone can read and write messages to this folder; group &#8211; only allow members of your own system group to access messages in this folder (instead of everyone).</dl>
<p> &#8211;add <i>name</i>=<i>pathname</i>, &#8211;del <i>name</i></p>
<dl>
<dt>
<dd> create or delete the directories and links needed to access shared folders. See below for more information.</dl>
<h3>FOLDERS</h3>
<p> This <code>maildirmake</code> command supports enhanced maildirs that contain folders. </p>
<p> By itself, <code>maildirmake</code> makes a new subdirectory <i>maildir</i>, and creates all the necessary structures. The <code>-f</code> option creates a new &quot;folder&quot; within an existing <i>maildir</i>. <i>maildir</i> must already exist, and the <code>maildirmake</code> command will create a new folder in the maildir. </p>
<p> Folders are simply subdirectories inside the main maildir whose names start with a period, and which are themselves maildirs. For example, the command &quot;<code>maildirmake -f Drafts mail/Maildir</code>&quot; creates mail/Maildir/.Drafts, that has the usual tmp, new and cur. You MUST use the <code>-f</code> option, instead of specifying mail/Maildir/.Drafts directly, in order to correctly initialize certain enhanced maildir features. </p>
<p> Folders cannot be created directly within other folders. Running <code>maildirmake -f Urgent mail/Maildir/.Drafts</code> will not work. Instead, the period character is designated as a hierarchy separator, run <code>maildirmake -f Drafts.Urgent mail/Maildir</code> instead. This creates mail/Maildir/.Drafts.Urgent, and all mail software that supports enhanced maildirs will interpret it as a subfolder Urgent of the Drafts folder.</p>
<h3>SHARED FOLDERS</h3>
<p> This is another extension to the Maildir format that allows folders to be shared between multiple clients. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> The Courier IMAP server implements two types of shared folders: filesystem permission-based shared folders, as well as virtual shared folders based on IMAP access control lists. Use the <code>maildirmake</code> command to implement shared folders based on filesystem permissions. The m[blue]<code><a href="/docs/linux/man/1-maildiracl/">maildiracl</a></code>(1)m[]<font SIZE="-2">[2]</font> command manages access control lists, which are used by virtual shared folders. </p>
<p> See the Courier IMAP server documentation for more information. </p>
</dl>
<p> First, you need to create a collection of sharable folders, as a separate maildir: </p>
<dl>
<dt>
<dd>
<pre>
<code>maildirmake -S /usr/local/share/maildirs/notices</code>
</pre>
</dl>
<p> Then, create individuals folders that will be accessed in shared mode: </p>
<dl>
<dt>
<dd>
<pre>
<code>maildirmake -s write -f Weekly /usr/local/share/maildirs/notices</code>
</pre>
</dl>
<p> In this example, the &quot;Weekly&quot; folder is created, with read/write access to everyone. Multiple folders can be created in the same maildir, with different access permissions. Everyone can create a sharable maildir. The access privileges for individual folders are set by the <code>-s</code> option, and are implemented using traditional filesystem permissions. </p>
<p> Use the <code>&#8211;add</code> and <code>&#8211;del</code> options to add a sharable maildir to an existing maildir. Client software that implements this extension will now know where to find sharable folders: </p>
<dl>
<dt>
<dd>
<pre>
<code>maildirmake --add notices=/usr/local/share/maildirs/notices $HOME/Maildir</code>
</pre>
</dl>
<p> $HOME/Maildir is your main maildir. The argument to <code>-add</code> is <i>nick</i>=<i>path</i>. <i>nick</i> is a nickname for this collection of sharable folders, and <i>path</i> is the location of the sharable maildir. All folders in the sharable maildir that you have access to &#8212; such as &quot;Weekly&quot;, in this case, will now be accessible. Multiple sharable maildirs can be added, by giving each one a unique <i>nick</i>. </p>
<p> The <code>&#8211;del</code> option &quot;disconnects&quot; the sharable maildir from the main maildir.</p>
<h3>GLOBAL SHARED FOLDERS</h3>
<p> Normally <code>-add</code> command must be run for every maildir which needs to access the sharable maildir. Alternatively the file /etc/maildirshared can be created, to specify a default set of sharable maildirs. Each line in this file takes the following format: </p>
<dl>
<dt>
<dd>
<pre>
<i>nick</i>&lt;tab&gt;<i>path</i>
</pre>
</dl>
<p> <i>nick</i> is a short nickname for the sharable maildir, &lt;tab&gt; is a single tab character, <i>path</i> is the pathname to the sharable maildir.</p>
<h3>ACCESSING SHARED FOLDERS</h3>
<p> You may have read or write access to a shared folder. If you have write access, you can add messages to the shared folder. You can also delete messages that you&#8217;ve added. </p>
<p> Anyone can create a sharable maildir, so if the sharable maildir is actually created by you, can can delete any message, not just your own.</p>
<h2>SEE ALSO</h2>
<p> m[blue]<code><a href="/docs/linux/man/5-maildir/">maildir</a></code>(5)m[]<font SIZE="-2">[3]</font>, m[blue]<code><a href="/docs/linux/man/1-maildiracl/">maildiracl</a></code>(1)m[]<font SIZE="-2">[2]</font>, m[blue]<code><a href="/docs/linux/man/1-maildirkw/">maildirkw</a></code>(1)m[]<font SIZE="-2">[4]</font>, m[blue]<code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)m[]<font SIZE="-2">[5]</font>, m[blue]<code><a href="/docs/linux/man/7-maildirquota/">maildirquota</a></code>(7)m[]<font SIZE="-2">[1]</font>, m[blue]<code><a href="/docs/linux/man/8-deliverquota/">deliverquota</a></code>(8)m[]<font SIZE="-2">[6]</font>, m[blue]<code><a href="/docs/linux/man/7-maildropfilter/">maildropfilter</a></code>(7)m[]<font SIZE="-2">[7]</font>, m[blue]<code><a rel="nofollow" href="http://www.qmail.org/man/man5/maildir.html">http://www.qmail.org/man/man5/maildir.html</a></code>m[].</p>
<h2>AUTHOR</h2>
<p> <code>Sam Varshavchik</code></p>
<dl>
<dt>
<dd> Author</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> <code><a href="/docs/linux/man/7-maildirquota/">maildirquota</a></code>(7)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/maildirquota.html</dl>
<dt> 2.</p>
<dd> <code><a href="/docs/linux/man/1-maildiracl/">maildiracl</a></code>(1)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/maildiracl.html</dl>
<dt> 3.</p>
<dd> <code><a href="/docs/linux/man/5-maildir/">maildir</a></code>(5)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/maildir.html</dl>
<dt> 4.</p>
<dd> <code><a href="/docs/linux/man/1-maildirkw/">maildirkw</a></code>(1)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/maildirkw.html</dl>
<dt> 5.</p>
<dd> <code><a href="/docs/linux/man/1-maildrop/">maildrop</a></code>(1)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/maildrop.html</dl>
<dt> 6.</p>
<dd> <code><a href="/docs/linux/man/8-deliverquota/">deliverquota</a></code>(8)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/deliverquota.html</dl>
<dt> 7.</p>
<dd> <code><a href="/docs/linux/man/7-maildropfilter/">maildropfilter</a></code>(7)</p>
<dl>
<dt>
<dd> [set $man.base.url.for.relative.links]/maildropfilter.html</dl>
</dl>
<h2>Index</h2>
