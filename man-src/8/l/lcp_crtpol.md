---
title: "lcp_crtpol(8)"
name: "lcp_crtpol"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lcp_crtpol/"
description: "lcp_crtpol – create a TXT v1 Launch Control Policy"
---

<p>lcp_crtpol &#8211; create a TXT v1 Launch Control Policy</p>
<h2>Synopsis</h2>
<p><code>lcp_crtpol</code> <code>-t</code> <i>policy-type</i> [<code>-a</code> <i>hashalg</i>] [<code>-v</code> <i>version</i>] [<code>-sr</code> <i>SINIT-revocation-counter</i>] [<code>-s</code> <i>srtm-file</i>] [<code>-m</code> <i>mle-file</i>] [<code>-o</code> <i>policy-file</i>] [<code>-b</code> <i>policy-data-file</i>] [<code>-pcf</code> <i>policy-control-field</i>] [<code>-h</code>]</p>
<h2>Description</h2>
<p><code>lcp_crtpol</code> is used to create a TXT v1 LCP policy (and optionally policy data), which can later be written to the TPM. The policy created are for platforms produced before 2009 (Weybridge, Montevina, McCreary).</p>
<h2>Options</h2>
<dl>
<dt><code>-t&nbsp;<wbr></code><i>policy-type</i></p>
<dd>Policy type can be UINT8 or string. 5 strings are supported for the reserved LCP policy types. Strings and default policy type values for each string are:</p>
<dl>
<dd>
<dl>
<dt>0 or &quot;hashonly&quot;</p>
<dd>
<dt>1 or &quot;unsigned&quot;</p>
<dd>
<dt>2 or &quot;signed&quot;</p>
<dd>
<dt>3 or &quot;any&quot;</p>
<dd>
<dt>4 or &quot;forceowner&quot;</p>
<dd></dl>
</dl>
<dt><code>-a&nbsp;<wbr></code><i>hashalg</i></p>
<dd>Hash algorithm. Currently we only support SHA-1 algorithm: 0 OR &#8216;sha1&#8217;.</p>
<dt><code>-v&nbsp;<wbr></code><i>version</i></p>
<dd>Version number. Currently it can be set to 0 or 1 if specified. The default value is 0.</p>
<dt><code>-sr&nbsp;<wbr></code><i>SINIT-revocation-counter</i></p>
<dd>The default sinit revocation counter is 0.</p>
<dt><code>-s&nbsp;<wbr></code><i>srtm-file</i></p>
<dd>File name of platform configuration data, as produced by <code>lcp_crtpconf.</code></p>
<dt><code>-m&nbsp;<wbr></code><i>mle-file</i></p>
<dd>File name of file containing the MLE hash values. This is a text file that contains one SHA-1 hash per line. The value of the hash must be hexadecimal values, specified either a single un-deliminated set or as space-delimited two-character (i.e. one byte) values. This can be produced by the <code>lcp_mlehash</code> command.</p>
<dt><code>-o&nbsp;<wbr></code><i>policy-file</i></p>
<dd>File name to store the output policy.</p>
<dt><code>-b&nbsp;<wbr></code><i>policy-data-file</i></p>
<dd>File name to store the LCP Policy data.</p>
<dt><code>-pcf&nbsp;<wbr></code><i>policy-control-field</i></p>
<dd>The default policy control field value is 0.</p>
<dt><code>-h</code></p>
<dd>Print out the help message</dl>
<h2>Examples</h2>
<p><code>lcp_crtpol -t </code><i>0 </i><code> -m </code><i>mle-file </i><code> -o </code><i>policy-hashonly-file </p>
<p> </i><code>lcp_crtpol -t </code><i>1 </i><code> -m </code><i>mle-file </i><code> -s </code><i>pconf-file </i><code> -b </code><i> policy-data-file </p>
<p> </i><code>lcp_crtpol -t </code><i>unsigned </i><code> -a </code><i>sha1 </i><code> -m </code><i>mle-file </i><code> -s </code><i>pconf-file </i><code> -o </code><i>policy-unsigned-file </i><code> -b </code><i>policy-data-file </i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lcp_readpol/">lcp_readpol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_writepol/">lcp_writepol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_mlehash/">lcp_mlehash</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpconf/">lcp_crtpconf</a></code>(8). </p>
