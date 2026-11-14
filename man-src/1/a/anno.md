---
title: "anno(1)"
name: "anno"
section: "1"
letter: "a"
url: "/docs/linux/man/1-anno/"
description: "anno – annotate messages"
---

<h2 class="name">NAME</h2>
<p> anno &#8211; annotate messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>anno</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-component</code> <i>field</i>] [<code>-inplace</code> | <code>-noinplace</code>] [<code>-date</code> | <code>-nodate</code>] [<code>-draft</code>] [<code>-append</code>] [<code>-list</code>] [<code>-delete</code>] [<code>-number</code> <i>[</i>num|all<i>]]</i> [<code>-preserve</code> | <code>-nopreserve</code>] [<code>-version</code>] [<code>-help</code>] [<code>-text</code> <i>body</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Anno</code></p>
<dd>manipulates header fields or <i>annotations</i> in messages. Header fields consist of a field name and an optional field body as defined by RFC 2822. The <code>-component</code> option specifies the field name, and the <code>-text</code> option specifies the field body. </p>
<p> The messages are either the <i>msgs</i> in the named folder, or the draft if invoked with the <code>-draft</code> option. </p>
<p> Usually, annotation is performed by the commands <code>dist</code>, <code>forw</code>, and <code>repl</code>, if they are given the <code>-anno</code> switch. This allows you to keep track of your distribution of, forwarding of, and replies to a message. </p>
<p> By using <code>anno</code>, you can perform arbitrary annotations of your own. Each message selected will be annotated with the lines </p>
<p>&nbsp;<wbr>field: date<br />
&nbsp;<wbr>field: body </p>
<p> The <code>-nodate</code> switch inhibits the date annotation, leaving only the body annotation. </p>
<p> By default, <code>anno</code> prepends the annotations to the message. Annotations are instead appended if the <code>-append</code> option is specified. </p>
<p> If a <code>-component</code> <i>field</i> is not specified when <code>anno</code> is invoked, <code>anno</code> will prompt the user for the name of field for the annotation. </p>
<p> The field specified must be a valid RFC 2822-style message field name, which means that it may only consist of alphanumerics and dashes. The body specified is arbitrary text. </p>
<p> Normally <code>anno</code> does the annotation inplace in order to preserve any links to the message. You may change this by using the <code>-noinplace</code> switch. </p>
<p> The <code>-list</code> option produces a listing of the field bodies for header fields with names matching the specified component, one per line. The listing is numbered, starting at 1, if the <code>-number</code> option is also used. A tab character separates the number and the field body. The field body is treated as if it is a file name, and only the final path name component is listed. The complete field body is listed if the <code>-text</code> option is used, the contents of the text are ignored. </p>
<p> The <code>-delete</code> option removes header fields from messages. The first header field whose name matches the component is deleted if no other options are specified. If the <code>-text</code> option is used in conjunction with the <code>-delete</code> option, the first header field whose name matches the component and whose body matches the text is deleted. The text is treated as if it was a file name; if it begins with a slash, the entire field body must match the text, otherwise just the last path name component of the field body must match. If the <code>-number</code> option is used in conjuction with the <code>-delete</code> option, header field <i>num</i> whose name matches the component is deleted. The number matches that which is produced by the <code>-list</code> option. The special value <code>all</code> can be used for the number, and causes all components that match the name to be deleted. </p>
<p> By default, <code>anno</code> changes the last-accessed and last-modified times on annotate messages to the time at which the annotation occurs. <code>Anno</code> preserves the original times if the <code>-preserve</code> option is used. A matching <code>-nopreserve</code> option exists that allows time preservation to be turned off if enabled in the profile.</p>
<h2>FILES</h2>
<dl>
<dt>$HOME/.mh_profile</p>
<dd> The user&#8217;s profile.</dl>
<h2>PROFILE COMPONENTS</h2>
<dl>
<dt>Path:</p>
<dd> To determine the user&#8217;s nmh directory.</p>
<dt>Current-Folder:</p>
<dd> To find the default current folder.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dist/">dist</a></i>(1), <i><a href="/docs/linux/man/1-forw/">forw</a></i>(1), <i><a href="/docs/linux/man/1-repl/">repl</a></i>(1)</p>
<h2>DEFAULTS</h2>
<dl>
<dt>+folder</p>
<dd> The current folder.</p>
<dt>msgs</p>
<dd> The current message.</p>
<dt>-inplace</p>
<dd>
<dt>-date</p>
<dd></dl>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder. The first message annotated will become the current message. </p>
<h2>Index</h2>
