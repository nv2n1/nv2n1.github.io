---
title: "cpanp(1)"
name: "cpanp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpanp/"
description: "cpanp – The CPANPLUS launcher"
---

<h2 class="name">NAME</h2>
<p> cpanp &#8211; The CPANPLUS launcher </p>
<h2>SYNOPSIS</h2>
<p> <code>cpanp</code> </p>
<p> <code>cpanp</code> [-]<code>a</code> [&nbsp;<wbr>&#8211;[<code>no</code>-]<i>option</i>&#8230;&nbsp;<wbr>] &nbsp;<wbr><i>author</i>&#8230;&nbsp;<wbr> </p>
<p> <code>cpanp</code> [-]<code>mfitulrcz</code> [&nbsp;<wbr>&#8211;[<code>no</code>-]<i>option</i>&#8230;&nbsp;<wbr>] &nbsp;<wbr><i>module</i>&#8230;&nbsp;<wbr> </p>
<p> <code>cpanp</code> [-]<code>d</code> [&nbsp;<wbr>&#8211;[<code>no</code>-]<i>option</i>&#8230;&nbsp;<wbr>] [&nbsp;<wbr>&#8212;<code>fetchdir</code>=&#8230;&nbsp;<wbr>] &nbsp;<wbr><i>module</i>&#8230;&nbsp;<wbr> </p>
<p> <code>cpanp</code> [-]<code>xb</code> [&nbsp;<wbr>&#8211;[<code>no</code>-]<i>option</i>&#8230;&nbsp;<wbr>] </p>
<p> <code>cpanp</code> [-]<code>o</code> [&nbsp;<wbr>&#8211;[<code>no</code>-]<i>option</i>&#8230;&nbsp;<wbr>] [&nbsp;<wbr><i>module</i>&#8230;&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> This script launches the <font SIZE="-1"><code>CPANPLUS</code></font> utility to perform various operations from the command line. If it&#8217;s invoked without arguments, an interactive shell is executed by default. </p>
<p> Optionally, it can take a single-letter switch and one or more argument, to perform the associated action on each arguments. A summary of the available commands is listed below; <tt>&quot;cpanp -h&quot;</tt> provides a detailed list. </p>
<pre><code>
h #help information
    v #version information
        a AUTHOR... #search by
        author(s)
m MODULE... #search by module(s)
f MODULE... #list all releases of a module
    i MODULE... #install module(s)
t MODULE... #test module(s)
u MODULE... #uninstall module(s)
d MODULE... #download module(s)
l MODULE... #display detailed information about module(s)
r MODULE... #display README files of module(s)
    c MODULE ...        # check for module report(s)
    from cpan - testers
                    z MODULE... #extract module(s) and
        open command prompt in it
        x #reload CPAN indices
        o[MODULE...] #list installed module(s) that aren't up to date
    b                   # write a bundle file for your configuration
</code></pre>
<p> Each command may be followed by one or more <i>options</i>. If preceded by <tt>&quot;no&quot;</tt>, the corresponding option will be set to <tt>0</tt>, otherwise it&#8217;s set to <tt>1</tt>. </p>
<p> Example: To skip a module&#8217;s tests, </p>
<pre>
    cpanp -i --skiptest MODULE ...
</pre>
<p> Valid options for most commands are <tt>&quot;cpantest&quot;</tt>, <tt>&quot;debug&quot;</tt>, <tt>&quot;flush&quot;</tt>, <tt>&quot;force&quot;</tt>, <tt>&quot;prereqs&quot;</tt>, <tt>&quot;storable&quot;</tt>, <tt>&quot;verbose&quot;</tt>, <tt>&quot;md5&quot;</tt>, <tt>&quot;signature&quot;</tt>, and <tt>&quot;skiptest&quot;</tt>; the &#8216;d&#8217; command also accepts <tt>&quot;fetchdir&quot;</tt>. Please consult CPANPLUS::Configure for an explanation to their meanings. </p>
<p> Example: To download a module&#8217;s tarball to the current directory, </p>
<pre>
    cpanp -d --fetchdir=. MODULE ...
</pre>
<h2>Index</h2>
