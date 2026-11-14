---
title: "libnftables-json(5)"
name: "libnftables-json"
section: "5"
letter: "l"
url: "/docs/linux/man/5-libnftables-json/"
description: "libnftables-json – Supported JSON schema by libnftables"
---

<p>libnftables-json &#8211; Supported JSON schema by libnftables</p>
<h2>Synopsis</h2>
<pre><code>{ &quot;nftables&quot;: [ OBJECTS ] }</code></pre>
<p> <i>OBJECTS</i> := <i>LIST_OBJECTS</i> | <i>CMD_OBJECTS</i> <i>LIST_OBJECTS</i> := <i>LIST_OBJECT</i> [ <code>,</code> <i>LIST_OBJECTS</i> ] <i>CMD_OBJECTS</i> := <i>CMD_OBJECT</i> [ <code>,</code> <i>CMD_OBJECTS</i> ] <i>CMD_OBJECT</i> := <code>{</code> <i>CMD</i><code>:</code> <i>LIST_OBJECT</i> <code>}</code> | <i>METAINFO_OBJECT</i> </p>
<pre><code>CMD := &quot;add&quot; | &quot;replace&quot; | &quot;create&quot; | &quot;insert&quot; | &quot;delete&quot; | &quot;list&quot; | &quot;reset&quot; | &quot;flush&quot; | &quot;rename&quot;</code></pre>
<p> <i>LIST_OBJECT</i> := <i>TABLE</i> | <i>CHAIN</i> | <i>RULE</i> | <i>SET</i> | <i>MAP</i> | <i>ELEMENT</i> | <i>FLOWTABLE</i> | <i>COUNTER</i> | <i>QUOTA</i> | <i>CT_HELPER</i> | <i>LIMIT</i> | <i>METAINFO_OBJECT</i> | <i>CT_TIMEOUT</i> | <i>CT_EXPECTATION</i></p>
<h2>Description</h2>
<p>libnftables supports JSON formatted input and output. This is implemented as an alternative frontend to the standard CLI syntax parser, therefore basic behaviour is identical and, for (almost) any operation available in standard syntax, there should be an equivalent one in JSON. </p>
<p> JSON input may be provided in a single string as parameter to <code>nft_run_cmd_from_buffer()</code> or in a file identified by the <i>filename</i> parameter of the <code>nft_run_cmd_from_filename()</code> function. </p>
<p> JSON output has to be enabled via the <code>nft_ctx_output_set_json()</code> function, turning library standard output into JSON format. Error output remains unaffected.</p>
<h2>Global Structure</h2>
<p>In general, any JSON input or output is enclosed in an object with a single property named <i>nftables</i>. Its value is an array containing commands (for input) or ruleset elements (for output). </p>
<p> A command is an object with a single property whose name identifies the command. Its value is a ruleset element &#8211; basically identical to output elements, apart from certain properties which may be interpreted differently or are required when output generally omits them.</p>
<h2>Metainfo Object</h2>
<p>In output, the first object in an <code>nftables</code> array is a special one containing library information. Its content is as follows: </p>
<dl>
<dd>
<pre><code>{ &quot;metainfo&quot;: {
 &quot;version&quot;:</code> <i>STRING</i><code>,
 &quot;release_name&quot;:</code> <i>STRING</i><code>,
 &quot;json_schema_version&quot;:</code> <i>NUMBER</i>
<code>}}</code></pre>
</dl>
<p> The values of <code>version</code> and <code>release_name</code> properties are equal to the package version and release name as printed by <code>nft -v</code>. The value of the <code>json_schema_version</code> property is an integer indicating the schema version. </p>
<p> If supplied in library input, the parser will verify the <code>json_schema_version</code> value to not exceed the internally hardcoded one (to make sure the given schema is fully understood). In future, a lower number than the internal one may activate compatibility mode to parse outdated and incompatible JSON input.</p>
<h2>Command Objects</h2>
<p>The structure accepts an arbitrary amount of commands which are interpreted in order of appearance. For instance, the following standard syntax input: </p>
<dl>
<dd>
<pre>flush ruleset
add table inet mytable
add chain inet mytable mychain
add rule inet mytable mychain tcp dport 22 accept</pre>
</dl>
<p> translates into JSON as such: </p>
<dl>
<dd>
<pre>{ &quot;nftables&quot;: [
 { &quot;flush&quot;: { &quot;ruleset&quot;: null }},
 { &quot;add&quot;: { &quot;table&quot;: {
 &quot;family&quot;: &quot;inet&quot;,
 &quot;name&quot;: &quot;mytable&quot;
 }}},
 { &quot;add&quot;: { &quot;chain&quot;: {
 &quot;family&quot;: &quot;inet&quot;,
 &quot;table&quot;: &quot;mytable&quot;,
 &quot;name&quot;: &quot;mychain&quot;
 }}},
 { &quot;add&quot;: { &quot;rule&quot;: {
 &quot;family&quot;: &quot;inet&quot;,
 &quot;table&quot;: &quot;mytable&quot;,
 &quot;chain&quot;: &quot;mychain&quot;,
 &quot;expr&quot;: [
 { &quot;match&quot;: {
 &quot;op&quot;: &quot;==&quot;,
 &quot;left&quot;: { &quot;payload&quot;: {
 &quot;protocol&quot;: &quot;tcp&quot;,
 &quot;field&quot;: &quot;dport&quot;
 }},
 &quot;right&quot;: 22
 }},
 { &quot;accept&quot;: null }
 ]
 }}}
]}</pre>
</dl>
<h3>Add</h3>
<dl>
<dd>
<pre><code>{ &quot;add&quot;:</code> <i>ADD_OBJECT</i> <code>}</code>
<i>ADD_OBJECT</i> := <i>TABLE</i> | <i>CHAIN</i> | <i>RULE</i> | <i>SET</i> | <i>MAP</i> | <i>ELEMENT</i> |
 <i>FLOWTABLE</i> | <i>COUNTER</i> | <i>QUOTA</i> | <i>CT_HELPER</i> | <i>LIMIT</i> |
 <i>CT_TIMEOUT</i> | <i>CT_EXPECTATION</i></pre>
