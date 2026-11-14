---
title: "pandoc(1)"
name: "pandoc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pandoc/"
---

<h2 class="name">NAME</h2>
 

 pandoc - general markup converter 

<h2>SYNOPSIS</h2>

 

 pandoc [options] [input-file]...

<h2>DESCRIPTION</h2>

 

 Pandoc is a Haskell library for converting from one markup format to another, and a command-line tool that uses this library. 

 Pandoc can convert between numerous markup and word processing formats, including, but not limited to, various flavors of Markdown, HTML, LaTeX and Word docx. For the full lists of input and output formats, see the --from and --to options below. Pandoc can also produce PDF output: see creating a PDF, below. 

 Pandoc's enhanced version of Markdown includes syntax for tables, definition lists, metadata blocks, footnotes, citations, math, and much more. See below under Pandoc's Markdown. 

 Pandoc has a modular design: it consists of a set of readers, which parse text in a given format and produce a native representation of the document (an abstract syntax tree or AST), and a set of writers, which convert this native representation into a target format. Thus, adding an input or output format requires only adding a reader or writer. Users can also run custom pandoc filters to modify the intermediate AST. 

 Because pandoc's intermediate representation of a document is less expressive than many of the formats it converts between, one should not expect perfect conversions between every format and every other. Pandoc attempts to preserve the structural elements of a document, but not formatting details such as margin size. And some document elements, such as complex tables, may not fit into pandoc's simple document model. While conversions from pandoc's Markdown to all formats aspire to be perfect, conversions from formats more expressive than pandoc's Markdown can be expected to be lossy.

<h3>Using pandoc</h3>

 

 If no input-files are specified, input is read from stdin. Output goes to stdout by default. For output to a file, use the -o option:
<dl>
<dt>
<dd> <pre>
pandoc -o output.html input.txt
</pre></dl>
 

 By default, pandoc produces a document fragment. To produce a standalone document (e.g. a valid HTML file including &lt;head&gt; and &lt;body&gt;), use the -s or --standalone flag:
<dl>
<dt>
<dd> <pre>
pandoc -s -o output.html input.txt
</pre></dl>
 

 For more information on how standalone documents are produced, see Templates below. 

 If multiple input files are given, pandoc will concatenate them all (with blank lines between them) before parsing. (Use --file-scope to parse files individually.)

<h3>Specifying formats</h3>

 

 The format of the input and output can be specified explicitly using command-line options. The input format can be specified using the -f/--from option, the output format using the -t/--to option. Thus, to convert hello.txt from Markdown to LaTeX, you could type:
<dl>
<dt>
<dd> <pre>
pandoc -f markdown -t latex hello.txt
</pre></dl>
 

 To convert hello.html from HTML to Markdown:
<dl>
<dt>
<dd> <pre>
pandoc -f html -t markdown hello.html
</pre></dl>
 

 Supported input and output formats are listed below under Options (see -f for input formats and -t for output formats). You can also use pandoc --list-input-formats and pandoc --list-output-formats to print lists of supported formats. 

 If the input or output format is not specified explicitly, pandoc will attempt to guess it from the extensions of the filenames. Thus, for example,
<dl>
<dt>
<dd> <pre>
pandoc -o hello.tex hello.txt
</pre></dl>
 

 will convert hello.txt from Markdown to LaTeX. If no output file is specified (so that output goes to stdout), or if the output file's extension is unknown, the output format will default to HTML. If no input file is specified (so that input comes from stdin), or if the input files' extensions are unknown, the input format will be assumed to be Markdown.

<h3>Character encoding</h3>

 

 Pandoc uses the UTF-8 character encoding for both input and output. If your local character encoding is not UTF-8, you should pipe input and output through iconv:
<dl>
<dt>
<dd> <pre>
iconv -t utf-8 input.txt | pandoc | iconv -f utf-8
</pre></dl>
 

 Note that in some output formats (such as HTML, LaTeX, ConTeXt, RTF, OPML, DocBook, and Texinfo), information about the character encoding is included in the document header, which will only be included if you use the -s/--standalone option.

<h3>Creating a PDF</h3>

 

 To produce a PDF, specify an output file with a .pdf extension:
<dl>
<dt>
<dd> <pre>
pandoc test.txt -o test.pdf
</pre></dl>
 

 By default, pandoc will use LaTeX to create the PDF, which requires that a LaTeX engine be installed (see --pdf-engine below). Alternatively, pandoc can use ConTeXt, roff ms, or HTML as an intermediate format. To do this, specify an output file with a .pdf extension, as before, but add the --pdf-engine option or -t context, -t html, or -t ms to the command line. The tool used to generate the PDF from the intermediate format may be specified using --pdf-engine. 

 You can control the PDF style using variables, depending on the intermediate format used: see variables for LaTeX, variables for ConTeXt, variables for wkhtmltopdf, variables for ms. When HTML is used as an intermediate format, the output can be styled using --css. 

 To debug the PDF creation, it can be useful to look at the intermediate representation: instead of -o test.pdf, use for example -s -o test.tex to output the generated LaTeX. You can then test it with pdflatex test.tex. 

 When using LaTeX, the following packages need to be available (they are included with all recent versions of TeX Live): amsfonts, amsmath, lm, unicode-math, ifxetex, ifluatex, listings (if the --listings option is used), fancyvrb, longtable, booktabs, graphicx (if the document contains images), hyperref, xcolor, ulem, geometry (with the geometry variable set), setspace (with linestretch), and babel (with lang). The use of xelatex or lualatex as the PDF engine requires fontspec. xelatex uses polyglossia (with lang), xecjk, and bidi (with the dir variable set). If the mathspec variable is set, xelatex will use mathspec instead of unicode-math. The upquote and microtype packages are used if available, and csquotes will be used for typography if the csquotes variable or metadata field is set to a true value. The natbib, biblatex, bibtex, and biber packages can optionally be used for citation rendering. The following packages will be used to improve output quality if present, but pandoc does not require them to be present: upquote (for straight quotes in verbatim environments), microtype (for better spacing adjustments), parskip (for better inter-paragraph spaces), xurl (for better line breaks in URLs), bookmark (for better PDF bookmarks), and footnotehyper or footnote (to allow footnotes in tables).

<h3>Reading from the Web</h3>

 

 Instead of an input file, an absolute URI may be given. In this case pandoc will fetch the content using HTTP:
<dl>
<dt>
<dd> <pre>
pandoc -f html -t markdown <a rel="nofollow" HREF="https://www.fsf.org">https://www.fsf.org</a>
</pre></dl>
 

 It is possible to supply a custom User-Agent string or other header when requesting a document from a URL:
<dl>
<dt>
<dd> <pre>
pandoc -f html -t markdown --request-header User-Agent:&quot;Mozilla/5.0&quot; \
  <a rel="nofollow" HREF="https://www.fsf.org">https://www.fsf.org</a>
</pre></dl>

<h2>OPTIONS</h2>

<h3>General options</h3>

