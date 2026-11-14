---
title: "urifind(1)"
name: "urifind"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urifind/"
---

<h2 class="name">NAME</h2>
 

 urifind - find URIs in a document and dump them to STDOUT. 

<h2>SYNOPSIS</h2>

 <pre>
    $ urifind file
</pre>

<h2>DESCRIPTION</h2>

 <i>urifind</i> is a simple script that finds URIs in one or more files (using <tt>&quot;URI::Find&quot;</tt>), and outputs them to to <font SIZE="-1">STDOUT. </font> That's it. 

 To find all the URIs in <i>file1</i>, use: 

 <pre>
    $ urifind file1
</pre> 

 To find the URIs in multiple files, simply list them as arguments: 

 <pre>
    $ urifind file1 file2 file3
</pre> 

 <i>urifind</i> will read from <tt>&quot;STDIN&quot;</tt> if no files are given or if a filename of <tt>&quot;-&quot;</tt> is specified: 

 <pre>
    $ wget <a rel="nofollow" HREF="http://www.boston.com/">http://www.boston.com/</a> -O - | urifind
</pre> 

 When multiple files are listed, <i>urifind</i> prefixes each found <font SIZE="-1">URI</font> with the file from which it came: 

 <pre>
    $ urifind file1 file2
    file1: <a rel="nofollow" HREF="http://www.boston.com/index.html">http://www.boston.com/index.html</a>
    file2: <a rel="nofollow" HREF="http://use.perl.org/">http://use.perl.org/</a>
</pre> 

 This can be turned on for single files with the <tt>&quot;-p&quot;</tt> (``prefix'') switch: 

 <pre>
    $urifind -p file3
    file1: <a rel="nofollow" HREF="http://fsck.com/rt/">http://fsck.com/rt/</a>
</pre> 

 It can also be turned off for multiple files with the <tt>&quot;-n&quot;</tt> (``no prefix'') switch: 

 <pre>
    $ urifind -n file1 file2
    <a rel="nofollow" HREF="http://www.boston.com/index.html">http://www.boston.com/index.html</a>
    <a rel="nofollow" HREF="http://use.perl.org/">http://use.perl.org/</a>
</pre> 

 By default, URIs will be displayed in the order found; to sort them ascii-betically, use the <tt>&quot;-s&quot;</tt> (``sort'') option. To reverse sort them, use the <tt>&quot;-r&quot;</tt> (``reverse'') flag (<tt>&quot;-r&quot;</tt> implies <tt>&quot;-s&quot;</tt>). 

 <pre><code>
$ urifind - s file1 file2 http :        // use.perl.org/
                                 http : // www.boston.com/index.html
                                        mailto : webmaster[at] boston.com $ urifind -
    r file1 file2
        mailto : webmaster[at] boston.com
                     http :       // www.boston.com/index.html
                            http: // use.perl.org/
</code></pre> 

 Finally, <i>urifind</i> supports limiting the returned URIs by scheme or by arbitrary pattern, using the <tt>&quot;-S&quot;</tt> option (for schemes) and the <tt>&quot;-P&quot;</tt> option. Both <tt>&quot;-S&quot;</tt> and <tt>&quot;-P&quot;</tt> can be specified multiple times: 

 <pre><code>
$ urifind - S mailto file1 mailto : webmaster[at] boston.com $ urifind - S mailto - S http file1 mailto : webmaster[at] boston.com http: // www.boston.com/index.html
</code></pre> 

 <tt>&quot;-P&quot;</tt> takes an arbitrary Perl regex. It might need to be protected from the shell: 

 <pre>
    $ urifind -P 's?html?' file1
    <a rel="nofollow" HREF="http://www.boston.com/index.html">http://www.boston.com/index.html</a>
    $ urifind -P '\.org\b' -S http file4
    <a rel="nofollow" HREF="http://www.gnu.org/software/wget/wget.html">http://www.gnu.org/software/wget/wget.html</a>
</pre> 

 Add a <tt>&quot;-d&quot;</tt> to have <i>urifind</i> dump the refexen generated from <tt>&quot;-S&quot;</tt> and <tt>&quot;-P&quot;</tt> to <tt>&quot;STDERR&quot;</tt>. <tt>&quot;-D&quot;</tt> does the same but exits immediately: 

 <pre>
    $ urifind -P '\.org\b' -S http -D 
    $scheme = '^(\bhttp\b):'
    @pats = ('^(\bhttp\b):', '\.org\b')
</pre> 

 To remove duplicates from the results, use the <tt>&quot;-u&quot;</tt> (``unique'') switch.

<h2>OPTION SUMMARY</h2>

<dl>
<dt>-s
<dd> Sort results.
<dt>-r
<dd> Reverse sort results (implies -s).
<dt>-u
<dd> Return unique results only.
<dt>-n
<dd> Don't include filename in output.
<dt>-p
<dd> Include filename in output (0 by default, but 1 if multiple files are included on the command line).
<dt>-P $re
<dd> Print only lines matching regex '$re' (may be specified multiple times).
<dt>-S $scheme
<dd> Only this scheme (may be specified multiple times).
<dt>-h
<dd> Help summary.
<dt>-v
<dd> Display version and exit.
<dt>-d
<dd> Dump compiled regexes for <tt>&quot;-S&quot;</tt> and <tt>&quot;-P&quot;</tt> to <tt>&quot;STDERR&quot;</tt>.
<dt>-D
<dd> Same as <tt>&quot;-d&quot;</tt>, but exit after dumping.</dl>

<h2>AUTHOR</h2>

 darren chamberlain &lt;darren [at] cpan.org&gt;

<h2>COPYRIGHT</h2>

 (C) 2003 darren chamberlain 

 This library is free software; you may distribute it and/or modify it under the same terms as Perl itself.

<h2>SEE ALSO</h2>

 URI::Find 

<h2>Index</h2>


