---
title: "rlm_digest(5)"
name: "rlm_digest"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_digest/"
description: "rlm_digest – FreeRADIUS Module"
---

<p>rlm_digest &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_digest</i> module authenticates RADIUS Access-Request packets that contain Cisco SIP digest authentication attributes. The module should be listed in the <i>authorize</i> and <i>authenticate</i> sections of <i>radiusd.conf</i>.</p>
<h2>Configuration</h2>
<p>The digest module requires no additional configuration items. When it is being used to authenticate requests, however, it does require access to the clear-text password for the user. Hashed passwords are not acceptable, and will not work.</p>
<h2>Examples</h2>
<p>Add the following lines to the top of your &#8216;raddb/users&#8217; file:</p>
<dl>
<dd>
<pre>#---
<br>
test Auth-Type := Digest, User-Password = &quot;test&quot;
<br>
 Reply-Message = &quot;Hello, test with digest&quot;
<br>
#---</pre>
</dl>
<p> Once the server has been started (debugging mode is recommended), use &#8216;<i>radclient</i> to send the following packet to the server:</p>
<dl>
<dd>
<pre>$ radclient -f digest localhost auth testing123</pre>
</dl>
<p> Where &#8216;digest&#8217; is a file containing: </p>
<pre><code>User-Name = &quot;test&quot;,

Digest-Response = &quot;631d6d73147add2f9e437f59bbc3aeb7&quot;,

Digest-Realm = &quot;testrealm&quot;,

Digest-Nonce = &quot;1234abcd&quot;,

Digest-Method = &quot;INVITE&quot;,

Digest-URI = &quot;sip:5555551212 [at] example.com&quot;,

Digest-Algorithm = &quot;MD5&quot;,

Digest-User-Name = &quot;test&quot;,

Message-Authenticator = &quot;&quot;
</code></pre>
<p> You should see the authentication succeed. </p>
<h2>Sections</h2>
<p><code>authorize,</code> <code>authenticate</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf,</i> <i>draft-sterman-aaa-sip-00.txt</i></p>
<h2>Author</h2>
<p>Alan DeKok &lt;aland [at] ox.org&gt;</p>
