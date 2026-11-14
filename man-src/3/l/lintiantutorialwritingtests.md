---
title: "lintiantutorialwritingtests(3)"
name: "lintiantutorialwritingtests"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiantutorialwritingtests/"
description: "Lintian::Tutorial::WritingTests — Short tutorial on writing tests"
---

<p>Lintian::Tutorial::WritingTests &#8212; Short tutorial on writing tests </p>
<h2>Synopsis</h2>
<p>Warning: This document may be out of date. </p>
<p> This document attempts to be a short / quick tutorial to the Lintian test suite from a test-writer&#8217;s perspective. As such, it will only cover the standard type of tests (from the &#8220;tests&#8221; suite). </p>
<p> The guide will involve writing a test for the &#8220;deb/pkg-check&#8221; check, which was documented in the Lintian::Tutorial::WritingChecks tutorial. </p>
<p> For running tests, please see Lintian::Tutorial::TestSuite instead.</p>
<h2>Description</h2>
<p>The Lintian test suite is divided into several parts. These are:</p>
<dl COMPACT>
<dt>&#8211;</p>
<dd>scripts </p>
<p> Small (Perl) &#8220;prove&#8221; tests. These assert that code style, data files and/or self-contained code units (i.e. unit tests) work as intended. They are <code>not</code> used for testing Lintian tags.</p>
<dt>&#8211;</p>
<dd>tags </p>
<p> These tests all test for the presence of tags after building test packages using skeletons. For most cases, we recommend </p>
<pre> Skeleton: upload-non-native</pre>
<p>suites are small test suites that test some particular tags for <i>.changes</i>, <i>.deb</i> or <i>.dsc</i> files. Typically, you will find the more exotic tags here, which require some special fiddling and cannot be built by a &#8220;standard&#8221; dh7 + dpkg build.</p>
<dt>&#8211;</p>
<dd>literal </p>
<p> These tests look to match the literal output of Lintian. These tests are useful as general false positives. They also catch Lintian messages unrelated to tags.</dl>
<p> With this in mind, let us move on to the scope.</p>
<h3>Scope of the tutorial</h3>
<p><font SIZE="-1">WARNING: THE REMAINDER OF THIS TUTORIAL IS OUT OF DATE.</font> </p>
<p> The &#8220;tests&#8221; suite alone is fairly complex on its own. To keep things simple, the tutorial will limit itself to creating a &#8220;native&#8221; package with no special requirements in the &#8220;tests&#8221; suite. </p>
<p> In particular, note that the tags <i>must not</i> be <i>pedantic</i> for this to work. If you followed the check writing tutorial and made the tags pedantic, please change them into &#8220;I&#8221;, &#8220;W&#8221; or &#8220;E&#8221; tags. </p>
<p> Once the basics are covered, you should be better equipped to deal with the other (&#8220;tag testing&#8221;) suites or using other features of the &#8220;tests&#8221; suite (e.g. pedantic tags).</p>
<h3>The design of the Lintian test suite</h3>
<p>The basic design of the Lintian test suite can be summed up as <i>less is more</i>. The Debian build system is changing all the time (albeit, slowly) and sometimes it deprecates or breaks existing features. </p>
<p> With over 400 tests all featuring the same basic parts, the test suite features several tricks to keep up with the pace. It uses &#8220;skeletons&#8221; (template) directories to seed the package structures and template files to fill in the basic files (e.g. &#8220;debian/control&#8221; and &#8220;debian/changelog&#8221;). </p>
<p> This means that when a new standards-version comes along, debhelper deprecates a feature or (more likely) Lintian adds a new tag, the majority of the tests can quickly be adapted with only a minor effort. </p>
<p> Since pedantic tags tend to require additional effort to avoid, most Lintian tests do <code>not</code> run with pedantic tags enabled.</p>
<h3>The basics of a native package in the tests suite</h3>
<p>For starters, you need 2 files and 1 directory, which will be placed in <i>t/tests/&lt;test-name&gt;</i>. </p>
<p> <i>The desc file (mandatory)</i> </p>
<p> This is the test description file. It is a deb822 file (i.e. same syntax as <i>debian/control</i>), which contains a number of fields. </p>
<p> Let&#8217;s start with the following template: </p>
<pre> Testname: pkg-deb-check-general
 Version: 1.0
 Description: General test of the pkg/deb-check check
 Test-For:
 missing-multi-arch-field
 missing-pre-depends-on-multiarch-support</pre>
<p>This defines the name of the test, its sequence number (i.e. how early it should be run), the version of the <i>generated</i> package, a description and the tags you intend to test for. </p>
<p> In case you were wondering why &#8220;invalid-multi-arch-field&#8221; is not listed, then it is because dpkg will not allow us to use an invalid Multi-Arch value. Therefore, that particular tag would have to be tested in the &#8220;debs&#8221; suite instead. </p>
<p> Note that the value of the Testname field (as Source field), Version field and Description field (as the synopsis) <i>will</i> be used in the package. As such, they must obey the normal requirements for these purposes. </p>
<p> Please keep the following conventions in mind:</p>
<dl COMPACT>
<dt>&#8211;</p>
<dd>The Testname should be &#8220;&lt;check-name&gt;-&lt;test-name&gt;&#8221; </p>
<p> Note that regular Lintian checks do <i>not</i> have a &#8220;/&#8221;, so the naming convention works slightly better there.</p>
<dt>&#8211;</p>
<dd>The Version should always be &#8220;1.0&#8221; unless the test requires anything else. </p>
<p> For non-native packages, the default would be &#8220;1.0-1&#8221;.</dl>
<p> <i>The &#8220;tags&#8221; file (mandatory, but may be empty)</i> </p>
<p> This file contains the <i>sorted</i> &#8220;expected&#8221; output of lintian. Assuming all of the tags are &#8220;I&#8221; tags, the file should look something like: </p>
<pre> I: pkg-deb-check-general-missing-ma: missing-multi-arch-field
 I: pkg-deb-check-general-missing-pred: missing-pre-depends-on-multiarch-support</pre>
<p><i>The &#8220;debian/&#8221; directory (optional, but usually needed)</i> </p>
<p> The unpacked debian package in its full glory. Note that this means that the (e.g.) <i>debian/rules</i> file would be <i>t/tests/&lt;test-name&gt;/debian/debian/rules</i> (note the double &#8220;debian/&#8221;). </p>
<p> The directory is seeded from <i>t/templates/tests/&lt;skeleton&gt;/</i>, where <i>skeleton</i> is the value of the &#8220;Skeleton&#8221; field from the &#8220;desc&#8221; file. </p>
<p> For this test, you only need a specialized control file. This file could look something like: </p>
<pre> Source: {$source}
 Priority: extra
 Section: {$section}
 Maintainer: {$author}
 Standards-Version: {$standards_version}
 Build-Depends: {$build_depends}
 
 Package: {$source}-missing-ma
 Architecture: {$architecture}
 Depends: $\{shlibs:Depends\}, $\{misc:Depends\}
 Description: {$description} (invalid)
 This is a test package designed to exercise some feature or tag of
 Lintian. It is part of the Lintian test suite and may do very odd
 things. It should not be installed like a regular package. It may
 be an empty package.
 .
 Missing M-A field.
 
 Package: {$source}-missing-pred
 Architecture: any
 Depends: $\{shlibs:Depends\}, $\{misc:Depends\}
 Multi-arch: same
 Description: {$description} (pre-depends)
 This is a test package designed to exercise some feature or tag of
 Lintian. It is part of the Lintian test suite and may do very odd
 things. It should not be installed like a regular package. It may
 be an empty package.
 .
 Missing Pre-Depends.</pre>
<p><i>Running the test</i> </p>
<p> At this point, the test is in fact ready to be executed. It can be run by using: </p>
<pre> $ debian/rules runtests onlyrun=pkg-deb-check-general
 OR
 $ t/bin/runtests --dump-logs t debian/test-out pkg-deb-check-general</pre>
<p>However, it will not emit the correct tags unless pkg/deb-check is part of the debian/main lintian profile. If your check is a part of a different profile, add the &#8220;Profile: &lt;name&gt;&#8221; field to the &#8220;desc&#8221; file. </p>
<p> With this, the tutorial is over. Below you will find some more resources that may be useful to your future test writing work.</p>
<h2>References / Appendix</h2>
<h3>A step-by-step guide of how a test case works</h3>
<p>Basically, the tag-testing test cases all involve building a package and running lintian on the result. The &#8220;tests&#8221; suite does a full build with dpkg-buildpackage, the other suites &#8220;hand-craft&#8221; only the type of artifacts they are named after (e.g. &#8220;source&#8221; produces only source packages). </p>
<p> <i>A test in the &#8220;tests&#8221; suite</i> </p>
<p> The basic process of a lintian test in the &#8220;tests&#8221; suite.</p>
<dl COMPACT>
<dt>1.</p>
<dd>Copy the &#8220;upstream&#8221; skeleton dir into the build dir (non-native only)</p>
<dt>2.</p>
<dd>Copy the &#8220;upstream&#8221; dir from the test into the build dir (if present, non-native only)</p>
<dt>3.</p>
<dd>Run the &#8220;pre_upstream&#8221; hook (if present, non-native only)</p>
<dt>4.</p>
<dd>Assemble the upstream tarball (non-native only)</p>
<dt>5.</p>
<dd>Copy the &#8220;debian&#8221; skeleton dir into the build dir</p>
<dt>6.</p>
<dd>Copy the &#8220;debian&#8221; directory from the test into the build dir (if present)</p>
<dt>7.</p>
<dd>Create debian/control and debian/changelog from &quot;<i>&lt;file&gt;</i>.in&quot; if they do not exist.</p>
<dt>8.</p>
<dd>Create an empty watch file (if missing, non-native only)</p>
<dt>9.</p>
<dd>Run the &#8220;pre_build&#8221; hook (if present)</p>
<dt>10.</p>
<dd>Run dpkg-buildpackage</p>
<dt>11.</p>
<dd>Run lintian on the build result</p>
<dt>12.</p>
<dd>Run the &#8220;post_test&#8221; hook (if present)</p>
<dt>13.</p>
<dd>Run the &#8220;test_calibration&#8221; hook (if present), which may produce a new &#8220;expected output file&#8221;.</p>
<dt>14.</p>
<dd>Compare the result with the expected output.</dl>
<p> Note that the majority of the steps are conditional on native/non-native packages or presence of hooks. </p>
<p> <i>A test in the &#8220;debs&#8221; and the &#8220;source&#8221; suite</i> </p>
<p> The &#8220;debs&#8221; and the &#8220;source&#8221; suite share the same basic steps, which are:</p>
<dl COMPACT>
<dt>1.</p>
<dd>Copy the skeleton dir into the build dir</p>
<dt>2.</p>
<dd>Copy the test directory files into the build dir</p>
<dt>3.</p>
<dd>Create changelog, control, and (debs-only) Makefile from &quot;<i>&lt;file&gt;</i>.in&quot; if they do not exist.</p>
<dt>4.</p>
<dd>Run make in the build dir</p>
<dt>5.</p>
<dd>Run lintian on the produced artifact (there must be exactly one)</p>
<dt>6.</p>
<dd>Compare the result with the expected output.</dl>
<p> <i>A test in the &#8220;changes&#8221; suite</i> </p>
<p> The changes test is fairly simple as there is not much building. The steps are as the following:</p>
<dl COMPACT>
<dt>1.</p>
<dd>Find or compute the test artifact as the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>If <i>&lt;test-dir&gt;/&lt;test-name&gt;.changes</i> exists, it is used as the artifact.</p>
<dt>&#8211;</p>
<dd>Otherwise, copy <i>&lt;test-dir&gt;/&lt;test-name&gt;.changes.in</i> into the build dir and use it as a template to create <i>&lt;build-dir&gt;/&lt;test-name&gt;.changes</i>. The result is then used as the artifact to test.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>2.</p>
<dd>Run lintian run on the artifact</p>
<dt>3.</p>
<dd>Compare the result with the expected output</dl>
<h3>The full layout of a test in the tests suite</h3>
<p>Each test in the &#8220;tests&#8221; suite is placed in <i>t/tests/&lt;check&gt;-&lt;name&gt;</i>. In these you will find some of the following files:</p>
<dl COMPACT>
<dt>&#8211;</p>
<dd>desc (mandatory) </p>
<p> This is the test description file. It is a deb822 file (i.e. same syntax as <i>debian/control</i>), which contains a number of fields.</p>
<dt>&#8211;</p>
<dd>tags (mandatory, but may be empty) </p>
<p> This file contains the &#8220;expected&#8221; output of lintian. </p>
<p> This is generally sorted, though a few tests rely on the order of the output. This can be controlled via the &#8220;Sort&#8221; field in the &#8220;desc&#8221; file.</p>
<dt>&#8211;</p>
<dd>debian/ (optional, but usually what you need) </p>
<p> The unpacked debian package. For &#8220;native&#8221; package tests, this is <i>also</i> the &#8220;upstream&#8221; part. For &#8220;non-native&#8221; package tests, this can be used to override files in the &#8220;upstream&#8221; part (rarely needed). </p>
<p> The actual packaging files (e.g. <i>debian/rules</i>) would be in </p>
<pre> I&lt;&lt; t/tests/&lt;test-name&gt;/debian/debian/rules &gt;&gt;</pre>
<p>Note the double &#8220;debian&#8221;. </p>
<p> This part is seeded from <i>t/templates/tests/&lt;skeleton&gt;/</i>, where <i>skeleton</i> is the value of the &#8220;Skeleton&#8221; field from the &#8220;desc&#8221; file.</p>
<dt>&#8211;</p>
<dd>upstream/ (optional, rarely needed) </p>
<p> This directory is the used to create the &#8220;upstream&#8221; tarball for &#8220;non-native&#8221; package tests. Since most tags are emitted for both &#8220;native&#8221; and &#8220;non-native&#8221; tests, it is simpler (and slightly faster) to use &#8220;native&#8221; packages for most tests. </p>
<p> The files here should also be present with the same contents in the debian directory unless you&#8217;re intentionally creating a diff. However, as normal with a Debian package, you can omit files entirely from the debian directory and the deletions will be ignored by dpkg-buildpackage. </p>
<p> The directory will be seeded from <i>t/templates/tests/&lt;skeleton&gt;.upstream/</i>, where <i>skeleton</i> is the value of the &#8220;Skeleton&#8221; field from the &#8220;desc&#8221; file.</p>
<dt>&#8211;</p>
<dd>post_test (optional, rarely needed) </p>
<p> This script (if present) is a sed script that can be used to &#8220;massage&#8221; the output of lintian before comparing it with the &#8220;expected output&#8221;. </p>
<p> The most common use for this script is to remove the architecture name, multi-arch path, drop hardening tags or exact standards-version number from tags output. Here are some examples files used: </p>
<pre> # Remove the exact standards version, so the tags file will not need
 # to be updated with every new standards-version
 s/\(current is ([0-9]+\.)+[0-9]\)/(current is CURRENT)/
 # Drop all hardening tags (they can differ between architectures)
 /: hardening-.*/ d
 # Massage e.g. usr/lib/i386-linux-gnu/pkgconfig into a generic path
 s, usr/lib/[^/]+/pkgconfig/, usr/lib/ARCH/pkgconfig/,</pre>
<p>It may be useful for other cases where the output of Lintian may change on different systems.</p>
<dt>&#8211;</p>
<dd>pre_build / pre_upstream (optional, special case usage) </p>
<p> If present and executable, these scripts can be used to mess with the package directory and (what will become) the upstream tarball. </p>
<p> Their common use case is to create files in the tarballs that cannot (or preferably should not) be included in the revision control system. Common cases include &#8220;binary&#8221;, &#8220;minimized&#8221; files or files with &#8220;weird&#8221; names such as backslashes or non <font SIZE="-1">UTF-8</font> characters. </p>
<p> Both scripts receive a directory as first argument, which is the directory they should work on. For:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>pre_upstream </p>
<p> The script will be run before the upstream tarball is compiled. The first argument is the directory that will be included in the upstream tarball.</p>
<dt>&#8211;</p>
<dd>pre_build </p>
<p> The script will be run before dpkg-buildpackage is invoked. The first argument is the directory of the unpacked debian source package.</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>&#8211;</p>
<dd>test_calibration (optional, special case usage) </p>
<p> If present and executable, this script will be invoked <code>after</code> lintian <i>and</i> post_test (if present) have been run. The script can then modify the expected output <i>and</i> the actual output. </p>
<p> This is useful for those extremely rare cases where post_test is insufficient to handle the requirements. So far, this has only been needed for the hardening checks, where the output differs between architectures. </p>
<p> The script will be passed 3 arguments:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>Path to the &#8220;expected output&#8221; file (read-only) </p>
<p> This is the &#8220;tags&#8221; file from the test suite and <code>must not</code> be modified.</p>
<dt>&#8211;</p>
<dd>Path to the &#8220;actual output&#8221; file (read-write) </p>
<p> This is the file as lintian and post_test created it.</p>
<dt>&#8211;</p>
<dd>Path to the &#8220;calibrated expected output&#8221; (create+write) </p>
<p> This file does not exist and should be created by the script, if it wishes to change the &#8220;expected output&#8221;. If this file exists when the script terminates, this file will be used instead of the original &#8220;expected output&#8221; file.</dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h2>See Also</h2>
<p>The READMEs in the suites: <i>t/tests/README</i>, <i>t/changes/README</i>, <i>t/debs/README</i> and <i>t/source/README</i>. </p>
<p> Lintian::Tutorial::WritingChecks, Lintian::Tutorial::TestSuite</p>
