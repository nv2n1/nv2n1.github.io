---
title: "sssd-secrets(5)"
name: "sssd-secrets"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sssd-secrets/"
description: "sssd-secrets – SSSD Secrets responder"
---

<p>sssd-secrets &#8211; SSSD Secrets responder</p>
<h2>Description</h2>
<p>This manual page describes the configuration of the Secrets responder for <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8). For a detailed syntax reference, refer to the &#8220;FILE FORMAT&#8221; section of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page. </p>
<p> Many system and user applications need to store private information such as passwords or service keys and have no good way to properly deal with them. The simple approach is to embed these &#8220;secrets&#8221; into configuration files potentially ending up exposing sensitive key material to backups, config management system and in general making it harder to secure data. </p>
<p> The m[blue]<code>custodia</code>m[]<font SIZE="-2">[1]</font> project was born to deal with this problem in cloud like environments, but we found the idea compelling even at a single system level. As a security service, SSSD is ideal to host this capability while offering the same API via a Unix Socket. This will make it possible to use local calls and have them transparently routed to a local or a remote key management store like IPA Vault for storage, escrow and recovery. </p>
<p> The secrets are simple key-value pairs. Each user&#8217;s secrets are namespaced using their user ID, which means the secrets will never collide between users. Secrets can be stored inside &#8220;containers&#8221; which can be nested.</p>
<h2>Using The Secrets Responder</h2>
<p>The UNIX socket the SSSD responder listens on is located at /var/run/secrets.socket. </p>
<p> The secrets responder is socket-activated by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1). Unlike other SSSD responders, it cannot be started by adding the &#8220;secrets&#8221; string to the &#8220;service&#8221; directive. The systemd socket unit is called &#8220;sssd-secrets.socket&#8221; and the corresponding service file is called &#8220;sssd-secrets.service&#8221;. In order for the service to be socket-activated, make sure the socket is enabled and active and the service is enabled: </p>
<dl>
<dd>
<pre>systemctl start sssd-secrets.socket
systemctl enable sssd-secrets.socket
systemctl enable sssd-secrets.service</pre>
</dl>
<p> Please note your distribution may already configure the units for you.</p>
<h2>Configuration Options</h2>
<p>The generic SSSD responder options such as &#8220;debug_level&#8221; or &#8220;fd_limit&#8221; are accepted by the secrets responder. Please refer to the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page for a complete list. In addition, there are some secrets-specific options as well. </p>
<p> provider (string)</p>
<dl>
<dd>This option specifies where should the secrets be stored. The secrets responder can configure a per-user subsections that define which provider store the secrets for this particular user. The per-user subsections should contain all options for that user&#8217;s provider. If a per-user section does not exist, the global settings from the secret responder&#8217;s section are used. The following providers are supported: </p>
<p> local</p>
<dl>
<dd>The secrets are stored in a local database, encrypted at rest with a master key. The local provider does not have any additional config options at the moment.</dl>
<p> proxy</p>
<dl>
<dd>The secrets responder forwards the requests to a Custodia server. The proxy provider supports several additional options (see below).</dl>
<p> Default: local</dl>
<p> containers_nest_level (integer)</p>
<dl>
<dd>This option specifies the maximum allowed number of nested containers. </p>
<p> Default: 4</dl>
<p> max_secrets (integer)</p>
<dl>
<dd>This option specifies the maximum number of secrets that can be stored. </p>
<p> Default: 1024</dl>
<p> max_payload_size (integer)</p>
<dl>
<dd>This option specifies the maximum payload size allowed for a secret payload in kilobytes. </p>
<p> Default: 16</dl>
<p> The following options are only applicable for configurations that use the &#8220;proxy&#8221; provider. </p>
<p> proxy_url (string)</p>
<dl>
<dd>The URL the Custodia server is listening on. At the moment, http and https protocols are supported. </p>
<p> The format of the URI must match the format defined in RFC 2732: </p>
<p> http[s]://&lt;host&gt;[:port] </p>
<p> Example: <a rel="nofollow" href="http://localhost:8080">http://localhost:8080</a></dl>
<p> auth_type (string)</p>
<dl>
<dd>The method to use when authenticating to a Custodia server. The following authentication methods are supported: </p>
<p> basic_auth</p>
<dl>
<dd>Authenticate with a username and a password as set in the &#8220;username&#8221; and &#8220;password&#8221; options.</dl>
<p> header</p>
<dl>
<dd>Authenticate with HTTP header value as defined in the &#8220;auth_header_name&#8221; and &#8220;auth_header_value&#8221; configuration options.</dl>
</dl>
<p> auth_header_name (string)</p>
<dl>
<dd>If set, the secrets responder would put a header with this name into the HTTP request with the value defined in the &#8220;auth_header_value&#8221; configuration option. </p>
<p> Example: MYSECRETNAME</dl>
<p> auth_header_value (string)</p>
<dl>
<dd>The value sssd-secrets would use for the &#8220;auth_header_name&#8221;. </p>
<p> Example: mysecret</dl>
<p> forward_headers (list of strings)</p>
<dl>
<dd>The list of HTTP headers to forward to the Custodia server together with the request. </p>
<p> Default: not set</dl>
<p> verify_peer (boolean)</p>
<dl>
<dd>Whether peer&#8217;s certificate should be verified and valid if HTTPS protocol is used with the proxy provider. </p>
<p> Default: true</dl>
<p> verify_host (boolean)</p>
<dl>
<dd>Whether peer&#8217;s hostname must match with hostname in its certificate if HTTPS protocol is used with the proxy provider. </p>
<p> Default: true</dl>
<p> capath (string)</p>
<dl>
<dd>Path to directory containing stored certificate authority certificates. System default path is used if this option is not set. </p>
<p> Default: not set</dl>
<p> cacert (string)</p>
<dl>
<dd>Path to file containing server&#8217;s certificate authority certificate. If this option is not set then the CA&#8217;s certificate is looked up in &#8220;capath&#8221;. </p>
<p> Default: not set</dl>
<p> cert (string)</p>
<dl>
<dd>Path to file containing client&#8217;s certificate if required by the server. This file may also contain private key or the private key may be in separate file set with &#8220;key&#8221;. </p>
<p> Default: not set</dl>
<p> key (string)</p>
<dl>
<dd>Path to file containing client&#8217;s private key. </p>
<p> Default: not set</dl>
<h2>Using The Rest Api</h2>
<p>This section lists the available commands and includes examples using the <code><a href="/docs/linux/man/1-curl/">curl</a></code>(1) utility. All requests towards the proxy provider must set the Content Type header to &#8220;application/json&#8221;. In addition, the local provider also supports Content Type set to &#8220;application/octet-stream&#8221;. Secrets stored with requests that set the Content Type header to &#8220;application/octet-stream&#8221; are base64-encoded when stored and decoded when retrieved, so it&#8217;s not possible to store a secret with one Content Type and retrieve with another. The secret URI must begin with /secrets/. </p>
<p> Listing secrets</p>
<dl>
<dd>To list the available secrets, send a HTTP GET request with a trailing slash appended to the container path. </p>
<p> Example: </p>
<dl>
<dd>
<pre>curl -H &quot;Content-Type: application/json&quot; \
 --unix-socket /var/run/secrets.socket \
 -XGET <a rel="nofollow" href="http://localhost/secrets/">http://localhost/secrets/</a></pre>
