---
title: "apt_preferences(5)"
name: "apt_preferences"
section: "5"
letter: "a"
url: "/docs/linux/man/5-apt_preferences/"
description: "apt_preferences – Preference control file for APT"
---

<p>apt_preferences &#8211; Preference control file for APT</p>
<h2>Description</h2>
<p>The APT preferences file /etc/apt/preferences and the fragment files in the /etc/apt/preferences.d/ folder can be used to control which versions of packages will be selected for installation. </p>
<p> Several versions of a package may be available for installation when the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file contains references to more than one distribution (for example, stable and testing). APT assigns a priority to each version that is available. Subject to dependency constraints, <code>apt-get</code> selects the version with the highest priority for installation. The APT preferences override the priorities that APT assigns to package versions by default, thus giving the user control over which one is selected for installation. </p>
<p> Several instances of the same version of a package may be available when the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file contains references to more than one source. In this case <code>apt-get</code> downloads the instance listed earliest in the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file. The APT preferences do not affect the choice of instance, only the choice of version. </p>
<p> Preferences are a strong power in the hands of a system administrator but they can become also their biggest nightmare if used without care! APT will not question the preferences, so wrong settings can lead to uninstallable packages or wrong decisions while upgrading packages. Even more problems will arise if multiple distribution releases are mixed without a good understanding of the following paragraphs. Packages included in a specific release aren&#8217;t tested in (and therefore don&#8217;t always work as expected in) older or newer releases, or together with other packages from different releases. You have been warned. </p>
<p> Note that the files in the /etc/apt/preferences.d directory are parsed in alphanumeric ascending order and need to obey the following naming convention: The files have either no or &quot;pref&quot; as filename extension and only contain alphanumeric, hyphen (-), underscore (_) and period (.) characters. Otherwise APT will print a notice that it has ignored a file, unless that file matches a pattern in the Dir::Ignore-Files-Silently configuration list &#8211; in which case it will be silently ignored.</p>
<h3>APT&#8217;s Default Priority Assignments</h3>
<p>If there is no preferences file or if there is no entry in the file that applies to a particular version then the priority assigned to that version is the priority of the distribution to which that version belongs. It is possible to single out a distribution, &quot;the target release&quot;, which receives a higher priority than other distributions do by default. The target release can be set on the <code>apt-get</code> command line or in the APT configuration file /etc/apt/apt.conf. Note that this has precedence over any general priority you set in the /etc/apt/preferences file described later, but not over specifically pinned packages. For example, </p>
<dl>
<dd>
<pre><code>apt-get install -t testing </code><i>some-package</i></pre>
</dl>
<dl>
<dd>
<pre>APT::Default-Release &quot;stable&quot;;</pre>
</dl>
<p> If the target release has been specified then APT uses the following algorithm to set the priorities of the versions of a package. Assign: </p>
<p> priority 1</p>
<dl>
<dd>to the versions coming from archives which in their Release files are marked as &quot;NotAutomatic: yes&quot; but <i>not</i> as &quot;ButAutomaticUpgrades: yes&quot; like the Debian experimental archive, as well as versions that are not phased on this systems.</dl>
<p> priority 100</p>
<dl>
<dd>to the version that is already installed (if any) and to the versions coming from archives which in their Release files are marked as &quot;NotAutomatic: yes&quot; and &quot;ButAutomaticUpgrades: yes&quot; like the Debian backports archive since squeeze-backports.</dl>
<p> priority 500</p>
<dl>
<dd>to the versions that do not belong to the target release.</dl>
<p> priority 990</p>
<dl>
<dd>to the versions that belong to the target release.</dl>
<p> The highest of those priorities whose description matches the version is assigned to the version. </p>
<p> If the target release has not been specified then APT simply assigns priority 100 to all installed package versions and priority 500 to all uninstalled package versions, except versions coming from archives which in their Release files are marked as &quot;NotAutomatic: yes&quot; &#8211; these versions get the priority 1 or priority 100 if it is additionally marked as &quot;ButAutomaticUpgrades: yes&quot;. </p>
<p> APT then applies the following rules, listed in order of precedence, to determine which version of a package to install. </p>
<dl>
<dd>&bull; Never downgrade unless the priority of an available version exceeds 1000. (&quot;Downgrading&quot; is installing a less recent version of a package in place of a more recent version. Note that none of APT&#8217;s default priorities exceeds 1000; such high priorities can only be set in the preferences file. Note also that downgrading a package can be risky.)</dl>
<dl>
<dd>&bull; Install the highest priority version.</dl>
<dl>
<dd>&bull; If two or more versions have the same priority, install the most recent one (that is, the one with the higher version number).</dl>
<dl>
<dd>&bull; If two or more versions have the same priority and version number but either the packages differ in some of their metadata or the &#8211;reinstall option is given, install the uninstalled one.</dl>
<p> In a typical situation, the installed version of a package (priority 100) is not as recent as one of the versions available from the sources listed in the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file (priority 500 or 990). Then the package will be upgraded when <code>apt-get install </code><i>some-package</i> or <code>apt-get upgrade</code> is executed. </p>
<p> More rarely, the installed version of a package is <i>more</i> recent than any of the other available versions. The package will not be downgraded when <code>apt-get install </code><i>some-package</i> or <code>apt-get upgrade</code> is executed. </p>
<p> Sometimes the installed version of a package is more recent than the version belonging to the target release, but not as recent as a version belonging to some other distribution. Such a package will indeed be upgraded when <code>apt-get install </code><i>some-package</i> or <code>apt-get upgrade</code> is executed, because at least <i>one</i> of the available versions has a higher priority than the installed version.</p>
<h3>Phased Updates</h3>
<p>APT understands a field called Phased-Update-Percentage which can be used to control the rollout of a new version. It is an integer between 0 and 100. </p>
<p> A system&#8217;s eligibility to a phased update is determined by seeding random number generator with the package source name, the version number, and /etc/machine-id, and then calculating an integer in the range [0, 100]. If this integer is larger than the Phased-Update-Percentage, the version is pinned to 1, and thus held back. Otherwise, normal policy rules apply. </p>
<p> In case you have multiple systems that you want to receive the same set of updates, you can set APT::Machine-ID to a UUID such that they all phase the same, or set APT::Get::Never-Include-Phased-Updates or APT::Get::Always-Include-Phased-Updates to true such that APT will never/always consider phased updates.</p>
<h3>The Effect of APT Preferences</h3>
<p>The APT preferences file allows the system administrator to control the assignment of priorities. The file consists of one or more multi-line records separated by blank lines. Records can have one of two forms, a specific form and a general form. </p>
<dl>
<dd>&bull; The specific form assigns a priority (a &quot;Pin-Priority&quot;) to one or more specified packages with a specified version or version range. For example, the following record assigns a high priority to all versions of the perl package whose version number begins with &quot;5.20&quot;. Multiple packages can be separated by spaces. </p>
<dl>
<dd>
<pre>Package: perl
Pin: version 5.20*
Pin-Priority: 1001</pre>
</dl>
</dl>
<dl>
<dd>&bull; The general form assigns a priority to all of the package versions in a given distribution (that is, to all the versions of packages that are listed in a certain Release file) or to all of the package versions coming from a particular Internet site, as identified by the site&#8217;s fully qualified domain name. </p>
<p> This general-form entry in the APT preferences file applies only to groups of packages. For example, the following record assigns a high priority to all package versions available from the local site. </p>
<dl>
<dd>
<pre>Package: *
Pin: origin &quot;&quot;
Pin-Priority: 999</pre>
</dl>
<p> A note of caution: the keyword used here is &quot;origin&quot; which can be used to match a hostname. The following record will assign a high priority to all versions available from the server identified by the hostname &quot;<a href="ftp://ftp.de.debian.org">ftp.de.debian.org</a>&quot; </p>
<dl>
<dd>
<pre>Package: *
Pin: origin &quot;<a href="ftp://ftp.de.debian.org">ftp.de.debian.org</a>&quot;
Pin-Priority: 999</pre>
</dl>
<p> This should <i>not</i> be confused with the Origin of a distribution as specified in a Release file. What follows the &quot;Origin:&quot; tag in a Release file is not an Internet address but an author or vendor name, such as &quot;Debian&quot; or &quot;Ximian&quot;. </p>
<p> The following record assigns a low priority to all package versions belonging to any distribution whose Archive name is &quot;unstable&quot;. </p>
<dl>
<dd>
<pre>Package: *
Pin: release a=unstable
Pin-Priority: 50</pre>
</dl>
<p> The following record assigns a high priority to all package versions belonging to any distribution whose Codename is &quot;bookworm&quot;. </p>
<dl>
<dd>
<pre>Package: *
Pin: release n=bookworm
Pin-Priority: 900</pre>
</dl>
<p> The following record assigns a high priority to all package versions belonging to any release whose Archive name is &quot;stable&quot; and whose release Version number is &quot;11&quot;. </p>
<dl>
<dd>
<pre>Package: *
Pin: release a=stable, v=11
Pin-Priority: 500</pre>
</dl>
</dl>
<p> The effect of the comma operator is similar to an &quot;and&quot; in logic: All conditions must be satisfied for the pin to match. There is one exception: For any type of condition (such as two &quot;a&quot; conditions), only the last such condition is checked.</p>
<h3>Matching packages in the Package field</h3>
<p>The Package field specifies the package that a pinning priority is applied to. The field can either contain a binary package name, a source package name (prefixed with &quot;src:&quot;), a <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) expression or a regular expression (surrounded by slashes). Multiple package names, <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) expressions and regular expressions can be listed separated by whitespace in which case the record will match any of the matched packages. </p>
<p> By default, only packages of the native architecture are matched. To match binary packages of any architecture, add the :any suffix to the package name. You can also limit matching to a specific architecture by appending the architecture name to the package name, separated by a colon character. </p>
<p> For example, the following example uses a glob expression and a regular expression to assign the priority 500 to all packages from experimental where the name starts with gnome (as a <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7)-like expression) or contains the word kde (as a POSIX extended regular expression surrounded by slashes). </p>
<dl>
<dd>
<pre>Package: gnome* /kde/
Pin: release a=experimental
Pin-Priority: 500</pre>
</dl>
<p> The rule for those expressions is that they can occur anywhere where a string can occur. Thus, the following pin assigns the priority 990 to all packages from a release starting with hirsute. </p>
<dl>
<dd>
<pre>Package: *
Pin: release n=hirsute*
Pin-Priority: 990</pre>
</dl>
<p> If a regular expression occurs in a Package field, the behavior is the same as if this regular expression were replaced with a list of all package names it matches. It is undecided whether this will change in the future; thus you should always list wild-card pins first, so later specific pins override it. The pattern &quot;*&quot; in a Package field is not considered a <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) expression in itself. </p>
<p> To pin all binaries produced by the apt source package of this APT&#8217;s version to 990, you can do: </p>
<dl>
<dd>
<pre>Package: src:apt
Pin: version 2.4.8
Pin-Priority: 990</pre>
</dl>
<p> Source package pinning can be combined with regular expressions and glob patterns, and can also take a binary architecture. </p>
<p> For example, let&#8217;s pin all binaries for all architectures produced by any source package containing apt in its name to 990: </p>
<dl>
<dd>
<pre>Package: src:*apt*:any
Pin: version *
Pin-Priority: 990</pre>
</dl>
<p> The :any suffix makes sure to select binary packages from any architecture. Without that suffix, apt implicitly assumes the :native suffix which would only select packages from the native architecture.</p>
<h3>How APT Interprets Priorities</h3>
<p>Priorities (P) assigned in the APT preferences file must be positive or negative integers. They are interpreted as follows (roughly speaking): </p>
<p> P &gt;= 1000</p>
<dl>
<dd>causes a version to be installed even if this constitutes a downgrade of the package</dl>
<p> 990 &lt;= P &lt; 1000</p>
<dl>
<dd>causes a version to be installed even if it does not come from the target release, unless the installed version is more recent</dl>
<p> 500 &lt;= P &lt; 990</p>
<dl>
<dd>causes a version to be installed unless there is a version available belonging to the target release or the installed version is more recent</dl>
<p> 100 &lt;= P &lt; 500</p>
<dl>
<dd>causes a version to be installed unless there is a version available belonging to some other distribution or the installed version is more recent</dl>
<p> 0 &lt; P &lt; 100</p>
<dl>
<dd>causes a version to be installed only if there is no installed version of the package</dl>
<p> P &lt; 0</p>
<dl>
<dd>prevents the version from being installed</dl>
<p> P = 0</p>
<dl>
<dd>has undefined behaviour, do not use it.</dl>
<p> The first specific-form record matching an available package version determines the priority of the package version. Failing that, the priority of the package is defined as the maximum of all priorities defined by generic-form records matching the version. Records defined using patterns in the Pin field other than &quot;*&quot; are treated like specific-form records. </p>
<p> For example, suppose the APT preferences file contains the three records presented earlier: </p>
<dl>
<dd>
<pre>Package: perl
Pin: version 5.20*
Pin-Priority: 1001
Package: *
Pin: origin &quot;&quot;
Pin-Priority: 999
Package: *
Pin: release unstable
Pin-Priority: 50</pre>
</dl>
<p> Then: </p>
<dl>
<dd>&bull; The most recent available version of the perl package will be installed, so long as that version&#8217;s version number begins with &quot;5.20&quot;. If <i>any</i> 5.20* version of perl is available and the installed version is 5.24*, then perl will be downgraded.</dl>
<dl>
<dd>&bull; A version of any package other than perl that is available from the local system has priority over other versions, even versions belonging to the target release.</dl>
<dl>
<dd>&bull; A version of a package whose origin is not the local system but some other site listed in <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) and which belongs to an unstable distribution is only installed if it is selected for installation and no version of the package is already installed.</dl>
<h3>Determination of Package Version and Distribution Properties</h3>
<p>The locations listed in the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file should provide Packages and Release files to describe the packages available at that location. </p>
<p> The Packages file is normally found in the directory &#8230;/dists/<i>dist-name</i>/<i>component</i>/<i>arch</i>: for example, &#8230;/dists/stable/main/binary-i386/Packages. It consists of a series of multi-line records, one for each package available in that directory. Only two lines in each record are relevant for setting APT priorities: </p>
<p> the Package: line</p>
<dl>
<dd>gives the package name</dl>
<p> the Version: line</p>
<dl>
<dd>gives the version number for the named package</dl>
<p> The Release file is normally found in the directory &#8230;/dists/<i>dist-name</i>: for example, &#8230;/dists/stable/Release, or &#8230;/dists/bullseye/Release. It consists of a single multi-line record which applies to <i>all</i> of the packages in the directory tree below its parent. Unlike the Packages file, nearly all of the lines in a Release file are relevant for setting APT priorities: </p>
<p> the Archive: or Suite: line</p>
<dl>
<dd>names the archive to which all the packages in the directory tree belong. For example, the line &quot;Archive: stable&quot; or &quot;Suite: stable&quot; specifies that all of the packages in the directory tree below the parent of the Release file are in a stable archive. Specifying this value in the APT preferences file would require the line: </p>
<dl>
<dd>
<pre>Pin: release a=stable</pre>
</dl>
</dl>
<p> the Codename: line</p>
<dl>
<dd>names the codename to which all the packages in the directory tree belong. For example, the line &quot;Codename: bookworm&quot; specifies that all of the packages in the directory tree below the parent of the Release file belong to a version named bookworm. Specifying this value in the APT preferences file would require the line: </p>
<dl>
<dd>
<pre>Pin: release n=bookworm</pre>
</dl>
</dl>
<p> the Version: line</p>
<dl>
<dd>names the release version. For example, the packages in the tree might belong to Debian release version 11. Note that there is normally no version number for the testing and unstable distributions because they have not been released yet. Specifying this in the APT preferences file would require one of the following lines. </p>
<dl>
<dd>
<pre>Pin: release v=11
Pin: release a=stable, v=11
Pin: release 11</pre>
</dl>
</dl>
<p> the Component: line</p>
<dl>
<dd>names the licensing component associated with the packages in the directory tree of the Release file. For example, the line &quot;Component: main&quot; specifies that all the packages in the directory tree are from the main component, which entails that they are licensed under terms listed in the Debian Free Software Guidelines. Specifying this component in the APT preferences file would require the line: </p>
<dl>
<dd>
<pre>Pin: release c=main</pre>
</dl>
</dl>
<p> the Origin: line</p>
<dl>
<dd>names the originator of the packages in the directory tree of the Release file. Most commonly, this is Debian. Specifying this origin in the APT preferences file would require the line: </p>
<dl>
<dd>
<pre>Pin: release o=Debian</pre>
</dl>
</dl>
<p> the Label: line</p>
<dl>
<dd>names the label of the packages in the directory tree of the Release file. Most commonly, this is Debian. Specifying this label in the APT preferences file would require the line: </p>
<dl>
<dd>
<pre>Pin: release l=Debian</pre>
</dl>
</dl>
<p> All of the Packages and Release files retrieved from locations listed in the <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file are stored in the directory /var/lib/apt/lists, or in the file named by the variable Dir::State::Lists in the apt.conf file. For example, the file debian.lcs.mit.edu_debian_dists_unstable_contrib_binary-i386_Release contains the Release file retrieved from the site debian.lcs.mit.edu for binary-i386 architecture files from the contrib component of the unstable distribution.</p>
<h3>Optional Lines in an APT Preferences Record</h3>
<p>Each record in the APT preferences file can optionally begin with one or more lines beginning with the word Explanation:. This provides a place for comments.</p>
<h2>Examples</h2>
<h3>Tracking Stable</h3>
<p>The following APT preferences file will cause APT to assign a priority higher than the default (500) to all package versions belonging to a stable distribution and a prohibitively low priority to package versions belonging to other Debian distributions.</p>
<dl>
<dd>
<pre>Explanation: Uninstall or do not install any Debian-originated
Explanation: package versions other than those in the stable distro
Package: *
Pin: release a=stable
Pin-Priority: 900
Package: *
Pin: release o=Debian
Pin-Priority: -10</pre>
</dl>
<p> With a suitable <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file and the above preferences file, any of the following commands will cause APT to upgrade to the latest stable version(s).</p>
<dl>
<dd>
<pre>apt-get install <i>package-name</i>
apt-get upgrade
apt-get dist-upgrade</pre>
</dl>
<p> The following command will cause APT to upgrade the specified package to the latest version from the testing distribution; the package will not be upgraded again unless this command is given again.</p>
<dl>
<dd>
<pre>apt-get install <i>package</i>/testing</pre>
</dl>
<h3>Tracking Testing or Unstable</h3>
<p>The following APT preferences file will cause APT to assign a high priority to package versions from the testing distribution, a lower priority to package versions from the unstable distribution, and a prohibitively low priority to package versions from other Debian distributions.</p>
<dl>
<dd>
<pre>Package: *
Pin: release a=testing
Pin-Priority: 900
Package: *
Pin: release a=unstable
Pin-Priority: 800
Package: *
Pin: release o=Debian
Pin-Priority: -10</pre>
</dl>
<p> With a suitable <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file and the above preferences file, any of the following commands will cause APT to upgrade to the latest testing version(s).</p>
<dl>
<dd>
<pre>apt-get install <i>package-name</i>
apt-get upgrade
apt-get dist-upgrade</pre>
</dl>
<p> The following command will cause APT to upgrade the specified package to the latest version from the unstable distribution. Thereafter, <code>apt-get upgrade</code> will upgrade the package to the most recent testing version if that is more recent than the installed version, otherwise, to the most recent unstable version if that is more recent than the installed version.</p>
<dl>
<dd>
<pre>apt-get install <i>package</i>/unstable</pre>
</dl>
<h3>Tracking the evolution of a codename release</h3>
<p>The following APT preferences file will cause APT to assign a priority higher than the default (500) to all package versions belonging to a specified codename of a distribution and a prohibitively low priority to package versions belonging to other Debian distributions, codenames and archives. Note that with this APT preference APT will follow the migration of a release from the archive testing to stable and later oldstable. If you want to follow for example the progress in testing notwithstanding the codename changes you should use the example configurations above.</p>
<dl>
<dd>
<pre>Explanation: Uninstall or do not install any Debian-originated package versions
Explanation: other than those in the distribution codenamed with bookworm or sid
Package: *
Pin: release n=bookworm
Pin-Priority: 900
Explanation: Debian unstable is always codenamed with sid
Package: *
Pin: release n=sid
Pin-Priority: 800
Package: *
Pin: release o=Debian
Pin-Priority: -10</pre>
</dl>
<p> With a suitable <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) file and the above preferences file, any of the following commands will cause APT to upgrade to the latest version(s) in the release codenamed with bookworm.</p>
<dl>
<dd>
<pre>apt-get install <i>package-name</i>
apt-get upgrade
apt-get dist-upgrade</pre>
</dl>
<p> The following command will cause APT to upgrade the specified package to the latest version from the sid distribution. Thereafter, <code>apt-get upgrade</code> will upgrade the package to the most recent bookworm version if that is more recent than the installed version, otherwise, to the most recent sid version if that is more recent than the installed version.</p>
<dl>
<dd>
<pre>apt-get install <i>package</i>/sid</pre>
</dl>
<h2>Files</h2>
<p>/etc/apt/preferences</p>
<dl>
<dd>Version preferences file. This is where you would specify &quot;pinning&quot;, i.e. a preference to get certain packages from a separate source or from a different version of a distribution. Configuration Item: Dir::Etc::Preferences.</dl>
<p> /etc/apt/preferences.d/</p>
<dl>
<dd>File fragments for the version preferences. Configuration Item: Dir::Etc::PreferencesParts.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8) <code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8) <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5)</p>
<h2>Bugs</h2>
<p>m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>Author</h2>
<p><code>APT team</code></p>
<dl>
<dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>APT bug page</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
