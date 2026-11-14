---
title: "h5import(1)"
name: "h5import"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5import/"
description: "h5import – Imports data into an existing or new HDF5 file."
---

<h2>NAME</h2>
<p> h5import &#8211; Imports data into an existing or new HDF5 file.</p>
<h2>SYNOPSIS</h2>
<p> <code>h5import </code> infile <code>-d </code> dim_list [ <code>-p </code> pathname ] [ <code>-t </code> input_class ] [ <code>-s </code> input_size ] [infile &#8230;] <code>-o </code> outfile </p>
<p> <code>h5import </code> infile <code>-dims </code> dim_list [ <code>-path </code> pathname ] [ <code>-type </code> input_class ] [ <code>-size </code> input_size ] [infile &#8230;] <code>-outfile </code> outfile </p>
<p> <code>h5import </code> infile <code>-c </code> config_file [infile &#8230;] <code>-outfile </code> outfile </p>
<p> <code>h5import </code> <code>-h </code> </p>
<p> <code>h5import </code> <code>-help </code></p>
<h2>DESCRIPTION</h2>
<p> h5import converts data from one or more ASCII or binary files, infile, into the same number of HDF5 datasets in the existing or new HDF5 file, outfile. Data conversion is performed in accordance with the user-specified type and storage properties specified in in_options. </p>
<p> The primary objective of h5import is to import floating point or integer data. The utility&#8217;s design allows for future versions that accept ASCII text files and store the contents as a compact array of one-dimensional strings, but that capability is not implemented in HDF5 Release 1.6. </p>
<p> <code>Input data and options</code> </p>
<p> Input data can be provided in one of the follwing forms:</p>
<dl>
<dt>*</p>
<dd> As an ASCII, or plain-text, file containing either floating point or integer data</p>
<dt>*</p>
<dd> As a binary file containing either 32-bit or 64-bit native floating point data</p>
<dt>*</p>
<dd> As a binary file containing native integer data, signed or unsigned and 8-bit, 16-bit, 32-bit, or 64-bit.</p>
<dt>*</p>
<dd> As an ASCII, or plain-text, file containing text data. (This feature is not implemented in HDF5 Release 1.6.)</dl>
<p> Each input file, infile, contains a single n-dimensional array of values of one of the above types expressed in the order of fastest-changing dimensions first. </p>
<p> Floating point data in an ASCII input file must be expressed in the fixed floating form (e.g., 323.56) h5import is designed to accept scientific notation (e.g., 3.23E+02) in an ASCII, but that is not implemented in HDF5 release 1.6. </p>
<p> Each input file can be associated with options specifying the datatype and storage properties. These options can be specified either as command line arguments or in a configuration file. Note that exactly one of these approaches must be used with a single input file. </p>
<p> Command line arguments, best used with simple input files, can be used to specify the class, size, dimensions of the input data and a path identifying the output dataset. </p>
<p> The recommended means of specifying input data options is in a configuration file; this is also the only means of specifying advanced storage features. See further discussion in &quot;The configuration file&quot; below. </p>
<p> The only required option for input data is dimension sizes; defaults are available for all others. </p>
<p> h5import will accept up to 30 input files in a single call. Other considerations, such as the maximum length of a command line, may impose a more stringent limitation. </p>
<p> <code>Output data and options:</code> </p>
<p> The name of the output file is specified following the -o or -output option in outfile. The data from each input file is stored as a separate dataset in this output file. outfile may be an existing file. If it does not yet exist, h5import will create it. </p>
<p> Output dataset information and storage properties can be specified only by means of a configuration file.</p>
<dl>
<dt><code>Dataset path</code></p>
<dd> If the groups in the path leading to the dataset do not exist, h5import will create them. If no group is specified, the dataset will be created as a member of the root group. If no dataset name is specified, the default name is dataset1 for the first input dataset, dataset2 for the second input dataset, dataset3 for the third input dataset, etc. h5import does not overwrite a pre-existing dataset of the specified or default name. When an existing dataset of a confilcting name is encountered, h5import quits with an error; the current input file and any subsequent input files are not processed.</p>
<dt><code>Output type <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code></p>
<dd> Datatype parameters for output data</p>
<dt><code>Output data class</code></p>
<dd> Signed or unsigned integer or floating point</p>
<dt><code>Output data size</code></p>
<dd> 8-, 16-, 32-, or 64-bit integer 32- or 64-bit floating point</p>
<dt><code>Output architecture <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code></p>
<dd> IEEE, STD, NATIVE (Default), Other architectures are included in the h5import design but are not implemented in this release.</p>
<dt><code>Output byte order </code></p>
<dd> Little- or big-endian. Relevant only if output architecture is IEEE, UNIX, or STD; fixed for other architectures.</p>
<dt><code>Dataset layout and storage properties</code></p>
<dd> Denote how raw data is to be organized on the disk. If none of the following are specified, the default configuration is contiguous layout and with no compression.</p>
<dt><code>Layout</code></p>
<dd> Contiguous (Default), Chunked</p>
<dt><code>External storage</code></p>
<dd> Allows raw data to be stored in a non-HDF5 file or in an external HDF5 file. Requires contiguous layout.</p>
<dt><code>Compressed</code></p>
<dd> Sets the type of compression and the level to which the dataset must be compressed. Requires chunked layout.</p>
<dt><code>Extendible</code></p>
<dd> Allows the dimensions of the dataset increase over time and/or to be unlimited. Requires chunked layout.</p>
<dt><code>Compressed and extendible </code></p>
<dd> Requires chunked layout.</dl>
<h2>FILES</h2>
<p> A configuration file is specified with the -c config_file option:</p>
<dl>
<dt>
<dd> h5import infile -c config_file [infile &#8211; config_file2 &#8230;] -outfile outfile</dl>
<p> The configuration file is an ASCII file and must be organized as &quot;Configuration_Keyword Value&quot; pairs, with one pair on each line. For example, the line indicating that the input data class (configuration keyword INPUT-CLASS) is floating point in a text file (value TEXTFP) would appear as follows:</p>
<dl>
<dt>
<dd> INPUT-CLASS TEXTFP</dl>
<p> A configuration file may have the following keywords each followed by one of the following defined values. One entry for each of the first two keywords, RANK and DIMENSION-SIZES, is required; all other keywords are optional. </p>
<dl>
<dt><code>RANK rank</code></p>
<dd> An integer specifying the number of dimensions in the dataset. Example: RANK 4 for a 4-dimensional dataset.</p>
<dt><code>DIMENSION-SIZES dim_sizes</code></p>
<dd> Sizes of the dataset dimensions. (Required) A string of space-separated integers specifying the sizes of the dimensions in the dataset. The number of sizes in this entry must match the value in the RANK entry. The fastest-changing dimension must be listed first. Example: DIMENSION_SIZES 4 3 4 38 for a 38x4x3x4 dataset.</p>
<dt><code>PATH path</code></p>
<dd> Path of the output dataset. The full HDF5 pathname identifying the output dataset relative to the root group within the output file. I.e., path is a string consisting of optional group names, each followed by a slash, and ending with a dataset name. If the groups in the path do no exist, they will be created. If PATH is not specified, the output dataset is stored as a member of the root group and the default dataset name is dataset1 for the first input dataset, dataset2 for the second input dataset, dataset3 for the third input dataset, etc. Note that h5import does not overwrite a pre-existing dataset of the specified or default name. When an existing dataset of a confilcting name is encountered, h5import quits with an error; the current input file and any subsequent input files are not processed. Example: The configuration file entry &quot;PATH grp1/grp2/dataset1&quot; indicates that the output dataset dataset1 will be written in the group grp2/ which is in the group grp1/, a member of the root group in the output file.</p>
<dt><code>INPUT-CLASS {TEXTIN|TEXTUIN|TEXTFP|TEXTFPE|IN|UIN|FP|STR}</code></p>
<dd> A string denoting the type of input data.</p>
<dl>
<dt>
<dd> <code>TEXTIN</code> Input is signed integer data in an ASCII file.</dl>
<dl>
<dt>
<dd> <code>TEXTUIN</code> Input is unsigned integer data in an ASCII file.</dl>
<dl>
<dt>
<dd> <code>TEXTFP</code> Input is floating point data in fixed notation (e.g., 325.34) in an ASCII file.</dl>
<dl>
<dt>
<dd> <code>TEXTFPE</code> Input is floating point data in scientific notation (e.g., 3.2534E+02) in an ASCII file. (Not implemented in this release.)</dl>
<dl>
<dt>
<dd> <code>IN</code> Input is signed integer data in a binary file.</dl>
<dl>
<dt>
<dd> <code>UIN</code> Input is unsigned integer data in a binary file.</dl>
<dl>
<dt>
<dd> <code>FP</code> Input is floating point data in a binary file. (Default)</dl>
<dl>
<dt>
<dd> <code>STR</code> Input is character data in an ASCII file. With this value, the configuration keywords RANK, DIMENSION-SIZES, OUTPUT-CLASS, OUTPUT-SIZE, OUTPUT-ARCHITECTURE, and OUTPUT-BYTE-ORDER will be ignored. (Not implemented in this release.)</dl>
<dt><code>INPUT-SIZE {8|16|32|64}</code></p>
<dd> An integer denoting the size of the input data, in bits. For signed and unsigned integer data (TEXTIN, TEXTUIN, IN, or UIN) any of 8, 16, 32, or 64 may be used. The default is 32. For floating point data (TEXTFP, TEXTFPE, or FP), either 32 or 64 may be specified. The default is 32.</p>
<dt><code>OUTPUT-CLASS {IN|UIN|FP|STR}</code></p>
<dd> A string denoting the type of output data.</p>
<dl>
<dt>
<dd> <code>IN</code> Output is signed integer data. (Default if INPUT-CLASS is IN or TEXTIN)</dl>
<dl>
<dt>
<dd> <code>UIN</code> Output is unsigned integer data. (Default if INPUT-CLASS is UIN or TEXTUIN)</dl>
<dl>
<dt>
<dd> <code>FP</code> Output is floating point data. (Default if INPUT-CLASS is not specified or is FP, TEXTFP, or TEXTFPE)</dl>
<dl>
<dt>
<dd> <code>STR</code> Output is character data, to be written as a 1-dimensional array of strings. (Default if INPUT-CLASS is STR) (Not implemented in this release.)</dl>
<dt><code>OUTPUT-SIZE {8|16|32|64}</code></p>
<dd> An integer denoting the size of the output data, in bits. For signed and unsigned integer data (IN or UIN), any of the four sizes are valid. The default is the same as INPUT-SIZE, else 32. For floating point data (FP), either 32 or 64 may be specified. The default is the same as INPUT-SIZE, else 32.</p>
<dt><code>OUTPUT-ARCHITECTURE {NATIVE|STD|IEEE|INTEL|CRAY|MIPS|ALPHA|UNIX}</code></p>
<dd> A string denoting the type of output architecture. See the &quot;Predefined Atomic Types&quot; section in the &quot;HDF5 Datatypes&quot; chapter of the HDF5 User&#8217;s Guide for a discussion of these architectures. INTEL, CRAY, MIPS, ALPHA, and UNIX are not implemented in this release. (Default: NATIVE)</p>
<dt><code>OUTPUT-BYTE-ORDER {BE|LE}</code></p>
<dd> A string denoting the output byte order. This entry is ignored if the OUTPUT-ARCHITECTURE is not specified or if it is not specified as IEEE, UNIX, or STD.</p>
<dl>
<dt>
<dd> <code>BE</code> Big-endian. (Default)</dl>
<dl>
<dt>
<dd> <code>LE</code> Little-endian.</dl>
</dl>
<p> The following options are disabled by default, making the default storage properties no chunking, no compression, no external storage, and no extensible dimensions.</p>
<dl>
<dt><code>CHUNKED-DIMENSION-SIZES chunk_dims</code></p>
<dd> Dimension sizes of the chunk for chunked output data. A string of space-separated integers specifying the dimension sizes of the chunk for chunked output data. The number of dimensions must correspond to the value of RANK. The presence of this field indicates that the output dataset is to be stored in chunked layout; if this configuration field is absent, the dataset will be stored in contiguous layout.</p>
<dt><code>COMPRESSION-TYPE {GZIP}</code></p>
<dd> Type of compression to be used with chunked storage. Requires that CHUNKED-DIMENSION-SIZES be specified. <code>GZIP <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code> is gzip compression. Othe compression algorithms are not implemented in this release of h5import.</p>
<dt><code>COMPRESSION-PARAM [1-9]</code></p>
<dd> Compression level. Required if COMPRESSION-TYPE is specified. Gzip compression levels: 1 will result in the fastest compression while 9 will result in the best compression ratio. (Default: 6. The default gzip compression level is 6; not all compression methods will have a default level.)</p>
<dt><code>EXTERNAL-STORAGE external_file</code></p>
<dd> Name of an external file in which to create the output dataset. Cannot be used with CHUNKED-DIMENSIONS-SIZES, COMPRESSION-TYPE, OR MAXIMUM-DIMENSIONS. A string specifying the name of an external file.</p>
<dt><code>MAXIMUM-DIMENSIONS max_dims</code></p>
<dd> Maximum sizes of all dimensions. Requires that CHUNKED-DIMENSION-SIZES be specified. A string of space-separated integers specifying the maximum size of each dimension of the output dataset. A value of -1 for any dimension implies unlimited size for that particular dimension. The number of dimensions must correspond to the value of RANK.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h[elp]</code></p>
<dd> prints the h5import usage summary</p>
<dt><code>infile(s)</code></p>
<dd> Name of the Input file(s).</p>
<dt><code>-d[ims] dim_list</code></p>
<dd> Input data dimensions. <i>dim_list </i> is a string of comma-separated numbers with no spaces describing the dimensions of the input data. For example, a 50 x 100 2-dimensional array would be specified as -dims 50,100. Required argument: if no configuration file is used, this command-line argument is mandatory.</p>
<dt><code>-p[athname] pathname</code></p>
<dd> <i>pathname </i> is a string consisting of one or more strings separated by slashes (/) specifying the path of the dataset in the output file. If the groups in the path do no exist, they will be created. Optional argument: if not specified, the default path is dataset1 for the first input dataset, dataset2 for the second input dataset, dataset3 for the third input dataset, etc. h5import does not overwrite a pre-existing dataset of the specified or default name. When an existing dataset of a confilcting name is encountered, h5import quits with an error; the current input file and any subsequent input files are not processed.</p>
<dt><code>-t[ype] input_class</code></p>
<dd> <i>input_class </i> specifies the class of the input data and determines the class of the output data. Valid values are as defined in the Keyword/Values table in the section &quot;The configuration file&quot; above. Optional argument: if not specified, the default value is FP.</p>
<dt><code>-s[size] input_size</code></p>
<dd> <i>input_size </i> specifies the size in bits of the input data and determines the size of the output data. Valid values for signed or unsigned integers are 8, 16, 32, and 64. Valid values for floating point data are 32 and 64. Optional argument: if not specified, the default value is 32.</p>
<dt><code>-c config_file</code></p>
<dd> <i>config_file </i> specifies a configuration file. This argument replaces all other arguments except infile and -o outfile</p>
<dt><code>outfile</code></p>
<dd> Name of the HDF5 output file.</dl>
<h2>NOTES</h2>
<p> If the -c config_file option is used with an input file, no other argument can be used with that input file. If the -c config_file option is not used with an input data file, the -d dim_list argument (or -dims dim_list) must be used and any combination of the remaining options may be used. Any arguments used must appear in exactly the order used in the syntax declarations immediately above. </p>
<p> Note that while only the -dims argument is required, arguments must used in the order in which they are listed below.</p>
<h2>EXAMPLES</h2>
<p> Using command-line arguments: </p>
<p> This command creates a file out1 containing a single 2x3x4 32-bit integer dataset. Since no pathname is specified, the dataset is stored in out1 as /dataset1.</p>
<dl>
<dt>
<dd> h5import infile -dims 2,3,4 -type TEXTIN -size 32 -o out1</dl>
<p> This command creates a file out2 containing a single a 20&#215;50 64-bit floating point dataset. The dataset is stored in out2 as /bin1/dset1.</p>
<dl>
<dt>
<dd> h5import infile -dims 20,50 -path bin1/dset1 -type FP -size 64 -o out2</dl>
<p> Sample configuration files: The following configuration file specifies the following:</p>
<dl>
<dt>o</p>
<dd> The input data is a 5x2x4 floating point array in an ASCII file.</p>
<dt>o</p>
<dd> The output dataset will be saved in chunked layout, with chunk dimension sizes of 2x2x2.</p>
<dt>o</p>
<dd> The output datatype will be 64-bit floating point, little-endian, IEEE.</p>
<dt>o</p>
<dd> The output dataset will be stored in outfile at /work/h5/pkamat/First-set.</p>
<dt>o</p>
<dd> The maximum dimension sizes of the output dataset will be 8x8x(unlimited).</dl>
<dl>
<dt>
<dd> PATH work/h5/pkamat/First-set</dl>
<dl>
<dt>
<dd> INPUT-CLASS TEXTFP</dl>
<dl>
<dt>
<dd> RANK 3</dl>
<dl>
<dt>
<dd> DIMENSION-SIZES 5 2 4</dl>
<dl>
<dt>
<dd> OUTPUT-CLASS FP</dl>
<dl>
<dt>
<dd> OUTPUT-SIZE 64</dl>
<dl>
<dt>
<dd> OUTPUT-ARCHITECTURE IEEE</dl>
<dl>
<dt>
<dd> OUTPUT-BYTE-ORDER LE</dl>
<dl>
<dt>
<dd> CHUNKED-DIMENSION-SIZES 2 2 2</dl>
<dl>
<dt>
<dd> MAXIMUM-DIMENSIONS 8 8 -1</dl>
<p> The next configuration file specifies the following:</p>
<dl>
<dt>o</p>
<dd> The input data is a 6x3x5x2x4 integer array in a binary file.</p>
<dt>o</p>
<dd> The output dataset will be saved in chunked layout, with chunk dimension sizes of 2x2x2x2x2.</p>
<dt>o</p>
<dd> The output datatype will be 32-bit integer in NATIVE format (as the output architecure is not specified).</p>
<dt>o</p>
<dd> The output dataset will be compressed using Gzip compression with a compression level of 7.</p>
<dt>o</p>
<dd> The output dataset will be stored in outfile at /Second-set.</dl>
<dl>
<dt>
<dd> PATH Second-set</dl>
<dl>
<dt>
<dd> INPUT-CLASS IN</dl>
<dl>
<dt>
<dd> RANK 5</dl>
<dl>
<dt>
<dd> DIMENSION-SIZES 6 3 5 2 4</dl>
<dl>
<dt>
<dd> OUTPUT-CLASS IN</dl>
<dl>
<dt>
<dd> OUTPUT-SIZE 32</dl>
<dl>
<dt>
<dd> CHUNKED-DIMENSION-SIZES 2 2 2 2 2</dl>
<dl>
<dt>
<dd> COMPRESSION-TYPE GZIP</dl>
<dl>
<dt>
<dd> COMPRESSION-PARAM 7</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-h5dump/">h5dump</a></i>(1), <i><a href="/docs/linux/man/1-h5ls/">h5ls</a></i>(1), <i><a href="/docs/linux/man/1-h5diff/">h5diff</a></i>(1), <i><a href="/docs/linux/man/1-h5repart/">h5repart</a></i>(1), <i><a href="/docs/linux/man/1-gif2h5/">gif2h5</a></i>(1), <i><a href="/docs/linux/man/1-h52gif/">h52gif</a></i>(1), <i><a href="/docs/linux/man/1-h5perf/">h5perf</a></i>(1)<br />
&nbsp;<wbr> </p>
<h2>Index</h2>
