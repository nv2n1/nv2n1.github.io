---

title: "libraptor(3)"
name: "libraptor"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libraptor/"
description: "libraptor – Raptor RDF parser and serializer library"
---

<p> libraptor - Raptor RDF parser and serializer library </p>
<h2>SYNOPSIS</h2>
<pre><code>
 #include &lt;raptor.h&gt; 




 raptor_init(); 


 raptor_parser *  p  =raptor_new_parser(rdfxml); 


 raptor_set_statement_handler(  p  ,  NULL  ,  print_triples  ); 


 raptor_uri *  file_uri  =raptor_new_uri(http://example.org/); 


 raptor_parse_file(  p  ,  file_uri  ,  base_uri  ); 


 raptor_parse_uri(  p  ,  uri  ,  NULL  ); 


 raptor_free_parser(  p  ); 


 raptor_free_uri(  file_uri  ); 


 raptor_finish(); 


 cc file.c -lraptor 


</code></pre>
<h2>DESCRIPTION</h2>
<p> The <i>Raptor</i> library provides a high-level interface to a set of parsers and serializers that generate Resource Description Framework (RDF) triples by parsing syntaxes or serialize the triples into syntaxes. </p>
<p> The supported parsing syntaxes are RDF/XML, N-Triples, Turtle, RSS tag soup including Atom 0.3 and the serializing syntaxes are RDF/XML, N-Triples and RSS 1.0. The RDF/XML parser can use either <i>expat</i> or <i>libxml</i> XML parsers for providing the SAX event stream. The library functions are arranged in an object-oriented style with constructors, destructors and method calls. The statements and error messages are delivered via callback functions. </p>
<p> Raptor contains a URI-reference parsing and resolving (not retrieval) class (raptor_uri) sufficient for dealing with URI-references inside RDF. This functionality is modular and can be transparently replaced with another existing and compatible URI implementation. </p>
<p> It also provides a URI-retrieval class (raptor_www) for wrapping existing library such as libcurl, libxml2 or BSD libfetch that provides full or partial retrieval of data from URIs and an I/O stream abstraction (raptor_iostream) for supportin serializing to a variety of outputs. </p>
<p> Raptor uses Unicode strings for RDF literals and URIs and preserves them throughout the library. It uses the UTF-8 encoding of Unicode at the API for passing in or returning Unicode strings. It is intended that the preservation of Unicode for URIs will support Internationalized Resource Identifiers (IRIs) which are still under development and standardisation.  </p>
<h2>LIBRARY INITIALISATION AND CLEANUP</h2>
<dl>
<dt><code>raptor_init()</code></dt>
<dd>  </dd>
<dt><code>raptor_finish()</code></dt>
<dd> <p> Initialise and cleanup the library. These must be called before any raptor class such as raptor_parser, raptor_uri is created or used. </p>
 </dd></dl>
<h2>PARSER CLASS</h2>
<p> This class provides the functionality of turning syntaxes into RDF triples - RDF parsing.  </p>
<h2>PARSER CONSTRUCTORS</h2>
<dl>
<dt><code>raptor_parser* raptor_new_parser(name)</code></dt>
<dd> <p> Create a new raptor parser object for the parser with name <i>name</i> currently either &quot;rdfxml&quot;, &quot;turtle&quot; or &quot;rss-tag-soup&quot; for the RSS Tag Soup parser. </p>
 </dd>
<dt><code>raptor_parser* raptor_new_parser_for_content(raptor_uri *</code><i>uri</i>, const char *<i>mime_type</i>, const unsigned char *<i>buffer</i>, size_t <i>len</i>, const unsigned char *<i>identifier</i>)</dt>
<dd> <p> Create a new raptor parser object for a syntax identified by URI <i>uri</i>, MIME type <i>mime_type</i>, some initial content <i>buffer</i> of size <i>len</i> or content with identifier <i>identifier</i>. See the raptor_guess_parser_name description for further details. </p>
 </dd></dl>
<h2>PARSER DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_parser(raptor_parser *</code><i>parser</i><code>)</code></dt>
<dd> <p> Destroy a Raptor parser object. </p>
 </dd></dl>
<h2>PARSER MESSAGE CALLBACK METHODS</h2>
<p> Several methods can be registered for the parser that return a variable-argument message in the style of <a href="/docs/linux/man/3-printf/">printf</a>(3). These also return a <i>raptor_locator</i> that can contain URI, file, line, column and byte counts of where the message is about. This structure can be used with the raptor_format_locator, raptor_print_locator functions below or the structures fields directly, which are defined in raptor.h </p>
<dl>
<dt><code>void raptor_set_fatal_error_handler(raptor_parser* </code><i>parser, void *user_data, raptor_message_handler handler)</i></dt>
<dd> <p> Set the parser fatal error handler callback. </p>
 </dd>
<dt><code>void raptor_set_error_handler(raptor_parser* </code><i>parser</i><code>, void *</code><i>user_data</i><code>, raptor_message_handler </code><i>handler</i><code>)</code></dt>
<dd> <p> Set the parser non-fatal error handler callback. </p>
 </dd>
<dt><code>void raptor_set_warning_handler(raptor_parser* </code><i>parser</i><code>, void *</code><i>user_data</i><code>, raptor_message_handler </code><i>handler</i><code>)</code></dt>
<dd> <p> Set the parser warning message handler callback. </p>
 </dd>
<dt><code>raptor_set_namespace_handler(raptor_parser* </code><i>parser</i>, void* <i>user_data</i>, raptor_namespace_handler <i>handler</i>)</dt>
<dd> <p> Set the namespace declaration handler callback. </p>
 </dd></dl>
<h2>PARSER STATEMENT CALLBACK METHOD</h2>
<p> The parser allows the registration of a callback function to return the statements to the application. </p>
<dl>
<dt><code>void raptor_set_statement_handler(raptor_parser* </code><i>parser</i><code>, void *</code><i>user_data</i><code>, raptor_statement_handler </code><i>handler</i><code>)</code></dt>
<dd> <p> Set the statement callback function for the parser. The <i>raptor_statement</i> structure is defined in raptor.h and includes fields for the subject, predicate, object of the statements along with their types and for literals, language and datatype. </p>
 </dd></dl>
<h2>PARSER PARSING METHODS</h2>
<p> These methods perform the entire parsing in one method. Statements warnings, errors and fatal errors are delivered via the registered statement, error etc. handler functions. </p>
<p> In both of these methods, the base URI is required for the RDF/XML parser (name &quot;rdfxml&quot;) and Turtle parser (name &quot;turtle&quot;). The N-Triples parser (name &quot;ntriples&quot;) or RSS Tag Soup parser (name &quot;rss-tag-soup&quot;) do not use this. </p>
<dl>
<dt><code>int raptor_parse_file(raptor_parser* </code><i>parser</i><code>, raptor_uri *</code><i>uri</i><code>, raptor_uri *</code><i>base_uri</i><code>)</code></dt>
<dd> <p> Parse the given filename (a URI like file:filename) according to the optional base URI <i>base_uri</i>. If <i>uri</i> is NULL, read from standard input and <i>base_uri</i> is then required. </p>
 </dd>
<dt><code>int raptor_parse_file_stream(raptor_parser* </code><i>parser</i><code>, FILE* </code><i>stream</i><code>, const char* </code><i>filename</i><code>, raptor_uri *</code><i>base_uri</i><code>)</code></dt>
<dd> <p> Parse the given C FILE* stream according to the base URI <i>base_uri</i> (required). <i>filename</i> is optional and if given, is used for error messages via the raptor_locator structure. </p>
 </dd>
<dt><code>int raptor_parse_uri(raptor_parser* </code><i>parser</i><code>, raptor_uri* </code><i>uri</i><code>, raptor_uri *</code><i>base_uri</i><code>)</code></dt>
<dd> <p> Parse the URI according to the base URI <i>base_uri</i>, or NULL if not needed. If no base URI is given, the <i>uri</i> is used. This method depends on the raptor_www subsystem (see <code>WWW Class</code> section below) and an existing underlying URI retrieval implementation such as libcurl, libxml or BSD libfetch to retrieve the content. </p>
 </dd></dl>
<h2>PARSER CHUNKED PARSING METHODS</h2>
<p> These methods perform the parsing in parts by working on multiple chunks of memory passed by the application. Statements warnings, errors and fatal errors are delivered via the registered statement, error etc. handler functions. </p>
<dl>
<dt><code>int raptor_start_parse(raptor_parser* </code><i>parser</i><code>, const char *</code><i>uri</i><code>)</code></dt>
<dd> <p> Start a parse of chunked content with the base URI <i>uri</i> or NULL if not needed. The base URI is required for the RDF/XML parser (name &quot;rdfxml&quot;) and Turtle parser (name &quot;turtle&quot;). The N-Triples parser (name &quot;ntriples&quot;) or RSS Tag Soup parser (name &quot;rss-tag-soup&quot;) do not use this. </p>
 </dd>
<dt><code>int raptor_parse_chunk(raptor_parser* </code><i>parser</i><code>, const unsigned char *buffer, size_t </code><i>len</i><code>, int </code><i>is_end</i><code>)</code></dt>
<dd> <p> Parse the memory at <i>buffer</i> of size <i>len</i> returning statements via the statement handler callback. If <i>is_end</i> is non-zero, it indicates the end of the parsing stream. This method can only be called after <code>raptor_start_parse()</code>. </p>
 </dd></dl>
<h2>PARSER UTILITY METHODS</h2>
<dl>
<dt><code>const char* raptor_get_mime_type(raptor_parser* </code><i>rdf_parser</i><code>)</code></dt>
<dd> <p> Return the MIME type for the parser. </p>
 </dd>
<dt><code>void raptor_set_parser_strict(raptor_parser *</code><i>parser</i><code>, int </code><i>is_strict</i><code>)</code></dt>
<dd> <p> Set the parser to strict (<i>is_strict</i> not zero) or lax (default) mode. The detail of the strictness can be controlled by raptor_set_feature. </p>
 </dd>
<dt><code>int raptor_set_feature(raptor_parser *</code><i>parser</i><code>, raptor_feature </code><i>feature</i><code>, int </code><i>value</i><code>)</code></dt>
<dd> <p> Set a parser feature <i>feature</i> to a particular <i>value</i>. Returns non 0 on failure or if the feature is unknown. The current defined parser features are: <br />
&nbsp;<wbr>&nbsp;<wbr><i>Feature&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Values</i> <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ALLOW_BAGID</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ALLOW_NON_NS_ATTRIBUTES</code>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ALLOW_OTHER_PARSETYPES</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ALLOW_RDF_TYPE_RDF_LIST</code>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ASSUME_IS_RDF</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_CHECK_RDF_ID</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_HTML_LINK</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_HTML_TAG_SOUP</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_MICROFORMATS</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_NON_NFC_FATAL</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_NORMALIZE_LANGUAGE</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_NO_NET</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_RELATIVE_URIS</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_SCANNING</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WARN_OTHER_PARSETYPES</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WWW_TIMEOUT</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Integer <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WWW_HTTP_CACHE_CONTROL</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WWW_HTTP_USER_AGENT</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String If the <i>allow_bagid</i> feature is true (default true) then the RDF/XML parser will support the rdf:bagID attribute that was removed from the RDF/XML language when it was revised. This support may be removed in future. If the <i>allow_non_ns_attributes</i> feature is true (default true), then the RDF/XML parser will allow non-XML namespaced attributes to be accepted as well as rdf: namespaced ones. For example, &#8216;about&#8217; and &#8216;ID&#8217; will be interpreted as if they were rdf:about and rdf:ID respectively. If the <i>allow_other_parsetypes</i> feature is true (default true) then the RDF/XML parser will allow unknown parsetypes to be present and will pass them on to the user. Unimplemented at present. If the <i>allow_rdf_type_rdf_list</i> feature is true (default false) then the RDF/XML parser will generate the idList rdf:type rdf:List triple in the handling of rdf:parseType=&quot;Collection&quot;. This triple was removed during the revising of RDF/XML after collections were initially added. If the <i>assume_is_rdf</i> feature is true (default false), then the RDF/XML parser will assume the content is RDF/XML, not require that rdf:RDF root element, and immediately interpret the content as RDF/XML. If the <i>check_rdf_id</i> feature is true (default true) then rdf:ID values will be checked for duplicates and cause an error if found. if the <i>html_link</i> feature is true (default true), look for head &amp;lt;link&amp;gt; to type rdf/xml for GRDDL parser If the <i>html_tag_soup</i> feature is true (default true), use a lax HTML parser if an XML parser fails when read HTML for GRDDL parser. If the <i>microformats</i> feature is true (default true), look for microformats for GRDDL parser. If the <i>non_nfc_fatal</i> feature is true (default false) then illegal Unicode Normal Form C in literals will give a fatal error, otherwise it gives a warning. If the <i>normalize_language</i> feature is true (default true) then XML language values such as from xml:lang will be normalized to lowercase. If the <i>no_net</i> feature is true (default false) then network requests are denied. If the <i>scanning</i> feature is true (default false), then the RDF/XML parser will look for embedded rdf:RDF elements inside the XML content, and not require that the XML start with an rdf:RDF root element. If the <i>www_timeout</i> feature is set to an integer larger than 0, it sets the timeout in seconds for internal WWW URI requests for the GRDDL parser. If the <i>www_http_cache_control</i> feature is set to a string value (default none), it is sent as the value of the HTTP Cache-Control: header in requests. If the <i>www_http_user_agent</i> feature is set to a string value, it is sent as the value of the HTTP User-Agent: header in requests. </p>
 </dd>
<dt><code>raptor_parser_set_feature_string(raptor_parser *</code><i>parser</i>, raptor_feature <i>feature</i>, const unsigned char *<i>value</i>)</dt>
<dd> <p> Set a parser feature <i>feature</i> to a particular string <i>value</i>. Returns non 0 on failure or if the feature is unknown. The current defined parser features are given in <code>raptor_set_feature</code> and at present only take integer values. If an integer value feature is set with this function, <i>value</i> is interpreted as an integer and then that value is used. </p>
 </dd>
<dt><code>int raptor_get_feature(raptor_parser* </code><i>parser</i><code>, raptor_feature </code><i>feature</i><code>)</code></dt>
<dd> <p> Get parser feature integer values. The allowed <i>feature</i> values and types are given under <code>raptor_features_enumerate</code>. </p>
 </dd>
<dt><code>const unsigned char* raptor_parser_get_feature_string(raptor_parser *</code><i>parser</i>, raptor_feature <i>feature</i>)</dt>
<dd> <p> Get parser feature string values. The allowed <i>feature</i> values and types are given under <code>raptor_features_enumerate</code>. </p>
 </dd>
<dt><code>unsigned int raptor_get_feature_count(void)</code></dt>
<dd> <p> Get the count of features defined. Prefered to the compile time-only symbol <code>RAPTOR_FEATURE_LAST</code> which returns the maximum value, not the count. Added raptor_get_need_base_uri </p>
 </dd>
<dt><code>int raptor_feature_value_type(const raptor_feature feature)</code></dt>
<dd> <p> Get a raptor feature value tyype - integer or string. </p>
 </dd>
<dt><code>raptor_locator* raptor_get_locator(raptor_parser* </code><i>rdf_parser</i><code>)</code></dt>
<dd> <p> Return the current raptor_locator object for the parser. This is a public structure defined in raptor.h that can be used directly, or formatted via raptor_print_locator. </p>
 </dd>
<dt><code>void raptor_get_name(raptor_parser *</code><i>parser</i><code>)</code></dt>
<dd> <p> Return the string short name for the parser. </p>
 </dd>
<dt><code>void raptor_get_label(raptor_parser *</code><i>parser</i><code>)</code></dt>
<dd> <p> Return a string label for the parser. </p>
 </dd>
<dt><code>void raptor_set_default_generate_id_parameters(raptor_parser* </code><i>rdf_parser</i><code>, char *</code><i>prefix</i><code>, int </code><i>base</i><code>)</code></dt>
<dd> <p> Control the default method for generation of IDs for blank nodes and bags. The method uses a short string <i>prefix</i> and an integer <i>base</i> to generate the identifier which is not guaranteed to be a strict concatenation. If <i>prefix</i> is NULL, the default is used. If base is less than 1, it is initialised to 1. </p>
 </dd>
<dt><code>void raptor_set_generate_id_handler(raptor_parser* </code><i>parser</i><code>, void *</code><i>user_data</i><code>, raptor_generate_id_handler </code><i>handler</i><code>)</code></dt>
<dd> <p> Allow full customisation of the generated IDs by setting a callback <i>handler</i> and associated <i>user_data</i> that is called whenever a blank node or bag identifier is required. The memory returned is deallocated inside raptor. Some systems require this to be allocated inside the same library, in which case the <code>raptor_alloc_memory</code> function may be useful. </p>
 </dd>
<dt><code>void raptor_parser_set_uri_filter(raptor_parser* </code><i>parser</i>, raptor_uri_filter_func <i>filter</i>, void* <i>user_data</i>)</dt>
<dd> <p> Set the URI filter function <i>filter</i> for URIs retrieved during parsing by the the raptor_parser. </p>
 </dd>
<dt><code>int raptor_get_need_base_uri(raptor_parser* </code><i>rdf_parser</i>)</dt>
<dd> <p> Get a boolean whether this parser needs a base URI to start parsing. </p>
 </dd>
<dt><code>unsigned char* raptor_parser_generate_id(raptor_parser* </code><i>rdf_parser</i>, raptor_genid_type <i>type</i>)</dt>
<dd> <p> Generate an ID for a parser of type <i>type</i>, either <code>RAPTOR_GENID_TYPE_BNODEID</code> or <code>RAPTOR_GENID_TYPE_BAGID</code>. This uses any configuration set by <code>raptor_set_generate_id_handler</code>. </p>
 </dd>
<dt><code>void raptor_set_graph_handler(raptor_parser* </code><i>parser</i>, void* <i>user_data</i>, raptor_graph_handler <i>handler</i>)</dt>
<dd> <p> Set the graph handler callback. </p>
 </dd></dl>
<h2>PARSER UTILITY FUNCTIONS</h2>
<dl>
<dt><code>int raptor_parsers_enumerate(const unsigned int </code><i>counter</i><code>, const char **</code><i>name</i><code>, const char **</code><i>label</i><code>)</code></dt>
<dd> <p> Return the parser name/label for a parser with a given integer counter, returning non-zero if no such parser at that offset exists. The counter should start from 0 and be incremented by 1 until the function returns non-zero. </p>
 </dd>
<dt><code>int raptor_syntaxes_enumerate(const unsigned int </code><i>counter</i><code>, const char **name, const char **</code><i>label</i><code>, const char **</code><i>mime_type</i><code>, const unsigned char **</code><i>uri-string</i><code>)</code></dt>
<dd> <p> Return the name, label, mime type or URI string (all optional) for a parser syntax with a given integer counter, returning non-zero if no such syntax parser at that offset exists. The counter should start from 0 and be incremented by 1 until the function returns non-zero. </p>
 </dd>
<dt><code>int raptor_features_enumerate(const raptor_feature </code><i>feature</i>, const char **<i>name</i>, raptor_uri **<i>uri</i>, const char **<i>label</i>)</dt>
<dd> <p> Return the name, URI, string label (all optional) for a parser <i>feature</i>, returning non-zero if no such feature exists. Raptor features have URIs that are constructed from the URI <i><a rel="nofollow" href="http://feature.librdf.org/raptor-">http://feature.librdf.org/raptor-</a></i> and the <i>name</i> so for example feature <i>scanForRDF</i> has URI <i><a rel="nofollow" href="http://feature.librdf.org/raptor-scanForRDF">http://feature.librdf.org/raptor-scanForRDF</a></i> </p>
 </dd>
<dt><code>int raptor_syntax_name_check(const char *</code><i>name</i>)</dt>
<dd> <p> Check <i>name</i> is a known syntax name. </p>
 </dd>
<dt><code>const char* raptor_guess_parser_name(raptor_uri *</code><i>uri</i>, const char *<i>mime_type</i>, const unsigned char *<i>buffer</i>, size_t <i>len</i>, const unsigned char *<i>identifier</i>)</dt>
<dd> <p> Guess a parser name for a syntax identified by URI <i>uri</i>, MIME type <i>mime_type</i>, some initial content <i>buffer</i> of size <i>len</i> or with content identifier <i>identifier</i>. All of these parameters are optional and only used if not NULL. The parser is chosen by scoring the hints that are given. </p>
 </dd>
<dt><code>raptor_feature raptor_feature_from_uri(raptor_uri *</code><i>uri</i>)</dt>
<dd> <p> Turn a URI <i>uri</i> into a raptor feature identifier, or &lt;0 if the feature is unknown. The URIs are described below raptor_set_feature. </p>
 </dd></dl>
<h2>STATEMENT UTILITY FUNCTIONS</h2>
<dl>
<dt><code>int raptor_statement_compare(const raptor_statement *</code><i>s1</i>, const raptor_statement *<i>s2</i>)</dt>
<dd> <p> Compare two statements and return an ordering between them. </p>
 </dd>
<dt><code>void raptor_print_statement(const raptor_statement* const </code><i>statement</i><code>, FILE *</code><i>stream</i><code>)</code></dt>
<dd> <p> Print a raptor statement object in a simple format for debugging only. The format of this output is not guaranteed to remain the same between releases. </p>
 </dd>
<dt><code>void raptor_print_statement_as_ntriples(const raptor_statement* </code><i>statement</i><code>, FILE *</code><i>stream</i><code>)</code></dt>
<dd> <p> Print a raptor statement object in N-Triples format, using all the escapes as defined in <a rel="nofollow" href="http://www.w3.org/TR/rdf-testcases/#ntriples">http://www.w3.org/TR/rdf-testcases/#ntriples</a> </p>
 </dd>
<dt><code>raptor_statement_part_as_counted_string(const void *</code><i>term</i><code>, raptor_identifier_type </code><i>type</i><code>, raptor_uri* </code><i>literal_datatype</i><code>, const unsigned char *</code><i>literal_language</i><code>, size_t* </code><i>len_p</i><code>)</code></dt>
<dd>  </dd>
<dt><code>char* raptor_statement_part_as_string(const void *</code><i>term</i><code>, raptor_identifier_type </code><i>type</i><code>, raptor_uri* </code><i>literal_datatype</i><code>, const unsigned char *</code><i>literal_language</i><code>)</code></dt>
<dd> <p> Turns part of raptor statement into N-Triples format, using all the escapes as defined in <a rel="nofollow" href="http://www.w3.org/TR/rdf-testcases/#ntriples">http://www.w3.org/TR/rdf-testcases/#ntriples</a> The part (subject, predicate, object) of the raptor_statement is passed in as <i>term</i>, the part type (subject_type, predicate_type, object_type) is passed in as <i>type</i>. When the part is a literal, the <i>literal_datatype</i> and <i>literal_language</i> fields are set, otherwise NULL (usually object_datatype, object_literal_language). </p>
 </dd>
<dd> <p> If <code>raptor_statement_part_as_counted_string</code> is used, the length of the returned string is stored in *<i>len_p</i> if not NULL. </p>
 </dd></dl>
<h2>LOCATOR UTILITY FUNCTIONS</h2>
<dl>
<dt><code>int raptor_format_locator(char *</code><i>buffer</i><code>, size_t </code><i>length</i><code>, raptor_locator* </code><i>locator</i><code>)</code></dt>
<dd> <p> This method takes a <i>raptor_locator</i> object as passed to an error, warning or other handler callback and formats it into the <i>buffer</i> of size <i>length</i> bytes. If <i>buffer</i> is NULL or <i>length</i> is insufficient for the size of the formatted locator, returns the number of additional bytes required in the buffer to write the locator. </p>
<p> In particular, if this form is used: <br />
&nbsp;<wbr>&nbsp;<wbr>length=raptor_format_locator(NULL, 0, locator) it will return in <i>length</i> the size of a buffer that can be allocated for <i>locator</i> and a second call will perform the formatting: <br />
&nbsp;<wbr>&nbsp;<wbr>raptor_format_locator(buffer, length, locator) </p>
 </dd>
<dt><code>void raptor_print_locator(FILE *</code><i>stream</i><code>, raptor_locator* </code><i>locator</i><code>)</code></dt>
<dd> <p> This method takes a <i>raptor_locator</i> object as passed to an error, warning or other handler callback, formats and prints it to the given stdio <i>stream</i>. </p>
 </dd>
<dt><code>int raptor_locator_line(raptor_locator *locator)</code></dt>
<dd> <p> Returns the line number in a locator structure or &lt;0 if not available. </p>
 </dd>
<dt><code>int raptor_locator_column(raptor_locator *locator)</code></dt>
<dd> <p> Returns the column number in a locator structure or &lt;0 if not available. </p>
 </dd>
<dt><code>int raptor_locator_byte(raptor_locator *locator)</code></dt>
<dd> <p> Returns the byte offset in a locator structure or &lt;0 if not available. </p>
 </dd>
<dt><code>const char * raptor_locator_file(raptor_locator *locator)</code></dt>
<dd> <p> Returns the filename in a locator structure or NULL if not available. Note the returned pointer is to a shared string that must be copied if needed. </p>
 </dd>
<dt><code>const char * raptor_locator_uri(raptor_locator *locator)</code></dt>
<dd> <p> Returns the URI string in a locator structure or NULL if not available. Note this does not return a raptor_uri* pointer and the returned pointer is to a shared string that must be copied if needed. </p>
 </dd></dl>
<h2>N-TRIPLES UTILITY FUNCTIONS</h2>
<dl>
<dt><code>void raptor_print_ntriples_string(FILE* </code><i>stream</i><code>, const char* </code><i>string</i><code>, const char </code><i>delim</i><code>)</code></dt>
<dd> <p> This is a standalone function that prints the given string according to N-Triples escaping rules, expecting to be terminated by delimiter <i>delim</i> which is usually either &#8216;, dq or &lt;. If a null delimiter \0 is given, no extra escaping is performed. </p>
 </dd>
<dt><code>int raptor_iostream_write_string_ntriples(raptor_iostream *</code><i>iostr</i>, const unsigned char *<i>string</i>, size_t <i>len</i>, const char <i>delim</i>)</dt>
<dd> <p> Write an N-Triples encoded version of the given string to iostream <i>iostr</i>. If <i>delim</i> is given, that is the ending delimeter of the encoded string and it will be escaped in the output as appropriate. Useful delim values are &#8216;, dq and &gt;. If a null delimiter \0 is given, no extra escaping is performed. </p>
 </dd>
<dt>int raptor_iostream_write_string_python(raptor_iostream *<i>iostr</i>, const unsigned char *<i>string</i>, size_t <i>len</i>, const char <i>delim</i>, int <i>flags</i>)</dt>
<dd> <p> Write <i>string</i> encoded to an iostream according to the delimeter <i>delim</i> and encoding flags. The <i>flag</i> value selects formatting according to the appropriate Python-related languages such as N-Triples (0), Turtle (1), Turtle long quoted string (2), JSON (3). </p>
 </dd>
<dt><code>void raptor_iostream_write_statement_ntriples(raptor_iostream* iostr, const raptor_statement *statement)</code></dt>
<dd> <p> Write an N-Triples encoded version of the raptor_statement <i>statement</i> to iostream <i>iostr</i>. </p>
 </dd>
<dt><code>void raptor_iostream_write_string_turtle(raptor_iostream* </code><i>iostr</i>, const unsigned char* <i>string</i>, size_t <i>len</i>)</dt>
<dd> <p> DEPRECATED in 1.4.17 - use raptor_iostream_write_string_python instead. Write an UTF-8 <i>string</i> of length <i>len</i> using the Turtle &quot;longString&quot; triple quoting format to the iostream <i>iostr</i>. </p>
 </dd>
<dt><code>const char* raptor_ntriples_term_as_string (raptor_ntriples_term_type </code><i>term</i>)</dt>
<dd> <p> Deprecated, for internal use. </p>
 </dd></dl>
<h2>XML UTILITY FUNCTIONS</h2>
<dl>
<dt><code>int raptor_xml_any_escape_string(const unsigned char* </code><i>string</i>, size_t <i>len</i>, unsigned char* <i>buffer</i>, size_t <i>length</i>, char <i>quote</i>, int <i>xml_version</i>, raptor_simple_message_handler <i>error_handler</i>, void* <i>error_data</i>)</dt>
<dd>  </dd>
<dt><code>int raptor_xml_escape_string(const unsigned char *</code><i>string</i><code>, size_t </code><i>len</i><code>, unsigned char *</code><i>buffer</i><code>, size_t </code><i>length</i><code>, char </code><i>quote</i><code>, raptor_message_handler </code><i>error_handler</i><code>, void *</code><i>error_data</i><code>)</code></dt>
<dd> <p> Apply the XML escaping rules to the string given in (string, len) into the <i>buffer</i> of size <i>length</i>. If <i>quote</i> is given, the escaped content is for an XML attribute and the appropriate quote character XML element content (CDATA). The <i>error_handler</i> method along with <i>error_data</i> allow error reporting to be given. If buffer is NULL, returns the size of the buffer required to escape. Otherwise the return value is the number of bytes used or &lt;0 on failure. </p>
 </dd>
<dd> <p> When an <i>xml_version</i> argument is present and has a value 10 (XML 1.0) or 11 (XML 1.1) then that version is used. The default with no argument is to generate XML 1.0. </p>
 </dd>
<dt><code>int raptor_iostream_write_xml_any_escaped_string(raptor_iostream* </code><i>iostr</i>, const unsigned char* <i>string</i>, size_t <i>len</i>, char <i>quote</i>, int <i>xml_version</i>, raptor_simple_message_handler <i>error_handler</i>, void* <i>error_data</i>)</dt>
<dd>  </dd>
<dt><code>int raptor_iostream_write_xml_escaped_string(raptor_iostream* </code><i>iostr</i><code>, const unsigned char *</code><i>string</i><code>, size_t </code><i>len</i><code>, char </code><i>quote</i><code>, raptor_simple_message_handler </code><i>error_handler</i><code>, void *</code><i>error_data</i><code>)</code></dt>
<dd> <p> Write an XML-escaped version of the string given in (string, len) to iostream <i>iostr</i>. If <i>quote</i> is given, the escaped content is for an XML attribute and the appropriate quote character is used, otherwise it is XML element content (CDATA). The <i>error_handler</i> method along with <i>error_data</i> allow error reporting to be given. </p>
 </dd>
<dd> <p> When an <i>xml_version</i> argument is present and has a value 10 (XML 1.0) or 11 (XML 1.1) then that version is used. The default with no argument is to generate XML 1.0. </p>
 </dd>
<dt><code>int raptor_xml_name_check(const unsigned char *</code><i>string</i>, size_t <i>length</i>, int xml_version)</dt>
<dd> <p> Check that the given <i>string</i> of <i>length</i> bytes is a legal XML name according to XML 1.0 or XML 1.1. <i>xml_version</i> is set to 10 or 11 respectively. Returns non-zero if the name is legal. </p>
 </dd></dl>
<h2>MEMORY UTILITY FUNCTIONS</h2>
<dl>
<dt><code>void raptor_free_memory(void *</code><i>ptr</i>)</dt>
<dd> <p> Free memory allocated inside raptor. Some systems require memory allocated in a library to be deallocated inside that library. This function can be used in that situation to free memory allocated by raptor, such as the result of the <i>_to_</i> methods that return allocated memory such as <code>raptor_uri_to_filename</code>, <code>raptor_uri_to_string</code>, <code>raptor_uri_to_relative_counted_uri_string</code>, <code>raptor_uri_to_relative_uri_string</code> or <code>raptor_new_namespace_parts_from_string</code>. </p>
 </dd>
<dt><code>void* raptor_alloc_memory(size_t </code><i>size</i>)</dt>
<dd> <p> Allocate memory inside the raptor library. Some systems require memory allocated in a library to be deallocated inside that library. This function can be used in that situation to allocate memory for raptor to free later, such as inside the handler function declared with <code>raptor_set_generate_id_handler</code> which returns new memory. </p>
 </dd>
<dt><code>void* raptor_calloc_memory(size_t </code><i>nmemb</i>, size_t <i>size</i>)</dt>
<dd> <p> Allocate zeroed array of items inside raptor. Some systems require memory allocated in a library to be deallocated inside that library. This function can be used in that situation to clear an array of allocated memory for raptor to use, for freeing later, such as inside the handler function declared with <code>raptor_set_generate_id_handler</code> which returns new memory. </p>
 </dd></dl>
<h2>UNICODE UTILITY FUNCTIONS</h2>
<dl>
<dt><code>int raptor_unicode_char_to_utf8(raptor_unichar </code><i>c</i>, unsigned char *<i>output</i>)</dt>
<dd> <p> Turn a Unicode character into UTF8 bytes in <i>output</i> of size <i>c</i> bytes which must be of sufficient size. Returns the number of bytes encoded or &lt;0 on failure. </p>
 </dd>
<dt><code>int raptor_utf8_to_unicode_char(raptor_unichar *</code><i>output</i>, const unsigned char *<i>input</i>, int <i>length</i>)</dt>
<dd> <p> Decode a sequence UTF8 bytes in <i>input</i> of size <i>length</i> into a Unicode character in <i>output</i> returning the number of bytes used or &lt;0 on failure. </p>
 </dd>
<dt><code>int raptor_utf8_check(const unsigned char *</code><i>string</i>, size_t <i>len</i>gth)</dt>
<dd> <p> Check that a given <i>string</i> is legal UTF-8 encoding and includes only legal Unicode characters U+0 to U+0x10ffff inclusive. Returns non-0 if the string is good. </p>
 </dd>
<dt><code>int raptor_unicode_is_xml11_namestartchar(raptor_unichar </code><i>c</i>)</dt>
<dd>  </dd>
<dt><code>int raptor_unicode_is_xml10_namestartchar(raptor_unichar </code><i>c</i>)</dt>
<dd>  </dd>
<dt><code>int raptor_unicode_is_xml11_namechar(raptor_unichar </code><i>c</i>)</dt>
<dd>  </dd>
<dt><code>int raptor_unicode_is_xml10_namechar(raptor-unichar </code><i>c</i>)</dt>
<dd> <p> Check that given Unicode characters are allowed as XML 1.0 or XML 1.0 names - either as the starting character (<code>*_namestartchar</code>) or continuing character (<code>*_namechar</code>). Returns non-0 if the character is allowed. </p>
 </dd></dl>
<h2>ERROR UTILITY FUNCTIONS</h2>
<dl>
<dt><code>void raptor_error_handlers_init(raptor_error_handlers* </code><i>error_handlers</i>)</dt>
<dd> <p> Initialise an error_handlers structure after the log level handlers and user data pointers have been set. </p>
 </dd></dl>
<h2>MISCELLANEOUS UTILITY FUNCTIONS</h2>
<dl>
<dt><code>char* raptor_vsnprintf(const char *message, va_list arguments)</code></dt>
<dd> <p> Compatibility wrapper around vsnprintf. </p>
 </dd></dl>
<h2>STATIC VARIABLES</h2>
<p> There are several read-only static variables in the raptor library: </p>
<dl>
<dt><code>const char * const raptor_short_copyright_string</code></dt>
<dd> <p> Short copyright string, suitable for one line. </p>
 </dd>
<dt><code>const char * const raptor_copyright_string</code></dt>
<dd> <p> Full copyright over several lines including URLs. </p>
 </dd>
<dt><code>const char * const raptor_version_string</code></dt>
<dd> <p> The version as a string </p>
 </dd>
<dt><code>const unsigned int raptor_version_major</code></dt>
<dd> <p> The major version number as an integer. </p>
 </dd>
<dt><code>const unsigned int raptor_version_minor</code></dt>
<dd> <p> The minor version number as an integer. </p>
 </dd>
<dt><code>const unsigned int raptor_version_release</code></dt>
<dd> <p> The release version number as an integer. </p>
 </dd>
<dt><code>const unsigned int raptor_version_decimal</code></dt>
<dd> <p> The version number as a single decimal. </p>
 </dd>
<dt><code>const char * const raptor_license_string</code></dt>
<dd> <p> The license string over several lines including URLs. </p>
 </dd>
<dt><code>const char * const raptor_home_url_string</code></dt>
<dd> <p> The home page URL as a string. </p>
 </dd></dl>
<h2>SERIALIZER CLASS</h2>
<p> This class provides the functionality of turning RDF triples into syntaxes - RDF serializing.  </p>
<h2>SERIALIZER CONSTRUCTOR</h2>
<dl>
<dt><code>raptor_serializer* raptor_new_serializer(const char *</code><i>name</i>)</dt>
<dd> <p> Create a new raptor serializer object for the serializer with name <i>name</i> currently either &quot;rdfxml&quot; or &quot;ntriples&quot;. or &quot;rss-1.0&quot; for the RSS 1.0 serializer. </p>
 </dd></dl>
<h2>SERIALIZER DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_serializer(raptor_serializer* </code><i>rdf_serializer</i><code>)</code></dt>
<dd> <p> Destroy a Raptor serializer object. </p>
 </dd></dl>
<h2>SERIALIZER SERIALIZING METHODS</h2>
<dl>
<dt><code>int raptor_serialize_start(raptor_serializer* </code><i>rdf_serializer</i><code>, raptor_uri *</code><i>uri</i>, raptor_iostream *<i>iostream</i>)</dt>
<dd> <p> Start to serialize content using the given <i>iostream</i> to write to with optional base URI <i>uri</i>. The <i>iostream</i> becomes owned by the serializer object and is destroyed at the end of serializing when raptor_serialize_end() is called. Note that some syntaxes may refuse to serialize without a base URI, such as RDF/XML. </p>
 </dd>
<dt><code>int raptor_serialize_start_to_iostream(raptor_serializer* </code><i>rdf_serializer</i>, raptor_uri* <i>uri</i>, raptor_iostream* <i>iostream</i>)</dt>
<dd> <p> Start to serialize content using the given <i>iostream</i> to write to with optional base URI <i>uri</i>. The <i>iostream</i> does NOT become owned by the serializer object and the caller may continue to write to it after serializing is finished. Note that some syntaxes may refuse to serialize without a base URI, such as RDF/XML. </p>
 </dd>
<dt><code>int raptor_serialize_start_to_filename(raptor_serializer* </code><i>rdf_serializer</i><code>, const char *</code><i>filename</i>)</dt>
<dd> <p> Start to serialize content to the file <i>filename</i> which is opened for writing. The base URI is calculated from the file name. </p>
 </dd>
<dt><code>int raptor_serialize_start_to_string(raptor_serializer* </code><i>rdf_serializer</i><code>, raptor_uri *</code><i>uri</i>, void **<i>string_p</i>, size_t *<i>length_p</i>)</dt>
<dd> <p> Start to serialize content to a string. <i>string_p</i> must point to a void* pointer that will be used at the end of serializing to store the newly allocated string. <i>length_p</i> if not NULL, it will be used to store the length of the new string. The serializing is done with optional base URI <i>uri</i> however some syntaxes may refuse to serialize without a base URI, such as RDF/XML. </p>
 </dd>
<dt><code>int raptor_serialize_start_to_file_handle(raptor_serializer* </code><i>rdf_serializer</i><code>, raptor_uri *</code><i>uri</i>, FILE *<i>handle</i>)</dt>
<dd> <p> Start to serialize content to the already open C Standard I/O FILE* <i>handle</i> with the base URI <i>uri</i>, which is optional and may be NULL. Note that some syntaxes may refuse to serialize without a base URI, such as RDF/XML. </p>
 </dd>
<dt><code>int raptor_serialize_statement(raptor_serializer* </code><i>rdf_serializer</i><code>, const raptor_statement *</code><i>statement</i>)</dt>
<dd> <p> Serialize a single <i>statement</i> using the serializer. </p>
 </dd>
<dt><code>int raptor_serialize_end(raptor_serializer* </code><i>rdf_serializer</i><code>)</code></dt>
<dd> <p> End the serializing. This may close and delete resources used in serializing. No more calls to raptor_serialize_statement or raptor_serialize_end may be done at this point. </p>
 </dd>
<dt><code>raptor_iostream* raptor_serializer_get_iostream(raptor_serializer *</code><i>serializer</i>)</dt>
<dd> <p> Return a pointer to the raptor_iostream* used by the serializer. </p>
 </dd>
<dt><code>int raptor_serializer_set_namespace(raptor_serializer* </code><i>serializer</i>, raptor_uri *<i>uri</i>, const char *<i>prefix</i>)</dt>
<dd> <p> Set a suggested namespace URI/prefix mapping for use in serializing. </p>
 </dd></dl>
<h2>SERIALIZER UTILITY METHODS</h2>
<dl>
<dt><code>void raptor_serializer_set_error_handler(raptor_serializer* </code><i>serializer</i><code>, void *</code><i>user_data</i><code>, raptor_message_handler </code><i>handler</i><code>)</code></dt>
<dd> <p> Set the serializer non-fatal error handler callback. </p>
 </dd>
<dt><code>void raptor_serializer_set_warning_handler(raptor_serializer* </code><i>serializer</i><code>, void *</code><i>user_data</i><code>, raptor_message_handler </code><i>handler</i><code>)</code></dt>
<dd> <p> Set the serializer warning message handler callback. </p>
 </dd>
<dt><code>raptor_locator* raptor_serializer_get_locator(raptor_serializer* </code><i>rdf_serializer</i><code>)</code></dt>
<dd> <p> Return the current raptor_locator object for the serializer. This is a public structure defined in raptor.h that can be used directly, or formatted via raptor_print_locator. </p>
 </dd>
<dt><code>int raptor_serializer_set_feature(raptor_serializer *</code><i>serializer</i><code>, raptor_feature </code><i>feature</i><code>, int </code><i>value</i><code>)</code></dt>
<dd> <p> Set a serializer feature <i>feature</i> to a particular <i>value</i>. Returns non 0 on failure or if the feature is unknown. The current defined serializer features are: <br />
&nbsp;<wbr>&nbsp;<wbr><i>Feature&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Values</i> <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_RELATIVE_URIS</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WRITE_BASE_URI</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_START_URI</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>URI String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_BNODE_BORDER</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_BNODE_FILL</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_JSON_CALLBACK</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_JSON_EXTRA_DATA</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_LITERAL_BORDER</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_LITERAL_FILL</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_RESOURCE_BORDER</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_RESOURCE_FILL</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_RSS_TRIPLES</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ATOM_ENTRY_URI</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String </p>
<p> If the <i>relative_uris</i> feature is true (default false) then when serialising, preference is given to generating relative URIs where possible. If the <i>write_base_uri</i> feature is true (default true) then the atom, rdfxml, rdfxml-abbrev and turtle serializers will write an @base or xml:base directive in the output. If the <i>start_uri</i> feature is set to a URI it is used by the serializer to start serializing from. If the <i>bnode_border</i> feature is set, the DOT serializer uses it as the bnode border colour. If the <i>bnode_fill</i> feature is set, the DOT serializer uses it as the bnode fill colour. If the <i>json_callback</i> feature is set, the JSON serializers use it as the name of the callback to wrap the outer JSON object. If the <i>json_extra_data</i> feature is set, the JSON serializers use it as extra data inside the outer JSON object. If the <i>literal_border</i> feature is set, the DOT serializer uses it as the literal border colour. If the <i>literal_fill</i> feature is set, the DOT serializer uses it as the literal fill colour. If the <i>resource_border</i> feature is set, the DOT serializer uses it as the resource border colour. If the <i>resource_fill</i> feature is set, the DOT serializer uses it as the resource fill colour. If the <i>rss_triples</i> feature is set to the string &quot;rdf-xml&quot; for the rss-1.0 serializer or &quot;atom-triples&quot; for the atom serializer, it writes extra rdf triples into the serialized output. If the <i>atom_entry_uri</i> feature is set to a URI string, it is used to trigger generation of an atom entry document for the atom serializer. </p>
 </dd>
<dt><code>int raptor_serializer_get_feature(raptor_serializer* </code><i>serializer</i><code>, raptor_feature </code><i>feature</i><code>)</code></dt>
<dd> <p> Get serializer features, the allowed <i>feature</i> values are available </p>
 </dd></dl>
<h2>SERIALIZER UTILITY FUNCTIONS</h2>
<dl>
<dt><code>int raptor_serializers_enumerate(const unsigned </code><i>int counter</i><code>, const char **</code><i>name</i><code>, const char **</code><i>label</i><code>, const char **</code><i>mime_type</i><code>, const unsigned char **</code><i>uri_string</i><code>)</code></dt>
<dd> <p> Return the serializer name/label for a serializer with a given integer counter, returning non-zero if no such parser at that offset exists. The counter should start from 0 and be incremented by 1 until the function returns non-zero. </p>
 </dd>
<dt><code>int raptor_serializer_syntax_name_check(const char *</code><i>name</i><code>)</code></dt>
<dd> <p> Check <i>name</i> is a known serializer syntax name. </p>
 </dd></dl>
<h2>URI CLASS</h2>
<p> Raptor has a raptor_uri class must be used for manipulating and passing URI references. The default internal implementation uses char* strings for URIs, manipulating them and constructing them. This URI implementation can be replaced by any other that provides the equivalent functionality, using the <code>raptor_uri_set_handler</code> function.  </p>
<h2>URI CONSTRUCTORS</h2>
<p> There a several constructors for raptor_uri to build them from char* strings and existing raptor_uri objects. </p>
<dl>
<dt><code>raptor_uri* raptor_new_uri(const unsigned char* </code><i>uri_string</i><code>)</code></dt>
<dd> <p> Create a raptor URI from a string URI-reference <i>uri_string</i>. </p>
 </dd>
<dt><code>raptor_uri* raptor_new_uri_from_uri_local_name(raptor_uri* </code><i>uri</i><code>, const unsigned char* </code><i>local_name</i><code>)</code></dt>
<dd> <p> Create a raptor URI from a string URI-reference <i>local_name</i> relative to an existing URI-reference. This performs concatenation of the <i>local_name</i> to the <i>uri</i> and not relative URI resolution, which is done by the raptor_new_uri_relative_to_base constructor. </p>
 </dd>
<dt><code>raptor_uri* raptor_new_uri_relative_to_base(raptor_uri* </code><i>base_uri, const unsigned char* uri_string</i><code>)</code></dt>
<dd> <p> Create a raptor URI from a string URI-reference <i>uri_string</i> using relative URI resolution to the <i>base_uri</i>. </p>
 </dd>
<dt><code>raptor_uri* raptor_new_uri_from_id(raptor_uri* </code><i>base_uri</i><code>, const unsigned char* </code><i>id</i><code>)</code></dt>
<dd> <p> Create a raptor URI from a string RDF ID <i>id</i> concatenated to the <i>base_uri</i> base URI. </p>
 </dd>
<dt><code>raptor_uri* raptor_new_uri_for_rdf_concept(const char* </code><i>name</i><code>)</code></dt>
<dd> <p> Create a raptor URI for the RDF namespace concept <i>name</i>. </p>
 </dd>
<dt><code>raptor_uri* raptor_new_uri_for_xmlbase(raptor_uri* </code><i>old_uri</i><code>))</code></dt>
<dd> <p> Create a raptor URI suitable for use with xml:base (throw away fragment) </p>
 </dd></dl>
