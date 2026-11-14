---
title: "mulk(1)"
name: "mulk"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mulk/"
description: "mulk – Non-interactive multi-connection network downloader with image filtering and Metalink support."
---

<h2>NAME</h2>
<p> mulk &#8211; Non-interactive multi-connection network downloader with image filtering and Metalink support.</p>
<h2>SYNOPSIS</h2>
<p> <code>mulk [OPTION]&#8230; [URL]&#8230; </code></p>
<h2>DESCRIPTION</h2>
<p> Multi-connection command line tool for downloading Internet sites with image filtering and Metalink support. Similar to wget and cURL, but it manages up to 50 simultaneous and parallel links. Main features are: HTML code parsing, recursive fetching, Metalink retrieving, segmented download and image filtering by width and height. It is based on libcurl, libtidy and libxml2. </p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt>&#8211;version</p>
<dd> Show <code>Mulk</code> version number.</p>
<dt>-h, &#8211;help</p>
<dd> Show this help message.</p>
<dt>-q, &#8211;quiet</p>
<dd> Quiet (no output).</p>
<dt>-v, &#8211;verbose</p>
<dd> Verbosity enabled.</p>
<dt>-d, &#8211;depth</p>
<dd> Link depth when downloading Internet sites.</p>
<dt>-t, &#8211;option-file</p>
<dd> Text file with list of options. The file accepts only long options without &#8216;&#8211;&#8216;. The lines starting with &#8216;#&#8217; are skipped.</p>
<dt>-f, &#8211;url-file</p>
<dd> Text file with list of URLs to download. The lines starting with &#8216;#&#8217; are skipped.</p>
<dt>-l, &#8211;metalink-file</p>
<dd> Metalink XML file to download.</p>
<dt> &#8211;metalink-location</p>
<dd> Location origin of the file to download.</p>
<dt> &#8211;metalink-os</p>
<dd> Operating system of the file to download.</p>
<dt>-r, &#8211;report-file</p>
<dd> Generate a report in a text file.</p>
<dt>-c, &#8211;report-csv-file</p>
<dd> Generate a report in a CSV file.</p>
<dt>-p, &#8211;max-sim-conns-per-host</p>
<dd> Maximum simultaneous connections per each host (default = 2, max value = 5).</p>
<dt>-m, &#8211;max-sim-conns</p>
<dd> Maximum simultaneous connections (default = 50, maxvalue = 50).</p>
<dt>-x, &#8211;disable-site-save</p>
<dd> Don&#8217;t save whole site tree to disk (enabled by default).</p>
<dt>-g, &#8211;save-gif-image</p>
<dd> Save only GIF images.</p>
<dt>-n, &#8211;save-png-image</p>
<dd> Save only PNG images.</p>
<dt>-j, &#8211;save-jpeg-image</p>
<dd> Save only JPEG images.</dl>
<h2>IMAGE OPTIONS (active only with -g, -n or -j)</h2>
<dl>
<dt> &#8211;min-image-width WIDTH</p>
<dd> Minimum image width.</p>
<dt> &#8211;max-image-width WIDTH</p>
<dd> Maximum image width.</p>
<dt> &#8211;min-image-height HEIGHT</p>
<dd> Minimum image height.</p>
<dt> &#8211;max-image-height HEIGHT</p>
<dd> Maximum image height.</p>
<dt> &#8211;output-dir OUTPUTDIR</p>
<dd> Output directory to save images.</dl>
<h2>BUGS</h2>
<p> <code>Please report any bugs using the bug reporting form on the</code> <code>Mulk</code> web site: <code><a rel="nofollow" href="http://sourceforge.net/projects/mulk">http://sourceforge.net/projects/mulk</a></code> </p>
<h2>SEE ALSO</h2>
<p> Additional information and the latest version is available at the web site: <code><a rel="nofollow" href="http://sourceforge.net/projects/mulk">http://sourceforge.net/projects/mulk</a></code> </p>
<h2>AUTHOR</h2>
<p> Emanuele Bovisio &lt;pocoyo [at] users.sourceforge.net&gt; wrote this manpage. </p>
<p> <code>Mulk</code> was written by Emanuele Bovisio. </p>
<h2>Index</h2>
