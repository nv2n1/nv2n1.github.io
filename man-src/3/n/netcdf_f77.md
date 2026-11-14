---
title: "netcdf_f77(3)"
name: "netcdf_f77"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netcdf_f77/"
description: "netcdf – Unidata’s Network Common Data Form (netCDF) library interface"
---

<p>netcdf &#8211; Unidata&#8217;s Network Common Data Form (netCDF) library interface</p>
<h2>Synopsis</h2>
<p><code> include netcdf.inc </code></p>
<h3>Most Systems:</h3>
<p>f77 &#8230; -lnetcdf</p>
<h3>CRAY PVP Systems:</h3>
<p>f90 -dp -i64 &#8230; -lnetcdf Complete documentation for the netCDF libraries can be found at the netCDF website: <a rel="nofollow" href="http://www.unidata.ucar.edu/software/netcdf/.">http://www.unidata.ucar.edu/software/netcdf/.</a> </p>
<h2>Library Version</h2>
<p>This document describes version 3 </p>
<p> of Unidata netCDF data-access interface for the FORTRAN programming language.</p>
<dl>
<dt> <code>character*80 nf_inq_libvers(void)</code> </p>
<dd>Returns a string identifying the version of the netCDF library, and when it was built, like: &quot;3.1a of Aug 22 1996 12:57:47 $&quot;.</dl>
<p> The RCS <code><a href="/docs/linux/man/1-ident/">ident</a>(1)</code> command will find a string like &quot;$Id: @(#) netcdf library version 3.1a of Sep 6 1996 15:56:26 $&quot; in the library. The SCCS <code><a href="/docs/linux/man/1-what/">what</a>(1)</code> command will find a string like &quot;netcdf library version 3.1a of Aug 23 1996 16:07:40 $&quot;.</p>
<h2>Return Values</h2>
<p>All netCDF functions (except <code>nf_inq_libvers()</code> and <code>nf_strerror()</code>) return an integer status. </p>
<p> If this returned status value is not equal to <code>NF_NOERR</code> (zero), it indicates that an error occurred. The possible status values are defined in netcdf.inc.</p>
<dl>
<dt> <code>character*80 nf_strerror(integer </code><i>status</i>) </p>
<dd>Returns a string textual translation of the <i>status</i> value, like &quot;Attribute or variable name contains illegal characters&quot; or &quot;No such file or directory&quot;. </p>
</dl>
<h2>File Operations</h2>
<dl>
<dt> <code>integer function nf_create(character*(*) </code><i>path</i>, integer <i>cmode</i>, integer <i>ncid</i>) </p>
<dd>Creates a new netCDF dataset at <i>path</i>, returning a netCDF ID in <i>ncid</i>. The argument <i>cmode</i> may include the bitwise-or of the following flags: <code>NF_NOCLOBBER</code> to protect existing datasets (default silently blows them away), <code>NF_SHARE</code> for synchronous dataset updates for classic format files (default is to buffer accesses), </p>
<p> When a netCDF dataset is created, is is opened <code>NF_WRITE</code>. The new netCDF dataset is in define mode. <code>NF_64BIT_OFFSET</code>. to create a file in the 64-bit offset format (as opposed to classic format, the default). </p>
<dt> <code>integer function nf__create(character*(*) </code><i>path</i>, integer <i>cmode</i>, integer <i>initialsize</i>, integer <i>chunksize</i>, integer <i>ncid</i>) </p>
<dd>Like <code>nf_create()</code> but has additional performance tuning parameters. </p>
<p> The argument <i>initialsize</i> sets the initial size of the file at creation time. </p>
<p> See <code>nf__open()</code> below for an explanation of the <i>chunksize</i> parameter.</p>
<dt> <code>integer function nf_open(character*(*) </code><i>path</i>, integer <i>mode</i>, integer <i>ncid</i>) </p>
<p> (Corresponds to <code>ncopn()</code> in version 2) </p>
<dd>Opens a existing netCDF dataset at <i>path</i> returning a netCDF ID in <i>ncid</i>. The type of access is described by the <i>mode</i> parameter, which may include the bitwise-or of the following flags: <code>NF_WRITE</code> for read-write access (default read-only), <code>NF_SHARE</code> for synchronous dataset updates (default is to buffer accesses), and <code>NF_LOCK</code> (not yet implemented). </p>
<dt> <code>integer function nf__open(character*(*) </code><i>path</i>, integer <i>mode</i>, integer <i>chunksize</i>, integer <i>ncid</i>) </p>
<dd>Like <code>nf_open()</code> but has an additional performance tuning parameter. </p>
<p> The argument referenced by <i>chunksize</i> controls a space versus time tradeoff, memory allocated in the netcdf library versus number of system calls. Because of internal requirements, the value may not be set to exactly the value requested. The actual value chosen is returned by reference. Using the value <code>NF_SIZEHINT_DEFAULT</code> causes the library to choose a default. How the system choses the default depends on the system. On many systems, the &quot;preferred I/O block size&quot; is available from the <code>stat()</code> system call, <code>struct stat</code> member <code>st_blksize</code>. If this is available it is used. Lacking that, twice the system pagesize is used. Lacking a call to discover the system pagesize, we just set default chunksize to 8192. </p>
<p> The chunksize is a property of a given open netcdf descriptor <i>ncid</i>, it is not a persistent property of the netcdf dataset. </p>
<dt> <code>integer function nf_redef(integer </code><i>ncid</i>) </p>
<p> (Corresponds to <code>ncredf()</code> in version 2) </p>
<dd>Puts an open netCDF dataset into define mode, so dimensions, variables, and attributes can be added or renamed and attributes can be deleted.</p>
<dt> <code>integer function nf_enddef(integer </code><i>ncid</i>) </p>
<p> (Corresponds to <code>ncendf()</code> in version 2) </p>
<dd>Takes an open netCDF dataset out of define mode. The changes made to the netCDF dataset while it was in define mode are checked and committed to disk if no problems occurred. Some data values may be written as well, see &quot;VARIABLE PREFILLING&quot; below. After a successful call, variable data can be read or written to the dataset.</p>
<dt> <code>integer function nf__enddef(integer </code><i>ncid</i>, integer <i>h_minfree</i>, integer <i>v_align</i>, integer <i>v_minfree</i>, integer <i>r_align</i>) </p>
<dd>Like <code>nf_enddef()</code> but has additional performance tuning parameters. </p>
<p> Caution: this function exposes internals of the netcdf version 1 file format. It may not be available on future netcdf implementations. </p>
<p> The current netcdf file format has three sections, the &quot;header&quot; section, the data section for fixed size variables, and the data section for variables which have an unlimited dimension (record variables). The header begins at the beginning of the file. The index (offset) of the beginning of the other two sections is contained in the header. Typically, there is no space between the sections. This causes copying overhead to accrue if one wishes to change the size of the sections, as may happen when changing names of things, text attribute values, adding attributes or adding variables. Also, for buffered i/o, there may be advantages to aligning sections in certain ways. </p>
<p> The minfree parameters allow one to control costs of future calls to <code>nf_redef()</code>, <code>nf_enddef()</code> by requesting that <i>minfree</i> bytes be available at the end of the section. The <i>h_minfree</i> parameter sets the pad at the end of the &quot;header&quot; section. The <i>v_minfree</i> parameter sets the pad at the end of the data section for fixed size variables. </p>
<p> The align parameters allow one to set the alignment of the beginning of the corresponding sections. The beginning of the section is rounded up to an index which is a multiple of the align parameter. The flag value <code>NF_ALIGN_CHUNK</code> tells the library to use the chunksize (see above) as the align parameter. The <i>v_align</i> parameter controls the alignment of the beginning of the data section for fixed size variables. The <i>r_align</i> parameter controls the alignment of the beginning of the data section for variables which have an unlimited dimension (record variables). </p>
<p> The file format requires mod 4 alignment, so the align parameters are silently rounded up to multiples of 4. The usual call, <code>nf_enddef(</code><i>ncid</i>) is equivalent to <code>nf__enddef(</code><i>ncid</i>, 0, 4, 0, 4). </p>
<p> The file format does not contain a &quot;record size&quot; value, this is calculated from the sizes of the record variables. This unfortunate fact prevents us from providing minfree and alignment control of the &quot;records&quot; in a netcdf file. If you add a variable which has an unlimited dimension, the third section will always be copied with the new variable added.</p>
<dt> <code>integer function nf_sync(integer </code><i>ncid</i>) </p>
<p> (Corresponds to <code>ncsnc()</code> in version 2) </p>
<dd>Unless the <code>NF_SHARE</code> bit is set in <code>nf_open()</code> or <code>nf_create()</code>, accesses to the underlying netCDF dataset are buffered by the library. This function synchronizes the state of the underlying dataset and the library. This is done automatically by <code>nf_close()</code> and <code>nf_enddef()</code>.</p>
<dt> <code>integer function nf_abort(integer </code><i>ncid</i>) </p>
<p> (Corresponds to <code>ncabor()</code> in version 2) </p>
<dd>You don&#8217;t need to call this function. This function is called automatically by <code>nf_close()</code> if the netCDF was in define mode and something goes wrong with the commit. If the netCDF dataset isn&#8217;t in define mode, then this function is equivalent to <code>nf_close()</code>. If it is called after <code>nf_redef()</code>, but before <code>nf_enddef()</code>, the new definitions are not committed and the dataset is closed. If it is called after <code>nf_create()</code> but before <code>nf_enddef()</code>, the dataset disappears.</p>
<dt> <code>integer function nf_close(integer </code><i>ncid</i>) </p>
<p> (Corresponds to <code>ncclos()</code> in version 2) </p>
<dd>Closes an open netCDF dataset. If the dataset is in define mode, <code>nf_enddef()</code> will be called before closing. After a dataset is closed, its ID may be reassigned to another dataset.</p>
<dt> <code>integer function nf_inq(integer </code><i>ncid</i>, integer <i>ndims</i>, integer <i>nvars</i>,</p>
<dd>integer <i>natts</i>, integer <i>unlimdimid</i>)</p>
<dt> <code>integer function nf_inq_ndims(integer </code><i>ncid</i>, integer <i>ndims</i>)</p>
<dt> <code>integer function nf_inq_nvars(integer </code><i>ncid</i>, integer <i>nvars</i>)</p>
<dt> <code>integer function nf_inq_natts(integer </code><i>ncid</i>, integer <i>natts</i>)</p>
<dt> <code>integer function nf_inq_unlimdim(integer </code><i>ncid</i>, integer <i>unlimdimid</i>)</p>
<dt> <code>integer function nf_inq_format(integer </code><i>ncid</i>, integer <i>formatn</i>) </p>
<dd>Use these functions to find out what is in a netCDF dataset. Upon successful return, <i>ndims</i> will contain the number of dimensions defined for this netCDF dataset, <i>nvars</i> will contain the number of variables, <i>natts</i> will contain the number of attributes, and <i>unlimdimid</i> will contain the dimension ID of the unlimited dimension if one exists, or 0 otherwise. <i>formatn</i> will contain the version number of the dataset &lt;format&gt;, one of <code>NF_FORMAT_CLASSIC</code>, <code>NF_FORMAT_64BIT</code>, <code>NF_FORMAT_NETCDF4</code>, or <code>NF_FORMAT_NETCDF4_CLASSIC</code>. </p>
<dt> <code>integer function nf_def_dim(integer </code><i>ncid</i>, character*(*) <i>name</i>, integer <i>len</i>, integer <i>dimid</i>) </p>
<p> (Corresponds to <code>ncddef()</code> in version 2) </p>
<dd>Adds a new dimension to an open netCDF dataset, which must be in define mode. <i>name</i> is the dimension name. <i>dimid</i> will contain the dimension ID of the newly created dimension. </p>
</dl>
<h2>Dimensions</h2>
<dl>
<dt> <code>integer function nf_inq_dimid(integer </code><i>ncid</i>, character*(*) <i>name</i>, integer <i>dimid</i>) </p>
<p> (Corresponds to <code>ncdid()</code> in version 2) </p>
<dd>Given a dimension name, returns the ID of a netCDF dimension in <i>dimid</i>.</p>
<dt> <code>integer function nf_inq_dim(integer </code><i>ncid</i>, integer <i>dimid</i>, character*(*) <i>name</i>, integer <i>len</i>)</p>
<dt> <code>integer function nf_inq_dimname(integer </code><i>ncid</i>, integer <i>dimid</i>, character*(*) <i>name</i>)</p>
<dt> <code>integer function nf_inq_dimlen(integer </code><i>ncid</i>, integer <i>dimid</i>, integer <i>len</i>) </p>
<dd>Use these functions to find out about a dimension. </p>
<p> <i>name</i> should be big enough (<code>NF_MAX_NAME</code>) to hold the dimension name as the name will be copied into your storage. The length return parameter, <i>len</i> will contain the size of the dimension. For the unlimited dimension, the returned length is the current maximum value used for writing into any of the variables which use the dimension.</p>
<dt> <code>integer function nf_rename_dim(integer </code><i>ncid</i>, integer <i>dimid</i>, character*(*) <i>name</i>) </p>
<p> (Corresponds to <code>ncdren()</code> in version 2) </p>
<dd>Renames an existing dimension in an open netCDF dataset. If the new name is longer than the old name, the netCDF dataset must be in define mode. You cannot rename a dimension to have the same name as another dimension.</dl>
<h2>Variables</h2>
<dl>
<dt> <code>integer function nf_def_var(integer </code><i>ncid</i>, character*(*) <i>name</i>, integer <i>xtype</i>, integer <i>ndims</i>, integer <i><a href="/docs/linux/man/1-dimids/">dimids</a></i>(1), integer <i>varid</i>) </p>
<p> (Corresponds to <code>ncvdef()</code> in version 2) </p>
<dd>Adds a new variable to a netCDF dataset. The netCDF must be in define mode. <i>varid</i> will be set to the netCDF variable ID.</p>
<dt> <code>integer function nf_inq_varid(integer </code><i>ncid</i>, character*(*) <i>name</i>, integer <i>varid</i>) </p>
<p> (Corresponds to <code>ncvid()</code> in version 2) </p>
<dd>Returns the ID of a netCDF variable in <i>varid</i> given its name.</p>
<dt> <code>integer function nf_inq_var(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>xtype</i>, integer <i>ndims</i>, integer <i><a href="/docs/linux/man/1-dimids/">dimids</a></i>(1),</p>
<dd>integer <i>natts</i>)</p>
<dt> <code>integer function nf_inq_varname(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>)</p>
<dt> <code>integer function nf_inq_vartype(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i>xtype</i>)</p>
<dt> <code>integer function nf_inq_varndims(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i>ndims</i>)</p>
<dt> <code>integer function nf_inq_vardimid(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-dimids/">dimids</a></i>(1))</p>
<dt> <code>integer function nf_inq_varnatts(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i>natts</i>) </p>
<dd>Returns information about a netCDF variable, given its ID. </p>
<dt> <code>integer function nf_rename_var(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>) </p>
<p> (Corresponds to <code>ncvren()</code> in version 2) </p>
<dd>Changes the name of a netCDF variable. If the new name is longer than the old name, the netCDF must be in define mode. You cannot rename a variable to have the name of any existing variable. </p>
</dl>
<h2>Writing And Reading Whole Variables</h2>
<dl>
<dt> <code>integer function nf_put_var_text(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>out</i>) </p>
<dt> <code>integer function nf_put_var_int1(integer </code><i>ncid</i>, integer <i>varid</i>, integer*1 <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_var_int2(integer </code><i>ncid</i>, integer <i>varid</i>, integer*2 <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_var_int(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-out/">out</a></i>(1)) </p>
<dt> <code>integer function nf_put_var_real(integer </code><i>ncid</i>, integer <i>varid</i>, real <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_var_double(integer </code><i>ncid</i>, integer <i>varid</i>, doubleprecision <i><a href="/docs/linux/man/1-out/">out</a></i>(1)) </p>
<dd>Writes an entire netCDF variable (i.e. all the values). The netCDF dataset must be open and in data mode. The type of the data is specified in the function name, and it is converted to the external type of the specified variable, if possible, otherwise an <code>NF_ERANGE</code> error is returned. Note that rounding is not performed during the conversion. Floating point numbers are truncated when converted to integers.</p>
<dt> <code>integer function nf_get_var_text(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>in</i>) </p>
<dt> <code>integer function nf_get_var_int1(integer </code><i>ncid</i>, integer <i>varid</i>, integer*1 <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_var_int2(integer </code><i>ncid</i>, integer <i>varid</i>, integer*2 <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_var_int(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-in/">in</a></i>(1)) </p>
<dt> <code>integer function nf_get_var_real(integer </code><i>ncid</i>, integer <i>varid</i>, real <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_var_double(integer </code><i>ncid</i>, integer <i>varid</i>, doubleprecision <i><a href="/docs/linux/man/1-in/">in</a></i>(1)) </p>
<dd>Reads an entire netCDF variable (i.e. all the values). The netCDF dataset must be open and in data mode. The data is converted from the external type of the specified variable, if necessary, to the type specified in the function name. If conversion is not possible, an <code>NF_ERANGE</code> error is returned.</dl>
<h2>Writing And Reading One Datum</h2>
<dl>
<dt> <code>integer function nf_put_var1_text(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), character*1 <i>*out</i>) </p>
<dt> <code>integer function nf_put_var1_int1(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), integer*1 <i>*out</i>)</p>
<dt> <code>integer function nf_put_var1_int2(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), integer*2 <i>*out</i>)</p>
<dt> <code>integer function nf_put_var1_int(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), integer <i>*out</i>) </p>
<dt> <code>integer function nf_put_var1_real(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), real <i>*out</i>)</p>
<dt> <code>integer function nf_put_var1_double(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), doubleprecision <i>*out</i>) </p>
<dd>Puts a single data value into a variable at the position <i>index</i> of an open netCDF dataset that is in data mode. The type of the data is specified in the function name, and it is converted to the external type of the specified variable, if possible, otherwise an <code>NF_ERANGE</code> error is returned.</p>
<dt> <code>integer function nf_get_var1_text(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), character*1 <i>in</i>) </p>
<dt> <code>integer function nf_get_var1_int1(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), integer*1 <i>in</i>)</p>
<dt> <code>integer function nf_get_var1_int2(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), integer*2 <i>in</i>)</p>
<dt> <code>integer function nf_get_var1_int(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), integer <i>in</i>) </p>
<dt> <code>integer function nf_get_var1_real(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), real <i>in</i>)</p>
<dt> <code>integer function nf_get_var1_double(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1), doubleprecision <i>in</i>) </p>
<dd>Gets a single data value from a variable at the position <i>index</i> of an open netCDF dataset that is in data mode. The data is converted from the external type of the specified variable, if necessary, to the type specified in the function name. If conversion is not possible, an <code>NF_ERANGE</code> error is returned.</dl>
<h2>Writing And Reading An Array</h2>
<dl>
<dt> <code>integer function nf_put_vara_text(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), character*(*) <i>out</i>) </p>
<dt> <code>integer function nf_put_vara_int1(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer*1 <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_vara_int2(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer*2 <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_vara_int(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-out/">out</a></i>(1)) </p>
<dt> <code>integer function nf_put_vara_real(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), real <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_vara_double(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), doubleprecision <i><a href="/docs/linux/man/1-out/">out</a></i>(1)) </p>
<dd>Writes an array section of values into a netCDF variable of an open netCDF dataset, which must be in data mode. The array section is specified by the <i>start</i> and <i>count</i> vectors, which give the starting index and count of values along each dimension of the specified variable. The type of the data is specified in the function name and is converted to the external type of the specified variable, if possible, otherwise an <code>NF_ERANGE</code> error is returned.</p>
<dt> <code>integer function nf_get_vara_text(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), character*(*) <i>in</i>) </p>
<dt> <code>integer function nf_get_vara_int1(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer*1 <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_vara_int2(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer*2 <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_vara_int(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-in/">in</a></i>(1)) </p>
<dt> <code>integer function nf_get_vara_real(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), real <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_vara_double(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), doubleprecision <i><a href="/docs/linux/man/1-in/">in</a></i>(1)) </p>
<dd>Reads an array section of values from a netCDF variable of an open netCDF dataset, which must be in data mode. The array section is specified by the <i>start</i> and <i>count</i> vectors, which give the starting index and count of values along each dimension of the specified variable. The data is converted from the external type of the specified variable, if necessary, to the type specified in the function name. If conversion is not possible, an <code>NF_ERANGE</code> error is returned.</dl>
<h2>Writing And Reading A Sliced Array</h2>
<dl>
<dt> <code>integer function nf_put_vars_text(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), character*(*) <i>out</i>) </p>
<dt> <code>integer function nf_put_vars_int1(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), integer*1 <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_vars_int2(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), integer*2 <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_vars_int(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), integer <i><a href="/docs/linux/man/1-out/">out</a></i>(1)) </p>
<dt> <code>integer function nf_put_vars_real(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), real <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_vars_double(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), doubleprecision <i><a href="/docs/linux/man/1-out/">out</a></i>(1)) </p>
<dd>These functions are used for <i>strided output</i>, which is like the array section output described above, except that the sampling stride (the interval between accessed values) is specified for each dimension. For an explanation of the sampling stride vector, see COMMON ARGUMENTS DESCRIPTIONS below.</p>
<dt> <code>integer function nf_get_vars_text(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), character*(*) <i>in</i>) </p>
<dt> <code>integer function nf_get_vars_int1(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), integer*1 <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_vars_int2(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), integer*2 <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_vars_int(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), integer <i><a href="/docs/linux/man/1-in/">in</a></i>(1)) </p>
<dt> <code>integer function nf_get_vars_real(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), real <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_vars_double(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), doubleprecision <i><a href="/docs/linux/man/1-in/">in</a></i>(1)) </p>
<dd>These functions are used for <i>strided input</i>, which is like the array section input described above, except that the sampling stride (the interval between accessed values) is specified for each dimension. For an explanation of the sampling stride vector, see COMMON ARGUMENTS DESCRIPTIONS below.</dl>
<h2>Writing And Reading A Mapped Array</h2>
<dl>
<dt> <code>integer function nf_put_varm_text(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, character*(*) <i>out</i>) </p>
<dt> <code>integer function nf_put_varm_int1(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, integer*1 <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_varm_int2(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, integer*2 <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_varm_int(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, integer <i><a href="/docs/linux/man/1-out/">out</a></i>(1)) </p>
<dt> <code>integer function nf_put_varm_real(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, real <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_varm_double(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, doubleprecision <i><a href="/docs/linux/man/1-out/">out</a></i>(1)) </p>
<dd>These functions are used for <i>mapped output</i>, which is like strided output described above, except that an additional index mapping vector is provided to specify the in-memory arrangement of the data values. For an explanation of the index mapping vector, see COMMON ARGUMENTS DESCRIPTIONS below.</p>
<dt> <code>integer function nf_get_varm_text(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, character*(*) <i>in</i>) </p>
<dt> <code>integer function nf_get_varm_int1(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, integer*1 <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_varm_int2(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, integer*2 <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_varm_int(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, integer <i><a href="/docs/linux/man/1-in/">in</a></i>(1)) </p>
<dt> <code>integer function nf_get_varm_real(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, real <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_varm_double(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1), integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1), integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1), <i>imap</i>, doubleprecision <i><a href="/docs/linux/man/1-in/">in</a></i>(1)) </p>
<dd>These functions are used for <i>mapped input</i>, which is like strided input described above, except that an additional index mapping vector is provided to specify the in-memory arrangement of the data values. For an explanation of the index mapping vector, see COMMON ARGUMENTS DESCRIPTIONS below.</dl>
<h2>Attributes</h2>
<dl>
<dt> <code>integer function nf_put_att_text(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>xtype</i>, integer <i>len</i>, character*(*) <i>out</i>) </p>
<dt> <code>integer function nf_put_att_int1(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>xtype</i>, integer <i>len</i>, integer*1 <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_att_int2(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>xtype</i>, integer <i>len</i>, integer*2 <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_att_int(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>xtype</i>, integer <i>len</i>, integer <i><a href="/docs/linux/man/1-out/">out</a></i>(1)) </p>
<dt> <code>integer function nf_put_att_real(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>xtype</i>, integer <i>len</i>, real <i><a href="/docs/linux/man/1-out/">out</a></i>(1))</p>
<dt> <code>integer function nf_put_att_double(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>xtype</i>, integer <i>len</i>, doubleprecision <i><a href="/docs/linux/man/1-out/">out</a></i>(1)) </p>
<dt> <code>integer function nf_put_att(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>xtype</i>, integer <i>len</i>, void * <i>ip</i>)</p>
<dt> <code>integer function nf_get_att(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, void * <i>ip</i>) </p>
<dd>Unlike variables, attributes do not have separate functions for defining and writing values. This family of functions defines a new attribute with a value or changes the value of an existing attribute. If the attribute is new, or if the space required to store the attribute value is greater than before, the netCDF dataset must be in define mode. The parameter <i>len</i> is the number of values from <i>out</i> to transfer. It is often one, except that for <code>nf_put_att_text()</code> it will usually be <code>len_trim(</code><i>out</i>). </p>
<p> For these functions, the type component of the function name refers to the in-memory type of the value, whereas the <i>xtype</i> argument refers to the external type for storing the value. An <code>NF_ERANGE</code> error results if a conversion between these types is not possible. In this case the value is represented with the appropriate fill-value for the associated external type.</p>
<dt> <code>integer function nf_inq_attname(integer </code><i>ncid</i>, integer <i>varid</i>, integer <i>attnum</i>, character*(*) <i>name</i>) </p>
<dd>Gets the name of an attribute, given its variable ID and attribute number. This function is useful in generic applications that need to get the names of all the attributes associated with a variable, since attributes are accessed by name rather than number in all other attribute functions. The number of an attribute is more volatile than the name, since it can change when other attributes of the same variable are deleted. The attributes for each variable are numbered from 1 (the first attribute) to <i>nvatts</i>, where <i>nvatts</i> is the number of attributes for the variable, as returned from a call to <code>nf_inq_varnatts()</code>. </p>
<dt> <code>integer function nf_inq_att(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>xtype</i>, integer <i>len</i>)</p>
<dt> <code>integer function nf_inq_attid(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>attnum</i>)</p>
<dt> <code>integer function nf_inq_atttype(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>xtype</i>)</p>
<dt> <code>integer function nf_inq_attlen(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i>len</i>) </p>
<dd>These functions return information about a netCDF attribute, given its variable ID and name. The information returned is the external type in <i>xtype</i> and the number of elements in the attribute as <i>len</i>. </p>
<dt> <code>integer function nf_copy_att(integer </code><i>ncid</i>, integer <i>varid_in</i>, character*(*) <i>name</i>, integer <i>ncid_out</i>, integer <i>varid_out</i>) </p>
<dd>Copies an attribute from one netCDF dataset to another. It can also be used to copy an attribute from one variable to another within the same netCDF. <i>ncid_in</i> is the netCDF ID of an input netCDF dataset from which the attribute will be copied. <i>varid_in</i> is the ID of the variable in the input netCDF dataset from which the attribute will be copied, or <code>NF_GLOBAL</code> for a global attribute. <i>name</i> is the name of the attribute in the input netCDF dataset to be copied. <i>ncid_out</i> is the netCDF ID of the output netCDF dataset to which the attribute will be copied. It is permissible for the input and output netCDF ID&#8217;s to be the same. The output netCDF dataset should be in define mode if the attribute to be copied does not already exist for the target variable, or if it would cause an existing target attribute to grow. <i>varid_out</i> is the ID of the variable in the output netCDF dataset to which the attribute will be copied, or <code>NF_GLOBAL</code> to copy to a global attribute.</p>
<dt> <code>integer function nf_rename_att(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, character*(*) <i>newname</i>) </p>
<dd>Changes the name of an attribute. If the new name is longer than the original name, the netCDF must be in define mode. You cannot rename an attribute to have the same name as another attribute of the same variable. <i>name</i> is the original attribute name. <i>newname</i> is the new name to be assigned to the specified attribute. If the new name is longer than the old name, the netCDF dataset must be in define mode.</p>
<dt> <code>integer function nf_del_att(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>) </p>
<dd>Deletes an attribute from a netCDF dataset. The dataset must be in define mode.</p>
<dt> <code>integer function nf_get_att_text(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, character*(*) <i>in</i>) </p>
<dt> <code>integer function nf_get_att_int1(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer*1 <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_att_int2(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer*2 <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_att_int(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, integer <i><a href="/docs/linux/man/1-in/">in</a></i>(1)) </p>
<dt> <code>integer function nf_get_att_real(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, real <i><a href="/docs/linux/man/1-in/">in</a></i>(1))</p>
<dt> <code>integer function nf_get_att_double(integer </code><i>ncid</i>, integer <i>varid</i>, character*(*) <i>name</i>, doubleprecision <i><a href="/docs/linux/man/1-in/">in</a></i>(1)) </p>
<dd>Gets the value(s) of a netCDF attribute, given its variable ID and name. Converts from the external type to the type specified in the function name, if possible, otherwise returns an <code>NF_ERANGE</code> error. All elements of the vector of attribute values are returned, so you must allocate enough space to hold them. If you don&#8217;t know how much space to reserve, call <code>nf_inq_attlen()</code> first to find out the length of the attribute.</dl>
<h2>Common Argument Descriptions</h2>
<p>In this section we define some common arguments which are used in the &quot;FUNCTION DESCRIPTIONS&quot; section.</p>
<dl>
<dt>integer <i>ncid</i></p>
<dd>is the netCDF ID returned from a previous, successful call to <code>nf_open()</code> or <code>nf_create()</code></p>
<dt>character*(*) <i>name</i></p>
<dd>is the name of a dimension, variable, or attribute. The names of dimensions, variables and attributes consist of arbitrary sequences of alphanumeric characters (as well as underscore &#8216;_&#8217;, period &#8216;.&#8217; and hyphen &#8216;-&#8216;), beginning with a letter or underscore. (However names commencing with underscore are reserved for system use.) Case is significant in netCDF names. A zero-length name is not allowed. </p>
<p> The maximum allowable number of characters<br />
&nbsp;<wbr>is&nbsp;<wbr><code>NF_MAX_NAME</code>.</p>
<dt>integer <i>xtype</i></p>
<dd>specifies the external data type of a netCDF variable or attribute and is one of the following: <code>NF_BYTE</code>, <code>NF_CHAR</code>, <code>NF_SHORT</code>, <code>NF_INT</code>, <code>NF_FLOAT</code>, or <code>NF_DOUBLE</code>. These are used to specify 8-bit integers, characters, 16-bit integers, 32-bit integers, 32-bit IEEE floating point numbers, and 64-bit IEEE floating-point numbers, respectively. </p>
<dt>integer <i><a href="/docs/linux/man/1-dimids/">dimids</a></i>(1)</p>
<dd>is a vector of dimension ID&#8217;s and defines the shape of a netCDF variable. The size of the vector shall be greater than or equal to the rank (i.e. the number of dimensions) of the variable (<i>ndims</i>). The vector shall be ordered by the speed with which a dimension varies: <i><a href="/docs/linux/man/1-dimids/">dimids</a></i>(1) shall be the dimension ID of the most rapidly varying dimension and <i>dimids</i>(<i>ndims</i>) shall be the dimension ID of the most slowly varying dimension. The maximum possible number of dimensions for a variable is given by the symbolic constant <code>NF_MAX_VAR_DIMS</code>.</p>
<dt>integer <i>dimid</i></p>
<dd>is the ID of a netCDF dimension. netCDF dimension ID&#8217;s are allocated sequentially from the positive integers beginning with 1.</p>
<dt>integer <i>ndims</i></p>
<dd>is either the total number of dimensions in a netCDF dataset or the rank (i.e. the number of dimensions) of a netCDF variable. The value shall not be negative or greater than the symbolic constant <code>NF_MAX_VAR_DIMS</code>.</p>
<dt>integer <i>varid</i></p>
<dd>is the ID of a netCDF variable or (for the attribute-access functions) the symbolic constant <code>NF_GLOBAL</code>, which is used to reference global attributes. netCDF variable ID&#8217;s are allocated sequentially from the positive integers beginning with 1.</p>
<dt>integer <i>natts</i></p>
<dd>is the number of global attributes in a netCDF dataset for the <code>nf_inquire()</code> function or the number of attributes associated with a netCDF variable for the <code>nf_varinq()</code> function.</p>
<dt>integer <i><a href="/docs/linux/man/1-index/">index</a></i>(1)</p>
<dd>specifies the indicial coordinates of the netCDF data value to be accessed. The indices start at 1; thus, for example, the first data value of a two-dimensional variable is (1,1). The size of the vector shall be at least the rank of the associated netCDF variable and its elements shall correspond, in order, to the variable&#8217;s dimensions.</p>
<dt>integer <i><a href="/docs/linux/man/1-start/">start</a></i>(1)</p>
<dd>specifies the starting point for accessing a netCDF variable&#8217;s data values in terms of the indicial coordinates of the corner of the array section. The indices start at 1; thus, the first data value of a variable is (1, 1, &#8230;, 1). The size of the vector shall be at least the rank of the associated netCDF variable and its elements shall correspond, in order, to the variable&#8217;s dimensions.</p>
<dt>integer <i><a href="/docs/linux/man/1-count/">count</a></i>(1)</p>
<dd>specifies the number of indices selected along each dimension of the array section. Thus, to access a single value, for example, specify <i>count</i> as (1, 1, &#8230;, 1). Note that, for strided I/O, this argument must be adjusted to be compatible with the <i>stride</i> and <i>start</i> arguments so that the interaction of the three does not attempt to access an invalid data co-ordinate. The elements of the <i>count</i> vector correspond, in order, to the variable&#8217;s dimensions.</p>
<dt>integer <i><a href="/docs/linux/man/1-stride/">stride</a></i>(1)</p>
<dd>specifies the sampling interval along each dimension of the netCDF variable. The elements of the stride vector correspond, in order, to the netCDF variable&#8217;s dimensions (<i><a href="/docs/linux/man/1-stride/">stride</a></i>(1)) gives the sampling interval along the most rapidly varying dimension of the netCDF variable). Sampling intervals are specified in type-independent units of elements (a value of 1 selects consecutive elements of the netCDF variable along the corresponding dimension, a value of 2 selects every other element, etc.). </p>
<dt><i>imap</i></p>
<dd>specifies the mapping between the dimensions of a netCDF variable and the in-memory structure of the internal data array. The elements of the index mapping vector correspond, in order, to the netCDF variable&#8217;s dimensions (<i><a href="/docs/linux/man/1-imap/">imap</a></i>(1) gives the distance between elements of the internal array corresponding to the most rapidly varying dimension of the netCDF variable). Distances between elements are specified in type-independent units of elements (the distance between internal elements that occupy adjacent memory locations is 1 and not the element&#8217;s byte-length as in netCDF 2). </p>
</dl>
<h2>Variable Prefilling</h2>
<p>By default, the netCDF interface sets the values of all newly-defined variables of finite length (i.e. those that do not have an unlimited, dimension) to the type-dependent fill-value associated with each variable. This is done when <code>nf_enddef()</code> is called. The fill-value for a variable may be changed from the default value by defining the attribute `<code>_FillValue</code>&#8216; for the variable. This attribute must have the same type as the variable and be of length one. </p>
<p> Variables with an unlimited dimension are also prefilled, but on an `as needed&#8217; basis. For example, if the first write of such a variable is to position 5, then positions 1 through 4 (and no others) would be set to the fill-value at the same time. </p>
<p> This default prefilling of data values may be disabled by or&#8217;ing the <code>NF_NOFILL</code> flag into the mode parameter of <code>nf_open()</code> or <code>nf_create()</code>, or, by calling the function <code>nf_set_fill()</code> with the argument <code>NF_NOFILL</code>. For variables that do not use the unlimited dimension, this call must be made before <code>nf_enddef()</code>. For variables that use the unlimited dimension, this call may be made at any time. </p>
<p> One can obtain increased performance of the netCDF interface by using this feature, but only at the expense of requiring the application to set every single data value. The performance enhancing behavior of this function is dependent on the particulars of the implementation and dataset format. The flag value controlled by <code>nf_set_fill()</code> is per netCDF ID, not per variable or per write. Allowing this to change affects the degree to which a program can be effectively parallelized. Given all of this, we state that the use of this feature may not be available (or even needed) in future releases. Programmers are cautioned against heavy reliance upon this feature.</p>
<dl>
<dt> <code>integer function nf_setfill(integer </code><i>ncid</i>, integer <i>fillmode</i>, integer <i>old_fillemode</i>) </p>
<dd>Determines whether or not variable prefilling will be done (see above). The netCDF dataset shall be writable. <i>fillmode</i> is either <code>NF_FILL</code> to enable prefilling (the default) or <code>NF_NOFILL</code> to disable prefilling. This function returns the previous setting in <i>old_fillmode</i>. </p>
<dt></dl>
<h2>Mpp Function Descriptions</h2>
<dd>Additional functions for use on SGI/Cray MPP machines (_CRAYMPP). These are used to set and inquire which PE is the base for MPP for a particular netCDF. These are only relevant when using the SGI/Cray &#8220;global&#8221; Flexible File I/O layer and desire to have only a subset of PEs to open the specific netCDF file. For technical reasons, these functions are available on all platforms. On a platform other than SGI/Cray MPP, it is as if only processor available were processor 0. </p>
<p> To use this feature, you need to specify a communicator group and call <code>glio_group_mpi()</code> or <code>glio_group_shmem()</code> prior to the netCDF <code>nf_open()</code> and <code>nf_create()</code> calls.</p>
<dl>
<dt> <code>integer function nf__create_mp(character*(*) </code><i>path</i>, integer <i>cmode</i>, integer <i>initialsize</i>, integer <i>pe</i>, integer <i>chunksize</i>, integer <i>ncid</i>) </p>
<dd>Like <code>nf__create()</code> but allows the base PE to be set. </p>
<p> The argument <i>pe</i> sets the base PE at creation time. In the MPP environment, <code>nf__create()</code> and <code>nf_create()</code> set the base PE to processor zero by default.</p>
<dt> <code>integer function nf__open_mp(character*(*) </code><i>path</i>, integer <i>mode</i>, integer <i>pe</i>, integer <i>chunksize</i>, integer <i>ncid</i>) </p>
<dd>Like <code>nf__open()</code> but allows the base PE to be set. The argument <i>pe</i> sets the base PE at creation time. In the MPP environment, <code>nf__open()</code> and <code>nf_open()</code> set the base PE to processor zero by default.</p>
<dt> <code>integer function nf_inq_base_pe(integer </code><i>ncid</i>, integer <i>pe</i>) </p>
<dd>Inquires of the netCDF dataset which PE is being used as the base for MPP use. This is safe to use at any time.</p>
<dt> <code>integer function nf_set_base_pe(integer </code><i>ncid</i>, integer <i>pe</i>) </p>
<dd>Resets the base PE for the netCDF dataset. Only perform this operation when the affected communicator group synchronizes before and after the call. This operation is very risky and should only be contemplated under only the most extreme cases.</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>NETCDF_FFIOSPEC</code></p>
<dd>Specifies the Flexible File I/O buffers for netCDF I/O when executing under the UNICOS operating system (the variable is ignored on other operating systems). An appropriate specification can greatly increase the efficiency of netCDF I/O &#8212; to the extent that it can actually surpass FORTRAN binary I/O. This environment variable has been made a little more generalized, such that other FFIO option specifications can now be added. The default specification is <code>bufa:336:2</code>, unless a current FFIO specification is in operation, which will be honored. See UNICOS Flexible File I/O for more information.</dl>
<h2>Mailing-Lists</h2>
<p>Both a mailing list and a digest are available for discussion of the netCDF interface and announcements about netCDF bugs, fixes, and enhancements. To begin or change your subscription to either the mailing-list or the digest, send one of the following in the body (not the subject line) of an email message to &quot;majordomo [at] unidata.ucar.edu&quot;. Use your email address in place of <i>jdoe [at] host.inst.domain</i>. </p>
<p> To subscribe to the netCDF mailing list:</p>
<dl>
<dd><code>subscribe netcdfgroup </code><i>jdoe [at] host.inst.domain</i></dl>
<p> To unsubscribe from the netCDF mailing list:</p>
<dl>
<dd><code>unsubscribe netcdfgroup </code><i>jdoe [at] host.inst.domain</i></dl>
<p> To subscribe to the netCDF digest:</p>
<dl>
<dd><code>subscribe netcdfdigest </code><i>jdoe [at] host.inst.domain</i></dl>
<p> To unsubscribe from the netCDF digest:</p>
<dl>
<dd><code>unsubscribe netcdfdigest </code><i>jdoe [at] host.inst.domain</i></dl>
<p> To retrieve the general introductory information for the mailing list:</p>
<dl>
<dd><code>info netcdfgroup</code></dl>
<p> To get a synopsis of other majordomo commands:</p>
<dl>
<dd><code>help</code></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ncdump/">ncdump</a></code>(1), <code><a href="/docs/linux/man/1-ncgen/">ncgen</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3f-netcdf/">netcdf</a></code>(3f). <i>netCDF User&#8217;s Guide</i>, published by the Unidata Program Center, University Corporation for Atmospheric Research, located in Boulder, Colorado. NetCDF home page at http:/<a rel="nofollow" href="http://www.unidata.ucar.edu">www.unidata.ucar.edu</a>/netcdf. </p>
