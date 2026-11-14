---
title: "xbuild(1)"
name: "xbuild"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xbuild/"
description: "xbuild – Mono’s tool to build MSBuild project files"
---

<h2>NAME</h2>
<p> xbuild &#8211; Mono&#8217;s tool to build MSBuild project files</p>
<h2>SYNOPSIS</h2>
<p> <code>xbuild</code> [option] [project-file]</p>
<h2>DESCRIPTION</h2>
<p> xbuild can be used to build MSBuild project files. Integrated Development Environments like MonoDevelop and &quot;Microsoft Visual Studio .NET&quot; use msbuild project file format. </p>
<p> xbuild takes the path of the project or solution file to build, as the main argument. If no file is specified then it tries to build any solution file or project file in the current directory, that has a *proj extension.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>//target:T1[,TN]</code></p>
<dd> List of targets to build</p>
<dt><code>//property:Name=Value</code></p>
<dd> Set or override project properties</p>
<dt><code>//logger:&lt;logger&gt;</code></p>
<dd> Custom logger to log build events</p>
<dt><code>//toolsversion:version , /tv:version</code></p>
<dd> Specify the toolset version to use. </p>
<p> Eg. /tv:4.0<br />
&nbsp;<wbr>This would cause 4.0 version of the Microsoft.Common.targets&nbsp;<wbr>(among others)&nbsp;<wbr>to be used. This overrides<br />
&nbsp;<wbr>the value specified in a project file. </p>
<p> Valid values: 2.0, 3.0, 3.5 and 4.0</p>
<dt><code>//verbosity:&lt;level&gt;</code></p>
<dd> Logger verbosity level : quiet, minimal, normal, detailed, diagnostic</p>
<dt><code>//validate</code></p>
<dd> Validate the project file against the schema</p>
<dt><code>//validate:&lt;schema&gt;</code></p>
<dd> Validate the project file against the specified schema</p>
<dt><code>//consoleloggerparameters:&lt;params&gt; , /clp:&lt;params&gt;</code></p>
<dd> Parameters for the console logger : PerfomanceSummary, Summary, NoSummary, NoItemAndPropertyList, Verbosity</p>
<dt><code>//filelogger[n] , /fl[n]</code></p>
<dd> Logs the output to a file, named &#8216;msbuild.log&#8217; by default. If the optional number &#8216;n&#8217; is specified, then it logs to &#8216;msbuild[n].log&#8217; . Parameters for this logger, including the log file name can be specified via a corresponding /flp[n] option. Default verbosity for file loggers is &#8216;detailed. &#8216;n&#8217; can be between 1-9.</p>
<dt><code>//fileloggerparameters[n]:&lt;params&gt; , /flp[n]:&lt;params&gt;</code></p>
<dd> Parameters for a file logger. This implies a corresponding /fl[n]. &#8216;n&#8217; can be between 1-9, and is used to add upto 10 file loggers. Parameters can be, besides the ones available for console logger:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>LogFile=&lt;file&gt;</i></p>
<dd> File to which the build log will be written.</p>
<dt><i>Append</i></p>
<dd> If this is used, then the log file is appended to, else a new one will be created.</p>
<dt><i>Encoding=&lt;encoding&gt;</i></p>
<dd> Encoding to use for the log file, eg. UTF-8, ASCII.</p>
<dt>Eg: xbuild foo.csproj /flp:Verbosity=normal &quot;/flp1:LogFile=build.log;Append;Encoding=ASCII&quot;</p>
<dd></dl>
</dl>
<dt><code>//nologo</code></p>
<dd> Don&#8217;t show the initial xbuild banner</p>
<dt><code>//help</code></p>
<dd> Show xbuild usage</p>
<dt><code>//version</code></p>
<dd> Display xbuild version</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>XBUILD_EMIT_SOLUTION</i></p>
<dd> If this variable is set, then the project file generated from a solution file is emitted.</p>
<dt><i>XBUILD_LOG_REFERENCE_RESOLVER</i></p>
<dd> References are resolved by trying a list of assembly search paths ($(AssemblySearchPaths)). If xbuild is unable to resolve a reference, then it logs details of why the various search paths failed. If this variable is set, then it logs the same even for references that were resolved successfully. These logs show up if the verbosity is set to detailed or higher.</p>
<dt><i>MSBuildExtensionsPath</i></p>
<dd> MSBuild extensions are usually installed in $(MSBuildExtensionsPath), which xbuild resolves to $prefix/lib/mono/xbuild . When used in Import, like: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;Import Project=&quot;$(MSBuildExtensionsPath)\TestTargets.targets&quot;/&gt; </p>
<p> xbuild tries various values for the msbuild property $(MSBuildExtensionsPath), in order: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1. Paths specified in the environment variable&nbsp;<wbr>$MSBuildExtensionsPath.<br />
&nbsp;<wbr>&nbsp;<wbr>2.&nbsp;<wbr>/Library/Frameworks/Mono.framework/External/xbuild on Mac OSX.<br />
&nbsp;<wbr>&nbsp;<wbr>3.&nbsp;<wbr>$XDG_CONFIG_HOME/xbuild/tasks&nbsp;<wbr>(or Environment.SpecialFolder.ApplicationData)<br />
&nbsp;<wbr>&nbsp;<wbr>4.&nbsp;<wbr>$prefix/lib/mono/xbuild&nbsp;<wbr>(default location) </p>
<p> Anywhere else in the project files, $(MSBuildExtensionsPath) will always resolve to the default location. This is a xbuild-only feature. This is also applicable for the properties $(MSBuildExtensionsPath32) and $(MSBuildExtensionsPath64), and the environment variables have the corresponding names &#8211; MSBuildExtensionsPath32/64 .</p>
<dt><i>XBUILD_FRAMEWORK_FOLDERS_PATH</i></p>
<dd> With ToolsVersion 4.0, projects can target arbitrary frameworks referenced by TargetFrameworkMoniker, which is of the format: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Identifier,Version=&lt;version&gt;[,Profile=&lt;profile&gt;] </p>
<p> Eg. &quot;.NETFramework,Version=v4.0&quot; </p>
<p> The 3 parts of the moniker are given by the msbuild properties: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$(TargetFrameworkIdentifier),&nbsp;<wbr>$(TargetFrameworkVersion)&nbsp;<wbr>and&nbsp;<wbr>$(TargetFrameworkProfile) </p>
<p> This moniker maps to a framework description file on disk: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;framework_root&gt;/Identifier/Version/[Profile]/RedistList/FrameworkList.xml </p>
<p> This file is used to determine the path where to find the framework assemblies for this particular framework. </p>
<p> Framework root here is configurable and is resolved in the following order: </p>
<pre>
  1. Paths specified in the environment variable $XBUILD_FRAMEWORK_FOLDERS_PATH
  2. /Library/Frameworks/Mono.framework/External/xbuild-frameworks on Mac OSX.
  3. MSBuild property $(TargetFrameworkRoot)
  4. $prefix/lib/mono/xbuild-frameworks (default location)
