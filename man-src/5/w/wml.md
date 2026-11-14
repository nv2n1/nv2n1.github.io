---
title: "wml(5)"
name: "wml"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wml/"
description: "WML — The widget meta-language file format for creating uil compilers"
---

<p><code>WML</code> &#8212; The widget meta-language file format for creating uil compilers</p>
<h2>Description</h2>
<p>The widget meta-language facility (WML) is used to generate the components of the user interface language (UIL) compiler that can change depending on the widget set. Using WML you can add support in UIL for new widgets to the Motif widget set or for a totally new widget set.</p>
<h3>File</h3>
<p>WML files are ASCII files that you can modify with any standard text editor. They are accessed in the <code>tools/wml</code> directory by WML. By convention WML files have the suffix <code>.wml</code>. The Motif widget set is described in the <code>motif.wml</code> file. This is also the default WML file when using the WML facility. When adding new widgets or changing widget characteristics, you should start with a copy of the <code>motif.wml</code> file. If you are creating a new widget set for use with UIL, you should start from scratch. In either case the <code>motif.wml</code> file is a good example of WML syntax, and you should familiarize yourself with it before writing your own WML file. WML files have a simple syntax, similar in structure to UIL. It is made up of the following elements:</p>
<dl>
<dt> &bull;</p>
<dd>Comments</p>
<dt> &bull;</p>
<dd>Data Type Definitions</p>
<dt> &bull;</p>
<dd>Character Set Definitions</p>
<dt> &bull;</p>
<dd>Enumeration Set Definitions</p>
<dt> &bull;</p>
<dd>Control List Definitions</p>
<dt> &bull;</p>
<dd>Class Definitions</p>
<dt> &bull;</p>
<dd>Child Definitions</p>
<dt> &bull;</p>
<dd>Resource Definitions</dl>
<p> You can use space, tabs, or newlines anywhere in the syntax, as long as you do not split up keywords or strings, except that comments end at a newline. The order of elements is not important to the syntax. This description uses the following additional conventions to describe the syntax of the widget meta-language:</p>
<dl>
<dt>[&nbsp;<wbr>&nbsp;<wbr>]</p>
<dd>Indicates optional elements.</p>
<dt>&#8230;</p>
<dd>Indicates where an element of syntax can be repeated.</p>
<dt>|</p>
<dd>Indicates a choice among multiple items.</dl>
<h3>Comments</h3>
<p>You can include comments in the WML file. Comments have the following syntax: </p>
<pre>[any.element]!any.comment</pre>
<p>Comments begin with an exclamation point and extend to the end of the line. A comment can begin on a line by itself or follow any part of another element. A comment does not change the meaning of any other element. For example: </p>
<pre><tt>!This is a comment
! that spans two lines.
DataType !This is a comment following code.</tt></pre>
<h3>Data Type Definitions</h3>
<p>Data type definitions register all the resource data types used in the file. You must register all the data types used in your WML file. Data type definitions have the following syntax: </p>
<pre>DataType
 any.datatype [{ InternalLiteral = internal.name |
 DocName = &quot;<i>string</i>&quot;; [...]}];
 [...]</pre>
<p>A data type definition begins with the keyword <code>DataType</code>. Following the <code>DataType</code> keyword is a list of data types that can be further modified with</p>
<dl>
<dt><code>InternalLiteral</code></p>
<dd>This forces the value of the internal symbol table literal definition of the data type name. This modifier is only used to get around symbol table definitions hard coded into the UIL compiler. It should rarely be used.</p>
<dt><code>DocName</code></p>
<dd>This gives an arbitrary string for use in the documentation. This string is meant to supply a different name for the data type for use in the documentation, or a single name for the data type if the data type has aliases.</dl>
<p> For example: </p>
<pre><code>DataType OddNumber {DocName=&quot;OddNumber&quot;;};
NewString;</code></pre>
<h3>Character Set Definitions</h3>
<p>Character set definitions register the Motif Toolkit name and other information for the character set names used in UIL. Character set definitions have the following syntax: </p>
<pre>CharacterSet
 any.character.set
 { [ FontListElementTag | XmStringCharsetName ] = &quot;<i>string</i>&quot;;
 [ Alias = &quot;<i>string</i>&quot; ...; |
 Direction = [ LeftToRight | RightToLeft ]; |
 ParseDirection = [ LeftToRight | RightToLeft ]; |
 CharacterSize = [ OneByte | TwoByte ]; ]
 [ ... ] };
 [ ... ]</pre>
