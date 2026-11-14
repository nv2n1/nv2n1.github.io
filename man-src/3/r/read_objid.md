---
title: "read_objid(3)"
name: "read_objid"
section: "3"
letter: "r"
url: "/docs/linux/man/3-read_objid/"
description: "add_mibdir, netsnmp_init_mib, shutdown_mib, netsnmp_read_module, read_mib, read_all_mibs, add_module_replacement, snmp_set_mib_errors, snmp_set_mib_warnings, snmp_set_save_descriptions, read_objid,..."
---

<p>add_mibdir, netsnmp_init_mib, shutdown_mib, netsnmp_read_module, read_mib, read_all_mibs, add_module_replacement, snmp_set_mib_errors, snmp_set_mib_warnings, snmp_set_save_descriptions, read_objid, snmp_parse_oid, get_module_node, print_mib, print_objid, fprint_objid, snprint_objid, print_description, fprint_description, snprint_description &#8211; netsnmp_mib_api functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/mib_api.h&gt;</code></pre>
<h3>Initialisation and Shutdown</h3>
<p><code>int add_mibdir(const char *</code><i>dirname</i><code>);</code> void netsnmp_init_mib(void);</p>
<p>void shutdown_mib(void);</p>
<p>Reading and Parsing MIBs</p>
<p>    struct tree *<br />
    netsnmp_read_module(const char *name);</p>
<p>struct tree *read_mib(const char *filename);</p>
<p>struct tree *read_all_mibs(void);<br />
int add_module_replacement(const char *old_module,</p>
<p>                           const char *new_module,</p>
<p>                           const char *tag, int len); <code>void snmp_set_mib_warnings(int </code><i>level</i><code>);</code><br />
 <code>void snmp_set_mib_errors(int </code><i>level</i><code>);</code><br />
 <code>void snmp_set_save_descriptions(int </code><i>save</i><code>);</code></p>
<h3>Searching the MIB Tree</h3>
<p><code>int read_objid(const char *</code><i>input</i><code>,</code><br />
 <code> oid *</code><i>objid</i><code>, size_t *</code><i>objidlen</i><code>);</code><br />
 <code>oid *snmp_parse_oid(const char *</code><i>input</i><code>,</code><br />
 <code> oid *</code><i>objid</i><code>, size_t *</code><i>objidlen</i><code>);</code><br />
 <code>int get_module_node(const char *</code><i>name</i><code>, const char *</code><i>module</i><code>,</code><br />
 <code> oid *</code><i>objid</i><code>, size_t *</code><i>objidlen</i><code>);</code></p>
<h3>Output</h3>
<pre><code>void print_mib(FILE *fp);
void print_objid(const oid *objid, size_t objidlen);

void fprint_objid(FILE *fp,

                  const oid *objid, size_t objidlen);

int snprint_objid(char *buf, size_t len,

                  const oid *objid, size_t objidlen);
void print_description(const oid *objid, size_t objidlen, int width);

void fprint_description(FILE *fp,

                        const oid *objid, size_t objidlen, int width);

int snprint_description(char *buf, size_t len,

                        const oid *objid, size_t objidlen, int width);
</code></pre>
<h2>Description</h2>
<p>The functions dealing with MIB modules fall into four groups &#8211; those dealing with initialisation and shutdown, with reading in and parsing MIB files, with searching the MIB tree, and output routines.</p>
<h3>Initialisation and Shutdown</h3>
<p><code>add_mibdir</code> is used to add the specified directory to the path of locations which are searched for files containing MIB modules. Note that this does not actually load the MIB modules located in that directory, but is simply an initialisation step to make them available to <code>netsnmp_read_module</code>. This function returns a count of files found in the directory, or a -1 if there is an error. It should be called <i>before</i> invoking <code>netsnmp_init_mib</code>. </p>
<p> <code>netsnmp_init_mib</code> configures the MIB directory search path (using <code>add_mibdir</code> ), sets up the internal MIB framework, and then loads the appropriate MIB modules (using <code>netsnmp_read_module</code> and <code>read_mib</code>). See the ENVIRONMENTAL VARIABLES section for details.<br />
 It should be called before any other routine that manipulates or accesses the MIB tree (but after any additional <code>add_mibdir</code> calls). </p>
