---
title: "client-conf(5)"
name: "client-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-client-conf/"
description: "client.conf – client configuration file for cups (deprecated on macos)"
---

<p>client.conf &#8211; client configuration file for cups (deprecated on macos)</p>
<h2>Description</h2>
<p>The <code>client.conf</code> file configures the CUPS client and is normally located in the <i>/etc/cups</i> and/or <i>~/.cups</i> directories. Each line in the file can be a configuration directive, a blank line, or a comment. Comment lines start with the # character. </p>
<p> <code>Note:</code> Starting with macOS 10.7, this file is only used by command-line and X11 applications plus the IPP backend. The <code>ServerName</code> directive is not supported on macOS at all. Starting with macOS 10.12, all applications can access these settings in the <i>/Library/Preferences/org.cups.PrintingPrefs.plist</i> file instead. See the NOTES section below for more information.</p>
<h3>Directives</h3>
<p>The following directives are understood by the client. Consult the online help for detailed descriptions:</p>
<dl>
<dt><code>AllowAnyRoot Yes</code></p>
<dd>
<dt><code>AllowAnyRoot No</code></p>
<dd>Specifies whether to allow TLS with certificates that have not been signed by a trusted Certificate Authority. The default is &quot;Yes&quot;.</p>
<dt><code>AllowExpiredCerts Yes</code></p>
<dd>
<dt><code>AllowExpiredCerts No</code></p>
<dd>Specifies whether to allow TLS with expired certificates. The default is &quot;No&quot;.</p>
<dt><code>DigestOptions DenyMD5</code></p>
<dd>
<dt><code>DigestOptions None</code></p>
<dd>Specifies HTTP Digest authentication options. <code>DenyMD5</code> disables support for the original MD5 hash algorithm.</p>
<dt><code>Encryption IfRequested</code></p>
<dd>
<dt><code>Encryption Never</code></p>
<dd>
<dt><code>Encryption Required</code></p>
<dd>Specifies the level of encryption that should be used.</p>
<dt><code>GSSServiceName </code><i>name</i></p>
<dd>Specifies the Kerberos service name that is used for authentication, typically &quot;host&quot;, &quot;http&quot;, or &quot;ipp&quot;. CUPS adds the remote hostname (&quot;name [at] server.example.com&quot;) for you. The default name is &quot;http&quot;.</p>
<dt><code>ServerName </code><i>hostname-or-ip-address</i>[<i>:port</i>]</p>
<dd>
<dt><code>ServerName </code><i>/domain/socket</i></p>
<dd>Specifies the address and optionally the port to use when connecting to the server. <code>Note: This directive is not supported on macOS 10.7 or later.</code></p>
<dt><code>ServerName </code><i>hostname-or-ip-address</i>[<i>:port</i>]<code>/version=1.1</code></p>
<dd>Specifies the address and optionally the port to use when connecting to a server running CUPS 1.3.12 and earlier.</p>
<dt><code>SSLOptions </code>[<i>AllowDH</i>] [<i>AllowRC4</i>] [<i>AllowSSL3</i>] [<i>DenyCBC</i>] [<i>DenyTLS1.0</i>] [<i>MaxTLS1.0</i>] [<i>MaxTLS1.1</i>] [<i>MaxTLS1.2</i>] [<i>MaxTLS1.3</i>] [<i>MinTLS1.0</i>] [<i>MinTLS1.1</i>] [<i>MinTLS1.2</i>] [<i>MinTLS1.3</i>]</p>
<dd>
<dt><code>SSLOptions None</code></p>
<dd>Sets encryption options (only in /etc/cups/client.conf). By default, CUPS only supports encryption using TLS v1.0 or higher using known secure cipher suites. Security is reduced when <i>Allow</i> options are used. Security is enhanced when <i>Deny</i> options are used. The <i>AllowDH</i> option enables cipher suites using plain Diffie-Hellman key negotiation (not supported on systems using GNU TLS). The <i>AllowRC4</i> option enables the 128-bit RC4 cipher suites, which are required for some older clients. The <i>AllowSSL3</i> option enables SSL v3.0, which is required for some older clients that do not support TLS v1.0. The <i>DenyCBC</i> option disables all CBC cipher suites. The <i>DenyTLS1.0</i> option disables TLS v1.0 support &#8211; this sets the minimum protocol version to TLS v1.1. The <i>MinTLS</i> options set the minimum TLS version to support. The <i>MaxTLS</i> options set the maximum TLS version to support. Not all operating systems support TLS 1.3 at this time.</p>
<dt><code>TrustOnFirstUse Yes</code></p>
<dd>
<dt><code>TrustOnFirstUse No</code></p>
<dd>Specifies whether to trust new TLS certificates by default. The default is &quot;Yes&quot;.</p>
<dt><code>User </code><i>name</i></p>
<dd>Specifies the default user name to use for requests.</p>
<dt><code>UserAgentTokens None</code></p>
<dd>
<dt><code>UserAgentTokens ProductOnly</code></p>
<dd>
<dt><code>UserAgentTokens Major</code></p>
<dd>
<dt><code>UserAgentTokens Minor</code></p>
<dd>
<dt><code>UserAgentTokens Minimal</code></p>
<dd>
<dt><code>UserAgentTokens OS</code></p>
<dd>
<dt><code>UserAgentTokens Full</code></p>
<dd>Specifies what information is included in the User-Agent header of HTTP requests. &quot;None&quot; disables the User-Agent header. &quot;ProductOnly&quot; reports &quot;CUPS&quot;. &quot;Major&quot; reports &quot;CUPS/major IPP/2&quot;. &quot;Minor&quot; reports &quot;CUPS/major.minor IPP/2.1&quot;. &quot;Minimal&quot; reports &quot;CUPS/major.minor.patch IPP/2.1&quot;. &quot;OS&quot; reports &quot;CUPS/major.minor.path (osname osversion) IPP/2.1&quot;. &quot;Full&quot; reports &quot;CUPS/major.minor.path (osname osversion; architecture) IPP/2.1&quot;. The default is &quot;Minimal&quot;.</p>
<dt><code>ValidateCerts Yes</code></p>
<dd>
<dt><code>ValidateCerts No</code></p>
<dd>Specifies whether to only allow TLS with certificates whose common name matches the hostname. The default is &quot;No&quot;.</dl>
<h2>Notes</h2>
<p>The <code>client.conf</code> file is deprecated on macOS and will no longer be supported in a future version of CUPS. Configuration settings can instead be viewed or changed using the <code><a href="/docs/linux/man/1-defaults/">defaults</a></code>(1) command: </p>
<pre>defaults write /Library/Preferences/org.cups.PrintingPrefs.plist Encryption Required
defaults write /Library/Preferences/org.cups.PrintingPrefs.plist TrustOnFirstUse -bool NO
defaults read /Library/Preferences/org.cups.PrintingPrefs.plist Encryption</pre>
<p>On Linux and other systems using GNU TLS, the <i>/etc/cups/ssl/site.crl</i> file, if present, provides a list of revoked X.509 certificates and is used when validating certificates.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-cups/">cups</a></code>(1), <code><a href="/docs/linux/man/1-default/">default</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