<dl>
<dt>-f FORMAT, -r FORMAT, --from=FORMAT, --read=FORMAT
<dd> Specify input format. FORMAT can be:
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> commonmark (CommonMark Markdown)
<dt>&bull;
<dd> creole (Creole 1.0)
<dt>&bull;
<dd> csv (CSV table)
<dt>&bull;
<dd> docbook (DocBook)
<dt>&bull;
<dd> docx (Word docx)
<dt>&bull;
<dd> dokuwiki (DokuWiki markup)
<dt>&bull;
<dd> epub (EPUB)
<dt>&bull;
<dd> fb2 (FictionBook2 e-book)
<dt>&bull;
<dd> gfm (GitHub-Flavored Markdown), or the deprecated and less accurate markdown_github; use markdown_github only if you need extensions not supported in gfm.
<dt>&bull;
<dd> haddock (Haddock markup)
<dt>&bull;
<dd> html (HTML)
<dt>&bull;
<dd> ipynb (Jupyter notebook)
<dt>&bull;
<dd> jats (JATS XML)
<dt>&bull;
<dd> jira (Jira wiki markup)
<dt>&bull;
<dd> json (JSON version of native AST)
<dt>&bull;
<dd> latex (LaTeX)
<dt>&bull;
<dd> markdown (Pandoc's Markdown)
<dt>&bull;
<dd> markdown_mmd (MultiMarkdown)
<dt>&bull;
<dd> markdown_phpextra (PHP Markdown Extra)
<dt>&bull;
<dd> markdown_strict (original unextended Markdown)
<dt>&bull;
<dd> mediawiki (MediaWiki markup)
<dt>&bull;
<dd> man (roff man)
<dt>&bull;
<dd> muse (Muse)
<dt>&bull;
<dd> native (native Haskell)
<dt>&bull;
<dd> odt (ODT)
<dt>&bull;
<dd> opml (OPML)
<dt>&bull;
<dd> org (Emacs Org mode)
<dt>&bull;
<dd> rst (reStructuredText)
<dt>&bull;
<dd> t2t (txt2tags)
<dt>&bull;
<dd> textile (Textile)
<dt>&bull;
<dd> tikiwiki (TikiWiki markup)
<dt>&bull;
<dd> twiki (TWiki markup)
<dt>&bull;
<dd> vimwiki (Vimwiki)</dl>
 

 Extensions can be individually enabled or disabled by appending +EXTENSION or -EXTENSION to the format name. See Extensions below, for a list of extensions and their names. See --list-input-formats and --list-extensions, below.</dl>

<dt>-t FORMAT, -w FORMAT, --to=FORMAT, --write=FORMAT
<dd> Specify output format. FORMAT can be:
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> asciidoc (AsciiDoc) or asciidoctor (AsciiDoctor)
<dt>&bull;
<dd> beamer (LaTeX beamer slide show)
<dt>&bull;
<dd> commonmark (CommonMark Markdown)
<dt>&bull;
<dd> context (ConTeXt)
<dt>&bull;
<dd> docbook or docbook4 (DocBook 4)
<dt>&bull;
<dd> docbook5 (DocBook 5)
<dt>&bull;
<dd> docx (Word docx)
<dt>&bull;
<dd> dokuwiki (DokuWiki markup)
<dt>&bull;
<dd> epub or epub3 (EPUB v3 book)
<dt>&bull;
<dd> epub2 (EPUB v2)
<dt>&bull;
<dd> fb2 (FictionBook2 e-book)
<dt>&bull;
<dd> gfm (GitHub-Flavored Markdown), or the deprecated and less accurate markdown_github; use markdown_github only if you need extensions not supported in gfm.
<dt>&bull;
<dd> haddock (Haddock markup)
<dt>&bull;
<dd> html or html5 (HTML, i.e. HTML5/XHTML polyglot markup)
<dt>&bull;
<dd> html4 (XHTML 1.0 Transitional)
<dt>&bull;
<dd> icml (InDesign ICML)
<dt>&bull;
<dd> ipynb (Jupyter notebook)
<dt>&bull;
<dd> jats_archiving (JATS XML, Archiving and Interchange Tag Set)
<dt>&bull;
<dd> jats_articleauthoring (JATS XML, Article Authoring Tag Set)
<dt>&bull;
<dd> jats_publishing (JATS XML, Journal Publishing Tag Set)
<dt>&bull;
<dd> jats (alias for jats_archiving)
<dt>&bull;
<dd> jira (Jira wiki markup)
<dt>&bull;
<dd> json (JSON version of native AST)
<dt>&bull;
<dd> latex (LaTeX)
<dt>&bull;
<dd> man (roff man)
<dt>&bull;
<dd> markdown (Pandoc's Markdown)
<dt>&bull;
<dd> markdown_mmd (MultiMarkdown)
<dt>&bull;
<dd> markdown_phpextra (PHP Markdown Extra)
<dt>&bull;
<dd> markdown_strict (original unextended Markdown)
<dt>&bull;
<dd> mediawiki (MediaWiki markup)
<dt>&bull;
<dd> ms (roff ms)
<dt>&bull;
<dd> muse (Muse),
<dt>&bull;
<dd> native (native Haskell),
<dt>&bull;
<dd> odt (OpenOffice text document)
<dt>&bull;
<dd> opml (OPML)
<dt>&bull;
<dd> opendocument (OpenDocument)
<dt>&bull;
<dd> org (Emacs Org mode)
<dt>&bull;
<dd> pdf (PDF)
<dt>&bull;
<dd> plain (plain text),
<dt>&bull;
<dd> pptx (PowerPoint slide show)
<dt>&bull;
<dd> rst (reStructuredText)
<dt>&bull;
<dd> rtf (Rich Text Format)
<dt>&bull;
<dd> texinfo (GNU Texinfo)
<dt>&bull;
<dd> textile (Textile)
<dt>&bull;
<dd> slideous (Slideous HTML and JavaScript slide show)
<dt>&bull;
<dd> slidy (Slidy HTML and JavaScript slide show)
<dt>&bull;
<dd> dzslides (DZSlides HTML5 + JavaScript slide show),
<dt>&bull;
<dd> revealjs (reveal.js HTML5 + JavaScript slide show)
<dt>&bull;
<dd> s5 (S5 HTML and JavaScript slide show)
<dt>&bull;
<dd> tei (TEI Simple)
<dt>&bull;
<dd> xwiki (XWiki markup)
<dt>&bull;
<dd> zimwiki (ZimWiki markup)
<dt>&bull;
<dd> the path of a custom Lua writer, see Custom writers below</dl>
 

 Note that odt, docx, epub, and pdf output will not be directed to stdout unless forced with -o -. 

 Extensions can be individually enabled or disabled by appending +EXTENSION or -EXTENSION to the format name. See Extensions below, for a list of extensions and their names. See --list-output-formats and --list-extensions, below.</dl>

<dt>-o FILE, --output=FILE
<dd> Write output to FILE instead of stdout. If FILE is -, output will go to stdout, even if a non-textual format (docx, odt, epub2, epub3) is specified.
<dt>--data-dir=DIRECTORY
<dd> Specify the user data directory to search for pandoc data files. If this option is not specified, the default user data directory will be used. On *nix and macOS systems this will be the pandoc subdirectory of the XDG data directory (by default, $HOME/.local/share, overridable by setting the XDG_DATA_HOME environment variable). If that directory does not exist, $HOME/.pandoc will be used (for backwards compatibility). In Windows the default user data directory is C:\Users\USERNAME\AppData\Roaming\pandoc. You can find the default user data directory on your system by looking at the output of pandoc --version. A reference.odt, reference.docx, epub.css, templates, slidy, slideous, or s5 directory placed in this directory will override pandoc's normal defaults.
<dt>-d FILE, --defaults=FILE
<dd> Specify a set of default option settings. FILE is a YAML file whose fields correspond to command-line option settings. All options for document conversion, including input and output files, can be set using a defaults file. The file will be searched for first in the working directory, and then in the defaults subdirectory of the user data directory (see --data-dir). The .yaml extension may be omitted. See the section Default files for more information on the file format. Settings from the defaults file may be overridden or extended by subsequent options on the command line.
<dt>--bash-completion
<dd> Generate a bash completion script. To enable bash completion with pandoc, add this to your .bashrc:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
eval &quot;$(pandoc --bash-completion)&quot;
</pre></dl>
</dl>

<dt>--verbose
<dd> Give verbose debugging output. Currently this only has an effect with PDF output.
<dt>--quiet
<dd> Suppress warning messages.
<dt>--fail-if-warnings
<dd> Exit with error status if there are any warnings.
<dt>--log=FILE
<dd> Write log messages in machine-readable JSON format to FILE. All messages above DEBUG level will be written, regardless of verbosity settings (--verbose, --quiet).
<dt>--list-input-formats
<dd> List supported input formats, one per line.
<dt>--list-output-formats
<dd> List supported output formats, one per line.
<dt>--list-extensions[=FORMAT]
<dd> List supported extensions for FORMAT, one per line, preceded by a + or - indicating whether it is enabled by default in FORMAT. If FORMAT is not specified, defaults for pandoc's Markdown are given.
<dt>--list-highlight-languages
<dd> List supported languages for syntax highlighting, one per line.
<dt>--list-highlight-styles
<dd> List supported styles for syntax highlighting, one per line. See --highlight-style.
<dt>-v, --version
<dd> Print version.
<dt>-h, --help
<dd> Show usage message.</dl>

<h3>Reader options</h3>

<dl>
<dt>--shift-heading-level-by=NUMBER
<dd> Shift heading levels by a positive or negative integer. For example, with --shift-heading-level-by=-1, level 2 headings become level 1 headings, and level 3 headings become level 2 headings. Headings cannot have a level less than 1, so a heading that would be shifted below level 1 becomes a regular paragraph. Exception: with a shift of -N, a level-N heading at the beginning of the document replaces the metadata title. --shift-heading-level-by=-1 is a good choice when converting HTML or Markdown documents that use an initial level-1 heading for the document title and level-2+ headings for sections. --shift-heading-level-by=1 may be a good choice for converting Markdown documents that use level-1 headings for sections to HTML, since pandoc uses a level-1 heading to render the document title.
<dt>--base-header-level=NUMBER
<dd> Deprecated. Use --shift-heading-level-by=X instead, where X = NUMBER - 1. Specify the base level for headings (defaults to 1).
<dt>--strip-empty-paragraphs
<dd> Deprecated. Use the +empty_paragraphs extension instead. Ignore paragraphs with no content. This option is useful for converting word processing documents where users have used empty paragraphs to create inter-paragraph space.
<dt>--indented-code-classes=CLASSES
<dd> Specify classes to use for indented code blocks--for example, perl,numberLines or haskell. Multiple classes may be separated by spaces or commas.
<dt>--default-image-extension=EXTENSION
<dd> Specify a default extension to use when image paths/URLs have no extension. This allows you to use the same source for formats that require different kinds of images. Currently this option only affects the Markdown and LaTeX readers.
<dt>--file-scope
<dd> Parse each file individually before combining for multifile documents. This will allow footnotes in different files with the same identifiers to work as expected. If this option is set, footnotes and links will not work across files. Reading binary files (docx, odt, epub) implies --file-scope.
<dt>-F PROGRAM, --filter=PROGRAM
<dd> Specify an executable to be used as a filter transforming the pandoc AST after the input is parsed and before the output is written. The executable should read JSON from stdin and write JSON to stdout. The JSON must be formatted like pandoc's own JSON input and output. The name of the output format will be passed to the filter as the first argument. Hence,
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
pandoc --filter ./caps.py -t latex
</pre></dl>
 

 is equivalent to
<dl>
<dt>
<dd> <pre>
pandoc -t json | ./caps.py latex | pandoc -f json -t latex
</pre></dl>
 

 The latter form may be useful for debugging filters. 

 Filters may be written in any language. Text.Pandoc.JSON exports toJSONFilter to facilitate writing filters in Haskell. Those who would prefer to write filters in python can use the module pandocfilters, installable from PyPI. There are also pandoc filter libraries in PHP, perl, and JavaScript/node.js. 

 In order of preference, pandoc will look for filters in
<dl>
<dt>1.
<dd> a specified full or relative path (executable or non-executable)
<dt>2.
<dd> $DATADIR/filters (executable or non-executable) where $DATADIR is the user data directory (see --data-dir, above).
<dt>3.
<dd> $PATH (executable only)</dl>
 

 Filters and Lua-filters are applied in the order specified on the command line.</dl>

<dt>-L SCRIPT, --lua-filter=SCRIPT
<dd> Transform the document in a similar fashion as JSON filters (see --filter), but use pandoc's build-in Lua filtering system. The given Lua script is expected to return a list of Lua filters which will be applied in order. Each Lua filter must contain element-transforming functions indexed by the name of the AST element on which the filter function should be applied.
<dl>
<dt>
<dd> 

 The pandoc Lua module provides helper functions for element creation. It is always loaded into the script's Lua environment. 

 The following is an example Lua script for macro-expansion:
<dl>
<dt>
<dd> <pre><code>
function expand_hello_world(inline) if inline.c == '&#123;&#123;helloworld}}' then
                                                   return pandoc.Emph
{
    pandoc.Str "Hello, World"
}
else return inline end
    end return
{
    {
        Str = expand_hello_world
    }
}
</code></pre></dl>
 

 In order of preference, pandoc will look for Lua filters in
<dl>
<dt>1.
<dd> a specified full or relative path (executable or non-executable)
<dt>2.
<dd> $DATADIR/filters (executable or non-executable) where $DATADIR is the user data directory (see --data-dir, above).</dl>
</dl>

<dt>-M KEY[=VAL], --metadata=KEY[:VAL]
<dd> Set the metadata field KEY to the value VAL. A value specified on the command line overrides a value specified in the document using YAML metadata blocks. Values will be parsed as YAML boolean or string values. If no value is specified, the value will be treated as Boolean true. Like --variable, --metadata causes template variables to be set. But unlike --variable, --metadata affects the metadata of the underlying document (which is accessible from filters and may be printed in some output formats) and metadata values will be escaped when inserted into the template.
<dt>--metadata-file=FILE
<dd> Read metadata from the supplied YAML (or JSON) file. This option can be used with every input format, but string scalars in the YAML file will always be parsed as Markdown. Generally, the input will be handled the same as in YAML metadata blocks. This option can be used repeatedly to include multiple metadata files; values in files specified later on the command line will be preferred over those specified in earlier files. Metadata values specified inside the document, or by using -M, overwrite values specified with this option.
<dt>-p, --preserve-tabs
<dd> Preserve tabs instead of converting them to spaces. (By default, pandoc converts tabs to spaces before parsing its input.) Note that this will only affect tabs in literal code spans and code blocks. Tabs in regular text are always treated as spaces.
<dt>--tab-stop=NUMBER
<dd> Specify the number of spaces per tab (default is 4).
<dt>--track-changes=accept|reject|all
<dd> Specifies what to do with insertions, deletions, and comments produced by the MS Word &quot;Track Changes&quot; feature. accept (the default), inserts all insertions, and ignores all deletions. reject inserts all deletions and ignores insertions. Both accept and reject ignore comments. all puts in insertions, deletions, and comments, wrapped in spans with insertion, deletion, comment-start, and comment-end classes, respectively. The author and time of change is included. all is useful for scripting: only accepting changes from a certain reviewer, say, or before a certain date. If a paragraph is inserted or deleted, track-changes=all produces a span with the class paragraph-insertion/paragraph-deletion before the affected paragraph break. This option only affects the docx reader.
<dt>--extract-media=DIR
<dd> Extract images and other media contained in or linked from the source document to the path DIR, creating it if necessary, and adjust the images references in the document so they point to the extracted files. If the source format is a binary container (docx, epub, or odt), the media is extracted from the container and the original filenames are used. Otherwise the media is read from the file system or downloaded, and new filenames are constructed based on SHA1 hashes of the contents.
<dt>--abbreviations=FILE
<dd> Specifies a custom abbreviations file, with abbreviations one to a line. If this option is not specified, pandoc will read the data file abbreviations from the user data directory or fall back on a system default. To see the system default, use pandoc --print-default-data-file=abbreviations. The only use pandoc makes of this list is in the Markdown reader. Strings ending in a period that are found in this list will be followed by a nonbreaking space, so that the period will not produce sentence-ending space in formats like LaTeX.</dl>

<h3>General writer options</h3>

<dl>
<dt>-s, --standalone
<dd> Produce output with an appropriate header and footer (e.g. a standalone HTML, LaTeX, TEI, or RTF file, not a fragment). This option is set automatically for pdf, epub, epub3, fb2, docx, and odt output. For native output, this option causes metadata to be included; otherwise, metadata is suppressed.
<dt>--template=FILE|URL
<dd> Use the specified file as a custom template for the generated document. Implies --standalone. See Templates, below, for a description of template syntax. If no extension is specified, an extension corresponding to the writer will be added, so that --template=special looks for special.html for HTML output. If the template is not found, pandoc will search for it in the templates subdirectory of the user data directory (see --data-dir). If this option is not used, a default template appropriate for the output format will be used (see -D/--print-default-template).
<dt>-V KEY[=VAL], --variable=KEY[:VAL]
<dd> Set the template variable KEY to the value VAL when rendering the document in standalone mode. If no VAL is specified, the key will be given the value true.
<dt>-D FORMAT, --print-default-template=FORMAT
<dd> Print the system default template for an output FORMAT. (See -t for a list of possible FORMATs.) Templates in the user data directory are ignored. This option may be used with -o/--output to redirect output to a file, but -o/--output must come before --print-default-template on the command line.
<dl>
<dt>
<dd> 

 Note that some of the default templates use partials, for example styles.html. To print the partials, use --print-default-data-file: for example, --print-default-data-file=templates/styles.html.</dl>

<dt>--print-default-data-file=FILE
<dd> Print a system default data file. Files in the user data directory are ignored. This option may be used with -o/--output to redirect output to a file, but -o/--output must come before --print-default-data-file on the command line.
<dt>--eol=crlf|lf|native
<dd> Manually specify line endings: crlf (Windows), lf (macOS/Linux/UNIX), or native (line endings appropriate to the OS on which pandoc is being run). The default is native.
<dt>--dpi=NUMBER
<dd> Specify the default dpi (dots per inch) value for conversion from pixels to inch/centimeters and vice versa. (Technically, the correct term would be ppi: pixels per inch.) The default is 96dpi. When images contain information about dpi internally, the encoded value is used instead of the default specified by this option.
<dt>--wrap=auto|none|preserve
<dd> Determine how text is wrapped in the output (the source code, not the rendered version). With auto (the default), pandoc will attempt to wrap lines to the column width specified by --columns (default 72). With none, pandoc will not wrap lines at all. With preserve, pandoc will attempt to preserve the wrapping from the source document (that is, where there are nonsemantic newlines in the source, there will be nonsemantic newlines in the output as well). Automatic wrapping does not currently work in HTML output. In ipynb output, this option affects wrapping of the contents of markdown cells.
<dt>--columns=NUMBER
<dd> Specify length of lines in characters. This affects text wrapping in the generated source code (see --wrap). It also affects calculation of column widths for plain text tables (see Tables below).
<dt>--toc, --table-of-contents
<dd> Include an automatically generated table of contents (or, in the case of latex, context, docx, odt, opendocument, rst, or ms, an instruction to create one) in the output document. This option has no effect unless -s/--standalone is used, and it has no effect on man, docbook4, docbook5, or jats output.
<dl>
<dt>
<dd> 

 Note that if you are producing a PDF via ms, the table of contents will appear at the beginning of the document, before the title. If you would prefer it to be at the end of the document, use the option --pdf-engine-opt=--no-toc-relocation.</dl>

<dt>--toc-depth=NUMBER
<dd> Specify the number of section levels to include in the table of contents. The default is 3 (which means that level-1, 2, and 3 headings will be listed in the contents).
<dt>--strip-comments
<dd> Strip out HTML comments in the Markdown or Textile source, rather than passing them on to Markdown, Textile or HTML output as raw HTML. This does not apply to HTML comments inside raw HTML blocks when the markdown_in_html_blocks extension is not set.
<dt>--no-highlight
<dd> Disables syntax highlighting for code blocks and inlines, even when a language attribute is given.
<dt>--highlight-style=STYLE|FILE
<dd> Specifies the coloring style to be used in highlighted source code. Options are pygments (the default), kate, monochrome, breezeDark, espresso, zenburn, haddock, and tango. For more information on syntax highlighting in pandoc, see Syntax highlighting, below. See also --list-highlight-styles.
<dl>
<dt>
<dd> 

 Instead of a STYLE name, a JSON file with extension .theme may be supplied. This will be parsed as a KDE syntax highlighting theme and (if valid) used as the highlighting style. 

 To generate the JSON version of an existing style, use --print-highlight-style.</dl>

<dt>--print-highlight-style=STYLE|FILE
<dd> Prints a JSON version of a highlighting style, which can be modified, saved with a .theme extension, and used with --highlight-style. This option may be used with -o/--output to redirect output to a file, but -o/--output must come before --print-highlight-style on the command line.
<dt>--syntax-definition=FILE
<dd> Instructs pandoc to load a KDE XML syntax definition file, which will be used for syntax highlighting of appropriately marked code blocks. This can be used to add support for new languages or to use altered syntax definitions for existing languages. This option may be repeated to add multiple syntax definitions.
<dt>-H FILE, --include-in-header=FILE|URL
<dd> Include contents of FILE, verbatim, at the end of the header. This can be used, for example, to include special CSS or JavaScript in HTML documents. This option can be used repeatedly to include multiple files in the header. They will be included in the order specified. Implies --standalone.
<dt>-B FILE, --include-before-body=FILE|URL
<dd> Include contents of FILE, verbatim, at the beginning of the document body (e.g. after the &lt;body&gt; tag in HTML, or the \begin{document} command in LaTeX). This can be used to include navigation bars or banners in HTML documents. This option can be used repeatedly to include multiple files. They will be included in the order specified. Implies --standalone.
<dt>-A FILE, --include-after-body=FILE|URL
<dd> Include contents of FILE, verbatim, at the end of the document body (before the &lt;/body&gt; tag in HTML, or the \end{document} command in LaTeX). This option can be used repeatedly to include multiple files. They will be included in the order specified. Implies --standalone.
<dt>--resource-path=SEARCHPATH
<dd> List of paths to search for images and other resources. The paths should be separated by : on Linux, UNIX, and macOS systems, and by ; on Windows. If --resource-path is not specified, the default resource path is the working directory. Note that, if --resource-path is specified, the working directory must be explicitly listed or it will not be searched. For example: --resource-path=.:test will search the working directory and the test subdirectory, in that order.
<dl>
<dt>
<dd> 

 --resource-path only has an effect if (a) the output format embeds images (for example, docx, pdf, or html with --self-contained) or (b) it is used together with --extract-media.</dl>

<dt>--request-header=NAME:VAL
<dd> Set the request header NAME to the value VAL when making HTTP requests (for example, when a URL is given on the command line, or when resources used in a document must be downloaded). If you're behind a proxy, you also need to set the environment variable http_proxy to <a rel="nofollow" HREF="http://....">http://....</a></dl>

<h3>Options affecting specific writers</h3>

<dl>
<dt>--self-contained
<dd> Produce a standalone HTML file with no external dependencies, using data: URIs to incorporate the contents of linked scripts, stylesheets, images, and videos. Implies --standalone. The resulting file should be &quot;self-contained,&quot; in the sense that it needs no external files and no net access to be displayed properly by a browser. This option works only with HTML output formats, including html4, html5, html+lhs, html5+lhs, s5, slidy, slideous, dzslides, and revealjs. Scripts, images, and stylesheets at absolute URLs will be downloaded; those at relative URLs will be sought relative to the working directory (if the first source file is local) or relative to the base URL (if the first source file is remote). Elements with the attribute data-external=&quot;1&quot; will be left alone; the documents they link to will not be incorporated in the document. Limitation: resources that are loaded dynamically through JavaScript cannot be incorporated; as a result, --self-contained does not work with --mathjax, and some advanced features (e.g. zoom or speaker notes) may not work in an offline &quot;self-contained&quot; reveal.js slide show.
<dt>--html-q-tags
<dd> Use &lt;q&gt; tags for quotes in HTML.
<dt>--ascii
<dd> Use only ASCII characters in output. Currently supported for XML and HTML formats (which use entities instead of UTF-8 when this option is selected), CommonMark, gfm, and Markdown (which use entities), roff ms (which use hexadecimal escapes), and to a limited degree LaTeX (which uses standard commands for accented characters when possible). roff man output uses ASCII by default.
<dt>--reference-links
<dd> Use reference-style links, rather than inline links, in writing Markdown or reStructuredText. By default inline links are used. The placement of link references is affected by the --reference-location option.
<dt>--reference-location = block|section|document
<dd> Specify whether footnotes (and references, if reference-links is set) are placed at the end of the current (top-level) block, the current section, or the document. The default is document. Currently only affects the markdown writer.
<dt>--atx-headers
<dd> Use ATX-style headings in Markdown output. The default is to use setext-style headings for levels 1 to 2, and then ATX headings. (Note: for gfm output, ATX headings are always used.) This option also affects markdown cells in ipynb output.
<dt>--top-level-division=[default|section|chapter|part]
<dd> Treat top-level headings as the given division type in LaTeX, ConTeXt, DocBook, and TEI output. The hierarchy order is part, chapter, then section; all headings are shifted such that the top-level heading becomes the specified type. The default behavior is to determine the best division type via heuristics: unless other conditions apply, section is chosen. When the documentclass variable is set to report, book, or memoir (unless the article option is specified), chapter is implied as the setting for this option. If beamer is the output format, specifying either chapter or part will cause top-level headings to become \part{..}, while second-level headings remain as their default type.
<dt>-N, --number-sections
<dd> Number section headings in LaTeX, ConTeXt, HTML, or EPUB output. By default, sections are not numbered. Sections with class unnumbered will never be numbered, even if --number-sections is specified.
<dt>--number-offset=NUMBER[,NUMBER,...]
<dd> Offset for section headings in HTML output (ignored in other output formats). The first number is added to the section number for top-level headings, the second for second-level headings, and so on. So, for example, if you want the first top-level heading in your document to be numbered &quot;6&quot;, specify --number-offset=5. If your document starts with a level-2 heading which you want to be numbered &quot;1.5&quot;, specify --number-offset=1,4. Offsets are 0 by default. Implies --number-sections.
<dt>--listings
<dd> Use the listings package for LaTeX code blocks. The package does not support multi-byte encoding for source code. To handle UTF-8 you would need to use a custom template. This issue is fully documented here: Encoding issue with the listings package.
<dt>-i, --incremental
<dd> Make list items in slide shows display incrementally (one by one). The default is for lists to be displayed all at once.
<dt>--slide-level=NUMBER
<dd> Specifies that headings with the specified level create slides (for beamer, s5, slidy, slideous, dzslides). Headings above this level in the hierarchy are used to divide the slide show into sections; headings below this level create subheads within a slide. Note that content that is not contained under slide-level headings will not appear in the slide show. The default is to set the slide level based on the contents of the document; see Structuring the slide show.
<dt>--section-divs
<dd> Wrap sections in &lt;section&gt; tags (or &lt;div&gt; tags for html4), and attach identifiers to the enclosing &lt;section&gt; (or &lt;div&gt;) rather than the heading itself. See Heading identifiers, below.
<dt>--email-obfuscation=none|javascript|references
<dd> Specify a method for obfuscating mailto: links in HTML documents. none leaves mailto: links as they are. javascript obfuscates them using JavaScript. references obfuscates them by printing their letters as decimal or hexadecimal character references. The default is none.
<dt>--id-prefix=STRING
<dd> Specify a prefix to be added to all identifiers and internal links in HTML and DocBook output, and to footnote numbers in Markdown and Haddock output. This is useful for preventing duplicate identifiers when generating fragments to be included in other pages.
<dt>-T STRING, --title-prefix=STRING
<dd> Specify STRING as a prefix at the beginning of the title that appears in the HTML header (but not in the title as it appears at the beginning of the HTML body). Implies --standalone.
<dt>-c URL, --css=URL
<dd> Link to a CSS style sheet. This option can be used repeatedly to include multiple files. They will be included in the order specified.
<dl>
<dt>
<dd> 

 A stylesheet is required for generating EPUB. If none is provided using this option (or the css or stylesheet metadata fields), pandoc will look for a file epub.css in the user data directory (see --data-dir). If it is not found there, sensible defaults will be used.</dl>

<dt>--reference-doc=FILE
<dd> Use the specified file as a style reference in producing a docx or ODT file.
<dl>
<dt>
<dd>
<dl>
<dt>Docx
<dd> For best results, the reference docx should be a modified version of a docx file produced using pandoc. The contents of the reference docx are ignored, but its stylesheets and document properties (including margins, page size, header, and footer) are used in the new docx. If no reference docx is specified on the command line, pandoc will look for a file reference.docx in the user data directory (see --data-dir). If this is not found either, sensible defaults will be used.
<dl>
<dt>
<dd> 

 To produce a custom reference.docx, first get a copy of the default reference.docx: pandoc -o custom-reference.docx --print-default-data-file reference.docx. Then open custom-reference.docx in Word, modify the styles as you wish, and save the file. For best results, do not make changes to this file other than modifying the styles used by pandoc: 

 Paragraph styles:
<dl>
<dt>&bull;
<dd> Normal
<dt>&bull;
<dd> Body Text
<dt>&bull;
<dd> First Paragraph
<dt>&bull;
<dd> Compact
<dt>&bull;
<dd> Title
<dt>&bull;
<dd> Subtitle
<dt>&bull;
<dd> Author
<dt>&bull;
<dd> Date
<dt>&bull;
<dd> Abstract
<dt>&bull;
<dd> Bibliography
<dt>&bull;
<dd> Heading 1
<dt>&bull;
<dd> Heading 2
<dt>&bull;
<dd> Heading 3
<dt>&bull;
<dd> Heading 4
<dt>&bull;
<dd> Heading 5
<dt>&bull;
<dd> Heading 6
<dt>&bull;
<dd> Heading 7
<dt>&bull;
<dd> Heading 8
<dt>&bull;
<dd> Heading 9
<dt>&bull;
<dd> Block Text
<dt>&bull;
<dd> Footnote Text
<dt>&bull;
<dd> Definition Term
<dt>&bull;
<dd> Definition
<dt>&bull;
<dd> Caption
<dt>&bull;
<dd> Table Caption
<dt>&bull;
<dd> Image Caption
<dt>&bull;
<dd> Figure
<dt>&bull;
<dd> Captioned Figure
<dt>&bull;
<dd> TOC Heading</dl>
 

 Character styles:
<dl>
<dt>&bull;
<dd> Default Paragraph Font
<dt>&bull;
<dd> Body Text Char
<dt>&bull;
<dd> Verbatim Char
<dt>&bull;
<dd> Footnote Reference
<dt>&bull;
<dd> Hyperlink</dl>
 

 Table style:
<dl>
<dt>&bull;
<dd> Table</dl>
</dl>

<dt>ODT
<dd> For best results, the reference ODT should be a modified version of an ODT produced using pandoc. The contents of the reference ODT are ignored, but its stylesheets are used in the new ODT. If no reference ODT is specified on the command line, pandoc will look for a file reference.odt in the user data directory (see --data-dir). If this is not found either, sensible defaults will be used.
<dl>
<dt>
<dd> 

 To produce a custom reference.odt, first get a copy of the default reference.odt: pandoc -o custom-reference.odt --print-default-data-file reference.odt. Then open custom-reference.odt in LibreOffice, modify the styles as you wish, and save the file.</dl>

<dt>PowerPoint
<dd> Templates included with Microsoft PowerPoint 2013 (either with .pptx or .potx extension) are known to work, as are most templates derived from these.
<dl>
<dt>
<dd> 

 The specific requirement is that the template should begin with the following first four layouts:
<dl>
<dt>1.
<dd> Title Slide
<dt>2.
<dd> Title and Content
<dt>3.
<dd> Section Header
<dt>4.
<dd> Two Content</dl>
 

 All templates included with a recent version of MS PowerPoint will fit these criteria. (You can click on Layout under the Home menu to check.) 

 You can also modify the default reference.pptx: first run pandoc -o custom-reference.pptx --print-default-data-file reference.pptx, and then modify custom-reference.pptx in MS PowerPoint (pandoc will use the first four layout slides, as mentioned above).</dl>
</dl>
</dl>

<dt>--epub-cover-image=FILE
<dd> Use the specified image as the EPUB cover. It is recommended that the image be less than 1000px in width and height. Note that in a Markdown source document you can also specify cover-image in a YAML metadata block (see EPUB Metadata, below).
<dt>--epub-metadata=FILE
<dd> Look in the specified XML file for metadata for the EPUB. The file should contain a series of Dublin Core elements. For example:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
 &lt;dc:rights&gt;Creative Commons&lt;/dc:rights&gt;
 &lt;dc:language&gt;es-AR&lt;/dc:language&gt;
</pre></dl>
 

 By default, pandoc will include the following metadata elements: &lt;dc:title&gt; (from the document title), &lt;dc:creator&gt; (from the document authors), &lt;dc:date&gt; (from the document date, which should be in ISO 8601 format), &lt;dc:language&gt; (from the lang variable, or, if is not set, the locale), and &lt;dc:identifier id=&quot;BookId&quot;&gt; (a randomly generated UUID). Any of these may be overridden by elements in the metadata file. 

 Note: if the source document is Markdown, a YAML metadata block in the document can be used instead. See below under EPUB Metadata.</dl>

<dt>--epub-embed-font=FILE
<dd> Embed the specified font in the EPUB. This option can be repeated to embed multiple fonts. Wildcards can also be used: for example, DejaVuSans-*.ttf. However, if you use wildcards on the command line, be sure to escape them or put the whole filename in single quotes, to prevent them from being interpreted by the shell. To use the embedded fonts, you will need to add declarations like the following to your CSS (see --css):
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
@font - face
{
    font - family : DejaVuSans;
    font - style : normal;
    font - weight : normal;
src:
    url("DejaVuSans-Regular.ttf");
}
@font - face
{
    font - family : DejaVuSans;
    font - style : normal;
    font - weight : bold;
src:
    url("DejaVuSans-Bold.ttf");
}
@font - face
{
    font - family : DejaVuSans;
    font - style : italic;
    font - weight : normal;
src:
    url("DejaVuSans-Oblique.ttf");
}
@font - face
{
    font - family : DejaVuSans;
    font - style : italic;
    font - weight : bold;
src:
    url("DejaVuSans-BoldOblique.ttf");
}
body
{
    font - family : "DejaVuSans";
}
</dl>
</dl>

<dt>--epub-chapter-level=NUMBER
<dd> Specify the heading level at which to split the EPUB into separate &quot;chapter&quot; files. The default is to split into chapters at level-1 headings. This option only affects the internal composition of the EPUB, not the way chapters and sections are displayed to users. Some readers may be slow if the chapter files are too large, so for large documents with few level-1 headings, one might want to use a chapter level of 2 or 3.
<dt>--epub-subdirectory=DIRNAME
<dd> Specify the subdirectory in the OCF container that is to hold the EPUB-specific contents. The default is EPUB. To put the EPUB contents in the top level, use an empty string.
<dt>--ipynb-output=all|none|best
<dd> Determines how ipynb output cells are treated. all means that all of the data formats included in the original are preserved. none means that the contents of data cells are omitted. best causes pandoc to try to pick the richest data block in each output cell that is compatible with the output format. The default is best.
<dt>--pdf-engine=PROGRAM
<dd> Use the specified engine when producing PDF output. Valid values are pdflatex, lualatex, xelatex, latexmk, tectonic, wkhtmltopdf, weasyprint, prince, context, and pdfroff. If the engine is not in your PATH, the full path of the engine may be specified here. If this option is not specified, pandoc uses the following defaults depending on the output format specified using -t/--to:
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> -t latex or none: pdflatex (other options: xelatex, lualatex, tectonic, latexmk)
<dt>&bull;
<dd> -t context: context
<dt>&bull;
<dd> -t html: wkhtmltopdf (other options: prince, weasyprint)
<dt>&bull;
<dd> -t ms: pdfroff</dl>
</dl>

<dt>--pdf-engine-opt=STRING
<dd> Use the given string as a command-line argument to the pdf-engine. For example, to use a persistent directory foo for latexmk's auxiliary files, use --pdf-engine-opt=-outdir=foo. Note that no check for duplicate options is done.</dl>

<h3>Citation rendering</h3>

<dl>
<dt>--bibliography=FILE
<dd> Set the bibliography field in the document's metadata to FILE, overriding any value set in the metadata, and process citations using pandoc-citeproc. (This is equivalent to --metadata bibliography=FILE --filter pandoc-citeproc.) If --natbib or --biblatex is also supplied, pandoc-citeproc is not used, making this equivalent to --metadata bibliography=FILE. If you supply this argument multiple times, each FILE will be added to bibliography.
<dt>--csl=FILE
<dd> Set the csl field in the document's metadata to FILE, overriding any value set in the metadata. (This is equivalent to --metadata csl=FILE.) This option is only relevant with pandoc-citeproc.
<dt>--citation-abbreviations=FILE
<dd> Set the citation-abbreviations field in the document's metadata to FILE, overriding any value set in the metadata. (This is equivalent to --metadata citation-abbreviations=FILE.) This option is only relevant with pandoc-citeproc.
<dt>--natbib
<dd> Use natbib for citations in LaTeX output. This option is not for use with the pandoc-citeproc filter or with PDF output. It is intended for use in producing a LaTeX file that can be processed with bibtex.
<dt>--biblatex
<dd> Use biblatex for citations in LaTeX output. This option is not for use with the pandoc-citeproc filter or with PDF output. It is intended for use in producing a LaTeX file that can be processed with bibtex or biber.</dl>

<h3>Math rendering in HTML</h3>

 

 The default is to render TeX math as far as possible using Unicode characters. Formulas are put inside a span with class=&quot;math&quot;, so that they may be styled differently from the surrounding text if needed. However, this gives acceptable results only for basic math, usually you will want to use --mathjax or another of the following options.
<dl>
<dt>--mathjax[=URL]
<dd> Use MathJax to display embedded TeX math in HTML output. TeX math will be put between \(...\) (for inline math) or \[...\] (for display math) and wrapped in &lt;span&gt; tags with class math. Then the MathJax JavaScript will render it. The URL should point to the MathJax.js load script. If a URL is not provided, a link to the Cloudflare CDN will be inserted.
<dt>--mathml
<dd> Convert TeX math to MathML (in epub3, docbook4, docbook5, jats, html4 and html5). This is the default in odt output. Note that currently only Firefox and Safari (and select e-book readers) natively support MathML.
<dt>--webtex[=URL]
<dd> Convert TeX formulas to &lt;img&gt; tags that link to an external script that converts formulas to images. The formula will be URL-encoded and concatenated with the URL provided. For SVG images you can for example use --webtex <a rel="nofollow" HREF="https://latex.codecogs.com/svg.latex?.">https://latex.codecogs.com/svg.latex?.</a> If no URL is specified, the CodeCogs URL generating PNGs will be used (<a rel="nofollow" HREF="https://latex.codecogs.com/png.latex?">https://latex.codecogs.com/png.latex?</a>). Note: the --webtex option will affect Markdown output as well as HTML, which is useful if you're targeting a version of Markdown without native math support.
<dt>--katex[=URL]
<dd> Use KaTeX to display embedded TeX math in HTML output. The URL is the base URL for the KaTeX library. That directory should contain a katex.min.js and a katex.min.css file. If a URL is not provided, a link to the KaTeX CDN will be inserted.
<dt>--gladtex
<dd> Enclose TeX math in &lt;eq&gt; tags in HTML output. The resulting HTML can then be processed by GladTeX to produce images of the typeset formulas and an HTML file with links to these images. So, the procedure is:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
pandoc -s --gladtex input.md -o myfile.htex
gladtex -d myfile-images myfile.htex
# produces myfile.html and images in myfile-images
</pre></dl>
</dl>
</dl>

<h3>Options for wrapper scripts</h3>

<dl>
<dt>--dump-args
<dd> Print information about command-line arguments to stdout, then exit. This option is intended primarily for use in wrapper scripts. The first line of output contains the name of the output file specified with the -o option, or - (for stdout) if no output file was specified. The remaining lines contain the command-line arguments, one per line, in the order they appear. These do not include regular pandoc options and their arguments, but do include any options appearing after a -- separator at the end of the line.
<dt>--ignore-args
<dd> Ignore command-line arguments (for use in wrapper scripts). Regular pandoc options are not ignored. Thus, for example,
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
pandoc --ignore-args -o foo.html -s foo.txt -- -e latin1
</pre></dl>
 

 is equivalent to
<dl>
<dt>
<dd> <pre>
pandoc -o foo.html -s
</pre></dl>
</dl>
</dl>

<h2>EXIT CODES</h2>

 

 If pandoc completes successfully, it will return exit code 0. Nonzero exit codes have the following meanings: 

 <table> <tr VALIGN=top><td ALIGN=right> Code </td><td> Error 
</td></tr> <tr VALIGN=top><td COLSPAN=2><hr></td></tr> <tr VALIGN=top><td ALIGN=right> 3 </td><td> PandocFailOnWarningError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 4 </td><td> PandocAppError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 5 </td><td> PandocTemplateError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 6 </td><td> PandocOptionError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 21 </td><td> PandocUnknownReaderError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 22 </td><td> PandocUnknownWriterError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 23 </td><td> PandocUnsupportedExtensionError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 31 </td><td> PandocEpubSubdirectoryError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 43 </td><td> PandocPDFError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 47 </td><td> PandocPDFProgramNotFoundError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 61 </td><td> PandocHttpError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 62 </td><td> PandocShouldNeverHappenError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 63 </td><td> PandocSomeError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 64 </td><td> PandocParseError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 65 </td><td> PandocParsecError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 66 </td><td> PandocMakePDFError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 67 </td><td> PandocSyntaxMapError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 83 </td><td> PandocFilterError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 91 </td><td> PandocMacroLoop 
</td></tr> <tr VALIGN=top><td ALIGN=right> 92 </td><td> PandocUTF8DecodingError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 93 </td><td> PandocIpynbDecodingError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 97 </td><td> PandocCouldNotFindDataFileError 
</td></tr> <tr VALIGN=top><td ALIGN=right> 99 </td><td> PandocResourceNotFound 
</td></tr> </table>

<h2>DEFAULT FILES</h2>

 

 The --defaults option may be used to specify a package of options. Here is a sample defaults file demonstrating all of the fields that may be used:
<dl>
<dt>
<dd> 
from : markdown + emoji
#reader : may be used instead of from:
                      to : html5
#writer : may be used instead of to:
#leave blank for output to stdout:
                               output -
                           file :
#leave blank for input from stdin, use[] for no input:
    input -
    files : -preface.md - content.md
# or you may use input - file : with a single value
                          template : letter standalone : true self -
    contained : false
#note that structured variables may be specified:
                variables : documentclass : book
                                                classoption : -twosides -
                                                              draft
#metadata values specified here are parsed as literal
#string text, not markdown:
                                                                  metadata : author : -Sam Smith -
                                                                                      Julie Liu
                                                                                          metadata -
                                                                                      files : -boilerplate.yaml
# or you may use metadata - file : with a single value
#Note that these take files, not their contents:
                                                                                                  include -
                                                                                      before - body : [] include - after - body : [] include - in - header : [] resource - path : ["."]
#filters will be assumed to be Lua filters if they have
#the.lua extension, and json filters otherwise.But
#the filter type can also be specified explicitly, as shown:
                                                                                                                                                                                  filters : -pandoc -
                                                                                                                                                                                            citeproc - wordcount.lua - type : json path : foo.lua file - scope : false data - dir :
#ERROR, WARNING, or INFO
    verbosity : INFO log -
                file : log.json
#citeproc, natbib, or biblatex
                           cite -
                method : citeproc
#part, chapter, section, or default:
                             top -
                         level - division : chapter abbreviations : pdf - engine : pdflatex pdf - engine - opts : -"-shell-escape"
#you may also use pdf - engine - opt : with a single option
#pdf - engine - opt : "-shell-escape"
#auto, preserve, or none
                                                                                                                  wrap : auto columns : 78 dpi : 72 extract -
                                                                                                                         media : mediadir
                                                                                                                                     table -
                                                                                                                                 of - contents : true toc - depth : 2 number - sections : false
#a list of offsets at each heading level
                                                                                                                                                                                          number -
                                                                                                                                                                                          offset : [ 0, 0, 0, 0, 0, 0 ]
#toc : may also be used instead of table - of - contents:
                                                                                                                                                                                                   shift -
                                                                                                                                                                                                   heading - level - by : 1 section - divs : true identifier - prefix : foo title - prefix : "" strip - empty - paragraphs : true
#lf, crlf, or native
                                                                                                                                                                                                                                                                                                                             eol : lf strip -
                                                                                                                                                                                                                                                                                                                                   comments : false indented - code - classes : [] ascii : true default - image - extension : ".jpg"
#either a style name of a style definition file:
                                                                                                                                                                                                                                                                                                                                                                                                                              highlight -
                                                                                                                                                                                                                                                                                                                                                                                                                              style : pygments
                                                                                                                                                                                                                                                                                                                                                                                                                                          syntax -
                                                                                                                                                                                                                                                                                                                                                                                                                                      definitions : -c.xml
# or you may use syntax - definition : with a single value
                                                                                                                                                                                                                                                                                                                                                                                                                                                        listings : false reference -
                                                                                                                                                                                                                                                                                                                                                                                                                                      doc : myref.docx
#method is plain, webtex, gladtex, mathml, mathjax, katex
#you may specify a url with webtex, mathjax, katex
                                                                                                                                                                                                                                                                                                                                                                                                                                                html -
                                                                                                                                                                                                                                                                                                                                                                                                                                      math - method : method : mathjax url : "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
#none, references, or javascript
                                                                                                                                                                                                                                                                                                                                                                                                                                                                             email -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                             obfuscation : javascript
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               tab -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           stop : 8 preserve - tabs : true incremental : false slide - level : 2 epub - subdirectory : EPUB epub - metadata : meta.xml epub - fonts : -foobar.otf epub - chapter - level : 1 epub - cover - image : cover.jpg reference - links : true
#block, section, or document
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  reference -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  location : block
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 atx -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             headers : false
#accept, reject, or all
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       track -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       changes : accept
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     html -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 q - tags : false css : -site.css
#none, all, or best
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ipynb -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 output : best
#A list of two - element lists
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              request -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          headers : -[ "User-Agent", "Mozilla/5.0" ] fail - if - warnings : false dump - args : false ignore - args : false trace : false
</dl>
 

 Fields that are omitted will just have their regular default values. So a defaults file can be as simple as one line:
<dl>
<dt>
<dd> <pre>
verbosity: INFO
</pre></dl>
 

 Default files can be placed in the defaults subdirectory of the user data directory and used from any directory. For example, one could create a file specifying defaults for writing letters, save it as letter.yaml in the defaults subdirectory of the user data directory, and then invoke these defaults from any directory using pandoc --defaults letter or pandoc -dletter. 

 When multiple defaults are used, their contents will be combined. 

 Note that, where command-line arguments may be repeated (--metadata-file, --css, --include-in-header, --include-before-body, --include-after-body, --variable, --metadata, --syntax-definition), the values specified on the command line will combine with values specified in the defaults file, rather than replacing them.

<h2>TEMPLATES</h2>

 

 When the -s/--standalone option is used, pandoc uses a template to add header and footer material that is needed for a self-standing document. To see the default template that is used, just type
<dl>
<dt>
<dd> <pre>
pandoc -D *FORMAT*
</pre></dl>
 

 where FORMAT is the name of the output format. A custom template can be specified using the --template option. You can also override the system default templates for a given output format FORMAT by putting a file templates/default.*FORMAT* in the user data directory (see --data-dir, above). Exceptions:
<dl>
<dt>&bull;
<dd> For odt output, customize the default.opendocument template.
<dt>&bull;
<dd> For pdf output, customize the default.latex template (or the default.context template, if you use -t context, or the default.ms template, if you use -t ms, or the default.html template, if you use -t html).
<dt>&bull;
<dd> docx and pptx have no template (however, you can use --reference-doc to customize the output).</dl>
 

 Templates contain variables, which allow for the inclusion of arbitrary information at any point in the file. They may be set at the command line using the -V/--variable option. If a variable is not set, pandoc will look for the key in the document's metadata, which can be set using either YAML metadata blocks or with the -M/--metadata option. In addition, some variables are given default values by pandoc. See Variables below for a list of variables used in pandoc's default templates. 

 If you use custom templates, you may need to revise them as pandoc changes. We recommend tracking the changes in the default templates, and modifying your custom templates accordingly. An easy way to do this is to fork the pandoc-templates repository and merge in changes after each pandoc release.

<h3>Template syntax</h3>

<h3>Comments</h3>

 

 Anything between the sequence $-- and the end of the line will be treated as a comment and omitted from the output.

<h3>Delimiters</h3>

 

 To mark variables and control structures in the template, either $...$ or ${...} may be used as delimiters. The styles may also be mixed in the same template, but the opening and closing delimiter must match in each case. The opening delimiter may be followed by one or more spaces or tabs, which will be ignored. The closing delimiter may be followed by one or more spaces or tabs, which will be ignored. 

 To include a literal $ in the document, use $$.

<h3>Interpolated variables</h3>

 

 A slot for an interpolated variable is a variable name surrounded by matched delimiters. Variable names must begin with a letter and can contain letters, numbers, _, -, and .. The keywords it, if, else, endif, for, sep, and endfor may not be used as variable names. Examples:
<dl>
<dt>
<dd> 
$foo$
        $foo.bar.baz$
            $foo_bar.baz -
    bim$
        $ foo $
            ${foo} ${foo.bar.baz} ${foo_bar.baz - bim} $
{
    foo
}
</dl>
 

 Variable names with periods are used to get at structured variable values. So, for example, employee.salary will return the value of the salary field of the object that is the value of the employee field.
<dl>
<dt>&bull;
<dd> If the value of the variable is simple value, it will be rendered verbatim. (Note that no escaping is done; the assumption is that the calling program will escape the strings appropriately for the output format.)
<dt>&bull;
<dd> If the value is a list, the values will be concatenated.
<dt>&bull;
<dd> If the value is a map, the string true will be rendered.
<dt>&bull;
<dd> Every other value will be rendered as the empty string.</dl>

<h3>Conditionals</h3>

 

 A conditional begins with if(variable) (enclosed in matched delimiters) and ends with endif (enclosed in matched delimiters). It may optionally contain an else (enclosed in matched delimiters). The if section is used if variable has a non-empty value, otherwise the else section is used (if present). Examples:
<dl>
<dt>
<dd> 
$if(foo) $bar$endif$
    $if(foo)
$
    $foo$
        $endif$
        $if(foo)
$
    part one
        $else$
            part two
                $endif$
                    $
{
    if (foo)
}
bar${endif} $
{
    if (foo)
}
${foo} ${endif} $
{
    if (foo)
}
${foo.bar} ${else} no foo !$
{
    endif
}
</dl>
 

 The keyword elseif may be used to simplify complex nested conditionals:
<dl>
<dt>
<dd> <pre>
$if(foo)$
XXX
$elseif(bar)$
YYY
$else$
ZZZ
$endif$
</pre></dl>

<h3>For loops</h3>

 

 A for loop begins with for(variable) (enclosed in matched delimiters) and ends with endfor (enclosed in matched delimiters.
<dl>
<dt>&bull;
<dd> If variable is an array, the material inside the loop will be evaluated repeatedly, with variable being set to each value of the array in turn, and concatenated.
<dt>&bull;
<dd> If variable is a map, the material inside will be set to the map.
<dt>&bull;
<dd> If the value of the associated variable is not an array or a map, a single iteration will be performed on its value.</dl>
 

 Examples:
<dl>
<dt>
<dd> 
$for(foo) $$foo$$sep$, $endfor$ $for(foo) $ - $foo.last$, $foo.first$ $endfor$ $
{
    for (foo.bar)
}
- ${foo.bar.last}, ${foo.bar.first} ${endfor} $for(mymap)$
                   $it.name$:$it.office$
                             $endfor$
</dl>
 

 You may optionally specify a separator between consecutive values using sep (enclosed in matched delimiters). The material between sep and the endfor is the separator.
<dl>
<dt>
<dd> 
$
{
    for (foo)
}
${foo} ${sep}, $
{
    endfor
}
</dl>
 

 Instead of using variable inside the loop, the special anaphoric keyword it may be used.
<dl>
<dt>
<dd> 
$
{
    for (foo.bar)
}
- ${it.last}, ${it.first} $
{
    endfor
}
</dl>

<h3>Partials</h3>

 

 Partials (subtemplates stored in different files) may be included using the syntax
<dl>
<dt>
<dd> <pre>
${ boilerplate() }
</pre></dl>
 

 Partials will be sought in the directory containing the main template, and will be assumed to have the same extension as the main template if they lack an explicit extension. (If the partials are not found here, they will also be sought in the templates subdirectory of the user data directory.) 

 Partials may optionally be applied to variables using a colon:
<dl>
<dt>
<dd> 
${date : fancy()} $
{
articles:
    bibentry()
}
</dl>
 

 If articles is an array, this will iterate over its values, applying the partial bibentry() to each one. So the second example above is equivalent to
<dl>
<dt>
<dd> 
$
{
    for (articles)
}
${it : bibentry()} $
{
    endfor
}
</dl>
 

 Note that the anaphoric keyword it must be used when iterating over partials. In the above examples, the bibentry partial should contain it.title (and so on) instead of articles.title. 

 Final newlines are omitted from included partials. 

 Partials may include other partials. 

 A separator between values of an array may be specified in square brackets, immediately after the variable name or partial:
<dl>
<dt>
<dd> 
${months[, ]} $
    $
{
articles:
    bibentry()[;] $
</dl>
 

 The separator in this case is literal and (unlike with sep in an explicit for loop) cannot contain interpolated variables or other template directives.

<h3>Nesting</h3>

 

 To ensure that content is &quot;nested,&quot; that is, subsequent lines indented, use the ha directive:
<dl>
<dt>
<dd> <pre>
$item.number$  $ha$$item.description$ ($item.price$)
</pre></dl>
 

 In this example, if item.description has multiple lines, they will all be indented to line up with the first line:
<dl>
<dt>
<dd> <pre>
00123  A fine bottle of 18-year old
       Oban whiskey. ($148)
</pre></dl>
 

 To nest multiple lines to the same level, align them with the ha directive in the template. For example:
<dl>
<dt>
<dd> <pre>
$item.number$  $ha$$item.description$ ($item.price$)
               (Available til $item.sellby$.)
</pre></dl>
 

 will produce
<dl>
<dt>
<dd> <pre>
00123  A fine bottle of 18-year old
       Oban whiskey. ($148)
       (Available til March 30, 2020.)
</pre></dl>
 

 If a variable occurs by itself on a line, preceded by whitespace and not followed by further text or directives on the same line, and the variable's value contains multiple lines, it will be nested automatically.

<h3>Breakable spaces</h3>

 

 Normally, spaces in the template itself (as opposed to values of the interpolated variables) are not breakable, but they can be made breakable in part of the template by using the ~ keyword (ended with another ~).
<dl>
<dt>
<dd> 
$ ~$This long line may break if the document is rendered
    with a short line length.$ ~$
</dl>

<h3>Pipes</h3>

 

 A pipe transforms the value of a variable or partial. Pipes are specified using a slash (/) between the variable name (or partial) and the pipe name. Example:
<dl>
<dt>
<dd> <pre>
$for(name)$
$name/uppercase$
$endfor$
$for(metadata/pairs)$
- $it.key$: $it.value$
$endfor$
$employee:name()/uppercase$
</pre></dl>
 

 Pipes may be chained:
<dl>
<dt>
<dd> <pre>
$for(employees/pairs)$
$it.key/alpha/uppercase$. $it.name$
$endfor$
</pre></dl>
 

 Some pipes take parameters:
<dl>
<dt>
<dd> 
| -- -- -- -- -- -- -- -- -- -- -- | -- -- -- -- -- -- |
    $for(employee) $
        $it.name.first
        / uppercase / left 20 "| " $$it.name.salary / right 10 " | "
                                                               " |" $ $endfor$
    | -- -- -- -- -- -- -- -- -- -- -- | -- -- -- -- -- -- |
</dl>
 

 Currently the following pipes are predefined:
<dl>
<dt>&bull;
<dd> pairs: Converts a map or array to an array of maps, each with key and value fields. If the original value was an array, the key will be the array index, starting with 1.
<dt>&bull;
<dd> uppercase: Converts text to uppercase.
<dt>&bull;
<dd> lowercase: Converts text to lowercase.
<dt>&bull;
<dd> length: Returns the length of the value: number of characters for a textual value, number of elements for a map or array.
<dt>&bull;
<dd> reverse: Reverses a textual value or array, and has no effect on other values.
<dt>&bull;
<dd> chomp: Removes trailing newlines (and breakable space).
<dt>&bull;
<dd> nowrap: Disables line wrapping on breakable spaces.
<dt>&bull;
<dd> alpha: Converts textual values that can be read as an integer into lowercase alphabetic characters a..z (mod 26). This can be used to get lettered enumeration from array indices. To get uppercase letters, chain with uppercase.
<dt>&bull;
<dd> roman: Converts textual values that can be read as an integer into lowercase roman numerials. This can be used to get lettered enumeration from array indices. To get uppercase roman, chain with uppercase.
<dt>&bull;
<dd> left n &quot;leftborder&quot; &quot;rightborder&quot;: Renders a textual value in a block of width n, aligned to the left, with an optional left and right border. Has no effect on other values. This can be used to align material in tables. Widths are positive integers indicating the number of characters. Borders are strings inside double quotes; literal &quot; and \ characters must be backslash-escaped.
<dt>&bull;
<dd> right n &quot;leftborder&quot; &quot;rightborder&quot;: Renders a textual value in a block of width n, aligned to the right, and has no effect on other values.
<dt>&bull;
<dd> center n &quot;leftborder&quot; &quot;rightborder&quot;: Renders a textual value in a block of width n, aligned to the center, and has no effect on other values.</dl>

<h3>Variables</h3>

<h3>Metadata variables</h3>

<dl>
<dt>title, author, date
<dd> allow identification of basic aspects of the document. Included in PDF metadata through LaTeX and ConTeXt. These can be set through a pandoc title block, which allows for multiple authors, or through a YAML metadata block:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
---
author:
- Aristotle
- Peter Abelard
...
</pre></dl>
 

 Note that if you just want to set PDF or HTML metadata, without including a title block in the document itself, you can set the title-meta, author-meta, and date-meta variables. (By default these are set automatically, based on title, author, and date.)</dl>

<dt>subtitle
<dd> document subtitle, included in HTML, EPUB, LaTeX, ConTeXt, and docx documents
<dt>abstract
<dd> document summary, included in LaTeX, ConTeXt, AsciiDoc, and docx documents
<dt>keywords
<dd> list of keywords to be included in HTML, PDF, ODT, pptx, docx and AsciiDoc metadata; repeat as for author, above
<dt>subject
<dd> document subject, included in ODT, PDF, docx and pptx metadata
<dt>description
<dd> document description, included in ODT, docx and pptx metadata. Some applications show this as Comments metadata.
<dt>category
<dd> document category, included in docx and pptx metadata</dl>
 

 Additionally, any root-level string metadata, not included in ODT, docx or pptx metadata is added as a custom property. The following YAML metadata block for instance:
<dl>
<dt>
<dd> <pre>
---
title:  'This is the title'
subtitle: &quot;This is the subtitle&quot;
author:
- Author One
- Author Two
description: |
    This is a long
    description.
    It consists of two paragraphs
...
</pre></dl>
 

 will include title, author and description as standard document properties and subtitle as a custom property when converting to docx, ODT or pptx.

<h3>Language variables</h3>

<dl>
<dt>lang
<dd> identifies the main language of the document using IETF language tags (following the BCP 47 standard), such as en or en-GB. The Language subtag lookup tool can look up or verify these tags. This affects most formats, and controls hyphenation in PDF output when using LaTeX (through babel and polyglossia) or ConTeXt.
<dl>
<dt>
<dd> 

 Use native pandoc Divs and Spans with the lang attribute to switch the language:
<dl>
<dt>
<dd> 
-- -lang : en - GB... Text in the main document language(British English).:: : {lang = fr - CA} &gt; Cette citation est &amp;eacute;
crite en fran &amp;ccedil;
ais canadien.:: : More text in English.['Zitat auf Deutsch.'] { lang = de }
</dl>
</dl>

<dt>dir
<dd> the base script direction, either rtl (right-to-left) or ltr (left-to-right).
<dl>
<dt>
<dd> 

 For bidirectional documents, native pandoc spans and divs with the dir attribute (value rtl or ltr) can be used to override the base direction in some output formats. This may not always be necessary if the final renderer (e.g. the browser, when generating HTML) supports the Unicode Bidirectional Algorithm. 

 When using LaTeX for bidirectional documents, only the xelatex engine is fully supported (use --pdf-engine=xelatex).</dl>
</dl>

<h3>Variables for HTML math</h3>

<dl>
<dt>classoption
<dd> when using KaTeX, you can render display math equations flush left using YAML metadata or with -M classoption=fleqn.</dl>

<h3>Variables for HTML slides</h3>

 

 These affect HTML output when producing slide shows with pandoc. 

 All reveal.js configuration options are available as variables. To turn off boolean flags that default to true in reveal.js, use 0.
<dl>
<dt>revealjs-url
<dd> base URL for reveal.js documents (defaults to reveal.js)
<dt>s5-url
<dd> base URL for S5 documents (defaults to s5/default)
<dt>slidy-url
<dd> base URL for Slidy documents (defaults to <a rel="nofollow" HREF="https://www.w3.org/Talks/Tools/Slidy2)">https://www.w3.org/Talks/Tools/Slidy2)</a>
<dt>slideous-url
<dd> base URL for Slideous documents (defaults to slideous)
<dt>title-slide-attributes
<dd> additional attributes for the title slide of reveal.js slide shows. See background in reveal.js and beamer for an example.</dl>

<h3>Variables for Beamer slides</h3>

 

 These variables change the appearance of PDF slides using beamer.
<dl>
<dt>aspectratio
<dd> slide aspect ratio (43 for 4:3 [default], 169 for 16:9, 1610 for 16:10, 149 for 14:9, 141 for 1.41:1, 54 for 5:4, 32 for 3:2)
<dt>beamerarticle
<dd> produce an article from Beamer slides
<dt>beameroption
<dd> add extra beamer option with \setbeameroption{}
<dt>institute
<dd> author affiliations: can be a list when there are multiple authors
<dt>logo
<dd> logo image for slides
<dt>navigation
<dd> controls navigation symbols (default is empty for no navigation symbols; other valid values are frame, vertical, and horizontal)
<dt>section-titles
<dd> enables &quot;title pages&quot; for new sections (default is true)
<dt>theme, colortheme, fonttheme, innertheme, outertheme
<dd> beamer themes
<dt>themeoptions
<dd> options for LaTeX beamer themes (a list).
<dt>titlegraphic
<dd> image for title slide</dl>

<h3>Variables for PowerPoint</h3>

 

 These variables control the visual aspects of a slide show that are not easily controlled via templates.
<dl>
<dt>monofont
<dd> font to use for code.</dl>

<h3>Variables for LaTeX</h3>

 

 Pandoc uses these variables when creating a PDF with a LaTeX engine.

<h3>Layout</h3>

<dl>
<dt>block-headings
<dd> make \paragraph and \subparagraph (fourth- and fifth-level headings, or fifth- and sixth-level with book classes) free-standing rather than run-in; requires further formatting to distinguish from \subsubsection (third- or fourth-level headings). Instead of using this option, KOMA-Script can adjust headings more extensively:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
-- -documentclass : scrartcl
                        header -
        includes : |
  \RedeclareSectionCommand[beforeskip = -10pt plus - 2pt minus - 1pt,
                            afterskip = 1sp plus - 1sp minus 1sp,
                            font =\normalfont\itshape]
{
    paragraph
}
\RedeclareSectionCommand[beforeskip = -10pt plus - 2pt minus - 1pt,
                         afterskip = 1sp plus - 1sp minus 1sp,
                         font =\normalfont\scshape,
                         indent = 0pt]{subparagraph}...
</dl>
</dl>

<dt>classoption
<dd> option for document class, e.g. oneside; repeat for multiple options:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
---
classoption:
- twocolumn
- landscape
...
</pre></dl>
</dl>

<dt>documentclass
<dd> document class: usually one of the standard classes, article, book, and report; the KOMA-Script equivalents, scrartcl, scrbook, and scrreprt, which default to smaller margins; or memoir
<dt>geometry
<dd> option for geometry package, e.g. margin=1in; repeat for multiple options:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
---
geometry:
- top=30mm
- left=20mm
- heightrounded
...
</pre></dl>
</dl>

<dt>hyperrefoptions
<dd> option for hyperref package, e.g. linktoc=all; repeat for multiple options:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
---
hyperrefoptions:
- linktoc=all
- pdfwindowui
- pdfpagemode=FullScreen
...
</pre></dl>
</dl>

<dt>indent
<dd> uses document class settings for indentation (the default LaTeX template otherwise removes indentation and adds space between paragraphs)
<dt>linestretch
<dd> adjusts line spacing using the setspace package, e.g. 1.25, 1.5
<dt>margin-left, margin-right, margin-top, margin-bottom
<dd> sets margins if geometry is not used (otherwise geometry overrides these)
<dt>pagestyle
<dd> control \pagestyle{}: the default article class supports plain (default), empty (no running heads or page numbers), and headings (section titles in running heads)
<dt>papersize
<dd> paper size, e.g. letter, a4
<dt>secnumdepth
<dd> numbering depth for sections (with --number-sections option or numbersections variable)</dl>

<h3>Fonts</h3>

<dl>
<dt>fontenc
<dd> allows font encoding to be specified through fontenc package (with pdflatex); default is T1 (see LaTeX font encodings guide)
<dt>fontfamily
<dd> font package for use with pdflatex: TeX Live includes many options, documented in the LaTeX Font Catalogue. The default is Latin Modern.
<dt>fontfamilyoptions
<dd> options for package used as fontfamily; repeat for multiple options. For example, to use the Libertine font with proportional lowercase (old-style) figures through the libertinus package:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
---
fontfamily: libertinus
fontfamilyoptions:
- osf
- p
...
</pre></dl>
</dl>

<dt>fontsize
<dd> font size for body text. The standard classes allow 10pt, 11pt, and 12pt. To use another size, set documentclass to one of the KOMA-Script classes, such as scrartcl or scrbook.
<dt>mainfont, sansfont, monofont, mathfont, CJKmainfont
<dd> font families for use with xelatex or lualatex: take the name of any system font, using the fontspec package. CJKmainfont uses the xecjk package.
<dt>mainfontoptions, sansfontoptions, monofontoptions, mathfontoptions, CJKoptions
<dd> options to use with mainfont, sansfont, monofont, mathfont, CJKmainfont in xelatex and lualatex. Allow for any choices available through fontspec; repeat for multiple options. For example, to use the TeX Gyre version of Palatino with lowercase figures:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
---
mainfont: TeX Gyre Pagella
mainfontoptions:
- Numbers=Lowercase
- Numbers=Proportional
...
</pre></dl>
</dl>

<dt>microtypeoptions
<dd> options to pass to the microtype package</dl>

<h3>Links</h3>

<dl>
<dt>colorlinks
<dd> add color to link text; automatically enabled if any of linkcolor, filecolor, citecolor, urlcolor, or toccolor are set
<dt>linkcolor, filecolor, citecolor, urlcolor, toccolor
<dd> color for internal links, external links, citation links, linked URLs, and links in table of contents, respectively: uses options allowed by xcolor, including the dvipsnames, svgnames, and x11names lists
<dt>links-as-notes
<dd> causes links to be printed as footnotes</dl>

<h3>Front matter</h3>

<dl>
<dt>lof, lot
<dd> include list of figures, list of tables
<dt>thanks
<dd> contents of acknowledgments footnote after document title
<dt>toc
<dd> include table of contents (can also be set using --toc/--table-of-contents)
<dt>toc-depth
<dd> level of section to include in table of contents</dl>

<h3>BibLaTeX Bibliographies</h3>

 

 These variables function when using BibLaTeX for citation rendering.
<dl>
<dt>biblatexoptions
<dd> list of options for biblatex
<dt>biblio-style
<dd> bibliography style, when used with --natbib and --biblatex.
<dt>biblio-title
<dd> bibliography title, when used with --natbib and --biblatex.
<dt>bibliography
<dd> bibliography to use for resolving references
<dt>natbiboptions
<dd> list of options for natbib</dl>

<h3>Variables for ConTeXt</h3>

 

 Pandoc uses these variables when creating a PDF with ConTeXt.
<dl>
<dt>fontsize
<dd> font size for body text (e.g. 10pt, 12pt)
<dt>headertext, footertext
<dd> text to be placed in running header or footer (see ConTeXt Headers and Footers); repeat up to four times for different placement
<dt>indenting
<dd> controls indentation of paragraphs, e.g. yes,small,next (see ConTeXt Indentation); repeat for multiple options
<dt>interlinespace
<dd> adjusts line spacing, e.g. 4ex (using setupinterlinespace); repeat for multiple options
<dt>layout
<dd> options for page margins and text arrangement (see ConTeXt Layout); repeat for multiple options
<dt>linkcolor, contrastcolor
<dd> color for links outside and inside a page, e.g. red, blue (see ConTeXt Color)
<dt>linkstyle
<dd> typeface style for links, e.g. normal, bold, slanted, boldslanted, type, cap, small
<dt>lof, lot
<dd> include list of figures, list of tables
<dt>mainfont, sansfont, monofont, mathfont
<dd> font families: take the name of any system font (see ConTeXt Font Switching)
<dt>margin-left, margin-right, margin-top, margin-bottom
<dd> sets margins, if layout is not used (otherwise layout overrides these)
<dt>pagenumbering
<dd> page number style and location (using setuppagenumbering); repeat for multiple options
<dt>papersize
<dd> paper size, e.g. letter, A4, landscape (see ConTeXt Paper Setup); repeat for multiple options
<dt>pdfa
<dd> adds to the preamble the setup necessary to generate PDF/A of the type specified, e.g. 1a:2005, 2a. If no type is specified (i.e. the value is set to True, by e.g. --metadata=pdfa or pdfa: true in a YAML metadata block), 1b:2005 will be used as default, for reasons of backwards compatibility. Using --variable=pdfa without specified value is not supported. To successfully generate PDF/A the required ICC color profiles have to be available and the content and all included files (such as images) have to be standard conforming. The ICC profiles and output intent may be specified using the variables pdfaiccprofile and pdfaintent. See also ConTeXt PDFA for more details.
<dt>pdfaiccprofile
<dd> when used in conjunction with pdfa, specifies the ICC profile to use in the PDF, e.g. default.cmyk. If left unspecified, sRGB.icc is used as default. May be repeated to include multiple profiles. Note that the profiles have to be available on the system. They can be obtained from ConTeXt ICC Profiles.
<dt>pdfaintent
<dd> when used in conjunction with pdfa, specifies the output intent for the colors, e.g. ISO coated v2 300\letterpercent\space (ECI) If left unspecified, sRGB IEC61966-2.1 is used as default.
<dt>toc
<dd> include table of contents (can also be set using --toc/--table-of-contents)
<dt>whitespace
<dd> spacing between paragraphs, e.g. none, small (using setupwhitespace)
<dt>includesource
<dd> include all source documents as file attachments in the PDF file</dl>

<h3>Variables for wkhtmltopdf</h3>

 

 Pandoc uses these variables when creating a PDF with wkhtmltopdf. The --css option also affects the output.
<dl>
<dt>footer-html, header-html
<dd> add information to the header and footer
<dt>margin-left, margin-right, margin-top, margin-bottom
<dd> set the page margins
<dt>papersize
<dd> sets the PDF paper size</dl>

<h3>Variables for man pages</h3>

<dl>
<dt>adjusting
<dd> adjusts text to left (l), right (r), center (c), or both (b) margins
<dt>footer
<dd> footer in man pages
<dt>header
<dd> header in man pages
<dt>hyphenate
<dd> if true (the default), hyphenation will be used
<dt>section
<dd> section number in man pages</dl>

<h3>Variables for ms</h3>

<dl>
<dt>fontfamily
<dd> font family (e.g. T or P)
<dt>indent
<dd> paragraph indent (e.g. 2m)
<dt>lineheight
<dd> line height (e.g. 12p)
<dt>pointsize
<dd> point size (e.g. 10p)</dl>

<h3>Variables set automatically</h3>

 

 Pandoc sets these variables automatically in response to options or document contents; users can also modify them. These vary depending on the output format, and include the following:
<dl>
<dt>body
<dd> body of document
<dt>date-meta
<dd> the date variable converted to ISO 8601 YYYY-MM-DD, included in all HTML based formats (dzslides, epub, html, html4, html5, revealjs, s5, slideous, slidy). The recognized formats for date are: mm/dd/yyyy, mm/dd/yy, yyyy-mm-dd (ISO 8601), dd MM yyyy (e.g. either 02 Apr 2018 or 02 April 2018), MM dd, yyyy (e.g. Apr. 02, 2018 or April 02, 2018),yyyy[mm[dd]]](e.g.20180402, 201804 or 2018).
<dt>header-includes
<dd> contents specified by -H/--include-in-header (may have multiple values)
<dt>include-before
<dd> contents specified by -B/--include-before-body (may have multiple values)
<dt>include-after
<dd> contents specified by -A/--include-after-body (may have multiple values)
<dt>meta-json
<dd> JSON representation of all of the document's metadata. Field values are transformed to the selected output format.
<dt>numbersections
<dd> non-null value if -N/--number-sections was specified
<dt>sourcefile, outputfile
<dd> source and destination filenames, as given on the command line. sourcefile can also be a list if input comes from multiple files, or empty if input is from stdin. You can use the following snippet in your template to distinguish them:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
$if(sourcefile) $
    $for(sourcefile)
$
    $sourcefile$
        $endfor$
        $else$(stdin)
            $endif$
</dl>
 

 Similarly, outputfile can be - if output goes to the terminal. 

 If you need absolute paths, use e.g. $curdir$/$sourcefile$.</dl>

<dt>curdir
<dd> working directory from which pandoc is run.
<dt>toc
<dd> non-null value if --toc/--table-of-contents was specified
<dt>toc-title
<dd> title of table of contents (works only with EPUB, HTML, opendocument, odt, docx, pptx, beamer, LaTeX)</dl>

<h2>EXTENSIONS</h2>

 

 The behavior of some of the readers and writers can be adjusted by enabling or disabling various extensions. 

 An extension can be enabled by adding +EXTENSION to the format name and disabled by adding -EXTENSION. For example, --from markdown_strict+footnotes is strict Markdown with footnotes enabled, while --from markdown-footnotes-pipe_tables is pandoc's Markdown without footnotes or pipe tables. 

 The markdown reader and writer make by far the most use of extensions. Extensions only used by them are therefore covered in the section Pandoc's Markdown below (See Markdown variants for commonmark and gfm.) In the following, extensions that also work for other formats are covered. 

 Note that markdown extensions added to the ipynb format affect Markdown cells in Jupyter notebooks (as do command-line options like --atx-headers).

<h3>Typography</h3>

<h3>Extension: smart</h3>

 

 Interpret straight quotes as curly quotes, --- as em-dashes, -- as en-dashes, and ... as ellipses. Nonbreaking spaces are inserted after certain abbreviations, such as &quot;Mr.&quot; 

 This extension can be enabled/disabled for the following formats:
<dl>
<dt>input formats
<dd> markdown, commonmark, latex, mediawiki, org, rst, twiki
<dt>output formats
<dd> markdown, latex, context, rst
<dt>enabled by default in
<dd> markdown, latex, context (both input and output)</dl>
 

 Note: If you are writing Markdown, then the smart extension has the reverse effect: what would have been curly quotes comes out straight. 

 In LaTeX, smart means to use the standard TeX ligatures for quotation marks (`` and '' for double quotes, ` and ' for single quotes) and dashes (-- for en-dash and --- for em-dash). If smart is disabled, then in reading LaTeX pandoc will parse these characters literally. In writing LaTeX, enabling smart tells pandoc to use the ligatures when possible; if smart is disabled pandoc will use unicode quotation mark and dash characters.

<h3>Headings and sections</h3>

<h3>Extension: auto_identifiers</h3>

 

 A heading without an explicitly specified identifier will be automatically assigned a unique identifier based on the heading text. 

 This extension can be enabled/disabled for the following formats:
<dl>
<dt>input formats
<dd> markdown, latex, rst, mediawiki, textile
<dt>output formats
<dd> markdown, muse
<dt>enabled by default in
<dd> markdown, muse</dl>
 

 The default algorithm used to derive the identifier from the heading text is:
<dl>
<dt>&bull;
<dd> Remove all formatting, links, etc.
<dt>&bull;
<dd> Remove all footnotes.
<dt>&bull;
<dd> Remove all non-alphanumeric characters, except underscores, hyphens, and periods.
<dt>&bull;
<dd> Replace all spaces and newlines with hyphens.
<dt>&bull;
<dd> Convert all alphabetic characters to lowercase.
<dt>&bull;
<dd> Remove everything up to the first letter (identifiers may not begin with a number or punctuation mark).
<dt>&bull;
<dd> If nothing is left after this, use the identifier section.</dl>
 

 Thus, for example, 

 <table> <tr VALIGN=top><td> Heading </td><td> Identifier 
</td></tr> <tr VALIGN=top><td COLSPAN=2><hr></td></tr> <tr VALIGN=top><td> Heading identifiers in HTML </td><td> heading-identifiers-in-html 
</td></tr> <tr VALIGN=top><td> Ma&icirc;tre d'h&ocirc;tel </td><td> ma&icirc;tre-dh&ocirc;tel 
</td></tr> <tr VALIGN=top><td> *Dogs*?--in *my* house? </td><td> dogs--in-my-house 
</td></tr> <tr VALIGN=top><td> [HTML], [S5], or [RTF]? </td><td> html-s5-or-rtf 
</td></tr> <tr VALIGN=top><td> 3. Applications </td><td> applications 
</td></tr> <tr VALIGN=top><td> 33 </td><td> section 
</td></tr> </table> 

 These rules should, in most cases, allow one to determine the identifier from the heading text. The exception is when several headings have the same text; in this case, the first will get an identifier as described above; the second will get the same identifier with -1 appended; the third with -2; and so on. 

 (However, a different algorithm is used if gfm_auto_identifiers is enabled; see below.) 

 These identifiers are used to provide link targets in the table of contents generated by the --toc|--table-of-contents option. They also make it easy to provide links from one section of a document to another. A link to this section, for example, might look like this:
<dl>
<dt>
<dd> <pre>
See the section on
[heading identifiers](#heading-identifiers-in-html-latex-and-context).
</pre></dl>
 

 Note, however, that this method of providing links to sections works only in HTML, LaTeX, and ConTeXt formats. 

 If the --section-divs option is specified, then each section will be wrapped in a section (or a div, if html4 was specified), and the identifier will be attached to the enclosing &lt;section&gt; (or &lt;div&gt;) tag rather than the heading itself. This allows entire sections to be manipulated using JavaScript or treated differently in CSS.

<h3>Extension: ascii_identifiers</h3>

 

 Causes the identifiers produced by auto_identifiers to be pure ASCII. Accents are stripped off of accented Latin letters, and non-Latin letters are omitted.

<h3>Extension: gfm_auto_identifiers</h3>

 

 Changes the algorithm used by auto_identifiers to conform to GitHub's method. Spaces are converted to dashes (-), uppercase characters to lowercase characters, and punctuation characters other than - and _ are removed. Emojis are replaced by their names.

<h3>Math Input</h3>

 

 The extensions tex_math_dollars, tex_math_single_backslash, and tex_math_double_backslash are described in the section about Pandoc's Markdown. 

 However, they can also be used with HTML input. This is handy for reading web pages formatted using MathJax, for example.

<h3>Raw HTML/TeX</h3>

 

 The following extensions (especially how they affect Markdown input/output) are also described in more detail in their respective sections of Pandoc's Markdown.

<h3>Extension: raw_html</h3>

 

 When converting from HTML, parse elements to raw HTML which are not representable in pandoc's AST. By default, this is disabled for HTML input.

<h3>Extension: raw_tex</h3>

 

 Allows raw LaTeX, TeX, and ConTeXt to be included in a document. 

 This extension can be enabled/disabled for the following formats (in addition to markdown):
<dl>
<dt>input formats
<dd> latex, org, textile, html (environments, \ref, and \eqref only), ipynb
<dt>output formats
<dd> textile, commonmark</dl>
 

 Note: as applied to ipynb, raw_html and raw_tex affect not only raw TeX in markdown cells, but data with mime type text/html in output cells. Since the ipynb reader attempts to preserve the richest possible outputs when several options are given, you will get best results if you disable raw_html and raw_tex when converting to formats like docx which don't allow raw html or tex.

<h3>Extension: native_divs</h3>

 

 This extension is enabled by default for HTML input. This means that divs are parsed to pandoc native elements. (Alternatively, you can parse them to raw HTML using -f html-native_divs+raw_html.) 

 When converting HTML to Markdown, for example, you may want to drop all divs and spans:
<dl>
<dt>
<dd> <pre>
pandoc -f html-native_divs-native_spans -t markdown
</pre></dl>

<h3>Extension: native_spans</h3>

 

 Analogous to native_divs above.

<h3>Literate Haskell support</h3>

<h3>Extension: literate_haskell</h3>

 

 Treat the document as literate Haskell source. 

 This extension can be enabled/disabled for the following formats:
<dl>
<dt>input formats
<dd> markdown, rst, latex
<dt>output formats
<dd> markdown, rst, latex, html</dl>
 

 If you append +lhs (or +literate_haskell) to one of the formats above, pandoc will treat the document as literate Haskell source. This means that
<dl>
<dt>&bull;
<dd> In Markdown input, &quot;bird track&quot; sections will be parsed as Haskell code rather than block quotations. Text between \begin{code} and \end{code} will also be treated as Haskell code. For ATX-style headings the character '=' will be used instead of '#'.
<dt>&bull;
<dd> In Markdown output, code blocks with classes haskell and literate will be rendered using bird tracks, and block quotations will be indented one space, so they will not be treated as Haskell code. In addition, headings will be rendered setext-style (with underlines) rather than ATX-style (with '#' characters). (This is because ghc treats '#' characters in column 1 as introducing line numbers.)
<dt>&bull;
<dd> In restructured text input, &quot;bird track&quot; sections will be parsed as Haskell code.
<dt>&bull;
<dd> In restructured text output, code blocks with class haskell will be rendered using bird tracks.
<dt>&bull;
<dd> In LaTeX input, text in code environments will be parsed as Haskell code.
<dt>&bull;
<dd> In LaTeX output, code blocks with class haskell will be rendered inside code environments.
<dt>&bull;
<dd> In HTML output, code blocks with class haskell will be rendered with class literatehaskell and bird tracks.</dl>
 

 Examples:
<dl>
<dt>
<dd> <pre>
pandoc -f markdown+lhs -t html
</pre></dl>
 

 reads literate Haskell source formatted with Markdown conventions and writes ordinary HTML (without bird tracks).
<dl>
<dt>
<dd> <pre>
pandoc -f markdown+lhs -t html+lhs
</pre></dl>
 

 writes HTML with the Haskell code in bird tracks, so it can be copied and pasted as literate Haskell source. 

 Note that GHC expects the bird tracks in the first column, so indented literate code blocks (e.g. inside an itemized environment) will not be picked up by the Haskell compiler.

<h3>Other extensions</h3>

<h3>Extension: empty_paragraphs</h3>

 

 Allows empty paragraphs. By default empty paragraphs are omitted. 

 This extension can be enabled/disabled for the following formats:
<dl>
<dt>input formats
<dd> docx, html
<dt>output formats
<dd> docx, odt, opendocument, html</dl>

<h3>Extension: native_numbering</h3>

 

 Enables native numbering of figures and tables. Enumeration starts at 1. 

 This extension can be enabled/disabled for the following formats:
<dl>
<dt>output formats
<dd> odt, opendocument</dl>

<h3>Extension: styles</h3>

 

 When converting from docx, read all docx styles as divs (for paragraph styles) and spans (for character styles) regardless of whether pandoc understands the meaning of these styles. This can be used with docx custom styles. Disabled by default.
<dl>
<dt>input formats
<dd> docx</dl>

<h3>Extension: amuse</h3>

 

 In the muse input format, this enables Text::Amuse extensions to Emacs Muse markup.

<h3>Extension: citations</h3>

 

 Some aspects of Pandoc's Markdown citation syntax are also accepted in org input.

<h3>Extension: ntb</h3>

 

 In the context output format this enables the use of Natural Tables (TABLE) instead of the default Extreme Tables (xtables). Natural tables allow more fine-grained global customization but come at a performance penalty compared to extreme tables.

<h2>PANDOC'S MARKDOWN</h2>

 

 Pandoc understands an extended and slightly revised version of John Gruber's Markdown syntax. This document explains the syntax, noting differences from standard Markdown. Except where noted, these differences can be suppressed by using the markdown_strict format instead of markdown. Extensions can be enabled or disabled to specify the behavior more granularly. They are described in the following. See also Extensions above, for extensions that work also on other formats.

<h3>Philosophy</h3>

 

 Markdown is designed to be easy to write, and, even more importantly, easy to read:
<dl>
<dt>
<dd> 

 A Markdown-formatted document should be publishable as-is, as plain text, without looking like it's been marked up with tags or formatting instructions. -- John Gruber</dl>
 

 This principle has guided pandoc's decisions in finding syntax for tables, footnotes, and other extensions. 

 There is, however, one respect in which pandoc's aims are different from the original aims of Markdown. Whereas Markdown was originally designed with HTML generation in mind, pandoc is designed for multiple output formats. Thus, while pandoc allows the embedding of raw HTML, it discourages it, and provides other, non-HTMLish ways of representing important document elements like definition lists, tables, mathematics, and footnotes.

<h3>Paragraphs</h3>

 

 A paragraph is one or more lines of text followed by one or more blank lines. Newlines are treated as spaces, so you can reflow your paragraphs as you like. If you need a hard line break, put two or more spaces at the end of a line.

<h3>Extension: escaped_line_breaks</h3>

 

 A backslash followed by a newline is also a hard line break. Note: in multiline and grid table cells, this is the only way to create a hard line break, since trailing spaces in the cells are ignored.

<h3>Headings</h3>

 

 There are two kinds of headings: Setext and ATX.

<h3>Setext-style headings</h3>

 

 A setext-style heading is a line of text &quot;underlined&quot; with a row of = signs (for a level-one heading) or - signs (for a level-two heading):
<dl>
<dt>
<dd> 
A level - one heading == == == == == == == == == =
                                                     A level - two heading-- -- -- -- -- -- -- -- -- -
</dl>
 

 The heading text can contain inline formatting, such as emphasis (see Inline formatting, below).

<h3>ATX-style headings</h3>

 

 An ATX-style heading consists of one to six # signs and a line of text, optionally followed by any number of # signs. The number of # signs at the beginning of the line is the heading level:
<dl>
<dt>
<dd> <pre>
## A level-two heading
### A level-three heading ###
</pre></dl>
 

 As with setext-style headings, the heading text can contain formatting:
<dl>
<dt>
<dd> <pre>
# A level-one heading with a [link](/url) and *emphasis*
</pre></dl>

<h3>Extension: blank_before_header</h3>

 

 Standard Markdown syntax does not require a blank line before a heading. Pandoc does require this (except, of course, at the beginning of the document). The reason for the requirement is that it is all too easy for a # to end up at the beginning of a line by accident (perhaps through line wrapping). Consider, for example:
<dl>
<dt>
<dd> <pre>
I like several of their flavors of ice cream:
#22, for example, and #5.
</pre></dl>

<h3>Extension: space_in_atx_header</h3>

 

 Many Markdown implementations do not require a space between the opening #s of an ATX heading and the heading text, so that #5 bolt and #hashtag count as headings. With this extension, pandoc does require the space.

<h3>Heading identifiers</h3>

 

 See also the auto_identifiers extension above.

<h3>Extension: header_attributes</h3>

 

 Headings can be assigned attributes using this syntax at the end of the line containing the heading text:
<dl>
<dt>
<dd> <pre>
{#identifier .class .class key=value key=value}
</pre></dl>
 

 Thus, for example, the following headings will all be assigned the identifier foo:
<dl>
<dt>
<dd> 
#My heading{#foo }
##My heading##{#foo} My other heading
{
#foo
}
-- -- -- -- -- -- -- -
</dl>
 

 (This syntax is compatible with PHP Markdown Extra.) 

 Note that although this syntax allows assignment of classes and key/value attributes, writers generally don't use all of this information. Identifiers, classes, and key/value attributes are used in HTML and HTML-based formats such as EPUB and slidy. Identifiers are used for labels and link anchors in the LaTeX, ConTeXt, Textile, Jira markup, and AsciiDoc writers. 

 Headings with the class unnumbered will not be numbered, even if --number-sections is specified. A single hyphen (-) in an attribute context is equivalent to .unnumbered, and preferable in non-English documents. So,
<dl>
<dt>
<dd> <pre>
# My heading {-}
</pre></dl>
 

 is just the same as
<dl>
<dt>
<dd> <pre>
# My heading {.unnumbered}
</pre></dl>
 

 If the unlisted class is present in addition to unnumbered, the heading will not be included in a table of contents. (Currently this feature is only implemented for certain formats: those based on LaTeX and HTML, PowerPoint, and RTF.)

<h3>Extension: implicit_header_references</h3>

 

 Pandoc behaves as if reference links have been defined for each heading. So, to link to a heading
<dl>
<dt>
<dd> <pre>
# Heading identifiers in HTML
</pre></dl>
 

 you can simply write
<dl>
<dt>
<dd> <pre>
[Heading identifiers in HTML]
</pre></dl>
 

 or
<dl>
<dt>
<dd> 
[Heading identifiers in HTML][]
</dl>
 

 or
<dl>
<dt>
<dd> 
[the section on heading identifiers][heading identifiers in
                                         HTML]
</dl>
 

 instead of giving the identifier explicitly:
<dl>
<dt>
<dd> <pre>
[Heading identifiers in HTML](#heading-identifiers-in-html)
</pre></dl>
 

 If there are multiple headings with identical text, the corresponding reference will link to the first one only, and you will need to use explicit links to link to the others, as described above. 

 Like regular reference links, these references are case-insensitive. 

 Explicit link reference definitions always take priority over implicit heading references. So, in the following example, the link will point to bar, not to #foo:
<dl>
<dt>
<dd> 
#Foo
[foo] : bar
            See[foo]
</dl>

<h3>Block quotations</h3>

 

 Markdown uses email conventions for quoting blocks of text. A block quotation is one or more paragraphs or other block elements (such as lists or headings), with each line preceded by a &gt; character and an optional space. (The &gt; need not start at the left margin, but it should not be indented more than three spaces.)
<dl>
<dt>
<dd> <pre>
&gt; This is a block quote. This
&gt; paragraph has two lines.
&gt;
&gt; 1. This is a list inside a block quote.
&gt; 2. Second item.
</pre></dl>
 

 A &quot;lazy&quot; form, which requires the &gt; character only on the first line of each block, is also allowed:
<dl>
<dt>
<dd> <pre>
&gt; This is a block quote. This
paragraph has two lines.
&gt; 1. This is a list inside a block quote.
2. Second item.
</pre></dl>
 

 Among the block elements that can be contained in a block quote are other block quotes. That is, block quotes can be nested:
<dl>
<dt>
<dd> <pre>
&gt; This is a block quote.
&gt;
&gt; &gt; A block quote within a block quote.
</pre></dl>
 

 If the &gt; character is followed by an optional space, that space will be considered part of the block quote marker and not part of the indentation of the contents. Thus, to put an indented code block in a block quote, you need five spaces after the &gt;:
<dl>
<dt>
<dd> <pre>
&gt;     code
</pre></dl>

<h3>Extension: blank_before_blockquote</h3>

 

 Standard Markdown syntax does not require a blank line before a block quote. Pandoc does require this (except, of course, at the beginning of the document). The reason for the requirement is that it is all too easy for a &gt; to end up at the beginning of a line by accident (perhaps through line wrapping). So, unless the markdown_strict format is used, the following does not produce a nested block quote in pandoc:
<dl>
<dt>
<dd> <pre>
&gt; This is a block quote.
&gt;&gt; Nested.
</pre></dl>

<h3>Verbatim (code) blocks</h3>

<h3>Indented code blocks</h3>

 

 A block of text indented four spaces (or one tab) is treated as verbatim text: that is, special characters do not trigger special formatting, and all spaces and line breaks are preserved. For example,
<dl>
<dt>
<dd> 
if (a &gt; 3) {
    moveShip(5 * gravity, DOWN);
}
</dl>
 

 The initial (four space or one tab) indentation is not considered part of the verbatim text, and is removed in the output. 

 Note: blank lines in the verbatim text need not begin with four spaces.

<h3>Fenced code blocks</h3>

<h3>Extension: fenced_code_blocks</h3>

 

 In addition to standard indented code blocks, pandoc supports fenced code blocks. These begin with a row of three or more tildes (~) and end with a row of tildes that must be at least as long as the starting row. Everything between these lines is treated as code. No indentation is necessary:
<dl>
<dt>
<dd> 
~~~~~~~if (a &gt; 3)
{
    moveShip(5 * gravity, DOWN);
}
~~~~~~~
</dl>
 

 Like regular code blocks, fenced code blocks must be separated from surrounding text by blank lines. 

 If the code itself contains a row of tildes or backticks, just use a longer row of tildes or backticks at the start and end:
<dl>
<dt>
<dd> <pre>
~~~~~~~~~~~~~~~~
~~~~~~~~~~
code including tildes
~~~~~~~~~~
~~~~~~~~~~~~~~~~
</pre></dl>

<h3>Extension: backtick_code_blocks</h3>

 

 Same as fenced_code_blocks, but uses backticks (`) instead of tildes (~).

<h3>Extension: fenced_code_attributes</h3>

 

 Optionally, you may attach attributes to fenced or backtick code block using this syntax:
<dl>
<dt>
<dd> 
~~~~{#mycode.haskell.numberLines startFrom = "100"} qsort[] = [] qsort(x
                                                                       : xs) = qsort(filter(&lt; x) xs)++[x]++ qsort(filter(&gt;= x) xs) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
</dl>
 

 Here mycode is an identifier, haskell and numberLines are classes, and startFrom is an attribute with value 100. Some output formats can use this information to do syntax highlighting. Currently, the only output formats that uses this information are HTML, LaTeX, Docx, Ms, and PowerPoint. If highlighting is supported for your output format and language, then the code block above will appear highlighted, with numbered lines. (To see which languages are supported, type pandoc --list-highlight-languages.) Otherwise, the code block above will appear as follows:
<dl>
<dt>
<dd> <pre>
&lt;pre id=&quot;mycode&quot; class=&quot;haskell numberLines&quot; startFrom=&quot;100&quot;&gt;
  &lt;code&gt;
  ...
  &lt;/code&gt;
&lt;/pre&gt;
</pre></dl>
 

 The numberLines (or number-lines) class will cause the lines of the code block to be numbered, starting with 1 or the value of the startFrom attribute. The lineAnchors (or line-anchors) class will cause the lines to be clickable anchors in HTML output. 

 A shortcut form can also be used for specifying the language of the code block:
<dl>
<dt>
<dd> 
```haskell
    qsort[] = []
```
</dl>
 

 This is equivalent to:
<dl>
<dt>
<dd> 
``` {.haskell} qsort[] = []
```
</dl>
 

 If the fenced_code_attributes extension is disabled, but input contains class attribute(s) for the code block, the first class attribute will be printed after the opening fence as a bare word. 

 To prevent all highlighting, use the --no-highlight flag. To set the highlighting style, use --highlight-style. For more information on highlighting, see Syntax highlighting, below.

<h3>Line blocks</h3>

<h3>Extension: line_blocks</h3>

 

 A line block is a sequence of lines beginning with a vertical bar (|) followed by a space. The division into lines will be preserved in the output, as will any leading spaces; otherwise, the lines will be formatted as Markdown. This is useful for verse and addresses:
<dl>
<dt>
<dd> <pre>
| The limerick packs laughs anatomical
| In space that is quite economical.
|    But the good ones I've seen
|    So seldom are clean
| And the clean ones so seldom are comical
| 200 Main St.
| Berkeley, CA 94718
</pre></dl>
 

 The lines can be hard-wrapped if needed, but the continuation line must begin with a space.
<dl>
<dt>
<dd> <pre>
| The Right Honorable Most Venerable and Righteous Samuel L.
  Constable, Jr.
| 200 Main St.
| Berkeley, CA 94718
</pre></dl>
 

 This syntax is borrowed from reStructuredText.

<h3>Lists</h3>

<h3>Bullet lists</h3>

 

 A bullet list is a list of bulleted list items. A bulleted list item begins with a bullet (*, +, or -). Here is a simple example:
<dl>
<dt>
<dd> <pre>
* one
* two
* three
</pre></dl>
 

 This will produce a &quot;compact&quot; list. If you want a &quot;loose&quot; list, in which each item is formatted as a paragraph, put spaces between the items:
<dl>
<dt>
<dd> <pre>
* one
* two
* three
</pre></dl>
 

 The bullets need not be flush with the left margin; they may be indented one, two, or three spaces. The bullet must be followed by whitespace. 

 List items look best if subsequent lines are flush with the first line (after the bullet):
<dl>
<dt>
<dd> <pre>
* here is my first
  list item.
* and my second.
</pre></dl>
 

 But Markdown also allows a &quot;lazy&quot; format:
<dl>
<dt>
<dd> <pre>
* here is my first
list item.
* and my second.
</pre></dl>

<h3>Block content in list items</h3>

 

 A list item may contain multiple paragraphs and other block-level content. However, subsequent paragraphs must be preceded by a blank line and indented to line up with the first non-space content after the list marker.
<dl>
<dt>
<dd> <pre>
  * First paragraph.
    Continued.
  * Second paragraph. With a code block, which must be indented
    eight spaces:
        { code }
</pre></dl>
 

 Exception: if the list marker is followed by an indented code block, which must begin 5 spaces after the list marker, then subsequent paragraphs must begin two columns after the last character of the list marker:
<dl>
<dt>
<dd> <pre>
*     code
  continuation paragraph
</pre></dl>
 

 List items may include other lists. In this case the preceding blank line is optional. The nested list must be indented to line up with the first non-space character after the list marker of the containing list item.
<dl>
<dt>
<dd> <pre>
* fruits
  + apples
    - macintosh
    - red delicious
  + pears
  + peaches
* vegetables
  + broccoli
  + chard
</pre></dl>
 

 As noted above, Markdown allows you to write list items &quot;lazily,&quot; instead of indenting continuation lines. However, if there are multiple paragraphs or other blocks in a list item, the first line of each must be indented.
<dl>
<dt>
<dd> <pre>
+ A lazy, lazy, list
item.
+ Another one; this looks
bad but is legal.
    Second paragraph of second
list item.
</pre></dl>

<h3>Ordered lists</h3>

 

 Ordered lists work just like bulleted lists, except that the items begin with enumerators rather than bullets. 

 In standard Markdown, enumerators are decimal numbers followed by a period and a space. The numbers themselves are ignored, so there is no difference between this list:
<dl>
<dt>
<dd> <pre>
1.  one
2.  two
3.  three
</pre></dl>
 

 and this one:
<dl>
<dt>
<dd> <pre>
5.  one
7.  two
1.  three
</pre></dl>

<h3>Extension: fancy_lists</h3>

 

 Unlike standard Markdown, pandoc allows ordered list items to be marked with uppercase and lowercase letters and roman numerals, in addition to Arabic numerals. List markers may be enclosed in parentheses or followed by a single right-parentheses or period. They must be separated from the text that follows by at least one space, and, if the list marker is a capital letter with a period, by at least two spaces. 

 The fancy_lists extension also allows '#' to be used as an ordered list marker in place of a numeral:
<dl>
<dt>
<dd> <pre>
#. one
#. two
</pre></dl>

<h3>Extension: startnum</h3>

 

 Pandoc also pays attention to the type of list marker used, and to the starting number, and both of these are preserved where possible in the output format. Thus, the following yields a list with numbers followed by a single parenthesis, starting with 9, and a sublist with lowercase roman numerals:
<dl>
<dt>
<dd> <pre>
 9)  Ninth
10)  Tenth
11)  Eleventh
       i. subone
      ii. subtwo
     iii. subthree
</pre></dl>
 

 Pandoc will start a new list each time a different type of list marker is used. So, the following will create three lists:
<dl>
<dt>
<dd> <pre>
(2) Two
(5) Three
1.  Four
*   Five
</pre></dl>
 

 If default list markers are desired, use #.:
<dl>
<dt>
<dd> <pre>
#.  one
#.  two
#.  three
</pre></dl>

<h3>Extension: task_lists</h3>

 

 Pandoc supports task lists, using the syntax of GitHub-Flavored Markdown.
<dl>
<dt>
<dd> 
- [] an unchecked task list item - [x] checked item
</dl>

<h3>Definition lists</h3>

<h3>Extension: definition_lists</h3>

 

 Pandoc supports definition lists, using the syntax of PHP Markdown Extra with some extensions.
<dl>
<dt>
<dd> <pre>
Term 1
:   Definition 1
Term 2 with *inline markup*
:   Definition 2
        { some code, part of Definition 2 }
    Third paragraph of definition 2.
</pre></dl>
 

 Each term must fit on one line, which may optionally be followed by a blank line, and must be followed by one or more definitions. A definition begins with a colon or tilde, which may be indented one or two spaces. 

 A term may have multiple definitions, and each definition may consist of one or more block elements (paragraph, code block, list, etc.), each indented four spaces or one tab stop. The body of the definition (including the first line, aside from the colon or tilde) should be indented four spaces. However, as with other Markdown lists, you can &quot;lazily&quot; omit indentation except at the beginning of a paragraph or other block element:
<dl>
<dt>
<dd> <pre>
Term 1
:   Definition
with lazy continuation.
    Second paragraph of the definition.
</pre></dl>
 

 If you leave space before the definition (as in the example above), the text of the definition will be treated as a paragraph. In some output formats, this will mean greater spacing between term/definition pairs. For a more compact definition list, omit the space before the definition:
<dl>
<dt>
<dd> <pre>
Term 1
  ~ Definition 1
Term 2
  ~ Definition 2a
  ~ Definition 2b
</pre></dl>
 

 Note that space between items in a definition list is required. (A variant that loosens this requirement, but disallows &quot;lazy&quot; hard wrapping, can be activated with compact_definition_lists: see Non-pandoc extensions, below.)

<h3>Numbered example lists</h3>

<h3>Extension: example_lists</h3>

 

 The special list marker @ can be used for sequentially numbered examples. The first list item with a @ marker will be numbered '1', the next '2', and so on, throughout the document. The numbered examples need not occur in a single list; each new list using @ will take up where the last stopped. So, for example:
<dl>
<dt>
<dd> <pre>
(@)  My first example will be numbered (1).
(@)  My second example will be numbered (2).
Explanation of examples.
(@)  My third example will be numbered (3).
</pre></dl>
 

 Numbered examples can be labeled and referred to elsewhere in the document:
<dl>
<dt>
<dd> <pre>
(@good)  This is a good example.
As (@good) illustrates, ...
</pre></dl>
 

 The label can be any string of alphanumeric characters, underscores, or hyphens. 

 Note: continuation paragraphs in example lists must always be indented four spaces, regardless of the length of the list marker. That is, example lists always behave as if the four_space_rule extension is set. This is because example labels tend to be long, and indenting content to the first non-space character after the label would be awkward.

<h3>Compact and loose lists</h3>

 

 Pandoc behaves differently from Markdown.pl on some &quot;edge cases&quot; involving lists. Consider this source:
<dl>
<dt>
<dd> <pre>
+   First
+   Second:
    -   Fee
    -   Fie
    -   Foe
+   Third
</pre></dl>
 

 Pandoc transforms this into a &quot;compact list&quot; (with no &lt;p&gt; tags around &quot;First&quot;, &quot;Second&quot;, or &quot;Third&quot;), while Markdown puts &lt;p&gt; tags around &quot;Second&quot; and &quot;Third&quot; (but not &quot;First&quot;), because of the blank space around &quot;Third&quot;. Pandoc follows a simple rule: if the text is followed by a blank line, it is treated as a paragraph. Since &quot;Second&quot; is followed by a list, and not a blank line, it isn't treated as a paragraph. The fact that the list is followed by a blank line is irrelevant. (Note: Pandoc works this way even when the markdown_strict format is specified. This behavior is consistent with the official Markdown syntax description, even though it is different from that of Markdown.pl.)

<h3>Ending a list</h3>

 

 What if you want to put an indented code block after a list?
<dl>
<dt>
<dd> <pre>
-   item one
-   item two
    { my code block }
</pre></dl>
 

 Trouble! Here pandoc (like other Markdown implementations) will treat { my code block } as the second paragraph of item two, and not as a code block. 

 To &quot;cut off&quot; the list after item two, you can insert some non-indented content, like an HTML comment, which won't produce visible output in any format:
<dl>
<dt>
<dd> 
- item one - item two&lt;!--end of list--&gt;
{
    my code block
}
</dl>
 

 You can use the same trick if you want two consecutive lists instead of one big list:
<dl>
<dt>
<dd> <pre>
1.  one
2.  two
3.  three
&lt;!-- --&gt;
1.  uno
2.  dos
3.  tres
</pre></dl>

<h3>Horizontal rules</h3>

 

 A line containing a row of three or more *, -, or _ characters (optionally separated by spaces) produces a horizontal rule:
<dl>
<dt>
<dd> 
****-- -- -- -- -- -- -- -
</dl>

<h3>Tables</h3>

 

 Four kinds of tables may be used. The first three kinds presuppose the use of a fixed-width font, such as Courier. The fourth kind can be used with proportionally spaced fonts, as it does not require lining up columns.

<h3>Extension: table_captions</h3>

 

 A caption may optionally be provided with all 4 kinds of tables (as illustrated in the examples below). A caption is a paragraph beginning with the string Table: (or just :), which will be stripped off. It may appear either before or after the table.

<h3>Extension: simple_tables</h3>

 

 Simple tables look like this:
<dl>
<dt>
<dd> 
Right Left Center Default-- -- -- - -- -- -- -- -- -- -- -- -- -- -- -12 12 12 12 123 123 123 123 1 1 1 1 Table : Demonstration of simple table syntax.
</dl>
 

 The header and table rows must each fit on one line. Column alignments are determined by the position of the header text relative to the dashed line below it:
<dl>
<dt>&bull;
<dd> If the dashed line is flush with the header text on the right side but extends beyond it on the left, the column is right-aligned.
<dt>&bull;
<dd> If the dashed line is flush with the header text on the left side but extends beyond it on the right, the column is left-aligned.
<dt>&bull;
<dd> If the dashed line extends beyond the header text on both sides, the column is centered.
<dt>&bull;
<dd> If the dashed line is flush with the header text on both sides, the default alignment is used (in most cases, this will be left).</dl>
 

 The table must end with a blank line, or a line of dashes followed by a blank line. 

 The column header row may be omitted, provided a dashed line is used to end the table. For example:
<dl>
<dt>
<dd> 
-- -- -- - -- -- -- -- -- -- -- -- -- -- -- -12 12 12 12 123 123 123 123 1 1 1 1 -- -- -- - -- -- -- -- -- -- -- -- -- -- -- -
</dl>
 

 When the header row is omitted, column alignments are determined on the basis of the first line of the table body. So, in the tables above, the columns would be right, left, center, and right aligned, respectively.

<h3>Extension: multiline_tables</h3>

 

 Multiline tables allow header and table rows to span multiple lines of text (but cells that span multiple columns or rows of the table are not supported). Here is an example:
<dl>
<dt>
<dd> 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -Centered Default Right Left
                                                                                               Header Aligned Aligned Aligned-- -- -- -- -- - -- -- -- - -- -- -- -- -- -- -- - -- -- -- -- -- -- -- -- -- -- -- -- -First row 12.0 Example of a row that
                                                                                                   spans multiple lines.Second row 5.0 Here's another one. Note the blank line between
                                                                                                       rows.-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -Table : Here's the caption. It, too, may span multiple lines.
</dl>
 

 These work like simple tables, but with the following differences:
<dl>
<dt>&bull;
<dd> They must begin with a row of dashes, before the header text (unless the header row is omitted).
<dt>&bull;
<dd> They must end with a row of dashes, then a blank line.
<dt>&bull;
<dd> The rows must be separated by blank lines.</dl>
 

 In multiline tables, the table parser pays attention to the widths of the columns, and the writers try to reproduce these relative widths in the output. So, if you find that one of the columns is too narrow in the output, try widening it in the Markdown source. 

 The header may be omitted in multiline tables as well as simple tables:
<dl>
<dt>
<dd> 
-- -- -- -- -- - -- -- -- - -- -- -- -- -- -- -- - -- -- -- -- -- -- -- -- -- -- -- -- -First row 12.0 Example of a row that
                                                                                            spans multiple lines.Second row 5.0 Here's another one. Note the blank line between
                                                                                                rows.-- -- -- -- -- - -- -- -- - -- -- -- -- -- -- -- - -- -- -- -- -- -- -- -- -- -- -- -- -
    : Here's a multiline table without a header.
</dl>
 

 It is possible for a multiline table to have just one row, but the row should be followed by a blank line (and then the row of dashes that ends the table), or the table may be interpreted as a simple table.

<h3>Extension: grid_tables</h3>

 

 Grid tables look like this:
<dl>
<dt>
<dd> 
: Sample grid table.
+---------------+---------------+--------------------+
| Fruit         | Price         | Advantages         |
+===============+===============+====================+
| Bananas       | $1.34         | - built-in wrapper |
|               |               | - bright color     |
+---------------+---------------+--------------------+
| Oranges       | $2.10         | - cures scurvy     |
|               |               | - tasty            |
+---------------+---------------+--------------------+
</dl>
 

 The row of =s separates the header from the table body, and can be omitted for a headerless table. The cells of grid tables may contain arbitrary block elements (multiple paragraphs, code blocks, lists, etc.). Cells that span multiple columns or rows are not supported. Grid tables can be created easily using Emacs' table-mode (M-x table-insert). 

 Alignments can be specified as with pipe tables, by putting colons at the boundaries of the separator line after the header:
<dl>
<dt>
<dd> 
+ -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- --+ | Right | Left | Centered |
    += == == == == == ==
     =:+: == == == == == == == +: == == == == == == == == ==:+ | Bananas | $1 .34 | built - in wrapper | +-- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- --+
</dl>
 

 For headerless tables, the colons go on the top line instead:
<dl>
<dt>
<dd> 
+ -- -- -- -- -- -- --:+:-- -- -- -- -- -- --+:-- -- -- -- -- -- -- -- --:+ | Right | Left | Centered |
                                                                          +-- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -- -- --+
</dl>

<h3>Grid Table Limitations</h3>

 

 Pandoc does not support grid tables with row spans or column spans. This means that neither variable numbers of columns across rows nor variable numbers of rows across columns are supported by Pandoc. All grid tables must have the same number of columns in each row, and the same number of rows in each column. For example, the Docutils sample grid tables will not render as expected with Pandoc.

<h3>Extension: pipe_tables</h3>

 

 Pipe tables look like this:
<dl>
<dt>
<dd> 
| Right | Left | Default | Center |
    | -- -- -- : | : -- -- - | -- -- -- -- - | : -- -- -- : |
                                                            | 12 | 12 | 12 | 12 |
                                                            | 123 | 123 | 123 | 123 |
                                                            | 1 | 1 | 1 | 1 |
    : Demonstration of pipe table syntax.
</dl>
 

 The syntax is identical to PHP Markdown Extra tables. The beginning and ending pipe characters are optional, but pipes are required between all columns. The colons indicate column alignment as shown. The header cannot be omitted. To simulate a headerless table, include a header with blank cells. 

 Since the pipes indicate column boundaries, columns need not be vertically aligned, as they are in the above example. So, this is a perfectly legal (though ugly) pipe table:
<dl>
<dt>
<dd> 
fruit | price-- -- - | -- -- - : apple | 2.05 pear | 1.37 orange | 3.09
</dl>
 

 The cells of pipe tables cannot contain block elements like paragraphs and lists, and cannot span multiple lines. If a pipe table contains a row whose printable content is wider than the column width (see --columns), then the table will take up the full text width and the cell contents will wrap, with the relative cell widths determined by the number of dashes in the line separating the table header from the table body. (For example ---|- would make the first column 3/4 and the second column 1/4 of the full text width.) On the other hand, if no lines are wider than column width, then cell contents will not be wrapped, and the cells will be sized to their contents. 

 Note: pandoc also recognizes pipe tables of the following form, as can be produced by Emacs' orgtbl-mode:
<dl>
<dt>
<dd> 
| One | Two |
    | -- -- -+-- -- -- - |
    | my | table |
    | is | nice |
</dl>
 

 The difference is that + is used instead of |. Other orgtbl features are not supported. In particular, to get non-default column alignment, you'll need to add colons as above.

<h3>Metadata blocks</h3>

<h3>Extension: pandoc_title_block</h3>

 

 If the file begins with a title block
<dl>
<dt>
<dd> <pre>
% title
% author(s) (separated by semicolons)
% date
</pre></dl>
 

 it will be parsed as bibliographic information, not regular text. (It will be used, for example, in the title of standalone LaTeX or HTML output.) The block may contain just a title, a title and an author, or all three elements. If you want to include an author but no title, or a title and a date but no author, you need a blank line:
<dl>
<dt>
<dd> <pre>
%
% Author
% My title
%
% June 15, 2006
</pre></dl>
 

 The title may occupy multiple lines, but continuation lines must begin with leading space, thus:
<dl>
<dt>
<dd> <pre>
% My title
  on multiple lines
</pre></dl>
 

 If a document has multiple authors, the authors may be put on separate lines with leading space, or separated by semicolons, or both. So, all of the following are equivalent:
<dl>
<dt>
<dd> <pre>
% Author One
  Author Two
% Author One; Author Two
% Author One;
  Author Two
</pre></dl>
 

 The date must fit on one line. 

 All three metadata fields may contain standard inline formatting (italics, links, footnotes, etc.). 

 Title blocks will always be parsed, but they will affect the output only when the --standalone (-s) option is chosen. In HTML output, titles will appear twice: once in the document head -- this is the title that will appear at the top of the window in a browser -- and once at the beginning of the document body. The title in the document head can have an optional prefix attached (--title-prefix or -T option). The title in the body appears as an H1 element with class &quot;title&quot;, so it can be suppressed or reformatted with CSS. If a title prefix is specified with -T and no title block appears in the document, the title prefix will be used by itself as the HTML title. 

 The man page writer extracts a title, man page section number, and other header and footer information from the title line. The title is assumed to be the first word on the title line, which may optionally end with a (single-digit) section number in parentheses. (There should be no space between the title and the parentheses.) Anything after this is assumed to be additional footer and header text. A single pipe character (|) should be used to separate the footer text from the header text. Thus,
<dl>
<dt>
<dd> <pre>
% <a HREF="//www.systutorials.com/docs/linux/man/1-PANDOC/">PANDOC</a>(1)
</pre></dl>
 

 will yield a man page with the title PANDOC and section 1.
<dl>
<dt>
<dd> <pre>
% <a HREF="//www.systutorials.com/docs/linux/man/1-PANDOC/">PANDOC</a>(1) Pandoc User Manuals
</pre></dl>
 

 will also have &quot;Pandoc User Manuals&quot; in the footer.
<dl>
<dt>
<dd> <pre>
% <a HREF="//www.systutorials.com/docs/linux/man/1-PANDOC/">PANDOC</a>(1) Pandoc User Manuals | Version 4.0
</pre></dl>
 

 will also have &quot;Version 4.0&quot; in the header.

<h3>Extension: yaml_metadata_block</h3>

 

 A YAML metadata block is a valid YAML object, delimited by a line of three hyphens (---) at the top and a line of three hyphens (---) or three dots (...) at the bottom. A YAML metadata block may occur anywhere in the document, but if it is not at the beginning, it must be preceded by a blank line. (Note that, because of the way pandoc concatenates input files when several are provided, you may also keep the metadata in a separate YAML file and pass it to pandoc as an argument, along with your Markdown files:
<dl>
<dt>
<dd> <pre>
pandoc chap1.md chap2.md chap3.md metadata.yaml -s -o book.html
</pre></dl>
 

 Just be sure that the YAML file begins with --- and ends with --- or ....) Alternatively, you can use the --metadata-file option. Using that approach however, you cannot reference content (like footnotes) from the main markdown input document. 

 Metadata will be taken from the fields of the YAML object and added to any existing document metadata. Metadata can contain lists and objects (nested arbitrarily), but all string scalars will be interpreted as Markdown. Fields with names ending in an underscore will be ignored by pandoc. (They may be given a role by external processors.) Field names must not be interpretable as YAML numbers or boolean values (so, for example, yes, True, and 15 cannot be used as field names). 

 A document may contain multiple metadata blocks. If two metadata blocks attempt to set the same field, the value from the second block will be taken. 

 When pandoc is used with -t markdown to create a Markdown document, a YAML metadata block will be produced only if the -s/--standalone option is used. All of the metadata will appear in a single block at the beginning of the document. 

 Note that YAML escaping rules must be followed. Thus, for example, if a title contains a colon, it must be quoted. The pipe character (|) can be used to begin an indented block that will be interpreted literally, without need for escaping. This form is necessary when the field contains blank lines or block-level formatting:
<dl>
<dt>
<dd> <pre>
---
title:  'This is the title: it contains a colon'
author:
- Author One
- Author Two
keywords: [nothing, nothingness]
abstract: |
  This is the abstract.
  It consists of two paragraphs.
...
</pre></dl>
 

 Template variables will be set automatically from the metadata. Thus, for example, in writing HTML, the variable abstract will be set to the HTML equivalent of the Markdown in the abstract field:
<dl>
<dt>
<dd> <pre>
&lt;p&gt;This is the abstract.&lt;/p&gt;
&lt;p&gt;It consists of two paragraphs.&lt;/p&gt;
</pre></dl>
 

 Variables can contain arbitrary YAML structures, but the template must match this structure. The author variable in the default templates expects a simple list or string, but can be changed to support more complicated structures. The following combination, for example, would add an affiliation to the author if one is given:
<dl>
<dt>
<dd> <pre>
---
title: The document title
author:
- name: Author One
  affiliation: University of Somewhere
- name: Author Two
  affiliation: University of Nowhere
...
</pre></dl>
 

 To use the structured authors in the example above, you would need a custom template:
<dl>
<dt>
<dd> 
$for(author) $
    $if(author.name) $
    $author.name$$if(author.affiliation) $($author.affiliation$) $endif$
    $else$
    $author$
    $endif$
    $endfor$
</dl>
 

 Raw content to include in the document's header may be specified using header-includes; however, it is important to mark up this content as raw code for a particular output format, using the raw_attribute extension), or it will be interpreted as markdown. For example:
<dl>
<dt>
<dd> 
header - includes : - |
  ```
{
    = latex
}
\let\oldsection\section
  \renewcommand{\section}[1]
{
    \clearpage\oldsection
    {
# 1
    }
}
```
</dl>

<h3>Backslash escapes</h3>

<h3>Extension: all_symbols_escapable</h3>

 

 Except inside a code block or inline code, any punctuation or space character preceded by a backslash will be treated literally, even if it would normally indicate formatting. Thus, for example, if one writes
<dl>
<dt>
<dd> <pre>
*\*hello\**
</pre></dl>
 

 one will get
<dl>
<dt>
<dd> <pre>
&lt;em&gt;*hello*&lt;/em&gt;
</pre></dl>
 

 instead of
<dl>
<dt>
<dd> <pre>
&lt;strong&gt;hello&lt;/strong&gt;
</pre></dl>
 

 This rule is easier to remember than standard Markdown's rule, which allows only the following characters to be backslash-escaped:
<dl>
<dt>
<dd> 
\`*_{}[]() &gt; # + -.!
</dl>
 

 (However, if the markdown_strict format is used, the standard Markdown rule will be used.) 

 A backslash-escaped space is parsed as a nonbreaking space. In TeX output, it will appear as ~. In HTML and XML output, it will appear as a literal unicode nonbreaking space character (note that it will thus actually look &quot;invisible&quot; in the generated HTML source; you can still use the --ascii command-line option to make it appear as an explicit entity). 

 A backslash-escaped newline (i.e. a backslash occurring at the end of a line) is parsed as a hard line break. It will appear in TeX output as \\ and in HTML as &lt;br /&gt;. This is a nice alternative to Markdown's &quot;invisible&quot; way of indicating hard line breaks using two trailing spaces on a line. 

 Backslash escapes do not work in verbatim contexts.

<h3>Inline formatting</h3>

<h3>Emphasis</h3>

 

 To emphasize some text, surround it with *s or _, like this:
<dl>
<dt>
<dd> <pre>
This text is _emphasized with underscores_, and this
is *emphasized with asterisks*.
</pre></dl>
 

 Double * or _ produces strong emphasis:
<dl>
<dt>
<dd> <pre>
This is **strong emphasis** and __with underscores__.
</pre></dl>
 

 A * or _ character surrounded by spaces, or backslash-escaped, will not trigger emphasis:
<dl>
<dt>
<dd> <pre>
This is * not emphasized *, and \*neither is this\*.
</pre></dl>

<h3>Extension: intraword_underscores</h3>

 

 Because _ is sometimes used inside words and identifiers, pandoc does not interpret a _ surrounded by alphanumeric characters as an emphasis marker. If you want to emphasize just part of a word, use *:
<dl>
<dt>
<dd> <pre>
feas*ible*, not feas*able*.
</pre></dl>

<h3>Strikeout</h3>

<h3>Extension: strikeout</h3>

 

 To strikeout a section of text with a horizontal line, begin and end it with ~~. Thus, for example,
<dl>
<dt>
<dd> <pre>
This ~~is deleted text.~~
</pre></dl>

<h3>Superscripts and subscripts</h3>

<h3>Extension: superscript, subscript</h3>

 

 Superscripts may be written by surrounding the superscripted text by ha characters; subscripts may be written by surrounding the subscripted text by ~ characters. Thus, for example,
<dl>
<dt>
<dd> <pre>
H~2~O is a liquid.  2ha10ha is 1024.
</pre></dl>
 

 The text between ha...ha or ~...~ may not contain spaces or newlines. If the superscripted or subscripted text contains spaces, these spaces must be escaped with backslashes. (This is to prevent accidental superscripting and subscripting through the ordinary use of ~ and ha, and also bad interactions with footnotes.) Thus, if you want the letter P with 'a cat' in subscripts, use P~a\ cat~, not P~a cat~.

<h3>Verbatim</h3>

 

 To make a short span of text verbatim, put it inside backticks:
<dl>
<dt>
<dd> <pre>
What is the difference between `&gt;&gt;=` and `&gt;&gt;`?
</pre></dl>
 

 If the verbatim text includes a backtick, use double backticks:
<dl>
<dt>
<dd> <pre>
Here is a literal backtick `` ` ``.
</pre></dl>
 

 (The spaces after the opening backticks and before the closing backticks will be ignored.) 

 The general rule is that a verbatim span starts with a string of consecutive backticks (optionally followed by a space) and ends with a string of the same number of backticks (optionally preceded by a space). 

 Note that backslash-escapes (and other Markdown constructs) do not work in verbatim contexts:
<dl>
<dt>
<dd> <pre>
This is a backslash followed by an asterisk: `\*`.
</pre></dl>

<h3>Extension: inline_code_attributes</h3>

 

 Attributes can be attached to verbatim text, just as with fenced code blocks:
<dl>
<dt>
<dd> <pre>
`&lt;$&gt;`{.haskell}
</pre></dl>

<h3>Small caps</h3>

 

 To write small caps, use the smallcaps class:
<dl>
<dt>
<dd> 
[Small caps] { .smallcaps }
</dl>
 

 Or, without the bracketed_spans extension:
<dl>
<dt>
<dd> <pre>
&lt;span class=&quot;smallcaps&quot;&gt;Small caps&lt;/span&gt;
</pre></dl>
 

 For compatibility with other Markdown flavors, CSS is also supported:
<dl>
<dt>
<dd> <pre>
&lt;span style=&quot;font-variant:small-caps;&quot;&gt;Small caps&lt;/span&gt;
</pre></dl>
 

 This will work in all output formats that support small caps.

<h3>Math</h3>

<h3>Extension: tex_math_dollars</h3>

 

 Anything between two $ characters will be treated as TeX math. The opening $ must have a non-space character immediately to its right, while the closing $ must have a non-space character immediately to its left, and must not be followed immediately by a digit. Thus, $20,000 and $30,000 won't parse as math. If for some reason you need to enclose text in literal $ characters, backslash-escape them and they won't be treated as math delimiters. 

 For display math, use $$ delimiters. (In this case, the delimiters may be separated from the formula by whitespace.) 

 TeX math will be printed in all output formats. How it is rendered depends on the output format:
<dl>
<dt>LaTeX
<dd> It will appear verbatim surrounded by \(...\) (for inline math) or \[...\] (for display math).
<dt>Markdown, Emacs Org mode, ConTeXt, ZimWiki
<dd> It will appear verbatim surrounded by $...$ (for inline math) or $$...$$ (for display math).
<dt>XWiki
<dd> It will appear verbatim surrounded by &#123;&#123;formula}}..&#123;&#123;/formula}}.
<dt>reStructuredText
<dd> It will be rendered using an interpreted text role :math:.
<dt>AsciiDoc
<dd> For AsciiDoc output format (-t asciidoc) it will appear verbatim surrounded by latexmath:[$...$] (for inline math) or [latexmath]++++\[...\]+++ (for display math). For AsciiDoctor output format (-t asciidoctor) the LaTex delimiters ($..$ and \[..\]) are omitted.
<dt>Texinfo
<dd> It will be rendered inside a @math command.
<dt>roff man, Jira markup
<dd> It will be rendered verbatim without $'s.
<dt>MediaWiki, DokuWiki
<dd> It will be rendered inside &lt;math&gt; tags.
<dt>Textile
<dd> It will be rendered inside &lt;span class=&quot;math&quot;&gt; tags.
<dt>RTF, OpenDocument
<dd> It will be rendered, if possible, using Unicode characters, and will otherwise appear verbatim.
<dt>ODT
<dd> It will be rendered, if possible, using MathML.
<dt>DocBook
<dd> If the --mathml flag is used, it will be rendered using MathML in an inlineequation or informalequation tag. Otherwise it will be rendered, if possible, using Unicode characters.
<dt>Docx
<dd> It will be rendered using OMML math markup.
<dt>FictionBook2
<dd> If the --webtex option is used, formulas are rendered as images using CodeCogs or other compatible web service, downloaded and embedded in the e-book. Otherwise, they will appear verbatim.
<dt>HTML, Slidy, DZSlides, S5, EPUB
<dd> The way math is rendered in HTML will depend on the command-line options selected. Therefore see Math rendering in HTML above.</dl>

<h3>Raw HTML</h3>

<h3>Extension: raw_html</h3>

 

 Markdown allows you to insert raw HTML (or DocBook) anywhere in a document (except verbatim contexts, where &lt;, &gt;, and &amp; are interpreted literally). (Technically this is not an extension, since standard Markdown allows it, but it has been made an extension so that it can be disabled if desired.) 

 The raw HTML is passed through unchanged in HTML, S5, Slidy, Slideous, DZSlides, EPUB, Markdown, CommonMark, Emacs Org mode, and Textile output, and suppressed in other formats. 

 For a more explicit way of including raw HTML in a Markdown document, see the raw_attribute extension. 

 In the CommonMark format, if raw_html is enabled, superscripts, subscripts, strikeouts and small capitals will be represented as HTML. Otherwise, plain-text fallbacks will be used. Note that even if raw_html is disabled, tables will be rendered with HTML syntax if they cannot use pipe syntax.

<h3>Extension: markdown_in_html_blocks</h3>

 

 Standard Markdown allows you to include HTML &quot;blocks&quot;: blocks of HTML between balanced tags that are separated from the surrounding text with blank lines, and start and end at the left margin. Within these blocks, everything is interpreted as HTML, not Markdown; so (for example), * does not signify emphasis. 

 Pandoc behaves this way when the markdown_strict format is used; but by default, pandoc interprets material between HTML block tags as Markdown. Thus, for example, pandoc will turn
<dl>
<dt>
<dd> <pre>
&lt;table&gt;
&lt;tr&gt;
&lt;td&gt;*one*&lt;/td&gt;
&lt;td&gt;[a link](<a rel="nofollow" HREF="https://google.com)">https://google.com)</a>&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
</pre></dl>
 

 into
<dl>
<dt>
<dd> <pre>
&lt;table&gt;
&lt;tr&gt;
&lt;td&gt;&lt;em&gt;one&lt;/em&gt;&lt;/td&gt;
&lt;td&gt;&lt;a href=&quot;<a rel="nofollow" HREF="https://google.com">https://google.com</a>&quot;&gt;a link&lt;/a&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
</pre></dl>
 

 whereas Markdown.pl will preserve it as is. 

 There is one exception to this rule: text between &lt;script&gt; and &lt;style&gt; tags is not interpreted as Markdown. 

 This departure from standard Markdown should make it easier to mix Markdown with HTML block elements. For example, one can surround a block of Markdown text with &lt;div&gt; tags without preventing it from being interpreted as Markdown.

<h3>Extension: native_divs</h3>

 

 Use native pandoc Div blocks for content inside &lt;div&gt; tags. For the most part this should give the same output as markdown_in_html_blocks, but it makes it easier to write pandoc filters to manipulate groups of blocks.

<h3>Extension: native_spans</h3>

 

 Use native pandoc Span blocks for content inside &lt;span&gt; tags. For the most part this should give the same output as raw_html, but it makes it easier to write pandoc filters to manipulate groups of inlines.

<h3>Extension: raw_tex</h3>

 

 In addition to raw HTML, pandoc allows raw LaTeX, TeX, and ConTeXt to be included in a document. Inline TeX commands will be preserved and passed unchanged to the LaTeX and ConTeXt writers. Thus, for example, you can use LaTeX to include BibTeX citations:
<dl>
<dt>
<dd> <pre>
This result was proved in \cite{jones.1967}.
</pre></dl>
 

 Note that in LaTeX environments, like
<dl>
<dt>
<dd> 
\begin{tabular}
{
    | l | l |
}
\hline
        Age &amp;Frequency \\ \hline 18 --25 &amp;
    15 \ 26 --35 &amp; 33 \ 36 --45 &amp; 22 \\ \hline
\end
{
    tabular
}
</dl>
 

 the material between the begin and end tags will be interpreted as raw LaTeX, not as Markdown. 

 For a more explicit and flexible way of including raw TeX in a Markdown document, see the raw_attribute extension. 

 Inline LaTeX is ignored in output formats other than Markdown, LaTeX, Emacs Org mode, and ConTeXt.

<h3>Generic raw attribute</h3>

<h3>Extension: raw_attribute</h3>

 

 Inline spans and fenced code blocks with a special kind of attribute will be parsed as raw content with the designated format. For example, the following produces a raw roff ms block:
<dl>
<dt>
<dd> <pre>
```{=ms}
.MYMACRO
blah blah
```
</pre></dl>
 

 And the following produces a raw html inline element:
<dl>
<dt>
<dd> <pre>
This is `&lt;a&gt;html&lt;/a&gt;`{=html}
</pre></dl>
 

 This can be useful to insert raw xml into docx documents, e.g. a pagebreak:
<dl>
<dt>
<dd> <pre>
```{=openxml}
&lt;w:p&gt;
  &lt;w:r&gt;
    &lt;w:br w:type=&quot;page&quot;/&gt;
  &lt;/w:r&gt;
&lt;/w:p&gt;
```
</pre></dl>
 

 The format name should match the target format name (see -t/--to, above, for a list, or use pandoc --list-output-formats). Use openxml for docx output, opendocument for odt output, html5 for epub3 output, html4 for epub2 output, and latex, beamer, ms, or html5 for pdf output (depending on what you use for --pdf-engine). 

 This extension presupposes that the relevant kind of inline code or fenced code block is enabled. Thus, for example, to use a raw attribute with a backtick code block, backtick_code_blocks must be enabled. 

 The raw attribute cannot be combined with regular attributes.

<h3>LaTeX macros</h3>

<h3>Extension: latex_macros</h3>

 

 When this extension is enabled, pandoc will parse LaTeX macro definitions and apply the resulting macros to all LaTeX math and raw LaTeX. So, for example, the following will work in all output formats, not just LaTeX:
<dl>
<dt>
<dd> 
\newcommand{\tuple}[1]{\langle #1 \rangle} $\tuple{a, b, c} $
</dl>
 

 Note that LaTeX macros will not be applied if they occur inside a raw span or block marked with the raw_attribute extension. 

 When latex_macros is disabled, the raw LaTeX and math will not have macros applied. This is usually a better approach when you are targeting LaTeX or PDF. 

 Macro definitions in LaTeX will be passed through as raw LaTeX only if latex_macros is not enabled. Macro definitions in Markdown source (or other formats allowing raw_tex) will be passed through regardless of whether latex_macros is enabled.

<h3>Links</h3>

 

 Markdown allows links to be specified in several ways.

<h3>Automatic links</h3>

 

 If you enclose a URL or email address in pointy brackets, it will become a link:
<dl>
<dt>
<dd> <pre>
&lt;<a rel="nofollow" HREF="https://google.com">https://google.com</a>&gt;
&lt;sam [at] green.eggs.ham&gt;
</pre></dl>

<h3>Inline links</h3>

 

 An inline link consists of the link text in square brackets, followed by the URL in parentheses. (Optionally, the URL can be followed by a link title, in quotes.)
<dl>
<dt>
<dd> <pre>
This is an [inline link](/url), and here's [one with
a title](<a rel="nofollow" HREF="https://fsf.org">https://fsf.org</a> &quot;click here for a good time!&quot;).
</pre></dl>
 

 There can be no space between the bracketed part and the parenthesized part. The link text can contain formatting (such as emphasis), but the title cannot. 

 Email addresses in inline links are not autodetected, so they have to be prefixed with mailto:
<dl>
<dt>
<dd> 
[Write me !](mailto
             : sam[at] green.eggs.ham)
</dl>

<h3>Reference links</h3>

 

 An explicit reference link has two parts, the link itself and the link definition, which may occur elsewhere in the document (either before or after the link). 

 The link consists of link text in square brackets, followed by a label in square brackets. (There cannot be space between the two unless the spaced_reference_links extension is enabled.) The link definition consists of the bracketed label, followed by a colon and a space, followed by the URL, and optionally (after a space) a link title either in quotes or in parentheses. The label must not be parseable as a citation (assuming the citations extension is enabled): citations take precedence over link labels. 

 Here are some examples:
<dl>
<dt>
<dd> 
[my label 1] : / foo / bar.html "My title, optional"[my label 2] : / foo[my label 3] : https : // fsf.org (The free software foundation)
                                                                                               [my label 4] : /
                                                                                                              bar #special 'A title in single quotes'
</dl>
 

 The URL may optionally be surrounded by angle brackets:
<dl>
<dt>
<dd> <pre>
[my label 5]: &lt;<a rel="nofollow" HREF="http://foo.bar.baz">http://foo.bar.baz</a>&gt;
</pre></dl>
 

 The title may go on the next line:
<dl>
<dt>
<dd> <pre>
[my label 3]: <a rel="nofollow" HREF="https://fsf.org">https://fsf.org</a>
  &quot;The free software foundation&quot;
</pre></dl>
 

 Note that link labels are not case sensitive. So, this will work:
<dl>
<dt>
<dd> 
Here is[my link][FOO]
       [Foo] : /
               bar / baz
</dl>
 

 In an implicit reference link, the second pair of brackets is empty:
<dl>
<dt>
<dd> 
See[my website][].
    [my website] : http: // foo.bar.baz
</dl>
 

 Note: In Markdown.pl and most other Markdown implementations, reference link definitions cannot occur in nested constructions such as list items or block quotes. Pandoc lifts this arbitrary seeming restriction. So the following is fine in pandoc, though not in most other implementations:
<dl>
<dt>
<dd> 
&gt; My block[quote].&gt;&gt; [quote] : / foo
</dl>

<h3>Extension: shortcut_reference_links</h3>

 

 In a shortcut reference link, the second pair of brackets may be omitted entirely:
<dl>
<dt>
<dd> 
See[my website].
    [my website] : http: // foo.bar.baz
</dl>

<h3>Internal links</h3>

 

 To link to another section of the same document, use the automatically generated identifier (see Heading identifiers). For example:
<dl>
<dt>
<dd> <pre>
See the [Introduction](#introduction).
</pre></dl>
 

 or
<dl>
<dt>
<dd> 
See the[Introduction].
    [Introduction] : #introduction
</dl>
 

 Internal links are currently supported for HTML formats (including HTML slide shows and EPUB), LaTeX, and ConTeXt.

<h3>Images</h3>

 

 A link immediately preceded by a ! will be treated as an image. The link text will be used as the image's alt text:
<dl>
<dt>
<dd> 
![la lune](lalune.jpg "Voyage to the moon") ![movie reel]
     [movie reel] : movie.gif
</dl>

<h3>Extension: implicit_figures</h3>

 

 An image with nonempty alt text, occurring by itself in a paragraph, will be rendered as a figure with a caption. The image's alt text will be used as the caption.
<dl>
<dt>
<dd> <pre>
![This is the caption](/url/of/image.png)
</pre></dl>
 

 How this is rendered depends on the output format. Some output formats (e.g. RTF) do not yet support figures. In those formats, you'll just get an image in a paragraph by itself, with no caption. 

 If you just want a regular inline image, just make sure it is not the only thing in the paragraph. One way to do this is to insert a nonbreaking space after the image:
<dl>
<dt>
<dd> <pre>
![This image won't be a figure](/url/of/image.png)\
</pre></dl>
 

 Note that in reveal.js slide shows, an image in a paragraph by itself that has the stretch class will fill the screen, and the caption and figure tags will be omitted.

<h3>Extension: link_attributes</h3>

 

 Attributes can be set on links and images:
<dl>
<dt>
<dd> 
An inline ![image](foo.jpg) { #id.class width = 30 height = 20px } and a reference ![image][ref] with attributes.
                                                                           [ref] : foo.jpg "optional title"
{
#id.class key = val key2 = "val 2"
}
</dl>
 

 (This syntax is compatible with PHP Markdown Extra when only #id and .class are used.) 

 For HTML and EPUB, all known HTML5 attributes except width and height (but including srcset and sizes) are passed through as is. Unknown attributes are passed through as custom attributes, with data- prepended. The other writers ignore attributes that are not specifically supported by their output format. 

 The width and height attributes on images are treated specially. When used without a unit, the unit is assumed to be pixels. However, any of the following unit identifiers can be used: px, cm, mm, in, inch and %. There must not be any spaces between the number and the unit. For example:
<dl>
<dt>
<dd> 
![](file.jpg) { width = 50 % }

<dt>&bull;
<dd> Dimensions are converted to inches for output in page-based formats like LaTeX. Dimensions are converted to pixels for output in HTML-like formats. Use the --dpi option to specify the number of pixels per inch. The default is 96dpi.
<dt>&bull;
<dd> The % unit is generally relative to some available space. For example the above example will render to the following.
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> HTML: &lt;img href=&quot;file.jpg&quot; style=&quot;width: 50%;&quot; /&gt;
<dt>&bull;
<dd> LaTeX: \includegraphics[width=0.5\textwidth,height=\textheight]{file.jpg} (If you're using a custom template, you need to configure graphicx as in the default template.)
<dt>&bull;
<dd> ConTeXt: \externalfigure[file.jpg][width=0.5\textwidth]</dl>
</dl>

<dt>&bull;
<dd> Some output formats have a notion of a class (ConTeXt) or a unique identifier (LaTeX \caption), or both (HTML).
<dt>&bull;
<dd> When no width or height attributes are specified, the fallback is to look at the image resolution and the dpi metadata embedded in the image file.</dl>

<h3>Divs and Spans</h3>

 

 Using the native_divs and native_spans extensions (see above), HTML syntax can be used as part of markdown to create native Div and Span elements in the pandoc AST (as opposed to raw HTML). However, there is also nicer syntax available:

<h3>Extension: fenced_divs</h3>

 

 Allow special fenced syntax for native Div blocks. A Div starts with a fence containing at least three consecutive colons plus some attributes. The attributes may optionally be followed by another string of consecutive colons. The attribute syntax is exactly as in fenced code blocks (see Extension: fenced_code_attributes). As with fenced code blocks, one can use either attributes in curly braces or a single unbraced word, which will be treated as a class name. The Div ends with another line containing a string of at least three consecutive colons. The fenced Div should be separated by blank lines from preceding and following blocks. 

 Example:
<dl>
<dt>
<dd> <pre>
::::: {#special .sidebar}
Here is a paragraph.
And another.
:::::
</pre></dl>
 

 Fenced divs can be nested. Opening fences are distinguished because they must have attributes:
<dl>
<dt>
<dd> <pre>
::: Warning ::::::
This is a warning.
::: Danger
This is a warning within a warning.
:::
::::::::::::::::::
</pre></dl>
 

 Fences without attributes are always closing fences. Unlike with fenced code blocks, the number of colons in the closing fence need not match the number in the opening fence. However, it can be helpful for visual clarity to use fences of different lengths to distinguish nested divs from their parents.

<h3>Extension: bracketed_spans</h3>

 

 A bracketed sequence of inlines, as one would use to begin a link, will be treated as a Span with attributes if it is followed immediately by attributes:
<dl>
<dt>
<dd> 
[This is * some text * ] { .class key = "val" }
</dl>

<h3>Footnotes</h3>

<h3>Extension: footnotes</h3>

 

 Pandoc's Markdown allows footnotes, using the following syntax:
<dl>
<dt>
<dd> 
Here is a footnote reference, [ha1] and another.[halongnote][ha1] : Here is the footnote.[halongnote] : Here's one with multiple blocks. Subsequent paragraphs are indented to show that they belong to the previous footnote.{some.code} The whole paragraph can be indented, or just the first
                                                                                                                                                                                                                                                                                       line.In this way,
    multi - paragraph footnotes work like multi - paragraph list items.This paragraph won't be part of the note, because it isn't indented.
</dl>
 

 The identifiers in footnote references may not contain spaces, tabs, or newlines. These identifiers are used only to correlate the footnote reference with the note itself; in the output, footnotes will be numbered sequentially. 

 The footnotes themselves need not be placed at the end of the document. They may appear anywhere except inside other block elements (lists, block quotes, tables, etc.). Each footnote should be separated from surrounding content (including other footnotes) by blank lines.

<h3>Extension: inline_notes</h3>

 

 Inline footnotes are also allowed (though, unlike regular notes, they cannot contain multiple paragraphs). The syntax is as follows:
<dl>
<dt>
<dd> <pre>
Here is an inline note.ha[Inlines notes are easier to write, since
you don't have to pick an identifier and move down to type the
note.]
</pre></dl>
 

 Inline and regular footnotes may be mixed freely.

<h3>Citations</h3>

<h3>Extension: citations</h3>

 

 Using an external filter, pandoc-citeproc, pandoc can automatically generate citations and a bibliography in a number of styles. Basic usage is
<dl>
<dt>
<dd> <pre>
pandoc --filter pandoc-citeproc myinput.txt
</pre></dl>
 

 In order to use this feature, you will need to specify a bibliography file using the bibliography metadata field in a YAML metadata section, or --bibliography command line argument. You can supply multiple --bibliography arguments or set bibliography metadata field to YAML array, if you want to use multiple bibliography files. The bibliography may have any of these formats: 

 <table> <tr VALIGN=top><td> Format </td><td> File extension 
</td></tr> <tr VALIGN=top><td COLSPAN=2><hr></td></tr> <tr VALIGN=top><td> BibLaTeX </td><td> .bib 
</td></tr> <tr VALIGN=top><td> BibTeX </td><td> .bibtex 
</td></tr> <tr VALIGN=top><td> Copac </td><td> .copac 
</td></tr> <tr VALIGN=top><td> CSL JSON </td><td> .json 
</td></tr> <tr VALIGN=top><td> CSL YAML </td><td> .yaml 
</td></tr> <tr VALIGN=top><td> EndNote </td><td> .enl 
</td></tr> <tr VALIGN=top><td> EndNote XML </td><td> .xml 
</td></tr> <tr VALIGN=top><td> ISI </td><td> .wos 
</td></tr> <tr VALIGN=top><td> MEDLINE </td><td> .medline 
</td></tr> <tr VALIGN=top><td> MODS </td><td> .mods 
</td></tr> <tr VALIGN=top><td> RIS </td><td> .ris 
</td></tr> </table> 

 Note that .bib can be used with both BibTeX and BibLaTeX files; use .bibtex to force BibTeX. 

 Note that pandoc-citeproc --bib2json and pandoc-citeproc --bib2yaml can produce .json and .yaml files from any of the supported formats. 

 In-field markup: In BibTeX and BibLaTeX databases, pandoc-citeproc parses a subset of LaTeX markup; in CSL YAML databases, pandoc Markdown; and in CSL JSON databases, an HTML-like markup:
<dl>
<dt>&lt;i&gt;...&lt;/i&gt;
<dd> italics
<dt>&lt;b&gt;...&lt;/b&gt;
<dd> bold
<dt>&lt;span style=&quot;font-variant:small-caps;&quot;&gt;...&lt;/span&gt; or &lt;sc&gt;...&lt;/sc&gt;
<dd> small capitals
<dt>&lt;sub&gt;...&lt;/sub&gt;
<dd> subscript
<dt>&lt;sup&gt;...&lt;/sup&gt;
<dd> superscript
<dt>&lt;span class=&quot;nocase&quot;&gt;...&lt;/span&gt;
<dd> prevent a phrase from being capitalized as title case</dl>
 

 pandoc-citeproc -j and -y interconvert the CSL JSON and CSL YAML formats as far as possible. 

 As an alternative to specifying a bibliography file using --bibliography or the YAML metadata field bibliography, you can include the citation data directly in the references field of the document's YAML metadata. The field should contain an array of YAML-encoded references, for example:
<dl>
<dt>
<dd> <pre>
---
references:
- type: article-journal
  id: WatsonCrick1953
  author:
  - family: Watson
    given: J. D.
  - family: Crick
    given: F. H. C.
  issued:
    date-parts:
    - - 1953
      - 4
      - 25
  title: 'Molecular structure of nucleic acids: a structure for deoxyribose
    nucleic acid'
  title-short: Molecular structure of nucleic acids
  container-title: Nature
  volume: 171
  issue: 4356
  page: 737-738
  DOI: 10.1038/171737a0
  URL: <a rel="nofollow" HREF="https://www.nature.com/articles/171737a0">https://www.nature.com/articles/171737a0</a>
  language: en-GB
...
</pre></dl>
 

 (pandoc-citeproc --bib2yaml can produce these from a bibliography file in one of the supported formats.) 

 Citations and references can be formatted using any style supported by the Citation Style Language, listed in the Zotero Style Repository. These files are specified using the --csl option or the csl metadata field. By default, pandoc-citeproc will use the Chicago Manual of Style author-date format. The CSL project provides further information on finding and editing styles. 

 To make your citations hyperlinks to the corresponding bibliography entries, add link-citations: true to your YAML metadata. 

 Citations go inside square brackets and are separated by semicolons. Each citation must have a key, composed of '@' + the citation identifier from the database, and may optionally have a prefix, a locator, and a suffix. The citation key must begin with a letter, digit, or _, and may contain alphanumerics, _, and internal punctuation characters (:.#$%&amp;-+?&lt;&gt;~/). Here are some examples:
<dl>
<dt>
<dd> 
Blah blah[see @doe99, pp.33 - 35; also @smith04, chap.1].Blah blah[@doe99, pp.33 - 35, 38 - 39 and *passim *].Blah blah[@smith04; @doe99].
</dl>
 

 pandoc-citeproc detects locator terms in the CSL locale files. Either abbreviated or unabbreviated forms are accepted. In the en-US locale, locator terms can be written in either singular or plural forms, as book, bk./bks.; chapter, chap./chaps.; column, col./cols.; figure, fig./figs.; folio, fol./fols.; number, no./nos.; line, l./ll.; note, n./nn.; opus, op./opp.; page, p./pp.; paragraph, para./paras.; part, pt./pts.; section, sec./secs.; sub verbo, s.v./s.vv.; verse, v./vv.; volume, vol./vols.; &para;/&para;&para;; &#167;/&#167;&#167;. If no locator term is used, &quot;page&quot; is assumed. 

 pandoc-citeproc will use heuristics to distinguish the locator from the suffix. In complex cases, the locator can be enclosed in curly braces (using pandoc-citeproc 0.15 and higher only):
<dl>
<dt>
<dd> 
[ @smith{ii, A, D - Z}, with a suffix ]
    [@smith, {pp.iv, vi - xi, (xv) - (xvii)} with suffix here]
</dl>
 

 A minus sign (-) before the @ will suppress mention of the author in the citation. This can be useful when the author is already mentioned in the text:
<dl>
<dt>
<dd> <pre>
Smith says blah [-@smith04].
</pre></dl>
 

 You can also write an in-text citation, as follows:
<dl>
<dt>
<dd> <pre>
@smith04 says blah.
@smith04 [p. 33] says blah.
</pre></dl>
 

 If the style calls for a list of works cited, it will be placed in a div with id refs, if one exists:
<dl>
<dt>
<dd> <pre>
::: {#refs}
:::
</pre></dl>
 

 Otherwise, it will be placed at the end of the document. Generation of the bibliography can be suppressed by setting suppress-bibliography: true in the YAML metadata. 

 If you wish the bibliography to have a section heading, you can set reference-section-title in the metadata, or put the heading at the beginning of the div with id refs (if you are using it) or at the end of your document:
<dl>
<dt>
<dd> <pre>
last paragraph...
# References
</pre></dl>
 

 The bibliography will be inserted after this heading. Note that the unnumbered class will be added to this heading, so that the section will not be numbered. 

 If you want to include items in the bibliography without actually citing them in the body text, you can define a dummy nocite metadata field and put the citations there:
<dl>
<dt>
<dd> <pre>
---
nocite: |
  @item1, @item2
...
@item3
</pre></dl>
 

 In this example, the document will contain a citation for item3 only, but the bibliography will contain entries for item1, item2, and item3. 

 It is possible to create a bibliography with all the citations, whether or not they appear in the document, by using a wildcard:
<dl>
<dt>
<dd> <pre>
---
nocite: |
  @*
...
</pre></dl>
 

 For LaTeX output, you can also use natbib or biblatex to render the bibliography. In order to do so, specify bibliography files as outlined above, and add --natbib or --biblatex argument to pandoc invocation. Bear in mind that bibliography files have to be in respective format (either BibTeX or BibLaTeX). 

 For more information, see the pandoc-citeproc man page.

<h3>Non-pandoc extensions</h3>

 

 The following Markdown syntax extensions are not enabled by default in pandoc, but may be enabled by adding +EXTENSION to the format name, where EXTENSION is the name of the extension. Thus, for example, markdown+hard_line_breaks is Markdown with hard line breaks.

<h3>Extension: old_dashes</h3>

 

 Selects the pandoc &lt;= 1.8.2.1 behavior for parsing smart dashes: - before a numeral is an en-dash, and -- is an em-dash. This option only has an effect if smart is enabled. It is selected automatically for textile input.

<h3>Extension: angle_brackets_escapable</h3>

 

 Allow &lt; and &gt; to be backslash-escaped, as they can be in GitHub flavored Markdown but not original Markdown. This is implied by pandoc's default all_symbols_escapable.

<h3>Extension: lists_without_preceding_blankline</h3>

 

 Allow a list to occur right after a paragraph, with no intervening blank space.

<h3>Extension: four_space_rule</h3>

 

 Selects the pandoc &lt;= 2.0 behavior for parsing lists, so that four spaces indent are needed for list item continuation paragraphs.

<h3>Extension: spaced_reference_links</h3>

 

 Allow whitespace between the two components of a reference link, for example,
<dl>
<dt>
<dd> 
[foo][bar].
</dl>

<h3>Extension: hard_line_breaks</h3>

 

 Causes all newlines within a paragraph to be interpreted as hard line breaks instead of spaces.

<h3>Extension: ignore_line_breaks</h3>

 

 Causes newlines within a paragraph to be ignored, rather than being treated as spaces or as hard line breaks. This option is intended for use with East Asian languages where spaces are not used between words, but text is divided into lines for readability.

<h3>Extension: east_asian_line_breaks</h3>

 

 Causes newlines within a paragraph to be ignored, rather than being treated as spaces or as hard line breaks, when they occur between two East Asian wide characters. This is a better choice than ignore_line_breaks for texts that include a mix of East Asian wide characters and other characters.

<h3>Extension: emoji</h3>

 

 Parses textual emojis like :smile: as Unicode emoticons.

<h3>Extension: tex_math_single_backslash</h3>

 

 Causes anything between \( and \) to be interpreted as inline TeX math, and anything between \[ and \] to be interpreted as display TeX math. Note: a drawback of this extension is that it precludes escaping ( and [.

<h3>Extension: tex_math_double_backslash</h3>

 

 Causes anything between \\( and \\) to be interpreted as inline TeX math, and anything between \\[ and \\] to be interpreted as display TeX math.

<h3>Extension: markdown_attribute</h3>

 

 By default, pandoc interprets material inside block-level tags as Markdown. This extension changes the behavior so that Markdown is only parsed inside block-level tags if the tags have the attribute markdown=1.

<h3>Extension: mmd_title_block</h3>

 

 Enables a MultiMarkdown style title block at the top of the document, for example:
<dl>
<dt>
<dd> <pre>
Title:   My title
Author:  John Doe
Date:    September 1, 2008
Comment: This is a sample mmd title block, with
         a field spanning multiple lines.
</pre></dl>
 

 See the MultiMarkdown documentation for details. If pandoc_title_block or yaml_metadata_block is enabled, it will take precedence over mmd_title_block.

<h3>Extension: abbreviations</h3>

 

 Parses PHP Markdown Extra abbreviation keys, like
<dl>
<dt>
<dd> <pre>
*[HTML]: Hypertext Markup Language
</pre></dl>
 

 Note that the pandoc document model does not support abbreviations, so if this extension is enabled, abbreviation keys are simply skipped (as opposed to being parsed as paragraphs).

<h3>Extension: autolink_bare_uris</h3>

 

 Makes all absolute URIs into links, even when not surrounded by pointy braces &lt;...&gt;.

<h3>Extension: mmd_link_attributes</h3>

 

 Parses multimarkdown style key-value attributes on link and image references. This extension should not be confused with the link_attributes extension.
<dl>
<dt>
<dd> 
This is a reference ![image][ref] with multimarkdown attributes.
    [ref] : https : // path.to/image "Image title" width=20px height=30px
                    id = myId class
    = "myClass1 myClass2"
</dl>

<h3>Extension: mmd_header_identifiers</h3>

 

 Parses multimarkdown style heading identifiers (in square brackets, after the heading but before any trailing #s in an ATX heading).

<h3>Extension: compact_definition_lists</h3>

 

 Activates the definition list syntax of pandoc 1.12.x and earlier. This syntax differs from the one described above under Definition lists in several respects:
<dl>
<dt>&bull;
<dd> No blank line is required between consecutive items of the definition list.
<dt>&bull;
<dd> To get a &quot;tight&quot; or &quot;compact&quot; list, omit space between consecutive items; the space between a term and its definition does not affect anything.
<dt>&bull;
<dd> Lazy wrapping of paragraphs is not allowed: the entire definition must be indented four spaces.</dl>

<h3>Extension: gutenberg</h3>

 

 Use Project Gutenberg conventions for plain output: all-caps for strong emphasis, surround by underscores for regular emphasis, add extra blank space around headings.

<h3>Markdown variants</h3>

 

 In addition to pandoc's extended Markdown, the following Markdown variants are supported:
<dl>
<dt>markdown_phpextra (PHP Markdown Extra)
<dd> footnotes, pipe_tables, raw_html, markdown_attribute, fenced_code_blocks, definition_lists, intraword_underscores, header_attributes, link_attributes, abbreviations, shortcut_reference_links, spaced_reference_links.
<dt>markdown_github (deprecated GitHub-Flavored Markdown)
<dd> pipe_tables, raw_html, fenced_code_blocks, auto_identifiers, gfm_auto_identifiers, backtick_code_blocks, autolink_bare_uris, space_in_atx_header, intraword_underscores, strikeout, task_lists, emoji, shortcut_reference_links, angle_brackets_escapable, lists_without_preceding_blankline.
<dt>markdown_mmd (MultiMarkdown)
<dd> pipe_tables, raw_html, markdown_attribute, mmd_link_attributes, tex_math_double_backslash, intraword_underscores, mmd_title_block, footnotes, definition_lists, all_symbols_escapable, implicit_header_references, auto_identifiers, mmd_header_identifiers, shortcut_reference_links, implicit_figures, superscript, subscript, backtick_code_blocks, spaced_reference_links, raw_attribute.
<dt>markdown_strict (Markdown.pl)
<dd> raw_html, shortcut_reference_links, spaced_reference_links.</dl>
 

 We also support commonmark and gfm (GitHub-Flavored Markdown, which is implemented as a set of extensions on commonmark). 

 Note, however, that commonmark and gfm have limited support for extensions. Only those listed below (and smart, raw_tex, and hard_line_breaks) will work. The extensions can, however, all be individually disabled. Also, raw_tex only affects gfm output, not input.
<dl>
<dt>gfm (GitHub-Flavored Markdown)
<dd> pipe_tables, raw_html, fenced_code_blocks, auto_identifiers, gfm_auto_identifiers, backtick_code_blocks, autolink_bare_uris, space_in_atx_header, intraword_underscores, strikeout, task_lists, emoji, shortcut_reference_links, angle_brackets_escapable, lists_without_preceding_blankline.</dl>

<h2>PRODUCING SLIDE SHOWS WITH PANDOC</h2>

 

 You can use pandoc to produce an HTML + JavaScript slide presentation that can be viewed via a web browser. There are five ways to do this, using S5, DZSlides, Slidy, Slideous, or reveal.js. You can also produce a PDF slide show using LaTeX beamer, or slides shows in Microsoft PowerPoint format. 

 Here's the Markdown source for a simple slide show, habits.txt:
<dl>
<dt>
<dd> 
% Habits % John Doe % March 22, 2005
#In the morning
                                    ##Getting up -
                                    Turn off alarm - Get out of bed##Breakfast - Eat eggs - Drink coffee
#In the evening
                                    ##Dinner -
                                    Eat spaghetti - Drink wine-- -- -- -- -- -- -- -- --![picture of spaghetti](images / spaghetti.jpg)##Going to sleep - Get in bed - Count sheep
</dl>
 

 To produce an HTML/JavaScript slide show, simply type
<dl>
<dt>
<dd> <pre>
pandoc -t FORMAT -s habits.txt -o habits.html
</pre></dl>
 

 where FORMAT is either s5, slidy, slideous, dzslides, or revealjs. 

 For Slidy, Slideous, reveal.js, and S5, the file produced by pandoc with the -s/--standalone option embeds a link to JavaScript and CSS files, which are assumed to be available at the relative path s5/default (for S5), slideous (for Slideous), reveal.js (for reveal.js), or at the Slidy website at w3.org (for Slidy). (These paths can be changed by setting the slidy-url, slideous-url, revealjs-url, or s5-url variables; see Variables for HTML slides, above.) For DZSlides, the (relatively short) JavaScript and CSS are included in the file by default. 

 With all HTML slide formats, the --self-contained option can be used to produce a single file that contains all of the data necessary to display the slide show, including linked scripts, stylesheets, images, and videos. 

 To produce a PDF slide show using beamer, type
<dl>
<dt>
<dd> <pre>
pandoc -t beamer habits.txt -o habits.pdf
</pre></dl>
 

 Note that a reveal.js slide show can also be converted to a PDF by printing it to a file from the browser. 

 To produce a Powerpoint slide show, type
<dl>
<dt>
<dd> <pre>
pandoc habits.txt -o habits.pptx
</pre></dl>

<h3>Structuring the slide show</h3>

 

 By default, the slide level is the highest heading level in the hierarchy that is followed immediately by content, and not another heading, somewhere in the document. In the example above, level-1 headings are always followed by level-2 headings, which are followed by content, so the slide level is 2. This default can be overridden using the --slide-level option. 

 The document is carved up into slides according to the following rules:
<dl>
<dt>&bull;
<dd> A horizontal rule always starts a new slide.
<dt>&bull;
<dd> A heading at the slide level always starts a new slide.
<dt>&bull;
<dd> Headings below the slide level in the hierarchy create headings within a slide.
<dt>&bull;
<dd> Headings above the slide level in the hierarchy create &quot;title slides,&quot; which just contain the section title and help to break the slide show into sections. Non-slide content under these headings will be included on the title slide (for HTML slide shows) or in a subsequent slide with the same title (for beamer).
<dt>&bull;
<dd> A title page is constructed automatically from the document's title block, if present. (In the case of beamer, this can be disabled by commenting out some lines in the default template.)</dl>
 

 These rules are designed to support many different styles of slide show. If you don't care about structuring your slides into sections and subsections, you can just use level-1 headings for all each slide. (In that case, level-1 will be the slide level.) But you can also structure the slide show into sections, as in the example above. 

 Note: in reveal.js slide shows, if slide level is 2, a two-dimensional layout will be produced, with level-1 headings building horizontally and level-2 headings building vertically. It is not recommended that you use deeper nesting of section levels with reveal.js.

<h3>Incremental lists</h3>

 

 By default, these writers produce lists that display &quot;all at once.&quot; If you want your lists to display incrementally (one item at a time), use the -i option. If you want a particular list to depart from the default, put it in a div block with class incremental or nonincremental. So, for example, using the fenced div syntax, the following would be incremental regardless of the document default:
<dl>
<dt>
<dd> <pre>
::: incremental
- Eat spaghetti
- Drink wine
:::
</pre></dl>
 

 or
<dl>
<dt>
<dd> <pre>
::: nonincremental
- Eat spaghetti
- Drink wine
:::
</pre></dl>
 

 While using incremental and nonincremental divs are the recommended method of setting incremental lists on a per-case basis, an older method is also supported: putting lists inside a blockquote will depart from the document default (that is, it will display incrementally without the -i option and all at once with the -i option):
<dl>
<dt>
<dd> <pre>
&gt; - Eat spaghetti
&gt; - Drink wine
</pre></dl>
 

 Both methods allow incremental and nonincremental lists to be mixed in a single document. 

 Note: Neither the -i/--incremental option nor any of the methods described here currently works for PowerPoint output.

<h3>Inserting pauses</h3>

 

 You can add &quot;pauses&quot; within a slide by including a paragraph containing three dots, separated by spaces:
<dl>
<dt>
<dd> <pre>
# Slide with a pause
content before the pause
. . .
content after the pause
</pre></dl>
 

 Note: this feature is not yet implemented for PowerPoint output.

<h3>Styling the slides</h3>

 

 You can change the style of HTML slides by putting customized CSS files in $DATADIR/s5/default (for S5), $DATADIR/slidy (for Slidy), or $DATADIR/slideous (for Slideous), where $DATADIR is the user data directory (see --data-dir, above). The originals may be found in pandoc's system data directory (generally $CABALDIR/pandoc-VERSION/s5/default). Pandoc will look there for any files it does not find in the user data directory. 

 For dzslides, the CSS is included in the HTML file itself, and may be modified there. 

 All reveal.js configuration options can be set through variables. For example, themes can be used by setting the theme variable:
<dl>
<dt>
<dd> <pre>
-V theme=moon
</pre></dl>
 

 Or you can specify a custom stylesheet using the --css option. 

 To style beamer slides, you can specify a theme, colortheme, fonttheme, innertheme, and outertheme, using the -V option:
<dl>
<dt>
<dd> <pre>
pandoc -t beamer habits.txt -V theme:Warsaw -o habits.pdf
</pre></dl>
 

 Note that heading attributes will turn into slide attributes (on a &lt;div&gt; or &lt;section&gt;) in HTML slide formats, allowing you to style individual slides. In beamer, the only heading attribute that affects slides is the allowframebreaks class, which sets the allowframebreaks option, causing multiple slides to be created if the content overfills the frame. This is recommended especially for bibliographies:
<dl>
<dt>
<dd> <pre>
# References {.allowframebreaks}
</pre></dl>

<h3>Speaker notes</h3>

 

 Speaker notes are supported in reveal.js and PowerPoint (pptx) output. You can add notes to your Markdown document thus:
<dl>
<dt>
<dd> <pre>
::: notes
This is my note.
- It can contain Markdown
- like this list
:::
</pre></dl>
 

 To show the notes window in reveal.js, press s while viewing the presentation. Speaker notes in PowerPoint will be available, as usual, in handouts and presenter view. 

 Notes are not yet supported for other slide formats, but the notes will not appear on the slides themselves.

<h3>Columns</h3>

 

 To put material in side by side columns, you can use a native div container with class columns, containing two or more div containers with class column and a width attribute:
<dl>
<dt>
<dd> 
:: :: :: :: :: :: ::
{
    .columns
}
:: : {.column width = "40%"} contents... :: : :: : {.column width = "60%"} contents... :: : :: :: :: :: :: :: ::
</dl>

<h3>Frame attributes in beamer</h3>

 

 Sometimes it is necessary to add the LaTeX [fragile] option to a frame in beamer (for example, when using the minted environment). This can be forced by adding the fragile class to the heading introducing the slide:
<dl>
<dt>
<dd> <pre>
# Fragile slide {.fragile}
</pre></dl>
 

 All of the other frame attributes described in Section 8.1 of the Beamer User's Guide may also be used: allowdisplaybreaks, allowframebreaks, b, c, t, environment, label, plain, shrink, standout, noframenumbering.

<h3>Background in reveal.js and beamer</h3>

 

 Background images can be added to self-contained reveal.js slideshows and to beamer slideshows. 

 For the same image on every slide, use the configuration option background-image either in the YAML metadata block or as a command-line variable. (There are no other options in beamer and the rest of this section concerns reveal.js slideshows.) 

 For reveal.js, you can instead use the reveal.js-native option parallaxBackgroundImage. You can also set parallaxBackgroundHorizontal and parallaxBackgroundVertical the same way and must also set parallaxBackgroundSize to have your values take effect. 

 To set an image for a particular reveal.js slide, add {data-background-image=&quot;/path/to/image&quot;} to the first slide-level heading on the slide (which may even be empty). 

 In reveal.js's overview mode, the parallaxBackgroundImage will show up only on the first slide. 

 Other reveal.js background settings also work on individual slides, including data-background-size, data-background-repeat, data-background-color, data-transition, and data-transition-speed. 

 To add a background image to the automatically generated title slide, use the title-slide-attributes variable in the YAML metadata block. It must contain a map of attribute names and values. 

 See the reveal.js documentation for more details. 

 For example in reveal.js:
<dl>
<dt>
<dd> 
---
title: My Slideshow
parallaxBackgroundImage: /path/to/my/background_image.png
title-slide-attributes:
    data-background-image: /path/to/title_image.png
    data-background-size: contain
---
## Slide One
Slide 1 has background_image.png as its background.
## {data-background-image="/path/to/special_image.jpg"}
Slide 2 has a special image for its background, even though the heading has no content.
</dl>

<h2>CREATING EPUBS WITH PANDOC</h2>

<h3>EPUB Metadata</h3>

 

 EPUB metadata may be specified using the --epub-metadata option, but if the source document is Markdown, it is better to use a YAML metadata block. Here is an example:
<dl>
<dt>
<dd> <pre>
---
title:
- type: main
  text: My Book
- type: subtitle
  text: An investigation of metadata
creator:
- role: author
  text: John Smith
- role: editor
  text: Sarah Jones
identifier:
- scheme: DOI
  text: doi:10.234234.234/33
publisher:  My Press
rights: &#169; 2007 John Smith, CC BY-NC
ibooks:
  version: 1.3.4
...
</pre></dl>
 

 The following fields are recognized:
<dl>
<dt>identifier
<dd> Either a string value or an object with fields text and scheme. Valid values for scheme are ISBN-10, GTIN-13, UPC, ISMN-10, DOI, LCCN, GTIN-14, ISBN-13, Legal deposit number, URN, OCLC, ISMN-13, ISBN-A, JP, OLCC.
<dt>title
<dd> Either a string value, or an object with fields file-as and type, or a list of such objects. Valid values for type are main, subtitle, short, collection, edition, extended.
<dt>creator
<dd> Either a string value, or an object with fields role, file-as, and text, or a list of such objects. Valid values for role are MARC relators, but pandoc will attempt to translate the human-readable versions (like &quot;author&quot; and &quot;editor&quot;) to the appropriate marc relators.
<dt>contributor
<dd> Same format as creator.
<dt>date
<dd> A string value in YYYY-MM-DD format. (Only the year is necessary.) Pandoc will attempt to convert other common date formats.
<dt>lang (or legacy: language)
<dd> A string value in BCP 47 format. Pandoc will default to the local language if nothing is specified.
<dt>subject
<dd> A string value or a list of such values.
<dt>description
<dd> A string value.
<dt>type
<dd> A string value.
<dt>format
<dd> A string value.
<dt>relation
<dd> A string value.
<dt>coverage
<dd> A string value.
<dt>rights
<dd> A string value.
<dt>cover-image
<dd> A string value (path to cover image).
<dt>css (or legacy: stylesheet)
<dd> A string value (path to CSS stylesheet).
<dt>page-progression-direction
<dd> Either ltr or rtl. Specifies the page-progression-direction attribute for the spine element.
<dt>ibooks
<dd> iBooks-specific metadata, with the following fields:
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> version: (string)
<dt>&bull;
<dd> specified-fonts: true|false (default false)
<dt>&bull;
<dd> ipad-orientation-lock: portrait-only|landscape-only
<dt>&bull;
<dd> iphone-orientation-lock: portrait-only|landscape-only
<dt>&bull;
<dd> binding: true|false (default true)
<dt>&bull;
<dd> scroll-axis: vertical|horizontal|default</dl>
</dl>
</dl>

<h3>The epub:type attribute</h3>

 

 For epub3 output, you can mark up the heading that corresponds to an EPUB chapter using the epub:type attribute. For example, to set the attribute to the value prologue, use this markdown:
<dl>
<dt>
<dd> <pre>
# My chapter {epub:type=prologue}
</pre></dl>
 

 Which will result in:
<dl>
<dt>
<dd> <pre>
&lt;body epub:type=&quot;frontmatter&quot;&gt;
  &lt;section epub:type=&quot;prologue&quot;&gt;
    &lt;h1&gt;My chapter&lt;/h1&gt;
</pre></dl>
 

 Pandoc will output &lt;body epub:type=&quot;bodymatter&quot;&gt;, unless you use one of the following values, in which case either frontmatter or backmatter will be output. 

 <table> <tr VALIGN=top><td> epub:type of first section </td><td> epub:type of body 
</td></tr> <tr VALIGN=top><td COLSPAN=2><hr></td></tr> <tr VALIGN=top><td> prologue </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> abstract </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> acknowledgments </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> copyright-page </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> dedication </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> credits </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> keywords </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> imprint </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> contributors </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> other-credits </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> errata </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> revision-history </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> titlepage </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> halftitlepage </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> seriespage </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> foreword </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> preface </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> seriespage </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> titlepage </td><td> frontmatter 
</td></tr> <tr VALIGN=top><td> appendix </td><td> backmatter 
</td></tr> <tr VALIGN=top><td> colophon </td><td> backmatter 
</td></tr> <tr VALIGN=top><td> bibliography </td><td> backmatter 
</td></tr> <tr VALIGN=top><td> index </td><td> backmatter 
</td></tr> </table>

<h3>Linked media</h3>

 

 By default, pandoc will download media referenced from any &lt;img&gt;, &lt;audio&gt;, &lt;video&gt; or &lt;source&gt; element present in the generated EPUB, and include it in the EPUB container, yielding a completely self-contained EPUB. If you want to link to external media resources instead, use raw HTML in your source and add data-external=&quot;1&quot; to the tag with the src attribute. For example:
<dl>
<dt>
<dd> <pre>
&lt;audio controls=&quot;1&quot;&gt;
  &lt;source src=&quot;<a rel="nofollow" HREF="https://example.com/music/toccata.mp3">https://example.com/music/toccata.mp3</a>&quot;
          data-external=&quot;1&quot; type=&quot;audio/mpeg&quot;&gt;
  &lt;/source&gt;
&lt;/audio&gt;
</pre></dl>

<h2>CREATING JUPYTER NOTEBOOKS WITH PANDOC</h2>

 

 When creating a Jupyter notebook, pandoc will try to infer the notebook structure. Code blocks with the class code will be taken as code cells, and intervening content will be taken as Markdown cells. Attachments will automatically be created for images in Markdown cells. Metadata will be taken from the jupyter metadata field. For example:
<dl>
<dt>
<dd> 
---
title: My notebook
jupyter:
  nbformat: 4
  nbformat_minor: 5
  kernelspec:
     display_name: Python 2
     language: python
     name: python2
  language_info:
     codemirror_mode:
       name: ipython
       version: 2
     file_extension: ".py"
     mimetype: "text/x-python"
     name: "python"
     nbconvert_exporter: "python"
     pygments_lexer: "ipython2"
     version: "2.7.15"
---
#Lorem ipsum
**Lorem ipsum** dolor sit amet, consectetur adipiscing elit. Nunc luctus
bibendum felis dictum sodales.
``` code
print("hello")
```
## Pyout
``` code
from IPython.display import HTML
HTML("""
&lt;script&gt;
console.log("hello");
&lt;/script&gt;
&lt;b&gt;HTML&lt;/b&gt;
""")
```
## Image
This image ![image](myimage.png) will be
included as a cell attachment.
</dl>
 

 If you want to add cell attributes, group cells differently, or add output to code cells, then you need to include divs to indicate the structure. You can use either fenced divs or native divs for this. Here is an example:
<dl>
<dt>
<dd> 
:: :: ::{.cell.markdown}
#Lorem
    * *Lorem ipsum **dolor sit amet,
    consectetur adipiscing elit.Nunc luctus
        bibendum felis dictum sodales.:: :: ::
            :: :: ::
{
    .cell.code execution_count = 1
}
``` {.python} print("hello")
``` :::
{
    .output.stream.stdout
}
``` hello
``` :: : :: :: ::
              :: :: ::
{
    .cell.code execution_count = 2
}
``` {.python}
from IPython.display import HTML
HTML("""
&lt;script&gt;
console.log("hello");
&lt;/script&gt;
&lt;b&gt;HTML&lt;/b&gt;
""")
```
::: {
    .output.execute_result execution_count = 2}
```{=html}
&lt;script&gt;
console.log("hello");
&lt;/script&gt;
&lt;b&gt;HTML&lt;/b&gt;
hello
```
:::
::::::
</dl>
 

 If you include raw HTML or TeX in an output cell, use the [raw attribute][Extension: fenced_attribute], as shown in the last cell of the example above. Although pandoc can process &quot;bare&quot; raw HTML and TeX, the result is often interspersed raw elements and normal textual elements, and in an output cell pandoc expects a single, connected raw block. To avoid using raw HTML or TeX except when marked explicitly using raw attributes, we recommend specifying the extensions -raw_html-raw_tex+raw_attribute when translating between Markdown and ipynb notebooks. 

 Note that options and extensions that affect reading and writing of Markdown will also affect Markdown cells in ipynb notebooks. For example, --wrap=preserve will preserve soft line breaks in Markdown cells; --atx-headers will cause ATX-style headings to be used; and --preserve-tabs will prevent tabs from being turned to spaces.

<h2>SYNTAX HIGHLIGHTING</h2>

 

 Pandoc will automatically highlight syntax in fenced code blocks that are marked with a language name. The Haskell library skylighting is used for highlighting. Currently highlighting is supported only for HTML, EPUB, Docx, Ms, and LaTeX/PDF output. To see a list of language names that pandoc will recognize, type pandoc --list-highlight-languages. 

 The color scheme can be selected using the --highlight-style option. The default color scheme is pygments, which imitates the default color scheme used by the Python library pygments (though pygments is not actually used to do the highlighting). To see a list of highlight styles, type pandoc --list-highlight-styles. 

 If you are not satisfied with the predefined styles, you can use --print-highlight-style to generate a JSON .theme file which can be modified and used as the argument to --highlight-style. To get a JSON version of the pygments style, for example:
<dl>
<dt>
<dd> <pre>
pandoc --print-highlight-style pygments &gt; my.theme
</pre></dl>
 

 Then edit my.theme and use it like this:
<dl>
<dt>
<dd> <pre>
pandoc --highlight-style my.theme
</pre></dl>
 

 If you are not satisfied with the built-in highlighting, or you want highlight a language that isn't supported, you can use the --syntax-definition option to load a KDE-style XML syntax definition file. Before writing your own, have a look at KDE's repository of syntax definitions. 

 To disable highlighting, use the --no-highlight option.

<h2>CUSTOM STYLES</h2>

 

 Custom styles can be used in the docx and ICML formats.

<h3>Output</h3>

 

 By default, pandoc's docx and ICML output applies a predefined set of styles for blocks such as paragraphs and block quotes, and uses largely default formatting (italics, bold) for inlines. This will work for most purposes, especially alongside a reference.docx file. However, if you need to apply your own styles to blocks, or match a preexisting set of styles, pandoc allows you to define custom styles for blocks and text using divs and spans, respectively. 

 If you define a div or span with the attribute custom-style, pandoc will apply your specified style to the contained elements (with the exception of elements whose function depends on a style, like headings, code blocks, block quotes, or links). So, for example, using the bracketed_spans syntax,
<dl>
<dt>
<dd> 
[Get out] { custom - style = "Emphatically" }, he said.
</dl>
 

 would produce a docx file with &quot;Get out&quot; styled with character style Emphatically. Similarly, using the fenced_divs syntax,
<dl>
<dt>
<dd> 
Dickinson starts the poem simply : :: : {custom - style = "Poetry"} | A Bird came down the Walk-- -
                                        | He did not know I saw-- - :::
</dl>
 

 would style the two contained lines with the Poetry paragraph style. 

 For docx output, styles will be defined in the output file as inheriting from normal text, if the styles are not yet in your reference.docx. If they are already defined, pandoc will not alter the definition. 

 This feature allows for greatest customization in conjunction with pandoc filters. If you want all paragraphs after block quotes to be indented, you can write a filter to apply the styles necessary. If you want all italics to be transformed to the Emphasis character style (perhaps to change their color), you can write a filter which will transform all italicized inlines to inlines within an Emphasis custom-style span. 

 For docx output, you don't need to enable any extensions for custom styles to work.

<h3>Input</h3>

 

 The docx reader, by default, only reads those styles that it can convert into pandoc elements, either by direct conversion or interpreting the derivation of the input document's styles. 

 By enabling the styles extension in the docx reader (-f docx+styles), you can produce output that maintains the styles of the input document, using the custom-style class. Paragraph styles are interpreted as divs, while character styles are interpreted as spans. 

 For example, using the custom-style-reference.docx file in the test directory, we have the following different outputs: 

 Without the +styles extension:
<dl>
<dt>
<dd> <pre>
$ pandoc test/docx/custom-style-reference.docx -f docx -t markdown
This is some text.
This is text with an *emphasized* text style. And this is text with a
**strengthened** text style.
&gt; Here is a styled paragraph that inherits from Block Text.
</pre></dl>
 

 And with the extension:
<dl>
<dt>
<dd> <pre><code>
$ pandoc test / docx / custom - style - reference.docx - f docx + styles - t markdown :: : {custom - style = "First Paragraph"} This is some text.:: : :: : {custom - style = "Body Text"} This is text with an[emphasized]{custom - style = "Emphatic"} text style.And this is text with a[strengthened]{custom - style = "Strengthened"} text style.:: : :: : {custom - style = "My Block Style"} &gt; Here is a styled paragraph that inherits from Block Text.:::
</code></pre></dl>
 

 With these custom styles, you can use your input document as a reference-doc while creating docx output (see below), and maintain the same styles in your input and output files.

<h2>CUSTOM WRITERS</h2>

 

 Pandoc can be extended with custom writers written in Lua. (Pandoc includes a Lua interpreter, so Lua need not be installed separately.) 

 To use a custom writer, simply specify the path to the Lua script in place of the output format. For example:
<dl>
<dt>
<dd> <pre>
pandoc -t data/sample.lua
</pre></dl>
 

 Creating a custom writer requires writing a Lua function for each possible element in a pandoc document. To get a documented example which you can modify according to your needs, do
<dl>
<dt>
<dd> <pre>
pandoc --print-default-data-file sample.lua
</pre></dl>
 

 Note that custom writers have no default template. If you want to use --standalone with a custom writer, you will need to specify a template manually using --template or add a new default template with the name default.NAME_OF_CUSTOM_WRITER.lua to the templates subdirectory of your user data directory (see Templates).

<h2>A NOTE ON SECURITY</h2>

 

 If you use pandoc to convert user-contributed content in a web application, here are some things to keep in mind:
<dl>
<dt>1.
<dd> Although pandoc itself will not create or modify any files other than those you explicitly ask it create (with the exception of temporary files used in producing PDFs), a filter or custom writer could in principle do anything on your file system. Please audit filters and custom writers very carefully before using them.
<dt>2.
<dd> If your application uses pandoc as a Haskell library (rather than shelling out to the executable), it is possible to use it in a mode that fully isolates pandoc from your file system, by running the pandoc operations in the PandocPure monad. See the document Using the pandoc API for more details.
<dt>3.
<dd> Pandoc's parsers can exhibit pathological performance on some corner cases. It is wise to put any pandoc operations under a timeout, to avoid DOS attacks that exploit these issues. If you are using the pandoc executable, you can add the command line options +RTS -M512M -RTS (for example) to limit the heap size to 512MB.
<dt>4.
<dd> The HTML generated by pandoc is not guaranteed to be safe. If raw_html is enabled for the Markdown input, users can inject arbitrary HTML. Even if raw_html is disabled, users can include dangerous content in attributes for headings, spans, and code blocks. To be safe, you should run all the generated HTML through an HTML sanitizer.</dl>

<h2>AUTHORS</h2>

 

 Copyright 2006--2020 John MacFarlane (jgm [at] berkeley.edu). Released under the GPL, version 2 or greater. This software carries no warranty of any kind. (See COPYRIGHT for full copyright and warranty notices.) For a full list of contributors, see the file AUTHORS.md in the pandoc source code. 

 The Pandoc source code and all documentation may be downloaded from &lt;<a rel="nofollow" HREF="http://pandoc.org">http://pandoc.org</a>&gt;. 

<h2>Index</h2>


