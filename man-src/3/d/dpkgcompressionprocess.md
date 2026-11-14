---
title: "dpkgcompressionprocess(3)"
name: "dpkgcompressionprocess"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgcompressionprocess/"
description: "Dpkg::Compression::Process – run compression/decompression processes"
---

<p>Dpkg::Compression::Process &#8211; run compression/decompression processes </p>
<h2>Description</h2>
<p>This module provides an object oriented interface to run and manage compression/decompression processes.</p>
<h2>Methods</h2>
<dl COMPACT>
<dt>my $proc = Dpkg::Compression::Process-&gt;new(%opts)</p>
<dd>Create a new instance of the object. Supported options are &#8220;compression&#8221; and &#8220;compression_level&#8221; (see corresponding set_* functions).</p>
<dt>$proc-&gt;set_compression($comp)</p>
<dd>Select the compression method to use. It errors out if the method is not supported according to <tt>&quot;compression_is_supported&quot;</tt> (of <code>Dpkg::Compression</code>).</p>
<dt>$proc-&gt;set_compression_level($level)</p>
<dd>Select the compression level to use. It errors out if the level is not valid according to <tt>&quot;compression_is_valid_level&quot;</tt> (of <code>Dpkg::Compression</code>).</p>
<dt>my @exec = $proc-&gt;<i>get_compress_cmdline()</i></p>
<dd>
<dt>my @exec = $proc-&gt;<i>get_uncompress_cmdline()</i></p>
<dd>Returns a list ready to be passed to <tt>&quot;exec&quot;</tt>, its first element is the program name (either for compression or decompression) and the following elements are parameters for the program. </p>
<p> When executed the program acts as a filter between its standard input and its standard output.</p>
<dt>$proc-&gt;compress(%opts)</p>
<dd>Starts a compressor program. You must indicate where it will read its uncompressed data from and where it will write its compressed data to. This is accomplished by passing one parameter <tt>&quot;to_*&quot;</tt> and one parameter <tt>&quot;from_*&quot;</tt> as accepted by <code>Dpkg::IPC::spawn</code>. </p>
<p> You must call <tt>&quot;wait_end_process&quot;</tt> after having called this method to properly close the sub-process (and verify that it exited without error).</p>
<dt>$proc-&gt;uncompress(%opts)</p>
<dd>Starts a decompressor program. You must indicate where it will read its compressed data from and where it will write its uncompressed data to. This is accomplished by passing one parameter <tt>&quot;to_*&quot;</tt> and one parameter <tt>&quot;from_*&quot;</tt> as accepted by <code>Dpkg::IPC::spawn</code>. </p>
<p> You must call <tt>&quot;wait_end_process&quot;</tt> after having called this method to properly close the sub-process (and verify that it exited without error).</p>
<dt>$proc-&gt;wait_end_process(%opts)</p>
<dd>Call <code>Dpkg::IPC::wait_child</code> to wait until the sub-process has exited and verify its return code. Any given option will be forwarded to the <tt>&quot;wait_child&quot;</tt> function. Most notably you can use the &#8220;nocheck&#8221; option to verify the return code yourself instead of letting <tt>&quot;wait_child&quot;</tt> do it for you.</dl>
<h2>Changes</h2>
<h3>Version 1.00</h3>
<p>Mark the module as public.</p>
<h2>Author</h2>
<p>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;.</p>
