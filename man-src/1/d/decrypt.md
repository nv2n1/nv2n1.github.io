---
title: "decrypt(1)"
name: "decrypt"
section: "1"
letter: "d"
url: "/docs/linux/man/1-decrypt/"
description: "decrypt – 802.11b packet decryption tool"
---

<h2 class="name">NAME</h2>
<p> <code>decrypt</code> &#8211; 802.11b packet decryption tool </p>
<h2>SYNOPSIS</h2>
<p> <code>decrypt (-p </code><i>key | </i><code>-f </code><i>dictfile ) </i><code>-m </code><i>bssid </i><code>-e </code><i>infile </i> <code>-d </code><i>outfile </i> [-b ] [-o <i>offset</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>decrypt</code> is a command line tool that takes 3 pieces of input, a pcap format input file, a WEP key, and a bssid (access point MAC address). If the provided WEP key is found to be the key for the indicated bssid, associated packets are decrypted and copied to the output file. If the key is not a valid key, all input packets are written unchanged to the output file. The output is a pcap compatible dump file and can be examined with tools such as tcpdump or ethereal to view the decrypted data. </p>
<p> This tool understands two link types, LINKTYPE_IEEE802_11 and LINKTYPE_PRISM_HEADER. Other 802.11b capture formats can be decrypted by specifying an optional offset command line argument with the -o switch to indicate the number of header bytes that precede the actual 802.11b packet. That is, the number of bytes that precede the first frame control byte of each 802.11b packet. </p>
<p> An alternate dictionary mode utilizes an input word list of potential WEP keys to attempt to find a valid key for the specified bssid. If a valid key is found packets are decrypted and copied to the specified output file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p </code><i>key</i></p>
<dd> password whose length must be 5 or 13 bytes of ascii data or 5 or 13 2 digit, colon separated hex values.</p>
<dt><code>-f </code><i>dictfile </i></p>
<dd> the name of a file containing one password per line in the format specified above. All passwords in the file will be tried against the specified bssid.</p>
<dt><code>-b</code></p>
<dd> Discard beacon packets. Beacon packets will not be written in the output file.</p>
<dt><code>-o </code><i>offset</i></p>
<dd> Optional integer number of bytes of header that precede the first frame control byte in the 802.11b packet. <code>decrypt</code> can recognized packets captured with no prefix bytes (pcap type DLT_IEEE802_11) as well as packets prefixed with prism2 style headers (pcap type DLT_PRISM_HEADER). In these two cases, no offest argument is required.</p>
<dt><code>-m </code><i>bssid</i></p>
<dd> 6 byte mac address of the AP for which traffic is to be decrypted in the form xx:xx:xx:xx:xx:xx</p>
<dt><code>-e </code><i>infile</i></p>
<dd> The name of the file containing encrypted packets. This file is expected to be in pcap dump file format.</p>
<dt><code>-d </code><i>outfile</i></p>
<dd> The output file produced by decrypting all data packets associated with the named AP using the specified key. All other packets are copied from infile unchanged. This file will be in pcap dump file format. If the provided key is not a valid key for the specified bssid, all packets are copied unchanged to the output file.</dl>
<h2>EXAMPLES</h2>
<p> Decrypt all trafic to/from the access point with bssid 01:02:34:56:78:9a using ascii key &quot;MyKey&quot;, reading from input file &quot;capture&quot;, writing the results to a file named &quot;decrypted&quot; </p>
<blockquote>
<pre>
decrypt -p MyKey -m 01:02:34:56:78:9a -e capture -d decrypted
</pre>
</blockquote>
<p> Attempt to find a key for traffic to/from the access point with bssid 01:02:34:56:78:9a by trying all keys contained in the dictionary file &quot;words&quot;. Packets are read from the input file &quot;packets&quot; and contain 50 bytes of prefix data Results are written to file &quot;decrypted&quot; </p>
<blockquote>
<pre>
decrypt -f words -o 50 -m 01:02:34:56:78:9a -e packets -d decrypted
</pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-airsnort/">airsnort</a>(1) <a href="/docs/linux/man/1-gencases/">gencases</a>(1)</p>
<h2>AUTHORS</h2>
<p> An Jeremy Bruestle &lt;melvin [at] melvin.net&gt; An Blake Hegerle &lt;blake [at] melvin.net&gt; An Snax &lt;snax [at] shmoo.com&gt;</p>
<h2>Index</h2>
