---
title: "mdoc-update(1)"
name: "mdoc-update"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdoc-update/"
description: "mdoc update – mdoc(5) documentation format support"
---

<h2>NAME</h2>
<p> mdoc update &#8211; <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) documentation format support</p>
<h2>SYNOPSIS</h2>
<p> <code>mdoc update</code> [OPTIONS]* ASSEMBLIES</p>
<h2>DESCRIPTION</h2>
<p> <code>mdoc update</code> is responsible for the following:</p>
<dl>
<dt><code>*</code></p>
<dd> Creating documentation stubs based on <i>ASSEMBLIES</i>. The stub-creation process will create new <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) XML files for each type within <i>ASSEMBLIES</i>, and provide documentation stubs for each member of those types.</p>
<dt><code>*</code></p>
<dd> Update documentation stubs based on <i>ASSEMBLIES</i>. Existing <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) documentation can be updated to reflect changes within <i>ASSEMBLIES</i>, such as added types and members, while preserving existing documentation. </p>
<p> In some limited circumstances, renames will be tracked, minimizing the documentation burden when e.g. a parameter is renamed.</dl>
<p> <code>mdoc update</code> does not rely on documentation found within source code, though it can import XML Documentation Comments via the <code>-i</code> option. </p>
<p> See <code><a href="/docs/linux/man/1-mdoc/">mdoc</a></code>(1) and <code><a href="/docs/linux/man/5-mdoc/">mdoc</a></code>(5) for more information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;delete</code></p>
<dd> Allow <code>mdoc update</code> to delete members from documentation files. The only members deleted are members which are no longer present within <i>ASSEMBLIES</i> and are not present in any other assembly versions. </p>
<p> If a type is no longer present, the documentation file is <i>not</i> deleted, but is instead <i>renamed</i> to have a <code>.remove </code> extension. </p>
<p> Version detection is done with the <i>//AssemblyVersion</i> elements; if there are no <i>//AssemblyVersion</i> elements for a given <i>&lt;Type&gt;</i> or <i>&lt;Member/&gt;</i>, then the <i>&lt;Type&gt;</i> will be renamed and/or the <i>&lt;Member/&gt;</i> will be removed.</p>
<dt><code>&#8211;exceptions</code>[=<i>SOURCES</i>]</p>
<dd> EXPERIMENTAL. This is not 100% reliable, but is intended to serve as an aid for documentation writers. </p>
<p> Inspect member bodies to determine what exceptions can be generated from the member. </p>
<p> <i>SOURCES</i> is an optional comma-separated list of the following sources that should be searched for exceptions: </p>
<pre>
        added   Only generate &lt;exception/&gt; elements for members 
                  added during the current program execution.
                  This keeps mdoc-update from re-generating
                  &lt;exception/&gt; elements for all members (and thus
                  prevents re-insertion for members that had the
                  &lt;exception/&gt; elements removed).
        all     Find exceptions created in the member itself, 
                  references to members in the same assembly, 
                  and references to members in dependent 
                  assemblies.
        asm     Find exceptions created in the member itself and
                  references to members within the same assembly
                  as the member.
        depasm  Find exceptions created in the member itself and
                  references to members within dependent 
                  assemblies.
</pre>
<p> If <i>SOURCES</i> isn&#8217;t provided (the default), then only exceptions created within the member itself will be documented. </p>
<p> LIMITATIONS: Exception searching is currently implemented by looking for the exception types that are explicitly created based on the known compile-time types. This has the following limitations:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>*</code></p>
<dd> This will not find exceptions which are implicit to the IL, such as NullReferenceException and IndexOutOfRangeException.</p>
<dt><code>*</code></p>
<dd> This will find exceptions which are <i>not</i> thrown, e.g. </p>
<pre><code>
public
void CreateAnException()
{
    Exception e = new Exception();
}
</code></pre>
<dt><code>*</code></p>
<dd> This will not &quot;follow&quot; delegate and interface calls:<br />
public<br />
void UsesDelegates()<br />
{<br />
    Func&lt;int, int&gt; a = x = &gt;<br />
    {<br />
        throw new Exception();<br />
    };<br />
    a(4);<br />
}<br />
 The function <i>UsesDelegates()</i> won&#8217;t have any exceptions documented.</p>
