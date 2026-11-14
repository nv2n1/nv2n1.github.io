---
title: "lua(1)"
name: "lua"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lua/"
description: "lua – Lua interpreter"
---

<h2>NAME</h2>
<p> lua &#8211; Lua interpreter</p>
<h2>SYNOPSIS</h2>
<p> <code>lua</code> [ <i>options</i> ] [ <i>script</i> [ <i>args</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lua</code> is the stand-alone Lua interpreter. It loads and executes Lua programs, either in textual source form or in precompiled binary form. (Precompiled binaries are output by <code>luac</code>, the Lua compiler.) <code>lua</code> can be used as a batch interpreter and also interactively. </p>
<p> The given <i>options</i> (see below) are executed and then the Lua program in file <i>script</i> is loaded and executed. The given <i>args</i> are available to <i>script</i> as strings in a global table named <code>arg</code>. If these arguments contain spaces or other characters special to the shell, then they should be quoted (but note that the quotes will be removed by the shell). The arguments in <code>arg</code> start at 0, which contains the string &#8216;<i>script</i>&#8216;. The index of the last argument is stored in <code>arg.n</code>. The arguments given in the command line before <i>script</i>, including the name of the interpreter, are available in negative indices in <code>arg</code>. </p>
<p> At the very start, before even handling the command line, <code>lua</code> executes the contents of the environment variable <code>LUA_INIT</code>, if it is defined. If the value of <code>LUA_INIT</code> is of the form &#8216;@<i>filename</i>&#8216;, then <i>filename</i> is executed. Otherwise, the string is assumed to be a Lua statement and is executed. </p>
<p> Options start with <code>&#8216;-&#8216;</code> and are described below. You can use <code>&#8216;&#8211;&#8216;</code> to signal the end of options. </p>
<p> If no arguments are given, then <code>-v -i</code> is assumed when the standard input is a terminal; otherwise, <code>&#8211;</code> is assumed. </p>
<p> In interactive mode, <code>lua</code> prompts the user, reads lines from the standard input, and executes them as they are read. If a line does not contain a complete statement, then a secondary prompt is displayed and lines are read until a complete statement is formed or a syntax error is found. So, one way to interrupt the reading of an incomplete statement is to force a syntax error: adding a <code>&#8216;;&#8217; </code> in the middle of a statement is a sure way of forcing a syntax error (except inside multiline strings and comments; these must be closed explicitly). If a line starts with <code>&#8216;=&#8217;</code>, then <code>lua</code> displays the values of all the expressions in the remainder of the line. The expressions must be separated by commas. The primary prompt is the value of the global variable <code>_PROMPT</code>, if this value is a string; otherwise, the default prompt is used. Similarly, the secondary prompt is the value of the global variable <code>_PROMPT2</code>. So, to change the prompts, set the corresponding variable to a string of your choice. You can do that after calling the interpreter or on the command line (but in this case you have to be careful with quotes if the prompt string contains a space; otherwise you may confuse the shell.) The default prompts are &quot;&gt; &quot; and &quot;&gt;&gt; &quot;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;</code></p>
<dd> load and execute the standard input as a file, that is, not interactively, even when the standard input is a terminal.</p>
<dt><code>-e</code><i> stat</i></p>
<dd> execute statement <i>stat</i>. You need to quote <i>stat </i> if it contains spaces, quotes, or other characters special to the shell.</p>
<dt><code>-i</code></p>
<dd> enter interactive mode after <i>script</i> is executed.</p>
<dt><code>-l</code><i> name</i></p>
<dd> call <code>require(&#8216;</code><i>name</i><code>&#8216;)</code> before executing <i>script</i>. Typically used to load libraries.</p>
<dt><code>-v</code></p>
<dd> show version information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-luac/">luac</a></code>(1)<br />
 <a rel="nofollow" href="http://www.lua.org/">http://www.lua.org/</a></p>
<h2>DIAGNOSTICS</h2>
<p> Error messages should be self explanatory.</p>
<h2>AUTHORS</h2>
<p> R. Ierusalimschy, L. H. de Figueiredo, and W. Celes </p>
<h2>Index</h2>
