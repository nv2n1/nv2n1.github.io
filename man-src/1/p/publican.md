---
title: "publican(1)"
name: "publican"
section: "1"
letter: "p"
url: "/docs/linux/man/1-publican/"
---

<h2 class="name">NAME</h2>
 

 publican - a DocBook XML publishing tool. 

<h2>VERSION</h2>

 This document describes publican version 1.0

<h2>SYNOPSIS</h2>

 publican &lt;command options&gt; 

 publican &lt;action&gt; &lt;action options&gt; 

 Command Options 

 <pre>
    --help              Display help message
    --man               Display the man page
    --help_actions      Display a list of valid actions
    -v                  Display the version of Publican
</pre> 

 Valid actions are: 

 <pre><code>
add_revision Add an entry to the revision history
    build Transform XML to other
    formats(pdf, html, html - single, drupal - book, etc)
    clean         Remove all temporary files and directories
    clean_ids     Run clean ids for source XML
    clean_set     Remove local copies of remote set books
    create        Create a new book, set, or article
    create_brand  Create a new brand
    create_site   Create a new WebSite in the supplied location.
    help_config   Display help text for the configuration file
    install_book  Install a book in to a WebSite.
    install_brand  Install a brand to the supplied location
    lang_stats    report PO statistics
    migrate_site  Migrate a website DataBase from Publican &lt; 3 to Publican 3.
    package       Package a language for shipping
    print_banned  Print a list of banned DocBook tags
    print_known   Print a list of QA'd DocBook tags
    print_tree    Print a tree of the xi:includes
    print_unused  Print a list of unused XML files
    print_unused_images  Print a list of unused Image files
    remove_book   Remove a book from a WebSite.
    rename        Rename a publican book
    site_stats    Report on the contents of a WebSite
    trans_drop    Snapshot the source language for use in translation.
    update_db     Add or remove database entries. Used for processing pre-build books, such as when building packages.
    update_po     Update the PO files
    update_pot    Update the POT files
    update_site   Update an existing sites templates.
</code></pre> 

 Run: 'bin/publican &lt;action&gt; --help' for details on action usage

<h2>INTERFACE</h2>

 add_revision 
&nbsp;<wbr>Add an entry to the revision history 

 
        Options:
        --help                    Display help message
        --config=s                Use a nonstandard config file
        --common_config=s         Override path to Common_Config directory
        --common_content=s        Override path to Common_Content directory
        --nocolours               Disable ANSI colourisation of logging.
        --quiet                   Disable all logging.
        --brand_dir=s             Directory to source brand files from.
        --lang=&lt;LANG&gt;             The language the XML will be written in
        --revnumber=&lt;REVNUMBER&gt;    Revision number to use for a revision.
        --date=&lt;DATE&gt;             Date to use for a revision.
        --member=&lt;MEMBER&gt;         An entry to be added to the revision. Can be specified multiple times.
        --firstname=&lt;FIRSTNAME&gt;    firstname to use for a revision.
        --surname=&lt;SURNAME&gt;       surname to use for a revision.
        --email=&lt;EMAIL&gt;           email to use for a revision.
 

 build 
&nbsp;<wbr>Transform&nbsp;<wbr><font SIZE="-1">XML</font>&nbsp;<wbr>to other formats&nbsp;<wbr>(pdf, html, html-single, drupal-book, etc) 

 
        Options:
        --help                    Display help message
        --config=s                Use a nonstandard config file
        --common_config=s         Override path to Common_Config directory
        --common_content=s        Override path to Common_Content directory
        --nocolours               Disable ANSI colourisation of logging.
        --quiet                   Disable all logging.
        --brand_dir=s             Directory to source brand files from.
        --formats=&lt;FORMATS&gt;       Comma-separated list of formats, for example: html,pdf,html-single,html-desktop,txt,epub
        --langs=&lt;LANGS&gt;           Comma-separated list of languages, for example: en-US,de-DE,all
        --publish                 Set up built content for publishing
        --embedtoc                Embed the web site TOC object in the generated HTML
        --distributed_set         This flag tells publican the data being processed is a distributed set. Note: do not use distributed_set on the command line. Publican uses this flag when calling itself to process distributed sets. This is the only safe way this flag can be used.
        --novalid                 Do not run the DTD validation
        --src_dir=&lt;SRC_DIR&gt;       Directory to source publican files from.
        --pdftool=&lt;PDFTOOL&gt;       Override the tool to use when creating PDFs. Valid options are wkhtmltopdf and fop.
        --pub_dir=&lt;PUB_DIR&gt;       Directory to publish files to. Defaults to publish.
 

 clean 
&nbsp;<wbr>Remove all temporary files and directories 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--pub_dir = &lt;PUB_DIR&gt; Directory to publish files to.Defaults to publish.
 

 clean_ids 
&nbsp;<wbr>Run clean ids for source&nbsp;<wbr><font SIZE="-1">XML</font> 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.
 

 clean_set 
