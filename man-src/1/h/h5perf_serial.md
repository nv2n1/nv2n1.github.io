---
title: "h5perf_serial(1)"
name: "h5perf_serial"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5perf_serial/"
description: "h5perf_serial: – Measures HDF5 serial performance."
---

<h2>NAME</h2>
<p> h5perf_serial: &#8211; Measures HDF5 serial performance.</p>
<h2>DESCRIPTION</h2>
<p> h5perf_serial: Version 1.8.7 usage: h5perf_serial [OPTIONS]</p>
<dl>
<dt>
</dt><dd> OPTIONS</dd>
<dt><code>-h</code></dt>
<dd> Print an usage message and exit</dd>
<dt><code>-A</code> AL</dt>
<dd> Which APIs to test [default: all of them]</dd>
<dt><code>-c</code> SL</dt>
<dd> Selects chunked storage and defines chunks dimensions and sizes [default: Off]</dd>
<dt><code>-e</code> SL</dt>
<dd> Dimensions and sizes of dataset [default: 100,200]</dd>
<dt><code>-i</code> N</dt>
<dd> Number of iterations to perform [default: 1]</dd>
<dt><code>-r</code> NL</dt>
<dd> Dimension access order (see below for description) [default: 1,2]</dd>
<dt><code>-t</code></dt>
<dd> Selects extendable dimensions for HDF5 dataset [default: Off]</dd>
<dt><code>-v</code> VFD</dt>
<dd> Selects file driver for HDF5 access [default: sec2]</dd>
<dt><code>-w</code></dt>
<dd> Perform write tests, not the read tests [default: Off]</dd>
<dt><code>-x</code> SL</dt>
<dd> Dimensions and sizes of the transfer buffer [default: 10,20]</dd>
<dt>N</dt>
<dd> &#8211; is an integer &gt; 0.</dd>
<dt>S</dt>
<dd> &#8211; is a size specifier, an integer &gt; 0 followed by a size indicator:</dd>
<dt>
</dt><dd> K &#8211; Kilobyte (1024) M &#8211; Megabyte (1048576) G &#8211; Gigabyte (1073741824)</dd>
<dt>
</dt><dd> Example: &#8217;37M&#8217; is 37 megabytes or 38797312 bytes</dd>
<dt>
</dt><dd> AL &#8211; is an API list. Valid values are:</dd>
<dt>
</dt><dd> hdf5 &#8211; HDF5 posix &#8211; POSIX</dd>
<dt>
</dt><dd> Example: <code>-A</code> posix,hdf5</dd>
<dt>
</dt><dd> NL &#8211; is list of integers (N) separated by commas.</dd>
<dt>
</dt><dd> Example: 1,2,3</dd>
<dt>
</dt><dd> SL &#8211; is list of size specifiers (S) separated by commas.</dd>
<dt>
</dt><dd> Example: 2K,2K,3K</dd>
<dt>
</dt><dd> The example defines an object (dataset, tranfer buffer) with three dimensions. Be aware that as the number of dimensions increases, the the total size of the object increases exponentially.</dd>
<dt>VFD</dt>
<dd> &#8211; is an HDF5 file driver specifier. Valid values are:</dd>
<dt>
</dt><dd> sec2, stdio, core, split, multi, family, direct</dd>
<dt>
</dt><dd> Dimension access order:</dd>
<dt>
</dt><dd> Data access starts at the cardinal origin of the dataset using the transfer buffer. The next access occurs on a dataset region next to the previous one. For a multidimensional dataset, there are several directions as to where to proceed. This can be specified in the dimension access order. For example, <code>-r</code> 1,2 states that the tool should traverse dimension 1 first, and then dimension 2.</dd>
<dt>
</dt><dd> Environment variables:</dd>
<dt>HDF5_NOCLEANUP</dt>
<dd> Do not remove data files if set [default remove]</dd>
<dt>HDF5_PREFIX</dt>
<dd> Data file prefix</dd></dl>
<p> usage: h5perf_serial [OPTIONS]</p>
<dl>
<dt>
</dt><dd> OPTIONS</dd>
<dt><code>-h</code></dt>
<dd> Print an usage message and exit</dd>
<dt><code>-A</code> AL</dt>
<dd> Which APIs to test [default: all of them]</dd>
<dt><code>-c</code> SL</dt>
<dd> Selects chunked storage and defines chunks dimensions and sizes [default: Off]</dd>
<dt><code>-e</code> SL</dt>
<dd> Dimensions and sizes of dataset [default: 100,200]</dd>
<dt><code>-i</code> N</dt>
<dd> Number of iterations to perform [default: 1]</dd>
<dt><code>-r</code> NL</dt>
<dd> Dimension access order (see below for description) [default: 1,2]</dd>
<dt><code>-t</code></dt>
<dd> Selects extendable dimensions for HDF5 dataset [default: Off]</dd>
<dt><code>-v</code> VFD</dt>
<dd> Selects file driver for HDF5 access [default: sec2]</dd>
<dt><code>-w</code></dt>
<dd> Perform write tests, not the read tests [default: Off]</dd>
<dt><code>-x</code> SL</dt>
<dd> Dimensions and sizes of the transfer buffer [default: 10,20]</dd>
<dt>N</dt>
<dd> &#8211; is an integer &gt; 0.</dd>
<dt>S</dt>
<dd> &#8211; is a size specifier, an integer &gt; 0 followed by a size indicator:</dd>
<dt>
</dt><dd> K &#8211; Kilobyte (1024) M &#8211; Megabyte (1048576) G &#8211; Gigabyte (1073741824)</dd>
<dt>
</dt><dd> Example: &#8217;37M&#8217; is 37 megabytes or 38797312 bytes</dd>
<dt>
</dt><dd> AL &#8211; is an API list. Valid values are:</dd>
<dt>
</dt><dd> hdf5 &#8211; HDF5 posix &#8211; POSIX</dd>
<dt>
</dt><dd> Example: <code>-A</code> posix,hdf5</dd>
<dt>
</dt><dd> NL &#8211; is list of integers (N) separated by commas.</dd>
<dt>
</dt><dd> Example: 1,2,3</dd>
<dt>
</dt><dd> SL &#8211; is list of size specifiers (S) separated by commas.</dd>
<dt>
</dt><dd> Example: 2K,2K,3K</dd>
<dt>
</dt><dd> The example defines an object (dataset, tranfer buffer) with three dimensions. Be aware that as the number of dimensions increases, the the total size of the object increases exponentially.</dd>
<dt>VFD</dt>
<dd> &#8211; is an HDF5 file driver specifier. Valid values are:</dd>
<dt>
</dt><dd> sec2, stdio, core, split, multi, family, direct</dd>
<dt>
</dt><dd> Dimension access order:</dd>
<dt>
</dt><dd> Data access starts at the cardinal origin of the dataset using the transfer buffer. The next access occurs on a dataset region next to the previous one. For a multidimensional dataset, there are several directions as to where to proceed. This can be specified in the dimension access order. For example, <code>-r</code> 1,2 states that the tool should traverse dimension 1 first, and then dimension 2.</dd>
<dt>
</dt><dd> Environment variables:</dd>
<dt>HDF5_NOCLEANUP</dt>
<dd> Do not remove data files if set [default remove]</dd>
<dt>HDF5_PREFIX</dt>
<dd> Data file prefix</dd></dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>h5perf_serial:</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>h5perf_serial:</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info h5perf_serial:</code></dd></dl>
<p> should give you access to the complete manual. </p>
