---
title: "uil(5)"
name: "uil"
section: "5"
letter: "u"
url: "/docs/linux/man/5-uil/"
description: "UIL — The user interface language file format"
---

<p><code>UIL</code> &#8212; The user interface language file format</p>
<h2>Synopsis</h2>
<pre><code>MODULE module_name
[ NAMES = CASE_INSENSITIVE | CASE_SENSITIVE ]
[ CHARACTER_SET = character_set ]
[ OBJECTS = { widget_name = GADGET | WIDGET; [...] } ]
{ [
    [ value_section ] |
    [ procedure_section ] |
    [ list_section ] |
    [ object_section ] |
    [ identifier_section ]
    [ ... ]
    ] }
END MODULE;</code></pre>
<h2>Description</h2>
<p>The UIL language is used for describing the initial state of a user interface for a widget based application. UIL describes the widgets used in the interface, the resources of those widgets, and the callbacks of those widgets. The UIL file is compiled into a UID file using the command <code>uil</code> or by the callable compiler <code>Uil()</code>. The contents of the compiled UID file can then be accessed by the various Motif Resource Management (MRM) functions from within an application program. </p>
<p> The UID file is independent of the platform on which the Motif program will eventually be run. In other words, the same UID file can be used on any system that can run Motif.</p>
<h3>File</h3>
<p>A UIL file consists of a single complete module, described in the syntax description above, or, if the file is to be included in a larger UIL file, one complete &quot;section,&quot; as described below. UIL uses five different kinds of sections: value, procedure, list, object, and identifier. </p>
<p> UIL is a free-form language. This means that high-level constructs such as object and value declarations do not need to begin in any particular column and can span any number of lines. Low-level constructs such as keywords and punctuation characters can also begin in any column; however, except for string literals and comments, they cannot span lines. </p>
<p> The UIL compiler accepts input lines up to 132 characters in length.</p>
<dl>
<dt><code>MODULE</code> <i>module_name</i></p>
<dd>The name by which the UIL module is known in the UID file. This name is stored in the UID file for later use in the retrieval of resources by the MRM. This name is always stored in uppercase in the UID file.</p>
<dt><code>NAMES</code>&nbsp;<wbr><code>=</code>&nbsp;<wbr><code>CASE_INSENSITIVE</code>&nbsp;<wbr>|&nbsp;<wbr><code>CASE_SENSITIVE</code></p>
<dd>
<dd>Indicates whether names should be treated as case sensitive or case insensitive. The default is case sensitive. The case-sensitivity clause should be the first clause in the module header, and in any case must precede any statement that contains a name. If names are case sensitive in a UIL module, UIL keywords in that module must be in lowercase. Each name is stored in the UIL file in the same case as it appears in the UIL module. If names are case insensitive, then keywords can be in uppercase, lowercase, or mixed case, and the uppercase equivalent of each name is stored in the UID file.</p>
<dt><code>CHARACTER_SET</code>&nbsp;<wbr><code>=</code>&nbsp;<wbr><code>character_set</code></p>
<dd>
<dd>Specifies the default character set for string literals in the module that do not explicitly set their character set. The default character set, in the absence of this clause is the codeset component of the <code>LANG</code> environment variable, or the value of <code>XmFALLBACK_CHARSET</code> if <code>LANG</code> is not set or has no codeset component. The value of <code>XmFALLBACK_CHARSET</code> is defined by the UIL supplier, but is usually ISO8859-1 (equivalent to ISO_LATIN1). Use of this clause turns off all localized string literal processing turned on by the compiler flag <code>-s</code> or the <code>Uil_command_type</code> data structure element <code>use_setlocale_flag</code>.</p>
<dt><code>OBJECTS&nbsp;<wbr>=&nbsp;<wbr>{</code>&nbsp;<wbr><i>widget_name</i> = <code>GADGET</code> | <code>WIDGET;&nbsp;<wbr>}</code></p>
<dd>
<dd>Indicates whether the widget or gadget form of the control specified by <i>widget_name</i> is used by default. By default the widget form is used, so the gadget keyword is usually the only one used. The specified control should be one that has both a widget and gadget version: XmCascadeButton, XmLabel, XmPushButton, XmSeparator, and XmToggleButton. The form of more than one control can be specified by delimiting them with semicolons. The gadget or widget form of an instance of a control can be specified with the <code>GADGET</code> and <code>WIDGET</code> keywords in a particular object declaration.</p>
<dt><i>value_section</i></p>
<dd>Provides a way to name a value expression or literal. The value name can then be referred to by declarations that occur elsewhere in the UIL module in any context where a value can be used. Values can be forward referenced. Value sections are described in more detail later in the reference page.</p>
<dt><i>procedure_section</i></p>
<dd>Defines the callback routines used by a widget and the creation routines for user-defined widgets. These definitions are used for error checking. Procedure sections are described in more detail later in the reference page.</p>
<dt><i>list_section</i></p>
<dd>Provides a way to group together a set of arguments, controls (children), callbacks, or procedures for later use in the UIL module. Lists can contain other lists, so that you can set up a hierarchy to clearly show which arguments, controls, callbacks, and procedures are common to which widgets. List sections are described in more detail later in the reference page.</p>
<dt><i>object_section</i></p>
<dd>Defines the objects that make up the user interface of the application. You can reference the object names in declarations that occur elsewhere in the UIL module in any context where an object name can be used (for example, in a controls list, as a symbolic reference to a widget ID, or as the <i>tag_value</i> argument for a callback procedure). Objects can be forward referenced. Object sections are described in more detail later in the reference page.</p>
<dt><i>identifier_section</i></p>
<dd>Defines a run-time binding of data to names that appear in the UIL module. Identifier sections are described in more detail later in the reference page.</dl>
<p> The UIL file can also contain comments and include directives, which are described along with the main elements of the UIL file format in the following sections.</p>
<h3>Comments</h3>
<p>Comments can take one of two forms, as follows:</p>
<dl>
<dt> &bull;</p>
<dd>The comment is introduced with the sequence <code>/*</code> followed by the text of the comment and terminated with the sequence <code>*/</code>. This form of comment can span multiple source lines.</p>
<dt> &bull;</p>
<dd>The comment is introduced with an ! (exclamation point), followed by the text of the comment and terminated by the end of the source line.</dl>
<p> Neither form of comment can be nested.</p>
<h3>Value sections</h3>
<p>A value section consists of the keyword <code>VALUE</code> followed by a sequence of value declarations. It has the following syntax: </p>
<p> <code>VALUE</code> <i>value_name</i> <code>:</code> [ <code>EXPORTED</code> | <code>PRIVATE</code> ] <i>value_expression</i> | <code>IMPORTED</code> <i>value_type</i> <code>;</code> </p>
<p> Where <i>value_expression</i> is assigned to <i>value_name</i> or a <i>value_type</i> is assigned to an imported value name. A value declaration provides a way to name a value expression or literal. The value name can be referred to by declarations that occur later in the UIL module in any context where a value can be used. Values can be forward referenced.</p>
<dl>
<dt><code>EXPORTED</code></p>
<dd>A value that you define as exported is stored in the UID file as a named resource, and therefore can be referenced by name in other UID files. When you define a value as exported, MRM looks outside the module in which the exported value is declared to get its value at run time.</p>
<dt><code>PRIVATE</code></p>
<dd>A private value is a value that is not imported or exported. A value that you define as private is not stored as a distinct resource in the UID file. You can reference a private value only in the UIL module containing the value declaration. The value or object is directly incorporated into anything in the UIL module that references the declaration.</p>
<dt><code>IMPORTED</code></p>
<dd>A value that you define as imported is one that is defined as a named resource in a UID file. MRM resolves this declaration with the corresponding exported declaration at application run time.</dl>
<p> By default, values and objects are private. The following is a list of the supported value types in UIL:</p>
<dl>
<dt> &bull;</p>
<dd><code>ANY</code></p>
<dt> &bull;</p>
<dd><code>ARGUMENT</code></p>
<dt> &bull;</p>
<dd><code>BOOLEAN</code></p>
<dt> &bull;</p>
<dd><code>COLOR</code></p>
<dt> &bull;</p>
<dd><code>COLOR_TABLE</code></p>
<dt> &bull;</p>
<dd><code>COMPOUND_STRING</code></p>
<dt> &bull;</p>
<dd><code>FLOAT</code></p>
<dt> &bull;</p>
<dd><code>FONT</code></p>
<dt> &bull;</p>
<dd><code>FONT_TABLE</code></p>
<dt> &bull;</p>
<dd><code>FONTSET</code></p>
<dt> &bull;</p>
<dd><code>ICON</code></p>
<dt> &bull;</p>
<dd><code>INTEGER</code></p>
<dt> &bull;</p>
<dd><code>INTEGER_TABLE</code></p>
<dt> &bull;</p>
<dd><code>KEYSYM</code></p>
<dt> &bull;</p>
<dd><code>REASON</code></p>
<dt> &bull;</p>
<dd><code>SINGLE_FLOAT</code></p>
<dt> &bull;</p>
<dd><code>STRING</code></p>
<dt> &bull;</p>
<dd><code>STRING_TABLE</code></p>
<dt> &bull;</p>
<dd><code>TRANSLATION_TABLE</code></p>
<dt> &bull;</p>
<dd><code>WIDE_CHARACTER</code></p>
<dt> &bull;</p>
<dd><code>WIDGET</code></dl>
<h3>Procedure sections</h3>
<p>A procedure section consists of the keyword <code>PROCEDURE</code> followed by a sequence of procedure declarations. It has the following syntax: </p>
<pre>PROCEDURE
 <i>procedure_name</i> [ ( [ <i>value_type</i> ]) ];</pre>
