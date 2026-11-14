---
title: "repocutter(1)"
name: "repocutter"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repocutter/"
description: "repocutter – surgical and filtering operations on Subversion dump files"
---

<h2 class="name">NAME</h2>
<p> repocutter &#8211; surgical and filtering operations on Subversion dump files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>repocutter</code> [-q] [-r&nbsp;<wbr><i>selection</i>] <i>subcommand</i></dl>
<h2>DESCRIPTION</h2>
<dd>This program does surgical and filtering operations on Subversion dump files. While it is is not as flexible as <code><a href="/docs/linux/man/1-reposurgeon/">reposurgeon</a></code>(1), it can perform Subversion-specific transformations that reposurgeon cannot, and can be useful for processing Subversion repositories into a form suitable for conversion. </p>
<p> (As a matter of possible historical interest, the reason for the partial functional overlap between repocutter and reposurgeon is that repocutter was first written earlier and became a testbed for some of the design concepts in reposurgeon. After reposurgeon was written, the author learned that it could not naturally support some useful operations very specific to Subversion, and enhanced repocutter to do those.) </p>
<p> In all commands, the -r (or &#8211;range) option limits the selection of revisions over which an operation will be performed. A selection consists of one or more comma-separated ranges. A range may consist of an integer revision number or the special name HEAD for the head revision. Or it may be a colon-separated pair of integers, or an integer followed by a colon followed by HEAD. </p>
<p> Normally, each subcommand produces a progress spinner on standard error; each turn means another revision has been filtered. The -q (or &#8211;quiet) option suppresses this. </p>
<p> Generally, if you need to use this program at all, you will find that you need to pipe your dump file through multiple instances of it doing one kind of operation each. This is not as expensive as it sounds; with the exception of the reduce subcommand, the working set of this program is bounded by the size of the largest commit metadata item. It does not need to hold the entire repo metadata in memory. </p>
<p> The following subcommands are available: </p>
<p> help</p>
<dl>
<dt>
<dd> Without arguments, list available commands. With a command-name argument, show detailed help for that subcommand.</dl>
<p> select</p>
<dl>
<dt>
<dd> The &#8216;select&#8217; subcommand selects a range and permits only revisions in that range to pass to standard output. A range beginning with 0 includes the dumpfile header.</dl>
<p> propset</p>
<dl>
<dt>
<dd> Set a property to a value. May be restricted by a revision selection. You may specify multiple property settings. See the embedded help for syntax details.</dl>
<p> propdel</p>
<dl>
<dt>
<dd> Delete the named property. May be restricted by a revision selection. You may specify multiple properties to be deleted. See the embedded help for syntax details.</dl>
<p> proprename</p>
<dl>
<dt>
<dd> Rename a property. May be restricted by a revision selection. You may specify multiple properties to be renamed. See the embedded help for syntax details.</dl>
<p> log</p>
<dl>
<dt>
<dd> enerate a log report, same format as the output of svn log on a repository, to standard output.</dl>
<p> setlog</p>
<dl>
<dt>
<dd> Replace the log entries in the input dumpfile with the corresponding entries in a specified file, which should be in the format of an svn log output. Replacements may be restricted to a specified range. See the embedded help for syntax details.</dl>
<p> squash</p>
<dl>
<dt>
<dd> The &#8216;squash&#8217; subcommand merges adjacent commits that have the same author and log text and were made within 5 minutes of each other. This can be helpful in cleaning up after migrations from file-oriented revision control systems, or if a developer has been using a pre-2006 version of Emacs VC. See the embedded help for syntax details.</dl>
<p> strip</p>
<dl>
<dt>
<dd> Replace content with unique generated cookies on all node paths matching the specified regular expressions; if no expressions are given, match all paths. Useful when you need to examine a particularly complex node structure.</dl>
<p> expunge</p>
<dl>
<dt>
<dd> Delete all operations with Node-path headers matching specified Python regular expressions. Any revision left with no Node records after this filtering has its Revision record removed as well.</dl>
<p> pathrename</p>
<dl>
<dt>
<dd> Modify Node-path and Node-copyfrom-path headers matching a specified Python regular expression; replace with a given string. The string may contain Python backreferences to parenthesized portions of the pattern. See the embedded help for syntax details.</dl>
<p> renumber</p>
<dl>
<dt>
<dd> Renumber all revisions, patching Node-copyfrom headers as required. Any selection option is ignored. Takes no arguments.</dl>
<p> reduce</p>
<dl>
<dt>
<dd> Strip revisions out of a dump so the only parts left those likely to be relevant to a conversion problem. See the embedded help for syntax details and the relevance filter.</dl>
<h2>HISTORY</h2>
<p> Under the name &#8220;snvcutter&#8221;, an ancestor of this program traveled in the contrib/ director of the Subversion distribution. It had functional overlap with <code><a href="/docs/linux/man/1-reposurgeon/">reposurgeon</a></code>(1) because it was directly ancestral to that code. It was moved to the <code><a href="/docs/linux/man/1-reposurgeon/">reposurgeon</a></code>(1) distribution in January 2016. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-reposurgeon/">reposurgeon</a></code>(1).</p>
<h2>EXAMPLE</h2>
<p> Suppose you have a Subversion repository with the following semi-pathological structure: </p>
<dl>
<dt>
<dd>
<pre>
Directory1/ (with unrelated content)
Directory2/ (with unrelated content)
TheDirIWantToMigrate/
                branches/
                               crazy-feature/
                                               UnrelatedApp1/
                                               TheAppIWantToMigrate/
                tags/
                               v1.001/
                                               UnrelatedApp1/
                                               UnrelatedApp2/
                                               TheAppIWantToMigrate/
                trunk/
                               UnrelatedApp1/
                               UnrelatedApp2/
                               TheAppIWantToMigrate/
</pre>
</dl>
<p> You want to transform the dump file so that TheAppIWantToMigrate can be subject to a regular branchy lift. A way to dissect out the code of interest would be with the following series of filters applied: </p>
<dl>
<dt>
<dd>
<pre>
repocutter expunge '^Directory1' '^Directory2'
repocutter pathrename '^TheDirIWantToMigrate/' ''
repocutter expunge '^branches/crazy-feature/UnrelatedApp1/
repocutter pathrename 'branches/crazy-feature/TheAppIWantToMigrate/' 'branches/crazy-feature/'
repocutter expunge '^tags/v1.001/UnrelatedApp1/'
repocutter expunge '^tags/v1.001/UnrelatedApp2/'
repocutter pathrename '^tags/v1.001/TheAppIWantToMigrate/' 'tags/v1.001/'
repocutter expunge '^trunk/UnrelatedApp1/'
repocutter expunge '^trunk/UnrelatedApp2/'
repocutter pathrename '^trunk/TheAppIWantToMigrate/' 'trunk/'
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;. This tool is distributed with reposurgeon; see the project page at m[blue]<code><a rel="nofollow" href="http://www.catb.org/~esr/reposurgeon">http://www.catb.org/~esr/reposurgeon</a></code>m[]. </p>
<h2>Index</h2>
