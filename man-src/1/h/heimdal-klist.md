---
title: "heimdal-klist(1)"
name: "heimdal-klist"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-klist/"
description: "klist – list Kerberos credentials"
---

<h2 class="name">NAME</h2>
<p> <code>klist</code> &#8211; list Kerberos credentials </p>
<h2>SYNOPSIS</h2>
<p> -words [-<code>c </code><i>cache | </i> &#8211;<code>-cache= </code><i>cache</i> ] [-<code>s | -t | &#8211;test</code> ] [-<code>T | &#8211;tokens</code> ] [-<code>5 | &#8211;v5</code> ] [-<code>v | &#8211;verbose</code> ] [-<code>l | &#8211;list-caches</code> ] [-<code>f</code> ] [-<code>-version</code> ] [-<code>-help</code> ]</p>
<h2>DESCRIPTION</h2>
<p> reads and displays the current tickets in the credential cache (also known as the ticket file). </p>
<p> Options supported:</p>
<dl>
<dt><code>-c </code><i>cache , &#8211;</i><code>-cache= </code><i>cache</i></p>
<dd> credential cache to list</p>
<dt><code>-s , -t , &#8211;test</code></p>
<dd> Test for there being an active and valid TGT for the local realm of the user in the credential cache.</p>
<dt><code>-T , &#8211;tokens</code></p>
<dd> display AFS tokens</p>
<dt><code>-5 , &#8211;v5</code></p>
<dd> display v5 cred cache (this is the default)</p>
<dt><code>-f</code></p>
<dd> Include ticket flags in short form, each character stands for a specific flag, as follows:</p>
<dl>
<dt><code>F</code></p>
<dd> forwardable</p>
<dt><code>f</code></p>
<dd> forwarded</p>
<dt><code>P</code></p>
<dd> proxiable</p>
<dt><code>p</code></p>
<dd> proxied</p>
<dt><code>D</code></p>
<dd> postdate-able</p>
<dt><code>d</code></p>
<dd> postdated</p>
<dt><code>R</code></p>
<dd> renewable</p>
<dt><code>I</code></p>
<dd> initial</p>
<dt><code>i</code></p>
<dd> invalid</p>
<dt><code>A</code></p>
<dd> pre-authenticated</p>
<dt><code>H</code></p>
<dd> hardware authenticated</dl>
<p> This information is also output with the &#8211;<code>-verbose</code> option, but in a more verbose way.</p>
<dt><code>-v , &#8211;verbose</code></p>
<dd> Verbose output. Include all possible information:</p>
<dl>
<dt><code>Server</code></p>
<dd> the principal the ticket is for</p>
<dt><code>Ticket etype</code></p>
<dd> the encryption type used in the ticket, followed by the key version of the ticket, if it is available</p>
<dt><code>Session key</code></p>
<dd> the encryption type of the session key, if it&#8217;s different from the encryption type of the ticket</p>
<dt><code>Auth time</code></p>
<dd> the time the authentication exchange took place</p>
<dt><code>Start time</code></p>
<dd> the time that this ticket is valid from (only printed if it&#8217;s different from the auth time)</p>
<dt><code>End time</code></p>
<dd> when the ticket expires, if it has already expired this is also noted</p>
<dt><code>Renew till</code></p>
<dd> the maximum possible end time of any ticket derived from this one</p>
<dt><code>Ticket flags</code></p>
<dd> the flags set on the ticket</p>
<dt><code>Addresses</code></p>
<dd> the set of addresses from which this ticket is valid</dl>
<dt><code>-l , &#8211;list-caches</code></p>
<dd> List the credential caches for the current users, not all cache types supports listing multiple caches. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kdestroy/">kdestroy</a>(1), <a href="/docs/linux/man/1-kinit/">kinit</a>(1) </p>
<h2>Index</h2>