<p>A character set definition begins with the keyword <code>CharacterSet</code>. Following the <code>CharacterSet</code> keyword is a list of character sets that can be further modified with</p>
<dl>
<dt><code>FontListElementTag</code>&nbsp;<wbr>|&nbsp;<wbr><code>XmStringCharsetName</code></p>
<dd>Specifies the name of the character set, which will become the character set component of a compound string segment created using this character set. This modifier is required.</p>
<dt><code>Alias</code></p>
<dd>Specifies one or more aliases for the character set name. Each alias can be used within UIL to refer to the same character set.</p>
<dt><code>Direction</code></p>
<dd>Specifies the direction of a compound string segment created using this character set. The default is <code>LeftToRight</code>.</p>
<dt><code>ParseDirection</code></p>
<dd>Specifies the direction in which an input string is parsed when a compound string segment is created using this character set. The default is whatever <code>Direction</code> is specified.</p>
<dt><code>CharacterSize</code></p>
<dd>Specifies the number of bytes in each character of a compound string segment created using this character set. The default is <code>OneByte</code>.</dl>
<p> For example: CharacterSet<br />
iso_latin1<br />
{ XmStringCharsetName = &quot;ISO8859-1&quot;;<br />
    Alias = &quot;ISOLatin1&quot;; };<br />
iso_hebrew_lr<br />
{ XmStringCharsetName = &quot;ISO8859-8&quot;;<br />
    Alias = &quot;iso_latin8_lr&quot;;<br />
    Direction = RightToLeft;<br />
    ParseDirection = LeftToRight; };<br />
ksc_korean<br />
{ XmStringCharsetName = &quot;KSC5601.1987-0&quot;;<br />
    CharacterSize = TwoByte; };</p>
<h3>Enumeration Set Definitions</h3>
<p>Enumeration set definitions register the named constants used in the Motif Toolkit to specify some resource values. Enumeration set definitions have the following syntax: </p>
<pre>EnumerationSet
 resource.name: resource.type
 { enum.value.name; [ ... ] };</pre>
<p>An enumeration set definition begins with the keyword <code>EnumerationSet</code>. For each enumeration set defined, the name and type of the resource are listed. The resource name is the Motif Toolkit resource name, with the beginning <code>XmN</code> removed and with the initial letter capitalized. For example, the name of the Motif Toolkit resource <code>XmNrowColumnType</code> is <code>RowColumnType</code>. The resource type is the data type for the resource; for most resources, this is <i>integer</i>. Following the resource name and type is a list of names of enumeration values that can be used as settings for the resource. These names are the same as those in the Motif Toolkit. For example: </p>
<pre><tt>EnumerationSet
 RowColumnType: integer
 { XmWORK_AREA; XmMENU_BAR; XmMENU_POPUP;
 XmMENU_PULLDOWN; XmMENU_OPTION; };</tt></pre>
<p>Enumeration sets also support Boolean values.</p>
<h3>Control List Definitions</h3>
<p>Control list definitions assign a name to groups of controls. You can use these control lists later in class definitions to simplify the structure of your WML file. Control list definitions have the following syntax: </p>
<pre>ControlList
 any.control.list [{ any.control; [...]}];</pre>
<p>A control list definition starts with the <code>ControlList</code> keyword. Following the <code>ControlList</code> keyword are any number of control list definitions. Control list definitions are made up of a control list name followed by the set of controls it represents. For example: </p>
<pre><tt>ControlList
 Buttons {PushButton;
 RadioButton;
 CascadeButton;
 NewCascadebutton;};</tt></pre>
