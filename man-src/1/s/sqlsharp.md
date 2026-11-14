---
title: "sqlsharp(1)"
name: "sqlsharp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sqlsharp/"
description: "sqlsharp – Mono SQL Query command-line tool"
---

<h2>NAME</h2>
<p> sqlsharp &#8211; Mono SQL Query command-line tool</p>
<h2>SYNOPSIS</h2>
<p> <code>sqlsharp </code> [-f filename] [-o filename] [-s]</p>
<h2>DESCRIPTION</h2>
<p> sqlsharp is a Mono SQL tool used for entering SQL queries to a database using Mono data providers. </p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>-f filename</i></p>
<dd> Output file to load SQL commands from.</p>
<dt><i>-o filename</i></p>
<dd> Output file to send results.</p>
<dt><i>-s</i></p>
<dd> Silent mode.</dl>
<h2>HOW TO USE</h2>
<p> The SQL tool accepts commands via its command line interface. Commands begin with a backslash followed by the command name. </p>
<p> Example: </p>
<pre>
        \open
</pre>
<p> Basically, there are five commands a user should know: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>\provider, 
