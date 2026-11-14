---
title: "ncap(1)"
name: "ncap"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncap/"
description: "ncap – netCDF Arithmetic Processor"
---

<h2>NAME</h2>
<p> ncap &#8211; netCDF Arithmetic Processor</p>
<h2>SYNTAX</h2>
<p> ncap [-3] [-4] [-6] [-7] [-A] [-C] [-c] [-D <i>dbg_lvl</i>] [-F] [-f] [-h] [&#8211;hdf] [&#8211;hdr_pad <i>sz</i>] [-L <i>dfl_lvl</i>] [-l <i>path</i>] [&#8211;no_tmp_fl] [-O] [-o <i>output-file</i>] [-p <i>path</i>] [-R] [-r] [&#8211;ram_all] [-S <i>script-file</i>]<i>[-s</i> <i>script</i>]<i>[-v</i> <i>var</i>[, &#8230;&nbsp;<wbr>]] <i>input-file [</i> <i>output-file ]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ncap </code> arithmetically processes a netCDF file. However, in about 2008 <code>ncap </code> was deprecated in favor of <code>ncap2</code> which far surpasses its capabilities. <code>ncap will eventually be completely removed from</code> <code>NCO.</code> It is currently retained only because it provides an easier-to-build arithmetic operator than <code>ncap2.</code> </p>
<p> The processing instructions are contained either in the <code>NCO</code> script file <code>fl.nco</code> or in a sequence of command line arguments. The options <code>-s</code> (or long options <code>&#8211;spt</code> or <code>&#8211;script)</code> are used for in-line scripts and <code>-S</code> (or long options <code>&#8211;fl_spt</code> or <code>&#8211;script-file)</code> are used to provide the filename where (usually multiple) scripting commands are pre-stored. <code>ncap</code> was written to perform arbitrary albebraic transformations of data and archive the results as easily as possible. Missing values are treated correctly. The results of the algebraic manipulations are called <i>derived fields. </i> </p>
<p> Unlike the other operators, <code>ncap</code> does not accept a list of variables to be operated on as an argument to <code>-v.</code> Rather, the <code>-v </code> switch takes no arguments and indicates that <code>ncap</code> should output <i>only</i> user-defined variables. <code>ncap</code> does not accept or understand the <code>-x </code> switch. </p>
<h2>EXAMPLES</h2>
<p> Compute the square of variable <code>T</code></p>
<dl>
<dt>
<dd> ncap -s &quot;T2=T*T&quot; in.nc out.nc</dl>
<h2>AUTHOR</h2>
<p> <code>NCO</code> manual pages written by Charlie Zender and originally formatted by Brian Mays. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://sf.net/bugs/?group_id=3331">http://sf.net/bugs/?group_id=3331</a>&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-2014 Charlie Zender<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>NCO</code> is maintained as a Texinfo manual called the <code>NCO User&#8217;s Guide.</code> Because <code>NCO</code> is mathematical in nature, the documentation includes TeX-intensive portions not viewable on character-based displays. Hence the only complete and authoritative versions of the <code>NCO User&#8217;s Guide </code> are the PDF (recommended), DVI, and Postscript versions at &lt;<a rel="nofollow" href="http://nco.sf.net/nco.pdf">http://nco.sf.net/nco.pdf</a>&gt;, &lt;<a href="http://nco.sf.net/nco.dvi">http://nco.sf.net/nco.dvi</a>&gt;, and &lt;<a rel="nofollow" href="http://nco.sf.net/nco.ps">http://nco.sf.net/nco.ps</a>&gt;, respectively. HTML and XML versions are available at &lt;<a rel="nofollow" href="http://nco.sf.net/nco.html">http://nco.sf.net/nco.html</a>&gt; and &lt;<a rel="nofollow" href="http://nco.sf.net/nco.xml">http://nco.sf.net/nco.xml</a>&gt;, respectively. </p>
<p> If the <code>info</code> and <code>NCO</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info nco</code></dl>
<p> should give you access to the complete manual, except for the TeX-intensive portions. </p>
<h2>HOMEPAGE</h2>
<p> The <code>NCO</code> homepage at &lt;<a rel="nofollow" href="http://nco.sf.net">http://nco.sf.net</a>&gt; contains more information. </p>
<h2>Index</h2>
