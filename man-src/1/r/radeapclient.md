---
title: "radeapclient(1)"
name: "radeapclient"
section: "1"
letter: "r"
url: "/docs/linux/man/1-radeapclient/"
description: "radeapclient – send EAP packets to a RADIUS server, calculate responses"
---

<h2>NAME</h2>
<p> radeapclient &#8211; send EAP packets to a RADIUS server, calculate responses</p>
<h2>SYNOPSIS</h2>
<p> <code>radeapclient</code> [<code>-4</code>] [<code>-6</code>] [<code>-c</code> <i>count</i>] [<code>-d</code> <i>raddb_directory</i>] [<code>-f</code> <i>file</i>] [<code>-h</code>] [<code>-i</code> <i>source_ip</i>] [<code>-q</code>] [<code>-s</code>] [<code>-r</code> <i>retries</i>] [<code>-S</code> <i>file</i>] [<code>-t</code> <i>timeout</i>] [<code>-v</code>] [<code>-x</code>] <i>server {acct|auth} secret</i></p>
<h2>DESCRIPTION</h2>
<p> <code>radeapclient</code> is a radius client program. It can send arbitrary radius packets to a radius server, then shows the reply. Radeapclient differs from radclient in that if there is an EAP-MD5 challenge, then it will be responded to. </p>
<p> <code>radeapclient</code> is otherwise identical to <code>radclient</code>. </p>
<p> The <i>EAP-Identity</i> attribute, if present is used to construct an EAP Identity message. </p>
<p> The <i>EAP-MD5-Password</i> attribute, if present is used to respond to an MD5 challenge. </p>
<p> No other EAP types are currently supported. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-4</p>
<dd> Use IPv4 (default)</p>
<dt>-6</p>
<dd> Use IPv6</p>
<dt>-c&nbsp;<wbr><i>count</i></p>
<dd> Send each packet <i>count</i> times.</p>
<dt>-d&nbsp;<wbr><i>raddb</i></p>
<dd> Set dictionary directory.</p>
<dt>-f&nbsp;<wbr><i>file</i></p>
<dd> Read packets from <i>file</i>, not stdin.</p>
<dt>-r&nbsp;<wbr><i>retries</i></p>
<dd> If timeout, retry sending the packet <i>retries</i> times.</p>
<dt>-t&nbsp;<wbr><i>timeout</i></p>
<dd> Wait <i>timeout</i> seconds before retrying (may be a floating point number).</p>
<dt>-h</p>
<dd> Print usage help information.</p>
<dt>-i&nbsp;<wbr><i>id</i></p>
<dd> Set request id to &#8216;<i>id</i>&#8216;. Values may be 0..255</p>
<dt>-S&nbsp;<wbr><i>file</i></p>
<dd> Read secret from <i>file</i>, not command line.</p>
<dt>-q</p>
<dd> Quiet, do not print anything out.</p>
<dt>-s</p>
<dd> Print out summary information of auth results.</p>
<dt>-v</p>
<dd> Show program version information.</p>
<dt>-x</p>
<dd> Enable debugging mode. </p>
</dl>
<h2>EXAMPLE</h2>
<p> A sample session that queries the remote server with an EAP-MD5 challenge.</p>
<dl>
<dt>
<dd>
<pre><code>
(echo 'User-Name = "bob"';
 echo 'EAP-MD5-Password = "hello"';
 echo 'NAS-IP-Address = marajade.sandelman.ottawa.on.c';
 echo 'EAP-Code = Response';
 echo 'EAP-Id = 210';
 echo 'EAP-Type-Identity = "bob"; echo 'Message-Authenticator = 0x00';
 echo 'NAS-Port = 0') &gt; req.txt
                            radeapclient
                            - x localhost auth testing123 &lt;
    req.txt
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-radclient/">radclient</a>(1)</p>
<h2>AUTHOR</h2>
<p> Michael Richardson, &lt;mcr [at] sandelman.ottawa.on.ca&gt; </p>
<h2>Index</h2>
