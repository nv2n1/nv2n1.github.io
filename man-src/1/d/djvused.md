---
title: "djvused(1)"
name: "djvused"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvused/"
description: "djvused – Multi-purpose DjVu document editor."
---

<h2 class="name">NAME</h2>
<p> djvused &#8211; Multi-purpose DjVu document editor.</p>
<h2>SYNOPSIS</h2>
<p> <code>djvused [</code><i>options</i><code>] </code><i>djvufile</i> </p>
<h2>DESCRIPTION</h2>
<p> Program <code>djvused </code> is a powerful command line tool for manipulating multi-page documents, creating or editing annotation chunks, creating or editing hidden text layers, pre-computing thumbnail images, and more. The program first reads the DjVu document <i>djvufile</i> and executes a number of djvused commands. </p>
<p> Djvused commands can be read from a specific file (when option <code>-f</code> is specified), read from the command line (when option <code>-e</code> is specified), or read from the standard input (the default). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Cause <code>djvused </code> to print a command line prompt before reading commands and a brief message describing how each command was executed. This option is very useful for debugging djvused scripts and also for interactively entering djvused commands on the standard input.</p>
<dt><code>-f </code><i>scriptfile</i></p>
<dd> Cause <code>djvused</code> to read commands from file <i>scriptfile</i>.</p>
<dt><code>-e </code><i>command</i></p>
<dd> Cause <code>djvused</code> to execute the commands specified by the option argument <i>commands</i>. It is advisable to surround the djvused commands by single quotes in order to prevent unwanted shell expansion.</p>
<dt><code>-s</code></p>
<dd> Cause <code>djvused</code> to save the file <i>djvufile</i> after executing the specified commands. This is similar to executing command <code>save</code> immediately before terminating the program.</p>
<dt><code>-u</code></p>
<dd> Cause <code>djvused</code> to print hidden text and annotations as UTF-8 instead of encoding non-ASCII characters with octal escape sequences for maximal portability. This option is convenient for manually editing or viewing the djvused output. This option also causes the emission of an UTF-8 BOM under Windows.</p>
<dt><code>-n</code></p>
<dd> Cause <code>djvused </code> to disregard save commands. This is useful for debugging djvused scripts without overwriting files on your disk. </p>
</dl>
<h2>DJVUSED EXAMPLES</h2>
<p> There are many ways to use program <code>djvused</code>. The following examples illustrate some common uses of this program. </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Obtaining the size of a page</h2>
<p> Command <code>size </code> outputs the width and height of the selected pages using a <font SIZE="-1">HTML</font> friendly syntax. For instance, the following command prints the size of page <i>3</i> of document <i>myfile.djvu</i>.</p>
<dl>
<dt>
<dd> <code>djvused </code><i>myfile.djvu</i><code> -e &#8216;select 3; size&#8217;</code></dl>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Extracting the hidden text</h2>
<p> Command <code>print-pure-txt</code> outputs the text associated with a page or a document. For instance, the following shell command outputs the text for the entire document. Lines and pages are delimited by the usual control characters.</p>
<dl>
<dt>
<dd> <code>djvused </code><i>myfile.djvu</i><code> -e &#8216;print-pure-txt&#8217;</code></dl>
<p> Command <code>print-txt</code> produces a more extensive output describing the structure and the location of the text components. The syntax of this output is described later in this man page. For instance, the following shell command outputs extended text information for page <i>3 </i> of document <i>myfile.djvu</i>.</p>
<dl>
<dt>
<dd> <code>djvused </code><i>myfile.djvu</i><code> -e &#8216;select 3; print-txt&#8217;</code></dl>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Extracting the annotations</h2>
<p> Annotation data can be extracted using command <code>print-ant</code>. The syntax of the annotation data is described later in this man page. For instance, the following shell command outputs the annotation data for the first page of document <code>myfile.djvu</code>.</p>
<dl>
<dt>
<dd> <code>djvused </code><i>myfile.djvu</i><code> -e &#8216;select 1; print-ant&#8217;</code></dl>
<p> Command <code>print-ant</code> only prints the annotations stored in the selected component file. Command <code>print-merged-ant</code> also retrieves annotations from all the component files referenced by the current page (using <font SIZE="-1">INCL</font> chunks) and prints the merged information. </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dumping/restoring annotations and text</h2>
<p> Three commands, <code>output-txt</code>, <code>output-ant</code>, and <code>output-all</code>, produce djvused scripts. For instance, the following shell command produces a djvused script, <i>myfile.dsed</i>, that recreates all the text and annotation data in document <i>myfile.djvu</i>.</p>
<dl>
<dt>
<dd> <code>djvused </code><i>myfile.djvu</i><code> -e &#8216;output-all&#8217; &gt; </code><i>myfile.dsed</i></dl>
<p> Script <i>myfile.dsed</i> is a text file that can be easily edited. The following shell command then recreates the text and annotation information in file <i>myfile.djvu</i>.</p>
<dl>
<dt>
<dd> <code>djvused </code><i>myfile.djvu</i><code> -f </code><i>myfile.dsed</i><code> -s</code> </p>
</dl>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Extracting a page</h2>
<p> Both commands <code>save-page</code> and <code>save-page-with</code> create a DjVu file representing the selected component file of a document. The following shell command, for instance, creates a file <i>p05.djvu</i> containing page <i>5</i> of document <i>myfile.djvu</i>.</p>
<dl>
<dt>
<dd> <code>djvused </code><i>myfile.djvu</i><code> -e &#8216;select 5; save-page </code><i>p05.djvu</i><code>&#8216;</code></dl>
<p> Each page of a document might import data from another component file using the so-called inclusion ( <font SIZE="-1">INCL</font> ) chunks. Command <code>save-page</code> then produces a file with unresolved references to imported data. Such a file should then be made part of a multi-page document containing the required data in other component files. On the other hand, command <code>save-page-with</code> copies all the imported data into the output file. This file is directly usable. Yet collecting several such files into a multi-page document might lead to useless data replication. </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pre-computing thumbnails</h2>
<p> Commands <code>set-thumbnails</code> constructs thumbnails that can be later displayed by DjVu viewers. The following shell command, for instance, computes thumbnails of size <i>64</i>x<i>64</i> pixels for all pages of file <i>myfile.djvu</i>.</p>
<dl>
<dt>
<dd> <code>djvused </code><i>myfile.djvu</i><code> -e &#8216;set-thumbnails 64&#8217; -s</code> </p>
</dl>
<h2>DJVUSED COMMANDS</h2>
<p> Command lines might contain zero, one, or more djvused commands and an optional comment. Multiple djvused commands must be separated by a semicolon character &#8216;;&#8217;. Comments are introduced by the &#8216;#&#8217; character and extend until the end of the command line. </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Selection commands</h2>
<p> Multi-page DjVu documents are composed of a number of component files. Most component files describe a specific page of a document. Some component files contain information shared by several pages such as shared image data, shared annotations or thumbnails. Many djvused commands operate on selected component files. All component files are initially selected. The following commands are useful for changing the selection.</p>
<dl>
<dt><code>n</code></p>
<dd> Print the total number of pages in the document.</p>
<dt><code>ls</code></p>
<dd> List all component files in the document. Each line contains an optional page number, a letter describing the component file type, the size of the component file, and identifier of the component file. Component file type letters <code>P</code>, <code>I</code>, <code>A</code>, and <code>T</code> respectively stand for page data, shared image data, shared annotation data, and thumbnail data. Page numbers are only listed for component files containing page data. When it is set, the optional page title (see command <code>set-page-title</code> below) is displayed after the component file identifier.</p>
<dt><code>select [</code><i>fileid</i><code>]</code></p>
<dd> Select the component file identified by argument <i>fileid</i>. Argument <i>fileid</i> must be either a page number or a component file identifier. The <code>select</code> command selects all component files when the argument <i>fileid</i> is omitted.</p>
<dt><code>select-shared-ant</code></p>
<dd> Select a component file containing shared annotations. Only one such component file is supported by the current DjVu software. This component file usually contains annotations pertaining to the whole document as opposed to specific pages. An error message is displayed if there is no such component file.</p>
<dt><code>create-shared-ant</code></p>
<dd> Create and select a component file containing shared annotations. This command only selects the shared annotation component file if such a component file already exists. Otherwise it creates a new shared annotation component file and makes sure that it is imported by all pages in the document.</p>
<dt><code>showsel</code></p>
<dd> Shows the currently selected component files with the same format as command <code>ls</code>. </p>
</dl>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Text and annotation commands</h2>
<dl>
<dt><code>print-pure-txt</code></p>
<dd> Print the text stored in the hidden text layer of the selected pages. A similar capability is offered by program <code>djvutxt</code>. Structural information is sometimes represented by control characters. Text from different pages is delimited by form feed characters (&quot;&quot;). Lines are delimited by newline characters (&quot;
&quot;). Columns, regions, and paragraphs are sometimes delimited by vertical tab (&quot;&quot;), group separators (&quot;&quot;) and unit separators (&quot;&quot;) respectively.</p>
<dt><code>print-txt</code></p>
<dd> Prints extensive hidden text information for the selected pages. This information describes the structure of the text on the document page and locates the structural elements in the page image. The syntax of this output is described later in this man page.</p>
<dt><code>remove-txt</code></p>
<dd> Remove the hidden text information from the selected component files. For instance, executing commands <code>select</code> and <code>remove-txt</code> removes all hidden text information from the DjVu document.</p>
<dt><code>set-txt [</code><i>djvusedtxtfile</i><code>]</code></p>
<dd> Insert hidden text information into the selected pages. The optional argument <i>djvusedtxtfile</i> names a file containing the hidden text information. This file must contain data similar to what is produced by command <code>print-txt</code>. When the optional argument is omitted, the program reads the hidden text information from the djvused script until reaching an end-of-file or a line containing a single period.</p>
<dt><code>output-txt</code></p>
<dd> Prints a djvused script that reconstructs the hidden text information for the selected pages. This script can later be edited and executed by invoking program <code>djvused</code> with option <code>-f</code>.</p>
<dt><code>print-ant</code></p>
<dd> Prints the annotations of the selected component file. The annotation data is represented using a simple syntax described later in this document.</p>
<dt><code>print-merged-ant</code></p>
<dd> Merge the annotations stored in the selected component files with the annotations imported from other component files such as the shared annotation component file.. The annotation data is represented using a simple syntax described later in this document.</p>
<dt><code>remove-ant</code></p>
<dd> Remove the annotation information from the selected component files. For instance, executing commands <code>select</code> and <code>remove-ant</code> removes all annotation information from the DjVu document.</p>
<dt><code>set-ant [</code><i>djvusedantfile</i><code>]</code></p>
<dd> Insert annotations into the selected component file. The optional argument <i>djvusedantfile</i> names a file containing the annotation data. This file must contain data similar to what is produced by command <code>print-ant</code>. When the optional argument is omitted, the program reads the annotation data from the djvused script itself until reaching an end-of-file or a line containing a single period.</p>
<dt><code>output-ant</code></p>
<dd> Print a djvused script that reconstructs the annotation information for the selected pages. This script can later be edited and executed by invoking program <code>djvused</code> with option <code>-f</code>.</p>
<dt><code>print-meta</code></p>
<dd> Print the meta-data part of the annotations for the selected component file. This command displays a subset of the information printed by command <code>print-ant</code> using a different syntax. Meta-data are organized as key-value pairs. Each printed line contains the key name such as <code>author</code>, <code>title</code>,etc., followed by a tab character (&quot;	&quot;) and a double-quoted string representing the <font SIZE="-1">UTF-8</font> encoded meta-data value.</p>
<dt><code>remove-meta</code></p>
<dd> Remove the meta-data part of the annotations of the selected component files.</p>
<dt><code>set-meta [</code><i>djvusedmetafile</i><code>]</code></p>
<dd> Set the meta-data part of the annotations of the selected component file. The remaining part of the annotations is left unchanged. The optional argument <i>djvusedmetafile</i> names a file containing the meta-data. This file must contain data similar to what is produced by command <code>print-meta</code>. When the optional argument is omitted, the program reads the annotation data from the djvused script itself until reaching an end-of-file or a line containing a single period.</p>
<dt><code>print-xmp</code></p>
<dd> Print the XMP metadata string contained in the annotation chunk of the selected component file. This command displays in fact a subset of the information printed by command <code>print-ant</code>.</p>
<dt><code>remove-xmp</code></p>
<dd> Removes the XMP tag from the annotation chunk of the selected component file.</p>
<dt><code>set-xmp [</code><i>xmpfile</i><code>]</code></p>
<dd> Set the XMP metadata part of the annotations of the selected component file. The remaining part of the annotations is left unchanged. The optional argument <i>xmpfile</i> names a file containing the XMP metadata in a format similar to that produced by command <code>print-xmp</code>. When the optional argument is omitted, the program reads the XMP annotation data from the djvused script itself until reaching an end-of-file or a line containing a single period.</p>
<dt><code>output-all</code></p>
<dd> Print a djvused script that reconstructs both the hidden text and the annotation information for the selected pages. This script can later be edited and executed by invoking program <code>djvused</code> with option <code>-f</code>.</dl>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Outline/bookmarks commands</h2>
<dl>
<dt><code>print-outline</code></p>
<dd> Print the outline of the document. Nothing is printed if the document contains no outline.</p>
<dt><code>remove-outline</code></p>
<dd> Removes the outline from the document.</p>
<dt><code>set-outline [</code><i>djvusedoutlinefile</i><code>]</code></p>
<dd> Insert outline information into the document. The optional argument <i>djvusedoutlinefile</i> names a file containing the outline information. This file must contain data similar to what is produced by command <code>print-outline</code>. When the optional argument is omitted, the program reads the hidden text information from the djvused script until reaching an end-of-file or a line containing a single period.</dl>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Thumbnail commands</h2>
<dl>
<dt><code>set-thumbnails </code><i>sz</i></p>
<dd> Compute thumbnails of size <i>sz</i>x<i>sz</i> pixels and insert them into the document. DjVu viewers can later display these thumbnails very efficiently without need to download the data for each page. Typical thumbnail size range from 48 to 128 pixels.</p>
<dt><code>remove-thumbnails</code></p>
<dd> Remove the pre-computed thumbnails from the DjVu document. New thumbnails can then be computed using command <code>set-thumbnails</code>. </p>
</dl>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Save commands</h2>
<p> The above commands only modify the memory image of the DjVu document. The following commands provide means to save the modified data into the file system.</p>
<dl>
<dt><code>save</code></p>
<dd> Save the modified DjVu document back into the input file <i>djvufile</i> specified by the arguments of the program <code>djvused</code>. Nothing is done if the DjVu file was not modified. Passing option <code>-s</code> program <code>djvused </code> is equivalent to executing command <code>save</code> before exiting the program.</p>
<dt><code>save-bundled </code><i>filename</i></p>
<dd> Save the current DjVu document as a bundled multi-page DjVu document named <i>filename</i>. A similar capability is offered by program <code>djvmcvt</code>.</p>
<dt><code>save-indirect </code><i>filename</i></p>
<dd> Save the current DjVu document as an indirect multi-page DjVu document. The index file of the indirect document will be named <code>filename</code>. All other files composing the indirect document will be saved into the same directory as the index file. A similar capability is offered by program <code>djvmcvt</code>.</p>
<dt><code>save-page </code><i>filename</i></p>
<dd> Save the selected component file into DjVu file <i>filename</i>. The selected component file might import data from another component file using the so-called inclusion ( <font SIZE="-1">INCL</font> ) chunks. This command then produces a file with unresolved references to imported data. Such a file should then be made part of a multi-page document containing the required data in other component files.</p>
<dt><code>save-page-with </code><i>filename</i></p>
<dd> Save the selected component file into DjVu file <i>filename</i>. All data imported from other component files is copied into the output file as well. This command always produces a usable DjVu file. On the other hand, collecting several such files into a multi-page document might lead to useless data replication. </p>
</dl>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Miscellaneous commands</h2>
<dl>
<dt><code>help</code></p>
<dd> Display a help message listing all commands supported by <code>djvused</code>.</p>
<dt><code>dump</code></p>
<dd> Display the <font SIZE="-1">EA IFF 85</font> structure of the document or of the selected component file. A similar capability is offered by program <code>djvudump</code>.</p>
<dt><code>size</code></p>
<dd> Display the width and the height of the selected pages. The dimensions of each page are displayed using a syntax suitable for direct insertion into the <font SIZE="-1">&lt;EMBED&#8230;&gt;&lt;/EMBED&gt;</font> tags.</p>
<dt><code>set-page-title </code><i>title</i></p>
<dd> Sets a page title for the selected page. When page titles are available, recent versions of the DjVuLibre viewers display these page titles instead of page numbers and also accept them in page selection options. Command <code>ls</code> can be used to see both the page titles and page identifiers. To unset a page title, simply make it equal to the page identifier. </p>
</dl>
<h2>DJVUSED FILE FORMATS</h2>
<p> Djvused uses a simple parenthesized syntax to represent both annotations and hidden text.</p>
<dl>
<dt>*</p>
<dd> This syntax is the native syntax used by DjVu for storing annotations. Program <code>djvused</code> simply compresses the annotation data using the <code><a href="/docs/linux/man/1-bzz/">bzz</a></code>(1) algorithm.</p>
<dt>*</p>
<dd> This syntax differs from the native syntax used by DjVu for storing the hidden text. Program <code>djvused</code> performs the translations between the compact binary representation used by DjVu and the easily modifiable parenthesized syntax.</dl>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>General syntax</h2>
<p> Djvused files are <font SIZE="-1">ASCII</font> text files. The legal characters in djvused files are the printable <font SIZE="-1">ASCII </font> characters and the space, tab, cr, and nl characters. Using other characters has undefined results. </p>
<p> Djvused files are composed of a sequence of expressions separated by blank characters (space, tab, cr, or nl). There are four kind of expressions, namely integers, symbols, strings and lists.</p>
<dl>
<dt>Integers:</p>
<dd> Integer numbers are represented by one or more digits, with the usual interpretation.</p>
<dt>Symbols:</p>
<dd> Symbols, or identifiers, are sequences of printable ascii characters representing a name or a keyword. Acceptable characters are the alpha-numeric characters, the underscore &quot;_&quot;, the minus character &quot;-&quot;, and the hash character &quot;#&quot;. Names should not begin with a digit or a minus character.</p>
<dt>Strings:</p>
<dd> Strings denote an arbitrary sequence of bytes, usually interpreted as a sequence of <font SIZE="-1">UTF-8</font> encoded characters. Strings in djvused files are similar to strings in the C language. They are surrounded by double quote characters. Certain sequences of characters starting with a backslash (&quot;\&quot;) have a special meaning. A backslash followed by letter &quot;a&quot;, &quot;b&quot;, &quot;t&quot;, &quot;n&quot;, &quot;v&quot;, &quot;f&quot;, &quot;r&quot;, &quot;\&quot;, and stands for the ascii character BEL(007), BS(008), HT(009), LF(010), VT(011), FF(012), CR(013), BACKSLASH(134) and DOUBLEQUOTE(042) respectively. A backslash followed by one to three digits stands for the byte whose octal code is expressed by the digits. All other backslash sequences are illegal. All non printable ascii characters must be escaped.</p>
<dt>Lists:</p>
<dd> Lists are sequence of expressions separated by blanks and surrounded by parentheses. All expressions types are acceptable within a list, including sub-lists. </p>
</dl>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Hidden text syntax</h2>
<p> The building blocks of the hidden text syntax are lists representing each structural component of the hidden text. Structural components have the following form:</p>
<dl>
<dt>
<dd> <code>(</code><i>type</i><i>xmin</i><i>ymin</i><i>xmax</i><i>ymax</i><code> &#8230; )</code></dl>
<p> The symbol <i>type</i> must be one of <code>page</code>, <code>column</code>, <code>region</code>, <code>para</code>, <code>line</code>, <code>word</code>, or <code>char</code>, listed here by decreasing order of importance. The integers <i>xmin</i>, <i>ymin</i>, <i>xmax</i>, and <i>ymax</i> represent the coordinates of a rectangle indicating the position of the structural component in the page. Coordinates are measured in pixels and have their origin at the bottom left corner of the page. The remaining expressions in the list either is a single string representing the encoded text associated with this structural component, or is a sequence of structural components with a lesser type. </p>
<p> The hidden text for each page is simply represented by a single structural element of type <code>page</code>. Various level of structural information are acceptable. For instance, the page level component might only specify a page level string, or might only provide a list of lines, or might provide a full hierarchy down to the individual characters. </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Outline/Bookmark syntax</h2>
<p> The outline syntax is a single list of the form</p>
<dl>
<dt>
<dd> <code>(bookmarks &#8230;)</code></dl>
<p> The first element of the list is symbol <code>bookmarks</code>. The subsequent elements are lists representing the toplevel outline entries. Each outline entry is represented by a list with the following form:</p>
<dl>
<dt>
<dd> <code>(</code><i>title</i><i>url</i><code> &#8230; )</code></dl>
<p> The string <i>title</i> is the title of the outline entry. The destination string <i>url</i> can be either an arbitrary percent encoded <font SIZE="-1">URL,</font> or composed of the hash character (&quot;#&quot;) followed by a page name or number, or composed of the question mark character (&quot;?&quot;) followed by cgi-style arguments interpreted by the djvu viewer. The remaining expressions in the list describe subentries of this outline entry. </p>
<h2>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Annotation syntax</h2>
<p> Annotations are represented by a sequence of annotation expressions. The following annotation expressions are recognized:</p>
<dl>
<dt><code>(background </code><i>color</i><code>)</code></p>
<dd> Specify the color of the viewer area surrounding the DjVu image. Colors are represented with the X11 hexadecimal syntax <code>#RRGGBB</code>. For instance, <code>#000000</code> is black and <code>#FFFFFF</code> is white.</p>
<dt><code>(zoom </code><i>zoomvalue</i><code>)</code></p>
<dd> Specify the initial zoom factor of the image. Argument <i>zoomvalue</i> can be one of <code>stretch</code>, <code>one2one</code>, <code>width</code>, <code>page</code>, or composed of the letter <code>d</code> followed by a number in range 1 to 999 representing a zoom factor (such as in <code>d300</code> or <code>d150</code> for instance.)</p>
<dt><code>(mode </code><i>modevalue</i><code>)</code></p>
<dd> Specify the initial display mode of the image. Argument <i>modevalue</i> is one of <code>color</code>, <code>bw</code>, <code>fore</code>, or <code>back</code>.</p>
<dt><code>(align </code><i>horzalign</i><i>vertalign</i><code>)</code></p>
<dd> Specify how the image should be aligned on the viewer surface. By default the image is located in the center. Argument <i>horzalign</i> can be one of <code>left</code>, <code>center</code>, or <code>right</code>. Argument <i>vertalign</i> can be one of <code>top</code>, <code>center</code>, or <code>bottom</code>.</p>
<dt><code>(maparea </code><i>url</i><i>comment</i><i>area</i><code> &#8230;)</code></p>
<dd> Define an hyper-link for the specified destination.</p>
<dl>
<dt>
<dd>
<p> Argument <i>url</i> can have one of the following forms:</p>
<dl>
<dt>
<dd> <i>href</i><br />
 <code>(url </code><i>href</i><i>target</i><code>)</code>
</dl>
<p> where <i>href</i> is a string representing the destination and <i>target </i> is a string representing the target frame for the hyper-link, as defined by the <font SIZE="-1">HTML</font> anchor tag <font SIZE="-1">&lt;A&gt;.</font> The destination string <i>href</i> can be either an arbitrary percent encoded <font SIZE="-1">URL,</font> or composed of the hash character (&quot;#&quot;) followed by a page name or number, or composed of the question mark character (&quot;?&quot;) followed by cgi-style arguments interpreted by the djvu viewer. Page numbers may be prefixed with an optional sign to represent a page displacement. For instance the strings <code>#-1 </code> and <code>#+1</code> can be used to access the previous page and the next page. </p>
<p> Argument <i>comment </i> is a string that might be displayed by the viewer when the user moves the mouse over the hyper-link. </p>
<p> Argument <i>area</i> defines the shape and the location of the hyperlink. The following forms are recognized:</p>
<dl>
<dt>
<dd> <code>(rect </code><i>xmin</i><i>ymin</i><i>width</i><i>height</i><code>)</code><br />
 <code>(oval </code><i>xmin</i><i>ymin</i><i>width</i><i>height</i><code>)</code><br />
 <code>(poly </code><i>x0</i><i>y0</i><i>x1</i><i>y1</i><code> &#8230; )</code><br />
 <code>(text </code><i>xmin</i><i>ymin</i><i>width</i><i>height</i><code>)</code><br />
 <code>(line </code><i>x0</i><i>y0</i><i>x1</i><i>y1</i><code>)</code></dl>
<p> All parameters are numbers representing coordinates. Coordinates are measured in pixels and have their origin at the bottom left corner of the page. </p>
<p> The remaining expressions in the <code>maparea</code> list represent the visual effect associated with the hyper-link. </p>
<p> A first set of options defines how borders are drawn for <code>rect</code>, <code>oval</code>, <code>polygon</code>, or <code>text</code> hyperlink areas.</p>
<dl>
<dt>
<dd> <code>(none)</code><br />
 <code>(xor)</code><br />
 <code>(border </code><i>color</i><code>)</code><br />
 <code>(shadow_in [</code><i>thickness</i><code>])</code><br />
 <code>(shadow_out [</code><i>thickness</i><code>])</code><br />
 <code>(shadow_ein [</code><i>thickness</i><code>])</code><br />
 <code>(shadow_eout [</code><i>thickness</i><code>])</code></dl>
<p> where parameter <i>color</i> has syntax <code>#RRGGBB</code> as described above, and parameter thickness is an integer in range 1 to 32. The last four border options are only supported for <code>rect</code> hyperlink areas. The default border is a simple black line. Border options do not apply to <code>line </code> areas. </p>
<p> When a border option is specified, the border becomes visible when the user moves the mouse over the hyperlink. The border may be made always visible by using the following option:</p>
<dl>
<dt>
<dd> <code>(border_avis)</code></dl>
<p> The following two options may be used with <code>rect</code> hyperlink areas. The complete area will be highlighted using the specified color at the specified opacity (0-100, default 50).</p>
<dl>
<dt>
<dd> <code>(hilite </code><i>color</i><code>)</code><br />
 <code>(opacity </code><i>op</i><code>)</code></dl>
<p> This is often used with an empty <font SIZE="-1">URL </font> for simply emphasizing a specific segment of an image. </p>
<p> The following three options may be used with line areas to specify an optional ending arrow, the line width and color. The default is a black line with width 1 and without arrow.</p>
<dl>
<dt>
<dd> <code>(arrow)</code><br />
 <code>(width </code><i>w</i><code>)</code><br />
 <code>(lineclr </code><i>color</i><code>)</code></dl>
<p> Finally the following three options can be used with text areas. The default background color is transparent. The default text color is black. The <code>pushpin</code> option indicates that the text is symbolized by a small pushpin icon. Clicking the icon reveals the text.</p>
<dl>
<dt>
<dd> <code>(backclr </code><i>bkcolor</i><code>)</code><br />
 <code>(textclr </code><i>txtcolor</i><code>)</code><br />
 <code>(pushpin)</code></dl>
</dl>
<dt><code>(metadata &#8230; (</code><i>key</i><i>value</i><code>) &#8230; )</code></p>
<dd> Define meta-data entries. Each entry is identified by a symbol <i>key</i> representing the nature of the meta data entry. The string <i>value</i> represents the value associated with the corresponding key. Two sets of keys are noteworthy: keys borrowed from the BibTex bibliography system, and keys borrowed from the PDF DocInfo metadata. BibTex keys are always expressed in lowercase, such as <code>year</code>, <code>booktitle</code>, <code>editor</code>, <code>author</code>, etc.. DocInfo keys start with an uppercase letter, such as <code>Title</code>, <code>Author</code>, <code>Subject</code>, <code>Creator</code>, <code>Produced</code>, <code>Trapped</code>, <code>CreationDate</code>, and <code>ModDate</code>. The values associated with the last two keys should be dates expressed according to RFC 3339. </p>
</dl>
<h2>LIMITATIONS</h2>
<p> The current version of program <code>djvused</code> only supports selecting one component file or all component files. There is no way to select only a few component files. </p>
<h2>CREDITS</h2>
<p> This program was initially written by L&eacute;on Bottou &lt;leonb [at] users.sourceforge.net&gt; and was improved by Yann Le Cun &lt;profshadoko [at] users.sourceforge.net&gt;, Florin Nicsa, Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djvutxt/">djvutxt</a></code>(1), <code><a href="/docs/linux/man/1-djvmcvt/">djvmcvt</a></code>(1), <code><a href="/docs/linux/man/1-djvudump/">djvudump</a></code>(1), <code><a href="/docs/linux/man/1-bzz/">bzz</a></code>(1), Emacs djvused front end <code>djvu.el</code> on <font SIZE="-1">GNU Elpa</font> repository. </p>
<h2>Index</h2>
