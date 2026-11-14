---
title: "addwords(1)"
name: "addwords"
section: "1"
letter: "a"
url: "/docs/linux/man/1-addwords/"
description: "addwords – Adding words to specified dictionary collectively"
---

<h2>NAME</h2>
<p> addwords &#8211; Adding words to specified dictionary collectively</p>
<h2>SYNOPSIS</h2>
<p> <code>addwords [{-cs|-cannaserver} </code><i>cannaserver</i>][-l <i>file</i>] dicname</p>
<h2>DESCRIPTION</h2>
<p> <i>addwords</i> adds words to specified dictionary according to the word information from the standard input. The standard input must be in a format of &#8220;Text Dictionary format&#8221; of Canna. </p>
<p> <i>dicname</i> must be a &#8220;Text Dictionary format&#8221; which can be rewritten.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-is <i>cannaserver</i> (or -cannaserver <i>cannaserver</i>)</p>
<dd> Specifies the hostname on which the specified dictionary is expected to exist.</dl>
<h2>EXAMPLE</h2>
<pre>
  % addwords mydic &lt; newwords
</pre>
<p> Adds words defined in <i>newwords</i> to <i>mydic</i>. </p>
<h2>Index</h2>
