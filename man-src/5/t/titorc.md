---
title: "titorc(5)"
name: "titorc"
section: "5"
letter: "t"
url: "/docs/linux/man/5-titorc/"
---

titorc - A user specific settings file for `tito`.

<h2>Synopsis</h2>

None

<h2>Description</h2>

User preferences can optionally be stored: 

 ~/.titorc

<h2>Options</h2>

KOJI_OPTIONS
<dl><dd>Specify strings of options, which is passed to koji on commandline when you use KojiReleaser. For example: 

<dl><dd><pre>KOJI_OPTIONS=-c ~/.koji/katello-config build --nowait</pre></dl></dl>
 

 NO_AUTO_INSTALL
<dl><dd>Specify list of packages (separated by space), which should NOT be installed, when tito is run with -i option.</dl>
 

 RPMBUILD_BASEDIR
<dl><dd>Specifies a base directory for temp files, tarballs, and RPMs. If defined, and if the directory exists, tito will automatically create subdirectories as needed for <a HREF="/docs/linux/man/8-rpmbuild/">rpmbuild</a>(8). Can be overridden on the fly with -o. The default output directory is /tmp/tito.</dl>
 

 HIDE_EMAIL
<dl><dd>If set to something other than 0, your email address will not be used in changelog entries. I.e. instead of 

<dl><dd>&bull; Tue Feb 11 2011 Miroslav Suchy &lt;msuchy [at] redhat.com&gt; 0.3.0-2 You will get:</dl><dl><dd>&bull; Tue Feb 11 2011 Miroslav Suchy 0.3.0-2</dl></dl>
 

 RHPKG_USER, FEDPKG_USER
<dl><dd>By default this is the UNIX user running the command. Overriding it will run all rhpkg/fedpkg commands with --user $RHPKG_USER/FEDPKG_USER</dl>
 

 COLOR
<dl><dd>Set to <i>0</i> or <i>False</i> to disable colored output.</dl>
 

 MEAD_SCM_USERNAME
<dl><dd>The username to use when pushing the repository MEAD is going to build from. If this value is unset, the MEAD releaser will default to using the name of the current user.</dl>
 

 COPR_REMOTE_LOCATION
<dl><dd>URL that Tito will push SRPMs to for Copr to use.</dl>

<h2>Example</h2>

KOJI_OPTIONS=-c ~/.koji/spacewalkproject.org-config build --nowait <pre><code># Default Location to write temp files, tarballs and rpms to:
RPMBUILD_BASEDIR = &quot;/tmp/tito&quot;</code></pre>

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-tito/">tito</a>(8)

<h2>Authors</h2>

Devan Goodwin &lt;dgoodwin [at] rm-rf.ca&gt; 

 James Bowes &lt;jbowes [at] repl.ca&gt; 

 Jan Pazdziora 

 Jesus M Rodriguez &lt;jesusr [at] redhat.com&gt; 

 Pall Sigurdsson &lt;palli [at] opensource.is&gt; 

 Miroslav Suchý &lt;msuchy [at] redhat.com&gt; 

 and: Adam Miller, Alex Wood, Aron Parsons, Brenton Leanhardt, Ivan Nečas, John Eckersberg, Kenny MacDermid, Lukáš Zapletal, Luke Meyer, Marian Csontos, Martin Bačovský, Michael Stead, Mike McCune, mscherer, Paul Morgan, Sean P. Kane, Steve <i>Ashcrow</i> Milner
