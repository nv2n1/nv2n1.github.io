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
<p> <code>delve</code> [<i>OPTIONS</i>] <i>DATABASE</i>&#8230;</p>
<p> delve &#8211; Inspect the contents of a Xapian database</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> show all terms in the database</dd>
<dt><code>-A</code> &lt;prefix&gt;</dt>
<dd> show all terms in the database with given prefix</dd>
<dt><code>-r</code> &lt;recno&gt;</dt>
<dd> for term list(s)</dd>
<dt><code>-t</code> &lt;term&gt;</dt>
<dd> for posting list(s)</dd>
<dt><code>-t</code> &lt;term&gt; <code>-r</code> &lt;recno&gt;</dt>
<dd> for position list(s)</dd>
<dt><code>-s</code>, <code>&#8211;stemmer</code>=<i>LANG</i></dt>
<dd> set the stemming language, the default is &#8216;none&#8217;</dd>
<dt><code>-1</code></dt>
<dd> output one list entry per line</dd>
<dt><code>-V</code></dt>
<dd> output values for each document referred to</dd>
<dt><code>-V</code>&lt;valueno&gt;</dt>
<dd> output value valueno for each document referred to (or each document in the database if no <code>-r</code> options)</dd>
<dt><code>-d</code></dt>
<dd> output document data for each document referred to</dd>
<dt><code>-z</code></dt>
<dd> for db, count documents with length 0</dd>
<dt><code>-v</code></dt>
<dd> extra info (wdf and len for postlist; wdf and termfreq for termlist; number of terms for db; termfreq when showing all terms)</dd>
<dt><code>-vv</code></dt>
<dd> even more info (also show collection freq and wdf upper bound for terms)</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit </dd>
</dl>
