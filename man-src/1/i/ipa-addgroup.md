---
title: "ipa-addgroup(1)"
name: "ipa-addgroup"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-addgroup/"
description: "ipa-addgroup – Add a group"
---

<h2>NAME</h2>
<p> ipa-addgroup &#8211; Add a group </p>
<h2>SYNOPSIS</h2>
<p> ipa-addgroup [<i>OPTION</i>]&#8230; <i>group</i> </p>
<h2>DESCRIPTION</h2>
<p> Adds a group with name <i>group</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;description</code>=<i>description</i></p>
<dd> Set the description of the group to <i>description</i>.</p>
<dt><code>-g</code>, <code>&#8211;gid</code>=<i>gid</i></p>
<dd> Set the gid for this group to <i>gid</i>. If this option is not present, one is created automatically by <code>freeIPA</code>.</p>
<dt><code>&#8211;addattr</code> <i>attr=value</i></p>
<dd> Adds <i>value</i> to attribute <i>attr</i>. Attributes set this way are done after other options. If an attribute is listed more than once or already exists in the entry, it is considered a multi-valued attribute and a list of the values is created.</p>
<dt><code>&#8211;setattr</code> <i>attr=value</i></p>
<dd> Set attribute <i>attr</i> to <i>value</i>. Any existing value will be replaced with <i>value</i>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display the XML-RPC request and response for more verbose debugging output.</dl>
<p> The group name and description are mandatory fields. If either of these are not included on the command line you will be asked interactively. </p>
<p> If no options are passed then all questions are asked.</p>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
