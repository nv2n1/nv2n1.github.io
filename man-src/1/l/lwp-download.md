---
title: "lwp-download(1)"
name: "lwp-download"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lwp-download/"
description: "lwp-download – Fetch large files from the web"
---

<h2 class="name">NAME</h2>
<p> lwp-download &#8211; Fetch large files from the web </p>
<h2>SYNOPSIS</h2>
<p> <code>lwp-download</code> [<code>-a</code>] [<code>-s</code>] &lt;<i>url</i>&gt; [&lt;<i>local path</i>&gt;]</p>
<h2>DESCRIPTION</h2>
<p> The <code>lwp-download</code> program will save the file at <i>url</i> to a local file. </p>
<p> If <i>local path</i> is not specified, then the current directory is assumed. </p>
<p> If <i>local path</i> is a directory, then the last segment of the path of the <i>url</i> is appended to form a local filename. If the <i>url</i> path ends with slash the name &#8220;index&#8221; is used. With the <code>-s</code> option pick up the last segment of the filename from server provided sources like the Content-Disposition header or any redirect URLs. A file extension to match the server reported Content-Type might also be appended. If a file with the produced filename already exists, then <code>lwp-download</code> will prompt before it overwrites and will fail if its standard input is not a terminal. This form of invocation will also fail is no acceptable filename can be derived from the sources mentioned above. </p>
<p> If <i>local path</i> is not a directory, then it is simply used as the path to save into. If the file already exists it&#8217;s overwritten. </p>
<p> The <i>lwp-download</i> program is implemented using the <i>libwww-perl</i> library. It is better suited to down load big files than the <i>lwp-request</i> program because it does not store the file in memory. Another benefit is that it will keep you updated about its progress and that you don&#8217;t have much options to worry about. </p>
<p> Use the <tt>&quot;-a&quot;</tt> option to save the file in text (ascii) mode. Might make a difference on dosish systems.</p>
<h2>EXAMPLE</h2>
<p> Fetch the newest and greatest perl version: </p>
<pre>
 $ lwp-download <a rel="nofollow" href="http://www.perl.com/CPAN/src/latest.tar.gz">http://www.perl.com/CPAN/src/latest.tar.gz</a>
 Saving to 'latest.tar.gz'...
 11.4 MB received in 8 seconds (1.43 MB/sec)
</pre>
<h2>AUTHOR</h2>
<p> Gisle Aas &lt;gisle [at] aas.no&gt; </p>
<h2>Index</h2>
