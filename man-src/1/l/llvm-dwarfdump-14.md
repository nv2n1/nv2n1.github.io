---

title: "llvm-dwarfdump-14(1)"
name: "llvm-dwarfdump-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-dwarfdump-14/"
description: "llvm-dwarfdump – manual page for llvm-dwarfdump 14"
---

<p> llvm-dwarfdump &#8211; manual page for llvm-dwarfdump 14 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: pretty-print DWARF debug information in object files and debug info archives. </p>
<p> USAGE: llvm-dwarfdump [options] &lt;input object files or .dSYM bundles&gt; </p>
<p> OPTIONS: </p>
<p> Color Options:</p>
<dl>
<dt> <code>&#8211;color</code> &#8211; Use colors in output (default=autodetect)</dt></dl>
<dd>Generic Options:</dd>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</dt>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</dt>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program</dt></dl>
<dd>Section-specific Dump Options: These control which sections are dumped. Where applicable these parameters take an optional =&lt;offset&gt; argument to dump only the entry at the specified offset.</dd>
<dl>
<dt> <code>-a</code> &#8211; Alias for <code>&#8211;all</code></dt>
<dt> <code>&#8211;all</code> &#8211; Dump all debug info sections</dt>
<dt> <code>&#8211;apple-names</code> &#8211; Dump the .apple_names section</dt>
<dt> <code>&#8211;apple-namespaces</code> &#8211; Dump the .apple_namespaces section</dt>
<dt> <code>&#8211;apple-objc</code> &#8211; Dump the .apple_objc section</dt>
<dt> <code>&#8211;apple-types</code> &#8211; Dump the .apple_types section</dt>
<dt> <code>&#8211;debug-abbrev</code> &#8211; Dump the .debug_abbrev section</dt>
<dt> <code>&#8211;debug-addr</code> &#8211; Dump the .debug_addr section</dt>
<dt> <code>&#8211;debug-aranges</code> &#8211; Dump the .debug_aranges section</dt>
<dt> <code>&#8211;debug-cu-index</code> &#8211; Dump the .debug_cu_index section</dt>
<dt> <code>&#8211;debug-frame[=</code>&lt;offset&gt;] &#8211; Dump the .debug_frame section</dt>
<dt> <code>&#8211;debug-gnu-pubnames</code> &#8211; Dump the .debug_gnu_pubnames section</dt>
<dt> <code>&#8211;debug-gnu-pubtypes</code> &#8211; Dump the .debug_gnu_pubtypes section</dt>
<dt> <code>&#8211;debug-info[=</code>&lt;offset&gt;] &#8211; Dump the .debug_info section</dt>
<dt> <code>&#8211;debug-line[=</code>&lt;offset&gt;] &#8211; Dump the .debug_line section</dt>
<dt> <code>&#8211;debug-line-str</code> &#8211; Dump the .debug_line_str section</dt>
<dt> <code>&#8211;debug-loc[=</code>&lt;offset&gt;] &#8211; Dump the .debug_loc section</dt>
<dt> <code>&#8211;debug-loclists[=</code>&lt;offset&gt;] &#8211; Dump the .debug_loclists section</dt>
<dt> <code>&#8211;debug-macro</code> &#8211; Dump the .debug_macro section</dt>
<dt> <code>&#8211;debug-names</code> &#8211; Dump the .debug_names section</dt>
<dt> <code>&#8211;debug-pubnames</code> &#8211; Dump the .debug_pubnames section</dt>
<dt> <code>&#8211;debug-pubtypes</code> &#8211; Dump the .debug_pubtypes section</dt>
<dt> <code>&#8211;debug-ranges</code> &#8211; Dump the .debug_ranges section</dt>
<dt> <code>&#8211;debug-rnglists</code> &#8211; Dump the .debug_rnglists section</dt>
<dt> <code>&#8211;debug-str</code> &#8211; Dump the .debug_str section</dt>
<dt> <code>&#8211;debug-str-offsets</code> &#8211; Dump the .debug_str_offsets section</dt>
<dt> <code>&#8211;debug-tu-index</code> &#8211; Dump the .debug_tu_index section</dt>
<dt> <code>&#8211;debug-types[=</code>&lt;offset&gt;] &#8211; Dump the .debug_types section</dt>
<dt> <code>&#8211;eh-frame</code> &#8211; Alias for <code>&#8211;debug-frame</code></dt>
<dt> <code>&#8211;gdb-index</code> &#8211; Dump the .gdb_index section</dt></dl>
<dd>Specific Options:</dd>
<dl>
<dt> <code>-F</code> &#8211; Alias for <code>&#8211;show-form</code>.</dt>
<dt> <code>&#8211;arch=</code>&lt;string&gt; &#8211; Dump debug information for the specified CPU architecture only. Architectures may be specified by name or by number. This option can be specified multiple times, once for each desired architecture.</dt>
<dt> <code>-c</code> &#8211; Alias for <code>&#8211;show-children</code>.</dt>
<dt> <code>&#8211;diff</code> &#8211; Emit diff-friendly output by omitting offsets and addresses.</dt>
<dt> <code>-f</code> &#8211; Alias for <code>&#8211;find</code>.</dt>
<dt> <code>&#8211;find=</code>&lt;name&gt; &#8211; Search for the exact match for &lt;name&gt; in the accelerator tables and print the matching debug information entries. When no accelerator tables are available, the slower but more complete <code>-name</code> option can be used instead.</dt>
<dt> <code>-i</code> &#8211; Alias for <code>&#8211;ignore-case</code>.</dt>
<dt> <code>&#8211;ignore-case</code> &#8211; Ignore case distinctions when using <code>&#8211;name</code>.</dt>
<dt> <code>&#8211;lookup=</code>&lt;address&gt; &#8211; Lookup &lt;address&gt; in the debug information and print out any available file, function, block and line table details.</dt>
<dt> <code>-n</code> &#8211; Alias for <code>&#8211;name</code></dt>
<dt><code>&#8211;name=</code>&lt;pattern&gt; &#8211; Find and print all debug info entries whose name (DW_AT_name attribute) matches the exact text in &lt;pattern&gt;.</dt>
<dd>
</dd><dd>When used with the the <code>-regex</code> option &lt;pattern&gt; is interpreted as a regular expression.</dd>
<dt> <code>-o=</code>&lt;filename&gt; &#8211; Redirect output to the specified file.</dt>
<dt> <code>-p</code> &#8211; Alias for <code>&#8211;show-parents</code>.</dt>
<dt> <code>&#8211;parent-recurse-depth=</code>&lt;N&gt; &#8211; Only recurse to a depth of N when displaying parents of debug info entries.</dt>
<dt> <code>&#8211;quiet</code> &#8211; Use with <code>-verify</code> to not emit to STDOUT.</dt>
<dt> <code>-r</code> &#8211; Alias for <code>&#8211;recurse-depth</code>.</dt>
<dt> <code>&#8211;recurse-depth=</code>&lt;N&gt; &#8211; Only recurse to a depth of N when displaying children of debug info entries.</dt>
<dt> <code>&#8211;regex</code> &#8211; Treat any &lt;pattern&gt; strings as regular expressions when searching with <code>&#8211;name</code>. If <code>&#8211;ignore-case</code> is also specified, the regular expression becomes case-insensitive.</dt>
<dt> <code>&#8211;show-children</code> &#8211; Show a debug info entry&#8217;s children when selectively printing entries.</dt>
<dt> <code>&#8211;show-form</code> &#8211; Show DWARF form types after the DWARF attribute types.</dt>
<dt> <code>&#8211;show-parents</code> &#8211; Show a debug info entry&#8217;s parents when selectively printing entries.</dt>
<dt> <code>&#8211;show-section-sizes</code> &#8211; Show the sizes of all debug sections, expressed in bytes.</dt>
<dt> <code>&#8211;statistics</code> &#8211; Emit JSON-formatted debug info quality metrics.</dt>
<dt> <code>&#8211;summarize-types</code> &#8211; Abbreviate the description of type unit entries.</dt>
<dt> <code>-u</code> &#8211; Alias for <code>&#8211;uuid</code>.</dt>
<dt> <code>&#8211;uuid</code> &#8211; Show the UUID for each architecture.</dt>
<dt> <code>-v</code> &#8211; Alias for <code>&#8211;verbose</code>.</dt>
<dt> <code>&#8211;verbose</code> &#8211; Print more low-level encoding details.</dt>
<dt> <code>&#8211;verify</code> &#8211; Verify the DWARF debug info.</dt>
<dt> <code>-x</code> &#8211; Alias for <code>&#8211;regex</code></dt></dl>
<dd>Pass @FILE as argument to read options from FILE. </dd>
