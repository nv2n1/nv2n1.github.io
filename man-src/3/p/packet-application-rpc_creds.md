---
title: "packet-application-rpc_creds(3)"
name: "packet-application-rpc_creds"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-application-rpc_creds/"
description: "packet.application.rpc_creds – RPC Credentials module"
---

<p>packet.application.rpc_creds &#8211; RPC Credentials module</p>
<h2>Description</h2>
<p>Decode RPC Credentials.</p>
<h2>Classes</h2>
<h3>class AuthNone(baseobj.BaseObj)</h3>
<pre>AuthNone object
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code>
 Constructor which takes the Unpack object as input
Data and other attributes defined here:
flavor = 0</pre>
<h3>class AuthSys(baseobj.BaseObj)</h3>
<pre>AuthSys object
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code>
 Constructor which takes the Unpack object as input
Data and other attributes defined here:
flavor = 1</pre>
<h3>class GSS_Credential(baseobj.BaseObj)</h3>
<pre>GSS_Credential object
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code>
 Constructor which takes the Unpack object as input
Data and other attributes defined here:
flavor = 6</pre>
<h3>class GSS_Verifier(baseobj.BaseObj)</h3>
<pre>GSS_Verifier object
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code>
 Constructor which takes the Unpack object as input
Data and other attributes defined here:
flavor = 6</pre>
<h2>Functions</h2>
<h3>rpc_credential(unpack, verifier=False)</h3>
<p>Process and return the credential or verifier</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
