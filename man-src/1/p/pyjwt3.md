---

title: "pyjwt3(1)"
name: "pyjwt3"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pyjwt3/"
description: "pyjwt3 – Python implementation of JSON Web Token"
---

<p> <code>pyjwt3</code> [<i>,options/</i>] &lt;command&gt; [<i>,options/</i>] <i>,input/</i></p>
<p> Encodes or decodes JSON Web Tokens based on input</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-n</code>, <code>&#8211;no-verify</code></dt>
<dd> ignore signature verification on decode</dd>
<dt><code>&#8211;key</code>=<i>,KEY/</i></dt>
<dd> set the secret key to sign with</dd>
<dt><code>&#8211;alg</code>=<i>,ALG/</i></dt>
<dd> set crypto algorithm to sign with. default=HS256</dd></dl>
<h3>PyJWT subcommands are: <i>,encode/</i> and <i>,decode/</i>.</h3>
<dl>
<dt>encode</dt>
<dd> use to encode a supplied payload</dd>
<dt>decode</dt>
<dd> use to decode a supplied JSON web token</dd></dl>
<h2>EXAMPLES</h2>
<p> Decoding: </p>
<p> pyjwt3 <code>&#8211;key</code>=<i>,secret/</i> decode json.web.token </p>
<p> pyjwt3 decode <code>&#8211;no-verify</code> json.web.token </p>
<p> Encoding requires the key option and takes space separated key/value pairs separated by equals (=) as input. </p>
<p> Examples: </p>
<p> pyjwt3 <code>&#8211;key</code>=<i>,secret/</i> encode iss=me exp=1302049071 </p>
<p> pyjwt3 <code>&#8211;key</code>=<i>,secret/</i> encode foo=bar exp=+10 </p>
<p> The exp key is special and can take an offset to current Unix time.</p>
<h2>AUTHOR</h2>
<p> Jeff Lindsay &lt;progrium [at] gmail.com&gt; </p>
<p> This manual page was written by Daniele Tricoli &lt;eriol [at] mornie.org&gt;, for the Debian project (but may be used by others). </p>
