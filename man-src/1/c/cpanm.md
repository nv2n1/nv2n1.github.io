---
title: "cpanm(1)"
name: "cpanm"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpanm/"
description: "cpanm – get, unpack build and install modules from CPAN"
---

<h2 class="name">NAME</h2>
<p> cpanm &#8211; get, unpack build and install modules from CPAN </p>
<h2>SYNOPSIS</h2>
<pre><code>
  cpanm Test::More                                 # install Test::More
  cpanm MIYAGAWA/Plack-0.99_05.tar.gz              # full distribution path
  cpanm http://example.org/LDS/CGI.pm-3.20.tar.gz  # install from URL
  cpanm ~/dists/MyCompany-Enterprise-1.00.tar.gz   # install from a local file
  cpanm --interactive Task::Kensho                 # Configure interactively
  cpanm .                                          # install from local directory
  cpanm --installdeps .                            # install all the deps for the current directory
  cpanm -L extlib Plack                            # install Plack and all non-core deps into extlib
  cpanm --mirror http://cpan.cpantesters.org/ DBI  # use the fast-syncing mirror
</code></pre>
<h2>COMMANDS</h2>
<dl>
<dt>(arguments)</p>
<dd> Command line arguments can be either a module name, distribution file, local file path, <font SIZE="-1">HTTP URL</font> or git repository <font SIZE="-1">URL.</font> Following commands will all work as you expect. </p>
<pre>
    cpanm Plack
    cpanm Plack/Request.pm
    cpanm MIYAGAWA/Plack-1.0000.tar.gz
    cpanm /path/to/Plack-1.0000.tar.gz
    cpanm <a rel="nofollow" href="http://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-0.9990.tar.gz">http://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-0.9990.tar.gz</a>
    cpanm <a href="git://github.com/miyagawa/Plack.git">git://github.com/miyagawa/Plack.git</a>
</pre>
<p> Additionally, you can use the notation using <tt>&quot;~&quot;</tt> and <tt>&quot;@&quot;</tt> to specify version for a given module. <tt>&quot;~&quot;</tt> specifies the version requirement in the CPAN::Meta::Spec format, while <tt>&quot;@&quot;</tt> pins the exact version, and is a shortcut for <tt>&quot;~&quot;== VERSION&quot;&quot;</tt>. </p>
<p>cpanm Plack ~1.0000 #1.0000 or later<br />
                                   cpanm Plack ~&#8221;&gt;= 1.0000, &lt; 2.0000&#8243; #latest of 1.xxxx cpanm Plack[at] 0.9990 #specific version.same as Plack ~&#8221;== 0.9990&#8243;</p>
<p> The version query including specific version or range will be sent to MetaCPAN to search for previous releases. The query will search for BackPAN archives by default, unless you specify <tt>&quot;--dev&quot;</tt> option, in which case, archived versions will be filtered out. </p>
<p> For a git repository, you can specify a branch, tag, or commit <font SIZE="-1">SHA</font> to build. The default is <tt>&quot;master&quot;</tt> </p>
<pre>
    cpanm <a href="git://github.com/miyagawa/Plack.git@1.0000">git://github.com/miyagawa/Plack.git@1.0000</a>        # tag
    cpanm <a href="git://github.com/miyagawa/Plack.git@devel">git://github.com/miyagawa/Plack.git@devel</a>         # branch
</pre>
<dt>-i, &#8211;install</p>
<dd> Installs the modules. This is a default behavior and this is just a compatibility option to make it work like cpan or cpanp.</p>
<dt>&#8211;self-upgrade</p>
<dd> Upgrades itself. It&#8217;s just an alias for: </p>
<pre>
  cpanm App::cpanminus
</pre>
<dt>&#8211;info</p>
<dd> Displays the distribution information in <tt>&quot;AUTHOR/Dist-Name-ver.tar.gz&quot;</tt> format in the standard out.</p>
<dt>&#8211;installdeps</p>
<dd> Installs the dependencies of the target distribution but won&#8217;t build itself. Handy if you want to try the application from a version controlled repository such as git. </p>
<pre>
  cpanm --installdeps .
