---
title: "dpkgcompressionfilehandle(3)"
name: "dpkgcompressionfilehandle"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgcompressionfilehandle/"
description: "Dpkg::Compression::FileHandle – object dealing transparently with file compression"
---

<p>Dpkg::Compression::FileHandle &#8211; object dealing transparently with file compression </p>
<h2>Synopsis</h2>
<pre> use Dpkg::Compression::FileHandle;
 $fh = Dpkg::Compression::FileHandle-&gt;new(filename =&gt; 'sample.gz');
 print $fh &quot;Something
&quot;;
 close $fh;
 $fh = Dpkg::Compression::FileHandle-&gt;new();
 open($fh, '&gt;', 'sample.bz2');
 print $fh &quot;Something
&quot;;
 close $fh;
 $fh = Dpkg::Compression::FileHandle-&gt;new();
 $fh-&gt;open('sample.xz', 'w');
 $fh-&gt;print(&quot;Something
&quot;);
 $fh-&gt;close();
 $fh = Dpkg::Compression::FileHandle-&gt;new(filename =&gt; 'sample.gz');
 my @lines = &lt;$fh&gt;;
 close $fh;
 $fh = Dpkg::Compression::FileHandle-&gt;new();
 open($fh, '&lt;', 'sample.bz2');
 my @lines = &lt;$fh&gt;;
 close $fh;
 $fh = Dpkg::Compression::FileHandle-&gt;new();
 $fh-&gt;open('sample.xz', 'r');
 my @lines = $fh-&gt;getlines();
 $fh-&gt;close();</pre>
<h2>Description</h2>
<p>Dpkg::Compression::FileHandle is an object that can be used like any filehandle and that deals transparently with compressed files. By default, the compression scheme is guessed from the filename but you can override this behaviour with the method <tt>&quot;set_compression&quot;</tt>. </p>
<p> If you don&#8217;t open the file explicitly, it will be auto-opened on the first read or write operation based on the filename set at creation time (or later with the <tt>&quot;set_filename&quot;</tt> method). </p>
<p> Once a file has been opened, the filehandle must be closed before being able to open another file.</p>
<h2>Standard Functions</h2>
<p>The standard functions acting on filehandles should accept a Dpkg::Compression::FileHandle object transparently including <tt>&quot;open&quot;</tt> (only when using the variant with 3 parameters), <tt>&quot;close&quot;</tt>, <tt>&quot;binmode&quot;</tt>, <tt>&quot;eof&quot;</tt>, <tt>&quot;fileno&quot;</tt>, <tt>&quot;getc&quot;</tt>, <tt>&quot;print&quot;</tt>, <tt>&quot;printf&quot;</tt>, <tt>&quot;read&quot;</tt>, <tt>&quot;sysread&quot;</tt>, <tt>&quot;say&quot;</tt>, <tt>&quot;write&quot;</tt>, <tt>&quot;syswrite&quot;</tt>, <tt>&quot;seek&quot;</tt>, <tt>&quot;sysseek&quot;</tt>, <tt>&quot;tell&quot;</tt>. </p>
<p> Note however that <tt>&quot;seek&quot;</tt> and <tt>&quot;sysseek&quot;</tt> will only work on uncompressed files as compressed files are really pipes to the compressor programs and you can&#8217;t seek on a pipe.</p>
<h2>FileHandle METHODS</h2>
<p>The object inherits from FileHandle so all methods that work on this object should work for Dpkg::Compression::FileHandle too. There may be exceptions though.</p>
<h2>Public Methods</h2>
<dl COMPACT>
<dt>my $fh = Dpkg::Compression::FileHandle-&gt;new(%opts)</p>
<dd>Creates a new filehandle supporting on-the-fly compression/decompression. Supported options are &#8220;filename&#8221;, &#8220;compression&#8221;, &#8220;compression_level&#8221; (see respective set_* functions) and &#8220;add_comp_ext&#8221;. If &#8220;add_comp_ext&#8221; evaluates to true, then the extension corresponding to the selected compression scheme is automatically added to the recorded filename. It&#8217;s obviously incompatible with automatic detection of the compression method.</p>
<dt>$fh-&gt;ensure_open($mode, %opts)</p>
<dd>Ensure the file is opened in the requested mode (&#8220;r&#8221; for read and &#8220;w&#8221; for write). The options are passed down to the compressor&#8217;s <i>spawn()</i> call, if one is used. Opens the file with the recorded filename if needed. If the file is already open but not in the requested mode, then it errors out.</p>
<dt>$fh-&gt;set_compression($comp)</p>
<dd>Defines the compression method used. <tt>$comp</tt> should one of the methods supported by <code>Dpkg::Compression</code> or &#8220;none&#8221; or &#8220;auto&#8221;. &#8220;none&#8221; indicates that the file is uncompressed and &#8220;auto&#8221; indicates that the method must be guessed based on the filename extension used.</p>
<dt>$fh-&gt;set_compression_level($level)</p>
<dd>Indicate the desired compression level. It should be a value accepted by the function <tt>&quot;compression_is_valid_level&quot;</tt> of <code>Dpkg::Compression</code>.</p>
<dt>$fh-&gt;set_filename($name, [$add_comp_ext])</p>
<dd>Use <tt>$name</tt> as filename when the file must be opened/created. If <tt>$add_comp_ext</tt> is passed, it indicates whether the default extension of the compression method must be automatically added to the filename (or not).</p>
<dt>my $file = $fh-&gt;<i>get_filename()</i></p>
<dd>Returns the filename that would be used when the filehandle must be opened (both in read and write mode). This function errors out if &#8220;add_comp_ext&#8221; is enabled while the compression method is set to &#8220;auto&#8221;. The returned filename includes the extension of the compression method if &#8220;add_comp_ext&#8221; is enabled.</p>
<dt>$ret = $fh-&gt;<i>use_compression()</i></p>
<dd>Returns &#8220;0&#8221; if no compression is used and the compression method used otherwise. If the compression is set to &#8220;auto&#8221;, the value returned depends on the extension of the filename obtained with the <code>get_filename</code> method.</p>
<dt>my $real_fh = $fh-&gt;<i>get_filehandle()</i></p>
<dd>Returns the real underlying filehandle. Useful if you want to pass it along in a derived object.</dl>
<h2>Derived Objects</h2>
<p>If you want to create an object that inherits from Dpkg::Compression::FileHandle you must be aware that the object is a reference to a <font SIZE="-1">GLOB</font> that is returned by <i>Symbol::gensym()</i> and as such it&#8217;s not a <font SIZE="-1">HASH.</font> </p>
<p> You can store internal data in a hash but you have to use <tt>&quot;*$self-&quot;</tt>{&#8230;}&gt; to access the associated hash like in the example below: </p>
<pre> sub set_option {
 my ($self, $value) = @_;
 *$self-&gt;{option} = $value;
 }</pre>
<h2>Changes</h2>
<h3>Version 1.01</h3>
<p>New argument: <tt>$fh</tt>-&gt;<i>ensure_open()</i> accepts an <tt>%opts</tt> argument.</p>
<h3>Version 1.00</h3>
<p>Mark the module as public.</p>
<h2>Author</h2>
<p>Raphaël Hertzog &lt;hertzog [at] debian.org&gt;</p>
