---
title: "nco(1)"
name: "nco"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nco/"
description: "NCO – netCDF Operators"
---

<h2>NAME</h2>
<p> NCO &#8211; netCDF Operators</p>
<h2>SYNTAX</h2>
<p> operator [ <i>options</i>] <i>input-files</i> <i>output-file</i></p>
<h2>DESCRIPTION</h2>
<p> The netCDF Operators, or <code>NCO</code> are a suite of programs known as <i>operators</i>. Each operator is a standalone, command line program which is executed at the UNIX shell-level like, e.g., <code>ls</code> or <code>mkdir</code>. The operators take netCDF (&lt;<a rel="nofollow" href="http://www.unidata.ucar.edu/packages/netcdf">http://www.unidata.ucar.edu/packages/netcdf</a>&gt;) files as input, then perform a set of operations (e.g., deriving new data, averaging, hyperslabbing, or metadata manipulation) and produce a netCDF file as output. The operators are primarily designed to aid manipulation and analysis of gridded scientific data. The single command style of <code>NCO </code> allows users to manipulate and analyze files interactively and with simple scripts, avoiding the overhead (and some of the power) of a higher level programming environment. The <code>NCO User&#8217;s Guide</code> illustrates their use with examples from the field of climate modeling and analysis. </p>
<p> The available <i>operators </i> are: </p>
<dl>
<dt>
<dd> <code>ncap2</code>, netCDF Arithmetic Processor</dl>
<dl>
<dt>
<dd> <code>ncatted</code>, netCDF Attribute Editor</dl>
<dl>
<dt>
<dd> <code>ncbo</code>, netCDF Binary Operator (includes <code>ncadd</code>, <code>ncsubtract</code>, <code>ncmultiply</code>, <code>ncdivide</code>)</dl>
<dl>
<dt>
<dd> <code>nces</code>, netCDF Ensemble Averager</dl>
<dl>
<dt>
<dd> <code>ncecat</code>, netCDF Ensemble Concatenator</dl>
<dl>
<dt>
<dd> <code>ncflint</code>, netCDF File Interpolator</dl>
<dl>
<dt>
<dd> <code>ncks</code>, netCDF Kitchen Sink</dl>
<dl>
<dt>
<dd> <code>ncpdq</code>, netCDF Permute Dimensions Quickly, Pack Data Quietly</dl>
<dl>
<dt>
<dd> <code>ncra</code>, netCDF Record Averager</dl>
<dl>
<dt>
<dd> <code>ncrcat</code>, netCDF Record Concatenator</dl>
<dl>
<dt>
<dd> <code>ncrename</code>, netCDF Renamer</dl>
<dl>
<dt>
<dd> <code>ncwa</code>, netCDF Weighted Averager.</dl>
<p> (Note that the &quot;averagers&quot; are misnamed because they perform many non-linear operations as well, e.g., total, minimum, maximum, RMS). </p>
<p> The operators are as general as netCDF itself: there are no restrictions on the contents of the netCDF file(s) used as input. <code>NCO</code>&#8216;s internal routines are completely dynamic and impose no limit on the number or sizes of dimensions, variables, and files. <code>NCO </code> is designed to be used both interactively and with large batch jobs. The default operator behavior is often sufficient for everyday needs, and there are numerous command line (i.e., run-time) options, for special cases. <code>NCO</code> works well on all modern operating systems. </p>
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
<p> <code><a href="/docs/linux/man/1-ncap2/">ncap2</a></code>(1), <code><a href="/docs/linux/man/1-ncatted/">ncatted</a></code>(1), <code><a href="/docs/linux/man/1-ncbo/">ncbo</a></code>(1), <code><a href="/docs/linux/man/1-ncdiff/">ncdiff</a></code>(1), <code><a href="/docs/linux/man/1-nces/">nces</a></code>(1), <code><a href="/docs/linux/man/1-ncecat/">ncecat</a></code>(1), <code><a href="/docs/linux/man/1-ncflint/">ncflint</a></code>(1), <code><a href="/docs/linux/man/1-ncks/">ncks</a></code>(1), <code><a href="/docs/linux/man/1-nco/">nco</a></code>(1), <code><a href="/docs/linux/man/1-ncpdq/">ncpdq</a></code>(1), <code><a href="/docs/linux/man/1-ncra/">ncra</a></code>(1), <code><a href="/docs/linux/man/1-ncrcat/">ncrcat</a></code>(1), <code><a href="/docs/linux/man/1-ncrename/">ncrename</a></code>(1), <code><a href="/docs/linux/man/1-ncwa/">ncwa</a></code>(1) </p>
<h2>HOMEPAGE</h2>
<p> The <code>NCO</code> homepage at &lt;<a rel="nofollow" href="http://nco.sf.net">http://nco.sf.net</a>&gt; contains more information. </p>
<h2>Index</h2>
