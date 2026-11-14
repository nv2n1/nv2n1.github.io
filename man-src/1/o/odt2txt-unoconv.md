---
title: "odt2txt-unoconv(1)"
name: "odt2txt-unoconv"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odt2txt-unoconv/"
description: "unoconv – convert any document from and to any LibreOffice supported format"
---

<p>unoconv &#8211; convert any document from and to any LibreOffice supported format </p>
<h2>Synopsis</h2>
<p><i>unoconv</i> [options] file [file2 ..] </p>
<p> <i>unoconv</i> &#8211;listener [&#8211;server SRV] [&#8211;port PRT] [&#8211;connection CON]</p>
<h2>Description</h2>
<p>unoconv is a command line utility that can convert any file format that LibreOffice can import, to any file format that LibreOffice is capable of exporting. </p>
<p> unoconv uses the LibreOffice&#8217;s UNO bindings for non-interactive conversion of documents and therefore needs an LibreOffice instance to communicate with. Therefore if it cannot find one, it will start its own instance for temporary usage. If desired, one can start a &#8220;listener&#8221; instance to use for subsequent connections or even for remote connections.</p>
<h2>Options</h2>
<p>-c, &#8211;connection</p>
<dl COMPACT>
<dd>UNO connection string to be used by the client to connect to an LibreOffice instance, or used by the listener to make LibreOffice listen. </p>
<dl COMPACT>
<dd>
<pre>Default connection string is &quot;socket,host=localhost,port=2002;urp;StarOffice.ComponentContext&quot;</pre>
</dl>
</dl>
<p> -d, &#8211;doctype</p>
<dl COMPACT>
<dd>Specify the LibreOffice document type of the backend format. Possible document types are: <i>document</i>, <i>graphics</i>, <i>presentation</i>, <i>spreadsheet</i>. </p>
<dl COMPACT>
<dd>
<pre>Default document type is 'document'.</pre>
</dl>
</dl>
<p> -e, &#8211;export</p>
<dl COMPACT>
<dd>Set specific export filter options (related to the used LibreOffice filter). </p>
<dl COMPACT>
<dd>
<pre>eg. for the PDF output filter one can specify: -e PageRange=1-2</pre>
</dl>
<dl COMPACT>
<dd>
<pre>See the *EXPORT FILTERS* section.</pre>
</dl>
</dl>
<p> -f, &#8211;format</p>
<dl COMPACT>
<dd>Specify the output format for the document. You can get a list of possible output formats per document type by using the &#8211;show option. </p>
<dl COMPACT>
<dd>
<pre>Default document type is 'pdf'.</pre>
</dl>
</dl>
<p> -F, &#8211;field</p>
<dl COMPACT>
<dd>Replace user-defined text field with value </p>
<dl COMPACT>
<dd>
<pre>eg. -F Client_Name=&quot;Oracle&quot;</pre>
</dl>
</dl>
<p> -i, &#8211;import</p>
<dl COMPACT>
<dd>Set specific import filters options (related to the used LibreOffice import filter based on the input filename). </p>
<dl COMPACT>
<dd>
<pre>See the *IMPORT FILTERS* section.</pre>
</dl>
</dl>
<p> -l, &#8211;listener</p>
<dl COMPACT>
<dd>Start unoconv as listener for unoconv clients to connect to.</dl>
<p> -n, &#8211;no-launch</p>
<dl COMPACT>
<dd>By default if no listener is running, unoconv will launch its own (temporary) listener to make sure the conversion works. This option will abort the conversion if no listener is found, rather than starting our own listener.</dl>
<p> -o, &#8211;output</p>
<dl COMPACT>
<dd>If the argument is a directory, put the converted documents in this directory. If multiple input files are provided, use it as a basename (and add output extension). Otherwise use it as the output filename.</dl>
<p> &#8211;password</p>
<dl COMPACT>
<dd>Provide a password to decrypt the document</dl>
<p> &#8211;pipe</p>
<dl COMPACT>
<dd>Use a pipe as an alternative connection mechanism to talk to LibreOffice.</dl>
<p> -p, &#8211;port</p>
<dl COMPACT>
<dd>Port to listen on (as listener) or to connect to (as client). </p>
<dl COMPACT>
<dd>
<pre>Default port is '2002'.</pre>
</dl>
</dl>
<p> &#8211;preserve</p>
<dl COMPACT>
<dd>Keep timestamp and permissions of the original document</dl>
<p> -s, &#8211;server</p>
<dl COMPACT>
<dd>Server (address) to listen on (as listener) or to connect to (as client). </p>
<dl COMPACT>
<dd>
<pre>Default server is 'localhost'.</pre>
</dl>
</dl>
<p> &#8211;show</p>
<dl COMPACT>
<dd>List the possible output formats to be used with -f.</dl>
<p> &#8211;stdin</p>
<dl COMPACT>
<dd>Read input file from stdin (filenames are ignored if provided)</dl>
<p> &#8211;stdout</p>
<dl COMPACT>
<dd>Print converted output file to stdout.</dl>
<p> -t, &#8211;template</p>
<dl COMPACT>
<dd>Specify the template to use for importing styles from. This can be very useful if you have a corporate identity you have to apply to every document you distribute.</dl>
<p> -T, &#8211;timeout</p>
<dl COMPACT>
<dd>When unoconv starts its own listener, try to connect to it for an amount of seconds before giving up. Increasing this may help when you receive random errors caused by the listener not being ready to accept conversion jobs.</dl>
<p> -v, &#8211;verbose</p>
<dl COMPACT>
<dd>Be more and more and more verbose.</dl>
<h2>Arguments</h2>
<p>You can provide one or more <code>files</code> as arguments to convert each of them to the specified <code>output format</code>.</p>
<h2>Import Filters</h2>
<p>Depending on the used input file, a different LibreOffice import filter is automatically used by unoconv. This import filter can be influenced by the -i option that, depending on the filter used, accepts different arguments. </p>
<p> It is not always clear what import filter options you can provide, the import dialog in LibreOffice for the filter you ar using might give a good indication as to what you can expect as import filter options. </p>
<p> The reference is LibreOffice&#8217;s documentation, for spreadsheets it is described at: m[blue]<code><a rel="nofollow" href="http://wiki.services.openoffice.org/wiki/Documentation/DevGuide/Spreadsheets/Filter_Options">http://wiki.services.openoffice.org/wiki/Documentation/DevGuide/Spreadsheets/Filter_Options</a></code>m[] but we will look into some examples.</p>
<h2>Default Import Filter Options</h2>
<p>The default import filter for many imports (eg. Lotus, dBase or DIF) accepts as the only argument the input encoding-type, so if you require utf-8 (76) you can do: </p>
<dl COMPACT>
<dd>
<pre>-i FilterOptions=76</pre>
</dl>
<p> For a list of possible encoding types, you can use the above link to find the possible options. </p>
<dl COMPACT>
<dd>&bull; FilterOptions</dl>
<h2>Text Import Filter Options</h2>
<p>The Text import filter accepts a FilterOptions setting holding the input encoding. </p>
<dl COMPACT>
<dd>&bull; FilterOptions</dl>
<h2>Csv Import Filter Options</h2>
<p>The CSV import filter accepts a FilterOptions setting, the order is: <i>separator(s),text-delimiter,encoding,first-row,column-format</i> </p>
<p> For example you might want to use this for a <i>real</i> comma-separated document: </p>
<dl COMPACT>
<dd>
<pre>-i FilterOptions=44,34,76,2,1/5/2/1/3/1/4/1</pre>
</dl>
<p> which will use a comma (44) as the field separator, a double quote (34) as the text delimiter, UTF-8 (76) for the input encoding, start from the second row and use the specified formats for each column (1 means standard, 5 means YY/MM/DD date) </p>
<p> If you like to use more than one separator (say a space or a tab) and use the system&#8217;s encoding (9), but with no text-delimiter, you can do: </p>
<dl COMPACT>
<dd>
<pre>-i FilterOptions=9/32,,9,2</pre>
</dl>
<p> For a list of possible encoding types, you can use the above link to find the possible options. </p>
<dl COMPACT>
<dd>&bull; FilterOptions</dl>
<h2>Export Filters</h2>
<p>In contrast to import filters, export filters can have multiple named options, although it is not always clear what options are available. It all depends on the version of LibreOffice. The export dialog you get in LibreOffice might give you a clue about what is possible, each of those widgets represents an option.</p>
<h2>Text Export Filter Options</h2>
<p>The Text export filter accepts a FilterOptions setting holding the output encoding. </p>
<dl COMPACT>
<dd>&bull; FilterOptions</dl>
<p> The order of the arguments is: <i>encoding,field-seperator,text-delimiter,quote-all-text-cells,save-cell-content-as-shown</i></p>
<h2>Csv Export Filter Options</h2>
<p>The CSV export filter accepts various arguments, the order is: <i>field-seperator(s),text-delimiter,encoding</i> </p>
<p> For example you might want to use this for a <i>real</i> comma-separated document: </p>
<dl COMPACT>
<dd>
<pre>-e FilterOptions=44,34,76</pre>
</dl>
<p> which will use a comma (44) as the field separator, a double quote (34) as the text delimiter, UTF-8 (76) for the export encoding, start from the second row and use the specified formats for each column (1 means standard, 5 means YY/MM/DD date) </p>
<p> If you like to use more than one separator (say a space or a tab) and use the system&#8217;s encoding (9), but with no text-delimiter, you can do: </p>
<dl COMPACT>
<dd>
<pre>-e FilterOptions=9/32,,9</pre>
</dl>
<p> For a list of possible encoding types, you can use the above link to find the possible options. </p>
<dl COMPACT>
<dd>&bull; FilterOptions</dl>
<h2>Pdf Export Filter Options</h2>
<p>The PDF export filter is likely the most advanced export filter in its kind with a myriad of options one can use. The export filter options are described in a separate document, or on LibreOffice&#8217;s wiki at: </p>
<p> m[blue]<code><a rel="nofollow" href="http://wiki.services.openoffice.org/wiki/API/Tutorials/PDF_export">http://wiki.services.openoffice.org/wiki/API/Tutorials/PDF_export</a></code>m[] </p>
<p> For example one can specify: -e PageRange=1-2 </p>
<p> Here is a list of all options, however for more details please look in <i>filters.txt</i>: </p>
<dl COMPACT>
<dd>&bull; AllowDuplicateFieldNames</dl>
<dl COMPACT>
<dd>&bull; CenterWindow</dl>
<dl COMPACT>
<dd>&bull; Changes</dl>
<dl COMPACT>
<dd>&bull; ConvertOOoTargetToPDFTarget</dl>
<dl COMPACT>
<dd>&bull; DisplayPDFDocumentTitle</dl>
<dl COMPACT>
<dd>&bull; DocumentOpenPassword</dl>
<dl COMPACT>
<dd>&bull; EmbedStandardFonts</dl>
<dl COMPACT>
<dd>&bull; EnableCopyingOfContent</dl>
<dl COMPACT>
<dd>&bull; EnableTextAccessForAccessibilityTools</dl>
<dl COMPACT>
<dd>&bull; EncryptFile</dl>
<dl COMPACT>
<dd>&bull; ExportBookmarks</dl>
<dl COMPACT>
<dd>&bull; ExportBookmarksToPDFDestination</dl>
<dl COMPACT>
<dd>&bull; ExportFormFields</dl>
<dl COMPACT>
<dd>&bull; ExportLinksRelativeFsys</dl>
<dl COMPACT>
<dd>&bull; ExportNotes</dl>
<dl COMPACT>
<dd>&bull; ExportNotesPages</dl>
<dl COMPACT>
<dd>&bull; FirstPageOnLeft</dl>
<dl COMPACT>
<dd>&bull; FormsType</dl>
<dl COMPACT>
<dd>&bull; HideViewerMenubar</dl>
<dl COMPACT>
<dd>&bull; HideViewerToolbar</dl>
<dl COMPACT>
<dd>&bull; HideViewerWindowControls</dl>
<dl COMPACT>
<dd>&bull; InitialPage</dl>
<dl COMPACT>
<dd>&bull; InitialView</dl>
<dl COMPACT>
<dd>&bull; IsAddStream</dl>
<dl COMPACT>
<dd>&bull; IsSkipEmptyPages</dl>
<dl COMPACT>
<dd>&bull; Magnification</dl>
<dl COMPACT>
<dd>&bull; MaxImageResolution</dl>
<dl COMPACT>
<dd>&bull; OpenBookmarkLevels</dl>
<dl COMPACT>
<dd>&bull; OpenInFullScreenMode</dl>
<dl COMPACT>
<dd>&bull; PageLayout</dl>
<dl COMPACT>
<dd>&bull; PageRange</dl>
<dl COMPACT>
<dd>&bull; PDFViewSelection</dl>
<dl COMPACT>
<dd>&bull; PermissionPassword</dl>
<dl COMPACT>
<dd>&bull; Printing</dl>
<dl COMPACT>
<dd>&bull; Quality</dl>
<dl COMPACT>
<dd>&bull; ReduceImageResolution</dl>
<dl COMPACT>
<dd>&bull; ResizeWindowToInitialPage</dl>
<dl COMPACT>
<dd>&bull; RestrictPermissionPassword</dl>
<dl COMPACT>
<dd>&bull; Selection</dl>
<dl COMPACT>
<dd>&bull; SelectPdfVersion</dl>
<dl COMPACT>
<dd>&bull; UseLosslessCompression</dl>
<dl COMPACT>
<dd>&bull; UseTaggedPDF</dl>
<dl COMPACT>
<dd>&bull; UseTransitionEffects</dl>
<dl COMPACT>
<dd>&bull; Watermark</dl>
<dl COMPACT>
<dd>&bull; Zoom</dl>
<h3>Graphics Export Filter Options</h3>
<dl COMPACT>
<dd>&bull; Height</dl>
<dl COMPACT>
<dd>&bull; Resolution</dl>
<dl COMPACT>
<dd>&bull; Width</dl>
<p> <font SIZE="+1"> <code>BMP EXPORT FILTER OPTIONS</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dd>&bull; Compression</dl>
<dl COMPACT>
<dd>&bull; RLEEncoding</dl>
</dl>
<p> </font><font SIZE="+2"> <code>JPEG EXPORT FILTER OPTIONS</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dd>&bull; ColorDepth</dl>
<dl COMPACT>
<dd>&bull; Quality</dl>
</dl>
<p> </font><font SIZE="+3"> <code>PBM/PGM/PPM EXPORT FILTER OPTIONS</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dd>&bull; Encoding</dl>
</dl>
<p> </font><font SIZE="+4"> <code>PNG EXPORT FILTER OPTIONS</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dd>&bull; Compression</dl>
<dl COMPACT>
<dd>&bull; InterlacedMode</dl>
</dl>
<p> </font><font SIZE="+5"> <code>GIF EXPORT FILTER OPTIONS</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dd>&bull; InterlacedMode</dl>
<dl COMPACT>
<dd>&bull; Transparency</dl>
</dl>
<p> </font><font SIZE="+6"> <code>EPS EXPORT FILTER OPTIONS</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dd>&bull; ColorFormat</dl>
<dl COMPACT>
<dd>&bull; Compression</dl>
<dl COMPACT>
<dd>&bull; Preview</dl>
<dl COMPACT>
<dd>&bull; Version</dl>
</dl>
<p> </font></p>
<h2>Examples</h2>
<p>You can use unoconv in standalone mode, this means that in absence of an LibreOffice listener, it will starts its own: </p>
<dl COMPACT>
<dd>
<pre>unoconv -f pdf some-document.odt</pre>
</dl>
<p> One can use unoconv as a listener (by default localhost:2002) to let other unoconv instances connect to it: </p>
<dl COMPACT>
<dd>
<pre>unoconv --listener &amp;
unoconv -f pdf some-document.odt
unoconv -f doc other-document.odt
unoconv -f jpg some-image.png
unoconv -f xsl some-spreadsheet.csv
kill -15 %-</pre>
</dl>
<p> This also works on a remote host: </p>
<dl COMPACT>
<dd>
<pre>unoconv --listener --server 1.2.3.4 --port 4567</pre>
</dl>
<p> and then connect another system to convert documents: </p>
<dl COMPACT>
<dd>
<pre>unoconv --server 1.2.3.4 --port 4567</pre>
</dl>
<h2>Environment Variables</h2>
<p>UNO_PATH</p>
<dl COMPACT>
<dd>specifies what LibreOffice pyuno installation unoconv needs to use eg. <i>/opt/libreoffice3.4/basis-link/program</i></dl>
<h2>Exit Status</h2>
<p>Normally, the exit status is 0 if the conversion ran successful. If an error has occured, the return code is most likely an error returned by LibreOffice (or its interface, called UNO) however, the error never translates to something meaningful. In case you like to decipher the LibreOffice errCode, look at: </p>
<dl COMPACT>
<dd>
<pre><a rel="nofollow" href="http://cgit.freedesktop.org/libreoffice/core/tree/tools/inc/tools/errcode.hxx">http://cgit.freedesktop.org/libreoffice/core/tree/tools/inc/tools/errcode.hxx</a>
<a rel="nofollow" href="http://cgit.freedesktop.org/libreoffice/core/tree/svtools/inc/svtools/sfxecode.hxx">http://cgit.freedesktop.org/libreoffice/core/tree/svtools/inc/svtools/sfxecode.hxx</a>
<a rel="nofollow" href="http://cgit.freedesktop.org/libreoffice/core/tree/svtools/inc/svtools/soerr.hxx">http://cgit.freedesktop.org/libreoffice/core/tree/svtools/inc/svtools/soerr.hxx</a></pre>
</dl>
<p> Using the above lists, the error code 2074 means: </p>
<dl COMPACT>
<dd>
<pre>Class: 1 (ERRCODE_CLASS_ABORT)
Code: 26 (ERRCODE_IO_INVALIDPARAMETER or SVSTREAM_INVALID_PARAMETER)</pre>
</dl>
<p> And the error code 3088 means: </p>
<dl COMPACT>
<dd>
<pre>Class: 3 (ERRCODE_CLASS_NOTEXISTS)
Code: 16 (ERRCODE_IO_CANTWRITE)</pre>
</dl>
<h2>See Also</h2>
<dl COMPACT>
<dd>
<pre><a href="//www.systutorials.com/docs/linux/man/1-convert/">convert</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-file/">file</a>(1), odt2txt</pre>
</dl>
<h2>Bugs</h2>
<p>unoconv uses the UNO bindings to connect to LibreOffice, in absence of a usable socket, it will start its own LibreOffice instance with the correct parameters. </p>
<dl COMPACT>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Please see the TODO file for known bugs and future plans. </p>
</dl>
<h2>References</h2>
<p>unoconv is very useful together with the following tools: </p>
<p> Asciidoc</p>
<dl COMPACT>
<dd>m[blue]<code><a rel="nofollow" href="http://www.methods.co.nz/asciidoc/">http://www.methods.co.nz/asciidoc/</a></code>m[]</dl>
<p> asciidoc-odf</p>
<dl COMPACT>
<dd>m[blue]<code><a rel="nofollow" href="http://github.com/dagwieers/asciidoc-odf">http://github.com/dagwieers/asciidoc-odf</a></code>m[]</dl>
<p> docbook2odf</p>
<dl COMPACT>
<dd>m[blue]<code><a rel="nofollow" href="http://open.comsultia.com/docbook2odf/">http://open.comsultia.com/docbook2odf/</a></code>m[]</dl>
<p> A list of possible import and export formats is available from: </p>
<p> OpenOffice 2.1</p>
<dl COMPACT>
<dd>m[blue]<code><a rel="nofollow" href="http://wiki.services.openoffice.org/wiki/Framework/Article/Filter/FilterList_OOo_2_1">http://wiki.services.openoffice.org/wiki/Framework/Article/Filter/FilterList_OOo_2_1</a></code>m[]</dl>
<p> OpenOffice 3.0</p>
<dl COMPACT>
<dd>m[blue]<code><a rel="nofollow" href="http://wiki.services.openoffice.org/wiki/Framework/Article/Filter/FilterList_OOo_3_0">http://wiki.services.openoffice.org/wiki/Framework/Article/Filter/FilterList_OOo_3_0</a></code>m[]</dl>
<h2>Author</h2>
<p>Written by Dag Wieers, &lt;m[blue]<code>dag [at] wieers.com</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Resources</h2>
<p>Main web site: m[blue]<code><a rel="nofollow" href="http://dag.wieers.com/home-made/unoconv/">http://dag.wieers.com/home-made/unoconv/</a></code>m[]</p>
<h2>Copying</h2>
<p>Copyright (C) 2007 Dag Wieers. Free use of this software is granted under the terms of the GNU General Public License (GPL).</p>
<h2>Author</h2>
<p><code>Dag Wieers</code> &lt;dag [at] wieers.com&gt;</p>
<dl COMPACT>
<dd>Author.</dl>
<h2>Notes</h2>
<dl COMPACT>
<dt> 1.</p>
<dd>dag [at] wieers.com</p>
<dl COMPACT>
<dd>mailto:dag [at] wieers.com</dl>
</dl>
