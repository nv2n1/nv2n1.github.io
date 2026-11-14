---
title: "ncflint(1)"
name: "ncflint"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncflint/"
description: "ncflint – netCDF File Interpolator"
---

<h2>NAME</h2>
<p> ncflint &#8211; netCDF File Interpolator</p>
<h2>SYNTAX</h2>
<p> ncflint [-3] [-4] [-6] [-7] [-A] [&#8211;bfr <i>sz</i>]<i>[-C]</i>[-c]<i>[-D</i> <i>dbg_lvl</i>] [-d <i>dim</i>,[ <i>min</i>][,[ <i>max</i>]]] [-F] [&#8211;fix_rec_crd] [-G <i>gpe_dsc</i>] [-g <i>grp</i>[,&#8230;]] [-h] [&#8211;hdf] [&#8211;hdr_pad <i>sz</i>] [-i <i>var,</i>val3<i>]</i>[-L <i>dfl_lvl</i>]<i>[-l</i> <i>path</i>] [&#8211;msa] [&#8211;no_tmp_fl] [-O] [-p <i>path</i>] [-R] [-r] [&#8211;ram_all] [-t <i>thr_nbr</i>] [&#8211;unn] [-v <i>var</i>[,&#8230;]] [-w <i>wgt[,</i> <i>wgt2</i>]] [-X <i>box</i>] [-x] <i>file1 file2 file3</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ncflint</code> creates an output file that is a linear combination of the input files. This linear combination can be a weighted average, a normalized weighted average, or an interpolation of the input files. Coordinate variables are not acted upon in any case, they are simply copied from <i>file_1.</i><br />
&nbsp;<wbr>There are two conceptually distinct methods of using&nbsp;<wbr> <code>ncflint.</code> The first method is to specify the weight each input file is to have in the output file. In this method, the value <i>val3</i> of a variable in the output file <i>file_3</i> is determined from its values <i>val1</i> and <i>val2</i> in the two input files according to <i>wgt1*val1</i>+<i>wgt2*val2</i> </p>
<p> Here at least <i>wgt1,</i> and, optionally, <i>wgt2,</i> are specified on the command line with the <code>-w</code> (or <code>&#8211;weight</code> or <code>&#8211;wgt_var</code> ) switch. If only IR wgt1 is specified then <i>wgt2</i> is automatically computed as <i>wgt2</i>=<i>1</i>&#8211;<i>wgt1.</i> Note that weights larger than 1 are allowed. Thus it is possible to specify <i>wgt1</i>=<i>2</i> and <i>wgt2</i>=<i>-3.</i> One can use this functionality to multiply all the values in a given file by a constant. </p>
<p> The second method of using <code>ncflint</code> is to specify the interpolation option with <code>-i</code> (or with the <code>&#8211;ntp</code> or <code>&#8211;interpolate</code> long options). This is really the inverse of the first method in the following sense. When the user specifies the weights directly, <code>ncflint</code> has no work to do besides multiplying the input values by their respective weights and adding the results together to produce the output values. This assumes it is the weights that are known a priori. In another class of cases it is the &quot;arrival value&quot; (i.e., <i>val3</i> ) of a particular variable <i>var</i> that is known a priori. In this case, the implied weights can always be inferred by examining the values of <i>var</i> in the input files. This results in one equation in two unknowns, <i>wgt1</i> and <i>wgt2:</i> <i>val3</i>=<i>wgt1*val1</i>+<i>wgt2*val2.</i> </p>
<p> Unique determination of the weights requires imposing the additional constraint of normalization on the weights: <i>wgt1</i>+<i>wgt2</i>=<i>1.</i> Thus, to use the interpolation option, the user specifies <i>var</i> and <i>val3</i> with the <code>-i</code> option. <code>ncflint</code> will compute <i>wgt1</i> and <i>wgt2,</i> and use these weights on all variables to generate the output file. Although <i>var</i> may have any number of dimensions in the input files, it must represent a single, scalar value. Thus any dimensions associated with <i>var</i> must be &quot;degenerate&quot;, i.e., of size one. </p>
<p>&nbsp;<wbr>If neither&nbsp;<wbr> <code>-i</code> nor <code>-w</code> is specified on the command line, <code>ncflint</code> defaults to weighting each input file equally in the output file. This is equivalent to specifying <i>-w</i>0.5 or <i>-w</i>0.5,0.5. Attempting to specify both .BR <code>-i</code> and <code>-w</code> methods in the same command is an error. </p>
<p> <code>ncflint</code> is programmed not to interpolate variables of type <code>NC_CHAR</code> and <code>NC_BYTE.</code> This behavior is hardcoded. </p>
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
