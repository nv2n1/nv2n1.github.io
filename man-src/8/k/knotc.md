---
title: "knotc(8)"
name: "knotc"
section: "8"
letter: "k"
url: "/docs/linux/man/8-knotc/"
description: "knotc – Knot DNS control utility"
---

<p><code>knotc</code> &#8211; Knot DNS control utility</p>
<h2>Synopsis</h2>
<p><code>knotc</code> [<i>parameters</i>] <i>action</i> [<i>action_args</i>]</p>
<h2>Description</h2>
<h3>Parameters:</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;config</code> <i>file</i></p>
<dd>Select configuration file.</p>
<dt><code>-s</code> <i>server</i></p>
<dd>Remote UNIX socket/IP address (default /var/run/knot/knot.sock).</p>
<dt><code>-p</code> <i>port</i></p>
<dd>Remote server port (only for IP).</p>
<dt><code>-y</code> [<i>hmac</i>:]<i>name</i>:<i>key</i></p>
<dd>Use key specified on the command line (default algorithm is hmac-md5).</p>
<dt><code>-k</code> <i>file</i></p>
<dd>Use key file (as in config section &#8216;keys&#8217;).</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Force operation &#8211; override some checks.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose mode &#8211; additional runtime information.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version of the server.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and usage.</dl>
<h3>Actions:</h3>
<dl>
<dt><code>stop</code></p>
<dd>Stop server (no-op if not running).</p>
<dt><code>reload</code> [<i>zone</i>]&#8230;</p>
<dd>Reload configuration and changed zones (all if not specified).</p>
<dt><code>flush</code> [<i>zone</i>]&#8230;</p>
<dd>Flush journal and update zone files (all if not specified).</p>
<dt><code>status</code></p>
<dd>Check if server is running.</p>
<dt><code>zonestatus</code></p>
<dd>Show status of configured zones.</p>
<dt><code>refresh</code> [<i>zone</i>]&#8230;</p>
<dd>Refresh slave zones (all if not specified).</p>
<dt><code>checkconf</code></p>
<dd>Check current server configuration.</p>
<dt><code>checkzone</code> [<i>zone</i>]&#8230;</p>
<dd>Check zone (all if not specified).</p>
<dt><code>memstats</code> [<i>zone</i>]&#8230;</p>
<dd>Estimate memory consumption for zone (all if not specified).</dl>
<h2>Examples</h2>
<dl>
<dt><code>Setup a keyfile for remote control</code></p>
<dd>
<dt>1. Generate key:</p>
<dd>
<dt># dnssec-keygen -a hmac-md5 -b 256 -n HOST knotc-key</p>
<dd>
<dt>2. Extract secret in base64 format and create keyfile:</p>
<dd>
<dt># echo &quot;knotc-key hmac-md5 &lt;secret&gt;&quot; &gt; knotc.key</p>
<dd>
<dt>Make sure the key can be read/written only by the owner for security reasons.</p>
<dd>
<dt><code>Reload server remotely</code></p>
<dd>
<dt># knotc -s 127.0.0.1 -k knotc.key reload</p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-knotd/">knotd</a></code>(8), <code><a href="/docs/linux/man/5-knot-conf/">knot.conf</a></code>(5).</p>
<h2>Note</h2>
<p>The full documentation for <code>Knot DNS</code> is maintained as a Texinfo manual. If the <code>info</code> program is properly installed at your site, the <code>info Knot</code> command should give you an access to the complete manual.</p>
