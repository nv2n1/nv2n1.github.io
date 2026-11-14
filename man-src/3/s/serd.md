---
title: "serd(3)"
name: "serd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-serd/"
description: "Serd –"
---

<p>Serd &#8211;</p>
<h2>Detailed Description</h2>
<p>A lightweight RDF syntax library.</p>
<h3>Data Structures</h3>
<p>struct <code>SerdNode</code> </p>
<p> struct <code>SerdChunk</code> </p>
<p> struct <code>SerdError</code> </p>
<p> struct <code>SerdURI</code></p>
<h3>Typedefs</h3>
<p>typedef struct SerdEnvImpl <code>SerdEnv</code> </p>
<p> typedef struct SerdReaderImpl <code>SerdReader</code> </p>
<p> typedef struct SerdWriterImpl <code>SerdWriter</code> </p>
<p> typedef uint32_t <code>SerdStatementFlags</code> </p>
<p> typedef uint32_t <code>SerdNodeFlags</code></p>
<h3>Enumerations</h3>
<p>enum <code>SerdStatus</code> { <code>SERD_SUCCESS</code>, <code>SERD_FAILURE</code>, <code>SERD_ERR_UNKNOWN</code>, <code>SERD_ERR_BAD_SYNTAX</code>, <code>SERD_ERR_BAD_ARG</code>, <code>SERD_ERR_NOT_FOUND</code>, <code>SERD_ERR_ID_CLASH</code>, <code>SERD_ERR_BAD_CURIE</code>, <code>SERD_ERR_INTERNAL</code> } </p>
<p> enum <code>SerdSyntax</code> { <code>SERD_TURTLE</code> = 1, <code>SERD_NTRIPLES</code> = 2 } </p>
<p> enum <code>SerdStatementFlag</code> { <code>SERD_EMPTY_S</code> = 1 &lt;&lt; 1, <code>SERD_EMPTY_O</code> = 1 &lt;&lt; 2, <code>SERD_ANON_S_BEGIN</code> = 1 &lt;&lt; 3, <code>SERD_ANON_O_BEGIN</code> = 1 &lt;&lt; 4, <code>SERD_ANON_CONT</code> = 1 &lt;&lt; 5, <code>SERD_LIST_S_BEGIN</code> = 1 &lt;&lt; 6, <code>SERD_LIST_O_BEGIN</code> = 1 &lt;&lt; 7, <code>SERD_LIST_CONT</code> = 1 &lt;&lt; 8 } </p>
<p> enum <code>SerdType</code> { <code>SERD_NOTHING</code> = 0, <code>SERD_LITERAL</code> = 1, <code>SERD_URI</code> = 2, <code>SERD_CURIE</code> = 3, <code>SERD_BLANK</code> = 4 } </p>
<p> enum <code>SerdNodeFlag</code> { <code>SERD_HAS_NEWLINE</code> = 1, <code>SERD_HAS_QUOTE</code> = 1 &lt;&lt; 1 } </p>
<p> enum <code>SerdStyle</code> { <code>SERD_STYLE_ABBREVIATED</code> = 1, <code>SERD_STYLE_ASCII</code> = 1 &lt;&lt; 1, <code>SERD_STYLE_RESOLVED</code> = 1 &lt;&lt; 2, <code>SERD_STYLE_CURIED</code> = 1 &lt;&lt; 3, <code>SERD_STYLE_BULK</code> = 1 &lt;&lt; 4 }</p>
<h3>String Utilities</h3>
<p>const uint8_t * <code>serd_strerror</code> (<code>SerdStatus</code> status) </p>
<p> size_t <code>serd_strlen</code> (const uint8_t *str, size_t *n_bytes, <code>SerdNodeFlags</code> *flags) </p>
<p> double <code>serd_strtod</code> (const char *str, char **endptr) </p>
<p> void * <code>serd_base64_decode</code> (const uint8_t *str, size_t len, size_t *size)</p>
<h3>Uri</h3>
<p>typedef size_t(* <code>SerdSink</code> )(const void *buf, size_t len, void *stream) </p>
<p> static const <code>SerdURI</code> <code>SERD_URI_NULL</code> = &#123;&#123;0,0},{0,0},{0,0},{0,0},{0,0},{0,0}} </p>
<p> const uint8_t * <code>serd_uri_to_path</code> (const uint8_t *uri) </p>
<p> uint8_t * <code>serd_file_uri_parse</code> (const uint8_t *uri, uint8_t **hostname) </p>
<p> bool <code>serd_uri_string_has_scheme</code> (const uint8_t *utf8) </p>
<p> <code>SerdStatus</code> <code>serd_uri_parse</code> (const uint8_t *utf8, <code>SerdURI</code> *out) </p>
<p> void <code>serd_uri_resolve</code> (const <code>SerdURI</code> *uri, const <code>SerdURI</code> *base, <code>SerdURI</code> *out) </p>
<p> size_t <code>serd_uri_serialise</code> (const <code>SerdURI</code> *uri, <code>SerdSink</code> sink, void *stream) </p>
<p> size_t <code>serd_uri_serialise_relative</code> (const <code>SerdURI</code> *uri, const <code>SerdURI</code> *base, const <code>SerdURI</code> *root, <code>SerdSink</code> sink, void *stream)</p>
<h3>Node</h3>
<p>static const <code>SerdNode</code> <code>SERD_NODE_NULL</code> = { 0, 0, 0, 0, <code>SERD_NOTHING</code> } </p>
<p> <code>SerdNode</code> <code>serd_node_from_string</code> (<code>SerdType</code> type, const uint8_t *str) </p>
<p> <code>SerdNode</code> <code>serd_node_copy</code> (const <code>SerdNode</code> *node) </p>
<p> bool <code>serd_node_equals</code> (const <code>SerdNode</code> *a, const <code>SerdNode</code> *b) </p>
<p> <code>SerdNode</code> <code>serd_node_new_uri_from_node</code> (const <code>SerdNode</code> *uri_node, const <code>SerdURI</code> *base, <code>SerdURI</code> *out) </p>
<p> <code>SerdNode</code> <code>serd_node_new_uri_from_string</code> (const uint8_t *str, const <code>SerdURI</code> *base, <code>SerdURI</code> *out) </p>
<p> <code>SerdNode</code> <code>serd_node_new_file_uri</code> (const uint8_t *path, const uint8_t *hostname, <code>SerdURI</code> *out, bool escape) </p>
<p> <code>SerdNode</code> <code>serd_node_new_uri</code> (const <code>SerdURI</code> *uri, const <code>SerdURI</code> *base, <code>SerdURI</code> *out) </p>
<p> <code>SerdNode</code> <code>serd_node_new_decimal</code> (double d, unsigned frac_digits) </p>
<p> <code>SerdNode</code> <code>serd_node_new_integer</code> (int64_t i) </p>
<p> <code>SerdNode</code> <code>serd_node_new_blob</code> (const void *buf, size_t size, bool wrap_lines) </p>
<p> void <code>serd_node_free</code> (<code>SerdNode</code> *node)</p>
<h3>Event Handlers</h3>
<p>typedef <code>SerdStatus</code>(* <code>SerdErrorSink</code> )(void *handle, const <code>SerdError</code> *error) </p>
<p> typedef <code>SerdStatus</code>(* <code>SerdBaseSink</code> )(void *handle, const <code>SerdNode</code> *uri) </p>
<p> typedef <code>SerdStatus</code>(* <code>SerdPrefixSink</code> )(void *handle, const <code>SerdNode</code> *name, const <code>SerdNode</code> *uri) </p>
<p> typedef <code>SerdStatus</code>(* <code>SerdStatementSink</code> )(void *handle, <code>SerdStatementFlags</code> flags, const <code>SerdNode</code> *graph, const <code>SerdNode</code> *subject, const <code>SerdNode</code> *predicate, const <code>SerdNode</code> *object, const <code>SerdNode</code> *object_datatype, const <code>SerdNode</code> *object_lang) </p>
<p> typedef <code>SerdStatus</code>(* <code>SerdEndSink</code> )(void *handle, const <code>SerdNode</code> *node)</p>
<h3>Environment</h3>
<p><code>SerdEnv</code> * <code>serd_env_new</code> (const <code>SerdNode</code> *base_uri) </p>
<p> void <code>serd_env_free</code> (<code>SerdEnv</code> *env) </p>
<p> const <code>SerdNode</code> * <code>serd_env_get_base_uri</code> (const <code>SerdEnv</code> *env, <code>SerdURI</code> *out) </p>
<p> <code>SerdStatus</code> <code>serd_env_set_base_uri</code> (<code>SerdEnv</code> *env, const <code>SerdNode</code> *uri) </p>
<p> <code>SerdStatus</code> <code>serd_env_set_prefix</code> (<code>SerdEnv</code> *env, const <code>SerdNode</code> *name, const <code>SerdNode</code> *uri) </p>
<p> <code>SerdStatus</code> <code>serd_env_set_prefix_from_strings</code> (<code>SerdEnv</code> *env, const uint8_t *name, const uint8_t *uri) </p>
<p> bool <code>serd_env_qualify</code> (const <code>SerdEnv</code> *env, const <code>SerdNode</code> *uri, <code>SerdNode</code> *prefix, <code>SerdChunk</code> *suffix) </p>
<p> <code>SerdStatus</code> <code>serd_env_expand</code> (const <code>SerdEnv</code> *env, const <code>SerdNode</code> *curie, <code>SerdChunk</code> *uri_prefix, <code>SerdChunk</code> *uri_suffix) </p>
<p> <code>SerdNode</code> <code>serd_env_expand_node</code> (const <code>SerdEnv</code> *env, const <code>SerdNode</code> *node) </p>
<p> void <code>serd_env_foreach</code> (const <code>SerdEnv</code> *env, <code>SerdPrefixSink</code> func, void *handle)</p>
<h3>Reader</h3>
<p><code>SerdReader</code> * <code>serd_reader_new</code> (<code>SerdSyntax</code> syntax, void *handle, void(*free_handle)(void *), <code>SerdBaseSink</code> base_sink, <code>SerdPrefixSink</code> prefix_sink, <code>SerdStatementSink</code> statement_sink, <code>SerdEndSink</code> end_sink) </p>
<p> void <code>serd_reader_set_error_sink</code> (<code>SerdReader</code> *reader, <code>SerdErrorSink</code> error_sink, void *handle) </p>
<p> void * <code>serd_reader_get_handle</code> (const <code>SerdReader</code> *reader) </p>
<p> void <code>serd_reader_add_blank_prefix</code> (<code>SerdReader</code> *reader, const uint8_t *prefix) </p>
<p> void <code>serd_reader_set_default_graph</code> (<code>SerdReader</code> *reader, const <code>SerdNode</code> *graph) </p>
<p> <code>SerdStatus</code> <code>serd_reader_read_file</code> (<code>SerdReader</code> *reader, const uint8_t *uri) </p>
<p> <code>SerdStatus</code> <code>serd_reader_start_stream</code> (<code>SerdReader</code> *me, FILE *file, const uint8_t *name, bool bulk) </p>
<p> <code>SerdStatus</code> <code>serd_reader_read_chunk</code> (<code>SerdReader</code> *me) </p>
<p> <code>SerdStatus</code> <code>serd_reader_end_stream</code> (<code>SerdReader</code> *me) </p>
<p> <code>SerdStatus</code> <code>serd_reader_read_file_handle</code> (<code>SerdReader</code> *reader, FILE *file, const uint8_t *name) </p>
<p> <code>SerdStatus</code> <code>serd_reader_read_string</code> (<code>SerdReader</code> *me, const uint8_t *utf8) </p>
<p> void <code>serd_reader_free</code> (<code>SerdReader</code> *reader)</p>
<h3>Writer</h3>
<p><code>SerdWriter</code> * <code>serd_writer_new</code> (<code>SerdSyntax</code> syntax, <code>SerdStyle</code> style, <code>SerdEnv</code> *env, const <code>SerdURI</code> *base_uri, <code>SerdSink</code> sink, void *stream) </p>
<p> void <code>serd_writer_free</code> (<code>SerdWriter</code> *writer) </p>
<p> <code>SerdEnv</code> * <code>serd_writer_get_env</code> (<code>SerdWriter</code> *writer) </p>
<p> size_t <code>serd_file_sink</code> (const void *buf, size_t len, void *stream) </p>
<p> size_t <code>serd_chunk_sink</code> (const void *buf, size_t len, void *stream) </p>
<p> uint8_t * <code>serd_chunk_sink_finish</code> (<code>SerdChunk</code> *stream) </p>
<p> void <code>serd_writer_set_error_sink</code> (<code>SerdWriter</code> *writer, <code>SerdErrorSink</code> error_sink, void *handle) </p>
<p> void <code>serd_writer_chop_blank_prefix</code> (<code>SerdWriter</code> *writer, const uint8_t *prefix) </p>
<p> <code>SerdStatus</code> <code>serd_writer_set_base_uri</code> (<code>SerdWriter</code> *writer, const <code>SerdNode</code> *uri) </p>
<p> <code>SerdStatus</code> <code>serd_writer_set_root_uri</code> (<code>SerdWriter</code> *writer, const <code>SerdNode</code> *uri) </p>
<p> <code>SerdStatus</code> <code>serd_writer_set_prefix</code> (<code>SerdWriter</code> *writer, const <code>SerdNode</code> *name, const <code>SerdNode</code> *uri) </p>
<p> <code>SerdStatus</code> <code>serd_writer_write_statement</code> (<code>SerdWriter</code> *writer, <code>SerdStatementFlags</code> flags, const <code>SerdNode</code> *graph, const <code>SerdNode</code> *subject, const <code>SerdNode</code> *predicate, const <code>SerdNode</code> *object, const <code>SerdNode</code> *object_datatype, const <code>SerdNode</code> *object_lang) </p>
<p> <code>SerdStatus</code> <code>serd_writer_end_anon</code> (<code>SerdWriter</code> *writer, const <code>SerdNode</code> *node) </p>
<p> <code>SerdStatus</code> <code>serd_writer_finish</code> (<code>SerdWriter</code> *writer)</p>
<h2>Data Structure Documentation</h2>
<h2>struct SerdNode</h2>
<p>A syntactic RDF node. </p>
<p> <code>Data Fields:</code></p>
<dl>
<dd>const uint8_t * <i>buf</i> Value string. </p>
<p> size_t <i>n_bytes</i> Size in bytes (not including null) </p>
<p> size_t <i>n_chars</i> Length in characters (not including null) </p>
<p> <code>SerdNodeFlags</code> <i>flags</i> Node flags (e.g. string properties) </p>
<p> <code>SerdType</code> <i>type</i> Node type. </p>
</dl>
<h2>struct SerdChunk</h2>
<p>An unterminated string fragment. </p>
<p> <code>Data Fields:</code></p>
<dl>
<dd>const uint8_t * <i>buf</i> Start of chunk. </p>
<p> size_t <i>len</i> Length of chunk in bytes. </p>
</dl>
<h2>struct SerdError</h2>
<p>An error description. </p>
<p> <code>Data Fields:</code></p>
<dl>
<dd><code>SerdStatus</code> <i>status</i> Error code. </p>
<p> const uint8_t * <i>filename</i> File where error was encountered, or NULL. </p>
<p> unsigned <i>line</i> Line where error was encountered, or 0. </p>
<p> unsigned <i>col</i> Column where error was encountered. </p>
<p> const char * <i>fmt</i> Message format string (printf style) </p>
<p> va_list * <i>args</i> Arguments for fmt. </p>
</dl>
<h2>struct SerdURI</h2>
<p>A parsed URI. </p>
<p> This struct directly refers to chunks in other strings, it does not own any memory itself. Thus, URIs can be parsed and/or resolved against a base URI in-place without allocating memory. </p>
<p> <code>Data Fields:</code></p>
<dl>
<dd><code>SerdChunk</code> <i>scheme</i> Scheme. </p>
<p> <code>SerdChunk</code> <i>authority</i> Authority. </p>
<p> <code>SerdChunk</code> <i>path_base</i> Path prefix if relative. </p>
<p> <code>SerdChunk</code> <i>path</i> Path suffix. </p>
<p> <code>SerdChunk</code> <i>query</i> Query. </p>
<p> <code>SerdChunk</code> <i>fragment</i> Fragment. </p>
</dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct SerdEnvImpl <code>SerdEnv</code></h3>
<p>Environment. Represents the state required to resolve a CURIE or relative URI, e.g. the base URI and set of namespace prefixes at a particular point.</p>
<h3>typedef struct SerdReaderImpl <code>SerdReader</code></h3>
<p>RDF reader. Parses RDF by calling user-provided sink functions as input is consumed (much like an XML SAX parser).</p>
<h3>typedef struct SerdWriterImpl <code>SerdWriter</code></h3>
<p>RDF writer. Provides a number of functions to allow writing RDF syntax out to some stream. These functions are deliberately compatible with the sink functions used by SerdReader, so a reader can be directly connected to a writer to re-serialise a document with minimal overhead.</p>
<h3>typedef uint32_t <code>SerdStatementFlags</code></h3>
<p>Bitwise OR of SerdNodeFlag values.</p>
<h3>typedef uint32_t <code>SerdNodeFlags</code></h3>
<p>Bitwise OR of SerdNodeFlag values.</p>
<h3>typedef size_t(* SerdSink)(const void *buf, size_t len, void *stream)</h3>
<p>Sink function for raw string output.</p>
<h3>typedef <code>SerdStatus</code>(* SerdErrorSink)(void *handle, const <code>SerdError</code> *error)</h3>
<p>Sink (callback) for errors. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>handle</i> Handle for user data.<br />
 <i>error</i> Error description.</dl>
