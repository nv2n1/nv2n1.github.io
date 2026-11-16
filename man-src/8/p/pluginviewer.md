---
title: "pluginviewer(8)"
name: "pluginviewer"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pluginviewer/"
description: "pluginviewer – list loadable SASL plugins and their properties"
---

<p>pluginviewer &#8211; list loadable SASL plugins and their properties</p>
<h2>Synopsis</h2>
<p><code>pluginviewer</code> [<code>-a</code>] [<code>-s</code>] [<code>-c</code>] [<code>-b min=N,max=N</code>] [<code>-e ssf=N,id=ID</code>] [<code>-m MECHS</code>] [<code>-x AUXPROP_MECH</code>] [<code>-f FLAGS</code>] [<code>-p PATH</code>]</p>
<h2>Description</h2>
<p><i>pluginviewer</i> can be used by a server administrator to troubleshoot SASL installations. The utility can list loadable (properly configured) client and server side plugins, as well as auxprop plugins.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></dt>
<dd>List auxprop plugins.</dd>
<dt><code>-s</code></dt>
<dd>List server authentication (SASL) plugins.</dd>
<dt><code>-c</code></dt>
<dd>List client authentication (SASL) plugins.</dd>
<dt><code>-b min=N1,max=N2</code></dt>
<dd>List client authentication (SASL) plugins. Strength of the SASL security layer in bits. min=N1 specifies the minumum strength to use (1 =&gt; integrity protection). max=N2 specifies the maximum strength to use. Only SASL mechanisms which support security layer with strength M such that N1 &lt;= M &lt;= N2 will be shown.</dd>
<dt><code>-e ssf=N,id=ID</code></dt>
<dd>Assume that an external security layer (e.g. TLS) with N-bit strength is installed. The ID is the authentication identity used by the external security layer.</dd>
<dt><code>-m MECHS</code></dt>
<dd>Limit listed SASL plugins to the ones included in the MECHS (space separated) list.</dd>
<dt><code>-x AUXPROP_MECHS</code></dt>
<dd>Limit listed auxprop plugins to the one listed in the AUXPROP_MECHS (space separated) list.</dd>
<dt><code>-f FLAGS</code></dt>
<dd>Set security flags. FLAGS is a comma separated list of one or more of the following security flags: noplain (SASL mechanism doesn&#8217;t send password in the clear during authentication), noactive (require protection from active attacks), nodict (require mechanisms which are secure against passive dictionary attacks), forwardsec (require forward secrecy), passcred (require mechanisms that can delegate client credentials), maximum (require all security flags).</dd>
<dt><code>-p PATH</code></dt>
<dd>Specifies a colon-separated search path for plugins.</dd></dl>
<h2>See Also</h2>
<dl>
<dt>rfc4422 &#8211; Simple Authentication and Security Layer (SASL)</dt>
<dd>
</dd></dl>