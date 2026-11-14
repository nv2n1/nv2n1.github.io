---
title: "lvmreport(7)"
name: "lvmreport"
section: "7"
letter: "l"
url: "/docs/linux/man/7-lvmreport/"
description: "lvmreport — LVM reporting and related features"
---

<p>lvmreport &#8212; LVM reporting and related features</p>
<h2>Description</h2>
<p>LVM uses single reporting infrastructure that sets standard on LVM command&#8217;s output and it provides wide range of configuration settings and command line options to customize report and filter the report&#8217;s output. </p>
<h2>Categorization based on reporting facility</h2>
<p>Based on functionality, commands which make use of the reporting infrastructure are divided in two groups:</p>
<dl>
<dt><code>Report-oriented</p>
<dd>These commands inform about current LVM state and their primary role is to display this information in compendious way. To make a distinction, we will name this report as main report</code>. The set of report-only commands include: pvs, vgs, lvs, pvdisplay, vgdisplay, lvdisplay, lvm devtypes, lvm fullreport. For further information about main report, see <code>main report specifics</code>.</p>
<dt><code>Processing-oriented</p>
<dd>These commands are responsible for changing LVM state and they do not contain any main report as identified for report-oriented commands, they only perform some kind of processing. The set of processing-oriented commands includes: pvcreate, vgcreate, lvcreate, pvchange, vgchange, lvchange, pvremove, vgremove, lvremove, pvresize, vgextend, vgreduce, lvextend, lvreduce, lvresize, lvrename, pvscan, vgscan, lvscan, pvmove, vgcfgbackup, vgck, vgconvert, vgexport, vgimport, vgmknodes. </p>
<p> If enabled, so called log report</code> is either displayed solely (for processing-oriented commands) or in addition to main report (for report-oriented commands). The log report contains a log of operations, messages and per-object status with complete object identification collected during LVM command execution. See <code>log report specifics</code> for more information about this report type. </p>
</dl>
<h2>Terms</h2>
<p>When describing reporting functionality and features in this text, we will use terms <code>row</code> and <code>column</code>. By row we mean series of values reported for single entity (for example single PV, VG or LV). Each value from the row then belongs to a column of certain type. The columns have <code>column headings</code> which are short descriptions for the columns. The columns are referenced by <code>column names</code>. Please note that this text is also using term <code>field</code> interchangeably with the term <code>column</code>. Most of the time the term columns is abbreviated as <code>col</code> in configuration.</p>
<h2>Common report configuration settings and command line options</h2>
<p>There are common configuration settings and command line options which apply to both <code>main report</code> and <code>log report</code>. Following lists contain all of them, separated into groups based on their use. </p>
<dl>
<dd><code>Common configuration settings:</code> </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Changing report output format, composition and other output modifiers:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>global/units</p>
<dt>&#8211;</p>
<dd>global/suffix</p>
<dt>&#8211;</p>
<dd>report/output_format</p>
<dt>&#8211;</p>
<dd>report/compact_output</p>
<dt>&#8211;</p>
<dd>report/compact_output_cols</p>
<dt>&#8211;</p>
<dd>report/aligned</p>
<dt>&#8211;</p>
<dd>report/headings</p>
<dt>&#8211;</p>
<dd>report/separator</p>
<dt>&#8211;</p>
<dd>report/list_item_separator</p>
<dt>&#8211;</p>
<dd>report/prefixes</p>
<dt>&#8211;</p>
<dd>report/quoted</p>
<dt>&#8211;</p>
<dd>report/columns_as_rows</p>
<dt>&#8211;</p>
<dd>report/binary_values_as_numeric</p>
<dt>&#8211;</p>
<dd>report/time_format</p>
<dt>&#8211;</p>
<dd>report/mark_hidden_devices</p>
<dt>&#8211;</p>
<dd>report/two_word_unknown_device</dl>
</dl>
<dt>&bull;</p>
<dd>Special settings</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>report/buffered</dl>
</dl>
</dl>
</dl>
</dl>
<p> This document does not describe these settings in more detail &#8211; if you need detailed information, including values which are accepted for the settings, please run <code>lvmconfig &#8211;type default &#8211;withcomments &lt;setting&gt;</code>. There are more configuration settings in addition to the common set listed above, but they are specific to either <code>main report</code> or <code>log report</code>, see <code>main report specifics</code> and <code>log report specifics</code> for these settings. Besides configuring reports globally by using configuration settings, there are also command line options you can use to extend, override or further specify the report configuration. </p>
<dl>
<dd><code>Common command line options:</code> </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Definition of the set set of fields to use</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>&#8211;options|-o FieldSet<br />
 Field set to use. See <code>main report specifics</code> and <code>log report specifics</code> for information about field sets configured with global configuratin settings that this option overrides.</p>
<dt>&#8211;</p>
<dd>&#8211;options|-o+ FieldSet<br />
 Fields to include to current field set. See <code>main report specifics</code>&nbsp;and <code>log report specifics</code> for information about field sets configured with global configuration settings that this option extends.</p>
<dt>&#8211;</p>
<dd>&#8211;options|-o- FieldSet<br />
 Fields to exclude from current field set. See <code>main report specifics</code> and <code>log report specifics</code> for information about field sets configured with global configuration settings that this option reduces.</p>
<dt>&#8211;</p>
<dd>&#8211;options|-o# FieldSet<br />
 Compaction of unused fields. Overrides report/compact_output_cols configuration setting.</dl>
</dl>
<dt>&bull;</p>
<dd>Sorting</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>&#8211;sort|-O+ FieldSet<br />
 Fields to sort by in ascending order. See <code>main report specifics</code> and <code>log report specifics</code> for information about field sets configured with global configuration settings that this option overrides.</p>
<dt>&#8211;</p>
<dd>&#8211;sort|-O- FieldSet<br />
 Fields to sort by in descending order. See <code>main report specifics</code> and <code>log report specifics</code> for information about fields sets configured with global configuration settings that this options overrides.</dl>
</dl>
<dt>&bull;</p>
<dd>Selection</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>&#8211;select|-S Selection<br />
 Define selection criteria for report output. For <code>log report</code>, this also overrides log/command_log_selection configuration setting, see also <code>log report specifics</code>.</dl>
</dl>
<dt>&bull;</p>
<dd>Changing output format and composition</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>&#8211;reportformat<br />
 Overrides report/output_format configuration setting.</p>
<dt>&#8211;</p>
<dd>&#8211;aligned<br />
 Overrides report/aligned configuration setting.</p>
<dt>&#8211;</p>
<dd>&#8211;binary<br />
 Overrides report/binary_values_as_numeric configuration setting.</p>
<dt>&#8211;</p>
<dd>&#8211;nameprefixes<br />
 Overrides report/prefixes configuration setting.</p>
<dt>&#8211;</p>
<dd>&#8211;noheadings<br />
 Overrides report/noheadings configuration setting.</p>
<dt>&#8211;</p>
<dd>&#8211;nosuffix<br />
 Overrides global/suffix configuration setting.</p>
<dt>&#8211;</p>
<dd>&#8211;rows<br />
 Overrides report/columns_as_rows configuration setting.</p>
<dt>&#8211;</p>
<dd>&#8211;separator<br />
 Overrides report/separator configuration setting.</p>
<dt>&#8211;</p>
<dd>&#8211;units<br />
 Overrides global/units configuration setting.</p>
<dt>&#8211;</p>
<dd>&#8211;unquoted<br />
 Overrides report/quoted configuration setting.</dl>
</dl>
<dt>&bull;</p>
<dd>Special options</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>&#8211;configreport <code>ReportName</code><br />
 This defines the <code>ReportName</code> for which any subsequent -o&#8211;columns, -O&#8211;sort or -S&#8211;select applies to. See also <code>main report specifics</code> and <code>log report specifics</code> for possible <code>ReportName</code> values.</p>
