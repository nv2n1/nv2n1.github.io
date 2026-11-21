---

title: "heimdal-kdestroy(1)"
name: "heimdal-kdestroy"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-kdestroy/"
description: "kdestroy – remove one credential or destroy the current ticket file"
---

<p> <code>kdestroy</code> &#8211; remove one credential or destroy the current ticket file </p>
<h2>SYNOPSIS</h2>
<p> -words [-<code>c </code><i>cachefile</i> ] [-<code>-credential= </code><i>principal</i> ] [-<code>-cache= </code><i>cachefile</i> ] [-<code>A | &#8211;all</code> ] [-<code>-no-unlog</code> ] [-<code>-no-delete-v4</code> ] [-<code>-version</code> ] [-<code>-help</code> ]</p>
<h2>DESCRIPTION</h2>
<p> removes one credential or the current set of tickets. </p>
<p> Supported options:</p>
<dl>
<dt><code>-credential= </code><i>principal</i></dt>
<dd> remove Fa principal from the credential cache if it exists.</dd>
<dt><code>-c </code><i>cachefile</i></dt>
<dd>
</dd><dt><code>-cache= </code><i>cachefile</i></dt>
<dd> The cache file to remove.</dd>
<dt><code>-A</code></dt>
<dd>
</dd><dt><code>&#8211;all</code></dt>
<dd> remove all credential caches.</dd>
<dt><code>&#8211;no-unlog</code></dt>
<dd> Do not remove AFS tokens.</dd>
<dt><code>&#8211;no-delete-v4</code></dt>
<dd> Do not remove v4 tickets.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kinit/">kinit</a>(1), <a href="/docs/linux/man/1-klist/">klist</a>(1) </p>
