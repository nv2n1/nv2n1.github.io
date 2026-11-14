---
title: "rpmrebuild_plugins(1)"
name: "rpmrebuild_plugins"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmrebuild_plugins/"
description: "rpmrebuild_plugins – is an engine to expand rpmrebuild functionality."
---

<h2>NAME</h2>
<p> rpmrebuild_plugins &#8211; is an engine to expand <code>rpmrebuild</code> functionality.</p>
<h2>SYNOPSIS</h2>
<p> rpmrebuild [<i>non-plugins-option</i>] [<i>plugins-option</i>] &lt;<i>packagename</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>rpmrebuild</code> itself try to do it&#8217;s best to reconstruct rpm package as close to original as possible. </p>
<p> rpmrebuild plugins&#8217;s aim is opposite &#8211; somehow change rebuilded rpm.</p>
<h2>RPMREBUILD WITHOUT PLUGINS</h2>
<p> Without plugins process of rpm rebuilding looks like:</p>
<dl>
<dt><code>query</code> &#8211;</p>
<dd> Query rpm to be rebuilded for the different pieces of information.</p>
<dt><code>concatenate</code> &#8211;</p>
<dd> Create from these pieces specfile.</p>
<dt><code>build</code> &#8211;</p>
<dd> Use specfile to build rpm.</dl>
<h2>RPMREBUILD WITH PLUGINS</h2>
<p> With plugins process of rpm rebuilding looks like:</p>
<dl>
<dt><code>query</code> &#8211;</p>
<dd> Query rpm to be rebuilded for the different pieces of information.</p>
<dt><code>change parts</code> &#8211;</p>
<dd> Change parts of the spec created by query.</p>
<dt><code>concatenate</code> &#8211;</p>
<dd> Create specfile from the pieces.</p>
<dt><code>change whole</code> &#8211;</p>
<dd> Change concatenated specfile.</p>
<dt><code>build</code> &#8211;</p>
<dd> use specfile to build rpm.</dl>
<h2>SPECFILE PIECES</h2>
<p> Query&quot; queries for the following information:</p>
<dl>
<dt>
<dd>
 preamble<br />
 conflicts<br />
 obsoletes<br />
 provides<br />
 requires<br />
 description<br />
 files<br />
 triggers<br />
 pre<br />
 post<br />
 preun<br />
 postun<br />
 verifyscript<br />
 changelog</dl>
<h2>SPECFILE CONCATENATION</h2>
<p> Concatenate&quot; create &#8216;full&#8217; specfile from the pieces. It do following: </p>
<p> add AutoReq / AutoProv tags<br />
 add BuildRoot tag<br />
 add some defines to adjust rpm&#8217;s behaviour.<br />
 double all &#8216;%&#8217; &#8211; it&#8217;ll prevent rpm from attempting expand %something as macro.<br />
 add &#8216;%description&#8217; before description<br />
 add &#8216;%files&#8217; before files<br />
 add &#8216;%changelog&#8217; before changelog</p>
