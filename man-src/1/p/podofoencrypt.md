---
title: "podofoencrypt(1)"
name: "podofoencrypt"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podofoencrypt/"
description: "podofoencrypt – encrypt PDF files and set PDF security settings"
---

<h2 class="name">NAME</h2>
<p> podofoencrypt &#8211; encrypt PDF files and set PDF security settings</p>
<h2>SYNOPSIS</h2>
<p> <code>podofoencrypt</code> [&#8211;rc4v1] [&#8211;rc4v2] [&#8211;aes] [-u &lt;userpassword&gt;] -o &lt;ownerpassword&gt; &lt;inputfile&gt; &lt;outputfile&gt; </p>
<h2>DESCRIPTION</h2>
<p> <code>podofoencrypt</code> is one of the command line tools from the PoDoFo library that provide several useful operations to work with PDF files. It can encrypt PDF files using RC4 or AES encoding and can set PDF security settings. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display the help text</dl>
<p> Algorithm: </p>
<dl>
<dt>
<dd> <code>&#8211;rc4v1</code></p>
<dl>
<dt>
<dd> Use rc4v1 encryption</dl>
<p> <code>&#8211;rc4v2</code></p>
<dl>
<dt>
<dd> Use rc4v2 encryption (Default value)</dl>
<p> <code>&#8211;aes</code></p>
<dl>
<dt>
<dd> Use aes encryption (currently not supported)</dl>
</dl>
<p> Passwords: </p>
<dl>
<dt>
<dd> <code>-u &lt;password&gt;</code></p>
<dl>
<dt>
<dd> An optional user password</dl>
<p> <code>-o &lt;password&gt;</code></p>
<dl>
<dt>
<dd> The required owner password</dl>
</dl>
<p> Permissions:</p>
<dl>
<dt>
<dd>
<p> <code>&#8211;print</code></p>
<dl>
<dt>
<dd>
<p> Allow printing the document</dl>
<p> <code>&#8211;edit</code></p>
<dl>
<dt>
<dd>
<p> Allow modification of the document besides annotations, form fields or changing pages</dl>
<p> <code>&#8211;copy</code></p>
<dl>
<dt>
<dd>
<p> Allow extraction of text and graphics</dl>
<p> <code>&#8211;editnotes</code></p>
<dl>
<dt>
<dd>
<p> Add or modify text annoations or form fields (if ePdfPermissions_Edit is set also allow to create interactive form fields including signature)</dl>
<p> <code>&#8211;fillandsign</code></p>
<dl>
<dt>
<dd>
<p> Fill in existing form or signature fields</dl>
<p> <code>&#8211;accessible</code></p>
<dl>
<dt>
<dd>
<p> Extract text and graphics to support user with disabillities</dl>
<p> <code>&#8211;assemble</code></p>
<dl>
<dt>
<dd>
<p> Assemble the document: insert, create, rotate delete pages or add bookmarks</dl>
<p> <code>&#8211;highprint </code></p>
<dl>
<dt>
<dd>
<p> Print a high resolution version of the document </p>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-podofobox/">podofobox</a></code>(1), <code><a href="/docs/linux/man/1-podofocolor/">podofocolor</a></code>(1), <code><a href="/docs/linux/man/1-podofocountpages/">podofocountpages</a></code>(1), <code><a href="/docs/linux/man/1-podofocrop/">podofocrop</a></code>(1), <code><a href="/docs/linux/man/1-podofogc/">podofogc</a></code>(1), <code><a href="/docs/linux/man/1-podofoimg2pdf/">podofoimg2pdf</a></code>(1), <code><a href="/docs/linux/man/1-podofoimgextract/">podofoimgextract</a></code>(1), <code><a href="/docs/linux/man/1-podofoincrementalupdates/">podofoincrementalupdates</a></code>(1), <code><a href="/docs/linux/man/1-podofoimpose/">podofoimpose</a></code>(1), <code><a href="/docs/linux/man/1-podofomerge/">podofomerge</a></code>(1), <code><a href="/docs/linux/man/1-podofopages/">podofopages</a></code>(1), <code><a href="/docs/linux/man/1-podofopdfinfo/">podofopdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-podofotxt2pdf/">podofotxt2pdf</a></code>(1), <code><a href="/docs/linux/man/1-podofotxtextract/">podofotxtextract</a></code>(1), <code><a href="/docs/linux/man/1-podofouncompress/">podofouncompress</a></code>(1), <code><a href="/docs/linux/man/1-podofoxmp/">podofoxmp</a></code>(1) </p>
<h2>AUTHORS</h2>
<p> PoDoFo is written by Dominik Seichter &lt;domseichter [at] web.de&gt; and others. </p>
<p> This manual page was written by Oleksandr Moskalenko &lt;malex [at] debian.org&gt; for the Debian Project (but may be used by others). </p>
<h2>Index</h2>
