---
title: "cockpit-conf(5)"
name: "cockpit-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cockpit-conf/"
description: "cockpit.conf – Cockpit configuration file"
---

<p>cockpit.conf &#8211; Cockpit configuration file</p>
<h2>Description</h2>
<p>Cockpit can be configured via /etc/cockpit/cockpit.conf. That file has a INI file syntax and thus contains key / value pairs, grouped into topical groups. See the examples below for details.. </p>
<p> Note: The port that cockpit listens on cannot be changed in this file. To change the port change the systemd cockpit.socket file.</p>
<h2>Webservice</h2>
<p><code>Origins</code></p>
<dl>
<dd>By default cockpit will not accept crossdomain websocket connections. Use this setting to allow access from alternate domains. Origins should include scheme, host and port, if necessary. </p>
<dl>
<dd>
<pre>[WebService]
Origins = <a rel="nofollow" href="https://somedomain1.com">https://somedomain1.com</a> <a href="https://somedomain2.com:9090">https://somedomain2.com:9090</a></pre>
</dl>
</dl>
<p> <code>ProtocolHeader</code></p>
<dl>
<dd>Configure cockpit to look at the contents of this header to determine if a connection is using tls. This should only be used when cockpit is behind a reverse proxy, and care should be taken to make sure that incoming requests cannot set this header. </p>
<dl>
<dd>
<pre>[WebService]
ProtocolHeader = X-Forwarded-Proto</pre>
</dl>
</dl>
<p> <code>LoginTitle</code></p>
<dl>
<dd>Set the browser title for the login screen.</dl>
<p> <code>LoginTo</code></p>
<dl>
<dd>When set to true the <i>Connect to</i> option on the login screen is visible and allows logging into another server. If this option is not specified then it will be automatically detected based on whether the <code>cockpit-ssh</code> process is available or not.</dl>
<p> <code>MaxStartups</code></p>
<dl>
<dd>Same as the <code>sshd</code> configuration option by the same name. Specifies the maximum number of concurrent login attempts allowed. Additional connections will be dropped until authentication succeeds or the connections are closed. Defaults to 10. </p>
<p> Alternatively, random early drop can be enabled by specifying the three colon separated values start:rate:full (e.g. &quot;10:30:60&quot;). Cockpit will start refusing authentication attempts with a probability of rate/100 (30%) if there are currently start (10) unauthenticated connections. The probability increases linearly and all connection attempts are refused if the number of unauthenticated connections reaches full (60).</dl>
<p> <code>AllowUnencrypted</code></p>
<dl>
<dd>If true, cockpit will accept unencrypted HTTP connections. Otherwise, it redirects all HTTP connections to HTTPS. Exceptions are connections from localhost and for certain URLs (like /ping). Defaults to false.</dl>
<p> <code>UrlRoot</code></p>
<dl>
<dd>The root URL where you will be serving cockpit. When provided cockpit will expect all requests to be prefixed with the given url. This is mostly useful when you are using cockpit behind a reverse proxy, such as nginx. /cockpit/ and /cockpit+ are reserved and should not be used. For example /cockpit-new/ is ok. /cockpit/ and /cockpit+new/ are not.</dl>
<h2>Oauth</h2>
<p>Cockpit can be configured to support the m[blue]<code>implicit grant</code>m[]<font SIZE="-2">[1]</font> OAuth authorization flow. When successful the resulting oauth token will be passed to cockpit-ws using the Bearer auth-scheme. For a login to be successful, cockpit will also need a to be configured to verify and allow Bearer tokens. </p>
<p> <code>URL</code></p>
<dl>
<dd>This is the url that cockpit will redirect the users browser to when it needs to obtain an oauth token. Cockpit will add a redirect_uri parameter to the url with the location of where the oauth provider should redirect to once a token has been obtained.</dl>
<p> <code>ErrorParam</code></p>
<dl>
<dd>When a oauth provider redirects a user back to cockpit, look for this parameter in the querystring or fragment portion of the url to find a error message. When not provided it will default to error_description</dl>
<p> <code>TokenParam</code></p>
<dl>
<dd>When a oauth provider redirects a user back to cockpit, look for this parameter in the querystring or fragment portion of the url to find the access token. When not provided it will default to access_token</dl>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the m[blue]<code>upstream bug tracker</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>Author</h2>
<p>Cockpit has been written by many m[blue]<code>contributors</code>m[]<font SIZE="-2">[3]</font>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cockpit-ws/">cockpit-ws</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>implicit grant</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc6749#section-4.2">https://tools.ietf.org/html/rfc6749#section-4.2</a></dl>
<dt> 2.</p>
<dd>upstream bug tracker</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/cockpit-project/cockpit/issues/new">https://github.com/cockpit-project/cockpit/issues/new</a></dl>
<dt> 3.</p>
<dd>contributors</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/cockpit-project/cockpit/">https://github.com/cockpit-project/cockpit/</a></dl>
