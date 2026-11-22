---
title: "testlintianbuild(3)"
name: "testlintianbuild"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testlintianbuild/"
---

Test::Lintian::Build -- routines to prepare the work directories 

<h2>Synopsis</h2><pre> use Test::Lintian::Build qw(build_subject);</pre><h2>Description</h2>The routines in this module prepare the work directories in which the tests are run. To do so, they use the specifications in the test set.
<h2>Functions</h2><dl COMPACT><dt>build_subject(PATH)
</dt><dd>Populates a work directory RUN_PATH with data from the test located in SPEC_PATH. The optional parameter REBUILD forces a rebuild if true. 
</dd></dl>
