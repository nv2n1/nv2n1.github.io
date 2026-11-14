---
title: "ziptorrent(1)"
name: "ziptorrent"
section: "1"
letter: "z"
url: "/docs/linux/man/1-ziptorrent/"
description: "ziptorrent – torrentzip zip archives"
---

<h2>NAME</h2>
<p> ziptorrent &#8211; torrentzip zip archives</p>
<h2>SYNOPSIS</h2>
<p> <code>ziptorrent</code> [<code>-hnVv</code>] <code>archive Op &#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ziptorrent</code> torrentzips <code>archive.</code> This is a restricted file format used for using bittorrent on zip files. Please see <a href="/docs/linux/man/3-zip_set_archive_flag/">zip_set_archive_flag</a>(3) for details on what information gets lost through this process. </p>
<p> Supported options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-h</code></p>
<dd> Display a short help message and exit.</p>
<dt><code>-n</code></p>
<dd> Don&#8217;t actually change archives, just print what would be done.</p>
<dt><code>-V</code></p>
<dd> Display version information and exit.</p>
<dt><code>-v</code></p>
<dd> Be verbose: print which archives are already torrentzipped and which need to be rezipped.</dl>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>ziptorrent</code> exits 0 on success and &gt;1 if an error occurred.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zipcmp/">zipcmp</a>(1), <a href="/docs/linux/man/1-zipmerge/">zipmerge</a>(1), <a href="/docs/linux/man/3-libzip/">libzip</a>(3)</p>
<h2>AUTHORS</h2>
<p> Dieter Baron &lt;dillo [at] giga.or.at&gt; and Thomas Klausner &lt;tk [at] giga.or.at&gt; </p>
<h2>Index</h2>
