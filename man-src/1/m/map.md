---
title: "map(1)"
name: "map"
section: "1"
letter: "m"
url: "/docs/linux/man/1-map/"
---

<h2 class="name">NAME</h2>
 

 map - An utility to map texts from and to unicode 

<h2>SYNOPSIS</h2>

 <pre><code>
map - recode from and to various character sets.Reads from STDIN, writes to STDOUT.usage : map[--from cset][--to cset]&lt;input.txt&gt; output.txt
                                                                                               from s Encoding of input files(default "ISO-8859-1")
                                                                                                   list Lists available character sets and their alias names.to s Encoding of output files(default "ISO-8859-1")
</code></pre>

<h2>DESCRIPTION</h2>

 Maps text from one character set representation to another. This work is actually long time very well done by <tt>&quot;recode&quot;</tt>, but unfortunately recode does not support Unicode and eastern asia character sets. But, if you have pure 8 bit things to do, recode will still be the best solution. 

 Examples: 

 Conversion from <font SIZE="-1">ISO-8859-1</font> to Unicode: 

 <pre>
 map --to unicode &lt; iso-8859-1.txt &gt; unicode.txt
</pre> 

 Conversion from <font SIZE="-1">GB2312</font> to <font SIZE="-1">CP936:</font> 

 <pre>
 map --from cp936 --to GB2312 &lt; gb2312.txt &gt; cp936.txt
</pre> 

 Conversion from <font SIZE="-1">CP850</font> to Unicode: 

 <pre>
 map --from cp850 --to unicode &lt; cp850.txt &gt; unicode.txt
</pre>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-recode/">recode</a></i>(1), <i><a HREF="/docs/linux/man/3-unicode--map/">Unicode::Map</a></i>(3), <i><a HREF="/docs/linux/man/3-unicode--map8/">Unicode::Map8</a></i>(3), <i><a HREF="/docs/linux/man/3-unicode--string/">Unicode::String</a></i>(3)

<h2>AUTHOR</h2>

 Martin Schwartz &lt;<i>martin [at] nacho.de</i>&gt;. 

<h2>Index</h2>


