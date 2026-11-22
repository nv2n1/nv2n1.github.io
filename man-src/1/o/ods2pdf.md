---

title: "ods2pdf(1)"
name: "ods2pdf"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ods2pdf/"
description: "unoconv – convert any document from and to any LibreOffice supported format"
---

<p> unoconv &#8211; convert any document from and to any LibreOffice supported format </p>
<h2>SYNOPSIS</h2>
<p> <i>unoconv</i> [options] file [file2 ..] </p>
<p> <i>unoconv</i> &#8211;listener [&#8211;server SRV] [&#8211;port PRT] [&#8211;connection CON]</p>
<h2>DESCRIPTION</h2>
<p> unoconv is a command line utility that can convert any file format that LibreOffice can import, to any file format that LibreOffice is capable of exporting. </p>
<p> unoconv uses the LibreOffice&#8217;s UNO bindings for non-interactive conversion of documents and therefore needs an LibreOffice instance to communicate with. Therefore if it cannot find one, it will start its own instance for temporary usage. If desired, one can start a &#8220;listener&#8221; instance to use for subsequent connections or even for remote connections.</p>
<h2>OPTIONS</h2>
<p> -c, &#8211;connection</p>
<dl>
<dt>
</dt><dd> UNO connection string to be used by the client to connect to an LibreOffice instance, or used by the listener to make LibreOffice listen. </dd>
<dl>
<dt>
</dt><dd>
<pre>
Default connection string is &quot;socket,host=localhost,port=2002;urp;StarOffice.ComponentContext&quot;
</pre>
</dd></dl>
</dl>
<p> -d, &#8211;doctype</p>
<dl>
<dt>
</dt><dd> Specify the LibreOffice document type of the backend format. Possible document types are: <i>document</i>, <i>graphics</i>, <i>presentation</i>, <i>spreadsheet</i>. </dd>
<dl>
<dt>
</dt><dd>
<pre>
Default document type is 'document'.
</pre>
</dd></dl>
</dl>
<p> -e, &#8211;export</p>
<dl>
<dt>
</dt><dd> Set specific export filter options (related to the used LibreOffice filter). </dd>
<dl>
<dt>
</dt><dd>
<pre>
eg. for the PDF output filter one can specify: -e PageRange=1-2
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
See the *EXPORT FILTERS* section.
</pre>
</dd></dl>
</dl>
<p> -f, &#8211;format</p>
<dl>
<dt>
</dt><dd> Specify the output format for the document. You can get a list of possible output formats per document type by using the &#8211;show option. </dd>
<dl>
<dt>
</dt><dd>
<pre>
Default document type is 'pdf'.
</pre>
</dd></dl>
</dl>
<p> -F, &#8211;field</p>
<dl>
<dt>
</dt><dd> Replace user-defined text field with value </dd>
<dl>
<dt>
</dt><dd>
<pre>
eg. -F Client_Name=&quot;Oracle&quot;
</pre>
</dd></dl>
</dl>
<p> -i, &#8211;import</p>
<dl>
<dt>
</dt><dd> Set specific import filters options (related to the used LibreOffice import filter based on the input filename). </dd>
<dl>
<dt>
</dt><dd>
<pre>
See the *IMPORT FILTERS* section.
</pre>
</dd></dl>
</dl>
<p> -l, &#8211;listener</p>
<dl>
<dt>
</dt><dd> Start unoconv as listener for unoconv clients to connect to.</dd></dl>
<p> -n, &#8211;no-launch</p>
<dl>
<dt>
</dt><dd> By default if no listener is running, unoconv will launch its own (temporary) listener to make sure the conversion works. This option will abort the conversion if no listener is found, rather than starting our own listener.</dd></dl>
<p> -o, &#8211;output</p>
<dl>
<dt>
</dt><dd> If the argument is a directory, put the converted documents in this directory. If multiple input files are provided, use it as a basename (and add output extension). Otherwise use it as the output filename.</dd></dl>
<p> &#8211;password</p>
<dl>
<dt>
</dt><dd> Provide a password to decrypt the document</dd></dl>
<p> &#8211;pipe</p>
<dl>
<dt>
</dt><dd> Use a pipe as an alternative connection mechanism to talk to LibreOffice.</dd></dl>
<p> -p, &#8211;port</p>
<dl>
<dt>
</dt><dd> Port to listen on (as listener) or to connect to (as client). </dd>
<dl>
<dt>
</dt><dd>
<pre>
Default port is '2002'.
</pre>
</dd></dl>
</dl>
<p> &#8211;preserve</p>
<dl>
<dt>
</dt><dd> Keep timestamp and permissions of the original document</dd></dl>
<p> -s, &#8211;server</p>
<dl>
<dt>
</dt><dd> Server (address) to listen on (as listener) or to connect to (as client). </dd>
<dl>
<dt>
</dt><dd>
<pre>
Default server is 'localhost'.
</pre>
</dd></dl>
</dl>
<p> &#8211;show</p>
<dl>
<dt>
</dt><dd> List the possible output formats to be used with -f.</dd></dl>
<p> &#8211;stdin</p>
<dl>
<dt>
</dt><dd> Read input file from stdin (filenames are ignored if provided)</dd></dl>
<p> &#8211;stdout</p>
<dl>
<dt>
</dt><dd> Print converted output file to stdout.</dd></dl>
<p> -t, &#8211;template</p>
<dl>
<dt>
</dt><dd> Specify the template to use for importing styles from. This can be very useful if you have a corporate identity you have to apply to every document you distribute.</dd></dl>
<p> -T, &#8211;timeout</p>
<dl>
<dt>
</dt><dd> When unoconv starts its own listener, try to connect to it for an amount of seconds before giving up. Increasing this may help when you receive random errors caused by the listener not being ready to accept conversion jobs.</dd></dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
</dt><dd> Be more and more and more verbose.</dd></dl>
<h2>ARGUMENTS</h2>
<p> You can provide one or more <code>files</code> as arguments to convert each of them to the specified <code>output format</code>.</p>
<h2>IMPORT FILTERS</h2>
<p> Depending on the used input file, a different LibreOffice import filter is automatically used by unoconv. This import filter can be influenced by the -i option that, depending on the filter used, accepts different arguments. </p>
<p> It is not always clear what import filter options you can provide, the import dialog in LibreOffice for the filter you ar using might give a good indication as to what you can expect as import filter options. </p>
<p> The reference is LibreOffice&#8217;s documentation, for spreadsheets it is described at: m[blue]<code><a rel="nofollow" href="http://wiki.services.openoffice.org/wiki/Documentation/DevGuide/Spreadsheets/Filter_Options">http://wiki.services.openoffice.org/wiki/Documentation/DevGuide/Spreadsheets/Filter_Options</a></code>m[] but we will look into some examples.</p>
<h2>DEFAULT IMPORT FILTER OPTIONS</h2>
<p> The default import filter for many imports (eg. Lotus, dBase or DIF) accepts as the only argument the input encoding-type, so if you require utf-8 (76) you can do: </p>
<dl>
<dt>
</dt><dd>
<pre>
-i FilterOptions=76
</pre>
</dd></dl>
<p> For a list of possible encoding types, you can use the above link to find the possible options. </p>
<dl>
<dt>
</dt><dd> &bull; FilterOptions</dd></dl>
<h2>TEXT IMPORT FILTER OPTIONS</h2>
<p> The Text import filter accepts a FilterOptions setting holding the input encoding. </p>
<dl>
<dt>
</dt><dd> &bull; FilterOptions</dd></dl>
<h2>CSV IMPORT FILTER OPTIONS</h2>
<p> The CSV import filter accepts a FilterOptions setting, the order is: <i>separator(s),text-delimiter,encoding,first-row,column-format</i> </p>
<p> For example you might want to use this for a <i>real</i> comma-separated document: </p>
<dl>
<dt>
</dt><dd>
<pre>
-i FilterOptions=44,34,76,2,1/5/2/1/3/1/4/1
</pre>
</dd></dl>
<p> which will use a comma (44) as the field separator, a double quote (34) as the text delimiter, UTF-8 (76) for the input encoding, start from the second row and use the specified formats for each column (1 means standard, 5 means YY/MM/DD date) </p>
<p> If you like to use more than one separator (say a space or a tab) and use the system&#8217;s encoding (9), but with no text-delimiter, you can do: </p>
<dl>
<dt>
</dt><dd>
<pre>
-i FilterOptions=9/32,,9,2
</pre>
</dd></dl>
<p> For a list of possible encoding types, you can use the above link to find the possible options. </p>
<dl>
<dt>
</dt><dd> &bull; FilterOptions</dd></dl>
<h2>EXPORT FILTERS</h2>
<p> In contrast to import filters, export filters can have multiple named options, although it is not always clear what options are available. It all depends on the version of LibreOffice. The export dialog you get in LibreOffice might give you a clue about what is possible, each of those widgets represents an option.</p>
<h2>TEXT EXPORT FILTER OPTIONS</h2>
<p> The Text export filter accepts a FilterOptions setting holding the output encoding. </p>
<dl>
<dt>
</dt><dd> &bull; FilterOptions</dd></dl>
<p> The order of the arguments is: <i>encoding,field-seperator,text-delimiter,quote-all-text-cells,save-cell-content-as-shown</i></p>
<h2>CSV EXPORT FILTER OPTIONS</h2>
<p> The CSV export filter accepts various arguments, the order is: <i>field-seperator(s),text-delimiter,encoding</i> </p>
<p> For example you might want to use this for a <i>real</i> comma-separated document: </p>
<dl>
<dt>
</dt><dd>
<pre>
-e FilterOptions=44,34,76
</pre>
</dd></dl>
<p> which will use a comma (44) as the field separator, a double quote (34) as the text delimiter, UTF-8 (76) for the export encoding, start from the second row and use the specified formats for each column (1 means standard, 5 means YY/MM/DD date) </p>
<p> If you like to use more than one separator (say a space or a tab) and use the system&#8217;s encoding (9), but with no text-delimiter, you can do: </p>
<dl>
<dt>
</dt><dd>
<pre>
-e FilterOptions=9/32,,9
</pre>
</dd></dl>
<p> For a list of possible encoding types, you can use the above link to find the possible options. </p>
<dl>
<dt>
</dt><dd> &bull; FilterOptions</dd></dl>
<h2>PDF EXPORT FILTER OPTIONS</h2>
<p> The PDF export filter is likely the most advanced export filter in its kind with a myriad of options one can use. The export filter options are described in a separate document, or on LibreOffice&#8217;s wiki at: </p>
<p> m[blue]<code><a rel="nofollow" href="http://wiki.services.openoffice.org/wiki/API/Tutorials/PDF_export">http://wiki.services.openoffice.org/wiki/API/Tutorials/PDF_export</a></code>m[] </p>
<p> For example one can specify: -e PageRange=1-2 </p>
<p> Here is a list of all options, however for more details please look in <i>filters.txt</i>: </p>
<dl>
<dt>
</dt><dd> &bull; AllowDuplicateFieldNames</dd></dl>
<dl>
<dt>
</dt><dd> &bull; CenterWindow</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Changes</dd></dl>
<dl>
<dt>
</dt><dd> &bull; ConvertOOoTargetToPDFTarget</dd></dl>
<dl>
<dt>
</dt><dd> &bull; DisplayPDFDocumentTitle</dd></dl>
<dl>
<dt>
</dt><dd> &bull; DocumentOpenPassword</dd></dl>
<dl>
<dt>
</dt><dd> &bull; EmbedStandardFonts</dd></dl>
<dl>
<dt>
</dt><dd> &bull; EnableCopyingOfContent</dd></dl>
<dl>
<dt>
</dt><dd> &bull; EnableTextAccessForAccessibilityTools</dd></dl>
<dl>
<dt>
</dt><dd> &bull; EncryptFile</dd></dl>
<dl>
<dt>
</dt><dd> &bull; ExportBookmarks</dd></dl>
<dl>
<dt>
</dt><dd> &bull; ExportBookmarksToPDFDestination</dd></dl>
<dl>
<dt>
</dt><dd> &bull; ExportFormFields</dd></dl>
<dl>
<dt>
</dt><dd> &bull; ExportLinksRelativeFsys</dd></dl>
<dl>
<dt>
</dt><dd> &bull; ExportNotes</dd></dl>
<dl>
<dt>
</dt><dd> &bull; ExportNotesPages</dd></dl>
<dl>
<dt>
</dt><dd> &bull; FirstPageOnLeft</dd></dl>
<dl>
<dt>
</dt><dd> &bull; FormsType</dd></dl>
<dl>
<dt>
</dt><dd> &bull; HideViewerMenubar</dd></dl>
<dl>
<dt>
</dt><dd> &bull; HideViewerToolbar</dd></dl>
<dl>
<dt>
</dt><dd> &bull; HideViewerWindowControls</dd></dl>
<dl>
<dt>
</dt><dd> &bull; InitialPage</dd></dl>
<dl>
<dt>
</dt><dd> &bull; InitialView</dd></dl>
<dl>
<dt>
</dt><dd> &bull; IsAddStream</dd></dl>
<dl>
<dt>
</dt><dd> &bull; IsSkipEmptyPages</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Magnification</dd></dl>
<dl>
<dt>
</dt><dd> &bull; MaxImageResolution</dd></dl>
<dl>
<dt>
</dt><dd> &bull; OpenBookmarkLevels</dd></dl>
<dl>
<dt>
</dt><dd> &bull; OpenInFullScreenMode</dd></dl>
<dl>
<dt>
</dt><dd> &bull; PageLayout</dd></dl>
<dl>
<dt>
</dt><dd> &bull; PageRange</dd></dl>
<dl>
<dt>
</dt><dd> &bull; PDFViewSelection</dd></dl>
<dl>
<dt>
</dt><dd> &bull; PermissionPassword</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Printing</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Quality</dd></dl>
<dl>
<dt>
</dt><dd> &bull; ReduceImageResolution</dd></dl>
<dl>
<dt>
</dt><dd> &bull; ResizeWindowToInitialPage</dd></dl>
<dl>
<dt>
</dt><dd> &bull; RestrictPermissionPassword</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Selection</dd></dl>
<dl>
<dt>
</dt><dd> &bull; SelectPdfVersion</dd></dl>
<dl>
<dt>
</dt><dd> &bull; UseLosslessCompression</dd></dl>
<dl>
<dt>
</dt><dd> &bull; UseTaggedPDF</dd></dl>
<dl>
<dt>
</dt><dd> &bull; UseTransitionEffects</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Watermark</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Zoom</dd></dl>
<h3>GRAPHICS EXPORT FILTER OPTIONS</h3>
<dl>
<dt>
</dt><dd> &bull; Height</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Resolution</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Width</dd></dl>
<p>  <code>BMP EXPORT FILTER OPTIONS</code></p>
<dl>
<dl>
<dt>
</dt><dd> &bull; Compression</dd></dl>
<dl>
<dt>
</dt><dd> &bull; RLEEncoding</dd></dl>
</dl>
<p>  <code>JPEG EXPORT FILTER OPTIONS</code></p>
<dl>
<dl>
<dt>
</dt><dd> &bull; ColorDepth</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Quality</dd></dl>
</dl>
<p>  <code>PBM/PGM/PPM EXPORT FILTER OPTIONS</code></p>
<dl>
<dl>
<dt>
</dt><dd> &bull; Encoding</dd></dl>
</dl>
<p>  <code>PNG EXPORT FILTER OPTIONS</code></p>
<dl>
<dl>
<dt>
</dt><dd> &bull; Compression</dd></dl>
<dl>
<dt>
</dt><dd> &bull; InterlacedMode</dd></dl>
</dl>
<p>  <code>GIF EXPORT FILTER OPTIONS</code></p>
<dl>
<dl>
<dt>
</dt><dd> &bull; InterlacedMode</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Transparency</dd></dl>
</dl>
<p>  <code>EPS EXPORT FILTER OPTIONS</code></p>
<dl>
<dl>
<dt>
</dt><dd> &bull; ColorFormat</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Compression</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Preview</dd></dl>
<dl>
<dt>
</dt><dd> &bull; Version</dd></dl>
</dl>
<p> </p>
<h2>EXAMPLES</h2>
<p> You can use unoconv in standalone mode, this means that in absence of an LibreOffice listener, it will starts its own: </p>
<dl>
<dt>
</dt><dd>
<pre>
unoconv -f pdf some-document.odt
</pre>
</dd></dl>
<p> One can use unoconv as a listener (by default localhost:2002) to let other unoconv instances connect to it: </p>
<dl>
<dt>
</dt><dd>
<pre>
unoconv --listener &amp;
unoconv -f pdf some-document.odt
unoconv -f doc other-document.odt
unoconv -f jpg some-image.png
unoconv -f xsl some-spreadsheet.csv
kill -15 %-
</pre>
</dd></dl>
<p> This also works on a remote host: </p>
<dl>
<dt>
</dt><dd>
<pre>
unoconv --listener --server 1.2.3.4 --port 4567
</pre>
</dd></dl>
<p> and then connect another system to convert documents: </p>
<dl>
<dt>
</dt><dd>
<pre>
unoconv --server 1.2.3.4 --port 4567
</pre>
</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> UNO_PATH</p>
<dl>
<dt>
</dt><dd> specifies what LibreOffice pyuno installation unoconv needs to use eg. <i>/opt/libreoffice3.4/basis-link/program</i></dd></dl>
<h2>EXIT STATUS</h2>
<p> Normally, the exit status is 0 if the conversion ran successful. If an error has occured, the return code is most likely an error returned by LibreOffice (or its interface, called UNO) however, the error never translates to something meaningful. In case you like to decipher the LibreOffice errCode, look at: </p>
<dl>
<dt>
</dt><dd>
<pre>
<a rel="nofollow" href="http://cgit.freedesktop.org/libreoffice/core/tree/tools/inc/tools/errcode.hxx">http://cgit.freedesktop.org/libreoffice/core/tree/tools/inc/tools/errcode.hxx</a>
<a rel="nofollow" href="http://cgit.freedesktop.org/libreoffice/core/tree/svtools/inc/svtools/sfxecode.hxx">http://cgit.freedesktop.org/libreoffice/core/tree/svtools/inc/svtools/sfxecode.hxx</a>
<a rel="nofollow" href="http://cgit.freedesktop.org/libreoffice/core/tree/svtools/inc/svtools/soerr.hxx">http://cgit.freedesktop.org/libreoffice/core/tree/svtools/inc/svtools/soerr.hxx</a>
</pre>
</dd></dl>
<p> Using the above lists, the error code 2074 means: </p>
<dl>
<dt>
</dt><dd>
<pre>
Class: 1 (ERRCODE_CLASS_ABORT)
Code: 26 (ERRCODE_IO_INVALIDPARAMETER or SVSTREAM_INVALID_PARAMETER)
</pre>
</dd></dl>
<p> And the error code 3088 means: </p>
<dl>
<dt>
</dt><dd>
<pre>
Class: 3 (ERRCODE_CLASS_NOTEXISTS)
Code: 16 (ERRCODE_IO_CANTWRITE)
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
</dt><dd>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-convert/">convert</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-file/">file</a>(1), odt2txt
</pre>
</dd></dl>
<h2>BUGS</h2>
<p> unoconv uses the UNO bindings to connect to LibreOffice, in absence of a usable socket, it will start its own LibreOffice instance with the correct parameters. </p>
<dl>
<dt>
</dt><dd>
  <code>Note</code>  </dd>
