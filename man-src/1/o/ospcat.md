---
title: "ospcat(1)"
name: "ospcat"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ospcat/"
description: "ospcat – SGML print catalog"
---

<h2 class="name">NAME</h2>
<p> ospcat &#8211; SGML print catalog </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ospcat</code> [<code>-b&nbsp;<wbr></code><i>name</i>] [<code>&#8211;bctf=</code><i>name</i>] [<code>-C</code>] [<code>&#8211;catalogs</code>] [<code>-c&nbsp;<wbr></code><i>sysid</i>] [<code>&#8211;catalog=</code><i>sysid</i>] [<code>-f</code>] [<code>&#8211;error-file=</code><i>file</i>] [<code>-D&nbsp;<wbr></code><i>directory</i>] [<code>&#8211;directory=</code><i>directory</i>] [<code>-R</code>] [<code>&#8211;restricted</code>] [<code>-v</code>] [<code>-h</code>] [<code>&#8211;help</code>] [<code>-P&nbsp;<wbr></code><i>literal</i>] [<code>&#8211;public-id=</code><i>literal</i>] [<code>-S&nbsp;<wbr></code><i>literal</i>] [<code>&#8211;system_id=</code><i>literal</i>] [<code>-p&nbsp;<wbr></code><i>name</i>] [<code>&#8211;parameter-entity=</code><i>name</i>] [<code>-d&nbsp;<wbr></code><i>name</i>] [<code>&#8211;doctype=</code><i>name</i>] [<code>-l&nbsp;<wbr></code><i>name</i>] [<code>&#8211;linktype=</code><i>name</i>] [<code>-e&nbsp;<wbr></code><i>name</i>] [<code>&#8211;entity=</code><i>name</i>] [<code>-n&nbsp;<wbr></code><i>name</i>] [<code>&#8211;notation=</code><i>name</i>] [<code>-s&nbsp;<wbr></code><i>name</i>] [<code>&#8211;declaration=</code><i>name</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>ospcat</code></p>
<dd>prints effective system identifiers found in the catalogs on the standard output. It doesn&#8217;t check that the system identifiers correspond to actual files. The return value is 0 if the last system identifier was successfully created and 1 otherwise.</p>
<h2>OPTIONS</h2>
<p> The following options are available: </p>
<p> <code>-b </code><i>name</i>, <code>&#8211;bctf=</code><i>name</i></p>
<dl>
<dt>
<dd> Use bctf <i>name</i> for output.</dl>
<p> <code>-f </code><i>file</i>, <code>&#8211;error-file=</code><i>file</i></p>
<dl>
<dt>
<dd> Append error messages to file <i>file</i>.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the program version.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show this help text.</dl>
<p> <code>-c </code><i>sysid</i>, <code>&#8211;catalog=</code><i>sysid</i></p>
<dl>
<dt>
<dd> Use catalog <i>sysid</i>.</dl>
<p> <code>-C</code>, <code>&#8211;catalogs</code></p>
<dl>
<dt>
<dd> Arguments are catalogs, use DOCUMENT entry.</dl>
<p> <code>-D </code><i>directory</i>, <code>&#8211;directory=</code><i>directory</i></p>
<dl>
<dt>
<dd> Search files in directory <i>directory</i>.</dl>
<p> <code>-R</code>, <code>&#8211;restricted</code></p>
<dl>
<dt>
<dd> Restrict file reading (for use in Web apps).</dl>
<p> <code>-P </code><i>literal</i>, <code>&#8211;public-id=</code><i>literal</i></p>
<dl>
<dt>
<dd> Print the effective system id for the public id <i>literal</i>.</dl>
<p> <code>-S </code><i>literal</i>, <code>&#8211;system-id=</code><i>literal</i></p>
<dl>
<dt>
<dd> Print the effective system id for system id <i>literal</i>.</dl>
<p> <code>-p </code><i>name</i>, <code>&#8211;parameter-entity=</code><i>name</i></p>
<dl>
<dt>
<dd> Print the effective system id for parameter entity <i>name</i>.</dl>
<p> <code>-d </code><i>name</i>, <code>&#8211;doctype=</code><i>name</i></p>
<dl>
<dt>
<dd> Print the effective system id for the doctype <i>name</i>.</dl>
<p> <code>-l </code><i>name</i>, <code>&#8211;linktype=</code><i>name</i></p>
<dl>
<dt>
<dd> Print the effective system id for the linktype <i>name</i>.</dl>
<p> <code>-e </code><i>name</i>, <code>&#8211;entity=</code><i>name</i></p>
<dl>
<dt>
<dd> Print the effective system id for entity <i>name</i>.</dl>
<p> <code>-n </code><i>name</i>, <code>&#8211;notation=</code><i>name</i></p>
<dl>
<dt>
<dd> Print the effective system id for notation <i>name</i>.</dl>
<p> <code>-s </code><i>name</i>, <code>&#8211;declaration=</code><i>name</i></p>
<dl>
<dt>
<dd> Print the effective system id for the SGML declaration for doctype <i>name</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-onsgmls/">onsgmls</a>(1)</code>, <code><a href="/docs/linux/man/1-ospam/">ospam</a>(1)</code>, <code><a href="/docs/linux/man/1-onsgmlnorm/">onsgmlnorm</a>(1)</code>, <code><a href="/docs/linux/man/1-ospent/">ospent</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> <code>Ian Castle</code> &lt;ian.castle [at] openjade.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<h2>Index</h2>
