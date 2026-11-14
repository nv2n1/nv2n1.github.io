---
title: "changestool(1)"
name: "changestool"
section: "1"
letter: "c"
url: "/docs/linux/man/1-changestool/"
description: "changestool – verify, dump, modify, create or fix Debian .changes files"
---

<h2>NAME</h2>
<p> changestool &#8211; verify, dump, modify, create or fix Debian .changes files</p>
<h2>SYNOPSIS</h2>
<p> <code>changestool &#8211;help</code> </p>
<p> <code>changestool</code> [ <i>options</i> ] <i>.changes-filename</i> <i>command</i> [ <i>per-command-arguments</i> ]</p>
<h2>DESCRIPTION</h2>
<p> changestool is a little program to operate on Debian .changes files, as they are produced by <code><a href="/docs/linux/man/1-dpkg-genchanges/">dpkg-genchanges</a></code>(1) and used to feed built Debian packages into Debian repository managers like <code><a href="/docs/linux/man/1-reprepro/">reprepro</a></code>(1) or <code>dak</code>. </p>
<h2>EXAMPLES</h2>
<p> <code>changestool </code><i>bloat.changes</i> setdistribution <i>local</i><br />
 will modify the <code>Distribution:</code> header inside <i>bloat.changes</i> to say <i>local</i> instead of what was there before. </p>
<p> <code>changestool </code><i>reprepro_1.2.0-1.local_sparc.changes</i> includeallsources<br />
 will modify the given file to also list <code>.orig.tar.gz</code> it does not list because you forgot to build it with <code>dpkg-buildpackage -sa</code>. </p>
<p> <code>changestool </code><i>blafasel_1.0_abacus.changes</i> updatechecksums<br />
 will update the md5sums to those of the files referenced by this file. (So one can do quick&#8217;n&#8217;dirty corrections to them before uploading to your private package repository) </p>
<p> <code>changestool &#8211;create </code><i>test.changes</i> add <i>bla_1-1.dsc bla_1-1_abacus.deb</i><br />
 will add the specified files (format detected by filename, use <code>adddeb</code> or <code>adddsc</code> if you know it). If the file <i>test.changes</i> does not exist yet, a minimal one will be generated. Though that might be too minimal for most direct uses. </p>
<h2>GLOBAL OPTIONS</h2>
<p> Options can be specified before the command. Each affects a different subset of commands and is ignored by other commands.</p>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd> Displays a short list of options and commands with description.</p>
<dt><code>-o &#8211;outputdir </code><i>dir</i></p>
<dd> Not yet implemented.</p>
<dt><code>-s &#8211;searchpath </code><i>path</i></p>
<dd> A colon-separated list of directories to search for files if they are not found in the directory of the .changes file.</p>
<dt><code>&#8211;create</code></p>
<dd> Flag for the commands starting with <code>add</code> to create the <code>.changes</code> file if it does not yet exists.</p>
<dt><code>&#8211;create-with-all-fields</code></p>
<dd> Flag for the commands starting with <code>add</code> to create the <code>.changes</code> file if it does not yet exists. Unlike <code>&#8211;create</code>, this creates more fields to make things like dupload happier. Currently that creates fake <code>Urgency</code> and <code>Changes</code> fields.</p>
<dt><code>&#8211;unlzma </code><i>command</i></p>
<dd> External uncompressor used to uncompress lzma files to look into .diff.lzma, .tar.lzma or .tar.lzma within .debs.</p>
<dt><code>&#8211;unxz </code><i>command</i></p>
<dd> External uncompressor used to uncompress xz files to look into .diff.xz, .tar.xz or .tar.xz within .debs.</p>
<dt><code>&#8211;lunzip </code><i>command</i></p>
<dd> External uncompressor used to uncompress lzip files to look into .diff.lz, .tar.lz or .tar.lz within .debs.</p>
<dt><code>&#8211;bunzip2 </code><i>command</i></p>
<dd> External uncompressor used to uncompress bz2 when compiled without libbz2.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>verify</code></p>
<dd> Check for inconsistencies in the specified <code>.changes</code> file and the files referenced by it.</p>
<dt><code>updatechecksums</code> [ <i>filename</i> ]</p>
<dd> Update the checksum (md5sum and size) information within the specified <code>.changes</code> file and all <code>.dsc</code> files referenced by it. Without arguments, all files will be updated. To only update specific files, give their filename (without path) as arguments.</p>
<dt><code>setdistribution</code> [ <i>distributions</i> ]</p>
<dd> Change the <code>Distribution:</code> header to list the remaining arguments.</p>
<dt><code>includeallsources</code> [ <i>filename</i> ]</p>
<dd> List all files referenced by <code>.dsc</code> files mentioned in the <code>.changes</code> file in said file. Without arguments, all missing files will be included. To only include specific files, give their filename (without path) as arguments. </p>
<p> Take a look at the description of <code>-si</code>, <code>-sa</code> and <code>-sd</code> in the manpage of <code>dpkg-genchanges</code>/<code>dpkg-buildpackage</code> how to avoid to have to do this at all. </p>
<p> Note that while <code>reprepro</code> will just ignore files listed in a <code>.changes</code> file when it already has the file with the same size and md5sum, <code>dak</code> might choke in that case.</p>
<dt><code>adddeb </code><i>filenames</i></p>
<dd> Add the <code>.deb</code> and <code>.udeb</code> files specified by their filenames to the <code>.changes</code> file. Filenames without a slash will be searched in the current directory, the directory the changes file resides in and in the directories specified by the <code>&#8211;searchpath</code>.</p>
<dt><code>adddsc </code><i>filenames</i></p>
<dd> Add the <code>.dsc</code> files specified by their filenames to the <code>.changes</code> file. Filenames without a slash will be searched in the the current directory, in the directory the changes file resides in and in the directories specified by the <code>&#8211;searchpath</code>.</p>
<dt><code>addrawfile </code><i>filenames</i></p>
<dd> Add the files specified by their filenames to the <code>.changes</code> file. Filenames without a slash will be searched in the current directory, in the directory the changes file resides in and in the directories specified by the <code>&#8211;searchpath</code>.</p>
<dt><code>add </code><i>filenames</i></p>
<dd> Behave like <code>adddsc</code> for filenames ending in <code>.dsc</code>, like <code>adddeb</code> for filenames ending in <code>.deb</code> or <code>.udeb</code>, and like <code>addrawfile</code> for all other filenames</p>
<dt><code>dumbremove </code><i>filenames</i></p>
<dd> Remove the specified files from the .changes file. No other fields (Architectures, Binaries, &#8230;) are updated and no related files is removed. Just the given files (which must be specified without any <code>/</code>) are no longer listen in the .changes file (and only no longer in the changes file). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-reprepro/">reprepro</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-genchanges/">dpkg-genchanges</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1), <code><a href="/docs/linux/man/1-md5sum/">md5sum</a></code>(1).</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs or wishlist requests the Debian BTS (e.g. by using <code>reportbug reperepro</code>) or directly to &lt;brlink [at] debian.org&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006-2009 Bernhard R. Link<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
