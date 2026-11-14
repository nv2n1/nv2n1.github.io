---
title: "mh-draft(5)"
name: "mh-draft"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mh-draft/"
description: "mh-draft – draft folder facility for nmh message system"
---

<p>mh-draft &#8211; draft folder facility for nmh message system</p>
<h2>Description</h2>
<p>There are a number of interesting advanced facilities for the composition of outgoing mail.</p>
<h3>The Draft Folder</h3>
<p>The <code>comp</code>, <code>dist</code>, <code>forw</code>, <code>repl</code>, and <code>whom</code> commands have two additional switches, <code>-draftfolder</code> <i>+folder</i> and <code>-draftmessage</code> <i>msg</i> which allow you to manipulate the various draft messages you are composing. </p>
<p> If <code>-draftfolder</code> <i>+folder</i> is used, these commands are directed to construct a draft message in the indicated folder. (The &#8220;<i>Draft-Folder</i>&#8221; profile entry may be used to declare a default draft folder for use with <code>comp</code>, <code>dist</code>, <code>forw</code>, <code>repl</code>, and <code>whom ).</code> </p>
<p> If the switch <code>-draftmessage</code> <i>msg</i> is given, the specified draft is used to compose the message. If <code>-draftmessage</code> <i>msg</i> is not used, then the draft defaults to `new&#8217; (create a new draft) unless the user invokes <code>comp</code> with <code>-use</code>, in which case the default is `cur&#8217;. </p>
<p> Hence, the user may have several message compositions in progress simultaneously. Now, all of the <code>nmh</code> tools are available on each of the user&#8217;s message drafts (e.g. <code>show</code>, <code>scan</code>, <code>pick</code>, and so on). If the folder does not exist, the user is asked if it should be created (just like with <code>refile</code>). Also, the last draft message the user was composing is known as `cur&#8217; in the draft folder. </p>
<p> Furthermore, the <code>send</code> command has these switches as well. Hence, from the shell, the user can send off whatever drafts desired using the standard <code>nmh</code> `msgs&#8217; convention with <code>-draftmessage</code> <i>msgs</i>. If no `msgs&#8217; are given, it defaults to `cur&#8217;. </p>
<p> In addition, all five programs have a <code>-nodraftfolder</code> switch, which undoes the last occurrence of <code>-draftfolder</code> <i>folder</i> (useful if the latter occurs in the user&#8217;s <code>nmh</code> profile). </p>
<p> If the user does not give the <code>-draftfolder</code> <i>+folder</i> switch, then all these commands act &#8220;normally&#8221;. Note that the <code>-draft</code> switch to <code>send</code> and <code>show</code> still refers to the file called `draft&#8217; in the user&#8217;s <code>nmh</code> directory. In the interests of economy of expression, when using <code>comp</code> or <code>send</code>, the user needn&#8217;t prefix the draft `msg&#8217; or `msgs&#8217; with <code>-draftmessage</code>. Both of these commands accept a `file&#8217; or `files&#8217; argument, and they will, if given <code>-draftfolder</code> <i>+folder</i> treat these arguments as `msg&#8217; or `msgs&#8217;. (This may appear to be inconsistent, at first, but it saves a lot of typing) Hence, </p>
<dl>
<dd>
<pre>send -draftfolder +drafts first</pre>
</dl>
<p> is the same as </p>
<dl>
<dd>
<pre>send -draftfolder +drafts -draftmessage first</pre>
</dl>
<p> To make all this a bit more clear, here are some examples. Let&#8217;s assume that the following entries are in the <code>nmh</code> profile: </p>
<dl>
<dd>
<pre>Draft-Folder: +drafts
sendf: -draftfolder +drafts</pre>
</dl>
<p> Furthermore, let&#8217;s assume that the program <code>sendf</code> is a (symbolic) link in the user&#8217;s <i>$HOME/bin/</i> directory to <code>send</code>. Then, any of the commands </p>
<dl>
<dd>
<pre>comp
dist
forw
repl</pre>
</dl>
<p> constructs the message draft in the `draft&#8217; folder using the `new&#8217; message number. Furthermore, they each define `cur&#8217; in this folder to be that message draft. If the user were to use the <code>quit</code> option at `What now?&#8217; level, then later on, if no other draft composition was done, the draft could be sent with simply </p>
<dl>
<dd>
<pre>sendf</pre>
</dl>
<p> Or, if more editing was required, the draft could be edited with </p>
<dl>
<dd>
<pre>comp -use</pre>
</dl>
<p> Instead, if other drafts had been composed in the meantime, so that this message draft was no longer known as `cur&#8217; in the `draft&#8217; folder, then the user could <code>scan</code> the folder to see which message draft in the folder should be used for editing or sending. Clever users could even employ a backquoted <code>pick</code> to do the work: </p>
<dl>
<dd>
<pre>comp -use `pick +drafts -to nmh-workers`</pre>
</dl>
<p> or </p>
<dl>
<dd>
<pre>sendf `pick +drafts -to nmh-workers`</pre>
</dl>
<p> Note that in the <code>comp</code> example, the output from <code>pick</code> must resolve to a single message draft (it makes no sense to talk about composing two or more drafts with one invocation of <code>comp</code>). In contrast, in the <code>send</code> example, as many message drafts as desired can appear, since <code>send</code> doesn&#8217;t mind sending more than one draft at a time. </p>
<p> Note that the argument <code>-draftfolder</code> <i>+folder</i> is not included in the profile entry for <code>send</code>, since when <code>comp</code>, et. al., invoke <code>send</code> directly, they supply <code>send</code> with the UNIX pathname of the message draft, and <code>not</code> a <code>-draftmessage</code> <i>msg</i> argument. As far as <code>send</code> is concerned, a draft folder is not being used. </p>
<p> It is important to realize that <code>nmh</code> treats the draft folder like a standard <code>nmh</code> folder in nearly all respects. There are two exceptions: </p>
<p> First, under no circumstancs will the <code>-draftfolder</code> <i>folder</i> switch cause the named folder to become the current folder. </p>
<p> Obviously, if the folder appeared in the context of a standard <i>+folder</i> argument to an <code>nmh</code> program, as in </p>
<dl>
<dd>
<pre>scan +drafts</pre>
</dl>
<p> it might become the current folder, depending on the context changes of the <code>nmh</code> program in question. </p>
<p> Second, although conceptually <code>send</code> deletes the `msgs&#8217; named in the draft folder, it does not call <i>delete-prog</i> to perform the deletion.</p>
<h3>What Happens if the Draft Exists</h3>
<p>When the <code>comp</code>, <code>dist</code>, <code>forw</code>, and <code>repl</code> commands are invoked and the draft you indicated already exists, these programs will prompt the user for a reponse directing the program&#8217;s action. The prompt is </p>
<dl>
<dd>
<pre>Draft ``/home/foobar/nmhbox/draft'' exists (xx bytes).
Disposition?</pre>
</dl>
<p> The appropriate responses and their meanings are: </p>
<dl>
<dd>
<pre><code>^replace~^</code>- deletes the draft and starts afresh
<code>^list~^</code>- lists the draft
<code>^refile~^</code>- files the draft into a folder and starts afresh
<code>^quit~^</code>- leaves the draft intact and exits</pre>
</dl>
<p> In addition, if you specified <code>-draftfolder</code> <i>folder</i> to the command, then one other response will be accepted: </p>
<dl>
<dd>
<pre><code>^new~^</code>- finds a new draft</pre>
</dl>
<p> just as if <code>-draftmessage</code> <i>new</i> had been given. Finally, the <code>comp</code> command will accept one more response: </p>
<dl>
<dd>
<pre><code>^use~^</code>- re-uses the draft</pre>
</dl>
<p> just as if <code>-use</code> had been given.</p>
<h2>Context</h2>
<p>None</p>
