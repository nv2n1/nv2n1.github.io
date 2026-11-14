---
title: "ssltap(1)"
name: "ssltap"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssltap/"
description: "ssltap – Tap into SSL connections and display the data going by"
---

<h2 class="name">NAME</h2>
<p> ssltap &#8211; Tap into SSL connections and display the data going by </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ssltap</code> [-fhlsvx] [-p port] [hostname:port]</dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></p>
<h2>DESCRIPTION</h2>
<p> The SSL Debugging Tool <code>ssltap</code> is an SSL-aware command-line proxy. It watches TCP connections and displays the data going by. If a connection is SSL, the data display includes interpreted SSL records and handshaking</p>
<h2>OPTIONS</h2>
<p> -f</p>
<dl>
<dt>
<dd> Turn on fancy printing. Output is printed in colored HTML. Data sent from the client to the server is in blue; the server&#8217;s reply is in red. When used with looping mode, the different connections are separated with horizontal lines. You can use this option to upload the output into a browser.</dl>
<p> -h</p>
<dl>
<dt>
<dd> Turn on hex/ASCII printing. Instead of outputting raw data, the command interprets each record as a numbered line of hex values, followed by the same data as ASCII characters. The two parts are separated by a vertical bar. Nonprinting characters are replaced by dots.</dl>
<p> -l prefix</p>
<dl>
<dt>
<dd> Turn on looping; that is, continue to accept connections rather than stopping after the first connection is complete.</dl>
<p> -p port</p>
<dl>
<dt>
<dd> Change the default rendezvous port (1924) to another port. </p>
<p> The following are well-known port numbers: </p>
<p> * HTTP 80 </p>
<p> * HTTPS 443 </p>
<p> * SMTP 25 </p>
<p> * FTP 21 </p>
<p> * IMAP 143 </p>
<p> * IMAPS 993 (IMAP over SSL) </p>
<p> * NNTP 119 </p>
<p> * NNTPS 563 (NNTP over SSL)</dl>
<p> -s</p>
<dl>
<dt>
<dd> Turn on SSL parsing and decoding. The tool does not automatically detect SSL sessions. If you are intercepting an SSL connection, use this option so that the tool can detect and decode SSL structures. </p>
<p> If the tool detects a certificate chain, it saves the DER-encoded certificates into files in the current directory. The files are named cert.0x, where x is the sequence number of the certificate. </p>
<p> If the -s option is used with -h, two separate parts are printed for each record: the plain hex/ASCII output, and the parsed SSL output.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Print a version string for the tool.</dl>
<p> -x</p>
<dl>
<dt>
<dd> Turn on extra SSL hex dumps.</dl>
<h2>USAGE AND EXAMPLES</h2>
<p> You can use the SSL Debugging Tool to intercept any connection information. Although you can run the tool at its most basic by issuing the ssltap command with no options other than hostname:port, the information you get in this way is not very useful. For example, assume your development machine is called intercept. The simplest way to use the debugging tool is to execute the following command from a command shell: </p>
<dl>
<dt>
<dd>
<pre>
$ ssltap <a rel="nofollow" href="http://www.netscape.com">www.netscape.com</a>
</pre>
</dl>
<p> The program waits for an incoming connection on the default port 1924. In your browser window, enter the URL <a rel="nofollow" href="http://intercept:1924.">http://intercept:1924.</a> The browser retrieves the requested page from the server at <a href="http://www.netscape.com">www.netscape.com</a>, but the page is intercepted and passed on to the browser by the debugging tool on intercept. On its way to the browser, the data is printed to the command shell from which you issued the command. Data sent from the client to the server is surrounded by the following symbols: &#8211;&gt; [ data ] Data sent from the server to the client is surrounded by the following symbols: &quot;left arrow&quot;&#8211; [ data ] The raw data stream is sent to standard output and is not interpreted in any way. This can result in peculiar effects, such as sounds, flashes, and even crashes of the command shell window. To output a basic, printable interpretation of the data, use the -h option, or, if you are looking at an SSL connection, the -s option. You will notice that the page you retrieved looks incomplete in the browser. This is because, by default, the tool closes down after the first connection is complete, so the browser is not able to load images. To make the tool continue to accept connections, switch on looping mode with the -l option. The following examples show the output from commonly used combinations of options. </p>
<p> Example 1 </p>
<dl>
<dt>
<dd>
<pre>
$ ssltap.exe -sx -p 444 interzone.mcom.com:443 &gt; sx.txt
</pre>
</dl>
<p> Output </p>
<dl>
<dt>
<dd>
<pre><code>
Connected to interzone.mcom.com : 443 -- &gt; ; [
alloclen = 66 bytes
   [ssl2]  ClientHelloV2 {
            version = {0x03, 0x00}
            cipher-specs-length = 39 (0x27)
            sid-length = 0 (0x00)
            challenge-length = 16 (0x10)
            cipher-suites = {
                (0x010080) SSL2/RSA/RC4-128/MD5
                  (0x020080) SSL2/RSA/RC4-40/MD5
                  (0x030080) SSL2/RSA/RC2CBC128/MD5
                  (0x040080) SSL2/RSA/RC2CBC40/MD5
                  (0x060040) SSL2/RSA/DES64CBC/MD5
                  (0x0700c0) SSL2/RSA/3DES192EDE-CBC/MD5
                  (0x000004) SSL3/RSA/RC4-128/MD5
                  (0x00ffe0) SSL3/RSA-FIPS/3DES192EDE-CBC/SHA
                  (0x00000a) SSL3/RSA/3DES192EDE-CBC/SHA
                  (0x00ffe1) SSL3/RSA-FIPS/DES64CBC/SHA
                  (0x000009) SSL3/RSA/DES64CBC/SHA
                  (0x000003) SSL3/RSA/RC4-40/MD5
                  (0x000006) SSL3/RSA/RC2CBC40/MD5
                  }
            session-id = { }
            challenge = { 0xec5d 0x8edb 0x37c9 0xb5c9 0x7b70 0x8fe9 0xd1d3
0x2592 }
}
]
&lt;-- [
SSLRecord {
   0: 16 03 00 03  e5                                   |.....
   type    = 22 (handshake)
   version = { 3,0 }
   length  = 997 (0x3e5)
   handshake {
   0: 02 00 00 46                                      |...F
      type = 2 (server_hello)
      length = 70 (0x000046)
            ServerHello {
            server_version = {3, 0}
            random = {...}
   0: 77 8c 6e 26  6c 0c ec c0  d9 58 4f 47  d3 2d 01 45  |
wn&amp;l.&amp;igrave;..XOG.-.E
   10: 5c 17 75 43  a7 4c 88 c7  88 64 3c 50  41 48 4f 7f  |
\.uC&amp;#167;L.&amp;Ccedil;.d&lt;PAHO.
                  session ID = {
                  length = 32
                contents = {..}
   0: 14 11 07 a8  2a 31 91 29  11 94 40 37  57 10 a7 32  | ...ad*1.)..@7W.&amp;#167;
                  2 10 : 56 6f 52 62 fe 3d b3 65 b1 e4 13 0f 52 a3 c8 f6 | VoRb &amp;thorn;
                  = &amp;sup3;
                  e &amp;plusmn;
                  ... R &amp;pound;
                  &amp;Egrave;
                  .
         }
               cipher_suite = (0x0003) SSL3/RSA/RC4-40/MD5
}
0 : 0b 00 02 c5 | ... &amp;Aring;
type = 11(certificate)
    length = 709(0x0002c5)
        CertificateChain
{
    chainlength = 706(0x02c2)
        Certificate
    {
        size = 703(0x02bf)
            data = { saved in file 'cert.001' }
    }
}
0 : 0c 00 00 ca | ....type = 12(server_key_exchange)
    length = 202(0x0000ca)0 : 0e 00 00 00 | ....type = 14(server_hello_done)
                 length = 0(0x000000)
}
}
]
--&gt; [
SSLRecord {
   0: 16 03 00 00  44                                   |....D
   type    = 22 (handshake)
   version = { 3,0 }
   length  = 68 (0x44)
   handshake {
   0: 10 00 00 40                                      |...@
   type = 16 (client_key_exchange)
   length = 64 (0x000040)
         ClientKeyExchange {
            message = {...}
         }
   }
}
]
--&gt; [
SSLRecord {
   0: 14 03 00 00  01                                   |.....
   type    = 20 (change_cipher_spec)
   version = { 3,0 }
   length  = 1 (0x1)
   0: 01                                               |.
}
SSLRecord {
   0: 16 03 00 00  38                                   |....8
   type    = 22 (handshake)
   version = { 3,0 }
   length  = 56 (0x38)
               &lt; encrypted &gt;
}
]
&lt;-- [
SSLRecord {
   0: 14 03 00 00  01                                   |.....
   type    = 20 (change_cipher_spec)
   version = { 3,0 }
   length  = 1 (0x1)
   0: 01                                               |.
}
]
&lt;-- [
SSLRecord {
   0: 16 03 00 00  38                                   |....8
   type    = 22 (handshake)
   version = { 3,0 }
   length  = 56 (0x38)
                  &lt; encrypted &gt;
}
]
--&gt; [
SSLRecord {
   0: 17 03 00 01  1f                                   |.....
   type    = 23 (application_data)
   version = { 3,0 }
   length  = 287 (0x11f)
               &lt; encrypted &gt;
}
]
&lt;-- [
SSLRecord {
   0: 17 03 00 00  a0                                   |....
   type    = 23 (application_data)
   version = { 3,0 }
   length  = 160 (0xa0)
               &lt; encrypted &gt;
}
]
&lt;-- [
SSLRecord {
    0 : 17 03 00 00 df | ....&amp;szlig;
    type = 23(application_data)
        version = {3, 0} length = 223(0xdf)&lt;encrypted&gt;
}
SSLRecord {
   0: 15 03 00 00  12                                   |.....
   type    = 21 (alert)
   version = { 3,0 }
   length  = 18 (0x12)
               &lt; encrypted &gt;
}
]
Server socket closed.
</code></pre>
</dl>
<p> Example 2 </p>
<p> The -s option turns on SSL parsing. Because the -x option is not used in this example, undecoded values are output as raw data. The output is routed to a text file. </p>
<dl>
<dt>
<dd>
<pre>
$ ssltap -s  -p 444 interzone.mcom.com:443 &gt; s.txt
</pre>
</dl>
<p> Output </p>
<dl>
<dt>
<dd>
Connected to interzone.mcom.com:443<br />
&#8211;&gt; [<br />
alloclen = 63 bytes<br />
   [ssl2]  ClientHelloV2 {<br />
            version = {0x03, 0x00}<br />
            cipher-specs-length = 36 (0x24)<br />
            sid-length = 0 (0x00)<br />
            challenge-length = 16 (0x10)<br />
            cipher-suites = {<br />
                  (0x010080) SSL2/RSA/RC4-128/MD5<br />
                  (0x020080) SSL2/RSA/RC4-40/MD5<br />
                  (0x030080) SSL2/RSA/RC2CBC128/MD5<br />
                  (0x060040) SSL2/RSA/DES64CBC/MD5<br />
                  (0x0700c0) SSL2/RSA/3DES192EDE-CBC/MD5<br />
                  (0x000004) SSL3/RSA/RC4-128/MD5<br />
                  (0x00ffe0) SSL3/RSA-FIPS/3DES192EDE-CBC/SHA<br />
                  (0x00000a) SSL3/RSA/3DES192EDE-CBC/SHA<br />
                  (0x00ffe1) SSL3/RSA-FIPS/DES64CBC/SHA<br />
                  (0x000009) SSL3/RSA/DES64CBC/SHA<br />
                  (0x000003) SSL3/RSA/RC4-40/MD5<br />
                  }<br />
               session-id = { }<br />
            challenge = { 0x713c 0x9338 0x30e1 0xf8d6 0xb934 0x7351 0x200c<br />
0x3fd0 }<br />
]<br />
&gt;&#8211; [<br />
SSLRecord {<br />
   type    = 22 (handshake)<br />
   version = { 3,0 }<br />
   length  = 997 (0x3e5)<br />
   handshake {<br />
         type = 2 (server_hello)<br />
         length = 70 (0x000046)<br />
            ServerHello {<br />
            server_version = {3, 0}<br />
            random = {&#8230;}<br />
            session ID = {<br />
               length = 32<br />
               contents = {..}<br />
               }<br />
               cipher_suite = (0x0003) SSL3/RSA/RC4-40/MD5<br />
            }<br />
         type = 11 (certificate)<br />
         length = 709 (0x0002c5)<br />
            CertificateChain {<br />
               chainlength = 706 (0x02c2)<br />
               Certificate {<br />
                  size = 703 (0x02bf)<br />
                  data = { saved in file &#8216;cert.001&#8217; }<br />
               }<br />
            }<br />
         type = 12 (server_key_exchange)<br />
         length = 202 (0x0000ca)<br />
         type = 14 (server_hello_done)<br />
         length = 0 (0x000000)<br />
   }<br />
}<br />
]<br />
&#8211;&gt; [<br />
SSLRecord {<br />
   type    = 22 (handshake)<br />
   version = { 3,0 }<br />
   length  = 68 (0x44)<br />
   handshake {<br />
         type = 16 (client_key_exchange)<br />
         length = 64 (0x000040)<br />
            ClientKeyExchange {<br />
               message = {&#8230;}<br />
            }<br />
   }<br />
}<br />
]<br />
&#8211;&gt; [<br />
SSLRecord {<br />
   type    = 20 (change_cipher_spec)<br />
   version = { 3,0 }<br />
   length  = 1 (0x1)<br />
}<br />
SSLRecord {<br />
   type    = 22 (handshake)<br />
   version = { 3,0 }<br />
   length  = 56 (0x38)<br />
               &gt; encrypted &gt;<br />
}<br />
]<br />
&gt;&#8211; [<br />
SSLRecord {<br />
   type    = 20 (change_cipher_spec)<br />
   version = { 3,0 }<br />
   length  = 1 (0x1)<br />
}<br />
]<br />
&gt;&#8211; [<br />
SSLRecord {<br />
   type    = 22 (handshake)<br />
   version = { 3,0 }<br />
   length  = 56 (0x38)<br />
               &gt; encrypted &gt;<br />
}<br />
]<br />
&#8211;&gt; [<br />
SSLRecord {<br />
   type    = 23 (application_data)<br />
   version = { 3,0 }<br />
   length  = 287 (0x11f)<br />
               &gt; encrypted &gt;<br />
}<br />
]<br />
[<br />
SSLRecord {<br />
   type    = 23 (application_data)<br />
   version = { 3,0 }<br />
   length  = 160 (0xa0)<br />
               &gt; encrypted &gt;<br />
}<br />
]<br />
&gt;&#8211; [<br />
SSLRecord {<br />
   type    = 23 (application_data)<br />
   version = { 3,0 }<br />
   length  = 223 (0xdf)<br />
               &gt; encrypted &gt;<br />
}<br />
SSLRecord {<br />
   type    = 21 (alert)<br />
   version = { 3,0 }<br />
   length  = 18 (0x12)<br />
               &gt; encrypted &gt;<br />
}<br />
]<br />
Server socket closed.
</dl>
<p> Example 3 </p>
<p> In this example, the -h option turns hex/ASCII format. There is no SSL parsing or decoding. The output is routed to a text file. </p>
<dl>
<dt>
<dd>
<pre>
$ ssltap -h  -p 444 interzone.mcom.com:443 &gt; h.txt
</pre>
</dl>
<p> Output </p>
<dl>
<dt>
<dd>
Connected to interzone.mcom.com:443<br />
&#8211;&gt; [<br />
   0: 80 40 01 03  00 00 27 00  00 00 10 01  00 80 02 00  | .@&#8230;.&#8217;&#8230;&#8230;&#8230;<br />
   10: 80 03 00 80  04 00 80 06  00 40 07 00  c0 00 00 04  | &#8230;&#8230;&#8230; [at] &#8230;&#8230;<br />
   20: 00 ff e0 00  00 0a 00 ff  e1 00 00 09  00 00 03 00  | &#8230;&#8230;..&amp;aacute;&#8230;&#8230;.<br />
   30: 00 06 9b fe  5b 56 96 49  1f 9f ca dd  d5 ba b9 52  | ..&amp;thorn;[V.I.� &#8230;Om&amp;sup1;R<br />
   40: 6f 2d                                            |o-<br />
]<br />
&lt;&#8211; [<br />
   0: 16 03 00 03  e5 02 00 00  46 03 00 7f  e5 0d 1b 1d  | &#8230;&#8230;..F&#8230;&#8230;.<br />
   10: 68 7f 3a 79  60 d5 17 3c  1d 9c 96 b3  88 d2 69 3b  | h.:y`..&lt;..&amp;sup3;.&amp;Ograve;i;<br />
   20: 78 e2 4b 8b  a6 52 12 4b  46 e8 c2 20  14 11 89 05  | x.K.|R.KF&amp;egrave;. &#8230;<br />
   30: 4d 52 91 fd  93 e0 51 48  91 90 08 96  c1 b6 76 77  | MR.&amp;yacute;..QH&#8230;..&amp;para;vw<br />
   40: 2a f4 00 08  a1 06 61 a2  64 1f 2e 9b  00 03 00 0b  | *&amp;ocirc;..&amp;iexcl;.a&amp;#162;d&#8230;&#8230;<br />
   50: 00 02 c5 00  02 c2 00 02  bf 30 82 02  bb 30 82 02  | ..&amp;Aring;&#8230;&#8230;0&#8230;0..<br />
   60: 24 a0 03 02  01 02 02 02  01 36 30 0d  06 09 2a 86  | $ &#8230;&#8230;.60&#8230;*.<br />
   70: 48 86 f7 0d  01 01 04 05  00 30 77 31  0b 30 09 06  | H.&amp;#247;&#8230;&#8230;0w1.0..<br />
   80: 03 55 04 06  13 02 55 53  31 2c 30 2a  06 03 55 04  | .U&#8230;.US1,0*..U.<br />
   90: 0a 13 23 4e  65 74 73 63  61 70 65 20  43 6f 6d 6d  | ..#Netscape Comm<br />
   a0: 75 6e 69 63  61 74 69 6f  6e 73 20 43  6f 72 70 6f  | unications Corpo<br />
   b0: 72 61 74 69  6f 6e 31 11  30 0f 06 03  55 04 0b 13  | ration1.0&#8230;U&#8230;<br />
   c0: 08 48 61 72  64 63 6f 72  65 31 27 30  25 06 03 55  | .Hardcore1&#8217;0%..U<br />
   d0: 04 03 13 1e  48 61 72 64  63 6f 72 65  20 43 65 72  | &#8230;.Hardcore Cer<br />
   e0: 74 69 66 69  63 61 74 65  20 53 65 72  76 65 72 20  | tificate Server<br />
   f0: 49 49 30 1e  17 0d 39 38  30 35 31 36  30 31 30 33  | II0&#8230;9805160103<br />
&lt;additional data lines&gt;<br />
]<br />
&lt;additional records in same format&gt;<br />
Server socket closed.
</dl>
<p> Example 4 </p>
<p> In this example, the -s option turns on SSL parsing, and the -h option turns on hex/ASCII format. Both formats are shown for each record. The output is routed to a text file. </p>
<dl>
<dt>
<dd>
<pre>
$ ssltap -hs -p 444 interzone.mcom.com:443 &gt; hs.txt
</pre>
</dl>
<p> Output </p>
<dl>
<dt>
<dd>
<pre><code>
Connected to interzone.mcom.com : 443 -- &gt; [0:80 3d 01 03 00 00 24 00 00 00 10 01 00 80 02 00 |.= ....$.........
                                               10:80 03 00 80 04 00 80 06 00 40 07 00 c0 00 00 04 | .........[at]......
                                               20:00 ff e0 00 00 0a 00 ff e1 00 00 09 00 00 03 03 | ........&amp; aacute;.......
                                               30:55 e6 e4 99 79 c7 d7 2c 86 78 96 5d b5 cf e9 | U..y &amp; Ccedil;�, .x.] &amp;
    micro;
&amp;Iuml;
&amp;eacute;
alloclen = 63 bytes
   [ssl2]  ClientHelloV2 {
            version = {0x03, 0x00}
            cipher-specs-length = 36 (0x24)
            sid-length = 0 (0x00)
            challenge-length = 16 (0x10)
            cipher-suites = {
                  (0x010080) SSL2/RSA/RC4-128/MD5
                  (0x020080) SSL2/RSA/RC4-40/MD5
                  (0x030080) SSL2/RSA/RC2CBC128/MD5
                  (0x040080) SSL2/RSA/RC2CBC40/MD5
                  (0x060040) SSL2/RSA/DES64CBC/MD5
                  (0x0700c0) SSL2/RSA/3DES192EDE-CBC/MD5
                  (0x000004) SSL3/RSA/RC4-128/MD5
                  (0x00ffe0) SSL3/RSA-FIPS/3DES192EDE-CBC/SHA
                  (0x00000a) SSL3/RSA/3DES192EDE-CBC/SHA
                  (0x00ffe1) SSL3/RSA-FIPS/DES64CBC/SHA
                  (0x000009) SSL3/RSA/DES64CBC/SHA
                  (0x000003) SSL3/RSA/RC4-40/MD5
                  }
            session-id = { }
            challenge = { 0x0355 0xe6e4 0x9979 0xc7d7 0x2c86 0x7896 0x5db
0xcfe9 }
}
]
&lt;additional records in same formats&gt;
Server socket closed.
</code></pre>
</dl>
<h2>USAGE TIPS</h2>
<p> When SSL restarts a previous session, it makes use of cached information to do a partial handshake. If you wish to capture a full SSL handshake, restart the browser to clear the session id cache. </p>
<p> If you run the tool on a machine other than the SSL server to which you are trying to connect, the browser will complain that the host name you are trying to connect to is different from the certificate. If you are using the default BadCert callback, you can still connect through a dialog. If you are not using the default BadCert callback, the one you supply must allow for this possibility.</p>
<h2>SEE ALSO</h2>
<p> The NSS Security Tools are also documented at m[blue]<code><a rel="nofollow" href="http://www.mozilla.org/projects/security/pki/nss/">http://www.mozilla.org/projects/security/pki/nss/</a></code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>ADDITIONAL RESOURCES</h2>
<p> For information about NSS and other tools related to NSS (like JSS), check out the NSS project wiki at m[blue]<code><a rel="nofollow" href="http://www.mozilla.org/projects/security/pki/nss/">http://www.mozilla.org/projects/security/pki/nss/</a></code>m[]. The NSS site relates directly to NSS code changes and releases. </p>
<p> Mailing lists: <a rel="nofollow" href="https://lists.mozilla.org/listinfo/dev-tech-crypto">https://lists.mozilla.org/listinfo/dev-tech-crypto</a> </p>
<p> IRC: Freenode at #dogtag-pki</p>
<h2>AUTHORS</h2>
<p> The NSS tools were written and maintained by developers with Netscape, Red Hat, Sun, Oracle, Mozilla, and Google. </p>
<p> Authors: Elio Maldonado &lt;emaldona [at] redhat.com&gt;, Deon Lackey &lt;dlackey [at] redhat.com&gt;.</p>
<h2>LICENSE</h2>
<p> Licensed under the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a rel="nofollow" href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a></p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Mozilla NSS bug 836477</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://bugzilla.mozilla.org/show_bug.cgi?id=836477">https://bugzilla.mozilla.org/show_bug.cgi?id=836477</a></dl>
<dt> 2.</p>
<dd> <a rel="nofollow" href="http://www.mozilla.org/projects/security/pki/nss/">http://www.mozilla.org/projects/security/pki/nss/</a></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.mozilla.org/projects/security/pki/nss/tools">http://www.mozilla.org/projects/security/pki/nss/tools</a></dl>
</dl>
<h2>Index</h2>
