---
title: "rndc(5)"
name: "rndc"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rndc/"
description: "rndc.conf – rndc configuration file"
---

<p>rndc.conf &#8211; rndc configuration file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>rndc.conf</code></dl>
<h2>Description</h2>
<p><i>rndc.conf</i></p>
<dd>is the configuration file for <code>rndc</code>, the BIND 9 name server control utility. This file has a similar structure and syntax to <i>named.conf</i>. Statements are enclosed in braces and terminated with a semi-colon. Clauses in the statements are also semi-colon terminated. The usual comment styles are supported: </p>
<p> C style: /* */ </p>
<p> C++ style: // to end of line </p>
<p> Unix style: # to end of line </p>
<p> <i>rndc.conf</i> is much simpler than <i>named.conf</i>. The file uses three statements: an options statement, a server statement and a key statement. </p>
<p> The <code>options</code> statement contains five clauses. The <code>default-server</code> clause is followed by the name or address of a name server. This host will be used when no name server is given as an argument to <code>rndc</code>. The <code>default-key</code> clause is followed by the name of a key which is identified by a <code>key</code> statement. If no <code>keyid</code> is provided on the rndc command line, and no <code>key</code> clause is found in a matching <code>server</code> statement, this default key will be used to authenticate the server&#8217;s commands and responses. The <code>default-port</code> clause is followed by the port to connect to on the remote name server. If no <code>port</code> option is provided on the rndc command line, and no <code>port</code> clause is found in a matching <code>server</code> statement, this default port will be used to connect. The <code>default-source-address</code> and <code>default-source-address-v6</code> clauses which can be used to set the IPv4 and IPv6 source addresses respectively. </p>
<p> After the <code>server</code> keyword, the server statement includes a string which is the hostname or address for a name server. The statement has three possible clauses: <code>key</code>, <code>port</code> and <code>addresses</code>. The key name must match the name of a key statement in the file. The port number specifies the port to connect to. If an <code>addresses</code> clause is supplied these addresses will be used instead of the server name. Each address can take an optional port. If an <code>source-address</code> or <code>source-address-v6</code> of supplied then these will be used to specify the IPv4 and IPv6 source addresses respectively. </p>
<p> The <code>key</code> statement begins with an identifying string, the name of the key. The statement has two clauses. <code>algorithm</code> identifies the encryption algorithm for <code>rndc</code> to use; currently only HMAC-MD5 is supported. This is followed by a secret clause which contains the base-64 encoding of the algorithm&#8217;s encryption key. The base-64 string is enclosed in double quotes. </p>
<p> There are two common ways to generate the base-64 string for the secret. The BIND 9 program <code>rndc-confgen</code> can be used to generate a random key, or the <code>mmencode</code> program, also known as <code>mimencode</code>, can be used to generate a base-64 string from known input. <code>mmencode</code> does not ship with BIND 9 but is available on many systems. See the EXAMPLE section for sample command lines for each.</p>
<h2>Example</h2>
<dl>
<dd>
<pre> options {
 default-server localhost;
 default-key samplekey;
 };</pre>
</dl>
<dl>
<dd>
<pre> server localhost {
 key samplekey;
 };</pre>
</dl>
<dl>
<dd>
<pre> server testserver {
 key testkey;
 addresses { localhost port 5353; };
 };</pre>
</dl>
<dl>
<dd>
<pre> key samplekey {
 algorithm hmac-md5;
 secret &quot;6FMfj43Osz4lyb24OIe2iGEz9lf1llJO+lz&quot;;
 };</pre>
</dl>
<dl>
<dd>
<pre> key testkey {
 algorithm hmac-md5;
 secret &quot;R3HI8P6BKw9ZwXwN3VZKuQ==&quot;;
 };</pre>
</dl>
<p> In the above example, <code>rndc</code> will by default use the server at localhost (127.0.0.1) and the key called samplekey. Commands to the localhost server will use the samplekey key, which must also be defined in the server&#8217;s configuration file with the same name and secret. The key statement indicates that samplekey uses the HMAC-MD5 algorithm and its secret clause contains the base-64 encoding of the HMAC-MD5 secret enclosed in double quotes. </p>
<p> If <code>rndc -s testserver</code> is used then <code>rndc</code> will connect to server on localhost port 5353 using the key testkey. </p>
<p> To generate a random secret with <code>rndc-confgen</code>: </p>
<p> <code>rndc-confgen</code> </p>
<p> A complete <i>rndc.conf</i> file, including the randomly generated key, will be written to the standard output. Commented-out <code>key</code> and <code>controls</code> statements for <i>named.conf</i> are also printed. </p>
<p> To generate a base-64 secret with <code>mmencode</code>: </p>
<p> <code>echo &quot;known plaintext for a secret&quot; | mmencode</code></p>
<h2>Name Server Configuration</h2>
<p>The name server must be configured to accept rndc connections and to recognize the key specified in the <i>rndc.conf</i> file, using the controls statement in <i>named.conf</i>. See the sections on the <code>controls</code> statement in the BIND 9 Administrator Reference Manual for details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rndc/">rndc</a></code>(8), <code><a href="/docs/linux/man/8-rndc-confgen/">rndc-confgen</a></code>(8), <code><a href="/docs/linux/man/1-mmencode/">mmencode</a></code>(1), BIND 9 Administrator Reference Manual.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium.</p>
