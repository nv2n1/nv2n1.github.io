---
title: "modhex(1)"
name: "modhex"
section: "1"
letter: "m"
url: "/docs/linux/man/1-modhex/"
description: "modhex – convert data to/from modhex encoding"
---

<h2 class="name">NAME</h2>
<p> modhex &#8211; convert data to/from modhex encoding </p>
<h2>SYNOPSIS</h2>
<p> <code>modhex</code> [-d] [-h] <i>DATA</i></p>
<h2>DESCRIPTION</h2>
<p> Encode/decode modhex data <i>DATA</i> to binary and hex.</p>
<h2>OPTIONS</h2>
<p> The string DATA is the data to convert. </p>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Decode data (the default is to encode data).</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Use hex encoding for all non-modhex data.</dl>
<h2>EXAMPLES</h2>
<p> ModHex encode ASCII-string &quot;test&quot;: </p>
<dl>
<dt>
<dd>
<pre>
modhex test
</pre>
</dl>
<p> Decode ModHex data &quot;ifhgieif&quot; into ASCII string: </p>
<dl>
<dt>
<dd>
<pre>
modhex -d ifhgieif
</pre>
</dl>
<p> ModHex encode hex-encoded data &quot;b565716f&quot;: </p>
<dl>
<dt>
<dd>
<pre>
modhex -h b565716f
</pre>
</dl>
<p> Decode ModHex data &quot;nghgibhv&quot; and print hex-encode data: </p>
<dl>
<dt>
<dd>
<pre>
modhex -d -h nghgibhv
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> YubiKeys can be obtained from Yubico: <a rel="nofollow" href="http://www.yubico.com/">http://www.yubico.com/</a> </p>
<h2>Index</h2>
