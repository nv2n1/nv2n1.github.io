---
title: "pfunc(1)"
name: "pfunc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pfunc/"
description: "pfunc – grep for perl functions"
---

<h2 class="name">NAME</h2>
<p> pfunc &#8211; grep for perl functions </p>
<h2>SYNOPSIS</h2>
<pre>
    pfunc subroutine FILES...
</pre>
<h2>DESCRIPTION</h2>
<p> <code>pfunc</code> searches the named <font SIZE="-1">FILES</font> for all calls to the given subroutine. It will report back the file and line number each call is found on along with what sort of call it is </p>
<pre>
    function            foo()
    class method        Class-&gt;foo()
    object method       $obj-&gt;foo()
</pre>
<h2>EXAMPLE</h2>
<pre>
    $ pfunc isa /usr/share/perl/5.6.1/*.pm
    Called as function in /usr/share/perl/5.6.1/CGI.pm at line 316
    Called as function in /usr/share/perl/5.6.1/CGI.pm at line 327
    Called as function in /usr/share/perl/5.6.1/CGI.pm at line 397
    Called as function in /usr/share/perl/5.6.1/CGI.pm at line 494
    Called as function in /usr/share/perl/5.6.1/CGI.pm at line 495
    Called as object method in /usr/share/perl/5.6.1/CPAN.pm at line 4957
    Called as function in /usr/share/perl/5.6.1/Dumpvalue.pm at line 191
    Called as function in /usr/share/perl/5.6.1/Dumpvalue.pm at line 218
    Called as function in /usr/share/perl/5.6.1/Dumpvalue.pm at line 248
    Called as function in /usr/share/perl/5.6.1/Dumpvalue.pm at line 251
    Called as function in /usr/share/perl/5.6.1/Dumpvalue.pm at line 254
    Called as object method in /usr/share/perl/5.6.1/Shell.pm at line 28
    Called as object method in /usr/share/perl/5.6.1/base.pm at line 12
</pre>
<h2>NOTES</h2>
<p> Its not fast, but its accurate.</p>
<h2>AUTHOR</h2>
<p> Michael G Schwern &lt;schwern [at] pobox.com&gt;</p>
<h2>SEE ALSO</h2>
<p> Module::Info </p>
<h2>Index</h2>
