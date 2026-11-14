---
title: "gofmt(1)"
name: "gofmt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gofmt/"
description: "gofmt – format Go programs"
---

<h2 class="name">NAME</h2>
<p> gofmt &#8211; format Go programs </p>
<h2>SYNOPSIS</h2>
<p> <code>gofmt</code> [<i>flags</i>] [<i>path &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> Gofmt formats Go programs. It uses tabs for indentation and blanks for alignment. Alignment assumes that an editor is using a fixed-width font. </p>
<p> Without an explicit path, it processes the standard input. Given a file, it operates on that file; given a directory, it operates on all .go files in that directory, recursively. (Files starting with a period are ignored.) By default, gofmt prints the reformatted sources to standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Do not print reformatted sources to standard output. If a file&#8217;s formatting is different than gofmt&#8217;s, print diffs to standard output.</p>
<dt><code>-e</code></p>
<dd> Print all (including spurious) errors.</p>
<dt><code>-l</code></p>
<dd> Do not print reformatted sources to standard output. If a file&#8217;s formatting is different from gofmt&#8217;s, print its name to standard output.</p>
<dt><code>-r rule</code></p>
<dd> Apply the rewrite rule to the source before reformatting.</p>
<dt><code>-s</code></p>
<dd> Try to simplify code (after applying the rewrite rule, if any).</p>
<dt><code>-w</code></p>
<dd> Do not print reformatted sources to standard output. If a file&#8217;s formatting is different from gofmt&#8217;s, overwrite it with gofmt&#8217;s version. If an error occurred during overwriting, the original file is restored from an automatic backup.</dl>
<p> Debugging support:</p>
<dl>
<dt><code>-cpuprofile </code><i>filename</i></p>
<dd> Write cpu profile to the specified file.</dl>
<p> The rewrite rule specified with the -r flag must be a string of the form: </p>
<pre>
      pattern -&gt; replacement
</pre>
<p> Both pattern and replacement must be valid Go expressions. In the pattern, single-character lowercase identifiers serve as wildcards matching arbitrary sub-expressions; those expressions will be substituted for the same identifiers in the replacement. </p>
<p> When gofmt reads from standard input, it accepts either a full Go program or a program fragment. A program fragment must be a syntactically valid declaration list, statement list, or expression. When formatting such a fragment, gofmt preserves leading indentation as well as leading and trailing spaces, so that individual sections of a Go program can be formatted by piping them through gofmt.</p>
<h2>EXAMPLES</h2>
<p> To check files for unnecessary parentheses: </p>
<pre>
      gofmt -r '(a) -&gt; a' -l *.go
</pre>
<p> To remove the parentheses: </p>
<pre>
      gofmt -r '(a) -&gt; a' -w *.go
</pre>
<p> To convert the package tree from explicit slice upper bounds to implicit ones: </p>
<pre><code>
gofmt - r 'α[β:len(α)] -&gt; α[β:]' - w $GOROOT / src / pkg
</code></pre>
<h3>The simplify command</h3>
<p> When invoked with -s gofmt will make the following source transformations where possible. </p>
<p>An array, slice, or map composite literal of the form : [] T {T{}, T{} } will be simplified to : [] T &#123;&#123;}, {} }</p>
<pre>
    A slice expression of the form:
        s[a:len(s)]
    will be simplified to:
        s[a:]
</pre>
<pre><code>
    A range of the form:
        for x, _ = range v {...}
    will be simplified to:
        for x = range v
    {
        ...
    }
</code></pre>
<pre>
    A range of the form:
        for _ = range v {...}
    will be simplified to:
        for range v {...}
</pre>
<p> This may result in changes that are incompatible with earlier versions of Go.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go doc cmd/gofmt&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
