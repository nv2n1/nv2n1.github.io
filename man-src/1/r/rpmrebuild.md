---
title: "rpmrebuild(1)"
name: "rpmrebuild"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmrebuild/"
description: "rpmrebuild – a tool to build an rpm package from an installed package"
---

<h2>NAME</h2>
<p> rpmrebuild &#8211; a tool to build an rpm package from an installed package </p>
<h2>SYNOPSIS</h2>
<p> rpmrebuild [<i>option</i>] &lt;<i>packagename</i>&gt; </p>
<h2>DESCRIPTION</h2>
<p> rpmrebuild is a tool to build easily rpm package. it can be used to build an rpm file from an installed package (lost rpm) or to quickly make change to a package: just have your change on installed files and call rpmrebuild. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-5 &#8211;md5-compat-digest</code></p>
<dd> use rpm 4.4 compatible digest (md5)</p>
<dt><code>-a, &#8211;additional</code>=&lt;<i>flags</i>&gt;</p>
<dd> pass additional flags to <code>rpmbuild</code></p>
<dt><code>-b, &#8211;batch</code></p>
<dd> work in batch mode (no interactive query if files change)</p>
<dt><code>&#8211;cap-from-db (default)</code></p>
<dd> set files posix capabilities as saved in rpm database</p>
<dt><code>&#8211;cap-from-fs</code></p>
<dd> set files posix capabilities as installed files (do not force to original capabilities, saved in rpm database)</p>
<dt><code>-c, &#8211;comment-missing</code>=&lt;<i>yes</i>|<i>no</i>&gt;</p>
<dd> comment out in the specfile missing files. Default: <code>no</code>.</p>
<dt><code>-D, &#8211;define</code>=&lt;<i>defines</i>&gt;</p>
<dd> defines to be passed to rpmbuild.</p>
<dt><code>-d, &#8211;directory</code>=&lt;<i>directory</i>&gt;</p>
<dd> rpm package result will be written in <i>directory</i>.</p>
<dt><code>-e, &#8211;edit-spec</code></p>
<dd> alias to &#8211;edit-whole.</p>
<dt><code>-f, &#8211;filter</code>=&lt;<i>command</i>&gt;</p>
<dd> alias for <code>&#8211;change-spec-whole</code></p>
<dt><code>-h, &#8211;help</code></p>
<dd> output help information about all, but plugins option and exit.</p>
<dt><code>&#8211;help-plugins</code></p>
<dd> output help information about plugins options and exit.</p>
<dt><code>-i, &#8211;include</code>=&lt;<i>file</i>&gt;</p>
<dd> read more options from the file &#8216;file&#8217;.</p>
<dt><code>-I, &#8211;install&gt;</p>
<dd> install the created package</p>
<dt>-k, &#8211;keep-perm</p>
<dd> alias to &#8211;pug-from-fs</code></p>
<dt><code>-l, &#8211;list-plugin</code></p>
<dd> list installed plugins</p>
<dt><code>-m, &#8211;modify</code>=&lt;<i>command</i>&gt;</p>
<dd> alias to <code>&#8211;change-files</p>
<dt>-n, &#8211;notest-install </code></p>
<dd> do not test install at end of rpm building</p>
<dt><code>-p, &#8211;package</code></p>
<dd> use package file, not installed rpm (this option is like rpm&#8217;s -p option)</p>
<dt><code>&#8211;pug-from-db (default)</code></p>
<dd> set files permission, uid and gid as saved in rpm database</p>
<dt><code>&#8211;pug-from-fs</code></p>
<dd> keep installed files permission, uid and gid (do not force to original files permission, uid and gid saved in rpm database)</p>
<dt><code>-P, &#8211;autoprovide</code></p>
<dd> use rpm scripts to compute provides</p>
<dt><code>-R, &#8211;autorequire</code></p>
<dd> use rpm scripts to compute requires</p>
<dt><code>-r, &#8211;release</code>=&lt;<i>version</i>&gt;</p>
<dd> specify a release</p>
<dt><code>-s, &#8211;spec-only</code>=&lt;<i>specfile</i>&gt;</p>
<dd> do not rebuild package, only generate specfile. Can&#8217;t be used with <code>&#8211;change-files</code>.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> verbose output</p>
<dt><code>&#8211;debug</code></p>
<dd> for debugging purposes : do not remove temporary files at end of work</p>
<dt><code>-V, &#8211;version</code></p>
<dd> output version information and exit.</p>
<dt><code>-w, &#8211;warning</code></p>
<dd> display some warnings if it detects a potential problem (for example, spec file which contains filename with globbing char).</p>
<dt><code>-y, &#8211;verify</code>=&lt;<i>yes</i>|<i>no</i>&gt;</p>
<dd> Turn on/off package verifying before processing. Default: <code>yes</code>. Can be turn off to get better performance.</dl>
<p> PLUGINS OPTION </p>
<p> rpmrebuild use may be extended with plugins. Plugins are searched in <code>/usr/lib/rpmrebuild/plugins</code> and then in $PATH</p>
<dl>
<dt><code>&#8211;change-files</code>=&lt;<i>command</i>&gt;</p>
<dd> Invoke plugin which change package&#8217;s files. Note, that these files are copied before to the temporary location, so installed package&#8217;s files not changed.<br />
 Can&#8217;t be used with <code>&#8211;spec-only</code></dl>
<p> <code>&#8211;change-spec-whole</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-whole</p>
<dl>
<dt>
<dd> Invoke plugin or editor to change specfile.</dl>
<p> &#8211;change-spec-preamble</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-preamble </p>
<p> &#8211;change-spec-conflicts</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-conflicts </p>
<p> &#8211;change-spec-obsoletes</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-obsoletes </p>
<p> &#8211;change-spec-provides</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-provides </p>
<p> &#8211;change-spec-requires</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-requires </p>
<p> &#8211;change-spec-suggests</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-suggests </p>
<p> &#8211;change-spec-enhances</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-enhances </p>
<p> &#8211;change-spec-description</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-description </p>
<p> &#8211;change-spec-files</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-files </p>
<p> &#8211;change-spec-triggers</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-triggers </p>
<p> &#8211;change-spec-pre</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-pre </p>
<p> &#8211;change-spec-post</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-post </p>
<p> &#8211;change-spec-preun</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-preun </p>
<p> &#8211;change-spec-postun</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-postun </p>
<p> &#8211;change-spec-pretrans</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-postrans </p>
<p> &#8211;change-spec-postrans</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-postrans </p>
<p> &#8211;change-spec-verifyscript</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-verifyscript </p>
<p> &#8211;change-spec-changelog</code>=&lt;<i>command</i>&gt;<br />
 <code>&#8211;edit-changelog </p>
<dl>
<dt>
<dd> Invoke plugin or editor to change preamble, conflicts, obsoletes, provides, requires, description, files, triggers, preinstall, postinstall, preuninstall, postuninstall, verifyscript or changelog.<br />
 None of these options can be specified after &#8211;change-spec-whole</code> or <code>&#8211;edit-whole</code>. </p>
</dl>
<h2>INCLUDE FILES</h2>
<p> Any of the rpmrebuild&#8217;s LONG option can be specified on the command line or in the include file (file specified with -i/&#8211;include option). </p>
<p> Include files are also searched in the <code>/usr/lib/rpmrebuild/plugins</code> directory. </p>
<p> Include file has following syntax.</p>
<dl>
<dt><code>comments</code></p>
<dd> Any line begin with &#8216;#&#8217; or some number of whitespace and &#8216;#&#8217;.</p>
<dt><code>empty line</code></p>
<dd> empty line are ignored.</p>
<dt><code>option line</code></p>
<dd> option line is very similar to the option written on the command line. the limitation of the option line in the file are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>long option</p>
<dd> should be used ONLY long options WITHOUT leading &#8211;.</p>
<dt>option&#8217;s argument</p>
<dd> option&#8217;s argument should not be quoted.</p>
<dt>separator</p>
<dd> option&#8217;s argument should be separated from option by spaces or tabs, not by equal (&#8216;=&#8217;) sign.</p>
<dt>non-optional argument(s)</p>
<dd> package name (non-optional argument) shouldn&#8217;t be specified in the include file.</dl>
</dl>
</dl>
<p> For example, if command line looks like:</p>
<dl>
<dt>
<dd> rpmrebuild &#8211;change-files=&quot;pgm1 a b c&quot; &#8211;change-spec-pre=&quot;pgm2 bb&quot; pkg</dl>
<p> Then include file should be written like:</p>
<dl>
<dt>
<dd> change-files pgm1 a b c<br />
 change-spec-pre pgm2 bb
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.rpmmacros</code></p>
<dd> is used by rpm when building packages (macros)</p>
<dt><code>$RPMREBUILD_TMPDIR/work</code></p>
<dd> directory where rpmrebuild put temporary files. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>RPMREBUILD_TMPDIR</code></p>
<dd> Directory for temporal files. If not set ~/.tmp/rpmrebuild.$$ is used.</p>
<dt><code>RPMREBUILD_OPTS</code></p>
<dd> This is another way to pass options to rpmrebuild (to use with care). It allows to change the default options on a host. For example to activate the un_prelink plugin, just set RPMREBUILD_OPTS=&quot;&#8211;include un_prelink.plug&quot;</p>
<dt><code>VISUAL</code></p>
<dd> used to specify an editor for specfile. if not set <code>EDITOR</code> variable examined.</p>
<dt><code>EDITOR</code></p>
<dd> used to specify an editor for specfile. if not set <code>vi</code> used. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Build an rpm package as closed as possible to original one: </p>
<p> <code>rpmrebuild &#8211;batch package</code> </p>
<p> Build a modified package: </p>
<p> <code>rpmrebuild &#8211;keep-perm package</code> </p>
<p> Build a rpm from another rpm file: </p>
<p> <code>rpmrebuild &#8211;package &#8211;filter filter /usr/src/redhat/i386/package-i386.rpm</code> </p>
<p> rebuild and sign the bash package </p>
<p> <code>rpmrebuild &#8211;additional &quot;&#8211;sign&quot; bash</code> </p>
<p> Rebuild rpm as legacy (rpm[23]) package: </p>
<p> <code>rpmrebuild &#8211;additional &quot;&#8211;nodirtokens&quot; bash</code> </p>
<p> Specify generated rpm name: </p>
<p> <code>rpmrebuild &#8211;define &quot;_rpmfilename %%{NAME}.rpm&quot; bash</code> </p>
<p> Change package interactive </p>
<p> <code>rpmrebuild &#8211;package &#8211;change-files &quot;/bin/bash&quot; /some/place/bash.rpm</code> </p>
<p> Change package non-interactive </p>
<p> <code>rpmrebuild &#8211;package &#8211;change-files &quot;a.sh &amp;&amp; b.sh&quot; /some/place/bash.rpm</code> </p>
<p> if you have problem with rpm building, and if you know specfile syntax, you can also edit it: </p>
<p> <code>rpmrebuild &#8211;edit-whole package</code> </p>
<p> batch change of version tag </p>
<p> <code>rpmrebuild &#8211;change-spec-preamble=&#8217;sed -e &quot;s/^Version:.*/Version: YourVersion/&quot;&#8217; YourPackage</code> </p>
<h2>AUTHORS</h2>
<p> Eric Gerbier &lt;gerbier [at] users.sourceforge.net&gt;<br />
 Valery Reznic &lt;valery_reznic [at] users.sourceforge.net&gt;</p>
<dl>
<dt>See &lt;URL:<a rel="nofollow" href="http://rpmrebuild.sourceforge.net/">http://rpmrebuild.sourceforge.net/</a>&gt;.</p>
<dd>
</dl>
<h2>NOTES</h2>
<dl>
<dt>rpmrebuild can not reproduce exactly a package, so</p>
<dd>
 &#8211; md5 checksum will not match original ones.<br />
 &#8211; gpg or pgp signatures are lost</p>
<dt>packages which contains file with globbing characters (* .. ? ) will not build</p>
<dd>
</dl>
<h2>COPYRIGHT</h2>
<p> rpmrebuild is copyright (C) 2002 by Eric Gerbier.<br />
 this program is distributed under GNU General Public License<br />
 It is provided &quot;as is&quot;, without any express or implied warranties.<br />
 See the file COPYING for details. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-rpm/">rpm</a>(8), <a href="/docs/linux/man/8-rpmbuild/">rpmbuild</a>(8), <a href="/docs/linux/man/1-rpmrebuild_plugins/">rpmrebuild_plugins</a>(1), &#8216;man -k rrp&#8217; for plugins specific manpages. </p>
<h2>Index</h2>
