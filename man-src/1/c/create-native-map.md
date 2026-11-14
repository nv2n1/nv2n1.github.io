---
title: "create-native-map(1)"
name: "create-native-map"
section: "1"
letter: "c"
url: "/docs/linux/man/1-create-native-map/"
description: "create-native-map – C/C# Mapping Creator"
---

<h2>NAME</h2>
<p> create-native-map &#8211; C/C# Mapping Creator</p>
<h2>SYNOPSIS</h2>
<p> <code>create-native-map</code> [OPTIONS]* ASSEMBLY-FILE-NAME OUPUT-PREFIX</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;autoconf-header=HEADER</i></p>
<dd> <i>HEADER</i> is a header file name in the syntax typically used with the C <i>#include</i> statement, e.g. <i>#include &lt;<a href="file:/usr/include/stdio.h">stdio.h</a>&gt;</i> or <i>#include local.h</i> . </p>
<p> An Autoconf-formatted macro is generated from the include name, and a <i>#include</i> directive is wrapped within a <i>#ifdef</i> block for the Autoconf macro within the generated <i>.c</i> file. </p>
<p> For example, <i>&#8211;autoconf-header=&lt;<a href="file:/usr/include/stdio.h">stdio.h</a>&gt;</i> would generate the code: </p>
<pre><code>
#ifndef HAVE_STDIO_H
#include &lt;stdio.h&gt;
#endif /* ndef HAVE_STDIO_H */
</code></pre>
<dt><i>&#8211;autoconf-member=MEMBER</i></p>
<dd> Specify that any access to <i>MEMBER</i> should be wrapped within a <i>#ifdef HAVE_MEMBER</i> block. <i>MEMBER</i> can be either a <i>field-name</i> or a <i>class-name</i> . <i>field-name</i> combination. </p>
<p> For example, given the C# declaration:<br />
[Mono.Unix.Native.Map(&#8220;struct dirent&#8221;)] struct Dirent {<br />
  public<br />
    long d_off;<br />
}<br />
 then <i>&#8211;autoconf-member=d_off</i> would generate the code similar to:<br />
int ToDirent(struct dirent *from, struct Dirent *to)<br />
{<br />
#ifdef HAVE_STRUCT_DIRENT_D_OFF<br />
    to-&gt;d_off = from-&gt;d_off;<br />
#endif /* ndef HAVE_STRUCT_DIRENT_D_OFF */<br />
}</p>
<dt><i>&#8211;exclude-native-symbol=SYMBOL</i></p>
<dd> <i>SYMBOL</i> is a <i>[DllImport]</i> -marked method that should <i>not</i> have a prototype generated for it.</p>
<dt><i>&#8211;impl-header=HEADER</i></p>
<dd> Insert a <i>#include</i> statement within the generated <i>.c</i> file for <i>HEADER</i> . </p>
<p> For example, <i>&#8211;impl-header=&lt;<a href="file:/usr/include/stdlib.h">stdlib.h</a>&gt;</i> generates<br />
#include &lt;stdlib.h&gt;</p>
<dt><i>&#8211;impl-macro=MACRO</i></p>
<dd> Insert a <i>#define</i> statement within the generated <i>.c</i> file. <i>MACRO</i> can contain a <i>=</i> to separate the macro name from the macro value. </p>
<p> For example, <i>&#8211;impl-macro=FOO=42</i> generates<br />
#define FOO 42</p>
<dt><i>&#8211;library=LIBRARY</i></p>
<dd> Create prototypes for <i>[DllImport]</i> -marked methods which reference the native library <i>LIBRARY</i> into the generated <i>.h</i> file.</p>
<dt><i>&#8211;public-header=HEADER</i></p>
<dd> Insert a <i>#include</i> statement within the generated <i>.h</i> file for <i>HEADER</i> . </p>
<p> For example, <i>&#8211;public-header=&lt;<a href="file:/usr/include/stdlib.h">stdlib.h</a>&gt;</i> generates<br />
#include &lt;stdlib.h&gt;</p>
<dt><i>&#8211;public-macro=MACRO</i></p>
<dd> Insert a <i>#define</i> statement within the generated <i>.h</i> file. <i>MACRO</i> can contain a <i>=</i> to separate the macro name from the macro value. </p>
<p> For example, <i>&#8211;public-macro=FOO=42</i> generates<br />
#define FOO 42</p>
<dt><i>&#8211;rename-member=FROM=TO</i></p>
<dd> This is used when <i>FROM</i> is a C macro, and thus must be altered in order to be used sanely. All generated references to the managed representation will use <i>TO </i> instead of <i>FROM</i> . </p>
<p> For example, given the C# declaration:<br />
[Mono.Unix.Native.Map(&#8220;struct stat&#8221;)] struct Stat {<br />
  public<br />
    long st_atime;<br />
}<br />
 and the argument <i>&#8211;rename-member=st_atime=st_atime_</i> , the generated <i>.h</i> file would contain:<br />
struct Stat {<br />
    gint64 st_atime_;<br />
};<br />
 (note the altered field name), while the generated <i>.c</i> file would contain:<br />
ToStat(struct stat *from, struct Stat *to)<br />
{<br />
    to-&gt;st_atime_ = from-&gt;st_atime;<br />
}</p>
<dt><i>&#8211;rename-namespace=FROM=TO</i></p>
<dd> By default, the C &quot;namespace&quot; (symbol prefix) is the C# namespace; types within the C# namespace <i>Mono.Unix.Native</i> would be in the C &quot;namespace&quot; <i>Mono_Unix_Native</i> . Use <i>&#8211;rename-namespace</i> to modify the default, e.g. <i>&#8211;rename-namespace=Mono.Unix.Native=Mono_Posix</i> .</dl>
<h2>DESCRIPTION</h2>
<p> <i>create-native-map</i> is a program for a specific scenario: keeping code which is tightly coupled between C and C# in sync with each other, based upon the C# types. </p>
<p> Platform Invoke is only useful if the managed code knows the exact types and layout of all unmanaged structures it uses. This is usually the case on Windows, but it is <i>not</i> the case on Unix. For example, <i>struct stat</i> makes use of types with sizes that will vary from platform to platform (or even based on the compiler macros defined!). For example, <i>off_t</i> is usually a signed 32-bit integer on ILP32 platforms, but may be a signed 64-bit integer on LP64 platforms, but may also be a 64-bit signed integer on ILP32 platforms if the <i>_FILE_OFFSET_BITS</i> macro has the value 64. In short, everything is flexible within Unix, and managed code can&#8217;t deal with such flexibility. </p>
<p> Thus, the niche for <i>create-native-map</i> : assume a fixed ABI that managed code can target, and generate code to &quot;thunk&quot; the managed representations to the corresponding native representations. This needs to be done for <i>everything</i> that can vary between platforms and compiler flags, from enumeration values ( <i>SIGBUS</i> has the value 10 on FreeBSD but 7 on Linux) to structure members (how big is <i>off_t</i> ?). </p>
<p> <i>create-native-map</i> will inspect <i>ASSEMBLY-FILE-NAME</i> and output the following files:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>OUTPUT-PREFIX.h</i></p>
<dd> Contains enumeration values, class and structure declarations, delegate declarations, and <i>[DllImport]</i> -marked methods (from the library specified by <i>&#8211;library</i> ) within the assembly <i>ASSEMBLY-FILE-NAME</i> .</p>
<dt><i>OUTPUT-PREFIX.c</i></p>
<dd> Contains the implementation of enumeration and structure conversion functions.</p>
<dt><i>OUTPUT-PREFIX.cs</i></p>
<dd> Contains a partial class <i>NativeConvert</i> containing enumeration translation methods.</p>
<dt><i>OUTPUT-PREFIX.xml</i></p>
<dd> Generates ECMA XML documentation stubs for the enumeration translation methods in <i>OUTPUT-PREFIX.cs</i> .</dl>
</dl>
<p> <i>create-native-map</i> primarily looks for <i>MapAttribute</i> -decorated types, and makes use of two <i>MapAttribute</i> properties:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>NativeType</i></p>
<dd> Contains the corresponding C type. Only useful if applied to classes, structures, and fields.</p>
<dt><i>SuppressFlags</i></p>
<dd> When specified on an enumeration member of a <i>[Flags]</i> -decorated enumeration type, <i>disables</i> the normal code generator support for bit-masking enumeration types. </p>
<p> This is useful when bitmask and non-bitmask information is stored within the same type, and bitmask checking shouldn&#8217;t be used for the non-bitmask values. Example: <i>Mono.Unix.Native.FilePermissions.S_IFREG</i> , which is not a bitmask value, while most of <i>FilePermissions</i> consists of bitmask values ( <i>FilePermissions.S_IRUSR</i> , <i>FilePermissions.S_IWUSR</i> , etc.).</dl>
</dl>
<p> The <i>MapAttribute</i> attribute can be specified on classes, structures, delegates, fields, and enumerations.</p>
<dl>
<dt>Delegates</p>
<dd> Code generation for delegates ignores the <i>MapAttribute.NativeType</i> property, and generates a function pointer <i>typedef</i> that best matches the delegate declaration into the <i>.h</i> file. </p>
<p> For example,<br />
namespace Foo<br />
{<br />
[Map] delegate string MyCallback(string s);<br />
}<br />
 generates the <i>typedef</i> :<br />
typedef char *(*Foo_MyCallback)(const char *s);</p>
<dt>Classes and Structures</p>
<dd> A <i>[Map]</i> -decorated class or structure will get a C structure declaration within the <i>.h</i> file:<br />
[Map] struct Foo {<br />
  public<br />
    int i;<br />
}<br />
 becomes<br />
struct Foo {<br />
  public<br />
    int i;<br />
};<br />
 If the <i>MapAttribute.NativeType</i> property is set, then conversion functions will be declared within the <i>.h</i> file and created within the <i>.c</i> file:<br />
namespace Foo<br />
{<br />
[Map(&#8220;struct stat&#8221;)] struct Stat {<br />
  public<br />
    uint st_uid;<br />
}<br />
}<br />
 becomes<br />
/* The .h file */<br />
struct Foo_Stat {<br />
    unsigned int st_uid;<br />
};<br />
int Foo_FromStat(struct Foo_Stat *from, struct stat *to);<br />
int Foo_ToStat(struct stat *to, sxtruct Foo_Stat *to);<br />
/* The .c file */<br />
int Foo_FromStat(struct Foo_Stat *from, struct stat *to)<br />
{<br />
                memset (to, 0, sizeof(*to);<br />
                to-&gt;st_uid = from-&gt;st_uid;<br />
                return 0;<br />
}<br />
int Foo_ToStat(struct stat *to, sxtruct Foo_Stat *to)<br />
{<br />
                memset (to, 0, sizeof(*to);<br />
                to-&gt;st_uid = from-&gt;st_uid;<br />
                return 0;<br />
}</p>
<dt>Fields</p>
<dd> If a field (1) has the <i>MapAttribute</i> attribute, and (2) has the <i>MapAttribute.NativeType</i> property set, then the specified native type will be used for overflow checking. For example:<br />
namespace Foo<br />
{<br />
[Map(&#8220;struct stat&#8221;)] struct Stat {<br />
    [Map(&#8220;off_t&#8221;)] public long st_size;<br />
}<br />
}<br />
 generates<br />
/* The .h file */<br />
struct Foo_Stat {<br />
    gint64 st_size;<br />
};<br />
int Foo_FromStat(struct Foo_Stat *from, struct stat *to);<br />
int Foo_ToStat(struct stat *to, sxtruct Foo_Stat *to);<br />
/* The .c file */<br />
int Foo_FromStat(struct Foo_Stat *from, struct stat *to)<br />
{<br />
    _cnm_return_val_if_overflow(off_t, from-&gt;st_size, -1);<br />
                memset (to, 0, sizeof(*to);<br />
                to-&gt;st_size = from-&gt;st_size;<br />
                return 0;<br />
}<br />
int Foo_ToStat(struct stat *to, sxtruct Foo_Stat *to)<br />
{<br />
    _cnm_return_val_if_overflow(gint64, from-&gt;st_size, -1);<br />
                memset (to, 0, sizeof(*to);<br />
                to-&gt;st_size = from-&gt;st_size;<br />
                return 0;<br />
}<br />
 This is useful for better error checking within the conversion functions. <i>MapAttribute.NativeType</i> is required for this as there is no other way to know what the native type is (without parsing the system header files&#8230;).</p>
<dt>Enumerations</p>
<dd> Generates a C enumeration and macros for each of the members within the enumeration. <i>To</i> and <i>From</i> functions are also declared in the <i>.h</i> file and implemented in the <i>.c</i> file. </p>
<p> For example,<br />
namespace Foo<br />
{<br />
[Map] enum Errno {<br />
    EINVAL<br />
}<br />
}<br />
 would generate the following in the <i>.h</i> file:<br />
enum Foo_Errno {<br />
    Foo_Errno_EINVAL = 0,<br />
#define Foo_Errno_EINVAL Foo_Errno_EINVAL<br />
};<br />
int Foo_FromErrno(int from, int *to);<br />
int Foo_ToErrno(int from, int *to);<br />
 and generates the following in the the <i>.c</i> file: </p>
<pre><code>
int Foo_FromErrno(int from, int *to)
{
    *to = 0;
    if (from == Foo_Errno_EPERM)
#ifdef EINVAL
    {
        *to = EINVAL;
    }
#else
    {
        errno = EINVAL;
        return -1;
    }
#endif
    return 0;
}
int Foo_ToErrno(int from, int *to)
{
    *to = 0;
#ifdef EINVAL
    if (from == EINVAL) {
        *to = Foo_Errno_EPERM;
        return 0;
    }
#endif
    return -1;
}
</code></pre>
<p> Different code will be generated if the managed enum is a <i>[Flags]</i> -decorated enumeration (to account for bitwise flags), but this is the basic idea.</dl>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