<dt><code>*</code></p>
<dd> This will find exceptions which &quot;cannot happen&quot;, such as ArgumentNullExceptions for arguments which are &quot;known&quot; to be non-null: </p>
<pre><code>
public
void A()
{
    B("this parameter isn't null");
}
public
void B(string s)
{
    if (s == null)
        throw new ArgumentNullException("s");
}
</code></pre>
<p> For the above, if <code>&#8211;exceptions=asm</code> is provided then <i>A()</i> will be documented as throwing an ArgumentNullException, which cannot happen.</dl>
</dl>
<dt><code>-f</code>=<i>FLAG</i></p>
<dd> Specify a flag to alter behavior. Valid flags include:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>no-assembly-versions</code></p>
<dd> See the <code>-fno-assembly-versions</code> documentation, below.</dl>
</dl>
<dt><code>-fno-assembly-versions</code></p>
<dd> Do not generate <i>/Type/AssemblyInfo/AssemblyVersion</i> and <i>/Type/Members/Member/AssemblyInfo</i> elements. </p>
<p> This is useful to prevent &quot;churn&quot; during updates. Normally, if a type or member hasn&#8217;t changed but the assembly version has changed, then all types and members will be updated to include a new <i>//AssemblyVersion</i> element, thus increasing the amount of changes that need review before committing (assuming all changes are actually reviewed before commit). </p>
<p> WARNING: This <i>will</i> interact badly with the <code>&#8211;delete</code> option, as <code>&#8211;delete</code> uses the <i>//AssemblyVersion</i> elements to track version changes. Thus, if you have a member which is present in an early assembly version and is removed in a subsequent assembly version, such as <i>System.Text.UTF8Encoding.GetBytes(string)</i> (which is present in .NET 1.0 but not in .NET 2.0), then the member will be removed when the <code>&#8211;delete -fno-assembly-versions</code> options are specified, the member was present in an earlier version of the assembly, and the current version of the assembly does not contain the member. </p>
<p> Consequently, this option should <i>only</i> be specified if types and members will <i>never</i> be removed from an assembly.</p>
<dt><code>-i</code>, <code>&#8211;import</code>=<i>FILE</i></p>
<dd> Import documentation found within <i>FILE</i>. </p>
<p> <i>FILE</i> may contain either <i>csc /doc</i> XML or <i>ECMA-335</i> XML.</p>
<dt><code>-L</code>, <code>&#8211;lib</code>=<i>DIRECTORY</i></p>
<dd> Add <i>DIRECTORY</i> to the assembly search path, so that dependencies of <i>ASSEMBLIES</i> can be found without documenting those assemblies.</p>
<dt><code>-o</code>, <code>&#8211;out</code>=<i>DIRECTORY</i></p>
<dd> Place the generated stubs into <i>DIRECTORY</i>. </p>
<p> When updating documentation, <i>DIRECTORY</i> is also the source directory.</p>
<dt><code>-r</code>=<i>ASSEMBLY</i></p>
<dd> <i>ASSEMBLY</i> is a dependency for one of <i>ASSEMBLIES</i> which should <i>not</i> be documented but is required to process one of <i>ASSEMBLIES</i>. Add the directory containing <i>ASSEMBLY</i> to the assembly search path. </p>
<p> This option is equivalent to specifying <code>-L</code> `<i>dirname</i> ASSEMBLY`.</p>
<dt><code>&#8211;since</code>=<i>VERSION</i></p>
<dd> When <i>updating</i> documentation for an assembly, if a type or member is encountered which didn&#8217;t exist in the previous version of the assembly a <code>&lt;since version=&quot;</code><i>VERSION</i><code>&quot;/&gt;</code> element will be inserted.</p>
<dt><code>&#8211;type</code>=<i>TYPE</i></p>
<dd> Only update documentation for the type <i>TYPE</i>.</p>
<dt><code>-h, -?, &#8211;help</code></p>
<dd> Display a help message and exit.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mdoc/">mdoc</a>(1), <a href="/docs/linux/man/5-mdoc/">mdoc</a>(5), <a href="/docs/linux/man/1-mdoc-assemble/">mdoc-assemble</a>(1), <a href="/docs/linux/man/1-mdoc-export-html/">mdoc-export-html</a>(1), <a href="/docs/linux/man/1-mdoc-validate/">mdoc-validate</a>(1),</p>
<h2>MAILING LISTS</h2>
<dl>
<dt>Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-docs-list">http://lists.ximian.com/mailman/listinfo/mono-docs-list</a> for details.</p>
<dd></dl>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
