---
title: "mxml(3)"
name: "mxml"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mxml/"
description: "mxml – Mini-XML API"
---

<p>mxml &#8211; Mini-XML API</p>
<h2>Include File</h2>
<p>#include &lt;mxml.h&gt;</p>
<h2>Library</h2>
<p>-lmxml</p>
<h2>Description</h2>
<p>Mini-XML is a small XML parsing library that you can use to read XML and XML-like data files in your application without requiring large non-standard libraries. Mini-XML only requires an ANSI C compatible compiler (GCC works, as do most vendors&#8217; ANSI C compilers) and a &quot;make&quot; program. </p>
<p> Mini-XML provides the following functionality:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Reading of UTF-8 and UTF-16 and writing of UTF-8 encoded XML files and strings.</p>
<dt>&bull;</p>
<dd>Data is stored in a linked-list tree structure, preserving the XML data hierarchy.</p>
<dt>&bull;</p>
<dd>Supports arbitrary element names, attributes, and attribute values with no preset limits, just available memory.</p>
<dt>&bull;</p>
<dd>Supports integer, real, opaque (&quot;CDATA&quot;), and text data types in &quot;leaf&quot; nodes.</p>
<dt>&bull;</p>
<dd>Functions for creating, indexing, and managing trees of data.</p>
<dt>&bull;</p>
<dd>&quot;Find&quot; and &quot;walk&quot; functions for easily locating and navigating trees of data.</dl>
<p> Mini-XML doesn&#8217;t do validation or other types of processing on the data based upon schema files or other sources of definition information, nor does it support character entities other than those required by the XML specification.</p>
<h2>Using Mini-Xml</h2>
<p>Mini-XML provides a single header file which you include: </p>
<pre> #include &lt;mxml.h&gt;</pre>
<p>Nodes are defined by the &quot;mxml_node_t&quot; structure; the &quot;type&quot; member defines the node type (element, integer, opaque, real, or text) which determines which value you want to look at in the &quot;value&quot; union. New nodes can be created using the &quot;mxmlNewElement()&quot;, &quot;mxmlNewInteger()&quot;, &quot;mxmlNewOpaque()&quot;, &quot;mxmlNewReal()&quot;, and &quot;mxmlNewText()&quot; functions. Only elements can have child nodes, and the top node must be an element, usually &quot;?xml&quot;. </p>
<p> You load an XML file using the &quot;mxmlLoadFile()&quot; function: </p>
<pre> FILE *fp;
 mxml_node_t *tree;
 fp = fopen(&quot;filename.xml&quot;, &quot;r&quot;);
 tree = mxmlLoadFile(NULL, fp, MXML_NO_CALLBACK);
 fclose(fp);</pre>
<p>Similarly, you save an XML file using the &quot;mxmlSaveFile()&quot; function: </p>
<pre> FILE *fp;
 mxml_node_t *tree;
 fp = fopen(&quot;filename.xml&quot;, &quot;w&quot;);
 mxmlSaveFile(tree, fp, MXML_NO_CALLBACK);
 fclose(fp);</pre>
<p>The &quot;mxmlLoadString()&quot;, &quot;mxmlSaveAllocString()&quot;, and &quot;mxmlSaveString()&quot; functions load XML node trees from and save XML node trees to strings: </p>
<pre> char buffer[8192];
 char *ptr;
 mxml_node_t *tree;
 ...
 tree = mxmlLoadString(NULL, buffer, MXML_NO_CALLBACK);
 ...
 mxmlSaveString(tree, buffer, sizeof(buffer),
 MXML_NO_CALLBACK);
 ...
 ptr = mxmlSaveAllocString(tree, MXML_NO_CALLBACK);</pre>
<p>You can find a named element/node using the &quot;mxmlFindElement()&quot; function: </p>
<pre> mxml_node_t *node = mxmlFindElement(tree, tree, &quot;name&quot;,
 &quot;attr&quot;, &quot;value&quot;,
 MXML_DESCEND);</pre>
<p>The &quot;name&quot;, &quot;attr&quot;, and &quot;value&quot; arguments can be passed as NULL to act as wildcards, e.g.: </p>
<pre> /* Find the first &quot;a&quot; element */
 node = mxmlFindElement(tree, tree, &quot;a&quot;, NULL, NULL,
 MXML_DESCEND);
 /* Find the first &quot;a&quot; element with &quot;href&quot; attribute */
 node = mxmlFindElement(tree, tree, &quot;a&quot;, &quot;href&quot;, NULL,
 MXML_DESCEND);
 /* Find the first &quot;a&quot; element with &quot;href&quot; to a URL */
 node = mxmlFindElement(tree, tree, &quot;a&quot;, &quot;href&quot;,
 &quot;<a rel="nofollow" href="http://www.easysw.com/~mike/mxml/">http://www.easysw.com/~mike/mxml/</a>&quot;,
 MXML_DESCEND);
 /* Find the first element with a &quot;src&quot; attribute*/
 node = mxmlFindElement(tree, tree, NULL, &quot;src&quot;, NULL,
 MXML_DESCEND);
 /* Find the first element with a &quot;src&quot; = &quot;foo.jpg&quot; */
 node = mxmlFindElement(tree, tree, NULL, &quot;src&quot;,
 &quot;foo.jpg&quot;, MXML_DESCEND);</pre>
<p>You can also iterate with the same function: </p>
<pre> mxml_node_t *node;
 for (node = mxmlFindElement(tree, tree, &quot;name&quot;, NULL,
 NULL, MXML_DESCEND);
 node != NULL;
 node = mxmlFindElement(node, tree, &quot;name&quot;, NULL,
 NULL, MXML_DESCEND))
 {
 ... do something ...
 }</pre>
<p>To find the value of a specific node in the tree, use the &quot;mxmlFindPath()&quot; function: </p>
<pre> mxml_node_t *value = mxmlFindPath(tree, &quot;path/to/*/foo/bar&quot;);</pre>
<p>The &quot;mxmlGetInteger()&quot;, &quot;mxmlGetOpaque()&quot;, &quot;mxmlGetReal()&quot;, and &quot;mxmlGetText()&quot; functions retrieve the value from a node: </p>
<pre> mxml_node_t *node;
 int intvalue = mxmlGetInteger(node);
 const char *opaquevalue = mxmlGetOpaque(node);
 double realvalue = mxmlGetReal(node);
 int whitespacevalue;
 const char *textvalue = mxmlGetText(node, &amp;whitespacevalue);</pre>
<p>Finally, once you are done with the XML data, use the &quot;mxmlDelete()&quot; function to recursively free the memory that is used for a particular node or the entire tree: </p>
<pre> mxmlDelete(tree);</pre>
<h2>Enumerations</h2>
<h3>mxml_sax_event_e</h3>
<p>SAX event type.</p>
<dl COMPACT>
<dt>MXML_SAX_CDATA</p>
<dd>CDATA node</p>
<dt>MXML_SAX_COMMENT</p>
<dd>Comment node</p>
<dt>MXML_SAX_DATA</p>
<dd>Data node</p>
<dt>MXML_SAX_DIRECTIVE</p>
<dd>Processing directive node</p>
<dt>MXML_SAX_ELEMENT_CLOSE</p>
<dd>Element closed</p>
<dt>MXML_SAX_ELEMENT_OPEN</p>
<dd>Element opened</dl>
<h3>mxml_type_e</h3>
<p>The XML node type.</p>
<dl COMPACT>
<dt>MXML_CUSTOM</p>
<dd>Custom data</p>
<dt>MXML_ELEMENT</p>
<dd>XML element with attributes</p>
<dt>MXML_IGNORE</p>
<dd>Ignore/throw away node</p>
<dt>MXML_INTEGER</p>
<dd>Integer value</p>
<dt>MXML_OPAQUE</p>
<dd>Opaque string</p>
<dt>MXML_REAL</p>
<dd>Real value</p>
<dt>MXML_TEXT</p>
<dd>Text fragment</dl>
<h2>Functions</h2>
<h3>mxmlAdd</h3>
<p>Add a node to a tree. </p>
<pre>void mxmlAdd (
 mxml_node_t *parent,
 int where,
 mxml_node_t *child,
 mxml_node_t *node
);</pre>
<p>Adds the specified node to the parent. If the child argument is not NULL, puts the new node before or after the specified child depending on the value of the where argument. If the child argument is NULL, puts the new node at the beginning of the child list (MXML_ADD_BEFORE) or at the end of the child list (MXML_ADD_AFTER). The constant MXML_ADD_TO_PARENT can be used to specify a NULL child pointer.</p>
<h3>mxmlDelete</h3>
<p>Free this node&#8230; </p>
<pre>void mxmlDelete (
 mxml_node_t *node
);</pre>
<h3>mxmlElementDeleteAttr</h3>
<p>Delete an attribute. </p>
<pre>void mxmlElementDeleteAttr (
 mxml_node_t *node,
 const char *name
);</pre>
<h3>mxmlElementGetAttr</h3>
<p>Get an attribute. </p>
<pre>const char * mxmlElementGetAttr (
 mxml_node_t *node,
 const char *name
);</pre>
<p>This function returns NULL if the node is not an element or the named attribute does not exist.</p>
<h3>mxmlElementSetAttr</h3>
<p>Set an attribute. </p>
<pre>void mxmlElementSetAttr (
 mxml_node_t *node,
 const char *name,
 const char *value
);</pre>
<p>If the named attribute already exists, the value of the attribute is replaced by the new string value. The string value is copied into the element node. This function does nothing if the node is not an element.</p>
<h3>mxmlElementSetAttrf</h3>
<p>Set an attribute with a formatted value. </p>
<pre>void mxmlElementSetAttrf (
 mxml_node_t *node,
 const char *name,
 const char *format,
 ...
);</pre>
<p>If the named attribute already exists, the value of the attribute is replaced by the new formatted string. The formatted string value is copied into the element node. This function does nothing if the node is not an element. </p>
<h3>mxmlEntityAddCallback</h3>
<p>Add a callback to convert entities to Unicode. </p>
<pre>int mxmlEntityAddCallback (
 mxml_entity_cb_t cb
);</pre>
<h3>mxmlEntityGetName</h3>
<p>Get the name that corresponds to the character value. </p>
<pre>const char * mxmlEntityGetName (
 int val
);</pre>
<p>If val does not need to be represented by a named entity, NULL is returned.</p>
<h3>mxmlEntityGetValue</h3>
<p>Get the character corresponding to a named entity. </p>
<pre>int mxmlEntityGetValue (
 const char *name
);</pre>
<p>The entity name can also be a numeric constant. -1 is returned if the name is not known.</p>
<h3>mxmlEntityRemoveCallback</h3>
<p>Remove a callback. </p>
<pre>void mxmlEntityRemoveCallback (
 mxml_entity_cb_t cb
);</pre>
<h3>mxmlFindElement</h3>
<p>Find the named element. </p>
<pre>mxml_node_t * mxmlFindElement (
 mxml_node_t *node,
 mxml_node_t *top,
 const char *name,
 const char *attr,
 const char *value,
 int descend
);</pre>
<p>The search is constrained by the name, attribute name, and value; any NULL names or values are treated as wildcards, so different kinds of searches can be implemented by looking for all elements of a given name or all elements with a specific attribute. The descend argument determines whether the search descends into child nodes; normally you will use MXML_DESCEND_FIRST for the initial search and MXML_NO_DESCEND to find additional direct descendents of the node. The top node argument constrains the search to a particular node&#8217;s children.</p>
<h3>mxmlFindPath</h3>
<p>Find a node with the given path. </p>
<pre>mxml_node_t * mxmlFindPath (
 mxml_node_t *top,
 const char *path
);</pre>
<p>The &quot;path&quot; is a slash-separated list of element names. The name &quot;*&quot; is considered a wildcard for one or more levels of elements. For example, &quot;foo/one/two&quot;, &quot;bar/two/one&quot;, &quot;*/one&quot;, and so forth. </p>
<p> The first child node of the found node is returned if the given node has children and the first child is a value node. </p>
<h3>mxmlGetCDATA</h3>
<p>Get the value for a CDATA node. </p>
<pre>const char * mxmlGetCDATA (
 mxml_node_t *node
);</pre>
<p><code>NULL</code> is returned if the node is not a CDATA element. </p>
<h3>mxmlGetCustom</h3>
<p>Get the value for a custom node. </p>
<pre>const void * mxmlGetCustom (
 mxml_node_t *node
);</pre>
<p><code>NULL</code> is returned if the node (or its first child) is not a custom value node. </p>
<h3>mxmlGetElement</h3>
<p>Get the name for an element node. </p>
<pre>const char * mxmlGetElement (
 mxml_node_t *node
);</pre>
<p><code>NULL</code> is returned if the node is not an element node. </p>
<h3>mxmlGetFirstChild</h3>
<p>Get the first child of an element node. </p>
<pre>mxml_node_t * mxmlGetFirstChild (
 mxml_node_t *node
);</pre>
<p><code>NULL</code> is returned if the node is not an element node or if the node has no children. </p>
<h3>mxmlGetInteger</h3>
<p>Get the integer value from the specified node or its first child. </p>
<pre>int mxmlGetInteger (
 mxml_node_t *node
);</pre>
<p>0 is returned if the node (or its first child) is not an integer value node. </p>
<h3>mxmlGetLastChild</h3>
<p>Get the last child of an element node. </p>
<pre>mxml_node_t * mxmlGetLastChild (
 mxml_node_t *node
);</pre>
<p><code>NULL</code> is returned if the node is not an element node or if the node has no children. </p>
<h3>mxmlGetNextSibling</h3>
<p>Return the node type&#8230; </p>
<pre>mxml_node_t * mxmlGetNextSibling (
 mxml_node_t *node
);</pre>
<h3>mxmlGetOpaque</h3>
<p>Get an opaque string value for a node or its first child. </p>
<pre>const char * mxmlGetOpaque (
 mxml_node_t *node
);</pre>
<p><code>NULL</code> is returned if the node (or its first child) is not an opaque value node. </p>
<h3>mxmlGetParent</h3>
<p>Get the parent node. </p>
<pre>mxml_node_t * mxmlGetParent (
 mxml_node_t *node
);</pre>
<p><code>NULL</code> is returned for a root node. </p>
<h3>mxmlGetPrevSibling</h3>
<p>Get the previous node for the current parent. </p>
<pre>mxml_node_t * mxmlGetPrevSibling (
 mxml_node_t *node
);</pre>
<p><code>NULL</code> is returned if this is the first child for the current parent. </p>
<h3>mxmlGetReal</h3>
<p>Get the real value for a node or its first child. </p>
<pre>double mxmlGetReal (
 mxml_node_t *node
);</pre>
<p>0.0 is returned if the node (or its first child) is not a real value node. </p>
<h3>mxmlGetRefCount</h3>
<p>Get the current reference (use) count for a node. </p>
<pre>int mxmlGetRefCount (
 mxml_node_t *node
);</pre>
<p>The initial reference count of new nodes is 1. Use the <i>mxmlRetain</i> and <i>mxmlRelease</i> functions to increment and decrement a node&#8217;s reference count. </p>
<p> .</p>
<h3>mxmlGetText</h3>
<p>Get the text value for a node or its first child. </p>
<pre>const char * mxmlGetText (
 mxml_node_t *node,
 int *whitespace
);</pre>
<p><code>NULL</code> is returned if the node (or its first child) is not a text node. The &quot;whitespace&quot; argument can be NULL. </p>
<h3>mxmlGetType</h3>
<p>Get the node type. </p>
<pre>mxml_type_t mxmlGetType (
 mxml_node_t *node
);</pre>
<p><code>MXML_IGNORE</code> is returned if &quot;node&quot; is <code>NULL</code>. </p>
<h3>mxmlGetUserData</h3>
<p>Get the user data pointer for a node. </p>
<pre>void * mxmlGetUserData (
 mxml_node_t *node
);</pre>
<h3>mxmlIndexDelete</h3>
<p>Delete an index. </p>
<pre>void mxmlIndexDelete (
 mxml_index_t *ind
);</pre>
<h3>mxmlIndexEnum</h3>
<p>Return the next node in the index. </p>
<pre>mxml_node_t * mxmlIndexEnum (
 mxml_index_t *ind
);</pre>
<p>Nodes are returned in the sorted order of the index.</p>
<h3>mxmlIndexFind</h3>
<p>Find the next matching node. </p>
<pre>mxml_node_t * mxmlIndexFind (
 mxml_index_t *ind,
 const char *element,
 const char *value
);</pre>
<p>You should call mxmlIndexReset() prior to using this function for the first time with a particular set of &quot;element&quot; and &quot;value&quot; strings. Passing NULL for both &quot;element&quot; and &quot;value&quot; is equivalent to calling mxmlIndexEnum().</p>
<h3>mxmlIndexGetCount</h3>
<p>Get the number of nodes in an index. </p>
<pre>int mxmlIndexGetCount (
 mxml_index_t *ind
);</pre>
<h3>mxmlIndexNew</h3>
<p>Create a new index. </p>
<pre>mxml_index_t * mxmlIndexNew (
 mxml_node_t *node,
 const char *element,
 const char *attr
);</pre>
<p>The index will contain all nodes that contain the named element and/or attribute. If both &quot;element&quot; and &quot;attr&quot; are NULL, then the index will contain a sorted list of the elements in the node tree. Nodes are sorted by element name and optionally by attribute value if the &quot;attr&quot; argument is not NULL.</p>
<h3>mxmlIndexReset</h3>
<p>Reset the enumeration/find pointer in the index and return the first node in the index. </p>
<pre>mxml_node_t * mxmlIndexReset (
 mxml_index_t *ind
);</pre>
<p>This function should be called prior to using mxmlIndexEnum() or mxmlIndexFind() for the first time.</p>
<h3>mxmlLoadFd</h3>
<p>Load a file descriptor into an XML node tree. </p>
<pre>mxml_node_t * mxmlLoadFd (
 mxml_node_t *top,
 int fd,
 mxml_load_cb_t cb
);</pre>
<p>The nodes in the specified file are added to the specified top node. If no top node is provided, the XML file MUST be well-formed with a single parent node like &lt;?xml&gt; for the entire file. The callback function returns the value type that should be used for child nodes. If MXML_NO_CALLBACK is specified then all child nodes will be either MXML_ELEMENT or MXML_TEXT nodes. </p>
<p> The constants MXML_INTEGER_CALLBACK, MXML_OPAQUE_CALLBACK, MXML_REAL_CALLBACK, and MXML_TEXT_CALLBACK are defined for loading child nodes of the specified type.</p>
<h3>mxmlLoadFile</h3>
<p>Load a file into an XML node tree. </p>
<pre>mxml_node_t * mxmlLoadFile (
 mxml_node_t *top,
 FILE *fp,
 mxml_load_cb_t cb
);</pre>
<p>The nodes in the specified file are added to the specified top node. If no top node is provided, the XML file MUST be well-formed with a single parent node like &lt;?xml&gt; for the entire file. The callback function returns the value type that should be used for child nodes. If MXML_NO_CALLBACK is specified then all child nodes will be either MXML_ELEMENT or MXML_TEXT nodes. </p>
<p> The constants MXML_INTEGER_CALLBACK, MXML_OPAQUE_CALLBACK, MXML_REAL_CALLBACK, and MXML_TEXT_CALLBACK are defined for loading child nodes of the specified type.</p>
<h3>mxmlLoadString</h3>
<p>Load a string into an XML node tree. </p>
<pre>mxml_node_t * mxmlLoadString (
 mxml_node_t *top,
 const char *s,
 mxml_load_cb_t cb
);</pre>
<p>The nodes in the specified string are added to the specified top node. If no top node is provided, the XML string MUST be well-formed with a single parent node like &lt;?xml&gt; for the entire string. The callback function returns the value type that should be used for child nodes. If MXML_NO_CALLBACK is specified then all child nodes will be either MXML_ELEMENT or MXML_TEXT nodes. </p>
<p> The constants MXML_INTEGER_CALLBACK, MXML_OPAQUE_CALLBACK, MXML_REAL_CALLBACK, and MXML_TEXT_CALLBACK are defined for loading child nodes of the specified type.</p>
<h3>mxmlNewCDATA</h3>
<p>Create a new CDATA node. </p>
<pre>mxml_node_t * mxmlNewCDATA (
 mxml_node_t *parent,
 const char *data
);</pre>
<p>The new CDATA node is added to the end of the specified parent&#8217;s child list. The constant MXML_NO_PARENT can be used to specify that the new CDATA node has no parent. The data string must be nul-terminated and is copied into the new node. CDATA nodes use the MXML_ELEMENT type. </p>
<h3>mxmlNewCustom</h3>
<p>Create a new custom data node. </p>
<pre>mxml_node_t * mxmlNewCustom (
 mxml_node_t *parent,
 void *data,
 mxml_custom_destroy_cb_t destroy
);</pre>
<p>The new custom node is added to the end of the specified parent&#8217;s child list. The constant MXML_NO_PARENT can be used to specify that the new element node has no parent. NULL can be passed when the data in the node is not dynamically allocated or is separately managed. </p>
<h3>mxmlNewElement</h3>
<p>Create a new element node. </p>
<pre>mxml_node_t * mxmlNewElement (
 mxml_node_t *parent,
 const char *name
);</pre>
<p>The new element node is added to the end of the specified parent&#8217;s child list. The constant MXML_NO_PARENT can be used to specify that the new element node has no parent.</p>
<h3>mxmlNewInteger</h3>
<p>Create a new integer node. </p>
<pre>mxml_node_t * mxmlNewInteger (
 mxml_node_t *parent,
 int integer
);</pre>
<p>The new integer node is added to the end of the specified parent&#8217;s child list. The constant MXML_NO_PARENT can be used to specify that the new integer node has no parent.</p>
<h3>mxmlNewOpaque</h3>
<p>Create a new opaque string. </p>
<pre>mxml_node_t * mxmlNewOpaque (
 mxml_node_t *parent,
 const char *opaque
);</pre>
<p>The new opaque node is added to the end of the specified parent&#8217;s child list. The constant MXML_NO_PARENT can be used to specify that the new opaque node has no parent. The opaque string must be nul-terminated and is copied into the new node.</p>
<h3>mxmlNewReal</h3>
<p>Create a new real number node. </p>
<pre>mxml_node_t * mxmlNewReal (
 mxml_node_t *parent,
 double real
);</pre>
<p>The new real number node is added to the end of the specified parent&#8217;s child list. The constant MXML_NO_PARENT can be used to specify that the new real number node has no parent.</p>
<h3>mxmlNewText</h3>
<p>Create a new text fragment node. </p>
<pre>mxml_node_t * mxmlNewText (
 mxml_node_t *parent,
 int whitespace,
 const char *string
);</pre>
<p>The new text node is added to the end of the specified parent&#8217;s child list. The constant MXML_NO_PARENT can be used to specify that the new text node has no parent. The whitespace parameter is used to specify whether leading whitespace is present before the node. The text string must be nul-terminated and is copied into the new node.</p>
<h3>mxmlNewTextf</h3>
<p>Create a new formatted text fragment node. </p>
<pre>mxml_node_t * mxmlNewTextf (
 mxml_node_t *parent,
 int whitespace,
 const char *format,
 ...
);</pre>
<p>The new text node is added to the end of the specified parent&#8217;s child list. The constant MXML_NO_PARENT can be used to specify that the new text node has no parent. The whitespace parameter is used to specify whether leading whitespace is present before the node. The format string must be nul-terminated and is formatted into the new node.</p>
<h3>mxmlNewXML</h3>
<p>Create a new XML document tree. </p>
<pre>mxml_node_t * mxmlNewXML (
 const char *version
);</pre>
<p>The &quot;version&quot; argument specifies the version number to put in the ?xml element node. If NULL, version 1.0 is assumed. </p>
<h3>mxmlRelease</h3>
<p>Release a node. </p>
<pre>int mxmlRelease (
 mxml_node_t *node
);</pre>
<p>When the reference count reaches zero, the node (and any children) is deleted via mxmlDelete(). </p>
<h3>mxmlRemove</h3>
<p>Remove a node from its parent. </p>
<pre>void mxmlRemove (
 mxml_node_t *node
);</pre>
<p>Does not free memory used by the node &#8211; use mxmlDelete() for that. This function does nothing if the node has no parent.</p>
<h3>mxmlRetain</h3>
<p>Retain a node. </p>
<pre>int mxmlRetain (
 mxml_node_t *node
);</pre>
<h3>mxmlSAXLoadFd</h3>
<p>Load a file descriptor into an XML node tree using a SAX callback. </p>
<pre>mxml_node_t * mxmlSAXLoadFd (
 mxml_node_t *top,
 int fd,
 mxml_load_cb_t cb,
 mxml_sax_cb_t sax_cb,
 void *sax_data
);</pre>
<p>The nodes in the specified file are added to the specified top node. If no top node is provided, the XML file MUST be well-formed with a single parent node like &lt;?xml&gt; for the entire file. The callback function returns the value type that should be used for child nodes. If MXML_NO_CALLBACK is specified then all child nodes will be either MXML_ELEMENT or MXML_TEXT nodes. </p>
<p> The constants MXML_INTEGER_CALLBACK, MXML_OPAQUE_CALLBACK, MXML_REAL_CALLBACK, and MXML_TEXT_CALLBACK are defined for loading child nodes of the specified type. </p>
<p> The SAX callback must call mxmlRetain() for any nodes that need to be kept for later use. Otherwise, nodes are deleted when the parent node is closed or after each data, comment, CDATA, or directive node. </p>
<h3>mxmlSAXLoadFile</h3>
<p>Load a file into an XML node tree using a SAX callback. </p>
<pre>mxml_node_t * mxmlSAXLoadFile (
 mxml_node_t *top,
 FILE *fp,
 mxml_load_cb_t cb,
 mxml_sax_cb_t sax_cb,
 void *sax_data
);</pre>
<p>The nodes in the specified file are added to the specified top node. If no top node is provided, the XML file MUST be well-formed with a single parent node like &lt;?xml&gt; for the entire file. The callback function returns the value type that should be used for child nodes. If MXML_NO_CALLBACK is specified then all child nodes will be either MXML_ELEMENT or MXML_TEXT nodes. </p>
<p> The constants MXML_INTEGER_CALLBACK, MXML_OPAQUE_CALLBACK, MXML_REAL_CALLBACK, and MXML_TEXT_CALLBACK are defined for loading child nodes of the specified type. </p>
<p> The SAX callback must call mxmlRetain() for any nodes that need to be kept for later use. Otherwise, nodes are deleted when the parent node is closed or after each data, comment, CDATA, or directive node. </p>
<h3>mxmlSAXLoadString</h3>
<p>Load a string into an XML node tree using a SAX callback. </p>
<pre>mxml_node_t * mxmlSAXLoadString (
 mxml_node_t *top,
 const char *s,
 mxml_load_cb_t cb,
 mxml_sax_cb_t sax_cb,
 void *sax_data
);</pre>
<p>The nodes in the specified string are added to the specified top node. If no top node is provided, the XML string MUST be well-formed with a single parent node like &lt;?xml&gt; for the entire string. The callback function returns the value type that should be used for child nodes. If MXML_NO_CALLBACK is specified then all child nodes will be either MXML_ELEMENT or MXML_TEXT nodes. </p>
<p> The constants MXML_INTEGER_CALLBACK, MXML_OPAQUE_CALLBACK, MXML_REAL_CALLBACK, and MXML_TEXT_CALLBACK are defined for loading child nodes of the specified type. </p>
<p> The SAX callback must call mxmlRetain() for any nodes that need to be kept for later use. Otherwise, nodes are deleted when the parent node is closed or after each data, comment, CDATA, or directive node. </p>
<h3>mxmlSaveAllocString</h3>
<p>Save an XML tree to an allocated string. </p>
<pre>char * mxmlSaveAllocString (
 mxml_node_t *node,
 mxml_save_cb_t cb
);</pre>
<p>This function returns a pointer to a string containing the textual representation of the XML node tree. The string should be freed using the free() function when you are done with it. NULL is returned if the node would produce an empty string or if the string cannot be allocated. </p>
<p> The callback argument specifies a function that returns a whitespace string or NULL before and after each element. If MXML_NO_CALLBACK is specified, whitespace will only be added before MXML_TEXT nodes with leading whitespace and before attribute names inside opening element tags.</p>
<h3>mxmlSaveFd</h3>
<p>Save an XML tree to a file descriptor. </p>
<pre>int mxmlSaveFd (
 mxml_node_t *node,
 int fd,
 mxml_save_cb_t cb
);</pre>
<p>The callback argument specifies a function that returns a whitespace string or NULL before and after each element. If MXML_NO_CALLBACK is specified, whitespace will only be added before MXML_TEXT nodes with leading whitespace and before attribute names inside opening element tags.</p>
<h3>mxmlSaveFile</h3>
<p>Save an XML tree to a file. </p>
<pre>int mxmlSaveFile (
 mxml_node_t *node,
 FILE *fp,
 mxml_save_cb_t cb
);</pre>
<p>The callback argument specifies a function that returns a whitespace string or NULL before and after each element. If MXML_NO_CALLBACK is specified, whitespace will only be added before MXML_TEXT nodes with leading whitespace and before attribute names inside opening element tags.</p>
<h3>mxmlSaveString</h3>
<p>Save an XML node tree to a string. </p>
<pre>int mxmlSaveString (
 mxml_node_t *node,
 char *buffer,
 int bufsize,
 mxml_save_cb_t cb
);</pre>
<p>This function returns the total number of bytes that would be required for the string but only copies (bufsize &#8211; 1) characters into the specified buffer. </p>
<p> The callback argument specifies a function that returns a whitespace string or NULL before and after each element. If MXML_NO_CALLBACK is specified, whitespace will only be added before MXML_TEXT nodes with leading whitespace and before attribute names inside opening element tags.</p>
<h3>mxmlSetCDATA</h3>
<p>Set the element name of a CDATA node. </p>
<pre>int mxmlSetCDATA (
 mxml_node_t *node,
 const char *data
);</pre>
<p>The node is not changed if it (or its first child) is not a CDATA element node. </p>
<h3>mxmlSetCustom</h3>
<p>Set the data and destructor of a custom data node. </p>
<pre>int mxmlSetCustom (
 mxml_node_t *node,
 void *data,
 mxml_custom_destroy_cb_t destroy
);</pre>
<p>The node is not changed if it (or its first child) is not a custom node. </p>
<h3>mxmlSetCustomHandlers</h3>
<p>Set the handling functions for custom data. </p>
<pre>void mxmlSetCustomHandlers (
 mxml_custom_load_cb_t load,
 mxml_custom_save_cb_t save
);</pre>
<p>The load function accepts a node pointer and a data string and must return 0 on success and non-zero on error. </p>
<p> The save function accepts a node pointer and must return a malloc&#8217;d string on success and NULL on error.</p>
<h3>mxmlSetElement</h3>
<p>Set the name of an element node. </p>
<pre>int mxmlSetElement (
 mxml_node_t *node,
 const char *name
);</pre>
<p>The node is not changed if it is not an element node.</p>
<h3>mxmlSetErrorCallback</h3>
<p>Set the error message callback. </p>
<pre>void mxmlSetErrorCallback (
 mxml_error_cb_t cb
);</pre>
<h3>mxmlSetInteger</h3>
<p>Set the value of an integer node. </p>
<pre>int mxmlSetInteger (
 mxml_node_t *node,
 int integer
);</pre>
<p>The node is not changed if it (or its first child) is not an integer node.</p>
<h3>mxmlSetOpaque</h3>
<p>Set the value of an opaque node. </p>
<pre>int mxmlSetOpaque (
 mxml_node_t *node,
 const char *opaque
);</pre>
<p>The node is not changed if it (or its first child) is not an opaque node.</p>
<h3>mxmlSetReal</h3>
<p>Set the value of a real number node. </p>
<pre>int mxmlSetReal (
 mxml_node_t *node,
 double real
);</pre>
<p>The node is not changed if it (or its first child) is not a real number node.</p>
<h3>mxmlSetText</h3>
<p>Set the value of a text node. </p>
<pre>int mxmlSetText (
 mxml_node_t *node,
 int whitespace,
 const char *string
);</pre>
<p>The node is not changed if it (or its first child) is not a text node.</p>
<h3>mxmlSetTextf</h3>
<p>Set the value of a text node to a formatted string. </p>
<pre>int mxmlSetTextf (
 mxml_node_t *node,
 int whitespace,
 const char *format,
 ...
);</pre>
<p>The node is not changed if it (or its first child) is not a text node.</p>
<h3>mxmlSetUserData</h3>
<p>Set the user data pointer for a node. </p>
<pre>int mxmlSetUserData (
 mxml_node_t *node,
 void *data
);</pre>
<h3>mxmlSetWrapMargin</h3>
<p>Set the wrap margin when saving XML data. </p>
<pre>void mxmlSetWrapMargin (
 int column
);</pre>
<p>Wrapping is disabled when &quot;column&quot; is 0. </p>
<h3>mxmlWalkNext</h3>
<p>Walk to the next logical node in the tree. </p>
<pre>mxml_node_t * mxmlWalkNext (
 mxml_node_t *node,
 mxml_node_t *top,
 int descend
);</pre>
<p>The descend argument controls whether the first child is considered to be the next node. The top node argument constrains the walk to the node&#8217;s children.</p>
<h3>mxmlWalkPrev</h3>
<p>Walk to the previous logical node in the tree. </p>
<pre>mxml_node_t * mxmlWalkPrev (
 mxml_node_t *node,
 mxml_node_t *top,
 int descend
);</pre>
<p>The descend argument controls whether the previous node&#8217;s last child is considered to be the previous node. The top node argument constrains the walk to the node&#8217;s children.</p>
<h2>Types</h2>
<h3>mxml_custom_destroy_cb_t</h3>
<p>Custom data destructor </p>
<pre>typedef void(*)(void *) mxml_custom_destroy_cb_t;</pre>
<h3>mxml_custom_load_cb_t</h3>
<p>Custom data load callback function </p>
<pre>typedef int(*)(mxml_node_t *, const char *) mxml_custom_load_cb_t;</pre>
<h3>mxml_custom_save_cb_t</h3>
<p>Custom data save callback function </p>
<pre>typedef char *(*)(mxml_node_t *) mxml_custom_save_cb_t;</pre>
<h3>mxml_entity_cb_t</h3>
<p>Entity callback function </p>
<pre>typedef int(*)(const char *) mxml_entity_cb_t;</pre>
<h3>mxml_error_cb_t</h3>
<p>Error callback function </p>
<pre>typedef void(*)(const char *) mxml_error_cb_t;</pre>
<h3>mxml_index_t</h3>
<p>An XML node index. </p>
<pre>typedef struct mxml_index_s mxml_index_t;</pre>
<h3>mxml_load_cb_t</h3>
<p>Load callback function </p>
<pre>typedef mxml_type_t(*)(mxml_node_t *) mxml_load_cb_t;</pre>
<h3>mxml_node_t</h3>
<p>An XML node. </p>
<pre>typedef struct mxml_node_s mxml_node_t;</pre>
<h3>mxml_save_cb_t</h3>
<p>Save callback function </p>
<pre>typedef const char *(*)(mxml_node_t *, int) mxml_save_cb_t;</pre>
<h3>mxml_sax_cb_t</h3>
<p>SAX callback function </p>
<pre>typedef void(*)(mxml_node_t *, mxml_sax_event_t, void *) mxml_sax_cb_t;</pre>
<h3>mxml_sax_event_t</h3>
<p>SAX event type. </p>
<pre>typedef enum mxml_sax_event_e mxml_sax_event_t;</pre>
<h3>mxml_type_t</h3>
<p>The XML node type. </p>
<pre>typedef enum mxml_type_e mxml_type_t;</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-mxmldoc/">mxmldoc</a>(1), Mini-XML Programmers Manual, <a rel="nofollow" href="http://www.minixml.org/">http://www.minixml.org/</a></p>
<h2>Copyright</h2>
<p>Copyright 2003-2011 by Michael Sweet.</p>