<h3>typedef <code>SerdStatus</code>(* SerdBaseSink)(void *handle, const <code>SerdNode</code> *uri)</h3>
<p>Sink (callback) for base URI changes. Called whenever the base URI of the serialisation changes.</p>
<h3>typedef <code>SerdStatus</code>(* SerdPrefixSink)(void *handle, const <code>SerdNode</code> *name, const <code>SerdNode</code> *uri)</h3>
<p>Sink (callback) for namespace definitions. Called whenever a prefix is defined in the serialisation.</p>
<h3>typedef <code>SerdStatus</code>(* SerdStatementSink)(void *handle, <code>SerdStatementFlags</code> flags, const <code>SerdNode</code> *graph, const <code>SerdNode</code> *subject, const <code>SerdNode</code> *predicate, const <code>SerdNode</code> *object, const <code>SerdNode</code> *object_datatype, const <code>SerdNode</code> *object_lang)</h3>
<p>Sink (callback) for statements. Called for every RDF statement in the serialisation.</p>
<h3>typedef <code>SerdStatus</code>(* SerdEndSink)(void *handle, const <code>SerdNode</code> *node)</h3>
<p>Sink (callback) for anonymous node end markers. This is called to indicate that the anonymous node with the given value will no longer be referred to by any future statements (i.e. the anonymous serialisation of the node is finished).</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>SerdStatus</code></h3>
<p>Return status code. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>SERD_SUCCESS </i></p>
<dd>No error.</p>
<dt><i>SERD_FAILURE </i></p>
<dd>Non-fatal failure.</p>
<dt><i>SERD_ERR_UNKNOWN </i></p>
<dd>Unknown error.</p>
<dt><i>SERD_ERR_BAD_SYNTAX </i></p>
<dd>Invalid syntax.</p>
<dt><i>SERD_ERR_BAD_ARG </i></p>
<dd>Invalid argument.</p>
<dt><i>SERD_ERR_NOT_FOUND </i></p>
<dd>Not found.</p>
<dt><i>SERD_ERR_ID_CLASH </i></p>
<dd>Encountered clashing blank node IDs.</p>
<dt><i>SERD_ERR_BAD_CURIE </i></p>
<dd>Invalid CURIE (e.g. prefix does not exist)</p>
<dt><i>SERD_ERR_INTERNAL </i></p>
<dd>Unexpected internal error (should not happen)</dl>
<h3>enum <code>SerdSyntax</code></h3>
<p>RDF syntax type. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>SERD_TURTLE </i></p>
<dd>Turtle &#8211; Terse RDF Triple Language (UTF-8).</dl>
<p> <code>See Also:</code></p>
<dl>
<dd>Turtle</dl>
<dl>
<dt><i>SERD_NTRIPLES </i></p>
<dd>NTriples &#8211; Line-based RDF triples (ASCII).</dl>
<p> <code>See Also:</code></p>
<dl>
<dd>NTriples</dl>
<h3>enum <code>SerdStatementFlag</code></h3>
<p>Flags indication inline abbreviation information for a statement. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>SERD_EMPTY_S </i></p>
<dd>Empty blank node subject.</p>
<dt><i>SERD_EMPTY_O </i></p>
<dd>Empty blank node object.</p>
<dt><i>SERD_ANON_S_BEGIN </i></p>
<dd>Start of anonymous subject.</p>
<dt><i>SERD_ANON_O_BEGIN </i></p>
<dd>Start of anonymous object.</p>
<dt><i>SERD_ANON_CONT </i></p>
<dd>Continuation of anonymous node.</p>
<dt><i>SERD_LIST_S_BEGIN </i></p>
<dd>Start of list subject.</p>
<dt><i>SERD_LIST_O_BEGIN </i></p>
<dd>Start of list object.</p>
<dt><i>SERD_LIST_CONT </i></p>
<dd>Continuation of list.</dl>
<h3>enum <code>SerdType</code></h3>
<p>Type of a syntactic RDF node. This is more precise than the type of an abstract RDF node. An abstract node is either a resource, literal, or blank. In syntax there are two ways to refer to a resource (by URI or CURIE) and two ways to refer to a blank (by ID or anonymously). Anonymous (inline) blank nodes are expressed using SerdStatementFlags rather than this type. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>SERD_NOTHING </i></p>
<dd>The type of a nonexistent node. This type is useful as a sentinel, but is never emitted by the reader.</p>
<dt><i>SERD_LITERAL </i></p>
<dd>Literal value. A literal optionally has either a language, or a datatype (not both).</p>
<dt><i>SERD_URI </i></p>
<dd>URI (absolute or relative). Value is an unquoted URI string, which is either a relative reference with respect to the current base URI (e.g. &#8216;foo/bar&#8217;), or an absolute URI (e.g. &#8216;<a rel="nofollow" href="http://example.org/foo'">http://example.org/foo&#8217;</a>).</dl>
<p> <code>See Also:</code></p>
<dl>
<dd>RFC3986.</dl>
<dl>
<dt><i>SERD_CURIE </i></p>
<dd>CURIE, a shortened URI. Value is an unquoted CURIE string relative to the current environment, e.g. &#8216;rdf:type&#8217;.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd>CURIE Syntax 1.0</dl>
<dl>
<dt><i>SERD_BLANK </i></p>
<dd>A blank node. Value is a blank node ID, e.g. &#8216;id3&#8217;, which is meaningful only within this serialisation.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd>Turtle nodeID</dl>
<h3>enum <code>SerdNodeFlag</code></h3>
<p>Flags indicating certain string properties relevant to serialisation. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>SERD_HAS_NEWLINE </i></p>
<dd>Contains line breaks (&#8216;
&#8217; or &#8216;&#8217;)</p>
<dt><i>SERD_HAS_QUOTE </i></p>
<dd>Contains quotes (&#8221;&#8217;)</dl>
<h3>enum <code>SerdStyle</code></h3>
<p>Syntax style options. The style of the writer output can be controlled by ORing together values from this enumeration. Note that some options are only supported for some syntaxes (e.g. NTriples does not support abbreviation and is always ASCII). </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>SERD_STYLE_ABBREVIATED </i></p>
<dd>Abbreviate triples when possible.</p>
<dt><i>SERD_STYLE_ASCII </i></p>
<dd>Escape all non-ASCII characters.</p>
<dt><i>SERD_STYLE_RESOLVED </i></p>
<dd>Resolve URIs against base URI.</p>
<dt><i>SERD_STYLE_CURIED </i></p>
<dd>Shorten URIs into CURIEs.</p>
<dt><i>SERD_STYLE_BULK </i></p>
<dd>Write output in pages.</dl>
<h2>Function Documentation</h2>
<h3>const uint8_t* serd_strerror (<code>SerdStatus</code>status)</h3>
<p>Return a string describing a status code.</p>
<h3>size_t serd_strlen (const uint8_t *str, size_t *n_bytes, <code>SerdNodeFlags</code> *flags)</h3>
<p>Measure a UTF-8 string. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>Length of str in characters (except NULL).</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>str</i> A null-terminated UTF-8 string.<br />
 <i>n_bytes</i> (Output) Set to the size of str in bytes (except NULL).<br />
 <i>flags</i> (Output) Set to the applicable flags.</dl>
<h3>double serd_strtod (const char *str, char **endptr)</h3>
<p>Parse a string to a double. The API of this function is identical to the standard C strtod function, except this function is locale-independent and always matches the lexical format used in the Turtle grammar (the decimal point is always &#8216;.&#8217;).</p>
<h3>void* serd_base64_decode (const uint8_t *str, size_tlen, size_t *size)</h3>
<p>Decode a base64 string. This function can be used to deserialise a blob node created with <code>serd_node_new_blob()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>str</i> Base64 string to decode.<br />
 <i>len</i> The length of str.<br />
 <i>size</i> Set to the size of the returned blob in bytes.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A newly allocated blob which must be freed with free().</dl>
<h3>const uint8_t* serd_uri_to_path (const uint8_t *uri)</h3>
<p>Return the local path for uri, or NULL if uri is not a file URI. Note this (inappropriately named) function only removes the file scheme if necessary, and returns uri unmodified if it is an absolute path. Percent encoding and other issues are not handled, to properly convert a file URI to a path, use <code>serd_file_uri_parse()</code>.</p>
<h3>uint8_t* serd_file_uri_parse (const uint8_t *uri, uint8_t **hostname)</h3>
<p>Get the unescaped path and hostname from a file URI. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>uri</i> A file URI.<br />
 <i>hostname</i> If non-NULL, set to the hostname, if present.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The path component of the URI.</dl>
<p> Both the returned path and hostname (if applicable) are owned by the caller and must be freed with free().</p>
<h3>bool serd_uri_string_has_scheme (const uint8_t *utf8)</h3>
<p>Return true iff utf8 starts with a valid URI scheme.</p>
<h3><code>SerdStatus</code> serd_uri_parse (const uint8_t *utf8, <code>SerdURI</code> *out)</h3>
<p>Parse utf8, writing result to out.</p>
<h3>void serd_uri_resolve (const <code>SerdURI</code> *uri, const <code>SerdURI</code> *base, <code>SerdURI</code> *out)</h3>
<p>Set out to uri resolved against base.</p>
<h3>size_t serd_uri_serialise (const <code>SerdURI</code> *uri, <code>SerdSink</code>sink, void *stream)</h3>
<p>Serialise uri with a series of calls to sink.</p>
<h3>size_t serd_uri_serialise_relative (const <code>SerdURI</code> *uri, const <code>SerdURI</code> *base, const <code>SerdURI</code> *root, <code>SerdSink</code>sink, void *stream)</h3>
<p>Serialise uri relative to base with a series of calls to sink. The uri is written as a relative URI iff if it a child of base and root. The optional root parameter must be a prefix of base and can be used keep up-references (&#8216;../&#8217;) within a certain namespace.</p>
<h3><code>SerdNode</code> serd_node_from_string (<code>SerdType</code>type, const uint8_t *str)</h3>
<p>Make a (shallow) node from str. This measures, but does not copy, str. No memory is allocated.</p>
<h3><code>SerdNode</code> serd_node_copy (const <code>SerdNode</code> *node)</h3>
<p>Make a deep copy of node. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>a node that the caller must free with <code>serd_node_free()</code>.</dl>
<h3>bool serd_node_equals (const <code>SerdNode</code> *a, const <code>SerdNode</code> *b)</h3>
<p>Return true iff a is equal to b.</p>
<h3><code>SerdNode</code> serd_node_new_uri_from_node (const <code>SerdNode</code> *uri_node, const <code>SerdURI</code> *base, <code>SerdURI</code> *out)</h3>
<p>Simple wrapper for serd_node_new_uri to resolve a URI node.</p>
<h3><code>SerdNode</code> serd_node_new_uri_from_string (const uint8_t *str, const <code>SerdURI</code> *base, <code>SerdURI</code> *out)</h3>
<p>Simple wrapper for serd_node_new_uri to resolve a URI string.</p>
<h3><code>SerdNode</code> serd_node_new_file_uri (const uint8_t *path, const uint8_t *hostname, <code>SerdURI</code> *out, boolescape)</h3>
<p>Create a new file URI node from a file system path and optional hostname. Backslashes in Windows paths will be converted and &#8221; will always be percent encoded. If escape is true, all other invalid characters will be percent encoded as well. </p>
<p> If path is relative, hostname is ignored. If out is not NULL, it will be set to the parsed URI.</p>
<h3><code>SerdNode</code> serd_node_new_uri (const <code>SerdURI</code> *uri, const <code>SerdURI</code> *base, <code>SerdURI</code> *out)</h3>
<p>Create a new node by serialising uri into a new string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>uri</i> The URI to parse and serialise.<br />
 <i>base</i> Base URI to resolve uri against (or NULL for no resolution).<br />
 <i>out</i> Set to the parsing of the new URI (i.e. points only to memory owned by the new returned node).</dl>
<h3><code>SerdNode</code> serd_node_new_decimal (doubled, unsignedfrac_digits)</h3>
<p>Create a new node by serialising d into an xsd:decimal string. The resulting node will always contain a `.&#8217;, start with a digit, and end with a digit (i.e. will have a leading and/or trailing `0&#8242; if necessary). It will never be in scientific notation. A maximum of frac_digits digits will be written after the decimal point, but trailing zeros will automatically be omitted (except one if d is a round integer). </p>
<p> Note that about 16 and 8 fractional digits are required to precisely represent a double and float, respectively. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>d</i> The value for the new node.<br />
 <i>frac_digits</i> The maximum number of digits after the decimal place.</dl>
<h3><code>SerdNode</code> serd_node_new_integer (int64_ti)</h3>
<p>Create a new node by serialising i into an xsd:integer string.</p>
<h3><code>SerdNode</code> serd_node_new_blob (const void *buf, size_tsize, boolwrap_lines)</h3>
<p>Create a node by serialising buf into an xsd:base64Binary string. This function can be used to make a serialisable node out of arbitrary binary data, which can be decoded using <code>serd_base64_decode()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>buf</i> Raw binary input data.<br />
 <i>size</i> Size of buf.<br />
 <i>wrap_lines</i> Wrap lines at 76 characters to conform to RFC 2045.</dl>
<h3>void serd_node_free (<code>SerdNode</code> *node)</h3>
<p>Free any data owned by node. Note that if node is itself dynamically allocated (which is not the case for nodes created internally by serd), it will not be freed.</p>
<h3><code>SerdEnv</code>* serd_env_new (const <code>SerdNode</code> *base_uri)</h3>
<p>Create a new environment.</p>
<h3>void serd_env_free (<code>SerdEnv</code> *env)</h3>
<p>Free ns.</p>
<h3>const <code>SerdNode</code>* serd_env_get_base_uri (const <code>SerdEnv</code> *env, <code>SerdURI</code> *out)</h3>
<p>Get the current base URI.</p>
<h3><code>SerdStatus</code> serd_env_set_base_uri (<code>SerdEnv</code> *env, const <code>SerdNode</code> *uri)</h3>
<p>Set the current base URI.</p>
<h3><code>SerdStatus</code> serd_env_set_prefix (<code>SerdEnv</code> *env, const <code>SerdNode</code> *name, const <code>SerdNode</code> *uri)</h3>
<p>Set a namespace prefix.</p>
<h3><code>SerdStatus</code> serd_env_set_prefix_from_strings (<code>SerdEnv</code> *env, const uint8_t *name, const uint8_t *uri)</h3>
<p>Set a namespace prefix.</p>
<h3>bool serd_env_qualify (const <code>SerdEnv</code> *env, const <code>SerdNode</code> *uri, <code>SerdNode</code> *prefix, <code>SerdChunk</code> *suffix)</h3>
<p>Qualify uri into a CURIE if possible.</p>
<h3><code>SerdStatus</code> serd_env_expand (const <code>SerdEnv</code> *env, const <code>SerdNode</code> *curie, <code>SerdChunk</code> *uri_prefix, <code>SerdChunk</code> *uri_suffix)</h3>
<p>Expand curie.</p>
<h3><code>SerdNode</code> serd_env_expand_node (const <code>SerdEnv</code> *env, const <code>SerdNode</code> *node)</h3>
<p>Expand node, which must be a CURIE or URI, to a full URI.</p>
<h3>void serd_env_foreach (const <code>SerdEnv</code> *env, <code>SerdPrefixSink</code>func, void *handle)</h3>
<p>Call func for each prefix defined in env.</p>
<h3><code>SerdReader</code>* serd_reader_new (<code>SerdSyntax</code>syntax, void *handle, void(*)(void *)free_handle, <code>SerdBaseSink</code>base_sink, <code>SerdPrefixSink</code>prefix_sink, <code>SerdStatementSink</code>statement_sink, <code>SerdEndSink</code>end_sink)</h3>
<p>Create a new RDF reader.</p>
<h3>void serd_reader_set_error_sink (<code>SerdReader</code> *reader, <code>SerdErrorSink</code>error_sink, void *handle)</h3>
<p>Set a function to be called when errors occur during reading. The error_sink will be called with handle as its first argument. If no error function is set, errors are printed to stderr in GCC style.</p>
<h3>void* serd_reader_get_handle (const <code>SerdReader</code> *reader)</h3>
<p>Return the handle passed to <code>serd_reader_new()</code>.</p>
<h3>void serd_reader_add_blank_prefix (<code>SerdReader</code> *reader, const uint8_t *prefix)</h3>
<p>Set a prefix to be added to all blank node identifiers. This is useful when multiple files are to be parsed into the same output (e.g. a store, or other files). Since Serd preserves blank node IDs, this could cause conflicts where two non-equivalent blank nodes are merged, resulting in corrupt data. By setting a unique blank node prefix for each parsed file, this can be avoided, while preserving blank node names.</p>
<h3>void serd_reader_set_default_graph (<code>SerdReader</code> *reader, const <code>SerdNode</code> *graph)</h3>
<p>Set the URI of the default graph. If this is set, the reader will emit quads with the graph set to the given node for any statements that are not in a named graph (which is currently all of them since Serd currently does not support any graph syntaxes).</p>
<h3><code>SerdStatus</code> serd_reader_read_file (<code>SerdReader</code> *reader, const uint8_t *uri)</h3>
<p>Read a file at a given uri.</p>
<h3><code>SerdStatus</code> serd_reader_start_stream (<code>SerdReader</code> *me, FILE *file, const uint8_t *name, boolbulk)</h3>
<p>Start an incremental read from a file handle. Iff bulk is true, file will be read a page at a time. This is more efficient, but uses a page of memory and means that an entire page of input must be ready before any callbacks will fire. To react as soon as input arrives, set bulk to false.</p>
<h3><code>SerdStatus</code> serd_reader_read_chunk (<code>SerdReader</code> *me)</h3>
<p>Read a single &#8216;chunk&#8217; of data during an incremental read. This function will read a single top level description, and return. This may be a directive, statement, or several statements; essentially it reads until a &#8216;.&#8217; is encountered. This is particularly useful for reading directly from a pipe or socket.</p>
<h3><code>SerdStatus</code> serd_reader_end_stream (<code>SerdReader</code> *me)</h3>
<p>Finish an incremental read from a file handle.</p>
<h3><code>SerdStatus</code> serd_reader_read_file_handle (<code>SerdReader</code> *reader, FILE *file, const uint8_t *name)</h3>
<p>Read file.</p>
<h3><code>SerdStatus</code> serd_reader_read_string (<code>SerdReader</code> *me, const uint8_t *utf8)</h3>
<p>Read utf8.</p>
<h3>void serd_reader_free (<code>SerdReader</code> *reader)</h3>
<p>Free reader.</p>
<h3><code>SerdWriter</code>* serd_writer_new (<code>SerdSyntax</code>syntax, <code>SerdStyle</code>style, <code>SerdEnv</code> *env, const <code>SerdURI</code> *base_uri, <code>SerdSink</code>sink, void *stream)</h3>
<p>Create a new RDF writer.</p>
<h3>void serd_writer_free (<code>SerdWriter</code> *writer)</h3>
<p>Free writer.</p>
<h3><code>SerdEnv</code>* serd_writer_get_env (<code>SerdWriter</code> *writer)</h3>
<p>Return the env used by writer.</p>
<h3>size_t serd_file_sink (const void *buf, size_tlen, void *stream)</h3>
<p>A convenience sink function for writing to a FILE*. This function can be used as a SerdSink when writing to a FILE*. The stream parameter must be a FILE* opened for writing.</p>
<h3>size_t serd_chunk_sink (const void *buf, size_tlen, void *stream)</h3>
<p>A convenience sink function for writing to a string. This function can be used as a SerdSink to write to a <code>SerdChunk</code> which is resized as necessary with realloc(). The stream parameter must point to an initialized <code>SerdChunk</code>. When the write is finished, the string should be retrieved with <code>serd_chunk_sink_finish()</code>.</p>
<h3>uint8_t* serd_chunk_sink_finish (<code>SerdChunk</code> *stream)</h3>
<p>Finish a serialisation to a chunk with <code>serd_chunk_sink()</code>. The returned string is the result of the serialisation, which is NULL terminated (by this function) and owned by the caller.</p>
<h3>void serd_writer_set_error_sink (<code>SerdWriter</code> *writer, <code>SerdErrorSink</code>error_sink, void *handle)</h3>
<p>Set a function to be called when errors occur during writing. The error_sink will be called with handle as its first argument. If no error function is set, errors are printed to stderr.</p>
<h3>void serd_writer_chop_blank_prefix (<code>SerdWriter</code> *writer, const uint8_t *prefix)</h3>
<p>Set a prefix to be removed from matching blank node identifiers.</p>
<h3><code>SerdStatus</code> serd_writer_set_base_uri (<code>SerdWriter</code> *writer, const <code>SerdNode</code> *uri)</h3>
<p>Set the current output base URI (and emit directive if applicable). Note this function can be safely casted to SerdBaseSink.</p>
<h3><code>SerdStatus</code> serd_writer_set_root_uri (<code>SerdWriter</code> *writer, const <code>SerdNode</code> *uri)</h3>
<p>Set the current root URI. The root URI should be a prefix of the base URI. The path of the root URI is the highest path any relative up-reference can refer to. For example, with root file:///foo/root and base file:///foo/root/base, file:///foo/root will be written as &lt;../&gt;, but file:///foo will be written non-relatively as file:///foo. If the root is not explicitly set, it defaults to the base URI, so no up-references will be created at all.</p>
<h3><code>SerdStatus</code> serd_writer_set_prefix (<code>SerdWriter</code> *writer, const <code>SerdNode</code> *name, const <code>SerdNode</code> *uri)</h3>
<p>Set a namespace prefix (and emit directive if applicable). Note this function can be safely casted to SerdPrefixSink.</p>
<h3><code>SerdStatus</code> serd_writer_write_statement (<code>SerdWriter</code> *writer, <code>SerdStatementFlags</code>flags, const <code>SerdNode</code> *graph, const <code>SerdNode</code> *subject, const <code>SerdNode</code> *predicate, const <code>SerdNode</code> *object, const <code>SerdNode</code> *object_datatype, const <code>SerdNode</code> *object_lang)</h3>
<p>Write a statement. Note this function can be safely casted to SerdStatementSink.</p>
<h3><code>SerdStatus</code> serd_writer_end_anon (<code>SerdWriter</code> *writer, const <code>SerdNode</code> *node)</h3>
<p>Mark the end of an anonymous node&#8217;s description. Note this function can be safely casted to SerdEndSink.</p>
<h3><code>SerdStatus</code> serd_writer_finish (<code>SerdWriter</code> *writer)</h3>
<p>Finish a write.</p>
<h2>Variable Documentation</h2>
<h3>const <code>SerdURI</code> SERD_URI_NULL = &#123;&#123;0,0},{0,0},{0,0},{0,0},{0,0},{0,0}} [static]</h3>
<h3>const <code>SerdNode</code> SERD_NODE_NULL = { 0, 0, 0, 0, <code>SERD_NOTHING</code> } [static]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Serd from the source code.</p>
