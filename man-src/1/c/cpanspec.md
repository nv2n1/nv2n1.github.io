---
title: "cpanspec(1)"
name: "cpanspec"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpanspec/"
description: "cpanspec – Generate a spec file for a CPAN module"
---

<h2 class="name">NAME</h2>
<p> cpanspec &#8211; Generate a spec file for a CPAN module </p>
<h2>SYNOPSIS</h2>
<p> cpanspec [options] [file [&#8230;]] </p>
<pre><code>
 Options:
   --help       -h      Help message
   --old        -o      Be more compatible with old RHL/FC releases
   --license    -l      Include generated license texts if absent in source
   --noprefix   -n      Don't add perl- prefix to package name
   --force      -f      Force overwriting existing spec
   --packager   -p      Name and email address of packager (for changelog)
   --release    -r      Release of package (defaults to 1)
   --epoch      -e      Epoch of package
   --disttag    -d      Disttag (defaults to %{?dist})
   --srpm       -s      Build a source rpm
   --build      -b      Build source and binary rpms
   --cpan       -c      CPAN mirror URL
   --verbose    -v      Be more verbose
   --prefer-macros  -m  Prefer macros over environment variables in the spec
 Long options:
   --follow             Process build dependencies
   --filter-requires    Specify Requires to remove
   --filter-provides    Specify Provides to remove
   --add-requires       Add Requires for this item
   --add-provides       Add Provides for this item
   --add-buildrequires  Add BuildRequires for this item
   --version            Print the version number and exit
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>cpanspec</code> will generate a spec file to build a rpm from a CPAN-style Perl module distribution.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a brief help message and exit.</p>
<dt><code>-o</code>, <code>&#8211;old</code></p>
<dd> Be more compatible with old <font SIZE="-1">RHL/FC</font> releases. With this option enabled, the generated spec file</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Defines perl_vendorlib or perl_vendorarch.</p>
<dt>&bull;</p>
<dd> Includes explicit dependencies for core Perl modules.</p>
<dt>&bull;</p>
<dd> Uses <tt>&quot;%check || :&quot;</tt> instead of just <tt>%check</tt>.</p>
<dt>&bull;</p>
<dd> Includes a hack to remove <font SIZE="-1">LD_RUN_PATH</font> from Makefile.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-l</code>, <code>&#8211;license</code></p>
<dd> Generate <font SIZE="-1">COPYING</font> and Artistic license texts if the source doesn&#8217;t seem to include them.</p>
<dt><code>-n</code>, <code>&#8211;noprefix</code></p>
<dd> Don&#8217;t add <i>perl-</i> prefix to the name of the package. This is useful for perl-based applications (such as this one), so that the name of the rpm is simply <code>cpanspec</code> instead of <code>perl-cpanspec</code>.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Force overwriting an existing spec file. Normally <code>cpanspec</code> will refuse to overwrite an existing spec file for safety. This option removes that safety check. Please use with caution.</p>
<dt><code>-p</code>, <code>&#8211;packager</code></p>
<dd> The name and email address of the packager. Overrides the <tt>%packager</tt> macro in <tt>&quot;~/.rpmmacros&quot;</tt>.</p>
<dt><code>-r</code>, <code>&#8211;release</code></p>
<dd> The release number of the package. Defaults to 1.</p>
<dt><code>-e</code>, <code>&#8211;epoch</code></p>
<dd> The epoch number of the package. By default, this is undefined, so no epoch will be used in the generated spec.</p>
<dt><code>-d</code>, <code>&#8211;disttag</code></p>
<dd> Disttag (a string to append to the release number), used to differentiate builds for various releases. Defaults to the semi-standard (for Fedora) string <tt>&quot;%{?dist}&quot;</tt>.</p>
<dt><code>-s</code>, <code>&#8211;srpm</code></p>
<dd> Build a source rpm from the generated spec file.</p>
<dt><code>-b</code>, <code>&#8211;build</code></p>
<dd> Build source and binary rpms from the generated spec file. <code>Please be aware that this is likely to fail!</code> Even if it succeeds, the generated rpm will almost certainly need some work to make rpmlint happy.</p>
<dt><code>-c</code>, <code>&#8211;cpan</code></p>
<dd> The <font SIZE="-1">URL</font> to a <font SIZE="-1">CPAN</font> mirror. If not specified with this option or the <font SIZE="-1"><code>CPAN</code></font> environment variable, defaults to &lt;<a rel="nofollow" href="http://www.cpan.org/">http://www.cpan.org/</a>&gt;.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be more verbose.</p>
<dt><code>-m</code>, <code>&#8211;prefer-macros</code></p>
<dd> Prefer the macro form of common spec constructs over the environment variable form (e.g. %{buildroot} vs <tt>$RPM_BUILD_ROOT</tt>).</p>
<dt><code>&#8211;follow</code></p>
<dd> Add build dependencies to the list of modules to process.</p>
<dt><code>&#8211;filter-requires</code></p>
<dd> Specify Requires to remove.</p>
<dt><code>&#8211;filter-provides</code></p>
<dd> Specify Provides to remove.</p>
<dt><code>&#8211;add-requires</code></p>
<dd> Add Requires for this item.</p>
<dt><code>&#8211;add-provides</code></p>
<dd> Add Provides for this item.</p>
<dt><code>&#8211;add-buildrequires</code></p>
<dd> Add BuildRequires for this item.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and exit.</dl>
<h2>AUTHOR</h2>
<p> Steven Pritchard &lt;steve [at] kspei.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <i><a href="/docs/linux/man/1-cpan2rpm/">cpan2rpm</a></i>(1), <i><a href="/docs/linux/man/1-cpanflute2/">cpanflute2</a></i>(1) </p>
<h2>Index</h2>
