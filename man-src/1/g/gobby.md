---
title: "gobby(1)"
name: "gobby"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gobby/"
description: "gobby – a collaborative text editor"
---

<h2 class="name">NAME</h2>
<p> <code>gobby</code> &#8211; a collaborative text editor </p>
<h2>SYNOPSIS</h2>
<p> <code>gobby</code> [<i>options</i>] [<i>file(s)</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>gobby</code> is an editor which allows to edit text documents and source files collaboratively over a network. Changes to the documents are syncronised instantly to the other clients. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-j</code>, <code>&#8211;join</code>=<i>HOST</i>:<i>PORT</i></p>
<dd> Joins the obby session on the specified host.</p>
<dt><code>-n</code>, <code>&#8211;new-instance</code></p>
<dd> Forces a new instance of Gobby to be created.</p>
<dt><code>file(s)</code></p>
<dd> Files passed on the command line will be opened within Gobby. If there is already a Gobby instance running they will be opened therein, otherwise a new hosted session will be created automatically.</dl>
<h2>AUTHOR</h2>
<p> <code>gobby</code> was written by the 0x539 dev group &lt;crew [at] 0x539.de&gt;. </p>
<h2>Index</h2>
