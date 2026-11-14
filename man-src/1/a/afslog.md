---
title: "afslog(1)"
name: "afslog"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afslog/"
description: "afslog – obtain AFS tokens"
---

<h2 class="name">NAME</h2>
<p> <code>afslog</code> &#8211; obtain AFS tokens </p>
<h2>SYNOPSIS</h2>
<p> [-<code>h | &#8211;help</code> ] [-<code>-no-v4</code> ] [-<code>-no-v5</code> ] [-<code>u | &#8211;unlog</code> ] [-<code>v | &#8211;verbose</code> ] [-<code>-version</code> ] [-<code>c </code><i>cell | </i> &#8211;<code>-cell= </code><i>cell</i> ] [-<code>k </code><i>realm | </i> &#8211;<code>-realm= </code><i>realm</i> ] [-<code>P </code><i>principal | </i> &#8211;<code>-principal= </code><i>principal</i> ] -words [-<code>p </code><i>path | </i> &#8211;<code>-file= </code><i>path</i> ] [<i>cell | path &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> obtains AFS tokens for a number of cells. What cells to get tokens for can either be specified as an explicit list, as file paths to get tokens for, or be left unspecified, in which case will use whatever magic krb_afslog3 decides upon. </p>
<p> Supported options:</p>
<dl>
<dt><code>&#8211;no-v4</code></p>
<dd> This makes not try using Kerberos 4.</p>
<dt><code>&#8211;no-v5</code></p>
<dd> This makes not try using Kerberos 5.</p>
<dt> &#8211;<code>P </code><i>principal</i> &#8211;<code>-principal </code><i>principal</i></p>
<dd>
<dd>select what Kerberos 5 principal to use.</p>
<dt><code>&#8211;cache </code><i>cache</i></p>
<dd> select what Kerberos 5 credential cache to use. &#8211;<code>-principal</code> overrides this option.</p>
<dt> &#8211;<code>u</code> &#8211;<code>-unlog</code></p>
<dd>
<dd>Destroy tokens instead of obtaining new. If this is specified, all other options are ignored (except for &#8211;<code>-help</code> and &#8211;<code>-version</code></p>
<dt> &#8211;<code>v</code> &#8211;<code>-verbose</code></p>
<dd>
<dd>Adds more verbosity for what is actually going on.</p>
<dt> &#8211;<code>c </code><i>cell,</i> &#8211;<code>-cell= </code><i>cell</i></p>
<dd>
<dd>This specified one or more cell names to get tokens for.</p>
<dt> &#8211;<code>k </code><i>realm</i> &#8211;<code>-realm= </code><i>realm</i></p>
<dd>
<dd>This is the Kerberos realm the AFS servers live in, this should normally not be specified.</p>
<dt> &#8211;<code>p </code><i>path</i> &#8211;<code>-file= </code><i>path</i></p>
<dd>
<dd>This specified one or more file paths for which tokens should be obtained.</dl>
<p> Instead of using &#8211;<code>c</code> and &#8211;<code>p</code> you may also pass a list of cells and file paths after any other options. These arguments are considered files if they are either the strings Do . Dc or &#8220;..&#8221; or they contain a slash, or if there exists a file by that name.</p>
<h2>EXAMPLES</h2>
<p> Assuming that there is no file called &#8220;openafs.org&#8221; in the current directory, and that /afs/openafs.org points to that cell, the follwing should be identical: </p>
<blockquote>
<pre>
$ afslog -c openafs.org
$ afslog openafs.org
$ afslog /afs/openafs.org/some/file
</pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> krb_afslog3 </p>
<h2>Index</h2>
