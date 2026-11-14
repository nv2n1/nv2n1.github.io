---
title: "yum-utils(1)"
name: "yum-utils"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-utils/"
description: "yum-utils – tools for manipulating repositories and extended package management"
---

<h2>NAME</h2>
<p> yum-utils &#8211; tools for manipulating repositories and extended package management</p>
<h2>SYNOPSIS</h2>
<pre>
<code>debuginfo-install</code> - install debuginfo packages and their dependencies
<code>find-repos-of-install</code> - report which repository the package was installed from
<code>needs-restarting</code> - report process ids that started running before they or some component they use were updated
<code>package-cleanup</code> - manage package cleanup, duplicates, orphaned packages and outstanding dependency problems
<code>repo-graph</code> - outputs a full package dependency list in dot format 
<code>repo-rss</code> - generates an RSS feed from one or more repositories
<code>repoclosure</code> - reads metadata of repositories, checks dependencies and displays list of unresolved dependencies
<code>repodiff</code> - takes two or more repositories, returns a list of added, removed or changed packages
<code>repomanage</code> - manages a directory of rpm packages, returns a list of newest or oldest packages in a directory
<code>repoquery</code> - query yum repositories and get additional information on the them
<code>reposync</code> - synchronize a remote yum repository to a local directory using yum to retrieve packages
<code>repotrack</code> - track packages and its dependencies and downloads them
<code>show-changed-rco</code> - list of changes to a package Requires, Conflicts and Obsoletes data from installed to a specified rpm file
<code>show-installed</code> - gives a compact description of packages installed and makes use of comps groups in repositories
<code>verifytree</code> - verify that a local yum repository is consistent
<code>yum-builddep</code> - installs missing dependencies to build a specified package
<code>yum-complete-transaction</code> - finds incomplete or aborted yum transactions and attempts to complete them
<code>yum-config-manager</code> - toggle yum repositories, add new repositories and set main yum configuration options
<code>yum-debug-dump</code> - creates gzipped file containing information for debugging problems
<code>yum-debug-restore</code> - replays any transactions captured in gzipped file in yum shell
<code>yum-groups-manager</code> - create and edit yum's group metadata
<code>yum-installed</code> - print a compact package list making use of comps groups 
<code>yumdb</code> - query or alter the yum database
<code>yumdownloader</code> - downloads packages from yum repositories including source RPMs
</pre>
<h2>DESCRIPTION</h2>
<p> <code>yum-utils</code> is a collection of tools and programs for managing yum repositories, installing debug packages, source packages, extended information from repositories and administration.</p>
<h2>NOTES</h2>
<p> See respective tools for additional help for commands without a manual page</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-debuginfo-install/">debuginfo-install</a>(1), <a href="/docs/linux/man/1-package-cleanup/">package-cleanup</a>(1), <a href="/docs/linux/man/1-repodiff/">repodiff</a>(1), <a href="/docs/linux/man/1-repoquery/">repoquery</a>(1), <a href="/docs/linux/man/1-reposync/">reposync</a>(1), <a href="/docs/linux/man/1-repo-rss/">repo-rss</a>(1), <a href="/docs/linux/man/1-show-changed-rco/">show-changed-rco</a>(1), <a href="/docs/linux/man/1-show-installed/">show-installed</a>(1), <a href="/docs/linux/man/1-yumdownloader/">yumdownloader</a>(1), <a href="/docs/linux/man/1-yum-builddep/">yum-builddep</a>(1), <a href="/docs/linux/man/1-yum-debug-dump/">yum-debug-dump</a>(1), <a href="/docs/linux/man/1-yum-groups-manager/">yum-groups-manager</a>(1), <a href="/docs/linux/man/8-yumdb/">yumdb</a>(8), <a href="/docs/linux/man/8-yum-complete-transaction/">yum-complete-transaction</a>(8)</p>
<h2>AUTHOR</h2>
<p> Shawn Starr &lt;shawn.starr [at] rogers.com&gt; </p>
<h2>Index</h2>
