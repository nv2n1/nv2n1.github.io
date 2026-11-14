---
title: "zmq_curve(7)"
name: "zmq_curve"
section: "7"
letter: "z"
url: "/docs/linux/man/7-zmq_curve/"
description: "zmq_curve – secure authentication and confidentiality"
---

<p>zmq_curve &#8211; secure authentication and confidentiality</p>
<h2>Synopsis</h2>
<p>The CURVE mechanism defines a mechanism for secure authentication and confidentiality for communications between a client and a server. CURVE is intended for use on public networks. The CURVE mechanism is defined by this document: m[blue]<code><a rel="nofollow" href="http://rfc.zeromq.org/spec:25">http://rfc.zeromq.org/spec:25</a></code>m[].</p>
<h2>Client And Server Roles</h2>
<p>A socket using CURVE can be either client or server, at any moment, but not both. The role is independent of bind/connect direction. </p>
<p> A socket can change roles at any point by setting new options. The role affects all zmq_connect and zmq_bind calls that follow it. </p>
<p> To become a CURVE server, the application sets the ZMQ_CURVE_SERVER option on the socket, and then sets the ZMQ_CURVE_SECRETKEY option to provide the socket with its long-term secret key. The application does not provide the socket with its long-term public key, which is used only by clients. </p>
<p> To become a CURVE client, the application sets the ZMQ_CURVE_SERVERKEY option with the long-term public key of the server it intends to connect to, or accept connections from, next. The application then sets the ZMQ_CURVE_PUBLICKEY and ZMQ_CURVE_SECRETKEY options with its client long-term key pair. </p>
<p> If the server does authentication it will be based on the client&#8217;s long term public key.</p>
<h2>Key Encoding</h2>
<p>The standard representation for keys in source code is either 32 bytes of base 256 (binary) data, or 40 characters of base 85 data encoded using the Z85 algorithm defined by m[blue]<code><a rel="nofollow" href="http://rfc.zeromq.org/spec:32">http://rfc.zeromq.org/spec:32</a></code>m[]. </p>
<p> The Z85 algorithm is designed to produce printable key strings for use in configuration files, the command line, and code. There is a reference implementation in C at m[blue]<code><a rel="nofollow" href="https://github.com/zeromq/rfc/tree/master/src">https://github.com/zeromq/rfc/tree/master/src</a></code>m[].</p>
<h2>Test Key Values</h2>
<p>For test cases, the client shall use this long-term key pair (specified as hexadecimal and in Z85): </p>
<dl>
<dd>
<pre>public:
 BB88471D65E2659B30C55A5321CEBB5AAB2B70A398645C26DCA2B2FCB43FC518
 Yne@$w-vo&lt;fVvi]a&lt;NY6T1ed:M$fCG*[IaLV{hID
secret:
 7BB864B489AFA3671FBE69101F94B38972F24816DFB01B51656B3FEC8DFD0888
 D:)Q[IlAW!ahhC2ac:9*A}h:p?([4%wOTJ%JR%cs</pre>
</dl>
<p> And the server shall use this long-term key pair (specified as hexadecimal and in Z85): </p>
<dl>
<dd>
<pre>public:
 54FCBA24E93249969316FB617C872BB0C1D1FF14800427C594CBFACF1BC2D652
 rq:rM&gt;}U?@Lns47E1%kR.o@n%FcmmsL/@{H8]yf7
secret:
 8E0BDD697628B91D8F245587EE95C5B04D48963F79259877B49CD9063AEAD3B7
 JTKVSB%%)wK0E.X)V&gt;+}o?pNmC{O&amp;4W4b!Ni{Lh6</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_z85_encode/">zmq_z85_encode</a></code>(3) <code><a href="/docs/linux/man/3-zmq_z85_decode/">zmq_z85_decode</a></code>(3) <code><a href="/docs/linux/man/3-zmq_setsockopt/">zmq_setsockopt</a></code>(3) <code><a href="/docs/linux/man/7-zmq_null/">zmq_null</a></code>(7) <code><a href="/docs/linux/man/7-zmq_plain/">zmq_plain</a></code>(7) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7)</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