<h2>URI DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_uri(raptor_uri* </code><i>uri</i><code>)</code></dt>
<dd> <p> Destroy a raptor URI object. </p>
 </dd></dl>
<h2>URI METHODS</h2>
<dl>
<dt><code>int raptor_uri_equals(raptor_uri* </code><i>uri1</i><code>, raptor_uri* </code><i>uri2</i><code>)</code></dt>
<dd> <p> Return non-zero if the given URIs are equal. </p>
 </dd>
<dt><code>raptor_uri* raptor_uri_copy(raptor_uri* </code><i>uri</i><code>)</code></dt>
<dd> <p> Return a copy of the given raptor URI <i>uri</i>. </p>
 </dd>
<dt><code>unsigned char* raptor_uri_as_counted_string(raptor_uri *uri, size_t* len_p)</code></dt>
<dd>  </dd>
<dt><code>unsigned char* raptor_uri_as_string(raptor_uri* </code><i>uri</i><code>)</code></dt>
<dd> <p> Return a shared pointer to a string representation of the given raptor URI <i>uri</i>. This string is shared and must not be freed (otherwise see the <code>raptor_uri_to_*</code> methods below). If <code>raptor_uri_as_counted_string</code> is used, the length of the returned string is stored in *<i>len_p</i> if not NULL. </p>
 </dd>
