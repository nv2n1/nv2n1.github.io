---
title: "update-fmtlang(8)"
name: "update-fmtlang"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-fmtlang/"
description: "update-language, update-fmtutil, update-fmtlang – update various TeX-related configuration files"
---

<p>update-language, update-fmtutil, update-fmtlang &#8211; update various TeX-related configuration files</p>
<h2>Synopsis</h2>
<p><code>update-language</code> [<i>options</i>]<br />
 <code>update-fmtutil</code> [<i>options</i>] </p>
<h2>Description</h2>
<p>This manual page explains briefly the usage of the three TeX configuration update programs <code>update-language</code> and <code>update-fmtutil</code>. </p>
<p> The <code>update-fontlang</code> script should not be called directly, but only via the two described links. For a more in-depth description, please see the document <i>TeX on Debian</i> in <i>/usr/share/doc/tex-common/TeX-on-Debian.txt.gz</i> (also available as HTML and PDF). </p>
<p> The programs <code>update-language</code> and <code>update-fmtutil</code> create or update the configuration files <i>language.dat</i> and <i>fmtutil.cnf</i>, respectively. These files define the hyphenation patterns to be loaded into LaTeX-related TeX formats (<i>language.dat</i>), and the list of formats to be created (<i>fmtutil.cnf</i>). </p>
<p> These programs can be used either in system-wide mode if called by root, or in a user-specific mode if called by a user without super-user privileges.</p>
<h2>Options</h2>
<dl>
<dt><code>-c&nbsp;<wbr></code><i>DIR</i><code>, &#8211;conf-dir=</code><i>DIR</i></p>
<dd>directory where the user-specific configuration files are looked for in user-specific mode (default <i>TEXMFCONFIG/language.d</i> for <code>update-language</code> and <i>TEXMFCONFIG/fmt.d</i> for <code>update-fmtutil</code>, where <i>TEXMFCONFIG</i> is usually <i>$HOME/.texmf-config</i>).</p>
<dt><code>-o&nbsp;<wbr></code><i>FILE</i><code>, &#8211;output-file=</code><i>FILE</i></p>
<dd>file to write the output to. Per default, in system-wide mode, <code>update-language</code> writes to <i>/var/lib/texmf/tex/generic/config/language.dat</i> and <code>update-fmtutil</code> writes to <i>/var/lib/texmf/web2c/fmtutil.cnf</i>.</p>
<dt><code>&#8211;checks</code></p>
<dd>perform sanity checks on the generated config file. Don&#8217;t use this in maintainer scripts.</p>
<dt><code>&#8211;quiet</code></p>
<dd>don&#8217;t write anything to the standard output during normal operation</p>
<dt><code>&#8211;help</code></p>
<dd>print a summary of the command-line usage and exit</p>
<dt><code>&#8211;version</code></p>
<dd>output version information and exit </p>
</dl>
<h2>Usage</h2>
<p>In system-wide mode, both programs merge those files (&quot;configuration snippets&quot;) with a specific extension in the respective configuration directories to produce the final file. These configuration directories and extensions are <i>language.d</i> and <code>.cnf</code> for <code>update-language</code>, and <i>fmt.d</i> and <code>.cnf</code> for <code>update-fmtutil</code>. In system-wide mode, these directories are those under <i>/etc/texmf/</i>. Both TeX add-on packages and local administrators can add files to these directories. </p>
<p> If a package that provides such snippets is removed but not purged, including the snippet will likely break the system. To prevent the inclusion in these cases, snippets installed by <i>packages</i> have to contain a magic header: </p>
<p> # -_- DebPkgProvidedMaps -_- </p>
<p> which local administrators should <i>not</i> remove. From the files with a magic header, only those files which are also listed in one of the files in <i>/var/lib/tex-common/language-cnf/</i> for <code>update-language</code>, and <i>/var/lib/tex-common/fmtutil-cnf/</i> for <code>update-fmtutil</code>, are actually included into the final output file. This way, local changes to the configuration can be preserved while the package is in state &#8216;rc&#8217; (that is, the package is removed, but its configuration files are still present). For details about this mechanism, package maintainers should consult the Debian TeX Policy. As a special case, the files for JadeTeX and xmlTeX are only included if there is already a file for the LaTeX format (see <i>TeX on Debian</i> for details). </p>
<p> The user-specific mode provides a way for a non-admin user to override system-wide settings. In this mode, <code>update-language</code> writes to <i>TEXMFVAR/tex/generic/config/language.dat</i>, and <code>update-fmtutil</code> writes to <i>TEXMFVAR/web2c/fmtutil.cnf</i>, where <i>TEXMFVAR</i> is usually <i>$HOME/.texmf-var</i>. Furthermore, files present within the user-specific configuration directories are included <i>in addition</i> to the files present in the system-wide configuration directories. In case the same filename exists in the system-wide configuration directory and the user-specific configuration directory, the user-specific file is used instead of the system-wide one. The user-specific configuration directories are <i>TEXMFCONFIG/language.d</i> for <code>update-language</code> and <i>TEXMFCONFIG/fmt.d</i> for <code>update-fmtutil</code>, where <i>TEXMFCONFIG</i> is usually <i>$HOME/.texmf-config</i>. The system-wide configuration directories have the same names, but are located in <i>/etc/texmf/</i> instead of <i>TEXMFCONFIG</i>. </p>
<p> Note that changes introduced by updates of packages are <i>not</i> propagated to the user&#8217;s configuration files. This has to be done by hand.</p>
<h2>Files</h2>
<dl>
<dt><code>/var/lib/texmf/tex/generic/config/language.dat</code></p>
<dd>This file is generated or updated by <code>update-language</code> in system-wide mode and contains a list of the hyphenation patterns loaded into LaTeX-based formats by <code>fmtutil-sys</code>.</p>
<dt><code>/var/lib/texmf/web2c/fmtutil.cnf</code></p>
<dd>This file is generated or updated by <code>update-fmtutil</code> in system-wide mode and contains a list of formats to be generated by <code>fmtutil-sys</code>.</p>
<dt><code>/etc/texmf/language.d/</code><i>name</i>.cnf</p>
<dd>Input files for <code>update-language</code></p>
<dt><code>/etc/texmf/fmt.d/</code><i>name</i>.cnf</p>
<dd>Input files for <code>update-fmtutil</code></p>
<dt><code>/var/lib/tex-common/language-cnf/</code><i>package</i>.list</p>
<dd>Lists the file(s) installed by <i>package</i> in <i>/etc/texmf/language.d/</i>.</p>
<dt><code>/var/lib/tex-common/fmtutil-cnf/</code><i>package</i>.list</p>
<dd>Lists the file(s) installed by <i>package</i> in <i>/etc/texmf/fmt.d/</i>. </p>
</dl>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-fmtutil/">fmtutil</a>(1), <a href="/docs/linux/man/1-fmtutil-sys/">fmtutil-sys</a>(1)</code></p>
<dd>The programs actually using the generated configuration files (<i>language.dat</i> and <i>fmtutil.cnf</i>).</p>
<dt><code>TeX on Debian Documentation</code></p>
<dd>to be found in <i>/usr/share/doc/tex-common/TeX-on-Debian.txt.gz</i> (also available as HTML and PDF), describing in more detail how to setup and maintain a TeX system in Debian. It also includes details on user-specific configuration.</p>
<dt><code>Debian TeX Policy</code></p>
<dd>to be found in <i>/usr/share/doc/tex-common/Debian-TeX-Policy.txt.gz</i> (also available as HTML and PDF), describing the internals and the TeX Policy established on the Debian TeX mailing-list (debian-tex-maint [at] lists.debian.org). Intended audience is mainly developers packaging TeX-related resources for Debian.</p>
<dt><code><a href="/docs/linux/man/1-dh_installtex/">dh_installtex</a>(1)</code></p>
<dd>a debhelper-like script for managing the installation of files into the system-wide configuration directories; this script helps to write Debian packages containing TeX-related resources that conform to the Debian TeX Policy. </p>
<h2>Author</h2>
<p>This manual page was written by Norbert Preining &lt;preining [at] debian.org&gt; for the Debian distribution (and may be used by others). It was later updated by Florent Rougon &lt;f.rougon [at] free.fr&gt;.</p>
