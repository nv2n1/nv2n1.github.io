---
title: "ncatted(1)"
name: "ncatted"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncatted/"
description: "ncatted – netCDF Attribute Editor"
---

<h2>NAME</h2>
<p> ncatted &#8211; netCDF Attribute Editor</p>
<h2>SYNTAX</h2>
<p> ncatted [-a <i>att_dsc</i>] [-a &#8230;] [&#8211;bfr <i>sz</i>]<i>[-D</i> <i>dbg_lvl]</i> [-h] [&#8211;hdr_pad <i>sz</i>] [-l path] [-O] [-p path] [-R] [-r] [&#8211;ram_all] <i>input-file</i> [ <i>output-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ncatted</code> edits attributes in a netCDF file. If you are editing attributes then you are spending too much time in the world of metadata, and <code>ncatted</code> was written to get you back out as quickly and painlessly as possible. <code>ncatted</code> can <i>append</i>, <i>create</i>, <i>delete</i>, <i>modify</i>, and <i>overwrite</i> attributes (all explained below). Furthermore, <code>ncatted</code> allows each editing operation to be applied to every variable in a file, thus saving you time when you want to change attribute conventions throughout a file. <code>ncatted</code> interprets character attributes as strings. </p>
<p> Because repeated use of <code>ncatted</code> can considerably increase the size of the <code>history</code> global attribute, the <code>-h</code> switch is provided to override automatically appending the command to the <code>history</code> global attribute in the <i>output-file</i>. </p>
<p> When <code>ncatted</code> is used to change the <code>_FillValue</code> attribute, it changes the associated missing data self-consistently. If the internal floating point representation of a missing value, e.g., 1.0e36, differs between two machines then netCDF files produced on those machines will have incompatible missing values. This allows <code>ncatted</code> to change the missing values in files from different machines to a single value so that the files may then be concatenated together, e.g., by <code>ncrcat</code>, without losing any information. </p>
<p> The key to mastering <code>ncatted</code> is understanding the meaning of the structure describing the attribute modification, <i>att_dsc</i>. Each <i>att_dsc</i> contains five elements, which makes using <code>ncatted</code> somewhat complicated, but powerful. The <i>att_dsc</i> argument structure contains five arguments in the following order: </p>
<p> <i>att_dsc</i> = <i>att_nm</i>, <i>var_nm</i>, <i>mode</i>, <i>att_type</i>, <i>att_val</i> </p>
<dl>
<dt><code>att_nm</code></p>
<dd> Attribute name. Example: <code>units</code></p>
<dt><code>var_nm</code></p>
<dd> Variable name. Example: <code>pressure</code></p>
<dt><code>mode</code></p>
<dd> Edit mode abbreviation. Example: <code>a</code>. See below for complete listing of valid values of <i>mode</i>.</p>
<dt><code>att_type</code></p>
<dd> Attribute type abbreviation. Example: <code>c</code>. See below for complete listing of valid values of <i>att_type</i>.</p>
<dt><code>att_val</code></p>
<dd> Attribute value. Example: <code>pascal</code>. There should be no empty space between these five consecutive arguments. The description of these arguments follows in their order of appearance.</dl>
<p> The value of <i>att_nm</i> is the name of the attribute you want to edit. This meaning of this should be clear to all users of the <code>ncatted</code> operator. </p>
<p> The value of <i>var_nm</i> is the name of the variable containing the attribute (named <i>att_nm</i>) that you want to edit. There are two very important and useful exceptions to this rule. The value of <i>var_nm</i> can also be used to direct <code>ncatted</code> to edit global attributes, or to repeat the editing operation for every variable in a file. A value of <i>var_nm</i> of global&#8221; indicates that <i>att_nm</i> refers to a global attribute, rather than a particular variable&#8217;s attribute. This is the method <code>ncatted</code> supports for editing global attributes. If <i>var_nm</i> is left blank, on the other hand, then <code>ncatted</code> attempts to perform the editing operation on every variable in the file. This option may be convenient to use if you decide to change the conventions you use for describing the data. </p>
<p> The value of <i>mode</i> is a single character abbreviation ( <code>a</code>, <code>c</code>, <code>d</code>, <code>m</code>, or <code>o</code>) standing for one of five editing modes:</p>
<dl>
<dt><code>a </code></p>
<dd> <i>Append</i>. Append value <i>att_val</i> to current <i>var_nm</i> attribute <i>att_nm</i> value <i>att_val</i>, if any. If <i>var_nm</i> does not have an attribute <i>att_nm</i>, there is no effect.</p>
<dt><code>c</code></p>
<dd> <i>Create</i>. Create variable <i>var_nm</i> attribute <i>att_nm</i> with <i>att_val</i> if <i>att_nm</i> does not yet exist. If <i>var_nm</i> already has an attribute <i>att_nm</i>, there is no effect.</p>
<dt><code>d</code></p>
<dd> <i>Delete</i>. Delete current <i>var_nm</i> attribute <i>att_nm</i>. If <i>var_nm</i> does not have an attribute <i>att_nm</i>, there is no effect. When <i>Delete</i> mode is selected, the <i>att_type</i> and <i>att_val</i> arguments are superfluous and may be left blank.</p>
<dt><code>m</code></p>
<dd> <i>Modify</i>. Change value of current <i>var_nm</i> attribute <i>att_nm</i> to value <i>att_val</i>. If <i>var_nm</i> does not have an attribute <i>att_nm</i>, there is no effect.</p>
<dt><code>o</code></p>
<dd> <i>Overwrite</i>. Write attribute <i>att_nm</i> with value <i>att_val</i> to variable <i>var_nm</i>, overwriting existing attribute <i>att_nm</i>, if any. This is the default mode.</dl>
<p> The value of <i>att_type</i> is a single character abbreviation ( <code>f</code>, <code>d</code>, <code>l</code>, <code>s</code>, <code>c</code>, or <code>b</code>) standing for one of the six primitive netCDF data types:</p>
<dl>
<dt><code>f</code></p>
<dd> <i>Float</i>. Value(s) specified in <i>att_val</i> will be stored as netCDF intrinsic type NC_FLOAT.</p>
<dt><code>d</code></p>
<dd> <i>Double</i>. Value(s) specified in <i>att_val</i> will be stored as netCDF intrinsic type NC_DOUBLE.</p>
<dt><code>l</code></p>
<dd> <i>Long</i>. Value(s) specified in <i>att_val</i> will be stored as netCDF intrinsic type NC_LONG.</p>
<dt><code>s</code></p>
<dd> <i>Short</i>. Value(s) specified in <i>att_val</i> will be stored as netCDF intrinsic type NC_SHORT.</p>
<dt><code>c</code></p>
<dd> <i>Char.</i> Value(s) specified in <i>att_val</i> will be stored as netCDF intrinsic type NC_CHAR.</p>
<dt><code>b</code></p>
<dd> <i>Byte</i>. Value(s) specified in <i>att_val</i> will be stored as netCDF intrinsic type NC_BYTE. The specification of <i>att_type</i> is optional in <i>Delete</i> mode.</dl>
<p> The value of <i>att_val</i> is what you want to change attribute <i>att_nm</i> to contain. The specification of <i>att_val</i> is optional in <i>Delete</i> mode. Attribute values for all types besides NC_CHAR must have an attribute length of at least one. Thus <i>att_val</i> may be a single value or one-dimensional array of elements of type <code>att_type</code>. If the <i>att_val</i> is not set or is set to empty space, and the <i>att_type</i> is NC_CHAR, e.g., <code>-a units,T,o,c,</code> or <code>-a units,T,o,c,</code>, then the corresponding attribute is set to have zero length. When specifying an array of values, it is safest to enclose <i>att_val</i> in double or single quotes, e.g., <code>-a levels,T,o,s,1,2,3,4</code> or <code>-a levels,T,o,s,&#8217;1,2,3,4&#8242;</code>. The quotes are strictly unnecessary around <i>att_val</i> except when <i>att_val</i> contains characters which would confuse the calling shell, such as spaces, commas, and wildcard characters. </p>
<p> NCO processing of NC_CHAR attributes is a bit like Perl in that it attempts to do what you want by default (but this sometimes causes unexpected results if you want unusual data storage). If the <i>att_type</i> is NC_CHAR then the argument is interpreted as a string and it may contain C-language escape sequences, which NCO will interpret before writing anything to disk. NCO translates valid escape sequences and stores the appropriate ASCII code instead. Since two byte escape sequences represent one byte ASCII codes, e.g., ASCII 10 (decimal), the stored string attribute is one byte shorter than the input string length for each embedded escape sequence. These sequences in particular allow convenient editing of formatted text attributes. See ncks netCDF Kitchen Sink, for more examples of string formatting (with the <code>ncks</code> <code>-s</code> option) with special characters. </p>
<p> Analogous to <code>printf</code>, other special characters are also allowed by <code>ncatted</code> if they are &quot;protected&quot; by a backslash. NCO simply strips away the leading backslash from these characters before editing the attribute. No other characters require protection by a backslash. Backslashes which precede any other character will not be filtered and will be included in the attribute. </p>
<p> Note that the NUL character which terminates C language strings is assumed and need not be explicitly specified. If NUL is input, it will not be translated (because it would terminate the string in an additional location). Because of these context-sensitive rules, if wish to use an attribute of type NC_CHAR to store data, rather than text strings, you should use <code>ncatted</code> with care. </p>
<h2>EXAMPLES</h2>
<p> Append the string &quot;Data version 2.0.
&quot; to the global attribute <code>history</code>:</p>
<dl>
<dt>
<dd> ncatted -O -a history,global,a,c,&quot;Data version 2.0
&quot; in.nc</dl>
<p> Note the use of embedded C language <code>printf()</code>-style escape sequences. </p>
<p> Change the value of the <code>long_name</code> attribute for variable <code>T</code> from whatever it currently is to &quot;temperature&quot;:</p>
<dl>
<dt>
<dd> ncatted -O -a long_name,T,o,c,temperature in.nc</dl>
<p> Delete all existing <code>units</code> attributes:</p>
<dl>
<dt>
<dd> ncatted -O -a units,,d,, in.nc</dl>
<p> The value of <i>var_nm</i> was left blank in order to select all variables in the file. The values of <i>att_type</i> and <i>att_val</i> were left blank because they are superfluous in <i>Delete</i> mode. </p>
<p> Modify all existing <code>units</code> attributes to &quot;meter second-1&quot;</p>
<dl>
<dt>
<dd> ncatted -O -a units,,m,c,&quot;meter second-1&quot; in.nc</dl>
<p> Overwrite the <code>quanta</code> attribute of variable <code>energy</code> to an array of four integers.</p>
<dl>
<dt>
<dd> ncatted -O -a quanta,energy,o,s,&quot;010,101,111,121&quot; in.nc</dl>
<p> See the manual for more complex examples, including how to input C-language escape sequences and other special characters like backslashes and question marks. </p>
<h2>AUTHOR</h2>
<p> <code>NCO</code> manual pages written by Charlie Zender and originally formatted by Brian Mays. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://sf.net/bugs/?group_id=3331">http://sf.net/bugs/?group_id=3331</a>&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-2012 Charlie Zender<br />
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
