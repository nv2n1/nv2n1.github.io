---
title: "wnpkgs(7)"
name: "wnpkgs"
section: "7"
letter: "w"
url: "/docs/linux/man/7-wnpkgs/"
description: "wnpkgs – description of various WordNet system packages"
---

<p>wnpkgs &#8211; description of various WordNet system packages</p>
<h2>Description</h2>
<p>WordNet 3.0 is distributed in several formats and in various packages. All of the packages are available via anonymous FTP from <code><a href="ftp://ftp.cogsci.princeton.edu">ftp.cogsci.princeton.edu</a></code> and from the WordNet Web site at <code><a rel="nofollow" href="http://wordnet.princeton.edu">http://wordnet.princeton.edu</a></code>.</p>
<h3>Packages Available Via FTP and WWW</h3>
<p>The following WordNet packages can be downloaded using a web browser from <code><a href="ftp://ftp.cogsci.princeton.edu/wordnet/3.0">ftp://ftp.cogsci.princeton.edu/wordnet/3.0</a></code>, or from the Web site noted above. Users can also FTP directly from <code><a href="ftp://ftp.cogsci.princeton.edu">ftp.cogsci.princeton.edu</a></code>, directory <code>wordnet/3.0</code>. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Package</code></td>
<td ALIGN=center><code>Filename</code></td>
<td ALIGN=center><code>Platform</code></td>
<td ALIGN=center><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Database</td>
<td><code>WordNet-3.0.tar.gz</code></td>
<td>Unix/OS X</td>
<td> WordNet 3.0 database, interfaces, sense index, interface and library source code, documentation.
</td>
</tr>
<tr VALIGN=top>
<td>Database</td>
<td><code>WordNet-3.0.exe</code></td>
<td>Windows</td>
<td> WordNet 3.0 database, interfaces, sense index, interface and library source code, documentation.
</td>
</tr>
<tr VALIGN=top>
<td>Prolog Database</td>
<td><code>WNprolog-3.0.tar.gz</code></td>
<td>All</td>
<td> WordNet 3.0 database files in Prolog-readable format, documentation.
</td>
</tr>
<tr VALIGN=top>
<td>Sense Map</td>
<td><code>WNsnsmap-3.0.tar.gz</code></td>
<td>All</td>
<td> Mapping of 2.1 to 3.0 senses, documentation.
</td>
</tr>
</table>
</table>
<p></center></p>
<h3>Database Package</h3>
<p>The database package is a complete installation for WordNet 3.0 users. It includes the 3.0 database files, source code for the WordNet browsers and library, and documentation. The other packages are not included &#8211; they must be downloaded and installed separately. </p>
<p> Note that with this version of WordNet for Unix platforms, only source code is provided. Users should carefully read the README and INSTALL files for detailed information on compiling WordNet and dependencies.</p>
<h3>Prolog Database Package</h3>
<p>The WordNet 3.0 database files are available in this package in a Prolog-readable format. Documentation describing the file format is included. This package is only downloadable in compressed tar file format, although once unpackaged it can be used from Windows systems since the files are in ASCII. Many Windows utilities, such as WinZip, can deal with a compressed tar file.</p>
<h3>Sense Map Package</h3>
<p>To help users automatically convert 2.1 noun and verb senses to their corresponding 3.0 senses, we provide sense mapping information in this package. This package contains files to map polysemous and monosemous words, and documentation that describes the format of these files. As with the Prolog database, this package is only downloadable in compressed tar format, but the files are also in ASCII.</p>
<h2>Notes</h2>
<p>The lexicographer files and <code><a href="/docs/linux/man/1-grind/">grind</a></code>(1) program are not generally distributed. </p>
<p> All of the packages described above may not be available at the time of release of the 3.0 database package.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wnintro/">wnintro</a></code>(1), <code><a href="/docs/linux/man/3-wnintro/">wnintro</a></code>(3), <code><a href="/docs/linux/man/5-wnintro/">wnintro</a></code>(5), <code><a href="/docs/linux/man/7-wnintro/">wnintro</a></code>(7). </p>
