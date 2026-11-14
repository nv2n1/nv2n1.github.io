---
title: "netcdf_f90(3)"
name: "netcdf_f90"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netcdf_f90/"
description: "netcdf – Unidata Network Common Data Form (netCDF) library, version 3 interface"
---

<p>netcdf &#8211; Unidata Network Common Data Form (netCDF) library, version 3 interface</p>
<h2>Synopsis</h2>
<p><code> use netcdf </code></p>
<h3>Most Systems:</h3>
<p>f90 &#8230; -lnetcdf</p>
<h3>CRAY PVP Systems:</h3>
<p>f90 -dp -i64 &#8230; -lnetcdf </p>
<h2>Library Version</h2>
<p>This document describes version 3 of Unidata netCDF data-access interface for the Fortran-90 programming language.</p>
<dl>
<dt> <code>character*80 nf90_inq_libvers()</p>
<dl>
<dd>
<dd>character(len=80) :: nf90_inq_libvers</code></dl>
<p> Returns a string identifying the version of the netCDF library, and when it was built, like: &quot;3.1a of Aug 22 1996 12:57:47 $&quot;.</dl>
<p> The RCS <code><a href="/docs/linux/man/1-ident/">ident</a>(1)</code> command will find a string like &quot;$Id: @(#) netcdf library version 3.1a of Sep 6 1996 15:56:26 $&quot; in the library. The SCCS <code><a href="/docs/linux/man/1-what/">what</a>(1)</code> command will find a string like &quot;netcdf library version 3.1a of Aug 23 1996 16:07:40 $&quot;.</p>
<h2>Routine Descriptions</h2>
<p>All netCDF functions (except <code>nf90_inq_libvers()</code> and <code>nf90_strerror()</code>) return an integer status. This behavior replaces the <code>rcode</code> argument used in previous versions of the library. If this returned status value is not equal to <code>nf90_noerr</code> (zero), it indicates that an error occurred. The possible status values are defined in the module <code>netcdf</code>.</p>
<dl>
<dt> <code>function nf90_strerror(</code><i>ncerr</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncerr
character(len=80) :: nf90_strerror</pre>
<p>Returns a string textual translation of the <i>ncerr</i> value, like &quot;Attribute or variable name contains illegal characters&quot; or &quot;No such file or directory&quot;.</dl>
<dt> <code>function nf90_create(</code><i>path</i>, <i>cmode</i>, <i>ncid</i>)</p>
<dl>
<dd>
<pre><dd>character(len=*), intent(in) :: path
integer, intent(in) :: cmode
integer, optional, intent(in) :: initialsize
integer, optional, intent(inout) :: chunksize
integer, intent(out) :: ncid
integer :: nf90_create</pre>
<p>(Corresponds to <code>nccre()</code> in version 2) </p>
<p> Creates a new netCDF dataset at <i>path</i>, returning a netCDF ID in <i>ncid</i>. The argument <i>cmode</i> may include the bitwise-or of the following flags: <code>nf90_noclobber</code> to protect existing datasets (default silently blows them away), <code>nf90_share</code> for synchronous dataset updates (default is to buffer accesses), and <code>nf90_lock</code> (not yet implemented). When a netCDF dataset is created, is is opened <code>nf90_write</code>. The new netCDF dataset is in define mode. </p>
<p> The optional argument <i>initialsize</i> sets the initial size of the file at creation time. </p>
<p> See <code>nf__open()</code> below for an explanation of the optional <i>chunksize</i> argument.</dl>
<dt> <code>function nf90_open(</code><i>path</i>, <i>mode</i>, <i>ncid</i>, <i>chunksize</i>)</p>
<dl>
<dd>
<pre><dd>character(len=*), intent(in) :: path
integer, intent(in) :: mode
integer, intent(out) :: ncid
integer, optional, intent(inout) :: chunksize
integer :: nf90_open</pre>
<p>(Corresponds to <code>ncopn()</code> in version 2) </p>
<p> Opens a existing netCDF dataset at <i>path</i> returning a netCDF ID in <i>ncid</i>. As of NetCDF version 4.1, and if DAP support was enabled when the library was built, the path may instead specify a DAP URL (refer to the NetCDF user&#8217;s manual for details). </p>
<p> The type of access is described by the <i>mode</i> parameter, which may include the bitwise-or of the following flags: <code>nf90_write</code> for read-write access (default read-only), <code>nf90_share</code> for synchronous dataset updates (default is to buffer accesses), and <code>nf90_lock</code> (not yet implemented). </p>
<p> The optional argument referenced by <i>chunksize</i> controls a space versus time tradeoff, memory allocated in the netcdf library versus number of system calls. Because of internal requirements, the value may not be set to exactly the value requested. The actual value chosen is returned by reference. Using the value <code>nf90_sizehint_default</code> causes the library to choose a default. How the system choses the default depends on the system. On many systems, the &quot;preferred I/O block size&quot; is available from the <code>stat()</code> system call, <code>struct stat</code> member <code>st_blksize</code>. If this is available it is used. Lacking that, twice the system pagesize is used. Lacking a call to discover the system pagesize, we just set default chunksize to 8192. </p>
<p> The chunksize is a property of a given open netcdf descriptor <i>ncid</i>: it is not a persistent property of the netcdf dataset.</dl>
<dt> <code>function nf90_set_fill(</code><i>ncid</i>, <i>fillmode</i>, <i>old_mode</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid, fillmode
integer, intent(out) :: old_mode
integer :: nf90_set_fill</pre>
<p>Sets the fill-mode for a netCDF dataset to optimize writes under some circumstances. The fill-mode argument, <i>fillmode</i>, can be either <code>nf90_fill</code> or <code>nf90_nofill</code>. <code>nf90_fill</code> causes fill-values to be written into non-record variables and into skipped-over records when writing beyond the last valid record. <code>nf90_nofill</code> suspends this behavior. The default behavior corresponds to <code>nf90_fill</code>. </p>
<p> The previous fill-mode value is return in <i>old_mode</i>. </p>
<p> The fill-mode is a property of a given open netcdf descriptor <i>ncid</i>: it is not a persistent property of the netcdf dataset.</dl>
<dt> <code>function nf90_redef(</code><i>ncid</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
integer :: nf90_redef</pre>
<p>(Corresponds to <code>ncredf()</code> in version 2) </p>
<p> Puts an open netCDF dataset into define mode, so dimensions, variables, and attributes can be added or renamed and attributes can be deleted.</dl>
<dt> <code>function nf90_enddef(</code><i>ncid</i>, <i>h_minfree</i>, <i>v_align</i>, <i>v_minfree</i>, <i>r_align</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
integer, optional, intent(in) :: h_minfree, v_align
integer, optional, intent(in) :: v_minfree, r_align
integer :: nf90_enddef</pre>
<p>(Corresponds to <code>ncendf()</code> in version 2) </p>
<p> Takes an open netCDF dataset out of define mode. The changes made to the netCDF dataset while it was in define mode are checked and committed to disk if no problems occurred. Some data values may be written as well, see &quot;VARIABLE PREFILLING&quot; below. After a successful call, variable data can be read or written to the dataset. </p>
<p> The optional arguments are performance tuning parameters. They exposes internals of the netcdf version 1 file format and may not be available on future netcdf implementations. </p>
<p> The current netcdf file format has three sections, the &quot;header&quot; section, the data section for fixed size variables, and the data section for variables which have an unlimited dimension (record variables). The header begins at the beginning of the file. The index (offset) of the beginning of the other two sections is contained in the header. Typically, there is no space between the sections. This causes copying overhead to accrue if one wishes to change the size of the sections, as may happen when changing names of things, text attribute values, adding attributes or adding variables. Also, for buffered i/o, there may be advantages to aligning sections in certain ways. </p>
<p> The minfree parameters allow one to control costs of future calls to <code>nf90_redef()</code>, <code>nf90_enddef()</code> by requesting that <i>minfree</i> bytes be available at the end of the section. The <i>h_minfree</i> parameter sets the pad at the end of the &quot;header&quot; section. The <i>v_minfree</i> parameter sets the pad at the end of the data section for fixed size variables. </p>
<p> The align parameters allow one to set the alignment of the beginning of the corresponding sections. The beginning of the section is rounded up to an index which is a multiple of the align parameter. The flag value <code>nf90_align_chunk</code> tells the library to use the chunksize (see above) as the align parameter. The <i>v_align</i> parameter controls the alignment of the beginning of the data section for fixed size variables. The <i>r_align</i> parameter controls the alignment of the beginning of the data section for variables which have an unlimited dimension (record variables). </p>
<p> The file format requires mod 4 alignment, so the align parameters are silently rounded up to multiples of 4. The usual call, <code>nf90_enddef(</code><i>ncid</i>) is equivalent to <code>nf__enddef(</code><i>ncid</i>, 0, 4, 0, 4). </p>
<p> The file format does not contain a &quot;record size&quot; value, this is calculated from the sizes of the record variables. This unfortunate fact prevents us from providing minfree and alignment control of the &quot;records&quot; in a netcdf file. If you add a variable which has an unlimited dimension, the third section will always be copied with the new variable added.</dl>
<dt> <code>function nf90_sync(</code><i>ncid</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
integer :: nf90_sync</pre>
<p>(Corresponds to <code>ncsnc()</code> in version 2) </p>
<p> Unless the <code>nf90_share</code> bit is set in <code>nf90_open()</code> or <code>nf90_create()</code>, accesses to the underlying netCDF dataset are buffered by the library. This function synchronizes the state of the underlying dataset and the library. This is done automatically by <code>nf90_close()</code> and <code>nf90_enddef()</code>.</dl>
<dt> <code>function nf90_abort(</code><i>ncid</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
integer :: nf90_abort</pre>
<p>(Corresponds to <code>ncabor()</code> in version 2) </p>
<p> You don&#8217;t need to call this function. This function is called automatically by <code>nf90_close()</code> if the netCDF dataset was in define mode and something goes wrong with the commit. If the netCDF dataset isn&#8217;t in define mode, then this function is equivalent to <code>nf90_close()</code>. If it is called after <code>nf90_redef()</code>, but before <code>nf90_enddef()</code>, the new definitions are not committed and the dataset is closed. If it is called after <code>nf90_create()</code> but before <code>nf90_enddef()</code>, the dataset disappears.</dl>
<dt> <code>function nf90_close(</code><i>ncid</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
integer :: nf90_close</pre>
<p>(Corresponds to <code>ncclos()</code> in version 2) </p>
<p> Closes an open netCDF dataset. If the dataset is in define mode, <code>nf90_enddef()</code> will be called before closing. After a dataset is closed, its ID may be reassigned to another dataset.</dl>
<dt> <code>function nf90_inquire(</code><i>ncid</i>, <i>ndims</i>, <i>nvars</i>, <i>natts</i>, <i>unlimdimid</i>, <i>nformat</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
integer, optional, intent(out) :: ndims, nvars
integer, optional, intent(out) :: natts, unlimdimid
integer, optional, intent(out) :: nformat
integer :: nf90_inquire</pre>
<p>Inquire about an open netCDF dataset. <i>ncid</i> is the netCDF ID of the open dataset. Upon successful return, <i>ndims</i> will contain the number of dimensions defined for this netCDF dataset, <i>nvars</i> will contain the number of variables, <i>natts</i> will contain the number of attributes, and <i>unlimdimid</i> will contain the dimension ID of the unlimited dimension if one exists, or 0 otherwise. <i>nformat</i> will contain the format version number, rarely needed because the library detects the format version and behaves appropriately.</dl>
<dt> <code>function nf90_def_dim(</code><i>ncid</i>, <i>name</i>, <i>len</i>, <i>dimid</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
character(len=*), intent(in) :: name
integer, intent(in) :: len
integer, intent(out) :: dimid
integer :: nf90_def_dim</pre>
<p>(Corresponds to <code>ncddef()</code> in version 2) </p>
<p> Adds a new dimension to an open netCDF dataset, which must be in define mode. <i>name</i> is the dimension name. <i>len</i> is the size of the new dimension or <code>nf90_unlimited</code> to define the unlimited dimension. On return, <i>dimid</i> will contain the dimension ID of the newly created dimension.</dl>
<dt> <code>function nf90_inq_dimid(</code><i>ncid</i>, <i>name</i>, <i>dimid</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
character(len=*), intent(in) :: name
integer, intent(out) :: dimid
integer :: nf90_inq_dimid</pre>
<p>(Corresponds to <code>ncdid()</code> in version 2) </p>
<p> Given an open netCDF dataset and dimension name, returns the dimension ID of the netCDF dimension in <i>dimid</i>.</dl>
<dt> <code>function nf90_inquire_dimension(</code><i>ncid</i>, <i>dimid</i>, <i>name</i>, <i>len</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid, dimid
character(len=*), optional, intent(out) :: name
integer, optional, intent(out) :: len
integer :: nf90_inquire_dimension</pre>
<p>Inquire about a dimension. <i>name</i> should be big enough (<code>nf90_max_name</code>) to hold the dimension name as the name will be copied into your storage. The length return parameter, <i>len</i> will contain the size of the dimension. For the unlimited dimension, the returned length is the current maximum value used for writing into any of the variables which use the dimension.</dl>
<dt> <code>function nf90_rename_dim(</code><i>ncid</i>, <i>dimid</i>, <i>name</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
character(len=*), intent(in) :: name
integer, intent(in) :: dimid
integer :: nf90_rename_dim</pre>
<p>(Corresponds to <code>ncdren()</code> in version 2) </p>
<p> Renames an existing dimension in an open netCDF dataset. If the new name is longer than the old name, the netCDF dataset must be in define mode. You cannot rename a dimension to have the same name as another dimension.</dl>
<dt> <code>function nf90_def_var(</code><i>ncid</i>, <i>name</i>, <i>xtype</i>, <i>dimids</i>, <i>varid</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
character(len=*), intent(in) :: name
integer, intent(in) :: xtype
integer, optional, dimension(:), intent(in) :: dimids
integer :: nf90_def_var</pre>
<p>(Corresponds to <code>ncvdef()</code> in version 2) </p>
<p> Adds a new variable to a netCDF dataset. The netCDF must be in define mode. <i>name</i> will be the name of the netCDF variable. <i>xtype</i> is the external, netCDF type of the variable and should be one of <code>nf90_byte</code>, <code>nf90_char</code>, <code>nf90_short</code>, <code>nf90_int</code>, <code>nf90_float</code>, or <code>nf90_double</code>, The optional <i>dimids</i> argument contains the dimension ID-s of the domain of the netCDF variable and, consequently, determines the rank of the created variable: if <i>dimids</i> is omitted, then the netCDF variable will be a scalar; if <i>dimids</i> is a scalar, then the netCDF variable will be 1 dimensional; and if <i>dimids</i> is a vector, then the netCDF variable will have rank equal to the number of elements in <i>dimids</i>. <i>varid</i> will be set to the netCDF variable ID.</dl>
<dt> <code>function nf90_inq_varid(</code><i>ncid</i>, <i>name</i>, <i>varid</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid
character(len=*), intent(in) :: name
integer, intent(out) :: varid
integer :: nf90_inq_varid</pre>
<p>(Corresponds to <code>ncvid()</code> in version 2) </p>
<p> Returns the ID of a netCDF variable in <i>varid</i> given an open netCDF dataset and the name of the variable.</dl>
<dt> <code>function nf90_inquire_variable(</code><i>ncid</i>, <i>varid</i>, <i>name</i>, <i>xtype</i>, <i>ndims</i>, <i>dimids</i>, <i>natts</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid, varid
character(len=*), optional, intent(out) :: name
integer, optional, intent(out) :: xtype, ndims
integer, dimension(*), optional, intent(out) :: dimids
integer, optional, intent(out) :: natts
integer :: nf90_inquire_variable</pre>
<p>Inquire about a netCDF variable in an open netCDF dataset, given its variable ID. On return, <i>name</i> will contain the name of the variable and should be capacious enough (<code>nf90_max_name</code>). <i>xtype</i> will contain the external, netCDF type of the variable. <i>ndims</i> will contain the dimensionality of the netCDF variable: if the variable is a scalar, then size(<i>ndims</i>) will be zero; otherwise, size(<i>ndims</i>) will be the rank of the variable and <i>ndims</i> will contain the dimension ID-s of the netCDF dimensions that constitute the domain of the variable. <i>natts</i> will contain the number of attributes associated with the netCDF variable.</dl>
<dt> <code>function nf90_rename_var(</code><i>ncid</i>, <i>varid</i>, <i>name</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent9in) :: ncid, varid
character(len=*), intent(in) :: newname
integer :: nf90_rename_var</pre>
<p>(Corresponds to <code>ncvren()</code> in version 2) </p>
<p> Changes the name of a netCDF variable. If the new name is longer than the old name, the netCDF must be in define mode. You cannot rename a variable to have the name of any existing variable.</dl>
<dt> <code>function nf90_put_var(</code><i>ncid</i>, <i>varid</i>, <i>values</i>, <i>start</i>, <i>stride</i>, <i>imap</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid, varid
&lt;&lt;whatever&gt;&gt;, intent(in) :: values
integer, dimension(:), optional, intent(in) :: start
integer, dimension(:), optional, intent(in) :: stride
integer, dimension(:), optional, intent(in) :: imap
integer :: nf90_put_var</pre>
<p>(Replaces <code>ncvpt()</code> in version 2) </p>
<p> Writes a value or values to a netCDF variable. The netCDF dataset must be open and in data mode. <i>values</i> contains the value(s) what will be written to the netCDF variable identified by <i>ncid</i> and <i>varid</i>; it may be a scalar or an array and must be of type <code>character</code>, <code>integer(kind=OneByteInt)</code>, <code>integer(kind=TwoByteInt)</code>, <code>integer(kind=FourByteInt)</code>, <code>integer(kind=EightByteInt)</code>, <code>real(kind=FourByteReal)</code>, or <code>real(kind=EightByteReal)</code>. All values are converted to the external type of the netCDF variable, if possible; otherwise, an <code>nf90_erange</code> error is returned. The optional argument <i>start</i> specifies the starting index in the netCDF variable for writing for each dimension of the netCDF variable. The optional argument <i>stride</i> specifies the sampling stride (the interval between accessed values in the netCDF variable) for each dimension of the netCDF variable (see COMMON ARGUMENT DESCRIPTIONS below). The optional argument <i>imap</i> specifies the in-memory arrangement of the data values (see COMMON ARGUMENT DESCRIPTIONS below).</dl>
<dt> <code>function nf90_get_var(</code><i>ncid</i>, <i>varid</i>, <i>values</i>, <i>start</i>, <i>stride</i>, <i>imap</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid, varid
&lt;&lt;whatever&gt;&gt;, intent(out) :: values
integer, dimension(:), optional, intent(in) :: start
integer, dimension(:), optional, intent(in) :: stride
integer, dimension(:), optional, intent(in) :: imap
integer :: nf90_get_var</pre>
<p>(Replaces <code>ncvgt()</code> in version 2) </p>
<p> Reads a value or values from a netCDF variable. The netCDF dataset must be open and in data mode. <i>values</i> will receive the value(s) what will be read from the netCDF<br />
&nbsp;<wbr>variable identified by <i>ncid</i> and <i>varid</i>; it may be a scalar or an array and must be of type <code>character</code>, <code>integer(kind=OneByteInt)</code>, <code>integer(kind=TwoByteInt)</code>, <code>integer(kind=FourByteInt)</code>, <code>integer(kind=EightByteInt)</code>, <code>real(kind=FourByteReal)</code>, or <code>real(kind=EightByteReal)</code>. All values are converted from the external type of the netCDF variable, if possible; otherwise, an <code>nf90_erange</code> error is returned. The optional argument <i>start</i> specifies the starting index in the netCDF variable for reading for each dimension of the netCDF variable. The optional argument <i>stride</i> specifies the sampling stride (the interval between accessed values in the netCDF variable) for each dimension of the netCDF variable (see COMMON ARGUMENT DESCRIPTIONS below). The optional argument <i>imap</i> specifies the in-memory arrangement of the data values (see COMMON ARGUMENT DESCRIPTIONS below).</dl>
<dt> <code>function nf90_inquire_attribute(</code><i>ncid</i>, <i>varid</i>, <i>name</i>, <i>xtype</i>, <i>len</i>, <i>attnum</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid, varid
character(len=*), intent(in) :: name
integer, optional, intent(out) :: xtype, len, attnum
integer :: nf90_inquire_attribute</pre>
<p>Inquires about the netCDF attribute named <i>name</i>, of variable <i>varid</i>, in the open netCDF dataset <i>ncid</i>. <i>xtype</i> will contain the external, netCDF type of the variable. <i>len</i> will contain the number of elements in the attribute. <i>attnum</i> will contain the attribute number.</dl>
<dt> <code>function nf90_inq_attname(</code><i>ncid</i>, <i>varid</i>, <i>attnum</i>, <i>name</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid, varid, attnum
character(len=*), intent(out) :: name
integer :: nf90_inq_attname</pre>
<p>(Corresponds to <code>ncanam()</code> in version 2) </p>
<p> Gets the name of an attribute, given its variable ID and attribute number. This function is useful in generic applications that need to get the names of all the attributes associated with a variable because attributes are accessed by name rather than number in all other attribute functions (the number of an attribute is more volatile than the name because it can change when other attributes of the same variable are deleted). The attributes for each variable are numbered from 1 (the first attribute) to <i>natts</i>, where <i>natts</i> is the number of attributes for the variable, as returned from a call to <code>nf90_inquire_variable()</code>.</dl>
<dt> <code>function nf90_put_att(</code><i>ncid</i>, <i>varid</i>, <i>name</i>, <i>values</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid, varid
character(len=*), intent(in) :: name
&lt;&lt;whatever&gt;&gt;, intent(in) :: values
integer :: nf90_put_att</pre>
<p>Unlike variables, attributes do not have separate functions for defining and writing values. This function defines a new attribute with a value or changes the value of an existing attribute. If the attribute is new, or if the space required to store the attribute value is greater than before, the netCDF dataset must be in define mode. <i>values</i> contains the attribute values to be written; it may be a scalar or a vector and must be of type <code>character</code>, <code>integer(kind=OneByteInt)</code>, <code>integer(kind=TwoByteInt)</code>, <code>integer(kind=FourByteInt)</code>, <code>integer(kind=EightByteInt)</code>, <code>real(kind=FourByteReal)</code>, or <code>real(kind=EightByteReal)</code>.</dl>
<dt> <code>function nf90_get_att(</code><i>ncid</i>, <i>varid</i>, <i>name</i>,</p>
<dd>fIvalues)</p>
<dl>
<dd>
<pre>integer, intent(in) :: ncid, varid
character(len=*), intent(in) :: name
&lt;&lt;whatever&gt;&gt;, intent(out) :: values
integer :: nf90_get_att</pre>
<p>(Replaces <code>ncagt()</code> in version 2) </p>
<p> Gets the value(s) of a netCDF attribute, given its variable ID and name. The values are returned in <i>values</i>, which must be of type <code>character</code>, <code>integer(kind=OneByteInt)</code>, <code>integer(kind=TwoByteInt)</code>, <code>integer(kind=FourByteInt)</code>, <code>integer(kind=EightByteInt)</code>, <code>real(kind=FourByteReal)</code>, or <code>real(kind=EightByteReal)</code>. Converts from the external type to the type of the receiving variable, if possible; otherwise returns an <code>nf90_erange</code> error. All values of the attribute are returned, so you must allocate enough space to hold them. If you don&#8217;t know how much space to reserve, call <code>nf90_inquire_attribute()</code> first to find out the length of the attribute.</dl>
<dt> <code>function nf90_copy_att(</code><i>ncid_in</i>, <i>varid_in</i>, <i>name</i>, <i>ncid_out</i>, <i>varid_out</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid_in, varid_in
character(len=*), intent(in) :: name
integer, intent(in) :: ncid_out, varid_out
integer :: nf90_copy_att</pre>
<p>(Corresponds to <code>ncacpy()</code> in version 2) </p>
<p> Copies an attribute from one netCDF dataset to another. It can also be used to copy an attribute from one variable to another within the same netCDF dataset. <i>ncid_in</i> is the netCDF ID of an input netCDF dataset from which the attribute will be copied. <i>varid_in</i> is the ID of the variable in the input netCDF dataset from which the attribute will be copied, or <code>nf90_global</code> for a global attribute. <i>name</i> is the name of the attribute in the input netCDF dataset to be copied. <i>ncid_out</i> is the netCDF ID of the output netCDF dataset to which the attribute will be copied. It is permissible for the input and output netCDF ID&#8217;s to be the same. The output netCDF dataset should be in define mode if the attribute to be copied does not already exist for the target variable, or if it would cause an existing target attribute to grow. <i>varid_out</i> is the ID of the variable in the output netCDF dataset to which the attribute will be copied, or <code>nf90_global</code> to copy to a global attribute.</dl>
<dt> <code>function nf90_rename_att(</code><i>ncid</i>, <i>varid</i>, <i>name</i>, <i>newname</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid, varid
character(len=*), intent(in) :: name, newname
integer :: nf90_rename_att</pre>
<p>(Corresponds to <code>ncaren()</code> </p>
<p> Changes the name of an attribute. If the new name is longer than the original name, the netCDF must be in define mode. You cannot rename an attribute to have the same name as another attribute of the same variable. <i>name</i> is the original attribute name. <i>newname</i> is the new name to be assigned to the specified attribute. If the new name is longer than the old name, the netCDF dataset must be in define mode.</p>
<dl>
<dt> <code>function nf90_del_att(</code><i>ncid</i>, <i>varid</i>, <i>name</i>)</p>
<dl>
<dd>
<pre><dd>integer, intent(in) :: ncid, varid
character(len=*), intent(in) :: name
integer :: nf90_del_att</pre>
<p>(Corresponds to <code>ncadel()</code> in version 2) </p>
<p> Deletes an attribute from a netCDF dataset. The dataset must be in define mode.</dl>
</dl>
</dl>
</dl>
<h2>Common Argument Descriptions</h2>
<p>In this section we define some common arguments which are used in the &quot;FUNCTION DESCRIPTIONS&quot; section.</p>
<dl>
<dt>integer <i>ncid</i></p>
<dd>is the netCDF ID returned from a previous, successful call to <code>nf90_open()</code> or <code>nf90_create()</code></p>
<dt>character(len=*) <i>name</i></p>
<dd>is the name of a dimension, variable, or attribute. It shall begin with an alphabetic character, followed by zero or more alphanumeric characters including the underscore (`_&#8217;) or hyphen (`-&#8216;). Case is significant. The maximum allowable number of characters is <code>nf90_max_name</code>. Names that begin with an underscore (`_&#8217;) are reserved for use by the netCDF interface.</p>
<dt>integer <i>xtype</i></p>
<dd>specifies the external data type of a netCDF variable or attribute and is one of the following: <code>nf90_byte</code>, <code>nf90_char</code>, <code>nf90_short</code>, <code>nf90_int</code>, <code>nf90_float</code>, or <code>nf90_double</code>. These are used to specify 8-bit integers, characters, 16-bit integers, 32-bit integers, 32-bit IEEE floating point numbers, and 64-bit IEEE floating-point numbers, respectively. </p>
<dt>integer <i>dimids</i></p>
<dd>is a vector of dimension ID&#8217;s and defines the shape of a netCDF variable. The size of the vector shall be greater than or equal to the rank (i.e. the number of dimensions) of the variable (<i>ndims</i>). The vector shall be ordered by the speed with which a dimension varies: <i><a href="/docs/linux/man/1-dimids/">dimids</a></i>(1) shall be the dimension ID of the most rapidly varying dimension and <i>dimids</i>(<i>ndims</i>) shall be the dimension ID of the most slowly varying dimension. The maximum possible number of dimensions for a variable is given by the symbolic constant <code>nf90_max_var_dims</code>.</p>
<dt>integer <i>dimid</i></p>
<dd>is the ID of a netCDF dimension. netCDF dimension ID&#8217;s are allocated sequentially from the positive integers beginning with 1.</p>
<dt>integer <i>ndims</i></p>
<dd>is either the total number of dimensions in a netCDF dataset or the rank (i.e. the number of dimensions) of a netCDF variable. The value shall not be negative or greater than the symbolic constant <code>nf90_max_var_dims</code>.</p>
<dt>integer <i>varid</i></p>
<dd>is the ID of a netCDF variable or (for the attribute-access functions) the symbolic constant <code>nf90_global</code>, which is used to reference global attributes. netCDF variable ID&#8217;s are allocated sequentially from the positive integers beginning with 1.</p>
<dt>integer <i>natts</i></p>
<dd>is the number of global attributes in a netCDF dataset for the <code>nf90_inquire()</code> function or the number of attributes associated with a netCDF variable for the <code>nf90_varinq()</code> function.</p>
<dt>integer <i>start</i></p>
<dd>specifies the starting point for accessing a netCDF variable&#8217;s data values in terms of the indicial coordinates of the corner of the array section. The indices start at 1; thus, the first data value of a variable is (1, 1, &#8230;, 1). The size of the vector shall be at least the rank of the associated netCDF variable and its elements shall correspond, in order, to the variable&#8217;s dimensions.</p>
<dt>integer <i>stride</i></p>
<dd>specifies the sampling interval along each dimension of the netCDF variable. The elements of the stride vector correspond, in order, to the netCDF variable&#8217;s dimensions (<i><a href="/docs/linux/man/1-stride/">stride</a></i>(1)) gives the sampling interval along the most rapidly varying dimension of the netCDF variable). Sampling intervals are specified in type-independent units of elements (a value of 1 selects consecutive elements of the netCDF variable along the corresponding dimension, a value of 2 selects every other element, etc.). </p>
<dt><i>imap</i></p>
<dd>specifies the mapping between the dimensions of a netCDF variable and the in-memory structure of the internal data array. The elements of the index mapping vector correspond, in order, to the netCDF variable&#8217;s dimensions (<i><a href="/docs/linux/man/1-imap/">imap</a></i>(1) gives the distance between elements of the internal array corresponding to the most rapidly varying dimension of the netCDF variable). Distances between elements are specified in type-independent units of elements (the distance between internal elements that occupy adjacent memory locations is 1 and not the element&#8217;s byte-length as in netCDF 2). </p>
</dl>
<h2>Variable Prefilling</h2>
<p>By default, the netCDF interface sets the values of all newly-defined variables of finite length (i.e. those that do not have an unlimited, dimension) to the type-dependent fill-value associated with each variable. This is done when <code>nf90_enddef()</code> is called. The fill-value for a variable may be changed from the default value by defining the attribute `<code>_FillValue</code>&#8216; for the variable. This attribute must have the same type as the variable and be of length one. </p>
<p> Variables with an unlimited dimension are also prefilled, but on an `as needed&#8217; basis. For example, if the first write of such a variable is to position 5, then positions 1 through 4 (and no others) would be set to the fill-value at the same time. </p>
<p> This default prefilling of data values may be disabled by or&#8217;ing the <code>nf90_nofill</code> flag into the mode parameter of <code>nf90_open()</code> or <code>nf90_create()</code>, or, by calling the function <code>nf90_set_fill()</code> with the argument <code>nf90_nofill</code>. For variables that do not use the unlimited dimension, this call must be made before <code>nf90_enddef()</code>. For variables that use the unlimited dimension, this call may be made at any time. </p>
<p> One can obtain increased performance of the netCDF interface by using this feature, but only at the expense of requiring the application to set every single data value. The performance enhancing behavior of this function is dependent on the particulars of the implementation and dataset format. The flag value controlled by <code>nf90_set_fill()</code> is per netCDF ID, not per variable or per write. Allowing this to change affects the degree to which a program can be effectively parallelized. Given all of this, we state that the use of this feature may not be available (or even needed) in future releases. Programmers are cautioned against heavy reliance upon this feature.</p>
<h2>Mpp Function Descriptions</h2>
<p>Additional functions for use on SGI/Cray MPP machines (_CRAYMPP). These are used to set and inquire which PE is the base for MPP for a particular netCDF. These are only relevant when using the SGI/Cray &#8220;global&#8221; Flexible File I/O layer and desire to have only a subset of PEs to open the specific netCDF file. For technical reasons, these functions are available on all platforms. On a platform other than SGI/Cray MPP, it is as if only processor available were processor 0. </p>
<p> To use this feature, you need to specify a communicator group and call <code>glio_group_mpi()</code> or <code>glio_group_shmem()</code> prior to the netCDF <code>nf90_open()</code> and <code>nf90_create()</code> calls. </p>
<p> Note that the routines described below are Fortran-77 routines rather than Fortran-90 routines (they have an &quot;nf_&quot; prefix rather than an &quot;nf90_&quot; prefix).</p>
<dl>
<dt> <code>integer function nf__create_mp(character*(*) </code><i>path</i>, integer <i>cmode</i>, integer <i>initialsize</i>, integer <i>pe</i>, integer <i>chunksize</i>, integer <i>ncid</i>) </p>
<dd>Like <code>nf__create()</code> but allows the base PE to be set. </p>
<p> The argument <i>pe</i> sets the base PE at creation time. In the MPP environment, <code>nf__create()</code> and <code>nf90_create()</code> set the base PE to processor zero by default.</p>
<dt> <code>integer function nf__open_mp(character*(*) </code><i>path</i>, integer <i>mode</i>, integer <i>pe</i>, integer <i>chunksize</i>, integer <i>ncid</i>) </p>
<dd>Like <code>nf__open()</code> but allows the base PE to be set. The argument <i>pe</i> sets the base PE at creation time. In the MPP environment, <code>nf__open()</code> and <code>nf90_open()</code> set the base PE to processor zero by default.</p>
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
<p><code><a href="/docs/linux/man/1-ncdump/">ncdump</a></code>(1), <code><a href="/docs/linux/man/1-ncgen/">ncgen</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/3f-netcdf/">netcdf</a></code>(3f). <i>netCDF User&#8217;s Guide</i>, published by the Unidata Program Center, University Corporation for Atmospheric Research, located in Boulder, Colorado. </p>
