---
title: "repl(1)"
name: "repl"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repl/"
description: "repl – reply to a message"
---

<h2 class="name">NAME</h2>
<p> repl &#8211; reply to a message </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>repl</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-annotate</code> | <code>-noannotate</code>] [<code>-group</code> | <code>-nogroup</code>] [<code>-cc</code></p>
<dd>all/to/cc/me] [<code>-nocc</code> all/to/cc/me] [<code>-query</code> | <code>-noquery</code>] [<code>-form</code> <i>formfile</i>] [<code>-format</code> | <code>-noformat</code>] [<code>-filter</code> <i>filterfile</i>] [<code>-inplace</code> | <code>-noinplace</code>] [<code>-mime</code> | <code>-nomime</code>] [<code>-fcc</code> <i>+folder</i>] [<code>-width</code> <i>columns</i>] [<code>-draftfolder</code> <i>+folder</i>] [<code>-draftmessage</code> <i>msg</i>] [<code>-nodraftfolder</code>] [<code>-editor</code> <i>editor</i>] [<code>-noedit</code>] [<code>-whatnowproc</code> <i>program</i>] [<code>-nowhatnowproc</code>] [<code>-atfile</code>] [<code>-noatfile</code>] [<code>-fmtproc</code> <i>program</i>] [<code>-nofmtproc</code>] [<code>-build</code>] [<code>-file</code> <i>msgfile</i>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Repl</code> may be used to produce a reply to an existing message. </p>
<p> In its simplest form (with no arguments), <code>repl</code> will set up a message-form skeleton in reply to the current message in the current folder, and invoke the whatnow shell. </p>
<p> In order to construct the message draft of the reply, <code>repl</code> uses a reply template to guide its actions. A reply template is simply a <code>mhl</code> format file (see <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) for details). </p>
<p> If the switch <code>-nogroup</code> is given (it is on by default), then <code>repl</code> will use the standard forms file &#8220;replcomps&#8221;. This will construct a draft message that is intended to be sent only to the author of the message to which you are replying. If a file named &#8220;replcomps&#8221; exists in the user&#8217;s <code>nmh</code> directory, it will be used instead of this default forms file. </p>
<p> The default reply template &#8220;replcomps&#8221; will direct <code>repl</code> to construct the reply message draft as follows: </p>
<dl>
<dt>
<dd>
<pre><code>
To : &lt;Mail - Reply - To&gt; or &lt;Reply - To&gt; or &lt;From&gt; cc : &lt;To&gt; and&lt;cc&gt; and&lt;personal address&gt; Fcc:
{
    fcc switch
}
or +outbox Subject : Re : &lt;Subject&gt; In - Reply - To : &lt;Message - Id&gt; References : &lt;Message - Id&gt; Comments : In - Reply - To&lt;From&gt; or &lt;apparently from&gt; or &lt;Sender&gt;

                                                                                                                                                              &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
message dated&lt;date&gt; -- -- -- --
</code></pre>
</dl>
<p> where field names enclosed in angle brackets (&lt;&nbsp;<wbr>&gt;) indicate the contents of the named field from the message to which the reply is being made. </p>
<p> By default, the &#8220;cc:&#8221; field is empty. You may selectively add addresses to this default with the <code>-cc</code> <i>type</i> switch. This switch takes an argument (<i>all</i>/<i>to</i>/<i>cc</i>/<i>me</i>) which specifies who gets added to the default &#8220;cc:&#8221; list of the reply. You may give this switch multiple times (with different arguments) if you wish to add multiple types of addresses. </p>
<p> If the switch <code>-group</code> is given, then <code>repl</code> will use the standard forms file &#8220;replgroupcomps&#8221;. This will construct a draft message that is intended as a group or followup reply. If a file named &#8220;replgroupcomps&#8221; exists in the user&#8217;s nmh directory, it will be used instead of this default forms file, unless you specify another forms file on the command line or in your profile. </p>
<p> The default group reply template &#8220;replgroupcomps&#8221; will direct <code>repl</code> to construct the reply message draft as follows: </p>
<dl>
<dt>
<dd>
To : &lt;Mail &#8211; Followup &#8211; To&gt;<br />
         Subject : Re : &lt;Subject&gt;<br />
                            In &#8211;<br />
                        Reply &#8211; To : Message from&lt;From&gt; of&lt;Date&gt;.</p>
