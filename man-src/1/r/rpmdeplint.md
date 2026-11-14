---
title: "rpmdeplint(1)"
name: "rpmdeplint"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmdeplint/"
description: "rpmdeplint – a tool to find errors in RPM packages in the context of their dependency graph"
---

<h2>NAME</h2>
<p> rpmdeplint &#8211; a tool to find errors in RPM packages in the context of their dependency graph</p>
<h2>SYNOPSIS</h2>
<pre><code>
rpmdeplint COMMAND[--repo NAME, PATH][RPMPATH]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>rpmdeplint</code> command will test dependency satisfiability of given RPM packages against given repositories.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;repo NAME,PATH</code></p>
<dd> You can provide multiple repos of each type. The NAME may be anything you choose. The path must either be a filesystem path or a URL. In either case, the path is expected to point at <i>repodata/repomd.xml</i>.</p>
<dt><code>&#8211;repos-from-system</code></p>
<dd> Use yum repos from the system-wide configuration in <code>/etc/yum.conf</code> and <code>/etc/yum.repos.d/</code><i>*</i>.repo. Repos which are disabled in the configuration (<code>enabled=0</code>) are ignored. </p>
<p> This option can be combined with one or more <i>&#8211;repo</i> options.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>RPMPATH</code></p>
<dd> Path to an RPM package. This can be a relative or absolute filesystem path.</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>check</code></p>
<dd> Performs each of the checks listed below.</p>
<dt><code>check-sat</code></p>
<dd> Checks for unmet dependencies with the given RPM packages against the given repositories. Each unmet dependency is listed.</p>
<dt><code>check-repoclosure</code></p>
<dd> Checks for unmet dependencies in the given repositories, when considered together with the given packages. This check is similar to <i>check-sat</i>, except it checks only packages in the repositories, not the packages under test. </p>
<p> Packages are only considered to be available for dependency resolution if they are the latest version and not obsoleted by any other package. Therefore this check can detect problems where a package under test is updating an existing package in the repositories, but it no longer provides a requirement needed by some other package in the repositories. </p>
<p> In case a pre-existing repoclosure problem is found (that is, the same problem exists when considering only the repositories without the packages under test) a warning is printed to stderr, but the check is <i>not</i> considered to have failed.</p>
<dt><code>check-conflicts</code></p>
<dd> Checks for undeclared file conflicts in the given RPM packages: that is, when one of the given package contains a file which is also contained in some other package. </p>
<p> This command will not report a file as conflicting between two packages if:</p>
<dt>&bull;</p>
<dd> there is an explicit RPM <code>Conflicts</code> between the two packages; or</p>
<dt>&bull;</p>
<dd> the file’s checksum, permissions, owner, and group are identical in both packages (RPM allows both packages to own the file in this case); or</p>
<dt>&bull;</p>
<dd> the file’s color is different between the two packages (RPM will silently resolve the conflict in favour of the 64-bit file).</p>
<dt><code>check-upgrade</code></p>
<dd> Checks that there are no existing packages in the repositories which would upgrade or obsolete the given packages. </p>
<p> If this check fails, it means that the package under test will never be installed (since the package manager will always pick the newer or obsoleting package from the repositories instead) which is not desirable, assuming the package is intended as an update.</p>
<dt><code>list-deps</code></p>
<dd> All dependencies will be listed for each given RPM package.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> Normally, exit status is 0 if rpmdeplint executes successfully.</p>
<dt><code>1</code></p>
<dd> Errors that result in tracebacks, such as infrastructure errors.</p>
<dt><code>2</code></p>
<dd> Usage error, in case of incorrect use of commands or options.</p>
<dt><code>3</code></p>
<dd> Failure of a test.</dl>
<h2>EXAMPLES</h2>
<p> Test if an RPM package has unsatisfied dependencies against a remote repository: </p>
<pre>
rpmdeplint check-sat --repo beaker,<a rel="nofollow" href="https://beaker-project.org/yum/client/Fedora23/">https://beaker-project.org/yum/client/Fedora23/</a> my-package.rpm
  Problems with dependency set:
  nothing provides python(abi) = 2.7 needed by some-package-1.2.3.fc23.noarch
  nothing provides TurboGears &gt;= 1.1.3 needed by other-package-33.2-1.fc23.noarch
</pre>
<p> List all dependencies for <i>my-package.rpm</i>: </p>
<pre>
rpmdeplint list-deps --repo beaker,<a rel="nofollow" href="https://beaker-project.org/yum/client/Fedora23/">https://beaker-project.org/yum/client/Fedora23/</a> my-package.rpm
  my-package has 72 dependencies:
          basesystem-11-1.fc23.noarch
          bash-4.3.42-1.fc23.x86_64
          beaker-common-22.1-1.fc22.noarch
          ....
</pre>
<h2>BUGS</h2>
<p> Bug reports can be submitted to <i><a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a></i>.</p>
<h2>AUTHOR</h2>
<p> rpmdeplint contributors</p>
<h2>COPYRIGHT</h2>
<p> 2016, Red Hat </p>
<h2>Index</h2>
