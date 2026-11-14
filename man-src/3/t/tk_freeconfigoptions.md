---
title: "tk_freeconfigoptions(3)"
name: "tk_freeconfigoptions"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_freeconfigoptions/"
description: "Tk_CreateOptionTable, Tk_DeleteOptionTable, Tk_InitOptions, Tk_SetOptions, Tk_FreeSavedOptions, Tk_RestoreSavedOptions, Tk_GetOptionValue, Tk_GetOptionInfo, Tk_FreeConfigOptions, Tk_Offset – proces..."
---

<p>Tk_CreateOptionTable, Tk_DeleteOptionTable, Tk_InitOptions, Tk_SetOptions, Tk_FreeSavedOptions, Tk_RestoreSavedOptions, Tk_GetOptionValue, Tk_GetOptionInfo, Tk_FreeConfigOptions, Tk_Offset &#8211; process configuration options </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_OptionTable
<code>Tk_CreateOptionTable(</code><i>interp, templatePtr</i><code>)</code>
<code>Tk_DeleteOptionTable(</code><i>optionTable</i><code>)</code>
int
<code>Tk_InitOptions(</code><i>interp, recordPtr, optionTable, tkwin</i><code>)</code>
int
<code>Tk_SetOptions(</code><i>interp, recordPtr, optionTable, objc, objv, tkwin, savePtr, maskPtr</i><code>)</code>
<code>Tk_FreeSavedOptions(</code><i>savedPtr</i><code>)</code>
<code>Tk_RestoreSavedOptions(</code><i>savedPtr</i><code>)</code>
Tcl_Obj *
<code>Tk_GetOptionValue(</code><i>interp, recordPtr, optionTable, namePtr, tkwin</i><code>)</code>
Tcl_Obj *
<code>Tk_GetOptionInfo(</code><i>interp, recordPtr, optionTable, namePtr, tkwin</i><code>)</code>
<code>Tk_FreeConfigOptions(</code><i>recordPtr, optionTable, tkwin</i><code>)</code>
int
<code>Tk_Offset(</code><i>type, field</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) A Tcl interpreter. Most procedures use this only for returning error messages; if it is NULL then no error messages are returned. For <code>Tk_CreateOptionTable</code> the value cannot be NULL; it gives the interpreter in which the option table will be used.</p>
<dd>const Tk_OptionSpec <i>*templatePtr</i> (in) Points to an array of static information that describes the configuration options that are supported. Used to build a Tk_OptionTable. The information pointed to by this argument must exist for the lifetime of the Tk_OptionTable.</p>
<dd>Tk_OptionTable <i>optionTable</i> (in) Token for an option table. Must have been returned by a previous call to <code>Tk_CreateOptionTable</code>.</p>
<dd>char <i>*recordPtr</i> (in/out) Points to structure in which values of configuration options are stored; fields of this record are modified by procedures such as <code>Tk_SetOptions</code> and read by procedures such as <code>Tk_GetOptionValue</code>.</p>
<dd>Tk_Window <i>tkwin</i> (in) For options such as <code>TK_OPTION_COLOR</code>, this argument indicates the window in which the option will be used. If <i>optionTable</i> uses no window-dependent options, then a NULL value may be supplied for this argument.</p>
<dd>int <i>objc</i> (in) Number of values in <i>objv</i>.</p>
<dd>Tcl_Obj <i>*const objv[]</i> (in) Command-line arguments for setting configuring options.</p>
<dd>Tk_SavedOptions <i>*savePtr</i> (out) If not NULL, the structure pointed to by this argument is filled in with the old values of any options that were modified and old values are restored automatically if an error occurs in <code>Tk_SetOptions</code>.</p>
<dd>int <i>*maskPtr</i> (out) If not NULL, the word pointed to by <i>maskPtr</i> is filled in with the bit-wise OR of the <i>typeMask</i> fields for the options that were modified.</p>
<dd>Tk_SavedOptions <i>*savedPtr</i> (in/out) Points to a structure previously filled in by <code>Tk_SetOptions</code> with old values of modified options.</p>
<dd>Tcl_Obj <i>*namePtr</i> (in) The value of this object is the name of a particular option. If NULL is passed to <code>Tk_GetOptionInfo</code> then information is returned for all options. Must not be NULL when <code>Tk_GetOptionValue</code> is called.</p>
<dd>type name <i>type</i> (in) The name of the type of a record.</p>
<dd>field name <i>field</i> (in) The name of a field in records of type <i>type</i>.
</dl>
<h2>Description</h2>
<p>These procedures handle most of the details of parsing configuration options such as those for Tk widgets. Given a description of what options are supported, these procedures handle all the details of parsing options and storing their values into a C structure associated with the widget or object. The procedures were designed primarily for widgets in Tk, but they can also be used for other kinds of objects that have configuration options. In the rest of this manual page &#8220;widget&#8221; will be used to refer to the object whose options are being managed; in practice the object may not actually be a widget. The term &#8220;widget record&#8221; is used to refer to the C-level structure in which information about a particular widget or object is stored. </p>
<p> Note: the easiest way to learn how to use these procedures is to look at a working example. In Tk, the simplest example is the code that implements the button family of widgets, which is in <code>tkButton.c</code>. Other examples are in <code>tkSquare.c</code> and <code>tkMenu.c</code>. </p>
<p> In order to use these procedures, the code that implements the widget must contain a static array of Tk_OptionSpec structures. This is a template that describes the various options supported by that class of widget; there is a separate template for each kind of widget. The template contains information such as the name of each option, its type, its default value, and where the value of the option is stored in the widget record. See TEMPLATES below for more detail. </p>
<p> In order to process configuration options efficiently, the static template must be augmented with additional information that is available only at runtime. The procedure <code>Tk_CreateOptionTable</code> creates this dynamic information from the template and returns a Tk_OptionTable token that describes both the static and dynamic information. All of the other procedures, such as <code>Tk_SetOptions</code>, take a Tk_OptionTable token as argument. Typically, <code>Tk_CreateOptionTable</code> is called the first time that a widget of a particular class is created and the resulting Tk_OptionTable is used in the future for all widgets of that class. A Tk_OptionTable may be used only in a single interpreter, given by the <i>interp</i> argument to <code>Tk_CreateOptionTable</code>. When an option table is no longer needed <code>Tk_DeleteOptionTable</code> should be called to free all of its resources. All of the option tables for a Tcl interpreter are freed automatically if the interpreter is deleted. </p>
<p> <code>Tk_InitOptions</code> is invoked when a new widget is created to set the default values for all of the widget&#8217;s configuration options. <code>Tk_InitOptions</code> is passed a token for an option table (<i>optionTable</i>) and a pointer to a widget record (<i>recordPtr</i>), which is the C structure that holds information about this widget. <code>Tk_InitOptions</code> uses the information in the option table to choose an appropriate default for each option, then it stores the default value directly into the widget record, overwriting any information that was already present in the widget record. <code>Tk_InitOptions</code> normally returns <code>TCL_OK</code>. If an error occurred while setting the default values (e.g., because a default value was erroneous) then <code>TCL_ERROR</code> is returned and an error message is left in <i>interp</i>&#8216;s result if <i>interp</i> is not NULL. </p>
<p> <code>Tk_SetOptions</code> is invoked to modify configuration options based on information specified in a Tcl command. The command might be one that creates a new widget, or a command that modifies options on an existing widget. The <i>objc</i> and <i>objv</i> arguments describe the values of the arguments from the Tcl command. <i>Objv</i> must contain an even number of objects: the first object of each pair gives the name of an option and the second object gives the new value for that option. <code>Tk_SetOptions</code> looks up each name in <i>optionTable</i>, checks that the new value of the option conforms to the type in <i>optionTable</i>, and stores the value of the option into the widget record given by <i>recordPtr</i>. <code>Tk_SetOptions</code> normally returns <code>TCL_OK</code>. If an error occurred (such as an unknown option name or an illegal option value) then <code>TCL_ERROR</code> is returned and an error message is left in <i>interp</i>&#8216;s result if <i>interp</i> is not NULL. </p>
<p> <code>Tk_SetOptions</code> has two additional features. First, if the <i>maskPtr</i> argument is not NULL then it points to an integer value that is filled in with information about the options that were modified. For each option in the template passed to <code>Tk_CreateOptionTable</code> there is a <i>typeMask</i> field. The bits of this field are defined by the code that implements the widget; for example, each bit might correspond to a particular configuration option. Alternatively, bits might be used functionally. For example, one bit might be used for redisplay: all options that affect the widget&#8217;s display, such that changing the option requires the widget to be redisplayed, might have that bit set. Another bit might indicate that the geometry of the widget must be recomputed, and so on. <code>Tk_SetOptions</code> OR&#8217;s together the <i>typeMask</i> fields from all the options that were modified and returns this value at *<i>maskPtr</i>; the caller can then use this information to optimize itself so that, for example, it does not redisplay the widget if the modified options do not affect the widget&#8217;s appearance. </p>
<p> The second additional feature of <code>Tk_SetOptions</code> has to do with error recovery. If an error occurs while processing configuration options, this feature makes it possible to restore all the configuration options to their previous values. Errors can occur either while processing options in <code>Tk_SetOptions</code> or later in the caller. In many cases the caller does additional processing after <code>Tk_SetOptions</code> returns; for example, it might use an option value to set a trace on a variable and may detect an error if the variable is an array instead of a scalar. Error recovery is enabled by passing in a non-NULL value for the <i>savePtr</i> argument to <code>Tk_SetOptions</code>; this should be a pointer to an uninitialized Tk_SavedOptions structure on the caller&#8217;s stack. <code>Tk_SetOptions</code> overwrites the structure pointed to by <i>savePtr</i> with information about the old values of any options modified by the procedure. If <code>Tk_SetOptions</code> returns successfully, the caller uses the structure in one of two ways. If the caller completes its processing of the new options without any errors, then it must pass the structure to <code>Tk_FreeSavedOptions</code> so that the old values can be freed. If the caller detects an error in its processing of the new options, then it should pass the structure to <code>Tk_RestoreSavedOptions</code>, which will copy the old values back into the widget record and free the new values. If <code>Tk_SetOptions</code> detects an error then it automatically restores any options that had already been modified and leaves *<i>savePtr</i> in an empty state: the caller need not call either <code>Tk_FreeSavedOptions</code> or <code>Tk_RestoreSavedOptions</code>. If the <i>savePtr</i> argument to <code>Tk_SetOptions</code> is NULL then <code>Tk_SetOptions</code> frees each old option value immediately when it sets a new value for the option. In this case, if an error occurs in the third option, the old values for the first two options cannot be restored. </p>
<p> <code>Tk_GetOptionValue</code> returns the current value of a configuration option for a particular widget. The <i>namePtr</i> argument contains the name of an option; <code>Tk_GetOptionValue</code> uses <i>optionTable</i> to lookup the option and extract its value from the widget record pointed to by <i>recordPtr</i>, then it returns an object containing that value. If an error occurs (e.g., because <i>namePtr</i> contains an unknown option name) then NULL is returned and an error message is left in <i>interp</i>&#8216;s result unless <i>interp</i> is NULL. </p>
<p> <code>Tk_GetOptionInfo</code> returns information about configuration options in a form suitable for <code>configure</code> widget commands. If the <i>namePtr</i> argument is not NULL, it points to an object that gives the name of a configuration option; <code>Tk_GetOptionInfo</code> returns an object containing a list with five elements, which are the name of the option, the name and class used for the option in the option database, the default value for the option, and the current value for the option. If the <i>namePtr</i> argument is NULL, then <code>Tk_GetOptionInfo</code> returns information about all options in the form of a list of lists; each sublist describes one option. Synonym options are handled differently depending on whether <i>namePtr</i> is NULL: if <i>namePtr</i> is NULL then the sublist for each synonym option has only two elements, which are the name of the option and the name of the other option that it refers to; if <i>namePtr</i> is non-NULL and names a synonym option then the object returned is the five-element list for the other option that the synonym refers to. If an error occurs (e.g., because <i>namePtr</i> contains an unknown option name) then NULL is returned and an error message is left in <i>interp</i>&#8216;s result unless <i>interp</i> is NULL. </p>
<p> <code>Tk_FreeConfigOptions</code> must be invoked when a widget is deleted. It frees all of the resources associated with any of the configuration options defined in <i>recordPtr</i> by <i>optionTable</i>. </p>
<p> The <code>Tk_Offset</code> macro is provided as a safe way of generating the <i>objOffset</i> and <i>internalOffset</i> values for entries in Tk_OptionSpec structures. It takes two arguments: the name of a type of record, and the name of a field in that record. It returns the byte offset of the named field in records of the given type.</p>
<h2>Templates</h2>
<p>The array of Tk_OptionSpec structures passed to <code>Tk_CreateOptionTable</code> via its <i>templatePtr</i> argument describes the configuration options supported by a particular class of widgets. Each structure specifies one configuration option and has the following fields:</p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 Tk_OptionType <i>type</i>;
 const char *<i>optionName</i>;
 const char *<i>dbName</i>;
 const char *<i>dbClass</i>;
 const char *<i>defValue</i>;
 int <i>objOffset</i>;
 int <i>internalOffset</i>;
 int <i>flags</i>;
 ClientData <i>clientData</i>;
 int <i>typeMask</i>;
} <code>Tk_OptionSpec</code>;</pre>
</dl>
<p> The <i>type</i> field indicates what kind of configuration option this is (e.g. <code>TK_OPTION_COLOR</code> for a color value, or <code>TK_OPTION_INT</code> for an integer value). <i>Type</i> determines how the value of the option is parsed (more on this below). The <i>optionName</i> field is a string such as <code>-font</code> or <code>-bg</code>; it is the name used for the option in Tcl commands and passed to procedures via the <i>objc</i> or <i>namePtr</i> arguments. The <i>dbName</i> and <i>dbClass</i> fields are used by <code>Tk_InitOptions</code> to look up a default value for this option in the option database; if <i>dbName</i> is NULL then the option database is not used by <code>Tk_InitOptions</code> for this option. The <i>defValue</i> field specifies a default value for this configuration option if no value is specified in the option database. The <i>objOffset</i> and <i>internalOffset</i> fields indicate where to store the value of this option in widget records (more on this below); values for the <i>objOffset</i> and <i>internalOffset</i> fields should always be generated with the <code>Tk_Offset</code> macro. The <i>flags</i> field contains additional information to control the processing of this configuration option (see below for details). <i>ClientData</i> provides additional type-specific data needed by certain types. For instance, for <code>TK_OPTION_COLOR</code> types, <i>clientData</i> is a string giving the default value to use on monochrome displays. See the descriptions of the different types below for details. The last field, <i>typeMask</i>, is used by <code>Tk_SetOptions</code> to return information about which options were modified; see the description of <code>Tk_SetOptions</code> above for details. </p>
<p> When <code>Tk_InitOptions</code> and <code>Tk_SetOptions</code> store the value of an option into the widget record, they can do it in either of two ways. If the <i>objOffset</i> field of the Tk_OptionSpec is greater than or equal to zero, then the value of the option is stored as a (Tcl_Obj *) at the location in the widget record given by <i>objOffset</i>. If the <i>internalOffset</i> field of the Tk_OptionSpec is greater than or equal to zero, then the value of the option is stored in a type-specific internal form at the location in the widget record given by <i>internalOffset</i>. For example, if the option&#8217;s type is <code>TK_OPTION_INT</code> then the internal form is an integer. If the <i>objOffset</i> or <i>internalOffset</i> field is negative then the value is not stored in that form. At least one of the offsets must be greater than or equal to zero. </p>
<p> The <i>flags</i> field consists of one or more bits ORed together. At present only a single flag is supported: <code>TK_OPTION_NULL_OK</code>. If this bit is set for an option then an empty string will be accepted as the value for the option and the resulting internal form will be a NULL pointer, a zero value, or <code>None</code>, depending on the type of the option. If the flag is not set then empty strings will result in errors. <code>TK_OPTION_NULL_OK</code> is typically used to allow a feature to be turned off entirely, e.g. set a cursor value to <code>None</code> so that a window simply inherits its parent&#8217;s cursor. Not all option types support the <code>TK_OPTION_NULL_OK</code> flag; for those that do, there is an explicit indication of that fact in the descriptions below. </p>
<p> The <i>type</i> field of each Tk_OptionSpec structure determines how to parse the value of that configuration option. The legal value for <i>type</i>, and the corresponding actions, are described below. If the type requires a <i>tkwin</i> value to be passed into procedures like <code>Tk_SetOptions</code>, or if it uses the <i>clientData</i> field of the Tk_OptionSpec, then it is indicated explicitly; if not mentioned, the type requires neither <i>tkwin</i> nor <i>clientData</i>.</p>
<dl COMPACT>
<dt><code>TK_OPTION_ANCHOR</code></p>
<dd>The value must be a standard anchor position such as <code>ne</code> or <code>center</code>. The internal form is a Tk_Anchor value like the ones returned by <code>Tk_GetAnchorFromObj</code>.</p>
<dt><code>TK_OPTION_BITMAP</code></p>
<dd>The value must be a standard Tk bitmap name. The internal form is a Pixmap token like the ones returned by <code>Tk_AllocBitmapFromObj</code>. This option type requires <i>tkwin</i> to be supplied to procedures such as <code>Tk_SetOptions</code>, and it supports the <code>TK_OPTION_NULL_OK</code> flag.</p>
<dt><code>TK_OPTION_BOOLEAN</code></p>
<dd>The value must be a standard boolean value such as <code>true</code> or <code>no</code>. The internal form is an integer with value 0 or 1.</p>
<dt><code>TK_OPTION_BORDER</code></p>
<dd>The value must be a standard color name such as <code>red</code> or <code>#ff8080</code>. The internal form is a Tk_3DBorder token like the ones returned by <code>Tk_Alloc3DBorderFromObj</code>. This option type requires <i>tkwin</i> to be supplied to procedures such as <code>Tk_SetOptions</code>, and it supports the <code>TK_OPTION_NULL_OK</code> flag.</p>
<dt><code>TK_OPTION_COLOR</code></p>
<dd>The value must be a standard color name such as <code>red</code> or <code>#ff8080</code>. The internal form is an (XColor *) token like the ones returned by <code>Tk_AllocColorFromObj</code>. This option type requires <i>tkwin</i> to be supplied to procedures such as <code>Tk_SetOptions</code>, and it supports the <code>TK_OPTION_NULL_OK</code> flag.</p>
<dt><code>TK_OPTION_CURSOR</code></p>
<dd>The value must be a standard cursor name such as <code>cross</code> or <code>@foo</code>. The internal form is a Tk_Cursor token like the ones returned by <code>Tk_AllocCursorFromObj</code>. This option type requires <i>tkwin</i> to be supplied to procedures such as <code>Tk_SetOptions</code>, and when the option is set the cursor for the window is changed by calling <code>XDefineCursor</code>. This option type also supports the <code>TK_OPTION_NULL_OK</code> flag.</p>
<dt><code>TK_OPTION_CUSTOM</code></p>
<dd>This option allows applications to define new option types. The clientData field of the entry points to a structure defining the new option type. See the section <code>CUSTOM OPTION TYPES</code> below for details.</p>
<dt><code>TK_OPTION_DOUBLE</code></p>
<dd>The string value must be a floating-point number in the format accepted by <code>strtol</code>. The internal form is a C <code>double</code> value. This option type supports the <code>TK_OPTION_NULL_OK</code> flag; if a NULL value is set, the internal representation is set to zero.</p>
<dt><code>TK_OPTION_END</code></p>
<dd>Marks the end of the template. There must be a Tk_OptionSpec structure with <i>type</i> <code>TK_OPTION_END</code> at the end of each template. If the <i>clientData</i> field of this structure is not NULL, then it points to an additional array of Tk_OptionSpec&#8217;s, which is itself terminated by another <code>TK_OPTION_END</code> entry. Templates may be chained arbitrarily deeply. This feature allows common options to be shared by several widget classes.</p>
<dt><code>TK_OPTION_FONT</code></p>
<dd>The value must be a standard font name such as <code>Times 16</code>. The internal form is a Tk_Font handle like the ones returned by <code>Tk_AllocFontFromObj</code>. This option type requires <i>tkwin</i> to be supplied to procedures such as <code>Tk_SetOptions</code>, and it supports the <code>TK_OPTION_NULL_OK</code> flag.</p>
<dt><code>TK_OPTION_INT</code></p>
<dd>The string value must be an integer in the format accepted by <code>strtol</code> (e.g. <code>0</code> and <code>0x</code> prefixes may be used to specify octal or hexadecimal numbers, respectively). The internal form is a C <code>int</code> value.</p>
<dt><code>TK_OPTION_JUSTIFY</code></p>
<dd>The value must be a standard justification value such as <code>left</code>. The internal form is a Tk_Justify like the values returned by <code>Tk_GetJustifyFromObj</code>.</p>
<dt><code>TK_OPTION_PIXELS</code></p>
<dd>The value must specify a screen distance such as <code>2i</code> or <code>6.4</code>. The internal form is an integer value giving a distance in pixels, like the values returned by <code>Tk_GetPixelsFromObj</code>. Note: if the <i>objOffset</i> field is not used then information about the original value of this option will be lost. See <code>OBJOFFSET VS. INTERNALOFFSET</code> below for details. This option type supports the <code>TK_OPTION_NULL_OK</code> flag; if a NULL value is set, the internal representation is set to zero.</p>
<dt><code>TK_OPTION_RELIEF</code></p>
<dd>The value must be standard relief such as <code>raised</code>. The internal form is an integer relief value such as <code>TK_RELIEF_RAISED</code>. This option type supports the <code>TK_OPTION_NULL_OK</code> flag; if the empty string is specified as the value for the option, the integer relief value is set to <code>TK_RELIEF_NULL</code>.</p>
<dt><code>TK_OPTION_STRING</code></p>
<dd>The value may be any string. The internal form is a (char *) pointer that points to a dynamically allocated copy of the value. This option type supports the <code>TK_OPTION_NULL_OK</code> flag.</p>
<dt><code>TK_OPTION_STRING_TABLE</code></p>
<dd>For this type, <i>clientData</i> is a pointer to an array of strings suitable for passing to <code>Tcl_GetIndexFromObj</code>. The value must be one of the strings in the table, or a unique abbreviation of one of the strings. The internal form is an integer giving the index into the table of the matching string, like the return value from <code>Tcl_GetStringFromObj</code>.</p>
<dt><code>TK_OPTION_SYNONYM</code></p>
<dd>This type is used to provide alternative names for an option (for example, <code>-bg</code> is often used as a synonym for <code>-background</code>). The <code>clientData</code> field is a string that gives the name of another option in the same table. Whenever the synonym option is used, the information from the other option will be used instead.</p>
<dt><code>TK_OPTION_WINDOW</code></p>
<dd>The value must be a window path name. The internal form is a <code>Tk_Window</code> token for the window. This option type requires <i>tkwin</i> to be supplied to procedures such as <code>Tk_SetOptions</code> (in order to identify the application), and it supports the <code>TK_OPTION_NULL_OK</code> flag.</dl>
<h2>Storage Management Issues</h2>
<p>If a field of a widget record has its offset stored in the <i>objOffset</i> or <i>internalOffset</i> field of a Tk_OptionSpec structure then the procedures described here will handle all of the storage allocation and resource management issues associated with the field. When the value of an option is changed, <code>Tk_SetOptions</code> (or <code>Tk_FreeSavedOptions</code>) will automatically free any resources associated with the old value, such as Tk_Fonts for <code>TK_OPTION_FONT</code> options or dynamically allocated memory for <code>TK_OPTION_STRING</code> options. For an option stored as an object using the <i>objOffset</i> field of a Tk_OptionSpec, the widget record shares the object pointed to by the <i>objv</i> value from the call to <code>Tk_SetOptions</code>. The reference count for this object is incremented when a pointer to it is stored in the widget record and decremented when the option is modified. When the widget is deleted <code>Tk_FreeConfigOptions</code> should be invoked; it will free the resources associated with all options and decrement reference counts for any objects. </p>
<p> However, the widget code is responsible for storing NULL or <code>None</code> in all pointer and token fields before invoking <code>Tk_InitOptions</code>. This is needed to allow proper cleanup in the rare case where an error occurs in <code>Tk_InitOptions</code>.</p>
<h2>Objoffset Vs. Internaloffset</h2>
<p>In most cases it is simplest to use the <i>internalOffset</i> field of a Tk_OptionSpec structure and not the <i>objOffset</i> field. This makes the internal form of the value immediately available to the widget code so the value does not have to be extracted from an object each time it is used. However, there are two cases where the <i>objOffset</i> field is useful. The first case is for <code>TK_OPTION_PIXELS</code> options. In this case, the internal form is an integer pixel value that is valid only for a particular screen. If the value of the option is retrieved, it will be returned as a simple number. For example, after the command <code>.b configure -borderwidth 2m</code>, the command <code>.b configure -borderwidth</code> might return 7, which is the integer pixel value corresponding to <code>2m</code>. Unfortunately, this loses the original screen-independent value. Thus for <code>TK_OPTION_PIXELS</code> options it is better to use the <i>objOffset</i> field. In this case the original value of the option is retained in the object and can be returned when the option is retrieved. In most cases it is convenient to use the <i>internalOffset</i> field as well, so that the integer value is immediately available for use in the widget code (alternatively, <code>Tk_GetPixelsFromObj</code> can be used to extract the integer value from the object whenever it is needed). Note: the problem of losing information on retrievals exists only for <code>TK_OPTION_PIXELS</code> options. </p>
<p> The second reason to use the <i>objOffset</i> field is in order to implement new types of options not supported by these procedures. To implement a new type of option, you can use <code>TK_OPTION_STRING</code> as the type in the Tk_OptionSpec structure and set the <i>objOffset</i> field but not the <i>internalOffset</i> field. Then, after calling <code>Tk_SetOptions</code>, convert the object to internal form yourself.</p>
<h2>Custom Option Types</h2>
<p>Applications can extend the built-in configuration types with additional configuration types by writing procedures to parse, print, free, and restore saved copies of the type and creating a structure pointing to those procedures:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tk_ObjCustomOption {
 char *name;
 Tk_CustomOptionSetProc *<i>setProc</i>;
 Tk_CustomOptionGetProc *<i>getProc</i>;
 Tk_CustomOptionRestoreProc *<i>restoreProc</i>;
 Tk_CustomOptionFreeProc *<i>freeProc</i>;
 ClientData <i>clientData</i>;
} <code>Tk_ObjCustomOption</code>;
typedef int <code>Tk_CustomOptionSetProc</code>(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 Tk_Window <i>tkwin</i>,
 Tcl_Obj **<i>valuePtr</i>,
 char *<i>recordPtr</i>,
 int <i>internalOffset</i>,
 char *<i>saveInternalPtr</i>,
 int <i>flags</i>);
