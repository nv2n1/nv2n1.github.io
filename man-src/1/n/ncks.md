---
title: "ncks(1)"
name: "ncks"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncks/"
description: "ncks – netCDF Kitchen Sink"
---

<h2>NAME</h2>
<p> ncks &#8211; netCDF Kitchen Sink</p>
<h2>SYNTAX</h2>
<p> ncks [-3] [-4] [-5] [-6] [-7] [-A] [-a] [-b <i>bnr_fl]</i> [&#8211;bfr <i>sz</i>]<i>[-C]</i>[-c] [&#8211;cdl] [&#8211;cnk_byt <i>sz</i>]<i>[&#8211;cnk_dmn</i> <i>nm,sz</i>] [&#8211;cnk_map <i>map</i>] [&#8211;cnk_plc <i>plc</i>] [&#8211;cnk_scl <i>sz</i>] [-D dbg_lvl] [-d <i>dim</i>,[ <i>min</i>][,[ <i>max</i>]][,[ <i>stride</i>]]] [-F] [&#8211;fix_rec_dmn <i>dim</i>] [-G <i>gpe_dsc</i>] [-g <i>grp</i>[,&#8230;]] [-H] [-h] [&#8211;hdn] [&#8211;hdr_pad <i>sz</i>] [-L <i>dfl_lvl</i>] [-l <i>path</i>] [-M] [-m] [&#8211;md5] [&#8211;mk_rec_dmn <i>dim</i>]<i>[&#8211;msa]</i>[&#8211;no_blank]<i>[&#8211;no_tmp_fl]</i>[-O]<i>[-o</i> <i>output-file</i>] [-P] [-p <i>path</i>] [-Q] [-q] [-R] [-r] [&#8211;rad] [&#8211;ram_all] [-s <i>format</i>] [-u] [&#8211;unn] [-v <i>var</i>[,&#8230;]] [-X <i>box</i>] [-x] [&#8211;xml] <i>input-file</i> [ <i>output-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ncks</code> combines every feature we could think of, except the kitchen sink, into one versatile utility to manipulate netCDF files. <code>ncks</code> extracts a subset of the data from <i>input-file</i> and either prints it as ASCII text to stdout, or writes (or pastes) it to <i>output-file</i>, or both. </p>
<p> <code>ncks</code> will print netCDF data in ASCII format to <code>stdout</code>, like <code>ncdump</code>, but with these differences: <code>ncks</code> prints data in a tabular format intended to be easy to search for the data you want, one datum per screen line, with all dimension subscripts and coordinate values (if any) preceding the datum. Option <code>-s</code> allows the user the format the data using C-style format strings. </p>
<p> Options <code>-a</code>, <code>-F</code>, <code>-H</code>, <code>-M</code>, <code>-m</code>, <code>-q</code>, <code>-s</code>, and <code>-u</code> control the formatted appearance of the data. </p>
<p> <code>ncks</code> will extract (and optionally create a new netCDF file comprised of) only selected variable from the input file, like <code>ncextr</code> but with these differences: Only variables and coordinates may be specifically included or excluded&#8212;all global attributes and any attribute associated with an extracted variable will be copied to the screen and/or output netCDF file. Options <code>-c</code>, <code>-C</code>, <code>-v</code>, and <code>-x</code> control which variables are extracted. </p>
<p> <code>ncks</code> will extract hyperslabs from the specified variables. In fact <code>ncks</code> implements the nccut specification exactly. Option <code>-d</code> controls the hyperslab specification. </p>
<p> Input dimensions that are not associated with any output variable will not appear in the output netCDF. This feature removes superfluous dimensions from a netCDF file. </p>
<p> <code>ncks</code> will append variables and attributes from the <i>input-file</i> to <i>output-file</i> if <i>output-file</i> is a pre-existing netCDF file whose relevant dimensions conform to dimension sizes of <i>input-file</i>. The append features of <code>ncks</code> are intended to provide a rudimentary means of adding data from one netCDF file to another, conforming, netCDF file. When naming conflicts exists between the two files, data in <i>output-file</i> is usually overwritten by the corresponding data from <i>input-file</i>. Thus it is recommended that the user backup <i>output-file</i> in case valuable data is accidentally overwritten. </p>
<p> If <i>output-file</i> exists, the user will be queried whether to <i>overwrite</i>, <i>append</i>, or <i>exit</i> the <code>ncks</code> call completely. Choosing <i>overwrite</i> destroys the existing <i>output-file</i> and create an entirely new one from the output of the <code>ncks</code> call. Append has differing effects depending on the uniqueness of the variables and attributes output by <code>ncks</code>: If a variable or attribute extracted from <i>input-file</i> does not have a name conflict with the members of <i>output-file</i> then it will be added to <i>output-file</i> without overwriting any of the existing contents of <i>output-file</i>. In this case the relevant dimensions must agree (conform) between the two files; new dimensions are created in <i>output-file</i> as required. When a name conflict occurs, a global attribute from <i>input-file</i> will overwrite the corresponding global attribute from <i>output-file</i>. If the name conflict occurs for a non-record variable, then the dimensions and type of the variable (and of its coordinate dimensions, if any) must agree (conform) in both files. Then the variable values (and any coordinate dimension values) from <i>input-file</i> will overwrite the corresponding variable values (and coordinate dimension values, if any) in <i>output-file</i> </p>
<p> Since there can only be one record dimension in a file, the record dimension must have the same name (but not necessarily the same size) in both files if a record dimension variable is to be appended. If the record dimensions are of differing sizes, the record dimension of <i>output-file</i> will become the greater of the two record dimension sizes, the record variable from <i>input-file</i> will overwrite any counterpart in <i>output-file</i> and fill values will be written to any gaps left in the rest of the record variables (I think). In all cases variable attributes in <i>output-file</i> are superseded by attributes of the same name from <i>input-file</i>, and left alone if there is no name conflict. </p>
<p> Some users may wish to avoid interactive <code>ncks</code> queries about whether to overwrite existing data. For example, batch scripts will fail if <code>ncks</code> does not receive responses to its queries. Options <code>-O</code> and <code>-A</code> are available to force overwriting existing files and variables, respectively. </p>
<p> Options specific to <code>ncks</code> </p>
<p> The following list provides a short summary of the features unique to <code>ncks</code>. </p>
<dl>
<dt><code>-a </code></p>
<dd> Do not alphabetize extracted fields. By default, the specified output variables are extracted, printed, and written to disk in alphabetical order. This tends to make long output lists easier to search for particular variables. Specifying <code>-a</code> results in the variables being extracted, printed, and written to disk in the order in which they were saved in the input file. Thus <code>-a</code> retains the original ordering of the variables.</dl>
<dl>
<dt><code>-d </code></p>
<dd> <i>dim</i>,[ <i>min</i>][,[ <i>max</i>]][,[ <i>stride</i>]] Add <i>stride</i> argument to hyperslabber.</dl>
<dl>
<dt><code>-H </code></p>
<dd> Print data to screen. The default behavior is to print data to screen if no netCDF output file is specified. Use <code>-H </code> to print data to screen if a netCDF output is specified (the same behavior applies to <code>-m</code> ). Unless otherwise specified (with <code>-s</code>), each element of the data hyperslab is printed on a separate line containing the names, indices, and, values, if any, of all of the variables dimensions. The dimension and variable indices refer to the location of the corresponding data element with respect to the variable as stored on disk (i.e., not the hyperslab).</p>
<dl>
<dt>
<dd> % ncks -H -C -v three_dmn_var in.nc<br />
 lat[0]=-90 lev[0]=100 lon[0]=0 three_dmn_var[0]=0<br />
 lat[0]=-90 lev[0]=100 lon[1]=90 three_dmn_var[1]=1<br />
 lat[0]=-90 lev[0]=100 lon[2]=180 three_dmn_var[2]=2<br />
 &nbsp;<wbr>&#8230;&nbsp;<wbr><br />
 lat[1]=90 lev[2]=1000 lon[1]=90 three_dmn_var[21]=21<br />
 lat[1]=90 lev[2]=1000 lon[2]=180 three_dmn_var[22]=22<br />
 lat[1]=90 lev[2]=1000 lon[3]=270 three_dmn_var[23]=23</dl>
<p> Printing the same variable with the <code>-F</code> option shows the same variable indexed with Fortran conventions</p>
<dl>
<dt>
<dd> % ncks -F -H -C -v three_dmn_var in.nc<br />
 <a href="/docs/linux/man/1-lon/">lon</a>(1)=0 <a href="/docs/linux/man/1-lev/">lev</a>(1)=100 <a href="/docs/linux/man/1-lat/">lat</a>(1)=-90 <a href="/docs/linux/man/1-three_dmn_var/">three_dmn_var</a>(1)=0<br />
 <a href="/docs/linux/man/2-lon/">lon</a>(2)=90 <a href="/docs/linux/man/1-lev/">lev</a>(1)=100 <a href="/docs/linux/man/1-lat/">lat</a>(1)=-90 <a href="/docs/linux/man/2-three_dmn_var/">three_dmn_var</a>(2)=1<br />
 <a href="/docs/linux/man/3-lon/">lon</a>(3)=180 <a href="/docs/linux/man/1-lev/">lev</a>(1)=100 <a href="/docs/linux/man/1-lat/">lat</a>(1)=-90 <a href="/docs/linux/man/3-three_dmn_var/">three_dmn_var</a>(3)=2<br />
 &nbsp;<wbr>&#8230;&nbsp;<wbr></dl>
<p> Printing a hyperslab does not affect the variable or dimension indices since these indices are relative to the full variable (as stored in the input file), and the input file has not changed. However, if the hypserslab is saved to an output file and those values are printed, the indices will change:</p>
<dl>
<dt>
<dd> % ncks -H -d lat,90.0 -d lev,1000.0 -v three_dmn_var in.nc out.nc<br />
 lat[1]=90 lev[2]=1000 lon[0]=0 three_dmn_var[20]=20<br />
 lat[1]=90 lev[2]=1000 lon[1]=90 three_dmn_var[21]=21<br />
 lat[1]=90 lev[2]=1000 lon[2]=180 three_dmn_var[22]=22<br />
 lat[1]=90 lev[2]=1000 lon[3]=270 three_dmn_var[23]=23<br />
 % ncks -H out.nc<br />
 lat[0]=90 lev[0]=1000 lon[0]=0 three_dmn_var[0]=20<br />
 lat[0]=90 lev[0]=1000 lon[1]=90 three_dmn_var[1]=21<br />
 lat[0]=90 lev[0]=1000 lon[2]=180 three_dmn_var[2]=22<br />
 lat[0]=90 lev[0]=1000 lon[3]=270 three_dmn_var[3]=23</dl>
</dl>
<dl>
<dt><code>-M</code></p>
<dd> Print to screen the global metadata describing the file. This includes file summary information and global attributes.</dl>
<dl>
<dt><code>-m</code></p>
<dd> Print variable metadata to screen (similar to <code>ncdump -h</code>). This displays all metadata pertaining to each variable, one variable at a time.</dl>
<dl>
<dt><code>-q </code></p>
<dd> Toggle printing of dimension indices and coordinate values when printing arrays. The name of each variable will appear flush left in the output. This is useful when trying to locate specific variables when displaying many variables with different dimensions. The mnemonic for this option is &quot;quiet&quot;.</dl>
<dl>
<dt><code>-s </code></p>
<dd> <i>format</i> String format for text output. Accepts C language escape sequences and <code>printf()</code> formats.</dl>
<dl>
<dt><code>-u </code></p>
<dd> Accompany the printing of a variable&#8217;s values with its units attribute, if it exists.</dl>
<h2>EXAMPLES</h2>
<p> View all data in netCDF <code>in.nc</code>, printed with Fortran indexing conventions:</p>
<dl>
<dt>
<dd> ncks -H -F in.nc</dl>
<p> Copy the netCDF file <code>in.nc</code> to file <code>out.nc</code>.</p>
<dl>
<dt>
<dd> ncks -O in.nc out.nc</dl>
<p> Now the file <code>out.nc</code> contains all the data from <code>in.nc</code>. There are, however, two differences between <code>in.nc</code> and <code>out.nc</code>. First, the <code>history</code> global attribute will contain the command used to create <code>out.nc</code>. Second, the variables in <code>out.nc</code> will be defined in alphabetical order. Of course the internal storage of variable in a netCDF file should be transparent to the user, but there are cases when alphabetizing a file is useful (see description of <code>-a</code> switch). </p>
<p> Print variable <code>three_dmn_var</code> from file <code>in.nc</code> with default notations. Next print <code>three_dmn_var</code> as an un-annotated text column. Then print <code>three_dmn_var</code> signed with very high precision. Finally, print <code>three_dmn_var</code> as a comma-separated list.</p>
<dl>
<dt>
<dd> % ncks -H -C -v three_dmn_var in.nc<br />
 lat[0]=-90 lev[0]=100 lon[0]=0 three_dmn_var[0]=0<br />
 lat[0]=-90 lev[0]=100 lon[1]=90 three_dmn_var[1]=1<br />
 &nbsp;<wbr>&#8230;&nbsp;<wbr><br />
 lat[1]=90 lev[2]=1000 lon[3]=270 three_dmn_var[23]=23<br />
 % ncks -s &quot;%f
&quot; -H -C -v three_dmn_var in.nc<br />
 0.000000<br />
 1.000000<br />
 &nbsp;<wbr>&#8230;&nbsp;<wbr><br />
 23.000000<br />
 % ncks -s &quot;%+16.10f
&quot; -H -C -v three_dmn_var in.nc </p>
<p>+0.0000000000 </p>
<p>+1.0000000000<br />
 &nbsp;<wbr>&#8230;&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>+23.0000000000<br />
 % ncks -s &quot;%f, &quot; -H -C -v three_dmn_var in.nc<br />
 0.000000, 1.000000, &nbsp;<wbr>&#8230; , 23.000000,</dl>
<p> The second and third options are useful when pasting data into text files like reports or papers. </p>
<p> One dimensional arrays of characters stored as netCDF variables are automatically printed as strings, whether or not they are NUL-terminated, e.g.,</p>
<dl>
<dt>
<dd> ncks -v fl_nm in.nc</dl>
<p> The <code>%c</code> formatting code is useful for printing multidimensional arrays of characters representing fixed length strings</p>
<dl>
<dt>
<dd> ncks -H -s &quot;%c&quot; -v fl_nm_arr in.nc</dl>
<p> Using the <code>%s</code> format code on strings which are not NUL-terminated (and thus not technically strings) is likely to result in a core dump. </p>
<p> Create netCDF <code>out.nc</code> containing all variables, and any associated coordinates, except variable <code>time</code>, from netCDF <code>in.nc</code>:</p>
<dl>
<dt>
<dd> ncks -x -v time in.nc out.nc</dl>
<p> Extract variables <code>time</code> and <code>pressure</code> from netCDF <code>in.nc</code>. If <code>out.nc</code> does not exist it will be created. Otherwise the you will be prompted whether to append to or to overwrite <code>out.nc</code>:</p>
<dl>
<dt>
<dd> ncks -v time,pressure in.nc out.nc<br />
 ncks -C -v time,pressure in.nc out.nc</dl>
<p> The first version of the command creates an <code>out.nc</code> which contains <code>time</code>, <code>pressure</code>, and any coordinate variables associated with <i>pressure</i>. The <code>out.nc</code> from the second version is guaranteed to contain only two variables <code>time</code> and <code>pressure</code>. </p>
<p> Create netCDF <code>out.nc</code> containing all variables from file <code>in.nc</code>. Restrict the dimensions of these variables to a hyperslab. Print (with <code>-H</code>) the hyperslabs to the screen for good measure. The specified hyperslab is: the sixth value in dimension <code>time</code>; the half-open range <i>lat</i> &lt;= 0.0 in coordinate <code>lat</code>; the half-open range <i>lon</i> &gt;= 330.0 in coordinate <code>lon</code>; the closed interval 0.3 &lt;= <i>band</i> &lt;= 0.5 in coordinate <code>band</code>; and cross-section closest to 1000.0 in coordinate <code>lev</code>. Note that limits applied to coordinate values are specified with a decimal point, and limits applied to dimension indices do not have a decimal point.</p>
<dl>
<dt>
<dd> ncks -H -d time,5 -d lat,,0. -d lon,330., -d band,.3,.5 -d lev,1000. in.nc out.nc</dl>
<p> Assume the domain of the monotonically increasing longitude coordinate <code>lon</code> is 0 &lt; <i>lon</i> &lt; 360. Here, <code>lon</code> is an example of a wrapped coordinate. <code>ncks</code> will extract a hyperslab which crosses the Greenwich meridian simply by specifying the westernmost longitude as <i>min</i> and the easternmost longitude as <i>max</i>, as follows:</p>
<dl>
<dt>
<dd> ncks -d lon,260.,45. in.nc out.nc</dl>
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
<p> <code><a href="/docs/linux/man/1-ncap/">ncap</a></code>(1), <code><a href="/docs/linux/man/1-ncap2/">ncap2</a></code>(1), <code><a href="/docs/linux/man/1-ncatted/">ncatted</a></code>(1), <code><a href="/docs/linux/man/1-ncbo/">ncbo</a></code>(1), <code><a href="/docs/linux/man/1-ncdiff/">ncdiff</a></code>(1), <code><a href="/docs/linux/man/1-nces/">nces</a></code>(1), <code><a href="/docs/linux/man/1-ncecat/">ncecat</a></code>(1), <code><a href="/docs/linux/man/1-ncflint/">ncflint</a></code>(1), <code><a href="/docs/linux/man/1-ncks/">ncks</a></code>(1), <code><a href="/docs/linux/man/1-nco/">nco</a></code>(1), <code><a href="/docs/linux/man/1-ncpdq/">ncpdq</a></code>(1), <code><a href="/docs/linux/man/1-ncra/">ncra</a></code>(1), <code><a href="/docs/linux/man/1-ncrcat/">ncrcat</a></code>(1), <code><a href="/docs/linux/man/1-ncrename/">ncrename</a></code>(1), <code><a href="/docs/linux/man/1-ncwa/">ncwa</a></code>(1) </p>
<h2>HOMEPAGE</h2>
<p> The <code>NCO</code> homepage at &lt;<a rel="nofollow" href="http://nco.sf.net">http://nco.sf.net</a>&gt; contains more information. </p>
<h2>Index</h2>
