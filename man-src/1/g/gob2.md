---
title: "gob2(1)"
name: "gob2"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gob2/"
description: "GOB2 – The GObject Builder"
---

<h2>NAME</h2>
<p> GOB2 &#8211; The GObject Builder</p>
<h2>SYNOPSIS</h2>
<p> <code>gob2</code> [ option ] &#8230; file </p>
<h2>DESCRIPTION</h2>
<p> GObject Builder is a simple preprocessor for easily creating GObject objects. It does not parse any C code and ignores any C errors. It is in spirit similar to things like lex or yacc. In some ways it also resembles java. But it is really just a simple preprocessor for creating GObjects for use in C or C++ and it is not a programming language. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-? -h &#8211;help</code></p>
<dd> Display a simple help screen.</p>
<dt><code>&#8211;version</code></p>
<dd> Display version information</p>
<dt><code>-w &#8211;exit-on-warn</code></p>
<dd> Exit with an error code even when you encounter a warning.</p>
<dt><code>&#8211;no-exit-on-warn</code></p>
<dd> Exit with an error only on errors, not on warnings, this is the default.</p>
<dt><code>&#8211;for-cpp</code></p>
<dd> Generate C++ code.</p>
<dt><code>&#8211;no-extern-c</code></p>
<dd> Never add the extern &quot;C&quot; to the header.</p>
<dt><code>&#8211;no-gnu</code></p>
<dd> Never generate any code with GNU C extensions. However all the GNU C extensions are always wrapped in #ifdef __GNUC__, so code using them compiles correctly even on non-GNU compilers. This option is for purists only. (using GNU extensions some warnings are eliminated, some ugly hacks and there is better argument type safety, so it&#8217;s good to use them)</p>
<dt><code>&#8211;no-touch</code></p>
<dd> Don&#8217;t touch output files unless they really changed (implies &#8211;no-touch-headers). Be careful with automake, see section PREVENTING SPURIOUS BUILDS.</p>
<dt><code>&#8211;no-touch-headers</code></p>
<dd> Don&#8217;t touch the generated header file unless it really changed, this avoids spurious rebuilds, but can confuse some make systems (automake in particular), so it is not enabled by default. Private header is still touched even if unchanged however.</p>
<dt><code>&#8211;always-private-header</code></p>
<dd> Always create a <code>&lt;basename&gt;-private.h</code> file, even if it would be empty.</p>
<dt><code>&#8211;ondemand-private-header</code></p>
<dd> Create the private header only if it would have something in it, that is, if there are some private data members or protected methods. This is the default.</p>
<dt><code>&#8211;no-private-header</code></p>
<dd> Never create a private header file. If we use any private data members, define the private data structure at the point in the .c source where the class definition begins.</p>
<dt><code>&#8211;m4</code></p>
<dd> Preprocess source with m4. Following args will be passed to m4.</p>
<dt><code>&#8211;m4-dir</code></p>
<dd> Print directory that will be searched for m4 files.</p>
<dt><code>-n &#8211;no-write</code></p>
<dd> Do not write any output files, just check syntax of the input file.</p>
<dt><code>&#8211;no-lines</code></p>
<dd> Do not print out the &#8216;#line&#8217; statements into the output. Useful for debugging the auto-generated generated code.</p>
<dt><code>&#8211;no-self-alias</code></p>
<dd> Do not create the Self and SelfClass type aliases and the SELF, IS_SELF and SELF_CLASS macros.</p>
<dt><code>&#8211;no-kill-underscores</code></p>
<dd> Do not remove the initial underscore from method names.</p>
<dt><code>&#8211;always-private-struct</code></p>
<dd> Always include the private pointer in the public header file. This is useful for files which are part of a library and you want to reserve the right to add some private data members without breaking binary compatibility.</p>
<dt><code>-o &#8211;output-dir</code></p>
<dd> The directory into which output should be placed.</p>
<dt><code>&#8211;file-sep[=c]</code></p>
<dd> Replace default &#8216;-&#8216; file name separator. If no separator character is given then none is used. Only one character can be used. </p>
</dl>
<h2>TYPENAMES</h2>
<p> Because we need to parse out different parts of the typename, sometimes you need to specify the typename with some special syntax. Types are specified in capitalized form and words are separated by &#8216;:&#8217;. The first word of the type (which can be empty) is the &quot;namespace&quot;. This fact is for example used for the type checking macro and the type macro. For &quot;Gtk:New:Button&quot;, the macros will be GTK_IS_NEW_BUTTON and GTK_TYPE_NEW_BUTTON. This colon separated format of typenames is used in the class declaration header and for method argument types. </p>
<h2>OUTPUT FILES</h2>
<p> The filenames are created from the typename. The words are separated by &#8216;-&#8216; (this can be changed with <code>&#8211;file-sep</code> option) and all in lower case. For example for an object named &quot;Gtk:New:Button&quot;, the files are <code>gtk-new-button.c</code> and <code>gtk-new-button.h</code>. If you are using C++ mode, the output .c file will in fact be a .cc file. If you have any private data members, a private header file will also be created, called <code>&lt;basename&gt;-private.h</code> (for the example above it would be gtk-new-button-private.h). The public header file is created to be human readable and to be used as a reference to the object. The .c source file is not created as a human readable source and is littered with #line statements, which make the compiler attempt to point you to the right line in your .gob file in case of parsing errors. The output should not be edited by hand, and you should only edit the .gob file. </p>
<h2>INCLUDING NORMAL C CODE IN THE OUTPUT FILES</h2>
<p> To include some code directly in the output C file begin with &#8216;%{&#8216; on an empty line and end the code with a &#8216;%}&#8217; on an empty line. These sections will appear in the output files in the order they are given. There are several other <i>sections</i> to which you can put code. You can put it in the &#8216;header&#8217; section (which can be abbreviated &#8216;h&#8217;) and it will go into the public header file. You can also put it in the &#8216;privateheader&#8217; section (abbreviated &#8216;ph&#8217;) which will make the code go into the private header file. Sometimes you want some code (other includes) to appear before the extern &quot;C&quot; and the protecting define. To do this you can put them into the &#8216;headertop&#8217; (or &#8216;ht&#8217;) section. You may wish to include code or comments in all the files, which you can do by putting them into the &#8216;all&#8217; (or &#8216;a&#8217;) section. Similarly, code you wish to appear at the top of all files go in the &#8216;alltop&#8217; (or &#8216;at&#8217;) section. When you want code to appear as in alltop but only in the cfile you use the &#8216;ctop&#8217; (or &#8216;ct&#8217;) section. Note that ctop requires 2.0.18. Finally, &#8216;afterdecls&#8217; includes code between the declarations and the method implementations, but note that &#8216;afterdecls&#8217; requires version 2.0.16. For example: </p>
<pre><code>
% alltop{/* this will be at the very top of all output files */
         % } %
    ctop{/* this will be at the very top of the C file */
         /* Requires 2.0.18 */
         % } %
    headertop{/* this will be on top of the public header */
              % } %
    privateheader{/* this will go into the private header file */
                  % } %
    h
{
    /* will be included in the header */
    void somefunc(int i);
    %
}
% a{/* will be included in all files */
    % } %
    afterdecls{/* between the declarations and the method implementations */
               /* Requires gob version 2.0.16 */
               % } %
{
    /* will be included in the C file */
    void somefunc(int i){
        /* some code */
    } %
}
</code></pre>
<h2>INCLUDE FILES</h2>
<p> Gob will automatically include the class header file at the top of the .c source file. If you wish to include it somewhere else, put the include into some %{ %} section above the class definition, and gob will not include it automatically. This way you can avoid circular includes and control where in the file do you want to include the header. </p>
<p> If you made any data members private, gob will also create a source file that will be called <code>&lt;basename&gt;-private.h</code>. Same rule as above applies for this just as it does for the regular header file. If you do explicitly include the regular header file, you should always include this private header file below it. That is, if you use any private data members. If you don&#8217;t, the private header file automatically includes the public header file, and thus the public header file will be indirectly included at the very top of the file. </p>
<h2>THE CLASS HEADER</h2>
<p> There can be only one class per input file. Defining a class is sort of like in Java, you define the class and write inline code directly into the class definition. To define a class you need to specify the new object name and the name of the object from which it is derived from, such as this &quot;class &lt;new type&gt; from &lt;parent type&gt; { &lt;class code&gt; }&quot;. For example: </p>
<pre>
  class Gtk:New:Button from Gtk:Button {
          &lt;class code&gt;
  }
