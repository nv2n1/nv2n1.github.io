---
title: "brlapi_connectionsettings_t(3)"
name: "brlapi_connectionsettings_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brlapi_connectionsettings_t/"
description: "brlapi_connectionSettings_t –"
---

<p>brlapi_connectionSettings_t &#8211; </p>
<p> Settings structure for <i>BrlAPI</i> connection.</p>
<h2>Synopsis</h2>
<p>#include &lt;brlapi.h&gt;</p>
<h3>Data Fields</h3>
<p>char * <code>auth</code> </p>
<p> char * <code>host</code> </p>
<h2>Detailed Description</h2>
<p>This structure holds every parameter needed to connect to <i>BrlAPI:</i> which file the authorization key can be found in and which computer to connect to. </p>
<p> <code>Examples:</code></p>
<dl COMPACT>
<dd>
<pre>brlapi_connectionSettings_t settings;
settings.auth='/etc/brlapi.key';
settings.host='foo';</pre>
</dl>
<p> <i>libbrlapi</i> will read authorization key from file /etc/brlapi.key and connect to the machine called &#8216;foo&#8217;, on the default TCP port. </p>
<pre>settings.host='10.1.0.2';</pre>
<p>lets directly enter an IP address instead of a machine name. </p>
<pre>settings.host=':1';</pre>
<p>lets <i>libbrlapi</i> connect to the local computer, on port BRLAPI_SOCKETPORTNUM+1 </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brlapi_openConnection()</code></dl>
<h2>Field Documentation</h2>
<h3>char* brlapi_connectionSettings_t::auth</h3>
<p>For security reasons, <i>libbrlapi</i> has to get authorized to connect to the <i>BrlAPI</i> server. This can be done via a secret key, for instance. This is the path to the file which holds it; it will hence have to be readable by the application. </p>
<p> Setting NULL defaults it to local installation setup or to the content of the BRLAPI_AUTH environment variable, if it exists.</p>
<h3>char* brlapi_connectionSettings_t::host</h3>
<p>This tells where the <i>BrlAPI</i> server resides: it might be listening on another computer, on any TCP port. It should look like &#8216;foo:1&#8217;, which means TCP port number BRLAPI_SOCKETPORTNUM+1 on computer called &#8216;foo&#8217;. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Please check that resolving this name works before complaining</dl>
<p> Settings NULL defaults it to localhost, using the local installation&#8217;s default TCP port, or to the content of the BRLAPI_HOST environment variable, if it exists. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for BrlAPI from the source code.</p>
