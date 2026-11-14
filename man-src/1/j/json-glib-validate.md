---
title: "json-glib-validate(1)"
name: "json-glib-validate"
section: "1"
letter: "j"
url: "/docs/linux/man/1-json-glib-validate/"
description: "json-glib-validate – JSON-GLib validation tool"
---

<h2 class="name">NAME</h2>
<p> json-glib-validate &#8211; JSON-GLib validation tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>json-glib-validate</code> [<code>-h</code>,&nbsp;<wbr><code>&#8211;help</code>] URI [URI&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>json-glib-validate</code></p>
<dd>offers a simple command line interface to validate JSON data. It lets you list URIs that point to JSON data and checks that the data conforms to the JSON syntax. </p>
<p> The resources to operate on are specified by the <i>URI</i> argument. </p>
<p> If the JSON data is valid, <code>json-glib-validate</code> will terminate with an exit code of 0; if the data is invalid, an error will be printed on <i>stderr</i> and <code>json-glib-validate</code> will terminate with a nonzero exit code.</p>
<h2>COMMANDS</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints help and exits.</dl>
<h2>Index</h2>
