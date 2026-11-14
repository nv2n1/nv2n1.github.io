---
title: "ncrename(1)"
name: "ncrename"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncrename/"
description: "ncrename – netCDF Renamer"
---

<h2>NAME</h2>
<p> ncrename &#8211; netCDF Renamer</p>
<h2>SYNTAX</h2>
<p> ncrename [-a <i>old_name,new_name</i>] [-a &nbsp;<wbr>&#8230;&nbsp;<wbr>] [-D] [-d <i>old_name,new_name</i>] [-d &nbsp;<wbr>&#8230;&nbsp;<wbr>] [-g <i>old_name,new_name</i>] [-g &nbsp;<wbr>&#8230;&nbsp;<wbr>] [-h] [&#8211;hdr_pad <i>sz</i>] [-l path] [-O] [-p path] [-R] [-r] [&#8211;ram_all] [-v <i>old_name,new_name</i>] [-v &nbsp;<wbr>&#8230;&nbsp;<wbr>] <i>input-file</i> [ <i>output-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ncrename</code> renames dimensions, variables, and attributes in a netCDF file. Each object that has a name in the list of old names is renamed using the corresponding name in the list of new names. All the new names must be unique. Every old name must exist in the input file, unless the name is preceded by the character <code>.</code>. The validity of the old names is not checked prior to the renaming. Thus, if an old name is specified without the the <code>.</code> prefix and is not present in <i>input-file</i>, <code>ncrename</code> will abort. </p>
<p> <code>ncrename</code> is the exception to the normal rules that the user will be interactively prompted before an existing file is changed, and that a temporary copy of an output file is constructed during the operation. If only <i>input-file</i> is specified, then <code>ncrename</code> will change the names of the <i>input-file</i> in place without prompting and without creating a temporary copy of <code>input-file</code>. This is because the renaming operation is considered reversible if the user makes a mistake. The <i>new_name</i> can easily be changed back to <i>old_name</i> by using <code>ncrename</code> one more time. </p>
<p> Note that renaming a dimension to the name of a dependent variable can be used to invert the relationship between an independent coordinate variable and a dependent variable. In this case, the named dependent variable must be one-dimensional and should have no missing values. Such a variable will become a coordinate variable. </p>
<p> According to the netCDF User&#8217;s Guide, renaming properties in netCDF files does not incur the penalty of recopying the entire file when the <i>new_name</i> is shorter than the <i>old_name</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a </code></p>
<dd> <i>old_name</i>, <i>new_name</i> Attribute renaming. The old and new names of the attribute are specified by the associated <i>old_name</i> and <i>new_name</i> values. Global attributes are treated no differently than variable attributes. This option may be specified more than once. You cannot change the attribute name for one particular variable (unless it is uniquely named); all occurrences of the attribute of a given name will be renamed. This is considered an oversight and will be addressed in a future version of NCO.</dl>
<dl>
<dt><code>-d </code></p>
<dd> <i>old_name</i>, <i>new_name</i> Dimension renaming. The old and new names of the dimension are specified by the associated <i>old_name</i> and <i>new_name</i> values. This option may be specified more than once.</p>
<dt><code>-g </code></p>
<dd> <i>old_name</i>, <i>new_name</i> Group renaming. The old and new names of the group are specified by the associated <i>old_name</i> and <i>new_name</i> values. This option may be specified more than once.</p>
<dt><code>-v </code></p>
<dd> <i>old_name</i>, <i>new_name</i> Variable renaming. The old and new names of the variable are specified by the associated <i>old_name</i> and <i>new_name</i> values. This option may be specified more than once.</p>
<dt><code>-i </code></p>
<dd> Interactive. <code>ncrename</code> will prompt for confirmation before overwriting an existing file.</dl>
<h2>EXAMPLES</h2>
<p> Rename the variable <code>p</code> to <code>pressure</code> and <code>t</code> to <code>temperature</code> in netCDF <code>in.nc</code>. In this case <code>p</code> must exist in the input file (or <code>ncrename</code> will abort), but the presence of <code>t</code> is optional:</p>
<dl>
<dt>
<dd> ncrename -v p,pressure -v .t,temperature in.nc</dl>
<p> <code>ncrename</code> does not automatically attach dimensions to variables of the same name. If you want to rename a coordinate variable so that it remains a coordinate variable, you must separately rename both the dimension and the variable:</p>
<dl>
<dt>
<dd> ncrename -d lon,longitude -v lon,longitude in.nc</dl>
<p> Create netCDF <code>out.nc</code> identical to <code>in.nc</code> except the attribute <code>_FillValue</code> is changed to <code>missing_value</code> (in all variables which possess it) and the global attribute <code>Zaire</code> is changed to <code>Congo</code>:</p>
<dl>
<dt>
<dd> ncrename -a _FillValue,missing_value -a Zaire,Congo in.nc out.nc</dl>
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
