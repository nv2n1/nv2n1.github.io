---
title: "glib-genmarshal(1)"
name: "glib-genmarshal"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glib-genmarshal/"
description: "glib-genmarshal – C code marshaller generation utility for GLib closures"
---

<h2 class="name">NAME</h2>
<p> glib-genmarshal &#8211; C code marshaller generation utility for GLib closures </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>glib-genmarshal</code> [OPTION&#8230;] [FILE&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>glib-genmarshal</code></p>
<dd>is a small utility that generates C code marshallers for callback functions of the GClosure mechanism in the GObject sublibrary of GLib. The marshaller functions have a standard signature, they get passed in the invoking closure, an array of value structures holding the callback function parameters and a value structure for the return value of the callback. The marshaller is then responsible to call the respective C code function of the closure with all the parameters on the stack and to collect its return value. </p>
<p> <code>glib-genmarshal</code> takes a list of marshallers to generate as input. The marshaller list is either read from files passed as additional arguments on the command line; or from standard input, by using &#8211; as the input file.</p>
<h3>Marshaller list format</h3>
<p> The marshaller lists are processed line by line, a line can contain a comment in the form of </p>
<p> or a marshaller specification of the form </p>
<dl>
<dt>
<dd>
<pre>
<i>RTYPE</i>:<i>PTYPE</i>
<i>RTYPE</i>:<i>PTYPE</i>,<i>PTYPE</i>
<i>RTYPE</i>:<i>PTYPE</i>,<i>PTYPE</i>,<i>PTYPE</i>
</pre>
</dl>
<p> The <i>RTYPE</i> part specifies the callback&#8217;s return type and the <i>PTYPE</i>s right to the colon specify the callback&#8217;s parameter list, except for the first and the last arguments which are always pointers.</p>
<h3>Parameter types</h3>
<p> Currently, the following types are supported: </p>
<p> <i>VOID</i></p>
<dl>
<dt>
<dd> indicates no return type, or no extra parameters. If <i>VOID</i> is used as the parameter list, no additional parameters may be present.</dl>
<p> <i>BOOLEAN</i></p>
<dl>
<dt>
<dd> for boolean types (gboolean)</dl>
<p> <i>CHAR</i></p>
<dl>
<dt>
<dd> for signed char types (gchar)</dl>
<p> <i>UCHAR</i></p>
<dl>
<dt>
<dd> for unsigned char types (guchar)</dl>
<p> <i>INT</i></p>
<dl>
<dt>
<dd> for signed integer types (gint)</dl>
<p> <i>UINT</i></p>
<dl>
<dt>
<dd> for unsigned integer types (guint)</dl>
<p> <i>LONG</i></p>
<dl>
<dt>
<dd> for signed long integer types (glong)</dl>
<p> <i>ULONG</i></p>
<dl>
<dt>
<dd> for unsigned long integer types (gulong)</dl>
<p> <i>INT64</i></p>
<dl>
<dt>
<dd> for signed 64bit integer types (gint64)</dl>
<p> <i>UINT64</i></p>
<dl>
<dt>
<dd> for unsigned 64bit integer types (guint64)</dl>
<p> <i>ENUM</i></p>
<dl>
<dt>
<dd> for enumeration types (gint)</dl>
<p> <i>FLAGS</i></p>
<dl>
<dt>
<dd> for flag enumeration types (guint)</dl>
<p> <i>FLOAT</i></p>
<dl>
<dt>
<dd> for single-precision float types (gfloat)</dl>
<p> <i>DOUBLE</i></p>
<dl>
<dt>
<dd> for double-precision float types (gdouble)</dl>
<p> <i>STRING</i></p>
<dl>
<dt>
<dd> for string types (gchar*)</dl>
<p> <i>BOXED</i></p>
<dl>
<dt>
<dd> for boxed (anonymous but reference counted) types (GBoxed*)</dl>
<p> <i>PARAM</i></p>
<dl>
<dt>
<dd> for GParamSpec or derived types (GParamSpec*)</dl>
<p> <i>POINTER</i></p>
<dl>
<dt>
<dd> for anonymous pointer types (gpointer)</dl>
<p> <i>OBJECT</i></p>
<dl>
<dt>
<dd> for GObject or derived types (GObject*)</dl>
<p> <i>VARIANT</i></p>
<dl>
<dt>
<dd> for GVariant types (GVariant*)</dl>
<p> <i>NONE</i></p>
<dl>
<dt>
<dd> deprecated alias for <i>VOID</i></dl>
<p> <i>BOOL</i></p>
<dl>
<dt>
<dd> deprecated alias for <i>BOOLEAN</i></dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;header</code></p>
<dl>
<dt>
<dd> Generate header file contents of the marshallers. This option is mutually exclusive with the <code>&#8211;body</code> option.</dl>
<p> <code>&#8211;body</code></p>
<dl>
<dt>
<dd> Generate C code file contents of the marshallers. This option is mutually exclusive with the <code>&#8211;header</code> option.</dl>
<p> <code>&#8211;prefix=</code><i>PREFIX</i></p>
<dl>
<dt>
<dd> Specify marshaller prefix. The default prefix is `g_cclosure_user_marshal&#8217;.</dl>
<p> <code>&#8211;skip-source</code></p>
<dl>
<dt>
<dd> Skip source location remarks in generated comments.</dl>
<p> <code>&#8211;stdinc</code></p>
<dl>
<dt>
<dd> Use the standard marshallers of the GObject library, and include glib-object.h in generated header files. This option is mutually exclusive with the <code>&#8211;nostdinc</code> option.</dl>
<p> <code>&#8211;nostdinc</code></p>
<dl>
<dt>
<dd> Do not use the standard marshallers of the GObject library, and skip glib-object.h include directive in generated header files. This option is mutually exclusive with the <code>&#8211;stdinc</code> option.</dl>
<p> <code>&#8211;internal</code></p>
<dl>
<dt>
<dd> Mark generated functions as internal, using G_GNUC_INTERNAL.</dl>
<p> <code>&#8211;valist-marshallers</code></p>
<dl>
<dt>
<dd> Generate valist marshallers, for use with <code>g_signal_set_va_marshaller()</code>.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version information.</dl>
<p> <code>&#8211;g-fatal-warnings</code></p>
<dl>
<dt>
<dd> Make warnings fatal, that is, exit immediately once a warning occurs.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print brief help and exit.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version and exit.</dl>
<p> <code>&#8211;output=FILE</code></p>
<dl>
<dt>
<dd> Write output to <i>FILE</i> instead of the standard output.</dl>
<p> <code>&#8211;prototypes</code></p>
<dl>
<dt>
<dd> Generate function prototypes before the function definition in the C source file, in order to avoid a missing-prototypes compiler warning. This option is only useful when using the <code>&#8211;body</code> option.</dl>
<p> <code>&#8211;pragma-once</code></p>
<dl>
<dt>
<dd> Use the once pragma instead of an old style header guard when generating the C header file. This option is only useful when using the <code>&#8211;header</code> option.</dl>
<p> <code>&#8211;include-header=</code><i>HEADER</i></p>
<dl>
<dt>
<dd> Adds a #include directive for the given file in the C source file. This option is only useful when using the <code>&#8211;body</code> option.</dl>
<p> <code>-D </code><i>SYMBOL[=VALUE]</i></p>
<dl>
<dt>
<dd> Adds a #define C pre-processor directive for <i>SYMBOL</i> and its given <i>VALUE</i>, or &quot;1&quot; if the value is unset. You can use this option multiple times; if you do, all the symbols will be defined in the same order given on the command line, before the symbols undefined using the <code>-U</code> option. This option is only useful when using the <code>&#8211;body</code> option.</dl>
<p> <code>-U </code><i>SYMBOL</i></p>
<dl>
<dt>
<dd> Adds a #undef C pre-processor directive to undefine the given <i>SYMBOL</i>. You can use this option multiple times; if you do, all the symbols will be undefined in the same order given on the command line, after the symbols defined using the <code>-D</code> option. This option is only useful when using the <code>&#8211;body</code> option.</dl>
<p> <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Minimizes the output of <code>glib-genmarshal</code>, by printing only warnings and errors. This option is mutually exclusive with the <code>&#8211;verbose</code> option.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Increases the verbosity of <code>glib-genmarshal</code>, by printing debugging information. This option is mutually exclusive with the <code>&#8211;quiet</code> option.</dl>
<h2>USING GLIB-GENMARSHAL WITH MESON</h2>
<p> Meson supports generating closure marshallers using <code>glib-genmarshal</code> out of the box in its &quot;gnome&quot; module. </p>
<p> In your meson.build file you will typically call the gnome.genmarshal() method with the source list of marshallers to generate: </p>
<dl>
<dt>
<dd>
<pre>
gnome = import('gnome')
marshal_files = gnome.genmarshal('marshal',
  sources: 'marshal.list',
  internal: true,
)
</pre>
</dl>
<p> The marshal_files variable will contain an array of two elements in the following order: </p>
<dl>
<dt>
<dd> &bull; a build target for the source file</dl>
<dl>
<dt>
<dd> &bull; a build target for the header file</dl>
<p> You should use the returned objects to provide a dependency on every other build target that references the source or header file; for instance, if you are using the source to build a library: </p>
<dl>
<dt>
<dd>
<pre>
mainlib = library('project',
  sources: project_sources + marshal_files,
  ...
)
</pre>
</dl>
<p> Additionally, if you are including the generated header file inside a build target that depends on the library you just built, you must ensure that the internal dependency includes the generated header as a required source file: </p>
<dl>
<dt>
<dd>
<pre>
mainlib_dep = declare_dependency(sources: marshal_files[1], link_with: mainlib)
</pre>
</dl>
<p> You should not include the generated source file as well, otherwise it will be built separately for every target that depends on it, causing build failures. To know more about why all this is required, please refer to the m[blue]<code>corresponding Meson FAQ entry</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> For more information on how to use the method, see the m[blue]<code>Meson documentation for gnome.genmarshal()</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>USING GLIB-GENMARSHAL WITH AUTOTOOLS</h2>
<p> In order to use <code>glib-genmarshal</code> in your project when using Autotools as the build system, you will first need to modify your configure.ac file to ensure you find the appropriate command using <code>pkg-config</code>, similarly as to how you discover the compiler and linker flags for GLib. </p>
<dl>
<dt>
<dd>
<pre><code>
PKG_PROG_PKG_CONFIG([0.28])
PKG_CHECK_VAR([GLIB_GENMARSHAL], [glib - 2.0], [glib_genmarshal])
</code></pre>
</dl>
<p> In your Makefile.am file you will typically need very simple rules to generate the C files needed for the build. </p>
<dl>
<dt>
<dd>
marshal.h : marshal.list<br />
            $(AM_V_GEN) $(GLIB_GENMARSHAL)&#8211; header<br />
            &#8212; output = $ @$ &lt;<br />
                        marshal.c : marshal.list marshal.h<br />
                                    $(AM_V_GEN) $(GLIB_GENMARSHAL)&#8211; include<br />
                            &#8211; header = marshal.h<br />
                                       &#8212; body<br />
                                       &#8212; output = $ @$ &lt;<br />
                                                   BUILT_SOURCES<br />
    += marshal.h marshal.c<br />
       CLEANFILES<br />
    += marshal.h marshal.c<br />
       EXTRA_DIST<br />
    += marshal.list
</dl>
<p> In the example above, the first rule generates the header file and depends on a marshal.list file in order to regenerate the result in case the marshallers list is updated. The second rule generates the source file for the same marshal.list, and includes the file generated by the header rule.</p>
<h2>EXAMPLE</h2>
<p> To generate marshallers for the following callback functions: </p>
<dl>
<dt>
<dd>
void foo(gpointer data1,<br />
         gpointer data2);<br />
void bar(gpointer data1,<br />
         gint param1,<br />
         gpointer data2);<br />
gfloat baz(gpointer data1,<br />
           gboolean param1,<br />
           guchar param2,<br />
           gpointer data2);
</dl>
<p> The marshaller.list file has to look like this: </p>
<dl>
<dt>
<dd>
<pre>
VOID:VOID
VOID:INT
FLOAT:BOOLEAN,UCHAR
</pre>
</dl>
<p> and you call glib-genmarshal like this: </p>
<dl>
<dt>
<dd>
<pre>
glib-genmarshal --header marshaller.list &gt; marshaller.h
glib-genmarshal --body marshaller.list &gt; marshaller.c
</pre>
</dl>
<p> The generated marshallers have the arguments encoded in their function name. For this particular list, they are </p>
<dl>
<dt>
<dd>
<pre>
g_cclosure_user_marshal_VOID__VOID(...),
g_cclosure_user_marshal_VOID__INT(...),
g_cclosure_user_marshal_FLOAT__BOOLEAN_UCHAR(...).
</pre>
</dl>
<p> They can be used directly for GClosures or be passed in as the GSignalCMarshaller c_marshaller; argument upon creation of signals: </p>
<dl>
<dt>
<dd>
<pre><code>
GClosure *cc_foo, *cc_bar, *cc_baz;
cc_foo = g_cclosure_new(NULL, foo, NULL);
g_closure_set_marshal(cc_foo, g_cclosure_user_marshal_VOID__VOID);
cc_bar = g_cclosure_new(NULL, bar, NULL);
g_closure_set_marshal(cc_bar, g_cclosure_user_marshal_VOID__INT);
cc_baz = g_cclosure_new(NULL, baz, NULL);
g_closure_set_marshal(cc_baz, g_cclosure_user_marshal_FLOAT__BOOLEAN_UCHAR);
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-glib-mkenums/">glib-mkenums</a></code>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> corresponding Meson FAQ entry</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://mesonbuild.com/FAQ.html#how-do-i-tell-meson-that-my-sources-use-generated-headers">https://mesonbuild.com/FAQ.html#how-do-i-tell-meson-that-my-sources-use-generated-headers</a></dl>
<dt> 2.</p>
<dd> Meson documentation for gnome.genmarshal()</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://mesonbuild.com/Gnome-module.html#gnomegenmarshal">https://mesonbuild.com/Gnome-module.html#gnomegenmarshal</a></dl>
</dl>
<h2>Index</h2>
