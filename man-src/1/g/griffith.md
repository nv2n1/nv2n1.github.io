---
title: "griffith(1)"
name: "griffith"
section: "1"
letter: "g"
url: "/docs/linux/man/1-griffith/"
description: "griffith – film collection manager"
---

<h2>NAME</h2>
<p> griffith &#8211; film collection manager</p>
<h2>SYNOPSIS</h2>
<p> <code>griffith</code></p>
<h2>DESCRIPTION</h2>
<p> Griffith is a film collection manager. Adding items to the movie collection is as quick and easy as typing the film title and selecting a supported source. Griffith will then try to fetch all the related information from the Web.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> Show usage information.</p>
<dt><code>-D</code> <code>&#8211;debug</code></p>
<dd> Run in debug mode.</p>
<dt><code>-C</code> <code>&#8211;clean</code></p>
<dd> find and delete orphan files in posters directory.</p>
<dt><code>&#8211;check-dep</code></p>
<dd> check dependencies &#8211; if all needed Python modules are installed, it prints nothting.</p>
<dt><code>&#8211;sqlecho</code></p>
<dd> Prints all SQL queries to standart output.</p>
<dt><code>&#8211;home DIR</code></p>
<dd> Set Griffith&#8217;s home directory. Use this option if you want to change the default ~/.griffith</dl>
<p> Printing movie list:</p>
<dl>
<dt><code>-c &lt;expr&gt;</code> <code>&#8211;cast=&lt;expr&gt;</code></p>
<dd> cast field must contain &lt;expr&gt;</p>
<dt><code>-d &lt;expr&gt;</code> <code>&#8211;director=&lt;expr&gt;</code></p>
<dd> director field must contain &lt;expr&gt;</p>
<dt><code>-o &lt;expr&gt;</code> <code>&#8211;original_title=&lt;expr&gt;</code></p>
<dd> original title field must contain &lt;expr&gt;</p>
<dt><code>-t &lt;expr&gt;</code> <code>&#8211;title=&lt;expr&gt;</code></p>
<dd> title field must contain &lt;expr&gt;</p>
<dt><code>-y &lt;number&gt;</code> <code>&#8211;year=&lt;number&gt;</code></p>
<dd> movie must be released in year &lt;number&gt;</p>
<dt><code>-s &lt;columns&gt;</code> <code>&#8211;sort=&lt;columns&gt;</code></p>
<dd> set sort columns to &lt;columns&gt;. Example: &#8211;sort=o_title,number,director</dl>
<h2>SEE ALSO</h2>
<p> Homepage: <a href="lahttp://www.griffith.cc/ra">lahttp://www.griffith.cc/ra</a></p>
<h2>BUGS</h2>
<p> If you want to help or report any bugs founded please visit <a rel="nofollow" href="http://www.griffith.cc/">http://www.griffith.cc/</a> laLrahomepage or lahttps://bugs.launchpad.net/griffithra</p>
<h2>AUTHORS</h2>
<p> Griffith was written by Vasco Nunes and Piotr OoA&#188;arowski. See the AUTHORS and THANKS files for a list of other contributors. </p>
<p> Copyright (C) 2005-2008 Vasco Nunes &lt;vasco.m.nunes [at] gmail.com&gt;, Piotr OoA&#188;arowski &lt;ozarow+griffith [at] gmail.com&gt;, </p>
<p> This man page was written by Piotr Ozarowski </p>
<h2>Index</h2>
