---
title: "tcpcryptd(8)"
name: "tcpcryptd"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcpcryptd/"
---

tcpcryptd - Implement the tcpcrypt protocol by transparently modifying network I/O

<h2>Synopsis</h2>

tcpcryptd [options]

<h2>Options</h2>

A list of all options is produced by:
<dl><dd>tcpcryptd -h</dl>
 

 Configuration of packet-diversion rules allows the system administrator to control which TCP connections are protected by tcpcryptd. The daemon receives packets for transformation via a &quot;divert port&quot;, configurable with -p port. 

 The daemon communicates with user programs via a &quot;control socket&quot;, configurable with -u socket_address. If socket_address begins with &quot;/&quot;, it is interpreted as a filesystem path pointing to a unix-domain socket; if it is of the form &quot;:port&quot;, it is interpreted as the internet address localhost:port. 

 Verbosity may be increased with multiple -v options. 

 A &quot;phone-home&quot; test will be performed at daemon startup to confirm end-to-end functionality of the implementation (by default, with the authors' server), but may be redirected to another test-server with -s hostname or disabled completely with -f.

<h2>Description</h2>

The tcpcryptd daemon transforms TCP segments via a kernel &quot;divert&quot; port in order to implement &quot;opportunistic encryption&quot; according to the tcpcrypt protocol. 

 For a peer that signals in the connection handshake that it has support for the tcpcrypt protocol, ephemeral keys are exchanged and used to protect the confidentiality and integrity of the connection's application data. (The protocol protects the integrity of parts of the TCP header as well.) When a peer does not indicate support for the protocol, the daemon will pass the remainder of the connection unperturbed (and thus unprotected). 

 Application software need not be modified to take advantage of this facility, which provides confidentiality in the face of passive network attackers (those who cannot modify network data in transit). But in order to protect communication from active attackers, the application must intentionally authenticate the connection as described below.

<h3>Authentication</h3>

The tcpcrypt protocol does not itself protect communications against &quot;active attackers&quot;, that is, those who are able to modify network packets in transit. Such an attacker may perform a &quot;man in the middle&quot; attack that allows her to behave as the endpoint of the encrypted connection and thus compromise its security. 

 However, applications aware of tcpcrypt may authenticate the connection in whatever manner they choose, aided by an identifier for the connection that is derived from the protocol and made available by tcpcryptd: 

 A session id is derived from the ephemeral keys used to encrypt each connection protected by tcpcrypt. This identifier is (probabalistically) unique over all connections, is not secret, and may be extracted by applications via the user library libtcpcrypt. Session ids for all active connections may also be listed with the netstat-like utility <a HREF="/docs/linux/man/8-tcnetstat/">tcnetstat</a>(8). 

 Connection peers may ensure they are communicating securely with each other (enjoying confidentiality and integrity in the face of active network attackers) by confirming that the tcpcrypt session ids derived at each end are identical. For example, they may bind the session id together with a shared secret such as a password, sign it with public keys, use a voice connection to speak a fingerprint of it, or simply record it for later confirmation.

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-tcnetstat/">tcnetstat</a>(8), &lt;<a rel="nofollow" HREF="http://tcpcrypt.org/">http://tcpcrypt.org/</a>&gt; 
