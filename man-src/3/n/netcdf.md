---
title: "netcdf(3)"
name: "netcdf"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netcdf/"
description: "netcdf – Unidata’s Network Common Data Form (netCDF) library interface"
---

<p>netcdf &#8211; Unidata&#8217;s Network Common Data Form (netCDF) library interface</p>
<h2>Synopsis</h2>
<pre><code>#include &quot;netcdf.h&quot;
</code></pre>
<p> cc &#8230; -lnetcdf -lhdf5_hl -lhdf5 -lz -lm Complete documentation for the netCDF libraries can be found at the netCDF website: <a rel="nofollow" href="http://www.unidata.ucar.edu/software/netcdf/.">http://www.unidata.ucar.edu/software/netcdf/.</a> </p>
<h2>Library Version</h2>
<p>This document describes versions 3 and 4 of Unidata netCDF data-access interface for the C programming language.</p>
<dl>
<dt> <code>const char* nc_inq_libvers()</code> </p>
<dd>Returns a string identifying the version of the netCDF library, and when it was built, like: &quot;3.1a of Aug 22 1996 12:57:47 $&quot;.</dl>
<p> The RCS <code><a href="/docs/linux/man/1-ident/">ident</a>(1)</code> command will find a string like &quot;$Id: @(#) netcdf library version 3.1a of Sep 6 1996 15:56:26 $&quot; in the library. The SCCS <code><a href="/docs/linux/man/1-what/">what</a>(1)</code> command will find a string like &quot;netcdf library version 3.1a of Aug 23 1996 16:07:40 $&quot;.</p>
<h2>Return Values</h2>
<p>All netCDF functions (except <code>nc_inq_libvers()</code> and <code>nc_strerror()</code>) return an integer status. </p>
<p> If this returned status value is not equal to <code>NC_NOERR</code> (zero), it indicates that an error occurred. The possible status values are defined in system include file &lt;errno.h&gt; and in &quot;netcdf.h&quot;.</p>
<dl>
<dt> <code>const char* nc_strerror(int </code><i>status</i>) </p>
<dd>Returns a string textual translation of the <i>status</i> value, like &quot;Attribute or variable name contains illegal characters&quot; or &quot;No such file or directory&quot;. </p>
</dl>
<h2>File Operations</h2>
<dl>
<dt> <code>int nc_create(const char </code><i>path</i>[], int <i>cmode</i>, int* <i>ncid</i>) </p>
<dd>Creates a new netCDF dataset at <i>path</i>, returning a netCDF ID in <i>ncid</i>. The argument <i>cmode</i> may include the bitwise-or of the following flags: <code>NC_NOCLOBBER</code> to protect existing datasets (default silently blows them away), <code>NC_SHARE</code> for synchronous dataset updates for classic format files (default is to buffer accesses), </p>
<p> When a netCDF dataset is created, is is opened <code>NC_WRITE</code>. The new netCDF dataset is in define mode. <code>NC_64BIT_OFFSET</code>. to create a file in the 64-bit offset format (as opposed to classic format, the default). <code>NC_TRUE</code> to create a netCDF-4/HDF5 file, and <code>NC_CLASSIC_MODEL</code> to guarantee that netCDF-4/HDF5 files maintain compatibility with the netCDF classic data model.</p>
<dt> <code>int nc__create(const char </code><i>path</i>[], int <i>cmode</i>, size_t <i>initialsize</i>, size_t* <i>chunksize</i>, int* <i>ncid</i>) </p>
<dd>Like <code>nc_create()</code> but has additional performance tuning parameters. </p>
<p> The argument <i>initialsize</i> sets the initial size of the file at creation time. </p>
<p> See <code>nc__open()</code> below for an explanation of the <i>chunksize</i> parameter.</p>
<dt> <code>int nc_open(const char </code><i>path</i>[], int <i>mode</i>, int* <i>ncid</i>) </p>
<p> (Corresponds to <code>ncopen()</code> in version 2) </p>
<dd>Opens a existing netCDF dataset at <i>path</i> returning a netCDF ID in <i>ncid</i>. The type of access is described by the <i>mode</i> parameter, which may include the bitwise-or of the following flags: <code>NC_WRITE</code> for read-write access (default read-only), <code>NC_SHARE</code> for synchronous dataset updates (default is to buffer accesses), and <code>NC_LOCK</code> (not yet implemented). </p>
<p> As of NetCDF version 4.1, and if TRUE support was enabled when the NetCDF library was built, the path parameter may specify a TRUE URL. In this case, the access mode is forced to be read-only.</p>
<dt> <code>int nc__open(const char </code><i>path</i>[], int <i>mode</i>, size_t* <i>chunksize</i>, int* <i>ncid</i>) </p>
<dd>Like <code>nc_open()</code> but has an additional performance tuning parameter. </p>
<p> The argument referenced by <i>chunksize</i> controls a space versus time tradeoff, memory allocated in the netcdf library versus number of system calls. Because of internal requirements, the value may not be set to exactly the value requested. The actual value chosen is returned by reference. Using the value <code>NC_SIZEHINT_DEFAULT</code> causes the library to choose a default. How the system choses the default depends on the system. On many systems, the &quot;preferred I/O block size&quot; is available from the <code>stat()</code> system call, <code>struct stat</code> member <code>st_blksize</code>. If this is available it is used. Lacking that, twice the system pagesize is used. Lacking a call to discover the system pagesize, we just set default chunksize to 8192. </p>
<p> The chunksize is a property of a given open netcdf descriptor <i>ncid</i>, it is not a persistent property of the netcdf dataset. </p>
<p> As with <code>nc__open()</code>, the path parameter may specify a TRUE URL, but the tuning parameters are ignored.</p>
<dt> <code>int nc_redef(int </code><i>ncid</i>) </p>
<p> (Corresponds to <code>ncredef()</code> in version 2) </p>
<dd>Puts an open netCDF dataset into define mode, so dimensions, variables, and attributes can be added or renamed and attributes can be deleted.</p>
<dt> <code>int nc_enddef(int </code><i>ncid</i>) </p>
<p> (Corresponds to <code>ncendef()</code> in version 2) </p>
<dd>Takes an open netCDF dataset out of define mode. The changes made to the netCDF dataset while it was in define mode are checked and committed to disk if no problems occurred. Some data values may be written as well, see &quot;VARIABLE PREFILLING&quot; below. After a successful call, variable data can be read or written to the dataset.</p>
<dt> <code>int nc__enddef(int </code><i>ncid</i>, size_t <i>h_minfree</i>, size_t <i>v_align</i>, size_t <i>v_minfree</i>, size_t <i>r_align</i>) </p>
<dd>Like <code>nc_enddef()</code> but has additional performance tuning parameters. </p>
<p> Caution: this function exposes internals of the netcdf version 1 file format. It may not be available on future netcdf implementations. </p>
<p> The current netcdf file format has three sections, the &quot;header&quot; section, the data section for fixed size variables, and the data section for variables which have an unlimited dimension (record variables). The header begins at the beginning of the file. The index (offset) of the beginning of the other two sections is contained in the header. Typically, there is no space between the sections. This causes copying overhead to accrue if one wishes to change the size of the sections, as may happen when changing names of things, text attribute values, adding attributes or adding variables. Also, for buffered i/o, there may be advantages to aligning sections in certain ways. </p>
<p> The minfree parameters allow one to control costs of future calls to <code>nc_redef()</code>, <code>nc_enddef()</code> by requesting that <i>minfree</i> bytes be available at the end of the section. The <i>h_minfree</i> parameter sets the pad at the end of the &quot;header&quot; section. The <i>v_minfree</i> parameter sets the pad at the end of the data section for fixed size variables. </p>
<p> The align parameters allow one to set the alignment of the beginning of the corresponding sections. The beginning of the section is rounded up to an index which is a multiple of the align parameter. The flag value <code>NC_ALIGN_CHUNK</code> tells the library to use the chunksize (see above) as the align parameter. The <i>v_align</i> parameter controls the alignment of the beginning of the data section for fixed size variables. The <i>r_align</i> parameter controls the alignment of the beginning of the data section for variables which have an unlimited dimension (record variables). </p>
<p> The file format requires mod 4 alignment, so the align parameters are silently rounded up to multiples of 4. The usual call, <code>nc_enddef(</code><i>ncid</i>) is equivalent to <code>nc__enddef(</code><i>ncid</i>, 0, 4, 0, 4). </p>
<p> The file format does not contain a &quot;record size&quot; value, this is calculated from the sizes of the record variables. This unfortunate fact prevents us from providing minfree and alignment control of the &quot;records&quot; in a netcdf file. If you add a variable which has an unlimited dimension, the third section will always be copied with the new variable added.</p>
<dt> <code>int nc_sync(int </code><i>ncid</i>) </p>
<p> (Corresponds to <code>ncsync()</code> in version 2) </p>
<dd>Unless the <code>NC_SHARE</code> bit is set in <code>nc_open()</code> or <code>nc_create()</code>, accesses to the underlying netCDF dataset are buffered by the library. This function synchronizes the state of the underlying dataset and the library. This is done automatically by <code>nc_close()</code> and <code>nc_enddef()</code>.</p>
<dt> <code>int nc_abort(int </code><i>ncid</i>) </p>
<p> (Corresponds to <code>ncabort()</code> in version 2) </p>
<dd>You don&#8217;t need to call this function. This function is called automatically by <code>nc_close()</code> if the netCDF was in define mode and something goes wrong with the commit. If the netCDF dataset isn&#8217;t in define mode, then this function is equivalent to <code>nc_close()</code>. If it is called after <code>nc_redef()</code>, but before <code>nc_enddef()</code>, the new definitions are not committed and the dataset is closed. If it is called after <code>nc_create()</code> but before <code>nc_enddef()</code>, the dataset disappears.</p>
<dt> <code>int nc_close(int </code><i>ncid</i>) </p>
<p> (Corresponds to <code>ncclose()</code> in version 2) </p>
<dd>Closes an open netCDF dataset. If the dataset is in define mode, <code>nc_enddef()</code> will be called before closing. After a dataset is closed, its ID may be reassigned to another dataset.</p>
<dt> <code>int nc_inq(int </code><i>ncid</i>, int* <i>ndims</i>, int* <i>nvars</i>,</p>
<dd>int* <i>natts</i>, int* <i>unlimdimid</i>)</p>
<dt> <code>int nc_inq_ndims(int </code><i>ncid</i>, int* <i>ndims</i>)</p>
<dt> <code>int nc_inq_nvars(int </code><i>ncid</i>, int* <i>nvars</i>)</p>
<dt> <code>int nc_inq_natts(int </code><i>ncid</i>, int* <i>natts</i>)</p>
<dt> <code>int nc_inq_unlimdim(int </code><i>ncid</i>, int* <i>unlimdimid</i>)</p>
<dt> <code>int nc_inq_format(int </code><i>ncid</i>, int* <i>formatn</i>) </p>
<dd>Use these functions to find out what is in a netCDF dataset. Upon successful return, <i>ndims</i> will contain the number of dimensions defined for this netCDF dataset, <i>nvars</i> will contain the number of variables, <i>natts</i> will contain the number of attributes, and <i>unlimdimid</i> will contain the dimension ID of the unlimited dimension if one exists, or -1 otherwise. <i>formatn</i> will contain the version number of the dataset &lt;format&gt;, one of <code>NC_FORMAT_CLASSIC</code>, <code>NC_FORMAT_64BIT</code>, <code>NC_FORMAT_NETCDF4</code>, or <code>NC_FORMAT_NETCDF4_CLASSIC</code>. If any of the return parameters is a <code>NULL</code> pointer, then the corresponding information will not be returned; hence, no space need be allocated for it.</p>
<dt> <code>int nc_def_dim(int </code><i>ncid</i>, const char <i>name</i>[], size_t <i>len</i>, int* <i>dimid</i>) </p>
<p> (Corresponds to <code>ncdimdef()</code> in version 2) </p>
<dd>Adds a new dimension to an open netCDF dataset, which must be in define mode. <i>name</i> is the dimension name. If <i>dimid</i> is not a <code>NULL</code> pointer then upon successful completion <i>dimid</i> will contain the dimension ID of the newly created dimension. </p>
</dl>
<h2>User Defined Types</h2>
<p>Users many define types for a netCDF-4/HDF5 file (unless the <code>NC_CLASSIC_MODEL</code> was used when the file was creates). Users may define compound types, variable length arrays, enumeration types, and opaque types. </p>
<dl>
<dt> <code>int nc_def_compound(int </code><i>ncid</i>, size_t <i>size</i>, const char <i>name</i>[], int* <i>typeidp</i>) </p>
<dd>Define a compound type.</p>
<dt> <code>int nc_insert_compound(int </code><i>ncid</i>, nc_type <i></i>, const char <i>name</i>[], size_t <i>offset</i>, nc_type <i>field_typeid</i>) </p>
<dd>Insert an element into a compound type. May not be done after type has been used, or after the type has been written by an enddef.</p>
<dt> <code>int nc_insert_array_compound(int </code><i>ncid</i>, nc_type <i></i>, const char <i>name</i>[], size_t <i>offset</i>, nc_type <i>field_typeid</i>, int <i>ndims</i>, const int <i>dim_sizes</i>[]) </p>
<dd>Insert an array into a compound type.</p>
<dt> <code>int nc_inq_type(int </code><i>ncid</i>, nc_type <i></i>, char <i>name</i>[], size_t* <i>sizep</i>) </p>
<dd>Learn about a type.</p>
<dt> <code>int nc_inq_compound(int </code><i>ncid</i>, nc_type <i></i>, char <i>name</i>[], size_t* <i>sizep</i>, size_t* <i>nfieldsp</i>)</p>
<dt> <code>int nc_inq_compound_name(int </code><i>ncid</i>, nc_type <i></i>, char <i>name</i>[])</p>
<dt> <code>int nc_inq_compound_size(int </code><i>ncid</i>, nc_type <i></i>, size_t* <i>sizep</i>)</p>
<dt> <code>int nc_inq_compound_nfields(int </code><i>ncid</i>, nc_type <i></i>, size_t* <i>nfieldsp</i>)</p>
<dt> <code>int nc_inq_compound_fieldname(int </code><i>ncid</i>, nc_type <i></i>, int <i>fieldid</i>, char <i>name</i>[])</p>
<dt> <code>int nc_inq_compound_fieldindex(int </code><i>ncid</i>, nc_type <i></i>, const char <i>name</i>[], int* <i>fieldidp</i>)</p>
<dt> <code>int nc_inq_compound_fieldoffset(int </code><i>ncid</i>, nc_type <i></i>, int <i>fieldid</i>, size_t* <i>offsetp</i>)</p>
<dt> <code>int nc_inq_compound_fieldtype(int </code><i>ncid</i>, nc_type <i></i>, int <i>fieldid</i>, nc_type* <i>field_typeid</i>)</p>
<dt> <code>int nc_inq_compound_fieldndims(int </code><i>ncid</i>, nc_type <i></i>, int <i>fieldid</i>, int* <i>ndims</i>)</p>
<dt> <code>int nc_inq_compound_fielddim_sizes(int </code><i>ncid</i>, nc_type <i></i>, int <i>fieldid</i>, int <i>dim_sizes</i>[]) </p>
<dd>Learn about a compound type.</p>
<dt> <code>int nc_def_vlen(int </code><i>ncid</i>, const char <i>name</i>[], nc_type <i>base_typeid</i>, nc_type* <i>xtypep</i>) </p>
<dd>Create a varaible length array type.</p>
<dt> <code>int nc_inq_vlen(int </code><i>ncid</i>, nc_type <i></i>, char <i>name</i>[], size_t* <i>datum_sizep</i>, nc_type* <i>base_nc_typep</i>) </p>
<dd>Learn about a varaible length array type.</p>
<dt> <code>int nc_free_vlen(nc_vlen_t *vl)</code> </p>
<dd>Free memory comsumed by reading data of a varaible length array type.</p>
<dt> <code>int nc_put_vlen_element(int </code><i>ncid</i>, nc_type <i></i>, void * <i>vlen_element</i>, size_t <i>len</i>, void * <i>data</i>) </p>
<dd>Write one VLEN.</p>
<dt> <code>int nc_get_vlen_element(int </code><i>ncid</i>, nc_type <i></i>, void ** <i>vlen_element</i>, size_t <i>len</i>, void ** <i>data</i>) </p>
<dd>Read one VLEN.</p>
<dt> <code>int nc_free_string(size_t </code><i>len</i>, char **data) </p>
<dd>Free memory comsumed by reading data of a string type.</p>
<dt> <code>int nc_inq_user_type(int </code><i>ncid</i>, nc_type <i></i>, char <i>name</i>[], size_t* <i></i>, nc_type* <i></i>, size_t* <i></i>, int* <i></i>) </p>
<dd>Learn about a user define type.</p>
<dt> <code>int nc_def_enum(int </code><i>ncid</i>, nc_type <i>base_typeid</i>, const char <i>name</i>[], nc_type* <i>typeidp</i>) </p>
<dd>Define an enumeration type.</p>
<dt> <code>int nc_insert_enum(int </code><i>ncid</i>, nc_type <i>base_typeid</i>, const char <i>name</i>[], const void *value) </p>
<dd>Insert a name-value pair into enumeration type.</p>
<dt> <code>int nc_inq_enum_member(int </code><i>ncid</i>, nc_type <i>xtype</i>, int <i>idx</i>, char <i>name</i>[], void *value)</p>
<dt> <code>int nc_inq_enum_ident(int </code><i>ncid</i>, nc_type <i>xtype</i>, int <i>idx</i>, long long <i>value</i>, char <i>identifier</i>[]) </p>
<dd>Learn about a name-value pair into enumeration type.</p>
<dt> <code>int nc_def_opaque(int </code><i>ncid</i>, size_t <i>size</i>, const char <i>name</i>[], nc_type* <i>xtypep</i>) </p>
<dd>Create an opaque type.</p>
<dt> <code>int nc_inq_opaque(int </code><i>ncid</i>, nc_type <i>xtype</i>, char <i>name</i>[], size_t* <i>sizep</i>) </p>
<dd>Learn about opaque type.</p>
<dt></dl>
<h2>Groups</h2>
<dd>Users may organize data into hierarchical groups in netCDF-4/HDF5 files (unless <code>NC_CLASSIC_MODEL</code> was used when creating the file).</p>
<dl>
<dt> <code>int nc_inq_grps(int </code><i>ncid</i>, int* <i>numgrps</i>, int <i>ncids</i>[]) </p>
<dd>Learn how many groups (and their ncids) are available from the group represented by ncid.</p>
<dt> <code>int nc_inq_grpname(int </code><i>ncid</i>, char <i>name</i>[])</p>
<dt> <code>int nc_inq_grpname_full(int </code><i>ncid</i>, size_t* <i>len</i>, char <i>name</i>[])</p>
<dt> <code>int nc_inq_grpname_len(int </code><i>ncid</i>, size_t* <i>len</i>)</p>
<dt> <code>int nc_inq_grp_parent(int </code><i>ncid</i>, int* <i>ncid</i>)</p>
<dt> <code>int nc_inq_grp_ncid(int </code><i>ncid</i>, char <i>name</i>[], int* <i>ncid</i>)</p>
<dt> <code>int nc_inq_full_ncid(int </code><i>ncid</i>, char <i>name</i>[], int* <i>ncid</i>) </p>
<dd>Learn about a group.</p>
<dt> <code>int nc_inq_varids(int </code><i>ncid</i>, int* <i>nvars</i>, int* <i></i>) </p>
<dd>Get the varids in a group.</p>
<dt> <code>int nc_inq_dimids(int </code><i>ncid</i>, int* <i>ndims</i>, int* <i>dimids</i>, int <i>include_parents</i>) </p>
<dd>Get the dimids in a group and (potentially) its parents.</p>
<dt> <code>int nc_inq_typeids(int </code><i>ncid</i>, int* <i>ntypes</i>, int <i>typeids</i>[]) </p>
<dd>Get the typeids of user-defined types in a group.</p>
<dt> <code>int nc_def_grp(int </code><i>ncid</i>, char <i>name</i>[], int* <i>ncid</i>) </p>
<dd>Create a group.</dl>
<h2>Dimensions</h2>
<dl>
<dt> <code>int nc_inq_dimid(int </code><i>ncid</i>, const char <i>name</i>[], int* <i>dimid</i>) </p>
<p> (Corresponds to <code>ncdimid()</code> in version 2) </p>
<dd>Given a dimension name, returns the ID of a netCDF dimension in <i>dimid</i>.</p>
<dt> <code>int nc_inq_dim(int </code><i>ncid</i>, int <i>dimid</i>, char <i>name</i>[], size_t* <i>len</i>)</p>
<dt> <code>int nc_inq_dimname(int </code><i>ncid</i>, int <i>dimid</i>, char <i>name</i>[])</p>
<dt> <code>int nc_inq_dimlen(int </code><i>ncid</i>, int <i>dimid</i>, size_t* <i>len</i>) </p>
<dd>Use these functions to find out about a dimension. If either the <i>name</i> argument or <i>len</i> argument is a <code>NULL</code> pointer, then the associated information will not be returned. Otherwise, <i>name</i> should be big enough (<code>NC_MAX_NAME</code>) to hold the dimension name as the name will be copied into your storage. The length return parameter, <i>len</i> will contain the size of the dimension. For the unlimited dimension, the returned length is the current maximum value used for writing into any of the variables which use the dimension.</p>
<dt> <code>int nc_rename_dim(int </code><i>ncid</i>, int <i>dimid</i>, const char <i>name</i>[]) </p>
<p> (Corresponds to <code>ncdimrename()</code> in version 2) </p>
<dd>Renames an existing dimension in an open netCDF dataset. If the new name is longer than the old name, the netCDF dataset must be in define mode. You cannot rename a dimension to have the same name as another dimension.</dl>
<h2>Variables</h2>
<dl>
<dt> <code>int nc_def_var(int </code><i>ncid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, int <i>ndims</i>, const int <i>dimids</i>[], int* <i>varid</i>) </p>
<p> (Corresponds to <code>ncvardef()</code> in version 2) </p>
<dd>Adds a new variable to a netCDF dataset. The netCDF must be in define mode. If not <code>NULL</code>, then <i>varid</i> will be set to the netCDF variable ID.</p>
<dt> <code>int nc_inq_varid(int </code><i>ncid</i>, const char <i>name</i>[], int* <i>varid</i>) </p>
<p> (Corresponds to <code>ncvarid()</code> in version 2) </p>
<dd>Returns the ID of a netCDF variable in <i>varid</i> given its name.</p>
<dt> <code>int nc_inq_var(int </code><i>ncid</i>, int <i>varid</i>, char <i>name</i>[], nc_type* <i>xtype</i>, int* <i>ndims</i>, int <i>dimids</i>[],</p>
<dd>int* <i>natts</i>)</p>
<dt> <code>int nc_inq_varname(int </code><i>ncid</i>, int <i>varid</i>, char <i>name</i>[])</p>
<dt> <code>int nc_inq_vartype(int </code><i>ncid</i>, int <i>varid</i>, nc_type* <i>xtype</i>)</p>
<dt> <code>int nc_inq_varndims(int </code><i>ncid</i>, int <i>varid</i>, int* <i>ndims</i>)</p>
<dt> <code>int nc_inq_vardimid(int </code><i>ncid</i>, int <i>varid</i>, int <i>dimids</i>[])</p>
<dt> <code>int nc_inq_varnatts(int </code><i>ncid</i>, int <i>varid</i>, int* <i>natts</i>) </p>
<dd>Returns information about a netCDF variable, given its ID. If any of the return parameters (<i>name</i>, <i>xtype</i>, <i>ndims</i>, <i>dimids</i>, or <i>natts</i>) is a <code>NULL</code> pointer, then the corresponding information will not be returned; hence, no space need be allocated for it.</p>
<dt> <code>int nc_rename_var(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[]) </p>
<p> (Corresponds to <code>ncvarrename()</code> in version 2) </p>
<dd>Changes the name of a netCDF variable. If the new name is longer than the old name, the netCDF must be in define mode. You cannot rename a variable to have the name of any existing variable. </p>
</dl>
<h2>VARIABLES <i>in</i> NETCDF-4 FILES</h2>
<p>The following functions may only be used on variables in a netCDF-4/HDF5 data file. These functions must be called after the variable is defined, but before an enddef call. </p>
<p> <code>int nc_def_var_deflate(int </code><i>ncid</i>, int <i>varid</i>, int <i>shuffle</i>, int <i>deflate</i>, int <i>deflate_level</i>) </p>
<p> Turn on compression and/or shuffle filter. (Shuffle filter is only useful for integer data.)</p>
<dl>
<dt> <code>int nc_inq_var_deflate(int </code><i>ncid</i>, int <i>varid</i>, int* <i>shufflep</i>, int* <i>deflatep</i>, int* <i>deflate_levelp</i>) </p>
<dd>Learn about a variable&#8217;s deflate settings.</p>
<dt> <code>int nc_def_var_fletcher32(int </code><i>ncid</i>, int <i>varid</i>, int <i>fletcher32</i>) </p>
<dd>Turn on checksumming for a variable.</p>
<dt> <code>int nc_inq_var_fletcher32(int </code><i>ncid</i>, int <i>varid</i>, int* <i>fletcher32</i>) </p>
<dd>Learn about checksumming for a variable.</p>
<dt> <code>int nc_def_var_chunking(int </code><i>ncid</i>, int <i>varid</i>, int <i>storage</i>, const size_t <i>chunksizesp</i>[]) </p>
<dd>Set chunksizes for a variable.</p>
<dt> <code>int nc_inq_var_chunking(int </code><i>ncid</i>, int <i>varid</i>, int* <i>storagep</i>, size_t <i>chunksizesp</i>[]) </p>
<dd>Learn about chunksizes for a variable.</p>
<dt> <code>int nc_def_var_fill(int </code><i>ncid</i>, int <i>varid</i>, int <i>no_fill</i>, const size_t <i>chunksizesp</i>[]) </p>
<dd>Set a fill value for a variable.</p>
<dt> <code>int nc_inq_var_fill(int </code><i>ncid</i>, int <i>varid</i>, int* <i>storagep</i>, size_t <i>chunksizesp</i>[]) </p>
<dd>Learn the fill value for a variable.</p>
<dt> <code>int nc_def_var_endian(int </code><i>ncid</i>, int <i>varid</i>, int <i>endian</i>) </p>
<dd>Set endianness of variable.</p>
<dt> <code>int nc_inq_var_endian(int </code><i>ncid</i>, int <i>varid</i>, int* <i>endianp</i>) </p>
<dd>Learn the endianness of a variable.</p>
<dt>
</dl>
<h2>Writing And Reading Whole Variables</h2>
<dl>
<dt> <code>int nc_put_var_text(int </code><i>ncid</i>, int <i>varid</i>, const char <i>out</i>[])</p>
<dt> <code>int nc_put_var_uchar(int </code><i>ncid</i>, int <i>varid</i>, const unsigned char <i>out</i>[])</p>
<dt> <code>int nc_put_var_schar(int </code><i>ncid</i>, int <i>varid</i>, const signed char <i>out</i>[])</p>
<dt> <code>int nc_put_var_short(int </code><i>ncid</i>, int <i>varid</i>, const short <i>out</i>[])</p>
<dt> <code>int nc_put_var_int(int </code><i>ncid</i>, int <i>varid</i>, const int <i>out</i>[])</p>
<dt> <code>int nc_put_var_long(int </code><i>ncid</i>, int <i>varid</i>, const long <i>out</i>[])</p>
<dt> <code>int nc_put_var_float(int </code><i>ncid</i>, int <i>varid</i>, const float <i>out</i>[])</p>
<dt> <code>int nc_put_var_double(int </code><i>ncid</i>, int <i>varid</i>, const double <i>out</i>[])</p>
<dt> <code>int nc_put_var_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const unsigned char <i>out</i>[])</p>
<dt> <code>int nc_put_var_ushort(int </code><i>ncid</i>, int <i>varid</i>, const unsigned short <i>out</i>[])</p>
<dt> <code>int nc_put_var_uint(int </code><i>ncid</i>, int <i>varid</i>, const unsigned int <i>out</i>[])</p>
<dt> <code>int nc_put_var_int64(int </code><i>ncid</i>, int <i>varid</i>, const long long <i>out</i>[])</p>
<dt> <code>int nc_put_var_uint64(int </code><i>ncid</i>, int <i>varid</i>, const unsigned long long <i>out</i>[])</p>
<dt> <code>int nc_put_var_string(int </code><i>ncid</i>, int <i>varid</i>, const char * <i>out</i>[]) </p>
<dd>Writes an entire netCDF variable (i.e. all the values). The netCDF dataset must be open and in data mode. The type of the data is specified in the function name, and it is converted to the external type of the specified variable, if possible, otherwise an <code>NC_ERANGE</code> error is returned. Note that rounding is not performed during the conversion. Floating point numbers are truncated when converted to integers.</p>
<dt> <code>int nc_get_var_text(int </code><i>ncid</i>, int <i>varid</i>, char <i>in</i>[])</p>
<dt> <code>int nc_get_var_uchar(int </code><i>ncid</i>, int <i>varid</i>, unsigned char <i>in</i>[])</p>
<dt> <code>int nc_get_var_schar(int </code><i>ncid</i>, int <i>varid</i>, signed char <i>in</i>[])</p>
<dt> <code>int nc_get_var_short(int </code><i>ncid</i>, int <i>varid</i>, short <i>in</i>[])</p>
<dt> <code>int nc_get_var_int(int </code><i>ncid</i>, int <i>varid</i>, int <i>in</i>[])</p>
<dt> <code>int nc_get_var_long(int </code><i>ncid</i>, int <i>varid</i>, long <i>in</i>[])</p>
<dt> <code>int nc_get_var_float(int </code><i>ncid</i>, int <i>varid</i>, float <i>in</i>[])</p>
<dt> <code>int nc_get_var_double(int </code><i>ncid</i>, int <i>varid</i>, double <i>in</i>[])</p>
<dt> <code>int nc_get_var_ubyte(int </code><i>ncid</i>, int <i>varid</i>, unsigned char <i>in</i>[])</p>
<dt> <code>int nc_get_var_ushort(int </code><i>ncid</i>, int <i>varid</i>, unsigned short <i>in</i>[])</p>
<dt> <code>int nc_get_var_uint(int </code><i>ncid</i>, int <i>varid</i>, unsigned int <i>in</i>[])</p>
<dt> <code>int nc_get_var_int64(int </code><i>ncid</i>, int <i>varid</i>, long long <i>in</i>[])</p>
<dt> <code>int nc_get_var_uint64(int </code><i>ncid</i>, int <i>varid</i>, unsigned long long <i>in</i>[])</p>
<dt> <code>int nc_get_var_string(int </code><i>ncid</i>, int <i>varid</i>, char * <i>in</i>[]) </p>
<dd>Reads an entire netCDF variable (i.e. all the values). The netCDF dataset must be open and in data mode. The data is converted from the external type of the specified variable, if necessary, to the type specified in the function name. If conversion is not possible, an <code>NC_ERANGE</code> error is returned.</dl>
<h2>Writing And Reading One Datum</h2>
<dl>
<dt> <code>int nc_put_var1_text(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], char <i>*out</i>)</p>
<dt> <code>int nc_put_var1_uchar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], unsigned char <i>*out</i>)</p>
<dt> <code>int nc_put_var1_schar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], signed char <i>*out</i>)</p>
<dt> <code>int nc_put_var1_short(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], short <i>*out</i>)</p>
<dt> <code>int nc_put_var1_int(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], int <i>*out</i>)</p>
<dt> <code>int nc_put_var1_long(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], long <i>*out</i>)</p>
<dt> <code>int nc_put_var1_float(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], float <i>*out</i>)</p>
<dt> <code>int nc_put_var1_double(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], double <i>*out</i>)</p>
<dt> <code>int nc_put_var1_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], unsigned char <i>*out</i>)</p>
<dt> <code>int nc_put_var1_ushort(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], unsigned short <i>*out</i>)</p>
<dt> <code>int nc_put_var1_uint(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], unsigned int <i>*out</i>)</p>
<dt> <code>int nc_put_var1_int64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], long long <i>*out</i>)</p>
<dt> <code>int nc_put_var1_uint64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], unsigned long long <i>*out</i>)</p>
<dt> <code>int nc_put_var1_string(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], char * <i>*out</i>) </p>
<dd>Puts a single data value into a variable at the position <i>index</i> of an open netCDF dataset that is in data mode. The type of the data is specified in the function name, and it is converted to the external type of the specified variable, if possible, otherwise an <code>NC_ERANGE</code> error is returned.</p>
<dt> <code>int nc_get_var1_text(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], char* <i>in</i>)</p>
<dt> <code>int nc_get_var1_uchar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], unsigned char* <i>in</i>)</p>
<dt> <code>int nc_get_var1_schar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], signed char* <i>in</i>)</p>
<dt> <code>int nc_get_var1_short(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], short* <i>in</i>)</p>
<dt> <code>int nc_get_var1_int(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], int* <i>in</i>)</p>
<dt> <code>int nc_get_var1_long(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], long* <i>in</i>)</p>
<dt> <code>int nc_get_var1_float(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], float* <i>in</i>)</p>
<dt> <code>int nc_get_var1_double(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], double* <i>in</i>)</p>
<dt> <code>int nc_get_var1_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], unsigned char* <i>in</i>)</p>
<dt> <code>int nc_get_var1_ushort(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], unsigned short* <i>in</i>)</p>
<dt> <code>int nc_get_var1_uint(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], unsigned int* <i>in</i>)</p>
<dt> <code>int nc_get_var1_int64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], long long* <i>in</i>)</p>
<dt> <code>int nc_get_var1_uint64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], unsigned long long* <i>in</i>)</p>
<dt> <code>int nc_get_var1_string(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>index</i>[], char ** <i>in</i>) </p>
<dd>Gets a single data value from a variable at the position <i>index</i> of an open netCDF dataset that is in data mode. The data is converted from the external type of the specified variable, if necessary, to the type specified in the function name. If conversion is not possible, an <code>NC_ERANGE</code> error is returned.</dl>
<h2>Writing And Reading An Array</h2>
<dl>
<dt> <code>int nc_put_vara_text(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const char <i>out</i>[])</p>
<dt> <code>int nc_put_vara_uchar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const unsigned char <i>out</i>[])</p>
<dt> <code>int nc_put_vara_schar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const signed char <i>out</i>[])</p>
<dt> <code>int nc_put_vara_short(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const short <i>out</i>[])</p>
<dt> <code>int nc_put_vara_int(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const int <i>out</i>[])</p>
<dt> <code>int nc_put_vara_long(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const long <i>out</i>[])</p>
<dt> <code>int nc_put_vara_float(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const float <i>out</i>[])</p>
<dt> <code>int nc_put_vara_double(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const double <i>out</i>[])</p>
<dt> <code>int nc_put_vara_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const unsigned char <i>out</i>[])</p>
<dt> <code>int nc_put_vara_ushort(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const unsigned short <i>out</i>[])</p>
<dt> <code>int nc_put_vara_uint(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const unsigned int <i>out</i>[])</p>
<dt> <code>int nc_put_vara_int64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const long long <i>out</i>[])</p>
<dt> <code>int nc_put_vara_uint64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const unsigned long long <i>out</i>[])</p>
<dt> <code>int nc_put_vara_string(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const char * <i>out</i>[]) </p>
<dd>Writes an array section of values into a netCDF variable of an open netCDF dataset, which must be in data mode. The array section is specified by the <i>start</i> and <i>count</i> vectors, which give the starting index and count of values along each dimension of the specified variable. The type of the data is specified in the function name and is converted to the external type of the specified variable, if possible, otherwise an <code>NC_ERANGE</code> error is returned.</p>
<dt> <code>int nc_get_vara_text(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], char <i>in</i>[])</p>
<dt> <code>int nc_get_vara_uchar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], unsigned char <i>in</i>[])</p>
<dt> <code>int nc_get_vara_schar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], signed char <i>in</i>[])</p>
<dt> <code>int nc_get_vara_short(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], short <i>in</i>[])</p>
<dt> <code>int nc_get_vara_int(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], int <i>in</i>[])</p>
<dt> <code>int nc_get_vara_long(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], long <i>in</i>[])</p>
<dt> <code>int nc_get_vara_float(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], float <i>in</i>[])</p>
<dt> <code>int nc_get_vara_double(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], double <i>in</i>[])</p>
<dt> <code>int nc_get_vara_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], unsigned char <i>in</i>[])</p>
<dt> <code>int nc_get_vara_ushort(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], unsigned short <i>in</i>[])</p>
<dt> <code>int nc_get_vara_uint(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], unsigned int <i>in</i>[])</p>
<dt> <code>int nc_get_vara_int64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], long long <i>in</i>[])</p>
<dt> <code>int nc_get_vara_uint64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], unsigned long long <i>in</i>[])</p>
<dt> <code>int nc_get_vara_string(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], char * <i>in</i>[]) </p>
<dd>Reads an array section of values from a netCDF variable of an open netCDF dataset, which must be in data mode. The array section is specified by the <i>start</i> and <i>count</i> vectors, which give the starting index and count of values along each dimension of the specified variable. The data is converted from the external type of the specified variable, if necessary, to the type specified in the function name. If conversion is not possible, an <code>NC_ERANGE</code> error is returned.</dl>
<h2>Writing And Reading A Sliced Array</h2>
<dl>
<dt> <code>int nc_put_vars_text(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const char <i>out</i>[])</p>
<dt> <code>int nc_put_vars_uchar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const unsigned char <i>out</i>[])</p>
<dt> <code>int nc_put_vars_schar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const signed char <i>out</i>[])</p>
<dt> <code>int nc_put_vars_short(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const short <i>out</i>[])</p>
<dt> <code>int nc_put_vars_int(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const int <i>out</i>[])</p>
<dt> <code>int nc_put_vars_long(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const long <i>out</i>[])</p>
<dt> <code>int nc_put_vars_float(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const float <i>out</i>[])</p>
<dt> <code>int nc_put_vars_double(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const double <i>out</i>[])</p>
<dt> <code>int nc_put_vars_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const unsigned char <i>out</i>[])</p>
<dt> <code>int nc_put_vars_ushort(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const unsigned short <i>out</i>[])</p>
<dt> <code>int nc_put_vars_uint(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const unsigned int <i>out</i>[])</p>
<dt> <code>int nc_put_vars_int64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const long long <i>out</i>[])</p>
<dt> <code>int nc_put_vars_uint64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const unsigned long long <i>out</i>[])</p>
<dt> <code>int nc_put_vars_string(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], const char * <i>out</i>[]) </p>
<dd>These functions are used for <i>strided output</i>, which is like the array section output described above, except that the sampling stride (the interval between accessed values) is specified for each dimension. For an explanation of the sampling stride vector, see COMMON ARGUMENTS DESCRIPTIONS below.</p>
<dt> <code>int nc_get_vars_text(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], char <i>in</i>[])</p>
<dt> <code>int nc_get_vars_uchar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], unsigned char <i>in</i>[])</p>
<dt> <code>int nc_get_vars_schar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], signed char <i>in</i>[])</p>
<dt> <code>int nc_get_vars_short(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], short <i>in</i>[])</p>
<dt> <code>int nc_get_vars_int(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], int <i>in</i>[])</p>
<dt> <code>int nc_get_vars_long(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], long <i>in</i>[])</p>
<dt> <code>int nc_get_vars_float(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], float <i>in</i>[])</p>
<dt> <code>int nc_get_vars_double(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], double <i>in</i>[])</p>
<dt> <code>int nc_get_vars_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], unsigned char <i>in</i>[])</p>
<dt> <code>int nc_get_vars_ushort(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], unsigned short <i>in</i>[])</p>
<dt> <code>int nc_get_vars_uint(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], unsigned int <i>in</i>[])</p>
<dt> <code>int nc_get_vars_int64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], long long <i>in</i>[])</p>
<dt> <code>int nc_get_vars_uint64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], unsigned long long <i>in</i>[])</p>
<dt> <code>int nc_get_vars_string(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], char * <i>in</i>[]) </p>
<dd>These functions are used for <i>strided input</i>, which is like the array section input described above, except that the sampling stride (the interval between accessed values) is specified for each dimension. For an explanation of the sampling stride vector, see COMMON ARGUMENTS DESCRIPTIONS below.</dl>
<h2>Writing And Reading A Mapped Array</h2>
<dl>
<dt> <code>int nc_put_varm_text(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const char <i>out</i>[])</p>
<dt> <code>int nc_put_varm_uchar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const unsigned char <i>out</i>[])</p>
<dt> <code>int nc_put_varm_schar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const signed char <i>out</i>[])</p>
<dt> <code>int nc_put_varm_short(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const short <i>out</i>[])</p>
<dt> <code>int nc_put_varm_int(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const int <i>out</i>[])</p>
<dt> <code>int nc_put_varm_long(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const long <i>out</i>[])</p>
<dt> <code>int nc_put_varm_float(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const float <i>out</i>[])</p>
<dt> <code>int nc_put_varm_double(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const double <i>out</i>[])</p>
<dt> <code>int nc_put_varm_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const unsigned char <i>out</i>[])</p>
<dt> <code>int nc_put_varm_ushort(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const unsigned short <i>out</i>[])</p>
<dt> <code>int nc_put_varm_uint(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const unsigned int <i>out</i>[])</p>
<dt> <code>int nc_put_varm_int64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const long long <i>out</i>[])</p>
<dt> <code>int nc_put_varm_uint64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const unsigned long long <i>out</i>[])</p>
<dt> <code>int nc_put_varm_string(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, const char * <i>out</i>[]) </p>
<dd>These functions are used for <i>mapped output</i>, which is like strided output described above, except that an additional index mapping vector is provided to specify the in-memory arrangement of the data values. For an explanation of the index mapping vector, see COMMON ARGUMENTS DESCRIPTIONS below.</p>
<dt> <code>int nc_get_varm_text(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, char <i>in</i>[])</p>
<dt> <code>int nc_get_varm_uchar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, unsigned char <i>in</i>[])</p>
<dt> <code>int nc_get_varm_schar(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, signed char <i>in</i>[])</p>
<dt> <code>int nc_get_varm_short(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, short <i>in</i>[])</p>
<dt> <code>int nc_get_varm_int(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, int <i>in</i>[])</p>
<dt> <code>int nc_get_varm_long(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, long <i>in</i>[])</p>
<dt> <code>int nc_get_varm_float(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, float <i>in</i>[])</p>
<dt> <code>int nc_get_varm_double(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, double <i>in</i>[])</p>
<dt> <code>int nc_get_varm_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, unsigned char <i>in</i>[])</p>
<dt> <code>int nc_get_varm_ushort(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, unsigned short <i>in</i>[])</p>
<dt> <code>int nc_get_varm_uint(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, unsigned int <i>in</i>[])</p>
<dt> <code>int nc_get_varm_int64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, long long <i>in</i>[])</p>
<dt> <code>int nc_get_varm_uint64(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, unsigned long long <i>in</i>[])</p>
<dt> <code>int nc_get_varm_string(int </code><i>ncid</i>, int <i>varid</i>, const size_t <i>start</i>[], const size_t <i>count</i>[], const size_t <i>stride</i>[], <i>imap</i>, char * <i>in</i>[]) </p>
<dd>These functions are used for <i>mapped input</i>, which is like strided input described above, except that an additional index mapping vector is provided to specify the in-memory arrangement of the data values. For an explanation of the index mapping vector, see COMMON ARGUMENTS DESCRIPTIONS below.</dl>
<h2>Attributes</h2>
<dl>
<dt> <code>int nc_put_att_text(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const char <i>out</i>[])</p>
<dt> <code>int nc_put_att_uchar(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const unsigned char <i>out</i>[])</p>
<dt> <code>int nc_put_att_schar(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const signed char <i>out</i>[])</p>
<dt> <code>int nc_put_att_short(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const short <i>out</i>[])</p>
<dt> <code>int nc_put_att_int(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const int <i>out</i>[])</p>
<dt> <code>int nc_put_att_long(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const long <i>out</i>[])</p>
<dt> <code>int nc_put_att_float(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const float <i>out</i>[])</p>
<dt> <code>int nc_put_att_double(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const double <i>out</i>[])</p>
<dt> <code>int nc_put_att_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const unsigned char <i>out</i>[])</p>
<dt> <code>int nc_put_att_ushort(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const unsigned short <i>out</i>[])</p>
<dt> <code>int nc_put_att_uint(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const unsigned int <i>out</i>[])</p>
<dt> <code>int nc_put_att_int64(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const long long <i>out</i>[])</p>
<dt> <code>int nc_put_att_uint64(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const unsigned long long <i>out</i>[])</p>
<dt> <code>int nc_put_att_string(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, const char * <i>out</i>[]) </p>
<dt> <code>int nc_put_att(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type <i>xtype</i>, size_t <i>len</i>, void * <i>ip</i>)</p>
<dt> <code>int nc_get_att(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], void ** <i>ip</i>) </p>
<dd>Unlike variables, attributes do not have separate functions for defining and writing values. This family of functions defines a new attribute with a value or changes the value of an existing attribute. If the attribute is new, or if the space required to store the attribute value is greater than before, the netCDF dataset must be in define mode. The parameter <i>len</i> is the number of values from <i>out</i> to transfer. It is often one, except that for <code>nc_put_att_text()</code> it will usually be <code>strlen(</code><i>out</i>). </p>
<p> For these functions, the type component of the function name refers to the in-memory type of the value, whereas the <i>xtype</i> argument refers to the external type for storing the value. An <code>NC_ERANGE</code> error results if a conversion between these types is not possible. In this case the value is represented with the appropriate fill-value for the associated external type.</p>
<dt> <code>int nc_inq_attname(int </code><i>ncid</i>, int <i>varid</i>, int <i>attnum</i>, char <i>name</i>[]) </p>
<dd>Gets the name of an attribute, given its variable ID and attribute number. This function is useful in generic applications that need to get the names of all the attributes associated with a variable, since attributes are accessed by name rather than number in all other attribute functions. The number of an attribute is more volatile than the name, since it can change when other attributes of the same variable are deleted. The attributes for each variable are numbered from 0 (the first attribute) to <i>nvatts</i>-1, where <i>nvatts</i> is the number of attributes for the variable, as returned from a call to <code>nc_inq_varnatts()</code>. If the <i>name</i> parameter is a <code>NULL</code> pointer, no name will be returned and no space need be allocated.</p>
<dt> <code>int nc_inq_att(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type* <i>xtype</i>, size_t* <i>len</i>)</p>
<dt> <code>int nc_inq_attid(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], int* <i>attnum</i>)</p>
<dt> <code>int nc_inq_atttype(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], nc_type* <i>xtype</i>)</p>
<dt> <code>int nc_inq_attlen(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], size_t* <i>len</i>) </p>
<dd>These functions return information about a netCDF attribute, given its variable ID and name. The information returned is the external type in <i>xtype</i> and the number of elements in the attribute as <i>len</i>. If any of the return arguments is a <code>NULL</code> pointer, the specified information will not be returned.</p>
<dt> <code>int nc_copy_att(int </code><i>ncid</i>, int <i>varid_in</i>, const char <i>name</i>[], int <i>ncid_out</i>, int <i>varid_out</i>) </p>
<dd>Copies an attribute from one netCDF dataset to another. It can also be used to copy an attribute from one variable to another within the same netCDF. <i>ncid_in</i> is the netCDF ID of an input netCDF dataset from which the attribute will be copied. <i>varid_in</i> is the ID of the variable in the input netCDF dataset from which the attribute will be copied, or <code>NC_GLOBAL</code> for a global attribute. <i>name</i> is the name of the attribute in the input netCDF dataset to be copied. <i>ncid_out</i> is the netCDF ID of the output netCDF dataset to which the attribute will be copied. It is permissible for the input and output netCDF ID&#8217;s to be the same. The output netCDF dataset should be in define mode if the attribute to be copied does not already exist for the target variable, or if it would cause an existing target attribute to grow. <i>varid_out</i> is the ID of the variable in the output netCDF dataset to which the attribute will be copied, or <code>NC_GLOBAL</code> to copy to a global attribute.</p>
<dt> <code>int nc_rename_att(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], const char <i>newname</i>[]) </p>
<dd>Changes the name of an attribute. If the new name is longer than the original name, the netCDF must be in define mode. You cannot rename an attribute to have the same name as another attribute of the same variable. <i>name</i> is the original attribute name. <i>newname</i> is the new name to be assigned to the specified attribute. If the new name is longer than the old name, the netCDF dataset must be in define mode.</p>
<dt> <code>int nc_del_att(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[]) </p>
<dd>Deletes an attribute from a netCDF dataset. The dataset must be in define mode.</p>
<dt> <code>int nc_get_att_text(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], char <i>in</i>[])</p>
<dt> <code>int nc_get_att_uchar(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], unsigned char <i>in</i>[])</p>
<dt> <code>int nc_get_att_schar(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], signed char <i>in</i>[])</p>
<dt> <code>int nc_get_att_short(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], short <i>in</i>[])</p>
<dt> <code>int nc_get_att_int(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], int <i>in</i>[])</p>
<dt> <code>int nc_get_att_long(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], long <i>in</i>[])</p>
<dt> <code>int nc_get_att_float(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], float <i>in</i>[])</p>
<dt> <code>int nc_get_att_double(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], double <i>in</i>[])</p>
<dt> <code>int nc_get_att_ubyte(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], unsigned char <i>in</i>[])</p>
<dt> <code>int nc_get_att_ushort(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], unsigned short <i>in</i>[])</p>
<dt> <code>int nc_get_att_uint(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], unsigned int <i>in</i>[])</p>
<dt> <code>int nc_get_att_int64(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], long long <i>in</i>[])</p>
<dt> <code>int nc_get_att_uint64(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], unsigned long long <i>in</i>[])</p>
<dt> <code>int nc_get_att_string(int </code><i>ncid</i>, int <i>varid</i>, const char <i>name</i>[], char * <i>in</i>[]) </p>
<dd>Gets the value(s) of a netCDF attribute, given its variable ID and name. Converts from the external type to the type specified in the function name, if possible, otherwise returns an <code>NC_ERANGE</code> error. All elements of the vector of attribute values are returned, so you must allocate enough space to hold them. If you don&#8217;t know how much space to reserve, call <code>nc_inq_attlen()</code> first to find out the length of the attribute.</dl>
<h2>Common Argument Descriptions</h2>
<p>In this section we define some common arguments which are used in the &quot;FUNCTION DESCRIPTIONS&quot; section.</p>
<dl>
<dt>int <i>ncid</i></p>
<dd>is the netCDF ID returned from a previous, successful call to <code>nc_open()</code> or <code>nc_create()</code></p>
<dt>char <i>name</i>[]</p>
<dd>is the name of a dimension, variable, or attribute. The names of dimensions, variables and attributes consist of arbitrary sequences of alphanumeric characters (as well as underscore &#8216;_&#8217;, period &#8216;.&#8217; and hyphen &#8216;-&#8216;), beginning with a letter or underscore. (However names commencing with underscore are reserved for system use.) Case is significant in netCDF names. A zero-length name is not allowed. As an input argument, it shall be a pointer to a 0-terminated string; as an output argument, it shall be the address of a buffer in which to hold such a string. The maximum allowable number of characters (excluding the terminating 0) is <code>NC_MAX_NAME</code>.</p>
<dt>nc_type <i>xtype</i></p>
<dd>specifies the external data type of a netCDF variable or attribute and is one of the following: <code>NC_BYTE</code>, <code>NC_CHAR</code>, <code>NC_SHORT</code>, <code>NC_INT</code>, <code>NC_FLOAT</code>, or <code>NC_DOUBLE</code>. These are used to specify 8-bit integers, characters, 16-bit integers, 32-bit integers, 32-bit IEEE floating point numbers, and 64-bit IEEE floating-point numbers, respectively. (<code>NC_INT</code> corresponds to <code>NC_LONG</code> in version 2, to specify a 32-bit integer).</p>
<dt>int <i>dimids</i>[]</p>
<dd>is a vector of dimension ID&#8217;s and defines the shape of a netCDF variable. The size of the vector shall be greater than or equal to the rank (i.e. the number of dimensions) of the variable (<i>ndims</i>). The vector shall be ordered by the speed with which a dimension varies: <i>dimids</i>[<i>ndims</i>-1] shall be the dimension ID of the most rapidly varying dimension and <i>dimids</i>[0] shall be the dimension ID of the most slowly varying dimension. The maximum possible number of dimensions for a variable is given by the symbolic constant <code>NC_MAX_VAR_DIMS</code>.</p>
<dt>int <i>dimid</i></p>
<dd>is the ID of a netCDF dimension. netCDF dimension ID&#8217;s are allocated sequentially from the non-negative integers beginning with 0.</p>
<dt>int <i>ndims</i></p>
<dd>is either the total number of dimensions in a netCDF dataset or the rank (i.e. the number of dimensions) of a netCDF variable. The value shall not be negative or greater than the symbolic constant <code>NC_MAX_VAR_DIMS</code>.</p>
<dt>int <i>varid</i></p>
<dd>is the ID of a netCDF variable or (for the attribute-access functions) the symbolic constant <code>NC_GLOBAL</code>, which is used to reference global attributes. netCDF variable ID&#8217;s are allocated sequentially from the non-negative integers beginning with 0.</p>
<dt>int* <i>natts</i></p>
<dd>is the number of global attributes in a netCDF dataset for the <code>nc_inquire()</code> function or the number of attributes associated with a netCDF variable for the <code>nc_varinq()</code> function.</p>
<dt>const size_t <i>index</i>[]</p>
<dd>specifies the indicial coordinates of the netCDF data value to be accessed. The indices start at 0; thus, for example, the first data value of a two-dimensional variable is (0,0). The size of the vector shall be at least the rank of the associated netCDF variable and its elements shall correspond, in order, to the variable&#8217;s dimensions.</p>
<dt>const size_t <i>start</i>[]</p>
<dd>specifies the starting point for accessing a netCDF variable&#8217;s data values in terms of the indicial coordinates of the corner of the array section. The indices start at 0; thus, the first data value of a variable is (0, 0, &#8230;, 0). The size of the vector shall be at least the rank of the associated netCDF variable and its elements shall correspond, in order, to the variable&#8217;s dimensions.</p>
<dt>const size_t <i>count</i>[]</p>
<dd>specifies the number of indices selected along each dimension of the array section. Thus, to access a single value, for example, specify <i>count</i> as (1, 1, &#8230;, 1). Note that, for strided I/O, this argument must be adjusted to be compatible with the <i>stride</i> and <i>start</i> arguments so that the interaction of the three does not attempt to access an invalid data co-ordinate. The elements of the <i>count</i> vector correspond, in order, to the variable&#8217;s dimensions.</p>
<dt>const size_t <i>stride</i>[]</p>
<dd>specifies the sampling interval along each dimension of the netCDF variable. The elements of the stride vector correspond, in order, to the netCDF variable&#8217;s dimensions (<i>stride</i>[0]) gives the sampling interval along the most slowly varying dimension of the netCDF variable). Sampling intervals are specified in type-independent units of elements (a value of 1 selects consecutive elements of the netCDF variable along the corresponding dimension, a value of 2 selects every other element, etc.). A <code>NULL</code> stride argument is treated as (1, 1, &#8230; , 1).</p>
<dt><i>imap</i></p>
<dd>specifies the mapping between the dimensions of a netCDF variable and the in-memory structure of the internal data array. The elements of the index mapping vector correspond, in order, to the netCDF variable&#8217;s dimensions (<i>imap</i>[0] gives the distance between elements of the internal array corresponding to the most slowly varying dimension of the netCDF variable). Distances between elements are specified in type-independent units of elements (the distance between internal elements that occupy adjacent memory locations is 1 and not the element&#8217;s byte-length as in netCDF 2). A <code>NULL</code> pointer means the memory-resident values have the same structure as the associated netCDF variable.</dl>
<h2>Variable Prefilling</h2>
<p>By default, the netCDF interface sets the values of all newly-defined variables of finite length (i.e. those that do not have an unlimited, dimension) to the type-dependent fill-value associated with each variable. This is done when <code>nc_enddef()</code> is called. The fill-value for a variable may be changed from the default value by defining the attribute `<code>_FillValue</code>&#8216; for the variable. This attribute must have the same type as the variable and be of length one. </p>
<p> Variables with an unlimited dimension are also prefilled, but on an `as needed&#8217; basis. For example, if the first write of such a variable is to position 5, then positions 0 through 4 (and no others) would be set to the fill-value at the same time. </p>
<p> This default prefilling of data values may be disabled by or&#8217;ing the <code>NC_NOFILL</code> flag into the mode parameter of <code>nc_open()</code> or <code>nc_create()</code>, or, by calling the function <code>nc_set_fill()</code> with the argument <code>NC_NOFILL</code>. For variables that do not use the unlimited dimension, this call must be made before <code>nc_enddef()</code>. For variables that use the unlimited dimension, this call may be made at any time. </p>
<p> One can obtain increased performance of the netCDF interface by using this feature, but only at the expense of requiring the application to set every single data value. The performance enhancing behavior of this function is dependent on the particulars of the implementation and dataset format. The flag value controlled by <code>nc_set_fill()</code> is per netCDF ID, not per variable or per write. Allowing this to change affects the degree to which a program can be effectively parallelized. Given all of this, we state that the use of this feature may not be available (or even needed) in future releases. Programmers are cautioned against heavy reliance upon this feature.</p>
<dl>
<dt> <code>int nc_setfill(int </code><i>ncid</i>, int <i>fillmode</i>, int* <i>old_fillemode</i>) </p>
<p> (Corresponds to <code>ncsetfill()</code> in version 2) </p>
<dd>Determines whether or not variable prefilling will be done (see above). The netCDF dataset shall be writable. <i>fillmode</i> is either <code>NC_FILL</code> to enable prefilling (the default) or <code>NC_NOFILL</code> to disable prefilling. This function returns the previous setting in <i>old_fillmode</i>. </p>
<dt></dl>
<h2>Mpp Function Descriptions</h2>
<dd>Additional functions for use on SGI/Cray MPP machines (_CRAYMPP). These are used to set and inquire which PE is the base for MPP for a particular netCDF. These are only relevant when using the SGI/Cray &#8220;global&#8221; Flexible File I/O layer and desire to have only a subset of PEs to open the specific netCDF file. For technical reasons, these functions are available on all platforms. On a platform other than SGI/Cray MPP, it is as if only processor available were processor 0. </p>
<p> To use this feature, you need to specify a communicator group and call <code>glio_group_mpi()</code> or <code>glio_group_shmem()</code> prior to the netCDF <code>nc_open()</code> and <code>nc_create()</code> calls.</p>
<dl>
<dt> <code>int nc__create_mp(const char </code><i>path</i>[], int <i>cmode</i>, size_t <i>initialsize</i>, int <i>pe</i>, size_t* <i>chunksize</i>, int* <i>ncid</i>) </p>
<dd>Like <code>nc__create()</code> but allows the base PE to be set. </p>
<p> The argument <i>pe</i> sets the base PE at creation time. In the MPP environment, <code>nc__create()</code> and <code>nc_create()</code> set the base PE to processor zero by default.</p>
<dt> <code>int nc__open_mp(const char </code><i>path</i>[], int <i>mode</i>, int <i>pe</i>, size_t* <i>chunksize</i>, int* <i>ncid</i>) </p>
<dd>Like <code>nc__open()</code> but allows the base PE to be set. The argument <i>pe</i> sets the base PE at creation time. In the MPP environment, <code>nc__open()</code> and <code>nc_open()</code> set the base PE to processor zero by default.</p>
<dt> <code>int nc_inq_base_pe(int </code><i>ncid</i>, int* <i>pe</i>) </p>
<dd>Inquires of the netCDF dataset which PE is being used as the base for MPP use. This is safe to use at any time.</p>
<dt> <code>int nc_set_base_pe(int </code><i>ncid</i>, int <i>pe</i>) </p>
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
<p><code><a href="/docs/linux/man/1-ncdump/">ncdump</a></code>(1), <code><a href="/docs/linux/man/1-ncgen/">ncgen</a></code>(1), <code><a href="/docs/linux/man/3-netcdf/">netcdf</a></code>(3). <i>netCDF User&#8217;s Guide</i>, published by the Unidata Program Center, University Corporation for Atmospheric Research, located in Boulder, Colorado. NetCDF home page at http:/<a rel="nofollow" href="http://www.unidata.ucar.edu">www.unidata.ucar.edu</a>/netcdf. </p>
