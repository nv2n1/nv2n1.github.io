---
title: "packet-application-gss(3)"
name: "packet-application-gss"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-application-gss/"
description: "packet.application.gss – GSS module"
---

<p>packet.application.gss &#8211; GSS module</p>
<h2>Description</h2>
<p>Decode GSS layers. </p>
<p> NOTE:<br />
&nbsp;<wbr>&nbsp;<wbr>Only procedures RPCSEC_GSS_INIT and RPCSEC_GSS_DATA are supported</p>
<h2>Classes</h2>
<h3>class GSS(baseobj.BaseObj)</h3>
<pre>GSS Data object
This is a base object and should not be instantiated.
It gives the following methods:
 # Decode data preceding the RPC payload when flavor is RPCSEC_GSS
 x.decode_gss_data()
 # Decode data following the RPC payload when flavor is RPCSEC_GSS
 x.decode_gss_checksum()
<code>Methods defined here:</code>
---------------------
<code>decode_gss_checksum(self)</code>
Decode GSS checksum
<code>decode_gss_data(self)</code>
Decode GSS data</pre>
<h3>class GSS_Checksum(baseobj.BaseObj)</h3>
<pre>GSS Checksum object
This object is the representation of the data following the RPC
payload when flavor is RPCSEC_GSS.
<code>Methods defined here:</code>
---------------------
<code>__str__(self)</code>
String representation of object
The representation depends on the verbose level set by debug_repr().
If set to 0 the generic object representation is returned.
If set to 1 the representation of the object is:
 'GSSC token: 0x602306092a864886f71201020201010000...'
If set to 2 the representation of the object is as follows:
 'token: 0x602306092a864886f71201020201010000...'</pre>
<h3>class GSS_Data(baseobj.BaseObj)</h3>
<pre>GSS Data object
This object is the representation of the data preceding the RPC
payload when flavor is RPCSEC_GSS.
<code>Methods defined here:</code>
---------------------
<code>__str__(self)</code>
String representation of object
The representation depends on the verbose level set by debug_repr().
If set to 0 the generic object representation is returned.
If set to 1 the representation of the object is:
 'GSSD length: 176, seq_num: 1'
If set to 2 the representation of the object is as follows:
 'length: 176, seq_num: 1'</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
