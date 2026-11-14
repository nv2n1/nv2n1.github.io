---
title: "fedora-review(1)"
name: "fedora-review"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fedora-review/"
description: "fedora-review – Customized review template for Fedora packages"
---

<h2>NAME</h2>
<p> fedora-review &#8211; Customized review template for Fedora packages </p>
<h2>SYNOPSIS</h2>
<p> <code>fedora-review</code> [options] -b &lt;bug&gt;<br />
 <code>fedora-review</code> [options] [&#8211;prebuilt] -n &lt;package name&gt;<br />
 <code>fedora-review</code> [options] [&#8211;prebuilt] -rn &lt;srpm path&gt;<br />
 <code>fedora-review</code> [options] -u &lt;url&gt; </p>
<h2>DESCRIPTION</h2>
<p> Makes reviews of rpm packages for Fedora easier by providing a customized review template, automating some trivial tasks. The tool runs a number of checks to test whether a package complies to the Fedora Packaing Guidelines before creating the template. Through a bash API the checks can be extended. We have at the moment checks for C/C++, R, Java and Perl packages. </p>
<h2>USAGE</h2>
<p> Basic usage:</p>
<dl>
<dt>
<dd> $ fedora-review -b &lt;bug number&gt;<br />
 $ fedora-review -u &lt;url&gt;</dl>
<p> Will download the SPEC &amp; SRPM files from the Bugzilla report, build them in mock, run a number of tests and generate a template. </p>
<p> Not all bugzillas support the -b option. The -u option is available for these. See &#8211;url usage notes below.</p>
<dl>
<dt>
<dd> $ fedora-review -n &lt;package name&gt;</dl>
<p> This alternative usage expects &lt;package name&gt;.spec and source rpm in current directory. By adding the -p switch, fedora-review uses already built rpms in current directory instead of building using mock.</p>
<dl>
<dt>
<dd> $ fedora-review &#8211;rpm-spec -n &lt;srpm path&gt;</dl>
<p> This form accepts a single path to a source rpm. It uses the specfile bundled in the srpm package. </p>
<p> You will need to have mock installed and be member of the mock group for the build to work. Run as root:</p>
<dl>
<dt>
<dd> # usermod -a -G mock [your user name]</dl>
<p> After this, you will need to logout and login again (or use <a href="/docs/linux/man/1-newgrp/">newgrp</a>(1)) &#8211; the changes in user&#8217;s group list is not read until a new login.</p>
<h2>MODE OPTIONS &#8211; one is required</h2>
<dl>
<dt><code>-b, &#8211;bug &lt;bug nr&gt;</code></p>
<dd> Run against Fedora bugzilla at bugzilla.redhat.com, using the bugzilla bug number</p>
<dt><code>-n, &#8211;name &lt;name&gt;</code></p>
<dd> Runs the checks against the named spec and source rpm located in the current working directory. The files are expected to have the names &lt;name&gt;.spec and &lt;name&gt;*.src.rpm. When used together with &#8211;rpm-spec/-r, name can also be a complete path to a source rpm.</p>
<dt><code>-u url, &#8211;url &lt;url&gt;</code></p>
<dd> Fetch data from given url, typically another bugzilla instance such as rpmfusion. Before using this, first try the more convenient &#8211;bug &lt;bug nr&gt; &#8211;other-bz &lt;url&gt;. The option tries to retrieve the URL:s by scanning the page. See URL Limitations for how the url must look to be found.</p>
<dt><code>-d, &#8211;display-checks</code></p>
<dd> List all available checks, usable as arguments to &#8211;exclude and &#8211;single</p>
<dt><code>-f, &#8211;display-flags</code></p>
<dd> List all available flags, usable as arguments to &#8211;define or -D.</p>
<dt><code>-g, &#8211;display-plugins</code></p>
<dd> List all plugins which can be enabled/disabled using &#8211;plugins.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version info</dl>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-B, &#8211;no-colors</code></p>
<dd> Disable use of ansi colors in console output.</p>
<dt><code>-c, &#8211;cache</code></p>
<dd> Do not redownload the files from bugzilla or upstream, use the local ones from previous run instead.</p>
<dt><code>-D, &#8211;define &lt;flag[=value]&gt;</code></p>
<dd> Define a flag e. g., EPEL5. A flag can either just be activated using flag or set to a value using flag=value. &#8211;display-flags shows available flags.</p>
<dt><code>-k, &#8211;checksum &lt;md5|sha1|sha224|sha256|sha384|sha512&gt;</code></p>
<dd> Algorithm used for checksum.</p>
<dt><code>-L, &#8211;local-repo &lt;rpm directory&gt;</code></p>
<dd> Directory with rpms to install together with reviewed package during build and install phases.</p>
<dt><code>-m, &#8211;mock-config &lt;configuration&gt;</code></p>
<dd> Specify which mock config to use, one of the files in /etc/mock, with the .cfg suffix stripped. Defaults to the root defined in /etc/mock/default.cfg</p>
<dt><code>-o, &#8211;mock-options options&#8230;</code></p>
<dd> Mock options for the build. Defaults to &#8211;no-cleanup-after, you might want this along with other options you provide.</p>
<dt><code>&#8211;no-report</code></p>
<dd> Do not generate the review template.</p>
<dt><code>&#8211;no-build</code></p>
<dd> Do not rebuild or install the source rpm, instead use the last installed package available in mock. Implies &#8211;cache.</p>
<dt><code>&#8211;other_bz</code></p>
<dd> Url of alternative bugzilla, instead of using default <a rel="nofollow" href="https://bugzilla.redhat.com">https://bugzilla.redhat.com</a></p>
<dt><code>-p, &#8211;prebuilt</code></p>
<dd> When using -n &lt;name&gt;, use prebuilt rpms in current directory instead of building new ones in mock</p>
<dt><code>-P, &#8211;plugins</code></p>
<dd> Normally, the right plugin(s) to run are autodetected. Using &#8211;plugins overrides the decision to run a plugin or not. The argument is a comma-separated list of plugins, each possibly with a :off suffix e. g.,</p>
<dt>
<dd> &#8211;plugins Java:off,C/C++</dl>
<dl>
<dt>
<dd> Use &#8211;display-plugins to see available plugins. Enabling plugins has no well-defined semantics: some tests might leave no trace in the report even though they are actually run.</p>
<dt><code>-r, &#8211;rpm-spec</code></p>
<dd> Instead of using a spec file URL, use the spec file bundled in the srpm file.</p>
<dt><code>-s test, &#8211;single test</code></p>
<dd> Run a single test, as listed by &#8211;display-checks. Does not run dependencies, only the given test.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Provides a more detailed output of what&#8217;s going on.</p>
<dt><code>-x test1, test2, &#8230;, &#8211;exclude test1, test2, &#8230;</code></p>
<dd> Comma-separated list of test(s) to exclude, as listed by &#8211;display-checks. A test which depends on an excluded test, will run.</dl>
<h2>THE REVIEW DIRECTORY</h2>
<p> The review directory is created with a name corresponding to the command line options. The package name is always part of the name, sometime also the bug number. Here is:</p>
<dl>
<dt>review.txt</p>
<dd> The review template</p>
<dt>report.xml</p>
<dd> Report with failed issues based on the firehose xml format. This is as yet experimental and not stable. See <a rel="nofollow" href="https://github.com/fedora-static-analysis/firehose.">https://github.com/fedora-static-analysis/firehose.</a></p>
<dt>srpm directory</p>
<dd> Holds whats downloaded, normally a src.rpm and a spec file. When using &#8211;rpm-spec, here is no .spec file.</p>
<dt>srpm-unpacked directory</p>
<dd> Holds the unpacked content of the src.rpm file.</p>
<dt>upstream directory</p>
<dd> contains sources downloaded from the Source: url in the spec file.</p>
<dt>upstream-unpacked directory</p>
<dd> Occasionally contains the unpacked sources, but is normally empty.</p>
<dt>dependencies</p>
<dd> Used for dependencies specfiles when EXARCH flag is set, otherwise empty.</p>
<dt>BUILD link</p>
<dd> Points to the mock directory containing the sources used in the build. These sources have been created and modifified by the %prep stuff in the spec file. The link is only valid direct after the run, it&#8217;s overwritten next time mock executes.</p>
<dt>results directory</p>
<dd> Contains the result from the build, logs and rpm packages.</dl>
<h2>LOCAL SOURCES (GIT-BASED OR SIMILAR)</h2>
<p> Normally, the Source0 (or others SourceX) in the specfile contains an URL to the upstream source. fedora-review uses this url to download the upstream source and then compare md5sum with source in rpm. </p>
<p> However, in some cases the Source0: is just a filename e. g., when sources are generated from git, svn or similar tools. In these cases, fedora-review will look for a file matching the Source0 in current directory. If it exists, it&#8217;s used as upstream source. This way, a reviewer can generate the source according the comments in the spec before running fedora-review and then have it checked.</p>
<h2>USING KOJI SCRATCH BUILDS</h2>
<p> It&#8217;s possible to use koji to build packages instead of mock when using fedora-review. The basic idea is to run a koji scratch build, download the built packages and invoke fedora-review on these. This workflow uses the &#8211;prebuilt option, and has some limitations on checks performed since fedora-review cannot access the build directories. </p>
<p> The workflow:</p>
<dl>
<dt>&bull;</p>
<dd> Invoke koji, note the task number:</p>
<dt>
<dd> koji build &#8211;scratch my-package.src.rpm</p>
<dt>&bull;</p>
<dd> Download the results:</p>
<dt>
<dd> koji-download-scratch &lt;task number&gt;</p>
<dt>&bull;</p>
<dd> Invoke fedora-review using &#8211;prebuilt, &#8211;name options and &#8211;rpmspec:</p>
<dt>
<dd> fedora-review &#8211;rpm-spec &#8211;prebuilt &#8211;name my-package </p>
</dl>
<h2>URL limitations</h2>
<p> fedora-review handles two types of URL: the spec and srpm url found in e. g. the bugzilla page, and the source url(s) found in the spec file. </p>
<p> For the srpm and spec file url:</p>
<dl>
<dt>&bull;</p>
<dd> The parameters (i. e., the ? and everything beyond) is removed.</p>
<dt>&bull;</p>
<dd> The rest must end with /*.spec or /*.src.rpm </p>
</dl>
<p> For the source url, possible parameters are <code>not</code> removed. It must end with /filename, typically something like /package-2.0.1.tar.gz </p>
<h2>EXAMPLES</h2>
<p> Make a report template for Fedora bug 817271:</p>
<dl>
<dt>
<dd> $ fedora-review -b 817271</dl>
<p> fetches spec and srpm file from bugzilla.redhat.com and makes a report. To instead handle a bug at rpmfusion use something like</p>
<dl>
<dt>
<dd> $ fedora-review &#8211;url \<br />
 <a rel="nofollow" href="https://bugzilla.rpmfusion.org/show_bug.cgi?id=2150">https://bugzilla.rpmfusion.org/show_bug.cgi?id=2150</a> \<br />
 &#8211;mock-config fedora-16-i386-rpmfusion_free</dl>
<p> Occasionally, fedora-review isn&#8217;t able to pick up the links e. g., when the links does not end in .spec and/or .src.rpm. In these case you need to download files manually. Using &#8211;rpm-spec only the srpm is needed: </p>
<pre>
<dl>
<dt><dd>$ wget <a rel="nofollow" href="http://somewhere.com/bad-srpmlink">http://somewhere.com/bad-srpmlink</a> -O my-package-1.2-1.fc16.src.rpm
$ fedora-review --rpm-spec -n my-package-1.2-1.fc16.src.rpm
</pre>
</dl>
<h2>FILES</h2>
<p> <i>~/.cache/fedora-review.log</i></p>
<dl>
<dt>
<dd> Debug logging from last session.</dl>
<p> <i>/usr/share/fedora-review/plugins</i></p>
<dl>
<dt>
<dd> System-wide python plugins directory</dl>
<p> <i>/usr/share/fedora-review/scripts</i></p>
<dl>
<dt>
<dd> System-wide scripts directory</dl>
<p> <i>~/.local/share/fedora-review/plugins/</i></p>
<dl>
<dt>
<dd> User supplied directory for python plugins</dl>
<p> <i>~/.local/share/fedora-review/scripts/</i></p>
<dl>
<dt>
<dd> User supplied directory with shell-based plugins </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>REVIEW_LOGLEVEL</code></p>
<dd> loglevel used when not using -v/&#8211;verbose. A logging.* value like &#8216;DEBUG&#8217;, &#8216;Info&#8217;, or &#8216;warning&#8217;. Setting REVIEW_LOGLEVEL to &#8216;debug&#8217; is the same as providing the -v/&#8211;verbose option.</p>
<dt><code>REVIEW_NO_MOCKGROUP_CHECK</code></p>
<dd> Normally, fedora-review checks that user is member of the mock group before proceeding since this is required to run mock in most setups. In cases this check is not useful it can be suppressed by this variable.</p>
<dt><code>XDG_DATA_HOME</code></p>
<dd> fedora-review respects XDG_DATA_HOME which defaults to ~/.local/share. E. g., the personal data directory with plugins is by default ~/.local/share/fedora-review/plugins, but is $XDG_DATA_HOME/fedora-review/plugins if XDG_DATA_HOME is set. See FILES.</p>
<dt><code>XDG_CACHE_HOME</code></p>
<dd> If set, defines the directory where the logfile fedora-review.log is written. Defaults to ~/.cache. </p>
</dl>
<h2>AUTHORS</h2>
<p> Original author: Tim Lauridsen &lt;tim.lauridsen [at] gmail.com&gt; </p>
<p> Developers:<br />
&nbsp;<wbr>Pierre-Yves Chibon&nbsp;<wbr>&lt;pingou [at] pingoured.fr&gt;<br />
&nbsp;<wbr>Alec Leamas&nbsp;<wbr>&lt;leamas.alec [at] maybe.gmail&gt;<br />
&nbsp;<wbr>Stanislav Ochotnicky&nbsp;<wbr>&lt;sochotnicky [at] redhat.com&gt; </p>
<p> For a list of all contributors see AUTHORS file </p>
<h2>SEE ALSO</h2>
<dl>
<dt><a href="/docs/linux/man/1-bugzilla/">bugzilla</a>(1)</p>
<dd> CLI tool to create and modify bugzilla bug tickets.</p>
<dt><a rel="nofollow" href="https://fedorahosted.org/FedoraReview/">https://fedorahosted.org/FedoraReview/</a></p>
<dd> source, issue tracker, etc.</p>
<dt><a rel="nofollow" href="http://fedoraproject.org/wiki/Packaging:Guidelines">http://fedoraproject.org/wiki/Packaging:Guidelines</a></p>
<dd> Rules for Fedora packages. </p>
</dl>
<h2>Index</h2>
