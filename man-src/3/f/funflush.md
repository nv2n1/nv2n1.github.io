---
title: "funflush(3)"
name: "funflush"
section: "3"
letter: "f"
url: "/docs/linux/man/3-funflush/"
description: "FunFlush – flush data to output file"
---

<h2>NAME</h2>
<p> <code>FunFlush &#8211; flush data to output file</code></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;funtools.h&gt;
</code></pre>
<pre>
  void FunFlush(Fun fun, char *plist)
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>FunFlush</code> routine will flush data to a <font SIZE="-1">FITS</font> output file. In particular, it can be called after all rows have been written (using the <i>FunTableRowPut()</i> routine) in order to add the null padding that is required to complete a <font SIZE="-1">FITS</font> block. It also should be called after completely writing an image using <i>FunImagePut()</i> or after writing the final row of an image using <i>FunTableRowPut()</i>. </p>
<p> The <code>plist</code> (i.e., parameter list) argument is a string containing one or more comma-delimited <code>keyword=value</code> parameters. If the plist string contains the parameter &#8220;copy=remainder&#8221; and the file was opened with a reference file, which, in turn, was opened for extension copying (i.e. the input <i>FunOpen()</i> mode also was &#8220;c&#8221; or &#8220;C&#8221;), then FunFlush also will copy the remainder of the <font SIZE="-1">FITS</font> extensions from the input reference file to the output file. This normally would be done only at the end of processing. </p>
<p> Note that <i>FunFlush()</i> is called with &#8220;copy=remainder&#8221; in the mode string by <i>FunClose()</i>. This means that if you close the output file before the reference input file, it is not necessary to call <i>FunFlush()</i> explicitly, unless you are writing more than one extension. See the evmerge example code. However, it is safe to call <i>FunFlush()</i> more than once without fear of re-writing either the padding or the copied extensions. </p>
<p> In addition, if <i>FunFlush()</i> is called on an output file with the plist set to &#8220;copy=reference&#8221; and if the file was opened with a reference file, the reference extension is written to the output file. This mechanism provides a simple way to copy input extensions to an output file without processing the former. For example, in the code fragment below, an input extension is set to be the reference file for a newly opened output extension. If that reference extension is not a binary table, it is written to the output file: </p>
<pre><code>
/* process each input extension in turn */
for (ext = 0;; ext++) {
    /* get new extension name */
    sprintf(tbuf, "%s[%d]", argv[1], ext);
    /* open input extension -- if we cannot open it, we are done */
    if (!(ifun = FunOpen(tbuf, "r", NULL)))
        break;
    /* make the new extension the reference handle for the output file */
    FunInfoPut(ofun, FUN_IFUN, &amp;ifun, 0);
    /* if its not a binary table, just write it out */
    if (!(s = FunParamGets(ifun, "XTENSION", 0, NULL, &amp;got)) ||
        strcmp(s, "BINTABLE")) {
        if (s)
            free(s);
        FunFlush(ofun, "copy=reference");
        FunClose(ifun);
        continue;
    } else {
        /* process binary table */
        ....
    }
}
</code></pre>
<h2>SEE ALSO</h2>
<p> See <a href="/docs/linux/man/n-funtools/">funtools</a>(n) for a list of Funtools help pages </p>
<h2>Index</h2>
