---
title: "repoquery(1)"
name: "repoquery"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repoquery/"
description: "repoquery – query information from Yum repositories"
---

<h2>NAME</h2>
<p> repoquery &#8211; query information from Yum repositories</p>
<h2>SYNOPSIS</h2>
<p> <code>repoquery</code> [options] &lt;item &#8230;&gt;<br />
 <code>repoquery</code> -a [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>repoquery</code> is a program for querying information from YUM repositories similarly to rpm queries. </p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>&#8211;querytags</code></p>
<dd> List valid queryformat tags and exit..</p>
<dt><code>&#8211;version</code></p>
<dd> Report program version and exit.</p>
<dt><code>&#8211;repoid=&lt;repo&gt;</code></p>
<dd> Specify which repository to query. Using this option disables all repositories not explicitly enabled with &#8211;repoid option (can be used multiple times). By default repoquery uses whatever repositories are enabled in YUM configuration.</p>
<dt><code>&#8211;enablerepo=&lt;repo&gt;</code></p>
<dd> In addition to the default set, query the given additional repository, even if it is disabled in YUM configuration. Can be used multiple times.</p>
<dt><code>&#8211;disablerepo=&lt;repo&gt;</code></p>
<dd> Do not query the given repository, even if it is enabled in YUM configuration. Can be used multiple times.</p>
<dt><code>&#8211;repofrompath=&lt;repoid&gt;,&lt;path/url&gt;</code></p>
<dd> Specify a path or url to a repository (same path as in a baseurl) to add to the repositories for this query. This option can be used multiple times. If you want to view only the pkgs from this repository combine this with &#8211;repoid. The repoid for the repository is specified by &lt;repoid&gt;.</p>
<dt><code>&#8211;plugins</code></p>
<dd> Enable YUM plugin support.</p>
<dt><code>-q, &#8211;query</code></p>
<dd> For rpmquery compatibility, doesn&#8217;t do anything.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Help; display a help message and then quit.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Run quietly: no warnings printed to stderr.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Produce verbose output.</p>
<dt><code>-C, &#8211;cache</code></p>
<dd> Tells repoquery to run entirely from YUM cache &#8211; does not download any metadata or update the cache. Queries in this mode can fail or give partial/incorrect results if the cache isn&#8217;t fully populated beforehand with eg &quot;yum makecache&quot;.</p>
<dt><code>&#8211;tempcache</code></p>
<dd> Create and use a private cache instead of the main YUM cache. This is used by default when run as non-root user.</p>
<dt><code>-c &lt;config file&gt;, &#8211;config=&lt;config file&gt;</code></p>
<dd> Use alternative config file (default is /etc/yum.conf).</p>
<dt><code>&#8211;releasever=version</code></p>
<dd> Pretend the current release version is the given string. This is very useful when combined with &#8211;installroot. You can also use &#8211;releasever=/ to take the releasever information from outside the installroot. Note that with the default upstream cachedir, of /var/cache/yum, using this option will corrupt your cache (and you can use $releasever in your cachedir configuration to stop this).</p>
<dt><code>&#8211;installroot=root</code></p>
<dd> Specifies an alternative installroot, relative to which all packages will be installed. Think of this like doing &quot;chroot &lt;root&gt; yum&quot; except using &#8211;installroot allows yum to work before the chroot is created. Note: You may also want to use the option &#8211;releasever=/ when creating the installroot as otherwise the $releasever value is taken from the rpmdb within the installroot (and thus. will be empty, before creation).</p>
<dt><code>&#8211;setopt=option=value</code></p>
<dd> Set any config option in yum config or repo files. For options in the global config just use: &#8211;setopt=option=value for repo options use: &#8211;setopt=repoid.option=value </p>
</dl>
<h2>PACKAGE QUERY OPTIONS</h2>
<dl>
<dt><code>-i, &#8211;info</code></p>
<dd> Show general information about package similarly to &quot;rpm -qi&quot;</p>
<dt><code>-l, &#8211;list</code></p>
<dd> List files in package.</p>
<dt><code>-R, &#8211;requires</code></p>
<dd> List package dependencies.</p>
<dt><code>&#8211;resolve</code></p>
<dd> When used with &#8211;requires, resolve capabilities to originating packages.</p>
<dt><code>&#8211;provides</code></p>
<dd> List capabilities package provides.</p>
<dt><code>&#8211;obsoletes</code></p>
<dd> List capabilities obsoleted by package.</p>
<dt><code>&#8211;conflicts</code></p>
<dd> List capabilities conflicting with package.</p>
<dt><code>&#8211;changelog</code></p>
<dd> List package changelog.</p>
<dt><code>&#8211;location</code></p>
<dd> Show a location where the package could be downloaded from. For example: <code>wget `repoquery &#8211;location yum`</code></p>
<dt><code>-s, &#8211;source</code></p>
<dd> Show package source RPM name.</p>
<dt><code>&#8211;srpm</code></p>
<dd> Operate on corresponding source RPM.</p>
<dt><code>&#8211;groupmember PACKAGE</code></p>
<dd> List the repodata groups (yumgroups.xml) belongs to (if any).</p>
<dt><code>&#8211;nvr</code></p>
<dd> Use name-version-release output format (rpm query default)</p>
<dt><code>&#8211;nevra</code></p>
<dd> Use name-epoch:version-release.architecture output format (default)</p>
<dt><code>&#8211;envra</code></p>
<dd> Use epoch:name-version-release.architecture output format (easier to parse than nevra)</p>
<dt><code>&#8211;qf=FORMAT, &#8211;queryformat=FORMAT</code></p>
<dd> Specify custom output format for queries. You can add &quot;:date&quot;, &quot;:day&quot; and &quot;:isodate&quot; to all the tags that are a time, and you can add &quot;:k&quot;, &quot;:m&quot;, &quot;:g&quot;, &quot;:t&quot; and &quot;:h&quot; to sizes. You can also specify field width as in sprintf (Eg. %-20{name})</p>
<dt><code>&#8211;output [text|ascii-tree|dot-tree]</code></p>
<dd> Output format which can be used with &#8211;requires/&#8211;whatrequires/&#8211;obsoletes/&#8211;conflicts. Default output is &#8216;text&#8217;.</p>
<dt><code>&#8211;level [all|any int]</code></p>
<dd> In combination with &#8211;output ascii-tree|dot-tree this option specifies the number of level to print on the tree. Default level is &#8216;all&#8217;.</dl>
<h2>PACKAGE SELECTION OPTIONS</h2>
<dl>
<dt><code>-a, &#8211;all</code></p>
<dd> Query all available packages (for rpmquery compatibility / shorthand for repoquery &#8216;*&#8217;)</p>
<dt><code>&#8211;show-duplicates</code></p>
<dd> Query all versions of packages.</p>
<dt><code>-f, &#8211;file FILE</code></p>
<dd> Query package owning FILE.</p>
<dt><code>&#8211;whatobsoletes CAPABILITY</code></p>
<dd> Query all packages that obsolete CAPABILITY.</p>
<dt><code>&#8211;whatconflicts CAPABILITY</code></p>
<dd> Query all packages that conflict with CAPABILITY.</p>
<dt><code>&#8211;whatprovides CAPABILITY</code></p>
<dd> Query all packages that provide CAPABILITY.</p>
<dt><code>&#8211;whatrequires CAPABILITY</code></p>
<dd> Query all packages that require CAPABILITY.</p>
<dt><code>&#8211;alldeps</code></p>
<dd> When used with &#8211;whatrequires, look for non-explicit dependencies in addition to explicit ones (e.g. files and Provides in addition to package names). This is the default.</p>
<dt><code>&#8211;exactdeps</code></p>
<dd> When used with &#8211;whatrequires, search for dependencies only exactly as given. This is effectively the opposite of &#8211;alldeps.</p>
<dt><code>&#8211;recursive</code></p>
<dd> When used with &#8211;whatrequires, and &#8211;requires &#8211;resolve, query packages recursively.</p>
<dt><code>&#8211;archlist=ARCH1[,ARCH2&#8230;]</code></p>
<dd> Limit the query to packages of given architecture(s). Valid values are all architectures known to rpm/yum such as &#8216;i386&#8217; and &#8216;src&#8217; for source RPMS. Note that repoquery will now change yum&#8217;s &quot;arch&quot; to the first value in the archlist. So &quot;&#8211;archlist=i386,i686&quot; will change yum&#8217;s canonical arch to i386, but allow packages of i386 and i686.</p>
<dt><code>&#8211;pkgnarrow=WHAT</code></p>
<dd> Limit what packages are considered for the query. Valid values for WHAT are: installed, available, recent, updates, extras, all and repository (default).</p>
<dt><code>&#8211;installed</code></p>
<dd> Restrict query ONLY to installed pkgs &#8211; disables all repos and only acts on rpmdb. </p>
</dl>
<h2>GROUP QUERY OPTIONS</h2>
<dl>
<dt><code>-i, &#8211;info</code></p>
<dd> Show general information about group.</p>
<dt><code>-l, &#8211;list</code></p>
<dd> List packages belonging to (required by) group.</p>
<dt><code>&#8211;grouppkgs=WHAT</code></p>
<dd> Specify what type of packages are queried from groups. Valid values for WHAT are all, mandatory, default, optional.</p>
<dt><code>&#8211;requires</code></p>
<dd> List groups required by group.</dl>
<h2>GROUP SELECTION OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Query all available groups.</p>
<dt><code>-g, &#8211;group</code></p>
<dd> Query groups instead of packages.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>List all packages whose name contains &#8216;perl&#8217;:</p>
<dd> <code>repoquery &#8216;*perl*&#8217;</code></p>
<dt>List all packages depending on openssl:</p>
<dd> <code>repoquery &#8211;whatrequires openssl</code></p>
<dt>List all package names and the repository they come from, nicely formatted:</p>
<dd> <code>repoquery -a &#8211;qf &quot;%-20{repoid} %{name}&quot;</code></p>
<dt>List name and summary of all available updates (if any), nicely formatted:</p>
<dd> <code>repoquery -a &#8211;pkgnarrow=updates &#8211;qf &quot;%{name}:
%{summary}
&quot;</code></p>
<dt>List optional packages in base group:</p>
<dd> <code>repoquery -g &#8211;grouppkgs=optional -l base</code></p>
<dt>List build requirements from &#8216;anaconda&#8217; source rpm:</p>
<dd> <code>repoquery &#8211;requires anaconda.src</code></p>
<dt>List packages which BuildRequire gail-devel</p>
<dd> <code>repoquery &#8211;archlist=src &#8211;whatrequires gail-devel</code><br />
&nbsp;<wbr>&nbsp;<wbr>NB: This command will only work if you have repositories enabled which include srpms. </p>
</dl>
<h2>MISC</h2>
<dl>
<dt><code>Specifying package names</code></p>
<dd> A package can be referred to in all queries with any of the following:</p>
<dt>
<dd>
 <code>name</code><br />
 <code>name.arch</code><br />
 <code>name-ver</code><br />
 <code>name-ver-rel</code><br />
 <code>name-ver-rel.arch</code><br />
 <code>name-epoch:ver-rel.arch</code><br />
 <code>epoch:name-ver-rel.arch</code></p>
<dt>
<dd> For example: <code>repoquery -l kernel-2.4.1-10.i686</code><br />
 Additionally wildcards (shell-style globs) can be used. </p>
</dl>
<h2>FILES</h2>
<p> As repoquery uses YUM libraries for retrieving all the information, it relies on YUM configuration for its default values like which repositories to use. Consult YUM documentation for details: </p>
<pre>
/etc/yum.conf
/etc/yum/repos.d/
/var/cache/yum/
</pre>
<h2>SEE ALSO</h2>
<pre>
<i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
</pre>
<h2>AUTHORS</h2>
<pre>
See the Authors file included with this program.
</pre>
<h2>BUGS</h2>
<p> There are of course no bugs, but should you find any, you should first consult the FAQ section on <a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a> and if unsuccessful in finding a resolution contact the mailing list: yum-devel [at] lists.baseurl.org. To file a bug use <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> for Fedora/RHEL/Centos related bugs and <a rel="nofollow" href="http://yum.baseurl.org/report">http://yum.baseurl.org/report</a> for all other bugs. </p>
<h2>Index</h2>
