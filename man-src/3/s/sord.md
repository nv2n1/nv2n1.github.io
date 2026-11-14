---
title: "sord(3)"
name: "sord"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sord/"
description: "Sord –"
---

<p>Sord &#8211;</p>
<h2>Detailed Description</h2>
<p>A lightweight RDF model library. </p>
<p> Sord stores RDF (subject object predicate context) quads, where the context may be omitted (to represent triples in the default graph).</p>
<h3>Typedefs</h3>
<p>typedef struct SordWorldImpl <code>SordWorld</code> </p>
<p> typedef struct SordModelImpl <code>SordModel</code> </p>
<p> typedef struct SordInserterImpl <code>SordInserter</code> </p>
<p> typedef struct SordIterImpl <code>SordIter</code> </p>
<p> typedef struct SordNodeImpl <code>SordNode</code> </p>
<p> typedef const <code>SordNode</code> * <code>SordQuad</code> [4]</p>
<h3>Enumerations</h3>
<p>enum <code>SordQuadIndex</code> { <code>SORD_SUBJECT</code> = 0, <code>SORD_PREDICATE</code> = 1, <code>SORD_OBJECT</code> = 2, <code>SORD_GRAPH</code> = 3 } </p>
<p> enum <code>SordNodeType</code> { <code>SORD_URI</code> = 1, <code>SORD_BLANK</code> = 2, <code>SORD_LITERAL</code> = 3 } </p>
<p> enum <code>SordIndexOption</code> { <code>SORD_SPO</code> = 1, <code>SORD_SOP</code> = 1 &lt;&lt; 1, <code>SORD_OPS</code> = 1 &lt;&lt; 2, <code>SORD_OSP</code> = 1 &lt;&lt; 3, <code>SORD_PSO</code> = 1 &lt;&lt; 4, <code>SORD_POS</code> = 1 &lt;&lt; 5 }</p>
<h3>World</h3>
<p><code>SordWorld</code> * <code>sord_world_new</code> (void) </p>
<p> void <code>sord_world_free</code> (<code>SordWorld</code> *world) </p>
<p> void <code>sord_world_set_error_sink</code> (<code>SordWorld</code> *world, SerdErrorSink error_sink, void *handle)</p>
<h3>Node</h3>
<p><code>SordNode</code> * <code>sord_new_uri</code> (<code>SordWorld</code> *world, const uint8_t *uri) </p>
<p> <code>SordNode</code> * <code>sord_new_relative_uri</code> (<code>SordWorld</code> *world, const uint8_t *str, const uint8_t *base_uri) </p>
<p> <code>SordNode</code> * <code>sord_new_blank</code> (<code>SordWorld</code> *world, const uint8_t *str) </p>
<p> <code>SordNode</code> * <code>sord_new_literal</code> (<code>SordWorld</code> *world, <code>SordNode</code> *datatype, const uint8_t *str, const char *lang) </p>
<p> <code>SordNode</code> * <code>sord_node_copy</code> (const <code>SordNode</code> *node) </p>
<p> void <code>sord_node_free</code> (<code>SordWorld</code> *world, <code>SordNode</code> *node) </p>
<p> <code>SordNodeType</code> <code>sord_node_get_type</code> (const <code>SordNode</code> *node) </p>
<p> const uint8_t * <code>sord_node_get_string</code> (const <code>SordNode</code> *node) </p>
<p> const uint8_t * <code>sord_node_get_string_counted</code> (const <code>SordNode</code> *node, size_t *len) </p>
<p> const char * <code>sord_node_get_language</code> (const <code>SordNode</code> *node) </p>
<p> <code>SordNode</code> * <code>sord_node_get_datatype</code> (const <code>SordNode</code> *node) </p>
<p> SerdNodeFlags <code>sord_node_get_flags</code> (const <code>SordNode</code> *node) </p>
<p> bool <code>sord_node_is_inline_object</code> (const <code>SordNode</code> *node) </p>
<p> bool <code>sord_node_equals</code> (const <code>SordNode</code> *a, const <code>SordNode</code> *b) </p>
<p> const SerdNode * <code>sord_node_to_serd_node</code> (const <code>SordNode</code> *node) </p>
<p> <code>SordNode</code> * <code>sord_node_from_serd_node</code> (<code>SordWorld</code> *world, SerdEnv *env, const SerdNode *node, const SerdNode *datatype, const SerdNode *lang)</p>
<h3>Model</h3>
<p><code>SordModel</code> * <code>sord_new</code> (<code>SordWorld</code> *world, unsigned indices, bool graphs) </p>
<p> void <code>sord_free</code> (<code>SordModel</code> *model) </p>
<p> <code>SordWorld</code> * <code>sord_get_world</code> (<code>SordModel</code> *model) </p>
<p> size_t <code>sord_num_nodes</code> (const <code>SordWorld</code> *world) </p>
<p> size_t <code>sord_num_quads</code> (const <code>SordModel</code> *model) </p>
<p> <code>SordIter</code> * <code>sord_begin</code> (const <code>SordModel</code> *model) </p>
<p> <code>SordIter</code> * <code>sord_find</code> (<code>SordModel</code> *model, const <code>SordQuad</code> pat) </p>
<p> <code>SordIter</code> * <code>sord_search</code> (<code>SordModel</code> *model, const <code>SordNode</code> *s, const <code>SordNode</code> *p, const <code>SordNode</code> *o, const <code>SordNode</code> *g) </p>
<p> <code>SordNode</code> * <code>sord_get</code> (<code>SordModel</code> *model, const <code>SordNode</code> *s, const <code>SordNode</code> *p, const <code>SordNode</code> *o, const <code>SordNode</code> *g) </p>
<p> bool <code>sord_ask</code> (<code>SordModel</code> *model, const <code>SordNode</code> *s, const <code>SordNode</code> *p, const <code>SordNode</code> *o, const <code>SordNode</code> *g) </p>
<p> uint64_t <code>sord_count</code> (<code>SordModel</code> *model, const <code>SordNode</code> *s, const <code>SordNode</code> *p, const <code>SordNode</code> *o, const <code>SordNode</code> *g) </p>
<p> bool <code>sord_contains</code> (<code>SordModel</code> *model, const <code>SordQuad</code> pat) </p>
<p> bool <code>sord_add</code> (<code>SordModel</code> *model, const <code>SordQuad</code> quad) </p>
<p> void <code>sord_remove</code> (<code>SordModel</code> *model, const <code>SordQuad</code> quad)</p>
<h3>Inserter</h3>
<p><code>SordInserter</code> * <code>sord_inserter_new</code> (<code>SordModel</code> *model, SerdEnv *env) </p>
<p> void <code>sord_inserter_free</code> (<code>SordInserter</code> *inserter) </p>
<p> SerdStatus <code>sord_inserter_set_base_uri</code> (<code>SordInserter</code> *inserter, const SerdNode *uri) </p>
<p> SerdStatus <code>sord_inserter_set_prefix</code> (<code>SordInserter</code> *inserter, const SerdNode *name, const SerdNode *uri) </p>
<p> SerdStatus <code>sord_inserter_write_statement</code> (<code>SordInserter</code> *inserter, SerdStatementFlags flags, const SerdNode *graph, const SerdNode *subject, const SerdNode *predicate, const SerdNode *object, const SerdNode *object_datatype, const SerdNode *object_lang)</p>
<h3>Iteration</h3>
<p>void <code>sord_iter_get</code> (const <code>SordIter</code> *iter, <code>SordQuad</code> quad) </p>
<p> const <code>SordNode</code> * <code>sord_iter_get_node</code> (const <code>SordIter</code> *iter, <code>SordQuadIndex</code> index) </p>
<p> const <code>SordModel</code> * <code>sord_iter_get_model</code> (<code>SordIter</code> *iter) </p>
<p> bool <code>sord_iter_next</code> (<code>SordIter</code> *iter) </p>
<p> bool <code>sord_iter_end</code> (const <code>SordIter</code> *iter) </p>
<p> void <code>sord_iter_free</code> (<code>SordIter</code> *iter)</p>
<h3>Utilities</h3>
<p>bool <code>sord_quad_match</code> (const <code>SordQuad</code> x, const <code>SordQuad</code> y)</p>
<h3>Serialisation</h3>
<p>SerdReader * <code>sord_new_reader</code> (<code>SordModel</code> *model, SerdEnv *env, SerdSyntax syntax, <code>SordNode</code> *graph) </p>
<p> bool <code>sord_write</code> (<code>SordModel</code> *model, SerdWriter *writer, <code>SordNode</code> *graph) </p>
<p> bool <code>sord_write_iter</code> (<code>SordIter</code> *iter, SerdWriter *writer)</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct SordWorldImpl <code>SordWorld</code></h3>
<p>Sord World. The World represents all library state, including interned strings.</p>
<h3>typedef struct SordModelImpl <code>SordModel</code></h3>
<p>Sord Model. A model is an indexed set of Quads (i.e. it can contain several RDF graphs). It may be searched using various patterns depending on which indices are enabled.</p>
<h3>typedef struct SordInserterImpl <code>SordInserter</code></h3>
<p>Model Inserter. An inserter is used for writing statements to a model using the Serd sink interface. This makes it simple to write to a model directly using a SerdReader, or any other code that writes statements to a SerdStatementSink.</p>
<h3>typedef struct SordIterImpl <code>SordIter</code></h3>
<p>Model Iterator.</p>
<h3>typedef struct SordNodeImpl <code>SordNode</code></h3>
<p>RDF Node. A Node is a component of a Quad. Nodes may be URIs, blank nodes, or (in the case of quad objects only) string literals. Literal nodes may have an associate language or datatype (but not both).</p>
<h3>typedef const <code>SordNode</code>* SordQuad[4]</h3>
<p>Quad of nodes (a statement), or a quad pattern. Nodes are ordered (S P O G). The ID of the default graph is 0.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>SordQuadIndex</code></h3>
<p>Index into a SordQuad. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>SORD_SUBJECT </i></p>
<dd>Subject.</p>
<dt><i>SORD_PREDICATE </i></p>
<dd>Predicate (a.k.a. &#8216;key&#8217;)</p>
<dt><i>SORD_OBJECT </i></p>
<dd>Object (a.k.a. &#8216;value&#8217;)</p>
<dt><i>SORD_GRAPH </i></p>
<dd>Graph (a.k.a. &#8216;context&#8217;)</dl>
<h3>enum <code>SordNodeType</code></h3>
<p>Type of a node. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>SORD_URI </i></p>
<dd>URI.</p>
<dt><i>SORD_BLANK </i></p>
<dd>Blank node identifier.</p>
<dt><i>SORD_LITERAL </i></p>
<dd>Literal (string with optional lang or datatype)</dl>
<h3>enum <code>SordIndexOption</code></h3>
<p>Indexing option. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>SORD_SPO </i></p>
<dd>Subject, Predicate, Object.</p>
<dt><i>SORD_SOP </i></p>
<dd>Subject, Object, Predicate.</p>
<dt><i>SORD_OPS </i></p>
<dd>Object, Predicate, Subject.</p>
<dt><i>SORD_OSP </i></p>
<dd>Object, Subject, Predicate.</p>
<dt><i>SORD_PSO </i></p>
<dd>Predicate, Subject, Object.</p>
<dt><i>SORD_POS </i></p>
<dd>Predicate, Object, Subject.</dl>
<h2>Function Documentation</h2>
<h3><code>SordWorld</code>* sord_world_new (void)</h3>
<p>Create a new Sord World. It is safe to use multiple worlds in one process, though no data (e.g. nodes) can be shared between worlds, and this should be avoided if possible for performance reasons.</p>
<h3>void sord_world_free (<code>SordWorld</code> *world)</h3>
<p>Free world.</p>
<h3>void sord_world_set_error_sink (<code>SordWorld</code> *world, SerdErrorSinkerror_sink, void *handle)</h3>
<p>Set a function to be called when errors occur. The error_sink will be called with handle as its first argument. If no error function is set, errors are printed to stderr.</p>
<h3><code>SordNode</code>* sord_new_uri (<code>SordWorld</code> *world, const uint8_t *uri)</h3>
<p>Get a URI node from a string. Note this function measures str, which is a common bottleneck. Use sord_node_from_serd_node instead if str is already measured.</p>
<h3><code>SordNode</code>* sord_new_relative_uri (<code>SordWorld</code> *world, const uint8_t *str, const uint8_t *base_uri)</h3>
<p>Get a URI node from a relative URI string.</p>
<h3><code>SordNode</code>* sord_new_blank (<code>SordWorld</code> *world, const uint8_t *str)</h3>
<p>Get a blank node from a string. Note this function measures str, which is a common bottleneck. Use sord_node_from_serd_node instead if str is already measured.</p>
<h3><code>SordNode</code>* sord_new_literal (<code>SordWorld</code> *world, <code>SordNode</code> *datatype, const uint8_t *str, const char *lang)</h3>
<p>Get a literal node from a string. Note this function measures str, which is a common bottleneck. Use sord_node_from_serd_node instead if str is already measured.</p>
<h3><code>SordNode</code>* sord_node_copy (const <code>SordNode</code> *node)</h3>
<p>Copy a node (obtain a reference). Node that since nodes are interned and reference counted, this does not actually create a deep copy of node.</p>
<h3>void sord_node_free (<code>SordWorld</code> *world, <code>SordNode</code> *node)</h3>
<p>Free a node (drop a reference).</p>
<h3><code>SordNodeType</code> sord_node_get_type (const <code>SordNode</code> *node)</h3>
<p>Return the type of a node (SORD_URI, SORD_BLANK, or SORD_LITERAL).</p>
<h3>const uint8_t* sord_node_get_string (const <code>SordNode</code> *node)</h3>
<p>Return the string value of a node.</p>
<h3>const uint8_t* sord_node_get_string_counted (const <code>SordNode</code> *node, size_t *len)</h3>
<p>Return the string value of a node, and set len to its length.</p>
<h3>const char* sord_node_get_language (const <code>SordNode</code> *node)</h3>
<p>Return the language of a literal node (or NULL).</p>
<h3><code>SordNode</code>* sord_node_get_datatype (const <code>SordNode</code> *node)</h3>
<p>Return the datatype URI of a literal node (or NULL).</p>
<h3>SerdNodeFlags sord_node_get_flags (const <code>SordNode</code> *node)</h3>
<p>Return the flags (string attributes) of a node.</p>
<h3>bool sord_node_is_inline_object (const <code>SordNode</code> *node)</h3>
<p>Return true iff node can be serialised as an inline object. More specifically, this returns true iff the node is the object field of exactly one statement, and therefore can be inlined since it needn&#8217;t be referred to by name.</p>
<h3>bool sord_node_equals (const <code>SordNode</code> *a, const <code>SordNode</code> *b)</h3>
<p>Return true iff a is equal to b. Note this is much faster than comparing the node&#8217;s strings.</p>
<h3>const SerdNode* sord_node_to_serd_node (const <code>SordNode</code> *node)</h3>
<p>Return a SordNode as a SerdNode. The returned node is shared and must not be freed or modified.</p>
<h3><code>SordNode</code>* sord_node_from_serd_node (<code>SordWorld</code> *world, SerdEnv *env, const SerdNode *node, const SerdNode *datatype, const SerdNode *lang)</h3>
<p>Create a new SordNode from a SerdNode. The returned node must be freed using sord_node_free.</p>
<h3><code>SordModel</code>* sord_new (<code>SordWorld</code> *world, unsignedindices, boolgraphs)</h3>
<p>Create a new model. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>world</i> The world in which to make this model.<br />
 <i>indices</i> SordIndexOption flags (e.g. SORD_SPO|SORD_OPS). Be sure to enable an index where the most significant node(s) are not variables in your queries (e.g. to make (? P O) queries, enable either SORD_OPS or SORD_POS).<br />
 <i>graphs</i> If true, store (and index) graph contexts.</dl>
<h3>void sord_free (<code>SordModel</code> *model)</h3>
<p>Close and free model.</p>
<h3><code>SordWorld</code>* sord_get_world (<code>SordModel</code> *model)</h3>
<p>Get the world associated with model.</p>
<h3>size_t sord_num_nodes (const <code>SordWorld</code> *world)</h3>
<p>Return the number of nodes stored in world. Nodes are included in this count iff they are a part of a quad in world.</p>
<h3>size_t sord_num_quads (const <code>SordModel</code> *model)</h3>
<p>Return the number of quads stored in model.</p>
<h3><code>SordIter</code>* sord_begin (const <code>SordModel</code> *model)</h3>
<p>Return an iterator to the start of model.</p>
<h3><code>SordIter</code>* sord_find (<code>SordModel</code> *model, const <code>SordQuad</code>pat)</h3>
<p>Search for statements by a quad pattern. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>an iterator to the first match, or NULL if no matches found.</dl>
<h3><code>SordIter</code>* sord_search (<code>SordModel</code> *model, const <code>SordNode</code> *s, const <code>SordNode</code> *p, const <code>SordNode</code> *o, const <code>SordNode</code> *g)</h3>
<p>Search for statements by nodes. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>an iterator to the first match, or NULL if no matches found.</dl>
<h3><code>SordNode</code>* sord_get (<code>SordModel</code> *model, const <code>SordNode</code> *s, const <code>SordNode</code> *p, const <code>SordNode</code> *o, const <code>SordNode</code> *g)</h3>
<p>Search for a single node that matches a pattern. Exactly one of s, p, o must be NULL. This function is mainly useful for predicates that only have one value. The returned node must be freed using sord_node_free. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>the first matching node, or NULL if no matches are found.</dl>
<h3>bool sord_ask (<code>SordModel</code> *model, const <code>SordNode</code> *s, const <code>SordNode</code> *p, const <code>SordNode</code> *o, const <code>SordNode</code> *g)</h3>
<p>Return true iff a statement exists.</p>
<h3>uint64_t sord_count (<code>SordModel</code> *model, const <code>SordNode</code> *s, const <code>SordNode</code> *p, const <code>SordNode</code> *o, const <code>SordNode</code> *g)</h3>
<p>Return the number of matching statements.</p>
<h3>bool sord_contains (<code>SordModel</code> *model, const <code>SordQuad</code>pat)</h3>
<p>Check if model contains a triple pattern.</p>
<h3>bool sord_add (<code>SordModel</code> *model, const <code>SordQuad</code>quad)</h3>
<p>Add a quad to a model.</p>
<h3>void sord_remove (<code>SordModel</code> *model, const <code>SordQuad</code>quad)</h3>
<p>Remove a quad from a model. Note that is it illegal to remove while iterating over model.</p>
<h3><code>SordInserter</code>* sord_inserter_new (<code>SordModel</code> *model, SerdEnv *env)</h3>
<p>Create an inserter for writing statements to a model.</p>
<h3>void sord_inserter_free (<code>SordInserter</code> *inserter)</h3>
<p>Free an inserter.</p>
<h3>SerdStatus sord_inserter_set_base_uri (<code>SordInserter</code> *inserter, const SerdNode *uri)</h3>
<p>Set the current base URI for writing to the model. Note this function can be safely casted to SerdBaseSink.</p>
<h3>SerdStatus sord_inserter_set_prefix (<code>SordInserter</code> *inserter, const SerdNode *name, const SerdNode *uri)</h3>
<p>Set a namespace prefix for writing to the model. Note this function can be safely casted to SerdPrefixSink.</p>
<h3>SerdStatus sord_inserter_write_statement (<code>SordInserter</code> *inserter, SerdStatementFlagsflags, const SerdNode *graph, const SerdNode *subject, const SerdNode *predicate, const SerdNode *object, const SerdNode *object_datatype, const SerdNode *object_lang)</h3>
<p>Write a statement to the model. Note this function can be safely casted to SerdStatementSink.</p>
<h3>void sord_iter_get (const <code>SordIter</code> *iter, <code>SordQuad</code>quad)</h3>
<p>Set quad to the quad pointed to by iter.</p>
<h3>const <code>SordNode</code>* sord_iter_get_node (const <code>SordIter</code> *iter, <code>SordQuadIndex</code>index)</h3>
<p>Return a field of the quad pointed to by iter.</p>
<h3>const <code>SordModel</code>* sord_iter_get_model (<code>SordIter</code> *iter)</h3>
<p>Return the store pointed to by iter.</p>
<h3>bool sord_iter_next (<code>SordIter</code> *iter)</h3>
<p>Increment iter to point to the next statement.</p>
<h3>bool sord_iter_end (const <code>SordIter</code> *iter)</h3>
<p>Return true iff iter is at the end of its range.</p>
<h3>void sord_iter_free (<code>SordIter</code> *iter)</h3>
<p>Free iter.</p>
<h3>bool sord_quad_match (const <code>SordQuad</code>x, const <code>SordQuad</code>y)</h3>
<p>Match two quads (using ID comparison only). This function is a straightforward and fast equivalence match with wildcard support (ID 0 is a wildcard). It does not actually read node data. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>true iff x and y match.</dl>
<h3>SerdReader* sord_new_reader (<code>SordModel</code> *model, SerdEnv *env, SerdSyntaxsyntax, <code>SordNode</code> *graph)</h3>
<p>Return a reader that will read into model.</p>
<h3>bool sord_write (<code>SordModel</code> *model, SerdWriter *writer, <code>SordNode</code> *graph)</h3>
<p>Write a model to a writer.</p>
<h3>bool sord_write_iter (<code>SordIter</code> *iter, SerdWriter *writer)</h3>
<p>Write a range to a writer. This increments iter to its end, then frees it.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Sord from the source code.</p>
