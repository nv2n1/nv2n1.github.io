---
title: "djvu(1)"
name: "djvu"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvu/"
description: "DjVu – DjVu and DjVuLibre."
---

<h2 class="name">NAME</h2>
<p> DjVu &#8211; DjVu and DjVuLibre.</p>
<h2>INTRODUCTION</h2>
<p> Although the Internet has given us a worldwide infrastructure on which to build the universal library, much of the world knowledge, history, and literature is still trapped on paper in the basements of the world&#8217;s traditional libraries. Many libraries and content owners are in the process of digitizing their collections. While many such efforts involve the painstaking process of converting paper documents to computer-friendly form, such as <font SIZE="-1">SGML</font> based formats, the high cost of such conversions limits their extent. Scanning documents, and distributing the resulting images electronically is not only considerably cheaper, but also more faithful to the original document because it preserves its visual aspect. </p>
<p> Despite the quickly improving speed of network connections and computers, the number of scanned document images accessible on the Web today is relatively small. There are several reasons for this. </p>
<p> The first reason is the relatively high cost of scanning anything else but unbound sheets in black and white. This problem is slowly going away with the appearance of fast and low-cost color scanners with sheet feeders. </p>
<p> The second reason is that long-established image compression standards and file formats have proved inadequate for distributing scanned documents at high resolution, particularly color documents. Not only are the file sizes and download times impractical, the decoding and rendering times are also prohibitive. A typical magazine page scanned in color at 100 dpi in <font SIZE="-1">JPEG</font> would typically occupy 100 <font SIZE="-1">KB</font> to 200 <font SIZE="-1">KB</font> , but the text would be hardly readable: insufficient for screen viewing and totally unacceptable for printing. The same page at 300 dpi would have sufficient quality for viewing and printing, but the file size would be 300 <font SIZE="-1">KB</font> to 1000 <font SIZE="-1">KB</font> at best, which is impractical for remote access. Another major problem is that a fully decoded 300 dpi color images of a letter-size page occupies 24 <font SIZE="-1">MB</font> of memory and easily causes disk swapping. </p>
<p> The third reason is that digital documents are more than just a collection of individual page images. Pages in a scanned documents have a natural serial order. Special provision must be made to ensure that flipping pages be instantaneous and effortless so as to maintain a good user experience. Even more important, most existing document formats force users to download the entire document first before displaying a chosen page. However, users often want to jump to individual pages of the document without waiting for the entire document to download. Efficient browsing requires efficient random page access, fast sequential page flipping, and quick rendering. This can be achieved with a combination of advanced compression, pre-fetching, pre-decoding, caching, and progressive rendering. DjVu decomposes each page into multiple components (text, backgrounds, images, libraries of common shapes&#8230;) that may be shared by several pages and downloaded on demand. All these requirements call for a very sophisticated but parsimonious control mechanism to handle on-demand downloading, pre-fetching, decoding, caching, and progressive rendering of the page images. What is being considered here is not just a document image compression technique, but a whole platform for document delivery. </p>
<p> DjVu is an image compression technique, a document format, and a software platform for delivering documents images over the Internet that fulfills the above requirements. </p>
<h2>DJVU IMAGE COMPRESSION</h2>
<p> The DjVu image compression is based on three technologies:</p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DjVuPhoto</h2>
<p> DjVuPhoto, also known as <font SIZE="-1">IW44,</font> is a wavelet-based continuous-tone image compression technique with progressive decoding/rendering. It is best used for encoding photographic images in colors or in shades of gray. Images are typically half the size as <font SIZE="-1">JPEG</font> for the same distortion.</p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DjVuBitonal</h2>
<p> DjVuBitonal, also known as <font SIZE="-1">JB2,</font> is a bitonal image compression that takes advantage of repetitions of nearly identical shapes on the page (such as characters) to efficiently compress text images. It is best used to compress black and white images representing text and simple drawings. A typical 300 dpi page in DjVuBitonal occupies 5 to 25 <font SIZE="-1">KB</font> (3 to 8 times better than <font SIZE="-1">TIFF-G4</font> or <font SIZE="-1">PDF</font> ).</p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DjVuDocument</h2>
<p> DjVuDocument is a compression technique specifically designed for color digital documents images containing both pictures and text, such as a page of a magazine. DjVuDocument represents images into separately compressed layers. The foreground layer is usually compressed with DjVu Bitonal and contains the text and drawings. The background layer is usually compressed with DjVuPhoto and contains the background texture and the pictures at lower resolution. </p>
<h2>DJVU DOCUMENT DELIVERY PLATFORM</h2>
<p> The DjVu technology is designed from the ground up to support the efficient delivery of digital documents over the Internet. It provides various ways to deal with multi-page documents, and various ways to enrich the content with hyper-links, meta-data, searchable text, etc. </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MIME types</h2>
<p> The DjVu format has an official MIME type of <code>image/vnd.djvu</code>, which is the preferred content-type to be given by http servers for DjVu files. Unofficial mime types used historically are <code>image/x.djvu</code> and <code>image/x-djvu</code>, which may still be encountered. Ideally, clients should be configured to handle all three. (For web server configuration help, see <code><a rel="nofollow" href="http://www.djvuzone.org/support/tutorial/chapter-authoring1.html">http://www.djvuzone.org/support/tutorial/chapter-authoring1.html</a></code>.) </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Bundled multi-page documents</h2>
<p> Bundled multi-page DjVu document uses a single file to represent the entire document. This single file contains all the pages as well as ancillary information (e.g. the page directory, data shared by several pages, thumbnails, etc.). Using a single file format is very convenient for storing documents or for sending email attachments. </p>
<p> When you type the <font SIZE="-1">URL</font> of a multi-page document, the DjVu browser plugin starts downloading the whole file, but displays the first page as soon as it is available. You can immediately navigate to other pages using the DjVu toolbar. Suppose however that the document is stored on a remote web server. You can easily access the first page and see that this is not the document you wanted. Although you will never display the other pages the browser is transferring data for these pages and is wasting the bandwidth of your server (and the bandwidth of the Internet too). You could also see the summary of the document on the first page and jump to page 100. But page 100 cannot be displayed until data for pages 1 to 99 has been received. You may have to wait for the transmission of unnecessary page data. This second problem (the unnecessary wait) can be solved using the &#8220;byte serving&#8221; options of the <font SIZE="-1">HTTP/1.1</font> protocol. This option has to be supported by the web server, the proxies, the caches and the browser. Byte serving however does not solve the first problem (the waste of bandwidth).</p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Indirect multi-page documents</h2>
<p> Indirect multi-page DjVu documents solve both problems. An indirect multi-page DjVu document is composed of several files. The main file is named the index file. You can browse a document using the <font SIZE="-1">URL</font> of the index file, just like you do with a bundled multi-page document. The index file however is very small. It simply contains the document directory and the <font SIZE="-1">URLs</font> of secondary files containing the page data. When you browse an indirect multi-page document, the browser only accesses data for the pages you are viewing. This can be done at a reasonable speed because the browser maintains a cache of pages and sometimes pre-fetches a few pages ahead of the current page. This model uses the web serving bandwidth much more effectively. It also eliminates unnecessary delays when jumping ahead to pages located anywhere in a long document.</p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Annotations</h2>
<p> Every DjVu image optionally includes so-called annotation chunks. The annotation chunk is often used to define hyper-links to other document pages or to arbitrary web pages. Annotation chunks can also be used for other purposes such as setting the initial viewing mode of a page, defining highlighted zones, or storing arbitrary meta-data about the page or the document.</p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hidden text</h2>
<p> Every DjVu image optionally includes a hidden text layer that associated graphical features with the corresponding text. The hidden text layer is usually generated by running an Optical Character Recognition software. This textual information provides for indexing DjVu documents and copying/pasting text from DjVu page images.</p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Thumbnails</h2>
<p> DjVu documents sometimes contain pre-computed page thumbnails.</p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Outline</h2>
<p> DjVu documents sometimes contain a navigation chunk containing an outline, that is, a hierarchical table of contents with pointers to the corresponding document pages. </p>
<h2>DJVUZONE AND DJVULIBRE</h2>
<p> The DjVu technology was initially created by a few researchers in AT&amp;T Labs between 1995 and 1999. Lizardtech, Inc. ( <code><a rel="nofollow" href="http://www.lizardtech.com">http://www.lizardtech.com</a></code> ) then obtained a commercial license from AT&amp;T and continued the development. They have now a variety of solutions for producing and distributing documents using the DjVu technology. </p>
<p> The DjVuZone web site ( <code><a rel="nofollow" href="http://www.djvuzone.org">http://www.djvuzone.org</a></code> ) is managed by the few AT&amp;T Labs researchers who created the DjVu technology in the first place. We promote the DjVu technology by providing an independent source of information about DjVu. </p>
<p> Understanding how little room there is for a proprietary document format, Lizardtech released the DjVu Reference Library under the <font SIZE="-1">GNU</font> Public License in December 2000. This library entirely defines the compression format and the elementary codecs. Six month later, Lizardtech released an updated DjVu Reference Library as well as the source code of the Unix viewer. </p>
<p> These two releases form the basis of our initial DjVuLibre software. We modified the build system to comply with the expectations of the open source community. Various bugs and portability issues have been fixed. We also tried to make it simpler to use and install, while preserving the essential structure of the Lizardtech releases. </p>
<p> The DjVuLibre software contains the following components:</p>
<dl>
<dt><code><a href="/docs/linux/man/1-bzz/">bzz</a></code>(1)</p>
<dd> A general purpose compression command line program. Many internal DjVu data structures are compressed using this technique.</p>
<dt><code><a href="/docs/linux/man/1-c44/">c44</a></code>(1)</p>
<dd> A DjVuPhoto command line encoder. This state-of-the-art wavelet compressor produces DjVuPhoto images from PPM or JPEG images.</p>
<dt><code><a href="/docs/linux/man/1-cjb2/">cjb2</a></code>(1)</p>
<dd> A DjVuBitonal command line encoder. This soft-pattern-matching compressor produces DjVuBitonal images from PBM images. It can encode images without loss, or introduce small changes in order to improve the compression ratio. The lossless encoding mode is competitive with that of the Lizardtech commercial encoders.</p>
<dt><code><a href="/docs/linux/man/1-cpaldjvu/">cpaldjvu</a></code>(1)</p>
<dd> A DjVuDocument command line encoder for images with few colors. This encoder is well suited to compressing images with a small number of distinct colors (e.g. screen-shots). The dominant color is encoded by the background layer. The other colors are encoded by the foreground layer.</p>
<dt><code><a href="/docs/linux/man/1-csepdjvu/">csepdjvu</a></code>(1)</p>
<dd> A DjVuDocument command line encoder for separated images. This encoder takes a file containing pre-segmented foreground and background images and produces a DjVuDocument image.</p>
<dt><code><a href="/docs/linux/man/1-ddjvu/">ddjvu</a></code>(1)</p>
<dd> A command line decoder for DjVu images. This program produces a <font SIZE="-1">PNM</font> image representing any segment of any page of a DjVu document at any resolution.</p>
<dt><code><a href="/docs/linux/man/1-djview/">djview</a></code>(1)</p>
<dd> A stand-alone viewer for DjVu images. This sophisticated viewer displays DjVu documents. It implements document navigation as well as fast zooming and panning.</p>
<dt><code><a href="/docs/linux/man/1-nsdejavu/">nsdejavu</a></code>(1)</p>
<dd> A web browser plugin for viewing DjVu images. This small plugin allows for viewing DjVu documents from web browsers. It internally uses djview to perform the actual work.</p>
<dt><code><a href="/docs/linux/man/1-djvups/">djvups</a></code>(1)</p>
<dd> A command line tool for converting DjVu documents into PostScript .</p>
<dt><code><a href="/docs/linux/man/1-djvm/">djvm</a></code>(1)</p>
<dd> A command line tool for manipulating bundled multi-page DjVu documents. This program is often used to collect individual pages and produce a bundled document.</p>
<dt><code><a href="/docs/linux/man/1-djvmcvt/">djvmcvt</a></code>(1)</p>
<dd> A command line tool for converting bundled documents to indirect documents and conversely.</p>
<dt><code><a href="/docs/linux/man/1-djvused/">djvused</a></code>(1)</p>
<dd> A powerful command line tool for manipulating multi-page documents, creating or editing annotation chunks, creating or editing hidden text layers, pre-computing thumbnail images, and more&#8230;</p>
<dt><code><a href="/docs/linux/man/1-djvutxt/">djvutxt</a></code>(1)</p>
<dd> A command line tool to extract the hidden text from DjVu documents.</p>
<dt><code><a href="/docs/linux/man/1-djvudump/">djvudump</a></code>(1)</p>
<dd> A command line tool for inspecting DjVu files and displaying their internal structure.</p>
<dt><code><a href="/docs/linux/man/1-djvuextract/">djvuextract</a></code>(1)</p>
<dd> A command line tool for dis-assembling DjVu image files.</p>
<dt><code><a href="/docs/linux/man/1-djvumake/">djvumake</a></code>(1)</p>
<dd> A command line tool for assembling DjVu image files.</p>
<dt><code><a href="/docs/linux/man/1-djvuserve/">djvuserve</a></code>(1)</p>
<dd> A <font SIZE="-1">CGI</font> program for generating indirect multi-page DjVu documents on the fly.</p>
<dt><code><a href="/docs/linux/man/1-djvutoxml/">djvutoxml</a></code>(1), <code><a href="/docs/linux/man/1-djvuxmlparser/">djvuxmlparser</a></code>(1)</p>
<dd> Command line tools to edit DjVu metadata as XML files. </p>
</dl>
<h2>DJVU ENCODERS AND ANY2DJVU</h2>
<p> DjVuLibre comes with a variety of specialized encoders, <code><a href="/docs/linux/man/1-c44/">c44</a></code>(1) for photographic images, <code><a href="/docs/linux/man/1-cjb2/">cjb2</a></code>(1) for bitonal images, and <code><a href="/docs/linux/man/1-cpaldjvu/">cpaldjvu</a></code>(1) for images with few distinct colors. Although these encoders perform well in their specialized domain, they cannot handle complex tasks involving segmentation and multipage encoding. </p>
<p> The Lizardtech commercial products (see <code><a rel="nofollow" href="http://www.lizardtech.com/solutions/document">http://www.lizardtech.com/solutions/document</a></code>) can perform these complex encoding tasks </p>
<p> Another solution is provided by the compression server at (<code><a rel="nofollow" href="http://any2djvu.djvuzone.org">http://any2djvu.djvuzone.org</a></code>). This machine uses pre-lizardtech prototype encoders from AT&amp;T Labs and performs almost as well as the commercial Lizardtech encoders. Please note that the Any2DjVu compression server comes with no guarantee, that nothing is done to ensure that your documents will remain confidential, and that there is only one computer working for the whole planet. </p>
<h2>CREDITS</h2>
<p> Numerous people have contributed to the DjVu source code during the last five years. Please submit a sourceforge bug report to update the following list.</p>
<dl>
<dt>
<dd> Yoshua Bengio, L&eacute;on Bottou, Chakradhar Chandaluri, Regis M. Chaplin, Ming Chen, Parag Deshmukh, Royce Edwards, Andrew Erofeev, Praveen Guduru, Patrick Haffner, Paul G. Howard, Orlando Keise, Yann Le Cun, Artem Mikheev, Florin Nicsa, Joseph M. Orost, Steven Pigeon, Bill Riemers, Patrice Simard, Jeffery Triggs, Luc Vincent, Pascal Vincent. </p>
</dl>
<h2>Index</h2>
