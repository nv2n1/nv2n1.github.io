---
title: "cmark(3)"
name: "cmark"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmark/"
description: "cmark – CommonMark parsing, manipulating, and rendering"
---

<h2>NAME</h2>
<p> cmark &#8211; CommonMark parsing, manipulating, and rendering </p>
<h2>DESCRIPTION</h2>
<h3>Simple Interface</h3>
<p> <i>char *</i> <code>cmark_markdown_to_html</code>(<i>const char *text</i>, <i>size_t len</i>, <i>int options</i>) </p>
<p> Convert text (assumed to be a UTF-8 encoded string with length len from CommonMark Markdown to HTML, returning a null-terminated, UTF-8-encoded string. </p>
<h3>Node Structure</h3>
<h3>Creating and Destroying Nodes</h3>
<p> <i>cmark_node *</i> <code>cmark_node_new</code>(<i>cmark_node_type type</i>) </p>
<p> Creates a new node of type type. Note that the node may have other required properties, which it is the caller&#8217;s responsibility to assign. </p>
<p> <i>void</i> <code>cmark_node_free</code>(<i>cmark_node *node</i>) </p>
<p> Frees the memory allocated for a node. </p>
<h3>Tree Traversal</h3>
<p> <i>cmark_node *</i> <code>cmark_node_next</code>(<i>cmark_node *node</i>) </p>
<p> Returns the next node in the sequence after node, or NULL if there is none. </p>
<p> <i>cmark_node *</i> <code>cmark_node_previous</code>(<i>cmark_node *node</i>) </p>
<p> Returns the previous node in the sequence after node, or NULL if there is none. </p>
<p> <i>cmark_node *</i> <code>cmark_node_parent</code>(<i>cmark_node *node</i>) </p>
<p> Returns the parent of node, or NULL if there is none. </p>
<p> <i>cmark_node *</i> <code>cmark_node_first_child</code>(<i>cmark_node *node</i>) </p>
<p> Returns the first child of node, or NULL if node has no children. </p>
<p> <i>cmark_node *</i> <code>cmark_node_last_child</code>(<i>cmark_node *node</i>) </p>
<p> Returns the last child of node, or NULL if node has no children. </p>
<h3>Iterator</h3>
<p> An iterator will walk through a tree of nodes, starting from a root node, returning one node at a time, together with information about whether the node is being entered or exited. The iterator will first descend to a child node, if there is one. When there is no child, the iterator will go to the next sibling. When there is no next sibling, the iterator will return to the parent (but with a cmark_event_type of CMARK_EVENT_EXIT). The iterator will return CMARK_EVENT_DONE when it reaches the root node again. One natural application is an HTML renderer, where an ENTER event outputs an open tag and an EXIT event outputs a close tag. An iterator might also be used to transform an AST in some systematic way, for example, turning all level-3 headings into regular paragraphs.</p>
<dl>
<dt>
<dd>
<pre><code>
void usage_example(cmark_node *root)
{
    cmark_event_type ev_type;
    cmark_iter *iter = cmark_iter_new(root);
    while ((ev_type = cmark_iter_next(iter)) != CMARK_EVENT_DONE) {
        cmark_node *cur = cmark_iter_get_node(iter);
        // Do something with `cur` and `ev_type`
    }
    cmark_iter_free(iter);
}
</code></pre>
</dl>
<p> Iterators will never return EXIT events for leaf nodes, which are nodes of type:</p>
<dl>
<dt>&bull;</p>
<dd> CMARK_NODE_HTML_BLOCK</p>
<dt>&bull;</p>
<dd> CMARK_NODE_THEMATIC_BREAK</p>
<dt>&bull;</p>
<dd> CMARK_NODE_CODE_BLOCK</p>
<dt>&bull;</p>
<dd> CMARK_NODE_TEXT</p>
<dt>&bull;</p>
<dd> CMARK_NODE_SOFTBREAK</p>
<dt>&bull;</p>
<dd> CMARK_NODE_LINEBREAK</p>
<dt>&bull;</p>
<dd> CMARK_NODE_CODE</p>
<dt>&bull;</p>
<dd> CMARK_NODE_HTML_INLINE</dl>
<p> Nodes must only be modified after an EXIT event, or an ENTER event for leaf nodes. </p>
<p> <i>cmark_iter *</i> <code>cmark_iter_new</code>(<i>cmark_node *root</i>) </p>
<p> Creates a new iterator starting at root. The current node and event type are undefined until cmark_iter_next is called for the first time. </p>
<p> <i>void</i> <code>cmark_iter_free</code>(<i>cmark_iter *iter</i>) </p>
<p> Frees the memory allocated for an iterator. </p>
<p> <i>cmark_event_type</i> <code>cmark_iter_next</code>(<i>cmark_iter *iter</i>) </p>
<p> Advances to the next node and returns the event type (CMARK_EVENT_ENTER, CMARK_EVENT_EXIT or CMARK_EVENT_DONE). </p>
<p> <i>cmark_node *</i> <code>cmark_iter_get_node</code>(<i>cmark_iter *iter</i>) </p>
<p> Returns the current node. </p>
<p> <i>cmark_event_type</i> <code>cmark_iter_get_event_type</code>(<i>cmark_iter *iter</i>) </p>
<p> Returns the current event type. </p>
<p> <i>cmark_node *</i> <code>cmark_iter_get_root</code>(<i>cmark_iter *iter</i>) </p>
<p> Returns the root node. </p>
<p> <i>void</i> <code>cmark_iter_reset</code>(<i>cmark_iter *iter</i>, <i>cmark_node *current</i>, <i>cmark_event_type event_type</i>) </p>
<p> Resets the iterator so that the current node is current and the event type is event_type. The new current node must be a descendant of the root node or the root node itself. </p>
<h3>Accessors</h3>
<p> <i>void *</i> <code>cmark_node_get_user_data</code>(<i>cmark_node *node</i>) </p>
<p> Returns the user data of node. </p>
<p> <i>int</i> <code>cmark_node_set_user_data</code>(<i>cmark_node *node</i>, <i>void *user_data</i>) </p>
<p> Sets arbitrary user data for node. Returns 1 on success, 0 on failure. </p>
<p> <i>cmark_node_type</i> <code>cmark_node_get_type</code>(<i>cmark_node *node</i>) </p>
<p> Returns the type of node, or CMARK_NODE_NONE on error. </p>
<p> <i>const char *</i> <code>cmark_node_get_type_string</code>(<i>cmark_node *node</i>) </p>
<p> Like cmark_node_get_type, but returns a string representation of the type, or &quot;&lt;unknown&gt;&quot;. </p>
<p> <i>const char *</i> <code>cmark_node_get_literal</code>(<i>cmark_node *node</i>) </p>
<p> Returns the string contents of node, or an empty string if none is set. </p>
<p> <i>int</i> <code>cmark_node_set_literal</code>(<i>cmark_node *node</i>, <i>const char *content</i>) </p>
<p> Sets the string contents of node. Returns 1 on success, 0 on failure. </p>
<p> <i>int</i> <code>cmark_node_get_heading_level</code>(<i>cmark_node *node</i>) </p>
<p> Returns the heading level of node, or 0 if node is not a heading. </p>
<p> <i>int</i> <code>cmark_node_set_heading_level</code>(<i>cmark_node *node</i>, <i>int level</i>) </p>
<p> Sets the heading level of node, returning 1 on success and 0 on error. </p>
<p> <i>cmark_list_type</i> <code>cmark_node_get_list_type</code>(<i>cmark_node *node</i>) </p>
<p> Returns the list type of node, or CMARK_NO_LIST if node is not a list. </p>
<p> <i>int</i> <code>cmark_node_set_list_type</code>(<i>cmark_node *node</i>, <i>cmark_list_type type</i>) </p>
<p> Sets the list type of node, returning 1 on success and 0 on error. </p>
<p> <i>cmark_delim_type</i> <code>cmark_node_get_list_delim</code>(<i>cmark_node *node</i>) </p>
<p> Returns the list delimiter type of node, or CMARK_NO_DELIM if node is not a list. </p>
<p> <i>int</i> <code>cmark_node_set_list_delim</code>(<i>cmark_node *node</i>, <i>cmark_delim_type delim</i>) </p>
<p> Sets the list delimiter type of node, returning 1 on success and 0 on error. </p>
<p> <i>int</i> <code>cmark_node_get_list_start</code>(<i>cmark_node *node</i>) </p>
<p> Returns starting number of node, if it is an ordered list, otherwise 0. </p>
<p> <i>int</i> <code>cmark_node_set_list_start</code>(<i>cmark_node *node</i>, <i>int start</i>) </p>
<p> Sets starting number of node, if it is an ordered list. Returns 1 on success, 0 on failure. </p>
<p> <i>int</i> <code>cmark_node_get_list_tight</code>(<i>cmark_node *node</i>) </p>
<p> Returns 1 if node is a tight list, 0 otherwise. </p>
<p> <i>int</i> <code>cmark_node_set_list_tight</code>(<i>cmark_node *node</i>, <i>int tight</i>) </p>
<p> Sets the &quot;tightness&quot; of a list. Returns 1 on success, 0 on failure. </p>
<p> <i>const char *</i> <code>cmark_node_get_fence_info</code>(<i>cmark_node *node</i>) </p>
<p> Returns the info string from a fenced code block. </p>
<p> <i>int</i> <code>cmark_node_set_fence_info</code>(<i>cmark_node *node</i>, <i>const char *info</i>) </p>
<p> Sets the info string in a fenced code block, returning 1 on success and 0 on failure. </p>
<p> <i>const char *</i> <code>cmark_node_get_url</code>(<i>cmark_node *node</i>) </p>
<p> Returns the URL of a link or image node, or an empty string if no URL is set. </p>
<p> <i>int</i> <code>cmark_node_set_url</code>(<i>cmark_node *node</i>, <i>const char *url</i>) </p>
<p> Sets the URL of a link or image node. Returns 1 on success, 0 on failure. </p>
<p> <i>const char *</i> <code>cmark_node_get_title</code>(<i>cmark_node *node</i>) </p>
<p> Returns the title of a link or image node, or an empty string if no title is set. </p>
<p> <i>int</i> <code>cmark_node_set_title</code>(<i>cmark_node *node</i>, <i>const char *title</i>) </p>
<p> Sets the title of a link or image node. Returns 1 on success, 0 on failure. </p>
<p> <i>const char *</i> <code>cmark_node_get_on_enter</code>(<i>cmark_node *node</i>) </p>
<p> Returns the literal &quot;on enter&quot; text for a custom node, or an empty string if no on_enter is set. </p>
<p> <i>int</i> <code>cmark_node_set_on_enter</code>(<i>cmark_node *node</i>, <i>const char *on_enter</i>) </p>
<p> Sets the literal text to render &quot;on enter&quot; for a custom node. Any children of the node will be rendered after this text. Returns 1 on success 0 on failure. </p>
<p> <i>const char *</i> <code>cmark_node_get_on_exit</code>(<i>cmark_node *node</i>) </p>
<p> Returns the literal &quot;on exit&quot; text for a custom node, or an empty string if no on_exit is set. </p>
<p> <i>int</i> <code>cmark_node_set_on_exit</code>(<i>cmark_node *node</i>, <i>const char *on_exit</i>) </p>
<p> Sets the literal text to render &quot;on exit&quot; for a custom node. Any children of the node will be rendered before this text. Returns 1 on success 0 on failure. </p>
<p> <i>int</i> <code>cmark_node_get_start_line</code>(<i>cmark_node *node</i>) </p>
<p> Returns the line on which node begins. </p>
<p> <i>int</i> <code>cmark_node_get_start_column</code>(<i>cmark_node *node</i>) </p>
<p> Returns the column at which node begins. </p>
<p> <i>int</i> <code>cmark_node_get_end_line</code>(<i>cmark_node *node</i>) </p>
<p> Returns the line on which node ends. </p>
<p> <i>int</i> <code>cmark_node_get_end_column</code>(<i>cmark_node *node</i>) </p>
<p> Returns the column at which node ends. </p>
<h3>Tree Manipulation</h3>
<p> <i>void</i> <code>cmark_node_unlink</code>(<i>cmark_node *node</i>) </p>
<p> Unlinks a node, removing it from the tree, but not freeing its memory. (Use cmark_node_free for that.) </p>
<p> <i>int</i> <code>cmark_node_insert_before</code>(<i>cmark_node *node</i>, <i>cmark_node *sibling</i>) </p>
<p> Inserts sibling before node. Returns 1 on success, 0 on failure. </p>
<p> <i>int</i> <code>cmark_node_insert_after</code>(<i>cmark_node *node</i>, <i>cmark_node *sibling</i>) </p>
<p> Inserts sibling after node. Returns 1 on success, 0 on failure. </p>
<p> <i>int</i> <code>cmark_node_prepend_child</code>(<i>cmark_node *node</i>, <i>cmark_node *child</i>) </p>
<p> Adds child to the beginning of the children of node. Returns 1 on success, 0 on failure. </p>
<p> <i>int</i> <code>cmark_node_append_child</code>(<i>cmark_node *node</i>, <i>cmark_node *child</i>) </p>
<p> Adds child to the end of the children of node. Returns 1 on success, 0 on failure. </p>
<p> <i>void</i> <code>cmark_consolidate_text_nodes</code>(<i>cmark_node *root</i>) </p>
<p> Consolidates adjacent text nodes. </p>
<h3>Parsing</h3>
<p> Simple interface:</p>
<dl>
<dt>
<dd>
<pre>
cmark_node *document = cmark_parse_document(&quot;Hello *world*&quot;, 13,
                                            CMARK_OPT_DEFAULT);
</pre>
</dl>
<p> Streaming interface:</p>
<dl>
<dt>
<dd>
cmark_parser *parser = cmark_parser_new(CMARK_OPT_DEFAULT);<br />
FILE *fp = fopen(&#8220;myfile.md&#8221;, &#8220;r&#8221;);<br />
while ((bytes = fread(buffer, 1, sizeof(buffer), fp)) &gt; 0) {<br />
    cmark_parser_feed(parser, buffer, bytes);<br />
    if (bytes &lt; sizeof(buffer)) {<br />
        break;<br />
    }<br />
}<br />
document = cmark_parser_finish(parser);<br />
cmark_parser_free(parser);</p>
</dl>
<p> <i>cmark_parser *</i> <code>cmark_parser_new</code>(<i>int options</i>) </p>
<p> Creates a new parser object. </p>
<p> <i>void</i> <code>cmark_parser_free</code>(<i>cmark_parser *parser</i>) </p>
<p> Frees memory allocated for a parser object. </p>
<p> <i>void</i> <code>cmark_parser_feed</code>(<i>cmark_parser *parser</i>, <i>const char *buffer</i>, <i>size_t len</i>) </p>
<p> Feeds a string of length len to parser. </p>
<p> <i>cmark_node *</i> <code>cmark_parser_finish</code>(<i>cmark_parser *parser</i>) </p>
<p> Finish parsing and return a pointer to a tree of nodes. </p>
<p> <i>cmark_node *</i> <code>cmark_parse_document</code>(<i>const char *buffer</i>, <i>size_t len</i>, <i>int options</i>) </p>
<p> Parse a CommonMark document in buffer of length len. Returns a pointer to a tree of nodes. </p>
<p> <i>cmark_node *</i> <code>cmark_parse_file</code>(<i>FILE *f</i>, <i>int options</i>) </p>
<p> Parse a CommonMark document in file f, returning a pointer to a tree of nodes. </p>
<h3>Rendering</h3>
<p> <i>char *</i> <code>cmark_render_xml</code>(<i>cmark_node *root</i>, <i>int options</i>) </p>
<p> Render a node tree as XML. </p>
<p> <i>char *</i> <code>cmark_render_html</code>(<i>cmark_node *root</i>, <i>int options</i>) </p>
<p> Render a node tree as an HTML fragment. It is up to the user to add an appropriate header and footer. </p>
<p> <i>char *</i> <code>cmark_render_man</code>(<i>cmark_node *root</i>, <i>int options</i>, <i>int width</i>) </p>
<p> Render a node tree as a groff man page, without the header. </p>
<p> <i>char *</i> <code>cmark_render_commonmark</code>(<i>cmark_node *root</i>, <i>int options</i>, <i>int width</i>) </p>
<p> Render a node tree as a commonmark document. </p>
<p> <i>char *</i> <code>cmark_render_latex</code>(<i>cmark_node *root</i>, <i>int options</i>, <i>int width</i>) </p>
<p> Render a node tree as a LaTeX document. </p>
<h3>Options</h3>
<p>#define CMARK_OPT_DEFAULT 0</p>
<p> Default options. </p>
<h3>Options affecting rendering</h3>
<p>#define CMARK_OPT_SOURCEPOS (1 &lt;&lt; 1)</p>
<p> Include a data-sourcepos attribute on all block elements. </p>
<p>#define CMARK_OPT_HARDBREAKS (1 &lt;&lt; 2)</p>
<p> Render softbreak elements as hard line breaks. </p>
<p>#define CMARK_OPT_SAFE (1 &lt;&lt; 3)</p>
<p> Suppress raw HTML and unsafe links (javascript:, vbscript:, file:, and data:, except for image/png, image/gif, image/jpeg, or image/webp mime types). Raw HTML is replaced by a placeholder HTML comment. Unsafe links are replaced by empty strings. </p>
<h3>Options affecting parsing</h3>
<p>#define CMARK_OPT_NORMALIZE (1 &lt;&lt; 8)</p>
<p> Normalize tree by consolidating adjacent text nodes. </p>
<p>#define CMARK_OPT_VALIDATE_UTF8 (1 &lt;&lt; 9)</p>
<p> Validate UTF-8 in the input before parsing, replacing illegal sequences with the replacement character U+FFFD. </p>
<pre><code>
#define CMARK_OPT_SMART (1 &lt;&lt; 10)
</code></pre>
<p> Convert straight quotes to curly, &#8212; to em dashes, &#8212; to en dashes. </p>
<h3>Version information</h3>
<p> <i>int</i> <code>cmark_version</code>(<i></i>) </p>
<p> The library version as integer for runtime checks. Also available as macro CMARK_VERSION for compile time checks.</p>
<dl>
<dt>&bull;</p>
<dd> Bits 16-23 contain the major version.</p>
<dt>&bull;</p>
<dd> Bits 8-15 contain the minor version.</p>
<dt>&bull;</p>
<dd> Bits 0-7 contain the patchlevel.</dl>
<p> In hexadecimal format, the number 0x010203 represents version 1.2.3. </p>
<p> <i>const char *</i> <code>cmark_version_string</code>(<i></i>) </p>
<p> The library version string for runtime checks. Also available as macro CMARK_VERSION_STRING for compile time checks. </p>
<h2>AUTHORS</h2>
<p> John MacFarlane, Vicent Marti, Kārlis Gaņģis, Nick Wellnhofer. </p>
<h2>Index</h2>
