---

title: "wkhtmltopdf(1)"
name: "wkhtmltopdf"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wkhtmltopdf/"
description: "wkhtmltopdf – html to pdf converter"
---

<p> wkhtmltopdf &#8211; html to pdf converter </p>
<h2>Synopsis</h2>
<p>&nbsp;<wbr>&nbsp;wkhtmltopdf&nbsp;[GLOBAL OPTION]&#8230;&nbsp;[OBJECT]&#8230;&nbsp;&lt;output file&gt; </p>
<h2>Document objects</h2>
<p> wkhtmltopdf is able to put several objects into the output file, an object is either a single webpage, a cover webpage or a table of contents. The objects are put into the output document in the order they are specified on the command line, options can be specified on a per object basis or in the global options area. Options from the Global Options section can only be placed in the global options area. </p>
<p> A page objects puts the content of a single webpage into the output document. </p>
<p>&nbsp;<wbr>&nbsp;(page)?&nbsp;&lt;input url/file name&gt;&nbsp;[PAGE OPTION]&#8230; </p>
<p> Options for the page object can be placed in the global options and the page options areas. The applicable options can be found in the Page Options and Headers And Footer Options sections. </p>
<p> A cover objects puts the content of a single webpage into the output document, the page does not appear in the table of contents, and does not have headers and footers. </p>
<p>&nbsp;<wbr>&nbsp;cover&nbsp;&lt;input url/file name&gt;&nbsp;[PAGE OPTION]&#8230; </p>
<p> All options that can be specified for a page object can also be specified for a cover. </p>
<p> A table of contents object inserts a table of contents into the output document. </p>
<p>&nbsp;<wbr>&nbsp;toc&nbsp;[TOC OPTION]&#8230; </p>
<p> All options that can be specified for a page object can also be specified for a toc, further more the options from the TOC Options section can also be applied. The table of contents is generated via XSLT which means that it can be styled to look however you want it to look. To get an idea of how to do this you can dump the default xslt document by supplying the &#8211;dump-default-toc-xsl, and the outline it works on by supplying &#8211;dump-outline, see the Outline Options section. </p>
<h2>Description</h2>
<p> Converts one or more HTML pages into a PDF document, <code>not</code> using wkhtmltopdf patched qt. </p>
<h2>Global Options</h2>
<dl>
<dt><code> &#8211;collate</code></dt>
<dd> Collate when printing multiple copies</dd>
<dt><code> &#8211;no-collate</code></dt>
<dd> Do not collate when printing multiple copies</dd>
<dt><code> &#8211;cookie-jar</code> <i>&lt;path&gt;</i></dt>
<dd> Read and write cookies from and to the supplied cookie jar file</dd>
<dt><code> &#8211;copies</code> <i>&lt;number&gt;</i></dt>
<dd> Number of copies to print into the pdf file</dd>
<dt><code>-d, &#8211;dpi</code> <i>&lt;dpi&gt;</i></dt>
<dd> Change the dpi explicitly (this has no effect on X11 based systems)</dd>
<dt><code>-H, &#8211;extended-help</code></dt>
<dd> Display more extensive help, detailing less common command switches</dd>
<dt><code>-g, &#8211;grayscale</code></dt>
<dd> PDF will be generated in grayscale</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display help</dd>
<dt><code> &#8211;htmldoc</code></dt>
<dd> Output program html help</dd>
<dt><code> &#8211;license</code></dt>
<dd> Output license information and exit</dd>
<dt><code> &#8211;log-level</code> <i>&lt;level&gt;</i></dt>
<dd> Set log level to: none, error, warn or info</dd>
<dt><code>-l, &#8211;lowquality</code></dt>
<dd> Generates lower quality pdf/ps. Useful to shrink the result document space</dd>
<dt><code> &#8211;manpage</code></dt>
<dd> Output program man page</dd>
<dt><code>-B, &#8211;margin-bottom</code> <i>&lt;unitreal&gt;</i></dt>
<dd> Set the page bottom margin</dd>
<dt><code>-L, &#8211;margin-left</code> <i>&lt;unitreal&gt;</i></dt>
<dd> Set the page left margin</dd>
<dt><code>-R, &#8211;margin-right</code> <i>&lt;unitreal&gt;</i></dt>
<dd> Set the page right margin</dd>
<dt><code>-T, &#8211;margin-top</code> <i>&lt;unitreal&gt;</i></dt>
<dd> Set the page top margin</dd>
<dt><code>-O, &#8211;orientation</code> <i>&lt;orientation&gt;</i></dt>
<dd> Set orientation to Landscape or Portrait</dd>
<dt><code> &#8211;page-height</code> <i>&lt;unitreal&gt;</i></dt>
<dd> Page height</dd>
<dt><code>-s, &#8211;page-size</code> <i>&lt;Size&gt;</i></dt>
<dd> Set paper size to: A4, Letter, etc.</dd>
<dt><code> &#8211;page-width</code> <i>&lt;unitreal&gt;</i></dt>
<dd> Page width</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Be less verbose, maintained for backwards compatibility; Same as using &#8211;log-level none</dd>
<dt><code> &#8211;read-args-from-stdin</code></dt>
<dd> Read command line arguments from stdin</dd>
<dt><code> &#8211;readme</code></dt>
<dd> Output program readme</dd>
<dt><code> &#8211;title</code> <i>&lt;text&gt;</i></dt>
<dd> The title of the generated pdf file (The title of the first document is used if not specified)</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Output version information and exit </dd>
</dl>
<h2>Page Options</h2>
<dl>
<dt><code> &#8211;allow</code> <i>&lt;path&gt;</i></dt>
<dd> Allow the file or files from the specified folder to be loaded (repeatable)</dd>
<dt><code> &#8211;background</code></dt>
<dd> Do print background</dd>
<dt><code> &#8211;no-background</code></dt>
<dd> Do not print background</dd>
<dt><code> &#8211;bypass-proxy-for</code> <i>&lt;value&gt;</i></dt>
<dd> Bypass proxy for host (repeatable)</dd>
<dt><code> &#8211;cache-dir</code> <i>&lt;path&gt;</i></dt>
<dd> Web cache directory</dd>
<dt><code> &#8211;checkbox-checked-svg</code> <i>&lt;path&gt;</i></dt>
<dd> Use this SVG file when rendering checked checkboxes</dd>
<dt><code> &#8211;checkbox-svg</code> <i>&lt;path&gt;</i></dt>
<dd> Use this SVG file when rendering unchecked checkboxes</dd>
<dt><code> &#8211;cookie</code> <i>&lt;name&gt;</i> <i>&lt;value&gt;</i></dt>
<dd> Set an additional cookie (repeatable), value should be url encoded.</dd>
<dt><code> &#8211;custom-header</code> <i>&lt;name&gt;</i> <i>&lt;value&gt;</i></dt>
<dd> Set an additional HTTP header (repeatable)</dd>
<dt><code> &#8211;custom-header-propagation</code></dt>
<dd> Add HTTP headers specified by &#8211;custom-header for each resource request.</dd>
<dt><code> &#8211;no-custom-header-propagation</code></dt>
<dd> Do not add HTTP headers specified by &#8211;custom-header for each resource request.</dd>
<dt><code> &#8211;debug-javascript</code></dt>
<dd> Show javascript debugging output</dd>
<dt><code> &#8211;no-debug-javascript</code></dt>
<dd> Do not show javascript debugging output</dd>
<dt><code> &#8211;encoding</code> <i>&lt;encoding&gt;</i></dt>
<dd> Set the default text encoding, for input</dd>
<dt><code> &#8211;images</code></dt>
<dd> Do load or print images</dd>
<dt><code> &#8211;no-images</code></dt>
<dd> Do not load or print images</dd>
<dt><code>-n, &#8211;disable-javascript</code></dt>
<dd> Do not allow web pages to run javascript</dd>
<dt><code> &#8211;enable-javascript</code></dt>
<dd> Do allow web pages to run javascript</dd>
<dt><code> &#8211;javascript-delay</code> <i>&lt;msec&gt;</i></dt>
<dd> Wait some milliseconds for javascript finish</dd>
<dt><code> &#8211;load-error-handling</code> <i>&lt;handler&gt;</i></dt>
<dd> Specify how to handle pages that fail to load: abort, ignore or skip</dd>
<dt><code> &#8211;load-media-error-handling</code> <i>&lt;handler&gt;</i></dt>
<dd> Specify how to handle media files that fail to load: abort, ignore or skip</dd>
<dt><code> &#8211;disable-local-file-access</code></dt>
<dd> Do not allowed conversion of a local file to read in other local files, unless explicitly allowed with &#8211;allow</dd>
<dt><code> &#8211;enable-local-file-access</code></dt>
<dd> Allowed conversion of a local file to read in other local files.</dd>
<dt><code> &#8211;minimum-font-size</code> <i>&lt;int&gt;</i></dt>
<dd> Minimum font size</dd>
<dt><code> &#8211;page-offset</code> <i>&lt;offset&gt;</i></dt>
<dd> Set the starting page number</dd>
<dt><code> &#8211;password</code> <i>&lt;password&gt;</i></dt>
<dd> HTTP Authentication password</dd>
<dt><code> &#8211;disable-plugins</code></dt>
<dd> Disable installed plugins</dd>
<dt><code> &#8211;enable-plugins</code></dt>
<dd> Enable installed plugins (plugins will likely not work)</dd>
<dt><code> &#8211;post</code> <i>&lt;name&gt;</i> <i>&lt;value&gt;</i></dt>
<dd> Add an additional post field (repeatable)</dd>
<dt><code> &#8211;post-file</code> <i>&lt;name&gt;</i> <i>&lt;path&gt;</i></dt>
<dd> Post an additional file (repeatable)</dd>
<dt><code>-p, &#8211;proxy</code> <i>&lt;proxy&gt;</i></dt>
<dd> Use a proxy</dd>
<dt><code> &#8211;proxy-hostname-lookup</code></dt>
<dd> Use the proxy for resolving hostnames</dd>
<dt><code> &#8211;radiobutton-checked-svg</code> <i>&lt;path&gt;</i></dt>
<dd> Use this SVG file when rendering checked radiobuttons</dd>
<dt><code> &#8211;radiobutton-svg</code> <i>&lt;path&gt;</i></dt>
<dd> Use this SVG file when rendering unchecked radiobuttons</dd>
<dt><code> &#8211;run-script</code> <i>&lt;js&gt;</i></dt>
<dd> Run this additional javascript after the page is done loading (repeatable)</dd>
<dt><code> &#8211;ssl-crt-path</code> <i>&lt;path&gt;</i></dt>
<dd> Path to the ssl client cert public key in OpenSSL PEM format, optionally followed by intermediate ca and trusted certs</dd>
<dt><code> &#8211;ssl-key-password</code> <i>&lt;password&gt;</i></dt>
<dd> Password to ssl client cert private key</dd>
<dt><code> &#8211;ssl-key-path</code> <i>&lt;path&gt;</i></dt>
<dd> Path to ssl client cert private key in OpenSSL PEM format</dd>
<dt><code> &#8211;stop-slow-scripts</code></dt>
<dd> Stop slow running javascripts</dd>
<dt><code> &#8211;no-stop-slow-scripts</code></dt>
<dd> Do not Stop slow running javascripts</dd>
<dt><code> &#8211;user-style-sheet</code> <i>&lt;path&gt;</i></dt>
<dd> Specify a user style sheet, to load with every page</dd>
<dt><code> &#8211;username</code> <i>&lt;username&gt;</i></dt>
<dd> HTTP Authentication username</dd>
<dt><code> &#8211;window-status</code> <i>&lt;windowStatus&gt;</i></dt>
<dd> Wait until window.status is equal to this string before rendering page</dd>
<dt><code> &#8211;zoom</code> <i>&lt;float&gt;</i></dt>
<dd> Use this zoom factor </dd>
</dl>
<h2>Specifying A Proxy</h2>
<p> By default proxy information will be read from the environment variables: proxy, all_proxy and http_proxy, proxy options can also by specified with the -p switch </p>
<p>&nbsp;<wbr>&nbsp;&lt;type&gt;&nbsp;:=&nbsp;&quot;http://&quot;&nbsp;|&nbsp;&quot;socks5://&quot;<br />
&nbsp;<wbr>&nbsp;&lt;serif&gt;&nbsp;:=&nbsp;&lt;username&gt;&nbsp;(&quot;:&quot;&nbsp;&lt;password&gt;)?&nbsp;&quot;@&quot;<br />
&nbsp;<wbr>&nbsp;&lt;proxy&gt;&nbsp;:=&nbsp;&quot;None&quot;&nbsp;|&nbsp;&lt;type&gt;?&nbsp;&lt;string&gt;?&nbsp;&lt;host&gt;&nbsp;(&quot;:&quot;&nbsp;&lt;port&gt;)? </p>
<p> Here are some examples (In case you are unfamiliar with the BNF): </p>
<p>&nbsp;<wbr>&nbsp;<a rel="nofollow" href="http://user:password@myproxyserver:8080">http://user:password@myproxyserver:8080</a><br />
&nbsp;<wbr>&nbsp;socks5://myproxyserver<br />
&nbsp;<wbr>&nbsp;None </p>
<h2>Reduced Functionality</h2>
<p> This version of wkhtmltopdf has been compiled against a version of QT without the wkhtmltopdf patches. Therefore some features are missing, if you need these features please use the static version. </p>
<p> Currently the list of features only supported with patch QT includes: </p>
<p>&nbsp;*&nbsp;Printing more than one HTML document into a PDF file.<br />
&nbsp;*&nbsp;Running without an X11 server.<br />
&nbsp;*&nbsp;Adding a document outline to the PDF file.<br />
&nbsp;*&nbsp;Adding headers and footers to the PDF file.<br />
&nbsp;*&nbsp;Generating a table of contents.<br />
&nbsp;*&nbsp;Adding links in the generated PDF file.<br />
&nbsp;*&nbsp;Printing using the screen media-type.<br />
&nbsp;*&nbsp;Disabling the smart shrink feature of WebKit. </p>
<h2>Page sizes</h2>
<p> The default page size of the rendered document is A4, but by using the &#8211;page-size option this can be changed to almost anything else, such as: A3, Letter and Legal. For a full list of supported pages sizes please see &lt;<a rel="nofollow" href="https://qt-project.org/doc/qt-4.8/qprinter.html#PaperSize-enum">https://qt-project.org/doc/qt-4.8/qprinter.html#PaperSize-enum</a>&gt;. </p>
<p> For a more fine grained control over the page size the &#8211;page-height and &#8211;page-width options may be used </p>
<h2>Reading arguments from stdin</h2>
<p> If you need to convert a lot of pages in a batch, and you feel that wkhtmltopdf is a bit too slow to start up, then you should try &#8211;read-args-from-stdin, </p>
<p> When &#8211;read-args-from-stdin each line of input sent to wkhtmltopdf on stdin will act as a separate invocation of wkhtmltopdf, with the arguments specified on the given line combined with the arguments given to wkhtmltopdf </p>
<p> For example one could do the following: </p>
<p>&nbsp;<wbr>&nbsp;echo&nbsp;&quot;<a rel="nofollow" href="https://qt-project.org/doc/qt-4.8/qapplication.html">https://qt-project.org/doc/qt-4.8/qapplication.html</a>&nbsp;qapplication.pdf&quot;&nbsp;&gt;&gt;&nbsp;cmds<br />
&nbsp;<wbr>&nbsp;echo&nbsp;&quot;cover google.com&nbsp;<a rel="nofollow" href="https://en.wikipedia.org/wiki/Qt_(software)">https://en.wikipedia.org/wiki/Qt_(software)</a>&nbsp;qt.pdf&quot;&nbsp;&gt;&gt;&nbsp;cmds<br />
&nbsp;<wbr>&nbsp;wkhtmltopdf &#8211;read-args-from-stdin &#8211;book&nbsp;&lt;&nbsp;cmds </p>
<h2>Page Breaking</h2>
<p> The current page breaking algorithm of WebKit leaves much to be desired. Basically WebKit will render everything into one long page, and then cut it up into pages. This means that if you have two columns of text where one is vertically shifted by half a line. Then WebKit will cut a line into to pieces display the top half on one page. And the bottom half on another page. It will also break image in two and so on. If you are using the patched version of QT you can use the CSS page-break-inside property to remedy this somewhat. There is no easy solution to this problem, until this is solved try organizing your HTML documents such that it contains many lines on which pages can be cut cleanly. </p>
<h2>Contact</h2>
<p> If you experience bugs or want to request new features please visit &lt;<a rel="nofollow" href="https://wkhtmltopdf.org/support.html">https://wkhtmltopdf.org/support.html</a>&gt; </p>
<h2>Authors</h2>
<p>&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;Jakob Truelsen&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;antialize [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Ashish Kulkarni&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;ashish [at] kulkarni.dev&gt;<br />
&nbsp;<wbr>&nbsp;Jan Habermann&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;jan [at] habermann24.com&gt;<br />
&nbsp;<wbr>&nbsp;Pablo Ruiz García&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;pablo.ruiz [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Trevor North&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;trevor [at] blubolt.com&gt;<br />
&nbsp;<wbr>&nbsp;Nate Pinchot&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;nate.pinchot [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;pussbb&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;pussbb [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Aaron Stone&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;aaron [at] serendipity.cx&gt;<br />
&nbsp;<wbr>&nbsp;Patrick Widauer&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;@a-ctor<br />
&nbsp;<wbr>&nbsp;Peter van der Tak&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;pta [at] ibuildgreen.eu&gt;<br />
&nbsp;<wbr>&nbsp;Benjamin Sinkula&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;bsinky [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Kasper F. Brandt&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;poizan [at] poizan.dk&gt;<br />
&nbsp;<wbr>&nbsp;Michael Nitze&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;michael.nitze [at] online.de&gt;<br />
&nbsp;<wbr>&nbsp;Rok Dvojmoc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;rok.dvojmoc [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;theirix&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;theirix [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Tomsgu&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;tomasjakll [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Artem Butusov&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;art.sormy [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Christian Sciberras&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;uuf6429 [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Daniel M. Lambea&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;dmlambea [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Douglas Bagnall&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;douglas [at] paradise.net.nz&gt;<br />
&nbsp;<wbr>&nbsp;peterrehm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;peter.rehm [at] renvest.de&gt;<br />
&nbsp;<wbr>&nbsp;Renan Gonçalves&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;renan.saddam [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Ruslan Grabovoy&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;kudgo.test [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Sander Kleykens&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;sander.kleykens [at] avnu.be&gt;<br />
&nbsp;<wbr>&nbsp;Adam Thorsen&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;adam.thorsen [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Albin Kerouanton&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;albin.kerouanton [at] knplabs.com&gt;<br />
&nbsp;<wbr>&nbsp;Alejandro Dubrovsky&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;alito [at] organicrobot.com&gt;<br />
&nbsp;<wbr>&nbsp;Arthur Cinader&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;@acinader<br />
&nbsp;<wbr>&nbsp;Benoit Garret&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;benoit.garret [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Bill Kuker&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;bkuker [at] billkuker.com&gt;<br />
&nbsp;<wbr>&nbsp;cptjazz&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;alexander [at] jesner.eu&gt;<br />
&nbsp;<wbr>&nbsp;daigot&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;daigot [at] rayze.com&gt;<br />
&nbsp;<wbr>&nbsp;Destan Sarpkaya&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;@destan<br />
&nbsp;<wbr>&nbsp;Duncan Smart&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;duncan.smart [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Emil Lerch&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;emil [at] lerch.org&gt;<br />
&nbsp;<wbr>&nbsp;Erik Hyrkas&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;erik.hyrkas [at] thomsonreuters.com&gt;<br />
&nbsp;<wbr>&nbsp;Erling Linde&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;erlingwl [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Fábio C. Barrionuevo da Luz&nbsp;&lt;bnafta [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Fr33m1nd&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;lukion [at] gmx.de&gt;<br />
&nbsp;<wbr>&nbsp;Frank Groeneveld&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;frank [at] frankgroeneveld.nl&gt;<br />
&nbsp;<wbr>&nbsp;Immanuel Häussermann&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;haeussermann [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Jake Petroules&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;jake.petroules [at] petroules.com&gt;<br />
&nbsp;<wbr>&nbsp;James Macdonald&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;james [at] kingfisher-systems.co.uk&gt;<br />
&nbsp;<wbr>&nbsp;Jason Smith&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;JasonParallel [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;John Muccigrosso&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;@Jmuccigr<br />
&nbsp;<wbr>&nbsp;Julien Le Goff&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;julego [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Kay Lukas&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;kay.lukas [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Kurt Revis&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;krevis [at] snoize.com&gt;<br />
&nbsp;<wbr>&nbsp;laura&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;@holamon<br />
&nbsp;<wbr>&nbsp;Marc Laporte&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;marc [at] laporte.name&gt;<br />
&nbsp;<wbr>&nbsp;Matthew M. Boedicker&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;matthewm [at] boedicker.org&gt;<br />
&nbsp;<wbr>&nbsp;Matthieu Bontemps&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;matthieu.bontemps [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Max Sikstrom&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;max.sikstrom [at] op5.com&gt;<br />
&nbsp;<wbr>&nbsp;Nolan Neustaeter&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;github [at] noolan.ca&gt;<br />
&nbsp;<wbr>&nbsp;Oleg Kostyuk&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;cub.uanic [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Pankaj Jangid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;pankaj.jangid [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;robinbetts&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;robinbetts [at] yahoo.com&gt;<br />
&nbsp;<wbr>&nbsp;Sem&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;spam [at] esemi.ru&gt;<br />
&nbsp;<wbr>&nbsp;Stefan Weil&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;sw [at] weilnetz.de&gt;<br />
&nbsp;<wbr>&nbsp;Stephen Kennedy&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;sk4425 [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Steve Shreeve&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;steve.shreeve [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Sven Nierlein&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;sven [at] nierlein.org&gt;<br />
&nbsp;<wbr>&nbsp;Tobin Juday&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;tobinibot [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Todd Fisher&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;todd.fisher [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Костадин&nbsp;Дамянов&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;maxmight [at] gmail.com&gt;<br />
&nbsp;<wbr>&nbsp;Emmanuel Bouthenot&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;kolter [at] openics.org&gt;<br />
&nbsp;<wbr>&nbsp;Rami&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;@icnocop<br />
&nbsp;<wbr>&nbsp;Khodeir-hubdoc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;@Khodeir-hubdoc<br />
&nbsp;<wbr>&nbsp;Jonathan Jefferies&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;@jjok<br />
&nbsp;<wbr>&nbsp;Joe Ayers&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;joseph.ayers [at] crunchydata.com&gt;<br />
&nbsp;<wbr>&nbsp;Jeffrey Cafferata&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;jeffrey [at] jcid.nl&gt;<br />
&nbsp;<wbr>&nbsp;rainabba<br />
&nbsp;<wbr>&nbsp;Mehdi Abbad<br />
&nbsp;<wbr>&nbsp;Lyes Amazouz<br />
&nbsp;<wbr>&nbsp;Pascal Bach<br />
&nbsp;<wbr>&nbsp;Mário Silva </p>
