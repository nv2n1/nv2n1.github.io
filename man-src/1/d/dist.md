---
title: "dist(1)"
name: "dist"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dist/"
description: "dist – redistribute a message to additional addresses"
---

<h2 class="name">NAME</h2>
<p> dist &#8211; redistribute a message to additional addresses </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dist</code> [<i>+folder</i>] [<i>msg</i>] [<code>-form</code> <i>formfile</i>] [<code>-annotate</code> | <code>-noannotate</code>] [<code>-inplace</code> | <code>-noinplace</code>] [<code>-draftfolder</code> <i>+folder</i>] [<code>-draftmessage</code> <i>msg</i>] [<code>-nodraftfolder</code>] [<code>-editor</code> <i>editor</i>] [<code>-noedit</code>] [<code>-width</code> <i>columns</i>] [<code>-from</code> <i>address</i>] [<code>-to</code> <i>address</i>] [<code>-cc</code> <i>address</i>] [<code>-fcc</code> <i>+folder</i>] [<code>-whatnowproc</code> <i>program</i>] [<code>-nowhatnowproc</code>] [<code>-atfile</code>] [<code>-noatfile</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Dist</code></p>
<dd>is similar to <code>forw</code>. It prepares the specified message for redistribution to addresses that (presumably) are not on the original address list. </p>
<p> The default message form contains the following elements: </p>
<dl>
<dt>
<dd>
<pre><code>
Resent - From:
{
    from switch
}
or &lt;Local - Mailbox&gt; or &lt;username[at] hostname&gt; Resent - To:
{
    to switch
}
or blank
            Resent -
        cc:
{
    cc switch
}
or blank
            Resent -
        fcc:
{
    fcc switch
}
or blank
</code></pre>
</dl>
<p> If a file named &#8220;<i>distcomps</i>&#8221; exists in the user&#8217;s nmh directory, it will be used instead of this default form. You may specify an alternate forms file with the switch <code>-form</code> <i>formfile</i>. Forms are processed via the <code>nmh</code> template system; see <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) for details. Components from the redistributed message are available as standard component escapes in the forms file. </p>
<p> In addition to the standard <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) escapes, the following <i>component</i> escapes are also supported: </p>
<dl>
<dt>
<dd>
<pre>
<i>Escape        ReturnsDescription</i>
fcc    string  Any folders specified with `-fcc folder'
nmh-from       stringAddresses specified with `-from address'
nmh-to string  Addresses specified with `-to address'
nmh-cc string  Addresses specified with `-cc address'
</pre>
</dl>
<p> See the <i><a href="/docs/linux/man/1-forw/">forw</a></i>(1) man page for descriptions of the <code>-from</code>, <code>-to</code>, <code>-cc</code>, and <code>-fcc</code> switches. </p>
<p> If the draft already exists, <code>dist</code> will ask you as to the disposition of the draft. A reply of <code>quit</code> will abort <code>dist</code>, leaving the draft intact; <code>replace</code> will replace the existing draft with a blank skeleton; and <code>list</code> will display the draft. </p>
<p> Only those addresses in &#8220;<i>Resent-To:</i>&#8221;, &#8220;<i>Resent-cc:</i>&#8221;, and &#8220;<i>Resent-Bcc:</i>&#8221; will be sent. Also, a &#8220;<i>Resent-Fcc: folder</i>&#8221; will be honored (see <i><a href="/docs/linux/man/1-send/">send</a></i>(1)). Note that with <code>dist</code>, the draft should contain only &#8220;<i>Resent-xxx:</i>&#8221; fields and no body. The headers and the body of the original message are copied to the draft when the message is sent. Use care in constructing the headers for the redistribution. </p>
<p> Because the draft is minimal, the <i><a href="/docs/linux/man/1-prompter/">prompter</a></i>(1) editor is quite useful with <code>dist</code>. </p>
<p> If the <code>-annotate</code> switch is given, the message being distributed will be annotated with the lines:</p>
<dl>
<dt>
<dd> Resent: date<br />
 Resent: addrs</dl>
