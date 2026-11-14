---
title: "avahi-service(5)"
name: "avahi-service"
section: "5"
letter: "a"
url: "/docs/linux/man/5-avahi-service/"
description: "avahi.service – avahi-daemon static service file"
---

<p>avahi.service &#8211; avahi-daemon static service file</p>
<h2>Synopsis</h2>
<p><code>/etc/avahi/services/*.service </code></p>
<h2>Description</h2>
<p><i>/etc/avahi/services/*.service</i> are XML fragments containing static DNS-SD service data. Every service file can contain multiple service definitions which share the same name. This is useful for publishing service data for services which implement multiple protocols. (i.e. a printer implementing _ipp._tcp and _printer._tcp)</p>
<h2>Xml Tags</h2>
<dl>
<dt><code>&lt;service-group&gt;</code> The document tag of avahi service files. Should contain one <code>&lt;name&gt;</code> and one or more <code>&lt;service&gt;</code> elements.</p>
<dd>
<dt><code>&lt;name replace-wildcards=&quot;yes|no&quot;&gt;</code> The service name. If <code>replace-wildcards</code> is &quot;yes&quot;, any occurence of the string &quot;%h&quot; will be replaced by the local host name. This can be used for service names like &quot;Remote Terminal on %h&quot;. If <code>replace-wildcards</code> is not specified, defaults to &quot;no&quot;.</p>
<dd>
<dt><code>&lt;service protocol=&quot;ipv4|ipv6|any&quot;&gt;</code> Contains the service information for exactly one service type. Should contain one <code>&lt;type&gt;</code> and one <code>&lt;port&gt;</code> element. Optionally it may contain one <code>&lt;domain-name&gt;</code>, one <code>&lt;host-name&gt;</code>, any number of <code>&lt;subtype&gt;</code> and any number of <code>&lt;txt-record&gt;</code> elements. The attribute <code>protocol</code> specifies the protocol to advertise the service on. If <code>any</code> is used (which is the default), the service will be advertised on both IPv4 and IPv6.</p>
<dd>
<dt><code>&lt;type&gt;</code> Contains the DNS-SD service type for this service. e.g. &quot;_http._tcp&quot;.</p>
<dd>
<dt><code>&lt;subtype&gt;</code> Contains an additional DNS-SD service subtype for this service. e.g. &quot;_anon._sub._<a href="ftp://ftp._tcp">ftp._tcp</a>&quot;.</p>
<dd>
<dt><code>&lt;domain-name&gt;</code> The domain name this service should be registered. If omited defaults to the default domain of the avahi daemon. (probably .local)</p>
<dd>
<dt><code>&lt;host-name&gt;</code> The host name of the host that provides this service. This should be a host that is resolvable by multicast or unicast DNS. Please note that you need to specify a fully-qualified domain name (FQDN) here, i.e. .local is not appended implicitly! The host name doesn&#8217;t need to be part of the domain specified in <code>&lt;domain-name&gt;</code>. See <code><a href="/docs/linux/man/5-avahi-hosts/">avahi.hosts</a>(5)</code> for more information how to publish additional host name mappings.</p>
<dd>
<dt><code>&lt;port&gt;</code> The IP port number the service listens on.</p>
<dd>
<dt><code>&lt;txt-record value-format=&quot;text|binary-hex|binary-base64&quot;&gt;</code> DNS-SD TXT record data. If <code>value-format</code> is &quot;text&quot;, the value of the TXT record is taken verbatim. If <code>value-format</code> is &quot;binary-hex&quot; then the value of TXT record is decoded by taking pairs of characters after the &quot;=&quot; char and interpreting them as the textual representation of the two-digit hexadecimal number. Both uppercase and lowercase hexadecimal digits are allowed. The 0x or 0X prefix is not allowed. This requires the length of the value to be even. If <code>value-format</code> is &quot;binary-base64&quot; then the value of TXT record is decoded with a base64 decoder. The character set used is A-Za-z0-9+/. This requires the length of the value to be a multiple of 4, with &quot;=&quot; as padding at the end. If <code>value-format</code> is not specified, defaults to &quot;text&quot;. Examples (all the values are decoded to the string &quot;value&quot; without quotes):</p>
<dd>&lt;txt-record&gt;key=value&lt;txt-record&gt; </p>
<p> &lt;txt-record value-format=&quot;text&quot;&gt;key=value&lt;txt-record&gt; </p>
<p> &lt;txt-record value-format=&quot;binary-hex&quot;&gt;key=76616c7565&lt;txt-record&gt; </p>
<p> &lt;txt-record value-format=&quot;binary-base64&quot;&gt;key=dmFsdWU=&lt;txt-record&gt;</dl>
<h2>Authors</h2>
<p>The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a>(8)</code>, <code><a href="/docs/linux/man/5-avahi-hosts/">avahi.hosts</a>(5)</code></p>
<h2>Comments</h2>
<p>This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth.</p>
