---
title: "rpmbuild(8)"
name: "rpmbuild"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpmbuild/"
description: "rpmbuild – Build RPM Package(s)"
---

<p>rpmbuild &#8211; Build RPM Package(s)</p>
<h2>Synopsis</h2>
<h3>Building Packages:</h3>
<p><code>rpmbuild</code> {<code>-ba|-bb|-bp|-bc|-bi|-bl|-bs</code>} [<code>rpmbuild-options</code>] <i>SPECFILE</i><i> &#8230;</i> <code>rpmbuild</code> {<code>-ta|-tb|-tp|-tc|-ti|-tl|-ts</code>} [<code>rpmbuild-options</code>] <i>TARBALL</i><i> &#8230;</i> <code>rpmbuild</code> {<code>&#8211;rebuild|&#8211;recompile</code>} <i>SOURCEPKG</i><i> &#8230;</i></p>
<h3>Miscellaneous:</h3>
<p><code>rpmbuild</code> <code>&#8211;showrc</code></p>
<h3>rpmbuild-options</h3>
<p>&nbsp;<wbr>[<code>&#8211;buildroot&nbsp;<wbr></code><i>DIRECTORY</i>]&nbsp;<wbr>[<code>&#8211;clean</code>]&nbsp;<wbr>[<code>&#8211;nobuild</code>]<br />
&nbsp;<wbr>[<code>&#8211;rmsource</code>]&nbsp;<wbr>[<code>&#8211;rmspec</code>]&nbsp;<wbr>[<code>&#8211;short-circuit</code>]<br />
&nbsp;<wbr>[<code>&#8211;noclean</code>]&nbsp;<wbr>[<code>&#8211;nocheck</code>]<br />
&nbsp;<wbr>[<code>&#8211;target&nbsp;<wbr></code><i>PLATFORM</i>] </p>
<h2>Description</h2>
<p><code>rpmbuild</code> is used to build both binary and source software packages. A <code>package</code> consists of an archive of files and meta-data used to install and erase the archive files. The meta-data includes helper scripts, file attributes, and descriptive information about the package. <code>Packages</code> come in two varieties: binary packages, used to encapsulate software to be installed, and source packages, containing the source code and recipe necessary to produce binary packages. </p>
<p> One of the following basic modes must be selected: <code>Build Package</code>, <code>Build Package from Tarball</code>, <code>Recompile Package</code>, <code>Show Configuration</code>.</p>
<h3>General Options</h3>
<p>These options can be used in all the different modes.</p>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd>Print a longer usage message then normal.</p>
<dt><code>&#8211;version</code></p>
<dd>Print a single line containing the version number of <code>rpm</code> being used.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Print as little as possible &#8211; normally only error messages will be displayed.</p>
<dt><code>-v</code></p>
<dd>Print verbose information &#8211; normally routine progress messages will be displayed.</p>
<dt><code>-vv</code></p>
<dd>Print lots of ugly debugging information.</p>
<dt><code>&#8211;rcfile </code><i>FILELIST</i></p>
<dd>Each of the files in the colon separated <i>FILELIST</i> is read sequentially by <code>rpm</code> for configuration information. Only the first file in the list must exist, and tildes will be expanded to the value of <code>$HOME</code>. The default <i>FILELIST</i> is <i>/usr/lib/rpm/rpmrc</i>:<i>/usr/lib/rpm/redhat/rpmrc</i>:<i>/etc/rpmrc</i>:<i>~/.rpmrc</i>.</p>
<dt><code>&#8211;pipe </code><i>CMD</i></p>
<dd>Pipes the output of <code>rpm</code> to the command <i>CMD</i>.</p>
<dt><code>&#8211;dbpath </code><i>DIRECTORY</i></p>
<dd>Use the database in <i>DIRECTORY</i> rather than the default path <i>/var/lib/rpm</i></p>
<dt><code>&#8211;root </code><i>DIRECTORY</i></p>
<dd>Use the file system tree rooted at <i>DIRECTORY</i> for all operations. Note that this means the database within <i>DIRECTORY</i> will be used for dependency checks and any scriptlet(s) (e.g. <code>%post</code> if installing, or <code>%prep</code> if building, a package) will be run after a <a href="/docs/linux/man/2-chroot/">chroot</a>(2) to <i>DIRECTORY</i>.</p>
<dt><code>-D, &#8211;define=&#8217;</code><i>MACRO EXPR</i><code>&#8216;</code></p>
<dd>Defines <i>MACRO</i> with value <i>EXPR</i>.</dl>
<h3>Build Options</h3>
<p>The general form of an rpm build command is </p>
<p> <code>rpmbuild</code> <code>-b</code><i>STAGE</i><code>|-t</code><i>STAGE</i> [ <code> rpmbuild-options </code> ] <i>FILE</i><i> &#8230;</i> </p>
<p> The argument used is <code>-b</code> if a spec file is being used to build the package and <code>-t</code> if <code>rpmbuild</code> should look inside of a (possibly compressed) tar file for the spec file to use. After the first argument, the next character (<i>STAGE</i>) specifies the stages of building and packaging to be done and is one of:</p>
<dl>
<dt><code>-ba</code></p>
<dd>Build binary and source packages (after doing the %prep, %build, and %install stages).</p>
<dt><code>-bb</code></p>
<dd>Build a binary package (after doing the %prep, %build, and %install stages).</p>
<dt><code>-bp</code></p>
<dd>Executes the &quot;%prep&quot; stage from the spec file. Normally this involves unpacking the sources and applying any patches.</p>
<dt><code>-bc</code></p>
<dd>Do the &quot;%build&quot; stage from the spec file (after doing the %prep stage). This generally involves the equivalent of a &quot;make&quot;.</p>
<dt><code>-bi</code></p>
<dd>Do the &quot;%install&quot; stage from the spec file (after doing the %prep and %build stages). This generally involves the equivalent of a &quot;make install&quot;.</p>
<dt><code>-bl</code></p>
<dd>Do a &quot;list check&quot;. The &quot;%files&quot; section from the spec file is macro expanded, and checks are made to verify that each file exists.</p>
<dt><code>-bs</code></p>
<dd>Build just the source package.</dl>
<p> The following options may also be used:</p>
<dl>
<dt><code>&#8211;buildroot </code><i>DIRECTORY</i></p>
<dd>When building a package, override the BuildRoot tag with directory <i>DIRECTORY</i>.</p>
<dt><code>&#8211;clean</code></p>
<dd>Remove the build tree after the packages are made.</p>
<dt><code>&#8211;nobuild</code></p>
<dd>Do not execute any build stages. Useful for testing out spec files.</p>
<dt><code>&#8211;noclean</code></p>
<dd>Do not execute %clean build stage even if present in spec.</p>
<dt><code>&#8211;nocheck</code></p>
<dd>Do not execute %check build stage even if present in spec.</p>
<dt><code>&#8211;nodeps</code></p>
<dd>Do not verify build dependencies.</p>
<dt><code>&#8211;rmsource</code></p>
<dd>Remove the sources after the build (may also be used standalone, e.g. &quot;<code>rpmbuild</code> <code>&#8211;rmsource foo.spec</code>&quot;).</p>
<dt><code>&#8211;rmspec</code></p>
<dd>Remove the spec file after the build (may also be used standalone, eg. &quot;<code>rpmbuild</code> <code>&#8211;rmspec foo.spec</code>&quot;).</p>
<dt><code>&#8211;short-circuit</code></p>
<dd>Skip straight to specified stage (i.e., skip all stages leading up to the specified stage). Only valid with <code>-bc</code>, <code>-bi</code>, and <code>-bb</code>. Useful for local testing only. Packages built this way will be marked with an unsatisfiable dependency to prevent their accidental use.</p>
<dt><code>&#8211;target </code><i>PLATFORM</i></p>
<dd>When building the package, interpret <i>PLATFORM</i> as <code>arch-vendor-os</code> and set the macros <code>%_target</code>, <code>%_target_cpu</code>, and <code>%_target_os</code> accordingly.</dl>
<h3>Rebuild And Recompile Options</h3>
<p>There are two other ways to invoke building with rpm: </p>
<p> <code>rpmbuild</code> <code>&#8211;rebuild|&#8211;recompile</code> <i>SOURCEPKG</i><i> &#8230;</i> </p>
<p> When invoked this way, <code>rpmbuild</code> installs the named source package, and does a prep, compile and install. In addition, <code>&#8211;rebuild</code> builds a new binary package. When the build has completed, the build directory is removed (as in <code>&#8211;clean</code>) and the the sources and spec file for the package are removed.</p>
<h3>Showrc</h3>
<p>The command </p>
<p> <code>rpmbuild</code> <code>&#8211;showrc</code> </p>
<p> shows the values <code>rpmbuild</code> will use for all of the options are currently set in <i>rpmrc</i> and <i>macros</i> configuration file(s).</p>
<h2>Files</h2>
<h3>rpmrc Configuration</h3>
<pre><i>/usr/lib/rpm/rpmrc</i>
<i>/usr/lib/rpm/redhat/rpmrc</i>
<i>/etc/rpmrc</i>
<i>~/.rpmrc</i></pre>
<h3>Macro Configuration</h3>
<pre><i>/usr/lib/rpm/macros</i>
<i>/usr/lib/rpm/redhat/macros</i>
<i>/etc/rpm/macros</i>
<i>~/.rpmmacros</i></pre>
<h3>Temporary</h3>
<p><i>/var/tmp/rpm*</i></p>
<h2>See Also</h2>
<pre><code><a href="//www.systutorials.com/docs/linux/man/1-gendiff/">gendiff</a></code>(1),
<code><a href="//www.systutorials.com/docs/linux/man/3-popt/">popt</a></code>(3),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm/">rpm</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpm2cpio/">rpm2cpio</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmkeys/">rpmkeys</a></code>(8)
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmspec/">rpmspec</a></code>(8),
<code><a href="//www.systutorials.com/docs/linux/man/8-rpmsign/">rpmsign</a></code>(8),</pre>
<p><code>rpmbuild &#8211;help</code> &#8211; as rpm supports customizing the options via popt aliases it&#8217;s impossible to guarantee that what&#8217;s described in the manual matches what&#8217;s available. </p>
<p> <code><a rel="nofollow" href="http://www.rpm.org/">http://www.rpm.org/</a> &lt;URL:<a href="http://www.rpm.org/">http://www.rpm.org/</a>&gt; </code></p>
<h2>Authors</h2>
<pre>Marc Ewing &lt;marc [at] redhat.com&gt;
Jeff Johnson &lt;jbj [at] redhat.com&gt;
Erik Troan &lt;ewt [at] redhat.com&gt;</pre>
