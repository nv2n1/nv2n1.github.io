---
title: "read_module_node(3)"
name: "read_module_node"
section: "3"
letter: "r"
url: "/docs/linux/man/3-read_module_node/"
description: "init_mib, add_mibdir, init_mib_internals, add_module_replacement, read_module, read_mib, read_all_mibs, read_objid, read_module_node, get_module_node, snmp_set_mib_warnings, snmp_set_save_descripti..."
---

<p>init_mib, add_mibdir, init_mib_internals, add_module_replacement, read_module, read_mib, read_all_mibs, read_objid, read_module_node, get_module_node, snmp_set_mib_warnings, snmp_set_save_descriptions, shutdown_mib, print_mib, print_variable, fprint_variable, snprint_variable, sprint_realloc_variable, print_value, fprint_value, snprint_value, sprint_realloc_value, print_objid, fprint_objid, snprint_objid, sprint_realloc_objid, print_description, fprint_description &#8211; mib_api functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/mib_api.h&gt;
void init_mib(void);

int add_mibdir(const char *dirname);

int add_module_replacement(const char *old_module, const char *new_module, const char *tag, int len);

void init_mib_internals(void);

struct tree *read_module(const char *name);

struct tree *read_mib(const char *filename);

struct tree *read_all_mibs(void);
void shutdown_mib(void);
void print_mib(FILE *fp);
int read_objid(const char *input, oid *output, size_t *out_len);

int get_module_node(const char *name, const char *module, oid *objid, size_t *objidlen);
void print_variable(const oid *objid, size_t objidlen, const netsnmp_variable_list *variable);

void fprint_variable(FILE *fp, const oid *objid, size_t objidlen, const netsnmp_variable_list *variable);

int snprint_variable(char *buf, size_t len, const oid *objid, size_t objidlen, const netsnmp_variable_list *variable);

int sprint_realloc_variable(u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const oid *objid, size_t objidlen, const netsnmp_variable_list *variable);
void print_value(oid *objid, size_t objidlen, const netsnmp_variable_list *variable)

    void fprint_value(FILE *fp, const oid *objid, size_t objidlen, const netsnmp_variable_list *variable);

int snprint_value(char *buf, size_t len, const oid *objid, size_t objidlen, const netsnmp_variable_list *variable);

int sprint_realloc_value(u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const oid *objid, size_t objidlen, const netsnmp_variable_list *variable);
void print_objid(const oid *objid, size_t objidlen);

void fprint_objid(FILE *fp, const oid *objid, size_t objidlen);

int snprint_objid(char *buf, size_t len, const oid *objid, size_t objidlen);

int sprint_realloc_objid(u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const oid *objid, size_t objidlen);
void print_description(oid *objid, size_t objidlen, int width);

void fprint_description(FILE *fp, const oid *objid, size_t objidlen, int width);
void snmp_set_mib_warnings(int level);

void snmp_set_save_descriptions(int save);
</code></pre>
<h2>Description</h2>
<p>The functions dealing with MIB modules fall into four groups. Those dealing with initialisation and shutdown, those that read in and parse MIB files, those that search the MIB tree, and various output routines.</p>
<h3>Initialisation and Shutdown</h3>
<p><code>init_mib</code> is a convenience function that handles all calls to <code>add_mibdir</code>, <code>read_module</code> and <code>read_mib</code> for standard applications. It should be called before any other routine that manipulates or accesses the MIB tree. This routine sets up various internal structures, as well as reading in the default MIB modules, as detailed below. </p>
<p> <code>add_mibdir</code> is used to define the range of directory locations which are searched for files containing MIB modules (one module per file). By default, this will be set to the directory <i>/usr/share/mibs</i> but this can be overridden by setting the environment variable <i>MIBDIRS</i> to a (colon-separated) list of directories to search. Note that this does not actually load the MIB modules located in that directory, but is an initialisation step to make them available. This function returns a count of files found in the directory, or a -1 if there is an error. </p>
<p> <code>init_mib_internals</code> sets up the internal structures, preparatory to reading in MIB modules. It should be called after all calls to <code>add_mibdir</code>, and before and calls to <code>read_module</code>. This is called automatically if <code>init_mib</code> is used. </p>
<p> <code>shutdown_mib</code> will clear the information that was gathered by <code>read_module</code>, <code>add_mibdir</code> and <code>add_module_replacement</code>. It is strongly recommended that one does not invoke <code>shutdown_mib</code> while there are SNMP sessions being actively managed.</p>
<h3>Reading and Parsing MIBs</h3>
<p><code>add_module_replacement</code> can be used to allow new MIB modules to obsolete older ones, without needing to amend the imports clauses of other modules. It takes the names of the old and new modules, together with an indication of which portions of the old module are affected.</p>
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
<td> always (the old module is a strict subset of the new)
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
<p> It can also be used to handle errors in the module identifiers used in MIB import clauses (such as referring to <i>RFC1213</i> instead of <i>RFC1213-MIB</i>). </p>
<p> <code>read_module</code> locates and parses the module specified, together with any modules that it imports from, and adds the contents of these modules to the active MIB tree. Note that <code>add_mibdir</code> must first be called to add the directory containing the file with the module definition, if this is not in the standard path.<br />
 By default, the following MIB modules will be loaded: IP-MIB, IF-MIB, TCP-MIB, UDP-MIB, SNMPv2-MIB, RFC1213-MIB, UCD-SNMP-MIB. This can be overridden by setting the environment variable <i>MIBS</i> to a (colon-separated) list of modules to load. If this variable starts with a plus character, then the specified modules are added to the default list. Otherwise only those modules listed are loaded (together with any others they import from). If <i>MIBS</i> is set to <i>ALL</i>, <code>read_all_mibs</code> is called to load all the MIB files found in all the specified <i>MIBDIRS</i>. </p>
