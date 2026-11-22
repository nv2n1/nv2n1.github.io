---
title: "basic_msnt_multi_domain_auth(8)"
name: "basic_msnt_multi_domain_auth"
section: "8"
letter: "b"
url: "/docs/linux/man/8-basic_msnt_multi_domain_auth/"
---

<pre> basic_msnt_multi_domain_auth</pre>
<h2>Synopsis</h2>
<pre> basic_msnt_multi_domain_auth [options]</pre>
<h2>Description</h2>
<p><code>basic_msnt_multi_domain_auth</code> is a Squid authenticator to check user credentials against multiple NT domains using <code>nmblookup</code>. </p>
<p> The user is expected to enter his/her credentials as domain\username or domain/username (in analogy to what MS-Proxy does). </p>
<p> Requires Authen::SMB from CPAN and Samba if you need to perform NETBIOS queries.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>--debug</code></dt>
<dd> <p> Write debug info to stderr. </p>
 </dd>
<dt><code>--wins-server</code></dt>
<dd> <p> Use the named WINS server. </p>
<pre><code> Default: broadcast will be attempted.
</code></pre>
 </dd>
<dt><code>--no-fqdn</code></dt>
<dd> <p> Some servers don&#8217;t like to be called by their fully qualified name. Define this if you wish to call them ONLY by their hostname. </p>
 </dd>
<dt><code>--no-rdns</code></dt>
<dd> <p> Some servers really really want to be called by address. </p>
 </dd></dl>
<h2>AUTHOR</h2>
<p> This program was written by <i>Francesco Chemolli &lt;kinkie [at] kame.usr.dsi.unimi.it</i>&gt; </p>
<p> This manual was written by <i>Amos Jeffries &lt;squid3 [at] treenet.co.nz</i>&gt;  </p>
<h2>COPYRIGHT</h2>
<pre><code> * Copyright (C) 1996-2016 The Squid Software Foundation and contributors
 *
 * Squid software is distributed under GPLv2+ license and includes
 * contributions from numerous individuals and organizations.
 * Please see the COPYING and CONTRIBUTORS files for details.
</code></pre>
<h2>QUESTIONS</h2>
<p> Questions on the usage of this program can be sent to the <i>Squid Users mailing list &lt;squid-users [at] squid-cache.org</i>&gt;  </p>
<h2>REPORTING BUGS</h2>
<p> Bug reports need to be made in English. See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org</i>&gt; </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list &lt;squid-dev [at] squid-cache.org</i>&gt;  </p>
<h2>SEE ALSO</h2>
<p> squid (8), GPL \<a href="/docs/linux/man/7-fIs0/">fIs0</a>(7), </p>
<p> The Squid FAQ wiki <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq">http://wiki.squid-cache.org/SquidFaq</a> </p>
<p> The Squid Configuration Manual <a rel="nofollow" href="http://www.squid-cache.org/Doc/config/">http://www.squid-cache.org/Doc/config/</a> </p>