<p>                                         &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&lt;Message &#8211; Id&gt; &#8212; &#8212; &#8212; &#8212;
</dl>
<p> or if the field &lt;Mail-Followup-To&gt; is not available: </p>
<dl>
<dt>
<dd>
To : &lt;Mail &#8211; Reply &#8211; To&gt; or &lt;Reply &#8211; To&gt; or &lt;From&gt; cc : &lt;To&gt; and&lt;cc&gt; and&lt;personal address&gt; Subject : Re : &lt;Subject&gt; In &#8211; Reply &#8211; To : Message from&lt;From&gt; of&lt;Date&gt;.</p>
<p>                                                                                                                                          &amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&amp;nbsp;<br />
&lt;Message &#8211; Id&gt; &#8212; &#8212; &#8212; &#8212;
</dl>
<p> By default, the &#8220;cc:&#8221; contains all the addresses shown. You may selectively remove addresses from this default with the <code>-nocc</code> <i>type</i> switch. This switch takes an argument ( <i>all</i>/<i>to</i>/<i>cc</i>/<i>me</i>) which specifies who gets removed from the default &#8220;cc:&#8221; list of the reply. You may give this switch multiple times (with different arguments) if you wish to remove multiple types of addresses. </p>
<p> In any case, you may specify an alternate forms file with the switch <code>-form</code> <i>formfile</i>. </p>
<p> The <code>-query</code> switch modifies the action of <code>-nocc</code> <i>type</i> switch by interactively asking you if each address that normally would be placed in the &#8220;To:&#8221; and &#8220;cc:&#8221; list should actually be sent a copy. This is useful for special-purpose replies. Note that the position of the <code>-cc</code> and <code>-nocc</code> switches, like all other switches which take a positive and negative form, is important. </p>
<p> Lines beginning with the fields &#8220;To:&#8221;, &#8220;cc:&#8221;, and &#8221;Bcc:&#8221; will be standardized and have duplicate addresses removed. In addition, the <code>-width</code> <i>columns</i> switch will guide <code>repl</code>&#8216;s formatting of these fields. </p>
<p> If the draft already exists, <code>repl</code> will ask you as to the disposition of the draft. A reply of <code>quit</code> will abort <code>repl</code>, leaving the draft intact; <code>replace</code> will replace the existing draft with a blank skeleton; and <code>list</code> will display the draft. </p>
<p> See <i><a href="/docs/linux/man/1-comp/">comp</a></i>(1) for a description of the <code>-editor</code> and <code>-noedit</code> switches. Note that while in the editor, with <code>-atfile</code> and if the current directory is writable, the message being replied to is available through a link named &#8220;@&#8221; (assuming the default <i>whatnowproc</i>). In addition, the actual pathname of the message is stored in the environment variable <code>$editalt</code>, and the pathname of the folder containing the message is stored in the environment variable <code>$mhfolder</code>. The creation of the &#8220;@&#8221; file is controlled via the <code>-atfile</code> and <code>-noatfile</code> options. </p>
<p> Although <code>repl</code> uses a forms file to direct it how to construct the beginning of the draft, it uses a message filter file to direct it as to how the message to which you are replying should be filtered (re-formatted) in the body of the draft. The filter file for <code>repl</code> should be a standard form file for <code>mhl</code>, as <code>repl</code> will invoke <code>mhl</code> to format the message to which you are replying. </p>
<p> The switches <code>-noformat</code>, <code>-format</code>, and <code>-filter</code> <i>filterfile</i> specify which message filter file to use. </p>
<p> If the switch <code>-noformat</code> is given (it is the default), then the message to which you are replying is not included in the body of the draft. </p>
<p> If the switch <code>-format</code> is given, then a default message filter file is used. This default message filter should be adequate for most users. This default filter &#8220;<i>mhl.reply</i>&#8221; is: </p>
<dl>
<dt>
<dd>
;<br />
mhl.reply;<br />
; default message filter for `repl&#8217; (repl -format)<br />
;<br />
from : nocomponent, formatfield = &#8220;%(decode(friendly{text})) writes:&#8221; body : component = &#8220;&gt; &#8220;, overflowtext = &#8220;&gt; &#8220;, overflowoffset = 0
</dl>
<p> which outputs each line of the body of the message prefaced with the &#8220;&gt;&#8221; character and a space. </p>
<p> If a file named &#8220;<i>mhl.reply</i>&#8221; exists in the user&#8217;s <code>nmh</code> directory, it will be used instead of this form. You may specify an alternate message filter file with the switch <code>-filter</code> <i>filterfile</i>. </p>
<p> Other reply filters are commonly used, such as: </p>
<dl>
<dt>
<dd>
<pre>
:
body:nocomponent,compwidth=9,offset=9
</pre>
</dl>
<p> which says to output a blank line and then the body of the message being replied-to, indented by one tab-stop. Another popular format is: </p>
<dl>
<dt>
<dd>
<pre><code>
message - id : nocomponent, nonewline,
    formatfield =``In message % {text}, &amp;nbsp;
'' from : nocomponent, formatfield =``% (decode(friendly{text}))writes :'' body : component =``&gt;'', overflowtext =``&gt;'', overflowoffset = 0
</code></pre>
</dl>
<p> This message filter file cites the Message-ID and author of the message being replied-to, and then outputs each line of the body prefaced with the &#8220;&gt;&#8221; character. </p>
<p> You can also use an external format program to format the message body. The format program is specified by the <i>formatproc</i> profile entry, and is enabled by the &#8220;format&#8221; flag. A message filter using an external format program would look like this: </p>
<dl>
<dt>
<dd>
<pre>
body:component=``&gt;'',nowrap,format
</pre>
</dl>
<p> See the <i><a href="/docs/linux/man/1-mhl/">mhl</a>(1)</i> documentation for more information. The format program can be changed by the <code>-fmtproc</code> <i>program</i> and <code>-nofmtproc</code> switches. </p>
<p> To use the MIME rules for encapsulation, specify the <code>-mime</code> switch. This directs <code>repl</code> to generate an <code>mhbuild</code> composition file. Note that <code>nmh</code> will not invoke <code>mhbuild</code> automatically; you must specifically give the command </p>
<dl>
<dt>
<dd> What now? mime</dl>
<p> prior to sending the draft. </p>
<p> If the <code>-annotate</code> switch is given, the message being replied-to will be annotated with the lines </p>
<dl>
<dt>
<dd> Replied: date Replied: addrs</dl>
<p> where the address list contains one line for each addressee. The annotation will be done only if the message is sent directly from <code>repl</code>. If the message is not sent immediately from <code>repl</code>, &#8220;<code>comp -use</code>&#8221; may be used to re-edit and send the constructed message, but the annotations won&#8217;t take place. Normally annotations are done inplace in order to preserve any links to the message. You may use the <code>-noinplace</code> switch to change this. </p>
<p> Although the default template specifies that a copy of the reply will be put in the folder &#8216;outbox&#8217;, if the <code>-fcc</code> <i>+folder</i> switch is given it will override the default value. More than one folder, each preceded by <code>-fcc</code> can be named. </p>
<p> In addition to the standard <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) escapes, <code>repl</code> also recognizes the following additional <i>component</i> escape: </p>
<dl>
<dt>
<dd>
<pre>
<i>Escape Returns  Description</i>
fcc     string   Any folders specified with `-fcc folder'
</pre>
</dl>
<p> To avoid reiteration, <code>repl</code> strips any leading `Re: &#8216; strings from the <i>subject</i> component. </p>
<p> The <code>-draftfolder</code> <i>+folder</i> and <code>-draftmessage</code> <i>msg</i> switches invoke the <code>nmh</code> draft folder facility. This is an advanced (and highly useful) feature. Consult the <i><a href="/docs/linux/man/5-mh-draft/">mh-draft</a></i>(5) man page for more information. </p>
<p> Upon exiting from the editor, <code>repl</code> will invoke the <code>whatnow</code> program. See <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1) for a discussion of available options. The invocation of this program can be inhibited by using the <code>-nowhatnowproc</code> switch. (In truth of fact, it is the <code>whatnow</code> program which starts the initial edit. Hence, <code>-nowhatnowproc</code> will prevent any edit from occurring.) </p>
<p> The <code>-build</code> switch is intended to be used by the Emacs mh-e interface to <code>nmh</code>. It implies <code>-nowhatnowproc</code>. It causes a file <i>&lt;mh-dir&gt;/reply</i> to be created, containing the draft message that would normally be presented to the user for editing. No mail is actually sent. </p>
<p> The <code>-file</code> <i>msgfile</i> switch specifies the message to be replied to as an exact filename rather than as an <code>nmh</code> folder and message number. It is intended to be used by the <code>msh</code> interface to <code>nmh</code>. The same caveats apply to this option as to the <code>-build</code> switch.</p>
<h2>FILES</h2>
<p> <code>repl</code> looks for all format, filter and template files in multiple locations: absolute pathnames are accessed directly, tilde expansion is done on usernames, and files are searched for in the user&#8217;s <i>Mail</i> directory as specified in their profile. If not found there, the directory &#8220;<i>/etc/nmh</i>&#8221; is checked. </p>
<pre>
^/etc/nmh/replcomps~^The standard reply template
^or &lt;mh-dir&gt;/replcomps~^Rather than the standard template
^/etc/nmh/replgroupcomps~^The standard `reply -group' template
^or &lt;mh-dir&gt;/replgroupcomps~^Rather than the standard template
^/etc/nmh/mhl.reply~^The standard message filter
^or &lt;mh-dir&gt;/mhl.reply~^Rather than the standard filter
^$HOME/.mh_profile~^The user profile
^&lt;mh-dir&gt;/draft~^The draft file
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Alternate-Mailboxes:~^To determine the user's mailboxes
^Current-Folder:~^To find the default current folder
^Draft-Folder:~^To find the default draft-folder
^Editor:~^To override the default editor
^Msg-Protect:~^To set mode when creating a new message (draft)
^fileproc:~^Program to refile the message
^mhlproc:~^Program to filter message being replied-to
^whatnowproc:~^Program to ask the ``What now?'' questions
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-comp/">comp</a></i>(1), <i><a href="/docs/linux/man/1-forw/">forw</a></i>(1), <i><a href="/docs/linux/man/1-mhbuild/">mhbuild</a></i>(1), <i><a href="/docs/linux/man/1-send/">send</a></i>(1), <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1), <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder
`<code>msg</code>' defaults to cur
`<code>-nogroup</code>'
`<code>-nocc all</code>' with `-nogroup', `-cc all' with `-group'
`<code>-noannotate</code>'
`<code>-nodraftfolder</code>'
`<code>-noformat</code>'
`<code>-inplace</code>'
`<code>-nomime</code>'
`<code>-noquery</code>'
`<code>-noatfile</code>'
`<code>-width 72</code>'
</pre>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. The message replied-to will become the current message.</p>
<h2>BUGS</h2>
<p> If any addresses occur in the reply template, addresses in the template that do not contain hosts are defaulted incorrectly. Instead of using the localhost for the default, <code>repl</code> uses the sender&#8217;s host. Moral of the story: if you&#8217;re going to include addresses in a reply template, include the host portion of the address. </p>
<p> The <code>-width</code> <i>columns</i> switch is only used to do address-folding; other headers are not line-wrapped. </p>
<p> If <i>whatnowproc</i> is <code>whatnow</code>, then <code>repl</code> uses a built-in <code>whatnow</code>, it does not actually run the <code>whatnow</code> program. Hence, if you define your own <i>whatnowproc</i>, don&#8217;t call it <code>whatnow</code> since <code>repl</code> won&#8217;t run it. </p>
<h2>Index</h2>
