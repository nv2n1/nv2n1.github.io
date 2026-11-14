---
title: "libraptor(3)"
name: "libraptor"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libraptor/"
description: "libraptor – Raptor RDF parser and serializer library"
---

<h2 class="name">NAME</h2>
<p> libraptor &#8211; Raptor RDF parser and serializer library </p>
<h2>SYNOPSIS</h2>
<pre>
<code>#include &lt;<a href="file:/usr/include/raptor.h">raptor.h</a>&gt;</code>
<br>
<br>
<code>raptor_init();</code>
<br>
<code>raptor_parser *</code><i>p</i><code>=raptor_new_parser(rdfxml);</code>
<br>
<code>raptor_set_statement_handler(</code><i>p</i><code>,</code><i>NULL</i><code>,</code><i>print_triples</i><code>);</code>
<br>
<code>raptor_uri *</code><i>file_uri</i><code>=raptor_new_uri(<a rel="nofollow" href="http://example.org/">http://example.org/</a>);</code>
<br>
<code>raptor_parse_file(</code><i>p</i><code>,</code><i>file_uri</i><code>,</code><i>base_uri</i><code>);</code>
<br>
<code>raptor_parse_uri(</code><i>p</i><code>,</code><i>uri</i><code>,</code><i>NULL</i><code>);</code>
<br>
<code>raptor_free_parser(</code><i>p</i><code>);</code>
<br>
<code>raptor_free_uri(</code><i>file_uri</i><code>);</code>
<br>
<code>raptor_finish();</code>
<br>
<code>cc file.c -lraptor</code>
<br>
</pre>
<h2>DESCRIPTION</h2>
<p> The <i>Raptor</i> library provides a high-level interface to a set of parsers and serializers that generate Resource Description Framework (RDF) triples by parsing syntaxes or serialize the triples into syntaxes. </p>
<p> The supported parsing syntaxes are RDF/XML, N-Triples, Turtle, RSS tag soup including Atom 0.3 and the serializing syntaxes are RDF/XML, N-Triples and RSS 1.0. The RDF/XML parser can use either <i>expat</i> or <i>libxml</i> XML parsers for providing the SAX event stream. The library functions are arranged in an object-oriented style with constructors, destructors and method calls. The statements and error messages are delivered via callback functions. </p>
<p> Raptor contains a URI-reference parsing and resolving (not retrieval) class (raptor_uri) sufficient for dealing with URI-references inside RDF. This functionality is modular and can be transparently replaced with another existing and compatible URI implementation. </p>
<p> It also provides a URI-retrieval class (raptor_www) for wrapping existing library such as libcurl, libxml2 or BSD libfetch that provides full or partial retrieval of data from URIs and an I/O stream abstraction (raptor_iostream) for supportin serializing to a variety of outputs. </p>
<p> Raptor uses Unicode strings for RDF literals and URIs and preserves them throughout the library. It uses the UTF-8 encoding of Unicode at the API for passing in or returning Unicode strings. It is intended that the preservation of Unicode for URIs will support Internationalized Resource Identifiers (IRIs) which are still under development and standardisation.</p>
<h2>LIBRARY INITIALISATION AND CLEANUP</h2>
<dl>
<dt><code>raptor_init()</code></p>
<dd>
<dt><code>raptor_finish()</code></p>
<dd> Initialise and cleanup the library. These must be called before any raptor class such as raptor_parser, raptor_uri is created or used.</dl>
<h2>PARSER CLASS</h2>
<p> This class provides the functionality of turning syntaxes into RDF triples &#8211; RDF parsing.</p>
<h2>PARSER CONSTRUCTORS</h2>
<dl>
<dt><code>raptor_parser* raptor_new_parser(name)</code></p>
<dd> Create a new raptor parser object for the parser with name <i>name</i> currently either &quot;rdfxml&quot;, &quot;turtle&quot; or &quot;rss-tag-soup&quot; for the RSS Tag Soup parser.</p>
<dt><code>raptor_parser* raptor_new_parser_for_content(raptor_uri *</code><i>uri</i>, const char *<i>mime_type</i>, const unsigned char *<i>buffer</i>, size_t <i>len</i>, const unsigned char *<i>identifier</i>)</p>
<dd> Create a new raptor parser object for a syntax identified by URI <i>uri</i>, MIME type <i>mime_type</i>, some initial content <i>buffer</i> of size <i>len</i> or content with identifier <i>identifier</i>. See the raptor_guess_parser_name description for further details.</dl>
<h2>PARSER DESTRUCTOR</h2>
<dl>
<dt><code>void raptor_free_parser(raptor_parser *</code><i>parser</i><code>)</code></p>
<dd> Destroy a Raptor parser object.</dl>
<h2>PARSER MESSAGE CALLBACK METHODS</h2>
<p> Several methods can be registered for the parser that return a variable-argument message in the style of <a href="/docs/linux/man/3-printf/">printf</a>(3). These also return a <i>raptor_locator</i> that can contain URI, file, line, column and byte counts of where the message is about. This structure can be used with the raptor_format_locator, raptor_print_locator functions below or the structures fields directly, which are defined in raptor.h</p>
<dl>
<dt><code>void raptor_set_fatal_error_handler(raptor_parser* </code><i>parser, void *user_data, raptor_message_handler handler)</i></p>
<dd> Set the parser fatal error handler callback.</p>
<dt><code>void raptor_set_error_handler(raptor_parser* </code><i>parser</i><code>, void *</code><i>user_data</i><code>, raptor_message_handler </code><i>handler</i><code>)</code></p>
<dd> Set the parser non-fatal error handler callback.</p>
<dt><code>void raptor_set_warning_handler(raptor_parser* </code><i>parser</i><code>, void *</code><i>user_data</i><code>, raptor_message_handler </code><i>handler</i><code>)</code></p>
<dd> Set the parser warning message handler callback.</p>
<dt><code>raptor_set_namespace_handler(raptor_parser* </code><i>parser</i>, void* <i>user_data</i>, raptor_namespace_handler <i>handler</i>)</p>
<dd> Set the namespace declaration handler callback.</dl>
<h2>PARSER STATEMENT CALLBACK METHOD</h2>
<p> The parser allows the registration of a callback function to return the statements to the application.</p>
<dl>
<dt><code>void raptor_set_statement_handler(raptor_parser* </code><i>parser</i><code>, void *</code><i>user_data</i><code>, raptor_statement_handler </code><i>handler</i><code>)</code></p>
<dd> Set the statement callback function for the parser. The <i>raptor_statement</i> structure is defined in raptor.h and includes fields for the subject, predicate, object of the statements along with their types and for literals, language and datatype.</dl>
<h2>PARSER PARSING METHODS</h2>
<p> These methods perform the entire parsing in one method. Statements warnings, errors and fatal errors are delivered via the registered statement, error etc. handler functions. </p>
<p> In both of these methods, the base URI is required for the RDF/XML parser (name &quot;rdfxml&quot;) and Turtle parser (name &quot;turtle&quot;). The N-Triples parser (name &quot;ntriples&quot;) or RSS Tag Soup parser (name &quot;rss-tag-soup&quot;) do not use this.</p>
<dl>
<dt><code>int raptor_parse_file(raptor_parser* </code><i>parser</i><code>, raptor_uri *</code><i>uri</i><code>, raptor_uri *</code><i>base_uri</i><code>)</code></p>
<dd> Parse the given filename (a URI like file:filename) according to the optional base URI <i>base_uri</i>. If <i>uri</i> is NULL, read from standard input and <i>base_uri</i> is then required.</p>
<dt><code>int raptor_parse_file_stream(raptor_parser* </code><i>parser</i><code>, FILE* </code><i>stream</i><code>, const char* </code><i>filename</i><code>, raptor_uri *</code><i>base_uri</i><code>)</code></p>
<dd> Parse the given C FILE* stream according to the base URI <i>base_uri</i> (required). <i>filename</i> is optional and if given, is used for error messages via the raptor_locator structure.</p>
<dt><code>int raptor_parse_uri(raptor_parser* </code><i>parser</i><code>, raptor_uri* </code><i>uri</i><code>, raptor_uri *</code><i>base_uri</i><code>)</code></p>
<dd> Parse the URI according to the base URI <i>base_uri</i>, or NULL if not needed. If no base URI is given, the <i>uri</i> is used. This method depends on the raptor_www subsystem (see <code>WWW Class</code> section below) and an existing underlying URI retrieval implementation such as libcurl, libxml or BSD libfetch to retrieve the content.</dl>
<h2>PARSER CHUNKED PARSING METHODS</h2>
<p> These methods perform the parsing in parts by working on multiple chunks of memory passed by the application. Statements warnings, errors and fatal errors are delivered via the registered statement, error etc. handler functions.</p>
<dl>
<dt><code>int raptor_start_parse(raptor_parser* </code><i>parser</i><code>, const char *</code><i>uri</i><code>)</code></p>
<dd> Start a parse of chunked content with the base URI <i>uri</i> or NULL if not needed. The base URI is required for the RDF/XML parser (name &quot;rdfxml&quot;) and Turtle parser (name &quot;turtle&quot;). The N-Triples parser (name &quot;ntriples&quot;) or RSS Tag Soup parser (name &quot;rss-tag-soup&quot;) do not use this.</p>
<dt><code>int raptor_parse_chunk(raptor_parser* </code><i>parser</i><code>, const unsigned char *buffer, size_t </code><i>len</i><code>, int </code><i>is_end</i><code>)</code></p>
<dd> Parse the memory at <i>buffer</i> of size <i>len</i> returning statements via the statement handler callback. If <i>is_end</i> is non-zero, it indicates the end of the parsing stream. This method can only be called after <code>raptor_start_parse()</code>.</dl>
<h2>PARSER UTILITY METHODS</h2>
<dl>
<dt><code>const char* raptor_get_mime_type(raptor_parser* </code><i>rdf_parser</i><code>)</code></p>
<dd> Return the MIME type for the parser.</p>
<dt><code>void raptor_set_parser_strict(raptor_parser *</code><i>parser</i><code>, int </code><i>is_strict</i><code>)</code></p>
<dd> Set the parser to strict (<i>is_strict</i> not zero) or lax (default) mode. The detail of the strictness can be controlled by raptor_set_feature.</p>
<dt><code>int raptor_set_feature(raptor_parser *</code><i>parser</i><code>, raptor_feature </code><i>feature</i><code>, int </code><i>value</i><code>)</code></p>
<dd> Set a parser feature <i>feature</i> to a particular <i>value</i>. Returns non 0 on failure or if the feature is unknown. The current defined parser features are:<br />
&nbsp;<wbr>&nbsp;<wbr><i>Feature&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Values</i><br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ALLOW_BAGID</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ALLOW_NON_NS_ATTRIBUTES</code>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ALLOW_OTHER_PARSETYPES</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ALLOW_RDF_TYPE_RDF_LIST</code>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_ASSUME_IS_RDF</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_CHECK_RDF_ID</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_HTML_LINK</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_HTML_TAG_SOUP</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_MICROFORMATS</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_NON_NFC_FATAL</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_NORMALIZE_LANGUAGE</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_NO_NET</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_RELATIVE_URIS</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_SCANNING</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WARN_OTHER_PARSETYPES</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean&nbsp;<wbr>(non 0 true)<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WWW_TIMEOUT</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Integer<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WWW_HTTP_CACHE_CONTROL</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String<br />
&nbsp;<wbr>&nbsp;<wbr><code>RAPTOR_FEATURE_WWW_HTTP_USER_AGENT</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>String If the <i>allow_bagid</i> feature is true (default true) then the RDF/XML parser will support the rdf:bagID attribute that was removed from the RDF/XML language when it was revised. This support may be removed in future. If the <i>allow_non_ns_attributes</i> feature is true (default true), then the RDF/XML parser will allow non-XML namespaced attributes to be accepted as well as rdf: namespaced ones. For example, &#8216;about&#8217; and &#8216;ID&#8217; will be interpreted as if they were rdf:about and rdf:ID respectively. If the <i>allow_other_parsetypes</i> feature is true (default true) then the RDF/XML parser will allow unknown parsetypes to be present and will pass them on to the user. Unimplemented at present. If the <i>allow_rdf_type_rdf_list</i> feature is true (default false) then the RDF/XML parser will generate the idList rdf:type rdf:List triple in the handling of rdf:parseType=&quot;Collection&quot;. This triple was removed during the revising of RDF/XML after collections were initially added. If the <i>assume_is_rdf</i> feature is true (default false), then the RDF/XML parser will assume the content is RDF/XML, not require that rdf:RDF root element, and immediately interpret the content as RDF/XML. If the <i>check_rdf_id</i> feature is true (default true) then rdf:ID values will be checked for duplicates and cause an error if found. if the <i>html_link</i> feature is true (default true), look for head &amp;lt;link&amp;gt; to type rdf/xml for GRDDL parser If the <i>html_tag_soup</i> feature is true (default true), use a lax HTML parser if an XML parser fails when read HTML for GRDDL parser. If the <i>microformats</i> feature is true (default true), look for microformats for GRDDL parser. If the <i>non_nfc_fatal</i> feature is true (default false) then illegal Unicode Normal Form C in literals will give a fatal error, otherwise it gives a warning. If the <i>normalize_language</i> feature is true (default true) then XML language values such as from xml:lang will be normalized to lowercase. If the <i>no_net</i> feature is true (default false) then network requests are denied. If the <i>scanning</i> feature is true (default false), then the RDF/XML parser will look for embedded rdf:RDF elements inside the XML content, and not require that the XML start with an rdf:RDF root element. If the <i>www_timeout</i> feature is set to an integer larger than 0, it sets the timeout in seconds for internal WWW URI requests for the GRDDL parser. If the <i>www_http_cache_control</i> feature is set to a string value (default none), it is sent as the value of the HTTP Cache-Control: header in requests. If the <i>www_http_user_agent</i> feature is set to a string value, it is sent as the value of the HTTP User-Agent: header in requests.</p>
<dt><code>raptor_parser_set_feature_string(raptor_parser *</code><i>parser</i>, raptor_feature <i>feature</i>, const unsigned char *<i>value</i>)</p>
<dd> Set a parser feature <i>feature</i> to a particular string <i>value</i>. Returns non 0 on failure or if the feature is unknown. The current defined parser features are given in <code>raptor_set_feature</code> and at present only take integer values. If an integer value feature is set with this function, <i>value</i> is interpreted as an integer and then that value is used.</p>
<dt><code>int raptor_get_feature(raptor_parser* </code><i>parser</i><code>, raptor_feature </code><i>feature</i><code>)</code></p>
<dd> Get parser feature integer values. The allowed <i>feature</i> values and types are given under <code>raptor_features_enumerate</code>.</p>
<dt><code>const unsigned char* raptor_parser_get_feature_string(raptor_parser *</code><i>parser</i>, raptor_feature <i>feature</i>)</p>
<dd> Get parser feature string values. The allowed <i>feature</i> values and types are given under <code>raptor_features_enumerate</code>.</p>
<dt><code>unsigned int raptor_get_feature_count(void)</code></p>
<dd> Get the count of features defined. Prefered to the compile time-only symbol <code>RAPTOR_FEATURE_LAST</code> which returns the maximum value, not the count. Added raptor_get_need_base_uri</p>
<dt><code>int raptor_feature_value_type(const raptor_feature feature)</code></p>
<dd> Get a raptor feature value tyype &#8211; integer or string.</p>
<dt><code>raptor_locator* raptor_get_locator(raptor_parser* </code><i>rdf_parser</i><code>)</code></p>
<dd> Return the current raptor_locator object for the parser. This is a public structure defined in raptor.h that can be used directly, or formatted via raptor_print_locator.</p>
<dt><code>void raptor_get_name(raptor_parser *</code><i>parser</i><code>)</code></p>
<dd> Return the string short name for the parser.</p>
<dt><code>void raptor_get_label(raptor_parser *</code><i>parser</i><code>)</code></p>
<dd> Return a string label for the parser.</p>
<dt><code>void raptor_set_default_generate_id_parameters(raptor_parser* </code><i>rdf_parser</i><code>, char *</code><i>prefix</i><code>, int </code><i>base</i><code>)</code></p>
<dd> Control the default method for generation of IDs for blank nodes and bags. The method uses a short string <i>prefix</i> and an integer <i>base</i> to generate the identifier which is not guaranteed to be a strict concatenation. If <i>prefix</i> is NULL, the default is used. If base is less than 1, it is initialised to 1.</p>
<dt><code>void raptor_set_generate_id_handler(raptor_parser* </code><i>parser</i><code>, void *</code><i>user_data</i><code>, raptor_generate_id_handler </code><i>handler</i><code>)</code></p>
<dd> Allow full customisation of the generated IDs by setting a callback <i>handler</i> and associated <i>user_data</i> that is called whenever a blank node or bag identifier is required. The memory returned is deallocated inside raptor. Some systems require this to be allocated inside the same library, in which case the <code>raptor_alloc_memory</code> function may be useful.</p>
<dt><code>void raptor_parser_set_uri_filter(raptor_parser* </code><i>parser</i>, raptor_uri_filter_func <i>filter</i>, void* <i>user_data</i>)</p>
<dd> Set the URI filter function <i>filter</i> for URIs retrieved during parsing by the the raptor_parser.</p>
<dt><code>int raptor_get_need_base_uri(raptor_parser* </code><i>rdf_parser</i>)</p>
<dd> Get a boolean whether this parser needs a base URI to start parsing.</p>
<dt><code>unsigned char* raptor_parser_generate_id(raptor_parser* </code><i>rdf_parser</i>, raptor_genid_type <i>type</i>)</p>
<dd> Generate an ID for a parser of type <i>type</i>, either <code>RAPTOR_GENID_TYPE_BNODEID</code> or <code>RAPTOR_GENID_TYPE_BAGID</code>. This uses any configuration set by <code>raptor_set_generate_id_handler</code>.</p>
<dt><code>void raptor_set_graph_handler(raptor_parser* </code><i>parser</i>, void* <i>user_data</i>, raptor_graph_handler <i>handler</i>)</p>
<dd> Set the graph handler callback.</dl>
<h2>PARSER UTILITY FUNCTIONS</h2>
<dl>
<dt><code>int raptor_parsers_enumerate(const unsigned int </code><i>counter</i><code>, const char **</code><i>name</i><code>, const char **</code><i>label</i><code>)</code></p>
<dd> Return the parser name/label for a parser with a given integer counter, returning non-zero if no such parser at that offset exists. The counter should start from 0 and be incremented by 1 until the function returns non-zero.</p>
<dt><code>int raptor_syntaxes_enumerate(const unsigned int </code><i>counter</i><code>, const char **name, const char **</code><i>label</i><code>, const char **</code><i>mime_type</i><code>, const unsigned char **</code><i>uri-string</i><code>)</code></p>
<dd> Return the name, label, mime type or URI string (all optional) for a parser syntax with a given integer counter, returning non-zero if no such syntax parser at that offset exists. The counter should start from 0 and be incremented by 1 until the function returns non-zero.</p>
<dt><code>int raptor_features_enumerate(const raptor_feature </code><i>feature</i>, const char **<i>name</i>, raptor_uri **<i>uri</i>, const char **<i>label</i>)</p>
<dd> Return the name, URI, string label (all optional) for a parser <i>feature</i>, returning non-zero if no such feature exists. Raptor features have URIs that are constructed from the URI <i><a rel="nofollow" href="http://feature.librdf.org/raptor-">http://feature.librdf.org/raptor-</a></i> and the <i>name</i> so for example feature <i>scanForRDF</i> has URI <i><a rel="nofollow" href="http://feature.librdf.org/raptor-scanForRDF">http://feature.librdf.org/raptor-scanForRDF</a></i></p>
<dt><code>int raptor_syntax_name_check(const char *</code><i>name</i>)</p>
<dd> Check <i>name</i> is a known syntax name.</p>
<dt><code>const char* raptor_guess_parser_name(raptor_uri *</code><i>uri</i>, const char *<i>mime_type</i>, const unsigned char *<i>buffer</i>, size_t <i>len</i>, const unsigned char *<i>identifier</i>)</p>
<dd> Guess a parser name for a syntax identified by URI <i>uri</i>, MIME type <i>mime_type</i>, some initial content <i>buffer</i> of size <i>len</i> or with content identifier <i>identifier</i>. All of these parameters are optional and only used if not NULL. The parser is chosen by scoring the hints that are given.</p>
<dt><code>raptor_feature raptor_feature_from_uri(raptor_uri *</code><i>uri</i>)</p>
<dd> Turn a URI <i>uri</i> into a raptor feature identifier, or &lt;0 if the feature is unknown. The URIs are described below raptor_set_feature.</dl>
<h2>STATEMENT UTILITY FUNCTIONS</h2>
<dl>
<dt><code>int raptor_statement_compare(const raptor_statement *</code><i>s1</i>, const raptor_statement *<i>s2</i>)</p>
<dd> Compare two statements and return an ordering between them.</p>
<dt><code>void raptor_print_statement(const raptor_statement* const </code><i>statement</i><code>, FILE *</code><i>stream</i><code>)</code></p>
<dd> Print a raptor statement object in a simple format for debugging only. The format of this output is not guaranteed to remain the same between releases.</p>
<dt><code>void raptor_print_statement_as_ntriples(const raptor_statement* </code><i>statement</i><code>, FILE *</code><i>stream</i><code>)</code></p>
<dd> Print a raptor statement object in N-Triples format, using all the escapes as defined in <a rel="nofollow" href="http://www.w3.org/TR/rdf-testcases/#ntriples">http://www.w3.org/TR/rdf-testcases/#ntriples</a></p>
<dt><code>raptor_statement_part_as_counted_string(const void *</code><i>term</i><code>, raptor_identifier_type </code><i>type</i><code>, raptor_uri* </code><i>literal_datatype</i><code>, const unsigned char *</code><i>literal_language</i><code>, size_t* </code><i>len_p</i><code>)</code></p>
<dd>
<dt><code>char* raptor_statement_part_as_string(const void *</code><i>term</i><code>, raptor_identifier_type </code><i>type</i><code>, raptor_uri* </code><i>literal_datatype</i><code>, const unsigned char *</code><i>literal_language</i><code>)</code></p>
<dd> Turns part of raptor statement into N-Triples format, using all the escapes as defined in <a rel="nofollow" href="http://www.w3.org/TR/rdf-testcases/#ntriples">http://www.w3.org/TR/rdf-testcases/#ntriples</a> The part (subject, predicate, object) of the raptor_statement is passed in as <i>term</i>, the part type (subject_type, predicate_type, object_type) is passed in as <i>type</i>. When the part is a literal, the <i>literal_datatype</i> and <i>literal_language</i> fields are set, otherwise NULL (usually object_datatype, object_literal_language).</p>
<dt>
<dd> If <code>raptor_statement_part_as_counted_string</code> is used, the length of the returned string is stored in *<i>len_p</i> if not NULL.</dl>
<h2>LOCATOR UTILITY FUNCTIONS</h2>
<dl>
<dt><code>int raptor_format_locator(char *</code><i>buffer</i><code>, size_t </code><i>length</i><code>, raptor_locator* </code><i>locator</i><code>)</code></p>
<dd> This method takes a <i>raptor_locator</i> object as passed to an error, warning or other handler callback and formats it into the <i>buffer</i> of size <i>length</i> bytes. If <i>buffer</i> is NULL or <i>length</i> is insufficient for the size of the formatted locator, returns the number of additional bytes required in the buffer to write the locator. </p>
<p> In particular, if this form is used:<br />
&nbsp;<wbr>&nbsp;<wbr>length=raptor_format_locator(NULL, 0, locator) it will return in <i>length</i> the size of a buffer that can be allocated for <i>locator</i> and a second call will perform the formatting:<br />
&nbsp;<wbr>&nbsp;<wbr>raptor_format_locator(buffer, length, locator) </p>
<dt><code>void raptor_print_locator(FILE *</code><i>stream</i><code>, raptor_locator* </code><i>locator</i><code>)</code></p>
<dd> This method takes a <i>raptor_locator</i> object as passed to an error, warning or other handler callback, formats and prints it to the given stdio <i>stream</i>.</p>
<dt><code>int raptor_locator_line(raptor_locator *locator)</code></p>
<dd> Returns the line number in a locator structure or &lt;0 if not available.</p>
<dt><code>int raptor_locator_column(raptor_locator *locator)</code></p>
<dd> Returns the column number in a locator structure or &lt;0 if not available.</p>
<dt><code>int raptor_locator_byte(raptor_locator *locator)</code></p>
<dd> Returns the byte offset in a locator structure or &lt;0 if not available.</p>
<dt><code>const char * raptor_locator_file(raptor_locator *locator)</code></p>
<dd> Returns the filename in a locator structure or NULL if not available. Note the returned pointer is to a shared string that must be copied if needed.</p>
<dt><code>const char * raptor_locator_uri(raptor_locator *locator)</code></p>
<dd> Returns the URI string in a locator structure or NULL if not available. Note this does not return a raptor_uri* pointer and the returned pointer is to a shared string that must be copied if needed.</dl>
<h2>N-TRIPLES UTILITY FUNCTIONS</h2>
<dl>
<dt><code>void raptor_print_ntriples_string(FILE* </code><i>stream</i><code>, const char* </code><i>string</i><code>, const char </code><i>delim</i><code>)</code></p>
<dd> This is a standalone function that prints the given string according to N-Triples escaping rules, expecting to be terminated by delimiter <i>delim</i> which is usually either &#8216;, dq or &lt;. If a null delimiter 
