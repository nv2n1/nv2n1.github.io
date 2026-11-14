---
title: "zipcloak(1)"
name: "zipcloak"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zipcloak/"
description: "zipcloak – encrypt entries in a zipfile"
---

<h2 class="name">NAME</h2>
<p> zipcloak &#8211; encrypt entries in a zipfile</p>
<h2>SYNOPSIS</h2>
<p> <i>zipcloak</i> [<code>-d</code>] [<code>-b path</code>] [<code>-h</code>] [<code>-v</code>] [<code>-L</code>] zipfile </p>
<h2>ARGUMENTS</h2>
<p> zipfile Zipfile to encrypt entries in </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b&nbsp;</code>path</p>
<dd>
<dt><code>&#8211;temp-path </code>path</p>
<dd> Use the directory given by path for the temporary zip file. </p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;decrypt</code></p>
<dd> Decrypt encrypted entries (copy if given wrong password). </p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help&nbsp;</code></p>
<dd> Show a short help. </p>
<dt><code>-L</code></p>
<dd>
<dt><code>&#8211;license</code></p>
<dd> Show software license. </p>
<dt><code>-O&nbsp;</code>path</p>
<dd>
<dt><code>&#8211;output-file&nbsp;</code>zipfile</p>
<dd> Write output to new archive zipfile, leaving original archive as is. </p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Quiet operation. Suppresses some informational messages. </p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Show version information. </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <i>zipcloak</i> encrypts all unencrypted entries in the zipfile. This is the default action. </p>
<dl>
<dt>The -d option is used to decrypt encrypted entries in the zipfile.</p>
<dd>
<dt><i>zipcloak </i><code>uses original zip encryption which is considered weak.</p>
<dd>
<dt>Note:</p>
<dd> The encryption code of this program is not copyrighted and is put in the public domain. It was originally written in Europe and can be freely distributed from any country including the U.S.A. (Previously if this program was imported into the U.S.A, it could not be re-exported from the U.S.A to another country.) See the file README.CR included in the source distribution for more on this. Otherwise, the Info-ZIP license applies. </p>
</dl>
<p> </code></p>
<h2>EXAMPLES</h2>
<p> To be added. </p>
<h2>BUGS</h2>
<p> Large files (&gt; 2 GB) and large archives not yet supported. </p>
<p> Split archives not yet supported. A work around is to convert the split archive to a single-file archive using <i>zip</i> and then use <i>zipcloak</i> on the single-file archive. If needed, the resulting archive can then be split again using <i>zip</i>. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zip/">zip</a>(1), <a href="/docs/linux/man/1-unzip/">unzip</a>(1)</p>
<h2>AUTHOR</h2>
<p> Info-ZIP </p>
<h2>Index</h2>
