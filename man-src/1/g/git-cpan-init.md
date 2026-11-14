---
title: "git-cpan-init(1)"
name: "git-cpan-init"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-cpan-init/"
---

<h2 class="name">NAME</h2>
 

 git-cpan-init - Create a git repository for a CPAN module 

<h2>SYNOPSIS</h2>

 <pre><code>
    git cpan-init [ --help | --man ] [ --backpan ] [ Foo::Bar | Foo-Bar-0.03.tar.gz | http://... ]
</code></pre>

<h2>DESCRIPTION</h2>

 This command creates a new git repository, calls <tt>&quot;git-cpan-import&quot;</tt> and then checks out the code in the <tt>&quot;master&quot;</tt> branch.

<h2>VERSION</h2>

 This document describes git-cpan-init version 0.2.1

<h2>BUGS AND LIMITATIONS</h2>

 Please report any bugs or feature requests to <tt>&quot;bug-git-cpan-patch [at] rt.cpan.org&quot;</tt>, or through the web interface at &lt;<a rel="nofollow" HREF="http://rt.cpan.org">http://rt.cpan.org</a>&gt;.

<h2>AUTHORS</h2>

 Yanick Champoux <tt>&quot;&lt;yanick [at] cpan.org&gt;&quot;</tt> 

 Yuval Kogman <tt>&quot;&lt;nothingmuch [at] woobling.org&gt;&quot;</tt>

<h2>LICENCE</h2>

 This module is free software; you can redistribute it and/or modify it under the same terms as Perl itself. See perlartistic.

<h2>SEE ALSO</h2>

 Git::CPAN::Patch, git-cpan-import 

<h2>Index</h2>