&nbsp;<wbr>Remove local copies of remote set books 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.
 

 create 
&nbsp;<wbr>Create a new book, set, or article 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--name = &lt;NAME&gt; The name of the book, article, set, or brand-- version = &lt;VERSION&gt; The version of the product-- edition = &lt;EDITION&gt; The edition of the book, article, or set-- product = &lt;PRODUCT&gt; The name of the product-- brand = &lt;BRAND&gt; The brand to use-- lang = &lt;LANG&gt; The language the XML will be written in-- type = &lt;TYPE&gt; The type(book, article, or set)
 

 create_brand 
&nbsp;<wbr>Create a new brand 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--name = &lt;NAME&gt; The name of the book, article, set, or brand-- lang = &lt;LANG&gt; The language the XML will be written in
 

 create_site 
&nbsp;<wbr>Create a new WebSite in the supplied location. 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--site_config = &lt;SITE_CONFIG&gt; WebSite configuration file to use or create.--db_file = &lt;DB_FILE&gt; Override default database file.--toc_path = &lt;TOC_PATH&gt; Override the default TOC path.--tmpl_path = &lt;TMPL_PATH&gt; Override the default template path.--lang = &lt;LANG&gt; The language the XML will be written in
 

 help_config 
&nbsp;<wbr>Display help text for the configuration file 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.
 

 install_book 
&nbsp;<wbr>Install a book in to a WebSite. 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--site_config = &lt;SITE_CONFIG&gt; WebSite configuration file to use or create.--lang = &lt;LANG&gt; The language the XML will be written in
 

 install_brand 
&nbsp;<wbr>Install a brand to the supplied location 

 
        Options:
        --help                    Display help message
        --config=s                Use a nonstandard config file
        --common_config=s         Override path to Common_Config directory
        --common_content=s        Override path to Common_Content directory
        --nocolours               Disable ANSI colourisation of logging.
        --quiet                   Disable all logging.
        --brand_dir=s             Directory to source brand files from.
        --path=&lt;PATH&gt;             /path/to/install/to
        --web                     Install the web content for a brand.
        --pub_dir=&lt;PUB_DIR&gt;       Directory to publish files to. Defaults to publish.
 

 lang_stats 
&nbsp;<wbr>report&nbsp;<wbr><font SIZE="-1">PO</font>&nbsp;<wbr>statistics 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--lang = &lt;LANG&gt; The language the XML will be written in
 

 migrate_site 
&nbsp;<wbr>Migrate a website DataBase from Publican&nbsp;<wbr>&lt;&nbsp;<wbr>3 to Publican 3. 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--site_config = &lt;SITE_CONFIG&gt; WebSite configuration file to use or create.
 

 package 
&nbsp;<wbr>Package a language for shipping 

 
        Options:
        --help                    Display help message
        --config=s                Use a nonstandard config file
        --common_config=s         Override path to Common_Config directory
        --common_content=s        Override path to Common_Content directory
        --nocolours               Disable ANSI colourisation of logging.
        --quiet                   Disable all logging.
        --brand_dir=s             Directory to source brand files from.
        --lang=&lt;LANG&gt;             The language the XML will be written in
        --desktop                 Create desktop instead of web package
        --brew                    Push SRPM to brew
        --scratch                 Use scratch instead of tag build
        --short_sighted           Create package without using version in package name
        --binary                  Build binary rpm when running package
        --wait                    Wait for brew to finish building
        --pub_dir=&lt;PUB_DIR&gt;       Directory to publish files to. Defaults to publish.
 

 print_banned 
&nbsp;<wbr>Print a list of banned DocBook tags 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.
 

 print_known 
&nbsp;<wbr>Print a list of&nbsp;<wbr><font SIZE="-1">QA</font>'d DocBook tags 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.
 

 print_tree 
&nbsp;<wbr>Print a tree of the xi:includes 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.
 

 print_unused 
&nbsp;<wbr>Print a list of unused&nbsp;<wbr><font SIZE="-1">XML</font>&nbsp;<wbr>files 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.
 

 print_unused_images 
&nbsp;<wbr>Print a list of unused Image files 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.
 

 remove_book 
&nbsp;<wbr>Remove a book from a WebSite. 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--site_config = &lt;SITE_CONFIG&gt; WebSite configuration file to use or create.--lang = &lt;LANG&gt; The language the XML will be written in
 

 rename 
&nbsp;<wbr>Rename a publican book 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--name = &lt;NAME&gt; The name of the book, article, set, or brand-- product = &lt;PRODUCT&gt; The name of the product-- version = &lt;VERSION&gt; The version of the product
 

 site_stats 
&nbsp;<wbr>Report on the contents of a WebSite 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--site_config = &lt;SITE_CONFIG&gt; WebSite configuration file to use or create.
 

 trans_drop 
&nbsp;<wbr>Snapshot the source language for use in translation. 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.
 

 update_db 