<h2>PLUGINS TYPES</h2>
<p> rpm building (or rebuilding) process has two inputs: specfile and package&#8217;s files under buildroot directory. So, there are two plugins type:</p>
<dl>
<dt>&#8211; for specfile modification (exemple : demo.plug).</p>
<dd>
<dt>&#8211; for files (under buildroot) modification (exemple : demofiles.plug).</p>
<dd></dl>
<h2>PLUGIN&#8217;S INTERFACE</h2>
<p> Plugins are executed AFTER rpm package is queried and BEFORE new package is rebuilded in the order specified on the command line.</p>
<dl>
<dt>Exit status</p>
<dd> Any plugin should exit with status 0 on success, and any other value on failure. Failed plugin will immediately terminate whole rpmrebuild.</p>
<dt>Environment variables</p>
<dd> all plugins get following environment variables:</p>
<dl>
<dt>
<dd>
<dl>
<dt>RPMREBUILD_TMPDIR</p>
<dd> directory for plugin&#8217;s temporaries files. plugin no need remove this directory &#8211; rpmrebuild will care.</p>
<dt>RPMREBUILD_PLUGINS_DIR</p>
<dd> directory with plugins.</p>
<dt>RPMREBUILD_COMMENT_MISSING</p>
<dd> if &#8216;yes&#8217; missing files commented in the &#8216;files&#8217; part of specfile</p>
<dt>RPMREBUILD_PUG_FROM_FS</p>
<dd> if &#8216;yes&#8217; permission owner and group in the part file were taken from filesystem, otherwise &#8211; from rpm&#8217;s database.</p>
<dt>RPMREBUILD_WARNING</p>
<dd> if &#8216;yes&#8217; rpmrebuild will produce warning for filenames with glob characters.</p>
<dt>PATH</p>
<dd> This variable is set to $RPMREBUILD_PLUGINS_DIR:$PATH</p>
<dt>LONG_OPTION</p>
<dd> Contains long option (without &#8211;) which was used to invoke plugin.</p>
<dt>RPM_BUILD_ROOT</p>
<dd> For plugins modifying files under buildroot set to buildroot. For other plugins &#8211; empty.</dl>
</dl>
<dt>stdin and stdout</p>
<dd> Plugins for specfile modification (i.e., invoked with &#8211;spec-hange-*)got &quot;source&quot; spec file from stdin and have to write resulting spec file to stdout.</dl>
<h2>PLUGIN&#8217;S EXAMPLES</h2>
<p> Some plugins are given as examples :</p>
<dl>
<dt>demofiles.plug (change-files) : a &quot;dummy&quot; plugin to show what can be done with a file plugin</p>
<dd>
<dt>demo.plug (change-spec-*) : a &quot;dummy&quot; plugin to show how spec plugins work</p>
<dd>
<dt>uniq.plug (change-spec) : a very simple &quot;real&quot; plugin to sort and clean duplicate spec lines</p>
<dd>
<dt>file2pacDep.plug (change-spec-requires) : a &quot;real&quot; plugin to convert file dependencies to package dependencies</p>
<dd>
<dt>nodoc.plug (change-spec-files): a &quot;real&quot; plugin to remove documentation from a package</p>
<dd>
<dt>set_tag.plug (change-spec-preamble) : a &quot;real&quot; plugin to change a tag in spec file</p>
<dd>
<dt>unset_tag.plug (change-spec-preamble) : a &quot;real&quot; plugin to comment a tag in spec file</p>
<dd></dl>
<h2>PLUGINS&#8217; MANPAGES FILENAME CONVENTION</h2>
<p> If you are going to write plugin (and manpage for it) it&#8217;s strongly recommended than manpage&#8217;s file looks like <code>name.1rrp</code> &#8211; this way command <code>&#8216;man -k rrp&#8217;</code> will provide list of all rpmrebuild&#8217;s plugins installed. Please note, that <code>makewhatis</code> should be run before newly installed manpages will be available for <code>&#8216;man -k rrp&#8217; </code></p>
<h2>AUTHORS</h2>
<p> Eric Gerbier &lt;gerbier [at] users.sourceforge.net&gt;<br />
 Valery Reznic &lt;valery_reznic [at] users.sourceforge.net&gt;</p>
<dl>
<dt>See &lt;URL:<a rel="nofollow" href="http://rpmrebuild.sourceforge.net/">http://rpmrebuild.sourceforge.net/</a>&gt;.</p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-rpm/">rpm</a>(8), <a href="/docs/linux/man/8-rpmbuild/">rpmbuild</a>(8), <a href="/docs/linux/man/1-rpmrebuild/">rpmrebuild</a>(1), <a href="/docs/linux/man/1-demofiles-plug/">demofiles.plug</a>(1), <a href="/docs/linux/man/1-demo-plug/">demo.plug</a>(1), <a href="/docs/linux/man/1-nodoc-plug/">nodoc.plug</a>(1), <a href="/docs/linux/man/1-uniq-plug/">uniq.plug</a>(1), <a href="/docs/linux/man/1-file2pacdep-plug/">file2pacDep.plug</a>(1), <a href="/docs/linux/man/1-set_tag-plug/">set_tag.plug</a>(1), <a href="/docs/linux/man/1-unset_tag-plug/">unset_tag.plug</a>(1)<br />
&nbsp;<wbr>&#8216;man -k rrp&#8217;&nbsp;<wbr>for plugins specific manpages </p>
<h2>Index</h2>
