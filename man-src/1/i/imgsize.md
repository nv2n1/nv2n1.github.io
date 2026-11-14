---
title: "imgsize(1)"
name: "imgsize"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imgsize/"
description: "imgsize – read the dimensions of an image in several popular formats"
---

<h2 class="name">NAME</h2>
<p> imgsize &#8211; read the dimensions of an image in several popular formats </p>
<h2>USAGE</h2>
<pre><code>
imgsize[-r | -a | -f fmt] file[file...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> No-brainer to size an image supplied on the command-line. All the real work is done in Image::Size.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> <code>imgsize</code> expects file names on the command-line. If more than one file is provided, the file name will be included in the output: </p>
<pre>
    % imgsize dot.gif
    width=&quot;16&quot; height=&quot;16&quot;
    % imgsize dot.gif dash.gif
    dot.gif: width=&quot;16&quot; height=&quot;16&quot;
    dash.gif: width=&quot;32&quot; height=&quot;8&quot;
</pre>
<h2>OPTIONS</h2>
<p> By default, the width and height are returned as attributes for an <font SIZE="-1">IMG</font> tag in <font SIZE="-1">HTML,</font> essentially <tt>&quot;width=&quot;40&quot; height=&quot;30&quot;&quot;</tt> or similar. The following options may be used to return alternate formats (all report width first, then height):</p>
<dl>
<dt>&quot;-r&quot;</p>
<dd> Return &#8220;raw&#8221; format data. Just the numbers separated by a single space.</p>
<dt>&quot;-a&quot;</p>
<dd> Return a Perl-style list of attributes suitable for passing to the <tt>&quot;img()&quot;</tt> method of the <font SIZE="-1">CGI</font> module (see <font SIZE="-1">CGI</font>).</p>
<dt>&quot;-f&quot; <code>fmt</code></p>
<dd> Pass the string specified in <i>fmt</i> to <tt>&quot;sprintf&quot;</tt> and thus use it to format the results to your taste. <tt>&quot;sprintf&quot;</tt> will be passed two numbers, so any other formatting directives will be lost. The numbers are passed as width first, then height.</dl>
<h2>EXIT STATUS</h2>
<p> <code>imgsize</code> always exits</p>
<h2>BUGS</h2>
<p> Please report any bugs or feature requests to <tt>&quot;bug-image-size at rt.cpan.org&quot;</tt>, or through the web interface at &lt;<a rel="nofollow" href="http://rt.cpan.org/NoAuth/ReportBug.html?Queue=Image-Size">http://rt.cpan.org/NoAuth/ReportBug.html?Queue=Image-Size</a>&gt;. I will be notified, and then you&#8217;ll automatically be notified of progress on your bug as I make changes.</p>
<h2>SUPPORT</h2>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">RT: CPAN</font>&#8216;s request tracker </p>
<p> &lt;<a rel="nofollow" href="http://rt.cpan.org/NoAuth/Bugs.html?Dist=Image-Size">http://rt.cpan.org/NoAuth/Bugs.html?Dist=Image-Size</a>&gt;</p>
<dt>&bull;</p>
<dd> AnnoCPAN: Annotated <font SIZE="-1">CPAN</font> documentation </p>
<p> &lt;<a rel="nofollow" href="http://annocpan.org/dist/Image-Size">http://annocpan.org/dist/Image-Size</a>&gt;</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">CPAN</font> Ratings </p>
<p> &lt;<a rel="nofollow" href="http://cpanratings.perl.org/d/Image-Size">http://cpanratings.perl.org/d/Image-Size</a>&gt;</p>
<dt>&bull;</p>
<dd> Search <font SIZE="-1">CPAN</font> </p>
<p> &lt;<a rel="nofollow" href="http://search.cpan.org/dist/Image-Size">http://search.cpan.org/dist/Image-Size</a>&gt;</p>
<dt>&bull;</p>
<dd> Project page on GitHub </p>
<p> &lt;<a rel="nofollow" href="http://github.com/rjray/image-size">http://github.com/rjray/image-size</a>&gt;</dl>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copying and distribution are permitted under the terms of the Artistic License 2.0 (&lt;<a rel="nofollow" href="http://www.opensource.org/licenses/artistic-license-2.0.php">http://www.opensource.org/licenses/artistic-license-2.0.php</a>&gt;) or the <font SIZE="-1">GNU LGPL 2.1 </font>(&lt;<a rel="nofollow" href="http://www.opensource.org/licenses/lgpl-2.1.php">http://www.opensource.org/licenses/lgpl-2.1.php</a>&gt;).</p>
<h2>SEE ALSO</h2>
<p> Image::Size</p>
<h2>AUTHOR</h2>
<p> Randy J. Ray <tt>&quot;&lt;rjray [at] blackperl.com&gt;&quot;</tt>. </p>
<h2>Index</h2>
