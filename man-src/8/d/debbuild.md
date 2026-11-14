---
title: "debbuild(8)"
name: "debbuild"
section: "8"
letter: "d"
url: "/docs/linux/man/8-debbuild/"
description: "debbuild — Build Debian-compatible .deb packages from RPM .spec files"
---

<p>debbuild — Build Debian-compatible .deb packages from RPM .spec files</p>
<h2>Synopsis</h2>
<pre> debbuild {-ba|-bb|-bp|-bc|-bi|-bl|-bs} [build-options] file.spec
 debbuild {-ta|-tb|-tp|-tc|-ti|-tl|-ts} [build-options] file.{tgz|zip|tar.{gz|bz2|xz|Z}}
 debbuild {-ra|-rb|-rp|-rc|-ri|-rl|-rs} [build-options] file.{.src.rpm|sdeb}
 debbuild {--rebuild|--recompile} file.{src.rpm|sdeb}
 debbuild --showpkgs
 debbuild --nobuild file.spec
 debbuild {--install|-i} foo.sdeb</pre>
<h2>Description</h2>
<p><code>debbuild</code> attempts to build Debian-friendly semi-native packages from <font SIZE="-1">RPM</font> spec files, RPM-friendly tarballs, and <font SIZE="-1">RPM</font> source packages (.src.rpm files). It accepts <i>most</i> of the options <code>rpmbuild</code> does, and should be able to interpret most spec files usefully. Perl modules should be handled via CPAN+dh-make-perl instead as it’s simpler than even tweaking a .spec template. </p>
<p> As far as possible, the command-line options are identical to those from <code>rpmbuild</code>, although several <code>rpmbuild</code> options are not supported: </p>
<pre> --clean
 --rmsource
 --rmspec
 --showrc
 --sign
 --target</pre>
<p>Some of these could probably be trivially added. Feel free to send me a patch. ;) </p>
<p> Complex spec files will most likely <i>not</i> work well, if at all. Rewrite them from scratch – you’ll have to make heavy modifications anyway. </p>
<p> If you see something you don’t like, mail me. Send a patch if you feel inspired. I don’t promise I’ll do anything other than say “Yup, that’s broken” or “Got your message”. </p>
<p> The source package container I invented for <code>debbuild</code>, the .sdeb file, can be installed with <tt>&quot;debbuild -i&quot;</tt> exactly the same way as a .src.rpm can be installed with <tt>&quot;rpm -i&quot;</tt>. Both will unpack the file and place the source(s) and .spec file in the appropriate places in <tt>%_topdir</tt>/SOURCES and <tt>%_topdir</tt>/SPECS respectively.</p>
<h2>Assumptions</h2>
<p>As with <code>rpmbuild</code>, <code>debbuild</code> makes some assumptions about your system.</p>
<dl>
<dt>&bull;</p>
<dd>Either you have rights to do as you please under /usr/src/debian, or you have created a file <i>~/.debmacros</i> containing a suitable “%_topdir” definition. </p>
<p> Both <code>rpmbuild</code> and <code>debbuild</code> require the directories %_topdir<code>/{</code><font SIZE="-1"><code>BUILD,SOURCES,SPECS</code></font><code>}</code>. However, where <code>rpmbuild</code> requires the %_topdir<code>/{</code><font SIZE="-1"><code>RPMS,SRPMS</code></font><code>}</code> directories, <code>debbuild</code> requires %_topdir<code>/{</code><font SIZE="-1"><code>DEBS,SDEBS</code></font><code>}</code> instead. Create them in advance; <i>some</i> subdirectories are created automatically as needed, but most are not.</p>
<dt>&bull;</p>
<dd><code>/var/tmp</code> must allow script execution – <code>rpmbuild</code> and <code>debbuild</code> both rely on creating and executing shell scripts for much of their functionality. By default, <code>debbuild</code> also creates install trees under <code>/var/tmp</code> – however this is (almost) entirely under the control of the package’s .spec file.</p>
<dt>&bull;</p>
<dd>If you wish to <code>&#8211;rebuild</code> a .src.rpm file, your %_topdir for both <code>debbuild</code> and <code>rpmbuild</code> must either match, or be suitably symlinked one direction or another so that both programs are effectively working in the same tree. (Or you could just manually wrestle files around your system.) </p>
<p> You could symlink <i>~/.rpmmacros</i> to <i>~/.debmacros</i> (or vice versa) and save yourself some hassle if you need to rebuild .src.rpm packages on a regular basis.</dl>
<h2>Errata</h2>
<p><code>debbuild</code> deliberately does a few things differently from <code>rpmbuild</code>.</p>
<h3>BuildArch or BuildArchitecture</h3>
<p><code>rpmbuild</code> takes the last BuildArch entry it finds in the .spec file, whatever it is, and runs with that for all packages. Debian’s repository system is fairly heavily designed around the assumption that a single source package may generate small binary (executable) packages for each arch, and large binary arch-all packages containing shared data. </p>
<p> <code>debbuild</code> allows this by using the architecture specified by (in order of preference):</p>
<dl>
<dt>&bull;</p>
<dd>Host architecture</p>
<dt>&bull;</p>
<dd>BuildArch specified in .spec file preamble</p>
<dt>&bull;</p>
<dd>“Last specified” BuildArch for packages with several subpackages</p>
<dt>&bull;</p>
<dd>BuildArch specified in the <tt>%package</tt> section for that subpackage</dl>
<h3>Finding out what packages should be built (&#8211;showpkgs)</h3>
<p><code>rpmbuild</code> does not include any convenient method I know of to list the packages a spec file will produce. Since I needed this ability for another tool, I added it. </p>
<p> It requires the .spec file for the package, and produces a list of full package filenames (without path data) that would be generated by one of <code>&#8211;rebuild</code>, <code>-ta</code>, <code>-tb</code>, <code>-ra</code>, <code>-rb</code>, <code>-ba</code>, or <code>-bb</code>. This includes the .sdeb source package.</p>
<h2>Author</h2>
<p><code>debbuild</code> was written by Kris Deugau &lt;kdeugau [at] deepnet.cx&gt;. The present version was developed by Andreas Scherer &lt;<a rel="nofollow" href="http://ascherer.github.io">http://ascherer.github.io</a>&gt; and is available at &lt;<a href="http://github.com/ascherer/debbuild">http://github.com/ascherer/debbuild</a>&gt;.</p>
<h2>Bugs</h2>
<p>Funky Things Happen if you forget a command-line option or two. I’ve been too lazy to bother fixing this. </p>
<p> Many macro expansions are supported, some are incompletely supported, some not at all. </p>
<p> The generated scriptlets don’t quite match those from <code>rpmbuild</code> exactly. There are extra environment variables and preprocessing that I haven&#8217;t needed (yet). </p>
<p> Dcumentation, such as it is, will likely remain perpetually out of date (in which way it follows in RPM’s tradition). </p>
<p> <tt>%_topdir</tt> and the five “working” directories under <tt>%_topdir</tt> could arguably be created by <code>debbuild</code>. However, <code>rpmbuild</code> doesn&#8217;t create these directories either.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-rpm/">rpm</a></i>(8), <i><a href="/docs/linux/man/8-rpmbuild/">rpmbuild</a></i>(8), and pretty much any document describing how to write a .spec file. </p>
