---
title: "ncdiff(1)"
name: "ncdiff"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncdiff/"
description: "ncdiff – netCDF Differencer"
---

<h2>NAME</h2>
<p> ncdiff &#8211; netCDF Differencer</p>
<h2>SYNTAX</h2>
<p> ncdiff [-3] [-4] [-6] [-A] [-C] [-c] [-D dbg_lvl ] [-d <i>dim</i>,[ <i>min</i>][,[ <i>max</i>]]] [-F] [-h] [&#8211;hdr_pad <i>sz</i>] [-L <i>dfl_lvl</i>] [-l <i>path</i>] [-O] [-p <i>path</i>] [-R] [-r] [-v <i>var</i>[,&#8230;]] [-x] <i>file_1</i> <i>file_2</i> <i>file_3</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ncdiff</code> subtracts variables in <i>file_2</i> from the corresponding variables (those with the same name) in <i>file_1</i> and stores the results in <i>file_3</i>. Variables in <i>file_2</i> are <i>broadcast</i> to conform to the corresponding variable in <i>file_1</i> if necessary. Broadcasting a variable means creating data in non-existing dimensions from the data in existing dimensions. For example, a two dimensional variable in <i>file_2</i> can be subtracted from a four, three, or two (but not one or zero) dimensional variable (of the same name) in <code>file_1</code>. This functionality allows the user to compute anomalies from the mean. Note that variables in <i>file_1</i> are <i>not</i> broadcast to conform to the dimensions in <i>file_2</i>. Thus, <code>ncdiff</code>, the number of dimensions, or <i>rank</i>, of any processed variable in <i>file_1</i> must be greater than or equal to the rank of the same variable in <i>file_2</i>. Furthermore, the size of all dimensions common to both <i>file_1</i> and <i>file_2</i> must be equal. </p>
<p> When computing anomalies from the mean it is often the case that <i>file_2</i> was created by applying an averaging operator to a file with the same dimensions as <i>file_1</i>, if not <i>file_1</i> itself. In these cases, creating <i>file_2</i> with <code>ncra</code> rather than <code>ncwa</code> will cause the <code>ncdiff</code> operation to fail. For concreteness say the record dimension in <code>file_1</code> is <code>time</code>. If <i>file_2</i> were created by averaging <i>file_1</i> over the <code>time</code> dimension with the <code>ncra</code> operator rather than with the <code>ncwa</code> operator, then <i>file_2</i> will have a <code>time</code> dimension of size 1 rather than having no <code>time</code> dimension at all In this case the input files to <code>ncdiff</code>, <i>file_1</i> and <i>file_2</i>, will have unequally sized <code>time</code> dimensions which causes <code>ncdiff</code> to fail. To prevent this from occuring, use <code>ncwa</code> to remove the <code>time</code> dimension from <i>file_2</i>. An example is given below. </p>
<p> <code>ncdiff</code> will never difference coordinate variables or variables of type <code>NC_CHAR</code> or <code>NC_BYTE</code>. This ensures that coordinates like (e.g., latitude and longitude) are physically meaningful in the output file, <i>file_3</i>. This behavior is hardcoded. <code>ncdiff</code> applies special rules to some NCAR CSM fields (e.g., <code>ORO</code>). See <i>NCAR CSM Conventions</i> for a complete description. Finally, we note that <code>ncflint</code> (ncflint netCDF File Interpolator) can be also perform file subtraction (as well as addition, multiplication and interpolation). </p>
<h2>EXAMPLES</h2>
<p> Say files <code>85_0112.nc</code> and <code>86_0112.nc</code> each contain 12 months of data. Compute the change in the monthly averages from 1985 to 1986:</p>
<dl>
<dt>
<dd> ncdiff 86_0112.nc 85_0112.nc 86m85_0112.nc</dl>
<p> The following examples demonstrate the broadcasting feature of <code>ncdiff</code>. Say we wish to compute the monthly anomalies of <code>T</code> from the yearly average of <code>T</code> for the year 1985. First we create the 1985 average from the monthly data, which is stored with the record dimension <code>time</code>.</p>
<dl>
<dt>
<dd> ncra 85_0112.nc 85.nc<br />
 ncwa -O -a time 85.nc 85.nc</dl>
<p> The second command, <code>ncwa</code>, gets rid of the <code>time</code> dimension of size 1 that <code>ncra</code> left in <code>85.nc</code>. Now none of the variables in <code>85.nc</code> has a <code>time</code> dimension. A quicker way to accomplish this is to use <code>ncwa</code> from the beginning:</p>
<dl>
<dt>
<dd> ncwa -a time 85_0112.nc 85.nc</dl>
<p> We are now ready to use <code>ncdiff</code> to compute the anomalies for 1985:</p>
<dl>
<dt>
<dd> ncdiff -v T 85_0112.nc 85.nc t_anm_85_0112.nc</dl>
<p> Each of the 12 records in <code>t_anm_85_0112.nc</code> now contains the monthly deviation of <code>T</code> from the annual mean of <code>T</code> for each gridpoint. </p>
<p> Say we wish to compute the monthly gridpoint anomalies from the zonal annual mean. A <i>zonal mean</i> is a quantity that has been averaged over the longitudinal (or <i>x</i>) direction. First we use <code>ncwa</code> to average over longitudinal direction <code>lon</code>, creating <code>xavg_85.nc</code>, the zonal mean of <code>85.nc</code>. Then we use <code>ncdiff</code> to subtract the zonal annual means from the monthly gridpoint data:</p>
<dl>
<dt>
<dd> ncwa -a lon 85.nc xavg_85.nc<br />
 ncdiff 85_0112.nc xavg_85.nc tx_anm_85_0112.nc</dl>
<p> Assuming <code>85_0112.nc</code> has dimensions <code>time</code> and <code>lon</code>, this example only works if <code>xavg_85.nc</code> has no <code>time</code> or <code>lon</code> dimension. </p>
<p> As a final example, say we have five years of monthly data (i.e., 60 months) stored in <code>8501_8912.nc</code> and we wish to create a file which contains the twelve month seasonal cycle of the average monthly anomaly from the five-year mean of this data. The following method is just one permutation of many which will accomplish the same result. First use <code>ncwa</code> to create the file containing the five-year mean:</p>
<dl>
<dt>
<dd> ncwa -a time 8501_8912.nc 8589.nc</dl>
<p> Next use <code>ncdiff</code> to create a file containing the difference of each month&#8217;s data from the five-year mean:</p>
<dl>
<dt>
<dd> ncdiff 8501_8912.nc 8589.nc t_anm_8501_8912.nc</dl>
<p> Now use <code>ncks</code> to group the five January anomalies together in one file, and use <code>ncra</code> to create the average anomaly for all five Januarys. These commands are embedded in a shell loop so they are repeated for all twelve months:</p>
<dl>
<dt>
<dd> foreach idx (01 02 03 04 05 06 07 08 09 10 11 12)<br />
 ncks -F -d time,,,12 t_anm_8501_8912.nc foo.<br />
 ncra foo. t_anm_8589_.nc<br />
 end</dl>
<p> Note that <code>ncra</code> understands the <code>stride</code> argument so the two commands inside the loop may be combined into the single command</p>
<dl>
<dt>
<dd> ncra -F -d time,,,12 t_anm_8501_8912.nc foo.</dl>
<p> Finally, use <code>ncrcat</code> to concatenate the 12 average monthly anomaly files into one twelve-record file which contains the entire seasonal cycle of the monthly anomalies:</p>
<dl>
<dt>
<dd> ncrcat t_anm_8589_??.nc t_anm_8589_0112.nc</dl>
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
<p> <code><a href="/docs/linux/man/1-ncap/">ncap</a></code>(1), <code><a href="/docs/linux/man/1-ncap2/">ncap2</a></code>(1), <code><a href="/docs/linux/man/1-ncatted/">ncatted</a></code>(1), <code><a href="/docs/linux/man/1-ncbo/">ncbo</a></code>(1), <code><a href="/docs/linux/man/1-nces/">nces</a></code>(1), <code><a href="/docs/linux/man/1-ncecat/">ncecat</a></code>(1), <code><a href="/docs/linux/man/1-ncflint/">ncflint</a></code>(1), <code><a href="/docs/linux/man/1-ncks/">ncks</a></code>(1), <code><a href="/docs/linux/man/1-nco/">nco</a></code>(1), <code><a href="/docs/linux/man/1-ncpdq/">ncpdq</a></code>(1), <code><a href="/docs/linux/man/1-ncra/">ncra</a></code>(1), <code><a href="/docs/linux/man/1-ncrcat/">ncrcat</a></code>(1), <code><a href="/docs/linux/man/1-ncrename/">ncrename</a></code>(1), <code><a href="/docs/linux/man/1-ncwa/">ncwa</a></code>(1) </p>
<h2>HOMEPAGE</h2>
<p> The <code>NCO</code> homepage at &lt;<a rel="nofollow" href="http://nco.sf.net">http://nco.sf.net</a>&gt; contains more information. </p>
<h2>Index</h2>