<dt><code>unsigned char* raptor_uri_to_counted_string(raptor_uri *</code><i>uri</i>, size_t *<i>len_p</i>)</dt>
<dd>  </dd>
<dt><code>unsigned char* raptor_uri_to_string(raptor_uri *</code><i>uri</i>)</dt>
<dd> <p> Return a to a newly alloced string representation of the given raptor URI <i>uri</i>. This string must be freed by the caller using <code>raptor_free_memory</code>. If <code>raptor_uri_to_counted_string</code> is used, the length of the returned string is stored in *<i>len_p</i> if not NULL. </p>
 </dd>
<dt><code>unsigned char* raptor_uri_to_relative_counted_uri_string(raptor_uri *</code><i>base_uri</i><code>, raptor_uri *</code><i>reference_uri</i><code>, size_t *</code><i>length_p</i><code>)</code></dt>
<dd>  </dd>
<dt><code>unsigned char* raptor_uri_to_relative_uri_string(raptor_uri *</code><i>base_uri</i><code>, raptor_uri *</code><i>reference_uri</i><code>)</code></dt>
<dd> <p> Return a new relative URI string of a URI <i>reference_uri against a base URI base_uri</i>. The returned string must be freed with <code>raptor_free_memory</code>. If <code>raptor_uri_to_relative_counted_string</code> is used, the length of the returned string is stored in *<i>len_p</i> if not NULL. </p>
 </dd>
