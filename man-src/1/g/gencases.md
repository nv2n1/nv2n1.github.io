---
title: "gencases(1)"
name: "gencases"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gencases/"
description: "gencases – 802.11b weak IV generation tool"
---

<h2 class="name">NAME</h2>
<p> <code>gencases</code> &#8211; 802.11b weak IV generation tool </p>
<h2>SYNOPSIS</h2>
<p> <code>gencases (-s </code><i>pw | </i><code>-h </code><i>key ) </i><code>-f </code><i>file </i>[-n <i>num </i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gencases</code> is used to generate test 802.11b packets that are encrypted with weak initialization vectors as described by Fluhrer, Mantin, and Shamir (FMS). The packets are saved to a user specified file in libpcap compatible format for later use with the <a href="/docs/linux/man/1-airsnort/">airsnort</a>(1) program. The intent is to provide airsnort with the packets required to demonstrate the FMS attack. </p>
<p> Arguments to gencases allow the user to specify the WEP key that will be used to encrypt the packets as well as the number of packets to be generated for each byte of the wep key. The generated packets represent UDP echo requests from host 192.168.0.2 (on a wired net) to host 192.168.0.10 (on a wireless net) and the corresponding replies. The wireless client has MAC 00:02:2d:01:23:45, the wired host has MAC 00:04:5A:AB:CD:EF, and the access point has BSSID 00:02:2D:98:76:54. </p>
<p> The generated packet file can be examined with standard packet analysis tools such as tcpdump or ethereal. It can also be loaded into <a href="/docs/linux/man/1-airsnort/">airsnort</a>(1) which, given that a sufficient number of cases were generated for each key byte, will produce a cracked WEP key. Running the generated file through the <a href="/docs/linux/man/1-decrypt/">decrypt</a>(1) utility will produce the decrypted versions of the packets which should reflect the echo request/reply traffic described above, and which can be verified using tcpdump or ethereal.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s </code><i>pw</i></p>
<dd> Password as an ASCII string. 5 or 13 characters for 40 and 128 bit WEP cases respectively.</p>
<dt><code>-h </code><i>key </i></p>
<dd> Password as a colon separated list of 2 digit hex values. 5 or 13 hex values for 40 and 128 bit WEP cases respectively.</p>
<dt><code>-f </code><i>file </i></p>
<dd> Output file for generated cases.</p>
<dt><code>-n </code><i>num</i></p>
<dd> Number of sample cases to generate for each key byte (1-256). Default is 100.</dl>
<h2>EXAMPLES</h2>
<p> Generate 100 cases per key byte with the ASCII password &quot;hello&quot; to file &quot;test&quot; </p>
<blockquote>
<pre>
gencases -s hello -f test
</pre>
</blockquote>
<p> Generate 200 cases per key byte with the hex key &quot;23:56:89:ab:de&quot; to file &quot;test&quot; </p>
<blockquote>
<pre>
gencases -h 23:56:89:ab:de -f test -n 200 
</pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-airsnort/">airsnort</a>(1) <a href="/docs/linux/man/1-decrypt/">decrypt</a>(1)</p>
<h2>AUTHORS</h2>
<p> An Jeremy Bruestle &lt;melvin [at] melvin.net&gt; An Blake Hegerle &lt;blake [at] melvin.net&gt; An Snax &lt;snax [at] shmoo.com&gt;</p>
<h2>Index</h2>
