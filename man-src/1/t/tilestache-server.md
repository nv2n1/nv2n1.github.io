---

title: "tilestache-server(1)"
name: "tilestache-server"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tilestache-server/"
description: "tilestache-server – seed a single layer in your TileStache configuration"
---

<h2>NAME</h2>
<p> tilestache-server &#8211; seed a single layer in your TileStache configuration</p>
<p> <code>tilestache-server</code> [<i>options</i>]</p>
<p> This manual page documents briefly the <code>tilestache-server</code> command. </p>
<p> <code>tilestache-server</code> serves tiles through Werkzeug, using a tilestache configuration file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;config</code> <i>file</i></dt>
<dd> Path to configuration file. Defaults to <i>tilestache.cfg</i>.</dd>
<dt><code>-i</code>, <code>&#8211;ip</code> <i>address</i></dt>
<dd> IP address to listen to. Defaults to <i>127.0.0.1</i>.</dd>
<dt><code>-p</code>, <code>&#8211;port</code> <i>port</i></dt>
<dd> Port number to listen to. Defaults to <i>8080</i>.</dd>
<dt><code>&#8211;include-path</code> <i>paths</i></dt>
<dd> Add the following colon-separated list of paths to Python&#8217;s include path (aka sys.path).</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tilestache-render/">tilestache-render</a></code>(1) <code><a href="/docs/linux/man/1-tilestache-seed/">tilestache-seed</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>TileStache</code> was written by Michal Migurski &lt;mike [at] stamen.com&gt;. </p>
<p> This manual page was written by David Paleino &lt;dapal [at] debian.org&gt;, for the Debian project (and may be used by others). </p>
