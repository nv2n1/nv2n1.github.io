---
title: "git-cpan-update(1)"
name: "git-cpan-update"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-cpan-update/"
---

<h2 class="name">NAME</h2>
 

 git-cpan-update - Import the latest version of a module and rebase the current branch 

<h2>SYNOPSIS</h2>

 <pre>
    % git cpan-update
</pre>

<h2>DESCRIPTION</h2>

 This command runs <tt>&quot;git cpan-import&quot;</tt>, and then if <tt>&quot;cpan/master&quot;</tt> was updated runs <tt>&quot;git rebase cpan/master&quot;</tt>, bringing your patches up to date with the upstream.

<h2>VERSION</h2>

 This document describes git-cpan-update version 0.2.1

<h2>BUGS AND LIMITATIONS</h2>

 Please report any bugs or feature requests to <tt>&quot;bug-git-cpan-patch [at] rt.cpan.org&quot;</tt>, or through the web interface at &lt;<a rel="nofollow" HREF="http://rt.cpan.org">http://rt.cpan.org</a>&gt;.

<h2>AUTHORS</h2>

 Yuval Kogman <tt>&quot;&lt;nothingmuch [at] woobling.org&gt;&quot;</tt> 

 Yanick Champoux <tt>&quot;&lt;yanick [at] cpan.org&gt;&quot;</tt>

<h2>LICENCE</h2>

 This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself. See perlartistic.

<h2>SEE ALSO</h2>

 Git::CPAN::Patch, git-cpan-import 

<h2>Index</h2>


