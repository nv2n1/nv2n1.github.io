---
title: "forw(1)"
name: "forw"
section: "1"
letter: "f"
url: "/docs/linux/man/1-forw/"
description: "forw – forward messages"
---

<h2 class="name">NAME</h2>
<p> forw &#8211; forward messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>forw</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-annotate</code> | <code>-noannotate</code>] [<code>-form</code> <i>formfile</i>] [<code>-format</code> | <code>-noformat</code>] [<code>-filter</code> <i>filterfile</i>] [<code>-inplace</code> | <code>-noinplace</code>] [<code>-mime</code> | <code>-nomime</code>] [<code>-draftfolder</code> <i>+folder</i>] [<code>-draftmessage</code> <i>msg</i>] [<code>-nodraftfolder</code>] [<code>-editor</code> <i>editor</i>] [<code>-noedit</code>] [<code>-width</code> <i>colums</i>] [<code>-from</code> <i>address</i>] [<code>-to</code> <i>address</i>] [<code>-cc</code> <i>address</i>] [<code>-fcc</code> <i>+folder</i>] [<code>-subject</code> <i>text</i>] [<code>-whatnowproc</code> <i>program</i>] [<code>-nowhatnowproc</code>] [<code>-dashstuffing</code> | <code>-nodashstuffing</code>] [<code>-build</code>] [<code>-file</code> <i>msgfile</i>] [<code>-version</code>] [<code>-help</code>]</dl>
<dl>
<dt> <code>forw</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-digest</code> <i>list</i>] [<code>-issue</code> <i>number</i>] [<code>-volume</code> <i>number</i>] [other switches for&nbsp;<wbr> <code>forw</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Forw</code></p>
<dd>may be used to prepare a message containing other messages. </p>
<p> It constructs the new message from a forms (components) file, with a body composed of the message(s) to be forwarded. An editor is invoked as in <code>comp</code>, and after editing is complete, the user is prompted before the message is sent. </p>
<p> The default message template will direct <code>forw</code> to construct the draft as follows: </p>
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
        Fcc:
{
    fcc switch
}
or +outbox
        Subject:
{
    subject switch
}
or "{original subject} (fwd)" -- -- -- --
</code></pre>
</dl>
<p> If a file named &#8220;<i>forwcomps</i>&#8221; exists in the user&#8217;s nmh directory, it will be used instead of this default form. You may also specify an alternate forms file with the switch <code>-form</code> <i>formfile</i>. Forms are processed via the <code>nmh</code> template system; see <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) for details. Components from the first forwarded message are available as standard component escapes in the forms file. </p>
<p> In addition to the standard <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) escapes, the following <i>component</i> escapes are also supported: </p>
<dl>
<dt>
<dd>
<pre>
<i>Escape     Returns Description</i>
fcc         string  Any folders specified with `-fcc folder'
nmh-from    string  Addresses specified with `-from address'
nmh-to      string  Addresses specified with `-to address'
nmh-cc      string  Addresses specified with `-cc address'
nmh-subject string  Any text specified with `-subject text'
</pre>
</dl>
<p> By default the &#8220;To:&#8221; and &#8220;cc:&#8221; fields are empty. You may add addresses to these fields with the <code>-to</code> <i>address</i> and <code>-cc</code> <i>address</i> switches. You may give these switches multiple times to add multiple addresses. </p>
<p> By default the &#8220;From:&#8221; field has either the value of the <code>Local-Mailbox</code> profile entry a system default email address. This default can be overridden by using the <code>-from</code> <i>address</i> switch. The default mailbox in the &#8220;Fcc:&#8221; field is <i>+outbox</i>. This can be overridden by the <code>-fcc</code> switch. </p>
<p> Any text you give to the <code>-subject</code> switch will be placed in the &#8220;Subject:&#8221; field in the draft. </p>
<p> If the draft already exists, <code>forw</code> will ask you as to the disposition of the draft. A reply of <code>quit</code> will abort <code>forw</code>, leaving the draft intact; <code>replace</code> will replace the existing draft with a blank skeleton; and <code>list</code> will display the draft. </p>
<p> If the <code>-annotate</code> switch is given, each message being forwarded will be annotated with the lines: </p>
<dl>
<dt>
<dd>
<pre>
Forwarded: date
Forwarded: addrs
</pre>
</dl>
<p> where each address list contains as many lines as required. This annotation will be done only if the message is sent directly from <code>forw</code>. If the message is not sent immediately from <code>forw</code>, &#8220;<code>comp</code> <code>-use</code>&#8221; may be used to re-edit and send the constructed message, but the annotations won&#8217;t take place. Normally annotations are done inplace in order to preserve any links to the message. You may change this by using the <code>-noinplace</code> switch. </p>
<p> See <i><a href="/docs/linux/man/1-comp/">comp</a></i>(1) for a description of the <code>-editor</code> and <code>-noedit</code> switches. </p>
<p> Although <code>forw</code> uses a forms (components) file to direct it how to construct the beginning of the draft, it uses a message filter file to direct it as to how each forwarded message should be formatted in the body of the draft. The filter file for <i>forw</i> should be a standard form file for <code>mhl</code>, as <code>forw</code> will invoke <code>mhl</code> to filter (re-format) the forwarded messages prior to being output to the body of the draft. </p>
<p> The switches <code>-noformat</code>, <code>-format</code>, and <code>-filter</code> <i>filterfile</i> specify which message filter file to use. </p>
<p> If <code>-noformat</code> is specified (this is the default), then each forwarded message is output into the draft exactly as it appears with no <code>mhl</code> filtering. </p>
<p> If <code>-format</code> is specified, then a default message filter file is used. This default message filter should be adequate for most users. This default filter &#8220;<i>mhl.forward</i>&#8221; is: </p>
<dl>
<dt>
<dd>
<pre><code>
;
mhl.forward;
; default message filter for `forw' (forw -format)
;
width = 80, overflowtext =, overflowoffset = 10 leftadjust, compress, compwidth = 9 Date : formatfield = "%&lt;(nodate{text})%{text}%|%(tws{text})%&gt;" From : To : cc : Subject : : body : nocomponent, overflowoffset = 0, noleftadjust, nocompress
</code></pre>
</dl>
<p> If a file named &#8220;<i>mhl.forward</i>&#8221; exists in the user&#8217;s nmh directory, it will be used instead of this form. You may specify an alternate message filter file with the switch <code>-filter</code> <i>filterfile</i>. </p>
<p> Each forwarded message is separated with an encapsulation delimiter. By default, any dashes in the first column of the forwarded messages will be prepended with `-&nbsp;<wbr>&#8216; so that when received, the message is suitable for bursting by <code>burst</code>. This follows the Internet RFC 934 guidelines. You may use the flag <code>-nodashstuffing</code> in order to suppress this form of quoting to the forwarded messages. </p>
<p> For users of <code>prompter</code>, by specifying <code>prompter</code>&#8216;s <code>-prepend</code> switch in the <i>.mh_profile</i> file, any commentary text is entered before the forwarded messages. (A major win!) </p>
<p> To use the MIME rules for encapsulation, specify the <code>-mime</code> switch. This directs <code>forw</code> to generate an <code>mhbuild</code> composition file. Note that <code>nmh</code> will not invoke <code>mhbuild</code> automatically; you must specifically give the command </p>
<dl>
<dt>
<dd>
<pre>
What now? mime
</pre>
</dl>
<p> prior to sending the draft. </p>
<p> The <code>-draftfolder</code> <i>+folder</i> and <code>-draftmessage</code> <i>msg</i> switches invoke the <code>nmh</code> draft folder facility. This is an advanced (and highly useful) feature. Consult the <i><a href="/docs/linux/man/5-mh-draft/">mh-draft</a></i>(5) man page for more information. </p>
<p> The <code>-editor</code> <i>editor</i> switch indicates the editor to use for the initial edit. Upon exiting from the editor, <code>comp</code> will invoke the <code>whatnow</code> program. See <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1) for a discussion of available options. The invocation of this program can be inhibited by using the <code>-nowhatnowproc</code> switch. (In truth of fact, it is the <i>whatnow</i> program which starts the initial edit. Hence, <code>-nowhatnowproc</code> will prevent any edit from occurring.) </p>
<p> The <code>-build</code> switch is intended to be used by the Emacs mh-e interface to <code>nmh</code>. It implies <code>-nowhatnowproc</code>. It causes a file &lt;mh-dir&gt;/draft to be created, containing the draft message that would normally be presented to the user for editing. No mail is actually sent. </p>
<p> The <code>-file</code> <i>msgfile</i> switch specifies the message to be forwarded as an exact filename rather than as an <code>nmh</code> folder and message number. It is intended to be used by the <code>msh</code> interface to <code>nmh</code>. This switch implies <code>-noannotate</code>. The forwarded message is simply copied verbatim into the draft; the processing implied by the <code>-filter</code>, <code>-mime</code>, and <code>-digest</code> switches is bypassed, and the usual leading and trailing &#8216;Forwarded Message&#8217; delimiters are not added. The same caveats apply to this option as to the <code>-build</code> switch. </p>
<p> The <code>-digest</code> <i>list</i>, <code>-issue</code> <i>number</i>, and <code>-volume</code> <i>number</i> switches implement a digest facility for <code>nmh</code>. Specifying these switches enables and/or overloads the following escapes: </p>
<dl>
<dt>
<dd>
<pre>
<i>Type      Escape  Returns  Description</i>
component  digest  string   Argument to `-digest'
function   cur     integer  Argument to `-volume'
function   msg     integer  Argument to `-issue'
</pre>
</dl>
<p> Consult the <i>Advanced Features</i> section of the <code>nmh</code> User&#8217;s Manual for more information on making digests.</p>
<h2>FILES</h2>
<p> <code>forw</code> looks for format and filter files in multiple locations: absolute pathnames are accessed directly, tilde expansion is done on usernames, and files are searched for in the user&#8217;s <i>Mail</i> directory as specified in their profile. If not found there, the directory &#8220;<i>/etc/nmh</i>&#8221; is checked. </p>
<dl>
<dt>/etc/nmh/forwcomps</p>
<dd> The standard message skeleton.</p>
<dt>&lt;mh-dir&gt;/forwcomps</p>
<dd> Rather than the standard skeleton.</p>
<dt>/etc/nmh/digestcomps</p>
<dd> The message skeleton if <code>-digest</code> is given.</p>
<dt>&lt;mh-dir&gt;/digestcomps</p>
<dd> Rather than the standard skeleton.</p>
<dt>^/etc/nmh/mhl.forward</p>
<dd> The standard message filter.</p>
<dt>&lt;mh-dir&gt;/mhl.forward</p>
<dd> Rather than the standard filter.</p>
<dt>^$HOME/.mh_profile</p>
<dd> The user&#8217;s profile.</dl>
<h2>PROFILE COMPONENTS</h2>
<dl>
<dt>Path:</p>
<dd> To determine the user&#8217;s nmh directory.</p>
<dt>Current-Folder:</p>
<dd> To find the default current folder.</p>
<dt>Draft-Folder:</p>
<dd> To find the default draft-folder.</p>
<dt>Editor:</p>
<dd> To override the default editor.</p>
<dt>Msg-Protect:</p>
<dd> To set mode when creating a new message (draft).</p>
<dt>fileproc:</p>
<dd> Program to refile the message.</p>
<dt>mhlproc:</p>
<dd> Program to filter messages being forwarded.</p>
<dt>whatnowproc:</p>
<dd> Program to ask the &#8220;What now?&#8221; questions.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-comp/">comp</a></i>(1), <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1), <i><a href="/docs/linux/man/1-repl/">repl</a></i>(1), <i><a href="/docs/linux/man/1-send/">send</a></i>(1), <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1), <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) </p>
<p> <i>Proposed Standard for Message Encapsulation</i> (RFC 934)</p>
<h2>DEFAULTS</h2>
<dl>
<dt>+folder</p>
<dd> The current folder.</p>
<dt>msgs</p>
<dd> The current message.</p>
<dt>-noannotate</p>
<dd>
<dt>-nodraftfolder</p>
<dd>
<dt>-noformat</p>
<dd>
<dt>-inplace</p>
<dd>
<dt>-dashstuffing</p>
<dd>
<dt>-nomime</p>
<dd></dl>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. The first message forwarded will become the current message.</p>
<h2>BUGS</h2>
<p> If <i>whatnowproc</i> is <code>whatnow</code>, then <code>forw</code> uses a built-in <code>whatnow</code>, it does not actually run the <code>whatnow</code> program. Hence, if you define your own <i>whatnowproc</i>, don&#8217;t call it <code>whatnow</code> since <code>forw</code> won&#8217;t run it. </p>
<p> When <code>forw</code> is told to annotate the messages it forwards, it doesn&#8217;t actually annotate them until the draft is successfully sent. If from the <i>whatnowproc</i>, you <code>push</code> instead of <code>send</code>, it&#8217;s possible to confuse <code>forw</code> by re-ordering the file (e.g. by using &#8220;<code>folder</code> <code>-pack</code>&#8221;) before the message is successfully sent. <code>Dist</code> and <code>repl</code> don&#8217;t have this problem. </p>
<h2>Index</h2>