typedef Tcl_Obj *<code>Tk_CustomOptionGetProc</code>(
 ClientData <i>clientData</i>,
 Tk_Window <i>tkwin</i>,
 char *<i>recordPtr</i>,
 int <i>internalOffset</i>);
typedef void <code>Tk_CustomOptionRestoreProc</code>(
 ClientData <i>clientData</i>,
 Tk_Window <i>tkwin</i>,
 char *<i>internalPtr</i>,
 char *<i>saveInternalPtr</i>);
typedef void <code>Tk_CustomOptionFreeProc</code>(
 ClientData <i>clientData</i>,
 Tk_Window <i>tkwin</i>,
 char *<i>internalPtr</i>);</pre>
</dl>
<p> The Tk_ObjCustomOption structure contains six fields: a name for the custom option type; pointers to the four procedures; and a <i>clientData</i> value to be passed to those procedures when they are invoked. The <i>clientData</i> value typically points to a structure containing information that is needed by the procedures when they are parsing and printing options. <i>RestoreProc</i> and <i>freeProc</i> may be NULL, indicating that no function should be called for those operations. </p>
<p> The <i>setProc</i> procedure is invoked by <code>Tk_SetOptions</code> to convert a Tcl_Obj into an internal representation and store the resulting value in the widget record. The arguments are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>clientData</i></p>
<dd>A copy of the <i>clientData</i> field in the Tk_ObjCustomOption structure.</p>
<dt><i>interp</i></p>
<dd>A pointer to a Tcl interpreter, used for error reporting.</p>
<dt><i>Tkwin</i></p>
<dd>A copy of the <i>tkwin</i> argument to <code>Tk_SetOptions</code></p>
<dt><i>valuePtr</i></p>
<dd>A pointer to a reference to a Tcl_Obj describing the new value for the option; it could have been specified explicitly in the call to <code>Tk_SetOptions</code> or it could come from the option database or a default. If the objOffset for the option is non-negative (the option value is stored as a (Tcl_Obj *) in the widget record), the Tcl_Obj pointer referenced by <i>valuePtr</i> is the pointer that will be stored at the objOffset for the option. <i>SetProc</i> may modify the value if necessary; for example, <i>setProc</i> may change the value to NULL to support the <code>TK_OPTION_NULL_OK</code> flag.</p>
<dt><i>recordPtr</i></p>
<dd>A pointer to the start of the widget record to modify.</p>
<dt><i>internalOffset</i></p>
<dd>Offset in bytes from the start of the widget record to the location where the internal representation of the option value is to be placed.</p>
<dt><i>saveInternalPtr</i></p>
<dd>A pointer to storage allocated in a Tk_SavedOptions structure for the internal representation of the original option value. Before setting the option to its new value, <i>setProc</i> should set the value referenced by <i>saveInternalPtr</i> to the original value of the option in order to support <code>Tk_RestoreSavedOptions</code>.</p>
<dt><i>flags</i></p>
<dd>A copy of the <i>flags</i> field in the Tk_OptionSpec structure for the option</dl>
</dl>
<p> <i>SetProc</i> returns a standard Tcl result: <code>TCL_OK</code> to indicate successful processing, or <code>TCL_ERROR</code> to indicate a failure of any kind. An error message may be left in the Tcl interpreter given by <i>interp</i> in the case of an error. </p>
<p> The <i>getProc</i> procedure is invoked by <code>Tk_GetOptionValue</code> and <code>Tk_GetOptionInfo</code> to retrieve a Tcl_Obj representation of the internal representation of an option. The <i>clientData</i> argument is a copy of the <i>clientData</i> field in the Tk_ObjCustomOption structure. <i>Tkwin</i> is a copy of the <i>tkwin</i> argument to <code>Tk_GetOptionValue</code> or <code>Tk_GetOptionInfo</code>. <i>RecordPtr</i> is a pointer to the beginning of the widget record to query. <i>InternalOffset</i> is the offset in bytes from the beginning of the widget record to the location where the internal representation of the option value is stored. <i>GetProc</i> must return a pointer to a Tcl_Obj representing the value of the option. </p>
<p> The <i>restoreProc</i> procedure is invoked by <code>Tk_RestoreSavedOptions</code> to restore a previously saved internal representation of a custom option value. The <i>clientData</i> argument is a copy of the <i>clientData</i> field in the Tk_ObjCustomOption structure. <i>Tkwin</i> is a copy of the <i>tkwin</i> argument to <code>Tk_GetOptionValue</code> or <code>Tk_GetOptionInfo</code>. <i>InternalPtr</i> is a pointer to the location where internal representation of the option value is stored. <i>SaveInternalPtr</i> is a pointer to the saved value. <i>RestoreProc</i> must copy the value from <i>saveInternalPtr</i> to <i>internalPtr</i> to restore the value. <i>RestoreProc</i> need not free any memory associated with either <i>internalPtr</i> or <i>saveInternalPtr</i>; <i>freeProc</i> will be invoked to free that memory if necessary. <i>RestoreProc</i> has no return value. </p>
<p> The <i>freeProc</i> procedure is invoked by <code>Tk_SetOptions</code> and <code>Tk_FreeSavedOptions</code> to free any storage allocated for the internal representation of a custom option. The <i>clientData</i> argument is a copy of the <i>clientData</i> field in the Tk_ObjCustomOption structure. <i>Tkwin</i> is a copy of the <i>tkwin</i> argument to <code>Tk_GetOptionValue</code> or <code>Tk_GetOptionInfo</code>. <i>InternalPtr</i> is a pointer to the location where the internal representation of the option value is stored. The <i>freeProc</i> must free any storage associated with the option. <i>FreeProc</i> has no return value.</p>
<h2>Keywords</h2>
<p>anchor, bitmap, boolean, border, color, configuration option, cursor, double, font, integer, justify, pixels, relief, screen distance, synonym</p>
