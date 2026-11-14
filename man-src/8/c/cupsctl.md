---
title: "cupsctl(8)"
name: "cupsctl"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cupsctl/"
description: "cupsctl – configure cupsd.conf options"
---

<p>cupsctl &#8211; configure cupsd.conf options</p>
<h2>Synopsis</h2>
<p><code>cupsctl</code> [ <code>-E</code> ] [ <code>-U</code> <i>username</i> ] [ <code>-h</code> <i>server</i>[<code>:</code><i>port</i>] ] [ <code>&#8212;</code>[<code>no-</code>]<code>debug-logging</code> ] [ <code>&#8212;</code>[<code>no-</code>]<code>remote-admin</code> ] [ <code>&#8212;</code>[<code>no-</code>]<code>remote-any</code> ] [ <code>&#8212;</code>[<code>no-</code>]<code>share-printers</code> ] [ <code>&#8212;</code>[<code>no-</code>]<code>user-cancel-any</code> ] [ <i>name=value</i> ]</p>
<h2>Description</h2>
<p><code>cupsctl</code> updates or queries the <i>cupsd.conf</i> file for a server. When no changes are requested, the current configuration values are written to the standard output in the format &quot;name=value&quot;, one per line.</p>
<h2>Options</h2>
<p>The following options are recognized:</p>
<dl>
<dt><code>-E</code></p>
<dd>Enables encryption on the connection to the scheduler.</p>
<dt><code>-U </code><i>username</i></p>
<dd>Specifies an alternate username to use when authenticating with the scheduler.</p>
<dt><code>-h </code><i>server</i>[<code>:</code><i>port</i>]</p>
<dd>Specifies the server address.</p>
<dt><code>&#8212;</code>[<code>no-</code>]<code>debug-logging</code></p>
<dd>Enables (disables) debug logging to the <i>error_log</i> file.</p>
<dt><code>&#8212;</code>[<code>no-</code>]<code>remote-admin</code></p>
<dd>Enables (disables) remote administration.</p>
<dt><code>&#8212;</code>[<code>no-</code>]<code>remote-any</code></p>
<dd>Enables (disables) printing from any address, e.g., the Internet.</p>
<dt><code>&#8212;</code>[<code>no-</code>]<code>share-printers</code></p>
<dd>Enables (disables) sharing of local printers with other computers.</p>
<dt><code>&#8212;</code>[<code>no-</code>]<code>user-cancel-any</code></p>
<dd>Allows (prevents) users to cancel jobs owned by others.</dl>
<h2>Examples</h2>
<p>Display the current settings: </p>
<pre> cupsctl</pre>
<p>Enable debug logging: </p>
<pre> cupsctl --debug-logging</pre>
<p>Get the current debug logging state: </p>
<pre> cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'</pre>
<p>Disable printer sharing: </p>
<pre> cupsctl --no-share-printers</pre>
<h2>Known Issues</h2>
<p>You cannot set the Listen or Port directives using <code>cupsctl</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5), <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8),<br />
 CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
