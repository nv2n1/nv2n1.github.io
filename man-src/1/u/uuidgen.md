---
title: "uuidgen(1)"
name: "uuidgen"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uuidgen/"
description: "uuidgen – create a new UUID value"
---

<h2 class="name">NAME</h2>
<p> uuidgen &#8211; create a new UUID value </p>
<h2>SYNOPSIS</h2>
<p> <code>uuidgen</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> The <code>uuidgen</code> program creates (and prints) a new universally unique identifier (UUID) using the <code><a href="/docs/linux/man/3-libuuid/">libuuid</a></code>(3) library. The new UUID can reasonably be considered unique among all UUIDs created on the local system, and among UUIDs created on other systems in the past and in the future. </p>
<p> There are three types of UUIDs which <code>uuidgen</code> can generate: time-based UUIDs, random-based UUIDs, and hash-based UUIDs. By default <code>uuidgen</code> will generate a random-based UUID if a high-quality random number generator is present. Otherwise, it will choose a time-based UUID. It is possible to force the generation of one of these first two UUID types by using the <code>&#8211;random</code> or <code>&#8211;time</code> options. </p>
<p> The third type of UUID is generated with the <code>&#8211;md5</code> or <code>&#8211;sha1</code> options, followed by <code>&#8211;namespace</code> <i>namespace</i> and <code>&#8211;name</code> <i>name</i>. The <i>namespace</i> may either be a well-known UUID, or else an alias to one of the well-known UUIDs defined in RFC 4122, that is <code>@dns</code>, <code>@url</code>, <code>@oid</code>, or <code>@x500</code>. The <i>name</i> is an arbitrary string value. The generated UUID is the digest of the concatenation of the namespace UUID and the name value, hashed with the MD5 or SHA1 algorithms. It is, therefore, a predictable value which may be useful when UUIDs are being used as handles or nonces for more complex values or values which shouldn&#8217;t be disclosed directly. See the RFC for more information.</p>
<h2>OPTIONS</h2>
<p> <code>-r</code>, <code>&#8211;random</code></p>
<dl>
<dt>
<dd> Generate a random-based UUID. This method creates a UUID consisting mostly of random bits. It requires that the operating system has a high quality random number generator, such as <i>/dev/random</i>.</dl>
<p> <code>-t</code>, <code>&#8211;time</code></p>
<dl>
<dt>
<dd> Generate a time-based UUID. This method creates a UUID based on the system clock plus the system&#8217;s ethernet hardware address, if present.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-m</code>, <code>&#8211;md5</code></p>
<dl>
<dt>
<dd> Use MD5 as the hash algorithm.</dl>
<p> <code>-s</code>, <code>&#8211;sha1</code></p>
<dl>
<dt>
<dd> Use SHA1 as the hash algorithm.</dl>
<p> <code>-n</code>, <code>&#8211;namespace</code> <i>namespace</i></p>
<dl>
<dt>
<dd> Generate the hash with the <i>namespace</i> prefix. The <i>namespace</i> is UUID, or &#8216;@ns&#8217; where &quot;ns&quot; is well-known predefined UUID addressed by namespace name (see above).</dl>
<p> <code>-N</code>, <code>&#8211;name</code> <i>name</i></p>
<dl>
<dt>
<dd> Generate the hash of the <i>name</i>.</dl>
<p> <code>-x</code>, <code>&#8211;hex</code></p>
<dl>
<dt>
<dd> Interpret name <i>name</i> as a hexadecimal string.</dl>
<h2>CONFORMING TO</h2>
<p> OSF DCE 1.1</p>
<h2>EXAMPLES</h2>
<p> uuidgen &#8211;sha1 &#8211;namespace @dns &#8211;name &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;</p>
<h2>AUTHORS</h2>
<p> <code>uuidgen</code> was written by Andreas Dilger for <code><a href="/docs/linux/man/3-libuuid/">libuuid</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libuuid/">libuuid</a></code>(3), <i>RFC 4122</i> &lt;<a rel="nofollow" href="https://tools.ietf.org/html/rfc4122">https://tools.ietf.org/html/rfc4122</a>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>uuidgen</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
