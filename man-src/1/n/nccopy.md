---
title: "nccopy(1)"
name: "nccopy"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nccopy/"
description: "nccopy – Copy a netCDF file, optionally changing format, compression, or chunking in the output."
---

<h2>NAME</h2>
<p> nccopy &#8211; Copy a netCDF file, optionally changing format, compression, or chunking in the output.</p>
<h2>SYNOPSIS</h2>
<p> <code></p>
<dl>
<dt>
<dd>nccopy [-k </code><i> kind_name </i>] [-<i>kind_code</i>] [-d <i> n </i>] [-s] [-c <i> chunkspec </i>] [-u] [-w] [-[v|V] var1,&#8230;] [-[g|G] grp1,&#8230;] [-m <i> bufsize </i>] [-h <i> chunk_cache </i>] [-e <i> cache_elems </i>] [-r] <i> infile </i> <i> outfile </i></dl>
<h2>DESCRIPTION</h2>
<p> The <code>nccopy</code> utility copies an input netCDF file in any supported format variant to an output netCDF file, optionally converting the output to any compatible netCDF format variant, compressing the data, or rechunking the data. For example, if built with the netCDF-3 library, a netCDF classic file may be copied to a netCDF 64-bit offset file, permitting larger variables. If built with the netCDF-4 library, a netCDF classic file may be copied to a netCDF-4 file or to a netCDF-4 classic model file as well, permitting data compression, efficient schema changes, larger variable sizes, and use of other netCDF-4 features. </p>
<p> If no output format is specified, with either -k <i>kind_name</i> or <i>-kind_code</i>, then the output will use the same format as the input, unless the input is classic or 64-bit offset and either chunking or compression is specified, in which case the output will be netCDF-4 classic model format. Attempting some kinds of format conversion will result in an error, if the conversion is not possible. For example, an attempt to copy a netCDF-4 file that uses features of the enhanced model, such as groups or variable-length strings, to any of the other kinds of netCDF formats that use the classic model will result in an error. </p>
<p> <code>nccopy</code> also serves as an example of a generic netCDF-4 program, with its ability to read any valid netCDF file and handle nested groups, strings, and user-defined types, including arbitrarily nested compound types, variable-length types, and data of any valid netCDF-4 type. </p>
<p> If DAP support was enabled when <code>nccopy</code> was built, the file name may specify a DAP URL. This may be used to convert data on DAP servers to local netCDF files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code> -k </code> <i> kind_name </i></p>
<dd> Use format name to specify the kind of file to be created and, by inference, the data model (i.e. netcdf-3 (classic) or netcdf-4 (enhanced)). The possible arguments are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&#8216;nc3&#8217; or &#8216;classic&#8217; =&gt; netCDF classic format</p>
<dd>
<dt>&#8216;nc6&#8242; or &#8217;64-bit offset&#8217; =&gt; netCDF 64-bit format</p>
<dd>
<dt>&#8216;nc4&#8217; or &#8216;netCDF-4&#8217; =&gt; netCDF-4 format (enhanced data model)</p>
<dd>
<dt>&#8216;nc7&#8217; or &#8216;netCDF-4 classic model&#8217; =&gt; netCDF-4 classic model format</p>
<dd></dl>
</dl>
</dl>
<dt>
<dd> Note: The old format numbers &#8216;1&#8217;, &#8216;2&#8217;, &#8216;3&#8217;, &#8216;4&#8217;, equivalent to the format names &#8216;nc3&#8217;, &#8216;nc6&#8217;, &#8216;nc4&#8217;, or &#8216;nc7&#8217; respectively, are also still accepted but deprecated, due to easy confusion between format numbers and format names.</p>
<dt>[<code>&#8211;</code><i>kind_code</i>]</p>
<dd> Use format numeric code (instead of format name) to specify the kind of file to be created and, by inference, the data model (i.e. netcdf-3 (classic) versus netcdf-4 (enhanced)). The numeric codes are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>3 =&gt; netcdf classic format</p>
<dd>
<dt>6 =&gt; netCDF 64-bit format</p>
<dd>
<dt>4 =&gt; netCDF-4 format (enhanced data model)</p>
<dd>
<dt>7 =&gt; netCDF-4 classic model format</p>
<dd></dl>
</dl>
</dl>
<p> The numeric code &quot;7&quot; is used because &quot;7=3+4&quot;, specifying the format that uses the netCDF-3 data model for compatibility with the netCDF-4 storage format for performance. Credit is due to NCO for use of these numeric codes instead of the old and confusing format numbers.</p>
<dt><code> -d </code> <i> n </i></p>
<dd> For netCDF-4 output, including netCDF-4 classic model, specify deflation level (level of compression) for variable data output. 0 corresponds to no compression and 9 to maximum compression, with higher levels of compression requiring marginally more time to compress or uncompress than lower levels. Compression achieved may also depend on output chunking parameters. If this option is specified for a classic format or 64-bit offset format input file, it is not necessary to also specify that the output should be netCDF-4 classic model, as that will be the default. If this option is not specified and the input file has compressed variables, the compression will still be preserved in the output, using the same chunking as in the input by default.</p>
<dt>
<dd> Note that <code>nccopy</code> requires all variables to be compressed using the same compression level, but the API has no such restriction. With a program you can customize compression for each variable independently.</p>
<dt><code> -s </code></p>
<dd> For netCDF-4 output, including netCDF-4 classic model, specify shuffling of variable data bytes before compression or after decompression. Shuffling refers to interlacing of bytes in a chunk so that the first bytes of all values are contiguous in storage, followed by all the second bytes, and so on, which often improves compression. This option is ignored unless a non-zero deflation level is specified. Using -d0 to specify no deflation on input data that has been compressed and shuffled turns off both compression and shuffling in the output.</p>
<dt><code> -u </code></p>
<dd> Convert any unlimited size dimensions in the input to fixed size dimensions in the output. This can speed up variable-at-a-time access, but slow down record-at-a-time access to multiple variables along an unlimited dimension.</p>
<dt><code> -w </code></p>
<dd> Keep output in memory (as a diskless netCDF file) until output is closed, at which time output file is written to disk. This can greatly speedup operations such as converting unlimited dimension to fixed size (-u option), chunking, rechunking, or compressing the input. It requires that available memory is large enough to hold the output file. This option may provide a larger speedup than careful tuning of the -m, -h, or -e options, and it&#8217;s certainly a lot simpler.</p>
<dt><code> -c </code> <i>chunkspec</i></p>
<dd> For netCDF-4 output, including netCDF-4 classic model, specify chunking (multidimensional tiling) for variable data in the output. This is useful to specify the units of disk access, compression, or other filters such as checksums. Changing the chunking in a netCDF file can also greatly speedup access, by choosing chunk shapes that are appropriate for the most common access patterns.</p>
<dt>
<dd> The <i>chunkspec</i> argument is a string of comma-separated associations, each specifying a dimension name, a &#8216;/&#8217; character, and optionally the corresponding chunk length for that dimension. No blanks should appear in the chunkspec string, except possibly escaped blanks that are part of a dimension name. A chunkspec names at least one dimension, and may omit dimensions which are not to be chunked or for which the default chunk length is desired. If a dimension name is followed by a &#8216;/&#8217; character but no subsequent chunk length, the actual dimension length is assumed. If copying a classic model file to a netCDF-4 output file and not naming all dimensions in the chunkspec, unnamed dimensions will also use the actual dimension length for the chunk length. An example of a chunkspec for variables that use &#8216;m&#8217; and &#8216;n&#8217; dimensions might be &#8216;m/100,n/200&#8217; to specify 100 by 200 chunks. To see the chunking resulting from copying with a chunkspec, use the &#8216;-s&#8217; option of ncdump on the output file.</p>
<dt>
<dd> The chunkspec &#8216;/&#8217; that omits all dimension names and corresponding chunk lengths specifies that no chunking is to occur in the output, so can be used to unchunk all the chunked variables. To see the chunking resulting from copying with a chunkspec, use the &#8216;-s&#8217; option of ncdump on the output file.</p>
<dt>
<dd> As an I/O optimization, <code>nccopy</code> has a threshold for the minimum size of non-record variables that get chunked, currently 8192 bytes. In the future, use of this threshold and its size may be settable in an option.</p>
<dt>
<dd> Note that <code>nccopy</code> requires variables that share a dimension to also share the chunk size associated with that dimension, but the programming interface has no such restriction. If you need to customize chunking for variables independently, you will need to use the library API in a custom utility program.</p>
<dt><code> -v </code> <i> var1,&#8230; </i></p>
<dd> The output will include data values for the specified variables, in addition to the declarations of all dimensions, variables, and attributes. One or more variables must be specified by name in the comma-delimited list following this option. The list must be a single argument to the command, hence cannot contain unescaped blanks or other white space characters. The named variables must be valid netCDF variables in the input-file. A variable within a group in a netCDF-4 file may be specified with an absolute path name, such as &quot;/GroupA/GroupA2/var&quot;. Use of a relative path name such as &#8216;var&#8217; or &quot;grp/var&quot; specifies all matching variable names in the file. The default, without this option, is to include data values for <i> all </i> variables in the output.</p>
<dt><code> -V </code> <i> var1,&#8230; </i></p>
<dd> The output will include the specified variables only but all dimensions and global or group attributes. One or more variables must be specified by name in the comma-delimited list following this option. The list must be a single argument to the command, hence cannot contain unescaped blanks or other white space characters. The named variables must be valid netCDF variables in the input-file. A variable within a group in a netCDF-4 file may be specified with an absolute path name, such as &#8216;/GroupA/GroupA2/var&#8217;. Use of a relative path name such as &#8216;var&#8217; or &#8216;grp/var&#8217; specifies all matching variable names in the file. The default, without this option, is to include <i> all </i> variables in the output.</p>
<dt><code> -g </code> <i> grp1,&#8230; </i></p>
<dd> The output will include data values only for the specified groups. One or more groups must be specified by name in the comma-delimited list following this option. The list must be a single argument to the command. The named groups must be valid netCDF groups in the input-file. The default, without this option, is to include data values for all groups in the output.</p>
<dt><code> -G </code> <i> grp1,&#8230; </i></p>
<dd> The output will include only the specified groups. One or more groups must be specified by name in the comma-delimited list following this option. The list must be a single argument to the command. The named groups must be valid netCDF groups in the input-file. The default, without this option, is to include all groups in the output.</p>
<dt><code> -m </code> <i> bufsize </i></p>
<dd> An integer or floating-point number that specifies the size, in bytes, of the copy buffer used to copy large variables. A suffix of K, M, G, or T multiplies the copy buffer size by one thousand, million, billion, or trillion, respectively. The default is 5 Mbytes, but will be increased if necessary to hold at least one chunk of netCDF-4 chunked variables in the input file. You may want to specify a value larger than the default for copying large files over high latency networks. Using the &#8216;-w&#8217; option may provide better performance, if the output fits in memory.</p>
<dt><code> -h </code> <i> chunk_cache </i></p>
<dd> For netCDF-4 output, including netCDF-4 classic model, an integer or floating-point number that specifies the size in bytes of chunk cache allocated for each chunked variable. This is not a property of the file, but merely a performance tuning parameter for avoiding compressing or decompressing the same data multiple times while copying and changing chunk shapes. A suffix of K, M, G, or T multiplies the chunk cache size by one thousand, million, billion, or trillion, respectively. The default is 4.194304 Mbytes (or whatever was specified for the configure-time constant CHUNK_CACHE_SIZE when the netCDF library was built). Ideally, the <code>nccopy</code> utility should accept only one memory buffer size and divide it optimally between a copy buffer and chunk cache, but no general algorithm for computing the optimum chunk cache size has been implemented yet. Using the &#8216;-w&#8217; option may provide better performance, if the output fits in memory.</p>
<dt><code> -e </code> <i> cache_elems </i></p>
<dd> For netCDF-4 output, including netCDF-4 classic model, specifies number of chunks that the chunk cache can hold. A suffix of K, M, G, or T multiplies the number of chunks that can be held in the cache by one thousand, million, billion, or trillion, respectively. This is not a property of the file, but merely a performance tuning parameter for avoiding compressing or decompressing the same data multiple times while copying and changing chunk shapes. The default is 1009 (or whatever was specified for the configure-time constant CHUNK_CACHE_NELEMS when the netCDF library was built). Ideally, the <code>nccopy</code> utility should determine an optimum value for this parameter, but no general algorithm for computing the optimum number of chunk cache elements has been implemented yet.</p>
<dt><code> -r </code></p>
<dd> Read netCDF classic or 64-bit offset input file into a diskless netCDF file in memory before copying. Requires that input file be small enough to fit into memory. For <code>nccopy</code>, this doesn&#8217;t seem to provide any significant speedup, so may not be a useful option.</dl>
<h2>EXAMPLES</h2>
<p> Make a copy of foo1.nc, a netCDF file of any type, to foo2.nc, a netCDF file of the same type:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>nccopy foo1.nc foo2.nc</dl>
</dl>
<p> Note that the above copy will not be as fast as use of cp or other simple copy utility, because the file is copied using only the netCDF API. If the input file has extra bytes after the end of the netCDF data, those will not be copied, because they are not accessible through the netCDF interface. If the original file was generated in &quot;No fill&quot; mode so that fill values are not stored for padding for data alignment, the output file may have different padding bytes. </p>
<p> Convert a netCDF-4 classic model file, compressed.nc, that uses compression, to a netCDF-3 file classic.nc:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>nccopy -k classic compressed.nc classic.nc</dl>
</dl>
<p> Note that &#8216;nc3&#8217; could be used instead of &#8216;classic&#8217;. </p>
<p> Download the variable &#8216;time_bnds&#8217; and its associated attributes from an OPeNDAP server and copy the result to a netCDF file named &#8216;tb.nc&#8217;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>nccopy &#8216;<a rel="nofollow" href="http://test.opendap.org/opendap/data/nc/sst.mnmean.nc.gz?time_bnds'">http://test.opendap.org/opendap/data/nc/sst.mnmean.nc.gz?time_bnds&#8217;</a> tb.nc</dl>
</dl>
<p> Note that URLs that name specific variables as command-line arguments should generally be quoted, to avoid the shell interpreting special characters such as &#8216;?&#8217;. </p>
<p> Compress all the variables in the input file foo.nc, a netCDF file of any type, to the output file bar.nc:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>nccopy -d1 foo.nc bar.nc</dl>
</dl>
<p> If foo.nc was a classic or 64-bit offset netCDF file, bar.nc will be a netCDF-4 classic model netCDF file, because the classic and 64-bit offset format variants don&#8217;t support compression. If foo.nc was a netCDF-4 file with some variables compressed using various deflation levels, the output will also be a netCDF-4 file of the same type, but all the variables, including any uncompressed variables in the input, will now use deflation level 1. </p>
<p> Assume the input data includes gridded variables that use time, lat, lon dimensions, with 1000 times by 1000 latitudes by 1000 longitudes, and that the time dimension varies most slowly. Also assume that users want quick access to data at all times for a small set of lat-lon points. Accessing data for 1000 times would typically require accessing 1000 disk blocks, which may be slow. </p>
<p> Reorganizing the data into chunks on disk that have all the time in each chunk for a few lat and lon coordinates would greatly speed up such access. To chunk the data in the input file slow.nc, a netCDF file of any type, to the output file fast.nc, you could use;</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>nccopy -c time/1000,lat/40,lon/40 slow.nc fast.nc</dl>
</dl>
<p> to specify data chunks of 1000 times, 40 latitudes, and 40 longitudes. If you had enough memory to contain the output file, you could speed up the rechunking operation significantly by creating the output in memory before writing it to disk on close:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>nccopy -w -c time/1000,lat/40,lon/40 slow.nc fast.nc</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ncdump/">ncdump</a>(1),</code><a href="/docs/linux/man/1-ncgen/">ncgen</a>(1),<code><a href="/docs/linux/man/3-netcdf/">netcdf</a>(3)</code> </p>
<h2>Index</h2>