</dl>
</dl>
<p> Retrieving a secret</p>
<dl>
<dd>To read a value of a single secret, send a HTTP GET request without a trailing slash. The last portion of the URI is the name of the secret. </p>
<p> Examples: </p>
<dl>
<dd>
<pre>curl -H &quot;Content-Type: application/json&quot; \
 --unix-socket /var/run/secrets.socket \
 -XGET <a rel="nofollow" href="http://localhost/secrets/foo">http://localhost/secrets/foo</a></pre>
</dl>
<dl>
<dd>
<pre>curl -H &quot;Content-Type: application/octet-stream&quot; \
 --unix-socket /var/run/secrets.socket \
 -XGET <a rel="nofollow" href="http://localhost/secrets/bar">http://localhost/secrets/bar</a></pre>
</dl>
</dl>
<p> Setting a secret</p>
<dl>
<dd>To set a secret using the &#8220;application/json&#8221; type, send a HTTP PUT request with a JSON payload that includes type and value. The type should be set to &quot;simple&quot; and the value should be set to the secret value. If a secret with that name already exists, the response is a 409 HTTP error. </p>
<p> The &#8220;application/json&#8221; type just sends the secret as the message payload. </p>
<p> The following example sets a secret named &#8216;foo&#8217; to a value of &#8216;foosecret&#8217; and a secret named &#8216;bar&#8217; to a value of &#8216;barsecret&#8217; using a different Content Type. </p>
<dl>
<dd>
<pre>curl -H &quot;Content-Type: application/json&quot; \
 --unix-socket /var/run/secrets.socket \
 -XPUT <a rel="nofollow" href="http://localhost/secrets/foo">http://localhost/secrets/foo</a> \
 -d'{&quot;type&quot;:&quot;simple&quot;,&quot;value&quot;:&quot;foosecret&quot;}'</pre>