<dt><code>void raptor_uri_print(const raptor_uri* </code><i>uri</i>, FILE *<i>stream</i>)</dt>
<dd> <p> Print URI <i>uri</i> to the file handle <i>stream</i>. </p>
 </dd>
<dt><code>int raptor_iostream_write_uri(raptor_iostream* </code><i>iostr</i>, raptor_uri* <i>uri</i>)</dt>
<dd> <p> Write the raptor_uri <i>uri</i> to the iostream <i>ostr</i>. </p>
 </dd></dl>
<h2>URI UTILITY FUNCTIONS</h2>
<dl>
<dt><code>void raptor_uri_resolve_uri_reference (const unsigned char* </code><i>base_uri</i><code>, const unsigned char* </code><i>reference_uri</i><code>, char unsigned* </code><i>buffer</i><code>, size_t </code><i>length</i><code>)</code></dt>
<dd> <p> This is a standalone function that resolves the relative URI <i>reference_uri</i> against the base URI <i>base_uri</i> according to the URI resolution rules in RFC2396. The resulting URI is stored in <i>buffer</i> which is of <i>length</i> bytes. If this is too small, no work will be done. </p>
 </dd>
<dt><code>char *raptor_uri_filename_to_uri_string(const unsigned char* </code><i>filename</i><code>)</code></dt>
<dd> <p> This is a standalone function that turns a local filename (Windows or Unix style as appropriate for platform) into a URI string (file). <br />
&nbsp;<wbr>The returned string must be freed by the caller. Some systems require memory allocated in a library to be deallocated inside that library in which case <code>raptor_free_memory</code> may be used. </p>
 </dd>
<dt><code>char *raptor_uri_uri_string_to_filename(const unsigned char* </code><i>uri_string</i><code>)</code></dt>
<dd>  </dd>
<dt><code>char *raptor_uri_uri_string_to_filename(const unsigned char* </code><i>uri_string</i><code>, unsigned char **</code><i>fragment_p</i>)</dt>
<dd> <p> These are standalone functions that turn a URI string that represents a local filename (file:) into a filename, with optional URI fragment. If <i>fragment_p</i> is not NULL it points to the location to store a newly allocated string containing the fragment. The returned strings must be freed by the caller. Some systems require memory allocated in a library to be deallocated inside that library in which case <code>raptor_free_memory</code> may be used. </p>
 </dd>
<dt><code>int raptor_uri_is_file_uri(const unsigned char* </code><i>uri_string</i><code>)</code></dt>
<dd> <p> DEPRECATED in 1.4.9. Returns non-zero if the given URI string represents a filename. Use <code>raptor_uri_uri_string_is_file_uri</code> in preference. </p>
 </dd>
<dt><code>int raptor_uri_uri_string_is_file_uri(const unsigned char* </code><i>uri_string</i>)</dt>
<dd> <p> Returns non-zero if the given URI string represents a filename. </p>
 </dd></dl>
<h2>URI CLASS IMPLEMENTATION</h2>
<dl>
<dt><code>void raptor_uri_set_handler(const raptor_uri_handler *</code><i>handler</i><code>, void *</code><i>context</i><code>)</code></dt>
<dd> <p> Change the URI class implementation to the functions provided by the <i>handler</i> URI implementation. The <i>context</i> user data is passed in to the handler URI implementation calls. </p>
 </dd>
<dt><code>void raptor_uri_get_handler(raptor_uri_handler **</code><i>handler</i><code>, void **</code><i>context</i><code>)</code></dt>
<dd> <p> Return the current raptor URI class implementation <i>handler</i> and <i>context</i> </p>
 </dd></dl>
<h2>WWW CLASS</h2>
<p> This is a small wrapper class around existing WWW libraries in order to provide HTTP GET or better URI retrieval for Raptor. It is not intended to be a general purpose WWW retrieval interface.  </p>
<h2>WWW CLASS INITIALISATION AND CLEANUP</h2>
<dl>
<dt><code>void raptor_www_init(void)</code></dt>
<dd>  </dd>
<dt><code>void raptor_www_finish(void)</code></dt>
<dd> <p> Initialise or terminate the raptor_www infrastructure. raptor_www_init and raptor_finish are called by raptor_init and raptor_finish respecitively, otherwise must be called once each. </p>
 </dd>
<dt>NOTE</dt>
<dd> <p> Several of the WWW library implementations require once-only initialisation and termination functions to be called, however raptor cannot determine whether this is already done before the library is initialised in <code>raptor_www_init</code> or terminated in <code>raptor_www_finish</code>, so always performs it. This can be changed by <code>raptor_www_no_www_library_init_finish</code>. </p>
 </dd>
<dt><code>void raptor_www_no_www_library_init_finish(void)</code></dt>
<dd> <p> If this is called before <code>raptor_www_init</code>, it will not call the underlying WWW library global initialise or terminate functions. The application code must perform both operations. </p>
 </dd>
<dd> <p> For example with curl, after this function is called, neither <code>curl_global_init</code> nor <code>curl_global_cleanup</code> will be called during <code>raptor_www_init</code> or <code>raptor_www_finish</code> respectively. </p>
 </dd></dl>
<h2>WWW CONSTRUCTORS</h2>
<dl>
<dt><code>raptor_www *raptor_www_new(void)</code></dt>
<dd>  </dd>
<dt><code>raptor_www *raptor_www_new_with_connection(void* </code><i>connection</i><code>)</code></dt>
<dd> <p> Create a raptor WWW object capable of URI retrieval. If <i>connection</i> is given, it must match the connection object of the underlying WWW implementation. At present, this is only for libcurl, and allows you to re-use an existing curl handle, or use one which has been set up with some desired qualities. </p>
 </dd></dl>
<h2>WWW DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_www_free(raptor_www *</code><i>www</i><code>)</code></dt>
<dd> <p> Destroy a raptor WWW object. </p>
 </dd></dl>
<h2>WWW METHODS</h2>
<dl>
<dt><code>void raptor_www_set_user_agent(raptor_www *</code><i>www</i><code>, const char *</code><i>user_agent</i><code>)</code></dt>
<dd> <p> Set the HTTP User-Agent header value. </p>
 </dd>
<dt><code>int raptor_www_set_http_cache_control(raptor_www* </code><i>www</i>, const char* <i>cache_control</i>)</dt>
<dd> <p> Set the HTTP Cache-Control header value. </p>
 </dd>
<dt><code>void raptor_www_set_proxy(raptor_www *</code><i>www</i><code>, const char *</code><i>proxy</i><code>)</code></dt>
<dd> <p> Set the HTTP proxy - usually a string of the form <a rel="nofollow" href="http://server:port">http://server:port</a> </p>
 </dd>
<dt><code>raptor_www_set_write_bytes_handler(raptor_www *</code><i>www</i><code>, raptor_www_write_bytes_handler </code><i>handler</i><code>, void *</code><i>user_data</i><code>)</code></dt>
<dd> <p> Set the handler to receive bytes written by the raptor_www implementation. </p>
 </dd>
<dt><code>void raptor_www_set_content_type_handler(raptor_www *</code><i>www</i><code>, raptor_www_content_type_handler </code><i>handler</i><code>, void *</code><i>user_data</i><code>)</code></dt>
<dd> <p> Set the handler to receive the HTTP Content-Type value, when/if discovered during retrieval by the raptor_www implementation. </p>
 </dd>
<dt><code>void raptor_www_set_http_accept(raptor_www *</code><i>www</i>, const char *<i>value</i>)</dt>
<dd> <p> Set the WWW HTTP Accept: header to <i>value</i>. If <i>value</i> is NULL, an empty header is sent. </p>
 </dd>
<dt><code>void raptor_www_set_error_handler(raptor_www *www, raptor_message_handler </code><i>error_handler</i><code>, void *</code><i>error_data</i><code>)</code></dt>
<dd> <p> Set the error handler routine for the raptor_www class. This takes the same arguments as the raptor_parser error, warning handler methods. </p>
 </dd>
<dt><code>void raptor_www_set_uri_filter(raptor_www* </code><i>www</i>, raptor_uri_filter_func <i>filter</i>, void* <i>user_data</i>)</dt>
<dd> <p> Set the URI filter function <i>filter</i> for URIs retrieved by the raptor_www object. </p>
 </dd>
<dt><code>void* raptor_www_get_connection(raptor_www *</code><i>www</i><code>)</code></dt>
<dd> <p> Return the underlying WWW library connection object. For example, for libcurl this is the curl_handle. </p>
 </dd>
<dt><code>void raptor_www_set_connection_timeout(raptor_www* </code><i>www</i>, int <i>timeout</i>)</dt>
<dd> <p> Set the WWW connection <i>timeout</i> in seconds. </p>
 </dd>
<dt><code>raptor_uri* raptor_www_get_final_uri(raptor_www* </code><i>www</i>)</dt>
<dd> <p> Get the final URI from a WWW retrieval, which may include redirections. </p>
 </dd></dl>
<h2>WWW ACTION METHODS</h2>
<dl>
<dt><code>int raptor_www_fetch(raptor_www *www, raptor_uri *uri)</code></dt>
<dd> <p> Retrieve the given URL, returning non zero on failure. </p>
 </dd>
<dt><code>int raptor_www_fetch_to_string(raptor_www *www, raptor_uri *uri, void **string_p, size_t *length_p, void *(*malloc_handler)(size_t size))</code></dt>
<dd> <p> Retrieve the given URL to a string. <i>string_p</i> must point to a void* pointer that will be used to store the newly allocated string. <i>length_p</i> if not NULL, it will be used to store the length of the new string. </p>
 </dd>
<dt><code>void raptor_www_abort(raptor_www *www, const char *reason)</code></dt>
<dd> <p> Abort an ongoing raptor WWW operation. Typically used within one of the raptor WWW handlers. </p>
 </dd></dl>
<h2>QNAME CLASS</h2>
<p> This is a class for handling XML QNames consisting of the pair of (a URI from a namespace, a local name) along with an optional value -- useful for XML attributes. This is used with the raptor_namespace_stack and raptor_namespace classes to handle a stack of raptor_namespace that build on raptor_qname.  </p>
<h2>QNAME CONSTRUCTORS</h2>
<p> There are two constructors for raptor_qname to build qnames with optional values on a stack of names. </p>
<dl>
<dt><code>raptor_qname* raptor_new_qname(raptor_namespace_stack *</code><i>nstack</i><code>, const unsigned char *</code><i>name</i><code>, const unsigned char *</code><i>value</i><code>, raptor_simple_message_handler </code><i>error_handler</i><code>, void *</code><i>error_data</i><code>)</code></dt>
<dd> <p> Create a raptor QName <i>name</i> (a possibly :-separated name) with name to be resolved against the given <i>nstack</i> namespace stack. An optional <i>value</i> can be given, and if there is an error, the <i>error_handler</i><code> and </code><i>error_data</i> will be used to invoke the callback. </p>
 </dd>
<dt><code>raptor_qname* raptor_new_qname_from_namespace_local_name (raptor_namespace *</code><i>ns</i><code>, const unsigned char *</code><i>local_name</i><code>, const unsigned char *</code><i>value</i><code>)</code></dt>
<dd> <p> Create a raptor QName using the namespace name of the raptor_namespace <i>ns</i> and the local name <i>local_name</i>, along with optional value <i>value</i>. Errors are reported using the error handling and data of the namespace. </p>
 </dd>
<dt><code>raptor_qname* raptor_qname_copy(raptor_qname *</code><i>qname</i>)</dt>
<dd> <p> Create a raptor QName from an existing one, returning NULL on failure. </p>
 </dd></dl>
<h2>QNAME DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_qname(raptor_qname* </code><i>name</i><code>)</code></dt>
<dd> <p> Destroy a raptor qname object. </p>
 </dd></dl>
<h2>QNAME METHODS</h2>
<dl>
<dt><code>int raptor_qname_equal(raptor_qname* </code><i>name1</i>, raptor_qname *<i>name2</i>)</dt>
<dd> <p> Return non-zero if the given QNames are equal. </p>
 </dd>
<dt><code>int raptor_iostream_write_qname(raptor_iostream* </code><i>iostr</i>, raptor_qname *<i>qname</i>)</dt>
<dd> <p> Write the raptor_qname <i>qname</i> to the iostream <i>ostr</i>. </p>
 </dd>
<dt><code>const unsigned char* raptor_qname_get_local_name(raptor_qname* </code><i>name</i>)</dt>
<dd> <p> Get the local name of the QName. </p>
 </dd>
<dt><code>const unsigned char* raptor_qname_get_value(raptor_qname* </code><i>name</i>)</dt>
<dd> <p> Get the value of the QName for an XML attribute QName. </p>
 </dd>
<dt><code>const unsigned char* raptor_qname_get_counted_value(raptor_qname* </code><i>name</i>, size_t* <i>length_p</i>)</dt>
<dd> <p> Get the value fo the QName along with the length (if <i>length_p</i> is not NULL) for an XML attribute QName. </p>
 </dd>
<dt><code>unsigned char* raptor_qname_to_counted_name(raptor_qname* </code><i>qname</i>, size_t* <i>length_p</i>)</dt>
<dd> <p> Get the formatted QName as a newly allocated counted string (if <i>length_p</i> is not NULL). </p>
 </dd></dl>
