---
title: "kgetcred(1)"
name: "kgetcred"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kgetcred/"
description: "kgetcred – get a ticket for a particular service"
---

<h2 class="name">NAME</h2>
<p> <code>kgetcred</code> &#8211; get a ticket for a particular service </p>
<h2>SYNOPSIS</h2>
<p> [-<code>-canonicalize</code> ] [-<code>c cache | </code> &#8211;<code>-cache= </code><i>cache</i> ] [-<code>e </code><i>enctype | </i> &#8211;<code>-enctype= </code><i>enctype</i> ] [-<code>name-type= </code><i>name-type</i> ] [-<code>-no-transit-check</code> ] [-<code>-version</code> ] [-<code>-help</code> ] <i>service</i><br />
 [options] &#8211;<code>name-type= </code><i>SRV_HST</i> <i>service</i> <i>hostname</i></p>
<h2>DESCRIPTION</h2>
<p> obtains a ticket for a service. Usually tickets for services are obtained automatically when needed but sometimes for some odd reason you want to obtain a particular ticket or of a special type. </p>
<p> The second form applies hostname canonicalization using local name canonicalization rules just as applications normally would, possibly enabling canonicalization via referrals. </p>
<p> Supported options:</p>
<dl>
<dt><code>&#8211;canonicalize</code></p>
<dd> requests that the KDC canonicalize the principal.</p>
<dt><code>&#8211;name-type= </code><i>name-type</i></p>
<dd> the name-type to use when parsing the principal name.</p>
<dt><code>-c </code><i>cache , &#8211;</i><code>-cache= </code><i>cache</i></p>
<dd> the credential cache to use.</p>
<dt><code>&#8211;delegation-credential-cache= </code><i>cache</i></p>
<dd> the credential cache to use for delegation.</p>
<dt><code>-e </code><i>enctype , &#8211;</i><code>-enctype= </code><i>enctype</i></p>
<dd> encryption type to use.</p>
<dt><code>&#8211;no-transit-check</code></p>
<dd> requests that the KDC doesn&#8217;t do transit checking.</p>
<dt><code>&#8211;forwardable</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kinit/">kinit</a>(1), <a href="/docs/linux/man/1-klist/">klist</a>(1) </p>
<h2>Index</h2>