</pre>
<p> XBuild tries the paths given above, in order, till it finds a FrameworkList.xml for the moniker. Running with /v:detailed or higher verbosity will show the various paths that it tries. </p>
<p> The FrameworkList.xml itself just has a root element like: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;FileList&nbsp;<wbr>&nbsp;<wbr>Name=&quot;.NET Framework 3.5&quot;&nbsp;<wbr>TargetFrameworkDirectory=&quot;..\..\..\..\3.5&quot;&nbsp;<wbr>IncludeFramework=&quot;v3.0&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/FileList&gt; </p>
<p> Here the TargetFrameworkDirectory attribute specifies the directory where the assemblies for this particular framework can be found. If this is not set, then the parent of the folder containing the xml file is taken as the framework directory. </p>
<p> IncludeFramework attribute specifies the version of a framework (under the *same* $(TargetFrameworkIdentifier)) which should be included in the final list of Target framework directories. </p>
<dt><i>XBUILD_COLORS</i></p>
<dd> If this variable is set, it contains a string of the form &quot;type=foreground,type=..&quot; that specifies which color to use to display errors/warnings etc on some terminals. Type here can be: </p>
<pre>
        errors, warnings, messages or events
        events: These are project/target/task start and end event
                messages.
</pre>
<p> The possible colors for foreground are: <code>black, red, brightred, green, brightgreen, yellow, brightyellow,</code> blue, brightblue, magenta, brightmagenta, cyan, brightcyan, grey, white and brightwhite. </p>
<p> For example, you could set this variable from your shell: </p>
<pre>
        export XBUILD_COLORS
        XBUILD_COLORS=errors=brightred,warnings=blue
</pre>
<p> You can disable the built-in color scheme by setting this variable to &quot;disable&quot;. </p>
</dl>
<h2>NOTES</h2>
<p> On Mac OSX, for locating pkg-config (.pc) files, xbuild additionally looks in &quot;/Library/Frameworks/Mono.framework/External/pkgconfig&quot; . </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a>(1),</code><a href="/docs/linux/man/1-mcs/">mcs</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011 Novell, Inc (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a></p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit: <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
