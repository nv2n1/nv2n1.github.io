---
title: "lcp_mlehash(8)"
name: "lcp_mlehash"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lcp_mlehash/"
description: "lcp_mlehash – generate a SHA-1 hash of a TXT MLE binary file suitable for use in a TXT launch control policy"
---

<p>lcp_mlehash &#8211; generate a SHA-1 hash of a TXT MLE binary file suitable for use in a TXT launch control policy</p>
<h2>Synopsis</h2>
<p><code>lcp_mlehash</code> [<code>-v</code>] [<code>-c</code> <i>cmdline</i>] [<code>-h</code>] <i>mle-file</i></p>
<h2>Description</h2>
<p><code>lcp_mlehash</code> is used to generate a SHA-1 hash of the portion of an executable file that contains the Intel® TXT measured launched environment (MLE). In the MLE binary file, the portion of the file to be used as the MLE is specified in the MLE header structure. If verbose mode is not used, the output is suitable for use as the mle-file to the <code>lcp_crtpol</code> and <code>lcp_crtpolelt</code> commands.</p>
<h2>Options</h2>
<dl>
<dt><i>mle-file</i></p>
<dd>File name of the MLE binary. If it is a gzip file then it will be un-ziped before hashing.</p>
<dt><code>-v</code></p>
<dd>Verbose mode, display progress indications.</p>
<dt><code>-c&nbsp;<wbr></code><i>cmdline</i></p>
<dd>Specify quote-delimited command line. It is important to specify the command line that is used when launching the MLE or the hash will not match what is calculated by SINIT.</p>
<dt><code>-h</code></p>
<dd>Print out the help message.</dl>
<h2>Examples</h2>
<p><code>lcp_mlehash -c </code><i>&quot;logging=memory,serial,vga&quot; /boot/tboot.gz </i><code>&gt; </code><i>mle-hash </i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lcp_readpol/">lcp_readpol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_writepol/">lcp_writepol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpol/">lcp_crtpol</a></code>(8), <code><a href="/docs/linux/man/8-lcp_crtpolelt/">lcp_crtpolelt</a></code>(8). </p>