</dl>
<p> Add a new ruleset element to the kernel.</p>
<h3>Replace</h3>
<dl>
<dd>
<pre><code>{ &quot;replace&quot;:</code> <i>RULE</i> <code>}</code></pre>
</dl>
<p> Replace a rule. In <i>RULE</i>, the <code>handle</code> property is mandatory and identifies the rule to be replaced.</p>
<h3>Create</h3>
<dl>
<dd>
<pre><code>{ &quot;create&quot;:</code> <i>ADD_OBJECT</i> <code>}</code></pre>
</dl>
<p> Identical to <code>add</code> command, but returns an error if the object already exists.</p>
<h3>Insert</h3>
<dl>
<dd>
<pre><code>{ &quot;insert&quot;:</code> <i>RULE</i> <code>}</code></pre>
</dl>
<p> This command is identical to <code>add</code> for rules, but instead of appending the rule to the chain by default, it inserts at first position. If a <code>handle</code> or <code>index</code> property is given, the rule is inserted before the rule identified by those properties.</p>
<h3>Delete</h3>
<dl>
<dd>
<pre><code>{ &quot;delete&quot;:</code> <i>ADD_OBJECT</i> <code>}</code></pre>
</dl>
<p> Delete an object from the ruleset. Only the minimal number of properties required to uniquely identify an object is generally needed in <i>ADD_OBJECT</i>. For most ruleset elements, this is <code>family</code> and <code>table</code> plus either <code>handle</code> or <code>name</code> (except rules since they don&#8217;t have a name).</p>
<h3>List</h3>
<dl>
<dd>
<pre><code>{ &quot;list&quot;:</code> <i>LIST_OBJECT</i> <code>}</code>
<i>LIST_OBJECT</i> := <i>TABLE</i> | <i>TABLES</i> | <i>CHAIN</i> | <i>CHAINS</i> | <i>SET</i> | <i>SETS</i> |
 <i>MAP</i> | <i>MAPS | COUNTER</i> | <i>COUNTERS</i> | <i>QUOTA</i> | <i>QUOTAS</i> |
 <i>CT_HELPER</i> | <i>CT_HELPERS</i> | <i>LIMIT</i> | <i>LIMITS</i> | <i>RULESET</i> |
 <i>METER</i> | <i>METERS</i> | <i>FLOWTABLE</i> | <i>FLOWTABLES</i> |
 <i>CT_TIMEOUT</i> | <i>CT_EXPECTATION</i></pre>
</dl>
<p> List ruleset elements. The plural forms are used to list all objects of that kind, optionally filtered by <code>family</code> and for some, also <code>table</code>.</p>
<h3>Reset</h3>
<dl>
<dd>
<pre><code>{ &quot;reset&quot;:</code> <i>RESET_OBJECT</i> <code>}</code>
<i>RESET_OBJECT</i> := <i>COUNTER</i> | <i>COUNTERS</i> | <i>QUOTA</i> | <i>QUOTAS</i></pre>
</dl>
<p> Reset state in suitable objects, i.e. zero their internal counter.</p>
<h3>Flush</h3>
<dl>
<dd>
<pre><code>{ &quot;flush&quot;:</code> <i>FLUSH_OBJECT</i> <code>}</code>
<i>FLUSH_OBJECT</i> := <i>TABLE</i> | <i>CHAIN</i> | <i>SET</i> | <i>MAP</i> | <i>METER</i> | <i>RULESET</i></pre>
</dl>
<p> Empty contents in given object, e.g. remove all chains from given <code>table</code> or remove all elements from given <code>set</code>.</p>
<h3>Rename</h3>
<dl>
<dd>
<pre><code>{ &quot;rename&quot;:</code> <i>CHAIN</i> <code>}</code></pre>
</dl>
<p> Rename a chain. The new name is expected in a dedicated property named <code>newname</code>.</p>
<h2>Ruleset Elements</h2>
<h3>Table</h3>
<dl>
<dd>
<pre><code>{ &quot;table&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>NUMBER</i>
<code>}}</code></pre>
</dl>
<p> This object describes a table. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family, e.g. <code>&quot;ip&quot;</code> or <code>&quot;ip6&quot;</code>.</dl>
<p> <code>name</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The table&#8217;s handle. In input, it is used only in <code>delete</code> command as alternative to <code>name</code>.</dl>
<h3>Chain</h3>
<dl>
<dd>
<pre><code>{ &quot;chain&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;newname&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>NUMBER</i><code>,
 &quot;type&quot;:</code> <i>STRING</i><code>,
 &quot;hook&quot;:</code> <i>STRING</i><code>,
 &quot;prio&quot;:</code> <i>NUMBER</i><code>,
 &quot;dev&quot;:</code> <i>STRING</i><code>,
 &quot;policy&quot;:</code> <i>STRING</i>
<code>}}</code></pre>
</dl>
<p> This object describes a chain. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>name</code></p>
<dl>
<dd>The chain&#8217;s name.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The chain&#8217;s handle. In input, it is used only in <code>delete</code> command as alternative to <code>name</code>.</dl>
<p> <code>newname</code></p>
<dl>
<dd>A new name for the chain, only relevant in the <code>rename</code> command.</dl>
<p> The following properties are required for base chains: </p>
<p> <code>type</code></p>
<dl>
<dd>The chain&#8217;s type.</dl>
<p> <code>hook</code></p>
<dl>
<dd>The chain&#8217;s hook.</dl>
<p> <code>prio</code></p>
<dl>
<dd>The chain&#8217;s priority.</dl>
<p> <code>dev</code></p>
<dl>
<dd>The chain&#8217;s bound interface (if in the netdev family).</dl>
<p> <code>policy</code></p>
<dl>
<dd>The chain&#8217;s policy.</dl>
<h3>Rule</h3>
<dl>
<dd>
<pre><code>{ &quot;rule&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;chain&quot;:</code> <i>STRING</i><code>,
 &quot;expr&quot;: [</code> <i>STATEMENTS</i> <code>],
 &quot;handle&quot;:</code> <i>NUMBER</i><code>,
 &quot;index&quot;:</code> <i>NUMBER</i><code>,
 &quot;comment&quot;:</code> <i>STRING</i>
<code>}}</code>
<i>STATEMENTS</i> := <i>STATEMENT</i> [<code>,</code> <i>STATEMENTS</i> ]</pre>
</dl>
<p> This object describes a rule. Basic building blocks of rules are statements. Each rule consists of at least one. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>chain</code></p>
<dl>
<dd>The chain&#8217;s name.</dl>
<p> <code>expr</code></p>
<dl>
<dd>An array of statements this rule consists of. In input, it is used in <code>add</code>/<code>insert</code>/<code>replace</code> commands only.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The rule&#8217;s handle. In <code>delete</code>/<code>replace</code> commands, it serves as an identifier of the rule to delete/replace. In <code>add</code>/<code>insert</code> commands, it serves as an identifier of an existing rule to append/prepend the rule to.</dl>
<p> <code>index</code></p>
<dl>
<dd>The rule&#8217;s position for <code>add</code>/<code>insert</code> commands. It is used as an alternative to <code>handle</code> then.</dl>
<p> <code>comment</code></p>
<dl>
<dd>Optional rule comment.</dl>
<h3>Set / Map</h3>
<dl>
<dd>
<pre><code>{ &quot;set&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>NUMBER</i><code>,
 &quot;type&quot;:</code> <i>SET_TYPE</i><code>,
 &quot;policy&quot;:</code> <i>SET_POLICY</i><code>,
 &quot;flags&quot;: [</code> <i>SET_FLAG_LIST</i> <code>],
 &quot;elem&quot;:</code> <i>SET_ELEMENTS</i><code>,
 &quot;timeout&quot;:</code> <i>NUMBER</i><code>,
 &quot;gc-interval&quot;:</code> <i>NUMBER</i><code>,
 &quot;size&quot;:</code> <i>NUMBER</i>
<code>}}</code>
<code>{ &quot;map&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>NUMBER</i><code>,
 &quot;type&quot;:</code> <i>SET_TYPE</i><code>,
 &quot;map&quot;:</code> <i>STRING</i><code>,
 &quot;policy&quot;:</code> <i>SET_POLICY</i><code>,
 &quot;flags&quot;: [</code> <i>SET_FLAG_LIST</i> <code>],
 &quot;elem&quot;:</code> <i>SET_ELEMENTS</i><code>,
 &quot;timeout&quot;:</code> <i>NUMBER</i><code>,
 &quot;gc-interval&quot;:</code> <i>NUMBER</i><code>,
 &quot;size&quot;:</code> <i>NUMBER</i>
<code>}}</code>
<i>SET_TYPE</i> := <i>STRING</i> | <code>[</code> <i>SET_TYPE_LIST</i> <code>]</code>
<i>SET_TYPE_LIST</i> := <i>STRING</i> [<code>,</code> <i>SET_TYPE_LIST</i> ]
<i>SET_POLICY</i> := <code>&quot;performance&quot;</code> | <code>&quot;memory&quot;</code>
<i>SET_FLAG_LIST</i> := <i>SET_FLAG</i> [<code>,</code> <i>SET_FLAG_LIST</i> ]
<i>SET_FLAG</i> := <code>&quot;constant&quot;</code> | <code>&quot;interval&quot;</code> | <code>&quot;timeout&quot;</code>
<i>SET_ELEMENTS</i> := <i>EXPRESSION</i> | <code>[</code> <i>EXPRESSION_LIST</i> <code>]</code>
<i>EXPRESSION_LIST</i> := <i>EXPRESSION</i> [<code>,</code> <i>EXPRESSION_LIST</i> ]</pre>
</dl>
<p> These objects describe a named set or map. Maps are a special form of sets in that they translate a unique key to a value. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>name</code></p>
<dl>
<dd>The set&#8217;s name.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The set&#8217;s handle. For input, it is used in the <code>delete</code> command only.</dl>
<p> <code>type</code></p>
<dl>
<dd>The set&#8217;s datatype, see below.</dl>
<p> <code>map</code></p>
<dl>
<dd>Type of values this set maps to (i.e. this set is a map).</dl>
<p> <code>policy</code></p>
<dl>
<dd>The set&#8217;s policy.</dl>
<p> <code>flags</code></p>
<dl>
<dd>The set&#8217;s flags.</dl>
<p> <code>elem</code></p>
<dl>
<dd>Initial set element(s), see below.</dl>
<p> <code>timeout</code></p>
<dl>
<dd>Element timeout in seconds.</dl>
<p> <code>gc-interval</code></p>
<dl>
<dd>Garbage collector interval in seconds.</dl>
<p> <code>size</code></p>
<dl>
<dd>Maximum number of elements supported.</dl>
<p> <font SIZE="+1"> <code>TYPE</code></p>
<dl>
<dd>The set type might be a string, such as <code>&quot;ipv4_addr&quot;</code> or an array consisting of strings (for concatenated types).</dl>
<p> </font><font SIZE="+2"> <code>ELEM</code></p>
<dl>
<dd>A single set element might be given as string, integer or boolean value for simple cases. If additional properties are required, a formal <code>elem</code> object may be used. </p>
<p> Multiple elements may be given in an array.</dl>
<p> </font></p>
<h3>Element</h3>
<dl>
<dd>
<pre><code>{ &quot;element&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;elem&quot;:</code> <i>SET_ELEM</i>
<code>}}</code>
<i>SET_ELEM</i> := <i>EXPRESSION</i> | <code>[</code> <i>EXPRESSION_LIST</i> <code>]</code>
<i>EXPRESSION_LIST</i> := <i>EXPRESSION</i> [<code>,</code> <i>EXPRESSION</i> ]</pre>
</dl>
<p> Manipulate element(s) in a named set. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>name</code></p>
<dl>
<dd>The set&#8217;s name.</dl>
<p> <code>elem</code></p>
<dl>
<dd>See elem property of set object.</dl>
<h3>Flowtable</h3>
<dl>
<dd>
<pre><code>{ &quot;flowtable&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>NUMBER</i><code>,
 &quot;hook&quot;:</code> <i>STRING</i><code>,
 &quot;prio&quot;:</code> <i>NUMBER</i><code>,
 &quot;dev&quot;:</code> <i>FT_INTERFACE</i>
<code>}}</code>
<i>FT_INTERFACE</i> := <i>STRING</i> | <code>[</code> <i>FT_INTERFACE_LIST</i> <code>]</code>
<i>FT_INTERFACE_LIST</i> := <i>STRING</i> [<code>,</code> <i>STRING</i> ]</pre>
</dl>
<p> This object represents a named flowtable. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>name</code></p>
<dl>
<dd>The flow table&#8217;s name.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The flow table&#8217;s handle. In input, it is used by the <code>delete</code> command only.</dl>
<p> <code>hook</code></p>
<dl>
<dd>The flow table&#8217;s hook.</dl>
<p> <code>prio</code></p>
<dl>
<dd>The flow table&#8217;s priority.</dl>
<p> <code>dev</code></p>
<dl>
<dd>The flow table&#8217;s interface(s).</dl>
<h3>Counter</h3>
<dl>
<dd>
<pre><code>{ &quot;counter&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>NUMBER</i><code>,
 &quot;packets&quot;:</code> <i>NUMBER</i><code>,
 &quot;bytes&quot;:</code> <i>NUMBER</i>
<code>}}</code></pre>
</dl>
<p> This object represents a named counter. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>name</code></p>
<dl>
<dd>The counter&#8217;s name.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The counter&#8217;s handle. In input, it is used by the <code>delete</code> command only.</dl>
<p> <code>packets</code></p>
<dl>
<dd>Packet counter value.</dl>
<p> <code>bytes</code></p>
<dl>
<dd>Byte counter value.</dl>
<h3>Quota</h3>
<dl>
<dd>
<pre><code>{ &quot;quota&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>NUMBER</i><code>,
 &quot;bytes&quot;:</code> <i>NUMBER</i><code>,
 &quot;used&quot;:</code> <i>NUMBER</i><code>,
 &quot;inv&quot;:</code> <i>BOOLEAN</i>
<code>}}</code></pre>
</dl>
<p> This object represents a named quota. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>name</code></p>
<dl>
<dd>The quota&#8217;s name.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The quota&#8217;s handle. In input, it is used by the <code>delete</code> command only.</dl>
<p> <code>bytes</code></p>
<dl>
<dd>Quota threshold.</dl>
<p> <code>used</code></p>
<dl>
<dd>Quota used so far.</dl>
<p> <code>inv</code></p>
<dl>
<dd>If true, match if the quota has been exceeded.</dl>
<h3>Ct Helper</h3>
<dl>
<dd>
<pre><code>{ &quot;ct helper&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>... '</i><i></i><code>,
 &quot;type&quot;:</code><i> 'STRING</i><code>,
 &quot;protocol&quot;:</code> <i>CTH_PROTO</i><code>,
 &quot;l3proto&quot;:</code> <i>STRING</i>
<code>}}</code>
<i>CTH_PROTO</i> := <code>&quot;tcp&quot;</code> | <code>&quot;udp&quot;</code></pre>
</dl>
<p> This object represents a named conntrack helper. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>name</code></p>
<dl>
<dd>The ct helper&#8217;s name.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The ct helper&#8217;s handle. In input, it is used by the <code>delete</code> command only.</dl>
<p> <code>type</code></p>
<dl>
<dd>The ct helper type name, e.g. <code>&quot;ftp&quot;</code> or <code>&quot;tftp&quot;</code>.</dl>
<p> <code>protocol</code></p>
<dl>
<dd>The ct helper&#8217;s layer 4 protocol.</dl>
<p> <code>l3proto</code></p>
<dl>
<dd>The ct helper&#8217;s layer 3 protocol, e.g. <code>&quot;ip&quot;</code> or <code>&quot;ip6&quot;</code>.</dl>
<h3>Limit</h3>
<dl>
<dd>
<pre><code>{ &quot;limit&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>NUMBER</i><code>,
 &quot;rate&quot;:</code> <i>NUMBER</i><code>,
 &quot;per&quot;:</code> <i>STRING</i><code>,
 &quot;burst&quot;:</code> <i>NUMBER</i><code>,
 &quot;unit&quot;:</code> <i>LIMIT_UNIT</i><code>,
 &quot;inv&quot;:</code> <i>BOOLEAN</i>
<code>}}</code>
<i>LIMIT_UNIT</i> := <code>&quot;packets&quot;</code> | <code>&quot;bytes&quot;</code></pre>
</dl>
<p> This object represents a named limit. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>name</code></p>
<dl>
<dd>The limit&#8217;s name.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The limit&#8217;s handle. In input, it is used by the <code>delete</code> command only.</dl>
<p> <code>rate</code></p>
<dl>
<dd>The limit&#8217;s rate value.</dl>
<p> <code>per</code></p>
<dl>
<dd>Time unit to apply the limit to, e.g. <code>&quot;week&quot;</code>, <code>&quot;day&quot;</code>, <code>&quot;hour&quot;</code>, etc. If omitted, defaults to <code>&quot;second&quot;</code>.</dl>
<p> <code>burst</code></p>
<dl>
<dd>The limit&#8217;s burst value. If omitted, defaults to <code>0</code>.</dl>
<p> <code>unit</code></p>
<dl>
<dd>Unit of rate and burst values. If omitted, defaults to <code>&quot;packets&quot;</code>.</dl>
<p> <code>inv</code></p>
<dl>
<dd>If true, match if limit was exceeded. If omitted, defaults to <code>false</code>.</dl>
<h3>Ct Timeout</h3>
<dl>
<dd>
<pre><code>{ &quot;ct timeout&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>NUMBER</i><code>,
 &quot;protocol&quot;:</code> <i>CTH_PROTO</i><code>,
 &quot;state&quot;:</code> <i>STRING</i><code>,
 &quot;value:</code> <i>NUMBER</i><code>,
 &quot;l3proto&quot;:</code> <i>STRING</i>
<code>}}</code>
<i>CTH_PROTO</i> := <code>&quot;tcp&quot;</code> | <code>&quot;udp&quot;</code> | <code>&quot;dccp&quot;</code> | <code>&quot;sctp&quot;</code> | <code>&quot;gre&quot;</code> | <code>&quot;icmpv6&quot;</code> | <code>&quot;icmp&quot;</code> | <code>&quot;generic&quot;</code></pre>
</dl>
<p> This object represents a named conntrack timeout policy. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>name</code></p>
<dl>
<dd>The ct timeout object&#8217;s name.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The ct timeout object&#8217;s handle. In input, it is used by <code>delete</code> command only.</dl>
<p> <code>protocol</code></p>
<dl>
<dd>The ct timeout object&#8217;s layer 4 protocol.</dl>
<p> <code>state</code></p>
<dl>
<dd>The connection state name, e.g. <code>&quot;established&quot;</code>, <code>&quot;syn_sent&quot;</code>, <code>&quot;close&quot;</code> or <code>&quot;close_wait&quot;</code>, for which the timeout value has to be updated.</dl>
<p> <code>value</code></p>
<dl>
<dd>The updated timeout value for the specified connection state.</dl>
<p> <code>l3proto</code></p>
<dl>
<dd>The ct timeout object&#8217;s layer 3 protocol, e.g. <code>&quot;ip&quot;</code> or <code>&quot;ip6&quot;</code>.</dl>
<h3>Ct Expectation</h3>
<dl>
<dd>
<pre><code>{ &quot;ct expectation&quot;: {
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;table&quot;:</code> <i>STRING</i><code>,
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;handle&quot;:</code> <i>NUMBER</i><code>,
 &quot;l3proto&quot;:</code> <i>STRING</i>
 &quot;protocol&quot;:* <i>CTH_PROTO</i><code>,
 &quot;dport&quot;:</code> <i>NUMBER</i><code>,
 &quot;timeout:</code> <i>NUMBER</i><code>,
 &quot;size:</code> <i>NUMBER</i><code>,
*}}</code>
<i>CTH_PROTO</i> := <code>&quot;tcp&quot;</code> | <code>&quot;udp&quot;</code> | <code>&quot;dccp&quot;</code> | <code>&quot;sctp&quot;</code> | <code>&quot;gre&quot;</code> | <code>&quot;icmpv6&quot;</code> | <code>&quot;icmp&quot;</code> | <code>&quot;generic&quot;</code></pre>
</dl>
<p> This object represents a named conntrack expectation. </p>
<p> <code>family</code></p>
<dl>
<dd>The table&#8217;s family.</dl>
<p> <code>table</code></p>
<dl>
<dd>The table&#8217;s name.</dl>
<p> <code>name</code></p>
<dl>
<dd>The ct expectation object&#8217;s name.</dl>
<p> <code>handle</code></p>
<dl>
<dd>The ct expectation object&#8217;s handle. In input, it is used by <code>delete</code> command only.</dl>
<p> <code>l3proto</code></p>
<dl>
<dd>The ct expectation object&#8217;s layer 3 protocol, e.g. <code>&quot;ip&quot;</code> or <code>&quot;ip6&quot;</code>.</dl>
<p> <code>protocol</code></p>
<dl>
<dd>The ct expectation object&#8217;s layer 4 protocol.</dl>
<p> <code>dport</code></p>
<dl>
<dd>The destination port of the expected connection.</dl>
<p> <code>timeout</code></p>
<dl>
<dd>The time in millisecond that this expectation will live.</dl>
<p> <code>size</code></p>
<dl>
<dd>The maximum count of expectations to be living in the same time.</dl>
<h2>Statements</h2>
<p>Statements are the building blocks for rules. Each rule consists of at least one.</p>
<h3>Verdict</h3>
<dl>
<dd>
<pre><code>{ &quot;accept&quot;: null }</code>
<code>{ &quot;drop&quot;: null }</code>
<code>{ &quot;continue&quot;: null }</code>
<code>{ &quot;return&quot;: null }</code>
<code>{ &quot;jump&quot;: { &quot;target&quot;: * </code><i>STRING</i><code> *}}</code>
<code>{ &quot;goto&quot;: { &quot;target&quot;: * </code><i>STRING</i><code> *}}</code></pre>
</dl>
<p> A verdict either terminates packet traversal through the current chain or delegates to a different one. </p>
<p> <code>jump</code> and <code>goto</code> statements expect a target chain name.</p>
<h3>Match</h3>
<dl>
<dd>
<pre><code>{ &quot;match&quot;: {
 &quot;left&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;right&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;op&quot;:</code> <i>STRING</i>
<code>}}</code></pre>
</dl>
<p> This matches the expression on left hand side (typically a packet header or packet meta info) with the expression on right hand side (typically a constant value). If the statement evaluates to true, the next statement in this rule is considered. If not, processing continues with the next rule in the same chain. </p>
<p> <code>left</code></p>
<dl>
<dd>Left hand side of this match.</dl>
<p> <code>right</code></p>
<dl>
<dd>Right hand side of this match.</dl>
<p> <code>op</code></p>
<dl>
<dd>Operator indicating the type of comparison.</dl>
<p> <font SIZE="+1"> <code>OPERATORS</code></p>
<dl>
<dd></font></p>
<table>
<tr VALIGN=top>
<td>
<p> <code>&amp;</code> </td>
<td>
<p> Binary AND
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>|</code> </td>
<td>
<p> Binary OR
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>^</code> </td>
<td>
<p> Binary XOR
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>&lt;&lt;</code> </td>
<td>
<p> Left shift
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>&gt;&gt;</code> </td>
<td>
<p> Right shift
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>==</code> </td>
<td>
<p> Equal
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>!=</code> </td>
<td>
<p> Not equal
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>&lt;</code> </td>
<td>
<p> Less than
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>&gt;</code> </td>
<td>
<p> Greater than
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>⇐</code> </td>
<td>
<p> Less than or equal to
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>&gt;=</code> </td>
<td>
<p> Greater than or equal to
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>in</code> </td>
<td>
<p> Perform a lookup, i.e. test if bits on RHS are contained in LHS value
</td>
</tr>
</table>
<p> <font SIZE="+1"> </p>
<p> Unlike with the standard API, the operator is mandatory here. In the standard API, a missing operator may be resolved in two ways, depending on the type of expression on the RHS: </p>
<dl>
<dd>&bull; If the RHS is a bitmask or a list of bitmasks, the expression resolves into a binary operation with the inequality operator, like this: <i>LHS &amp; RHS != 0</i>.</dl>
<dl>
<dd>&bull; In any other case, the equality operator is simply inserted.</dl>
<p> For the non-trivial first case, the JSON API supports the <code>in</code> operator.</dl>
<p> </font></p>
<h3>Counter</h3>
<dl>
<dd>
<pre><code>{ &quot;counter&quot;: {
 &quot;packets&quot;:</code> <i>NUMBER</i><code>,
 &quot;bytes&quot;:</code> <i>NUMBER</i>
<code>}}</code>
<code>{ &quot;counter&quot;:</code> <i>STRING</i> <code>}</code></pre>
</dl>
<p> This object represents a byte/packet counter. In input, no properties are required. If given, they act as initial values for the counter. </p>
<p> The first form creates an anonymous counter which lives in the rule it appears in. The second form specifies a reference to a named counter object. </p>
<p> <code>packets</code></p>
<dl>
<dd>Packets counted.</dl>
<p> <code>bytes</code></p>
<dl>
<dd>Bytes counted.</dl>
<h3>Mangle</h3>
<dl>
<dd>
<pre><code>{ &quot;mangle&quot;: {
 &quot;key&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;value&quot;:</code> <i>EXPRESSION</i>
<code>}}</code></pre>
</dl>
<p> This changes the packet data or meta info. </p>
<p> <code>key</code></p>
<dl>
<dd>The packet data to be changed, given as an <code>exthdr</code>, <code>payload</code>, <code>meta</code>, <code>ct</code> or <code>ct helper</code> expression.</dl>
<p> <code>value</code></p>
<dl>
<dd>Value to change data to.</dl>
<h3>Quota</h3>
<dl>
<dd>
<pre><code>{ &quot;quota&quot;: {
 &quot;val&quot;:</code> <i>NUMBER</i><code>,
 &quot;val_unit&quot;:</code> <i>STRING</i><code>,
 &quot;used&quot;:</code> <i>NUMBER</i><code>,
 &quot;used_unit&quot;:</code> <i>STRING</i><code>,
 &quot;inv&quot;:</code> <i>BOOLEAN</i>
<code>}}</code>
<code>{ &quot;quota&quot;:</code> <i>STRING</i> <code>}</code></pre>
</dl>
<p> The first form creates an anonymous quota which lives in the rule it appears in. The second form specifies a reference to a named quota object. </p>
<p> <code>val</code></p>
<dl>
<dd>Quota value.</dl>
<p> <code>val_unit</code></p>
<dl>
<dd>Unit of <code>val</code>, e.g. <code>&quot;kbytes&quot;</code> or <code>&quot;mbytes&quot;</code>. If omitted, defaults to <code>&quot;bytes&quot;</code>.</dl>
<p> <code>used</code></p>
<dl>
<dd>Quota used so far. Optional on input. If given, serves as initial value.</dl>
<p> <code>used_unit</code></p>
<dl>
<dd>Unit of <code>used</code>. Defaults to <code>&quot;bytes&quot;</code>.</dl>
<p> <code>inv</code></p>
<dl>
<dd>If <code>true</code>, will match if quota was exceeded. Defaults to <code>false</code>.</dl>
<h3>Limit</h3>
<dl>
<dd>
<pre><code>{ &quot;limit&quot;: {
 &quot;rate&quot;:</code> <i>NUMBER</i><code>,
 &quot;rate_unit&quot;:</code> <i>STRING</i><code>,
 &quot;per&quot;:</code> <i>STRING</i><code>,
 &quot;burst&quot;:</code> <i>NUMBER</i><code>,
 &quot;burst_unit&quot;:</code> <i>STRING</i><code>,
 &quot;inv&quot;:</code> <i>BOOLEAN</i>
<code>}}</code>
<code>{ &quot;limit&quot;:</code> <i>STRING</i> <code>}</code></pre>
</dl>
<p> The first form creates an anonymous limit which lives in the rule it appears in. The second form specifies a reference to a named limit object. </p>
<p> <code>rate</code></p>
<dl>
<dd>Rate value to limit to.</dl>
<p> <code>rate_unit</code></p>
<dl>
<dd>Unit of <code>rate</code>, e.g. <code>&quot;packets&quot;</code> or <code>&quot;mbytes&quot;</code>. Defaults to <code>&quot;packets&quot;</code>.</dl>
<p> <code>per</code></p>
<dl>
<dd>Denominator of <code>rate</code>, e.g. <code>&quot;week&quot;</code> or <code>&quot;minutes&quot;</code>.</dl>
<p> <code>burst</code></p>
<dl>
<dd>Burst value. Defaults to <code>0</code>.</dl>
<p> <code>burst_unit</code></p>
<dl>
<dd>Unit of <code>burst</code>, ignored if <code>rate_unit</code> is <code>&quot;packets&quot;</code>. Defaults to <code>&quot;bytes&quot;</code>.</dl>
<p> <code>inv</code></p>
<dl>
<dd>If <code>true</code>, matches if the limit was exceeded. Defaults to <code>false</code>.</dl>
<h3>Fwd</h3>
<dl>
<dd>
<pre><code>{ &quot;fwd&quot;: {
 &quot;dev&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;family&quot;:</code> <i>FWD_FAMILY</i><code>,
 &quot;addr&quot;:</code> <i>EXPRESSION</i>
<code>}}</code>
<i>FWD_FAMILY</i> := <code>&quot;ip&quot;</code> | <code>&quot;ip6&quot;</code></pre>
</dl>
<p> Forward a packet to a different destination. </p>
<p> <code>dev</code></p>
<dl>
<dd>Interface to forward the packet on.</dl>
<p> <code>family</code></p>
<dl>
<dd>Family of <code>addr</code>.</dl>
<p> <code>addr</code></p>
<dl>
<dd>IP(v6) address to forward the packet to.</dl>
<p> Both <code>family</code> and <code>addr</code> are optional, but if at least one is given, both must be present.</p>
<h3>Notrack</h3>
<dl>
<dd>
<pre><code>{ &quot;notrack&quot;: null }</code></pre>
</dl>
<p> Disable connection tracking for the packet.</p>
<h3>Dup</h3>
<dl>
<dd>
<pre><code>{ &quot;dup&quot;: {
 &quot;addr&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;dev&quot;:</code> <i>EXPRESSION</i>
<code>}}</code></pre>
</dl>
<p> Duplicate a packet to a different destination. </p>
<p> <code>addr</code></p>
<dl>
<dd>Address to duplicate packet to.</dl>
<p> <code>dev</code></p>
<dl>
<dd>Interface to duplicate packet on. May be omitted to not specify an interface explicitly.</dl>
<h3>Network Address Translation</h3>
<dl>
<dd>
<pre><code>{ &quot;snat&quot;: {
 &quot;addr&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;port&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;flags&quot;:</code> <i>FLAGS</i>
<code>}}</code>
<code>{ &quot;dnat&quot;: {
 &quot;addr&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;family&quot;:</code> <i>STRING</i><code>,
 &quot;port&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;flags&quot;:</code> <i>FLAGS</i>
<code>}}</code>
<code>{ &quot;masquerade&quot;: {
 &quot;port&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;flags&quot;:</code> <i>FLAGS</i>
<code>}}</code>
<code>{ &quot;redirect&quot;: {
 &quot;port&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;flags&quot;:</code> <i>FLAGS</i>
<code>}}</code>
<i>FLAGS</i> := <i>FLAG</i> | <code>[</code> <i>FLAG_LIST</i> <code>]</code>
<i>FLAG_LIST</i> := <i>FLAG</i> [<code>,</code> <i>FLAG_LIST</i> ]
<i>FLAG</i> := <code>&quot;random&quot;</code> | <code>&quot;fully-random&quot;</code> | <code>&quot;persistent&quot;</code></pre>
</dl>
<p> Perform Network Address Translation. </p>
<p> <code>addr</code></p>
<dl>
<dd>Address to translate to.</dl>
<p> <code>family</code></p>
<dl>
<dd>Family of <code>addr</code>, either <code>ip</code> or <code>ip6</code>. Required in <code>inet</code> table family.</dl>
<p> <code>port</code></p>
<dl>
<dd>Port to translate to.</dl>
<p> <code>flags</code></p>
<dl>
<dd>Flag(s).</dl>
<p> All properties are optional and default to none.</p>
<h3>Reject</h3>
<dl>
<dd>
<pre><code>{ &quot;reject&quot;: {
 &quot;type&quot;:</code> <i>STRING</i><code>,
 &quot;expr&quot;:</code> <i>EXPRESSION</i>
<code>}}</code></pre>
</dl>
<p> Reject the packet and send the given error reply. </p>
<p> <code>type</code></p>
<dl>
<dd>Type of reject, either <code>&quot;tcp reset&quot;</code>, <code>&quot;icmpx&quot;</code>, <code>&quot;icmp&quot;</code> or <code>&quot;icmpv6&quot;</code>.</dl>
<p> <code>expr</code></p>
<dl>
<dd>ICMP code to reject with.</dl>
<p> All properties are optional.</p>
<h3>Set</h3>
<dl>
<dd>
<pre><code>{ &quot;set&quot;: {
 &quot;op&quot;:</code> <i>STRING</i><code>,
 &quot;elem&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;set&quot;:</code> <i>STRING</i>
<code>}}</code></pre>
</dl>
<p> Dynamically add/update elements to a set. </p>
<p> <code>op</code></p>
<dl>
<dd>Operator on set, either <code>&quot;add&quot;</code> or <code>&quot;update&quot;</code>.</dl>
<p> <code>elem</code></p>
<dl>
<dd>Set element to add or update.</dl>
<p> <code>set</code></p>
<dl>
<dd>Set reference.</dl>
<h3>Log</h3>
<dl>
<dd>
<pre><code>{ &quot;log&quot;: {
 &quot;prefix&quot;:</code> <i>STRING</i><code>,
 &quot;group&quot;:</code> <i>NUMBER</i><code>,
 &quot;snaplen&quot;:</code> <i>NUMBER</i><code>,
 &quot;queue-threshold&quot;:</code> <i>NUMBER</i><code>,
 &quot;level&quot;:</code> <i>LEVEL</i><code>,
 &quot;flags&quot;:</code> <i>FLAGS</i>
<code>}}</code>
<i>LEVEL</i> := <code>&quot;emerg&quot;</code> | <code>&quot;alert&quot;</code> | <code>&quot;crit&quot;</code> | <code>&quot;err&quot;</code> | <code>&quot;warn&quot;</code> | <code>&quot;notice&quot;</code> |
 <code>&quot;info&quot;</code> | <code>&quot;debug&quot;</code> | <code>&quot;audit&quot;</code>
