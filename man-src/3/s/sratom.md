---
title: "sratom(3)"
name: "sratom"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sratom/"
description: "Sratom –"
---

<p>Sratom &#8211;</p>
<h2>Detailed Description</h2>
<p>An LV2 Atom RDF serialisation library.</p>
<h3>Typedefs</h3>
<p>typedef struct SratomImpl <code>Sratom</code></p>
<h3>Enumerations</h3>
<p>enum <code>SratomObjectMode</code> { <code>SRATOM_OBJECT_MODE_BLANK</code>, <code>SRATOM_OBJECT_MODE_BLANK_SUBJECT</code> }</p>
<h3>Functions</h3>
<p><code>Sratom</code> * <code>sratom_new</code> (LV2_URID_Map *map) </p>
<p> void <code>sratom_free</code> (<code>Sratom</code> *sratom) </p>
<p> void <code>sratom_set_sink</code> (<code>Sratom</code> *sratom, const char *base_uri, SerdStatementSink sink, SerdEndSink end_sink, void *handle) </p>
<p> void <code>sratom_set_pretty_numbers</code> (<code>Sratom</code> *sratom, bool pretty_numbers) </p>
<p> void <code>sratom_set_object_mode</code> (<code>Sratom</code> *sratom, <code>SratomObjectMode</code> object_mode) </p>
<p> int <code>sratom_write</code> (<code>Sratom</code> *sratom, LV2_URID_Unmap *unmap, uint32_t flags, const SerdNode *subject, const SerdNode *predicate, uint32_t type, uint32_t size, const void *body) </p>
<p> void <code>sratom_read</code> (<code>Sratom</code> *sratom, LV2_Atom_Forge *forge, SordWorld *world, SordModel *model, const SordNode *subject) </p>
<p> char * <code>sratom_to_turtle</code> (<code>Sratom</code> *sratom, LV2_URID_Unmap *unmap, const char *base_uri, const SerdNode *subject, const SerdNode *predicate, uint32_t type, uint32_t size, const void *body) </p>
<p> LV2_Atom * <code>sratom_from_turtle</code> (<code>Sratom</code> *sratom, const char *base_uri, const SerdNode *subject, const SerdNode *predicate, const char *str) </p>
<p> LV2_Atom_Forge_Ref <code>sratom_forge_sink</code> (LV2_Atom_Forge_Sink_Handle handle, const void *buf, uint32_t size) </p>
<p> LV2_Atom * <code>sratom_forge_deref</code> (LV2_Atom_Forge_Sink_Handle handle, LV2_Atom_Forge_Ref ref)</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct SratomImpl <code>Sratom</code></h3>
<p>Atom serialiser.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>SratomObjectMode</code></h3>
<p>Mode for reading resources to LV2 Objects. This affects how resources (which are either blank nodes or have URIs) are read by <code>sratom_read()</code>, since they may be read as simple references (a URI or blank node ID) or a complete description (an atom &#8216;Object&#8217;). </p>
<p> Currently, blank nodes are always read as Objects, but support for reading blank node IDs may be added in the future. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>SRATOM_OBJECT_MODE_BLANK </i></p>
<dd>Read blank nodes as Objects, and named resources as URIs.</p>
<dt><i>SRATOM_OBJECT_MODE_BLANK_SUBJECT </i></p>
<dd>Read blank nodes and the main subject as Objects, and any other named resources as URIs. The &#8216;main subject&#8217; is the subject parameter passed to <code>sratom_read()</code>; if this is a resource it will be read as an Object, but all other named resources encountered will be read as URIs.</dl>
<h2>Function Documentation</h2>
<h3><code>Sratom</code>* sratom_new (LV2_URID_Map *map)</h3>
<p>Create a new Atom serialiser.</p>
<h3>void sratom_free (<code>Sratom</code> *sratom)</h3>
<p>Free an Atom serialisation.</p>
<h3>void sratom_set_sink (<code>Sratom</code> *sratom, const char *base_uri, SerdStatementSinksink, SerdEndSinkend_sink, void *handle)</h3>
<p>Set the sink(s) where sratom will write its output. This must be called before calling <code>sratom_write()</code>.</p>
<h3>void sratom_set_pretty_numbers (<code>Sratom</code> *sratom, boolpretty_numbers)</h3>
<p>Write pretty numeric literals. If pretty_numbers is true, numbers will be written as pretty Turtle literals, rather than string literals with precise types. The cost of this is that the types might get fudged on a round-trip to RDF and back.</p>
<h3>void sratom_set_object_mode (<code>Sratom</code> *sratom, <code>SratomObjectMode</code>object_mode)</h3>
<p>Configure how resources will be read to form LV2 Objects.</p>
<h3>int sratom_write (<code>Sratom</code> *sratom, LV2_URID_Unmap *unmap, uint32_tflags, const SerdNode *subject, const SerdNode *predicate, uint32_ttype, uint32_tsize, const void *body)</h3>
<p>Write an Atom to RDF. The serialised atom is written to the sink set by <code>sratom_set_sink()</code>. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success, or a non-zero error code otherwise.</dl>
<h3>void sratom_read (<code>Sratom</code> *sratom, LV2_Atom_Forge *forge, SordWorld *world, SordModel *model, const SordNode *subject)</h3>
<p>Read an Atom from RDF. The resulting atom will be written to forge.</p>
<h3>char* sratom_to_turtle (<code>Sratom</code> *sratom, LV2_URID_Unmap *unmap, const char *base_uri, const SerdNode *subject, const SerdNode *predicate, uint32_ttype, uint32_tsize, const void *body)</h3>
<p>Serialise an Atom to a Turtle string. The returned string must be free()&#8217;d by the caller.</p>
<h3>LV2_Atom* sratom_from_turtle (<code>Sratom</code> *sratom, const char *base_uri, const SerdNode *subject, const SerdNode *predicate, const char *str)</h3>
<p>Read an Atom from a Turtle string. The returned atom must be free()&#8217;d by the caller.</p>
<h3>LV2_Atom_Forge_Ref sratom_forge_sink (LV2_Atom_Forge_Sink_Handlehandle, const void *buf, uint32_tsize)</h3>
<p>A convenient resizing sink for LV2_Atom_Forge. The handle must point to an initialized SerdChunk.</p>
<h3>LV2_Atom* sratom_forge_deref (LV2_Atom_Forge_Sink_Handlehandle, LV2_Atom_Forge_Refref)</h3>
<p>The corresponding deref function for sratom_forge_sink.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Sratom from the source code.</p>
