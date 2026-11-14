---
title: "gtags-cscope(1)"
name: "gtags-cscope"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtags-cscope/"
description: "gtags-cscope – pseudo cscope which implements the line-oriented interface"
---

<h2>NAME</h2>
<p> gtags-cscope &#8211; pseudo cscope which implements the line-oriented interface</p>
<h2>SYNOPSIS</h2>
<p> <code>gtags-cscope</code> [-Cqv] </p>
<h2>DESCRIPTION</h2>
<p> <code>Gtags-cscope</code> is a pseudo cscope which implements the line-oriented interface. You can use this command for various clients instead of true cscope. </p>
<p> Since <code>gtags-cscope</code> is intended to make GLOBAL available through cscope interface, the output is not necessarily the same as cscope.</p>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><code>-C</code>, <code>&#8211;ignore-case</code></p>
<dd> Ignore letter case when searching.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Quiet mode.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode.</dl>
<h2>EXAMPLES</h2>
<pre><code>
$ gtags - cscope &gt;&gt; help 0 &lt; arg &gt; : Find this C symbol 1 &lt; arg &gt; : Find this definition 2 &lt; arg &gt; : Find functions called by this function(Not implemented yet.) 3 &lt; arg &gt; : Find functions calling this function
                                                                                                                                                                              4 &lt; arg
                                                                                                                                                                              &gt; : Find this text string
                                                                                                                                                                                  6 &lt; arg
                                                                                                                                                                                  &gt; : Find this egrep pattern
                                                                                                                                                                                      7 &lt; arg
                                                                                                                                                                                      &gt; : Find this file
                                                                                                                                                                                          8 &lt; arg
                                                                                                                                                                                          &gt; : Find files #including this file
                                                                                                                                                                                              c : Toggle ignore
                                                                                                                                                                                                  /
                                                                                                                                                                                                  use letter case r : Rebuild the database
                                                                                                                                                                                                                      q : Quit the session
                                                                                                                                                                                                                          h : Show help
    &gt;&gt;
    1main cscope : 9 lines
            global
            / global.c main 158 main(int argc, char **argv) gozilla / gozilla.c main 155 main(int argc, char **argv) gtags
        - parser / gctags.c main 158 main(int argc, char **argv) gtags - cscope / gtags - cscope.c main 115 main(int argc, char **argv) gtags / gtags.c main 150 main(int argc, char **argv) htags - refkit / htags_path2url.c main 281 main(int argc, char **argv) htags / htags.c main 1400 main(int argc, char **argv) libglibc / getopt.c main 704 main(argc, argv) libglibc / getopt1.c main 93 main(argc, argv) &gt;&gt;
    q
    $ _
</code></pre>
<h2>DIAGNOSTICS</h2>
<p> <code>Gtags-cscope</code> exits with a non 0 value if an error occurred, 0 otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cscope/">cscope</a></code>(1), <code><a href="/docs/linux/man/1-gtags-parser/">gtags-parser</a></code>(1), <code><a href="/docs/linux/man/1-gtags/">gtags</a></code>(1), <code><a href="/docs/linux/man/1-global/">global</a></code>(1), <code><a href="/docs/linux/man/1-htags/">htags</a></code>(1). </p>
<p> GNU GLOBAL source code tag system<br />
 (<a rel="nofollow" href="http://www.gnu.org/software/global/">http://www.gnu.org/software/global/</a>).</p>
<h2>BUG</h2>
<p> The second field of the output is almost &lt;unknown&gt; since GLOBAL doesn&#8217;t recognize it. Command 2 (Find functions called by this function) is not implemented.</p>
<h2>AUTHOR</h2>
<p> Tama Communications Corporation.</p>
<h2>HISTORY</h2>
<p> The <code>gtags-cscope</code> command appeared in 2006. </p>
<h2>Index</h2>