<i>FLAGS</i> := <i>FLAG</i> | <code>[</code> <i>FLAG_LIST</i> <code>]</code>
<i>FLAG_LIST</i> := <i>FLAG</i> [<code>,</code> <i>FLAG_LIST</i> ]
<i>FLAG</i> := <code>&quot;tcp sequence&quot;</code> | <code>&quot;tcp options&quot;</code> | <code>&quot;ip options&quot;</code> | <code>&quot;skuid&quot;</code> |
 <code>&quot;ether&quot;</code> | <code>&quot;all&quot;</code></pre>
</dl>
<p> Log the packet. </p>
<p> <code>prefix</code></p>
<dl>
<dd>Prefix for log entries.</dl>
<p> <code>group</code></p>
<dl>
<dd>Log group.</dl>
<p> <code>snaplen</code></p>
<dl>
<dd>Snaplen for logging.</dl>
<p> <code>queue-threshold</code></p>
<dl>
<dd>Queue threshold.</dl>
<p> <code>level</code></p>
<dl>
<dd>Log level. Defaults to <code>&quot;warn&quot;</code>.</dl>
<p> <code>flags</code></p>
<dl>
<dd>Log flags.</dl>
<p> All properties are optional.</p>
<h3>Ct Helper</h3>
<dl>
<dd>
<pre><code>{ &quot;ct helper&quot;:</code> <i>EXPRESSION</i> <code>}</code></pre>
</dl>
<p> Enable the specified conntrack helper for this packet. </p>
<p> <code>ct helper</code></p>
<dl>
<dd>CT helper reference.</dl>
<h3>Meter</h3>
<dl>
<dd>
<pre><code>{ &quot;meter&quot;: {
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;key&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;stmt&quot;:</code> <i>STATEMENT</i>
<code>}}</code></pre>
</dl>
<p> Apply a given statement using a meter. </p>
<p> <code>name</code></p>
<dl>
<dd>Meter name.</dl>
<p> <code>key</code></p>
<dl>
<dd>Meter key.</dl>
<p> <code>stmt</code></p>
<dl>
<dd>Meter statement.</dl>
<h3>Queue</h3>
<dl>
<dd>
<pre><code>{ &quot;queue&quot;: {
 &quot;num&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;flags&quot;:</code> <i>FLAGS</i>
<code>}}</code>
<i>FLAGS</i> := <i>FLAG</i> | <code>[</code> <i>FLAG_LIST</i> <code>]</code>
<i>FLAG_LIST</i> := <i>FLAG</i> [<code>,</code> <i>FLAG_LIST</i> ]
<i>FLAG</i> := <code>&quot;bypass&quot;</code> | <code>&quot;fanout&quot;</code></pre>
</dl>
<p> Queue the packet to userspace. </p>
<p> <code>num</code></p>
<dl>
<dd>Queue number.</dl>
<p> <code>flags</code></p>
<dl>
<dd>Queue flags.</dl>
<h3>Verdict Map</h3>
<dl>
<dd>
<pre><code>{ &quot;vmap&quot;: {
 &quot;key&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;data&quot;:</code> <i>EXPRESSION</i>
<code>}}</code></pre>
</dl>
<p> Apply a verdict conditionally. </p>
<p> <code>key</code></p>
<dl>
<dd>Map key.</dl>
<p> <code>data</code></p>
<dl>
<dd>Mapping expression consisting of value/verdict pairs.</dl>
<h3>Ct Count</h3>
<dl>
<dd>
<pre><code>{ &quot;ct count&quot;: {
 &quot;val&quot;:</code> <i>NUMBER</i><code>,
 &quot;inv&quot;:</code> <i>BOOLEAN</i>
<code>}}</code></pre>
</dl>
<p> Limit the number of connections using conntrack. </p>
<p> <code>val</code></p>
<dl>
<dd>Connection count threshold.</dl>
<p> <code>inv</code></p>
<dl>
<dd>If <code>true</code>, match if <code>val</code> was exceeded. If omitted, defaults to <code>false</code>.</dl>
<h3>Ct Timeout</h3>
<dl>
<dd>
<pre><code>{ &quot;ct timeout&quot;:</code> <i>EXPRESSION</i> <code>}</code></pre>
</dl>
<p> Assign connection tracking timeout policy. </p>
<p> <code>ct timeout</code></p>
<dl>
<dd>CT timeout reference.</dl>
<h3>Ct Expectation</h3>
<dl>
<dd>
<pre><code>{ &quot;ct expectation&quot;:</code> <i>EXPRESSION</i> <code>}</code></pre>
</dl>
<p> Assign connection tracking expectation. </p>
<p> <code>ct expectation</code></p>
<dl>
<dd>CT expectation reference.</dl>
<h3>Xt</h3>
<dl>
<dd>
<pre><code>{ &quot;xt&quot;: null }</code></pre>
</dl>
<p> This represents an xt statement from xtables compat interface. Sadly, at this point, it is not possible to provide any further information about its content.</p>
<h2>Expressions</h2>
<p>Expressions are the building blocks of (most) statements. In their most basic form, they are just immediate values represented as a JSON string, integer or boolean type.</p>
<h3>Immediates</h3>
<dl>
<dd>
<pre><i>STRING</i>
<i>NUMBER</i>
<i>BOOLEAN</i></pre>
</dl>
<p> Immediate expressions are typically used for constant values. For strings, there are two special cases: </p>
<p> <code>@STRING</code></p>
<dl>
<dd>The remaining part is taken as set name to create a set reference.</dl>
<p> <code>\</code>*</p>
<dl>
<dd>Construct a wildcard expression.</dl>
<h3>Lists</h3>
<dl>
<dd>
<pre><i>ARRAY</i></pre>
</dl>
<p> List expressions are constructed by plain arrays containing of an arbitrary number of expressions.</p>
<h3>Concat</h3>
<dl>
<dd>
<pre><code>{ &quot;concat&quot;:</code> <i>CONCAT</i> <code>}</code>
<i>CONCAT</i> := <code>[</code> <i>EXPRESSION_LIST</i> <code>]</code>
<i>EXPRESSION_LIST</i> := <i>EXPRESSION</i> [<code>,</code> <i>EXPRESSION_LIST</i> ]</pre>
</dl>
<p> Concatenate several expressions.</p>
<h3>Set</h3>
<dl>
<dd>
<pre><code>{ &quot;set&quot;:</code> <i>SET</i> <code>}</code>
<i>SET</i> := <i>EXPRESSION</i> | <code>[</code> <i>EXPRESSION_LIST</i> <code>]</code></pre>
</dl>
<p> This object constructs an anonymous set. For mappings, an array of arrays with exactly two elements is expected.</p>
<h3>Map</h3>
<dl>
<dd>
<pre><code>{ &quot;map&quot;: {
 &quot;key&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;data&quot;:</code> <i>EXPRESSION</i>
<code>}}</code></pre>
</dl>
<p> Map a key to a value. </p>
<p> <code>key</code></p>
<dl>
<dd>Map key.</dl>
<p> <code>data</code></p>
<dl>
<dd>Mapping expression consisting of value/target pairs.</dl>
<h3>Prefix</h3>
<dl>
<dd>
<pre><code>{ &quot;prefix&quot;: {
 &quot;addr&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;len&quot;:</code> <i>NUMBER</i>
<code>}}</code></pre>
</dl>
<p> Construct an IPv4 or IPv6 prefix consisting of address part in <code>addr</code> and prefix length in <code>len</code>.</p>
<h3>Range</h3>
<dl>
<dd>
<pre><code>{ &quot;range&quot;: [</code> <i>EXPRESSION</i> <code>,</code> <i>EXPRESSION</i> <code>] }</code></pre>
</dl>
<p> Construct a range of values. The first array item denotes the lower boundary, the second one the upper boundary.</p>
<h3>Payload</h3>
<dl>
<dd>
<pre><code>{ &quot;payload&quot;: {
 &quot;base&quot;:</code> <i>BASE</i><code>,
 &quot;offset&quot;:</code> <i>NUMBER</i><code>,
 &quot;len&quot;:</code> <i>NUMBER</i>
<code>}}</code>
<code>{ &quot;payload&quot;: {
 &quot;protocol&quot;:</code> <i>STRING</i><code>,
 &quot;field&quot;:</code> <i>STRING</i>
<code>}}</code>
<i>BASE</i> := <code>&quot;ll&quot;</code> | <code>&quot;nh&quot;</code> | <code>&quot;th&quot;</code></pre>
</dl>
<p> Construct a payload expression, i.e. a reference to a certain part of packet data. The first form creates a raw payload expression to point at a random number (<code>len</code>) of bytes at a certain offset (<code>offset</code>) from a given reference point (<code>base</code>). The following <code>base</code> values are accepted: </p>
<p> <code>&quot;ll&quot;</code></p>
<dl>
<dd>The offset is relative to Link Layer header start offset.</dl>
<p> <code>&quot;nh&quot;</code></p>
<dl>
<dd>The offset is relative to Network Layer header start offset.</dl>
<p> <code>&quot;th&quot;</code></p>
<dl>
<dd>The offset is relative to Transport Layer header start offset.</dl>
<p> The second form allows to reference a field by name (<code>field</code>) in a named packet header (<code>protocol</code>).</p>
<h3>Exthdr</h3>
<dl>
<dd>
<pre><code>{ &quot;exthdr&quot;: {
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;field&quot;:</code> <i>STRING</i><code>,
 &quot;offset&quot;:</code> <i>NUMBER</i>
<code>}}</code></pre>
</dl>
<p> Create a reference to a field (<code>field</code>) in an IPv6 extension header (<code>name</code>). <code>offset</code> is used only for <code>rt0</code> protocol. </p>
<p> If the <code>field</code> property is not given, the expression is to be used as a header existence check in a <code>match</code> statement with a boolean on the right hand side.</p>
<h3>Tcp Option</h3>
<dl>
<dd>
<pre><code>{ &quot;tcp option&quot;: {
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;field&quot;:</code> <i>STRING</i>
<code>}}</code></pre>
</dl>
<p> Create a reference to a field (<code>field</code>) of a TCP option header (<code>name</code>). </p>
<p> If the <code>field</code> property is not given, the expression is to be used as a TCP option existence check in a <code>match</code> statement with a boolean on the right hand side.</p>
<h3>Sctp Chunk</h3>
<dl>
<dd>
<pre><code>{ &quot;sctp chunk&quot;: {
 &quot;name&quot;:</code> <i>STRING</i><code>,
 &quot;field&quot;:</code> <i>STRING</i>
<code>}}</code></pre>
</dl>
<p> Create a reference to a field (<code>field</code>) of an SCTP chunk (<code>name</code>). </p>
<p> If the <code>field</code> property is not given, the expression is to be used as an SCTP chunk existence check in a <code>match</code> statement with a boolean on the right hand side.</p>
<h3>Meta</h3>
<dl>
<dd>
<pre><code>{ &quot;meta&quot;: {
 &quot;key&quot;:</code> <i>META_KEY</i>
<code>}}</code>
<i>META_KEY</i> := <code>&quot;length&quot;</code> | <code>&quot;protocol&quot;</code> | <code>&quot;priority&quot;</code> | <code>&quot;random&quot;</code> | <code>&quot;mark&quot;</code> |
 <code>&quot;iif&quot;</code> | <code>&quot;iifname&quot;</code> | <code>&quot;iiftype&quot;</code> | <code>&quot;oif&quot;</code> | <code>&quot;oifname&quot;</code> |
 <code>&quot;oiftype&quot;</code> | <code>&quot;skuid&quot;</code> | <code>&quot;skgid&quot;</code> | <code>&quot;nftrace&quot;</code> |
 <code>&quot;rtclassid&quot;</code> | <code>&quot;ibriport&quot;</code> | <code>&quot;obriport&quot;</code> | <code>&quot;ibridgename&quot;</code> |
 <code>&quot;obridgename&quot;</code> | <code>&quot;pkttype&quot;</code> | <code>&quot;cpu&quot;</code> | <code>&quot;iifgroup&quot;</code> |
 <code>&quot;oifgroup&quot;</code> | <code>&quot;cgroup&quot;</code> | <code>&quot;nfproto&quot;</code> | <code>&quot;l4proto&quot;</code> |
 <code>&quot;secpath&quot;</code></pre>
