---
title: "ldconfig(8)"
name: "ldconfig"
section: "8"
letter: "l"
url: "/docs/linux/man/8-ldconfig/"
description: "ldconfig – configure dynamic linker run-time bindings"
---

<p>ldconfig &#8211; configure dynamic linker run-time bindings</p>
<h2>Synopsis</h2>
<p><code>/sbin/ldconfig</code> [<code>-nNvXV</code>] [<code>-f</code> <i>conf</i>] [<code>-C</code> <i>cache</i>] [<code>-r</code> <i>root</i>] <i>directory</i>&#8230; </p>
<p> <code>/sbin/ldconfig</code> <code>-l</code> [<code>-v</code>] <i>library</i>&#8230; </p>
<p> <code>/sbin/ldconfig</code> <code>-p</code></p>
<h2>Description</h2>
<p><code>ldconfig</code> creates the necessary links and cache to the most recent shared libraries found in the directories specified on the command line, in the file <i>/etc/ld.so.conf</i>, and in the trusted directories, <i>/lib</i> and <i>/usr/lib</i> (on some 64-bit architectures such as x86-64, <i>/lib</i> and <i>/usr/lib</i> are the trusted directories for 32-bit libraries, while <i>/lib64</i> and <i>/usr/lib64</i> are used for 64-bit libraries). </p>
<p> The cache is used by the run-time linker, <i>ld.so</i> or <i>ld-linux.so</i>. <code>ldconfig</code> checks the header and filenames of the libraries it encounters when determining which versions should have their links updated. </p>
<p> <code>ldconfig</code> will attempt to deduce the type of ELF libraries (i.e., libc5 or libc6/glibc) based on what C libraries, if any, the library was linked against. </p>
<p> Some existing libraries do not contain enough information to allow the deduction of their type. Therefore, the <i>/etc/ld.so.conf</i> file format allows the specification of an expected type. This is used <i>only</i> for those ELF libraries which we can not work out. The format is &quot;dirname=TYPE&quot;, where TYPE can be libc4, libc5, or libc6. (This syntax also works on the command line.) Spaces are <i>not</i> allowed. Also see the <code>-p</code> option. <code>ldconfig</code> should normally be run by the superuser as it may require write permission on some root owned directories and files. </p>
<p> Note that <code>ldconfig</code> will only look at files that are named <i>lib*.so*</i> (for regular shared objects) or <i>ld-*.so*</i> (for the dynamic loader itself). Other files will be ignored. Also, <code>ldconfig</code> expects a certain pattern to how the symlinks are set up, like this example, where the middle file (<code>libfoo.so.1</code> here) is the SONAME for the library: </p>
<p> libfoo.so -&gt; libfoo.so.1 -&gt; libfoo.so.1.12 </p>
<p> Failure to follow this pattern may result in compatibility issues after an upgrade.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code> <i>fmt</i>, <code>&#8211;format=</code><i>fmt</i></p>
<dd>(Since glibc 2.2) Cache format to use: <i>old</i>, <i>new</i>, or <i>compat</i>. Since glibc 2.32, the default is <i>new</i>. Before that, it was <i>compat</i>.</p>
<dt><code>-C </code><i>cache</i></p>
<dd>Use <i>cache</i> instead of <i>/etc/ld.so.cache</i>.</p>
<dt><code>-f </code><i>conf</i></p>
<dd>Use <i>conf</i> instead of <i>/etc/ld.so.conf</i>.</p>
<dt><code>-i</code>, <code>&#8211;ignore-aux-cache</code></p>
<dd>(Since glibc 2.7) Ignore auxiliary cache file.</p>
<dt><code>-l</code></p>
<dd>(Since glibc 2.2) Library mode. Manually link individual libraries. Intended for use by experts only.</p>
<dt><code>-n</code></p>
<dd>Process only the directories specified on the command line. Don&#8217;t process the trusted directories, nor those specified in <i>/etc/ld.so.conf</i>. Implies <code>-N</code>.</p>
<dt><code>-N</code></p>
<dd>Don&#8217;t rebuild the cache. Unless <code>-X</code> is also specified, links are still updated.</p>
<dt><code>-p</code>, <code>&#8211;print-cache</code></p>
<dd>Print the lists of directories and candidate libraries stored in the current cache.</p>
<dt><code>-r </code><i>root</i></p>
<dd>Change to and use <i>root</i> as the root directory.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose mode. Print current version number, the name of each directory as it is scanned, and any links that are created. Overrides quiet mode.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print program version.</p>
<dt><code>-X</code></p>
<dd>Don&#8217;t update links. Unless <code>-N</code> is also specified, the cache is still rebuilt.</dl>
<h2>Files</h2>
<dl>
<dt><i>/lib/ld.so</i></p>
<dd>Run-time linker/loader.</p>
<dt><i>/etc/ld.so.conf</i></p>
<dd>File containing a list of directories, one per line, in which to search for libraries.</p>
<dt><i>/etc/ld.so.cache</i></p>
<dd>File containing an ordered list of libraries found in the directories specified in <i>/etc/ld.so.conf</i>, as well as those found in the trusted directories.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
