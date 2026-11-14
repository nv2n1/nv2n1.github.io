---
title: "h5dump(1)"
name: "h5dump"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5dump/"
description: "h5dump – Displays HDF5 file contents."
---

<h2>NAME</h2>
<p> h5dump &#8211; Displays HDF5 file contents.</p>
<h2>SYNOPSIS</h2>
<p> h5dump [OPTIONS] file</p>
<h2>DESCRIPTION</h2>
<p> h5dump enables the user to examine the contents of an HDF5 file and dump those contents, in human readable form, to an ASCII file. </p>
<p> h5dump dumps HDF5 file content to standard output. It can display the contents of the entire HDF5 file or selected objects, which can be groups, datasets, a subset of a dataset, links, attributes, or datatypes. </p>
<p> The &#8211;header option displays object header information only. </p>
<p> Names are the absolute names of the objects. h5dump displays objects in the order same as the command order. If a name does not start with a slash, h5dump begins searching for the specified object starting at the root group. </p>
<p> If an object is hard linked with multiple names, h5dump displays the content of the object in the first occurrence. Only the link information is displayed in later occurrences. </p>
<p> h5dump assigns a name for any unnamed datatype in the form of #oid1:oid2, where oid1 and oid2 are the object identifiers assigned by the library. The unnamed types are displayed within the root group. </p>
<p> Datatypes are displayed with standard type names. For example, if a dataset is created with H5T_NATIVE_INT type and the standard type name for integer on that machine is H5T_STD_I32BE, h5dump displays H5T_STD_I32BE as the type of the dataset. </p>
<p> h5dump can also dump a subset of a dataset. This feature operates in much the same way as hyperslabs in HDF5; the parameters specified on the commnd line are passed to the function H5Sselect_hyperslab and the resulting selection is displayed. </p>
<p> The h5dump output is described in detail in the DDL for HDF5, the Data Description Language document. </p>
<p> Note: It is not permissable to specify multiple attributes, datasets, datatypes, groups, or soft links with one flag. For example, one may not issue the command</p>
<dl>
<dt>
<dd> WRONG: h5dump -a /attr1 /attr2 foo.h5</dl>
<p> to display both /attr1 and /attr2. One must issue the following command:</p>
<dl>
<dt>
<dd> CORRECT: h5dump -a /attr1 -a /attr2 foo.h5</dl>
<p> It&#8217;s possible to select the file driver with which to open the HDF5 file by using the &#8211;filedriver (-f) command-line option. Acceptable values for the &#8211;filedriver option are: &quot;sec2&quot;, &quot;family&quot;, &quot;split&quot;, &quot;multi&quot;, and &quot;stream&quot;. If the file driver flag isn&#8217;t specified, then the file will be opened with each driver in turn and in the order specified above until one driver succeeds in opening the file.</p>
<h2>XML OUTPUT</h2>
<p> With the &#8211;xml option, h5dump generates XML output. This output contains a complete description of the file, marked up in XML. The XML conforms to the HDF5 Document Type Definition (DTD) available at <a rel="nofollow" href="http://hdf.ncsa.uiuc.edu/DTDs/HDF5-File.dtd.">http://hdf.ncsa.uiuc.edu/DTDs/HDF5-File.dtd.</a> </p>
<p> The XML output is suitable for use with other tools, including the HDF5 Java Tools.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h </code></p>
<dd> or <code>&#8211;help</code> Print a usage message and exit.</p>
<dt><code>-B </code></p>
<dd> or <code>&#8211;bootblock</code> Print the content of the boot block. (This option is not yet implemented.)</p>
<dt><code>-H </code></p>
<dd> or <code>&#8211;header</code> Print the header only; no data is displayed.</p>
<dt><code>-A</code></p>
<dd> Print the header and value of attributes; data of datasets is not displayed.</p>
<dt><code>-i </code></p>
<dd> or <code>&#8211;object-ids</code> Print the object ids.</p>
<dt><code>-r </code></p>
<dd> or <code>&#8211;string</code> Print 1-bytes integer datasets as ASCII.</p>
<dt><code>-V </code></p>
<dd> or <code>&#8211;version</code> Print version number and exit.</p>
<dt><code>-a P </code></p>
<dd> or <code>&#8211;attribute=P</code> Print the specified attribute.</p>
<dt><code>-d P </code></p>
<dd> or <code>&#8211;dataset=P</code> Print the specified dataset.</p>
<dt><code>-f D </code></p>
<dd> or <code>&#8211;filedriver=D</code> Specify which driver to open the file with.</p>
<dt><code>-g P </code></p>
<dd> or <code>&#8211;group=P</code> Print the specified group and all members.</p>
<dt><code>-l P </code></p>
<dd> or <code>&#8211;soft-link=P</code> Print the value(s) of the specified soft link.</p>
<dt><code>-o F </code></p>
<dd> or <code>&#8211;output=F</code> Output raw data into file F.</p>
<dt><code>-t T </code></p>
<dd> or <code>&#8211;datatype=T</code> Print the specified named datatype.</p>
<dt><code>-w N </code></p>
<dd> or <code>&#8211;width=N</code> Set the number of columns of output.</p>
<dt><code>-x </code></p>
<dd> or <code>&#8211;xml</code> Output XML using XML schema (default) instead of DDL.</p>
<dt><code>-u </code></p>
<dd> or <code>&#8211;use-dtd</code> Output XML using XML DTD instead of DDL.</p>
<dt><code>-D U </code></p>
<dd> or <code>&#8211;xml-dtd=U</code> In XML output, refer to the DTD or schema at U instead of the default schema/DTD.</p>
<dt><code>-X S </code></p>
<dd> or <code>&#8211;xml-dns=S</code> In XML output, (XML Schema) use qualified names in the XML: &quot;:&quot;: no namespace, default: &quot;hdf5:&quot;</p>
<dt><code>-s L </code></p>
<dd> or <code>&#8211;start=L</code> Offset of start of subsetting selection. Default: the beginning of the dataset.</p>
<dt><code>-S L </code></p>
<dd> or <code>&#8211;stride=L</code> Hyperslab stride. Default: 1 in all dimensions.</p>
<dt><code>-c L </code></p>
<dd> or <code>&#8211;count=L</code> Number of blocks to include in the selection.</p>
<dt><code>-k L </code></p>
<dd> or <code>&#8211;block=L</code> Size of block in hyperslab. Default: 1 in all dimensions.</p>
<dt><code>&#8212;</code></p>
<dd> Indicate that all following arguments are non-options. E.g., to dump a file called `-f&#8217;, use h5dump &#8212; -f.</p>
<dt><code>file</code></p>
<dd> The file to be examined.</dl>
<p> The option parameters listed above are defined as follows:</p>
<dl>
<dt><code>D </code></p>
<dd> which file driver to use in opening the file. Acceptable values are &quot;sec2&quot;, &quot;family&quot;, &quot;split&quot;, &quot;multi&quot;, and &quot;stream&quot;. Without the file driver flag the file will be opened with each driver in turn and in the order specified above until one driver succeeds in opening the file.</p>
<dt><code>P </code></p>
<dd> The full path from the root group to the object</p>
<dt><code>T </code></p>
<dd> The name of the datatype</p>
<dt><code>F </code></p>
<dd> A filename</p>
<dt><code>N </code></p>
<dd> An integer greater than 1</p>
<dt><code>L </code></p>
<dd> A list of integers, the number of which is equal to the number of dimensions in the dataspace being queried</p>
<dt><code>U </code></p>
<dd> A URI (as defined in [IETF RFC 2396], updated by [IETF RFC 2732]) that refers to the DTD to be used to validate the XML</dl>
<p> Subsetting paramaters can also be expressed in a convenient compact form, as follows:</p>
<dl>
<dt>
<dd> &#8211;dataset=&quot;/foo/mydataset[START;STRIDE;COUNT;BLOCK]&quot;</dl>
<p> All of the semicolons (;) are required, even when a parameter value is not specified. When not specified, default parameter values are used. </p>
<h2>EXAPLES</h2>
<dl>
<dt>1.</p>
<dd> Dumping the group /GroupFoo/GroupBar in the file quux.h5:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>h5dump -g&nbsp;<wbr>/GroupFoo/GroupBar quux.h5&nbsp;<wbr></dl>
</dl>
<dl>
<dt>2.</p>
<dd> Dumping the dataset Fnord in the group /GroupFoo/GroupBar in the file quux.h5:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>h5dump -d&nbsp;<wbr>/GroupFoo/GroupBar/Fnord quux.h5&nbsp;<wbr></dl>
</dl>
<dl>
<dt>3.</p>
<dd> Dumping the attribute metadata of the dataset Fnord which is in group /GroupFoo/GroupBar in the file quux.h5:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>h5dump -a&nbsp;<wbr>/GroupFoo/GroupBar/Fnord/metadata quux.h5&nbsp;<wbr></dl>
</dl>
<dl>
<dt>4.</p>
<dd> Dumping the attribute metadata which is an attribute of the root group in the file quux.h5:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>h5dump -a&nbsp;<wbr>/metadata quux.h5&nbsp;<wbr></dl>
</dl>
<dl>
<dt>5.</p>
<dd> Producing an XML listing of the file bobo.h5:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>h5dump &#8211;xml bobo.h5&nbsp;<wbr>&gt;&nbsp;<wbr>bobo.h5.xml&nbsp;<wbr></dl>
</dl>
<dl>
<dt>6.</p>
<dd> Dumping a subset of the dataset /GroupFoo/databar/ in the file quux.h5</p>
<dl>
<dt>
<dd> h5dump -d /GroupFoo/databar &#8211;start=&quot;1,1&quot; &#8211;stride=&quot;2,3&quot; &#8211;count=&quot;3,19&quot; &#8211;block=&quot;1,1&quot; quux.h5</dl>
</dl>
<dl>
<dt>7.</p>
<dd> The same example using the short form to specify the subsetting parameters:</p>
<dl>
<dt>
<dd> h5dump -d &quot;/GroupFoo/databar[1,1;2,3;3,19;1,1]&quot; quux.h5</dl>
</dl>
<h2>CURRENT STATUS</h2>
<p> The current version of h5dump displays the following information:</p>
<dl>
<dt>
<dd> * Group</p>
<dl>
<dt>
<dd> o group attribute (see Attribute)</dl>
<dl>
<dt>
<dd> o group member</dl>
<p> * Dataset</p>
<dl>
<dt>
<dd> o dataset attribute (see Attribute)</dl>
<dl>
<dt>
<dd> o dataset type (see Datatype)</dl>
<dl>
<dt>
<dd> o dataset space (see Dataspace)</dl>
<dl>
<dt>
<dd> o dataset data</dl>
<p> * Attribute</p>
<dl>
<dt>
<dd> o attribute type (see Datatype)</dl>
<dl>
<dt>
<dd> o attribute space (see Dataspace)</dl>
<dl>
<dt>
<dd> o attribute data</dl>
<p> * Datatype</p>
<dl>
<dt>
<dd> o integer type</p>
<dl>
<dt>
<dd> &#8211; H5T_STD_I8BE, H5T_STD_I8LE, H5T_STD_I16BE, &#8230;</dl>
<p> o floating point type</p>
<dl>
<dt>
<dd> &#8211; H5T_IEEE_F32BE, H5T_IEEE_F32LE, H5T_IEEE_F64BE, &#8230;</dl>
<p> o string type</dl>
<dl>
<dt>
<dd> o compound type</p>
<dl>
<dt>
<dd> &#8211; named, unnamed and transient compound type &#8211; integer, floating or string type member</dl>
<p> o opaque types</dl>
<dl>
<dt>
<dd> o reference type</p>
<dl>
<dt>
<dd> &#8211; object references</dl>
<dl>
<dt>
<dd> &#8211; data regions</dl>
<p> o enum type</dl>
<dl>
<dt>
<dd> o variable-length datatypes</p>
<dl>
<dt>
<dd> &#8211; atomic types only</dl>
<dl>
<dt>
<dd> &#8211; scalar or single dimensional array of variable-length types supported</dl>
</dl>
<p> * Dataspace</p>
<dl>
<dt>
<dd> o scalar and simple space</dl>
<p> * Soft link</dl>
<dl>
<dt>
<dd> * Hard link</dl>
<dl>
<dt>
<dd> * Loop detection</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-h5ls/">h5ls</a></i>(1), <i><a href="/docs/linux/man/1-h5diff/">h5diff</a></i>(1), <i><a href="/docs/linux/man/1-h5repart/">h5repart</a></i>(1), <i><a href="/docs/linux/man/1-h5import/">h5import</a></i>(1), <i><a href="/docs/linux/man/1-gif2h5/">gif2h5</a></i>(1), <i><a href="/docs/linux/man/1-h52gif/">h52gif</a></i>(1), <i><a href="/docs/linux/man/1-h5perf/">h5perf</a></i>(1) </p>
<dl>
<dt>
<dd> * HDF5 Data Description Language syntax at file:///usr/share/doc/libhdf5-doc/html/ddl.html</dl>
<dl>
<dt>
<dd> * HDF5 XML Schema at <a rel="nofollow" href="http://hdf.ncsa.uiuc.edu/DTDs/HDF5-File.xsd">http://hdf.ncsa.uiuc.edu/DTDs/HDF5-File.xsd</a></dl>
<dl>
<dt>
<dd> * HDF5 XML information at <a rel="nofollow" href="http://hdf.ncsa.uiuc.edu/HDF5/XML/">http://hdf.ncsa.uiuc.edu/HDF5/XML/</a></dl>
<h2>Index</h2>