<p>Use a procedure declaration to declare</p>
<dl>
<dt> &bull;</p>
<dd>A routine that can be used as a callback routine for a widget</p>
<dt> &bull;</p>
<dd>The creation function for a user-defined widget</dl>
<p> You can reference a procedure name in declarations that occur later in the UIL module in any context where a procedure can be used. Procedures can be forward referenced. You cannot use a name you used in another context as a procedure name. </p>
<p> In a procedure declaration, you have the option of specifying that a parameter will be passed to the corresponding callback routine at run time. This parameter is called the callback tag. You can specify the data type of the callback tag by putting the data type in parentheses following the procedure name. When you compile the module, the UIL compiler checks that the argument you specify in references to the procedure is of this type. Note that the data type of the callback tag must be one of the valid UIL data types. You can use a widget as a callback tag, as long as the widget is defined in the same widget hierarchy as the callback, that is they have a common ancestor that is in the same UIL hierarchy. </p>
<p> The following list summarizes how the UIL compiler checks argument type and argument count, depending on the procedure declaration.</p>
<dl>
<dt>No parameters</p>
<dd>No argument type or argument count checking occurs. You can supply either 0 or one arguments in the procedure reference.</p>
<dt><code>(&nbsp;<wbr>)</code></p>
<dd>Checks that the argument count is 0 (zero).</p>
<dt><code>(ANY)</code></p>
<dd>Checks that the argument count is 1. Does not check the argument type. Use the <code>ANY</code> type to prevent type checking on procedure tags.</p>
<dt><code>(</code><i>type</i><code>)</code></p>
<dd>Checks for one argument of the specified type.</p>
<dt><code>(</code><code>class_name</code><code>)</code></p>
<dd>Checks for one widget argument of the specified widget class.</dl>
<p> While it is possible to use any UIL data type to specify the type of a tag in a procedure declaration, you must be able to represent that data type in the programming language you are using. Some data types (such as integer, Boolean, and string) are common data types recognized by most programming languages. Other UIL data types (such as string tables) are more complicated and may require that you set up an appropriate corresponding data structure in the application in order to pass a tag of that type to a callback routine. </p>
<p> You can also use a procedure declaration to specify the creation function for a user-defined widget. In this case, you specify no formal parameters. The procedure is invoked with the standard three arguments passed to all widget creation functions. (See the Motif Toolkit documentation for more information about widget creation functions.)</p>
<h3>List sections</h3>
<p>A list section consists of the keyword <code>LIST</code> followed by a sequence of list declarations. It has the following syntax: </p>
<pre>LIST
 <i>list_name</i>: { list_item; [...] }
 [...]</pre>
<p>You can also use list sections to group together a set of arguments, controls (children), callbacks, or procedures for later use in the UIL module. Lists can contain other lists, so that you can set up a hierarchy to clearly show which arguments, controls, callbacks, and procedures are common to which widgets. You cannot mix the different types of lists; a list of a particular type cannot contain entries of a different list type or reference the name of a different list type. A list name is always private to the UIL module in which you declare the list and cannot be stored as a named resource in a UID file. </p>
<p> The additional list types are described in the following sections. </p>
<p> <code>Arguments List Structure</code> </p>
<p> An arguments list defines which arguments are to be specified in the arguments list parameter when the creation routine for a particular object is called at run time. An arguments list also specifies the values for those arguments. Argument lists have the following syntax: </p>
<pre>LIST
 <i>list_name</i>: ARGUMENTS {
 <i>argument_name</i> = <i>value_expression</i>;
 [...] }