<p> <code>read_mib</code> parses the file specified, together with any modules that it imports from, and adds the contents to the active MIB tree. Such a file can contain more then one module, though care must be taken that any imports occur earlier in the file, if they are not to be read from the installed modules. Note that the file specified does not need to be in any of the directories initialised by <code>add_mibdir</code> (or the default setup), though any imported modules do.<br />
 The environment variable <i>MIBFILES</i> can be set to a (colon-separated) list of files containing MIBs to load. </p>
<p> <code>read_objid</code> takes a string containing a textual version of an object identifier (in either numeric or descriptor form), and transforms this into the corresponding list of sub-identifiers. This is returned in the <i>output</i> parameter, with the number of sub-identifiers returned via <i>out_len</i>. When called, <i>out_len</i> must hold the maximum length of the <i>output</i> array. If multiple object identifiers are being processed, then this length should be reset before each call. This function returns a value of 1 if it succeeds in parsing the string and 0 otherwise.</p>
<h3>Searching the MIB Tree</h3>
<p><code>get_module_node</code> takes a descriptor and the name of a module, and returns the corresponding oid list, in the same way as <code>read_objid</code> above.<br />
 If the module name is specified as &quot;ANY&quot;, then this routine will assume that the descriptor given is unique within the tree, and will return the matching entry. If this assumption is invalid, then the behaviour as to which variable is returned is implementation dependent.</p>
<h3>Output</h3>
<p><code>print_mib</code> will print out a representation of the currently active MIB tree to the specified FILE pointer. </p>
<p> <code>print_variable</code> will take an object identifier (as returned by <code>read_objid</code> or <code>get_module_node</code>) and an instance of such a variable, and prints to the standard output the textual form of the object identifier together with the value of the variable. <code>fprint_variable</code> does the same, but prints to the FILE pointer specified by the initial parameter.<br />
 <code>snprint_variable</code> prints the same information into the buffer pointed to by <i>buf</i> which is of length <i>len</i> and returns either the number of characters printed, or -1 if the buffer was not large enough. In the latter case, <i>buf</i> will typically contained a truncated version of the information (but this behaviour is not guaranteed). This function replaces the obsolete function <code>sprint_variable</code>.<br />
 <code>sprint_realloc_variable</code> is the low-level function used to implement all these functions. It prints to a specified offset in a string buffer. The <i>buf</i> parameter points to a pointer to that buffer; <i>buf_len</i> points to a variable holding the current size of that buffer, and <i>out_len</i> points to a variable holding the offset to which to print. <i>out_len</i> will be updated to hold the offset of the character following the last one added to the buffer. If <i>allow_realloc</i> is 1, the buffer will be dynamically expanded, as necessary, to hold the output; the variables pointed to by <i>buf</i> and <i>buf_len</i> will be updated. If <i>allow_realloc</i> is 0, the buffer will not be dynamically expanded. <code>sprint_realloc_variable</code> returns 0 if <i>allow_realloc</i> is 1 and an attempt to allocate memory to expand the buffer fails, or if <i>allow_realloc</i> is 0 and the output wouldn&#8217;t fit in the buffer. Otherwise it returns 1. When using this function you should be careful to call <code><a href="/docs/linux/man/3-free/">free</a></code>(3) on <i>*buf</i> when you have finished with it. </p>
<p> <code>print_value</code>, <code>fprint_value</code>, <code>snprint_value</code> and <code>sprint_realloc_value</code> do the same as the equivalent <code>print_variable</code> routines, but only displaying the value of the variable, without the corresponding object identifier. </p>
<p> <code>print_objid</code>, <code>fprint_objid</code>, <code>snprint_objid</code>, and <code>sprint_realloc_objid</code> take an object identifier (without an accompanying variable instance) and print out the textual representation. </p>
<p> <code>print_description</code> and <code>fprint_description</code> take an object identifier (as for <code>print_objid</code> above) and print out the associated DESCRIPTION clause. The <i>width</i> argument gives the number of subidentifiers of an OID, e.g., .1.3.6 is composed of 3 subidentifiers. </p>
<p> Note that there are no corresponding routines <code>snprint_description</code> or <code>sprint_realloc_description</code>. By default the parser does not save descriptions since they may be huge. In order to be able to print them, you must call <code><a href="/docs/linux/man/1-snmp_set_save_descriptions/">snmp_set_save_descriptions</a>(1)</code>. </p>
<p> In general the parser is silent about what strangenesses it sees in the MIB files. To get warnings reported, call <code>snmp_set_mib_warnings</code> with a <i>level</i> of 1 (or 2 for even more warnings).</p>
<h2>Environment Variables</h2>
<dl>
<dt>MIBDIRS</p>
<dd>A colon separated list of directories to search for MIB modules. Default: /usr/share/snmp/mibs</p>
<dt>MIBFILES</p>
<dd>A colon separated list of files to load. Default: (none)</p>
<dt>MIBS</p>
<dd>A colon separated list of MIB modules to load. Default: IP-MIB:IF-MIB:TCP-MIB:UDP-MIB:SNMPv2-MIB:RFC1213-MIB:UCD-SNMP-MIB.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-snmp_api/">snmp_api</a></code>(3) </p>
