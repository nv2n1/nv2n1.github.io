---
title: "mewl(1)"
name: "mewl"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mewl/"
description: "mewl – Message scanner for Mew 4 or later"
---

<h2>NAME</h2>
<p> mewl &#8211; Message scanner for Mew 4 or later</p>
<h2>SYNOPSIS</h2>
<p> mewl [<i>options</i>] [<i>folder</i> [<i>range</i>]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>mewl</code> utility extracts necessary fields from messages stored in folders. This command is necessary for Mew to implement the asynchronous feature. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-a</code></p>
<dd> Print all necessary fields when picking.</p>
<dt><code>-b</code><i> dir</i></p>
<dd> Set the Mail home to <i>dir</i>.</p>
<dt><code>-c</code><i> bodylen</i></p>
<dd> Set the max body length to be extracted to <i>bodylen</i>.</p>
<dt><code>-d</code><i> field</i></p>
<dd> Set the field to be extracted to <i>field</i>.</p>
<dt><code>-e</code><i> command</i></p>
<dd> Specify an external <i>command</i> to fetch mailbox.</p>
<dt><code>-m</code><i> options</i></p>
<dd> Specify <i>options</i> for <i>command</i>.</p>
<dt><code>-f</code><i> fields</i></p>
<dd> Specify <i>fields</i> to display.</p>
<dt><code>-h</code></p>
<dd> Display this help message.</p>
<dt><code>-i</code><i> file</i></p>
<dd> Set the input stream to <i>file</i>.</p>
<dt><code>-l</code><i> length</i></p>
<dd> Set the max field length to be extracted to <i>length</i>. The default value is 3. 0 means no limit.</p>
<dt><code>-n</code></p>
<dd> Don&#8217;t use fstat().</p>
<dt><code>-p</code><i> pattern</i></p>
<dd> Specify the pick <i>pattern</i>.</p>
<dt><code>-s</code><i> src</i></p>
<dd> Set message source to <i>src</i> : &#8216;+folder range&#8217;.</p>
<dt><code>-w</code></p>
<dd> Wait for stdio input to synchronize.</p>
<dt><code>-v</code></p>
<dd> Display the version.</p>
<dt><code>-x</code><i> suffix</i></p>
<dd> Use this <i>suffix</i>. </p>
<p> Definitions of the symbols above are as follows:</p>
<dt><i>range</i></p>
<dd> N | [start]-[end] | last:N</p>
<dt><i>pattern</i></p>
<dd> &#8216;key=val&#8217; | &#8216;key!=val&#8217; | &#8216;!&lt;pattern&gt;&#8217; | &#8216;(&lt;pattern&gt;)&#8217; | &#8216;&lt;pattern&gt;&amp;&lt;pattern&gt;&#8217; | &#8216;&lt;pattern&gt;|&lt;pattern&gt;&#8217; </p>
</dl>
<h2>BUGS</h2>
<p> If a field is long, only the beginning three lines are extracted by default. </p>
<h2>Index</h2>
