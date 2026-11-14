---
title: "redland(3)"
name: "redland"
section: "3"
letter: "r"
url: "/docs/linux/man/3-redland/"
description: "redland – Resource Description Framework (RDF) Library"
---

<p>redland &#8211; Resource Description Framework (RDF) Library</p>
<h2>Version</h2>
<p><font SIZE="-1">1.0.16</font></p>
<h2>Synopsis</h2>
<pre><code>#include &lt;redland.h&gt;</code></pre>
<h2>Description</h2>
<p><code>redland</code> is a library providing support for the Resource Description Framework (<font SIZE="-1">RDF</font>) written in <font SIZE="-1">ANSI</font> C with APIs in several other languages. </p>
<p> This manual page lists most of the redland public <font SIZE="-1">API</font> functions but does not claim to be a complete summary of the entire <font SIZE="-1">API</font>. For the complete <font SIZE="-1">API</font> with full details of the function interface, see the <font SIZE="-1">HTML</font> <font SIZE="-1">API</font> documentation either on the Redland web site at &lt;<a rel="nofollow" href="http://librdf.org/">http://librdf.org/</a>&gt; or with the software release in the docs/api directory.</p>
<h2>Functions</h2>
<p>The functions defined by <code>redland</code> are all defined with the <tt>&quot;librdf_&quot;</tt> prefix</p>
<h3>class world</h3>
<dl>
<dt>librdf_world* <code>librdf_new_world</code>(<i>void</i>)</p>
<dd>
<dt>void <code>librdf_free_world</code>(librdf_world* <i>world</i>)</p>
<dd>
<dt>void <code>librdf_world_open</code>(librdf_world* <i>world</i>)</p>
<dd>
<dt>void <code>librdf_world_set_error</code>(librdf_world* <i>world</i>, void* <i>user_data</i>, void (*<i>error_fn</i>)(void* <i>user_data</i>, const char* <i>msg</i>, &#8230;))</p>
<dd>
<dt>void <code>librdf_world_set_warning</code>(librdf_world* <i>world</i>, void* <i>user_data</i>, void (*<i>warning_fn</i>)(void* <i>user_data</i>, const char* <i>msg</i>, &#8230;))</p>
<dd>
<dt>void <code>librdf_world_set_digest</code>(librdf_world*, const char* <i>name</i>)</p>
<dd>
<dt>void <code>librdf_world_set_uris_hash</code>(librdf_world* <i>world</i>, librdf_hash* <i>uris_hash</i>)</p>
<dd>
<dt>const char* <code>librdf_world_get_feature</code>(librdf_world* <i>world</i>, librdf_uri* <i>feature</i>)</p>
<dd>
<dt>int <code>librdf_world_set_feature</code>(librdf_world* <i>world</i>, librdf_uri* <i>feature</i>, const char* <i>value</i>)</p>
<dd></dl>
<h3>class iterator</h3>
<dl>
<dt>librdf_iterator* <code>librdf_new_iterator</code>(librdf_world* <i>world</i>, void* <i>context</i>, int (*<i>is_end</i>)(void*), void* (*<i>get_next</i>)(void*), void (*<i>finished</i>)(void*))</p>
<dd>
<dt>void <code>librdf_free_iterator</code>(librdf_iterator*)</p>
<dd>
<dt>int <code>librdf_iterator_end</code>(librdf_iterator* <i>iterator</i>)</p>
<dd>
<dt>int <code>librdf_iterator_finished</code>(librdf_iterator* <i>iterator</i>)</p>
<dd>
<dt>int <code>librdf_iterator_next</code>(librdf_iterator* <i>iterator</i>)</p>
<dd>
<dt>void* <code>librdf_iterator_get_object</code>(librdf_iterator* <i>iterator</i>)</p>
<dd>
<dt>void* <code>librdf_iterator_get_context</code>(librdf_iterator* <i>iterator</i>)</p>
<dd>
<dt>void* <code>librdf_iterator_get_key</code>(librdf_iterator* <i>iterator</i>)</p>
<dd>
<dt>void* <code>librdf_iterator_get_value</code>(librdf_iterator* <i>iterator</i>)</p>
<dd>
<dt>int <code>librdf_iterator_add_map</code>(librdf_iterator* <i>iterator</i>, void* (*<i>fn</i>)(void* <i>context</i>, void* <i>item</i>), void* <i>context</i>)</p>
<dd>
<dt>void* <code>librdf_iterator_map_remove_duplicate_nodes</code>(void* <i>item</i>, void* <i>user_data</i>)</p>
<dd></dl>
<h3>class digest</h3>
<dl>
<dt>void <code>librdf_digest_register_factory</code>(librdf_world* <i>world</i>, const char* <i>name</i>, void (*<i>factory</i>) (librdf_digest_factory*))</p>
<dd>
<dt>librdf_digest_factory* <code>librdf_get_digest_factory</code>(librdf_world* <i>world</i>, const char* <i>name</i>)</p>
<dd>
<dt>librdf_digest* <code>librdf_new_digest</code>(librdf_world* <i>world</i>, char* <i>name</i>)</p>
<dd>
<dt>librdf_digest* <code>librdf_new_digest_from_factory</code>(librdf_world* <i>world</i>, librdf_digest_factory* <i>factory</i>)</p>
<dd>
<dt>void <code>librdf_free_digest</code>(librdf_digest* <i>digest</i>)</p>
<dd>
<dt>void <code>librdf_digest_init</code>(librdf_digest* <i>digest</i>)</p>
<dd>
<dt>void <code>librdf_digest_update</code>(librdf_digest* <i>digest</i>, unsigned char* <i>buf</i>, size_t <i>length</i>)</p>
<dd>
<dt>void <code>librdf_digest_final</code>(librdf_digest* <i>digest</i>)</p>
<dd>
<dt>void* <code>librdf_digest_get_digest</code>(librdf_digest* <i>digest</i>)</p>
<dd>
<dt>char* <code>librdf_digest_to_string</code>(librdf_digest* <i>digest</i>)</p>
<dd>
<dt>void <code>librdf_digest_print</code>(librdf_digest* <i>digest</i>, FILE* <i>fh</i>)</p>
<dd></dl>
<h3>class uri</h3>
<dl>
<dt>librdf_uri* <code>librdf_new_uri</code>(librdf_world* <i>world</i>, const unsigned char * <i>string</i>)</p>
<dd>
<dt>librdf_uri* <code>librdf_new_uri_from_uri</code>(librdf_uri* <i>uri</i>)</p>
<dd>
<dt>librdf_uri* <code>librdf_new_uri_from_uri_local_name</code>(librdf_uri* <i>uri</i>, const unsigned char* <i>local_name</i>)</p>
<dd>
<dt>void <code>librdf_free_uri</code>(librdf_uri* <i>uri</i>)</p>
<dd>
<dt>unsigned char* <code>librdf_uri_as_string</code>(librdf_uri* <i>uri</i>)</p>
<dd>
<dt>unsigned char* <code>librdf_uri_as_counted_string</code>(librdf_uri* <i>uri</i>, size_t* <i>len_p</i>)</p>
<dd>
<dt>librdf_digest* <code>librdf_uri_get_digest</code>(librdf_uri* <i>uri</i>)</p>
<dd>
<dt>void librdf_uri_print&gt;(librdf_uri* <i>uri</i>, FILE* <i>fh</i>)</p>
<dd>
<dt>unsigned char* <code>librdf_uri_to_string</code>(librdf_uri* <i>uri</i>)</p>
<dd>
<dt>unsigned char* <code>librdf_uri_to_counted_string</code>(librdf_uri* <i>uri</i>, size_t* <i>len_p</i>)</p>
<dd>
<dt>int <code>librdf_uri_equals</code>(librdf_uri* <i>first_uri</i>, librdf_uri* <i>second_uri</i>)</p>
<dd>
<dt>int <code>librdf_uri_is_file_uri</code>(librdf_uri* <i>uri</i>)</p>
<dd>
<dt>const char* <code>librdf_uri_to_filename</code>(librdf_uri* <i>uri</i>)</p>
<dd>
<dt>librdf_uri* <code>librdf_new_uri_normalised_to_base</code>(const unsigned char* <i>uri_string</i>, librdf_uri* <i>source_uri</i>, librdf_uri* <i>base_uri</i>)</p>
<dd>
<dt>librdf_uri* <code>librdf_new_uri_relative_to_base</code>(librdf_uri* <i>base_uri</i>, const unsigned char* <i>uri_string</i>)</p>
<dd>
<dt>librdf_uri* <code>librdf_new_uri_from_filename</code>(librdf_world* <i>world</i>, const char* <i>filename</i>)</p>
<dd></dl>
<h3>class node</h3>
<dl>
<dt>librdf_node* <code>librdf_new_node</code>(librdf_world* <i>world</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_new_node_from_uri_string</code>(librdf_world* <i>world</i>, const char* <i>string</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_new_node_from_uri</code>(librdf_world* <i>world</i>, librdf_uri* <i>uri</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_new_node_from_uri_local_name</code>(librdf_world* <i>world</i>, librdf_uri* <i>uri</i>, const char* <i>local_name</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_new_node_from_normalised_uri_string</code>(librdf_world* <i>world</i>, const char* <i>uri_string</i>, librdf_uri* <i>source_uri</i>, librdf_uri* <i>base_uri</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_new_node_from_literal</code>(librdf_world* <i>world</i>, const char* <i>string</i>, const char* <i>xml_language</i>, int <i>xml_space</i>, int <i>is_wf_xml</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_new_node_from_typed_literal</code>(librdf_world* <i>world</i>, const unsigned char* <i>string</i>, const char* <i>xml_language</i>, librdf_uri* <i>datatype_uri</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_new_node_from_blank_identifier</code>(librdf_world* <i>world</i>, const unsigned char* <i>identifier</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_new_node_from_node</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>void <code>librdf_node_init</code>(librdf_world* <i>world</i>, librdf_node* <i>node</i>)</p>
<dd>
<dt>void <code>librdf_free_node</code>(librdf_node* <i>r</i>)</p>
<dd>
<dt>librdf_uri* <code>librdf_node_get_uri</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>librdf_node_type <code>librdf_node_get_type</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>unsigned char* <code>librdf_node_get_literal_value</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>unsigned char* <code>librdf_node_get_literal_value_as_counted_string</code>(librdf_node* <i>node</i>, size_t* <i>len_p</i>)</p>
<dd>
<dt>char* <code>librdf_node_get_literal_value_as_latin1</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>char* <code>librdf_node_get_literal_value_language</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>int <code>librdf_node_get_literal_value_is_wf_xml</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>librdf_uri* <code>librdf_node_get_literal_value_datatype_uri</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>int <code>librdf_node_get_li_ordinal</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>unsigned char* <code>librdf_node_get_blank_identifier</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>int <code>librdf_node_is_resource</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>int <code>librdf_node_is_literal</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>int <code>librdf_node_is_blank</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>librdf_digest* <code>librdf_node_get_digest</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>size_t <code>librdf_node_encode</code>(librdf_node* <i>node</i>, unsigned char* <i>buffer</i>, size_t <i>length</i>)</p>
<dd>
<dt>size_t <code>librdf_node_decode</code>(librdf_node* <i>node</i>, unsigned char* <i>buffer</i>, size_t <i>length</i>)</p>
<dd>
<dt>unsigned char* <code>librdf_node_to_string</code>(librdf_node* <i>node</i>)</p>
<dd>
<dt>unsigned char* <code>librdf_node_to_counted_string</code>(librdf_node* <i>node</i>, size_t* <i>len_p</i>)</p>
<dd>
<dt>void <code>librdf_node_print</code>(librdf_node* <i>node</i>, FILE* <i>fh</i>)</p>
<dd>
<dt>int <code>librdf_node_equals</code>(librdf_node* <i>first_node</i>, librdf_node* <i>second_node</i>)</p>
<dd></dl>
<h3>class concepts</h3>
<p>The library provides macros for all of the <font SIZE="-1">RDF</font> and <font SIZE="-1">RDFS</font> concepts &#8211; nodes and URIs. For example, <tt>&quot;LIBRDF_MS_Alt&quot;</tt> for the librdf_node for the rdf:Alt concept and <tt>&quot;LIBRDF_MS_Alt_URI&quot;</tt> for the librdf_uri for the <font SIZE="-1">URI</font> reference of rdf:Alt. </p>
<p> <tt>&quot;LIBRDF_URI_RDF_MS&quot;</tt> and <tt>&quot;LIBRDF_URI_RDF_SCHEMA&quot;</tt> provide the librdf_uri objects for the <font SIZE="-1">RDF</font> and <font SIZE="-1">RDFS</font> namespace URIs. They must be copied using <code>librdf_new_uri_from_uri</code> to be shared correctly.</p>
<dl>
<dt>void <code>librdf_get_concept_by_name</code>(librdf_world* <i>world</i>, int <i>is_ms</i>, const char* <i>name</i>, librdf_uri **<i>uri_p</i>, librdf_node **<i>node_p</i>)</p>
<dd></dl>
<h3>class statement</h3>
<dl>
<dt>librdf_statement* <code>librdf_new_statement</code>(librdf_world* <i>world</i>)</p>
<dd>
<dt>librdf_statement* <code>librdf_new_statement_from_statement</code>(librdf_statement* <i>statement</i>)</p>
<dd>
<dt>librdf_statement* <code>librdf_new_statement_from_nodes</code>(librdf_world* <i>world</i>, librdf_node* <i>subject</i>, librdf_node* <i>predicate</i>, librdf_node* <i>object</i>)</p>
<dd>
<dt>void <code>librdf_statement_init</code>(librdf_world* <i>world</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>void <code>librdf_statement_clear</code>(librdf_statement* <i>statement</i>)</p>
<dd>
<dt>void <code>librdf_free_statement</code>(librdf_statement* <i>statement</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_statement_get_subject</code>(librdf_statement* <i>statement</i>)</p>
<dd>
<dt>void <code>librdf_statement_set_subject</code>(librdf_statement* <i>statement</i>, librdf_node* <i>subject</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_statement_get_predicate</code>(librdf_statement* <i>statement</i>)</p>
<dd>
<dt>void <code>librdf_statement_set_predicate</code>(librdf_statement* <i>statement</i>, librdf_node* <i>predicate</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_statement_get_object</code>(librdf_statement* <i>statement</i>)</p>
<dd>
<dt>void <code>librdf_statement_set_object</code>(librdf_statement* <i>statement</i>, librdf_node* <i>object</i>)</p>
<dd>
<dt>int <code>librdf_statement_is_complete</code>(librdf_statement* <i>statement</i>)</p>
<dd>
<dt>char* <code>librdf_statement_to_string</code>(librdf_statement* <i>statement</i>)</p>
<dd>
<dt>void <code>librdf_statement_print</code>(librdf_statement* <i>statement</i>, FILE* <i>fh</i>)</p>
<dd>
<dt>int <code>librdf_statement_equals</code>(librdf_statement* <i>statement1</i>, librdf_statement* <i>statement2</i>)</p>
<dd>
<dt>int <code>librdf_statement_match</code>(librdf_statement* <i>statement</i>, librdf_statement* <i>partial_statement</i>)</p>
<dd>
<dt>size_t <code>librdf_statement_encode</code>(librdf_statement* <i>statement</i>, unsigned char* <i>buffer</i>, size_t <i>length</i>)</p>
<dd>
<dt>size_t <code>librdf_statement_encode_parts</code>(librdf_statement* <i>statement</i>, unsigned char* <i>buffer</i>, size_t <i>length</i>, librdf_statement_part <i>fields</i>)</p>
<dd>
<dt>size_t <code>librdf_statement_decode</code>(librdf_statement* <i>statement</i>, unsigned char* <i>buffer</i>, size_t <i>length</i>)</p>
<dd>
<dt>size_t <code>librdf_statement_decode_parts</code>(librdf_statement* <i>statement</i>, librdf_node** <i>context_node</i>, unsigned char* <i>buffer</i>, size_t <i>length</i>)</p>
<dd></dl>
<h3>class model</h3>
<dl>
<dt>librdf_model* <code>librdf_new_model</code>(librdf_world* <i>world</i>, librdf_storage* <i>storage</i>, char* <i>options_string</i>)</p>
<dd>
<dt>librdf_model* <code>librdf_new_model_with_options</code>(librdf_world* <i>world</i>, librdf_storage* <i>storage</i>, librdf_hash* <i>options</i>)</p>
<dd>
<dt>librdf_model* <code>librdf_new_model_from_model</code>(librdf_model* <i>model</i>)</p>
<dd>
<dt>void <code>librdf_free_model</code>(librdf_model* <i>model</i>)</p>
<dd>
<dt>int <code>librdf_model_size</code>(librdf_model* <i>model</i>)</p>
<dd>
<dt>int <code>librdf_model_add</code>(librdf_model* <i>model</i>, librdf_node* <i>subject</i>, librdf_node* <i>predicate</i>, librdf_node* <i>object</i>)</p>
<dd>
<dt>int <code>librdf_model_add_string_literal_statement</code>(librdf_model* <i>model</i>, librdf_node* <i>subject</i>, librdf_node* <i>predicate</i>, char* <i>string</i>, char* <i>xml_language</i>, int <i>xml_space</i>, int <i>is_wf_xml</i>)</p>
<dd>
<dt>int <code>librdf_model_add_typed_literal_statement</code>(librdf_model* <i>model</i>, librdf_node* <i>subject</i>, librdf_node* <i>predicate</i>, const unsigned char* <i>string</i>, char* <i>xml_language</i>, librdf_uri* <i>datatype_uri</i>)</p>
<dd>
<dt>int <code>librdf_model_add_statement</code>(librdf_model* <i>model</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>int <code>librdf_model_add_statements</code>(librdf_model* <i>model</i>, librdf_stream* <i>statement_stream</i>)</p>
<dd>
<dt>int <code>librdf_model_remove_statement</code>(librdf_model* <i>model</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>int <code>librdf_model_contains_statement</code>(librdf_model* <i>model</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>int <code>librdf_model_has_arc_in</code>(librdf_model* <i>model</i>, librdf_node* <i>node</i>, librdf_node* <i>property</i>)</p>
<dd>
<dt>int <code>librdf_model_has_arc_out</code>(librdf_model* <i>model</i>, librdf_node* <i>node</i>, librdf_node* <i>property</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_model_as_stream</code>(librdf_model* <i>model</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_model_find_statements</code>(librdf_model* <i>model</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_model_find_statements_in_context</code>(librdf_model* <i>model</i>, librdf_statement* <i>statement</i>, librdf_node* <i>context_node</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_model_find_statements_with_options</code>(librdf_model* <i>model</i>, librdf_statement* <i>statement</i>, librdf_node* <i>context_node</i>, librdf_hash* <i>options</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_model_get_contexts</code>(librdf_model* <i>model</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_model_get_sources</code>(librdf_model* <i>model</i>, librdf_node* <i>arc</i>, librdf_node* <i>target</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_model_get_arcs</code>(librdf_model* <i>model</i>, librdf_node* <i>source</i>, librdf_node* <i>target</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_model_get_targets</code>(librdf_model* <i>model</i>, librdf_node* <i>source</i>, librdf_node* <i>arc</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_model_get_source</code>(librdf_model* <i>model</i>, librdf_node* <i>arc</i>, librdf_node* <i>target</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_model_get_arc</code>(librdf_model* <i>model</i>, librdf_node* <i>source</i>, librdf_node* <i>target</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_model_get_target</code>(librdf_model* <i>model</i>, librdf_node* <i>source</i>, librdf_node* <i>arc</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_model_get_arcs_in</code>(librdf_model* <i>model</i>, librdf_node* <i>node</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_model_get_arcs_out</code>(librdf_model* <i>model</i>, librdf_node* <i>node</i>)</p>
<dd>
<dt>int <code>librdf_model_add_submodel</code>(librdf_model* <i>model</i>, librdf_model* <i>sub_model</i>)</p>
<dd>
<dt>int <code>librdf_model_remove_submodel</code>(librdf_model* <i>model</i>, librdf_model* <i>sub_model</i>)</p>
<dd>
<dt>void <code>librdf_model_print</code>(librdf_model* <i>model</i>, FILE* <i>fh</i>)</p>
<dd>
<dt>int <code>librdf_model_context_add_statement</code>(librdf_model* <i>model</i>, librdf_node* <i>context</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>int <code>librdf_model_context_add_statements</code>(librdf_model* <i>model</i>, librdf_node* <i>context</i>, librdf_stream* <i>stream</i>)</p>
<dd>
<dt>int <code>librdf_model_context_remove_statement</code>(librdf_model* <i>model</i>, librdf_node* <i>context</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>int <code>librdf_model_context_remove_statements</code>(librdf_model* <i>model</i>, librdf_node* <i>context</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_model_context_as_stream</code>(librdf_model* <i>model</i>, librdf_node* <i>context</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_model_query</code>(librdf_model* <i>model</i>, librdf_query* <i>query</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_model_query_string</code>(librdf_model* <i>model</i>, const char* <i>name</i>, librdf_uri* <i>uri</i>, const unsigned char* <i>query_string</i>)</p>
<dd>
<dt>void <code>librdf_model_sync</code>(librdf_model* <i>model</i>)</p>
<dd>
<dt>librdf_storage* <code>librdf_model_get_storage</code>(librdf_model* <i>model</i>)</p>
<dd>
<dt>librdf_node* <code>librdf_model_get_feature</code>(librdf_model* <i>model</i>, librdf_uri* <i>feature</i>) =item int <code>librdf_model_set_feature</code>(librdf_model* <i>model</i>, librdf_uri* <i>feature</i>, librdf_node* <i>value</i>)</p>
<dd></dl>
<h3>class storage</h3>
<dl>
<dt>void <code>librdf_storage_register_factory</code>(const char* <i>name</i>, void (*<i>factory</i>) (librdf_storage_factory*))</p>
<dd>
<dt>librdf_storage* <code>librdf_new_storage</code>(librdf_world* <i>world</i>, char* <i>storage_name</i>, char* <i>name</i>, char* <i>options_string</i>)</p>
<dd>
<dt>librdf_storage* <code>librdf_new_storage_with_options</code>(librdf_world* <i>world</i>, char* <i>storage_name</i>, char* <i>name</i>, librdf_hash* <i>options</i>)</p>
<dd>
<dt>librdf_storage* <code>librdf_new_storage_from_storage</code>(librdf_storage* <i>old_storage</i>)</p>
<dd>
<dt>librdf_storage* <code>librdf_new_storage_from_factory</code>(librdf_world* <i>world</i>, librdf_storage_factory* <i>factory</i>, char* <i>name</i>, librdf_hash* <i>options</i>)</p>
<dd>
<dt>void <code>librdf_free_storage</code>(librdf_storage* <i>storage</i>)</p>
<dd>
<dt>int <code>librdf_storage_open</code>(librdf_storage* <i>storage</i>, librdf_model* <i>model</i>)</p>
<dd>
<dt>int <code>librdf_storage_close</code>(librdf_storage* <i>storage</i>)</p>
<dd>
<dt>int <code>librdf_storage_get</code>(librdf_storage* <i>storage</i>, void* <i>key</i>, size_t <i>key_len</i>, void **<i>value</i>, size_t* <i>value_len</i>, unsigned int <i>flags</i>)</p>
<dd>
<dt>int <code>librdf_storage_size</code>(librdf_storage* <i>storage</i>)</p>
<dd>
<dt>int <code>librdf_storage_add_statement</code>(librdf_storage* <i>storage</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>int <code>librdf_storage_add_statements</code>(librdf_storage* <i>storage</i>, librdf_stream* <i>statement_stream</i>)</p>
<dd>
<dt>int <code>librdf_storage_remove_statement</code>(librdf_storage* <i>storage</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>int <code>librdf_storage_contains_statement</code>(librdf_storage* <i>storage</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_storage_serialise</code>(librdf_storage* <i>storage</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_storage_find_statements</code>(librdf_storage* <i>storage</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_storage_get_sources</code>(librdf_storage* <i>storage</i>, librdf_node* <i>arc</i>, librdf_node* <i>target</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_storage_get_arcs</code>(librdf_storage* <i>storage</i>, librdf_node* <i>source</i>, librdf_node* <i>target</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_storage_get_targets</code>(librdf_storage* <i>storage</i>, librdf_node* <i>source</i>, librdf_node* <i>arc</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_storage_get_arcs_in</code>(librdf_storage* <i>storage</i>, librdf_node* <i>node</i>)</p>
<dd>
<dt>librdf_iterator* <code>librdf_storage_get_arcs_out</code>(librdf_storage* <i>storage</i>, librdf_node* <i>node</i>)</p>
<dd>
<dt>int <code>librdf_storage_has_arc_in</code>(librdf_storage* <i>storage</i>, librdf_node* <i>node</i>, librdf_node* <i>property</i>)</p>
<dd>
<dt>int <code>librdf_storage_has_arc_out</code>(librdf_storage* <i>storage</i>, librdf_node* <i>node</i>, librdf_node* <i>property</i>)</p>
<dd>
<dt>int <code>librdf_storage_context_add_statement</code>(librdf_storage* <i>storage</i>, librdf_node* <i>context</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>int <code>librdf_storage_context_add_statements</code>(librdf_storage* <i>storage</i>, librdf_node* <i>context</i>, librdf_stream* <i>stream</i>)</p>
<dd>
<dt>int <code>librdf_storage_context_remove_statement</code>(librdf_storage* <i>storage</i>, librdf_node* <i>context</i>, librdf_statement* <i>statement</i>)</p>
<dd>
<dt>int <code>librdf_storage_context_remove_statements</code>(librdf_storage* <i>storage</i>, librdf_node* <i>context</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_storage_context_as_stream</code>(librdf_storage* <i>storage</i>, librdf_node* <i>context</i>)</p>
<dd>
<dt>int <code>librdf_storage_supports_query</code>(librdf_storage* <i>storage</i>, librdf_query* <i>query</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_storage_query</code>(librdf_storage* <i>storage</i>, librdf_query* <i>query</i>)</p>
<dd>
<dt>void <code>librdf_storage_sync</code>(librdf_storage* <i>storage</i>)</p>
<dd></dl>
<h3>class parser</h3>
<dl>
<dt>void <code>librdf_parser_register_factory</code>(librdf_world* <i>world</i>, const char* <i>name</i>, const char* <i>mime_type</i>, const char* <i>uri_string</i>, void (*<i>factory</i>) (librdf_parser_factory*))</p>
<dd>
<dt>librdf_parser* <code>librdf_new_parser</code>(librdf_world* <i>world</i>, const char* <i>name</i>, const char* <i>mime_type</i>, librdf_uri* <i>type_uri</i>)</p>
<dd>
<dt>librdf_parser* <code>librdf_new_parser_from_factory</code>(librdf_world* <i>world</i>, librdf_parser_factory* <i>factory</i>)</p>
<dd>
<dt>void <code>librdf_free_parser</code>(librdf_parser* <i>parser</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_parser_parse_as_stream</code>(librdf_parser* <i>parser</i>, librdf_uri* <i>uri</i>, librdf_uri* <i>base_uri</i>)</p>
<dd>
<dt>int <code>librdf_parser_parse_into_model</code>(librdf_parser* <i>parser</i>, librdf_uri* <i>uri</i>, librdf_uri* <i>base_uri</i>, librdf_model* <i>model</i>)</p>
<dd>
<dt>librdf_stream* <code>librdf_parser_parse_string_as_stream</code>(librdf_parser* <i>parser</i>, const unsigned char* <i>string</i>, librdf_uri* <i>base_uri</i>)</p>
<dd>
<dt>int librdf_parser_parse_string_into_model(librdf_parser* <i>parser</i>, const unsigned char* <i>string</i>, librdf_uri* <i>base_uri</i>, librdf_model* <i>model</i>)</p>
<dd>
<dt>void <code>librdf_parser_set_error</code>(librdf_parser* <i>parser</i>, void* <i>user_data</i>, void (*<i>error_fn</i>)(void* <i>user_data</i>, const char* <i>msg</i>, &#8230;))</p>
<dd>
<dt>void <code>librdf_parser_set_warning</code>(librdf_parser* <i>parser</i>, void* <i>user_data</i>, void (*<i>warning_fn</i>)(void* <i>user_data</i>, const char* <i>msg</i>, &#8230;))</p>
<dd>
<dt>librdf_node* <code>librdf_parser_get_feature</code>(librdf_parser* <i>parser</i>, librdf_uri* <i>feature</i>)</p>
<dd>
<dt>int <code>librdf_parser_set_feature</code>(librdf_parser* <i>parser</i>, librdf_uri* <i>feature</i>, librdf_node* <i>value</i>)</p>
<dd></dl>
<h3>class serializer</h3>
<dl>
<dt>librdf_serializer* librdf_new_serializer(librdf_world* <i>world</i>, const char *<i>name</i>, const char *<i>mime_type</i>, librdf_uri *<i>type_uri</i>)</p>
<dd>
<dt>librdf_serializer* librdf_new_serializer_from_factory(librdf_world* <i>world</i>, librdf_serializer_factory *<i>factory</i>)</p>
<dd>
<dt>void librdf_free_serializer(librdf_serializer *<i>serializer</i>)</p>
<dd>
<dt>int librdf_serializer_serialize_model(librdf_serializer* <i>serializer</i>, FILE* <i>handle</i>, librdf_uri* <i>base_uri</i>, librdf_model* <i>model</i>)</p>
<dd>
<dt>int librdf_serializer_serialize_model_to_file(librdf_serializer* <i>serializer</i>, const char *<i>name</i>, librdf_uri* <i>base_uri</i>, librdf_model* <i>model</i>)</p>
<dd>
<dt>void librdf_serializer_set_error(librdf_serializer* <i>serializer</i>, void *<i>user_data</i>, void (*<i>error_fn</i>)(void *user_data, const char *msg, &#8230;))</p>
<dd>
<dt>void librdf_serializer_set_warning(librdf_serializer* <i>serializer</i>, void *<i>user_data</i>, void (*<i>warning_fn</i>)(void *user_data, const char *msg, &#8230;))</p>
<dd>
<dt>librdf_node* librdf_serializer_get_feature(librdf_serializer* <i>serializer</i>, librdf_uri* <i>feature</i>)</p>
<dd>
<dt>int librdf_serializer_set_feature(librdf_serializer* <i>serializer</i>, librdf_uri* <i>feature</i>, librdf_node* <i>value</i>)b</p>
<dd>
<dt>int librdf_serializer_set_namespace(librdf_serializer* <i>serializer</i>, librdf_uri* <i>uri</i>, const char* <i>prefix</i>)</p>
<dd></dl>
<h3>class stream</h3>
<dl>
<dt>librdf_stream* <code>librdf_new_stream</code>(librdf_world* <i>world</i>, void* <i>context</i>, int (*<i>end_of_stream</i>)(void*), librdf_statement* (*<i>next_statement</i>)(void*), void (*<i>finished</i>)(void*))</p>
<dd>
<dt>librdf_stream* <code>librdf_new_stream_from_node_iterator</code>(librdf_iterator* <i>iterator</i>, librdf_statement* <i>statement</i>, librdf_statement_part <i>field</i>)</p>
<dd>
<dt>void <code>librdf_free_stream</code>(librdf_stream* <i>stream</i>)</p>
<dd>
<dt>int <code>librdf_stream_end</code>(librdf_stream* <i>stream</i>)</p>
<dd>
<dt>int <code>librdf_stream_next</code>(librdf_stream* <i>stream</i>)</p>
<dd>
<dt>librdf_statement* <code>librdf_stream_get_object</code>(librdf_stream* <i>stream</i>)</p>
<dd>
<dt>void* <code>librdf_stream_get_context</code>(librdf_stream* <i>stream</i>)</p>
<dd>
<dt>void <code>librdf_stream_set_map</code>(librdf_stream* <i>stream</i>, librdf_statement* (*<i>map</i>)(void* <i>context</i>, librdf_statement* <i>statement</i>), void* <i>map_context</i>)</p>
<dd>
<dt>void <code>librdf_stream_print</code>(librdf_stream* <i>stream</i>, FILE* <i>fh</i>)</p>
<dd></dl>
<h2>Examples</h2>
<pre><code>#include &lt;redland.h&gt;

librdf_storage *storage;
librdf_model* model;
librdf_statement* statement;
librdf_world* world

world=librdf_new_world();

librdf_world_open(world);

storage=librdf_new_storage(world, &quot;hashes&quot;, &quot;test&quot;, &quot;hash-type='bdb',dir='.'&quot;);
model=librdf_new_model(world, storage, NULL);
statement=librdf_new_statement_from_nodes(world, librdf_new_node_from_uri_string(world, &quot;http://purl.org/net/dajobe/&quot;), librdf_new_node_from_uri_string(world, &quot;http://purl.org/dc/elements/1.1/creator&quot;), librdf_new_node_from_literal(world, &quot;Dave Beckett&quot;, NULL, 0));

librdf_model_add_statement(model, statement);
librdf_free_statement(statement);

librdf_model_print(model, stdout);

librdf_free_model(model);
librdf_free_storage(storage);
librdf_free_world(world);</code></pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/3-libraptor/">libraptor</a></i>(3), <i><a href="/docs/linux/man/4-libxml/">libxml</a></i>(4).</p>
<h2>History</h2>
<p>The <code>redland</code> <font SIZE="-1">RDF</font> library was created by Dave Beckett in June 2000.</p>
<h2>Author</h2>
<p>Dave Beckett &lt;<a rel="nofollow" href="http://purl.org/net/dajobe/">http://purl.org/net/dajobe/</a>&gt;,</p>
