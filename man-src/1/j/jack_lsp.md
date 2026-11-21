---

title: "jack_lsp(1)"
name: "jack_lsp"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack_lsp/"
description: "jack_lsp – JACK toolkit client to list informtion on ports"
---

<h2>NAME</h2>
<p> jack_lsp &#8211; JACK toolkit client to list informtion on ports</p>
<p> <code>jack_lsp</code> [ <i>-s</i> | <i>&#8211;server</i> servername ] [ <i>-AclLptvh</i> ]</p>
<p> <code>jack_lsp</code> lists all known ports associated with a JACK server. It can also optionally list various kinds of information about each port.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code>, <code>&#8211;server</code> <i>servername</i></dt>
<dd>
 Connect to the jack server named <i>servername</i></dd>
<dt><code>-A</code>, <code>&#8211;aliases</code></dt>
<dd>
 List aliases for each port</dd>
<dt><code>-c</code>, <code>&#8211;connections</code></dt>
<dd>
 List connections to/from each port</dd>
<dt><code>-l</code>, <code>&#8211;latency</code></dt>
<dd>
 Display per-port latency in frames at each port</dd>
<dt><code>-L</code>, <i>&#8211;latency</i></dt>
<dd>
 Display total latency in frames at each port</dd>
<dt><code>-p</code>, <code>&#8211;properties</code></dt>
<dd>
 Display port properties. Output may include input|output, can-monitor, physical, terminal</dd>
<dt><code>-t</code>, <code>&#8211;type</code></dt>
<dd>
 Display port type</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>
 Display help/usage message</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>
 Output version information and exit </dd>
</dl>
