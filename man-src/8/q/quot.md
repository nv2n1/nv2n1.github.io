---
title: "quot(8)"
name: "quot"
section: "8"
letter: "q"
url: "/docs/linux/man/8-quot/"
description: "quot – summarize filesystem ownership"
---

<p>quot &#8211; summarize filesystem ownership</p>
<h2>Synopsis</h2>
<pre><code>quot</code> [ <code>-acfguvi</code> ] [ filesystem... ]</pre>
<h2>Description</h2>
<p><i>quot</i> displays the number of kilobytes in the named <i>filesystem</i> currently owned by each user or group. Note that this utility currently works only for XFS.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Generate a report for all mounted filesystems giving the number of kilobytes used by each user or group.</p>
<dt><code>-c</code></p>
<dd>Display three columns giving file size in kilobytes, number of files of that size, and cumulative total of kilobytes in that size or smaller file. The last row is used as an overflow bucket and is the total of all files greater than 500 kilobytes.</p>
<dt><code>-f</code></p>
<dd>Display count of kilobytes and number of files owned by each user or group.</p>
<dt><code>-g</code></p>
<dd>Report on groups.</p>
<dt><code>-u</code></p>
<dd>Report on users (the default).</p>
<dt><code>-v</code></p>
<dd>Display three columns containing the number of kilobytes not accessed in the last 30, 60, and 90 days.</p>
<dt><code>-i</code></p>
<dd>Ignore mountpoints mounted by automounter.</p>
<dt><code>-T</code></p>
<dd>Avoid truncation of user names longer than 8 characters.</p>
<dt><code>-q</code></p>
<dd>Do not sort the output.</dl>
<h2>Files</h2>
<dl>
<dt>/etc/mtab</p>
<dd>mounted filesystem table</p>
<dt>/etc/passwd</p>
<dd>default set of users</p>
<dt>/etc/group</p>
<dd>default set of groups</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-du/">du</a>(1), <a href="/docs/linux/man/1-ls/">ls</a>(1).</p>
<h2>Bugs</h2>
<p>Currently, only the XFS filesystem type is supported. </p>