</pre>
<dt>&#8211;look</p>
<dd> Download and unpack the distribution and then open the directory with your shell. Handy to poke around the source code or do manual testing.</p>
<dt>-U, &#8211;uninstall</p>
<dd> <font SIZE="-1"><code>EXPERIMENTAL</code></font>: Uninstalls the modules. Will remove the distribution files from your library path using the <tt>&quot;.packlist&quot;</tt> file. </p>
<p> When used with <tt>&quot;-l&quot;</tt> or <tt>&quot;-L&quot;</tt>, only the files under the local::lib directory will be removed. </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: If you have the &#8220;dual-life&#8221; module in multiple locations (i.e. <tt>&quot;site_perl&quot;</tt> and <tt>&quot;perl&quot;</tt> library path, with perl 5.12 or later), only the files in <tt>&quot;site_perl&quot;</tt> will be deleted. </p>
<p> If the distribution has bin scripts and man, they will be kept in case the core installation still references that, although there&#8217;s no guarantee that the script will continue working as expected with the older version of .pm files.</p>
<dt>-h, &#8211;help</p>
<dd> Displays the help message.</p>
<dt>-V, &#8211;version</p>
<dd> Displays the version number.</dl>
<h2>OPTIONS</h2>
<p> You can specify the default options in <tt>&quot;PERL_CPANM_OPT&quot;</tt> environment variable.</p>
<dl>
<dt>-f, &#8211;force</p>
<dd> Force install modules even when testing failed.</p>
<dt>-n, &#8211;notest</p>
<dd> Skip the testing of modules. Use this only when you just want to save time for installing hundreds of distributions to the same perl and architecture you&#8217;ve already tested to make sure it builds fine. </p>
<p> Defaults to false, and you can say <tt>&quot;--no-notest&quot;</tt> to override when it is set in the default options in <tt>&quot;PERL_CPANM_OPT&quot;</tt>.</p>
<dt>&#8211;test-only</p>
<dd> Run the tests only, and do not install the specified module or distributions. Handy if you want to verify the new (or even old) releases pass its unit tests without installing the module. </p>
<p> Note that if you specify this option with a module or distribution that has dependencies, these dependencies will be installed if you don&#8217;t currently have them.</p>
<dt>-S, &#8211;sudo</p>
<dd> Switch to the root user with <tt>&quot;sudo&quot;</tt> when installing modules. Use this if you want to install modules to the system perl include path. </p>
<p> Defaults to false, and you can say <tt>&quot;--no-sudo&quot;</tt> to override when it is set in the default options in <tt>&quot;PERL_CPANM_OPT&quot;</tt>.</p>
<dt>-v, &#8211;verbose</p>
<dd> Makes the output verbose. It also enables the interactive configuration. (See &#8211;interactive)</p>
<dt>-q, &#8211;quiet</p>
<dd> Makes the output even more quiet than the default. It only shows the successful/failed dependencies to the output.</p>
<dt>-l, &#8211;local-lib</p>
<dd> Sets the local::lib compatible path to install modules to. You don&#8217;t need to set this if you already configure the shell environment variables using local::lib, but this can be used to override that as well.</p>
<dt>-L, &#8211;local-lib-contained</p>
<dd> Same with <tt>&quot;--local-lib&quot;</tt> but with &#8211;self-contained set. All non-core dependencies will be installed even if they&#8217;re already installed. </p>
<p> For instance, </p>
<pre>
  cpanm -L extlib Plack
</pre>
<p> would install Plack and all of its non-core dependencies into the directory <tt>&quot;extlib&quot;</tt>, which can be loaded from your application with: </p>
<pre>
  use local::lib '/path/to/extlib';
</pre>
<dt>&#8211;self-contained</p>
<dd> When examining the dependencies, assume no non-core modules are installed on the system. Handy if you want to bundle application dependencies in one directory so you can distribute to other machines.</p>
<dt>&#8211;mirror</p>
<dd> Specifies the base <font SIZE="-1">URL</font> for the <font SIZE="-1">CPAN</font> mirror to use, such as <tt>&quot;<a rel="nofollow" href="http://cpan.cpantesters.org/">http://cpan.cpantesters.org/</a>&quot;</tt> (you can omit the trailing slash). You can specify multiple mirror URLs by repeating the command line option. </p>
<p> You can use a local directory that has a <font SIZE="-1">CPAN</font> mirror structure (created by tools such as OrePAN or Pinto) by using a special <font SIZE="-1">URL</font> scheme <tt>&quot;file://&quot;</tt>. If the given <font SIZE="-1">URL</font> begins with `/` (without any scheme), it is considered as a file scheme as well. </p>
<pre>
  cpanm --mirror file:///path/to/mirror
  cpanm --mirror ~/minicpan      # Because shell expands ~ to /home/user
</pre>
<p> Defaults to <tt>&quot;<a rel="nofollow" href="http://www.cpan.org/">http://www.cpan.org/</a>&quot;</tt>.</p>
<dt>&#8211;mirror-only</p>
<dd> Download the mirror&#8217;s 02packages.details.txt.gz index file instead of querying the <font SIZE="-1">CPAN</font> Meta <font SIZE="-1">DB.</font> This will also effectively opt out sending your local perl versions to backend database servers such as <font SIZE="-1">CPAN</font> Meta <font SIZE="-1">DB</font> and MetaCPAN. </p>
<p> Select this option if you are using a local mirror of <font SIZE="-1">CPAN,</font> such as minicpan when you&#8217;re offline, or your own <font SIZE="-1">CPAN</font> index (a.k.a darkpan). </p>
<p> <code>Tip:</code> It might be useful if you name these mirror options with your shell aliases, like: </p>
<pre><code>
alias minicpanm = 'cpanm --mirror ~/minicpan --mirror-only' alias darkpan = 'cpanm --mirror http://mycompany.example.com/DPAN --mirror-only'
</code></pre>
<dt>&#8211;mirror-index</p>
<dd> <font SIZE="-1"><code>EXPERIMENTAL</code></font>: Specifies the file path to <tt>&quot;02packages.details.txt&quot;</tt> for module search index.</p>
<dt>&#8211;prompt</p>
<dd> Prompts when a test fails so that you can skip, force install, retry or look in the shell to see what&#8217;s going wrong. It also prompts when one of the dependency failed if you want to proceed the installation. </p>
<p> Defaults to false, and you can say <tt>&quot;--no-prompt&quot;</tt> to override if it&#8217;s set in the default options in <tt>&quot;PERL_CPANM_OPT&quot;</tt>.</p>
<dt>&#8211;dev</p>
<dd> <font SIZE="-1"><code>EXPERIMENTAL</code></font>: search for a newer developer release as well. Defaults to false.</p>
<dt>&#8211;reinstall</p>
<dd> cpanm, when given a module name in the command line (i.e. <tt>&quot;cpanm Plack&quot;</tt>), checks the locally installed version first and skips if it is already installed. This option makes it skip the check, so: </p>
<pre>
  cpanm --reinstall Plack
</pre>
<p> would reinstall Plack even if your locally installed version is latest, or even newer (which would happen if you install a developer release from version control repositories). </p>
<p> Defaults to false.</p>
<dt>&#8211;interactive</p>
<dd> Makes the configuration (such as <tt>&quot;Makefile.PL&quot;</tt> and <tt>&quot;Build.PL&quot;</tt>) interactive, so you can answer questions in the distribution that requires custom configuration or Task:: distributions. </p>
<p> Defaults to false, and you can say <tt>&quot;--no-interactive&quot;</tt> to override when it&#8217;s set in the default options in <tt>&quot;PERL_CPANM_OPT&quot;</tt>.</p>
<dt>&#8211;pp, &#8211;pureperl</p>
<dd> Prefer Pure perl build of modules by setting <tt>&quot;PUREPERL_ONLY=1&quot;</tt> for MakeMaker and <tt>&quot;--pureperl-only&quot;</tt> for Build.PL based distributions. Note that not all of the <font SIZE="-1">CPAN</font> modules support this convention yet.</p>
<dt>&#8211;with-recommends, &#8211;with-suggests</p>
<dd> <font SIZE="-1"><code>EXPERIMENTAL</code></font>: Installs dependencies declared as <tt>&quot;recommends&quot;</tt> and <tt>&quot;suggests&quot;</tt> respectively, per <font SIZE="-1">META</font> spec. When these dependencies fail to install, cpanm continues the installation, since they&#8217;re just recommendation/suggestion. </p>
<p> Enabling this could potentially make a circular dependency for a few modules on <font SIZE="-1">CPAN,</font> when <tt>&quot;recommends&quot;</tt> adds a module that <tt>&quot;recommends&quot;</tt> back the module in return. </p>
<p> There&#8217;s also <tt>&quot;--without-recommend&quot;</tt> and <tt>&quot;--without-suggests&quot;</tt> to override the default decision made earlier in <tt>&quot;PERL_CPANM_OPT&quot;</tt>. </p>
<p> Defaults to false for both.</p>
<dt>&#8211;with-feature, &#8211;without-feature, &#8211;with-all-features</p>
<dd> <font SIZE="-1"><code>EXPERIMENTAL</code></font>: Specifies the feature to enable, if a module supports optional features per <font SIZE="-1">META</font> spec 2.0. </p>
<pre>
    cpanm --with-feature=opt_csv Spreadsheet::Read
</pre>
<p> the features can also be interactively chosen when <tt>&quot;--interactive&quot;</tt> option is enabled. </p>
<p> <tt>&quot;--with-all-features&quot;</tt> enables all the optional features, and <tt>&quot;--without-feature&quot;</tt> can select a feature to disable.</p>
<dt>&#8211;configure-timeout, &#8211;build-timeout, &#8211;test-timeout</p>
<dd> Specify the timeout length (in seconds) to wait for the configure, build and test process. Current default values are: 60 for configure, 3600 for build and 1800 for test.</p>
<dt>&#8211;configure-args, &#8211;build-args, &#8211;test-args, &#8211;install-args</p>
<dd> <font SIZE="-1"><code>EXPERIMENTAL</code></font>: Pass arguments for configure/build/test/install commands respectively, for a given module to install. </p>
<pre>
    cpanm DBD::mysql --configure-args=&quot;--cflags=... --libs=...&quot;
</pre>
<p> The argument is only enabled for the module passed as a command line argument, not dependencies.</p>
<dt>&#8211;scandeps</p>
<dd> Scans the depencencies of given modules and output the tree in a text format. (See <tt>&quot;--format&quot;</tt> below for more options) </p>
<p> Because this command doesn&#8217;t actually install any distributions, it will be useful that by typing: </p>
<pre>
  cpanm --scandeps Catalyst::Runtime
</pre>
<p> you can make sure what modules will be installed. </p>
<p> This command takes into account which modules you already have installed in your system. If you want to see what modules will be installed against a vanilla perl installation, you might want to combine it with <tt>&quot;-L&quot;</tt> option.</p>
<dt>&#8211;format</p>
<dd> Determines what format to display the scanned dependency tree. Available options are <tt>&quot;tree&quot;</tt>, <tt>&quot;json&quot;</tt>, <tt>&quot;yaml&quot;</tt> and <tt>&quot;dists&quot;</tt>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>tree</p>
<dd> Displays the tree in a plain text format. This is the default value.</p>
<dt>json, yaml</p>
<dd> Outputs the tree in a <font SIZE="-1">JSON</font> or <font SIZE="-1">YAML</font> format. <font SIZE="-1">JSON</font> and <font SIZE="-1">YAML</font> modules need to be installed respectively. The output tree is represented as a recursive tuple of: </p>
<pre>
  [ distribution, dependencies ]
</pre>
<p> and the container is an array containing the root elements. Note that there may be multiple root nodes, since you can give multiple modules to the <tt>&quot;--scandeps&quot;</tt> command.</p>
<dt>dists</p>
<dd> <tt>&quot;dists&quot;</tt> is a special output format, where it prints the distribution filename in the <i>depth first order</i> after the dependency resolution, like: </p>
<pre>
  GAAS/MIME-Base64-3.13.tar.gz
  GAAS/URI-1.58.tar.gz
  PETDANCE/HTML-Tagset-3.20.tar.gz
  GAAS/HTML-Parser-3.68.tar.gz
  GAAS/libwww-perl-5.837.tar.gz
</pre>
<p> which means you can install these distributions in this order without extra dependencies. When combined with <tt>&quot;-L&quot;</tt> option, it will be useful to replay installations on other machines.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&#8211;save-dists</p>
<dd> Specifies the optional directory path to copy downloaded tarballs in the <font SIZE="-1">CPAN</font> mirror compatible directory structure i.e. <i>authors/id/A/AU/AUTHORS/Foo-Bar-version.tar.gz</i> </p>
<p> If the distro tarball did not come from <font SIZE="-1">CPAN,</font> for example from a local file or from GitHub, then it will be saved under <i>vendor/Foo-Bar-version.tar.gz</i>.</p>
<dt>&#8211;uninst-shadows</p>
<dd> Uninstalls the shadow files of the distribution that you&#8217;re installing. This eliminates the confusion if you&#8217;re trying to install core (dual-life) modules from <font SIZE="-1">CPAN</font> against perl 5.10 or older, or modules that used to be XS-based but switched to pure perl at some version. </p>
<p> If you run cpanm as root and use <tt>&quot;INSTALL_BASE&quot;</tt> or equivalent to specify custom installation path, you <font SIZE="-1">SHOULD</font> disable this option so you won&#8217;t accidentally uninstall dual-life modules from the core include path. </p>
<p> Defaults to true if your perl version is smaller than 5.12, and you can disable that with <tt>&quot;--no-uninst-shadows&quot;</tt>. </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: Since version 1.3000 this flag is turned off by default for perl newer than 5.12, since with 5.12 <tt>@INC</tt> contains site_perl directory <i>before</i> the perl core library path, and uninstalling shadows is not necessary anymore and does more harm by deleting files from the core library path.</p>
<dt>&#8211;uninstall, -U</p>
<dd> Uninstalls a module from the library path. It finds a packlist for given modules, and removes all the files included in the same distribution. </p>
<p> If you enable local::lib, it only removes files from the local::lib directory. </p>
<p> If you try to uninstall a module in <tt>&quot;perl&quot;</tt> directory (i.e. core module), an error will be thrown. </p>
<p> A dialog wil be prompted to confirm the files to be deleted. If you pass <tt>&quot;-f&quot;</tt> option as well, the dialog will be skipped and uninstallation will be forced.</p>
<dt>&#8211;cascade-search</p>
<dd> <font SIZE="-1"><code>EXPERIMENTAL</code></font>: Specifies whether to cascade search when you specify multiple mirrors and a mirror doesn&#8217;t have a module or has a lower version of the module than requested. Defaults to false.</p>
<dt>&#8211;skip-installed</p>
<dd> Specifies whether a module given in the command line is skipped if its latest version is already installed. Defaults to true. </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: The <tt>&quot;PERL5LIB&quot;</tt> environment variable have to be correctly set for this to work with modules installed using local::lib, unless you always use the <tt>&quot;-l&quot;</tt> option.</p>
<dt>&#8211;skip-satisfied</p>
<dd> <font SIZE="-1"><code>EXPERIMENTAL</code></font>: Specifies whether a module (and version) given in the command line is skipped if it&#8217;s already installed. </p>
<p> If you run: </p>
<pre>
  cpanm --skip-satisfied CGI DBI~1.2
</pre>
<p> cpanm won&#8217;t install them if you already have <font SIZE="-1">CGI </font>(for whatever versions) or have <font SIZE="-1">DBI</font> with version higher than 1.2. It is similar to <tt>&quot;--skip-installed&quot;</tt> but while <tt>&quot;--skip-installed&quot;</tt> checks if the <i>latest</i> version of <font SIZE="-1">CPAN</font> is installed, <tt>&quot;--skip-satisfied&quot;</tt> checks if a requested version (or not, which means any version) is installed. </p>
<p> Defaults to false.</p>
<dt>&#8211;verify</p>
<dd> Verify the integrity of distribution files retrieved from <font SIZE="-1">PAUSE</font> using <font SIZE="-1">CHECKSUMS</font> and <font SIZE="-1">SIGNATURES </font>(if found). Defaults to false.</p>
<dt>&#8211;report-perl-version</p>
<dd> Whether it report the locally installed perl version to the various web server as part of User-Agent. Defaults to true, and you can disable it by using <tt>&quot;--no-report-perl-version&quot;</tt>.</p>
<dt>&#8211;auto-cleanup</p>
<dd> Specifies the number of days in which cpanm&#8217;s work directories expire. Defaults to 7, which means old work directories will be cleaned up in one week. </p>
<p> You can set the value to <tt>0</tt> to make cpan never cleanup those directories.</p>
<dt>&#8211;man-pages</p>
<dd> Generates man pages for executables (man1) and libraries (man3). </p>
<p> Defaults to true (man pages generated) unless <tt>&quot;-L|--local-lib-contained&quot;</tt> option is supplied in which case it&#8217;s set to false. You can disable it with <tt>&quot;--no-man-pages&quot;</tt>.</p>
<dt>&#8211;lwp</p>
<dd> Uses <font SIZE="-1">LWP</font> module to download stuff over <font SIZE="-1">HTTP.</font> Defaults to true, and you can say <tt>&quot;--no-lwp&quot;</tt> to disable using <font SIZE="-1">LWP,</font> when you want to upgrade <font SIZE="-1">LWP</font> from <font SIZE="-1">CPAN</font> on some broken perl systems.</p>
<dt>&#8211;wget</p>
<dd> Uses <font SIZE="-1">GNU</font> Wget (if available) to download stuff. Defaults to true, and you can say <tt>&quot;--no-wget&quot;</tt> to disable using Wget (versions of Wget older than 1.9 don&#8217;t support the <tt>&quot;--retry-connrefused&quot;</tt> option used by cpanm).</p>
<dt>&#8211;curl</p>
<dd> Uses cURL (if available) to download stuff. Defaults to true, and you can say <tt>&quot;--no-curl&quot;</tt> to disable using cURL. </p>
<p> Normally with <tt>&quot;--lwp&quot;</tt>, <tt>&quot;--wget&quot;</tt> and <tt>&quot;--curl&quot;</tt> options set to true (which is the default) cpanm tries <font SIZE="-1">LWP</font>, Wget, cURL and HTTP::Tiny (in that order) and uses the first one available.</dl>
<h2>SEE ALSO</h2>
<p> App::cpanminus</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2010 Tatsuhiko Miyagawa.</p>
<h2>AUTHOR</h2>
<p> Tatsuhiko Miyagawa </p>
<h2>Index</h2>
