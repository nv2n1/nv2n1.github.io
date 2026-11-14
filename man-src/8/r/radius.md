---
title: "radius(8)"
name: "radius"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radius/"
description: "radius – nnrpd RADIUS password authenticator"
---

<p>radius &#8211; nnrpd RADIUS password authenticator</p>
<h2>Synopsis</h2>
<p><code>radius</code> [<code>-h</code>] [<code>-f</code> <i>config</i>]</p>
<h2>Description</h2>
<p><code>radius</code> is an nnrpd authenticator, accepting a username and password from nnrpd (given to nnrpd by a reader connection) and attempting to authenticate that username and password against a <font SIZE="-1">RADIUS</font> server. See <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) for more information on how to configure an nnrpd authenticator. It is useful for a site that already does user authentication via <font SIZE="-1">RADIUS</font> and wants to authenticate news reading connections as well. </p>
<p> By default, <code>radius</code> reads <i>pathetc</i>/inn-radius.conf for configuration information, but a different configuration file can be specified with <code>-f</code>. See <i><a href="/docs/linux/man/5-inn-radius-conf/">inn-radius.conf</a></i>(5) for a description of the configuration file.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code> <i>config</i></p>
<dd>Read <i>config</i> instead of <i>pathetc</i>/inn-radius.conf for configuration information.</p>
<dt><code>-h</code></p>
<dd>Print out a usage message and exit.</dl>
<h2>Example</h2>
<p>The following <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) fragment tells nnrpd to authenticate all connections using this authenticator: </p>
<pre> auth radius {
 auth: radius
 default: &lt;FAIL&gt;
 default-domain: example.com
 }</pre>
<p><tt>&quot;@example.com&quot;</tt> will be appended to the user-supplied identity, and if <font SIZE="-1">RADIUS</font> authentication failes, the user will be assigned an identity of <tt>&quot;&lt;FAIL&gt;@example.com&quot;</tt>.</p>
<h2>Bugs</h2>
<p>It has been reported that this authenticator doesn&#8217;t work with Ascend <font SIZE="-1">RADIUS</font> servers, but does work with Cistron <font SIZE="-1">RADIUS</font> servers. It&#8217;s also believed to work with Livingston&#8217;s <font SIZE="-1">RADIUS</font> server. Contributions to make it work better with different types of <font SIZE="-1">RADIUS</font> servers would be gratefully accepted. </p>
<p> This code has not been audited against the <font SIZE="-1">RADIUS</font> protocol and may not implement it correctly.</p>
<h2>History</h2>
<p>The <font SIZE="-1">RADIUS</font> authenticator was originally written by Aidan Cully. This documentation was written by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> radius.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-radius-conf/">inn-radius.conf</a></i>(5), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) <font SIZE="-1">RFC</font>&nbsp;<wbr>2865, Remote Authentication Dial In User Service. </p>
