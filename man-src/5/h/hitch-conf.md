---
title: "hitch-conf(5)"
name: "hitch-conf"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hitch-conf/"
---

Hitch.conf - Configuration file for Hitch

<h2>Description</h2>

hitch.conf is the configuration file for <i><a HREF="/docs/linux/man/8-hitch/">hitch</a>(8)</i>. The configuration file is loaded using the Hitch option --config=, and can thus have different names and can exist in different locations. 

 Almost all options available in hitch.conf can be specified or overridden in the command line of Hitch, as described in <a HREF="/docs/linux/man/8-hitch/">hitch</a>(8). 

 The Hitch configuration file consists of a series of option assignments. Some options (pem-file, frontend) can be be set several times, and the effect is that multiple certificate files and &quot;listening frontends&quot; are defined. Other options can only be assigned once. 

 The hash mark, or pound sign (&quot;#&quot;), is used as a &quot;comment&quot; character. You can use it to annotate your config file. All text after the comment character to the end of the line is ignored. Empty lines are ignored.

<h2>Options</h2>

Options can either be in the top level of the configuration file (global scope), or inside a <i>frontend block</i>. Options inside a frontend block only affect the frontend, while options in the top level sets defaults for all frontends. 

 Unless otherwise noted below, options can only be used in the top level.

<h3>alpn-protos = &lt;protocol-list&gt;</h3>

Comma separated list of protocols supported by the backend in a quoted string. The list is used select protocols when the client supports Next Protocol Negotiation (NPN) or Application-Layer Protocol Negotiation (ALPN). If Hitch is compiled against a OpenSSL version that does not support ALPN, only NPN will be used to select a protocol. 

 The result of the NPN/ALPN negotiation will be communicated to the backend if and only if write-proxy-v2 or proxy-proxy is used. For HTTP/2 to work with modern browsers, ALPN negotiation is required.

<h3>backend = [HOST]:PORT</h3>

The host and port Hitch connects to when receiving a connection. Only a single backend is supported.

<h3>backlog = &lt;number&gt;</h3>

Listen backlog size

<h3>chroot = &lt;string&gt;</h3>

Chroot directory

<h3>ciphers = ...</h3>

List of ciphers to use in the secure communication. Refer to the OpenSSL documentation for a complete list of supported ciphers. 

 If not specified, OpenSSL will allow all ciphers. System administrators are advised to either only support strong ciphers (as in the example file below) or to pay close attention to security advisories related OpenSSL's ciphers. 

 This option is also available in frontend blocks.

<h3>daemon = on|off</h3>

Run as daemon. Default is off.

<h3>frontend = ...</h3>

This specifies the port and interface (the <i>listen endpoint</i>) that Hitch binds to when listening for connections. It is possible define several frontends, and Hitch will bind to several ports and/or several interfaces. 

 If &quot;*&quot; is used as the host, then Hitch will bind on all interfaces for the given port. 

 A frontend can be specified either in a single line: 

 <pre>frontend = &quot;[HOST]:PORT[+CERT]&quot;</pre>Or in a <i>frontend block</i>: 

 <pre>frontend = {
 host = &quot;HOST&quot;
 port = &quot;PORT&quot;
 &lt;other frontend options&gt;
}</pre>

<h3>group = &lt;string&gt;</h3>

If given, Hitch will change to this group after binding to listen sockets.

<h3>keepalive = &lt;number&gt;</h3>

Number of seconds a TCP socket is kept alive

<h3>ocsp-dir = &lt;string&gt;</h3>

Directory where Hitch will store and read OCSP responses for stapling. Default is &quot;/var/lib/hitch/&quot;. 

 Directory must be readable and writable for the configured Hitch user, or automatic retrieval and updating of OCSP responses will not take place. 

 If you have a manually pre-loaded OCSP staple, an alternative pem-file syntax can be used for stapling: 

 <pre>pem-file = {
 cert = &quot;mycert.pem&quot;
 ocsp-resp-file = &quot;ocsp-resp.der&quot;
}</pre>

<h3>ocsp-connect-tmo = &lt;number&gt;</h3>

OCSP fetch connect timeout. 

 This does normally not need to be changed. 

 Default is 4.0 seconds.

<h3>ocsp-resp-tmo = &lt;number&gt;</h3>

OCSP fetch response timeout. 

 This does normally not need to be changed. 

 Default is 10 seconds.

<h3>ocsp-verify-staple = on|off</h3>

If set, OCSP responses will be verified against the certificate after retrieval. 

 Default is off.

<h3>pem-file = &lt;string&gt;</h3>

Specify a SSL x509 certificate file. Server Name Indication (SNI) is supported by using one certificate file per SNI name. 

 Certificates are used in the order they are listed; the last certificate listed will be used if none of the others match. 

 A file suitable for Hitch is a concatenation of a private key and a corresponding certificate or certificate chain. 

 At least one PEM file is needed for Hitch to start, but it can be supplied on the command line. 

 This option is also available in a frontend declaration, to make a certificate only available for a specific listen endpoint.

<h3>prefer-server-ciphers = on|off</h3>

Turns on or off enforcement of the cipher ordering set in Hitch. 

 This option is also available in frontend blocks. 

 Default is off.

<h3>proxy-proxy = on|off</h3>

Proxy an existing PROXY protocol header through this request. At the moment this is equivalent to write-proxy-v2. 

 This option is mutually exclusive with option write-proxy-v2, write-ip and write-proxy-v1. 

 Default is off.

<h3>quiet = on|off</h3>

If quiet is turned on, only error messages will be shown.

<h3>tls-protos = ...</h3>

The SSL/TLS protocols to be used. This is an unquoted list of tokens. Available tokens are SSLv3, TLSv1.0, TLSv1.1 and TLSv1.2. 

 The default is TLSv1.1 and TLSv1.2. 

 There are two deprecated options, ssl= and tls=, that also select protocols. If &quot;ssl=on&quot; is used, then all protocols are selected. This is known to be insecure, and is strongly discouraged. If &quot;tls=on&quot; is used, the three TLS protocol versions will be used. Turning on SSLv3 and TLSv1.0 is not recommended - support for these protocols are only kept for backwards compatibility. 

 This option is also available in frontend blocks.

<h3>sni-nomatch-abort = on|off</h3>

Abort handshake when the client submits an unrecognized SNI server name. 

 This option is also available in a frontend declaration.

<h3>ssl-engine = &lt;string&gt;</h3>

Set the SSL engine. This is used with SSL accelerator cards. See the OpenSSL documentation for legal values.

<h3>syslog = on|off</h3>

Send messages to syslog. Default is off.

<h3>syslog-facility = &lt;string&gt;</h3>

Set the syslog facility. Default is &quot;daemon&quot;.

<h3>user = &lt;string&gt;</h3>

User to run as. If Hitch is started as root, it will insist on changing to a user with lower rights after binding to sockets.

<h3>workers = &lt;number&gt;</h3>

Number of worker processes. One per CPU core is recommended.

<h3>write-ip = on|off</h3>

Report the client ip to the backend by writing IP before sending data. 

 This option is mutually exclusive with each of the options write-proxy-v2, write-proxy-v1 and proxy-proxy. 

 Default is off.

<h3>write-proxy-v1 = on|off</h3>

Report client address using the PROXY protocol. 

 This option is mutually exclusive with option write-proxy-v2, write-ip and proxy-proxy. 

 Default is off.

<h3>write-proxy-v2 = on|off</h3>

Report client address using PROXY v2 protocol. 

 This option is mutually exclusive with option write-ip, write-proxy-v1 and proxy-proxy. 

 Default is off.

<h2>Example</h2>

The following file shows the syntax needed to get started with: 

 <pre>frontend = {
 host = &quot;*&quot;
 port = &quot;443&quot;
}
backend = &quot;[127.0.0.1]:6086&quot; # 6086 is the default Varnish PROXY port.
workers = 4 # number of CPU cores
daemon = on
user = &quot;nobody&quot;
group = &quot;nogroup&quot;
# Enable to let clients negotiate HTTP/2 with ALPN. (default off)
# alpn-protos = &quot;http/2, http/1.1&quot;
# run Varnish as backend over PROXY; varnishd -a :80 -a localhost:6086,PROXY ..
write-proxy-v2 = on # Write PROXY header</pre>

<h2>Author</h2>

This manual was written by Pål Hermunn Johansen &lt;<i>hermunn [at] varnish-software.com</i>&gt;