</pre>
<p> To make an abstract class (to pass G_TYPE_FLAG_ABSTRACT) add &#8216;(abstract)&#8217; before the curly braces above. This works since version 2.0.13. </p>
<h2>DATA MEMBERS</h2>
<p> There are five types of data members. Three of them are normal data members, one is class wide (global) in scope and one is a virtual one, usually linked to a normal data member or a class wide data member. The three normal data members are public, protected and private. Public and protected are basically just entries in the object structure, while private has it&#8217;s own dynamically allocated private structure. Protected members are always put after the public one in the structure and are marked protected in the header file. There is only one identifier allowed per typename unlike in normal C. Example:<br />
public<br />
int i;<br />
private<br />
GtkWidget *h;<br />
protected<br />
long k;</p>
<p> Public and protected data members are accessed normally as members of the object struct. Example where &#8216;i&#8217; is as above a public data member: </p>
<pre>
  object-&gt;i = 1;
</pre>
<p> The private data members are defined in a structure which is only available inside the .c file, or by including a private header file. You must access them using the structure _priv. Example where &#8216;h&#8217; is the private data member (as in the above example):<br />
object-&gt;_priv-&gt;h = NULL;<br />
 The _priv structure is defined in the <code>&lt;basename&gt;-private.h</code>. This file is automatically included if you don&#8217;t include it yourself. You should always explicitly include it in your .gob file if you explicitly also include the main header file. The reason it is a separate header file is that you can also include it in other places that need to access this objects private data, such as if you have the majority of functionality of an object in a separate .c file. Or if a derived object needs to access the protected methods. </p>
<p> In case you use the <code>&#8211;no-private-header</code> option, no private header file is created and you can only access the _priv pointer below the class definition in the .gob file. </p>
<p> Also note that this structure is dynamically allocated, and is freed in the finalize handler. If you override the finalized handler, your code will be run first and only then will the _priv structure be freed. </p>
<p> <code>Classwide data members:</code> </p>
<p> Sometimes you want a datamember to be shared by all objects. You then need the &quot;classwide&quot; scope keyword. So for example the following adds a global member foo: </p>
<pre>
  classwide int foo;
</pre>
<p> To access the member you can use the SELF_GET_CLASS macro (or YOUR_OBJECT_NAME_GET_CLASS) to get at the class. Thus the following would work: </p>
<pre>
  SELF_GET_CLASS(object)-&gt;foo = 20;
