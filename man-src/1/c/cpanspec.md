---

title: "cpanspec(1)"
name: "cpanspec"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpanspec/"
description: "cpanspec – Generate a spec file for a CPAN module"
---

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
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print a brief help message and exit.</dd>
<dt><code>-o</code>, <code>&#8211;old</code></dt>
<dd> Be more compatible with old RHL/FC releases. With this option enabled, the generated spec file</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Defines perl_vendorlib or perl_vendorarch.</dd>
<dt>&bull;</dt>
<dd> Includes explicit dependencies for core Perl modules.</dd>
<dt>&bull;</dt>
<dd> Uses <tt>&quot;%check || :&quot;</tt> instead of just <tt>%check</tt>.</dd>
<dt>&bull;</dt>
<dd> Includes a hack to remove LD_RUN_PATH from Makefile.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-l</code>, <code>&#8211;license</code></dt>
<dd> Generate COPYING and Artistic license texts if the source doesn&#8217;t seem to include them.</dd>
<dt><code>-n</code>, <code>&#8211;noprefix</code></dt>
<dd> Don&#8217;t add <i>perl-</i> prefix to the name of the package. This is useful for perl-based applications (such as this one), so that the name of the rpm is simply <code>cpanspec</code> instead of <code>perl-cpanspec</code>.</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> Force overwriting an existing spec file. Normally <code>cpanspec</code> will refuse to overwrite an existing spec file for safety. This option removes that safety check. Please use with caution.</dd>
<dt><code>-p</code>, <code>&#8211;packager</code></dt>
<dd> The name and email address of the packager. Overrides the <tt>%packager</tt> macro in <tt>&quot;~/.rpmmacros&quot;</tt>.</dd>
<dt><code>-r</code>, <code>&#8211;release</code></dt>
<dd> The release number of the package. Defaults to 1.</dd>
<dt><code>-e</code>, <code>&#8211;epoch</code></dt>
<dd> The epoch number of the package. By default, this is undefined, so no epoch will be used in the generated spec.</dd>
<dt><code>-d</code>, <code>&#8211;disttag</code></dt>
<dd> Disttag (a string to append to the release number), used to differentiate builds for various releases. Defaults to the semi-standard (for Fedora) string <tt>&quot;%{?dist}&quot;</tt>.</dd>
<dt><code>-s</code>, <code>&#8211;srpm</code></dt>
<dd> Build a source rpm from the generated spec file.</dd>
<dt><code>-b</code>, <code>&#8211;build</code></dt>
<dd> Build source and binary rpms from the generated spec file. <code>Please be aware that this is likely to fail!</code> Even if it succeeds, the generated rpm will almost certainly need some work to make rpmlint happy.</dd>
<dt><code>-c</code>, <code>&#8211;cpan</code></dt>
<dd> The URL to a CPAN mirror. If not specified with this option or the <code>CPAN</code> environment variable, defaults to &lt;<a rel="nofollow" href="http://www.cpan.org/">http://www.cpan.org/</a>&gt;.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Be more verbose.</dd>
<dt><code>-m</code>, <code>&#8211;prefer-macros</code></dt>
<dd> Prefer the macro form of common spec constructs over the environment variable form (e.g. %{buildroot} vs <tt>$RPM_BUILD_ROOT</tt>).</dd>
<dt><code>&#8211;follow</code></dt>
<dd> Add build dependencies to the list of modules to process.</dd>
<dt><code>&#8211;filter-requires</code></dt>
<dd> Specify Requires to remove.</dd>
<dt><code>&#8211;filter-provides</code></dt>
<dd> Specify Provides to remove.</dd>
<dt><code>&#8211;add-requires</code></dt>
<dd> Add Requires for this item.</dd>
<dt><code>&#8211;add-provides</code></dt>
<dd> Add Provides for this item.</dd>
<dt><code>&#8211;add-buildrequires</code></dt>
<dd> Add BuildRequires for this item.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print the version number and exit.</dd></dl>
<h2>AUTHOR</h2>
<p> Steven Pritchard &lt;steve [at] kspei.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <i>cpan2rpm</i>(1), <i>cpanflute2</i>(1) </p>