<p> Please see the TODO file for known bugs and future plans. </p>
</dl>
<h2>REFERENCES</h2>
<p> unoconv is very useful together with the following tools: </p>
<p> Asciidoc</p>
<dl>
<dt>
</dt><dd>
<p> m[blue]<code><a rel="nofollow" href="http://www.methods.co.nz/asciidoc/">http://www.methods.co.nz/asciidoc/</a></code>m[]</dd></dl>
<p> asciidoc-odf</p>
<dl>
<dt>
</dt><dd>
<p> m[blue]<code><a rel="nofollow" href="http://github.com/dagwieers/asciidoc-odf">http://github.com/dagwieers/asciidoc-odf</a></code>m[]</dd></dl>
<p> docbook2odf</p>
<dl>
<dt>
</dt><dd>
<p> m[blue]<code><a rel="nofollow" href="http://open.comsultia.com/docbook2odf/">http://open.comsultia.com/docbook2odf/</a></code>m[]</dd></dl>
<p> A list of possible import and export formats is available from: </p>
<p> OpenOffice 2.1</p>
<dl>
<dt>
</dt><dd>
<p> m[blue]<code><a rel="nofollow" href="http://wiki.services.openoffice.org/wiki/Framework/Article/Filter/FilterList_OOo_2_1">http://wiki.services.openoffice.org/wiki/Framework/Article/Filter/FilterList_OOo_2_1</a></code>m[]</dd></dl>
<p> OpenOffice 3.0</p>
<dl>
<dt>
</dt><dd>
<p> m[blue]<code><a rel="nofollow" href="http://wiki.services.openoffice.org/wiki/Framework/Article/Filter/FilterList_OOo_3_0">http://wiki.services.openoffice.org/wiki/Framework/Article/Filter/FilterList_OOo_3_0</a></code>m[]</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Dag Wieers, &lt;m[blue]<code>dag [at] wieers.com</code>m[][1]&gt;</p>
<h2>RESOURCES</h2>
<p> Main web site: m[blue]<code><a rel="nofollow" href="http://dag.wieers.com/home-made/unoconv/">http://dag.wieers.com/home-made/unoconv/</a></code>m[]</p>
<h2>COPYING</h2>
<p> Copyright (C) 2007 Dag Wieers. Free use of this software is granted under the terms of the GNU General Public License (GPL).</p>
<h2>AUTHOR</h2>
<p> <code>Dag Wieers</code> &lt;dag [at] wieers.com&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> dag [at] wieers.com</dd>
<dl>
<dt>
</dt><dd> mailto:dag [at] wieers.com</dd></dl>
</dl>
