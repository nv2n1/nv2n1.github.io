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
<dt><code>-a</code></dt>
<dd> Print all necessary fields when picking.</dd>
<dt><code>-b</code><i> dir</i></dt>
<dd> Set the Mail home to <i>dir</i>.</dd>
<dt><code>-c</code><i> bodylen</i></dt>
<dd> Set the max body length to be extracted to <i>bodylen</i>.</dd>
<dt><code>-d</code><i> field</i></dt>
<dd> Set the field to be extracted to <i>field</i>.</dd>
<dt><code>-e</code><i> command</i></dt>
<dd> Specify an external <i>command</i> to fetch mailbox.</dd>
<dt><code>-m</code><i> options</i></dt>
<dd> Specify <i>options</i> for <i>command</i>.</dd>
<dt><code>-f</code><i> fields</i></dt>
<dd> Specify <i>fields</i> to display.</dd>
<dt><code>-h</code></dt>
<dd> Display this help message.</dd>
<dt><code>-i</code><i> file</i></dt>
<dd> Set the input stream to <i>file</i>.</dd>
<dt><code>-l</code><i> length</i></dt>
<dd> Set the max field length to be extracted to <i>length</i>. The default value is 3. 0 means no limit.</dd>
<dt><code>-n</code></dt>
<dd> Don&#8217;t use fstat().</dd>
<dt><code>-p</code><i> pattern</i></dt>
<dd> Specify the pick <i>pattern</i>.</dd>
<dt><code>-s</code><i> src</i></dt>
<dd> Set message source to <i>src</i> : &#8216;+folder range&#8217;.</dd>
<dt><code>-w</code></dt>
<dd> Wait for stdio input to synchronize.</dd>
<dt><code>-v</code></dt>
<dd> Display the version.</dd>
<dt><code>-x</code><i> suffix</i></dt>
<dd> Use this <i>suffix</i>. </dd>
<p> Definitions of the symbols above are as follows:</p>
<dt><i>range</i></dt>
<dd> N | [start]-[end] | last:N</dd>
<dt><i>pattern</i></dt>
<dd> &#8216;key=val&#8217; | &#8216;key!=val&#8217; | &#8216;!&lt;pattern&gt;&#8217; | &#8216;(&lt;pattern&gt;)&#8217; | &#8216;&lt;pattern&gt;&amp;&lt;pattern&gt;&#8217; | &#8216;&lt;pattern&gt;|&lt;pattern&gt;&#8217; </dd>
</dl>
<h2>BUGS</h2>
<p> If a field is long, only the beginning three lines are extracted by default. </p>
