---
title: "zarafa-set-oof(1)"
name: "zarafa-set-oof"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-set-oof/"
description: "zarafa-set-oof – Control a user’s out of office settings."
---

<h2 class="name">NAME</h2>
<p> zarafa-set-oof &#8211; Control a user&#8217;s out of office settings. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-set-oof</code> <i>USERNAME</i> <i>MODE</i> [<i>SUBJECT</i>] [<i>MESSAGE FILE</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>This tool can be used to change a user&#8217;s out of office settings. The Zarafa server must be running for <code>zarafa-set-oof</code> to work. </p>
<p> You must choose a state, enabled, disabled or don&#8217;t change, when using this script.</p>
<h2>ACTIONS</h2>
<p> zarafa-set-oof needs atleast a state command. Valid states are: </p>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Disable the user&#8217;s out of office reply.</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Enable the user&#8217;s out of office reply.</dl>
<p> <code>&#8211;</code></p>
<dl>
<dt>
<dd> Don&#8217;t enable or disable the user&#8217;s out of office reply. Just update the subject and message, unless the user&#8217;s out of office reply is enabled. </p>
<p> This is useful to update all out of office settings without enabling them and without changing the messages of enabled replies because that might overwrite some useful information that a user has set.</dl>
<h2>OPTIONS</h2>
<p> The options used by actions are as follows: </p>
<p> <code>SUBJECT</code></p>
<dl>
<dt>
<dd> Set a new subject for the oof message. This subject will be placed between square brackets when the message is sent.</dl>
<p> <code>MESSAGE FILE</code> <i>/path/to/message</i></p>
<dl>
<dt>
<dd> The contents of this file will be used as plain text body in the oof email.</dl>
<h2>AUTHOR</h2>
<p> Written by Zarafa. </p>
<h2>Index</h2>