<p> <code>shutdown_mib</code> will clear the information that was gathered by <code>netsnmp_read_module</code>, <code>add_mibdir</code> and <code>add_module_replacement</code>. It is strongly recommended that one does not invoke <code>shutdown_mib</code> while there are SNMP sessions being actively managed.</p>
<h3>Reading and Parsing MIBs</h3>
<p><code>netsnmp_read_module</code> takes the name of a MIB module (which need not be the same as the name of the file that contains the module), locates this within the configured list of MIB directories, and loads the definitions from the module into the active MIB tree. It also loads any MIB modules listed in the IMPORTS clause of this module. </p>
<p> <code>read_mib</code> is similar, but takes the name of the file containing the MIB module. Note that this file need not be located within the MIB directory search list (although any modules listed in the IMPORTS clause do). </p>
<p> <code>read_all_mibs</code> will read in all the MIB modules found on the MIB directory search list. </p>
<p> In general the parser is silent about what strangenesses it sees in the MIB files. To get warnings reported, call <code>snmp_set_mib_warnings</code> with a <i>level</i> of 1 (or 2 for even more warnings). </p>
<p> <code>add_module_replacement</code> can be used to allow new MIB modules to obsolete older ones, without needing to amend the IMPORTS clauses of other modules. It takes the names of the old and new modules, together with an indication of which portions of the old module are affected.</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>tag </code></td>
<td><code> len </code></td>
<td><code> load the new module when:</code>
</td>
</tr>
<tr VALIGN=top>
<td>NULL </td>
<td> 0 </td>
<td> always (the old module is a strict subset of
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr></td>
<td> </td>
<td> the new)
</td>
</tr>
<tr VALIGN=top>
<td>name </td>
<td> 0 </td>
<td> for the given tag only
</td>
</tr>
<tr VALIGN=top>
<td>name </td>
<td> non-0 </td>
<td> for any identifier with this prefix
</td>
</tr>
</table>
</dl>
<p> It can also be used to handle errors in the module identifiers used in MIB IMPORTS clauses (such as referring to <i>RFC1213</i> instead of <i>RFC1213-MIB</i>).</p>
<h3>Searching the MIB Tree</h3>
<p><code>read_objid</code> takes a string containing a textual version of an object identifier (in either numeric or descriptor form), and transforms this into the corresponding list of sub-identifiers. This is returned in the <i>output</i> parameter, with the number of sub-identifiers returned via <i>out_len</i>. When called, <i>out_len</i> must hold the maximum length of the <i>output</i> array. If multiple object identifiers are being processed, then this length should be reset before each call. This function returns a value of 1 if it succeeds in parsing the string and 0 otherwise. </p>
<p> <code>snmp_parse_oid</code> is similar, but returns a pointer to the parsed OID buffer (or NULL). </p>
<p> <code>get_module_node</code> takes a descriptor and the name of a module, and returns the corresponding oid list, in the same way as <code>read_objid</code> above.<br />
 If the module name is specified as &quot;ANY&quot;, then this routine will assume that the descriptor given is unique within the tree, and will return the matching entry. If this assumption is invalid, then the behaviour as to which variable is returned is implementation dependent.</p>
<h3>Output</h3>
<p><code>print_mib</code> will print out a representation of the currently active MIB tree to the specified FILE pointer. </p>
<p> <code>print_objid</code> will take an object identifier (as returned by <code>read_objid</code>, <code>snmp_parse_oid</code> or <code>get_module_node</code>), and prints the textual form of this OID to the standard output. </p>
<p> <code>fprint_objid</code> does the same, but prints to the FILE pointer specified by the initial parameter. </p>
<p> <code>snprint_objid</code> prints the same information into the buffer pointed to by <i>buf</i> which is of length <i>len</i>. It returns the number of characters printed, or -1 if the buffer was not large enough. In the latter case, <i>buf</i> will typically contain a truncated version of the information (but this behaviour is not guaranteed). </p>
<p> <code>print_description</code>, <code>fprint_description</code>, and <code>snprint_description</code> take a similar object identifier and print out a version of the MIB definition for that object, together with the full OID. The <i>width</i> argument controls how the OID is layed out. </p>
<p> By default the parser does not save descriptions since they may be huge. In order to be able to print them, it is necessary to invoke <code><a href="/docs/linux/man/1-snmp_set_save_descriptions/">snmp_set_save_descriptions</a>(1)</code><i>before</i> calling <code>init_mib</code> (or similar).</p>
<h2>Environment Variables</h2>
<p>The main use of environmental variables with respect to these API calls is to configure which MIB modules should be loaded, and where they are located.</p>
<dl>
<dt>MIBDIRS</p>
<dd>A colon separated list of directories to search for MIB modules.<br />
 Default: /usr/share/snmp/mibs<br />
 Used by <code>init_mib</code>, <code>netsnmp_read_module</code>, <code>read_all_mibs</code> and (implicitly) by <code>read_mib</code>.</p>
<dt>MIBS</p>
<dd>A colon separated list of MIB modules to load.<br />
 The default list of modules will depend on how the Net-SNMP software was originally compiled, but is typically: IP-MIB:IF-MIB:TCP-MIB:UDP-MIB:SNMPv2-MIB:RFC1213-MIB: UCD-SNMP-MIB:HOST-RESOURCES-MIB</p>
<dd>If the value of the <code>MIBS</code> environmental variable starts with a &#8216;+&#8217; character, then these MIB modules will be added to the default list. Otherwise these modules (plus any that they IMPORT from) will be loaded <i>instead</i> of the default list.</p>
<dd>If the <code>MIBS</code> environmental variable has the value <code>ALL</code> then <code>read_all_mibs</code> will be called to load the full collection of all available MIB modules.</p>
<dd>Used by <code>init_mib</code> only.</p>
<dt>MIBFILES</p>
<dd>A colon separated list of files to load.<br />
 Default: (none)<br />
 Used by <code>init_mib</code> only.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-snmp_api/">snmp_api</a></code>(3), <code><a href="/docs/linux/man/3-output_api/">output_api</a></code>(3) </p>
