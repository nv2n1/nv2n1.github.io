---

title: "monop(1)"
name: "monop"
section: "1"
letter: "m"
url: "/docs/linux/man/1-monop/"
description: "monop, monop2 – Mono Class Outline Viewer"
---

<h2>NAME</h2>
<p> monop, monop2 &#8211; Mono Class Outline Viewer</p>
<p> <code>monop</code> [-r:assembly] [&#8211;search] class</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-r:assembly</i></dt>
<dd> Specifies the assembly to use for looking up the type</dd>
<dt><i>-a</i></dt>
<dd> Renders all of the types in the specified assembly.</dd>
<dt><i>&#8211;search, -s, -k</i></dt>
<dd> Searches through all known assemblies for types containing `class&#8217;.</dd>
<dt><i>&#8211;refs</i></dt>
<dd> Prints a list of the referenced assemblies for an assembly. Requires an assembly to be specified with -r:assembly.</dd>
<dt><i>&#8211;filter-obsolete, -f</i></dt>
<dd> Do not show obsolete types and members.</dd>
<dt><i>&#8211;declared-only, -d</i></dt>
<dd> Only show members declared in the type.</dd>
<dt><i>&#8211;private, -p</i></dt>
<dd> Show private members.</dd>
<dt><i>&#8211;runtime-version</i></dt>
<dd> Print runtime version.</dd>
<dt><i>-xa</i></dt>
<dd> Sets the lookup path to the Xamarin.Android directory. This will load both the mscorlib from there, and search assemblies in that directory.</dd>
<dt><i>-xi</i></dt>
<dd> Sets the lookup path to the Xamarin.iOS directory. This will load both the mscorlib from there, and search assemblies in that directory.</dd></dl>
<p> Monop is a tool that allows you to view the outline of a class. You can see the signature of each member of the class. Use <i>monop</i> to explore 1.0 assemblies, use <i>monop2</i> to explore 2.0 assemblies. </p>
<p> The tool takes one option, the class to view. You must specify the full name of the class, including namespace. </p>
<p> For generic classes, you must specify the generic arguments, for example: </p>
<pre>
monop2 'System.Collections.Generic.List`1'
</pre>
<p> The above is the string representation for the List&lt;T&gt; in System.Collections.Generic </p>
<p> If you are unsure of the full name of the class, you can use the `&#8211;search&#8217; option to search through all known assemblies. </p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