<dt>&#8211;</p>
<dd>&#8211;logonly<br />
 When an LVM command contains both <code>main report</code> and <code>log report</code>, this option suppresses the <code>main report</code> output and it causes the <code>log report</code> output to be displayed only.</p>
<dt>&#8211;</p>
<dd>&#8211;unbuffered<br />
 Overrides report/bufffered configuration setting.</dl>
</dl>
</dl>
</dl>
</dl>
<p> The <code>FieldSet</code> mentioned in the lists above is a set of field names where each field name is delimited by &quot;,&quot; character. Field set definition, sorting and selection may be repeated on command line (-o+/-o- includes/excludes fields to/from current list, for all the other repeatable options, the last value typed for the option on the command line is used). The <code>Selection</code> is a string with <code>selection criteria</code>, see also <code>Selection</code> paragraph below for more information about constructing these criteria.</p>
<h2>Main report specifics</h2>
<p>The <code>main report</code> currently encompasses these distinct subtypes, referenced by their name &#8211; <code>ReportName</code> as listed below. The command in parenthesis is representative command that uses the main report subtype by default. Each subtype has its own configuration setting for global field set definition as well as sort field definition (listed below each individual <code>ReportName</code>): </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>pv</code> representing report about Physical Volumes (<code>pvs</code>)</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>report/pvs_cols</p>
<dt>&#8211;</p>
<dd>report/pvs_sort</dl>
</dl>
<dt>&bull;</p>
<dd><code>pvseg</code> representing report about Physical Volume Segments (<code>pvs &#8211;segments</code>)</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>report/pvseg_cols</p>
<dt>&#8211;</p>
<dd>report/pvseg_sort</dl>
</dl>
<dt>&bull;</p>
<dd><code>vg</code> representing report about Volume Groups (<code>vgs</code>)</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>report/vgs_cols</p>
<dt>&#8211;</p>
<dd>report/vgs_sort</dl>
</dl>
<dt>&bull;</p>
<dd><code>lv</code> representing report about Logical Volumes (<code>lvs</code>)</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>report/lvs_cols</p>
<dt>&#8211;</p>
<dd>report/lvs_sort</dl>
</dl>
<dt>&bull;</p>
<dd><code>seg</code> representing report about Logical Volume Segments (<code>lvs &#8211;segments</code>)</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>report/segs_cols</p>
<dt>&#8211;</p>
<dd>report/segs_sort</dl>
</dl>
<dt>&bull;</p>
<dd><code>full</code> representing report combining all of the above as a whole (<code>lvm fullreport</code>)</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>report/pvs_cols_full</p>
<dt>&#8211;</p>
<dd>report/pvs_sort_full</p>
<dt>&#8211;</p>
<dd>report/pvsegs_cols_full</p>
<dt>&#8211;</p>
<dd>report/pvseg_sort_full</p>
<dt>&#8211;</p>
<dd>report/vgs_cols_full</p>
<dt>&#8211;</p>
<dd>report/vgs_sort_full</p>
<dt>&#8211;</p>
<dd>report/lvs_cols_full</p>
<dt>&#8211;</p>
<dd>report/lvs_sort_full</p>
<dt>&#8211;</p>
<dd>report/segs_cols_full</p>
<dt>&#8211;</p>
<dd>report/segs_sort_full</dl>
</dl>
<dt>&bull;</p>
<dd><code>devtype</code> representing report about device types (<code>lvm devtypes</code>)</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>report/devtypes_cols</p>
<dt>&#8211;</p>
<dd>report/devtypes_sort</dl>
</dl>
</dl>
</dl>
<p> Use <code>pvs, vgs, lvs -o help</code> or <code>lvm devtypes -o help</code> to get complete list of fields that you can use for main report. The list of fields in the help output is separated in groups based on which report type they belong to. Note that LVM can change final report type used if fields from different groups are combined together. Some of these combinations are not allowed in which case LVM will issue an error. </p>
<p> For all main report subtypes except <code>full</code>, it&#8217;s not necessary to use <code>&#8211;configreport ReportName</code> to denote which report any subsequent <code>-o, -O or -S</code> option applies to as they always apply to the single main report type. Currently, <code>lvm fullreport</code> is the only command that includes more than one <code>main report</code> subtype. Therefore, the &#8211;configreport is particularly suitable for the full report if you need to configure each of its subreports in a different way.</p>
<h2>Log report specifics</h2>
<p>You can enable log report with <code>log/report_command_log</code> configuration setting &#8211; this functionality is disabled by default. The <code>log report</code> contains a log collected during LVM command execution and then the log is displayed just like any other report known from main report. There is only one log report subtype as shown below together with related configuration settings for fields, sorting and selection: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>log</code> representing log report</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>log/command_log_cols</p>
<dt>&#8211;</p>
<dd>log/command_log_sort</p>
<dt>&#8211;</p>
<dd>log/command_log_selection</dl>
</dl>
</dl>
</dl>
<p> You always need to use <code>&#8211;configreport log</code> together with <code>-o&#8211;options, -O&#8211;sort or -S&#8211;selection</code> to override configuration settings directly on command line for <code>log report</code>. When compared to <code>main report</code>, in addition to usual configuration settings for report fields and sorting, the <code>log report</code> has also configuration option for selection &#8211; <code>report/command_log_selection</code>. This configuration setting is provided for convenience so it&#8217;s not necessary to use <code>-S&#8211;select</code> on command line each time an LVM command is executed and we need the same selection criteria to be applied for <code>log report</code>. Default selection criteria used for <code>log report</code> are <code>log/command_log_selection=&quot;!(log_type=status &amp;&amp; message=success)&quot;</code>. This means that, by default, <code>log report</code> doesn&#8217;t display status messages about successful operation and it displays only rows with error, warning, print-type messages and messages about failure states (for more information, see <code>log report content</code> below). </p>
<p> <code>Log report coverage</code><br />
 Currently, when running LVM commands directly (not in LVM shell), the log report covers command&#8217;s <code>processing stage</code> which is the moment when LVM entities are iterated and processed one by one. It does not cover any command initialization nor command finalization stage. If there is any message issued out of log report&#8217;s coverage range, such message goes directly to output, bypassing the <code>log report</code>. By default, that is <code>standard error output</code> for error and warning messages and <code>standard output</code> for common print-like messages. </p>
<p> When running LVM commands in <code>LVM shell</code>, the log report covers the whole LVM command&#8217;s execution, including command&#8217;s <code>processing</code> as well as <code>initialization</code> and <code>finalization stage</code>. So from this point of view, the log report coverage is complete for executed LVM commands. Note that there are still a few moments when LVM shell needs to initialize itself before it even enters the main loop in which it executes LVM commands. Also, there is a moment when <code>LVM shell</code> needs to prepare <code>log report</code> properly for next command executed in the shell and then, after the command&#8217;s run, the shell needs to display the log report for that recently executed command. If there is a failure or any other message issued during this time, the LVM will bypass <code>log report</code> and display messages on output directly. </p>
<p> For these reasons and for completeness, it&#8217;s not possible to rely fully on <code>log report</code> as the only indicator of LVM command&#8217;s status and the only place where all messages issued during LVM command execution are collected. You always need to check whether the command has not failed out of log report&#8217;s range by checking the non-report output too. </p>
<p> To help with this, LVM can separate output which you can then redirect to any <code>custom file descriptor</code> that you prepare before running an LVM command or LVM shell and then you make LVM to use these file descriptors for different kinds of output by defining environment variables with file descriptor numbers. See also <code>LVM_OUT_FD</code>, <code>LVM_ERR_FD</code> and <code>LVM_REPORT_FD</code> environment variable description in <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) man page. </p>
<p> Also note that, by default, reports use the same file descriptor as common print-like messages, which is <code>standard output</code>. If you plan to use <code>log report</code> in your scripts or any external tool, you should use <code>LVM_OUT_FD</code>, <code>LVM_ERR_FD</code> and <code>LVM_REPORT_FD</code> to separate all output types to different file descriptors. For example, with bash, that would be: </p>
<dl>
<dd>LVM_OUT_FD=3 LVM_ERR_FD=4 LVM_REPORT_FD=5 &lt;lvm command&gt; 3&gt;out_file 4&gt;err_file 5&gt;report_file</dl>
<p> Where the &lt;lvm_command&gt; is either direct LVM command or LVM shell. You can collect all three types of output in particular files then. </p>
<p> <code>Log report content</code><br />
 Each item in the log report consists of these set of fields providing various information: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Basic information (mandatory):</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>log_seq_num<br />
 Item sequence number. The sequence number is unique for each log item and it increases in the order of the log items as they appeared during LVM command execution. </p>
<dt>&#8211;</p>
<dd>log_type<br />
 Type of log for the item. Currently, these types are used:</p>
<dl>
<dd>
<dl>
<dd><code>status</code> for any status information that is logged</p>
<dd><code>print</code> for any common message printed while the log is collected</p>
<dd><code>error</code> for any error message printed while the log is collected</p>
<dd><code>warn</code> for any warning message printed while the log is collected</dl>
</dl>
<dt>&#8211;</p>
<dd>log_context<br />
 Context of the log for the item. Currently, two contexts are identified:</p>
<dl>
<dd>
<dl>
<dd><code>shell</code> for the log collected in the outermost code before and after executing concrete LVM commands</p>
<dd><code>processing</code> for the log collected while processing LVM entities during LVM command execution</dl>
</dl>
</dl>
</dl>
<dt>&bull;</p>
<dd>Message (mandatory):</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>log_message<br />
 Any message associated with current item. For <code>status</code> log type, the message contains either <code>success</code> or <code>failure</code> denoting current state. For <code>print</code>, <code>error</code> and <code>warn</code> log types, the message contains the exact message of that type that got issued.</dl>
</dl>
<dt>&bull;</p>
<dd>Object information (used only if applicable):</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>log_object_type field<br />
 Type of the object processed. Currently, these object types are recognized:</p>
<dl>
<dd>
<dl>
<dd><code>cmd</code> for command as a whole</p>
<dd><code>orphan</code> for processing group of PVs not in any VG yet</p>
<dd><code>pv</code> for PV processing</p>
<dd><code>label</code> for direct PV label processing (without VG metadata)</p>
<dd><code>vg</code> for VG processing</p>
<dd><code>lv</code> for LV processing</dl>
</dl>
<dt>&#8211;</p>
<dd>log_object_name<br />
 Name of the object processed. </p>
<dt>&#8211;</p>
<dd>log_object_id<br />
 ID of the object processed. </p>
<dt>&#8211;</p>
<dd>log_object_group<br />
 A group where the processed object belongs to. </p>
<dt>&#8211;</p>
<dd>log_object_group_id<br />
 An ID of a group where the processed object belongs to.</dl>
</dl>
<dt>&bull;</p>
<dd>Numeric status (used only if applicable)</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>log_errno<br />
 Error number associated with current item.</p>
<dt>&#8211;</p>
<dd>log_ret_code<br />
 Rreturn code associated with current item.</dl>
</dl>
</dl>
</dl>
<p> You can also run <code>&lt;lvm_command&gt; &#8211;configreport log -o help</code> to to display complete list of fields that you may use for the <code>log report</code>.</p>
<h2>Selection</h2>
<p>Selection is used for a report to display only rows that match <code>selection criteria</code>. All rows are displayed with the additional <code>selected</code> field (<code>-o selected</code>) displaying 1 if the row matches the <i>Selection</i> and 0 otherwise. The <code>selection criteria</code> are a set of <code>statements</code> combined by <code>logical and grouping operators</code>. The <code>statement</code> consists of a <code>field</code> name for which a set of valid <code>values</code> is defined using <code>comparison operators</code>. For complete list of fields names that you can use in selection, see the output of <code>&lt;lvm_command&gt; -S help</code>. The help output also contains type of values that each field displays enclosed in brackets. </p>
<p> <code>List of operators recognized in selection criteria</code></p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Comparison operators (cmp_op)</p>
<dl>
<dd>
<dl>
<dd><code>=~</code> matching regular expression.</p>
<dd><code>!~</code> not matching regular expression.</p>
<dd><code>= </code> equal to.</p>
<dd><code>!=</code> not equal to.</p>
<dd><code>&gt;=</code> greater than or equal to.</p>
<dd><code>&gt; </code> greater than</p>
<dd><code>&lt;=</code> less than or equal to.</p>
<dd><code>&lt; </code> less than.</dl>
</dl>
<dt>&bull;</p>
<dd>Binary logical operators (cmp_log)</p>
<dl>
<dd>
<dl>
<dd><code>&amp;&amp;</code> all fields must match</p>
<dd><code>, </code> all fields must match</p>
<dd><code>||</code> at least one field must match</p>
<dd><code># </code> at least one field must match</dl>
</dl>
<dt>&bull;</p>
<dd>Unary logical operators</p>
<dl>
<dd>
<dl>
<dd><code>! </code> logical negation</dl>
</dl>
<dt>&bull;</p>
<dd>Grouping operators</p>
<dl>
<dd>
<dl>
<dd><code>( </code> left parenthesis</p>
<dd><code>) </code> right parenthesis</p>
<dd><code>[ </code> list start</p>
<dd><code>] </code> list end</p>
<dd><code>{ </code> list subset start</p>
<dd><code>} </code> list subset end</dl>
</dl>
</dl>
</dl>
<p> <code>Field types and selection operands</code><br />
 Field type restricts the set of operators and values that you may use with the field when defining selection criteria. You can see field type for each field if you run <code>&lt;lvm command&gt; -S help</code> where you can find the type name enclosed in square brackets. Currently, LVM recognizes these field types in reports: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>string</code> for set of characters (for each string field type, you can use either string or regular expression &#8211; regex for the value used in selection criteria)</p>
<dt>&bull;</p>
<dd><code>string list</code> for set of strings</p>
<dt>&bull;</p>
<dd><code>number</code> for integer value</p>
<dt>&bull;</p>
<dd><code>size</code> for integer or floating point number with size unit suffix (see also <code><a href="/docs/linux/man/8-lvcreate/">lvcreate</a></code>(8) man page and description for &quot;-L&#8211;size&quot; option for the list of recognized suffixes)</p>
<dt>&bull;</p>
<dd><code>percent</code> for floating point number with or without &quot;%&quot; suffix (e.g. 50 or 50%)</p>
<dt>&bull;</p>
<dd><code>time</code> for time values</dl>
</dl>
<p> When using <code>string list</code> in selection criteria, there are several ways how LVM can match string list fields from report, depending on what list grouping operator is used and what item separator is used within that set of items. Also, note that order of items does not matter here. </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>matching the set strictly</code> where all items must match &#8211; use [ ], e.g. [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]</p>
<dt>&bull;</p>
<dd><code>matching a subset of the set</code> &#8211; use { } with &quot;,&quot; or &quot;&amp;&amp;&quot; as item delimiter, e.g. {&quot;a&quot;,&quot;b&quot;,&quot;c&quot;}</p>
<dt>&bull;</p>
<dd><code>matching an intersection with the set</code> &#8211; use { } with &quot;#&quot; or &quot;||&quot; as item delimiter, e.g. {&quot;a&quot; || &quot;b&quot; || &quot;c&quot;}</dl>
</dl>
<p> When using <code>time</code> in your selection criteria, LVM can recognize various time formats using standard, absolute or freeform expressions. For examples demonstrating time expressions in selection criteria, see <code>EXAMPLES</code> section. </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>Standard time format</code> </p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>date</p>
<dl>
<dd>
<dl>
<dd>YYYY-MM-DD</p>
<dd>YYYY-MM, auto DD=1</p>
<dd>YYYY, auto MM=01 and DD=01</dl>
</dl>
<dt>&#8211;</p>
<dd>time</p>
<dl>
<dd>
<dl>
<dd>hh:mm:ss</p>
<dd>hh:mm, auto ss=0</p>
<dd>hh, auto mm=0, auto ss=0</dl>
</dl>
<dt>&#8211;</p>
<dd>timezone</p>
<dl>
<dd>
<dl>
<dd>+hh:mm or -hh:mm</p>
<dd>+hh or -hh</dl>
</dl>
<p> The full date/time specification is YYYY-MM-DD hh:mm:ss. Users are able to leave date/time parts from right to left. Whenever these parts are left out, a range is assumed automatically with second granularity. For example: </p>
<dl>
<dd>
<dl>
<dd>&quot;2015-07-07 9:51&quot; means range of &quot;2015-07-07 9:51:00&quot; &#8211; &quot;2015-07-07 9:51:59&quot;.</p>
<dd>&quot;2015-07&quot; means range of &quot;2015-07-01 0:00:00&quot; &#8211; &quot;2015-07-31 23:59:59&quot;</p>
<dd>&quot;2015&quot; means range of &quot;2015-01-01 0:00:00&quot; &#8211; &quot;2015-12-31 23:59:59&quot;</dl>
</dl>
</dl>
</dl>
<dt>&bull;</p>
<dd><code>Absolute time format</code> </p>
<p> Absolute time is defined as number of seconds since the Epoch (1970:01:01 00:00 +00:00). </p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>@seconds</dl>
</dl>
<dt>&bull;</p>
<dd><code>Freeform time format</code></p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>weekday names (&quot;Sunday&quot; &#8211; &quot;Saturday&quot; or abbreviated as &quot;Sun&quot; &#8211; &quot;Sat&quot;)</p>
<dt>&#8211;</p>
<dd>labels for points in time (&quot;noon&quot;, &quot;midnight&quot;)</p>
<dt>&#8211;</p>
<dd>labels for a day relative to current day (&quot;today&quot;, &quot;yesterday&quot;)</p>
<dt>&#8211;</p>
<dd>points back in time with relative offset from today (N is a number)</p>
<dl>
<dd>
<dl>
<dd>&quot;N&quot; &quot;seconds&quot; / &quot;minutes&quot; / &quot;hours&quot; / &quot;days&quot; / &quot;weeks&quot; / &quot;years&quot; &quot;ago&quot;</p>
<dd>&quot;N&quot; &quot;secs&quot; / &quot;mins&quot; / &quot;hrs&quot; &#8230; &quot;ago&quot;</p>
<dd>&quot;N&quot; &quot;s&quot; / &quot;m&quot; / &quot;h&quot; &#8230; &quot;ago&quot;</dl>
</dl>
<dt>&#8211;</p>
<dd>time specification either in hh:mm:ss format or with AM/PM suffixes</p>
<dt>&#8211;</p>
<dd>month names (&quot;January&quot; &#8211; &quot;December&quot; or abbreviated as &quot;Jan&quot; &#8211; &quot;Dec&quot;)</dl>
</dl>
</dl>
</dl>
<p> <code>Informal grammar specification</code></p>
<dl>
<dd>
<dl>
<dd><code>STATEMENT</code> = <code>column</code> cmp_op <code>VALUE</code> | <code>STATEMENT</code> log_op <code>STATEMENT</code> | <code>(STATEMENT)</code> | <code>!(STATEMENT)</code></p>
<dd><code>VALUE</code> = <code>[VALUE</code> log_op <code>VALUE]</code><br />
 For list-based types: string list. Matches strictly. The log_op must always be of one type within the whole list value.</p>
<dd><code>VALUE</code> = <code>{VALUE</code> log_op <code>VALUE}</code><br />
 For list-based types: string list. Matches a subset. The log_op must always be of one type within the whole list value.</p>
<dd><code>VALUE</code> = <code>value</code><br />
 For scalar types: number, size, percent, string (or string regex).</dl>
</dl>
<h2>Examples</h2>
<h3>Basic usage</h3>
<p>We start our examples with default configuration &#8211; <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8) is helpful command to display configuration settings which are currently used, including all configuration related to reporting. We will use it throughout examples below to display current configuration. </p>
<pre># lvmconfig --type full global/units global/suffix \
 report/output_format report/compact_output \
 report/compact_output_cols report/aligned \
 report/headings report/separator \
 report/list_item_separator report/prefixes \
 report/quoted report/columns_as_rows \
 report/binary_values_as_numeric report/time_format \
 report/mark_hidden_devices report/two_word_unknown_device \
 report/buffered
units=&quot;h&quot;
suffix=1
output_format=&quot;basic&quot;
compact_output=0
compact_output_cols=&quot;&quot;
aligned=1
headings=1
separator=&quot; &quot;
list_item_separator=&quot;,&quot;
prefixes=0
quoted=1
columns_as_rows=0
binary_values_as_numeric=0
time_format=&quot;%Y-%m-%d %T %z&quot;
mark_hidden_devices=1
two_word_unknown_device=0
buffered=1</pre>
<p>Also, we start with simple LVM layout with two PVs (/dev/sda, /dev/sdb), VG (vg) and two LVs (lvol0 and lvol1) in the VG. We display all possible reports as single commands here, see also <code><a href="/docs/linux/man/8-pvs/">pvs</a></code>(8), <code><a href="/docs/linux/man/8-vgs/">vgs</a></code>(8), <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8) man pages for more information. The field set for each report type is configured with configuration settings as we already mentioned in <code>main report specifics</code> section in this man page.  </p>
<pre># pvs
 PV VG Fmt Attr PSize PFree 
 /dev/sda vg lvm2 a-- 100.00m 88.00m
 /dev/sdb vg lvm2 a-- 100.00m 92.00m
# pvs --segments
 PV VG Fmt Attr PSize PFree Start SSize
 /dev/sda vg lvm2 a-- 100.00m 88.00m 0 1
 /dev/sda vg lvm2 a-- 100.00m 88.00m 1 1
 /dev/sda vg lvm2 a-- 100.00m 88.00m 2 1
 /dev/sda vg lvm2 a-- 100.00m 88.00m 3 22
 /dev/sdb vg lvm2 a-- 100.00m 92.00m 0 1
 /dev/sdb vg lvm2 a-- 100.00m 92.00m 1 1
 /dev/sdb vg lvm2 a-- 100.00m 92.00m 2 23
# vgs
 VG #PV #LV #SN Attr VSize VFree 
 vg 2 2 0 wz--n- 200.00m 180.00m
# lvs
 LV VG Attr LSize Pool Origin Move Log Cpy%Sync Convert
 lvol0 vg -wi-a----- 4.00m 
 lvol1 vg rwi-a-r--- 4.00m 100.00 
# lvs --segments
 LV VG Attr #Str Type SSize
 lvol0 vg -wi-a----- 1 linear 4.00m
 lvol1 vg rwi-a-r--- 2 raid1 4.00m</pre>
<p>We will use <code>report/lvs_cols</code> and <code>report/lvs_sort</code> configuration settings to define our own list of fields to use and to sort by that is different from defaults. You can do this for other reports in same manner with <code>report/{pvs,pvseg,vgs,seg}_{cols,sort}</code> configuration settings. Also note that in the example below, we don&#8217;t display the &quot;lv_time&quot; field even though we&#8217;re using it for sorting &#8211; this is allowed. </p>
<pre># lvmconfig --type full report/lvs_cols report/lvs_sort
lvs_cols=&quot;lv_name,lv_size,origin,pool_lv,copy_percent&quot;
lvs_sort=&quot;-lv_time&quot;
# lvs
 LV LSize Origin Pool Cpy%Sync
 lvol1 4.00m 100.00 
 lvol0 4.00m </pre>
<p>You can use <code>-o&#8211;options</code> command line option to override current configuration directly on command line. </p>
<pre># lvs -o lv_name,lv_size
 LV LSize
 lvol1 4.00m
 lvol0 4.00m
# lvs -o+lv_layout
 LV LSize Origin Pool Cpy%Sync Layout 
 lvol1 4.00m 100.00 raid,raid1
 lvol0 4.00m linear 
# lvs -o-origin
 LV LSize Pool Cpy%Sync
 lvol1 4.00m 100.00 
 lvol0 4.00m 
# lvs -o lv_name,lv_size,origin -o+lv_layout -o-origin -O lv_name
 LV LSize Layout 
 lvol0 4.00m linear 
 lvol1 4.00m raid,raid1</pre>
<p>You can obtain the same information with single command where all the information about PVs, PV segments, LVs and LV segments are obtained per VG under a single VG lock for consistency, see also <code><a href="/docs/linux/man/8-lvm-fullreport/">lvm-fullreport</a></code>(8) man page for more information. The fullreport has its own configuration settings to define field sets to use, similar to individual reports as displayed above, but configuration settings have &quot;_full&quot; suffix now. This way, it&#8217;s possible to configure different sets of fields to display and to sort by for individual reports as well as the full report.  </p>
<pre># lvm fullreport
 VG
 vg
 PV VG
 /dev/sda vg
 /dev/sdb vg
 LV VG
 lvol0 vg
 lvol1 vg
 PV Start SSize
 /dev/sda 0 1
 /dev/sda 1 1
 /dev/sda 2 1
 /dev/sda 3 22
 /dev/sdb 0 1
 /dev/sdb 1 1
 /dev/sdb 2 23
 LV Start SSize
 lvol0 0 4.00m
 lvol1 0 4.00m</pre>
<h3>Automatic output compaction</h3>
<p>If you look at the lvs output above, you can see that the report also contains fields for which there is no information to display (e.g. the columns under &quot;Origin&quot; and &quot;Pool&quot; heading &#8211; the &quot;origin&quot; and &quot;pool_lv&quot; fields). LVM can automatically compact report output so such fields are not included in final output. To enable this feature and to compact all fields, use <code>report/compact_output=1</code> in your configuration. </p>
<pre># lvmconfig --type full report/compact_output
compact_output=1
# lvs
 LV LSize Cpy%Sync
 lvol1 4.00m 100.00 
 lvol0 4.00m 
# lvs vg/lvol0
 LV LSize 
 lvol0 4.00m</pre>
<p>Alternatively, you can define which fields should be compacted by configuring <code>report/compact_output_cols</code> configuration setting (or <code>-o&#8211;options #</code> command line option). </p>
<pre># lvmconfig --type full report/compact_output report/compact_output_cols
compact_output=0
compact_output_cols=&quot;origin&quot;
# lvs
 LV LSize Pool Cpy%Sync
 lvol1 4.00m 100.00 
 lvol0 4.00m 
# lvs vg/lvol0
 LV LSize Pool 
 lvol0 4.00m 
# lvs -o#pool_lv 
 LV LSize Origin Cpy%Sync
 lvol1 4.00m 100.00 
 lvol0 4.00m </pre>
<p>We will use <code>report/compact_output=1</code> for subsequent examples.</p>
<h3>Further formatting options</h3>
<p>By default, LVM displays sizes in reports in human-readable form which means that the most suitable unit is used so it&#8217;s easy to read. You can use <code>report/units</code> configuration setting (or <code>&#8211;units</code> option directly on command line) and <code>report/suffix</code> configuration setting (or <code>&#8211;nosuffix</code> command line option) to change this. </p>
<pre># lvs --units b --nosuffix
 LV LSize Cpy%Sync
 lvol1 4194304 100.00 
 lvol0 4194304 </pre>
<p>If you want to configure whether report headings are displayed or not, use <code>report/headings</code> configuration settings (or <code>&#8211;noheadings</code> command line option). </p>
<pre># lvs --noheadings
 lvol1 4.00m 100.00 
 lvol0 4.00m </pre>
<p>In some cases, it may be useful to display report content as key=value pairs where key here is actually the field name. Use <code>report/prefixes</code> configuration setting (or <code>&#8211;nameprefixes</code> command line option) to switch between standard output and the key=value output. The key=value pair is the output that is suitable for use in scripts and for other tools to parse easily. Usually, you also don&#8217;t want to display headings with the output that has these key=value pairs. </p>
<pre># lvs --noheadings --nameprefixes
 LVM2_LV_NAME='lvol1' LVM2_LV_SIZE='4.00m' LVM2_COPY_PERCENT='100.00'
 LVM2_LV_NAME='lvol0' LVM2_LV_SIZE='4.00m' LVM2_COPY_PERCENT=''</pre>
<p>To define whether quotation marks in key=value pairs should be used or not, use <code>report/quoted</code> configuration setting (or <code>&#8211;unquoted</code> command line option). </p>
<pre># lvs --noheadings --nameprefixes --unquoted
 LVM2_LV_NAME=lvol1 LVM2_LV_SIZE=4.00m LVM2_COPY_PERCENT=100.00
 LVM2_LV_NAME=lvol0 LVM2_LV_SIZE=4.00m LVM2_COPY_PERCENT=</pre>
<p>For easier parsing, you can even transpose the report so each column now becomes a row in the output. This is done with <code>report/output_as_rows</code> configuration setting (or <code>&#8211;rows</code> command line option). </p>
<pre># lvs --noheadings --nameprefixes --unquoted --rows
 LVM2_LV_NAME=lvol1 LVM2_LV_NAME=lvol0
 LVM2_LV_SIZE=4.00m LVM2_LV_SIZE=4.00m
 LVM2_COPY_PERCENT=100.00 LVM2_COPY_PERCENT=</pre>
<p>Use <code>report/separator</code> configuration setting (or <code>&#8211;separator</code> command line option) to define your own field separator to use. </p>
<pre># lvs --noheadings --nameprefixes --unquoted --separator &quot; | &quot;
 LVM2_LV_NAME=lvol1 | LVM2_LV_SIZE=4.00m | LVM2_COPY_PERCENT=100.00
 LVM2_LV_NAME=lvol0 | LVM2_LV_SIZE=4.00m | LVM2_COPY_PERCENT=</pre>
<p>If you are using your own separator, the columns in the output are not aligned by default. Use <code>report/aligned</code> configuration setting (or <code>&#8211;aligned</code> command line option) for LVM to add extra spaces in report to align the output properly. </p>
<pre># lvs --separator &quot; | &quot;
 LV | LSize | Cpy%Sync
 lvol1 | 4.00m | 100.00
 lvol0 | 4.00m | 
# lvs --separator &quot; | &quot; --aligned
 LV | LSize | Cpy%Sync
 lvol1 | 4.00m | 100.00 
 lvol0 | 4.00m | </pre>
<p>Let&#8217;s display one one more field in addition (&quot;lv_tags&quot; in this example) for the lvs report output. </p>
<pre># lvs -o+lv_tags
 LV LSize Cpy%Sync LV Tags 
 lvol1 4.00m 100.00 
 lvol0 4.00m tagA,tagB</pre>
<p>The &quot;LV Tags&quot; column in the example above displays two list values, separated by &quot;,&quot; character for LV lvol0. If you need different list item separator, use <code>report/list_item_separator</code> configuration setting its definition. </p>
<pre># lvmconfig --type full report/list_item_separator
list_item_separator=&quot;;&quot;
# lvs -o+tags
 LV LSize Cpy%Sync LV Tags 
 lvol1 4.00m 100.00 
 lvol0 4.00m tagA;tagB</pre>
<p>But let&#8217;s still use the original &quot;,&quot; character for list_item_separator for subsequent examples. Format for any of time values displayed in reports can be configured with <code>report/time_format</code> configuretion setting. By default complete date and time is displayed, including timezone. </p>
<pre># lvmconfig --type full report/time_format
time_format=&quot;%Y-%m-%d %T %z&quot;
# lvs -o+time
 LV LSize Cpy%Sync CTime 
 lvol1 4.00m 100.00 2016-08-29 12:53:36 +0200 
 lvol0 4.00m 2016-08-29 10:15:17 +0200 </pre>
<p>We can change time format in similar way as we do when using <code><a href="/docs/linux/man/1-date/">date</a></code>(1) command or <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) function (<code>lvmconfig &#8211;type default &#8211;withcomments report/time_format</code> will give you complete list of available formatting options). In the example below, we decided to use %s for number of seconds since Epoch (1970-01-01 UTC). </p>
<pre># lvmconfig --type full report/time_format
time_format=&quot;%s&quot;
# lvs
 LV Attr LSize Cpy%Sync LV Tags CTime 
 lvol1 rwi-a-r--- 4.00m 100.00 1472468016 
 lvol0 -wi-a----- 4.00m tagA,tagB 1472458517 </pre>
<p>The <code>lvs</code> does not display hidden LVs by default &#8211; to include these LVs in the output, you need to use <code>-a&#8211;all</code> command line option. Names for these hidden LVs are displayed within square brackets. </p>
<pre># lvs -a
 LV LSize Cpy%Sync
 lvol1 4.00m 100.00 
 [lvol1_rimage_0] 4.00m 
 [lvol1_rmeta_0] 4.00m 
 [lvol1_rimage_1] 4.00m 
 [lvol1_rmeta_1] 4.00m 
 lvol0 4.00m </pre>
<p>You can configure LVM to display the square brackets for hidden LVs or not with <code>report/mark_hidden_devices</code> configuration setting. </p>
<pre># lvmconfig --type full report/mark_hidden_devices
mark_hidden_devices=0
# lvs -a
 LV LSize Cpy%Sync
 lvol1 4.00m 100.00 
 lvol1_rimage_0 4.00m 
 lvol1_rmeta_0 4.00m 
 lvol1_rimage_1 4.00m 
 lvol1_rmeta_1 4.00m 
 lvol0 4.00m </pre>
<p>It&#8217;s not recommended to use LV marks for hidden devices to decide whether the LV is the one to use by end users or not. Please, use &quot;lv_role&quot; field instead which can report whether the LV is &quot;public&quot; or &quot;private&quot;. The private LVs are used by LVM only and they should not be accessed directly by end users. </p>
<pre># lvs -a -o+lv_role
 LV LSize Cpy%Sync Role 
 lvol1 4.00m 100.00 public 
 lvol1_rimage_0 4.00m private,raid,image 
 lvol1_rmeta_0 4.00m private,raid,metadata
 lvol1_rimage_1 4.00m private,raid,image 
 lvol1_rmeta_1 4.00m private,raid,metadata
 lvol0 4.00m public </pre>
<p>Some of the reporting fields that LVM reports are of binary nature. For such fields, it&#8217;s either possible to display word representation of the value (this is used by default) or numeric value (0/1 or -1 in case the value is undefined). </p>
<pre># lvs -o+lv_active_locally
 LV LSize Cpy%Sync ActLocal 
 lvol1 4.00m 100.00 active locally
 lvol0 4.00m active locally</pre>
<p>We can change the way how these binary values are displayed with <code>report/binary_values_as_numeric</code> configuration setting. </p>
<pre># lvmconfig --type full report/binary_values_as_numeric
binary_values_as_numeric=1
# lvs -o+lv_active_locally
 LV LSize Cpy%Sync ActLocal 
 lvol1 4.00m 100.00 1
 lvol0 4.00m 1</pre>
<h3>Changing output format</h3>
<p>LVM can output reports in different formats &#8211; use <code>report/output_format</code> configuration setting (or <code>&#8211;reportformat</code> command line option) to swith the report output format. Currently, LVM supports <code>&quot;basic&quot;</code> (all the examples we used above used this format) and <code>&quot;JSON&quot;</code> output format. </p>
<pre># lvs -o lv_name,lv_size --reportformat json
 {
 &quot;report&quot;: [
 {
 &quot;lv&quot;: [
 {&quot;lv_name&quot;:&quot;lvol1&quot;, &quot;lv_size&quot;:&quot;4.00m&quot;},
 {&quot;lv_name&quot;:&quot;lvol0&quot;, &quot;lv_size&quot;:&quot;4.00m&quot;}
 ]
 }
 ]
 }</pre>
<p>Note that some configuration settings and command line options have no effect with certain report formats. For example, with <code>JSON</code> output, it doesn&#8217;t have any meaning to use <code>report/aligned</code> (<code>&#8211;aligned</code>), <code>report/noheadings</code> (<code>&#8211;noheadings</code>), <code>report/columns_as_rows</code> (<code>&#8211;rows</code>) or <code>report/buffered</code> (<code>&#8211;unbuffered</code>). All these configuration settings and command line options are ignored if using the <code>JSON</code> report output format.</p>
<h3>Selection</h3>
<p>If you need to select only specific rows from report, you can use LVM&#8217;s report selection feature. If you call <code>&lt;lvm_command&gt; -S help</code>, you&#8217;ll get quick help on selection. The help contains list of all fields that LVM can use in reports together with its type enclosed in square brackets. The example below contains a line from lvs -S help. </p>
<pre># lvs -S help
 ...
 lv_size - Size of LV in current units. [size]
 ...</pre>
<p>This line tells you you that the &quot;lv_size&quot; field is of &quot;size&quot; type. If you look at the bottom of the help output, you can see section about &quot;Selection operators&quot; and its &quot;Comparison operators&quot;. </p>
<pre># lvs -S help
 ...
Selection operators
-------------------
Comparison operators:
 =~ - Matching regular expression. [regex]
 !~ - Not matching regular expression. [regex]
 = - Equal to. [number, size, percent, string, string list, time]
 != - Not equal to. [number, size, percent, string, string_list, time]
 &gt;= - Greater than or equal to. [number, size, percent, time]
 &gt; - Greater than. [number, size, percent, time]
 &lt;= - Less than or equal to. [number, size, percent, time]
 &lt; - Less than. [number, size, percent, time]
since - Since specified time (same as '&gt;='). [time]
after - After specified time (same as '&gt;'). [time]
until - Until specified time (same as '&lt;='). [time]
before - Before specified time (same as '&lt;'). [time]
 ...</pre>
<p>Here you can match comparison operators that you may use with the &quot;lv_size&quot; field which is of type &quot;size&quot; &#8211; it&#8217;s =, !=, &gt;=, &gt;, &lt;= and &lt;. You can find applicable comparison operators for other fields and other field types the same way. To demostrate selection functionality in LVM, we will create more LVs in addition to lvol0 and lvol1 we used in our previous examples. </p>
<pre># lvs -o name,size,origin,snap_percent,tags,time
 LV LSize Origin Snap% LV Tags CTime 
 lvol4 4.00m lvol2 24.61 2016-09-09 16:57:44 +0200 
 lvol3 4.00m lvol2 5.08 2016-09-09 16:56:48 +0200 
 lvol2 8.00m tagA,tagC,tagD 2016-09-09 16:55:12 +0200 
 lvol1 4.00m 2016-08-29 12:53:36 +0200 
 lvol0 4.00m tagA,tagB 2016-08-29 10:15:17 +0200</pre>
<p>When selecting size and percent fields, we don&#8217;t need to use units. For sizes, default &quot;m&quot; (for MiB) is used &#8211; this is the same behaviour as already used for LVM commands when specifying sizes (e.g. lvcreate -L). For percent fields, &quot;%&quot; is assumed automatically if it&#8217;s not specified. The example below also demonstrates how several criteria can be combined together. </p>
<pre># lvs -o name,size,snap_percent -S 'size=8m'
 LV LSize 
 lvol2 8.00m
# lvs -o name,size,snap_percent -S 'size=8'
 LV LSize 
 lvol2 8.00m
# lvs -o name,size,snap_percent -S 'size &lt; 5000k'
 LV LSize Snap% 
 lvol4 4.00m 24.61 
 lvol3 4.00m 5.08 
 lvol1 4.00m 
 lvol0 4.00m 
# lvs -o name,size,snap_percent -S 'size &lt; 5000k &amp;&amp; snap_percent &gt; 20'
 LV LSize Snap% 
 lvol4 4.00m 24.61 
# lvs -o name,size,snap_percent \
 -S '(size &lt; 5000k &amp;&amp; snap_percent &gt; 20%) || name=lvol2'
 LV LSize Snap% 
 lvol4 4.00m 24.61 
 lvol2 8.00m </pre>
<p>You can also use selection together with processing-oriented commands. </p>
<pre># lvchange --addtag test -S 'size &lt; 5000k'
 Logical volume vg/lvol1 changed.
 Logical volume vg/lvol0 changed.
 Logical volume vg/lvol3 changed.
 Logical volume vg/lvol4 changed.
# lvchange --deltag test -S 'tags = test'
 Logical volume vg/lvol1 changed.
 Logical volume vg/lvol0 changed.
 Logical volume vg/lvol3 changed.
 Logical volume vg/lvol4 changed.</pre>
<p>LVM can recognize more complex values used in selection criteria for string list and time field types. For string lists, you can match whole list strictly, its subset or intersection. Let&#8217;s take &quot;lv_tags&quot; field as an example &#8211; we select only rows which contain &quot;tagA&quot; within tags field. We&#8217;re using { } to denote that we&#8217;re interested in subset that matches. If the subset has only one item, we can leave out { }. </p>
<pre># lvs -o name,tags -S 'tags={tagA}'
 LV LV Tags 
 lvol2 tagA,tagC,tagD
 lvol0 tagA,tagB 
 
# lvs -o name,tags -S 'tags=tagA'
 LV LV Tags 
 lvol2 tagA,tagC,tagD
 lvol0 tagA,tagB </pre>
<p>Depending on whether we use &quot;&amp;&amp;&quot; (or &quot;,&quot;) or &quot;||&quot; ( or &quot;#&quot;) as delimiter for items in the set we define in selection criterion for string list, we either match subset (&quot;&amp;&amp;&quot; or &quot;,&quot;) or even intersection (&quot;||&quot; or &quot;#&quot;). </p>
<pre># lvs -o name,tags -S 'tags={tagA,tagC,tagD}'
 LV LV Tags 
 lvol2 tagA,tagC,tagD
# lvs -o name,tags -S 'tags={tagA || tagC || tagD}'
 LV LV Tags 
 lvol2 tagA,tagC,tagD
 lvol0 tagA,tagB </pre>
<p>To match the complete set, use [ ] with &quot;&amp;&amp;&quot; (or &quot;,&quot;) as delimiter for items. Also note that the order in which we define items in the set is not relevant. </p>
<pre># lvs -o name,tags -S 'tags=[tagA]' 
# lvs -o name,tags -S 'tags=[tagB,tagA]'
 LV LV Tags 
 lvol0 tagA,tagB</pre>
<p>If you use [ ] with &quot;||&quot; (or &quot;#&quot;), this is exactly the same as using { }. </p>
<pre># lvs -o name,tags -S 'tags=[tagA || tagC || tagD]'
 LV LV Tags 
 lvol2 tagA,tagC,tagD
 lvol0 tagA,tagB </pre>
<p>To match a set with no items, use &quot;&quot; to denote this (note that we have output compaction enabled so the &quot;LV Tags&quot; column is not displayed in the example below because it&#8217;s blank and so it gets compacted). </p>
<pre># lvs -o name,tags -S 'tags=&quot;&quot;'
 LV 
 lvol4
 lvol3
 lvol1
# lvs -o name,tags -S 'tags!=&quot;&quot;'
 LV LV Tags 
 lvol2 tagA,tagC,tagD
 lvol0 tagA,tagB </pre>
<p>When doing selection based on time fields, we can use either standard, absolute or freeform time expressions in selection criteria. Examples below are using standard forms. </p>
<pre># lvs -o name,time
 LV CTime 
 lvol4 2016-09-09 16:57:44 +0200 
 lvol3 2016-09-09 16:56:48 +0200 
 lvol2 2016-09-09 16:55:12 +0200 
 lvol1 2016-08-29 12:53:36 +0200 
 lvol0 2016-08-29 10:15:17 +0200 
# lvs -o name,time -S 'time since &quot;2016-09-01&quot;'
 LV CTime 
 lvol4 2016-09-09 16:57:44 +0200 
 lvol3 2016-09-09 16:56:48 +0200 
 lvol2 2016-09-09 16:55:12 +0200 
# lvs -o name,time -S 'time since &quot;2016-09-09 16:56&quot;'
 LV CTime 
 lvol4 2016-09-09 16:57:44 +0200 
 lvol3 2016-09-09 16:56:48 +0200 
# lvs -o name,time -S 'time since &quot;2016-09-09 16:57:30&quot;'
 LV CTime 
 lvol4 2016-09-09 16:57:44 +0200 
# lvs -o name,time \ 
 -S 'time since &quot;2016-08-29&quot; &amp;&amp; time until &quot;2016-09-09 16:55:12&quot;'
 LV CTime 
 lvol2 2016-09-09 16:55:12 +0200 
 lvol1 2016-08-29 12:53:36 +0200 
 lvol0 2016-08-29 10:15:17 +0200 
# lvs -o name,time \
 -S 'time since &quot;2016-08-29&quot; &amp;&amp; time before &quot;2016-09-09 16:55:12&quot;'
 LV CTime 
 lvol1 2016-08-29 12:53:36 +0200 
 lvol0 2016-08-29 10:15:17 +0200 </pre>
<p>Time operators have synonyms: &quot;&gt;=&quot; for since, &quot;&lt;=&quot; for until, &quot;&gt;&quot; for &quot;after&quot; and &quot;&lt;&quot; for &quot;before&quot;. </p>
<pre># lvs -o name,time \
 -S 'time &gt;= &quot;2016-08-29&quot; &amp;&amp; time &lt;= &quot;2016-09-09 16:55:30&quot;'
 LV CTime 
 lvol2 2016-09-09 16:55:12 +0200 
 lvol1 2016-08-29 12:53:36 +0200 
 lvol0 2016-08-29 10:15:17 +0200 
# lvs -o name,time \
 -S 'time since &quot;2016-08-29&quot; &amp;&amp; time &lt; &quot;2016-09-09 16:55:12&quot;'
 LV CTime 
 lvol1 2016-08-29 12:53:36 +0200 
 lvol0 2016-08-29 10:15:17 +0200 </pre>
<p>Example below demonstrates using absolute time expression. </p>
<pre># lvs -o name,time --config report/time_format=&quot;%s&quot;
 LV CTime 
 lvol4 1473433064 
 lvol3 1473433008 
 lvol2 1473432912 
 lvol1 1472468016 
 lvol0 1472458517 
# lvs -o name,time -S 'time since @1473433008'
 LV CTime 
 lvol4 2016-09-09 16:57:44 +0200 
 lvol3 2016-09-09 16:56:48 +0200 </pre>
<p>Examples below demonstrates using freeform time expressions. </p>
<pre># lvs -o name,time -S 'time since &quot;2 weeks ago&quot;'
 LV CTime 
 lvol4 2016-09-09 16:57:44 +0200 
 lvol3 2016-09-09 16:56:48 +0200 
 lvol2 2016-09-09 16:55:12 +0200 
 lvol1 2016-08-29 12:53:36 +0200 
 lvol0 2016-08-29 10:15:17 +0200 
# lvs -o name,time -S 'time since &quot;1 week ago&quot;'
 LV CTime 
 lvol4 2016-09-09 16:57:44 +0200 
 lvol3 2016-09-09 16:56:48 +0200 
 lvol2 2016-09-09 16:55:12 +0200 
# lvs -o name,time -S 'time since &quot;2 weeks ago&quot;'
 LV CTime 
 lvol1 2016-08-29 12:53:36 +0200 
 lvol0 2016-08-29 10:15:17 +0200 
# lvs -o name,time -S 'time before &quot;1 week ago&quot;'
 LV CTime 
 lvol1 2016-08-29 12:53:36 +0200 
 lvol0 2016-08-29 10:15:17 +0200 
# lvs -o name,time -S 'time since &quot;68 hours ago&quot;'
 LV CTime 
 lvol4 2016-09-09 16:57:44 +0200 
 lvol3 2016-09-09 16:56:48 +0200 
 lvol2 2016-09-09 16:55:12 +0200 
# lvs -o name,time -S 'time since &quot;1 year 3 months ago&quot;'
 LV CTime 
 lvol4 2016-09-09 16:57:44 +0200 
 lvol3 2016-09-09 16:56:48 +0200 
 lvol2 2016-09-09 16:55:12 +0200 
 lvol1 2016-08-29 12:53:36 +0200 
 lvol0 2016-08-29 10:15:17 +0200 </pre>
<h3>Command log reporting</h3>
<p>As described in <code>categorization based on reporting facility</code> section at the beginning of this document, both <code>report-oriented</code> and <code>processing-oriented</code> LVM commands can report the command log if this is enabled with <code>log/report_command_log</code> configuration setting. Just like any other report, we can set the set of fields to display (<code>log/command_log_cols</code>) and to sort by (<code>log/command_log_sort</code>) for this report. </p>
<pre># lvmconfig --type full log/report_command_log log/command_log_cols \
 log/command_log_sort log/command_log_selection
report_command_log=1
command_log_cols=&quot;log_seq_num,log_type,log_context,log_object_type,
 log_object_name,log_object_group,log_message,
 log_errno,log_ret_code&quot;
command_log_sort=&quot;log_seq_num&quot;
command_log_selection=&quot;!(log_type=status &amp;&amp; message=success)&quot;
# lvs
 Logical Volume
 ==============
 LV LSize Cpy%Sync
 lvol1 4.00m 100.00 
 lvol0 4.00m 
 
 Command Log
 ===========
 Seq LogType Context ObjType ObjName ObjGrp Msg Errno RetCode</pre>
<p>As you can see, the command log is empty (it contains only field names). By default, LVM uses selection on the command log report and this case no row matched the selection criteria, see also <code>log report specifics</code> section in this document for more information. We&#8217;re displaying complete log report in the example below where we can see that both LVs lvol0 and lvol1 were successfully processed as well as the VG vg they are part of. </p>
<pre># lvmconfig --type full log/command_log_selection
command_log_selection=&quot;all&quot;
# lvs
 Logical Volume
 ==============
 LV LSize Cpy%Sync
 lvol1 4.00m 100.00 
 lvol0 4.00m 
 
 Command Log
 ===========
 Seq LogType Context ObjType ObjName ObjGrp Msg Errno RetCode
 1 status processing lv lvol0 vg success 0 1
 2 status processing lv lvol1 vg success 0 1
 3 status processing vg vg success 0 1
# lvchange -an vg/lvol1
 Command Log
 ===========
 Seq LogType Context ObjType ObjName ObjGrp Msg Errno RetCode
 1 status processing lv lvol1 vg success 0 1
 2 status processing vg vg success 0 1</pre>
<h3>Handling multiple reports per single command</h3>
<p>To configure the log report directly on command line, we need to use <code>&#8211;configreport</code> option before we start any <code>-o&#8211;options</code>, <code>-O&#8211;sort</code> or <code>-S&#8211;select</code> that is targeted for log report. </p>
<pre># lvs -o lv_name,lv_size --configreport log -o log_object_type, \
 log_object_name,log_message,log_ret_code
 Logical Volume
 ==============
 LV LSize
 lvol1 4.00m
 lvol0 4.00m
 
 Command Log
 ===========
 ObjType ObjName Msg RetCode
 lv lvol0 success 1
 lv lvol1 success 1
 vg vg success 1</pre>
<p>The <code>lvm fullreport</code>, with or without log report, consists of several reports &#8211; the <code>&#8211;configreport</code> is also used to target particular subreport here. Below is an extended example with <code>lvm fullreport</code> to illustrate combination of various options. The report output is in JSON format. Also, we configure &quot;vg&quot;, &quot;pvseg&quot;, &quot;seg&quot; and &quot;log&quot; subreport to contain only specified fields. For the &quot;pvseg&quot; subreport, we&#8217;re intested only in PV names having &quot;sda&quot; in their name. For the &quot;log&quot; subreport we&#8217;re intested only in log lines related to either &quot;lvol0&quot; object or object having &quot;sda&quot; in its name. Also, for the log subreport we define ordering to be based on &quot;log_object_type&quot; field. </p>
<h3>Report extensions for LVM shell</h3>
<p>As already stated in <code>log report coverage</code> paragraph under <code>log report specifics</code> in this documentation, when using <code>LVM shell</code> the <code>log report</code> coverage is wider. There&#8217;s also special command designed to query last command&#8217;s log report in the <code>LVM shell</code> &#8211; the <code>lastlog</code> command. The example below illustrates a situation where we called lvs command. After that, we inspected the log report with the <code>lastlog</code>, without any selection so all the log report is displayed on output. Then we called <code>lastlog</code> further, giving various selection criteria. Then we ran unknown LVM command &quot;abc&quot; for which the log report displays appropriate failure state. </p>
<pre># lvm
lvm&gt; lvs
 Logical Volume
 ==============
 LV LSize Cpy%Sync
 lvol1 4.00m 100.00 
 lvol0 4.00m 
 
 Command Log
 ===========
 Seq LogType Context ObjType ObjName ObjGrp Msg Errno RetCode
 1 status processing lv lvol0 vg success 0 1
 2 status processing lv lvol1 vg success 0 1
 3 status processing vg vg success 0 1
 4 status shell cmd lvs success 0 1
lvm&gt; lastlog 
 Command Log
 ===========
 Seq LogType Context ObjType ObjName ObjGrp Msg Errno RetCode
 1 status processing lv lvol0 vg success 0 1
 2 status processing lv lvol1 vg success 0 1
 3 status processing vg vg success 0 1
 4 status shell cmd lvs success 0 1
lvm&gt; lastlog -S log_object_type=lv
 Command Log
 ===========
 Seq LogType Context ObjType ObjName ObjGrp Msg Errno RetCode
 1 status processing lv lvol0 vg success 0 1
 2 status processing lv lvol1 vg success 0 1
lvm&gt; lastlog -S log_context=shell
 Command Log
 ===========
 Seq LogType Context ObjType ObjName ObjGrp Msg Errno RetCode
 4 status shell cmd lvs success 0 1
lvm&gt; abc
 Command Log
 ===========
 Seq LogType Context ObjType ObjName ObjGrp Msg Errno RetCode
 1 error shell cmd abc No such command 'abc'. Try 'help'. -1 0
 2 status shell cmd abc failure -1 2</pre>
<h2>See Also</h2>
<p><code>lvm</code> (8), <code>lvmconfig</code> (8), <code>lvm fullreport</code> (8) </p>