<p> where each address list contains as many lines as required. This annotation will be done only if the message is sent directly from <code>dist</code>. If the message is not sent immediately from <code>dist</code>, &#8220;<code>comp</code> <code>-use</code>&#8221; may be used to re-edit and send the constructed message, but the annotations won&#8217;t take place. Normally annotations are done inplace in order to preserve any links to the message. You may use the <code>-noinplace</code> switch to change this. </p>
<p> See <i><a href="/docs/linux/man/1-comp/">comp</a></i>(1) for a description of the <code>-editor</code> and <code>-noedit</code> switches. Note that while in the editor, with <code>-atfile</code> and if the current directory is writable, the message being resent is available through a link named &#8220;@&#8221; (assuming the default <i>whatnowproc</i>). In addition, the actual pathname of the message is stored in the environment variable <code>$editalt</code>, and the pathname of the folder containing the message is stored in the environment variable <code>$mhfolder</code>. The creation of the &#8220;@&#8221; file is controlled via the <code>-atfile</code> and <code>-noatfile</code> options. </p>
<p> The <code>-draftfolder</code> <i>+folder</i> and <code>-draftmessage</code> <i>msg</i> switches invoke the <code>nmh</code> draft folder facility. This is an advanced (and highly useful) feature. Consult the <i><a href="/docs/linux/man/5-mh-draft/">mh-draft</a></i>(5) man page for more information. </p>
<p> Upon exiting from the editor, <code>dist</code> will invoke the <code>whatnow</code> program. See <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1) for a discussion of available options. The invocation of this program can be inhibited by using the <code>-nowhatnowproc</code> switch. (In truth of fact, it is the <code>whatnow</code> program which starts the initial edit. Hence, <code>-nowhatnowproc</code> will prevent any edit from occurring.)</p>
<h2>FILES</h2>
<pre>
^/etc/nmh/distcomps~^The standard message skeleton
^or &lt;mh-dir&gt;/distcomps~^Rather than the standard skeleton
^$HOME/.mh_profile~^The user profile
^&lt;mh-dir&gt;/draft~^The draft file
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^Draft-Folder:~^To find the default draft-folder
^Editor:~^To override the default editor
^fileproc:~^Program to refile the message
^whatnowproc:~^Program to ask the ``What now?'' questions
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-comp/">comp</a></i>(1), <i><a href="/docs/linux/man/1-forw/">forw</a></i>(1), <i><a href="/docs/linux/man/1-prompter/">prompter</a></i>(1), <i><a href="/docs/linux/man/1-repl/">repl</a></i>(1), <i><a href="/docs/linux/man/1-send/">send</a></i>(1), <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msg</code>' defaults to cur
`<code>-noannotate</code>'
`<code>-nodraftfolder</code>'
`<code>-inplace</code>'
`<code>-noatfile</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. The message distributed will become the current message.</p>
<h2>HISTORY</h2>
<p> <code>Dist</code> originally used headers of the form &#8220;<i>Distribute-xxx:</i>&#8221; instead of &#8220;<i>Resent-xxx:</i>&#8221;. In order to conform with the ARPA Internet standard, RFC 822, the &#8220;<i>Resent-xxx:</i>&#8221; form is now used. <code>Dist</code> will recognize &#8220;<i>Distribute-xxx:</i>&#8221; type headers and automatically convert them to &#8220;<i>Resent-xxx:</i>&#8221;.</p>
<h2>BUGS</h2>
<p> <code>Dist</code> does not rigorously check the message being distributed for adherence to the transport standard, but <code>post</code> called by <code>send</code> does. The <code>post</code> program will balk (and rightly so) at poorly formatted messages, and <code>dist</code> won&#8217;t correct things for you. </p>
<p> If <i>whatnowproc</i> is <code>whatnow</code>, then <code>comp</code> uses a built-in <code>whatnow</code>, it does not actually run the <code>whatnow</code> program. Hence, if you define your own <i>whatnowproc</i>, don&#8217;t call it <code>whatnow</code> since <code>comp</code> won&#8217;t run it. </p>
<h2>Index</h2>
