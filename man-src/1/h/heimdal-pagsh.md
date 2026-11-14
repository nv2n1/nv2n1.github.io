---
title: "heimdal-pagsh(1)"
name: "heimdal-pagsh"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-pagsh/"
description: "pagsh – creates a new credential cache sandbox"
---

<h2 class="name">NAME</h2>
<p> <code>pagsh</code> &#8211; creates a new credential cache sandbox </p>
<h2>SYNOPSIS</h2>
<p> [-<code>c </code><i>command-string</i> ] [-<code>h | &#8211;help</code> ] [-<code>-version</code> ] [-<code>-cache-type= </code><i>string</i> ] <i>command [args&#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> Supported options:</p>
<dl>
<dt> &#8211;<code>c </code><i>command-string</i></p>
<dd>Executes command(s) contained in <i>command-string</i></p>
<dt> &#8211;<code>-cache-type= </code><i>string</i></p>
<dd>
<dt> &#8211;<code>h</code> &#8211;<code>-help</code></p>
<dd>
<dt> &#8211;<code>-version</code></p>
<dd></dl>
<dd>creates a new credential cache sandbox for the user to live in. If AFS is installed on the computer, the user is put in a newly created Process Authentication Group (PAG). </p>
<p> For Kerberos 5, the credential cache type that is used is the same as the credential cache type that was used at the time of invocation. The credential cache type can be controlled by the option &#8211;<code>-cache-type</code></p>
<h2>EXAMPLES</h2>
<p> Create a new sandbox where new credentials can be used, while the old credentials can be used by other processes. </p>
<blockquote>
<pre><code>
$ klist
        Credentials cache : FILE : /
                                   tmp / krb5cc_913 Principal : lha[at] E.KTH.SE Issued Expires Principal Feb 12 10 : 08 : 31 Feb 12 20 : 06 : 36 krbtgt / E.KTH.SE[at] E.KTH.SE $ pagsh $ klist klist : No ticket file : / tmp / krb5cc_03014a
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-afslog/">afslog</a>(1), <a href="/docs/linux/man/1-kinit/">kinit</a>(1) </p>
<h2>Index</h2>