</dl>
<p> Create a reference to packet meta data.</p>
<h3>Rt</h3>
<dl>
<dd>
<pre><code>{ &quot;rt&quot;: {
 &quot;key&quot;:</code> <i>RT_KEY</i><code>,
 &quot;family&quot;:</code> <i>RT_FAMILY</i>
<code>}}</code>
<i>RT_KEY</i> := <code>&quot;classid&quot;</code> | <code>&quot;nexthop&quot;</code> | <code>&quot;mtu&quot;</code>
<i>RT_FAMILY</i> := <code>&quot;ip&quot;</code> | <code>&quot;ip6&quot;</code></pre>
</dl>
<p> Create a reference to packet routing data. </p>
<p> The <code>family</code> property is optional and defaults to unspecified.</p>
<h3>Ct</h3>
<dl>
<dd>
<pre><code>{ &quot;ct&quot;: {
 &quot;key&quot;:</code> <i>STRING</i><code>,
 &quot;family&quot;:</code> <i>CT_FAMILY</i><code>,
 &quot;dir&quot;:</code> <i>CT_DIRECTION</i>
<code>}}</code>
<i>CT_FAMILY</i> := <code>&quot;ip&quot;</code> | <code>&quot;ip6&quot;</code>
<i>CT_DIRECTION</i> := <code>&quot;original&quot;</code> | <code>&quot;reply&quot;</code></pre>
</dl>
<p> Create a reference to packet conntrack data. </p>
<p> Some CT keys do not support a direction. In this case, <code>dir</code> must not be given.</p>
<h3>Numgen</h3>
<dl>
<dd>
<pre><code>{ &quot;numgen&quot;: {
 &quot;mode&quot;:</code> <i>NG_MODE</i><code>,
 &quot;mod&quot;:</code> <i>NUMBER</i><code>,
 &quot;offset&quot;:</code> <i>NUMBER</i>
<code>}}</code>
<i>NG_MODE</i> := <code>&quot;inc&quot;</code> | <code>&quot;random&quot;</code></pre>
</dl>
<p> Create a number generator. </p>
<p> The <code>offset</code> property is optional and defaults to 0.</p>
<h3>Hash</h3>
<dl>
<dd>
<pre><code>{ &quot;jhash&quot;: {
 &quot;mod&quot;:</code> <i>NUMBER</i><code>,
 &quot;offset&quot;:</code> <i>NUMBER</i><code>,
 &quot;expr&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;seed&quot;:</code> <i>NUMBER</i>
<code>}}</code>
<code>{ &quot;symhash&quot;: {
 &quot;mod&quot;:</code> <i>NUMBER</i><code>,
 &quot;offset&quot;:</code> <i>NUMBER</i>
<code>}}</code></pre>
</dl>
<p> Hash packet data. </p>
<p> The <code>offset</code> and <code>seed</code> properties are optional and default to 0.</p>
<h3>Fib</h3>
<dl>
<dd>
<pre><code>{ &quot;fib&quot;: {
 &quot;result&quot;:</code> <i>FIB_RESULT</i><code>,
 &quot;flags&quot;:</code> <i>FIB_FLAGS</i>
<code>}}</code>
<i>FIB_RESULT</i> := <code>&quot;oif&quot;</code> | <code>&quot;oifname&quot;</code> | <code>&quot;type&quot;</code>
<i>FIB_FLAGS</i> := <i>FIB_FLAG</i> | <code>[</code> <i>FIB_FLAG_LIST</i> <code>]</code>
<i>FIB_FLAG_LIST</i> := <i>FIB_FLAG</i> [<code>,</code> <i>FIB_FLAG_LIST</i> ]
<i>FIB_FLAG</i> := <code>&quot;saddr&quot;</code> | <code>&quot;daddr&quot;</code> | <code>&quot;mark&quot;</code> | <code>&quot;iif&quot;</code> | <code>&quot;oif&quot;</code></pre>
</dl>
<p> Perform kernel Forwarding Information Base lookups.</p>
<h3>Binary Operation</h3>
<dl>
<dd>
<pre><code>{ &quot;|&quot;: [</code> <i>EXPRESSION</i><code>,</code> <i>EXPRESSION</i> <code>] }</code>
<code>{ &quot;^&quot;: [</code> <i>EXPRESSION</i><code>,</code> <i>EXPRESSION</i> <code>] }</code>
<code>{ &quot;&amp;&quot;: [</code> <i>EXPRESSION</i><code>,</code> <i>EXPRESSION</i> <code>] }</code>
<code>{ &quot;</code><code>&lt;&lt;</code><code>&quot;: [</code> <i>EXPRESSION</i><code>,</code> <i>EXPRESSION</i> <code>] }</code>
<code>{ &quot;&gt;&gt;&quot;: [</code> <i>EXPRESSION</i><code>,</code> <i>EXPRESSION</i> <code>] }</code></pre>
</dl>
<p> All binary operations expect an array of exactly two expressions, of which the first element denotes the left hand side and the second one the right hand side.</p>
<h3>Verdict</h3>
<dl>
<dd>
<pre><code>{ &quot;accept&quot;: null }</code>
<code>{ &quot;drop&quot;: null }</code>
<code>{ &quot;continue&quot;: null }</code>
<code>{ &quot;return&quot;: null }</code>
<code>{ &quot;jump&quot;: { &quot;target&quot;:</code> <i>STRING</i> <code>}}</code>
<code>{ &quot;goto&quot;: { &quot;target&quot;:</code> <i>STRING</i> <code>}}</code></pre>
</dl>
<p> Same as the <code>verdict</code> statement, but for use in verdict maps. </p>
<p> <code>jump</code> and <code>goto</code> verdicts expect a target chain name.</p>
<h3>Elem</h3>
<dl>
<dd>
<pre><code>{ &quot;elem&quot;: {
 &quot;val&quot;:</code> <i>EXPRESSION</i><code>,
 &quot;timeout&quot;:</code> <i>NUMBER</i><code>,
 &quot;expires&quot;:</code> <i>NUMBER</i><code>,
 &quot;comment&quot;:</code> <i>STRING</i>
<code>}}</code></pre>
</dl>
<p> Explicitly set element object, in case <code>timeout</code>, <code>expires</code> or <code>comment</code> are desired. Otherwise, it may be replaced by the value of <code>val</code>.</p>
<h3>Socket</h3>
<dl>
<dd>
<pre><code>{ &quot;socket&quot;: {
 &quot;key&quot;:</code> <i>SOCKET_KEY</i>
<code>}}</code>
<i>SOCKET_KEY</i> := <code>&quot;transparent&quot;</code></pre>
</dl>
<p> Construct a reference to packet&#8217;s socket.</p>
<h3>Osf</h3>
<dl>
<dd>
<pre><code>{ &quot;osf&quot;: {
 &quot;key&quot;:</code> <i>OSF_KEY</i><code>,
 &quot;ttl&quot;:</code> <i>OSF_TTL</i>
<code>}}</code>
<i>OSF_KEY</i> := <code>&quot;name&quot;</code>
<i>OSF_TTL</i> := <code>&quot;loose&quot;</code> | <code>&quot;skip&quot;</code></pre>
</dl>
<p> Perform OS fingerprinting. This expression is typically used in the LHS of a <code>match</code> statement. </p>
<p> <code>key</code></p>
<dl>
<dd>Which part of the fingerprint info to match against. At this point, only the OS name is supported.</dl>
<p> <code>ttl</code></p>
<dl>
<dd>Define how the packet&#8217;s TTL value is to be matched. This property is optional. If omitted, the TTL value has to match exactly. A value of <code>loose</code> accepts TTL values less than the fingerprint one. A value of <code>skip</code> omits TTL value comparison entirely.</dl>
<h2>Author</h2>
<p><code>Phil Sutter</code> &lt;phil [at] nwl.cc&gt;</p>
<dl>
<dd>Author.</dl>