[...]</pre>
<p>The argument name must be either a built-in argument name or a user-defined argument name that is specified with the <code>ARGUMENT</code> function. </p>
<p> If you use a built-in argument name as an arguments list entry in an object definition, the UIL compiler checks the argument name to be sure that it is supported by the type of object that you are defining. If the same argument name appears more than once in a given arguments list, the last entry that uses that argument name supersedes all previous entries with that name, and the compiler issues a message. </p>
<p> Some arguments, such as <code>XmNitems</code> and <code>XmNitemCount</code>, are coupled by the UIL compiler. When you specify one of the arguments, the compiler also sets the other. The coupled argument is not available to you. </p>
<p> The Motif Toolkit and the X Toolkit (intrinsics) support constraint arguments. A constraint argument is one that is passed to children of an object, beyond those arguments normally available. For example, the Form widget grants a set of constraint arguments to its children. These arguments control the position of the children within the Form. </p>
<p> Unlike the arguments used to define the attributes of a particular widget, constraint arguments are used exclusively to define additional attributes of the children of a particular widget. These attributes affect the behavior of the children within their parent. To supply constraint arguments to the children, you include the arguments in the arguments list for the child. </p>
<p> See <code>Appendix B</code> for information about which arguments are supported by which widgets. See <code>Appendix C</code> for information about what the valid value type is for each built-in argument. </p>
<p> <code>Callbacks List Structure</code> </p>
<p> Use a callbacks list to define which callback reasons are to be processed by a particular widget at run time. Callback lists have the following syntax: </p>
<p> <code>LIST</code> <i>list_name</i> <code>: CALLBACKS {</code> <i>reason_name</i> <code>= PROCEDURE</code> <i>procedure_name</i> <code>[</code> <code>(</code> [ <i>value_expression</i> ] <code>)</code> ]<code>;</code> | <i>reason_name</i> <code>=</code> <i>procedure_list</i> <code>;</code> [&#8230;] <code>}</code> [&#8230;] </p>
<p> For Motif Toolkit widgets, the reason name must be a built-in reason name. For a user-defined widget, you can use a reason name that you previously specified using the <code>REASON</code> function. If you use a built-in reason in an object definition, the UIL compiler ensures that reason is supported by the type of object you are defining. Appendix B shows which reasons each object supports. </p>
<p> If the same reason appears more than once in a callbacks list, the last entry referring to that name supersedes all previous entries using the same reason, and the UIL compiler issues a diagnostic message. </p>
<p> If you specify a named value for the procedure argument (callback tag), the data type of the value must match the type specified for the callback tag in the corresponding procedure declaration. When specifying a widget name as a procedure value expression you must also specify the type of the widget and a space before the name of the widget. </p>
<p> Because the UIL compiler produces a UID file rather than an object module (.o), the binding of the UIL name to the address of the entry point to the procedure is not done by the loader, but is established at run time with the MRM function <code>MrmRegisterNames</code>. You call this function before fetching any objects, giving it both the UIL names and the procedure addresses of each callback. The name you register with MRM in the application program must match the name you specified for the procedure in the UIL module. </p>
<p> Each callback procedure receives three arguments. The first two arguments have the same form for each callback. The form of the third argument varies from object to object. </p>
<p> The first argument is the address of the data structure maintained by the Motif Toolkit for this object instance. This address is called the widget ID for this object. </p>
<p> The second argument is the address of the value you specified in the callbacks list for this procedure. If you do not specify an argument, the address is NULL. Note that, in the case where the value you specified is a string or an <code>XmString</code>, the value specified in the callbacks list already represents an address rather than an actual value. In the case of a simple string, for example, the value is the address of the first character of that string. In these cases, UIL does not add a level of indirection, and the second argument to the callback procedure is simply the value as specified in the callbacks list. </p>
<p> The third argument is the reason name you specified in the callbacks list. </p>
<p> <code>Controls List Structure</code> </p>
<p> A controls list defines which objects are children of, or controlled by, a particular object. Each entry in a controls list has the following syntax: </p>
<pre>LIST
 <i>list_name</i>: CONTROLS {
 [<i>child_name</i>: ] [MANAGED | UNMANAGED] <i>object_definition</i>;
 [...] }
 [...]</pre>
<p>If you specify the keyword <code>MANAGED</code> at run time, the object is created and managed; if you specify <code>UNMANAGED</code> at run time, the object is only created. Objects are managed by default. </p>
<p> You can use <i>child_name</i> to specify resources for the automatically created children of a particular control. Names for automatically created children are formed by appending <code>Xm_</code> to the name of the child widget. This name is specified in the documentation for the parent widget. </p>
<p> Unlike the arguments list and the callbacks list, a controls list entry that is identical to a previous entry does not supersede the previous entry. At run time, each controls list entry causes a child to be created when the parent is created. If the same object definition is used for multiple children, multiple instances of the child are created at run time. See <code>Appendix B</code> for a list of which widget types can be controlled by which other widget types. </p>
<p> <code>Procedures List Structure</code> </p>
<p> You can specify multiple procedures for a callback reason in UIL by defining a procedures list. Just as with other list types, procedures lists can be defined in-line or in a list section and referenced by name. </p>
<p> If you define a reason more than once (for example, when the reason is defined both in a referenced procedures list and in the callbacks list for the object), previous definitions are overridden by the latest definition. The syntax for a procedures list is as follows: </p>
<pre>LIST
 <i>list_name</i>: PROCEDURES {
 <i>procedure_name</i> [ ( [ <i>value_expression</i> ]) ];
 [...] }
 [...]</pre>
<p>When specifying a widget name as a procedure value expression you must also specify the type of the widget and a space before the name of the widget.</p>
<h3>Object Sections</h3>
<p>An object section consists of the keyword <code>OBJECT</code> followed by a sequence of object declarations. It has the following syntax: </p>
<pre>OBJECT <i>object_name</i>:
 [ EXPORTED | PRIVATE | IMPORTED ] <i>object_type</i>
 [ PROCEDURE <i>creation_function</i> ]
 [ <i>object_name</i> [ WIDGET | GADGET ] | {<i>list_definitions</i> } ]</pre>
<p>Use an object declaration to define the objects that are to be stored in the UID file. You can reference the object name in declarations that occur elsewhere in the UIL module in any context where an object name can be used (for example, in a controls list, as a symbolic reference to a widget ID, or as the <i>tag_value</i> argument for a callback procedure). Objects can be forward referenced; that is, you can declare an object name after you reference it. All references to an object name must be consistent with the type of the object, as specified in the object declaration. You can specify an object as exported, imported, or private. </p>
<p> The object definition can contain a sequence of lists that define the arguments, hierarchy, and callbacks for the widget. You can specify only one list of each type for an object. When you declare a user-defined widget, you must include a reference to the widget creation function for the user-defined widget. </p>
<p> Note: Several widgets in the Motif Toolkit actually consist of two linked widgets. For example, <code>XmScrolledText</code> and <code>XmScrolledList</code> each consist of children <code>XmText</code> and <code>XmList</code> widgets under a <code>XmScrolledWindow</code> widget. When such a widget is created, its resources are available to both of the underlying widgets. This can occasionally cause problems, as when the programmer wants a <code>XmNdestroyCallback</code> routine named to act when the widget is destroyed. In this case, the callback resource will be available to both sub-widgets, and will cause an error when the widget is destroyed. To avoid these problems, the programmer should separately create the parent and child widgets, rather than relying on these linked widgets. </p>
<p> Use the <code>GADGET</code> or <code>WIDGET</code> keyword to specify the object type or to override the default variant for this object type. You can use the Motif Toolkit name of an object type that has a gadget variant (for example, <code>XmLabelGadget</code>) as an attribute of an object declaration. The <i>object_type</i> can be any object type, including gadgets. You need to specify the <code>GADGET</code> or <code>WIDGET</code> keyword only in the declaration of an object, not when you reference the object. You cannot specify the <code>GADGET</code> or <code>WIDGET</code> keyword for a user-defined object; user-defined objects are always widgets.</p>
<h3>Identifier sections</h3>
<p>The identifier section allows you to define an identifier, a mechanism that achieves run-time binding of data to names that appear in a UIL module. The identifier section consists of the reserved keyword <code>IDENTIFIER</code>, followed by a list of names, each name followed by a semicolon. </p>
<p> <code>IDENTIFIER</code> <i>identifier_name</i><code>;</code> [&#8230;<code>;</code>] </p>
<p> You can later use these names in the UIL module as either the value of an argument to a widget or the tag value to a callback procedure. At run time, you use the MRM functions <code>MrmRegisterNames</code> and <code>MrmRegisterNamesInHierarchy</code> to bind the identifier name with the data (or, in the case of callbacks, with the address of the data) associated with the identifier. </p>
<p> Each UIL module has a single name space; therefore, you cannot use a name you used for a value, object, or procedure as an identifier name in the same module. </p>
<p> The UIL compiler does not do any type checking on the use of identifiers in a UIL module. Unlike a UIL value, an identifier does not have a UIL type associated with it. Regardless of what particular type a widget argument or callback procedure tag is defined to be, you can use an identifier in that context instead of a value of the corresponding type. </p>
<p> To reference these identifier names in a UIL module, you use the name of the identifier wherever you want its value to be used.</p>
<h3>Include directives</h3>
<p>The include directive incorporates the contents of a specified file into a UIL module. This mechanism allows several UIL modules to share common definitions. The syntax for the include directive is as follows: </p>
<pre>INCLUDE FILE <i>file_name</i>;</pre>
<p>The UIL compiler replaces the include directive with the contents of the include file and processes it as if these contents had appeared in the current UIL source file. </p>
<p> You can nest include files; that is, an include file can contain include directives. The UIL compiler can process up to 100 references (including the file containing the UIL module). Therefore, you can include up to 99 files in a single UIL module, including nested files. Each time a file is opened counts as a reference, so including the same file twice counts as two references. </p>
<p> The <i>file_name</i> is a simple string containing a file specification that identifies the file to be included. The rules for finding the specified file are similar to the rules for finding header, or <code>.h</code> files using the include directive, <code>#include</code>, with a quoted string in C. The UIL uses the <code>-I</code> option for specifying a search directory for include files.</p>
<dl>
<dt> &bull;</p>
<dd>If you do not supply a directory, the UIL compiler searches for the include file in the directory of the main source file.</p>
<dt> &bull;</p>
<dd>If the compiler does not find the include file there, the compiler looks in the same directory as the source file.</p>
<dt> &bull;</p>
<dd>If you supply a directory, the UIL compiler searches only that directory for the file.</dl>
<h3>Names and Strings</h3>
<p>Names can consist of any of the characters A to Z, a to z, 0 to 9, $ (dollar sign), and _ (underscore). Names cannot begin with a digit (0 to 9). The maximum length of a name is 31 characters. </p>
<p> UIL gives you a choice of either case-sensitive or case-insensitive names through a clause in the <code>MODULE</code> header. For example, if names are case sensitive, the names &quot;sample&quot; and &quot;Sample&quot; are distinct from each other. If names are case insensitive, these names are treated as the same name and can be used interchangeably. By default, UIL assumes names are case sensitive. </p>
<p> In <code>CASE-INSENSITIVE</code> mode, the compiler outputs all names in the UID file in uppercase form. In <code>CASE-SENSITIVE</code> mode, names appear in the UIL file exactly as they appear in the source. </p>
<p> The following table lists the reserved keywords, which are not available for defining programmer defined names. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=4><code>Reserved Keywords</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ARGUMENTS</td>
<td>CALLBACKS</td>
<td>CONTROLS</td>
<td>END
</td>
</tr>
<tr VALIGN=top>
<td>EXPORTED</td>
<td>FALSE</td>
<td>GADGET</td>
<td>IDENTIFIER
</td>
</tr>
<tr VALIGN=top>
<td>INCLUDE</td>
<td>LIST</td>
<td>MODULE</td>
<td>OFF
</td>
</tr>
<tr VALIGN=top>
<td>ON</td>
<td>OBJECT</td>
<td>PRIVATE</td>
<td>PROCEDURE
</td>
</tr>
<tr VALIGN=top>
<td>PROCEDURES</td>
<td>TRUE</td>
<td>VALUE</td>
<td>WIDGET
</td>
</tr>
</table>
</table>
<p> The UIL unreserved keywords are described in the following list and table. These keywords can be used as programmer defined names, however, if you use any keyword as a name, you cannot use the UIL-supplied usage of that keyword.</p>
<dl>
<dt> &bull;</p>
<dd>Built-in argument names (for example, <code>XmNx</code>, <code>XmNheight</code>)</p>
<dt> &bull;</p>
<dd>Built-in reason names (for example, <code>XmNactivateCallback</code>, <code>XmNhelpCallback</code>)</p>
<dt> &bull;</p>
<dd>Character set names (for example, <code>ISO_LATIN1</code>, <code>ISO_HEBREW_LR</code>)</p>
<dt> &bull;</p>
<dd>Constant value names (for example, <code>XmMENU_OPTION</code>, <code>XmBROWSE_SELECT</code>)</p>
<dt> &bull;</p>
<dd>Object types (for example, <code>XmPushButton</code>, <code>XmBulletinBoard</code>) </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3><code>Unreserved Keywords</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ANY</td>
<td>ARGUMENT</td>
<td>ASCIZ_STRING_TABLE
</td>
</tr>
<tr VALIGN=top>
<td>ASCIZ_TABLE</td>
<td>BACKGROUND</td>
<td>BOOLEAN
</td>
</tr>
<tr VALIGN=top>
<td>CASE_INSENSITIVE</td>
<td>CASE_SENSITIVE</td>
<td>CHARACTER_SET
</td>
</tr>
<tr VALIGN=top>
<td>COLOR</td>
<td>COLOR_TABLE</td>
<td>COMPOUND_STRING
</td>
</tr>
<tr VALIGN=top>
<td>COMPOUND_STRING_COMPONENT</td>
<td>COMPOUND_STRING_TABLE</td>
<td>FILE
</td>
</tr>
<tr VALIGN=top>
<td>FLOAT</td>
<td>FONT</td>
<td>FONT_TABLE
</td>
</tr>
<tr VALIGN=top>
<td>FONTSET</td>
<td>FOREGROUND</td>
<td>ICON
</td>
</tr>
<tr VALIGN=top>
<td>IMPORTED</td>
<td>INTEGER</td>
<td>INTEGER_TABLE
</td>
</tr>
<tr VALIGN=top>
<td>KEYSYM</td>
<td>MANAGED</td>
<td>NAMES
</td>
</tr>
<tr VALIGN=top>
<td>OBJECTS</td>
<td>REASON</td>
<td>RGB
</td>
</tr>
<tr VALIGN=top>
<td>RIGHT_TO_LEFT</td>
<td>SINGLE_FLOAT</td>
<td>STRING
</td>
</tr>
<tr VALIGN=top>
<td>STRING_TABLE</td>
<td>TRANSLATION_TABLE</td>
<td>UNMANAGED
</td>
</tr>
<tr VALIGN=top>
<td>USER_DEFINED</td>
<td>VERSION</td>
<td>WIDE_CHARACTER
</td>
</tr>
<tr VALIGN=top>
<td>WIDGET</td>
<td>XBITMAPFILE</td>
<td>
</td>
</tr>
</table>
</table>
</dl>
<p> String literals can be composed of the uppercase and lowercase letters, digits, and punctuation characters. Spaces, tabs, and comments are special elements in the language. They are a means of delimiting other elements, such as two names. One or more of these elements can appear before or after any other element in the language. However, spaces, tabs, and comments that appear in string literals are treated as character sequences rather than delimiters.</p>
<h3>Data Types</h3>
<p>UIL provides literals for several of the value types it supports. Some of the value types are not supported as literals (for example, pixmaps and string tables). You can specify values for these types by using functions described in the <i>Functions</i> section. UIL directly supports the following literal types:</p>
<dl>
<dt> &bull;</p>
<dd>String literal</p>
<dt> &bull;</p>
<dd>Integer literal</p>
<dt> &bull;</p>
<dd>Boolean literal</p>
<dt> &bull;</p>
<dd>Floating-point literal</dl>
<p> UIL also includes the data type <code>ANY</code>, which is used to turn off compile time checking of data types.</p>
<h3>String Literals</h3>
<p>A string literal is a sequence of zero or more 8-bit or 16-bit characters or a combination delimited by <code>&#8216;</code> (single quotation marks) or <code>&quot;</code> (double quotation marks). String literals can also contain multibyte characters delimited with double quotation marks. String literals can be no more than 2000 characters long. </p>
<p> A single-quoted string literal can span multiple source lines. To continue a single-quoted string literal, terminate the continued line with a <code>\</code> (backslash). The literal continues with the first character on the next line. </p>
<p> Double-quoted string literals cannot span multiple source lines. (Because double-quoted strings can contain escape sequences and other special characters, you cannot use the backslash character to designate continuation of the string.) To build a string value that must span multiple source lines, use the concatenation operator described later in this section. </p>
<p> The syntax of a string literal is one of the following: </p>
<pre>'[<i>character_string</i>]'
[#<i>char_set</i>]&quot;[<i>character_string</i>]&quot;</pre>
<p>Both string forms associate a character set with a string value. UIL uses the following rules to determine the character set and storage format for string literals:</p>
<dl>
<dt> &bull;</p>
<dd>A string declared as <code>&#8216;</code><i>string</i><code>&#8216;</code> is equivalent to <code>#</code><i>cur_charset</i><code>&quot;</code><i>string</i><code>&quot;</code>, where <i>cur_charset</i> will be the codeset portion of the value of the <code>LANG</code> environment variable if it is set or the value of <code>XmFALLBACK_CHARSET</code> if <code>LANG</code> is not set or has no codeset component. By default, <code>XmFALLBACK_CHARSET</code> is <code>ISO8859-1</code> (equivalent to <code>ISO_LATIN1</code>), but vendors may define a different default.</p>
<dt> &bull;</p>
<dd>A string declared as <code>&quot;</code><i>string</i><code>&quot;</code> is equivalent to <code>#</code><i>char_set</i><code>&quot;</code><i>string</i><code>&quot;</code> if you specified <i>char_set</i> as the default character set for the module. If no default character set has been specified for the module, then if the <code>-s</code> option is provided to the <code>uil</code> command or the <code>use_setlocale_flag</code> is set for the callable compiler, <code>Uil()</code>, the string will be interpreted to be a string in the current locale. This means that the string is parsed in the locale of the user by calling <i>setlocale</i>, its charset is <code>XmFONTLIST_DEFAULT_TAG</code>, and that if the string is converted to a compound string, it is stored as a locale encoded text segment. Otherwise, <code>&quot;</code><i>string</i><code>&quot;</code> is equivalent to <code>#</code><i>cur_charset</i><code>&quot;</code><i>string</i><code>&quot;</code>, where <i>cur_charset</i> is interpreted as described for single quoted strings.</p>
<dt> &bull;</p>
<dd>A string of the form <code>&quot;</code><i>string</i><code>&quot;</code> or <code>#</code><i>char_set</i><code>&quot;</code><i>string</i><code>&quot;</code> is stored as a null-terminated string.</dl>
<p> If the <i>char_set</i> in a string specified in the form above is not a built-in charset, and is not a user-defined charset, the charset of the string will be set to <code>XmFONTLIST_DEFAULT_TAG</code>, and an informational message will be issued to the user to note that this substitution has been made. </p>
<p> The following table lists the character sets supported by the UIL compiler for string literals. Note that several UIL names map to the same character set. In some cases, the UIL name influences how string literals are read. For example, strings identified by a UIL character set name ending in <code>_LR</code> are read left-to-right. Names that end in a different number reflect different fonts (for example, ISO_LATIN1 or ISO_LATIN6). All character sets in this table are represented by 8 bits. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2><code>Supported Character Sets</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>UIL Name</code></td>
<td><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>ISO_LATIN1</code></td>
<td>GL: ASCII, GR: Latin-1 Supplement
</td>
</tr>
<tr VALIGN=top>
<td><code>ISO_LATIN2</code></td>
<td>GL: ASCII, GR: Latin-2 Supplement
</td>
</tr>
<tr VALIGN=top>
<td><code>ISO_ARABIC</code></td>
<td> GL: ASCII, GR: Latin-Arabic Supplement
</td>
</tr>
<tr VALIGN=top>
<td><code>ISO_LATIN6</code></td>
<td> GL: ASCII, GR: Latin-Arabic Supplement
</td>
</tr>
<tr VALIGN=top>
<td><code>ISO_GREEK</code></td>
<td> GL: ASCII, GR: Latin-Greek Supplement
</td>
</tr>
<tr VALIGN=top>
<td><code>ISO_LATIN7</code></td>
<td> GL: ASCII, GR: Latin-Greek Supplement
</td>
</tr>
<tr VALIGN=top>
<td><code>ISO_HEBREW</code></td>
<td> GL: ASCII, GR: Latin-Hebrew Supplement
</td>
</tr>
<tr VALIGN=top>
<td><code>ISO_LATIN8</code></td>
<td> GL: ASCII, GR: Latin-Hebrew Supplement
</td>
</tr>
<tr VALIGN=top>
<td><code>ISO_HEBREW_LR</code></td>
<td> GL: ASCII, GR: Latin-Hebrew Supplement
</td>
</tr>
<tr VALIGN=top>
<td><code>ISO_LATIN8_LR</code></td>
<td> GL: ASCII, GR: Latin-Hebrew Supplement
</td>
</tr>
<tr VALIGN=top>
<td><code>JIS_KATAKANA</code></td>
<td>GL: JIS Roman, GR: JIS Katakana
</td>
</tr>
</table>
</table>
<p> Following are the parsing rules for each of the character sets:</p>
<dl>
<dt>All character sets</p>
<dd>Character codes in the range 00&#8230;1F, 7F, and 80&#8230;9F are control characters including both bytes of 16-bit characters. The compiler flags these as illegal characters.</p>
<dt><code>ISO_LATIN1 ISO_LATIN2 ISO_LATIN3 ISO_GREEK ISO_LATIN4</code></p>
<dd>These sets are parsed from left to right. The escape sequences for null-terminated strings are also supported by these character sets.</p>
<dt><code>ISO_HEBREW ISO_ARABIC ISO_LATIN8</code></p>
<dd>These sets are parsed from right to left. For example, the string <tt>#ISO_HEBREW&quot;012345&quot;</tt> will generate a primitive string of &quot;543210&quot; with character set <code>ISO_HEBREW</code>. The string direction for such a string would be right-to-left, so when rendered, the string will appear as &quot;012345.&quot; The escape sequences for null-terminated strings are also supported by these character sets, and the characters that compose the escape sequences are in left-to-right order. For example, you would enter 
, not n\.</p>
<dt><code>ISO_HEBREW_LR ISO_ARABIC_LR ISO_LATIN8_LR</code></p>
<dd>These sets are parsed from left to right. For example, the string <tt>#ISO_HEBREW_LR&quot;012345&quot;</tt> generates a primitive string &quot;012345&quot; with character set <code>ISO_HEBREW</code>. The string direction for such a string would still be right-to-left, however, so when rendered, it will appear as &quot;543210.&quot; In other words, the characters were originally typed in the <i>same order</i> in which they would have been typed in Hebrew (although in Hebrew, the typist would have been using a text editor that went from right to left). The escape sequences for null-terminated strings are also supported by these character sets.</p>
<dt><code>JIS_KATAKANA</code></p>
<dd>This set is parsed from left to right. The escape sequences for null-terminated strings are also supported by this character set. Note that the <code>\</code> (backslash) may be displayed as a yen symbol.</dl>
<p> In addition to designating parsing rules for strings, character set information remains an attribute of a compound string. If the string is included in a string consisting of several concatenated segments, the character set information is included with that string segment. This gives the Motif Toolkit the information it needs to decipher the compound string and choose a font to display the string. </p>
<p> For an application interface displayed only in English, UIL lets you ignore the distinctions between the two uses of strings. The compiler recognizes by context when a string must be passed as a null-terminated string or as a compound string. </p>
<p> The UIL compiler recognizes enough about the various character sets to correctly parse string literals. The compiler also issues errors if you use a compound string in a context that supports only null-terminated strings. </p>
<p> Since the character set names are keywords, you must put them in lowercase if case-sensitive names are in force. If names are case insensitive, character set names can be uppercase, lowercase, or mixed case. </p>
<p> In addition to the built-in character sets recognized by UIL, you can define your own character sets with the <code>CHARACTER_SET</code> function. You can use the <code>CHARACTER_SET</code> function anywhere a character set can be specified. </p>
<p> String literals can contain characters with the eighth (high-order) bit set. You cannot type control characters (00-1F, 7F, and 80-9F) directly in a single-quoted string literal. However, you can represent these characters with escape sequences. The following list shows the escape sequences for special characters.</p>
<dl>
<dt><code></code></p>
<dd>Backspace</p>
<dt><code></code></p>
<dd>Form-feed</p>
<dt><code>
</code></p>
<dd>Newline</p>
<dt><code></code></p>
<dd>Carriage return</p>
<dt><code>	</code></p>
<dd>Horizontal tab</p>
<dt><code></code></p>
<dd>Vertical tab</p>
<dt><code>\&#8217;</code></p>
<dd>Single quotation mark</p>
<dt><code>\&quot;</code></p>
<dd>Double quotation mark</p>
<dt><code>\</code></p>
<dd>Backslash</p>
<dt><code>\</code><i>integer</i><code>\</code></p>
<dd>Character whose internal representation is given by <i>integer</i> (in the range 0 to 255 decimal)</dl>
<p> Note that escape sequences are processed literally in strings that are parsed in the current locale (localized strings). </p>
<p> The UIL compiler does not process newline characters in compound strings. The effect of a newline character in a compound string depends only on the character set of the string, and the result is not guaranteed to be a multiline string. </p>
<p> <code>Compound String Literals</code> </p>
<p> A compound string consists of a string of 8-bit, 16-bit, or multibyte characters, a named character set, and a writing direction. Its UIL data type is <code>compound_string</code>. </p>
<p> The writing direction of a compound string is implied by the character set specified for the string. You can explicitly set the writing direction for a compound string by using the <code>COMPOUND_STRING</code> function. </p>
<p> A compound string can consist of a sequence of concatenated compound strings, null-terminated strings, or a combination of both, each of which can have a different character set property and writing direction. Use the concatenation operator &amp; (ampersand) to create a sequence of compound strings. </p>
<p> Each string in the sequence is stored, including the character set and writing direction information. </p>
<p> Generally, a string literal is stored in the UID file as a compound string when the literal consists of concatenated strings having different character sets or writing directions, or when you use the string to specify a value for an argument that requires a compound string value. If you want to guarantee that a string literal is stored as a compound string, you must use the <code>COMPOUND_STRING</code> function. </p>
<p> <code>Data Storage Consumption for String Literals</code> </p>
<p> The way a string literal is stored in the UID file depends on how you declare and use the string. The UIL compiler automatically converts a null-terminated string to a compound string if you use the string to specify the value of an argument that requires a compound string. However, this conversion is costly in terms of storage consumption. </p>
<p> <code>PRIVATE</code>, <code>EXPORTED</code>, and <code>IMPORTED</code> string literals require storage for a single allocation when the literal is declared; thereafter, storage is required for each reference to the literal. Literals declared in-line require storage for both an allocation and a reference. </p>
<p> The following table summarizes data storage consumption for string literals. The storage requirement for an allocation consists of a fixed portion and a variable portion. The fixed portion of an allocation is roughly the same as the storage requirement for a reference (a few bytes). The storage consumed by the variable portion depends on the size of the literal value (that is, the length of the string). To conserve storage space, avoid making string literal declarations that result in an allocation per use. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=4> <code>Data Storage Consumption for String Literals</code>
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Storage Requirements</code></td>
</tr>
<tr VALIGN=top>
<td><code>Per Use</code></td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td VALIGN=center ROWSPAN=2>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> An allocation and a reference (within the module) </td>
</tr>
<tr VALIGN=top>
<td>A reference (within the module)</td>
</tr>
<tr VALIGN=top>
<td> A reference (within the UID hierarchy) </td>
</tr>
<tr VALIGN=top>
<td> A reference (within the UID hierarchy) </td>
</tr>
<tr VALIGN=top>
<td> An allocation and a reference (within the module) </td>
</tr>
<tr VALIGN=top>
<td> An allocation and a reference (within the module) </td>
</tr>
<tr VALIGN=top>
<td> A reference (within the UID hierarchy) </td>
</tr>
<tr VALIGN=top>
<td> A reference (within the UID hierarchy) </td>
</tr>
<tr VALIGN=top>
<td> An allocation and a reference (within the module) </td>
</tr>
<tr VALIGN=top>
<td>A reference (within the module)</td>
</tr>
<tr VALIGN=top>
<td> A reference (within the UID hierarchy) </td>
</tr>
<tr VALIGN=top>
<td> A reference (within the UID hierarchy) </td>
</tr>
</table>
</table>
<h3>Integer Literals</h3>
<p>An integer literal represents the value of a whole number. Integer literals have the form of an optional sign followed by one or more decimal digits. An integer literal must not contain embedded spaces or commas. </p>
<p> Integer literals are stored in the UID file as 32-bit integers. Exported and imported integer literals require a single allocation when the literal is declared; thereafter, a few bytes of storage are required for each reference to the literal. Private integer literals and those declared in-line require allocation and reference storage per use. To conserve storage space, avoid making integer literal declarations that result in an allocation per use. </p>
<p> The following table shows data storage consumption for integer literals. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2> <code>Data Storage Consumption for Integer Literals</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Declaration</code></td>
<td><code>Storage Requirements Per Use</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>In-line</td>
<td> An allocation and a reference (within the module)
</td>
</tr>
<tr VALIGN=top>
<td>Private</td>
<td> An allocation and a reference (within the module)
</td>
</tr>
<tr VALIGN=top>
<td>Exported</td>
<td> A reference (within the UID hierarchy)
</td>
</tr>
<tr VALIGN=top>
<td>Imported</td>
<td> A reference (within the UID hierarchy)
</td>
</tr>
</table>
</table>
<h3>Boolean Literal</h3>
<p>A Boolean literal represents the value True (reserved keyword <code>TRUE</code> or <code>On</code>) or False (reserved keyword <code>FALSE</code> or <code>Off</code>). These keywords are subject to case-sensitivity rules. </p>
<p> In a UID file, <code>TRUE</code> is represented by the integer value 1 and <code>FALSE</code> is represented by the integer value 0 (zero). </p>
<p> Data storage consumption for Boolean literals is the same as that for integer literals.</p>
<h3>Floating-Point Literal</h3>
<p>A floating-point literal represents the value of a real (or float) number. Floating-point literals have the following form: </p>
<pre>[+|-][<i>integer</i>].<i>integer</i>[E|e[+|-]<i>exponent</i>]</pre>
<p>For maximum portability, a floating-point literal can represent values in the range 1.0E-37 to 1.0E+37 with at least 6 significant digits. On many machines this range will be wider, with more significant digits. A floating-point literal must not contain embedded spaces or commas. </p>
<p> Floating-point literals are stored in the UID file as double-precision, floating-point numbers. The following table gives examples of valid and invalid floating-point notation for the UIL compiler. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2><code>Floating Point Literals</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Valid Floating-Point Literals</code></td>
<td><code>Invalid Floating-Point Literals</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>1.0</td>
<td>1e1 (no decimal point)
</td>
</tr>
<tr VALIGN=top>
<td> 3.1415E-2 (equals .031415) </td>
<td>2.87 e6 (embedded blanks)
</td>
</tr>
<tr VALIGN=top>
<td> -6.29e7 (equals -62900000) </td>
<td>2.0e100 (out of range)
</td>
</tr>
</table>
</table>
<p> Data storage consumption for floating-point literals is the same as that for integer literals. </p>
<p> The purpose of the <code>ANY</code> data type is to shut off the data-type checking feature of the UIL compiler. You can use the <code>ANY</code> data type for the following:</p>
<dl>
<dt> &bull;</p>
<dd>Specifying the type of a callback procedure tag</p>
<dt> &bull;</p>
<dd>Specifying the type of a user-defined argument</dl>
<p> You can use the <code>ANY</code> data type when you need to use a type not supported by the UIL compiler or when you want the data-type restrictions imposed by the compiler to be relaxed. For example, you might want to define a widget having an argument that can accept different types of values, depending on run-time circumstances. </p>
<p> If you specify that an argument takes an <code>ANY</code> value, the compiler does not check the type of the value specified for that argument; therefore, you need to take care when specifying a value for an argument of type <code>ANY</code>. You could get unexpected results at run time if you pass a value having a data type that the widget does not support for that argument.</p>
<h3>Expressions</h3>
<p>UIL includes compile-time value expressions. These expressions can contain references to other UIL values, but cannot be forward referenced. </p>
<p> The following table lists the set of operators in UIL that allow you to create integer, real, and Boolean values based on other values defined with the UIL module. In the table, a precedence of 1 is the highest. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td COLSPAN=4><code>Valid Operators</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>Operator</code></td>
<td><code>Operand Types</code></td>
<td><code>Meaning</code></td>
<td ALIGN=center><code>Precedence</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>~</td>
<td>Boolean</td>
<td>NOT</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>integer</td>
<td>One&#8217;s complement</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>&#8211;</td>
<td>float</td>
<td>Negate</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>integer</td>
<td>Negate</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>+</td>
<td>float</td>
<td>NOP</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>integer</td>
<td>NOP</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>*</td>
<td>float,float</td>
<td>Multiply</td>
<td ALIGN=center>2
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>integer,integer</td>
<td>Multiply</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>/</td>
<td>float,float</td>
<td>Divide</td>
<td ALIGN=center>2
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>integer,integer</td>
<td>Divide</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>+</td>
<td>float,float</td>
<td>Add</td>
<td ALIGN=center>3
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>integer,integer</td>
<td>Add</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>&#8211;</td>
<td>float,float</td>
<td>Subtract</td>
<td ALIGN=center>3
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>integer,integer</td>
<td>Subtract</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>&gt;&gt;</td>
<td>integer,integer</td>
<td>Shift right</td>
<td ALIGN=center>4
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>&lt;&lt;</td>
<td>integer,integer</td>
<td>Shift left</td>
<td ALIGN=center>4
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>&amp;</td>
<td>Boolean,Boolean</td>
<td>AND</td>
<td ALIGN=center>5
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>integer,integer</td>
<td>Bitwise AND</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>string,string</td>
<td>Concatenate</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>|</td>
<td>Boolean,Boolean</td>
<td>OR</td>
<td ALIGN=center>6
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>integer,integer</td>
<td>Bitwise OR</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>^</td>
<td>Boolean,Boolean</td>
<td>XOR</td>
<td ALIGN=center>6
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td>integer,integer</td>
<td>Bitwise XOR</td>
<td ALIGN=center>
</td>
</tr>
</table>
</table>
<p> A string can be either a single compound string or a sequence of compound strings. If the two concatenated strings have different properties (such as writing direction or character set), the result of the concatenation is a multisegment compound string. </p>
<p> The string resulting from the concatenation is a null-terminated string unless one or more of the following conditions exists:</p>
<dl>
<dt> &bull;</p>
<dd>One of the operands is a compound string</p>
<dt> &bull;</p>
<dd>The operands have different character set properties</p>
<dt> &bull;</p>
<dd>The operands have different writing directions</dl>
<p> Then the resulting string is a compound string. You cannot use imported or exported values as operands of the concatenation operator. </p>
<p> The result of each operator has the same type as its operands. You cannot mix types in an expression without using conversion routines. </p>
<p> You can use parentheses to override the normal precedence of operators. In a sequence of unary operators, the operations are performed in right-to-left order. For example, <code>&#8211; + -A</code> is equivalent to <code>-(+(-A))</code>. In a sequence of binary operators of the same precedence, the operations are performed in left-to-right order. For example, <code>A*B/C*D</code> is equivalent to <code>((A*B)/C)*D</code>. </p>
<p> A value declaration gives a value a name. You cannot redefine the value of that name in a subsequent value declaration. You can use a value containing operators and functions anywhere you can use a value in a UIL module. You cannot use imported values as operands in expressions. </p>
<p> Several of the binary operators are defined for multiple data types. For example, the operator for multiplication (<code>*</code>) is defined for both floating-point and integer operands. </p>
<p> For the UIL compiler to perform these binary operations, both operands must be of the same type. If you supply operands of different data types, the UIL compiler automatically converts one of the operands to the type of the other according to the following conversions rules:</p>
<dl>
<dt> &bull;</p>
<dd>If the operands are an integer and a Boolean, the Boolean is converted to an integer.</p>
<dt> &bull;</p>
<dd>If the operands are an integer and a floating-point, the integer is converted to an floating-point.</p>
<dt> &bull;</p>
<dd>If the operands are a floating-point and a Boolean, the Boolean is converted to a floating-point.</dl>
<p> You can also explicitly convert the data type of a value by using one of the conversion functions <code>INTEGER</code>, <code>FLOAT</code> or <code>SINGLE_FLOAT</code>.</p>
<h3>Functions</h3>
<p>UIL provides functions to generate the following types of values:</p>
<dl>
<dt> &bull;</p>
<dd>Character sets</p>
<dt> &bull;</p>
<dd>Keysyms</p>
<dt> &bull;</p>
<dd>Colors</p>
<dt> &bull;</p>
<dd>Pixmaps</p>
<dt> &bull;</p>
<dd>Single-precision, floating-point numbers</p>
<dt> &bull;</p>
<dd>Double-precision, floating-point numbers</p>
<dt> &bull;</p>
<dd>Fonts</p>
<dt> &bull;</p>
<dd>Fontsets</p>
<dt> &bull;</p>
<dd>Font tables</p>
<dt> &bull;</p>
<dd>Compound strings</p>
<dt> &bull;</p>
<dd>Compound string tables</p>
<dt> &bull;</p>
<dd>ASCIZ (null-terminated) string tables</p>
<dt> &bull;</p>
<dd>Wide character strings</p>
<dt> &bull;</p>
<dd>Widget class names</p>
<dt> &bull;</p>
<dd>Integer tables</p>
<dt> &bull;</p>
<dd>Arguments</p>
<dt> &bull;</p>
<dd>Reasons</p>
<dt> &bull;</p>
<dd>Translation tables</dl>
<p> Remember that all examples in the following sections assume case-insensitive mode. Keywords are shown in uppercase letters to distinguish them from user-specified names, which are shown in lowercase letters. This use of uppercase letters is not required in case-insensitive mode. In case-sensitive mode, keywords must be in lowercase letters.</p>
<dl>
<dt><code>CHARACTER_SET(</code><i>string_expression[</i>, property[, &#8230;]]<code>)</code></p>
<dd>
<dd>You can define your own character sets with the <code>CHARACTER_SET</code> function. You can use the <code>CHARACTER_SET</code> function anywhere a character set can be specified.</p>
<dd>The result of the <code>CHARACTER_SET</code> function is a character set with the name <code>string_expression</code> and the properties you specify. <code>string_expression</code> must be a null-terminated string. You can optionally include one or both of the following clauses to specify properties for the resulting character set:</dl>
<pre>RIGHT_TO_LEFT = <i>boolean_expression</i>
SIXTEEN_BIT = <i>boolean_expression</i></pre>
<dl>
<dd>The <code>RIGHT_TO_LEFT</code> clause sets the default writing direction of the string from right to left if <i>boolean_expression</i> is True, and right to left otherwise.</p>
<dd>The <code>SIXTEEN_BIT</code> clause allows the strings associated with this character set to be interpreted as 16-bit characters if <i>boolean_expression</i> is True, and 8-bit characters otherwise.</p>
<dt><code>KEYSYM(</code><i>string_literal</i><code>)</code></p>
<dd>
<dd>The <code>KEYSYM</code> function is used to specify a keysym for a mnemonic resource. <i>string_literal</i> must contain a valid <code>KeySym</code> name. (See XStringToKeysym(3 X11) for more information.)</p>
<dt><code>COLOR(</code><code>string_expression</code>[<code>,FOREGROUND</code>|<code>BACKGROUND</code>]<code>)</code></p>
<dd>
<dd>The <code>COLOR</code> function supports the definition of colors. Using the <code>COLOR</code> function, you can designate a value to specify a color and then use that value for arguments requiring a color value. The string expression names the color you want to define; the optional keywords <code>FOREGROUND</code> and <code>BACKGROUND</code> identify how the color is to be displayed on a monochrome device when the color is used in the definition of a color table.</p>
<dd>The UIL compiler does not have built-in color names. Colors are a server-dependent attribute of an object. Colors are defined on each server and may have different red-green-blue (RGB) values on each server. The string you specify as the color argument must be recognized by the server on which your application runs.</p>
<dd>In a UID file, UIL represents a color as a character string. MRM calls X translation routines that convert a color string to the device-specific pixel value. If you are running on a monochrome server, all colors translate to black or white. If you are on a color server, the color names translate to their proper colors if the following conditions are met:</p>
<dl>
<dd>
<dl>
<dt> &bull;</p>
<dd>The color is defined.</p>
<dt> &bull;</p>
<dd>The color map is not yet full.</dl>
</dl>
<dd>If the color map is full, even valid colors translate to black or white (foreground or background).</p>
<dd>Interfaces do not, in general, specify colors for widgets, so that the selection of colors can be controlled by the user through the <code>.Xdefaults</code> file.</p>
<dd>To write an application that runs on both monochrome and color devices, you need to specify which colors in a color table (defined with the <code>COLOR_TABLE</code> function) map to the background and which colors map to the foreground. UIL lets you use the <code>COLOR</code> function to designate this mapping in the definition of the color. The following example shows how to use the <code>COLOR</code> function to map the color red to the background color on a monochrome device:</dl>
<pre><tt>VALUE c: COLOR ( 'red',BACKGROUND );</tt></pre>
<dl>
<dd>The mapping comes into play only when the MRM is given a color and the application is to be displayed on a monochrome device. In this case, each color is considered to be in one of the following three categories:</p>
<dl>
<dd>
<dl>
<dt> &bull;</p>
<dd>The color is mapped to the background color on the monochrome device.</p>
<dt> &bull;</p>
<dd>The color is mapped to the foreground color on the monochrome device.</p>
<dt> &bull;</p>
<dd>Monochrome mapping is undefined for this color.</dl>
</dl>
<dd>If the color is mapped to the foreground or background color, MRM substitutes the foreground or background color, respectively. If you do not specify the monochrome mapping for a color, MRM passes the color string to the Motif Toolkit for mapping to the foreground or background color.</p>
<dt><code>RGB(</code><i>red_integer</i>,&nbsp;<wbr><i>green_integer</i>, <i>blue_integer</i><code>)</code></p>
<dd>
<dd>The three integers define the values for the red, green, and blue components of the color, in that order. The values of these components can range from 0 to 65,535, inclusive. The values may be represented as integer expressions.</p>
<dd>In a UID file, UIL represents an <code>RGB</code> value as three integers. MRM calls X translation routines that convert the integers to the device-specific pixel value. If you are running on a monochrome server, all colors translate to black or white. If you are on a color server, <code>RGB</code> values translate to their proper colors if the colormap is not yet full. If the colormap is full, values translate to black or white (foreground or background).</p>
<dt><code>COLOR_TABLE(</code><i>color_expression</i><code>=&#8217;</code><i>character</i><code>&#8216;</code>[,&#8230;]<code>)</code></p>
<dd>
<dd>The color expression is a previously defined color, a color defined in line with the <code>COLOR</code> function, or the phrase <code>BACKGROUND COLOR</code> or <code>FOREGROUND COLOR</code>. The character can be any valid UIL character.</p>
<dd>The <code>COLOR_TABLE</code> function provides a device-independent way to specify a set of colors. The <code>COLOR_TABLE</code> function accepts either previously defined UIL color names or in line color definitions (using the <code>COLOR</code> function). A color table must be private because its contents must be known by the UIL compiler to construct an icon. The colors within a color table, however, can be imported, exported, or private.</p>
<dd>The single letter associated with each color is the character you use to represent that color when creating an icon. Each letter used to represent a color must be unique within the color table.</p>
<dt><code>ICON(</code>[<code>COLOR_TABLE=</code><i>color_table_name</i>,]&nbsp;<wbr><i>row</i>[,&#8230;<code>)</code></p>
<dd><i>color-table-name</i> must refer to a previously defined color table, and <i>row</i> is a character expression giving one row of the icon.</p>
<dd>The <code>ICON</code> function describes a rectangular icon that is x pixels wide and y pixels high. The strings surrounded by single quotation marks describe the icon. Each string represents a row in the icon; each character in the string represents a pixel.</p>
<dd>The first row in an icon definition determines the width of the icon. All rows must have the same number of characters as the first row. The height of the icon is dictated by the number of rows. The maximum number of rows is 999.</p>
<dd>The first argument of the <code>ICON</code> function (the color table specification) is optional and identifies the colors that are available in this icon. By using the single letter associated with each color, you can specify the color of each pixel in the icon. The icon must be constructed of characters defined in the specified color table.</p>
<dd>A default color table is used if you omit the argument specifying the color table. To make use of the default color table, the rows of your icon must contain only spaces and asterisks. The default color table is defined as follows:</dl>
<pre><tt>COLOR_TABLE( BACKGROUND COLOR = ' ', FOREGROUND COLOR = '*')</tt></pre>
<dl>
<dd>You can define other characters to represent the background color and foreground color by replacing the space and asterisk in the <code>BACKGROUND COLOR</code> and <code>FOREGROUND COLOR</code> clauses shown in the previous statement. You can specify icons as private, imported, or exported. Use the MRM function <code>MrmFetchIconLiteral</code> to retrieve an exported icon at run time.</p>
<dt><code>XBITMAPFILE(</code><code>string_expression</code><code>)</code></p>
<dd>The <code>XBITMAPFILE</code> function is similar to the <code>ICON</code> function in that both describe a rectangular icon that is x pixels wide and y pixels high. However, <code>XBITMAPFILE</code> allows you to specify an external file containing the definition of an X bitmap, whereas all <code>ICON</code> function definitions must be coded directly within UIL. X bitmap files can be generated by many different X applications. UIL reads these files through the <code>XBITMAPFILE</code> function, but does not support creation of these files. The X bitmap file specified as the argument to the <code>XBITMAPFILE</code> function is read at application run time by MRM.</p>
<dd>The <code>XBITMAPFILE</code> function returns a value of type <i>pixmap</i> and can be used anywhere a pixmap data type is expected.</p>
<dt><code>SINGLE_FLOAT(</code><i>real_number_literal</i><code>)</code></p>
<dd>
<dd>The <code>SINGLE_FLOAT</code> function lets you store floating-point literals in UIL files as single-precision, floating-point numbers. Single-precision floating-point numbers can often be stored using less memory than double-precision, floating-point numbers. The <i>real_number_literal</i> can be either an integer literal or a floating-point literal.</p>
<dt><code>FLOAT(</code><i>real_number_literal</i><code>)</code></p>
<dd>
<dd>The <code>FLOAT</code> function lets you store floating-point literals in UIL files as double-precision, floating-point numbers. The <i>real_number_literal</i> can be either an integer literal or a floating-point literal.</p>
<dt><code>FONT(</code><code>string_expression</code>[<code>, CHARACTER_SET=</code><i>char_set</i>]<code>)</code></p>
<dd>
<dd>You define fonts with the <code>FONT</code> function. Using the <code>FONT</code> function, you designate a value to specify a font and then use that value for arguments that require a font value. The UIL compiler has no built-in fonts.</p>
<dd>Each font makes sense only in the context of a character set. The <code>FONT</code> function has an additional parameter to let you specify the character set for the font. This parameter is optional; if you omit it, the default character set depends on the value of the <code>LANG</code> environment variable if it is set, or on the value of <code>XmFALLBACK_CHARSET</code> if <code>LANG</code> is not set.</p>
<dd><code>string_expression</code> specifies the name of the font and the clause <code>CHARACTER_SET</code> = <i>char_set</i> specifies the character set for the font. The string expression used in the <code>FONT</code> function cannot be a compound string.</p>
<dt><code>FONTSET(</code><code>string_expression</code>[,&#8230;][<code>, CHARACTER_SET=</code><i>charset</i>]<code>)</code></p>
<dd>
<dd>You define fontsets with the <code>FONTSET</code> function. Using the <code>FONTSET</code> function, you designate a set of values to specify fonts and then use those values for arguments that require a fontset. The UIL compiler has no built-in fonts.</p>
<dd>Each font makes sense only in the context of a character set. The <code>FONTSET</code> function has an additional parameter to let you specify the character set for the font. This parameter is optional; if you omit it, the default character set depends on the value of the <code>LANG</code> environment variable if it is set, or on the value of <code>XmFALLBACK_CHARSET</code> if <code>LANG</code> is not set.</p>
<dd>The string expression specifies the name of the font and the clause <code>CHARACTER_SET</code> = <i>char_set</i> specifies the character set for the font. The string expression used in the <code>FONTSET</code> function cannot be a compound string.</p>
<dt><code>FONT_TABLE(</code><i>font_expression</i>[,&#8230;]<code>)</code></p>
<dd>
<dd>A font table is a sequence of pairs of fonts and character sets. At run time, when an object needs to display a string, the object scans the font table for the character set that matches the character set of the string to be displayed. UIL provides the <code>FONT_TABLE</code> function to let you supply such an argument. <i>font_expression</i> is created with the <code>FONT</code> and <code>FONTSET</code> functions.</p>
<dd>If you specify a single font value to specify an argument that requires a font table, the UIL compiler automatically converts a font value to a font table.</p>
<dt><code>COMPOUND_STRING(</code><code>string_expression</code>[,<i>property</i>[,&#8230;]]<code>)</code></p>
<dd>Use the <code>COMPOUND_STRING</code> function to set properties of a null-terminated string and to convert it into a compound string. The properties you can set are the writing direction and separator.</p>
<dd>The result of the <code>COMPOUND_STRING</code> function is a compound string with the string expression as its value. You can optionally include one or more of the following clauses to specify properties for the resulting compound string:</p>
<dd><code>RIGHT_TO_LEFT</code> = <i>boolean_expression</i> <code>SEPARATE</code> = <i>boolean_expression</i></p>
<dd>The <code>RIGHT_TO_LEFT</code> clause sets the writing direction of the string from right to left if <i>boolean_expression</i> is True, and left to right otherwise. Specifying this argument does not cause the value of the string expression to change. If you omit the <code>RIGHT_TO_LEFT</code> argument, the resulting string has the same writing direction as <code>string_expression</code>.</p>
<dd>The <code>SEPARATE</code> clause appends a separator to the end of the compound string if <i>boolean_expression</i> is True. If you omit the <code>SEPARATE</code> clause, the resulting string does not have a separator.</p>
<dd>You cannot use imported or exported values as the operands of the <code>COMPOUND_STRING</code> function.</p>
<dt><code>COMPOUND_STRING_COMPONENT</code>(<i>component_type</i> [, {<i>string</i> | <i>enumval</i>}])</p>
<dd>Use the <code>COMPOUND_STRING_COMPONENT</code> function to create compound strings in UIL consisting of single components. This function is analagous to <code>XmStringComponentCreate</code>. This function lets you create simple compound strings containing components such as <code>XmSTRING_COMPONENT_TAB</code> and <code>XmSTRING_COMPONENT_RENDITION_BEGIN</code> which are not produced by the <code>COMPOUND_STRING</code> function. These components can then be concatenated to other compound strings to build more complex compound strings.</p>
<dd>The first argument must be an <code>XmStringComponentType</code> enumerated constant. The type and interpretation of the second argument depends on the first argument. For example, if you specify any of the following enumerated constants for the first argument, then you should not specify a second argument: <code>XmSTRING_COMPONENT_SEPARATOR</code>, <code>XmSTRING_COMPONENT_LAYOUT_POP</code>, <code>XmSTRING_COMPONENT_TAB</code>, and <code>XmSTRING_COMPONENT_LOCALE</code>. However, if you specify an enumerated constant from the following group, then you must supply a <i>string</i> as the second argument: <code>XmSTRING_COMPONENT_CHARSET</code>, <code>XmSTRING_COMPONENT_TEXT</code>, <code>XmSTRING_COMPONENT_LOCALE_TEXT</code>, <code>XmSTRING_COMPONENT_WIDECHAR_TEXT</code>, <code>XmSTRING_COMPONENT_RENDITION_BEGIN</code>, and <code>XmSTRING_COMPONENT_RENDITION_END</code>. If you specify <code>XmSTRING_COMPONENT_DIRECTION</code> as the first argument, then you must specify an <code>XmStringDirection</code> enumerated constant as the second argument. Finally, if you specify <code>XmSTRING_COMPONENT_LAYOUT_PUSH</code> as the first argument, then you must specify an <code>XmDirection</code> enumerated constant as the second argument.</p>
<dd>The compound string components <code>XmSTRING_COMPONENT_RENDITION_BEGIN</code>, and <code>XmSTRING_COMPONENT_RENDITION_END</code> take, for their argument, the &quot;tag,&quot; or name, of a rendition from the current render table. See the following section for more information about how to specify a render table.</p>
<dt><code>COMPOUND_STRING_TABLE(</code><code>string_expression</code>[,&#8230;]<code>)</code></p>
<dd>A compound string table is an array of compound strings. Objects requiring a list of string values, such as the <code>XmNitems</code> and <code>XmNselectedItems</code> arguments for the list widget, use string table values. The <code>COMPOUND_STRING_TABLE</code> function builds the values for these two arguments of the list widget. The <code>COMPOUND_STRING_TABLE</code> function generates a value of type <i>string_table</i>. The name <code>STRING_TABLE</code> is a synonym for <code>COMPOUND_STRING_TABLE</code>.</p>
<dd>The strings inside the string table must be simple strings, which the UIL compiler automatically converts to compound strings.</p>
<dt><code>ASCIZ_STRING_TABLE(</code><code>string_expression</code>[,&#8230;]<code>)</code></p>
<dd>An ASCIZ string table is an array of ASCIZ (null-terminated) string values separated by commas. This function allows you to pass more than one ASCIZ string as a callback tag value. The <code>ASCIZ_STRING_TABLE</code> function generates a value of type <code>asciz_table</code>. The name <code>ASCIZ_TABLE</code> is a synonym for <code>ASCIZ_STRING_TABLE</code>.</p>
<dt><code>WIDE_CHARACTER(</code><code>string_expression</code><code>)</code></p>
<dd>
<dd>Use the <code>WIDE_CHARACTER</code> function to generate a wide character string from null-terminated string in the current locale.</p>
<dt><code>CLASS_REC_NAME(</code><code>string_expression</code><code>)</code></p>
<dd>
<dd>Use the <code>CLASS_REC_NAME</code> function to generate a widget class name. For a widget class defined by the toolkit, the string argument is the name of the class. For a user-defined widget, the string argument is the name of the creation routine for the widget.</p>
<dt><code>INTEGER_TABLE(</code><i>integer_expression</i>[,&#8230;]<code>)</code></p>
<dd>An integer table is an array of integer values separated by commas. This function allows you to pass more than one integer per callback tag value. The <code>INTEGER_TABLE</code> function generates a value of type <code>integer_table</code>.</p>
<dt><code>ARGUMENT(</code><code>string_expression</code>[,&nbsp;<wbr><i>argument_type</i>]<code>)</code></p>
<dd>
<dd>The <code>ARGUMENT</code> function defines the arguments to a user-defined widget. Each of the objects that can be described by UIL permits a set of arguments, listed in Appendix B. For example, <code>XmNheight</code> is an argument to most objects and has an integer data type. To specify height for a user-defined widget, you can use the built-in argument name <code>XmNheight</code>, and specify an integer value when you declare the user-defined widget. You do not use the <code>ARGUMENT</code> function to specify arguments that are built into the UIL compiler.</p>
<dd>The <code>string_expression</code> name is the name the UIL compiler uses for the argument in the UID file. <i>argument_type</i> is the type of value that can be associated with the argument. If you omit the second argument, the default type is <code>ANY</code> and no value type checking occurs. Use one of the following keywords to specify the argument type:</p>
<dl>
<dd>
<dl>
<dt> &bull;</p>
<dd>ANY</p>
<dt> &bull;</p>
<dd>ASCIZ_TABLE</p>
<dt> &bull;</p>
<dd>BOOLEAN</p>
<dt> &bull;</p>
<dd>COLOR</p>
<dt> &bull;</p>
<dd>COMPOUND_STRING</p>
<dt> &bull;</p>
<dd>FLOAT</p>
<dt> &bull;</p>
<dd>FONT</p>
<dt> &bull;</p>
<dd>FONT_TABLE</p>
<dt> &bull;</p>
<dd>FONTSET</p>
<dt> &bull;</p>
<dd>ICON</p>
<dt> &bull;</p>
<dd>INTEGER</p>
<dt> &bull;</p>
<dd>INTEGER_TABLE</p>
<dt> &bull;</p>
<dd>KEYSYM</p>
<dt> &bull;</p>
<dd>PIXMAP</p>
<dt> &bull;</p>
<dd>REASON</p>
<dt> &bull;</p>
<dd>SINGLE_FLOAT</p>
<dt> &bull;</p>
<dd>STRING</p>
<dt> &bull;</p>
<dd>STRING_TABLE</p>
<dt> &bull;</p>
<dd>TRANSLATION_TABLE</p>
<dt> &bull;</p>
<dd>WIDE_CHARACTER</p>
<dt> &bull;</p>
<dd>WIDGET</dl>
</dl>
<dd>You can use the <code>ARGUMENT</code> function to allow the UIL compiler to recognize extensions to the Motif Toolkit. For example, an existing widget may accept a new argument. Using the <code>ARGUMENT</code> function, you can make this new argument available to the UIL compiler before the updated version of the compiler is released.</p>
<dt><code>REASON(</code><code>string_expression</code><code>)</code></p>
<dd>
<dd>The <code>REASON</code> function is useful for defining new reasons for user-defined widgets.</p>
<dd>Each of the objects in the Motif Toolkit defines a set of conditions under which it calls a user-defined function. These conditions are known as callback reasons. The user-defined functions are termed callback procedures. In a UIL module, you use a callbacks list to specify which user-defined functions are to be called for which reasons.</p>
<dd>Appendix B lists the callback reasons supported by the Motif Toolkit objects.</p>
<dd>When you declare a user-defined widget, you can define callback reasons for that widget using the <code>REASON</code> function. The string expression specifies the argument name stored in the UID file for the reason. This reason name is supplied to the widget creation routine at run time.</p>
<dt><code>TRANSLATION_TABLE(</code><code>string_expression</code>[,&#8230;]<code>)</code></p>
<dd>
<dd>Each of the Motif Toolkit widgets has a translation table that maps X events (for example, mouse button 1 being pressed) to a sequence of actions. Through widget arguments, such as the common translations argument, you can specify an alternate set of events or actions for a particular widget. The <code>TRANSLATION_TABLE</code> function creates a translation table that can be used as the value of an argument that is of the data type <code>translation_table</code>.</p>
<dd>You can use one of the following translation table directives with the <code>TRANSLATION_TABLE</code> function: <code>#override</code>, <code>#augment</code>, or <code>#replace</code>. The default is <code>#replace</code>. If you specify one of these directives, it must be the first entry in the translation table.</p>
<dd>The <code>#override</code> directive causes any duplicate translations to be ignored. For example, if a translation for &lt;<code>Btn1Down</code>&gt; is already defined in the current translations for a PushButton, the translation defined by <i>new_translations</i> overrides the current definition. If the <code>#augment</code> directive is specified, the current definition takes precedence. The <code>#replace</code> directive replaces all current translations with those specified in the <code>XmNtranslations</code> resource.</dl>
<h3>Renditions and Render Tables</h3>
<p>In addition to the string direction, each compound string carries a great deal of information about how its text is to be rendered. Each compound string contains a &quot;tag,&quot; identifying the &quot;rendition&quot; to be used to draw that string. The rendition contains such information as the font, the size, the color, whether the text is to be underlined or crossed out, and the position and style of any tab stops. Many renditions are combined into a &quot;render table,&quot; which is specified to any widget with the <code>XmNrenderTable</code> resource, and in the widget&#8217;s <i>controls</i> list. </p>
<p> UIL implements render tables, renditions, tab lists, and tab stops as a special class of objects, in a form similar to the widget class. These objects are not themselves widgets or gadgets, but the format used by UIL to specify widget resources provides a convenient way to specify the qualities and dependencies of these objects. </p>
<p> For example, a render table, included in some widget&#8217;s <i>controls</i> list, must also have a <i>controls</i> list in its specification, containing the names of its member renditions. Each rendition, in its specification, will contain an <i>arguments</i> list specifying such qualities as the font, the color, and whether the text is to be underlined. Any of the renditions may also control a tablist, which will itself control one or more tab stops. </p>
<p> Please refer to the <i>Motif Programmer&#8217;s Guide</i> for a complete description of renditions and render tables, and for an example of how to use them in UIL.</p>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/1-uil/">uil</a></code>(1), <code><a href="/docs/linux/man/3-uil/">Uil</a></code>(3)</p>