</dl>
<dl>
<dd>
<pre>curl -H &quot;Content-Type: application/octet-stream&quot; \
 --unix-socket /var/run/secrets.socket \
 -XPUT <a rel="nofollow" href="http://localhost/secrets/bar">http://localhost/secrets/bar</a> \
 -d'barsecret'</pre>
</dl>
</dl>
<p> Creating a container</p>
<dl>
<dd>Containers provide an additional namespace for this user&#8217;s secrets. To create a container, send a HTTP POST request, whose URI ends with the container name. Please note the URI must end with a trailing slash. </p>
<p> The following example creates a container named &#8216;mycontainer&#8217;: </p>
<dl>
<dd>
<pre>curl -H &quot;Content-Type: application/json&quot; \
 --unix-socket /var/run/secrets.socket \
 -XPOST <a rel="nofollow" href="http://localhost/secrets/mycontainer/">http://localhost/secrets/mycontainer/</a></pre>
</dl>
<p> To manipulate secrets under this container, just nest the secrets underneath the container path: </p>
<dl>
<dd>
<pre><a rel="nofollow" href="http://localhost/secrets/mycontainer/mysecret">http://localhost/secrets/mycontainer/mysecret</a></pre>
</dl>
</dl>
<p> Deleting a secret or a container</p>
<dl>
<dd>To delete a secret or a container, send a HTTP DELETE request with a path to the secret or the container. </p>
<p> The following example deletes a secret named &#8216;foo&#8217;. </p>
<dl>
<dd>
<pre>curl -H &quot;Content-Type: application/json&quot; \
 --unix-socket /var/run/secrets.socket \
 -XDELETE <a rel="nofollow" href="http://localhost/secrets/foo">http://localhost/secrets/foo</a></pre>
</dl>
</dl>
<h2>Example Custodia And Proxy Provider Configuration</h2>
<p>For testing the proxy provider, you need to set up a Custodia server to proxy requests to. Please always consult the Custodia documentation, the configuration directives might change with different Custodia versions. </p>
<p> This configuration will set up a Custodia server listening on <a rel="nofollow" href="http://localhost:8080,">http://localhost:8080,</a> allowing anyone with header named MYSECRETNAME set to mysecretkey to communicate with the Custodia server. Place the contents into a file (for example, <i>custodia.conf</i>): </p>
<dl>
<dd>
<pre>[global]
server_version = &quot;Secret/0.0.7&quot;
server_url = <a rel="nofollow" href="http://localhost:8080/">http://localhost:8080/</a>
auditlog = /var/log/custodia.log
debug = True
[store:simple]
handler = custodia.store.sqlite.SqliteStore
dburi = /var/lib/custodia.db
table = secrets
[auth:header]
handler = custodia.httpd.authenticators.SimpleHeaderAuth
header = MYSECRETNAME
value = mysecretkey
[authz:paths]
handler = custodia.httpd.authorizers.SimplePathAuthz
paths = /secrets
[/]
handler = custodia.root.Root
store = simple</pre>
</dl>
<p> Then run the <i>custodia</i> command, pointing it at the config file as a command line argument. </p>
<p> Please note that currently it&#8217;s not possible to proxy all requests globally to a Custodia instance. Instead, per-user subsections for user IDs that should proxy requests to Custodia must be defined. The following example illustrates a configuration, where the user with UID 123 would proxy their requests to Custodia, but all other user&#8217;s requests would be handled by a local provider. </p>
<dl>
<dd>
<pre>[secrets]
[secrets/users/123]
provider = proxy
proxy_url = <a rel="nofollow" href="http://localhost:8080/secrets/">http://localhost:8080/secrets/</a>
auth_type = header
auth_header_name = MYSECRETNAME
auth_header_value = mysecretkey</pre>
</dl>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>custodia</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/latchset/custodia">https://github.com/latchset/custodia</a></dl>
