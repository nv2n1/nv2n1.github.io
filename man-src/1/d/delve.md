---
title: "delve(1)"
name: "delve"
section: "1"
letter: "d"
url: "/docs/linux/man/1-delve/"
description: "delve – Inspect the contents of a Xapian database"
---

<h2>NAME</h2>
<p> delve &#8211; Inspect the contents of a Xapian database</p>
<h2>SYNOPSIS</h2>
<p> <code>delve</code> [<i>OPTIONS</i>] <i>DATABASE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> delve &#8211; Inspect the contents of a Xapian database</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> show all terms in the database</p>
<dt><code>-A</code> &lt;prefix&gt;</p>
<dd> show all terms in the database with given prefix</p>
<dt><code>-r</code> &lt;recno&gt;</p>
<dd> for term list(s)</p>
<dt><code>-t</code> &lt;term&gt;</p>
<dd> for posting list(s)</p>
<dt><code>-t</code> &lt;term&gt; <code>-r</code> &lt;recno&gt;</p>
<dd> for position list(s)</p>
<dt><code>-s</code>, <code>&#8211;stemmer</code>=<i>LANG</i></p>
<dd> set the stemming language, the default is &#8216;none&#8217;</p>
<dt><code>-1</code></p>
<dd> output one list entry per line</p>
<dt><code>-V</code></p>
<dd> output values for each document referred to</p>
<dt><code>-V</code>&lt;valueno&gt;</p>
<dd> output value valueno for each document referred to (or each document in the database if no <code>-r</code> options)</p>
<dt><code>-d</code></p>
<dd> output document data for each document referred to</p>
<dt><code>-z</code></p>
<dd> for db, count documents with length 0</p>
<dt><code>-v</code></p>
<dd> extra info (wdf and len for postlist; wdf and termfreq for termlist; number of terms for db; termfreq when showing all terms)</p>
<dt><code>-vv</code></p>
<dd> even more info (also show collection freq and wdf upper bound for terms)</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit </p>
</dl>
<h2>Index</h2>
