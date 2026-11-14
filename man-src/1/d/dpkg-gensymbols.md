---
title: "dpkg-gensymbols(1)"
name: "dpkg-gensymbols"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-gensymbols/"
description: "dpkg-gensymbols – generate symbols files (shared library dependency information)"
---

<h2 class="name">NAME</h2>
<p> dpkg-gensymbols &#8211; generate symbols files (shared library dependency information) </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-gensymbols</code> [<i>option</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-gensymbols</code> scans a temporary build tree (debian/tmp by default) looking for libraries and generates a <i>symbols</i> file describing them. This file, if non-empty, is then installed in the <font SIZE="-1">DEBIAN</font> subdirectory of the build tree so that it ends up included in the control information of the package. </p>
<p> When generating those files, it uses as input some symbols files provided by the maintainer. It looks for the following files (and uses the first that is found):</p>
<dl>
<dt>&bull;</p>
<dd> debian/<i>package</i>.symbols.<i>arch</i></p>
<dt>&bull;</p>
<dd> debian/symbols.<i>arch</i></p>
<dt>&bull;</p>
<dd> debian/<i>package</i>.symbols</p>
<dt>&bull;</p>
<dd> debian/symbols</dl>
<p> The main interest of those files is to provide the minimal version associated to each symbol provided by the libraries. Usually it corresponds to the first version of that package that provided the symbol, but it can be manually incremented by the maintainer if the <font SIZE="-1">ABI</font> of the symbol is extended without breaking backwards compatibility. It&#8217;s the responsibility of the maintainer to keep those files up-to-date and accurate, but <code>dpkg-gensymbols</code> helps with that. </p>
<p> When the generated symbols files differ from the maintainer supplied one, <code>dpkg-gensymbols</code> will print a diff between the two versions. Furthermore if the difference is too significant, it will even fail (you can customize how much difference you can tolerate, see the <code>-c</code> option).</p>
<h2>MAINTAINING SYMBOLS FILES</h2>
<p> The base interchange format of the symbols file is described in <code><a href="/docs/linux/man/5-deb-symbols/">deb-symbols</a></code>(5), which is used by the symbols files included in binary packages. These are generated from template symbols files with a format based on the former, described in <code><a href="/docs/linux/man/5-deb-src-symbols/">deb-src-symbols</a></code>(5) and included in source packages. </p>
<p> The symbols files are really useful only if they reflect the evolution of the package through several releases. Thus the maintainer has to update them every time that a new symbol is added so that its associated minimal version matches reality. </p>
<p> The diffs contained in the build logs can be used as a starting point, but the maintainer, additionally, has to make sure that the behaviour of those symbols has not changed in a way that would make anything using those symbols and linking against the new version, stop working with the old version. </p>
<p> In most cases, the diff applies directly to the debian/<i>package</i>.symbols file. That said, further tweaks are usually needed: it&#8217;s recommended for example to drop the Debian revision from the minimal version so that backports with a lower version number but the same upstream version still satisfy the generated dependencies. If the Debian revision can&#8217;t be dropped because the symbol really got added by the Debian specific change, then one should suffix the version with &#8216;<code>~</code>&#8216;. </p>
<p> Before applying any patch to the symbols file, the maintainer should double-check that it&#8217;s sane. Public symbols are not supposed to disappear, so the patch should ideally only add new lines. </p>
<p> Note that you can put comments in symbols files. </p>
<p> Do not forget to check if old symbol versions need to be increased. There is no way <code>dpkg-gensymbols</code> can warn about this. Blindly applying the diff or assuming there is nothing to change if there is no diff, without checking for such changes, can lead to packages with loose dependencies that claim they can work with older packages they cannot work with. This will introduce hard to find bugs with (partial) upgrades.</p>
<h3>Good library management</h3>
<p> A well-maintained library has the following features:</p>
<dl>
<dt>&bull;</p>
<dd> its <font SIZE="-1">API</font> is stable (public symbols are never dropped, only new public symbols are added) and changes in incompatible ways only when the <font SIZE="-1">SONAME</font> changes;</p>
<dt>&bull;</p>
<dd> ideally, it uses symbol versioning to achieve <font SIZE="-1">ABI</font> stability despite internal changes and <font SIZE="-1">API</font> extension;</p>
<dt>&bull;</p>
<dd> it doesn&#8217;t export private symbols (such symbols can be tagged optional as workaround).</dl>
<p> While maintaining the symbols file, it&#8217;s easy to notice appearance and disappearance of symbols. But it&#8217;s more difficult to catch incompatible <font SIZE="-1">API</font> and <font SIZE="-1">ABI</font> change. Thus the maintainer should read thoroughly the upstream changelog looking for cases where the rules of good library management have been broken. If potential problems are discovered, the upstream author should be notified as an upstream fix is always better than a Debian specific work-around.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-P</code><i>package-build-dir</i></p>
<dd> Scan <i>package-build-dir</i> instead of debian/tmp.</p>
<dt><code>-p</code><i>package</i></p>
<dd> Define the package name. Required if more than one binary package is listed in debian/control (or if there&#8217;s no debian/control file).</p>
<dt><code>-v</code><i>version</i></p>
<dd> Define the package version. Defaults to the version extracted from debian/changelog. Required if called outside of a source package tree.</p>
<dt><code>-e</code><i>library-file</i></p>
<dd> Only analyze libraries explicitly listed instead of finding all public libraries. You can use shell patterns used for pathname expansions (see the <code>File::Glob</code>(3perl) manual page for details) in <i>library-file</i> to match multiple libraries with a single argument (otherwise you need multiple <code>-e</code>).</p>
<dt><code>-l</code><i>directory</i></p>
<dd> Prepend <i>directory</i> to the list of directories to search for private shared libraries (since dpkg 1.19.1). This option can be used multiple times. </p>
<p> <code>Note:</code> Use this option instead of setting <font SIZE="-1"><code>LD_LIBRARY_PATH</code></font>, as that environment variable is used to control the run-time linker and abusing it to set the shared library paths at build-time can be problematic when cross-compiling for example.</p>
<dt><code>-I</code><i>filename</i></p>
<dd> Use <i>filename</i> as reference file to generate the symbols file that is integrated in the package itself.</p>
<dt><code>-O</code>[<i>filename</i>]</p>
<dd> Print the generated symbols file to standard output or to <i>filename</i> if specified, rather than to <code>debian/tmp/DEBIAN/symbols</code> (or <i>package-build-dir</i><code>/DEBIAN/symbols</code> if <code>-P</code> was used). If <i>filename</i> is pre-existing, its contents are used as basis for the generated symbols file. You can use this feature to update a symbols file so that it matches a newer upstream version of your library.</p>
<dt><code>-t</code></p>
<dd> Write the symbol file in template mode rather than the format compatible with <code><a href="/docs/linux/man/5-deb-symbols/">deb-symbols</a></code>(5). The main difference is that in the template mode symbol names and tags are written in their original form contrary to the post-processed symbol names with tags stripped in the compatibility mode. Moreover, some symbols might be omitted when writing a standard <code><a href="/docs/linux/man/5-deb-symbols/">deb-symbols</a></code>(5) file (according to the tag processing rules) while all symbols are always written to the symbol file template.</p>
<dt><code>-c</code><i>[0-4]</i></p>
<dd> Define the checks to do when comparing the generated symbols file with the template file used as starting point. By default the level is 1. Increasing levels do more checks and include all checks of lower levels.</p>
<dl>
<dt>
<dd>
<dl>
<dt>Level 0</p>
<dd> Never fails.</p>
<dt>Level 1</p>
<dd> Fails if some symbols have disappeared.</p>
<dt>Level 2</p>
<dd> Fails if some new symbols have been introduced.</p>
<dt>Level 3</p>
<dd> Fails if some libraries have disappeared.</p>
<dt>Level 4</p>
<dd> Fails if some libraries have been introduced.</dl>
</dl>
<dl>
<dt>
<dd>
<p> This value can be overridden by the environment variable <font SIZE="-1"><code>DPKG_GENSYMBOLS_CHECK_LEVEL</code></font>.</dl>
<dt><code>-q</code></p>
<dd> Keep quiet and never generate a diff between generated symbols file and the template file used as starting point or show any warnings about new/lost libraries or new/lost symbols. This option only disables informational output but not the checks themselves (see <code>-c</code> option).</p>
<dt><code>-a</code><i>arch</i></p>
<dd> Assume <i>arch</i> as host architecture when processing symbol files. Use this option to generate a symbol file or diff for any architecture provided its binaries are already available.</p>
<dt><code>-d</code></p>
<dd> Enable debug mode. Numerous messages are displayed to explain what <code>dpkg-gensymbols</code> does.</p>
<dt><code>-V</code></p>
<dd> Enable verbose mode. The generated symbols file contains deprecated symbols as comments. Furthermore in template mode, pattern symbols are followed by comments listing real symbols that have matched the pattern.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_GENSYMBOLS_CHECK_LEVEL</code></font></p>
<dd> Overrides the command check level, even if the <code>-c</code> command-line argument was given (note that this goes against the common convention of command-line arguments having precedence over environment variables).</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dl>
<h2>SEE ALSO</h2>
<p> &lt;<a rel="nofollow" href="https://people.redhat.com/drepper/symbol-versioning">https://people.redhat.com/drepper/symbol-versioning</a>&gt;, &lt;<a rel="nofollow" href="https://people.redhat.com/drepper/goodpractice.pdf">https://people.redhat.com/drepper/goodpractice.pdf</a>&gt;, &lt;<a rel="nofollow" href="https://people.redhat.com/drepper/dsohowto.pdf">https://people.redhat.com/drepper/dsohowto.pdf</a>&gt;, <code><a href="/docs/linux/man/5-deb-src-symbol/">deb-src-symbol</a></code>(5), <code><a href="/docs/linux/man/5-deb-symbols/">deb-symbols</a></code>(5), <code><a href="/docs/linux/man/1-dpkg-shlibdeps/">dpkg-shlibdeps</a></code>(1). </p>
<h2>Index</h2>
