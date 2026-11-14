---
title: "zsyncmake(1)"
name: "zsyncmake"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zsyncmake/"
description: "zsyncmake – Build control file for"
---

<h2 class="name">NAME</h2>
<p> zsyncmake &#8211; Build control file for </p>
<p> <a href="/docs/linux/man/1-zsync/">zsync</a>(1)</p>
<h2>SYNTAX</h2>
<p> zsyncmake [ { -z | -Z } ] [ -e ] [ -C ] [ -u <i>url</i> ] [ -U <i>url</i> ] [ -b <i>blocksize</i> ] [ -o <i>outfile</i> ] [ -f <i>targetfilename</i> ] [ -v ] <i>filename</i> </p>
<p> zsync -V</p>
<h2>DESCRIPTION</h2>
<p> Constructs a metafile for the zsync client program to use to perform partial file downloads. <i>filename</i> is the file that users wish to downloads; zsyncmake constructs the appropriate metafile and writes <i>filename</i>.zsync in the current directory. </p>
<p> zsync will need at least one URL from which to download the file content. If the .zsync will be in the same directory as the file to download, you can accept the default &#8211; zsync includes a relative URL in the control file. If not, use the <code>-u</code> option to specify the URL. You should also specify a URL for the uncompressed content with -U if available, as zsync can make use of this for more efficient downloads sometimes. (You can edit the .zsync file and add these afterwards &#8211; it has a simple key: value format in the header &#8211; but I suggest you only do this once you are familiar with the tool.) </p>
<p> Note that zsyncmake itself does not (currently) verify the URLs or download any data, you must provide the file data locally and check the URLs yourself.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code> <i>blocksize</i></p>
<dd> Specify the blocksize to the underlying rsync algorithm. A smaller blocksize may be more efficient for files where there are likely to be lots of small, scattered changes between downloads; a larger blocksize is more efficient for files with fewer or less scattered changes. This blocksize must be a power of two. If not specified, zsyncmake chooses one which it thinks is best for this file (currently either 2048 or 4096 depending on file size) &#8211; so normally tyou should not need to override the default.</p>
<dt><code>-C</code></p>
<dd> Tells zsyncmake not to generate any instructions in the .zsync telling the client to compress the data it receives. This is implied by -z, but this option is here in case you compress a file yourself only for the transfer, but want the client to end up with the uncompressed file (e.g. you are transferring an ISO, which is held compressed on the server, but which the client cannot use unless it is uncompressed). Without -C, zsyncmake will produce directions for the client to compress the file it receives where appropriate; -C is here so you can stop it telling the client to do that.</p>
<dt><code>-e</code></p>
<dd> Tells zsyncmake that the client must be able to receive the exact file that was supplied. Without this option, zsyncmake only gives a weaker guarantee &#8211; that the client will receive the data it contains (e.g. it might transfer the uncompressed version of a .gz to the client). Note that this still doesn&#8217;t guarantee that the client will get it &#8211; the client could ignore the directives in the zsync file, or might be incapable of exactly reproducing the compression used. But with -e you know that zsyncmake has made it possible to get the exact data &#8211; it will exit with an error if it cannot.</p>
<dt><code>-f</code> <i>filename</i></p>
<dd> Set the filename to include in the output file (this is what the file will be called when a user finished downloading it).</p>
<dt><code>-o</code> <i>outputfile</i></p>
<dd> Override the default output file name.</p>
<dt><code>-u</code> <i>url</i></p>
<dd> Specifies the URL from which users can download the content of the supplied file. Users need the control file in order to find out what parts of the file they already have, and they need the URLs to retrieve the parts of the file that they don&#8217;t already have. You can specify multiple URLs by specifying -u multiple times. If not specified, zsync assumes that the file and the .zsync will reside in the same public directory, and includes a single relative URL.</p>
<dt><code>-U</code> <i>url</i></p>
<dd> Specifies a URL corresponding to the decompressed content of the file (only applicable if it is a gzip file). zsync can sometimes download more efficiently from the uncompressed data than from the compressed data &#8211; it will take advantage of this if available. If no URLs are specifies, zsync looks for a file without the .gz extension and assumes that this will be in the same public dir as the .zsync, and includes a relative URL to it.</p>
<dt><code>-v</code></p>
<dd> Enable verbose messages.</p>
<dt><code>-V</code></p>
<dd> Prints the version of zsync.</p>
<dt><code>-z</code></p>
<dd> Compress the file to transfer. Note that this overwrites any file called <i>filename</i>.gz without warning (if you don&#8217;t give a filename, e.g. because you are reading from stdin, then zsync will use the name supplied with -f, or as a last fallback, zsync-target.gz).</p>
<dt>zsync can work with compressed data, and, in most cases where the data is not already compressed, it is more efficient to compress it first. While you can just compress the file to transfer with gzip, if you use this option then zsyncmake will compress the file for you, producing a .gz file which is optimised for zsync. This can be 30% more efficient at download time than compressing with gzip &#8211;best &#8211; but the compressed file will not be as small at that produced by gzip.</p>
<dd>
<dt><code>-Z</code></p>
<dd> zsyncmake automatically looks inside gzip compressed files and exports the underlying, uncompressed data to the zsyncmake file. In testing this has proved to provide greater download efficiency. -Z overrides the default behaviour and treats gzip files as just binary data. Use this if it is essential that the user receives the compressed data (for instance because a cryptographic signature is available only for the compressed data). zsync is typically no use if you specify -Z, unless the gzip file was compressed with the special &#8211;rsync option to make it friendly to differential transfers.</dl>
<h2>EXAMPLES</h2>
<p> zsyncmake -C -u <a rel="nofollow" href="http://ftp.uk.debian.org/debian/dists/sarge/main/binary-i386/Packages.gz">http://ftp.uk.debian.org/debian/dists/sarge/main/binary-i386/Packages.gz</a> Packages.gz </p>
<p> Note use of -C to save the client compressing the file on receipt; the Debian package system uses the file uncompressed. </p>
<p> zsyncmake -z my-subversion-dump </p>
<p> In this case there is a large, compressible file to transfer. This creates a gzipped version of the file (optimised for zsync), and a .zsync file. A URL is automatically added assuming that the two files will be served from the same directory on the web server. </p>
<p> zsyncmake -e -u <a rel="nofollow" href="http://www.mirrorservice.org/sites/ftp.freebsd.org/pub/FreeBSD/ports/distfiles/zsync-0.2.2.tar.gz">http://www.mirrorservice.org/sites/ftp.freebsd.org/pub/FreeBSD/ports/distfiles/zsync-0.2.2.tar.gz</a> zsync-0.2.2.tar.gz </p>
<p> This creates a zsync referring to the named source tarball, which the client should download from the given URL. This example is for downloading a source tarball for a FreeBSD port, hence -e is specified so the client will be able to match its md5sum. </p>
<h2>AUTHORS</h2>
<p> Colin Phipps &lt;cph [at] moria.org.uk&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zsync/">zsync</a>(1) </p>
<h2>Index</h2>
