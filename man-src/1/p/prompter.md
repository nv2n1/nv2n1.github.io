---
title: "prompter(1)"
name: "prompter"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prompter/"
description: "prompter – prompting editor front-end for nmh"
---

<h2 class="name">NAME</h2>
<p> prompter &#8211; prompting editor front-end for nmh </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>prompter</code> [<code>-erase</code> <i>chr</i>] [<code>-kill</code> <i>chr</i>] [<code>-prepend</code> | <code>-noprepend</code>] [<code>-rapid</code> | <code>-norapid</code>] [<code>-doteof</code> | <code>-nodoteof</code>] <i>file</i> [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Prompter</code></p>
<dd>is an editor front-end for <code>nmh</code> which allows rapid composition of messages. This program is not normally invoked directly by users but takes the place of an editor and acts as an editor front-end. It operates on an RFC 822 style message draft skeleton specified by <i>file</i>, normally provided by the <code>nmh</code> commands <code>comp</code>, <code>dist</code>, <code>forw</code>, or <code>repl</code>. </p>
<p> <code>Prompter</code> is particularly useful when composing messages over slow network or modem lines. It is an <code>nmh program in that it can have</code> its own profile entry with switches, but it is not invoked directly by the user. The commands <code>comp</code>, <code>dist</code>, <code>forw</code>, and <code>repl</code> invoke <code>prompter as an editor, either when invoked with</code> <code>-editor</code> <i>prompter</i>, or by the profile entry &#8220;Editor: prompter&#8221;, or when given the command <code>edit</code> <code>prompter</code> at the &#8220;What now?&#8221; prompt. </p>
<p> For each empty component <code>prompter finds in the draft, the user</code> is prompted for a response; A &lt;RETURN&gt; will cause the whole component to be left out. Otherwise, a `\&#8217; preceding a &lt;RETURN&gt; will continue the response on the next line, allowing for multiline components. Continuation lines <code>must</code> begin with a space or tab. </p>
<p> Each non-empty component is copied to the draft and displayed on the terminal. </p>
<p> The start of the message body is denoted by a blank line or a line of dashes. If the body is non-empty, the prompt, which isn&#8217;t written to the file, is </p>
<dl>
<dt>
<dd> &#8212;&#8212;&#8211;Enter additional text</dl>
<p> or (if <code>-prepend</code> was given) </p>
<dl>
<dt>
<dd> &#8212;&#8212;&#8211;Enter initial text</dl>
<p> Message-body typing is terminated with an end-of-file (usually CTRL-D). With the <code>-doteof</code> switch, a period on a line all by itself also signifies end-of-file. At this point control is returned to the calling program, where the user is asked &#8220;What now?&#8221;. See <code>whatnow (1)</code> for the valid options to this query. </p>
<p> By using the <code>-prepend</code> switch, the user can add type-in to the beginning of the message body and have the rest of the body follow. This is useful for the <code>forw</code> command. </p>
<p> By using the <code>-rapid</code> switch, if the draft already contains text in the message-body, it is not displayed on the user&#8217;s terminal. This is useful for low-speed terminals. </p>
<p> The line editing characters for kill and erase may be specified by the user via the arguments <code>-kill</code> <i>chr</i> and <code>-erase</code> <i>chr</i>, where <i>chr</i> may be a character; or `
nn&#8217;, where &#8220;nnn&#8221; is the octal value for the character. </p>
<p> An interrupt (usually CTRL-C) during component typing will abort <code>prompter</code> and the <code>nmh</code> command that invoked it. An interrupt during message-body typing is equivalent to CTRL-D, for historical reasons. This means that <code>prompter</code> should finish up and exit. </p>
<p> The first non-flag argument to <code>prompter is taken as the name of</code> the draft file, and subsequent non-flag arguments are ignored.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
^/tmp/prompter*~^Temporary copy of message
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
prompter-next:       To name the editor to be used on exit from .B prompter
^Msg-Protect:~^To set mode when creating a new draft
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-comp/">comp</a></i>(1), <i><a href="/docs/linux/man/1-dist/">dist</a></i>(1), <i><a href="/docs/linux/man/1-forw/">forw</a></i>(1), <i><a href="/docs/linux/man/1-repl/">repl</a></i>(1), <i><a href="/docs/linux/man/1-whatnow/">whatnow</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-prepend</code>'
`<code>-norapid</code>'
`<code>-nodoteof</code>'
</pre>
<h2>CONTEXT</h2>
<p> None</p>
<h2>HELPFUL HINTS</h2>
<p> The <code>-rapid</code> option is particularly useful with <code>forw</code>, and <code>-noprepend</code> is useful with <code>comp</code> <code>-use</code>. </p>
<p> The user may wish to link <code>prompter under several names (e.g.,</code> &#8220;rapid&#8221;) and give appropriate switches in the profile entries under these names (e.g., &#8220;rapid: -rapid&#8221;). This facilitates invoking prompter differently for different <code>nmh</code> commands (e.g., &#8220;forw: -editor rapid&#8221;).</p>
<h2>BUGS</h2>
<p> <code>Prompter</code> uses <i><a href="/docs/linux/man/3-stdio/">stdio</a></i>(3), so it will lose if you edit files with nulls in them. </p>
<h2>Index</h2>
