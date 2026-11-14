---
title: "arara(1)"
name: "arara"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arara/"
description: "arara – a TeX automation tool based on rules and directives."
---

<h2 class="name">NAME</h2>
<p> arara &#8211; a TeX automation tool based on rules and directives. </p>
<h2>SYNOPSIS</h2>
<p> <code>arara</code> [<i>options</i>] <i>documents</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>arara</code> is a TeX automation tool based on rules and directives. It gives you a way to enhance your TeX experience. The tool is an effort to provide a concise way to automate the daily TeX workflow for users and also package writers. Users might write their own rules when the provided ones do not suffice. </p>
<p> arara takes a list of documents as input. They will be processed according to their directives. Options apply to the execution of all documents.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;log</code></p>
<dd> Generate a log output.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Print or suppress command output.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Go through all the motions of running a command but with no actual calls.</p>
<dt><code>&#8211;safe-run</code></p>
<dd> Run in safe mode and disable potentially harmful features.</p>
<dt><code>&#8211;header</code></p>
<dd> Extract directives only in the file header.</p>
<dt><code>&#8211;preamble</code></p>
<dd> Set the file preamble as named based on the configuration file.</p>
<dt><code>&#8211;timeout</code></p>
<dd> Sets an execution timeout for spawned processes.</p>
<dt><code>&#8211;language</code></p>
<dd> Set the localization to the language specified by code.</p>
<dt><code>&#8211;max-loops</code></p>
<dd> Set the number &gt; 0 of loops for looping directives.</p>
<dt><code>&#8211;working-directory</code></p>
<dd> Set the working directory for the whole execution.</p>
<dt><code>&#8211;call-property</code></p>
<dd> Pass a property as key=value parameter into the application to be used within the session.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> Show a help message and exit.</dl>
<h2>BUGS</h2>
<p> Issue tracker at </p>
<h2>Index</h2>