<h2>QNAME UTILITY FUNCTIONS</h2>
<dl>
<dt><code>raptor_uri* raptor_qname_string_to_uri(raptor_namespace_stack *</code><i>nstack</i><code>, const unsigned char *</code><i>name</i><code>, size_t </code><i>name_len</i><code>, raptor_simple_message_handler </code><i>error_handler</i><code>, void *</code><i>error_data</i><code>)</code></dt>
<dd> <p> Return the URI corresponding to the QName according to the RDF method; concatenating the namespace&#8217;s name (URI) with the local name. Takes the same arguments as <code>raptor_new_qname</code> but does not create a raptor_qname object. </p>
 </dd>
<dt><code>raptor_namespace* raptor_qname_get_namespace(raptor_qname* </code><i>name</i><code>)</code></dt>
<dd> <p> Return the raptor_namespace used by the QName. Will never be NULL even for the default namespace in which case the URI of the returned namespace object will be NULL. </p>
 </dd></dl>
<h2>NAMESPACE CLASS</h2>
<p> An XML namespace class - each entry is on a stack and consists of a name (URI) and prefix. The prefix or the name but not both may be empty. If the prefix is empty, it defines the default prefix. If the name is empty, it undefines the given prefix.  </p>
<h2>NAMESPACE CONSTRUCTORS</h2>
<dl>
<dt><code>raptor_namespace* raptor_new_namespace(raptor_namespace_stack *</code><i>nstack</i>, const unsigned char *<i>prefix</i>, const unsigned char *<i>ns_uri_string</i>, int <i>depth</i>)</dt>
<dd>  </dd>
<dt><code>raptor_namespace* raptor_new_namespace_from_uri(raptor_namespace_stack *</code><i>nstack</i>, const unsigned char *<i>prefix</i>, raptor_uri* <i>ns_uri</i>, int <i>depth</i>)</dt>
<dd> <p> Create a new raptor_namespace object on the given namespace stack <i>nstack</i> with prefix <i>prefix</i> and namespace name either from URI string <i>ns_uri_string</i> or from copying URI <i>ns_uri</i>. If <i>prefix</i> is NULL, it defines the URI for the default namespace prefix. If the namespace name (<i>ns_uri_string</i> or <i>ns_uri</i>) is NULL, it undefines the given <i>prefix</i> in the current scope. Both prefix and URI may be NULL to undefine the default namespace. <i>depth</i> signifies the position of the namespace on the stack; 0 is the bottom of the stack and generally the first depth for user namespace declarations. Namespaces declared on the same depth (such as on the same XML element, typically) can be handily freed with <i>raptor_namespaces_end_for_depth</i> method on the namespace stack class. </p>
 </dd></dl>
<h2>NAMESPACE DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_namespace(raptor_namespace *ns)</code></dt>
<dd> <p> Destroy a raptor namespace object. </p>
 </dd></dl>
<h2>NAMESPACE METHODS</h2>
<dl>
<dt><code>raptor_uri* raptor_namespace_get_uri(const raptor_namespace *ns)</code></dt>
<dd> <p> Return the namespace name (URI) of the namespace. </p>
 </dd>
<dt><code>const unsigned char* raptor_namespace_get_prefix(const raptor_namespace *ns)</code></dt>
<dd> <p> Return the prefix of the namespace. </p>
 </dd>
<dt><code>const unsigned char* raptor_namespace_get_counted_prefix(const raptor_namespace* </code><i>ns</i>, size_t* <i>length_p</i>)</dt>
<dd> <p> Return the prefix of the namespace as a string with optional count stored in the variable address <i>length_p</i> if it is not NULL. </p>
 </dd>
<dt><code>unsigned char *raptor_namespaces_format(const raptor_namespace *ns, size_t *length_p)</code></dt>
<dd> <p> Format the namespace as a string and return it as a new string, returning the length of the resulting string in <i>length_p</i> if it is not NULL. The string format is suitable for emitting in XML to declare the namespace. </p>
 </dd>
<dt><code>int raptor_iostream_write_namespace(raptor_iostream* </code><i>iostr</i>, raptor_namespace *<i>ns</i>)</dt>
<dd> <p> Write a formatted namespace declaration like xmlns... to an iostream <i>iostr</i>. </p>
 </dd></dl>
<h2>NAMESPACE UTILITY FUNCTIONS</h2>
<dl>
<dt><code>int raptor_namespace_copy(raptor_namespace_stack *nstack, raptor_namespace *ns, int new_depth)</code></dt>
<dd> <p> Copy the namespace from the current stack to the new one, <i>nstack</i> at depth <i>new_depth</i>. </p>
 </dd>
<dt><code>int raptor_new_namespace_parts_from_string(unsigned char *</code><i>string</i>, unsigned char **<i>prefix</i>, unsigned char **<i>uri_string</i>)</dt>
<dd> <p> Parse <i>string</i> with an XML-style namespace declaration like xmlns=&quot;&quot;, xmlns=&quot;uri&quot;, xmlns:prefix=&quot;&quot; or xmlns:prefix=&quot;uri&quot; into the strings pointed to by <i>prefix</i> string and a <i>uri_string</i>. Empty prefixes or namespace names return NULL pointers. Returned strings must be freed by the caller using <code>raptor_free_memory</code>. </p>
 </dd></dl>
<h2>NAMESPACE STACK CLASS</h2>
<p> A stack of raptor_namespace objects where the namespaces on top of the stack have wider scope and override earlier (lower) namespace declarations. Intended to match the XML namespace declaring semantics using xmlns attributes.  </p>
<h2>NAMESPACE STACK CONSTRUCTORS</h2>
<dl>
<dt><code>raptor_namespace_stack* raptor_new_namespaces(raptor_uri_handler *uri_handler, void *uri_context, raptor_simple_message_handler error_handler, void *error_data, int defaults)</code></dt>
<dd>  </dd>
<dt><code>int raptor_namespaces_init(raptor_namespace_stack *nstack, raptor_uri_handler *handler, void *context, raptor_simple_message_handler error_handler, void *error_data, int defaults)</code></dt>
<dd> <p> Create or initialise a new raptor_namespace_stack object with the given URI and error handlers. <code>raptor_namespaces_new</code> allocates new memory for the namespace stack and <code>raptor_namespaces_init</code> initialises an existing declared <i>nstack</i>, which could be statically allocated. Note that <code>raptor_uri_get_handler</code> can be useful to return the current raptor URI handler/context. The <i>defaults</i> argument describes which default namespaces are declared in the empty stack. At present, 0 is none, 1 for just the XML namespace and 2 is for a typical set of namespaces used for RDF, RDFS, Dublin Core, OWL, ... that may vary over time. </p>
 </dd>
<dd> <p> In versions 1.4.16 or newer this returns an integer result, non-0 on failure. </p>
 </dd></dl>
<h2>NAMESPACE STACK DESTRUCTORS</h2>
<dl>
<dt><code>void raptor_free_namespaces(raptor_namespace_stack *nstack)</code></dt>
<dd> <p> Destroy a namespace stack object, freeing the <i>nstack</i> (goes with <code>raptor_new_namespaces</code>). </p>
 </dd>
<dt><code>void raptor_namespaces_clear(raptor_namespace_stack *nstack)</code></dt>
<dd> <p> Clear a statically allocated namespace stack; does not free the <i>nstack</i>. (goes with <code>raptor_namespaces_init</code>). </p>
 </dd></dl>
<h2>NAMESPACE STACK METHODS</h2>
<dl>
<dt><code>void raptor_namespaces_start_namespace(raptor_namespace_stack *nstack, raptor_namespace *nspace)</code></dt>
<dd> <p> Start the given <i>nspace</i> on the stack, at the depth already defined. </p>
 </dd>
<dt><code>int raptor_namespaces_start_namespace_full(raptor_namespace_stack *nstack, const unsigned char *prefix, const unsigned char *nspace, int depth)</code></dt>
<dd> <p> Create a new raptor_namespace and start it on the stack. See <code>raptor_new_namespace</code> for the meaning of the argumens. </p>
 </dd>
<dt><code>void raptor_namespaces_end_for_depth(raptor_namespace_stack *nstack, int depth)</code></dt>
<dd> <p> End (and free) all namespaces on the stack at the given <i>depth</i>. </p>
 </dd>
<dt><code>raptor_namespace* raptor_namespaces_get_default_namespace (raptor_namespace_stack *nstack)</code></dt>
<dd> <p> Return the current default raptor_namespace of the namespace stack or NULL if there is none. </p>
 </dd>
<dt><code>raptor_namespace* raptor_namespaces_find_namespace_by_uri(raptor_namespace_stack *</code><i>nstack</i>, raptor_uri *<i>ns_uri</i>)</dt>
<dd> <p> Find the first namespace on the stack with the given uri <i>ns_uri</i> or NULL if there is none. </p>
 </dd>
<dt><code>raptor_namespace *raptor_namespaces_find_namespace_by_uri(raptor_namespace_stack *nstack, const unsigned char *prefix, int prefix_length)</code></dt>
<dd> <p> Find the first namespace on the stack with the given namespace <i>prefix</i> or NULL if there is none. </p>
 </dd>
<dt><code>int raptor_namespaces_namespace_in_scope(raptor_namespace_stack *nstack, const raptor_namespace *nspace)</code></dt>
<dd> <p> Return non-zero if the raptor_namespace <i>nspace</i> is declared on the stack; i.e. in scope if this is a stack of XML namespaces. </p>
 </dd></dl>
<h2>NAMESPACE STACK UTILITY FUNCTIONS</h2>
<dl>
<dt><code>raptor_qname* raptor_namespaces_qname_from_uri(raptor_namespace_stack* </code><i>nstack</i>, raptor_uri* <i>uri</i>, int <i>xml_version</i>)</dt>
<dd> <p> Create a raptor QName from the URI <i>uri</i> if the URI is squal one of the namespace URIs on the namespace stack <i>nstack</i> URIs concatenated to a legal XML name for the given XML version. URIs are created and errors are reported using the namespace stack fields. Fails if it cannot be legally described with any of the namespaces. </p>
 </dd></dl>
