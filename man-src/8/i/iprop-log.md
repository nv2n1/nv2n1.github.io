---
title: "iprop-log(8)"
name: "iprop-log"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iprop-log/"
description: "iprop-log – maintain the iprop log file"
---

<p><code>iprop-log</code> &#8211; maintain the iprop log file</p>
<h2>Synopsis</h2>
<p>[-<code>-version</code> ] [-<code>h | &#8211;help</code> ] <i>command</i> </p>
<pre><code>iprop-log truncate

[-c file |





--config-file= file









]
[-r string |





--realm= string









]
[-h | --help





]
iprop-log dump

[-c file |





--config-file= file









]
[-r string |





--realm= string









]
[-h | --help





]
iprop-log replay

[--start-version= version-number







]

[--end-version= version-number







]

[-c file |





--config-file= file









]
[-r string |





--realm= string









]
[-h | --help





]</code></pre>
<h2>Description</h2>
<p>Supported options:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd>
<dt><code>-h , &#8211;help</code></p>
<dd></dl>
<p> command can be one of the following:</p>
<dl>
<dt><code>truncate</code></p>
<dd>
<dl>
<dt><code>-c </code><i>file , &#8211;</i><code>-config-file= </code><i>file</i></p>
<dd>configuration file</p>
<dt><code>-r </code><i>string , &#8211;</i><code>-realm= </code><i>string</i></p>
<dd>realm</dl>
<p> Truncates the log. Sets the new logs version number for the to the last entry of the old log. If the log is truncted by emptying the file, the log will start over at the first version (0).</p>
<dt><code>dump</code></p>
<dd>
<dl>
<dt><code>-c </code><i>file , &#8211;</i><code>-config-file= </code><i>file</i></p>
<dd>configuration file</p>
<dt> &#8211;<code>r </code><i>string</i> &#8211;<code>-realm= </code><i>string</i></p>
<dd>
<dd>realm</dl>
<p> Print out all entries in the log to standard output.</p>
<dt><code>replay</code></p>
<dd>
<dl>
<dt><code>&#8211;start-version= </code><i>version-number</i></p>
<dd>start replay with this version</p>
<dt> &#8211;<code>-end-version= </code><i>version-number</i></p>
<dd>
<dd>end replay with this version</p>
<dt><code>-c </code><i>file , &#8211;</i><code>-config-file= </code><i>file</i></p>
<dd>configuration file</p>
<dt><code>-r </code><i>string , &#8211;</i><code>-realm= </code><i>string</i></p>
<dd>realm</dl>
<p> Replay the changes from specified entries (or all if none is specified) in the transaction log to the database.</p>
<dt><code>last-version</code></p>
<dd>
<dl>
<dt><code>-c </code><i>file , &#8211;</i><code>-config-file= </code><i>file</i></p>
<dd>configuration file</p>
<dt><code>-r </code><i>string , &#8211;</i><code>-realm= </code><i>string</i></p>
<dd>realm</dl>
<p> prints the version of the last log entry.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-iprop/">iprop</a>(8) </p>