&nbsp;<wbr>Add or remove database entries. Used for processing pre-build books, such as when building packages. 

 
        Options:
        --help                    Display help message
        --config=s                Use a nonstandard config file
        --common_config=s         Override path to Common_Config directory
        --common_content=s        Override path to Common_Content directory
        --nocolours               Disable ANSI colourisation of logging.
        --quiet                   Disable all logging.
        --brand_dir=s             Directory to source brand files from.
        --site_config=&lt;SITE_CONFIG&gt;    WebSite configuration file to use or create.
        --add                     Add a database entry
        --del                     Delete a database entry
        --lang=&lt;LANG&gt;             The language the XML will be written in
        --product=&lt;PRODUCT&gt;       The name of the product
        --version=&lt;VERSION&gt;       The version of the product
        --name=&lt;NAME&gt;             The name of the book, article, set, or brand
        --formats=&lt;FORMATS&gt;       Comma-separated list of formats, for example: html,pdf,html-single,html-desktop,txt,epub
        --subtitle=&lt;SUBTITLE&gt;     Sub title for a book
        --abstract=&lt;ABSTRACT&gt;     Abstract for a book
        --product_label=&lt;PRODUCT_LABEL&gt;    product label for a book
        --version_label=&lt;VERSION_LABEL&gt;    version label for a book
        --name_label=&lt;NAME_LABEL&gt;    name label for a book
        --sort_order=&lt;SORT_ORDER&gt;    Order to sort a book
 

 update_po 
&nbsp;<wbr>Update the&nbsp;<wbr><font SIZE="-1">PO</font>&nbsp;<wbr>files 

 
        Options:
        --help                    Display help message
        --config=s                Use a nonstandard config file
        --common_config=s         Override path to Common_Config directory
        --common_content=s        Override path to Common_Content directory
        --nocolours               Disable ANSI colourisation of logging.
        --quiet                   Disable all logging.
        --brand_dir=s             Directory to source brand files from.
        --langs=&lt;LANGS&gt;           Comma-separated list of languages, for example: en-US,de-DE,all
        --msgmerge                Use gettext's msgmerge for POT/PO merging.
        --firstname=&lt;FIRSTNAME&gt;    firstname to use for a revision.
        --surname=&lt;SURNAME&gt;       surname to use for a revision.
        --email=&lt;EMAIL&gt;           email to use for a revision.
 

 update_pot 
&nbsp;<wbr>Update the&nbsp;<wbr><font SIZE="-1">POT</font>&nbsp;<wbr>files 

 
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.
 

 update_site 
&nbsp;<wbr>Update an existing sites templates. 

 <pre><code>
Options : --help Display help message-- config = s Use a nonstandard config file-- common_config = s Override path to Common_Config directory-- common_content = s Override path to Common_Content directory-- nocolours Disable ANSI colourisation of logging.--quiet Disable all logging.--brand_dir = s Directory to source brand files from.--site_config = &lt;SITE_CONFIG&gt; WebSite configuration file to use or create.
</code></pre>

<h2>CONFIGURATION AND ENVIRONMENT</h2>

 Publican requires access to Apache <font SIZE="-1">FOP</font> for creating <font SIZE="-1">PDF</font> files.

<h2>DEPENDENCIES</h2>

 Archive::Tar Archive::Zip Carp Config::Simple Cwd <font SIZE="-1">DBI</font> DateTime DateTime::Format::DateParse Devel::Cover Encode File::Basename File::Copy::Recursive File::Find File::Find::Rule File::HomeDir File::Inplace File::Path File::Spec File::Which File::pushd Getopt::Long HTML::FormatText HTML::FormatText::WithLinks HTML::FormatText::WithLinks::AndTables HTML::TreeBuilder I18N::LangTags::List IO::String List::MoreUtils List::Util Locale::Language Locale::Maketext::Gettext Locale::PO Module::Build Pod::Usage Sort::Versions String::Similarity Syntax::Highlight::Engine::Kate Template Template::Constants Term::ANSIColor Test::More Test::Pod Test::Pod::Coverage Text::CSV_XS Text::Wrap Time::localtime XML::LibXML XML::LibXSLT XML::Simple XML::TreeBuilder

<h2>INCOMPATIBILITIES</h2>

 None reported.

<h2>BUGS AND LIMITATIONS</h2>

 No bugs have been reported. 

 Please report any bugs or feature requests to <tt>&quot;publican-list [at] redhat.com&quot;</tt>, or through the web interface at &lt;<a rel="nofollow" HREF="https://bugzilla.redhat.com/bugzilla/enter_bug.cgi?product=Publican">https://bugzilla.redhat.com/bugzilla/enter_bug.cgi?product=Publican</a>&amp;component=publican&amp;version=v3.2.0&gt;.

<h2>AUTHOR</h2>

 Jeff Fearn <tt>&quot;&lt;jfearn [at] redhat.com&gt;&quot;</tt> 

<h2>Index</h2>


