---
title: "ptrash(1)"
name: "ptrash"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ptrash/"
---

<h2>SYNOPSIS</h2>
<dl>
<dt><code>ptrash</code> [<i>Option</i>] file-name-1 [file-name-2 &#8230;]</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> <code>ptrash</code> is a console based simple application. <code>ptrash</code> moves the named file(s) to trash directory located under the home directory of a user. In case if ~/.trash is non-existent, <code>ptrash</code> creates it for you and then moves the file(s) to this directory. By default, ptrash runs in non-interactive mode, which means it does not ask user if she is sure to move the file to ~/.trash even when the named file already exists in trash and proceeds with overwriting that file.</p>
<h2>OPTIONS</h2>
<p> <code>ptrash</code> supports the following options</p>
<dl>
<dt><code>-d &#8211;delete</code></p>
<dd> Delete file(s) from trash</p>
<dt><code>-h &#8211;help</code></p>
<dd> Prints this short usage help</p>
<dt><code>-i</code></p>
<dd> Enables an interactive moving of files to trash, that is ask for confirmation before over writing an existing file in trash</p>
<dt><code>-r &#8211;restore</code></p>
<dd> Restore a file from trash to it&#8217;s original location</p>
<dt><code>-v &#8211;verbose</code></p>
<dd> Verbose operation mode</p>
<dt><code>-V &#8211;version</code></p>
<dd> Displays the version information</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cp/">cp</a>(1) <a href="/docs/linux/man/1-mv/">mv</a>(1) <a href="/docs/linux/man/1-rm/">rm</a>(1) <a href="/docs/linux/man/1-shred/">shred</a>(1)</p>
<h2>BUG(s)</h2>
<p> If you think you have found a bug in ptrash-v1.0, send an email to &lt;<i>pj.pandit AT yahoo.co.in</i>&gt;, and while doing so please include the ptrash-&lt;version&gt; string in the subject line, and describe precisely about the behaviour of ptrash.</p>
<h2>NOTE</h2>
<p> ptrash does not facilitate moving of symbolic links to/from ~/.trash.</p>
<h2>AUTHOR</h2>
<p> Prasad J Pandit &lt;<i>pj.pandit AT yahoo.co.in</i>&gt; </p>
<h2>Index</h2>
