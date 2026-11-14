---
title: "npm-token(1)"
name: "npm-token"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-token/"
description: "npm-token – Manage your authentication tokens"
---

<h2 class="name">NAME</h2>
<p> <code>npm-token</code> &#8211; Manage your authentication tokens </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre><code>
npm token list[--json | --parseable] npm token create[--read - only][--cidr = 1.1.1.1 / 24, 2.2.2.2 / 16] npm token revoke&lt;id | token&gt;
</code></pre>
</dl>
<h3>Description</h3>
<p> This lets you list, create and revoke authentication tokens.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>npm token list</code>: Shows a table of all active authentication tokens. You can request this as JSON with <code>&#8211;json</code> or tab-separated values with <code>&#8211;parseable</code>. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
+ &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | id | token | created | read &#8211; only | CIDR whitelist |<br />
    +&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | 7f3134 | 1fa9ba… | 2017 &#8211; 10 &#8211; 02 | yes | |<br />
    +&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | c03241 | af7aef… | 2017 &#8211; 10 &#8211; 02 | no | 192.168.0.1 / 24 |<br />
    +&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | e0cf92 | 3a436a… | 2017 &#8211; 10 &#8211; 02 | no | |<br />
    +&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | 63eb9d | 74ef35… | 2017 &#8211; 09 &#8211; 28 | no | |<br />
    +&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | 2daaa8 | cbad5f… | 2017 &#8211; 09 &#8211; 26 | no | |<br />
    +&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | 68c2fe | 127e51… | 2017 &#8211; 09 &#8211; 23 | no | |<br />
    +&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+ | 6334e1 | 1dadd1… | 2017 &#8211; 09 &#8211; 23 | no | |<br />
    +&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>npm token create [&#8211;read-only] [&#8211;cidr=&lt;cidr-ranges&gt;]</code>: Create a new authentication token. It can be <code>&#8211;read-only</code> or accept a list of CIDR <i><a rel="nofollow" href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing</a></i> ranges to limit use of this token to. This will prompt you for your password, and, if you have two-factor authentication enabled, an otp. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<pre><code>
+ -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+ | token | a73c9572 - f1b9 - 8983 - 983d - ba3ac3cc913d |
    +-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+ | cidr_whitelist | |
    +-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+ | readonly | false |
    +-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+ | created | 2017 - 10 -
    02T07:52:24.838Z |
             +-- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --+
</code></pre>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>npm token revoke &lt;token|id&gt;</code>: This removes an authentication token, making it immediately unusable. This can accept both complete tokens (as you get back from <code>npm token create</code> and will find in your <code>.npmrc</code>) and ids as seen in the <code>npm token list</code> output. This will NOT accept the truncated token found in <code>npm token list</code> output. </p>
</dl>
</dl>
<h2>Index</h2>
