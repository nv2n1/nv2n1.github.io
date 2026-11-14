---
title: "netcdf-2(3)"
name: "netcdf-2"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netcdf-2/"
description: "netcdf – Unidata Network Common Data Form (netCDF-2) library"
---

<p>netcdf &#8211; Unidata Network Common Data Form (netCDF-2) library</p>
<h2>Warning</h2>
<p>The interface described here is obsolete, but included because the perl module still use it.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netcdf.h&gt;

int nccreate(const char* path, int cmode)

int ncopen(const char* path, int mode)

int ncredef(int ncid)

int ncsetfill(int ncid, int fillmode)

int ncendef(int ncid)

int ncclose(int ncid)

int ncinquire(int ncid, int* ndims, int* nvars, int* natts, int* recdim)

int ncsync(int ncid)

int ncabort(int ncid)

int ncdimdef(int ncid, const char* name, long length)

int ncdimid(int ncid, const char* name)

int ncdiminq(int ncid, int dimid, char* name, long* length)

int ncdimrename(int ncid, int dimid, const char* name)

int ncvardef(int ncid, const char* name, nc_type datatype, int ndims,
const int dimids[])

int ncvarid(int ncid, const char* name)

int ncvarinq(int ncid, int varid, char* name, nc_type* datatype, int* ndims,
int dimids[], int* natts)

int ncvarput1(int ncid, int varid, const long coords[], const void* value)

int ncvarget1(int ncid, int varid, const long coords[], void* value)

int ncvarput(int ncid, int varid, const long start[], const long count[],
const void* value)

int ncvarget(int ncid, int varid, const long start[], const long count[],
void* value)

int ncvarputg(int ncid, int varid, const long start[], const long count[],
const long stride[], const long imap[], const void* value)

int ncvargetg(int ncid, int varid, const long start[], const long count[],
const long stride[], const long imap[], void* value)

int ncrecput(int ncid, long recnum, void* const valuep[])

int ncrecget(int ncid, long recnum, void* valuep[])

int ncrecinq(int ncid, int* nrvars, int rvarids[], long rsizes[])

int ncvarrename(int ncid, int varid, const char* name)

int ncattput(int ncid, int varid, const char* name, nc_type datatype,
int len, const void* value)

int ncattinq(int ncid, int varid, const char* name, nc_type* datatype,
int* len)

int ncattget(int ncid, int varid, const char* name, void* value)

int ncattcopy(int inncid, int invar, const char* name, int outncid,
int outvar)

int ncattname(int ncid, int varid, int attnum, char* name)

int ncattrename(int ncid, int varid, const char* name, const char* newname)

int ncattdel(int ncid, int varid, const char* name)

