---
title: "comp(1)"
name: "comp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-comp/"
description: "comp – compose a message"
---

<h2 class="name">NAME</h2>
<p> comp &#8211; compose a message </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>comp </code> [<i>+folder</i>] [<i>msg</i>] [<code>-form</code> <i>formfile</i>] [<code>-use</code> | <code>-nouse</code>] [<code>-file</code> <i>file</i>] [<code>-draftfolder</code> <i>+folder</i>] [<code>-draftmessage</code> <i>msg</i>] [<code>-nodraftfolder</code>] [<code>-editor</code> <i>editor</i>] [<code>-noedit</code>] [<code>-width</code> <i>columns</i>] [<code>-from</code> <i>address</i>] [<code>-to</code> <i>address</i>] [<code>-cc</code> <i>address</i>] [<code>-fcc</code> <i>+folder</i>] [<code>-subject</code> <i>text</i>] [<code>-whatnowproc</code> <i>program</i>] [<code>-nowhatnowproc</code>] [<code>-build</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Comp</code></p>
<dd>is used to create a new message to be mailed. It copies a message form to the draft being composed and then invokes an editor on the draft (unless <code>-noedit</code> is given, in which case the initial edit is suppressed). </p>
<p> The default message template &#8220;components&#8221; will direct <code>comp</code> to construct the message draft as follows: </p>
<dl>
<dt>
<dd>
<pre><code>
From:
{
    from switch
}
or &lt;Local - Mailbox&gt; or &lt;username[at] hostname&gt; To:
{
    to switch
}
or blank
        cc:
{
    cc switch
}
or blank
        Fcc:
{
    fcc switch
}
or +outbox
        Subject:
{
    subject switch
}
or blank-- -- -- --
</code></pre>
</dl>
<p> If a file named &#8220;<i>components</i>&#8221; exists in the user&#8217;s nmh directory, it will be used instead of this form. You may specify an alternate forms file with the switch <code>-form</code> <i>formfile</i>. </p>
<p> You may also start <code>comp</code> using the contents of an existing message as the form. If you supply either a <i>+folder</i> or <i>msg</i> argument, that message will be used as the message form. You may not supply both a <code>-form</code> <i>formfile</i> and a <i>+folder</i> or <i>msg</i> argument. The line of dashes or a blank line must be left between the header and the body of the message for the message to be identified properly when it is sent (see <i><a href="/docs/linux/man/1-send/">send</a></i>(1)). </p>
<p> The switch <code>-use</code> directs <code>comp</code> to continue editing an already started message. That is, if a <code>comp</code> (or <code>dist</code>, <code>repl</code>, or <code>forw</code>) is terminated without sending the draft, the draft can be edited again via &#8220;<code>comp</code> <code>-use</code>&#8221;. </p>
<p> The <code>-file</code> <i>file</i> switch says to use the named file as the message draft. </p>
<p> Forms that are selected via the <code>-form</code> switch are processed via the <code>nmh</code> template system; see <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) for details. Drafts constructed from another message or with the <code>-use</code> or <code>-file</code> switchs will NOT be processed with <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5). </p>
<p> In addition to the standard <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) escapes, the following <i>component</i> escapes are either new or have an alternate meaning: </p>
<dl>
<dt>
<dd>
<pre>
<i>Escape Returns  Description</i>
fcc     string   Any folders specified with `-fcc folder'
from    string   Any addresses specified with `-from address'
to      string   Any addresses specified with `-to address'
cc      string   Any addresses specified with `-cc address'
subject string   Any text specified with `-subject text'
</pre>
</dl>
<p> By default the &#8220;To:&#8221; and &#8220;cc:&#8221; fields are empty. You may add addresses to these fields with the <code>-to</code> <i>address</i> and <code>-cc</code> <i>address</i> switches. You may give these switches multiple times to add multiple addresses. </p>
<p> By default the &#8220;From:&#8221; field has either the value of the <code>Local-Mailbox</code> profile entry or a system default email address. This default can be overridden by using the <code>-from</code> <i>address</i> switch. The default mailbox in the &#8220;Fcc:&#8221; field is <i>+outbox</i>. This can be overridden by the <code>-fcc</code> switch. </p>
<p> Any text you give to the <code>-subject</code> switch will be placed in the &#8220;Subject:&#8221; field in the draft. </p>
<p> If the draft already exists, <code>comp</code> will ask you as to the disposition of the draft. A reply of <code>quit</code> will abort <code>comp</code>, leaving the draft intact; <code>replace</code> will replace the existing draft with the appropriate form; <code>list</code> will display the draft; <code>use</code> will use the draft for further composition; and <code>refile</code> <i>+folder</i> will file the draft in the given folder, and give you a new draft with the appropriate form. (The <i>+folder</i> argument to <code>refile</code> is required.) </p>
<p> The <code>-draftfolder</code> <i>+folder</i> and <code>-draftmessage</code> <i>msg</i> switches invoke the <code>nmh</code> draft folder facility. This is an advanced (and highly useful) feature. Consult the <i><a href="/docs/linux/man/5-mh-draft/">mh-draft</a></i>(5) man page for more information. </p>
<p> The <code>-editor</code> <i>editor</i> switch indicates the editor to use for the initial edit. Upon exiting from the editor, <code>comp</code> will invoke the <code>whatnow</code> program. See <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1) for a discussion of available options. The invocation of this program can be inhibited by using the <code>-nowhatnowproc</code> switch. (In truth of fact, it is the <i>whatnow</i> program which starts the initial edit. Hence, <code>-nowhatnowproc</code> will prevent any edit from occurring.) </p>
<p> The <code>-build</code> switch is intended to be used by the Emacs mh-e interface to <code>nmh</code>. It implies <code>-nowhatnowproc</code>. It causes a file &lt;mh-dir&gt;/draft to be created, containing the draft message that would normally be presented to the user for editing. No mail is actually sent.</p>
<h2>FILES</h2>
<dl>
<dt>/etc/nmh/components</p>
<dd> The standard message skeleton.</p>
<dt>&lt;mh-dir&gt;/components</p>
<dd> An alternative to the standard skeleton.</p>
<dt>$HOME/.mh_profile</p>
<dd> The user&#8217;s profile.</dl>
<h2>PROFILE COMPONENTS</h2>
<dl>
<dt>Path:</p>
<dd> To determine the user&#8217;s nmh directory.</p>
<dt>Draft-Folder:</p>
<dd> To find the default draft-folder.</p>
<dt>Editor:</p>
<dd> To override the default editor.</p>
<dt>Msg-Protect:</p>
<dd> To set mode when creating a new message (draft).</p>
<dt>fileproc:</p>
<dd> Program to refile the message.</p>
<dt>whatnowproc:</p>
<dd> Program to ask the &#8220;What now?&#8221; questions</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dist/">dist</a></i>(1), <i><a href="/docs/linux/man/1-forw/">forw</a></i>(1), <i><a href="/docs/linux/man/1-repl/">repl</a></i>(1), <i><a href="/docs/linux/man/1-send/">send</a></i>(1), <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1), <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5)</p>
<h2>DEFAULTS</h2>
<dl>
<dt>+folder</p>
<dd> The current folder.</p>
<dt>msg</p>
<dd> The current message.</p>
<dt>-nodraftfolder</p>
<dd>
<dt>-nouse</p>
<dd></dl>
<h2>CONTEXT</h2>
<p> None</p>
<h2>BUGS</h2>
<p> If <i>whatnowproc</i> is <code>whatnow</code>, then <code>comp</code> uses a built-in <code>whatnow</code>, it does not actually run the <code>whatnow</code> program. Hence, if you define your own <i>whatnowproc</i>, don&#8217;t call it <code>whatnow</code> since <code>comp</code> won&#8217;t run it. </p>
<h2>Index</h2>
