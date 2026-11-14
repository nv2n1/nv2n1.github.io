---
title: "mosquitto-tls(7)"
name: "mosquitto-tls"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mosquitto-tls/"
description: "mosquitto-tls – Configure SSL/TLS support for Mosquitto"
---

<p>mosquitto-tls &#8211; Configure SSL/TLS support for Mosquitto</p>
<h2>Description</h2>
<p><code>mosquitto</code> provides SSL support for encrypted network connections and authentication. This manual describes how to create the files needed.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 It is important to use different certificate subject parameters for your CA, server and clients. If the certificates appear identical, even though generated separately, the broker/client will not be able to distinguish between them and you will experience difficult to diagnose errors. </p>
<h2>Certificate Authority</h2>
<p>Generate a certificate authority certificate and key. </p>
<dl>
<dd>&bull; openssl req -new -x509 -days &lt;duration&gt; -extensions v3_ca -keyout ca.key -out ca.crt</dl>
<h2>Server</h2>
<p>Generate a server key. </p>
<dl>
<dd>&bull; openssl genrsa -des3 -out server.key 2048</dl>
<p> Generate a server key without encryption. </p>
<dl>
<dd>&bull; openssl genrsa -out server.key 2048</dl>
<p> Generate a certificate signing request to send to the CA. </p>
<dl>
<dd>&bull; openssl req -out server.csr -key server.key -new</dl>
<p> Send the CSR to the CA, or sign it with your CA key: </p>
<dl>
<dd>&bull; openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days &lt;duration&gt;</dl>
<h2>Client</h2>
<p>Generate a client key. </p>
<dl>
<dd>&bull; openssl genrsa -des3 -out client.key 2048</dl>
<p> Generate a certificate signing request to send to the CA. </p>
<dl>
<dd>&bull; openssl req -out client.csr -key client.key -new</dl>
<p> Send the CSR to the CA, or sign it with your CA key: </p>
<dl>
<dd>&bull; openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days &lt;duration&gt;</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mosquitto/">mosquitto</a></code>(8), <code><a href="/docs/linux/man/5-mosquitto-conf/">mosquitto-conf</a></code>(5)</p>
<h2>Author</h2>
<p>Roger Light &lt;roger [at] atchoo.org&gt;</p>
