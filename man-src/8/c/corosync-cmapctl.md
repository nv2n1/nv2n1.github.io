---
title: "corosync-cmapctl(8)"
name: "corosync-cmapctl"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-cmapctl/"
description: "corosync-cmapctl: – A tool for accessing the object database."
---

<p>corosync-cmapctl: &#8211; A tool for accessing the object database.</p>
<h2>Description</h2>
<p>usage: corosync-cmapctl [-b] [-dghsTtp] [params&#8230;]</p>
<dl>
<dt> <code>-b</code> show binary values</dt></dl>
<h3>Set key:</h3>
<dl>
<dd>
</dd><dd>corosync-cmapctl <code>-s</code> key_name type value</dd>
<dd>where type is one of ([i|u][8|16|32|64] | flt | dbl | str | bin) for bin, value is file name (or &#8211; for stdin)</dd></dl>
<h3>Load settings from a file:</h3>
<dl>
<dd>corosync-cmapctl <code>-p</code> filename</dd>
<dd>the format of the file is: [^[^]]&lt;key_name&gt;[ &lt;type&gt; &lt;value&gt;]</dd>
<dd>Keys prefixed with single caret (&#8216;^&#8217;) are deleted (see <code>-d</code>).</dd>
<dd>Keys (actually prefixes) prefixed with double caret (&#8216;^^&#8217;) are deleted by prefix (see <code>-D</code>).</dd>
<dd>&lt;type&gt; and &lt;value&gt; are optional (not checked) in above cases.</dd>
<dd>Other keys are set (see <code>-s</code>) so both &lt;type&gt; and &lt;value&gt; are required.</dd></dl>
<h3>Delete key:</h3>
<dl>
<dd>corosync-cmapctl <code>-d</code> key_name&#8230;</dd></dl>
<h3>Delete multiple keys with prefix:</h3>
<dl>
<dd>corosync-cmapctl <code>-D</code> key_prefix&#8230;</dd></dl>
<h3>Get key:</h3>
<dl>
<dd>corosync-cmapctl [-b] <code>-g</code> key_name&#8230;</dd></dl>
<h3>Display all keys:</h3>
<dl>
<dd>corosync-cmapctl [-b]</dd></dl>
<h3>Display keys with prefix key_name:</h3>
<dl>
<dd>corosync-cmapctl [-b] key_name&#8230;</dd></dl>
<h3>Track changes on keys with key_name:</h3>
<dl>
<dd>corosync-cmapctl [-b] <code>-t</code> key_name</dd></dl>
<h3>Track changes on keys with key prefix:</h3>
<dl>
<dd>corosync-cmapctl [-b] <code>-T</code> key_prefix </dd>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8), <code><a href="/docs/linux/man/8-cmap_keys/">cmap_keys</a></code>(8) </p>
</dl>