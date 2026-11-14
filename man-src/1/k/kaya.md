---
title: "kaya(1)"
name: "kaya"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kaya/"
description: "Kaya – Top-level interpreter for the kaya language"
---

<h2>NAME</h2>
<p> Kaya &#8211; Top-level interpreter for the kaya language</p>
<h2>SYNOPSIS</h2>
<p> <code>kaya</code> <i>FILE [-L DIRECTORY [-L &#8230;]] [-libdir DIRECTORY [-libdir &#8230;]] [-force] [-nochase] [-noprelude] [-nortchecks] [-noopts] [-htmldocs] [-xmldocs] [-static] [-profile] [-seedkey STRING] [-dumptac] [-dumpraw] [-dumptree] [-dumpsimpl] [-dumpeqns] [-dumpcg] [-dumpdeps] [-keepc] [-showgcc]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>kaya</code> is a top-level interpreter for the kaya language. It implements a read-eval-print loop, useful for quick evaluation and testing of functions.</p>
<h2>OPTIONS</h2>
<p> <code>kaya</code> takes the same options as <code><a href="/docs/linux/man/1-kayac/">kayac</a>(1)</code> with the same meaning (although not all options are necessarily useful in this context.</p>
<h2>DOCUMENTATION</h2>
<p> A set of interpreter commands can be obtained by typing <code>:?</code> at the interpreter prompt.</p>
<h2>EXAMPLE OF USAGE</h2>
<pre><code>
_ | | ____ _ _ _ __ _ Kaya top level, version 0.2.6 | / / _` | || / _` | http : // kayalang.org/
                                                                                |
                                                                                _\_\__,
    _ |\_, \__, _ | Type : ? for help | __ / Kaya &gt; abs(-4) Returned(Int) : 4 Kaya &gt; putStrLn(foo) foo Kaya &gt; putStrLn(foo)(top level) : 1 : Unknown name : foo Kaya &gt; putStrLn(5)(top level) : 1 : Type error in constant 5;
has type Int, expected String
                      Kaya &gt; putStrLn(abs(5))(top level) : 1 : Type error in application of 'abs';
has type Int(Int),
    expected String(t6)
            Kaya
        &gt; : l stdlib / Strings.k
                       Compiling module Strings
                       Strings
    &gt;
    lc(aBcDe)
        Returned(String)
    : abcde
      Strings
      &gt; : q
</code></pre>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>KAYA_LIBRARY_PATH</code></p>
<dd> A list of extra paths to search for kaya libraries. Paths are separated by &#8216;:&#8217; on Posix systems, and &#8216;;&#8217; on Windows.</dl>
<h2>OBTAINING</h2>
<p> The latest release of Kaya can be obtained from &lt;<a rel="nofollow" href="http://kayalang.org/download">http://kayalang.org/download</a>&gt;. You can receive announcements of new versions of Kaya by subscribing to the kaya-announce mailing list &lt;<a href="http://lists.kayalang.org/lists/listinfo/kaya-announce">http://lists.kayalang.org/lists/listinfo/kaya-announce</a>&gt; </p>
<p> Development versions can be obtained using <code><a href="/docs/linux/man/1-darcs/">darcs</a>(1)</code> from &lt;<a rel="nofollow" href="http://kayalang.org/darcs/">http://kayalang.org/darcs/</a>&gt; </p>
<h2>BUGS</h2>
<p> Please report bugs found to &lt;kaya [at] kayalang.org&gt; </p>
<p> <code>kaya</code> does not currently support all features of the Kaya language. </p>
<h2>LICENSE</h2>
<p> <code>kaya</code> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License (version 2 or any later version) as published by the Free Software Foundation. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kayac/">kayac</a>(1)</code> </p>
<h2>Index</h2>