</pre>
<p> <code>Automatic Initialization:</code> </p>
<p> You can automatically initialize the public private and protected data members without having to add an init method. The advantage here is that initialization is kept close to the definition of the data member and thus it&#8217;s easier to check. To do this, just add a &#8216;=&#8217; followed by a number or a token. It is also possible to include arbitrary C code for more elaborate initializations by putting it all in curly braces. Note that the curly braces will not be printed into the output, but since gob does not C parsing it needs them to figure out where the C code ends. The code will be inserted into the init method, above the user defined body. So for example the following will initialize an integer to -1 and a string with a newly allocated string of &quot;hello&quot;.<br />
public<br />
int foo = -1;<br />
private<br />
char *bar = {g_strdup(&#8220;hello&#8221;)};</p>
<p> <code>Automatic Destruction:</code> </p>
<p> Most data stored as pointers needs to have a function called when the object is finalized to either free the data. Gob will let you define a function to be called on the data the object is finalized. This is achieved by putting &#8216;destroywith&#8217; followed by a function name after the variable definition. It is only called if the data you defined this on is not NULL, so you cans specify functions which do not handle NULL. It is very much like the GDestroyNotify function used in GTK+ and glib in many places. Unlike many other places, gob will not enforce any kind of type safety here so be a little bit more careful. Any function you give it will be called as a &quot;void function(void *)&quot;. It will in fact be cast into such a form before called. This is to avoid spurious warnings for gtk calls to subclass methods. The function needs not be of that form exactly, it just has to take one argument which is the pointer to the data. You should also not define this on any non-pointer data as the results may be undefined. Example:<br />
public<br />
char *foo = {g_strdup(&#8220;bar&#8221;)} destroywith g_free;<br />
 Note that the function name you give must be a real function and not macro. Also note that this is always called in the &quot;finalize&quot; method of GObject. It is always called after any user defined body of the finalize handler. </p>
<p> Sometimes you may want to run arbitrary code on destruction. While this can be perfectly well done in the finalize handler. Depending on the style you may want to include all destruction/initialization code together with the definition of the data member. Thus you may want to put arbitrary code which will then be inserted into the &quot;finalize&quot; method of GObject. This can be done with the &quot;destroy&quot; keyword followed by arbitrary code in curly braces. Inside this code a macro called VAR will be define which refers to your variable. So for example destroying a GString can be either done with a helper routine or the following code:<br />
public<br />
GString *string = {g_string_new(NULL)} destroy<br />
{<br />
    if (VAR)<br />
        g_string_free(VAR, TRUE);<br />
};<br />
 The thing to remember with these is that there are many ways to do this and you&#8217;d better be consistent in your code in how you use the above things. Also defining a helper routine that will do the destruction will be a nicer thing to do if that&#8217;s a possibility. The &quot;destroy&quot; keyword with code does take up more space in the file and it may become more cluttered. </p>
<p> The data is zeroed out after being destroyed. This is to make debugging easier in case your code might try to access an already finalized object. In case you have overridden the finalize method, your code will be run first and only then will the destructors be called. You should not however make any assumptions about the order at which the destructors are called. If you have interdependencies between destructors for different data members, you will have to do this in your own finalize override function. </p>
<p> <code>Automatic Unreffing:</code> </p>
<p> This is very much like the automatic destruction, but is instead run in the dispose method (it is among other places called from the &quot;destroy&quot; method of GtkObject). All data and other objects that you need to unref should be done here, and not at finalize time. The semantics are otherwise the same as for the &quot;destroywith&quot; and &quot;destroy&quot; keywords, except that you use &quot;unrefwith&quot; and &quot;unref&quot;.<br />
public<br />
G : Object *foo = NULL<br />
        unrefwith g_object_unref;<br />
public<br />
G : Object *bar = NULL<br />
        unref<br />
{<br />
    g_object_unref(VAR);<br />
};</p>
<h2>GOBJECT PROPERTIES</h2>
<p> The fourth type of a data member a property type. It is a named data member which is one of the features of the GObject system. It just defines a way to get and set some data, but you have to take care of storing that data somewhere. So it is normal to also have a normal private (or public) data member where you store the real data. You normally need to define a get and a set handler. They are fragments of C code that will be used to get the value or set the value of the argument. Inside them you can use the define VAL to which you assign the data or get the data. You should treat this VAL as a GValue which stores the data of the correct type. You can also use the identifier &quot;self&quot; as pointer to the object instance. The type is defined as one of the GObject type enums, but without the G_TYPE_ prefix. There are also some attributes of a property which you can set. For example the following is a definition of an integer property &#8216;height&#8217; which will be synchronized with a private integer data member also of the name &#8216;height&#8217;.<br />
private<br />
int height;<br />
property INT height(nick = _(&#8220;Short nickname&#8221;),<br />
                    blurb = _(&#8220;Long description&#8221;),<br />
                    minimum = 10,<br />
                    maximum = 200,<br />
                    default_value = 100)<br />
    set<br />
{<br />
    self-&gt;_priv-&gt;height = g_value_get_int(VAL);<br />
}<br />
get<br />
{<br />
    g_value_set_int(VAL, self-&gt;_priv-&gt;height);<br />
};</p>
<p> The attributes are really optional though you should at least set some of them. All property types have a &#8216;nick&#8217; and a &#8216;blurb&#8217; attribute and you should set those accordingly. This will make runtime querying the object nicer as things such as gui editors and class browsers can be more verbose about the class itself. You can use the &#8216;_(&quot;string&quot;)&#8217; notation instead of just &quot;string&quot;, and that will mark the string for translation. </p>
<p> Almost all types also have a &#8216;default_value&#8217; attribute which sets the initial value of this property (on object initialization, the set handler will be run automatically with this value). This value will be overridden if the user sets a value of this property on the call to g_object_new. </p>
<p> All the numeric types (including CHAR) have &#8216;minimum&#8217; and &#8216;maximum&#8217; attributes which can restrict the range. If you do not specify these the range will be the full range that the data type can handle. </p>
<p> Types such as UNICHAR and BOOLEAN only have the &#8216;nick&#8217;, &#8216;blurb&#8217; and &#8216;default_value&#8217; attributes. </p>
<p> The ENUM type has an &#8216;enum_type&#8217; attribute which is the exact type of the enum. This is so that the property knows which exact type you can set, rather then just knowing it is an enum. You should always create an enum type specific for the enum itself (see section on the enum types) </p>
<p> Similarly FLAGS type has a &#8216;flags_type&#8217; which again you should set to the specific type of this flags data member. </p>
<p> There is a STRING type which has only the extra &#8216;default_value&#8217; attribute. </p>
<p> The OBJECT type is one of the types that doesn&#8217;t have a &#8216;default_value&#8217; and it only has an &#8216;object_type&#8217; attribute (in addition to nick and blurb of course) that is the exact object type that this property accepts. The object_type should be as a type, that is for example &#8216;Gtk:Button&#8217;. </p>
<p> There is a BOXED type which is a pointer which has a boxed type defined (such that GObject knows how to copy and destroy this pointer). Here you will need to specify the &#8216;boxed_type&#8217; attribute with the specific type of the boxed pointer. </p>
<p> There is also a POINTER type, which has only the &#8216;nick&#8217; and &#8216;blurb&#8217; attributes. This is for storing arbitrary pointers. You should be careful with this one, as GObject knows nothing about the data stored at this pointer. It is somewhat like a &#8216;void *&#8217; type. </p>
<p> There is also the PARAM type for storing parameters with a &#8216;param_type&#8217; attribute. </p>
<p> You should notice that this list is pretty much like the list of g_param_spec_* functions from gobject/gparamspecs.h, and the attributes are like the arguments of those functions. Note however that value array is NOT supported yet. </p>
<p> You can also specify extra flags, such as CONSTRUCT or CONSTRUCT_ONLY using the &#8216;flags&#8217; attribute. You can specify multiple flags by oring them together with &#8216;|&#8217;. These flags correspond to the GParamFlags enumeration except do not include the G_PARAM_ prefix. So for example to define an enumeration property, which is a CONSTRUCT_ONLY property, we could do the following: </p>
<pre>
  private SomeEnumerationType foo;
  property ENUM foo
         (nick = _(&quot;Short nickname&quot;),
          blurb = _(&quot;Long description&quot;),
          enum_type = Some:Enumeration:Type
          default_value = SOME_ENUMERATION_VALUE,
          flags = CONSTRUCT_ONLY,
          link);
</pre>
<p> The above example also gives an example of automatic linking to a standard data memember. By including the attribute &#8216;link&#8217; a get and set handlers will be automatically added without having to type them by hand. This is useful for a vast majority data types that are just linked to some standard data member and do not need to do anything extra on get or set. </p>
<p> Another extra feature of properties is the possibility of automatically exporing methods to get and set the property. That is without having to use g_object_set and g_object_get. This is achieved by adding an &#8216;export&#8217; attribute to the list of property attributes. </p>
<p> If you do not define a set or get handler, the property will automatically be only readable or writable as appropriate. </p>
<p> Gob2 also creates macros which can be used for type safe access to properties through g_object_set and g_object_get. The macros are called &lt;type&gt;_PROP_&lt;argument name&gt;(x) and &lt;type&gt;_GET_PROP_&lt;argument name&gt;(x). They define both the string and the value part of the argument. So for setting an argument of height, one would use (for object type My:Object): </p>
<pre>
  g_object_set (G_OBJECT (object),
                MY_OBJECT_PROP_HEIGHT (7),
                NULL);
</pre>
<p> And for getting, you would use:<br />
int height;<br />
g_object_get(G_OBJECT(object),<br />
             MY_OBJECT_GET_PROP_HEIGHT(&amp;height),<br />
             NULL);<br />
 Note however that the type safety only works completely on GNU C compilers. The code will compile on other compilers but with minimal type safety. For complete type safety it is useful to use the get/set methods that are defined by using the &#8216;export&#8217; attribute. </p>
<p> To get bettery type safety on some of the property types, you can specify the &#8216;type&#8217; attribute which will add casts where appropriate in code dealing with this property. This is especially useful for POINTER and OBJECT types. But even for others. </p>
<p> You can also override properties from parent objects (that is override their implementation, not their attributes). Do this by adding the special &#8216;override&#8217; attribute. For example if the parent object had a &#8216;height&#8217; property then you could override it by<br />
private<br />
int height;<br />
property INT height(override)<br />
    set<br />
{<br />
    self-&gt;_priv-&gt;height = g_value_get_int(VAL);<br />
}<br />
get<br />
{<br />
    g_value_set_int(VAL, self-&gt;_priv-&gt;height);<br />
};<br />
 Overriding is supported since gob 2.0.10. </p>
<h2>METHODS</h2>
<p> There is a whole array of possible methods. The three normal, &quot;familiar&quot; method types are private, protected and public. Public are defined as normal functions with a prototype in the header file. Protected methods are defined as normal methods (which you can call from other files), but their prototype is placed in the private header file. Private methods are defined as static functions with prototypes at the top of the .c file. Then there are signal, virtual and override methods. More on those later. You can also define init and class_init methods with a special definition if you want to add code to the constructors or you can just leave them out. You can also not define a body for a method, by just using &#8216;;&#8217; instead of a body. This will define an empty function. You can&#8217;t do this for non-void regular public, private or protected methods, however it is acceptable for non-void virtual, signal and override methods. </p>
<p> <code>Function argument lists:</code> </p>
<p> For all but the init and class_init methods, you use the following syntax for arguments. The first argument can be just &quot;self&quot;, which gob will translate into a pointer to the object instance. The rest of the arguments are very similar to normal C arguments. If the typename is an object pointer you should use the syntax defined above with the words separated by &#8216;:&#8217; </p>
<pre>
&lt;type&gt; &lt;argument id&gt;
or
&lt;type&gt; &lt;argument id&gt; (check &lt;list of checks&gt;)
</pre>
<p> The checks are glib type preconditions, and can be the following: &quot;null&quot;, which tests pointers for being NULL, &quot;type&quot; which checks GTK+ object pointers for being the right type, &quot;&lt;test&gt; &lt;number&gt;&quot; which tests numeric arguments for being a certain value. The test can be a &lt;,&gt;,&lt;=,&gt;= != or ==. Example: </p>
<pre>
  
  public int
  foo (self,
       int h (check &gt; 0 &lt; 11),
       Gtk:Widget *w (check null type))
</pre>
<p> This will be the prototype of a function which has a self pointer as the first argument, an integer argument which will be checked and has to be more then 0 and less then 11, and a pointer to a GtkWidget object instance and it is checked for being null and the type will also be checked. </p>
<p> <code>Function attributes:</code> </p>
<p> For method that aren&#8217;t virtual, signal or override methods, and aren&#8217;t init or class_init, GLib function attribute macros G_GNUC_PRINTF, G_GNUC_SCANF, and G_GNUC_FORMAT can optionally be included after the argument list. Simply include an &#8216;attr&#8217; keyword and the C code to include in the file. You have to include braces and anything inside the braces will be printed into the header file after the function declaration and before the trailing semicolon. The braces themselves are not printed. For example:<br />
public<br />
void print(self, const char *format(check null), &#8230;)<br />
    attr<br />
{<br />
    G_GNUC_PRINTF(2, 3)<br />
}</p>
<p> This will produce a prototype which will generate a warning at compile time if the contents of the format argument (argument number 2) aren&#8217;t consistent with the types and number of the subsequent variadic arguments (the first of which is argument number 3). Only one &#8216;attr&#8217; keyword per method is allowed. If you have more than one attribute to include, you should put them all within the braces. Note that function attributes were aded in version 2.0.16. </p>
<p> <code>Error return:</code> </p>
<p> Methods which have a return value, there also has to be something returned if there is an error, such as if a precondition is not met. The default is 0, casted to the type of the method. If you need to return something else then you can specify an &#8216;onerror&#8217; keyword after the prototype and any optional function attribute macros, and after that a number, a token (an identifier) or a bit of C code enclosed in braces {}. The braces will not be printed into the output, they just delimit the string. For example:<br />
public<br />
void *get_something(self, int i(check &gt;= 0)) onerror NULL<br />
{<br />
    &#8230;<br />
}<br />
 The onerror value is also used in overrides that have a return value, in case there isn&#8217;t a parent method, PARENT_HANDLER will return it. More about this later. </p>
<p> <code>Default return:</code> </p>
<p> Some signal and virtual methods have a return type. But what happens if there is no default handler and no one connects to a signal. GOB2 will normally have the wrappers return whatever you specify with onerror or &#8216;0&#8217; if you haven&#8217;t specified anything. You can also specify a default return value with the keyword &#8216;defreturn&#8217;. It&#8217;s use is identical to the use of onerror, and you can in fact use both at the same time. Example </p>
<pre>
  virtual int get_some_int (self) onerror -1 defreturn 10 ;
</pre>
<p> That is an empty virtual method (in C++ terms a pure virtual). If you never specify any handler for it in the derived children it will just return 10. </p>
<p> <code>Constructor methods:</code> </p>
<p> There are two methods that handle the construction of an object, init and class_init. You define them by just using the init or class_init keyword with an untyped argument in the argument list. The argument will be usable in your function as a pointer to your object or class depending if it&#8217;s init or class_init. For example:<br />
init(self)<br />
{<br />
    /* initialize the object here */<br />
    self-&gt;a = 9;<br />
    self-&gt;b = 9;<br />
}<br />
class_init(class)<br />
{<br />
    /* initialize the class, this is rarely needed */<br />
    class-&gt;blah = NULL;<br />
}<br />
 The class_init function is very rarely needed as all standard class initialization is taken care of for you by gob itself. The init function should on the other hand be used whenever you need to construct or initialize anything in the object to put it into a sane state. </p>
<p> <code>Constructor, dispose, finalize methods:</code> </p>
<p> Since 2.0.16, you can also easily add code to the object&#8217;s constructor, dispose, and finalize methods. See GObject documentation on how these are run. The code you add will be run before calling the parents function for dispose and finalize, and after the parent function for constructor. The syntax is just like init and class_init. For example:<br />
constructor(self)<br />
{<br />
    /* constructor method */<br />
}<br />
dispose(self)<br />
{<br />
    /* dispose method */<br />
}<br />
finalize(self)<br />
{<br />
    /* finalize method */<br />
}<br />
 You can also just override those methods as usual, but the above is much easier and nearly as flexible. </p>
<p> <code>Virtual methods:</code> </p>
<p> Virtual methods are basically pointers in the class structure, so that one can override the method in derived methods. That is to implement the method in a derived class, you must then use an override method (more on those later). They can be empty (if you put &#8216;;&#8217; instead of the C code). A wrapper will also be defined which makes calling the methods he same as public methods. This type of method is just a little bit &quot;slower&quot; then normal functions, but not as slow as signals. You define them by using &quot;virtual&quot; keyword before the prototype. If you put the keyword &quot;private&quot; right after the &quot;virtual&quot; keyword, the wrapper will not be a public method, but a private one. You can do the same with &quot;protected&quot; to make a protected wrapper. </p>
<p> <code>Signals:</code> </p>
<p> Signals are methods to which the user can bind other handlers and override the default handler. The default handler is basically the method body. This is the most versatile and flexible type of a method and also the slowest. You need to specify a whole bunch of things when you define a signal. One thing is when the default handler will be run, first or last. You specify that by &quot;first&quot; or &quot;last&quot; right after the &quot;signal&quot; keyword. Then you need to define the GObject enum types (again without the G_TYPE_ prefix). For that you define the return types and the types of arguments after the &quot;self&quot; pointer (not including the &quot;self&quot; pointer). You put it in the following syntax &quot;&lt;return type&gt; (&lt;list of arguments&gt;)&quot;. If the return type is void, the type should be &quot;NONE&quot;, the same should be for the argument list. The rest of the prototype is the same as for other method types. The body can also be empty, and also there is a public method wrapper which you can use for calling the signal just like a public method. Example:<br />
signal first INT(POINTER, INT)<br />
int do_something(self, Gtk<br />
                 : Widget *w(check null type), int length)<br />
{<br />
    &#8230;<br />
}<br />
 or<br />
signal last NONE(NONE) void foo(self);</p>
<p> If you don&#8217;t want the wrapper that emits the signal to be public, you can include the keyword &quot;private&quot; after the &quot;signal&quot; keyword. This will make the wrapper a normal private method. You can also make a protected wrapper by using &quot;protected&quot; instead of &quot;private&quot;. </p>
<p> If you don&#8217;t define a &quot;first&quot; or a &quot;last&quot;, the default will be taken as &quot;last&quot;. </p>
<p> You can also add additional flags. You do this just like with the argument flags, although this is probably very rare. These are the G_SIGNAL_* flags, and you can add them without the G_SIGNAL_ prefix into a parenthesis, just after the &quot;signal&quot; keyword. By default all public signals are G_SIGNAL_ACTION. </p>
<p> Also gob2 creates a wrapper macros for typesafe signal connection. That is you will be warned by the compiler if you pass a callback that is not the correct prototype. This will again only warn you on gcc, but it will compile without warning on another compiler. So as with all the typesafety hacks in gob, it is better to test your objects under gcc to get any warnings even if you are using a different compiler in the end. </p>
<p> The methods that are created for you are: </p>
<pre>
  &lt;class_name&gt;_connect__&lt;signal_name&gt; (&lt;object&gt;, &lt;callback&gt;, &lt;data&gt;)
  &lt;class_name&gt;_connect_after__&lt;signal_name&gt; (&lt;object&gt;, &lt;callback&gt;, &lt;data&gt;)
  &lt;class_name&gt;_connect_data__&lt;signal_name&gt; (&lt;object&gt;, &lt;callback&gt;, &lt;data&gt;,
                                            &lt;destroy_notify&gt;, &lt;flags&gt;)
</pre>
<p> These three functions correspond to the g_signal_connect, g_signal_connect_after and g_signal_connect_data functions that you would normally use, except they are for a specific signal. Also do note the two underscores between the method name and the signal name. For example to connect the signal &quot;foo&quot; on the object &quot;Test:Object&quot; you would do: </p>
<pre>
  test_object_connect__foo (object, callback, data);
</pre>
<p> To use BOXED in the signal arguments you need to tell gob which type of boxed argument you want to use. For this you can just add BOXED_GTK_TYPE_STRING instead of BOXED. For example BOXED_GTK_TYPE_TREE_ITER for GtkTreeIter. This works since version 2.0.13. </p>
<p> <code>Override methods:</code> </p>
<p> If you need to override some method (a signal or a virtual method of some class in the parent tree of the new object), you can define and override method. After the &quot;override&quot; keyword, you should put the typename of the class you are overriding a method from. Other then that it is the same as for other methods. The &quot;self&quot; pointer in this case should be the type of the method you are overriding so that you don&#8217;t get warnings during compilation. Also to call the method of the parent class, you can use the PARENT_HANDLER macro with your arguments. Example:<br />
override(Gtk<br />
         : Container) void add(Gtk<br />
                               : Container *self(check null type), Gtk<br />
                               : Widget *wid(check null type))<br />
{<br />
    /* some code here */<br />
    PARENT_HANDLER(self, wid);<br />
}<br />
 If the function has a return value, then PARENT_HANDLER is an expression that you can use. It will return whatever the parent handler returned, or the &quot;onerror&quot; expression if there was no parent handler. </p>
<p> <code>Method names:</code> </p>
<p> Inside the code, aliases are set for the methods, so that you don&#8217;t have to type the class name before each call, just type <code>self_</code> instead of the name of the class. So to call a method called <code>blah</code>, you would use the name <code>self_blah</code>. Example:<br />
private<br />
int foo(self)<br />
{<br />
    return self-&gt;len;<br />
}</p>
<p>private<br />
int bar(self, int i)<br />
{<br />
    return self_foo(self) + i;<br />
}</p>
<h2>MAKING NEW OBJECTS</h2>
<p> You should define a new method which should be a normal public method. Inside this method, you can use the GET_NEW macro that is defined for you and that will fetch a new object, so a fairly standard new method would look like:<br />
public<br />
GObject *new (void)<br />
{<br />
    GObject *ret = GET_NEW;<br />
    return G_OBJECT(ret);<br />
}</p>
<p> You should not a subtle peculiarity of the GObject system here. If there is any code inside the G_OBJECT macro argument, it will get executed multiple times. This means that things such as G_OBJECT(GET_NEW) would actually create 4 objects, leaking 3 of them. A good rule (as with anywhere in C) is to be careful with all macros. </p>
<h2>SELF REFERENCES</h2>
<p> <code>Self alias casts:</code> </p>
<p> There are some standard casts defined for you. Instead of using the full macros inside the .c file, you can use SELF, IS_SELF and SELF_CLASS. Using these makes it easier to for example change class names around. </p>
<p> <code>Self alias types:</code> </p>
<p> There are also the Self and SelfClass types inside your .c file. These serve the same function as the above, they make it easier to type and easier to change typenames around which can help a lot during prototyping stage. However you should note that the Self type should not be used in function prototypes as one of the arguments or as a return value type. This is because this is a simple C typedef which is only available inside your .c file and not in the header files. You can disable both the self casting macros and the self type aliases by passing &#8211;no-self-alias to gob. </p>
<h2>DEALING WITH DIFFERENT GOB VERSIONS</h2>
<p> <code>Defines:</code> </p>
<p> In your generated C file, you can use the defines GOB_VERSION_MAJOR GOB_VERSION_MINOR and GOB_VERSION_PATCHLEVEL if you wish to for example use a feature that is only available in some newer gob version. Note however that you can only use these defines in the C code portions of your .gob file, and #ifdef&#8217;s cannot span multiple functions. Check the BUGS section for more on using the C preprocessor and gob. </p>
<p> <code>Minimum version requires:</code> </p>
<p> You can also make your .gob file require at least certain version of gob. You do this by putting &#8216;requires x.y.z&#8217; (where x.y.z is the version number) outside of any C block, comment or class, usually you should make this the first line in the file or close to the top. If gob finds this and the version of gob used to compile the code is lower then that listed in the require, gob will generate an error and exit. For example to require that gob2 version 2.0.0 or higher be used to compile a file, put this at the top of that file: </p>
<pre>
  requires 2.0.0
</pre>
<h2>CREATING NEW ENUM, FLAGS and ERROR TYPES</h2>
<p> You can create new GObject ENUM, FLAGS and GError types for use in your classes easily. Glib includes some utilities for handling these, however it may be cleaner to use the below specified way in your classes. It also then doesn&#8217;t require any Makefile setup. Make sure this is defined in the same section as the class, that is not in any of the &#8216;%?{&#8216; &#8216;%}&#8217; sections. </p>
<p> You use the keywords &#8216;enum&#8217; &#8216;flags&#8217; and &#8216;error&#8217; as you would use the &#8216;class&#8217; keyword. Then you give a prefix for the values in the enumeration. Then you define a list of values just like in C. For &#8216;enum&#8217; types you can also specify the values assigned to each string. Then you specify the type in the standard gob style of specifying types. Here are a few examples of all of these:<br />
enum LAME_CLIENT {<br />
    IS_CONNECTED,<br />
    NONE = 9,<br />
    LAST<br />
} Test : Enum;<br />
flags BUGA_BUGA{<br />
    ONE,<br />
    TWO,<br />
    MANY,<br />
} Some : Flags;<br />
error TEST_OBJECT_ERROR{<br />
    BAD_THIS,<br />
    BAD_THAT} Test : Object : Error;</p>
<p> This will for example define an enum that is equivalent to the following C code:<br />
typedef enum {<br />
    LAME_CLIENT_IS_CONNECTED,<br />
    LAME_CLIENT_NONE = 9,<br />
    LAME_CLIENT_LAST<br />
} TestEnum;</p>
<h2>C++ MODE</h2>
<p> There is a C++ mode so that gob creates C++ compiler friendly files. You need to use the &#8211;for-cpp argument to gob. This will make the generated file have a .cc instead of a .c extension, and several things will be adjusted to make it all work for a C++ compiler. One thing that will be missing is an alias to the new method, as that clashes with C++, so instead you&#8217;ll have to use the full name of the method inside your code. Also note that gob does not use any C++ features, this option will just make the generated code compile with a C++ compiler. </p>
<h2>OVERRIDING THE GET_TYPE METHOD</h2>
<p> The get_type is not really a method, but a function which initializes your object. Recently objects appeared which require you to make a custom get_type function. So it is possible to override this function. To do so, just define a new public method called get_type, with no arguments. Example:<br />
public<br />
GType get_type(void)<br />
{<br />
    /* code goes here */<br />
    return some_type;<br />
}</p>
<h2>INTERFACES</h2>
<p> Currently gob will only allow you to implement interfaces (that is, define new classes which implement an interface) and doesn&#8217;t yet have support for making new interfaces, but this will be coming at some point in the future. </p>
<p> To define a class that implements an interface add a class flag &#8216;interface&#8217; with the type name of the interface as an argument. Then to implement a specific method of the interface, just add &#8216;interface &lt;typename&gt;&#8217; before the method definition. The method can, and probably should be, private. </p>
<p> The following example implements a new object, that implements the Gtk:Tree:Model interface and implements the get_flags method of that interface. Do note that except for standard (GTK+ and glib) specific interfaces which seem to have a non-standard name for the interface structure, the structure should end with and Iface, if you are implementing an interface. That is for example for the Gtk:Tree:Model, the structure containing the table of methods should be named GtkTreeModelIface.<br />
class Some : Object from G : Object(interface Gtk:Tree<br />
                                    : Model)<br />
{<br />
    /* function implemented for the Gtk:Tree:Model interface */<br />
    interface Gtk : Tree : Model private GtkTreeModelFlags<br />
                           get_flags(Gtk:Tree<br />
                                     : Model *self(check null type))<br />
    {<br />
        /* Here would be the implementation */<br />
        return (GtkTreeModelFlags)0;<br />
    }<br />
}</p>
<p> If you want to implement multiple interfaces just list more class flag lines as follows: </p>
<pre>
  class Some:Object from G:Object
          (interface Gtk:Tree:Model)
          (interface Gtk:Editable)
  {
          /* ... */
  }
</pre>
<h2>DIRECT BonoboObject SUPPORT</h2>
<p> If you want to build a BonoboObject class gob2 has direct support for these. Just create a new object that derives from Bonobo:Object. Then use a &quot;BonoboObject&quot; class flag with the interface name as an argument. The interface name should be as you would type it in C, that is with underscores as namespace separators. Then you add the methods (using exact same names as in the idl file) and prepend those methods with a BonoboObject keyword. For example imagine you have an interface GNOME/Foo/SomeInterface, with a method fooBar that takes a single string:<br />
class Foo : Some : Interface from Bonobo : Object(BonoboObject GNOME_Foo_SomeInterface)<br />
{<br />
    BonoboObject private void<br />
    fooBar(PortableServer_Servant servant,<br />
           const CORBA_char *string,<br />
           CORBA_Environment *ev)<br />
    {<br />
        Self *self = SELF(bonobo_object_from_servant(servant));<br />
        /* your code here */<br />
    }<br />
    /* rest of class */<br />
}<br />
 Note that the implementation method can be private, in fact that&#8217;s probably a good idea to do. It won&#8217;t work to make this a signal, it can however be a virtual. Note that the method prototype must match the one from the interface header file, or you will get a bad assignment warning. You should check the header file generated by orbit-idl and see the epv structure for the correct prototypes if you can&#8217;t figure them out from the idl itself. Also note that the first argument is not &quot;self&quot;, but the servant and you must use bonobo_object_from_servant function to get the actual object pointer. </p>
<h2>DIRECT LIBGLADE SUPPORT</h2>
<p> Gob can simplify writing a libglade class. Just create a new object that derives from a GtkContainer widget. Then use a &quot;GladeXML&quot; class flag with the glade file name, root widget and optional domain as arguments between double quotes. For example: </p>
<pre>
class My:Glade from Gtk:Window (GladeXML &quot;gob-libglade.glade&quot; &quot;root&quot;)
{
  ....
}
</pre>
<p> Note however that then &quot;gob-libglade.glade&quot; would have to be in the current directory. You could specify a path, but that may not work for all installations. You can replace the glade filename with a token to be used in the generated .c file and you can then have a macro with the filename, as follows: </p>
<pre>
class My:Glade from Gtk:Window (GladeXML GLADE_FILE &quot;root&quot;)
{
  ....
}
</pre>
<p> And somewhere in your header files you would have<br />
#define GLADE_FILE &#8220;/path/to/file.glade&#8221;</p>
<p> You can declare widgets as data members by adding a &#8216;GladeXML&#8217; to the definition. </p>
<pre>
private Gtk:Button * button1 GladeXML;
</pre>
<p> This will automatically set the &quot;button1&quot; from the GladeXML file. </p>
<p> All signals created with glade are automatically connected if you defined those class methods in your class. For example suppose in glade that we set the &quot;connect&quot; signal on button1 to go to on_button1_clicked, then in our gob file we can just write: </p>
<pre>
public void
on_button1_clicked(self, GtkButton * button)
{
}
</pre>
<p> See the examples directory for a full example. Note that this feature requires version at least 2.0.12. </p>
<h2>IDENTIFIER CONFLICTS</h2>
<p> Gob will need to define some local variables and functions in the generated files, so you need to take some precaution not to conflict with these. The general rule of thumb is that all of these start with three underscores. There is one, &quot;parent_class&quot; which doesn&#8217;t because it&#8217;s intended for use in your code. For virtuals or signals, you cannot use the identifier __parent__ which is used for the parent of the object. You should actually never access __parent__ either as it not guaranteed that it will stay named this way. Data members cannot be named __parent__ nor _priv. For methods, you cannot use the identifiers &quot;init&quot; or &quot;class_init&quot; unless you mean the constructor methods. You shouldn&#8217;t generally use 3 underscores even in override method argument lists and virtual and signal method names as it might confuse the PARENT_HANDLER macro. In fact avoiding all names with three underscores is the best policy when working with gob. </p>
<p> There are a couple of defines which you shouldn&#8217;t be redefining in the code or other headers. These are SELF, IS_SELF, SELF_CLASS, SELF_TYPE, ARG, VAR, PARENT_HANDLER, GET_NEW, GOB_VERSION_MAJOR, GOB_VERSION_MINOR and GOB_VERSION_PATCHLEVEL. </p>
<p> As for types, there are Self and SelfClass types which are only defined in your source files. Their generation (just like the generation of the SELF macros) can be turned off, see command line options. </p>
<h2>USING GTK-DOC STYLE INLINE DOCUMENTATION</h2>
<p> If you want to use gtk-doc style inline documentation for your objects, you can do one of two things. First, you could include the inline documentation comments in your %{ %} section which will then be put verbatim into the output source file. This is the way you should use for functions you define outside of the class. </p>
<p> For class methods, you should use a gtk+ style comment, however it can be indented any number of tabs or spaces and you can use the short method name without the type prefix. Gob will automatically try to extract these and translate to full names and put them in the output source file. An example would be:<br />
class Gtk : Button : Example from Gtk : Button<br />
{<br />
    /**<br />
     * new:<br />
     *<br />
     * Makes a new #GtkButtonExample widget<br />
     *<br />
     * Returns: a new widget<br />
     **/<br />
  public<br />
    GtkWidget *new (void)<br />
    {<br />
        return (GtkWidget *)GET_NEW;<br />
    }<br />
}<br />
 If the function you are documenting is a signal or a virtual then it will be documenting the wrapper that starts that virtual function or emits that signal. </p>
<h2>DEALING WITH CIRCULAR HEADERS</h2>
<p> Sometimes you may need to use an object of type MyObjectA in the MyObjectB class and vice versa. Obviously you can&#8217;t include headers for both. So you need to just declare the typedef in the header of A for B, and the other way around as well. The headers generated include a protecting define before it declares the typedef. This define is the __TYPEDEF_&lt;upper case object name&gt;__. So inside my-object-a.h there will be this:<br />
#ifndef __TYPEDEF_MY_OBJECT_A__<br />
#define __TYPEDEF_MY_OBJECT_A__<br />
typedef struct _MyObjectA MyObjectA;<br />
#endif<br />
 Now instead of including my-object-a.h in the header section of my-object-b.gob, just copy the above code there and you&#8217;re set for using MyObjectA as a type in the method parameters and public types. </p>
<p> Another way to get out of this problem is if you can use those types only in the private members, in which case they won&#8217;t be in the generated public header. </p>
<h2>BUILDING WITH MAKE</h2>
<p> If you are using normal makefiles, what you need to do is to add a generic rule for .gob files. So you would include the following in the Makefile and then just use the .c and .h files as usual (make sure the space before the &#8216;gob2&#8217; is a tab, not spaces): </p>
<pre>
  %.c %.h %-private.h: %.gob
          gob2 $&lt;
</pre>
<h2>BUILDING WITH AUTOCONF and AUTOMAKE</h2>
<p> This is a little bit more involved. Basically the first thing to do is to check for GOB2 in your configure.in file. You can use the supplied m4 macro which will also check the version of gob. Basically you include this: </p>
<pre>
  GOB2_CHECK([2.0.0])
</pre>
<p> This will replace @GOB2@ in your makefiles with the full path of gob2. Thus when adding the generic rule to your Makefile.am file, it should look like: </p>
<pre>
  %.c %.h %-private.h: %.gob
          @GOB2@ $&lt;
</pre>
<p> For Makefile.am you have to set up a couple more things. First you have to include the generated .c and .h files into BUILT_SOURCES variable. You have to include both the .gob and the .c and .h files in the SOURCES for your program. </p>
<h2>PREVENTING SPURIOUS BUILDS</h2>
<p> When nothing has changed you might not really want to rebuild everything and gob provides options &#8211;no-touch (since 2.0.13) and &#8211;no-touch-headers to avoid this. When working with build systems such as automake you have to be more careful as just using those options can cause automake to get confused and you will need to use something like the following: </p>
<pre>
  foo_SOURCES = foo.gob foo.gob.stamp foo.c foo.h foo-private.h
  BUILT_SOURCES = foo.gob.stamp
  MAINTAINERCLEANFILES = foo.gob.stamp
  %.gob.stamp: %.gob
          @GOB2@ --no-touch $&lt;
          @touch $@
</pre>
<h2>DEBUGGING</h2>
<p> GOB does several things to make debugging the code easier. First it adds preprocessor commands into the output c file that point to the correct places in your .gob input file. However sometimes there might be some bigger confusion and this is just not helpful. In this case you will probably want to have gcc point you directly at the generated files. For this use the &#8211;no-lines command line option. You should also note that these commands are not generated for the public header file at all. If there is an error which points you to the public header file, make sure you fix this error in the .gob file, otherwise your changes will not have any effect after gob recompiles the sources again. </p>
<p> Sometimes you might want to know which method you are in for some debugging output. GOB will define __GOB_FUNCTION__ macro, which is just a string constant with a pretty name of the method. </p>
<h2>M4 SUPPORT</h2>
<p> It is possible to have your .gob file also preprocessed by m4. This is useful if you have a lot of files and you&#8217;d like to have some preprocessor put in some common features. All you have to do is add &#8211;m4 to the command line of gob2 and gob2 will first run your file through m4. You can print the directory that is searched for m4 files by running &quot;gob2 &#8211;m4-dir&quot; </p>
<p> All the arguments after &#8211;m4 will be passed to m4 itself, so it has to be the last gob2 argument on the command line. This way you can specify arbitrary options to pass to m4. </p>
<h2>BUGS</h2>
<p> The lexer does not actually parse the C code, so I&#8217;m sure that some corner cases or maybe even some not so corner cases of C syntax might confuse gob completely. If you find any, send me the source that makes it go gaga and I&#8217;ll try to make the lexer try to handle it properly, but no promises. </p>
<p> Another thing is that gob ignores preprocessor macros. Since gob counts braces, the following code won&#8217;t work:<br />
#ifdef SOME_DEFINE<br />
if (foo) {<br />
#else<br />
if (bar) {<br />
#endif<br />
    blah();<br />
}<br />
 To make this work, you&#8217;d have to do this:<br />
#ifdef SOME_DEFINE<br />
if (foo)<br />
#else<br />
if (bar)<br />
#endif<br />
{<br />
    blah();<br />
}<br />
 There is no real good way we can handle this without parsing C code, so we probably never will. In the future, I might add #if 0 as a comment but that&#8217;s about as far as I can really take it and even that is problematic. Basically, if you use gob, just don&#8217;t use the C preprocessor too extensively. And if you use it make sure that you do not cross the boundaries of the C code segments. </p>
<p> Comments will not get through to the generated files unless inside C code. This is not the case for gtk-doc style comments which are supported. </p>
<p> The short name aliases are actually implemented as pointers to functions. Thus if you want to get the pointer of a function using the short name alias you can&#8217;t use the &#8216;&amp;&#8217;. Thus: </p>
<pre><code>
void (*foo)(Self *);
/* this will NOT work */
foo = &amp;self_short_name;
/* this will work */
foo = self_short_name;
/* Both of these will work */
foo = &amp;my_class_long_name;
foo = my_class_long_name;
</code></pre>
<h2>AUTHOR</h2>
<p> George Lebl &lt;jirka [at] 5z.com&gt; </p>
<p> GOB2 Homepage: <a rel="nofollow" href="http://www.jirka.org/gob.html">http://www.jirka.org/gob.html</a> </p>
<h2>Index</h2>
