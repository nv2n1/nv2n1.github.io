---
title: "tk_configureinfo(3)"
name: "tk_configureinfo"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_configureinfo/"
description: "Tk_ConfigureWidget, Tk_ConfigureInfo, Tk_ConfigureValue, Tk_FreeOptions – process configuration options for widgets"
---

<p>Tk_ConfigureWidget, Tk_ConfigureInfo, Tk_ConfigureValue, Tk_FreeOptions &#8211; process configuration options for widgets </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_ConfigureWidget(</code><i>interp, tkwin, specs, argc, argv, widgRec, flags</i><code>)</code>
int
<code>Tk_ConfigureInfo(</code><i>interp, tkwin, specs, widgRec, argvName, flags</i><code>)</code>
int
<code>Tk_ConfigureValue(</code><i>interp, tkwin, specs, widgRec, argvName, flags</i><code>)</code>
<code>Tk_FreeOptions(</code><i>specs, widgRec, display, flags</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for returning error messages.</p>
<dd>Tk_Window <i>tkwin</i> (in) Window used to represent widget (needed to set up X resources).</p>
<dd>Tk_ConfigSpec <i>*specs</i> (in) Pointer to table specifying legal configuration options for this widget.</p>
<dd>int <i>argc</i> (in) Number of arguments in <i>argv</i>.</p>
<dd>const char <i>**argv</i> (in) Command-line options for configuring widget.</p>
<dd>char <i>*widgRec</i> (in/out) Points to widget record structure. Fields in this structure get modified by <code>Tk_ConfigureWidget</code> to hold configuration information.</p>
<dd>int <i>flags</i> (in) If non-zero, then it specifies an OR-ed combination of flags that control the processing of configuration information. <code>TK_CONFIG_ARGV_ONLY</code> causes the option database and defaults to be ignored, and flag bits <code>TK_CONFIG_USER_BIT</code> and higher are used to selectively disable entries in <i>specs</i>.</p>
<dd>type name <i>type</i> (in) The name of the type of a widget record.</p>
<dd>field name <i>field</i> (in) The name of a field in records of type <i>type</i>.</p>
<dd>const char <i>*argvName</i> (in) The name used on Tcl command lines to refer to a particular option (e.g. when creating a widget or invoking the <code>configure</code> widget command). If non-NULL, then information is returned only for this option. If NULL, then information is returned for all available options.</p>
<dd>Display <i>*display</i> (in) Display containing widget whose record is being freed; needed in order to free up resources.
</dl>
<h2>Description</h2>
<p>Note: <code>Tk_ConfigureWidget</code> should be replaced with the new <code>Tcl_Obj</code> based API <code>Tk_SetOptions</code>. The old interface is retained for backward compatibility. </p>
<p> <code>Tk_ConfigureWidget</code> is called to configure various aspects of a widget, such as colors, fonts, border width, etc. It is intended as a convenience procedure to reduce the amount of code that must be written in individual widget managers to handle configuration information. It is typically invoked when widgets are created, and again when the <code>configure</code> command is invoked for a widget. Although intended primarily for widgets, <code>Tk_ConfigureWidget</code> can be used in other situations where <i>argc-argv</i> information is to be used to fill in a record structure, such as configuring graphical elements for a canvas widget or entries of a menu. </p>
<p> <code>Tk_ConfigureWidget</code> processes a table specifying the configuration options that are supported (<i>specs</i>) and a collection of command-line arguments (<i>argc</i> and <i>argv</i>) to fill in fields of a record (<i>widgRec</i>). It uses the option database and defaults specified in <i>specs</i> to fill in fields of <i>widgRec</i> that are not specified in <i>argv</i>. <code>Tk_ConfigureWidget</code> normally returns the value <code>TCL_OK</code>; in this case it does not modify <i>interp</i>. If an error occurs then <code>TCL_ERROR</code> is returned and <code>Tk_ConfigureWidget</code> will leave an error message in <i>interp-&gt;result</i> in the standard Tcl fashion. In the event of an error return, some of the fields of <i>widgRec</i> could already have been set, if configuration information for them was successfully processed before the error occurred. The other fields will be set to reasonable initial values so that <code>Tk_FreeOptions</code> can be called for cleanup. </p>
<p> The <i>specs</i> array specifies the kinds of configuration options expected by the widget. Each of its entries specifies one configuration option and has the following structure:</p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 int <i>type</i>;
 char *<i>argvName</i>;
 char *<i>dbName</i>;
 char *<i>dbClass</i>;
 char *<i>defValue</i>;
 int <i>offset</i>;
 int <i>specFlags</i>;
 Tk_CustomOption *<i>customPtr</i>;
} Tk_ConfigSpec;</pre>
</dl>
<p> The <i>type</i> field indicates what type of configuration option this is (e.g. <code>TK_CONFIG_COLOR</code> for a color value, or <code>TK_CONFIG_INT</code> for an integer value). The <i>type</i> field indicates how to use the value of the option (more on this below). The <i>argvName</i> field is a string such as &#8220;-font&#8221; or &#8220;-bg&#8221;, which is compared with the values in <i>argv</i> (if <i>argvName</i> is NULL it means this is a grouped entry; see <code>GROUPED ENTRIES</code> below). The <i>dbName</i> and <i>dbClass</i> fields are used to look up a value for this option in the option database. The <i>defValue</i> field specifies a default value for this configuration option if no value is specified in either <i>argv</i> or the option database. <i>Offset</i> indicates where in <i>widgRec</i> to store information about this option, and <i>specFlags</i> contains additional information to control the processing of this configuration option (see FLAGS below). The last field, <i>customPtr</i>, is only used if <i>type</i> is <code>TK_CONFIG_CUSTOM</code>; see CUSTOM OPTION TYPES below. </p>
<p> <code>Tk_ConfigureWidget</code> first processes <i>argv</i> to see which (if any) configuration options are specified there. <i>Argv</i> must contain an even number of fields; the first of each pair of fields must match the <i>argvName</i> of some entry in <i>specs</i> (unique abbreviations are acceptable), and the second field of the pair contains the value for that configuration option. If there are entries in <i>spec</i> for which there were no matching entries in <i>argv</i>, <code>Tk_ConfigureWidget</code> uses the <i>dbName</i> and <i>dbClass</i> fields of the <i>specs</i> entry to probe the option database; if a value is found, then it is used as the value for the option. Finally, if no entry is found in the option database, the <i>defValue</i> field of the <i>specs</i> entry is used as the value for the configuration option. If the <i>defValue</i> is NULL, or if the <code>TK_CONFIG_DONT_SET_DEFAULT</code> bit is set in <i>flags</i>, then there is no default value and this <i>specs</i> entry will be ignored if no value is specified in <i>argv</i> or the option database. </p>
<p> Once a string value has been determined for a configuration option, <code>Tk_ConfigureWidget</code> translates the string value into a more useful form, such as a color if <i>type</i> is <code>TK_CONFIG_COLOR</code> or an integer if <i>type</i> is <code>TK_CONFIG_INT</code>. This value is then stored in the record pointed to by <i>widgRec</i>. This record is assumed to contain information relevant to the manager of the widget; its exact type is unknown to <code>Tk_ConfigureWidget</code>. The <i>offset</i> field of each <i>specs</i> entry indicates where in <i>widgRec</i> to store the information about this configuration option. You should use the <code>Tk_Offset</code> macro to generate <i>offset</i> values (see below for a description of <code>Tk_Offset</code>). The location indicated by <i>widgRec</i> and <i>offset</i> will be referred to as the &#8220;target&#8221; in the descriptions below. </p>
<p> The <i>type</i> field of each entry in <i>specs</i> determines what to do with the string value of that configuration option. The legal values for <i>type</i>, and the corresponding actions, are:</p>
<dl COMPACT>
<dt><code>TK_CONFIG_ACTIVE_CURSOR</code></p>
<dd>The value must be an ASCII string identifying a cursor in a form suitable for passing to <code>Tk_GetCursor</code>. The value is converted to a <code>Tk_Cursor</code> by calling <code>Tk_GetCursor</code> and the result is stored in the target. In addition, the resulting cursor is made the active cursor for <i>tkwin</i> by calling <code>XDefineCursor</code>. If <code>TK_CONFIG_NULL_OK</code> is specified in <i>specFlags</i> then the value may be an empty string, in which case the target and <i>tkwin</i>&#8216;s active cursor will be set to <code>None</code>. If the previous value of the target was not <code>None</code>, then it is freed by passing it to <code>Tk_FreeCursor</code>.</p>
<dt><code>TK_CONFIG_ANCHOR</code></p>
<dd>The value must be an ASCII string identifying an anchor point in one of the ways accepted by <code>Tk_GetAnchor</code>. The string is converted to a <code>Tk_Anchor</code> by calling <code>Tk_GetAnchor</code> and the result is stored in the target.</p>
<dt><code>TK_CONFIG_BITMAP</code></p>
<dd>The value must be an ASCII string identifying a bitmap in a form suitable for passing to <code>Tk_GetBitmap</code>. The value is converted to a <code>Pixmap</code> by calling <code>Tk_GetBitmap</code> and the result is stored in the target. If <code>TK_CONFIG_NULL_OK</code> is specified in <i>specFlags</i> then the value may be an empty string, in which case the target is set to <code>None</code>. If the previous value of the target was not <code>None</code>, then it is freed by passing it to <code>Tk_FreeBitmap</code>.</p>
<dt><code>TK_CONFIG_BOOLEAN</code></p>
<dd>The value must be an ASCII string specifying a boolean value. Any of the values &#8220;true&#8221;, &#8220;yes&#8221;, &#8220;on&#8221;, or &#8220;1&#8221;, or an abbreviation of one of these values, means true; any of the values &#8220;false&#8221;, &#8220;no&#8221;, &#8220;off&#8221;, or &#8220;0&#8221;, or an abbreviation of one of these values, means false. The target is expected to be an integer; for true values it will be set to 1 and for false values it will be set to 0.</p>
<dt><code>TK_CONFIG_BORDER</code></p>
<dd>The value must be an ASCII string identifying a border color in a form suitable for passing to <code>Tk_Get3DBorder</code>. The value is converted to a (<code>Tk_3DBorder *</code>) by calling <code>Tk_Get3DBorder</code> and the result is stored in the target. If <code>TK_CONFIG_NULL_OK</code> is specified in <i>specFlags</i> then the value may be an empty string, in which case the target will be set to NULL. If the previous value of the target was not NULL, then it is freed by passing it to <code>Tk_Free3DBorder</code>.</p>
<dt><code>TK_CONFIG_CAP_STYLE</code></p>
<dd>The value must be an ASCII string identifying a cap style in one of the ways accepted by <code>Tk_GetCapStyle</code>. The string is converted to an integer value corresponding to the cap style by calling <code>Tk_GetCapStyle</code> and the result is stored in the target.</p>
<dt><code>TK_CONFIG_COLOR</code></p>
<dd>The value must be an ASCII string identifying a color in a form suitable for passing to <code>Tk_GetColor</code>. The value is converted to an (<code>XColor *</code>) by calling <code>Tk_GetColor</code> and the result is stored in the target. If <code>TK_CONFIG_NULL_OK</code> is specified in <i>specFlags</i> then the value may be an empty string, in which case the target will be set to <code>None</code>. If the previous value of the target was not NULL, then it is freed by passing it to <code>Tk_FreeColor</code>.</p>
<dt><code>TK_CONFIG_CURSOR</code></p>
<dd>This option is identical to <code>TK_CONFIG_ACTIVE_CURSOR</code> except that the new cursor is not made the active one for <i>tkwin</i>.</p>
<dt><code>TK_CONFIG_CUSTOM</code></p>
<dd>This option allows applications to define new option types. The <i>customPtr</i> field of the entry points to a structure defining the new option type. See the section <code>CUSTOM OPTION TYPES</code> below for details.</p>
<dt><code>TK_CONFIG_DOUBLE</code></p>
<dd>The value must be an ASCII floating-point number in the format accepted by <code>strtol</code>. The string is converted to a <code>double</code> value, and the value is stored in the target.</p>
<dt><code>TK_CONFIG_END</code></p>
<dd>Marks the end of the table. The last entry in <i>specs</i> must have this type; all of its other fields are ignored and it will never match any arguments.</p>
<dt><code>TK_CONFIG_FONT</code></p>
<dd>The value must be an ASCII string identifying a font in a form suitable for passing to <code>Tk_GetFont</code>. The value is converted to a <code>Tk_Font</code> by calling <code>Tk_GetFont</code> and the result is stored in the target. If <code>TK_CONFIG_NULL_OK</code> is specified in <i>specFlags</i> then the value may be an empty string, in which case the target will be set to NULL. If the previous value of the target was not NULL, then it is freed by passing it to <code>Tk_FreeFont</code>.</p>
<dt><code>TK_CONFIG_INT</code></p>
<dd>The value must be an ASCII integer string in the format accepted by <code>strtol</code> (e.g. &#8220;0&#8221; and &#8220;0x&#8221; prefixes may be used to specify octal or hexadecimal numbers, respectively). The string is converted to an integer value and the integer is stored in the target.</p>
<dt><code>TK_CONFIG_JOIN_STYLE</code></p>
<dd>The value must be an ASCII string identifying a join style in one of the ways accepted by <code>Tk_GetJoinStyle</code>. The string is converted to an integer value corresponding to the join style by calling <code>Tk_GetJoinStyle</code> and the result is stored in the target.</p>
<dt><code>TK_CONFIG_JUSTIFY</code></p>
<dd>The value must be an ASCII string identifying a justification method in one of the ways accepted by <code>Tk_GetJustify</code>. The string is converted to a <code>Tk_Justify</code> by calling <code>Tk_GetJustify</code> and the result is stored in the target.</p>
<dt><code>TK_CONFIG_MM</code></p>
<dd>The value must specify a screen distance in one of the forms acceptable to <code>Tk_GetScreenMM</code>. The string is converted to double-precision floating-point distance in millimeters and the value is stored in the target.</p>
<dt><code>TK_CONFIG_PIXELS</code></p>
<dd>The value must specify screen units in one of the forms acceptable to <code>Tk_GetPixels</code>. The string is converted to an integer distance in pixels and the value is stored in the target.</p>
<dt><code>TK_CONFIG_RELIEF</code></p>
<dd>The value must be an ASCII string identifying a relief in a form suitable for passing to <code>Tk_GetRelief</code>. The value is converted to an integer relief value by calling <code>Tk_GetRelief</code> and the result is stored in the target.</p>
<dt><code>TK_CONFIG_STRING</code></p>
<dd>A copy of the value is made by allocating memory space with <code>Tcl_Alloc</code> and copying the value into the dynamically-allocated space. A pointer to the new string is stored in the target. If <code>TK_CONFIG_NULL_OK</code> is specified in <i>specFlags</i> then the value may be an empty string, in which case the target will be set to NULL. If the previous value of the target was not NULL, then it is freed by passing it to <code>Tcl_Free</code>.</p>
<dt><code>TK_CONFIG_SYNONYM</code></p>
<dd>This <i>type</i> value identifies special entries in <i>specs</i> that are synonyms for other entries. If an <i>argv</i> value matches the <i>argvName</i> of a <code>TK_CONFIG_SYNONYM</code> entry, the entry is not used directly. Instead, <code>Tk_ConfigureWidget</code> searches <i>specs</i> for another entry whose <i>argvName</i> is the same as the <i>dbName</i> field in the <code>TK_CONFIG_SYNONYM</code> entry; this new entry is used just as if its <i>argvName</i> had matched the <i>argv</i> value. The synonym mechanism allows multiple <i>argv</i> values to be used for a single configuration option, such as &#8220;-background&#8221; and &#8220;-bg&#8221;.</p>
<dt><code>TK_CONFIG_UID</code></p>
<dd>The value is translated to a <code>Tk_Uid</code> (by passing it to <code>Tk_GetUid</code>). The resulting value is stored in the target. If <code>TK_CONFIG_NULL_OK</code> is specified in <i>specFlags</i> and the value is an empty string then the target will be set to NULL.</p>
<dt><code>TK_CONFIG_WINDOW</code></p>
<dd>The value must be a window path name. It is translated to a <code>Tk_Window</code> token and the token is stored in the target. </p>
</dl>
<h2>Grouped Entries</h2>
<p>In some cases it is useful to generate multiple resources from a single configuration value. For example, a color name might be used both to generate the background color for a widget (using <code>TK_CONFIG_COLOR</code>) and to generate a 3-D border to draw around the widget (using <code>TK_CONFIG_BORDER</code>). In cases like this it is possible to specify that several consecutive entries in <i>specs</i> are to be treated as a group. The first entry is used to determine a value (using its <i>argvName</i>, <i>dbName</i>, <i>dbClass</i>, and <i>defValue</i> fields). The value will be processed several times (one for each entry in the group), generating multiple different resources and modifying multiple targets within <i>widgRec</i>. Each of the entries after the first must have a NULL value in its <i>argvName</i> field; this indicates that the entry is to be grouped with the entry that precedes it. Only the <i>type</i> and <i>offset</i> fields are used from these follow-on entries. </p>
<h2>Flags</h2>
<p>The <i>flags</i> argument passed to <code>Tk_ConfigureWidget</code> is used in conjunction with the <i>specFlags</i> fields in the entries of <i>specs</i> to provide additional control over the processing of configuration options. These values are used in three different ways as described below. </p>
<p> First, if the <i>flags</i> argument to <code>Tk_ConfigureWidget</code> has the <code>TK_CONFIG_ARGV_ONLY</code> bit set (i.e., <i>flags</i> | <code>TK_CONFIG_ARGV_ONLY</code> != 0), then the option database and <i>defValue</i> fields are not used. In this case, if an entry in <i>specs</i> does not match a field in <i>argv</i> then nothing happens: the corresponding target is not modified. This feature is useful when the goal is to modify certain configuration options while leaving others in their current state, such as when a <code>configure</code> widget command is being processed. </p>
<p> Second, the <i>specFlags</i> field of an entry in <i>specs</i> may be used to control the processing of that entry. Each <i>specFlags</i> field may consists of an OR-ed combination of the following values:</p>
<dl COMPACT>
<dt><code>TK_CONFIG_COLOR_ONLY</code></p>
<dd>If this bit is set then the entry will only be considered if the display for <i>tkwin</i> has more than one bit plane. If the display is monochromatic then this <i>specs</i> entry will be ignored.</p>
<dt><code>TK_CONFIG_MONO_ONLY</code></p>
<dd>If this bit is set then the entry will only be considered if the display for <i>tkwin</i> has exactly one bit plane. If the display is not monochromatic then this <i>specs</i> entry will be ignored.</p>
<dt><code>TK_CONFIG_NULL_OK</code></p>
<dd>This bit is only relevant for some types of entries (see the descriptions of the various entry types above). If this bit is set, it indicates that an empty string value for the field is acceptable and if it occurs then the target should be set to NULL or <code>None</code>, depending on the type of the target. This flag is typically used to allow a feature to be turned off entirely, e.g. set a cursor value to <code>None</code> so that a window simply inherits its parent&#8217;s cursor. If this bit is not set then empty strings are processed as strings, which generally results in an error.</p>
<dt><code>TK_CONFIG_DONT_SET_DEFAULT</code></p>
<dd>If this bit is one, it means that the <i>defValue</i> field of the entry should only be used for returning the default value in <code>Tk_ConfigureInfo</code>. In calls to <code>Tk_ConfigureWidget</code> no default will be supplied for entries with this flag set; it is assumed that the caller has already supplied a default value in the target location. This flag provides a performance optimization where it is expensive to process the default string: the client can compute the default once, save the value, and provide it before calling <code>Tk_ConfigureWidget</code>.</p>
<dt><code>TK_CONFIG_OPTION_SPECIFIED</code></p>
<dd>This bit is deprecated. It used to be set and cleared by <code>Tk_ConfigureWidget</code> so that callers could detect what entries were specified in <i>argv</i>, but it was removed because it was inherently thread-unsafe. Code that wishes to detect what options were specified should use <code>Tk_SetOptions</code> instead.</dl>
<p> The <code>TK_CONFIG_MONO_ONLY</code> and <code>TK_CONFIG_COLOR_ONLY</code> flags are typically used to specify different default values for monochrome and color displays. This is done by creating two entries in <i>specs</i> that are identical except for their <i>defValue</i> and <i>specFlags</i> fields. One entry should have the value <code>TK_CONFIG_MONO_ONLY</code> in its <i>specFlags</i> and the default value for monochrome displays in its <i>defValue</i>; the other entry should have the value <code>TK_CONFIG_COLOR_ONLY</code> in its <i>specFlags</i> and the appropriate <i>defValue</i> for color displays. </p>
<p> Third, it is possible to use <i>flags</i> and <i>specFlags</i> together to selectively disable some entries. This feature is not needed very often. It is useful in cases where several similar kinds of widgets are implemented in one place. It allows a single <i>specs</i> table to be created with all the configuration options for all the widget types. When processing a particular widget type, only entries relevant to that type will be used. This effect is achieved by setting the high-order bits (those in positions equal to or greater than <code>TK_CONFIG_USER_BIT</code>) in <i>specFlags</i> values or in <i>flags</i>. In order for a particular entry in <i>specs</i> to be used, its high-order bits must match exactly the high-order bits of the <i>flags</i> value passed to <code>Tk_ConfigureWidget</code>. If a <i>specs</i> table is being used for N different widget types, then N of the high-order bits will be used. Each <i>specs</i> entry will have one of more of those bits set in its <i>specFlags</i> field to indicate the widget types for which this entry is valid. When calling <code>Tk_ConfigureWidget</code>, <i>flags</i> will have a single one of these bits set to select the entries for the desired widget type. For a working example of this feature, see the code in tkButton.c. </p>
<h2>Tk_Offset</h2>
<p>The <code>Tk_Offset</code> macro is provided as a safe way of generating the <i>offset</i> values for entries in Tk_ConfigSpec structures. It takes two arguments: the name of a type of record, and the name of a field in that record. It returns the byte offset of the named field in records of the given type. </p>
<h2>Tk_Configureinfo</h2>
<p>The <code>Tk_ConfigureInfo</code> procedure may be used to obtain information about one or all of the options for a given widget. Given a token for a window (<i>tkwin</i>), a table describing the configuration options for a class of widgets (<i>specs</i>), a pointer to a widget record containing the current information for a widget (<i>widgRec</i>), and a NULL <i>argvName</i> argument, <code>Tk_ConfigureInfo</code> generates a string describing all of the configuration options for the window. The string is placed in <i>interp-&gt;result</i>. Under normal circumstances it returns <code>TCL_OK</code>; if an error occurs then it returns <code>TCL_ERROR</code> and <i>interp-&gt;result</i> contains an error message. </p>
<p> If <i>argvName</i> is NULL, then the value left in <i>interp-&gt;result</i> by <code>Tk_ConfigureInfo</code> consists of a list of one or more entries, each of which describes one configuration option (i.e. one entry in <i>specs</i>). Each entry in the list will contain either two or five values. If the corresponding entry in <i>specs</i> has type <code>TK_CONFIG_SYNONYM</code>, then the list will contain two values: the <i>argvName</i> for the entry and the <i>dbName</i> (synonym name). Otherwise the list will contain five values: <i>argvName</i>, <i>dbName</i>, <i>dbClass</i>, <i>defValue</i>, and current value. The current value is computed from the appropriate field of <i>widgRec</i> by calling procedures like <code>Tk_NameOfColor</code>. </p>
<p> If the <i>argvName</i> argument to <code>Tk_ConfigureInfo</code> is non-NULL, then it indicates a single option, and information is returned only for that option. The string placed in <i>interp-&gt;result</i> will be a list containing two or five values as described above; this will be identical to the corresponding sublist that would have been returned if <i>argvName</i> had been NULL. </p>
<p> The <i>flags</i> argument to <code>Tk_ConfigureInfo</code> is used to restrict the <i>specs</i> entries to consider, just as for <code>Tk_ConfigureWidget</code>. </p>
<h2>Tk_Configurevalue</h2>
<p><code>Tk_ConfigureValue</code> takes arguments similar to <code>Tk_ConfigureInfo</code>; instead of returning a list of values, it just returns the current value of the option given by <i>argvName</i> (<i>argvName</i> must not be NULL). The value is returned in <i>interp-&gt;result</i> and <code>TCL_OK</code> is normally returned as the procedure&#8217;s result. If an error occurs in <code>Tk_ConfigureValue</code> (e.g., <i>argvName</i> is not a valid option name), <code>TCL_ERROR</code> is returned and an error message is left in <i>interp-&gt;result</i>. This procedure is typically called to implement <code>cget</code> widget commands. </p>
<h2>Tk_Freeoptions</h2>
<p>The <code>Tk_FreeOptions</code> procedure may be invoked during widget cleanup to release all of the resources associated with configuration options. It scans through <i>specs</i> and for each entry corresponding to a resource that must be explicitly freed (e.g. those with type <code>TK_CONFIG_COLOR</code>), it frees the resource in the widget record. If the field in the widget record does not refer to a resource (e.g. it contains a null pointer) then no resource is freed for that entry. After freeing a resource, <code>Tk_FreeOptions</code> sets the corresponding field of the widget record to null. </p>
<h2>Custom Option Types</h2>
<p>Applications can extend the built-in configuration types with additional configuration types by writing procedures to parse and print options of the a type and creating a structure pointing to those procedures:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tk_CustomOption {
 Tk_OptionParseProc *<i>parseProc</i>;
 Tk_OptionPrintProc *<i>printProc</i>;
 ClientData <i>clientData</i>;
} Tk_CustomOption;
typedef int Tk_OptionParseProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 Tk_Window <i>tkwin</i>,
 char *<i>value</i>,
 char *<i>widgRec</i>,
 int <i>offset</i>);
