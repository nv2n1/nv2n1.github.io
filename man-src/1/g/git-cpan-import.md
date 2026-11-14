---
title: "git-cpan-import(1)"
name: "git-cpan-import"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-cpan-import/"
---

<h2 class="name">NAME</h2>
 

 git-cpan-import - Import a module into a git repository 

<h2>SYNOPSIS</h2>

 <pre>
    # takes any string CPANPLUS handles:
    % git cpan-import Foo::Bar
    % git cpan-import A/AU/AUTHORID/Foo-Bar-0.03.tar.gz
    % git cpan-import <a rel="nofollow" HREF="http://backpan.cpan.org/authors/id/A/AU/AUTHORID/Foo-Bar-0.03.tar.gz">http://backpan.cpan.org/authors/id/A/AU/AUTHORID/Foo-Bar-0.03.tar.gz</a>
    # If the repository is already initialized, can be run with no arguments to
    # import the latest version
    git cpan-import
</pre>

<h2>DESCRIPTION</h2>

 This command is used internally by <tt>&quot;git-cpan-init&quot;</tt>, <tt>&quot;git-cpan-update&quot;</tt> and <tt>&quot;git-backpan-init&quot;</tt>. 

 This command takes a tarball, extracts it, and imports it into the repository. 

 It is only possible to update to a newer version of a module. 

 The module history is tracked in <tt>&quot;refs/remotes/cpan/master&quot;</tt>. 

 Tags are created for each version of the module. 

 This command does not touch the working directory, and is safe to run even if you have pending work.

<h2>OPTIONS</h2>

<dl>
<dt>--backpan
<dd> Enables Backpan index fetching (to get the author and release date).
<dt>--checkversion, --nocheckversion
<dd> Explicitly enables/disables version checking. If version checking is enabled, which is the default, git-cpan-import will refuse to import a version of the package that has a smaller version number than the <font SIZE="-1">HEAD</font> of the branch <i>cpan/master</i>.
<dt>--parent
<dd> Allows adding extra parents when importing, so that when a patch has been incorporated into an upstream version the generated commit is like a merge commit, incorporating both the <font SIZE="-1">CPAN</font> history and the user's local history. 

 For example, this will set the current <font SIZE="-1">HEAD</font> of the master branch as a parent of the imported <font SIZE="-1">CPAN</font> package: 

 <pre>
        $ git checkout master
        $ git cpan-import --parent HEAD My-Module
</pre> 

 More than one '--parent' can be specified.</dl>

<h2>VERSION</h2>

 This document describes git-cpan-import version 0.2.1

<h2>BUGS AND LIMITATIONS</h2>

 Please report any bugs or feature requests to <tt>&quot;bug-git-cpan-patch [at] rt.cpan.org&quot;</tt>, or through the web interface at &lt;<a rel="nofollow" HREF="http://rt.cpan.org">http://rt.cpan.org</a>&gt;.

<h2>AUTHORS</h2>

 Yuval Kogman <tt>&quot;&lt;nothingmuch [at] woobling.org&gt;&quot;</tt> 

 Yanick Champoux <tt>&quot;&lt;yanick [at] cpan.org&gt;&quot;</tt>

<h2>LICENCE</h2>

 This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself. See perlartistic.

<h2>SEE ALSO</h2>

 Git::CPAN::Patch 

<h2>Index</h2>


