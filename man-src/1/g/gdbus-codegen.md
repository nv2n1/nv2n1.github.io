---
title: "gdbus-codegen(1)"
name: "gdbus-codegen"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdbus-codegen/"
description: "gdbus-codegen – D-Bus code and documentation generator"
---

<h2 class="name">NAME</h2>
<p> gdbus-codegen &#8211; D-Bus code and documentation generator </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gdbus-codegen</code> [<code>-h</code>,&nbsp;<code>&#8211;help</code>] [<code>&#8211;interface-prefix</code>&nbsp;<i>org.project.Prefix</i>] [<code>&#8211;generate-c-code</code>&nbsp;<i>OUTFILES</i>] [<code>&#8211;c-namespace</code>&nbsp;<i>YourProject</i>] [<code>&#8211;c-generate-object-manager</code>] [<code>&#8211;c-generate-autocleanup</code>&nbsp;none|objects|all] [<code>&#8211;output-directory</code>&nbsp;<i>OUTDIR</i>] [<code>&#8211;generate-docbook</code>&nbsp;<i>OUTFILES</i>] [<code>&#8211;pragma-once</code>] [<code>&#8211;xml-files</code>&nbsp;<i>FILE</i>] [<code>&#8211;header</code>] [<code>&#8211;body</code>] [<code>&#8211;interface-info-header</code>] [<code>&#8211;interface-info-body</code>] [<code>&#8211;output</code>&nbsp;<i>OUTFILE</i>] [<code>&#8211;annotate</code>&nbsp;<i>ELEMENT</i>&nbsp;<i>KEY</i>&nbsp;<i>VALUE</i>]&#8230; [<code>&#8211;glib-min-required</code>&nbsp;<i>VERSION</i>] [<code>&#8211;glib-max-allowed</code>&nbsp;<i>VERSION</i>] FILE [FILE&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gdbus-codegen</code></p>
<dd>is used to generate code and/or documentation for one or more D-Bus interfaces. </p>
<p> <code>gdbus-codegen</code> reads m[blue]<code>D-Bus Introspection XML</code>m[]<font SIZE="-2">[1]</font> from files passed as additional arguments on the command line and generates output files. It currently supports generating C source code (via <code>&#8211;body</code>) or header (via <code>&#8211;header</code>) and Docbook XML (via <code>&#8211;generate-docbook</code>). Alternatively, more restricted C source code and headers can be generated, which just contain the interface information (as <code>GDBusInterfaceInfo</code> structures) using <code>&#8211;interface-info-body</code> and <code>&#8211;interface-info-header</code>.</p>
<h2>GENERATING C CODE</h2>
<p> When generating C code, a #GInterface -derived type is generated for each D-Bus interface. Additionally, for every generated type, <code>FooBar</code>, two concrete instantiable types, <code>FooBarProxy</code> and <code>FooBarSkeleton</code>, implementing said interface are also generated. The former is derived from #GDBusProxy and intended for use on the client side while the latter is derived from the #GDBusInterfaceSkeleton type making it easy to export on a #GDBusConnection either directly or via a #GDBusObjectManagerServer instance. </p>
<p> For C code generation either <code>&#8211;body</code> that generates source code, <code>&#8211;header</code> that generates headers, <code>&#8211;interface-info-body</code> that generates interface information source code, or <code>&#8211;interface-info-header</code> that generates interface information headers, can be used. These options must be used along with <code>&#8211;output</code>, which is used to specify the file to output to. </p>
<p> Both files can be generated at the same time by using <code>&#8211;generate-c-code</code>, but this option is deprecated. In this case <code>&#8211;output</code> cannot be used due to the generation of multiple files. Instead pass <code>&#8211;output-directory</code> to specify the directory to put the output files in. By default the current directory will be used. </p>
<p> The name of each generated C type is derived from the D-Bus interface name stripped with the prefix given with <code>&#8211;interface-prefix</code> and with the dots removed and initial characters capitalized. For example, for the D-Bus interface com.acme.Coyote the name used is ComAcmeCoyote. For the D-Bus interface org.project.Bar.Frobnicator with <code>&#8211;interface-prefix</code> org.project., the name used is BarFrobnicator. </p>
<p> For methods, signals and properties, if not specified, the name defaults to the name of the method, signal or property. </p>
<p> Two forms of the name are used &#8211; the CamelCase form and the lower-case form. The CamelCase form is used for the #GType and struct name, while lower-case form is used in function names. The lower-case form is calculated by converting from CamelCase to lower-case and inserting underscores at word boundaries (using certain heuristics). </p>
<p> If the value given by the org.gtk.GDBus.C.Name annotation or the <code>&#8211;c-namespace</code> option contains an underscore (sometimes called <i>Ugly_Case</i>), then the camel-case name is derived by removing all underscores, and the lower-case name is derived by lower-casing the string. This is useful in some situations where abbreviations are used. For example, if the annotation is used on the interface net.MyCorp.MyApp.iSCSITarget with the value iSCSI_Target the CamelCase form is iSCSITarget while the lower-case form is iscsi_target. If the annotation is used on the method EjectTheiPod with the value Eject_The_iPod, the lower-case form is eject_the_ipod.</p>
<h2>GENERATING DOCBOOK DOCUMENTATION</h2>
<p> Each generated Docbook XML file (see the <code>&#8211;generate-docbook</code> option for details) is a m[blue]<code>RefEntry</code>m[]<font SIZE="-2">[2]</font> article describing the D-Bus interface.</p>
<h2>OPTIONS</h2>
<p> The following options are supported: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help and exit.</dl>
<p> <code>&#8211;xml-files</code> <i>FILE</i></p>
<dl>
<dt>
<dd> This option is deprecated; use positional arguments instead. The D-Bus introspection XML file.</dl>
<p> <code>&#8211;interface-prefix</code> <i>org.project.Prefix.</i></p>
<dl>
<dt>
<dd> A prefix to strip from all D-Bus interface names when calculating the typename for the C binding and the Docbook m[blue]<code>sortas attribute</code>m[]<font SIZE="-2">[3]</font>.</dl>
<p> <code>&#8211;generate-docbook</code> <i>OUTFILES</i></p>
<dl>
<dt>
<dd> Generate Docbook Documentation for each D-Bus interface and put it in OUTFILES-NAME.xml where NAME is a place-holder for the interface name, e.g. net.Corp.FooBar and so on. </p>
<p> Pass <code>&#8211;output-directory</code> to specify the directory to put the output files in. By default the current directory will be used.</dl>
<p> <code>&#8211;generate-c-code</code> <i>OUTFILES</i></p>
<dl>
<dt>
<dd> Generate C code for all D-Bus interfaces and put it in OUTFILES.c and OUTFILES.h including any sub-directories. If you want the files to be output in a different location use <code>&#8211;output-directory</code> as OUTFILES.h including sub-directories will be referenced from OUTFILES.c. </p>
<p> The full paths would then be $(OUTDIR)/$(dirname $OUTFILES)/$(basename $OUTFILES).{c,h}.</dl>
<p> <code>&#8211;c-namespace</code> <i>YourProject</i></p>
<dl>
<dt>
<dd> The namespace to use for generated C code. This is expected to be in m[blue]<code>CamelCase</code>m[]<font SIZE="-2">[4]</font> or <i>Ugly_Case</i> (see above).</dl>
<p> <code>&#8211;pragma-once</code></p>
<dl>
<dt>
<dd> If this option is passed, the m[blue]<code>#pragma once</code>m[]<font SIZE="-2">[5]</font> preprocessor directive is used instead of include guards.</dl>
<p> <code>&#8211;c-generate-object-manager</code></p>
<dl>
<dt>
<dd> If this option is passed, suitable #GDBusObject, #GDBusObjectProxy, #GDBusObjectSkeleton and #GDBusObjectManagerClient subclasses are generated.</dl>
<p> <code>&#8211;c-generate-autocleanup</code> none|objects|all</p>
<dl>
<dt>
<dd> This option influences what types autocleanup functions are generated for. &#8216;none&#8217; means to not generate any autocleanup functions. &#8216;objects&#8217; means to generate them for object types, and &#8216;all&#8217; means to generate them for object types and interfaces. The default is &#8216;objects&#8217; due to a corner case in backwards compatibility with a few projects, but you should likely switch your project to use &#8216;all&#8217;. This option was added in GLib 2.50.</dl>
<p> <code>&#8211;output-directory</code> <i>OUTDIR</i></p>
<dl>
<dt>
<dd> Directory to output generated source to. Equivalent to changing directory before generation. </p>
<p> This option cannot be used with <code>&#8211;body</code>, <code>&#8211;header</code>, <code>&#8211;interface-info-body</code> or <code>&#8211;interface-info-header</code>; and <code>&#8211;output</code> must be used.</dl>
<p> <code>&#8211;header</code></p>
<dl>
<dt>
<dd> If this option is passed, it will generate the header code and write it to the disk by using the path and file name provided by <code>&#8211;output</code>. </p>
<p> Using <code>&#8211;generate-c-code</code>, <code>&#8211;generate-docbook</code> or <code>&#8211;output-directory</code> are not allowed to be used along with <code>&#8211;header</code> and <code>&#8211;body</code> options, because these options are used to generate only one file.</dl>
<p> <code>&#8211;body</code></p>
<dl>
<dt>
<dd> If this option is passed, it will generate the source code and write it to the disk by using the path and file name provided by <code>&#8211;output</code>. </p>
<p> Using <code>&#8211;generate-c-code</code>, <code>&#8211;generate-docbook</code> or <code>&#8211;output-directory</code> are not allowed to be used along with <code>&#8211;header</code> and <code>&#8211;body</code> options, because these options are used to generate only one file.</dl>
<p> <code>&#8211;interface-info-header</code></p>
<dl>
<dt>
<dd> If this option is passed, it will generate the header code for the <code>GDBusInterfaceInfo</code> structures only and will write it to the disk by using the path and file name provided by <code>&#8211;output</code>. </p>
<p> Using <code>&#8211;generate-c-code</code>, <code>&#8211;generate-docbook</code> or <code>&#8211;output-directory</code> are not allowed to be used along with the <code>&#8211;interface-info-header</code> and <code>&#8211;interface-info-body</code> options, because these options are used to generate only one file.</dl>
<p> <code>&#8211;interface-info-body</code></p>
<dl>
<dt>
<dd> If this option is passed, it will generate the source code for the <code>GDBusInterfaceInfo</code> structures only and will write it to the disk by using the path and file name provided by <code>&#8211;output</code>. </p>
<p> Using <code>&#8211;generate-c-code</code>, <code>&#8211;generate-docbook</code> or <code>&#8211;output-directory</code> are not allowed to be used along with the <code>&#8211;interface-info-header</code> and <code>&#8211;interface-info-body</code> options, because these options are used to generate only one file.</dl>
<p> <code>&#8211;output</code> <i>OUTFILE</i></p>
<dl>
<dt>
<dd> The full path where the header (<code>&#8211;header</code>, <code>&#8211;interface-info-header</code>) or the source code (<code>&#8211;body</code>, <code>&#8211;interface-info-body</code>) will be written, using the path and filename provided by <code>&#8211;output</code>. The full path could be something like $($OUTFILE).{c,h}. </p>
<p> Using <code>&#8211;generate-c-code</code>, <code>&#8211;generate-docbook</code> or <code>&#8211;output-directory</code> is not allowed along with <code>&#8211;output</code>, because the latter is used to generate only one file.</dl>
<p> <code>&#8211;annotate</code> <i>ELEMENT</i> <i>KEY</i> <i>VALUE</i></p>
<dl>
<dt>
<dd> Used to inject D-Bus annotations into the given XML files. It can be used with interfaces, methods, signals, properties and arguments in the following way: </p>
<dl>
<dt>
<dd>
<pre><code>
gdbus - codegen-- c - namespace MyApp-- generate - c - code myapp - generated-- annotate "org.project.InterfaceName" org.gtk.GDBus.C.Name MyFrobnicator-- annotate "org.project.InterfaceName:Property" bar bat-- annotate "org.project.InterfaceName.Method()" org.freedesktop.DBus.Deprecated true --annotate "org.project.InterfaceName.Method()[arg_name]" snake hiss-- annotate "org.project.InterfaceName::Signal" cat meow-- annotate "org.project.InterfaceName::Signal[arg_name]" dog wuff myapp - dbus - interfaces.xml
</code></pre>
</dl>
<p> Any UTF-8 string can be used for <i>KEY</i> and <i>VALUE</i>.</dl>
<p> <code>&#8211;glib-min-required</code> <i>VERSION</i></p>
<dl>
<dt>
<dd> Specifies the minimum version of GLib which the code generated by <code>gdbus-codegen</code> can depend on. This may be used to make backwards-incompatible changes in the output or behaviour of <code>gdbus-codegen</code> in future, which users may opt in to by increasing the value they pass for <code>&#8211;glib-min-required</code>. If this option is not passed, the output from <code>gdbus-codegen</code> is guaranteed to be compatible with all versions of GLib from 2.30 upwards, as that is when <code>gdbus-codegen</code> was first released. </p>
<p> Note that some version parameters introduce incompatible changes: all callers of the generated code might need to be updated, and if the generated code is part of a library&#8217;s API or ABI, then increasing the version parameter can result in an API or ABI break. </p>
<p> The version number must be of the form <i>MAJOR</i>.<i>MINOR</i>.<i>MICRO</i>, where all parts are integers. <i>MINOR</i> and <i>MICRO</i> are optional. The version number may not be smaller than 2.30. </p>
<p> If the version number is 2.64 or greater, the generated code will have the following features: (1) If a method has h (file descriptor) parameter(s), a <code>GUnixFDList</code> parameter will exist in the generated code for it (whereas previously the annotation org.gtk.GDBus.C.UnixFD was required), and (2) Method call functions will have two additional arguments to allow the user to specify <code>GDBusCallFlags</code> and a timeout value, as is possible when using <code>g_dbus_proxy_call()</code>.</dl>
<p> <code>&#8211;glib-max-allowed</code> <i>VERSION</i></p>
<dl>
<dt>
<dd> Specifies the maximum version of GLib which the code generated by <code>gdbus-codegen</code> can depend on. This may be used to ensure that code generated by <code>gdbus-codegen</code> is compilable with specific older versions of GLib that your software has to support. </p>
<p> The version number must be of the form <i>MAJOR</i>.<i>MINOR</i>.<i>MICRO</i>, where all parts are integers. <i>MINOR</i> and <i>MICRO</i> are optional. The version number must be greater than or equal to that passed to <code>&#8211;glib-min-required</code>. It defaults to the version of GLib which provides this <code>gdbus-codegen</code>.</dl>
<h2>SUPPORTED D-BUS ANNOTATIONS</h2>
<p> The following D-Bus annotations are supported by <code>gdbus-codegen</code>: </p>
<p> org.freedesktop.DBus.Deprecated</p>
<dl>
<dt>
<dd> Can be used on any &lt;interface&gt;, &lt;method&gt;, &lt;signal&gt; and &lt;property&gt; element to specify that the element is deprecated if its value is true. Note that this annotation is defined in the m[blue]<code>D-Bus specification</code>m[]<font SIZE="-2">[1]</font> and can only assume the values true and false. In particular, you cannot specify the version that the element was deprecated in nor any helpful deprecation message. Such information should be added to the element documentation instead. </p>
<p> When generating C code, this annotation is used to add #G_GNUC_DEPRECATED to generated functions for the element. </p>
<p> When generating Docbook XML, a deprecation warning will appear along the documentation for the element.</dl>
<p> org.gtk.GDBus.Since</p>
<dl>
<dt>
<dd> Can be used on any &lt;interface&gt;, &lt;method&gt;, &lt;signal&gt; and &lt;property&gt; element to specify the version (any free-form string but compared using a version-aware sort function) the element appeared in. </p>
<p> When generating C code, this field is used to ensure function pointer order for preserving ABI/API, see the section called &#8220;STABILITY GUARANTEES&#8221;. </p>
<p> When generating Docbook XML, the value of this tag appears in the documentation.</dl>
<p> org.gtk.GDBus.DocString</p>
<dl>
<dt>
<dd> A string with Docbook content for documentation. This annotation can be used on &lt;interface&gt;, &lt;method&gt;, &lt;signal&gt;, &lt;property&gt; and &lt;arg&gt; elements.</dl>
<p> org.gtk.GDBus.DocString.Short</p>
<dl>
<dt>
<dd> A string with Docbook content for short/brief documentation. This annotation can only be used on &lt;interface&gt; elements.</dl>
<p> org.gtk.GDBus.C.Name</p>
<dl>
<dt>
<dd> Can be used on any &lt;interface&gt;, &lt;method&gt;, &lt;signal&gt; and &lt;property&gt; element to specify the name to use when generating C code. The value is expected to be in m[blue]<code>CamelCase</code>m[]<font SIZE="-2">[4]</font> or <i>Ugly_Case</i> (see above).</dl>
<p> org.gtk.GDBus.C.ForceGVariant</p>
<dl>
<dt>
<dd> If set to a non-empty string, a #GVariant instance will be used instead of the natural C type. This annotation can be used on any &lt;arg&gt; and &lt;property&gt; element.</dl>
<p> org.gtk.GDBus.C.UnixFD</p>
<dl>
<dt>
<dd> If set to a non-empty string, the generated code will include parameters to exchange file descriptors using the #GUnixFDList type. This annotation can be used on &lt;method&gt; elements.</dl>
<p> As an easier alternative to using the org.gtk.GDBus.DocString annotation, note that parser used by <code>gdbus-codegen</code> parses XML comments in a way similar to m[blue]<code>gtk-doc</code>m[]<font SIZE="-2">[6]</font>: </p>
<p> Note that @since can be used in any inline documentation bit (e.g. for interfaces, methods, signals and properties) to set the org.gtk.GDBus.Since annotation. For the org.gtk.GDBus.DocString annotation (and inline comments), note that substrings of the form #net.Corp.Bar, net.Corp.Bar.FooMethod(), #net.Corp.Bar::BarSignal and #net.Corp.InlineDocs:BazProperty are all expanded to links to the respective interface, method, signal and property. Additionally, substrings starting with @ and % characters are rendered as m[blue]<code>parameter</code>m[]<font SIZE="-2">[7]</font> and m[blue]<code>constant</code>m[]<font SIZE="-2">[8]</font> respectively. </p>
<p> If both XML comments and org.gtk.GDBus.DocString or org.gtk.GDBus.DocString.Short annotations are present, the latter wins.</p>
<h2>EXAMPLE</h2>
<p> Consider the following D-Bus Introspection XML. </p>
<dl>
<dt>
<dd>
<pre>
&lt;node&gt;
  &lt;interface name=&quot;net.Corp.MyApp.Frobber&quot;&gt;
    &lt;method name=&quot;HelloWorld&quot;&gt;
      &lt;arg name=&quot;greeting&quot; direction=&quot;in&quot; type=&quot;s&quot;/&gt;
      &lt;arg name=&quot;response&quot; direction=&quot;out&quot; type=&quot;s&quot;/&gt;
    &lt;/method&gt;
    &lt;signal name=&quot;Notification&quot;&gt;
      &lt;arg name=&quot;icon_blob&quot; type=&quot;ay&quot;/&gt;
      &lt;arg name=&quot;height&quot; type=&quot;i&quot;/&gt;
      &lt;arg name=&quot;messages&quot; type=&quot;as&quot;/&gt;
    &lt;/signal&gt;
    &lt;property name=&quot;Verbose&quot; type=&quot;b&quot; access=&quot;readwrite&quot;/&gt;
  &lt;/interface&gt;
&lt;/node&gt;
</pre>
</dl>
<p> If <code>gdbus-codegen</code> is used on this file like this: </p>
<dl>
<dt>
<dd>
<pre>
gdbus-codegen --generate-c-code myapp-generated       \
              --c-namespace MyApp                     \
              --interface-prefix net.corp.MyApp.      \
              net.Corp.MyApp.Frobber.xml
</pre>
</dl>
<p> two files called myapp-generated.[ch] are generated. The files provide an abstract #GTypeInterface -derived type called <code>MyAppFrobber</code> as well as two instantiable types with the same name but suffixed with <code>Proxy</code> and <code>Skeleton</code>. The generated file, roughly, contains the following facilities: </p>
<dl>
<dt>
<dd>
/* GType macros for the three generated types */<br />
#define MY_APP_TYPE_FROBBER (my_app_frobber_get_type())<br />
#define MY_APP_TYPE_FROBBER_SKELETON (my_app_frobber_skeleton_get_type())<br />
#define MY_APP_TYPE_FROBBER_PROXY (my_app_frobber_proxy_get_type())<br />
typedef struct _MyAppFrobber MyAppFrobber; /* Dummy typedef */<br />
typedef struct<br />
{<br />
    GTypeInterface parent_iface;<br />
    /* Signal handler for the ::notification signal */<br />
    void (*notification)(MyAppFrobber *proxy,<br />
                         GVariant *icon_blob,<br />
                         gint height,<br />
                         const gchar *const *messages);<br />
    /* Signal handler for the ::handle-hello-world signal */<br />
    gboolean (*handle_hello_world)(MyAppFrobber *proxy,<br />
                                   GDBusMethodInvocation *invocation,<br />
                                   const gchar *greeting);<br />
} MyAppFrobberIface;<br />
/* Asynchronously calls HelloWorld() */<br />
void my_app_frobber_call_hello_world(MyAppFrobber *proxy,<br />
                                     const gchar *greeting,<br />
                                     GCancellable *cancellable,<br />
                                     GAsyncReadyCallback callback,<br />
                                     gpointer user_data);<br />
gboolean<br />
my_app_frobber_call_hello_world_finish(MyAppFrobber *proxy,<br />
                                       gchar **out_response,<br />
                                       GAsyncResult *res,<br />
                                       GError **error);<br />
/* Synchronously calls HelloWorld(). Blocks calling thread. */<br />
gboolean<br />
my_app_frobber_call_hello_world_sync(MyAppFrobber *proxy,<br />
                                     const gchar *greeting,<br />
                                     gchar **out_response,<br />
                                     GCancellable *cancellable,<br />
                                     GError **error);<br />
/* Completes handling the HelloWorld() method call */<br />
void my_app_frobber_complete_hello_world(MyAppFrobber *object,<br />
                                         GDBusMethodInvocation *invocation,<br />
                                         const gchar *response);<br />
/* Emits the ::notification signal / Notification() D-Bus signal */<br />
void my_app_frobber_emit_notification(MyAppFrobber *object,<br />
                                      GVariant *icon_blob,<br />
                                      gint height,<br />
                                      const gchar *const *messages);<br />
/* Gets the :verbose GObject property / Verbose D-Bus property.<br />
 * Does no blocking I/O.<br />
 */<br />
gboolean my_app_frobber_get_verbose(MyAppFrobber *object);<br />
/* Sets the :verbose GObject property / Verbose D-Bus property.<br />
 * Does no blocking I/O.<br />
 */<br />
void my_app_frobber_set_verbose(MyAppFrobber *object,<br />
                                gboolean value);<br />
/* Gets the interface info */<br />
GDBusInterfaceInfo *my_app_frobber_interface_info(void);<br />
/* Creates a new skeleton object, ready to be exported */<br />
MyAppFrobber *my_app_frobber_skeleton_new(void);<br />
/* Client-side proxy constructors.<br />
 *<br />
 * Additionally, _new_for_bus(), _new_for_bus_finish() and<br />
 * _new_for_bus_sync() proxy constructors are also generated.<br />
 */<br />
void my_app_frobber_proxy_new(GDBusConnection *connection,<br />
                              GDBusProxyFlags flags,<br />
                              const gchar *name,<br />
                              const gchar *object_path,<br />
                              GCancellable *cancellable,<br />
                              GAsyncReadyCallback callback,<br />
                              gpointer user_data);<br />
MyAppFrobber *<br />
my_app_frobber_proxy_new_finish(GAsyncResult *res,<br />
                                GError **error);<br />
MyAppFrobber *<br />
my_app_frobber_proxy_new_sync(GDBusConnection *connection,<br />
                              GDBusProxyFlags flags,<br />
                              const gchar *name,<br />
                              const gchar *object_path,<br />
                              GCancellable *cancellable,<br />
                              GError **error);
</dl>
<p> Thus, for every D-Bus method, there will be three C functions for calling the method, one #GObject signal for handling an incoming call and one C function for completing an incoming call. For every D-Bus signal, there&#8217;s one #GObject signal and one C function for emitting it. For every D-Bus property, two C functions are generated (one setter, one getter) and one #GObject property. The following table summarizes the generated facilities and where they are applicable: </p>
<table BORDER>
<tr VALIGN=top>
<td><code> &nbsp; </code></td>
<td><code> Client </code></td>
<td><code> Server </code>
</td>
</tr>
<tr VALIGN=top>
<td> Types </td>
<td> Use <code>MyAppFrobberProxy</code> </td>
<td> Any type implementing the <code>MyAppFrobber</code> interface
</td>
</tr>
<tr VALIGN=top>
<td> Methods </td>
<td> Use <code>m_a_f_hello_world()</code> to call. </td>
<td> Receive via the <code>handle_hello_world()</code> signal handler. Complete the call with <code>m_a_f_complete_hello_world()</code>
</td>
</tr>
<tr VALIGN=top>
<td> Signals </td>
<td> Connect to the <code>::notification</code> GObject signal. </td>
<td> Use <code>m_a_f_emit_notification()</code> to emit signal.
</td>
</tr>
<tr VALIGN=top>
<td> Properties (Reading) </td>
<td> Use <code>m_a_f_get_verbose()</code> or <i>:verbose</i>. </td>
<td> Implement #GObject&#8217;s <code>get_property()</code> vfunc.
</td>
</tr>
<tr VALIGN=top>
<td> Properties (writing) </td>
<td> Use <code>m_a_f_set_verbose()</code> or <i>:verbose</i>. </td>
<td> Implement #GObject&#8217;s <code>set_property()</code> vfunc.
</td>
</tr>
</table>
<h3>Client-side usage</h3>
<p> You can use the generated proxy type with the generated constructors: </p>
<dl>
<dt>
<dd>
MyAppFrobber *proxy;<br />
GError *error;<br />
error = NULL;<br />
proxy = my_app_frobber_proxy_new_for_bus_sync(<br />
    G_BUS_TYPE_SESSION,<br />
    G_DBUS_PROXY_FLAGS_NONE,<br />
    &#8220;net.Corp.MyApp&#8221;,              /* bus name */<br />
    &#8220;/net/Corp/MyApp/SomeFrobber&#8221;, /* object */<br />
    NULL,                          /* GCancellable* */<br />
    &amp;error);<br />
/* do stuff with proxy */<br />
g_object_unref(proxy);
</dl>
<p> Instead of using the generic #GDBusProxy facilities, one can use the generated methods such as <code>my_app_frobber_call_hello_world()</code> to invoke the <code>net.Corp.MyApp.Frobber.HelloWorld()</code> D-Bus method, connect to the <code>::notification</code> GObject signal to receive the <code>net.Corp.MyApp.Frobber::Notication</code> D-Bus signal and get/set the <i>net.Corp.MyApp.Frobber:Verbose</i> D-Bus Property using either the GObject property <i>:verbose</i> or the <code>my_app_get_verbose()</code> and <code>my_app_set_verbose()</code> methods. Use the standard #GObject::notify signal to listen to property changes. </p>
<p> Note that all property access is via #GDBusProxy &#8216;s property cache so no I/O is ever done when reading properties. Also note that setting a property will cause the m[blue]<code>org.freedesktop.DBus.Properties.Set</code>m[]<font SIZE="-2">[9]</font> method to be called on the remote object. This call, however, is asynchronous so setting a property won&#8217;t block. Further, the change is delayed and no error checking is possible.</p>
<h3>Server-side usage</h3>
<p> The generated <code>MyAppFrobber</code> interface is designed so it is easy to implement it in a #GObject subclass. For example, to handle <code>HelloWorld()</code> method invocations, set the vfunc for <code>handle_hello_hello_world()</code> in the <code>MyAppFrobberIface</code> structure. Similarly, to handle the <i>net.Corp.MyApp.Frobber:Verbose</i> property override the <i>:verbose</i> #GObject property from the subclass. To emit a signal, use e.g. <code>my_app_emit_signal()</code> or g_signal_emit_by_name(). </p>
<p> Instead of subclassing, it is often easier to use the generated <code>MyAppFrobberSkeleton</code> subclass. To handle incoming method calls, use <code>g_signal_connect()</code> with the <code>::handle-*</code> signals and instead of overriding #GObject &#8216;s <code>get_property()</code> and <code>set_property()</code> vfuncs, use g_object_get() and g_object_set() or the generated property getters and setters (the generated class has an internal property bag implementation). </p>
<dl>
<dt>
<dd>
<pre><code>
static gboolean
on_handle_hello_world(MyAppFrobber *interface,
                      GDBusMethodInvocation *invocation,
                      const gchar *greeting,
                      gpointer user_data)
{
    if (g_strcmp0(greeting, "Boo") != 0) {
        gchar *response;
        response = g_strdup_printf("Word! You said `%s'.", greeting);
        my_app_complete_hello_world(interface, invocation, response);
        g_free(response);
    } else {
        g_dbus_method_invocation_return_error(invocation,
                                              MY_APP_ERROR,
                                              MY_APP_ERROR_NO_WHINING,
                                              "Hey, %s, there will be no whining!",
                                              g_dbus_method_invocation_get_sender(invocation));
    }
    return TRUE;
}
[...] interface = my_app_frobber_skeleton_new();
my_app_frobber_set_verbose(interface, TRUE);
g_signal_connect(interface,
                 "handle-hello-world",
                 G_CALLBACK(on_handle_hello_world),
                 some_user_data);
[...] error = NULL;
if (!g_dbus_interface_skeleton_export(G_DBUS_INTERFACE_SKELETON(interface),
                                      connection,
                                      "/path/of/dbus_object",
                                      &amp;error)) {
    /* handle error */
}
</code></pre>
</dl>
<p> To facilitate atomic changesets (multiple properties changing at the same time), #GObject::notify signals are queued up when received. The queue is drained in an idle handler (which is called from the thread-default main loop of the thread where the skeleton object was constructed) and will cause emissions of the m[blue]<code>org.freedesktop.DBus.Properties::PropertiesChanged</code>m[]<font SIZE="-2">[9]</font> signal with all the properties that have changed. Use g_dbus_interface_skeleton_flush() or g_dbus_object_skeleton_flush() to empty the queue immediately. Use g_object_freeze_notify() and g_object_thaw_notify() for atomic changesets if on a different thread.</p>
<h2>C TYPE MAPPING</h2>
<p> Scalar types (type-strings &#8216;b&#8217;, &#8216;y&#8217;, &#8216;n&#8217;, &#8216;q&#8217;, &#8216;i&#8217;, &#8216;u&#8217;, &#8216;x&#8217;, &#8216;t&#8217; and &#8216;d&#8217;) ), strings (type-strings &#8216;s&#8217;, &#8216;ay&#8217;, &#8216;o&#8217; and &#8216;g&#8217;) and arrays of string (type-strings &#8216;as&#8217;, &#8216;ao&#8217; and &#8216;aay&#8217;) are mapped to the natural types, e.g. #gboolean, #gdouble, #gint, gchar*, gchar** and so on. Everything else is mapped to the #GVariant type. </p>
<p> This automatic mapping can be turned off by using the annotation org.gtk.GDBus.C.ForceGVariant &#8211; if used then a #GVariant is always exchanged instead of the corresponding native C type. This annotation may be convenient to use when using bytestrings (type-string &#8216;ay&#8217;) for data that could have embedded NUL bytes.</p>
<h2>STABILITY GUARANTEES</h2>
<p> The generated C functions are guaranteed to not change their ABI that is, if a method, signal or property does not change its signature in the introspection XML, the generated C functions will not change its C ABI either. The ABI of the generated instance and class structures will be preserved as well. </p>
<p> The ABI of the generated #GType s will be preserved only if the org.gtk.GDBus.Since annotation is used judiciously &#8212; this is because the VTable for the #GInterface relies on functions pointers for signal handlers. Specifically, if a D-Bus method, property or signal or is added to a D-Bus interface, then ABI of the generated #GInterface type is preserved if, and only if, each added method, property signal is annotated with they org.gtk.GDBus.Since annotation using a greater version number than previous versions. </p>
<p> The generated C code currently happens to be annotated with m[blue]<code>gtk-doc</code>m[]<font SIZE="-2">[6]</font> / m[blue]<code>GObject Introspection</code>m[]<font SIZE="-2">[10]</font> comments / annotations. The layout and contents might change in the future so no guarantees about e.g. SECTION usage etc. is given. </p>
<p> While the generated Docbook for D-Bus interfaces isn&#8217;t expected to change, no guarantees are given at this point. </p>
<p> It is important to note that the generated code should not be checked into revision control systems, nor it should be included in distributed source archives.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://gitlab.gnome.org/GNOME/glib/issues/new">https://gitlab.gnome.org/GNOME/glib/issues/new</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdbus/">gdbus</a></code>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> D-Bus Introspection XML</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://dbus.freedesktop.org/doc/dbus-specification.html#introspection-format">http://dbus.freedesktop.org/doc/dbus-specification.html#introspection-format</a></dl>
<dt> 2.</p>
<dd> RefEntry</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.docbook.org/tdg/en/html/refentry.html">http://www.docbook.org/tdg/en/html/refentry.html</a></dl>
<dt> 3.</p>
<dd> sortas attribute</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.docbook.org/tdg/en/html/primary.html">http://www.docbook.org/tdg/en/html/primary.html</a></dl>
<dt> 4.</p>
<dd> CamelCase</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://en.wikipedia.org/wiki/CamelCase">http://en.wikipedia.org/wiki/CamelCase</a></dl>
<dt> 5.</p>
<dd> #pragma once</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://en.wikipedia.org/wiki/Pragma_once">https://en.wikipedia.org/wiki/Pragma_once</a></dl>
<dt> 6.</p>
<dd> gtk-doc</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.gtk.org/gtk-doc/">http://www.gtk.org/gtk-doc/</a></dl>
<dt> 7.</p>
<dd> parameter</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.docbook.org/tdg/en/html/parameter.html">http://www.docbook.org/tdg/en/html/parameter.html</a></dl>
<dt> 8.</p>
<dd> constant</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.docbook.org/tdg/en/html/constant.html">http://www.docbook.org/tdg/en/html/constant.html</a></dl>
<dt> 9.</p>
<dd> org.freedesktop.DBus.Properties.Set</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://dbus.freedesktop.org/doc/dbus-specification.html#standard-interfaces-properties">http://dbus.freedesktop.org/doc/dbus-specification.html#standard-interfaces-properties</a></dl>
<dt>10.</p>
<dd> GObject Introspection</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://wiki.gnome.org/Projects/GObjectIntrospection">https://wiki.gnome.org/Projects/GObjectIntrospection</a></dl>
</dl>
<h2>Index</h2>