typedef char *Tk_OptionPrintProc(
 ClientData <i>clientData</i>,
 Tk_Window <i>tkwin</i>,
 char *<i>widgRec</i>,
 int <i>offset</i>,
 Tcl_FreeProc **<i>freeProcPtr</i>);</pre>
</dl>
<p> The Tk_CustomOption structure contains three fields, which are pointers to the two procedures and a <i>clientData</i> value to be passed to those procedures when they are invoked. The <i>clientData</i> value typically points to a structure containing information that is needed by the procedures when they are parsing and printing options. </p>
<p> The <i>parseProc</i> procedure is invoked by <code>Tk_ConfigureWidget</code> to parse a string and store the resulting value in the widget record. The <i>clientData</i> argument is a copy of the <i>clientData</i> field in the Tk_CustomOption structure. The <i>interp</i> argument points to a Tcl interpreter used for error reporting. <i>Tkwin</i> is a copy of the <i>tkwin</i> argument to <code>Tk_ConfigureWidget</code>. The <i>value</i> argument is a string describing the value for the option; it could have been specified explicitly in the call to <code>Tk_ConfigureWidget</code> or it could come from the option database or a default. <i>Value</i> will never be a null pointer but it may point to an empty string. <i>RecordPtr</i> is the same as the <i>widgRec</i> argument to <code>Tk_ConfigureWidget</code>; it points to the start of the widget record to modify. The last argument, <i>offset</i>, gives the offset in bytes from the start of the widget record to the location where the option value is to be placed. The procedure should translate the string to whatever form is appropriate for the option and store the value in the widget record. It should normally return <code>TCL_OK</code>, but if an error occurs in translating the string to a value then it should return <code>TCL_ERROR</code> and store an error message in <i>interp-&gt;result</i>. </p>
<p> The <i>printProc</i> procedure is called by <code>Tk_ConfigureInfo</code> to produce a string value describing an existing option. Its <i>clientData</i>, <i>tkwin</i>, <i>widgRec</i>, and <i>offset</i> arguments all have the same meaning as for Tk_OptionParseProc procedures. The <i>printProc</i> procedure should examine the option whose value is stored at <i>offset</i> in <i>widgRec</i>, produce a string describing that option, and return a pointer to the string. If the string is stored in dynamically-allocated memory, then the procedure must set <i>*freeProcPtr</i> to the address of a procedure to call to free the string&#8217;s memory; <code>Tk_ConfigureInfo</code> will call this procedure when it is finished with the string. If the result string is stored in static memory then <i>printProc</i> need not do anything with the <i>freeProcPtr</i> argument. </p>
<p> Once <i>parseProc</i> and <i>printProc</i> have been defined and a Tk_CustomOption structure has been created for them, options of this new type may be manipulated with Tk_ConfigSpec entries whose <i>type</i> fields are <code>TK_CONFIG_CUSTOM</code> and whose <i>customPtr</i> fields point to the Tk_CustomOption structure. </p>
<h2>Examples</h2>
<p>Although the explanation of <code>Tk_ConfigureWidget</code> is fairly complicated, its actual use is pretty straightforward. The easiest way to get started is to copy the code from an existing widget. The library implementation of frames (tkFrame.c) has a simple configuration table, and the library implementation of buttons (tkButton.c) has a much more complex table that uses many of the fancy <i>specFlags</i> mechanisms. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tk_setoptions/">Tk_SetOptions</a>(3) </p>
<h2>Keywords</h2>
<p>anchor, bitmap, boolean, border, cap style, color, configuration options, cursor, custom, double, font, integer, join style, justify, millimeters, pixels, relief, synonym, uid</p>