<h2>SEQUENCE CLASS</h2>
<p> A class for ordered sequences of items, adding at either end of the sequence. The method names should be familiar to Perl users.  </p>
<h2>SEQUENCE CONSTRUCTOR</h2>
<dl>
<dt><code>raptor_sequence* raptor_new_sequence(raptor_sequence_free_handler* </code><i>free_handler</i>, raptor_sequence_print_handler* <i>print_handler</i>)</dt>
<dd> <p> Create a new empty sequence, with optional handler for freeing elements (as used by <code>raptor_free_sequence</code> and printing out elements (used by <code>raptor_sequence_print</code>). </p>
 </dd></dl>
<h2>SEQUENCE DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_sequence(raptor_sequence* </code><i>seq</i>)</dt>
<dd> <p> Destoy a sequence object, freeing any items if the free handler was defined in the constructor. </p>
 </dd></dl>
<h2>SEQUENCE METHODS</h2>
<dl>
<dt><code>int raptor_sequence_size(raptor_sequence* </code><i>seq</i>)</dt>
<dd> <p> Return the number of items in the sequence. </p>
 </dd>
<dt><code>int raptor_sequence_set_at(raptor_sequence* </code><i>seq</i>, int <i>idx</i>, void *data)</dt>
<dd> <p> Set the sequence item at index <i>idx</i> to the value <i>data</i>, extending it if necessary. </p>
 </dd>
<dt><code>int raptor_sequence_push(raptor_sequence* </code><i>seq</i>, void *<i>data</i>)</dt>
<dd> <p> Add item <i>data</i> to the end of the sequence. </p>
 </dd>
<dt><code>int raptor_sequence_shift(raptor_sequence* </code><i>seq</i>, void *<i>data</i>)</dt>
<dd> <p> Add item <i>data</i> to the start of the sequence. </p>
 </dd>
<dt><code>void* raptor_sequence_get_at(raptor_sequence* </code><i>seq</i>, int <i>idx</i>)</dt>
<dd> <p> Get the sequence item at index <i>idx</i> or NULL if no such index exists. </p>
 </dd>
<dt><code>void* raptor_sequence_pop(raptor_sequence* </code><i>seq</i>)</dt>
<dd> <p> Remove and return an item from the end of the sequence, or NULL if is empty. </p>
 </dd>
<dt><code>void* raptor_sequence_unshift(raptor_sequence* </code><i>seq</i>)</dt>
<dd> <p> Remove and return an item from the start of the sequence, or NULL if is empty. </p>
 </dd>
<dt><code>void raptor_sequence_sort(raptor_sequence* </code><i>seq</i>, int(*<i>compare</i>)(const void *, const void *))</dt>
<dd> <p> Sort the sequence using the given comparison function <i>compare</i> which is passed to <a href="/docs/linux/man/3-qsort/">qsort</a>(3) internally. </p>
 </dd>
<dt><code>int raptor_compare_strings(const void *</code><i>a</i>, const void *<i>b</i>)</dt>
<dd> <p> Helper function useful with <code>raptor_sequence_sort</code>. </p>
 </dd>
<dt><code>void raptor_sequence_set_print_handler(raptor_sequence *</code><i>seq</i>, raptor_sequence_print_handler *<i>print_handler</i>)</dt>
<dd> <p> Set the print handler for the sequence, an alternative to setting it in the constructor. </p>
 </dd>
<dt><code>void raptor_sequence_print_string(char *</code><i>data</i>, FILE *<i>fh</i>)</dt>
<dd> <p> Helper print handler function useful for printing out sequences of strings. </p>
 </dd>
<dt><code>void raptor_sequence_print_uri(char *</code><i>data</i>, FILE *<i>fh</i>)</dt>
<dd> <p> Helper print handler function useful for printing out sequences of raptor_uri* objects. </p>
 </dd>
<dt><code>void raptor_sequence_print(raptor_sequence* </code><i>seq</i>, FILE* <i>fh</i>)</dt>
<dd> <p> Print out the sequence in a debug format to the given file handler <i>fh</i>. NOTE: The exact format is not guaranteed to remain the same between releases. </p>
 </dd>
<dt><code>int raptor_sequence_join(raptor_sequence* </code><i>dest</i>, raptor_sequence *<i>src</i>)</dt>
<dd> <p> Join two sequences moving all items from sequence <i>src</i> to the end of sequence <i>dest</i>. After this operation, sequence <i>src</i> will be empty (zero size) but will have the same item capacity as before. </p>
 </dd>
<dt><code>void* raptor_sequence_delete_at(raptor_sequence* </code><i>seq</i>, int <i>idx</i>)</dt>
<dd> <p> Remove an item from position <i>idx</i> in the sequence, returning it. </p>
 </dd></dl>
<h2>STRINGBUFFER CLASS</h2>
<p> A class for growing strings, small chunks at a time.  </p>
<h2>STRINGBUFFER CONSTRUCTOR</h2>
<dl>
<dt><code>raptor_stringbuffer* raptor_new_stringbuffer(void)</code></dt>
<dd> <p> Create a new stringbuffer. </p>
 </dd></dl>
<h2>STRINGBUFFER DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_stringbuffer(raptor_stringbuffer* </code><i>stringbuffer</i>)</dt>
<dd> <p> Destroy a stringbuffer. </p>
 </dd></dl>
<h2>STRINGBUFFER METHODS</h2>
<dl>
<dt><code>int raptor_stringbuffer_append_counted_string(raptor_stringbuffer* </code><i>stringbuffer</i>, const unsigned char *<i>string</i>, size_t <i>length</i>, int <i>do_copy</i>)</dt>
<dd> <p> Append a <i>string</i> of <i>length</i> bytes to a stringbuffer, copying it only if <i>do_copy</i> is non-0. </p>
 </dd>
<dt><code>int raptor_stringbuffer_append_string(raptor_stringbuffer* </code><i>stringbuffer</i>, const unsigned char* <i>string</i>, int <i>do_copy</i>)</dt>
<dd> <p> Append a <i>string</i> to a stringbuffer, copying it only if <i>do_copy</i> is non-0. </p>
 </dd>
<dt><code>int raptor_stringbuffer_append_decimal(raptor_stringbuffer* </code><i>stringbuffer</i>, int <i>integer</i>)</dt>
<dd> <p> Append a formatted decimal <i>integer</i> to a stringbuffer. </p>
 </dd>
<dt><code>int raptor_stringbuffer_append_stringbuffer(raptor_stringbuffer* </code><i>stringbuffer</i>, raptor_stringbuffer* <i>append</i>)</dt>
<dd> <p> Append a stringbuffer <i>append</i> to a stringbuffer. The append stringbuffer is emptied but not destroyed. </p>
 </dd>
<dt><code>int raptor_stringbuffer_prepend_counted_string(raptor_stringbuffer* </code><i>stringbuffer</i>, const unsigned char* <i>string</i>, size_t <i>length</i>, int <i>do_copy</i>)</dt>
<dd> <p> Prepend a <i>string</i> of <i>length</i> bytes to the start of a stringbuffer, copying it only if <i>do_copy</i> is non-0. </p>
 </dd>
<dt><code>int raptor_stringbuffer_prepend_string(raptor_stringbuffer* </code><i>stringbuffer</i>, const unsigned char* <i>string</i>, int <i>do_copy</i>)</dt>
<dd> <p> Prepend a <i>string</i> to the start of a stringbuffer, copying it only if <i>do_copy</i> is non-0. </p>
 </dd>
<dt><code>unsigned char * raptor_stringbuffer_as_string(raptor_stringbuffer* </code><i>stringbuffer</i>)</dt>
<dd> <p> Return the stringbuffer as a single string. The string is shared and should be copied if needed. </p>
 </dd>
<dt><code>size_t raptor_stringbuffer_length(raptor_stringbuffer* </code><i>stringbuffer</i>)</dt>
<dd> <p> Return the length of the stringbuffer. </p>
 </dd>
<dt><code>int raptor_stringbuffer_copy_to_string(raptor_stringbuffer* stringbuffer, unsigned char *</code><i>string</i>, size_t <i>len</i>gth)</dt>
<dd> <p> Copy the stringbuffer into a single string buffer <i>string</i> of size <i>length</i>. Returns non-0 on failure. </p>
 </dd></dl>
<h2>IOSTREAM CLASS</h2>
<p> This class provides an I/O stream that can write to filenames, FILE*, strings and user-defined output via callbacks.  </p>
<h2>IOSTREAM CONSTRUCTOR</h2>
<dl>
<dt><code>raptor_iostream* raptor_new_iostream_from_handler2(void* </code><i>context</i><code>, const raptor_iostream_handler2 *</code><i>handler</i>)</dt>
<dd> <p> Create a new raptor read or write iostream from a user-defined raptor_iostream_handler2 <i>handler</i> that is called with the passed-in <i>context</i> for the write operations. </p>
 </dd>
<dt><code>raptor_iostream* raptor_new_iostream_from_handler(void* </code><i>context</i><code>, const raptor_iostream_handler *</code><i>handler</i><code>)</code></dt>
<dd> <p> DEPRECATED in 1.4.17 - use <code>raptor_new_iostream_from_handler2()</code> with the new handler format. Create a new raptor read iostream from a user-defined raptor_iostream_handler <i>handler</i> that is called with the passed-in <i>context</i> for the write operations. </p>
 </dd>
<dt><code>raptor_iostream* raptor_new_iostream_to_sink(void)</code></dt>
<dd> <p> Create a new raptor write iostream that discards all written output. </p>
 </dd>
<dt><code>raptor_iostream* raptor_new_iostream_to_filename(const char *</code><i>filename</i><code>)</code></dt>
<dd> <p> Create a new raptor write iostream that creates and writes to a new file <i>filename</i>. </p>
 </dd>
<dt><code>raptor_iostream* raptor_new_iostream_to_file_handle(FILE *</code><i>handle</i><code>)</code></dt>
<dd> <p> Create a new raptor write iostream that creates and writes to an existing, already opened, C Standard I/O handle FILE* <i>handle</i>. </p>
 </dd>
<dt><code>raptor_iostream* raptor_new_iostream_to_string(void **</code><i>string_p</i><code>, size_t *</code><i>length_p</i><code>, void *(*</code><i>malloc_handler</i><code>)(size_t size))</code></dt>
<dd> <p> Create a new raptor write iostream which creates a new string once raptor_free_iostream is called. The new string pointer is written in <i>string</i>, the length in <i>length_p</i> (if not NULL) and the memory allocation is made using the <i>malloc_handler</i>, or if NULL, raptor&#8217;s default memory allocator. </p>
 </dd>
<dt><code>raptor_iostream* raptor_new_iostream_from_sink(void)</code></dt>
<dd> <p> Create a new raptor read iostream that is immediately finished and returns end of file. </p>
 </dd>
<dt><code>raptor_iostream* raptor_new_iostream_from_filename(const char *</code><i>filename</i>)</dt>
<dd> <p> Create a new raptor read iostream from an existing file <i>filename</i>. </p>
 </dd>
<dt><code>raptor_iostream* raptor_new_iostream_from_file_handle(FILE *</code><i>handle</i>)</dt>
<dd> <p> Create a new raptor read iostream from an already opened, C Standard I/O handle FILE* <i>handler</i>. </p>
 </dd>
<dt><code>raptor_iostream* raptor_new_iostream_from_string(void *</code><i>string</i>, size_t <i>length</i>)</dt>
<dd> <p> Create a new raptor read iostream reading from an existing <i>string</i> of <i>length</i> bytes. </p>
 </dd></dl>
<h2>IOSTREAM DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_iostream(raptor_iostream *</code><i>iostr</i><code>)</code></dt>
<dd> <p> Destroy a Raptor iostream object. </p>
 </dd></dl>
<h2>IOSTREAM METHODS</h2>
<dl>
<dt><code>int raptor_iostream_write_bytes(raptor_iostream *</code><i>iostr</i><code>, const void *</code><i>ptr</i><code>, size_t </code><i>size</i><code>, size_t </code><i>nmemb</i><code>)</code></dt>
<dd> <p> Write a counted set of elements to an iostream. Inmemb is the count of elements of size <i>size</i>, starting at memory <i>ptr</i>. Similar to <a href="/docs/linux/man/3-fwrite/">fwrite</a>(3) and <a href="/docs/linux/man/2-write/">write</a>(2). </p>
 </dd>
<dt><code>int raptor_iostream_write_byte(raptor_iostream *</code><i>iostr</i><code>, const int </code><i>byte</i><code>)</code></dt>
<dd> <p> Write a single <i>byte</i> an iostream. Similar to <a href="/docs/linux/man/3-fputc/">fputc</a>(3). </p>
 </dd>
<dt><code>void raptor_iostream_write_end(raptor_iostream *</code><i>iostr</i><code>)</code></dt>
<dd> <p> Finish writing to an iostream. </p>
 </dd>
<dt><code>int raptor_iostream_write_string(raptor_iostream *</code><i>iostr</i><code>, const void *</code><i>string</i><code>)</code></dt>
<dd> <p> Write a NUL-terminated <i>string</i> to an iostream. Similar to <a href="/docs/linux/man/3-fputs/">fputs</a>(3). </p>
 </dd>
<dt><code>int raptor_iostream_write_counted_string(raptor_iostream *</code><i>iostr</i><code>, const void *</code><i>string</i><code>, size_t </code><i>len</i><code>)</code></dt>
<dd> <p> Write a <i>string</i> of length <i>len</i> to an iostream. </p>
 </dd>
<dt><code>unsigned long raptor_iostream_tell(raptor_iostream *</code><i>iostr</i>)</dt>
<dd> <p> Return the byte offset into the iostream. </p>
 </dd>
<dt><code>size_t raptor_iostream_get_bytes_written_count(raptor_iostream *</code><i>iostr</i><code>)</code></dt>
<dd> <p> DEPRECATED in 1.4.17 for <code>raptor_iostream_tell()</code>. Return the number of bytes written so far to the iostream. </p>
 </dd>
<dt><code>int raptor_iostream_write_decimal(raptor_iostream *</code><i>iostr</i><code>, int </code><i>integer</i><code>)</code></dt>
<dd> <p> Write a decimal formatted integer <i>integer</i> to the iostream. </p>
 </dd>
<dt><code>int raptor_iostream_format_hexadecimal(raptor_iostream *</code><i>iostr</i><code>, unsigned int </code><i>integer</i><code>, int </code><i>width</i><code>)</code></dt>
<dd> <p> Write a hexadecimal formatted unsigned <i>integer</i> to the iostream, left-padded with &#8216;0&#8217;s to <i>width</i> columns. </p>
 </dd>
<dt><code>int raptor_iostream_write_stringbuffer(raptor_iostream* </code><i>iostr</i><code>, raptor_stringbuffer *</code><i>sb</i><code>)</code></dt>
<dd> <p> Write the stringbuffer to an iostream <i>iostr</i>. </p>
 </dd>
<dt><code>int raptor_iostream_read_bytes(raptor_iostream* </code><i>iostr</i>, void *<i>ptr</i>, size_t <i>size</i>, size_t <i>nmemb</i>)</dt>
<dd> <p> Read bytes from the iostream into buffer <i>ptr</i> up to <i>nmemb</i> elements of size <i>size</i>. </p>
 </dd>
<dt><code>int raptor_iostream_read_eof(raptor_iostream *</code><i>iostr</i>)</dt>
<dd> <p> Return non-0 if the iostream is finished. </p>
 </dd></dl>
<h2>XML SAX2 READER CLASS</h2>
<p> This class provides the functionality to generate SAX2 events from parsing XML content, including XML namespace support.  </p>
<h2>XML SAX2 CONSTRUCTOR</h2>
<dl>
<dt><code>raptor_sax2* raptor_new_sax2(void *</code><i>user_data</i>, raptor_error_handlers* <i>error_handlers</i>)</dt>
<dd> <p> Create a new SAX2 XML reader with the given error handler object. </p>
 </dd></dl>
<h2>XML WRITER DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_sax2(raptor_sax2 *</code><i>sax2</i>)</dt>
<dd> <p> Destroy a SAX2 XML reader object. </p>
 </dd></dl>
<h2>SAX2 SET HANDLER METHODS</h2>
<dl>
<dt><code>void raptor_sax2_set_start_element_handler(raptor_sax2 *</code><i>sax2</i>, raptor_sax2_start_element_handler <i>handler</i>)</dt>
<dd> <p> Set the SAX2 start element <i>handler</i>. </p>
 </dd>
<dt><code>void raptor_sax2_set_end_element_handler(raptor_sax2 *</code><i>sax2</i>, raptor_sax2_end_element_handler <i>handler</i>)</dt>
<dd> <p> Set the SAX2 end element <i>handler</i>. </p>
 </dd>
<dt><code>void raptor_sax2_set_characters_handler(raptor_sax2 *</code><i>sax2</i>, raptor_sax2_characters_handler <i>handler</i>)</dt>
<dd> <p> Set the SAX2 character data element <i>handler</i>. </p>
 </dd>
<dt><code>void raptor_sax2_set_cdata_handler(raptor_sax2 *</code><i>sax2</i>, raptor_sax2_cdata_handler <i>handler</i>)</dt>
<dd> <p> Set the SAX2 CDATA section element <i>handler</i>. </p>
 </dd>
<dt><code>void raptor_sax2_set_comment_handler(raptor_sax2 *</code><i>sax2</i>, raptor_sax2_comment_handler <i>handler</i>)</dt>
<dd> <p> Set the SAX2 XML comment <i>handler</i>. </p>
 </dd>
<dt><code>void raptor_sax2_set_unparsed_entity_decl_handler(raptor_sax2 *</code><i>sax2</i>, raptor_sax2_unparsed_entity_decl_handler <i>handler</i>)</dt>
<dd> <p> Set the SAX2 XML unparsed entity declaration <i>handler</i>. </p>
 </dd>
<dt><code>void raptor_sax2_set_external_entity_ref_handler(raptor_sax2 *</code><i>sax2</i>, raptor_sax2_external_entity_ref_handler <i>handler</i>)</dt>
<dd> <p> Set the SAX2 XML external entity reference <i>handler</i>. </p>
 </dd>
<dt><code>void raptor_sax2_set_namespace_handler(raptor_sax2 *</code><i>sax2</i>, raptor_namespace_handler <i>handler</i>)</dt>
<dd> <p> Set the SAX2 XML namespace declaration <i>handler</i> when an XML namespace is declared. </p>
 </dd></dl>
<h2>SAX2 PARSING METHODS</h2>
<dl>
<dt><code>void raptor_sax2_parse_start(raptor_sax2 *</code><i>sax2</i>, raptor_uri *<i>base_uri</i>)</dt>
<dd> <p> Start a SAX2 parse of XML content with the base URI <i>uri</i>. </p>
 </dd>
<dt><code>int raptor_sax2_parse_chunk(raptor_sax2 *</code><i>sax2</i>, const unsigned char *<i>buffer</i>, size_t <i>len</i>, int <i>is_end</i>)</dt>
<dd> <p> Parse the XML content in <i>buffer</i> of size <i>len</i> returning SAX2 events via handlers. If <i>is_end</i> is non-zero, it indicates the end of the parsing. This method can only be called after <code>raptor_sax2_parse_start()</code>. </p>
 </dd></dl>
<h2>SAX2 SCOPE METHODS</h2>
<dl>
<dt><code>const unsigned char* raptor_sax2_inscope_xml_language(raptor_sax2 *</code><i>sax2</i>)</dt>
<dd> <p> Get the current in-scope XML language (xml:lang) value. </p>
 </dd>
<dt><code>raptor_uri* raptor_sax2_inscope_base_uri(raptor_sax2 *</code><i>sax2</i>)</dt>
<dd> <p> Get the current in-scope Base URI (xml:base or document or protocol) value. </p>
 </dd></dl>
<h2>XML ELEMENT CLASS</h2>
<p> This class provides an XML element that can be used with the XML Writer Class to generate XML documents.  </p>
<h2>XML ELEMENT CONSTRUCTORS</h2>
<dl>
<dt><code>raptor_xml_element* raptor_new_xml_element(raptor_qname* </code><i>name</i>, const unsigned char* <i>xml_language</i>, raptor_uri* <i>xml_base</i>)</dt>
<dd> <p> Create a new XML element with the element name <i>name</i> in the context of xml:lang <i>xml_language</i> and base URI <i>xml_base</i>. </p>
 </dd>
<dt><code>raptor_xml_element* raptor_new_xml_element_from_namespace_local_name(raptor_namespace *</code><i>ns</i>, const unsigned char *<i>name</i>, const unsigned char* <i>xml_language</i>, raptor_uri* <i>xml_base</i></dt>
<dd> <p> Create a new XML element based on the given XML <i>namespace</i> and <i>localname</i> in the context of xml:lang <i>xml_languageFP and base URI xml_base</i>. </p>
 </dd></dl>
<h2>XML ELEMENT DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_xml_element(raptor_xml_element *</code><i>element</i>)</dt>
<dd> <p> Destroy a XML element object. </p>
 </dd></dl>
<h2>XML ELEMENT METHODS</h2>
<dl>
<dt><code>raptor_qname* raptor_xml_element_get_name(raptor_xml_element* </code><i>xml_element</i>)</dt>
<dd> <p> Get the XML element QName of XML element <i>xml_element</i>. </p>
 </dd>
<dt><code>void raptor_xml_element_set_attributes(raptor_xml_element* </code><i>xml_element</i>, raptor_qname **<i>attributes</i>, int <i>count</i>)</dt>
<dd> <p> Set the attributes on XML element <i>xml_element</i> to the array of QNames in array <i>attributes</i> of size <i>count</i>. </p>
 </dd>
<dt><code>raptor_qname** raptor_xml_element_get_attributes(raptor_xml_element* </code><i>xml_element</i>)</dt>
<dd> <p> Get the attributes of an XML element <i>xml_element</i> as an array of QNames. As set by <code>void raptor_xml_element_set_attributes</code>. </p>
 </dd>
<dt><code>int raptor_xml_element_get_attributes_count(raptor_xml_element* </code><i>xml_element</i>)</dt>
<dd> <p> Get the number of attributes of an XML element <i>xml_element</i> as set by <code>void raptor_xml_element_set_attributes</code>. </p>
 </dd>
<dt><code>int raptor_xml_element_declare_namespace(raptor_xml_element* </code><i>xml_element</i>, raptor_namespace* <i>nspace</i>)</dt>
<dd> <p> Declare an XML namespace <i>nspace</i> expliclitly on XML element <i>xml_element</i>. Namespaces used in the element or attribute names are automatically declared, this method allows additional ones to be done. </p>
 </dd>
<dt><code>int raptor_xml_element_is_empty(raptor_xml_element*</code><i> xml_element</i>)</dt>
<dd> <p> Return non-0 if the XML element is empty. </p>
 </dd>
<dt><code>int raptor_iostream_write_xml_element(raptor_iostream* </code><i>iostr</i>, raptor_xml_element *<i>element</i>, raptor_namespace_stack* <i>nstack</i>, int <i>is_empty</i>, int <i>is_end</i>, raptor_simple_message_handler <i>error_handler</i>, void* <i>error_data</i>, int <i>depth</i>)</dt>
<dd> <p> Write a XML element <i>xml_element</i> to iostream <i>ostr</i>. This is done in context of an XML namespace stack <i>nstack</i> and at depth <i>depth</i> in the stack (see Namespace class constructors). </p>
 </dd>
<dd> <p> The element may be an empty element if <i>is_empty</i> is non-zero or may be a close element if <i>is_end</i> is non-zero (else is a start element). The <i>error_handler</i> method along with <i>error_data</i> allow error reporting to be given. </p>
 </dd>
<dt><code>const unsigned char* raptor_xml_element_get_language(raptor_xml_element* </code><i>xml_element</i>)b</dt>
<dd> <p> Get the xml:lang language of the XML element. </p>
 </dd></dl>
<h2>XML WRITER CLASS</h2>
<p> This class provides the functionality to generate simple XML documents consisting of elements with attributes, character data and comments. The documents can be written to an iostream.  </p>
<h2>XML WRITER CONSTRUCTOR</h2>
<dl>
<dt><code>raptor_xml_writer* raptor_new_xml_writer(raptor_namespace_stack* </code><i>nstack</i>, raptor_uri_handler* <i>uri_handler</i>, void* <i>uri_context</i>, raptor_iostream* <i>iostr</i>, raptor_simple_message_handler <i>error_handler</i>, void *<i>error_data</i>, int <i>canonicalize</i>)</dt>
<dd> <p> Create a new XML Writer writing to iostream <i>iostr</i>. The <i>error_handler</i> method along with <i>error_data</i> allow error reporting to be given. <i>nstack</i> is either an existing namespace stack to be used or if NULL, a new one with only the XML namespace defined is created. Note that <code>raptor_uri_get_handler</code> can be useful to return the current raptor URI handler/context. <i>canonicalize</i> is currently unused and should be set to 1 but may allow non-canonical XML writing to be allowed in future. </p>
 </dd></dl>
<h2>XML WRITER DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_xml_writer(raptor_xml_writer* </code><i>xml_writer</i>)</dt>
<dd> <p> Destroy a XML Writer object. </p>
 </dd></dl>
<h2>XML WRITER METHODS</h2>
<dl>
<dt><code>void raptor_xml_writer_empty_element(raptor_xml_writer* </code><i>xml_writer</i>, raptor_xml_element *<i>element</i>)</dt>
<dd> <p> Write XML element <i>element</i> as an empty element (no element content) to the XML Writer <i>xml_writer</i>. </p>
 </dd>
<dt><code>void raptor_xml_writer_start_element(raptor_xml_writer* </code><i>xml_writer</i>, raptor_xml_element *<i>element</i>)</dt>
<dd> <p> Write a start element along with an attributes and namespace declarations for XML element <i>element</i> to the XML Writer <i>xml_writer</i>. </p>
 </dd>
<dt><code>void raptor_xml_writer_end_element(raptor_xml_writer* </code><i>xml_writer</i>, raptor_xml_element *<i>element</i>)</dt>
<dd> <p> Write an end element form for XML element <i>element</i> to the XML Writer <i>xml_writer</i>. </p>
 </dd>
<dt><code>void raptor_xml_writer_cdata(raptor_xml_writer* </code><i>xml_writer</i>, const unsigned char *str)</dt>
<dd> <p> Write XML character data in <i>str</i> to the XML Writer <i>xml_writer</i>. The characters in <i>str</i> will be XML escaped. </p>
 </dd>
<dt><code>void raptor_xml_writer_cdata_counted(raptor_xml_writer* </code><i>xml_writer</i>, const unsigned char* <i>str</i>, unsigned int <i>length</i>)</dt>
<dd> <p> Write XML character data in <i>str</i> of length <i>length</i> to the XML Writer <i>xml_writer</i>. The characters in <i>str</i> will be XML escaped. </p>
 </dd>
<dt><code>void raptor_xml_writer_raw(raptor_xml_writer* </code><i>xml_writer</i>, const unsigned char* <i>str</i>)</dt>
<dd> <p> Write character data in <i>str</i> <i>length</i> to the XML Writer <i>xml_writer</i> without XML escaping. </p>
 </dd>
<dt><code>void raptor_xml_writer_raw_counted(raptor_xml_writer* </code><i>xml_writer</i>, const unsigned char* <i>str</i>, unsigned int <i>length</i>)</dt>
<dd> <p> Write character data in <i>str</i> of length <i>length</i> to the XML Writer <i>xml_writer</i> without XML escaping. </p>
 </dd>
<dt><code>void raptor_xml_writer_comment(raptor_xml_writer* </code><i>xml_writer</i>, const unsigned char* <i>str</i>)</dt>
<dd> <p> Write an XML comment in <i>str</i> to the XML Writer <i>xml_writer</i>. </p>
 </dd>
<dt><code>void raptor_xml_writer_comment_counted(raptor_xml_writer* </code><i>xml_writer</i>, const unsigned char* <i>str</i>, unsigned int <i>length</i>)</dt>
<dd> <p> Write an XML comment in <i>str</i> of length <i>length</i> to the XML Writer <i>xml_writer</i>. </p>
 </dd>
<dt><code>int raptor_xml_writer_features_enumerate(const raptor_feature </code><i>feature</i>, const char **<i>name</i>, raptor_uri **<i>uri</i>, const char **<i>label</i>)</dt>
<dd> <p> Return the name, URI, string label (all optional) for an XML write <i>feature</i>, returning non-zero if no such feature exists. Raptor features have URIs that are constructed from the URI <i><a rel="nofollow" href="http://feature.librdf.org/raptor-">http://feature.librdf.org/raptor-</a></i> and the <i>name</i> so for example feature <i>scanForRDF</i> has URI <i><a rel="nofollow" href="http://feature.librdf.org/raptor-scanForRDF">http://feature.librdf.org/raptor-scanForRDF</a></i> </p>
 </dd>
<dt><code>int raptor_xml_writer_set_feature(raptor_xml_writer* </code><i>xml_writer</i>, raptor_feature <i>feature</i>, int <i>value</i>)</dt>
<dd> <p> Set an XML writer feature <i>feature</i> to a particular <i>value</i>. Returns non 0 on failure or if the feature is unknown. The current defined writer features are: <br />
&nbsp;<wbr>&nbsp;<wbr><i>Feature&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Values</i> <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WRITER_AUTO_INDENT</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WRITER_AUTO_EMPTY</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WRITER_INDENT_WIDTH</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Integer <br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WRITER_XML_DECLARATION</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true) If the <i>writer_auto_indent</i> feature is set (default true), the XML writer will automatically indent the output. If the <i>writer_auto_empty</i> feature is set (default true), the XML writer will automatically generate empty elements if a start/end element sequence has no content. If the <i>writer_indent_width</i> feature is set (default 2) if the XML writer is outputing indented XML, it will use that many spaces. If the <i>writer_xml_declaration</i> feature is set (default true) the XML declaration is written at the start of serialized XML. </p>
 </dd>
<dt><code>int raptor_xml_writer_set_feature_string(raptor_xml_writer *xml_writer, raptor_feature feature, const unsigned char *value)</code></dt>
<dd> <p> Set an XML writer feature <i>feature</i> to a particular string <i>value</i>. Returns non 0 on failure or if the feature is unknown. The current defined XML writer features are given in <code>raptor_xml_writer_set_feature</code> and at present only take integer values. If an integer value feature is set with this function, <i>value</i> is interpreted as an integer and then that value is used. </p>
 </dd>
<dt><code>int raptor_xml_writer_get_feature(raptor_xml_writer* </code><i>xml_writer</i>, raptor_feature <i>feature</i>)</dt>
<dd> <p> Get XML writer feature integer values. The allowed <i>feature</i> values and types are given under <code>raptor_xml_writer_features_enumerate</code>. </p>
 </dd>
<dt><code>const unsigned char *raptor_xml_writer_get_feature_string(raptor_xml_writer* </code><i>xml_writer</i>, raptor_feature <i>feature</i>)</dt>
<dd> <p> Get XML writer feature string values. The allowed <i>feature</i> values and types are given under <code>raptor_xml_writer_features_enumerate</code>. </p>
 </dd>
<dt><code>int raptor_xml_writer_get_depth(raptor_xml_writer* </code><i>xml_writer</i>)</dt>
<dd> <p> Get the current XML writer element stack depth. </p>
 </dd>
<dt><code>void raptor_xml_writer_flush(raptor_xml_writer* </code><i>xml_writer</i>)</dt>
<dd> <p> Flush the XML writer output for any pending writes. </p>
 </dd>
<dt><code>void raptor_xml_writer_newline(raptor_xml_writer* </code><i>xml_writer</i>)</dt>
<dd> <p> Write a newline to the XML writer (which may trigger indenting before the next item). </p>
 </dd></dl>
<h2>API CHANGES</h2>
<h3>1.4.18</h3>
<p> Added atom serializer </p>
<p> Added rdfa parser </p>
<p> Added serializer features RAPTOR_FEATURE_RSS_TRIPLES and RAPTOR_FEATURE_ATOM_ENTRY_URI </p>
<p> Added raptor_qname_to_counted_name </p>
<p> Added raptor_serialize_start_to_iostream </p>
<p> Added raptor_sequence_delete_at </p>
<p> Added raptor_xml_writer_newline </p>
<p> Added raptor_xml_writer_flush </p>
<p> Added raptor_xml_writer_get_depth  </p>
<h3>1.4.17</h3>
<p> Added SAX2 class <code>raptor_sax2</code>. Added new SAX2 API typedefs: <code>raptor_sax2_start_element_handler</code>, <code>raptor_sax2_end_element_handler</code>, <code>raptor_sax2_characters_handler</code>, <code>raptor_sax2_cdata_handler</code>, <code>raptor_sax2_comment_handler</code>, <code>raptor_sax2_unparsed_entity_decl_handler</code> and <code>raptor_sax2_external_entity_ref_handler</code>. Added new SAX2 API functions: <code>raptor_new_sax2()</code>, <code>raptor_free_sax2()</code>, <code>raptor_sax2_set_start_element_handler()</code>, <code>raptor_sax2_set_end_element_handler()</code>, <code>raptor_sax2_set_characters_handler()</code>, <code>raptor_sax2_set_cdata_handler()</code>, <code>raptor_sax2_set_comment_handler()</code>, <code>raptor_sax2_set_unparsed_entity_decl_handler()</code>, <code>raptor_sax2_set_external_entity_ref_handler()</code>, <code>raptor_sax2_set_namespace_handler()</code>, <code>raptor_sax2_parse_start()</code>, <code>raptor_sax2_parse_chunk()</code>, <code>raptor_sax2_inscope_xml_language()</code> and <code>raptor_sax2_inscope_base_uri()</code> </p>
<p> Added features <code>RAPTOR_FEATURE_WRITE_BASE_URI</code>, <code>RAPTOR_FEATURE_WWW_HTTP_CACHE_CONTROL</code>, <code>RAPTOR_FEATURE_WWW_HTTP_USER_AGENT</code>, <code>RAPTOR_FEATURE_JSON_CALLBACK</code> and <code>RAPTOR_FEATURE_JSON_EXTRA_DATA</code> </p>
<p> Added <code>raptor_handler_closure</code> structure for error handlers. </p>
<p> Added <code>raptor_statement_compare()</code> </p>
<p> Added <code>raptor_iostream_write_string_python()</code> and deprecated <code>raptor_iostream_write_string_turtle()</code> </p>
<p> <code>raptor_uri_set_handler()</code>, <code>raptor_uri_get_handler()</code>, <code>raptor_new_namespaces()</code>, <code>raptor_namespaces_init()</code> and <code>raptor_new_xml_writer()</code> now take const handler pointers. </p>
<p> Added <code>raptor_www_set_http_cache_control()</code> </p>
<p> Added QName class methods: <code>raptor_qname_get_local_name()</code>, <code>raptor_qname_get_value()</code> and <code>raptor_qname_get_counted_value()</code> </p>
<p> Added <code>raptor_iostream</code> read handler typedefs <code>raptor_iostream_read_bytes_func</code>, <code>raptor_iostream_read_eof_func</code> and added new structure <code>raptor_iostream_handler2</code> replacing deprecated <code>raptor_iostream_handler</code>. </p>
<p> Added <code>raptor_new_iostream_from_handler2()</code> replacing deprecated <code>raptor_new_iostream_from_handler()</code> </p>
<p> Added <code>raptor_new_iostream_from_sink()</code>, <code>raptor_new_iostream_from_filename()</code>, <code>raptor_new_iostream_from_file_handle()</code> and <code>raptor_new_iostream_from_string()</code>. </p>
<p> Added <code>raptor_iostream_tell</code> deprecating <code>raptor_iostream_get_bytes_written_count()</code>. </p>
<p> Added <code>raptor_iostream_read_bytes()</code> and <code>raptor_iostream_read_eof()</code>. </p>
<p> Added <code>raptor_xml_element_get_language()</code>. </p>
<p> Added new enum <code>raptor_log_level</code>. </p>
<p> Added new typedef <code>raptor_error_handlers</code>. and new function <code>raptor_error_handlers_init()</code>.  </p>
<h3>1.4.16</h3>
<p> <code>raptor_namespaces_init</code> now returns an integer status </p>
<p> Added <code>raptor_new_xml_element_from_namespace_local_name</code> </p>
<p> Added <code>raptor_uri_compare</code>. </p>
<p> Added new features for the &#8216;grddl&#8217; parser: RAPTOR_FEATURE_HTML_TAG_SOUP, RAPTOR_FEATURE_MICROFORMATS and RAPTOR_FEATURE_HTML_LINK. </p>
<p> Added parser feature RAPTOR_FEATURE_WWW_TIMEOUT </p>
<p> Added raptor_graph_handler typedef and <code>raptor_set_graph_handler</code> </p>
<p> Added raptor_www_final_uri_handler typedef and <code>raptor_www_set_final_uri_handler</code> </p>
<p> Added <code>raptor_www_set_connection_timeout</code> </p>
<p> Added <code>raptor_www_get_final_uri</code>  </p>
<h3>1.4.15</h3>
<p> No changes.  </p>
<h3>1.4.14</h3>
<p> Add two new exported strings raptor_license_string and raptor_home_url_string. </p>
<p> Added new features for the &#8216;dot&#8217; serializer: RAPTOR_FEATURE_RESOURCE_BORDER, RAPTOR_FEATURE_LITERAL_BORDER, RAPTOR_FEATURE_BNODE_BORDER, RAPTOR_FEATURE_RESOURCE_FILL, RAPTOR_FEATURE_LITERAL_FILL and RAPTOR_FEATURE_BNODE_FILL </p>
<p> Added <code>raptor_parser_generate_id</code> </p>
<p> Added <code>raptor_iostream_write_string_turtle</code>  </p>
<h3>1.4.13</h3>
<p> No API changes.  </p>
<h3>1.4.12</h3>
<p> No API changes.  </p>
<h3>1.4.11</h3>
<p> Added <code>raptor_get_feature_count</code> </p>
<p> Added <code>raptor_get_need_base_uri</code> </p>
<p> Added parser feature <code>RAPTOR_FEATURE_NO_NET</code> </p>
<p> Added <code>raptor_www_set_uri_filter</code>, <code>raptor_parser_set_uri_filter</code> with filter type <code>raptor_uri_filter_func</code>  </p>
<h3>1.4.10</h3>
<p> No API changes.  </p>
<h3>1.4.9</h3>
<p> Added <code>raptor_parser_get_accept_header</code> </p>
<p> Added <code>raptor_xml_element_is_empty</code> </p>
<p> Added <code>raptor_qname_get_namespace</code> </p>
<p> Added <code>raptor_iostream_write_uri</code> </p>
<p> Added <code>raptor_namespaces_qname_from_uri</code>. </p>
<p> Added <code>raptor_namespace_get_counted_prefix</code> </p>
<p> Added <code>raptor_serialize_set_namespace_from_namespace</code> </p>
<p> Deprecated <code>raptor_uri_is_file_uri</code> for new <code>raptor_uri_string_is_file_uri</code>. </p>
<p> Added <code>raptor_xml_element_get_attributes</code> and <code>raptor_xml_element_get_attributes_count</code>  </p>
<h3>1.4.8</h3>
<p> Added <code>raptor_set_namespace_handler</code>. </p>
<p> Added XML 1.1 serializing support, feature <code>RAPTOR_FEATURE_WRITER_XML_VERSION</code> with shortname <i>xmlVersion</i> for serializer and xml writer classes to support it. Added XML writer feature <code>RAPTOR_FEATURE_WRITER_XML_DECLARATION</code> to control generation of the XML declaration. Added new functions <code>raptor_xml_any_escape_string</code> and <code>raptor_iostream_write_xml_any_escaped_string</code> to allow generating XML 1.1 or XML 1.0. </p>
<p> <code>RAPTOR_IDENTIFIER_TYPE_PREDICATE</code> will no longer be generated from version 1.4.9 onwards as the type of returned statement predicates. <code>RAPTOR_IDENTIFIER_TYPE_RESOURCE</code> will be returned. </p>
<p> <code>RAPTOR_IDENTIFIER_TYPE_ORDINAL</code> may no longer be generated from version 1.4.9 onwards, <code>RAPTOR_IDENTIFIER_TYPE_RESOURCE</code> may replace it.  </p>
<h3>1.4.7</h3>
<p> No changes.  </p>
<h3>1.4.6</h3>
<p> No changes.  </p>
<h3>1.4.5</h3>
<p> Deprecated <code>raptor_ntriples_string_as_utf8_string</code> (never documented above) since it can only work with a raptor_parser object which makes it rather unusable alone. Added XML writer features and support functions <code>raptor_xml_writer_features_enumerate</code>, <code>raptor_xml_writer_set_feature</code>, <code>raptor_xml_writer_set_feature_string</code>, <code>raptor_xml_writer_get_feature</code> and <code>raptor_xml_writer_get_feature_string</code>  </p>
<h3>1.4.3</h3>
<p> Added XML Writer class (<code>raptor_xml_writer</code>) and XML Element class (<code>raptor_xml_element</code>) Added <code>raptor_parser_get_feature_string</code>, <code>raptor_parser_set_feature_string</code>, <code>raptor_serializer_set_feature_string</code>, <code>raptor_serializer_get_feature_string</code> and <code>raptor_feature_value_type</code>. Added <code>raptor_serializer_set_namespace</code>, <code>raptor_serializer_set_feature</code> and <code>raptor_serializer_get_feature</code>. Added <code>raptor_new_namespace_from_uri</code>, <code>raptor_new_namespace_parts_from_string</code>, Added <code>raptor_namespaces_find_namespace_by_uri</code>. and <code>raptor_iostream_write_namespace</code> to write a namespace declaration to an iostream. Added copy constructor <code>raptor_qname_copy</code> and <code>raptor_iostream_write_qname</code> to write a qname to an iostream. Added <code>raptor_sequence_join</code> to join two sequences, leaving one empty. Added <code>raptor_iostream_write_stringbuffer</code> to write a stringbuffer to an iostream. Added N-Triples <code>raptor_iostream_write_string_ntriples</code> and <code>raptor_iostream_write_statement_ntriples</code> utility functions for writing to raptor_iostreams. Added <code>raptor_uri_to_relative_counted_uri_string</code>, <code>raptor_uri_to_relative_uri_string</code>. <code>raptor_uri_print</code>, <code>raptor_uri_to_counted_string</code> and <code>raptor_uri_to_string</code> Added unicode name checking utility functions for XML 1.0 and XML 1.1 name starting character and continued name character. <code>raptor_unicode_is_xml10_namestartchar</code> <code>raptor_unicode_is_xml10_namechar</code>, <code>raptor_unicode_is_xml11_namechar</code> and <code>raptor_unicode_is_xml11_namestartchar</code>. Added <code>raptor_xml_name_check</code> to check if a name is a legal XML 1.0 or 1.0 name. and <code>raptor_iostream_write_xml_escaped_string</code> to write an XML-escaped string to an iostream. Added UTF8-checking utility function <code>raptor_utf8_check</code>.  </p>
<h3>1.4.2</h3>
<p> No changes.  </p>
<h3>1.4.1</h3>
<p> The <code>raptor_xml_escape_string</code> now returns &lt;0 on failure rather than 0, so that if an empty string is escaped, 0 bytes required is returned.  </p>
<h3>1.4.0</h3>
<p> Added new <code>raptor_serializer</code> class supporting RDF/XML (name <code>rdfxml</code>) and N-Triples (name <code>ntriples</code>). <br />
 Added new <code>raptor_iostream</code> class <br />
 Added <code>raptor_stringbuffer_copy_to_string</code> to allow efficient copy-out of a constructed string. <br />
 Added <code>raptor_www_fetch_to_string</code> to allow retrieving of web content as a single string.  </p>
<h3>1.3.3</h3>
<p> Added <code>raptor_calloc_memory</code> to provide a calloc inside raptor. <br />
 Added feature check_rdf_id (see raptor_set_feature documentation).  </p>
<h3>1.3.2</h3>
<p> Added <code>raptor_alloc_memory</code> to allocate memory inside raptor. </p>
<p> Added accessor functions for the public raptor_locator structure: </p>
<p> <code>raptor_locator_line</code> <br />
 <code>raptor_locator_column</code> <br />
 <code>raptor_locator_byte</code> <br />
 <code>raptor_locator_file</code> <br />
 <code>raptor_locator_uri</code>  </p>
<h3>1.3.1</h3>
<p> Correct raptor_print_statement declaration argument statement to have one less &#8216;const&#8217;, to match the code.  </p>
<h3>1.3.0</h3>
<p> Added the following parser methods, utility methods and helper functions: </p>
<p> <code>raptor_new_parser_for_content (Parser class constructor)</code> <br />
 <code>raptor_get_mime_type</code> <br />
 <code>raptor_get_feature</code> <br />
 <code>raptor_syntax_name_check</code> <br />
 <code>raptor_guess_parser_name</code> <br />
 <code>raptor_features_enumerate</code> <br />
 <code>raptor_feature_from_uri</code> <br />
 <code>raptor_www_set_http_accept (WWW class)</code> </p>
<p> Changed <code>raptor_set_feature</code> to now return an int success or failure. </p>
<p> Added the following functions: <br />
 <code>raptor_free_memory</code> <br />
 <code>raptor_unicode_char_to_utf8</code> <br />
 <code>raptor_utf8_to_unicode_char</code> <br />
 <code>raptor_vsnprintf</code> </p>
<p> Added the raptor_sequence class, its constructor, destructor, methods and helper functions. </p>
<p> Added the raptor_stringbuffer class and constructor, destructor and methods. </p>
<p> Deprecated <code>raptor_print_statement_detailed</code> always intended to be internal.  </p>
<h3>1.2.0</h3>
<p> Added <code>raptor_syntaxes_enumerate</code> to get full information on syntax mime type and URIs as well as name and label. </p>
<p> N-Triples Plus parser renamed to Turtle (name turtle)  </p>
<h3>1.1.0</h3>
<p> Added N-Triples Plus parser (name ntriples-plus) </p>
<p> Made URI class constructors, methods and factory methods as well as some other utility functions using or returning URIs or literals take unsigned char* rather than char*. The affected calls are: </p>
<p> URI factory methods changed to all take/return unsigned char* for URI strings: <br />
 <code>raptor_new_uri_func</code> <br />
 <code>raptor_new_uri_from_local_name_func</code> <br />
 <code>raptor_new_uri_relative_to_base_func</code> <br />
 <code>raptor_uri_as_string_func</code> <br />
 <code>raptor_uri_as_counted_string_func</code> </p>
<p> Constructors and methods changed to take/return unsigned char* for URI strings: <br />
 <code>raptor_statement_part_as_counted_string</code> <br />
 <code>raptor_statement_part_as_string</code> <br />
 <code>raptor_new_uri</code> <br />
 <code>raptor_new_uri_from_uri_local_name</code> <br />
 <code>raptor_new_uri_relative_to_base</code> <br />
 <code>raptor_uri_as_string</code> <br />
 <code>raptor_uri_as_counted_string</code> <br />
 <code>raptor_print_ntriples_string</code> </p>
<p> Changed to use unsigned char* for URI strings, char* for filenames: <br />
 <code>raptor_uri_resolve_uri_reference</code> <br />
 <code>raptor_uri_filename_to_uri_string</code> <br />
 <code>raptor_uri_uri_string_to_filename</code> <br />
 <code>raptor_uri_uri_string_to_filename_fragment</code> <br />
 <code>raptor_uri_is_file_uri</code> </p>
<p> Changed to return unsigned char* for UTF8 string: <br />
 <code>raptor_ntriples_string_as_utf8_string</code> </p>
<p> Added <code>raptor_parsers_enumerate</code> to discover supported parsers. </p>
<p> Added <code>raptor_uri_uri_string_to_filename_fragment</code> with fragment arg to return the URI fragment. </p>
<p> Made the raptor_namespace, raptor_namespace_stack and raptor_qname class and APIs public. </p>
<p> Added feature non_nfc_fatal (see raptor_set_feature documentation).  </p>
<h3>1.0.0</h3>
<p> Removed the following deprecated methods and functions (see 0.9.6 changes for the new names): <br />
 <code>raptor_free</code>, <code>raptor_new</code>, <code>raptor_ntriples_free</code>, <code>raptor_ntriples_new</code>, <code>raptor_ntriples_parse_file</code>, <code>raptor_ntriples_set_error_handler</code>, <code>raptor_ntriples_set_fatal_error_handler</code>, <code>raptor_ntriples_set_statement_handler</code> and <code>raptor_parser_abort</code>. </p>
<p> Added <code>raptor_parse_file_stream</code> for reading FILE* streams without necessarily having a file.  </p>
<h3>0.9.12</h3>
<p> Added <code>raptor_new_uri_for_retrieval</code> to turn URI references into URIs suitable for retrieval (no fragments).  </p>
<h3>0.9.11</h3>
<p> Added <code>raptor_get_name</code> and <code>raptor_get_label</code>. </p>
<p> <code>raptor_xml_escape_string</code> now takes error message handler, data pointer, loses parser argument. </p>
<p> Added <code>raptor_set_default_generate_id_parameters</code> and <code>raptor_set_generate_id_handler</code> to control the default generation of IDs, allow full customisation.  </p>
<h3>0.9.10</h3>
<p> Added <code>raptor_set_parser_strict</code> and <code>raptor_www_no_www_library_init_finish</code>. </p>
<p> <code>raptor_xml_escape_string</code> now takes an output string length pointer. </p>
<p> Added <code>raptor_statement_part_as_counted_string</code>, <code>raptor_statement_part_as_string and raptor_parse_abort</code>. </p>
<p> Deprecated <code>raptor_parser_abort</code>.  </p>
<h3>0.9.9</h3>
<p> Added raptor_www class and all its constructors, destructor, methods, calls. </p>
<p> Added <code>raptor_parse_uri</code>, <code>raptor_parser_abort</code>, <code>raptor_ntriples_term_as_string</code> and <code>raptor_xml_escape_string</code>.  </p>
<h3>0.9.7</h3>
<p> <code>raptor_parse_chunk, raptor_new_uri_from_id</code>, arguments are now unsigned char. </p>
<p> Added <code>raptor_new_uri_for_xmlbase</code>.  </p>
<h3>0.9.6</h3>
<p> In this version, the raptor/ntriples parser calling APIs were modified. The following table lists the changes: </p>
<p> <i>OLD API <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>NEW API (0.9.6+)</i><br />
 <br />
 <code>raptor_new()</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>raptor_new_parser(&quot;rdfxml&quot;)</code><br />
 <br />
 <code>ntriples_new()</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>raptor_new_parser(&quot;ntriples&quot;)</code><br />
 <br />
 <code>raptor_free</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>raptor_free_parser</code><br />
 <br />
 <code>ntriples_free</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>raptor_ntriples_parser</code><br />
 <br />
 <code>raptor_ntriples_parse_file</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>raptor_parse_file</code><br />
 <br />
 <code>raptor_ntriples_set_error_handler</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>raptor_set_error_handler</code><br />
 <br />
 <code>raptor_ntriples_set_fatal_error_handler</code><code>&nbsp;<wbr></code><code>raptor_set_fatal_error_handler</code><br />
 <br />
 <code>raptor_ntriples_set_statement_handler</code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><code>raptor_set_statement_handler</code><br />
 <br />
  </p>
<h2>CONFORMING TO</h2>
<p> <i>RDF/XML Syntax (Revised)</i>, Dave Beckett (ed.) W3C Recommendation, <a rel="nofollow" href="http://www.w3.org/TR/rdf-syntax-grammar/">http://www.w3.org/TR/rdf-syntax-grammar/</a> </p>
<p> <i>N-Triples</i>, in <i>RDF Test Cases</i>, Jan Grant and Dave Beckett (eds.) W3C Recommendation, <a rel="nofollow" href="http://www.w3.org/TR/rdf-testcases/#ntriples">http://www.w3.org/TR/rdf-testcases/#ntriples</a> </p>
<p> <i>Turtle - Terse RDF Triple Language</i>, Dave Beckett, <a rel="nofollow" href="http://www.dajobe.org/2004/01/turtle/">http://www.dajobe.org/2004/01/turtle/</a> </p>
<p> <i>RSS 0.91 spec revision 3</i>, Dan Libby, Netscape, <a rel="nofollow" href="http://my.netscape.com/publish/formats/rss-spec-0.91.html">http://my.netscape.com/publish/formats/rss-spec-0.91.html</a> </p>
<p> <i>RDF Site Summary (RSS) 1.0</i>, <a rel="nofollow" href="http://purl.org/rss/1.0/spec">http://purl.org/rss/1.0/spec</a> </p>
<p> <i>Atom 1.0 syndication format</i>, RFC 4287, <a rel="nofollow" href="http://www.ietf.org/rfc/rfc4287.txt">http://www.ietf.org/rfc/rfc4287.txt</a> </p>
<p> <i>Gleaning Resource Descriptions from Dialects of Languages (GRDDL)</i>, Dan Connolly (ed.), W3C Recommendation, 2007-09-11, <a rel="nofollow" href="http://www.w3.org/TR/2007/REC-grddl-20070911/">http://www.w3.org/TR/2007/REC-grddl-20070911/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rapper/">rapper</a>(1),</code><a href="/docs/linux/man/1-raptor-config/">raptor-config</a>(1)  </p>
<h2>AUTHOR</h2>
<p> Dave Beckett - <a rel="nofollow" href="http://purl.org/net/dajobe/">http://purl.org/net/dajobe/</a> </p>
