---
title: "monolinker(1)"
name: "monolinker"
section: "1"
letter: "m"
url: "/docs/linux/man/1-monolinker/"
description: "Mono CIL Linker"
---

<h2>NAME</h2>
<p> Mono CIL Linker</p>
<h2>SYNOPSIS</h2>
<p> <code>monolinker [-o output_directory][-l i18n_assemblies][-c skip | copy | link] -x descriptor | -a assembly | -i info_file &#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <i>monolinker</i> is a CIL Linker. </p>
<p> The linker is a tool one can use to only ship the minimal possible set of functions that a set of programs might require to run as opposed to the full libraries. </p>
<p> The linker analyses the intermediate code (CIL) produced by every compiler targeting the Mono platform like mcs, gmcs, vbnc, booc or others. It will walk through all the code that it is given to it, and remove all the unused methods and classes. This is done using a mark and sweep operation on all the code that it is referenced. </p>
<p> The generated output from the monolinker can be later processed by the <i>mkbundle</i> tool to generate small native self-contained executables. </p>
<p> Do not confuse this with the Assembly Linker (al) which creates assemblies from manifests, modules and resource files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-d search_directory</i></p>
<dd> Specify a directory to the linker where to look for assemblies.</p>
<dt><i>-o output_directory</i></p>
<dd> Specify the output directory, default is &#8216;output&#8217;. </p>
<p> If you specify the directory `.&#8217;, please ensure that you won&#8217;t write over important assemblies of yours.</p>
<dt><i>-b true | false</i></p>
<dd> Specify whether to generate debug symbols or not, default is false.</p>
<dt><i>-g true | false</i></p>
<dd> Specify whether to generate a new guid for each linked module or reuse the existing one, default is true.</p>
<dt><i>-l i18n_assemblies</i></p>
<dd> Specify what to do with the region specific assemblies </p>
<p> Mono have a few assemblies which contains everything region specific: </p>
<pre>
        I18N.CJK.dll
        I18N.MidEast.dll
        I18N.Other.dll
        I18N.Rare.dll
        I18N.West.dll
</pre>
<p> By default, they will all be copied to the output directory, but you can specify which one you want using this command. The choice can either be: none, all, cjk, mideast, other, rare or west. You can combine the values with a comma.</p>
<dt><i>-c action</i></p>
<dd> Specify the action to apply to the core assemblies. </p>
<p> Core assemblies are the assemblies that belongs to the base class library, like mscorlib.dll, System.dll or System.Windows.Forms.dll. </p>
<p> The linker supports three operations on these assemblies, you can specify one of the following actions:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>skip</i></p>
<dd> This instructs the linker to skip them and do nothing with them.</p>
<dt><i>copy</i></p>
<dd> This instructs the linker to copy them to the output directory,</p>
<dt><i>link</i></p>
<dd> This instructs the linker to apply the linking process and reduce their size.</dl>
</dl>
<dt><i>-p action assembly</i></p>
<dd> Specify per assembly which action to apply.</p>
<dt><i>-x descriptor</i></p>
<dd> Use an XML descriptor as a source for the linker. </p>
<p> Here is an example that shows all the possibilities of this format: </p>
<pre>
&lt;linker&gt;
        &lt;assembly fullname=&quot;Library&quot;&gt;
                &lt;type fullname=&quot;Foo&quot; /&gt;
                &lt;type fullname=&quot;Bar&quot; preserve=&quot;nothing&quot; required=&quot;false&quot; /&gt;
                &lt;type fullname=&quot;Baz&quot; preserve=&quot;fields&quot; required=&quot;false&quot; /&gt;
                &lt;type fullname=&quot;Gazonk&quot;&gt;
                        &lt;method signature=&quot;System.Void .ctor(System.String)&quot; /&gt;
                        &lt;field signature=&quot;System.String _blah&quot; /&gt;
                        &lt;field name=&quot;someFieldName&quot; /&gt;
                &lt;/type&gt;
        &lt;/assembly&gt;
&lt;/linker&gt;
</pre>
<p> In this example, the linker will link the types Foo, Bar, Baz and Gazonk. </p>
<p> The preserve attribute ensures that all the fields of the type Baz will be always be linked, not matter if they are used or not, but that neither the fields or the methods of Bar will be linked if they are not used. Not specifying a preserve attribute implies that we are preserving everything in the specified type. </p>
<p> The required attribute specifies that if the type is not marked, during the mark operation, it will not be linked. </p>
<p> The type Gazonk will be linked, as well as its constructor taking a string as a parameter, and it&#8217;s _blah field. </p>
<p> You can have multiple assembly nodes.</p>
<dt><i>-a assemblies</i></p>
<dd> use an assembly as a source for the linker. </p>
<p> The linker will walk through all the methods of the assembly to generate only what is necessary for this assembly to run.</p>
<dt><i>-i info_file</i></p>
<dd> use a .info xml file as a source for the linker. </p>
<p> An info file is a file produced by the tool mono-api-info. The linker will use it to generate an assembly that contains only what the public API defined in the info file needs.</p>
<dt><i>-s [StepBefore:]StepFullName,StepAssembly[:StepAfter]</i></p>
<dd>
<p> You can ask the linker to execute custom steps by using the -s command. This command takes the standard TypeFullName,Assembly format to locate the step. You can customize its position in the pipeline by either adding it before a step, or after. </p>
<p> Example: </p>
<pre><code>
using System;
using Mono.Linker;
using Mono.Linker.Steps;
namespace Foo
{
public
class FooStep : IStep
{
  public
    void Process(LinkContext context)
    {
        foreach (IStep step in context.Pipeline.GetSteps()) {
            Console.WriteLine(step.GetType().Name);
        }
    }
}
} // namespace Foo
</code></pre>
<p> If you compile this custom against monolinker to a Foo.dll assembly, you can use the <i>-s</i> switch as follows. To add the FooStep at the end of the pipeline: </p>
<pre>
        monolinker -s Foo.FooStep,Foo -a program.exe
</pre>
<p> This commanand will add the FooStep after the MarkStep: </p>
<pre>
        monolinker -s MarkStep:Foo.FooStep,Foo -a program.exe
</pre>
<p> This command will add the FooStep before the MarkStep: </p>
<pre>
        monolinker -s Foo.FooStep,Foo:MarkStep -a program.exe
</pre>
<p> This command will add the FooStep before the MarkStep</p>
<dt><i>-m CustomParam ParamValue</i></p>
<dd> Specify a parameter for a custom step.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007 Novell, Inc (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a></p>
<h2>BUGS</h2>
<p> Bugs report are welcome at <a rel="nofollow" href="http://bugzilla.xamarin.com">http://bugzilla.xamarin.com</a> </p>
<p> Product Mono Tools, Component linker.</p>
<h2>MAILING LISTS</h2>
<p> Mailing lists are listed at <a rel="nofollow" href="http://www.mono-project.com/community/help/mailing-lists/">http://www.mono-project.com/community/help/mailing-lists/</a></p>
<h2>WEB SITE</h2>
<p> <a rel="nofollow" href="http://www.mono-project.com/docs/tools+libraries/tools/linker/">http://www.mono-project.com/docs/tools+libraries/tools/linker/</a></p>
<h2>AUTHORS</h2>
<p> The linker has been written by Jb Evain, and have been partially founded by the Google Summer of Code.</p>
<h2>LICENSE</h2>
<p> The linker is licensed under the MIT/X11 license. Please read the accompayning MIT.X11 file for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-al/">al</a>(1),<a href="/docs/linux/man/1-mkbundle/">mkbundle</a>(1),<a href="/docs/linux/man/1-mono/">mono</a>(1),<a href="/docs/linux/man/1-mcs/">mcs</a>(1).</code> </p>
<h2>Index</h2>