int nctypelen(nc_type datatype)</code></pre>
<h2>Function Descriptions</h2>
<p>These routines implement the Unidata netCDF data-access interface for the C programming language. Only those arguments which are unique to the function being described are documented in this section. See the section &quot;COMMON ARGUMENT DESCRIPTIONS&quot; for descriptions of the other arguments.</p>
<dl>
<dt> <code>int nccreate(const char* </code><i>path</i><code>, int </code><i>cmode</i><code>)</code> </p>
<dd>Creates the new netCDF file, returning a netCDF ID that can subsequently be used to refer to the netCDF file. The new netCDF file is placed in define mode. The mode parameter, <i>cmode</i>, should be either <code>NC_CLOBBER</code> or <code>NC_NOCLOBBER</code>. <code>NC_CLOBBER</code> means that even if the file already exists, you want to create a new file with the same name, erasing the old file&#8217;s contents. <code>NC_NOCLOBBER</code> means you want to create a new netCDF file only if the given file name does not refer to a file that already exists. If an error occurs, this function returns -1.</p>
<dt> <code>int ncopen(const char* </code><i>path</i><code>, int </code><i>mode</i><code>)</code> </p>
<dd>Opens the existing netCDF file for access. The mode parameter, <i>mode</i>, should be either <code>NC_WRITE</code>, to open the file for writing, or <code>NC_NOWRITE</code>, to open the file read-only. &quot;Writing&quot; means any kind of change to the file, including appending or changing data, adding or renaming dimensions, variables, or attributes, or deleting attributes. If an error occurs, this function returns -1.</p>
<dt> <code>int ncredef(int </code><i>ncid</i><code>)</code> </p>
<dd>Puts an open netCDF file into define mode, so dimensions, variables, and attributes can be added or renamed and attributes can be deleted. If an error occurs, this function returns -1.</p>
<dt> <code>int ncsetfill(int </code><i>ncid</i><code>, int </code><i>fillmode</i><code>)</code> </p>
<dd>Determines whether or not variable prefilling will be done (see <code>VARIABLE PREFILLING</code> below). The netCDF file shall be writable. <i>fillmode</i> is either <code>NC_FILL</code> to enable prefilling (the default) or <code>NC_NOFILL</code> to disable prefilling. This function returns the previous setting or -1 if an error occurs.</p>
<dt> <code>int ncendef(int </code><i>ncid</i><code>)</code> </p>
<dd>Takes an open netCDF file out of define mode. The changes made to the netCDF file while it was in define mode are checked and committed to disk if no problems occurred. In particular, non-record variables are filled with their fill-values unless <code>ncsetfill()</code> has been called with the argument <code>NC_NOFILL</code>. The netCDF file is then placed in data mode, so that variable data can be read or written. If an error occurs, this function returns -1.</p>
<dt> <code>int ncclose(int </code><i>ncid</i><code>)</code> </p>
<dd>Closes an open netCDF file. If the file is in define mode, <code>ncendef()</code> will be called before closing. (In this case, if <code>ncendef()</code> returns an error, <code>ncabort()</code> will automatically be called to restore the file to the consistent state before define mode was last entered.) After an open netCDF file is closed, its netCDF ID will be reassigned to the next netCDF file that is opened or created. If an error occurs, this function returns -1.</p>
<dt> <code>int ncinquire(int </code><i>ncid</i><code>, int* </code><i>ndims</i><code>, int* </code><i>nvars</i><code>, int* </code><i>natts</i><code>, int* </code><i>recdim)</i> </p>
<dd>Returns information about an open netCDF file. Upon successful return, <i>ndims</i> will contain the number of dimensions defined for this netCDF file, <i>nvars</i> will contain the number of variables, <i>natts</i> will contain the number of attributes, and <i>recdim</i> will contain the ID of the unlimited dimension if one exists, or -1 otherwise. If any of the return parameters is a <code>NULL</code> pointer, then the corresponding information will not be returned; hence, no space need be allocated for it. If an error occurs, this function returns -1.</p>
<dt> <code>int ncsync(int </code><i>ncid</i><code>)</code> </p>
<dd>Updates a writable netCDF file. The netCDF file must be in data mode. A netCDF file in define mode is synchronized to disk only when <code>ncendef()</code> is called. It can be expensive in computer resources to always synchronize to disk after every write of variable data or change of an attribute value. There are two reasons you might want to synchronize after writes: 1) to minimize data loss in case of abnormal termination; and 2) to make data available to other processes for reading immediately after it is written. Data is automatically synchronized to disk when a netCDF file is closed, or whenever you leave define mode. If an error occurs, this function returns -1.</p>
<dt> <code>int ncabort(int </code><i>ncid</i><code>)</code> </p>
<dd>Closes or deletes a netCDF file. If the netCDF file isn&#8217;t in define mode, then the file is closed. If the file is being created and is still in define mode, the file is deleted. If define mode was entered by a call to <code>ncredef()</code>, the netCDF file is restored to its state before definition mode was entered and the file is closed. The main reason for calling <code>ncabort()</code> is to restore the netCDF to a known consistent state in case anything goes wrong during the definition of new dimensions, variables, or attributes. This function is called automatically if <code>ncclose()</code> is called from define mode and the call to leave define mode before closing fails. If an error occurs, this function returns -1.</p>
<dt> <code>int ncdimdef(int </code><i>ncid</i><code>, const char* </code><i>name</i><code>, long </code><i>length</i><code>)</code> </p>
<dd>Adds a new dimension to an open netCDF file, which must be in define mode. <i>name</i> is the dimension name. If an error occurs, this function returns -1.</p>
<dt> <code>int ncdimid(int </code><i>ncid</i><code>, const char* </code><i>name</i><code>)</code> </p>
<dd>Returns the ID of a netCDF dimension, given the name of the dimension. If an error occurs, this function returns -1.</p>
<dt> <code>int ncdiminq(int </code><i>ncid</i><code>, int </code><i>dimid</i><code>, char* </code><i>name</i><code>, long*&nbsp;<wbr></code><i>size</i><code>)</code> </p>
<dd>Returns the name and size of a dimension, given its ID. If either the <i>name</i> parameter or <i>size</i> parameter is a <code>NULL</code> pointer, the associated information will not be returned, so no space needs to be allocated. For the unlimited dimension, the returned size is the current maximum value used for writing any record variables, (i.e. the maximum record number). If an error occurs, this function returns -1.</p>
<dt> <code>int ncdimrename(int </code><i>ncid</i><code>, int </code><i>dimid</i><code>, const char* </code><i>name</i><code>)</code> </p>
<dd>Renames an existing dimension in an open netCDF file. If the new name is longer than the old name, the netCDF must be in define mode. You cannot rename a dimension to have the same name as another dimension. If an error occurs, this function returns -1.</p>
<dt> <code>int ncvardef(int </code><i>ncid</i><code>, const char* </code><i>name</i><code>, nc_type </code><i>datatype</i><code>,</p>
<dd>int </code><i>ndims</i><code>, const int </code><i>dimids[]</i><code>)</code> </p>
<p> Adds a new variable to an open netCDF file in define mode. It returns a netCDF variable ID. If an error occurs, this function returns -1.</p>
<dt> <code>int ncvarid(int </code><i>ncid</i><code>, const char* </code><i>name</i><code>)</code> </p>
<dd>Returns the ID of a netCDF variable, given its name. If an error occurs, this function returns -1.</p>
<dt> <code>int ncvarinq(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, char* </code><i>name</i><code>,</p>
<dd>nc_type* </code><i>datatype</i><code>, int* </code><i>ndims</i><code>, int </code><i>dimids[]</i><code>, int* </code><i>natts)</i> </p>
<p> Returns information about a netCDF variable, given its ID. If any of the return parameters (<i>name</i>, <i>datatype</i>, <i>ndims, dimids, or natts</i>) is a <code>NULL</code> pointer, then the corresponding information will not be returned; hence, no space need be allocated for it. If an error occurs, this function returns -1.</p>
<dt> <code>int ncvarput1(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const long </code><i>coords[]</i><code>,</p>
<dd>const void* </code><i>value</i><code>)</code> </p>
<p> Puts a single data value into a variable of an open netCDF file that is in data mode. If an error occurs, this function returns -1.</p>
<dt> <code>int ncvarget1(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const long </code><i>coords[]</i><code>,</p>
<dd>void* </code><i>value</i><code>)</code> </p>
<p> Gets a single data value from a variable of an open netCDF file that is in data mode. If an error occurs, this function returns -1.</p>
<dt> <code>int ncvarput(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const long </code><i>start[]</i><code>,</p>
<dd>const long </code><i>count[]</i><code>, const void* </code><i>value</i><code>)</code> </p>
<p> Writes a hyperslab of values into a netCDF variable of an open netCDF file, which must be in data mode. If an error occurs, this function returns -1.</p>
<dt> <code>int ncvarget(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const long </code><i>start[]</i><code>,</p>
<dd>const long </code><i>count[]</i><code>, void* </code><i>value</i><code>)</code> </p>
<p> Reads a hyperslab of values from a netCDF variable of an open netCDF file, which must be in data mode. If an error occurs, this function returns -1.</p>
<dt> <code>int ncvarputg(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const long </code><i>start[]</i><code>,</p>
<dd>const long </code><i>count[]</i><code>, const long </code><i>stride[]</i><code>, const long </code><i>imap[]</i><code>, const void* </code><i>value</i><code>)</code> </p>
<p> Writes a general hyperslab of values into a netCDF variable of an open netCDF file, which must be in data mode. The locations of the memory-resident data values may be arbitrary, though they are constrained to have a regular structure. In addition, the values of the netCDF variable may be accessed using non-unity strides. If an error occurs, this function returns -1.</p>
<dt> <code>int ncvargetg(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const long </code><i>start[]</i><code>,</p>
<dd>const long </code><i>count[]</i><code>, const long </code><i>stride[]</i><code>, const long </code><i>imap[]</i><code>, void* </code><i>value</i><code>)</code> </p>
<p> Reads a general hyperslab of values from a netCDF variable of an open netCDF file, which must be in data mode. The locations of the memory-resident data values may be arbitrary, though they are constrained to have a regular structure. In addition, the values of the netCDF variable may be accessed using non-unity strides. If an error occurs, this function returns -1.</p>
<dt> <code>int ncrecput(int&nbsp;<wbr></code><i>ncid</i>, long&nbsp;<wbr><i>recnum</i>, const void*&nbsp;<wbr><i>valuep[]</i>) </p>
<dd>Writes a record (or a subset of a record) of values into the record variables of an open netCDF file, which must be in data mode. The record number, <i>recnum</i>, must be a nonnegative number that specifies which record (which value of the unlimited or record dimension) to write. The array of pointers to blocks of data to be written, <i>valuep</i>, should have one pointer for each record variable. The pointer to the data to be written to the <i>n</i>-th record variable, <i>valuep[n]</i>, points to one record&#8217;s worth of data of the appropriate type to be written into the <i>recnum</i>-th record of that netCDF variable. If the pointer for any record variable is the <code>NULL</code> pointer, no data is written for that variable. Hence any subset of record variables may be written by specifying non-<code>NULL</code> pointers for the desired record variables. Invoking this function is equivalent to a sequence of invocations of ncvarput() for all record variables for which a non-<code>NULL</code> pointer is specified. If an error occurs, this function returns -1.</p>
<dt> <code>int ncrecget(int&nbsp;<wbr></code><i>ncid</i>, long&nbsp;<wbr><i>recnum</i>, void*&nbsp;<wbr><i>valuep[]</i>) </p>
<dd>Reads a record (or a subset of a record) of values from the record variables of an open netCDF file, which must be in data mode. The record number, <i>recnum</i>, must be a nonnegative number that specifies which record to read. The array of pointers to blocks of data to be read, <i>valuep</i>, should have one pointer for each record variable. The pointer to the data to be read for the <i>n</i>-th record variable, <i>valuep[n]</i>, shall point to enough space to hold one record&#8217;s worth of data of the appropriate type for that netCDF record variable. If the pointer for any record variable is the <code>NULL</code> pointer, no data is read from that variable. Hence any subset of record variables may be read by specifying non-<code>NULL</code> pointers for only the desired record variables. Invoking this function is equivalent to a sequence of invocations of ncvarget() for all record variables for which a non-<code>NULL</code> pointer is specified. If an error occurs, this function returns -1.</p>
<dt> <code>int ncrecinq(int </code><i>ncid</i>, int*&nbsp;<wbr><i>nrvars</i>, int&nbsp;<wbr><i>rvarids[]</i>, long&nbsp;<wbr><i>rsizes[]</i>) </p>
<dd>Returns information about the record variables (variables that use the unlimited dimension) of an open netCDF file. Upon successful return, <i>nrvars</i> will contain the number of record variables, <i>rvarids</i> will contain the variable IDs of those record variables, and <i>rsizes</i> will contain the size in bytes for a record&#8217;s worth of data for each record variable. If any of the return parameters (<i>nrvars</i>, <i>rvarids</i>, or <i>rsizes</i>) is a <code>NULL</code> pointer, the specified information will not be returned; hence no space needs to be allocated for it. If an error occurs, this function returns -1.</p>
<dt> <code>int ncvarrename(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const char* </code><i>name</i><code>)</code> </p>
<dd>Changes the name of a netCDF variable in an open netCDF. If the new name is longer than the old name, the netCDF must be in define mode. You cannot rename a variable to have the name of any existing variable. If an error occurs, this function returns -1.</p>
<dt> <code>int ncattput(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const char* </code><i>name</i><code>,</p>
<dd>nc_type </code><i>datatype</i><code>, int </code><i>len</i><code>, const void* </code><i>value</i><code>)</code> </p>
<p> Adds or changes a variable attribute or global attribute of an open netCDF file. If this attribute is new, or if the space required to store the attribute is greater than before, the netCDF file must be in define mode. If an error occurs, this function returns -1.</p>
<dt> <code>int ncattinq(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const char* </code><i>name</i><code>,</p>
<dd>nc_type* </code><i>datatype</i><code>, int* </code><i>len</i><code>)</code> </p>
<p> Returns information about a netCDF attribute, given its variable ID and name. The information returned is the type and length of the attribute. If either of the return parameters is a <code>NULL</code> pointer, the specified information will not be returned; hence no space needs to be allocated for it. If an error occurs, this function returns -1.</p>
<dt> <code>int ncattget(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const char* </code><i>name</i><code>,</p>
<dd>void* </code><i>value</i><code>)</code> </p>
<p> Gets the value(s) of a netCDF attribute, given its variable ID and name. All elements of the vector of attribute values are returned, so you must allocate enough space to hold them. If you don&#8217;t know how much space to reserve, call <code>ncattinq()</code> first to find out the length of the attribute. If an error occurs, this function returns -1.</p>
<dt> <code>int ncattcopy(int </code><i>inncid</i><code>, int </code><i>invar</i><code>, const char* </code><i>name</i><code>,</p>
<dd>int </code><i>outncid</i><code>, int </code><i>outvar</i><code>)</code> </p>
<p> Copies an attribute from one open netCDF file to another. It can also be used to copy an attribute from one variable to another within the same netCDF. <i>inncid</i> is the netCDF ID of an input netCDF file from which the attribute will be copied. <i>invar</i> is the ID of the variable in the input netCDF file from which the attribute will be copied, or <code>NC_GLOBAL</code> for a global attribute. <i>name</i> is the name of the attribute in the input netCDF file to be copied. <i>outncid</i> is the netCDF ID of the output netCDF file to which the attribute will be copied. It is permissible for the input and output netCDF IDs to be the same. The output netCDF file should be in define mode if the attribute to be copied does not already exist for the target variable, or if it would cause an existing target attribute to grow. <i>outvar</i> is the ID of the variable in the output netCDF file to which the attribute will be copied, or <code>NC_GLOBAL</code> to copy to a global attribute. If an error occurs, this function returns -1.</p>
<dt> <code>int ncattname(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, int </code><i>attnum</i><code>,</p>
<dd>char* </code><i>name</i><code>)</code> </p>
<p> Gets the name of an attribute, given its variable ID and number as an attribute of that variable. This function is useful in generic applications that need to get the names of all the attributes associated with a variable, since attributes are accessed by name rather than number in all other attribute functions. The number of an attribute is more volatile than the name, since it can change when other attributes of the same variable are deleted. This is why an attribute number is not called an attribute ID. <i>attnum</i> is the number of the attribute. The attributes for each variable are numbered from 0 (the first attribute) to <i>nvatts</i>-1, where <i>nvatts</i> is the number of attributes for the variable, as returned from a call to <code>ncvarinq()</code>. If the <i>name</i> parameter is a <code>NULL</code> pointer, no name will be returned and no space need be allocated. If an error occurs, this function returns -1.</p>
<dt> <code>int ncattrename(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const char* </code><i>name</i><code>,</p>
<dd>const char* </code><i>newname</i><code>)</code> </p>
<p> Changes the name of an attribute. If the new name is longer than the original name, the netCDF must be in define mode. You cannot rename an attribute to have the same name as another attribute of the same variable. <i>name</i> is the original attribute name. <i>newname</i> is the new name to be assigned to the specified attribute. If the new name is longer than the old name, the netCDF file must be in define mode. If an error occurs, this function returns -1.</p>
<dt> <code>int ncattdel(int </code><i>ncid</i><code>, int </code><i>varid</i><code>, const char* </code><i>name</i><code>)</code> </p>
<dd>Deletes a netCDF attribute from an open netCDF file. The netCDF file must be in define mode. If an error occurs, this function returns -1.</p>
<dt> <code>int nctypelen(nc_type </code><i>datatype</i><code>)</code> </p>
<dd>Returns the number of bytes in a netCDF data type. If an error occurs, this function returns -1.</dl>
<h2>Common Argument Descriptions</h2>
<dl>
<dt><code>char* </code><i>name</i></p>
<dd>is the name of a dimension, variable, or attribute. It shall begin with an alphabetic character, followed by zero or more alphanumeric characters including the underscore (`_&#8217;). Case is significant. As an input argument, it shall be a pointer to a 0-terminated string; as an output argument, it shall be the address of a buffer in which to hold such a string. The maximum allowable number of characters (excluding the terminating 0) is MAX_NC_NAME. Attribute names that begin with an underscore (`_&#8217;) are reserved for use by the netCDF interface.</p>
<dt><code>char* </code><i>path</i></p>
<dd>is the pathname of a netCDF file. It may be absolute or relative.</p>
<dt><code>int </code><i>ncid</i></p>
<dd>is the netCDF ID returned from a previous, successful call to <code>ncopen()</code> or <code>nccreate()</code>.</p>
<dt><code>int </code><i>dimids</i><code>[]</code></p>
<dd>is a vector of dimension ID&#8217;s and defines the shape of a netCDF variable. The size of the vector shall be greater than or equal to the rank (i.e. the number of dimensions) of the variable (<i>ndims</i>). The vector shall be ordered by the speed with which a dimension varies: <i>dimids</i>[<i>ndims</i>-1] shall be the dimension ID of the most rapidly varying dimension and <i>dimids</i>[0] shall be the dimension ID of the most slowly varying dimension. Consequently, if a variable is a record variable, then <i>dimids</i>[0] shall be the dimension ID of the record dimension. The maximum possible number of dimensions for a variable is given by the symbolic constant <code>MAX_VAR_DIMS</code>.</p>
<dt><code>int </code><i>dimid</i></p>
<dd>is the ID of a netCDF dimension. netCDF dimension ID&#8217;s are allocated sequentially from the non-negative integers beginning with 0.</p>
<dt><code>int </code><i>len</i></p>
<dd>is the number of values associated with an attribute. If the attribute is of type <code>NC_CHAR</code>, then this is one more than the string length (since the terminating 0 is stored).</p>
<dt><code>int </code><i>ndims</i></p>
<dd>is either the total number of dimensions in a netCDF dataset or the rank (i.e. the number of dimensions) of a netCDF variable. The value shall not be negative or greater than the symbolic constant <code>MAX_VAR_DIMS</code>.</p>
<dt><code>int </code><i>varid</i></p>
<dd>is the ID of a netCDF variable or (for the attribute-access functions) the symbolic constant <code>NC_GLOBAL</code>, which is used to reference global attributes. netCDF variable ID&#8217;s are allocated sequentially from the non-negative integers beginning with 0.</p>
<dt><code>int </code><i>natts</i></p>
<dd>is the number of global attributes in a netCDF dataset for the <code>ncinquire()</code> function or the number of attributes associated with a netCDF variable for the <code>ncvarinq()</code> function.</p>
<dt><code>long </code><i>imap</i><code>[]</code></p>
<dd>is the index mapping vector that specifies how data values associated with a netCDF variable are arranged in memory. The offset, in bytes, from the memory location pointed to by the <i>value</i> argument to a particular datum is given by the inner (dot) product of the index mapping vector with the coordinates of the datum. For example, on a machine where `<code>sizeof(float) == 4</code>&#8216;, the index mapping vector for the array `<code>float u[3][5];</code>&#8216; is `<code>long imap[2] = {20,4}</code>&#8216;. Note that the index mapping vector can be used to access memory-resident data values in a manner that differs radically from the nominal structure of the associated netCDF variable. For example, the following definitions </p>
<dl>
<dd>
<pre>struct vel {
 int flags;
 float u;
 float v;
} vel[NX][NY];
long imap[2] = {
 sizeof(struct vel),
 sizeof(struct vel)*NY};</pre>
</dl>
<dd>can be used to access the memory-resident values of the netCDF variable, `<code>u[NY][NX]</code>&#8216;, even though the dimensions are transposed and the data is contained in a 2-D array of structures rather than a 2-D array of floating-point values. The index mapping vector may contain negative values if the <i>value</i> argument is appropriately set. A <code>NULL</code> index mapping vector argument obtains the default behavior in which the memory-resident values are assumed to have the same structure as the associated netCDF variable.</p>
<dt><code>long </code><i>coords</i><code>[]</code></p>
<dd>specifies the indicial coordinates of the netCDF data value to be accessed. The indices are relative to 0; thus, for example, the first data value of a two-dimensional variable is <code>(0,0)</code>. The size of the vector shall be at least the rank of the associated netCDF variable and its elements shall correspond, in order, to the variable&#8217;s dimensions. Consequently, if the variable is a record variable, then the first index is the record number.</p>
<dt><code>long </code><i>count</i><code>[]</code></p>
<dd>specifies the number of data values to be accessed in terms of the lengths of the sides of the hyperslab. Thus, to access a single value, for example, specify <i>count</i> as <code>(1, 1, &#8230;, 1)</code>. Note that, for generalized hyperslab I/O, this argument must be adjusted to be compatible with the <i>stride</i> and <i>start</i> arguments so that the interaction of the three does not attempt to access an invalid data co-ordinate. For example, to access every <i>stride</i><code>(</code><i>i</i><code>)</code>&#8216;th datum along dimension <i>i</i> beginning with point <i>start</i><code>(</code><i>i</i><code>), </code><i>counts</i><code>(</code><i>i</i><code>)</code> should be <code>1+(</code><i>npts</i><code>(</code><i>i</i><code>)-1-</code><i>start</i><code>(</code><i>i</i><code>))/</code><i>stride</i><code>(</code><i>i</i><code>)</code>: where <i>npts</i><code>(</code><i>i</i><code>)</code> is the size of dimension <i>i</i>. The size of the <i>count</i> vector shall be at least the rank of the associated netCDF variable and its elements shall correspond, in order, to the variable&#8217;s dimensions. Consequently, if the variable is a record variable, then the first element of <i>count</i> is the number of records to access.</p>
<dt><code>long </code><i>length</i></p>
<dd>is the size of a netCDF dimension. As an input argument, it shall be a positive integer or the symbolic constant <code>NC_UNLIMITED</code>. At most one such unlimited size dimension, called the record dimension, shall be defined in a netCDF dataset. As an output argument, it shall be a positive integer.</p>
<dt><code>long </code><i>start</i><code>[]</code></p>
<dd>specifies the starting point for accessing a netCDF variable&#8217;s data values in terms of the indicial coordinates of the corner of the hyperslab. The indices are relative to 0; thus, the first data value of a variable is <code>(0, 0, &#8230;, 0)</code>. The size of the vector shall be at least the rank of the associated netCDF variable and its elements shall correspond, in order, to the variable&#8217;s dimensions. Consequently, if the variable is a record variable, then the first index is the starting record number for accessing the netCDF variable&#8217;s data values.</p>
<dt><code>long </code><i>stride</i><code>[]</code></p>
<dd>specifies, for each dimension, the interval between the accessed values of a netCDF variable. The size of the vector shall be at least the rank of the associated netCDF variable and its elements shall correspond, in order, to the variable&#8217;s dimensions. A value of 1 accesses adjacent values of the netCDF variable in the corresponding dimension; a value of 2 accesses every other value of the netCDF variable in the corresponding dimension; and so on. Attempting to access a data value that lies outside the defined data space of a variable is an error. A <code>NULL</code> stride argument obtains the default behavior in which adjacent values are accessed along each dimension.</p>
<dt><code>nc_type </code><i>datatype</i></p>
<dd>specifies the data type of a netCDF variable and is one of the following: <code>NC_BYTE</code>, <code>NC_CHAR</code>, <code>NC_SHORT</code>, <code>NC_LONG</code>, <code>NC_FLOAT</code>, or <code>NC_DOUBLE</code>.</p>
<dt><code>void* </code><i>value</i></p>
<dd>points to the start of the memory-resident data values to be accessed. The pointer is declared to be of type <code>void*</code> because it can point to data of any of the basic netCDF types. The data should be of the appropriate type for the netCDF variable: </p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>netCDF Type</code></td>
<td ALIGN=center>C Type
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>NC_BYTE</td>
<td>unsigned char
</td>
</tr>
<tr VALIGN=top>
<td>NC_CHAR</td>
<td>char
</td>
</tr>
<tr VALIGN=top>
<td>NC_SHORT</td>
<td>short
</td>
</tr>
<tr VALIGN=top>
<td>NC_LONG</td>
<td><code>nclong</code>
</td>
</tr>
<tr VALIGN=top>
<td>NC_FLOAT</td>
<td>float
</td>
</tr>
<tr VALIGN=top>
<td>NC_DOUBLE</td>
<td>double
</td>
</tr>
</table>
</dl>
<dd>NOTE: The C type corresponding to the netCDF type <code>NC_LONG</code> is <code>nclong</code>. This type is defined in the netCDF header file and is guaranteed to hold at least 32 bits. It is defined as either a C `<code>int</code>&#8216; or a C `<code>long</code>&#8216; &#8212; depending on the platform.</p>
<dd><code>Warning: neither the compiler nor the netCDF software can detect if the wrong type of data is used.</code></dl>
<h2>Variable Prefilling</h2>
<p>By default, the netCDF interface sets the values of all newly-defined variables of finite length (i.e. not having an unlimited, record dimension) to the type-dependent fill-value associated with each variable. This is done when `<code>ncendef()</code>&#8216; is called. The fill-value for a variable may be changed from the default value by defining the attribute `<code>_FillValue</code>&#8216; for the variable. This attribute must have the same type as the variable and be of length one. </p>
<p> Variables with an unlimited record dimension are also prefilled, but on an `as needed&#8217; basis. For example, if the first write of a record variable is to position 5, then positions 0 through 4 (and no others) would be set to the fill-value at the same time. </p>
<p> This default prefilling of data values may be disabled by calling the function <code>ncsetfill()</code> with the argument <code>NC_NOFILL</code>. Note that, for non-record variables, this call must be made before <code>ncendef()</code>; whereas, for record-variables, this call may be made at any time. </p>
<p> One can obtain increased performance of the netCDF interface by using this feature, but only at the expense of requiring the application to set every single data value.</p>
<h2>Global Options</h2>
<p>The global variable `<code>ncopts</code>&#8216;, which is defined in `<code>netcdf.h</code>&#8216;, affects the actions of the netCDF interface. It may be set by the user to the bitwise OR of any of the following, non-zero, symbolic bit-values:</p>
<dl>
<dt><code>NC_VERBOSE</code></p>
<dd>Print error-messages on standard error.</p>
<dt><code>NC_FATAL</code></p>
<dd>Abort. Call `<code>exit()</code>&#8216; with an error-condition if an error occurs.</dl>
<p> By default, `<code>ncopts</code>&#8216; is `<code>NC_VERBOSE | NC_FATAL</code>&#8216;.</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>NETCDF_FFIOSPEC</code></p>
<dd>Specifies the Flexible File I/O buffers for netCDF I/O when executing under the UNICOS operating system (the variable is ignored on other operating systems). An appropriate specification can greatly increase the efficiency of netCDF I/O &#8212; to the extent that it can actually surpass FORTRAN binary I/O. The default specification is <code>bufa:336:2</code>. See UNICOS Flexible File I/O for more information.</dl>
<h2>Mailing-Lists</h2>
<p>Both a mailing list and a digest are available for discussion of the netCDF interface and announcements about netCDF bugs, fixes, and enhancements. To begin or change your subscription to either the mailing-list or the digest, send one of the following in the body (not the subject line) of an email message to &quot;Majordomo [at] unidata.ucar.edu&quot;. Use your email address in place of <i>jdoe [at] host.inst.domain</i>. </p>
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