<p>Each control specified in the control list must be defined as a class in the file.</p>
<h3>Class Definitions</h3>
<p>Class definitions describe a particular widget class including its position in the class hierarchy, toolkit convenience function, resources, and controls. There should be one class definition for each widget or gadget in the widget set you want to support in UIL. Class definitions have the following syntax: Class class.name: MetaClass | Widget | Gadget<br />
[{[<br />
    SuperClass = class.name; |<br />
    ParentClass = parent.class.name; |<br />
    InternalLiteral = internal.name; |<br />
    Alias = alias; |<br />
    ConvenienceFunction = convenience.function; |<br />
    WidgetClass = widget.class; |<br />
    DocName = &quot;string&quot;; |<br />
    DialogClass = True | False; |<br />
    Resources { any.resource.name [{<br />
        Default = new.default.value; |<br />
        Exclude = True |<br />
        False;<br />
        [&#8230;]} ];<br />
    [&#8230;]}; |<br />
Controls { any.control.name; [&#8230;]};<br />
Children { any.child.name; [&#8230;] };<br />
[&#8230;]<br />
]}]; Class definitions start with the <code>Class</code> keyword. For each class defined, the name of the class and whether the class is a metaclass, widget, or gadget is listed. Each class definition can be further modified with the keywords described in the following list.</p>
<dl>
<dt><code>SuperClass</code></p>
<dd>This indicates the name of the parent class. Only the root of the hierarchy does not specify a SuperClass.</p>
<dt><code>ParentClass</code></p>
<dd>This indicates the name of the widget&#8217;s automatically created parent class if one exists. This allows resources for that automatically created class to be used in instances of this class. For example, <code>XmBulletinBoardDialog</code> creates both an <code>XmBulletinBoard</code> and an <code>XmDialogShell</code>. To access the resources of the <code>XmDialogShell</code> parent class it must be specified here.</p>
<dt><code>InternalLiteral</code></p>
<dd>This forces the value of the internal symbol table literal definition of the class name. This modifier is only used to get around symbol table definitions hard coded into the UIL compiler. It should rarely be used.</p>
<dt><code>Alias</code></p>
<dd>This indicates alternate names for the class for use in a UIL specification.</p>
<dt><code>ConvenienceFunction</code></p>
<dd>This indicates the name of the creation convenience function for this class. All widget and gadget classes must have a <code>ConvenienceFunction.</code></p>
<dt><code>WidgetClass</code></p>
<dd>This indicates the associated widget class of gadget type classes. Presently, nothing is done with this value.</p>
<dt><code>DocName</code></p>
<dd>This defines an arbitrary string for use in the documentation. Presently, nothing is done with this value.</p>
<dt><code>DialogClass</code></p>
<dd>This indicates whether the class is a dialog class. Presently, nothing is done with this value.</p>
<dt><code>Resources</code></p>
<dd>This lists the resources of the widget class. This keyword can be further modified with</p>
<dl>
<dd>
<dl>
<dt><code>Default</code></p>
<dd>This specifies a new default value for this resource. Resource default values are usually set in the resource definition. If an inherited resource&#8217;s default value is changed by the class, the new default value should be noted here.</p>
<dt><code>Exclude</code></p>
<dd>This specifies whether an inherited resource should be excluded from the resource list of the class. <code>Exclude</code> is False by default.</dl>
</dl>
<dt><code>Children</code></p>
<dd>This lists the names of the automatically created children of this class, so that those children can be accessed in the UIL file.</p>
<dt><code>Controls</code></p>
<dd>This lists the controls that the widget class allows. The controls can be other classes or a control list from the control list definition.</dl>
<p> The following example uses the examples from the data type definitions and control list definitions above. Class<br />
TopLevelWidget: MetaClass<br />
{<br />
    Resources<br />
    {<br />
        XtbNfirstResource;<br />
        XtbNsecondResource;<br />
    };<br />
};<br />
NewWidget: Widget<br />
{<br />
    SuperClass = TopLevelWidget;<br />
    ConvenienceFunction =<br />
    XtbCreateNewWidget;<br />
    Resources<br />
    {<br />
        XtbNnewResource;<br />
        XtbNfirstResource<br />
        {Default=&quot;XtbNEW_VALUE&quot;;};<br />
        XtbNsecondResource<br />
        {Exclude=True;};<br />
    };<br />
    Controls<br />
    {<br />
        NewWidget;<br />
        Buttons;<br />
    };<br />
};</p>
<h3>Child Definitions</h3>
<p>Child definitions register the classes of automatically created children. Automatically created children are referenced elsewhere in a <code>uil</code> file using the <code>Children</code> keyword within a class definition. Child definitions have the following syntax: <code>Child</code> <code>child.name</code> <code>:</code> <code>class.name</code><code>;</code> [&#8230;] Where <code>child.name</code> is the name of the automatically created child and <code>class.name</code> is the name of the class of that child.</p>
<h3>Resource Definitions</h3>
<p>Resource definitions describe a particular resource including its type, and default value. There should be a resource definition for each new resource referenced in the class definitions. Resource definitions have the following syntax: </p>
<pre>Resource
 resource.name: Argument | Reason | Constraint | SubResource
 [{[
 Type = <i>type</i>;
 [ResourceLiteral = resource.literal; ]
 [InternalLiteral = internal.name; ]
 [Alias = <i>alias</i>; ]
 [Related = <i>related</i>; ]
 [Default = <i>default</i>; ]
 [DocName = doc.name; ]
 [...]}]
 [...]</pre>
<p>Resource definitions start with the <code>Resource</code> keyword. For each resource definition, the name of the resource and whether the resource is an argument, reason, constraint or subresource is listed.</p>
<dl>
<dt><code>Argument</code></p>
<dd>Indicates a standard resource</p>
<dt><code>Reason</code></p>
<dd>Indicates a callback resource</p>
<dt><code>Constraint</code></p>
<dd>Indicates a constraint resource</p>
<dt><code>SubResource</code></p>
<dd>Presently, nothing is done with this value</dl>
<p> The resource definition can be further modified with the following keywords:</p>
<dl>
<dt><code>Type</code></p>
<dd>This indicates the data type of the resource. It must be listed in the data type definition.</p>
<dt><code>ResourceLiteral</code></p>
<dd>This indicates the keyword used in the UIL file to reference the resource. In Motif, the resource name is the same as the <code>ResourceLiteral</code>.</p>
<dt><code>InternalLiteral</code></p>
<dd>This forces the value of the internal symbol table literal definition of the resource name. This modifier is only used to get around symbol table definitions hard coded into the UIL compiler. It should rarely be used.</p>
<dt><code>Alias</code></p>
<dd>This indicates alternate names for the resource for use in a UIL specification.</p>
<dt><code>Related</code></p>
<dd>This is a special purpose field that allows resources that act as a counter for the current resources to be related to the resource. UIL automatically sets the value of this related resource to the number of items in the compiled instance of type <code>resource.name</code>.</p>
<dt><code>Default</code></p>
<dd>This indicates the default value of the resource.</p>
<dt><code>DocName</code></p>
<dd>This defines an arbitrary string for use in the documentation. Presently, nothing is done with this value.</dl>
<p> The following example uses the examples from the data type definitions, control list definitions and class definitions above. </p>
<pre><code>Resource
XtbNfirstResource: Argument
{ Type = OddNumber;
    Default = &quot;XtbOLD_VALUE&quot;;};
XtbNsecondResource: Argument
{ Type = NewString;
    Default = &quot;XtbNEW_STRING&quot;; };
XtbNnewResource: Argument
{ Type = OddNumber;
    Default = &quot;XtbODD_NUMBER&quot;; };

</code></pre>
