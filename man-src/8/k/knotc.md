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
<dt><code>-c</code>, <code>&#8211;config</code> <i>file</i></dt>
<dd>Select configuration file.</dd>
<dt><code>-s</code> <i>server</i></dt>
<dd>Remote UNIX socket/IP address (default /var/run/knot/knot.sock).</dd>
<dt><code>-p</code> <i>port</i></dt>
<dd>Remote server port (only for IP).</dd>
<dt><code>-y</code> [<i>hmac</i>:]<i>name</i>:<i>key</i></dt>
<dd>Use key specified on the command line (default algorithm is hmac-md5).</dd>
<dt><code>-k</code> <i>file</i></dt>
<dd>Use key file (as in config section &#8216;keys&#8217;).</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd>Force operation &#8211; override some checks.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd>Verbose mode &#8211; additional runtime information.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>Print version of the server.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Print help and usage.</dd></dl>
<h3>Actions:</h3>
<dl>
<dt><code>stop</code></dt>
<dd>Stop server (no-op if not running).</dd>
<dt><code>reload</code> [<i>zone</i>]&#8230;</dt>
<dd>Reload configuration and changed zones (all if not specified).</dd>
<dt><code>flush</code> [<i>zone</i>]&#8230;</dt>
<dd>Flush journal and update zone files (all if not specified).</dd>
<dt><code>status</code></dt>
<dd>Check if server is running.</dd>
<dt><code>zonestatus</code></dt>
<dd>Show status of configured zones.</dd>
<dt><code>refresh</code> [<i>zone</i>]&#8230;</dt>
<dd>Refresh slave zones (all if not specified).</dd>
<dt><code>checkconf</code></dt>
<dd>Check current server configuration.</dd>
<dt><code>checkzone</code> [<i>zone</i>]&#8230;</dt>
<dd>Check zone (all if not specified).</dd>
<dt><code>memstats</code> [<i>zone</i>]&#8230;</dt>
<dd>Estimate memory consumption for zone (all if not specified).</dd></dl>
<h2>Examples</h2>
<dl>
<dt><code>Setup a keyfile for remote control</code></dt>
<dd>
</dd><dt>1. Generate key:</dt>
<dd>
</dd><dt># dnssec-keygen -a hmac-md5 -b 256 -n HOST knotc-key</dt>
<dd>
</dd><dt>2. Extract secret in base64 format and create keyfile:</dt>
<dd>
</dd><dt># echo &quot;knotc-key hmac-md5 &lt;secret&gt;&quot; &gt; knotc.key</dt>
<dd>
</dd><dt>Make sure the key can be read/written only by the owner for security reasons.</dt>
<dd>
</dd><dt><code>Reload server remotely</code></dt>
<dd>
</dd><dt># knotc -s 127.0.0.1 -k knotc.key reload</dt>
<dd></dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-knotd/">knotd</a></code>(8), <code><a href="/docs/linux/man/5-knot-conf/">knot.conf</a></code>(5).</p>
<h2>Note</h2>
<p>The full documentation for <code>Knot DNS</code> is maintained as a Texinfo manual. If the <code>info</code> program is properly installed at your site, the <code>info Knot</code> command should give you an access to the complete manual.</p>
