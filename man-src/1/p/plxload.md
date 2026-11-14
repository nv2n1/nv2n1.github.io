---
title: "plxload(1)"
name: "plxload"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plxload/"
description: "plxload – show what files a perl program loads at compile time"
---

<h2 class="name">NAME</h2>
<p> plxload &#8211; show what files a perl program loads at compile time </p>
<h2>SYNOPSYS</h2>
<pre>
    $ plxload
</pre>
<h2>DESCRIPTION</h2>
<p> This program is used to show what modules a program would load at compile time via <tt>&quot;use&quot;</tt>. Because this installs an at-exit handler and then uses Perl&#8217;s <code>-c</code> flag for compile only, it will not find modules loaded at run-time. Use the Devel::Loaded module for that.</p>
<h2>EXAMPLES</h2>
<pre>
    $ plxload perldoc
    /usr/local/devperl/lib/5.00554/Exporter.pm
    /usr/local/devperl/lib/5.00554/strict.pm
    /usr/local/devperl/lib/5.00554/vars.pm
    /usr/local/devperl/lib/5.00554/i686-linux/Config.pm
    /usr/local/devperl/lib/5.00554/Getopt/Std.pm
    $ plxload /usr/src/perl5.005_54/installhtml
    /usr/local/devperl/lib/5.00554/Carp.pm
    /usr/local/devperl/lib/5.00554/Exporter.pm
    /usr/local/devperl/lib/5.00554/auto/Getopt/Long/autosplit.ix
    /usr/local/devperl/lib/5.00554/strict.pm
    /usr/local/devperl/lib/5.00554/vars.pm
    /usr/local/devperl/lib/5.00554/Pod/Functions.pm
    /usr/local/devperl/lib/5.00554/Getopt/Long.pm
    /usr/local/devperl/lib/5.00554/i686-linux/Config.pm
    /usr/local/devperl/lib/5.00554/lib.pm
    /home/tchrist/perllib/Pod/Html.pm
    /usr/local/devperl/lib/5.00554/Cwd.pm
    /usr/local/devperl/lib/5.00554/AutoLoader.pm
</pre>
<h2>SEE ALSO</h2>
<p> Devel::Loaded and <i><a href="/docs/linux/man/1-pmload/">pmload</a></i>(1).</p>
<h2>AUTHORS and COPYRIGHTS</h2>
<p> Copyright (C) 1999 Tom Christiansen. </p>
<p> Copyright (C) 2006-2014 Mark Leighton Fisher.</p>
<h2>LICENSE</h2>
<p> This is free software; you can redistribute it and/or modify it under the terms of either: (a) the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 1, or (at your option) any later version, or (b) the Perl &#8220;Artistic License&#8221;. (This is the Perl 5 licensing scheme.) </p>
<p> Please note this is a change from the original pmtools-1.00 (still available on <font SIZE="-1">CPAN</font>), as pmtools-1.00 were licensed only under the Perl &#8220;Artistic License&#8221;. </p>
<h2>Index</h2>
