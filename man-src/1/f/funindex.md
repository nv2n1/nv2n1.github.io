---
title: "funindex(1)"
name: "funindex"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funindex/"
description: "funindex – create an index for a column of a FITS binary table"
---

<h2>NAME</h2>
<p> <code>funindex &#8211; create an index for a column of a FITS binary table</code></p>
<h2>SYNOPSIS</h2>
<p> funindex &lt;switches&gt; &lt;iname&gt; [oname]</p>
<h2>OPTIONS</h2>
<pre><code>
NB : these options are not compatible with Funtools processing.Please
         use the defaults instead.-
    c #compress output using gzip "
    - a #ASCII output,
    ignore - c(default
               : FITS table) "
        - f #FITS table output(default
                               : FITS table) "
        - l #long output,
    i.e.with key value(s)(default
                          : long) "
        - s #short output,
    i.e.no key value(s)(default
                        : long) "
</code></pre>
<h2>DESCRIPTION</h2>
<p> The funindex script creates an index for the specified column (key) by running funtable -s (sort) and then saving the column value and the record number for each sorted row. This index will be used automatically<br />
&nbsp;<wbr>by funtools filtering of that column, provided the index file&#8217;s modification date is later than that of the data file. </p>
<p> The first required argument is the name of the <font SIZE="-1">FITS</font> binary table to index. Please note that text files cannot be indexed at this time. The second required argument is the column (key) name to index. While multiple keys can be specified in principle, the funtools index processing assume a single key and will not recognize files containing multiple keys. </p>
<p> By default, the output index file name is [root]_[key].idx, where [root] is the root of the input file. Funtools looks for this specific file name when deciding whether to use an index for faster filtering. Therefore, the optional third argument (output file name) should not be used for funtools processing. </p>
<p> For example, to create an index on column Y for a given <font SIZE="-1">FITS</font> file, use: </p>
<pre>
  funindex foo.fits Y
</pre>
<p> This will generate an index named foo_y.idx, which will be used by funtools for filters involving the Y column.</p>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
