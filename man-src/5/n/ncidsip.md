---
title: "ncidsip(5)"
name: "ncidsip"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ncidsip/"
description: "ncidsip.conf – ncidsip configuration file"
---

<p><code>ncidsip.conf</code> &#8211; ncidsip configuration file</p>
<h2>Description</h2>
<p>The <i>ncidsip.conf</i> file contains the configuration information for <i>ncidsip</i>, the Network Caller ID SIP Gateway. </p>
<p> The <i>ncidsip.conf</i> file understands 3 types of lines:</p>
<dl>
<dt><code>blank line</code></p>
<dd>skip it</p>
<dt><code>comment line, beginning with &#8216;#&#8217;</code></p>
<dd>skip it</p>
<dt><code>Variable=Argument</code></p>
<dd></dl>
<p> There is only one variable to set: args. Args is expected to contain the command line options. You should not set the &quot;-v|&#8211;verbose&quot;, &quot;-V|&#8211;version&quot;, &quot;&#8211;debug&quot;, or the &quot;-h|&#8211;help&quot; options See ncidsip.8 for a complete list of variables to set and what the default values are.</p>
<h2>Examples</h2>
<pre><code>Set the SIP port to 5061

args=&quot;--sip=:5061&quot;


Set PID file

args=&quot;--pidfile=/var/run/ncidsip.pid&quot;</code></pre>
<h2>See Also</h2>
<p>ncidd.8, ncidsip.8, sip2ncid.8 </p>
