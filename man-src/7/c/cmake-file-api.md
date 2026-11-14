---
title: "cmake-file-api(7)"
name: "cmake-file-api"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-file-api/"
description: "cmake-file-api – CMake File-Based API"
---

<p>cmake-file-api &#8211; CMake File-Based API</p>
<h2>Introduction</h2>
<p>CMake provides a file-based API that clients may use to get semantic information about the buildsystems CMake generates. Clients may use the API by writing query files to a specific location in a build tree to request zero or more <i>Object Kinds</i>. When CMake generates the buildsystem in that build tree it will read the query files and write reply files for the client to read. </p>
<p> The file-based API uses a <code>&lt;build&gt;/.cmake/api/</code> directory at the top of a build tree. The API is versioned to support changes to the layout of files within the API directory. API file layout versioning is orthogonal to the versioning of <i>Object Kinds</i> used in replies. This version of CMake supports only one API version, <i>API v1</i>.</p>
<h2>Api V1</h2>
<p>API v1 is housed in the <code>&lt;build&gt;/.cmake/api/v1/</code> directory. It has the following subdirectories:</p>
<dl>
<dt><code>query/</code></p>
<dd>Holds query files written by clients. These may be <i>v1 Shared Stateless Query Files</i>, <i>v1 Client Stateless Query Files</i>, or <i>v1 Client Stateful Query Files</i>.</p>
<dt><code>reply/</code></p>
<dd>Holds reply files written by CMake whenever it runs to generate a build system. These are indexed by a <i>v1 Reply Index File</i> file that may reference additional <i>v1 Reply Files</i>. CMake owns all reply files. Clients must never remove them. </p>
<p> Clients may look for and read a reply index file at any time. Clients may optionally create the <code>reply/</code> directory at any time and monitor it for the appearance of a new reply index file.</dl>
<h3>v1 Shared Stateless Query Files</h3>
<p>Shared stateless query files allow clients to share requests for major versions of the <i>Object Kinds</i> and get all requested versions recognized by the CMake that runs. </p>
<p> Clients may create shared requests by creating empty files in the <code>v1/query/</code> directory. The form is: </p>
<pre>&lt;build&gt;/.cmake/api/v1/query/&lt;kind&gt;-v&lt;major&gt;</pre>
<p>where <code>&lt;kind&gt;</code> is one of the <i>Object Kinds</i>, <code>-v</code> is literal, and <code>&lt;major&gt;</code> is the major version number. </p>
<p> Files of this form are stateless shared queries not owned by any specific client. Once created they should not be removed without external client coordination or human intervention.</p>
<h3>v1 Client Stateless Query Files</h3>
<p>Client stateless query files allow clients to create owned requests for major versions of the <i>Object Kinds</i> and get all requested versions recognized by the CMake that runs. </p>
<p> Clients may create owned requests by creating empty files in client-specific query subdirectories. The form is: </p>
<pre>&lt;build&gt;/.cmake/api/v1/query/client-&lt;client&gt;/&lt;kind&gt;-v&lt;major&gt;</pre>
<p>where <code>client-</code> is literal, <code>&lt;client&gt;</code> is a string uniquely identifying the client, <code>&lt;kind&gt;</code> is one of the <i>Object Kinds</i>, <code>-v</code> is literal, and <code>&lt;major&gt;</code> is the major version number. Each client must choose a unique <code>&lt;client&gt;</code> identifier via its own means. </p>
<p> Files of this form are stateless queries owned by the client <code>&lt;client&gt;</code>. The owning client may remove them at any time.</p>
<h3>v1 Client Stateful Query Files</h3>
<p>Stateful query files allow clients to request a list of versions of each of the <i>Object Kinds</i> and get only the most recent version recognized by the CMake that runs. </p>
<p> Clients may create owned stateful queries by creating <code>query.json</code> files in client-specific query subdirectories. The form is: </p>
<pre>&lt;build&gt;/.cmake/api/v1/query/client-&lt;client&gt;/query.json</pre>
<p>where <code>client-</code> is literal, <code>&lt;client&gt;</code> is a string uniquely identifying the client, and <code>query.json</code> is literal. Each client must choose a unique <code>&lt;client&gt;</code> identifier via its own means. </p>
<p> <code>query.json</code> files are stateful queries owned by the client <code>&lt;client&gt;</code>. The owning client may update or remove them at any time. When a given client installation is updated it may then update the stateful query it writes to build trees to request newer object versions. This can be used to avoid asking CMake to generate multiple object versions unnecessarily. </p>
<p> A <code>query.json</code> file must contain a JSON object: </p>
<pre>{
 &quot;requests&quot;: [
 { &quot;kind&quot;: &quot;&lt;kind&gt;&quot; , &quot;version&quot;: 1 },
 { &quot;kind&quot;: &quot;&lt;kind&gt;&quot; , &quot;version&quot;: { &quot;major&quot;: 1, &quot;minor&quot;: 2 } },
 { &quot;kind&quot;: &quot;&lt;kind&gt;&quot; , &quot;version&quot;: [2, 1] },
 { &quot;kind&quot;: &quot;&lt;kind&gt;&quot; , &quot;version&quot;: [2, { &quot;major&quot;: 1, &quot;minor&quot;: 2 }] },
 { &quot;kind&quot;: &quot;&lt;kind&gt;&quot; , &quot;version&quot;: 1, &quot;client&quot;: {} },
 { &quot;kind&quot;: &quot;...&quot; }
 ],
 &quot;client&quot;: {}
}</pre>
<p>The members are:</p>
<dl>
<dt><code>requests</code></p>
<dd>A JSON array containing zero or more requests. Each request is a JSON object with members:</p>
<dt><code>kind</code></p>
<dd>Specifies one of the <i>Object Kinds</i> to be included in the reply.</p>
<dt><code>version</code></p>
<dd>Indicates the version(s) of the object kind that the client understands. Versions have major and minor components following semantic version conventions. The value must be</p>
<dt>&bull;</p>
<dd>a JSON integer specifying a (non-negative) major version number, or</p>
<dt>&bull;</p>
<dd>a JSON object containing <code>major</code> and (optionally) <code>minor</code> members specifying non-negative integer version components, or</p>
<dt>&bull;</p>
<dd>a JSON array whose elements are each one of the above.</p>
<dt><code>client</code></p>
<dd>Optional member reserved for use by the client. This value is preserved in the reply written for the client in the <i>v1 Reply Index File</i> but is otherwise ignored. Clients may use this to pass custom information with a request through to its reply. </p>
<p> For each requested object kind CMake will choose the <i>first</i> version that it recognizes for that kind among those listed in the request. The response will use the selected <i>major</i> version with the highest <i>minor</i> version known to the running CMake for that major version. Therefore clients should list all supported major versions in preferred order along with the minimal minor version required for each major version.</p>
<dt><code>client</code></p>
<dd>Optional member reserved for use by the client. This value is preserved in the reply written for the client in the <i>v1 Reply Index File</i> but is otherwise ignored. Clients may use this to pass custom information with a query through to its reply. </p>
<p> Other <code>query.json</code> top-level members are reserved for future use. If present they are ignored for forward compatibility.</dl>
<h3>v1 Reply Index File</h3>
<p>CMake writes an <code>index-*.json</code> file to the <code>v1/reply/</code> directory whenever it runs to generate a build system. Clients must read the reply index file first and may read other <i>v1 Reply Files</i> only by following references. The form of the reply index file name is: </p>
<pre>&lt;build&gt;/.cmake/api/v1/reply/index-&lt;unspecified&gt;.json</pre>
<p>where <code>index-</code> is literal and <code>&lt;unspecified&gt;</code> is an unspecified name selected by CMake. Whenever a new index file is generated it is given a new name and any old one is deleted. During the short time between these steps there may be multiple index files present; the one with the largest name in lexicographic order is the current index file. </p>
<p> The reply index file contains a JSON object: </p>
<pre>{
 &quot;cmake&quot;: {
 &quot;version&quot;: {
 &quot;major&quot;: 3, &quot;minor&quot;: 14, &quot;patch&quot;: 0, &quot;suffix&quot;: &quot;&quot;,
 &quot;string&quot;: &quot;3.14.0&quot;, &quot;isDirty&quot;: false
 },
 &quot;paths&quot;: {
 &quot;cmake&quot;: &quot;/prefix/bin/cmake&quot;,
 &quot;ctest&quot;: &quot;/prefix/bin/ctest&quot;,
 &quot;cpack&quot;: &quot;/prefix/bin/cpack&quot;,
 &quot;root&quot;: &quot;/prefix/share/cmake-3.14&quot;
 },
 &quot;generator&quot;: {
 &quot;multiConfig&quot;: false,
 &quot;name&quot;: &quot;Unix Makefiles&quot;
 }
 },
 &quot;objects&quot;: [
 { &quot;kind&quot;: &quot;&lt;kind&gt;&quot;,
 &quot;version&quot;: { &quot;major&quot;: 1, &quot;minor&quot;: 0 },
 &quot;jsonFile&quot;: &quot;&lt;file&gt;&quot; },
 { &quot;...&quot;: &quot;...&quot; }
 ],
 &quot;reply&quot;: {
 &quot;&lt;kind&gt;-v&lt;major&gt;&quot;: { &quot;kind&quot;: &quot;&lt;kind&gt;&quot;,
 &quot;version&quot;: { &quot;major&quot;: 1, &quot;minor&quot;: 0 },
 &quot;jsonFile&quot;: &quot;&lt;file&gt;&quot; },
 &quot;&lt;unknown&gt;&quot;: { &quot;error&quot;: &quot;unknown query file&quot; },
 &quot;...&quot;: {},
 &quot;client-&lt;client&gt;&quot;: {
 &quot;&lt;kind&gt;-v&lt;major&gt;&quot;: { &quot;kind&quot;: &quot;&lt;kind&gt;&quot;,
 &quot;version&quot;: { &quot;major&quot;: 1, &quot;minor&quot;: 0 },
 &quot;jsonFile&quot;: &quot;&lt;file&gt;&quot; },
 &quot;&lt;unknown&gt;&quot;: { &quot;error&quot;: &quot;unknown query file&quot; },
 &quot;...&quot;: {},
 &quot;query.json&quot;: {
 &quot;requests&quot;: [ {}, {}, {} ],
 &quot;responses&quot;: [
 { &quot;kind&quot;: &quot;&lt;kind&gt;&quot;,
 &quot;version&quot;: { &quot;major&quot;: 1, &quot;minor&quot;: 0 },
 &quot;jsonFile&quot;: &quot;&lt;file&gt;&quot; },
 { &quot;error&quot;: &quot;unknown query file&quot; },
 { &quot;...&quot;: {} }
 ],
 &quot;client&quot;: {}
 }
 }
 }
}</pre>
<p>The members are:</p>
<dl>
<dt><code>cmake</code></p>
<dd>A JSON object containing information about the instance of CMake that generated the reply. It contains members:</p>
<dt><code>version</code></p>
<dd>A JSON object specifying the version of CMake with members:</p>
<dt><code>major</code>, <code>minor</code>, <code>patch</code></p>
<dd>Integer values specifying the major, minor, and patch version components.</p>
<dt><code>suffix</code></p>
<dd>A string specifying the version suffix, if any, e.g. <code>g0abc3</code>.</p>
<dt><code>string</code></p>
<dd>A string specifying the full version in the format <code>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;[-&lt;suffix&gt;]</code>.</p>
<dt><code>isDirty</code></p>
<dd>A boolean indicating whether the version was built from a version controlled source tree with local modifications.</p>
<dt><code>paths</code></p>
<dd>A JSON object specifying paths to things that come with CMake. It has members for <code>cmake</code>, <code>ctest</code>, and <code>cpack</code> whose values are JSON strings specifying the absolute path to each tool, represented with forward slashes. It also has a <code>root</code> member for the absolute path to the directory containing CMake resources like the <code>Modules/</code> directory (see <code>CMAKE_ROOT</code>).</p>
<dt><code>generator</code></p>
<dd>A JSON object describing the CMake generator used for the build. It has members:</p>
<dt><code>multiConfig</code></p>
<dd>A boolean specifying whether the generator supports multiple output configurations.</p>
<dt><code>name</code></p>
<dd>A string specifying the name of the generator.</p>
<dt><code>platform</code></p>
<dd>If the generator supports <code>CMAKE_GENERATOR_PLATFORM</code>, this is a string specifying the generator platform name.</p>
<dt><code>objects</code></p>
<dd>A JSON array listing all versions of all <i>Object Kinds</i> generated as part of the reply. Each array entry is a <i>v1 Reply File Reference</i>.</p>
<dt><code>reply</code></p>
<dd>A JSON object mirroring the content of the <code>query/</code> directory that CMake loaded to produce the reply. The members are of the form</p>
<dt><code>&lt;kind&gt;-v&lt;major&gt;</code></p>
<dd>A member of this form appears for each of the <i>v1 Shared Stateless Query Files</i> that CMake recognized as a request for object kind <code>&lt;kind&gt;</code> with major version <code>&lt;major&gt;</code>. The value is a <i>v1 Reply File Reference</i> to the corresponding reply file for that object kind and version.</p>
<dt><code>&lt;unknown&gt;</code></p>
<dd>A member of this form appears for each of the <i>v1 Shared Stateless Query Files</i> that CMake did not recognize. The value is a JSON object with a single <code>error</code> member containing a string with an error message indicating that the query file is unknown.</p>
<dt><code>client-&lt;client&gt;</code></p>
<dd>A member of this form appears for each client-owned directory holding <i>v1 Client Stateless Query Files</i>. The value is a JSON object mirroring the content of the <code>query/client-&lt;client&gt;/</code> directory. The members are of the form:</p>
<dt><code>&lt;kind&gt;-v&lt;major&gt;</code></p>
<dd>A member of this form appears for each of the <i>v1 Client Stateless Query Files</i> that CMake recognized as a request for object kind <code>&lt;kind&gt;</code> with major version <code>&lt;major&gt;</code>. The value is a <i>v1 Reply File Reference</i> to the corresponding reply file for that object kind and version.</p>
<dt><code>&lt;unknown&gt;</code></p>
<dd>A member of this form appears for each of the <i>v1 Client Stateless Query Files</i> that CMake did not recognize. The value is a JSON object with a single <code>error</code> member containing a string with an error message indicating that the query file is unknown.</p>
<dt><code>query.json</code></p>
<dd>This member appears for clients using <i>v1 Client Stateful Query Files</i>. If the <code>query.json</code> file failed to read or parse as a JSON object, this member is a JSON object with a single <code>error</code> member containing a string with an error message. Otherwise, this member is a JSON object mirroring the content of the <code>query.json</code> file. The members are:</p>
<dt><code>client</code></p>
<dd>A copy of the <code>query.json</code> file <code>client</code> member, if it exists.</p>
<dt><code>requests</code></p>
<dd>A copy of the <code>query.json</code> file <code>requests</code> member, if it exists.</p>
<dt><code>responses</code></p>
<dd>If the <code>query.json</code> file <code>requests</code> member is missing or invalid, this member is a JSON object with a single <code>error</code> member containing a string with an error message. Otherwise, this member contains a JSON array with a response for each entry of the <code>requests</code> array, in the same order. Each response is</p>
<dt>&bull;</p>
<dd>a JSON object with a single <code>error</code> member containing a string with an error message, or</p>
<dt>&bull;</p>
<dd>a <i>v1 Reply File Reference</i> to the corresponding reply file for the requested object kind and selected version. </p>
<p> After reading the reply index file, clients may read the other <i>v1 Reply Files</i> it references.</dl>
<h3>v1 Reply File Reference</h3>
<p>The reply index file represents each reference to another reply file using a JSON object with members:</p>
<dl>
<dt><code>kind</code></p>
<dd>A string specifying one of the <i>Object Kinds</i>.</p>
<dt><code>version</code></p>
<dd>A JSON object with members <code>major</code> and <code>minor</code> specifying integer version components of the object kind.</p>
<dt><code>jsonFile</code></p>
<dd>A JSON string specifying a path relative to the reply index file to another JSON file containing the object.</dl>
<h3>v1 Reply Files</h3>
<p>Reply files containing specific <i>Object Kinds</i> are written by CMake. The names of these files are unspecified and must not be interpreted by clients. Clients must first read the <i>v1 Reply Index File</i> and and follow references to the names of the desired response objects. </p>
<p> Reply files (including the index file) will never be replaced by files of the same name but different content. This allows a client to read the files concurrently with a running CMake that may generate a new reply. However, after generating a new reply CMake will attempt to remove reply files from previous runs that it did not just write. If a client attempts to read a reply file referenced by the index but finds the file missing, that means a concurrent CMake has generated a new reply. The client may simply start again by reading the new reply index file.</p>
<h2>Object Kinds</h2>
<p>The CMake file-based API reports semantic information about the build system using the following kinds of JSON objects. Each kind of object is versioned independently using semantic versioning with major and minor components. Every kind of object has the form: </p>
<pre>{
 &quot;kind&quot;: &quot;&lt;kind&gt;&quot;,
 &quot;version&quot;: { &quot;major&quot;: 1, &quot;minor&quot;: 0 },
 &quot;...&quot;: {}
}</pre>
<p>The <code>kind</code> member is a string specifying the object kind name. The <code>version</code> member is a JSON object with <code>major</code> and <code>minor</code> members specifying integer components of the object kind&#8217;s version. Additional top-level members are specific to each object kind.</p>
<h3>Object Kind codemodel</h3>
<p>The <code>codemodel</code> object kind describes the build system structure as modeled by CMake. </p>
<p> There is only one <code>codemodel</code> object major version, version 2. Version 1 does not exist to avoid confusion with that from <code><a href="/docs/linux/man/7-cmake-server/">cmake-server</a>(7)</code> mode.</p>
<h3>codemodel version 2</h3>
<p><code>codemodel</code> object version 2 is a JSON object: </p>
<pre>{
 &quot;kind&quot;: &quot;codemodel&quot;,
 &quot;version&quot;: { &quot;major&quot;: 2, &quot;minor&quot;: 2 },
 &quot;paths&quot;: {
 &quot;source&quot;: &quot;/path/to/top-level-source-dir&quot;,
 &quot;build&quot;: &quot;/path/to/top-level-build-dir&quot;
 },
 &quot;configurations&quot;: [
 {
 &quot;name&quot;: &quot;Debug&quot;,
 &quot;directories&quot;: [
 {
 &quot;source&quot;: &quot;.&quot;,
 &quot;build&quot;: &quot;.&quot;,
 &quot;childIndexes&quot;: [ 1 ],
 &quot;projectIndex&quot;: 0,
 &quot;targetIndexes&quot;: [ 0 ],
 &quot;hasInstallRule&quot;: true,
 &quot;minimumCMakeVersion&quot;: {
 &quot;string&quot;: &quot;3.14&quot;
 },
 &quot;jsonFile&quot;: &quot;&lt;file&gt;&quot;
 },
 {
 &quot;source&quot;: &quot;sub&quot;,
 &quot;build&quot;: &quot;sub&quot;,
 &quot;parentIndex&quot;: 0,
 &quot;projectIndex&quot;: 0,
 &quot;targetIndexes&quot;: [ 1 ],
 &quot;minimumCMakeVersion&quot;: {
 &quot;string&quot;: &quot;3.14&quot;
 },
 &quot;jsonFile&quot;: &quot;&lt;file&gt;&quot;
 }
 ],
 &quot;projects&quot;: [
 {
 &quot;name&quot;: &quot;MyProject&quot;,
 &quot;directoryIndexes&quot;: [ 0, 1 ],
 &quot;targetIndexes&quot;: [ 0, 1 ]
 }
 ],
 &quot;targets&quot;: [
 {
 &quot;name&quot;: &quot;MyExecutable&quot;,
 &quot;directoryIndex&quot;: 0,
 &quot;projectIndex&quot;: 0,
 &quot;jsonFile&quot;: &quot;&lt;file&gt;&quot;
 },
 {
 &quot;name&quot;: &quot;MyLibrary&quot;,
 &quot;directoryIndex&quot;: 1,
 &quot;projectIndex&quot;: 0,
 &quot;jsonFile&quot;: &quot;&lt;file&gt;&quot;
 }
 ]
 }
 ]
}</pre>
<p>The members specific to <code>codemodel</code> objects are:</p>
<dl>
<dt><code>paths</code></p>
<dd>A JSON object containing members:</p>
<dt><code>source</code></p>
<dd>A string specifying the absolute path to the top-level source directory, represented with forward slashes.</p>
<dt><code>build</code></p>
<dd>A string specifying the absolute path to the top-level build directory, represented with forward slashes.</p>
<dt><code>configurations</code></p>
<dd>A JSON array of entries corresponding to available build configurations. On single-configuration generators there is one entry for the value of the <code>CMAKE_BUILD_TYPE</code> variable. For multi-configuration generators there is an entry for each configuration listed in the <code>CMAKE_CONFIGURATION_TYPES</code> variable. Each entry is a JSON object containing members:</p>
<dt><code>name</code></p>
<dd>A string specifying the name of the configuration, e.g. <code>Debug</code>.</p>
<dt><code>directories</code></p>
<dd>A JSON array of entries each corresponding to a build system directory whose source directory contains a <code>CMakeLists.txt</code> file. The first entry corresponds to the top-level directory. Each entry is a JSON object containing members:</p>
<dt><code>source</code></p>
<dd>A string specifying the path to the source directory, represented with forward slashes. If the directory is inside the top-level source directory then the path is specified relative to that directory (with <code>.</code> for the top-level source directory itself). Otherwise the path is absolute.</p>
<dt><code>build</code></p>
<dd>A string specifying the path to the build directory, represented with forward slashes. If the directory is inside the top-level build directory then the path is specified relative to that directory (with <code>.</code> for the top-level build directory itself). Otherwise the path is absolute.</p>
<dt><code>parentIndex</code></p>
<dd>Optional member that is present when the directory is not top-level. The value is an unsigned integer 0-based index of another entry in the main <code>directories</code> array that corresponds to the parent directory that added this directory as a subdirectory.</p>
<dt><code>childIndexes</code></p>
<dd>Optional member that is present when the directory has subdirectories. The value is a JSON array of entries corresponding to child directories created by the <code>add_subdirectory()</code> or <code>subdirs()</code> command. Each entry is an unsigned integer 0-based index of another entry in the main <code>directories</code> array.</p>
<dt><code>projectIndex</code></p>
<dd>An unsigned integer 0-based index into the main <code>projects</code> array indicating the build system project to which the this directory belongs.</p>
<dt><code>targetIndexes</code></p>
<dd>Optional member that is present when the directory itself has targets, excluding those belonging to subdirectories. The value is a JSON array of entries corresponding to the targets. Each entry is an unsigned integer 0-based index into the main <code>targets</code> array.</p>
<dt><code>minimumCMakeVersion</code></p>
<dd>Optional member present when a minimum required version of CMake is known for the directory. This is the <code>&lt;min&gt;</code> version given to the most local call to the <code>cmake_minimum_required(VERSION)</code> command in the directory itself or one of its ancestors. The value is a JSON object with one member:</p>
<dt><code>string</code></p>
<dd>A string specifying the minimum required version in the format: </p>
<pre>&lt;major&gt;.&lt;minor&gt;[.&lt;patch&gt;[.&lt;tweak&gt;]][&lt;suffix&gt;]</pre>
<p>Each component is an unsigned integer and the suffix may be an arbitrary string.</p>
<dt><code>hasInstallRule</code></p>
<dd>Optional member that is present with boolean value <code>true</code> when the directory or one of its subdirectories contains any <code>install()</code> rules, i.e. whether a <code>make install</code> or equivalent rule is available.</p>
<dt><code>jsonFile</code></p>
<dd>A JSON string specifying a path relative to the codemodel file to another JSON file containing a <i>&quot;codemodel&quot; version 2 &quot;directory&quot; object</i>. </p>
<p> This field was added in codemodel version 2.3.</p>
<dt><code>projects</code></p>
<dd>A JSON array of entries corresponding to the top-level project and sub-projects defined in the build system. Each (sub-)project corresponds to a source directory whose <code>CMakeLists.txt</code> file calls the <code>project()</code> command with a project name different from its parent directory. The first entry corresponds to the top-level project. </p>
<p> Each entry is a JSON object containing members:</p>
<dt><code>name</code></p>
<dd>A string specifying the name given to the <code>project()</code> command.</p>
<dt><code>parentIndex</code></p>
<dd>Optional member that is present when the project is not top-level. The value is an unsigned integer 0-based index of another entry in the main <code>projects</code> array that corresponds to the parent project that added this project as a sub-project.</p>
<dt><code>childIndexes</code></p>
<dd>Optional member that is present when the project has sub-projects. The value is a JSON array of entries corresponding to the sub-projects. Each entry is an unsigned integer 0-based index of another entry in the main <code>projects</code> array.</p>
<dt><code>directoryIndexes</code></p>
<dd>A JSON array of entries corresponding to build system directories that are part of the project. The first entry corresponds to the top-level directory of the project. Each entry is an unsigned integer 0-based index into the main <code>directories</code> array.</p>
<dt><code>targetIndexes</code></p>
<dd>Optional member that is present when the project itself has targets, excluding those belonging to sub-projects. The value is a JSON array of entries corresponding to the targets. Each entry is an unsigned integer 0-based index into the main <code>targets</code> array.</p>
<dt><code>targets</code></p>
<dd>A JSON array of entries corresponding to the build system targets. Such targets are created by calls to <code>add_executable()</code>, <code>add_library()</code>, and <code>add_custom_target()</code>, excluding imported targets and interface libraries (which do not generate any build rules). Each entry is a JSON object containing members:</p>
<dt><code>name</code></p>
<dd>A string specifying the target name.</p>
<dt><code>id</code></p>
<dd>A string uniquely identifying the target. This matches the <code>id</code> field in the file referenced by <code>jsonFile</code>.</p>
<dt><code>directoryIndex</code></p>
<dd>An unsigned integer 0-based index into the main <code>directories</code> array indicating the build system directory in which the target is defined.</p>
<dt><code>projectIndex</code></p>
<dd>An unsigned integer 0-based index into the main <code>projects</code> array indicating the build system project in which the target is defined.</p>
<dt><code>jsonFile</code></p>
<dd>A JSON string specifying a path relative to the codemodel file to another JSON file containing a <i>&quot;codemodel&quot; version 2 &quot;target&quot; object</i>.</dl>
<h3>codemodel version 2 directory object</h3>
<p>A codemodel &quot;directory&quot; object is referenced by a <i>&quot;codemodel&quot; version 2</i> object&#8217;s <code>directories</code> array. Each &quot;directory&quot; object is a JSON object with members:</p>
<dl>
<dt><code>paths</code></p>
<dd>A JSON object containing members:</p>
<dt><code>source</code></p>
<dd>A string specifying the path to the source directory, represented with forward slashes. If the directory is inside the top-level source directory then the path is specified relative to that directory (with <code>.</code> for the top-level source directory itself). Otherwise the path is absolute.</p>
<dt><code>build</code></p>
<dd>A string specifying the path to the build directory, represented with forward slashes. If the directory is inside the top-level build directory then the path is specified relative to that directory (with <code>.</code> for the top-level build directory itself). Otherwise the path is absolute.</p>
<dt><code>installers</code></p>
<dd>A JSON array of entries corresponding to <code>install()</code> rules. Each entry is a JSON object containing members:</p>
<dt><code>component</code></p>
<dd>A string specifying the component selected by the corresponding <code>install()</code> command invocation.</p>
<dt><code>destination</code></p>
<dd>Optional member that is present for specific <code>type</code> values below. The value is a string specifying the install destination path. The path may be absolute or relative to the install prefix.</p>
<dt><code>paths</code></p>
<dd>Optional member that is present for specific <code>type</code> values below. The value is a JSON array of entries corresponding to the paths (files or directories) to be installed. Each entry is one of:</p>
<dt>&bull;</p>
<dd>A string specifying the path from which a file or directory is to be installed. The portion of the path not preceded by a <code>/</code> also specifies the path (name) to which the file or directory is to be installed under the destination.</p>
<dt>&bull;</p>
<dd>A JSON object with members:</p>
<dt><code>from</code></p>
<dd>A string specifying the path from which a file or directory is to be installed.</p>
<dt><code>to</code></p>
<dd>A string specifying the path to which the file or directory is to be installed under the destination. </p>
<p> In both cases the paths are represented with forward slashes. If the &quot;from&quot; path is inside the top-level directory documented by the corresponding <code>type</code> value, then the path is specified relative to that directory. Otherwise the path is absolute.</p>
<dt><code>type</code></p>
<dd>A string specifying the type of installation rule. The value is one of the following, with some variants providing additional members:</p>
<dt><code>file</code></p>
<dd>An <code>install(FILES)</code> or <code>install(PROGRAMS)</code> call. The <code>destination</code> and <code>paths</code> members are populated, with paths under the top-level <i>source</i> directory expressed relative to it. The <code>isOptional</code> member may exist. This type has no additional members.</p>
<dt><code>directory</code></p>
<dd>An <code>install(DIRECTORY)</code> call. The <code>destination</code> and <code>paths</code> members are populated, with paths under the top-level <i>source</i> directory expressed relative to it. The <code>isOptional</code> member may exist. This type has no additional members.</p>
<dt><code>target</code></p>
<dd>An <code>install(TARGETS)</code> call. The <code>destination</code> and <code>paths</code> members are populated, with paths under the top-level <i>build</i> directory expressed relative to it. The <code>isOptional</code> member may exist. This type has additional members <code>targetId</code>, <code>targetIndex</code>, <code>targetIsImportLibrary</code>, and <code>targetInstallNamelink</code>.</p>
<dt><code>export</code></p>
<dd>An <code>install(EXPORT)</code> call. The <code>destination</code> and <code>paths</code> members are populated, with paths under the top-level <i>build</i> directory expressed relative to it. The <code>paths</code> entries refer to files generated automatically by CMake for installation, and their actual values are considered private implementation details. This type has additional members <code>exportName</code> and <code>exportTargets</code>.</p>
<dt><code>script</code></p>
<dd>An <code>install(SCRIPT)</code> call. This type has additional member <code>scriptFile</code>.</p>
<dt><code>code</code></p>
<dd>An <code>install(CODE)</code> call. This type has no additional members.</p>
<dt><code>importedRuntimeArtifacts</code></p>
<dd>An <code>install(IMPORTED_RUNTIME_ARTIFACTS)</code> call. The <code>destination</code> member is populated. The <code>isOptional</code> member may exist. This type has no additional members.</p>
<dt><code>runtimeDependencySet</code></p>
<dd>An <code>install(RUNTIME_DEPENDENCY_SET)</code> call or an <code>install(TARGETS)</code> call with <code>RUNTIME_DEPENDENCIES</code>. The <code>destination</code> member is populated. This type has additional members <code>runtimeDependencySetName</code> and <code>runtimeDependencySetType</code>.</p>
<dt><code>isExcludeFromAll</code></p>
<dd>Optional member that is present with boolean value <code>true</code> when <code>install()</code> is called with the <code>EXCLUDE_FROM_ALL</code> option.</p>
<dt><code>isForAllComponents</code></p>
<dd>Optional member that is present with boolean value <code>true</code> when <code>install(SCRIPT|CODE)</code> is called with the <code>ALL_COMPONENTS</code> option.</p>
<dt><code>isOptional</code></p>
<dd>Optional member that is present with boolean value <code>true</code> when <code>install()</code> is called with the <code>OPTIONAL</code> option. This is allowed when <code>type</code> is <code>file</code>, <code>directory</code>, or <code>target</code>.</p>
<dt><code>targetId</code></p>
<dd>Optional member that is present when <code>type</code> is <code>target</code>. The value is a string uniquely identifying the target to be installed. This matches the <code>id</code> member of the target in the main &quot;codemodel&quot; object&#8217;s <code>targets</code> array.</p>
<dt><code>targetIndex</code></p>
<dd>Optional member that is present when <code>type</code> is <code>target</code>. The value is an unsigned integer 0-based index into the main &quot;codemodel&quot; object&#8217;s <code>targets</code> array for the target to be installed.</p>
<dt><code>targetIsImportLibrary</code></p>
<dd>Optional member that is present when <code>type</code> is <code>target</code> and the installer is for a Windows DLL import library file or for an AIX linker import file. If present, it has boolean value <code>true</code>.</p>
<dt><code>targetInstallNamelink</code></p>
<dd>Optional member that is present when <code>type</code> is <code>target</code> and the installer corresponds to a target that may use symbolic links to implement the <code>VERSION</code> and <code>SOVERSION</code> target properties. The value is a string indicating how the installer is supposed to handle the symlinks: <code>skip</code> means the installer should skip the symlinks and install only the real file, and <code>only</code> means the installer should install only the symlinks and not the real file. In all cases the <code>paths</code> member lists what it actually installs.</p>
<dt><code>exportName</code></p>
<dd>Optional member that is present when <code>type</code> is <code>export</code>. The value is a string specifying the name of the export.</p>
<dt><code>exportTargets</code></p>
<dd>Optional member that is present when <code>type</code> is <code>export</code>. The value is a JSON array of entries corresponding to the targets included in the export. Each entry is a JSON object with members:</p>
<dt><code>id</code></p>
<dd>A string uniquely identifying the target. This matches the <code>id</code> member of the target in the main &quot;codemodel&quot; object&#8217;s <code>targets</code> array.</p>
<dt><code>index</code></p>
<dd>An unsigned integer 0-based index into the main &quot;codemodel&quot; object&#8217;s <code>targets</code> array for the target.</p>
<dt><code>runtimeDependencySetName</code></p>
<dd>Optional member that is present when <code>type</code> is <code>runtimeDependencySet</code> and the installer was created by an <code>install(RUNTIME_DEPENDENCY_SET)</code> call. The value is a string specifying the name of the runtime dependency set that was installed.</p>
<dt><code>runtimeDependencySetType</code></p>
<dd>Optional member that is present when <code>type</code> is <code>runtimeDependencySet</code>. The value is a string with one of the following values:</p>
<dt><code>library</code></p>
<dd>Indicates that this installer installs dependencies that are not macOS frameworks.</p>
<dt><code>framework</code></p>
<dd>Indicates that this installer installs dependencies that are macOS frameworks.</p>
<dt><code>scriptFile</code></p>
<dd>Optional member that is present when <code>type</code> is <code>script</code>. The value is a string specifying the path to the script file on disk, represented with forward slashes. If the file is inside the top-level source directory then the path is specified relative to that directory. Otherwise the path is absolute.</p>
<dt><code>backtrace</code></p>
<dd>Optional member that is present when a CMake language backtrace to the <code>install()</code> or other command invocation that added this installer is available. The value is an unsigned integer 0-based index into the <code>backtraceGraph</code> member&#8217;s <code>nodes</code> array.</p>
<dt><code>backtraceGraph</code></p>
<dd>A <i>&quot;codemodel&quot; version 2 &quot;backtrace graph&quot;</i> whose nodes are referenced from <code>backtrace</code> members elsewhere in this &quot;directory&quot; object.</dl>
<h3>codemodel version 2 target object</h3>
<p>A codemodel &quot;target&quot; object is referenced by a <i>&quot;codemodel&quot; version 2</i> object&#8217;s <code>targets</code> array. Each &quot;target&quot; object is a JSON object with members:</p>
<dl>
<dt><code>name</code></p>
<dd>A string specifying the logical name of the target.</p>
<dt><code>id</code></p>
<dd>A string uniquely identifying the target. The format is unspecified and should not be interpreted by clients.</p>
<dt><code>type</code></p>
<dd>A string specifying the type of the target. The value is one of <code>EXECUTABLE</code>, <code>STATIC_LIBRARY</code>, <code>SHARED_LIBRARY</code>, <code>MODULE_LIBRARY</code>, <code>OBJECT_LIBRARY</code>, <code>INTERFACE_LIBRARY</code>, or <code>UTILITY</code>.</p>
<dt><code>backtrace</code></p>
<dd>Optional member that is present when a CMake language backtrace to the command in the source code that created the target is available. The value is an unsigned integer 0-based index into the <code>backtraceGraph</code> member&#8217;s <code>nodes</code> array.</p>
<dt><code>folder</code></p>
<dd>Optional member that is present when the <code>FOLDER</code> target property is set. The value is a JSON object with one member:</p>
<dt><code>name</code></p>
<dd>A string specifying the name of the target folder.</p>
<dt><code>paths</code></p>
<dd>A JSON object containing members:</p>
<dt><code>source</code></p>
<dd>A string specifying the path to the target&#8217;s source directory, represented with forward slashes. If the directory is inside the top-level source directory then the path is specified relative to that directory (with <code>.</code> for the top-level source directory itself). Otherwise the path is absolute.</p>
<dt><code>build</code></p>
<dd>A string specifying the path to the target&#8217;s build directory, represented with forward slashes. If the directory is inside the top-level build directory then the path is specified relative to that directory (with <code>.</code> for the top-level build directory itself). Otherwise the path is absolute.</p>
<dt><code>nameOnDisk</code></p>
<dd>Optional member that is present for executable and library targets that are linked or archived into a single primary artifact. The value is a string specifying the file name of that artifact on disk.</p>
<dt><code>artifacts</code></p>
<dd>Optional member that is present for executable and library targets that produce artifacts on disk meant for consumption by dependents. The value is a JSON array of entries corresponding to the artifacts. Each entry is a JSON object containing one member:</p>
<dt><code>path</code></p>
<dd>A string specifying the path to the file on disk, represented with forward slashes. If the file is inside the top-level build directory then the path is specified relative to that directory. Otherwise the path is absolute.</p>
<dt><code>isGeneratorProvided</code></p>
<dd>Optional member that is present with boolean value <code>true</code> if the target is provided by CMake&#8217;s build system generator rather than by a command in the source code.</p>
<dt><code>install</code></p>
<dd>Optional member that is present when the target has an <code>install()</code> rule. The value is a JSON object with members:</p>
<dt><code>prefix</code></p>
<dd>A JSON object specifying the installation prefix. It has one member:</p>
<dt><code>path</code></p>
<dd>A string specifying the value of <code>CMAKE_INSTALL_PREFIX</code>.</p>
<dt><code>destinations</code></p>
<dd>A JSON array of entries specifying an install destination path. Each entry is a JSON object with members:</p>
<dt><code>path</code></p>
<dd>A string specifying the install destination path. The path may be absolute or relative to the install prefix.</p>
<dt><code>backtrace</code></p>
<dd>Optional member that is present when a CMake language backtrace to the <code>install()</code> command invocation that specified this destination is available. The value is an unsigned integer 0-based index into the <code>backtraceGraph</code> member&#8217;s <code>nodes</code> array.</p>
<dt><code>link</code></p>
<dd>Optional member that is present for executables and shared library targets that link into a runtime binary. The value is a JSON object with members describing the link step:</p>
<dt><code>language</code></p>
<dd>A string specifying the language (e.g. <code>C</code>, <code>CXX</code>, <code>Fortran</code>) of the toolchain is used to invoke the linker.</p>
<dt><code>commandFragments</code></p>
<dd>Optional member that is present when fragments of the link command line invocation are available. The value is a JSON array of entries specifying ordered fragments. Each entry is a JSON object with members:</p>
<dt><code>fragment</code></p>
<dd>A string specifying a fragment of the link command line invocation. The value is encoded in the build system&#8217;s native shell format.</p>
<dt><code>role</code></p>
<dd>A string specifying the role of the fragment&#8217;s content:</p>
<dt>&bull;</p>
<dd><code>flags</code>: link flags.</p>
<dt>&bull;</p>
<dd><code>libraries</code>: link library file paths or flags.</p>
<dt>&bull;</p>
<dd><code>libraryPath</code>: library search path flags.</p>
<dt>&bull;</p>
<dd><code>frameworkPath</code>: macOS framework search path flags.</p>
<dt><code>lto</code></p>
<dd>Optional member that is present with boolean value <code>true</code> when link-time optimization (a.k.a. interprocedural optimization or link-time code generation) is enabled.</p>
<dt><code>sysroot</code></p>
<dd>Optional member that is present when the <code>CMAKE_SYSROOT_LINK</code> or <code>CMAKE_SYSROOT</code> variable is defined. The value is a JSON object with one member:</p>
<dt><code>path</code></p>
<dd>A string specifying the absolute path to the sysroot, represented with forward slashes.</p>
<dt><code>archive</code></p>
<dd>Optional member that is present for static library targets. The value is a JSON object with members describing the archive step:</p>
<dt><code>commandFragments</code></p>
<dd>Optional member that is present when fragments of the archiver command line invocation are available. The value is a JSON array of entries specifying the fragments. Each entry is a JSON object with members:</p>
<dt><code>fragment</code></p>
<dd>A string specifying a fragment of the archiver command line invocation. The value is encoded in the build system&#8217;s native shell format.</p>
<dt><code>role</code></p>
<dd>A string specifying the role of the fragment&#8217;s content:</p>
<dt>&bull;</p>
<dd><code>flags</code>: archiver flags.</p>
<dt><code>lto</code></p>
<dd>Optional member that is present with boolean value <code>true</code> when link-time optimization (a.k.a. interprocedural optimization or link-time code generation) is enabled.</p>
<dt><code>dependencies</code></p>
<dd>Optional member that is present when the target depends on other targets. The value is a JSON array of entries corresponding to the dependencies. Each entry is a JSON object with members:</p>
<dt><code>id</code></p>
<dd>A string uniquely identifying the target on which this target depends. This matches the main <code>id</code> member of the other target.</p>
<dt><code>backtrace</code></p>
<dd>Optional member that is present when a CMake language backtrace to the <code>add_dependencies()</code>, <code>target_link_libraries()</code>, or other command invocation that created this dependency is available. The value is an unsigned integer 0-based index into the <code>backtraceGraph</code> member&#8217;s <code>nodes</code> array.</p>
<dt><code>sources</code></p>
<dd>A JSON array of entries corresponding to the target&#8217;s source files. Each entry is a JSON object with members:</p>
<dt><code>path</code></p>
<dd>A string specifying the path to the source file on disk, represented with forward slashes. If the file is inside the top-level source directory then the path is specified relative to that directory. Otherwise the path is absolute.</p>
<dt><code>compileGroupIndex</code></p>
<dd>Optional member that is present when the source is compiled. The value is an unsigned integer 0-based index into the <code>compileGroups</code> array.</p>
<dt><code>sourceGroupIndex</code></p>
<dd>Optional member that is present when the source is part of a source group either via the <code>source_group()</code> command or by default. The value is an unsigned integer 0-based index into the <code>sourceGroups</code> array.</p>
<dt><code>isGenerated</code></p>
<dd>Optional member that is present with boolean value <code>true</code> if the source is <code>GENERATED</code>.</p>
<dt><code>backtrace</code></p>
<dd>Optional member that is present when a CMake language backtrace to the <code>target_sources()</code>, <code>add_executable()</code>, <code>add_library()</code>, <code>add_custom_target()</code>, or other command invocation that added this source to the target is available. The value is an unsigned integer 0-based index into the <code>backtraceGraph</code> member&#8217;s <code>nodes</code> array.</p>
<dt><code>sourceGroups</code></p>
<dd>Optional member that is present when sources are grouped together by the <code>source_group()</code> command or by default. The value is a JSON array of entries corresponding to the groups. Each entry is a JSON object with members:</p>
<dt><code>name</code></p>
<dd>A string specifying the name of the source group.</p>
<dt><code>sourceIndexes</code></p>
<dd>A JSON array listing the sources belonging to the group. Each entry is an unsigned integer 0-based index into the main <code>sources</code> array for the target.</p>
<dt><code>compileGroups</code></p>
<dd>Optional member that is present when the target has sources that compile. The value is a JSON array of entries corresponding to groups of sources that all compile with the same settings. Each entry is a JSON object with members:</p>
<dt><code>sourceIndexes</code></p>
<dd>A JSON array listing the sources belonging to the group. Each entry is an unsigned integer 0-based index into the main <code>sources</code> array for the target.</p>
<dt><code>language</code></p>
<dd>A string specifying the language (e.g. <code>C</code>, <code>CXX</code>, <code>Fortran</code>) of the toolchain is used to compile the source file.</p>
<dt><code>languageStandard</code></p>
<dd>Optional member that is present when the language standard is set explicitly (e.g. via <code>CXX_STANDARD</code>) or implicitly by compile features. Each entry is a JSON object with two members:</p>
<dt><code>backtraces</code></p>
<dd>Optional member that is present when a CMake language backtrace to the <code>&lt;LANG&gt;_STANDARD</code> setting is available. If the language standard was set implicitly by compile features those are used as the backtrace(s). It&#8217;s possible for multiple compile features to require the same language standard so there could be multiple backtraces. The value is a JSON array with each entry being an unsigned integer 0-based index into the <code>backtraceGraph</code> member&#8217;s <code>nodes</code> array.</p>
<dt><code>standard</code></p>
<dd>String representing the language standard. </p>
<p> This field was added in codemodel version 2.2.</p>
<dt><code>compileCommandFragments</code></p>
<dd>Optional member that is present when fragments of the compiler command line invocation are available. The value is a JSON array of entries specifying ordered fragments. Each entry is a JSON object with one member:</p>
<dt><code>fragment</code></p>
<dd>A string specifying a fragment of the compile command line invocation. The value is encoded in the build system&#8217;s native shell format.</p>
<dt><code>includes</code></p>
<dd>Optional member that is present when there are include directories. The value is a JSON array with an entry for each directory. Each entry is a JSON object with members:</p>
<dt><code>path</code></p>
<dd>A string specifying the path to the include directory, represented with forward slashes.</p>
<dt><code>isSystem</code></p>
<dd>Optional member that is present with boolean value <code>true</code> if the include directory is marked as a system include directory.</p>
<dt><code>backtrace</code></p>
<dd>Optional member that is present when a CMake language backtrace to the <code>target_include_directories()</code> or other command invocation that added this include directory is available. The value is an unsigned integer 0-based index into the <code>backtraceGraph</code> member&#8217;s <code>nodes</code> array.</p>
<dt><code>precompileHeaders</code></p>
<dd>Optional member that is present when <code>target_precompile_headers()</code> or other command invocations set <code>PRECOMPILE_HEADERS</code> on the target. The value is a JSON array with an entry for each header. Each entry is a JSON object with members:</p>
<dt><code>header</code></p>
<dd>Full path to the precompile header file.</p>
<dt><code>backtrace</code></p>
<dd>Optional member that is present when a CMake language backtrace to the <code>target_precompile_headers()</code> or other command invocation that added this precompiled header is available. The value is an unsigned integer 0-based index into the <code>backtraceGraph</code> member&#8217;s <code>nodes</code> array. </p>
<p> This field was added in codemodel version 2.1.</p>
<dt><code>defines</code></p>
<dd>Optional member that is present when there are preprocessor definitions. The value is a JSON array with an entry for each definition. Each entry is a JSON object with members:</p>
<dt><code>define</code></p>
<dd>A string specifying the preprocessor definition in the format <code>&lt;name&gt;[=&lt;value&gt;]</code>, e.g. <code>DEF</code> or <code>DEF=1</code>.</p>
<dt><code>backtrace</code></p>
<dd>Optional member that is present when a CMake language backtrace to the <code>target_compile_definitions()</code> or other command invocation that added this preprocessor definition is available. The value is an unsigned integer 0-based index into the <code>backtraceGraph</code> member&#8217;s <code>nodes</code> array.</p>
<dt><code>sysroot</code></p>
<dd>Optional member that is present when the <code>CMAKE_SYSROOT_COMPILE</code> or <code>CMAKE_SYSROOT</code> variable is defined. The value is a JSON object with one member:</p>
<dt><code>path</code></p>
<dd>A string specifying the absolute path to the sysroot, represented with forward slashes.</p>
<dt><code>backtraceGraph</code></p>
<dd>A <i>&quot;codemodel&quot; version 2 &quot;backtrace graph&quot;</i> whose nodes are referenced from <code>backtrace</code> members elsewhere in this &quot;target&quot; object.</dl>
<h3>codemodel version 2 backtrace graph</h3>
<p>The <code>backtraceGraph</code> member of a <i>&quot;codemodel&quot; version 2 &quot;directory&quot; object</i>, or <i>&quot;codemodel&quot; version 2 &quot;target&quot; object</i> is a JSON object describing a graph of backtraces. Its nodes are referenced from <code>backtrace</code> members elsewhere in the containing object. The backtrace graph object members are:</p>
<dl>
<dt><code>nodes</code></p>
<dd>A JSON array listing nodes in the backtrace graph. Each entry is a JSON object with members:</p>
<dt><code>file</code></p>
<dd>An unsigned integer 0-based index into the backtrace <code>files</code> array.</p>
<dt><code>line</code></p>
<dd>An optional member present when the node represents a line within the file. The value is an unsigned integer 1-based line number.</p>
<dt><code>command</code></p>
<dd>An optional member present when the node represents a command invocation within the file. The value is an unsigned integer 0-based index into the backtrace <code>commands</code> array.</p>
<dt><code>parent</code></p>
<dd>An optional member present when the node is not the bottom of the call stack. The value is an unsigned integer 0-based index of another entry in the backtrace <code>nodes</code> array.</p>
<dt><code>commands</code></p>
<dd>A JSON array listing command names referenced by backtrace nodes. Each entry is a string specifying a command name.</p>
<dt><code>files</code></p>
<dd>A JSON array listing CMake language files referenced by backtrace nodes. Each entry is a string specifying the path to a file, represented with forward slashes. If the file is inside the top-level source directory then the path is specified relative to that directory. Otherwise the path is absolute.</dl>
<h3>Object Kind cache</h3>
<p>The <code>cache</code> object kind lists cache entries. These are the CMake Language Variables stored in the persistent cache (<code>CMakeCache.txt</code>) for the build tree. </p>
<p> There is only one <code>cache</code> object major version, version 2. Version 1 does not exist to avoid confusion with that from <code><a href="/docs/linux/man/7-cmake-server/">cmake-server</a>(7)</code> mode.</p>
<h3>cache version 2</h3>
<p><code>cache</code> object version 2 is a JSON object: </p>
<pre>{
 &quot;kind&quot;: &quot;cache&quot;,
 &quot;version&quot;: { &quot;major&quot;: 2, &quot;minor&quot;: 0 },
 &quot;entries&quot;: [
 {
 &quot;name&quot;: &quot;BUILD_SHARED_LIBS&quot;,
 &quot;value&quot;: &quot;ON&quot;,
 &quot;type&quot;: &quot;BOOL&quot;,
 &quot;properties&quot;: [
 {
 &quot;name&quot;: &quot;HELPSTRING&quot;,
 &quot;value&quot;: &quot;Build shared libraries&quot;
 }
 ]
 },
 {
 &quot;name&quot;: &quot;CMAKE_GENERATOR&quot;,
 &quot;value&quot;: &quot;Unix Makefiles&quot;,
 &quot;type&quot;: &quot;INTERNAL&quot;,
 &quot;properties&quot;: [
 {
 &quot;name&quot;: &quot;HELPSTRING&quot;,
 &quot;value&quot;: &quot;Name of generator.&quot;
 }
 ]
 }
 ]
}</pre>
<p>The members specific to <code>cache</code> objects are:</p>
<dl>
<dt><code>entries</code></p>
<dd>A JSON array whose entries are each a JSON object specifying a cache entry. The members of each entry are:</p>
<dt><code>name</code></p>
<dd>A string specifying the name of the entry.</p>
<dt><code>value</code></p>
<dd>A string specifying the value of the entry.</p>
<dt><code>type</code></p>
<dd>A string specifying the type of the entry used by <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> to choose a widget for editing.</p>
<dt><code>properties</code></p>
<dd>A JSON array of entries specifying associated cache entry properties. Each entry is a JSON object containing members:</p>
<dt><code>name</code></p>
<dd>A string specifying the name of the cache entry property.</p>
<dt><code>value</code></p>
<dd>A string specifying the value of the cache entry property.</dl>
<h3>Object Kind cmakeFiles</h3>
<p>The <code>cmakeFiles</code> object kind lists files used by CMake while configuring and generating the build system. These include the <code>CMakeLists.txt</code> files as well as included <code>.cmake</code> files. </p>
<p> There is only one <code>cmakeFiles</code> object major version, version 1.</p>
<h3>cmakeFiles version 1</h3>
<p><code>cmakeFiles</code> object version 1 is a JSON object: </p>
<pre>{
 &quot;kind&quot;: &quot;cmakeFiles&quot;,
 &quot;version&quot;: { &quot;major&quot;: 1, &quot;minor&quot;: 0 },
 &quot;paths&quot;: {
 &quot;build&quot;: &quot;/path/to/top-level-build-dir&quot;,
 &quot;source&quot;: &quot;/path/to/top-level-source-dir&quot;
 },
 &quot;inputs&quot;: [
 {
 &quot;path&quot;: &quot;CMakeLists.txt&quot;
 },
 {
 &quot;isGenerated&quot;: true,
 &quot;path&quot;: &quot;/path/to/top-level-build-dir/.../CMakeSystem.cmake&quot;
 },
 {
 &quot;isExternal&quot;: true,
 &quot;path&quot;: &quot;/path/to/external/third-party/module.cmake&quot;
 },
 {
 &quot;isCMake&quot;: true,
 &quot;isExternal&quot;: true,
 &quot;path&quot;: &quot;/path/to/cmake/Modules/CMakeGenericSystem.cmake&quot;
 }
 ]
}</pre>
<p>The members specific to <code>cmakeFiles</code> objects are:</p>
<dl>
<dt><code>paths</code></p>
<dd>A JSON object containing members:</p>
<dt><code>source</code></p>
<dd>A string specifying the absolute path to the top-level source directory, represented with forward slashes.</p>
<dt><code>build</code></p>
<dd>A string specifying the absolute path to the top-level build directory, represented with forward slashes.</p>
<dt><code>inputs</code></p>
<dd>A JSON array whose entries are each a JSON object specifying an input file used by CMake when configuring and generating the build system. The members of each entry are:</p>
<dt><code>path</code></p>
<dd>A string specifying the path to an input file to CMake, represented with forward slashes. If the file is inside the top-level source directory then the path is specified relative to that directory. Otherwise the path is absolute.</p>
<dt><code>isGenerated</code></p>
<dd>Optional member that is present with boolean value <code>true</code> if the path specifies a file that is under the top-level build directory and the build is out-of-source. This member is not available on in-source builds.</p>
<dt><code>isExternal</code></p>
<dd>Optional member that is present with boolean value <code>true</code> if the path specifies a file that is not under the top-level source or build directories.</p>
<dt><code>isCMake</code></p>
<dd>Optional member that is present with boolean value <code>true</code> if the path specifies a file in the CMake installation.</dl>
<h3>Object Kind toolchains</h3>
<p>The <code>toolchains</code> object kind lists properties of the toolchains used during the build. These include the language, compiler path, ID, and version. </p>
<p> There is only one <code>toolchains</code> object major version, version 1.</p>
<h3>toolchains version 1</h3>
<p><code>toolchains</code> object version 1 is a JSON object: </p>
<pre>{
 &quot;kind&quot;: &quot;toolchains&quot;,
 &quot;version&quot;: { &quot;major&quot;: 1, &quot;minor&quot;: 0 },
 &quot;toolchains&quot;: [
 {
 &quot;language&quot;: &quot;C&quot;,
 &quot;compiler&quot;: {
 &quot;path&quot;: &quot;/usr/bin/cc&quot;,
 &quot;id&quot;: &quot;GNU&quot;,
 &quot;version&quot;: &quot;9.3.0&quot;,
 &quot;implicit&quot;: {
 &quot;includeDirectories&quot;: [
 &quot;/usr/lib/gcc/x86_64-linux-gnu/9/include&quot;,
 &quot;/usr/local/include&quot;,
 &quot;/usr/include/x86_64-linux-gnu&quot;,
 &quot;/usr/include&quot;
 ],
 &quot;linkDirectories&quot;: [
 &quot;/usr/lib/gcc/x86_64-linux-gnu/9&quot;,
 &quot;/usr/lib/x86_64-linux-gnu&quot;,
 &quot;/usr/lib&quot;,
 &quot;/lib/x86_64-linux-gnu&quot;,
 &quot;/lib&quot;
 ],
 &quot;linkFrameworkDirectories&quot;: [],
 &quot;linkLibraries&quot;: [ &quot;gcc&quot;, &quot;gcc_s&quot;, &quot;c&quot;, &quot;gcc&quot;, &quot;gcc_s&quot; ]
 }
 },
 &quot;sourceFileExtensions&quot;: [ &quot;c&quot;, &quot;m&quot; ]
 },
 {
 &quot;language&quot;: &quot;CXX&quot;,
 &quot;compiler&quot;: {
 &quot;path&quot;: &quot;/usr/bin/c++&quot;,
 &quot;id&quot;: &quot;GNU&quot;,
 &quot;version&quot;: &quot;9.3.0&quot;,
 &quot;implicit&quot;: {
 &quot;includeDirectories&quot;: [
 &quot;/usr/include/c++/9&quot;,
 &quot;/usr/include/x86_64-linux-gnu/c++/9&quot;,
 &quot;/usr/include/c++/9/backward&quot;,
 &quot;/usr/lib/gcc/x86_64-linux-gnu/9/include&quot;,
 &quot;/usr/local/include&quot;,
 &quot;/usr/include/x86_64-linux-gnu&quot;,
 &quot;/usr/include&quot;
 ],
 &quot;linkDirectories&quot;: [
 &quot;/usr/lib/gcc/x86_64-linux-gnu/9&quot;,
 &quot;/usr/lib/x86_64-linux-gnu&quot;,
 &quot;/usr/lib&quot;,
 &quot;/lib/x86_64-linux-gnu&quot;,
 &quot;/lib&quot;
 ],
 &quot;linkFrameworkDirectories&quot;: [],
 &quot;linkLibraries&quot;: [
 &quot;stdc++&quot;, &quot;m&quot;, &quot;gcc_s&quot;, &quot;gcc&quot;, &quot;c&quot;, &quot;gcc_s&quot;, &quot;gcc&quot;
 ]
 }
 },
 &quot;sourceFileExtensions&quot;: [
 &quot;C&quot;, &quot;M&quot;, &quot;c++&quot;, &quot;cc&quot;, &quot;cpp&quot;, &quot;cxx&quot;, &quot;mm&quot;, &quot;CPP&quot;
 ]
 }
 ]
}</pre>
<p>The members specific to <code>toolchains</code> objects are:</p>
<dl>
<dt><code>toolchains</code></p>
<dd>A JSON array whose entries are each a JSON object specifying a toolchain associated with a particular language. The members of each entry are:</p>
<dt><code>language</code></p>
<dd>A JSON string specifying the toolchain language, like C or CXX. Language names are the same as language names that can be passed to the <code>project()</code> command. Because CMake only supports a single toolchain per language, this field can be used as a key.</p>
<dt><code>compiler</code></p>
<dd>A JSON object containing members:</p>
<dt><code>path</code></p>
<dd>Optional member that is present when the <code>CMAKE_&lt;LANG&gt;_COMPILER</code> variable is defined for the current language. Its value is a JSON string holding the path to the compiler.</p>
<dt><code>id</code></p>
<dd>Optional member that is present when the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable is defined for the current language. Its value is a JSON string holding the ID (GNU, MSVC, etc.) of the compiler.</p>
<dt><code>version</code></p>
<dd>Optional member that is present when the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable is defined for the current language. Its value is a JSON string holding the version of the compiler.</p>
<dt><code>target</code></p>
<dd>Optional member that is present when the <code>CMAKE_&lt;LANG&gt;_COMPILER_TARGET</code> variable is defined for the current language. Its value is a JSON string holding the cross-compiling target of the compiler.</p>
<dt><code>implicit</code></p>
<dd>A JSON object containing members:</p>
<dt><code>includeDirectories</code></p>
<dd>Optional member that is present when the <code>CMAKE_&lt;LANG&gt;_IMPLICIT_INCLUDE_DIRECTORIES</code> variable is defined for the current language. Its value is a JSON array of JSON strings where each string holds a path to an implicit include directory for the compiler.</p>
<dt><code>linkDirectories</code></p>
<dd>Optional member that is present when the <code>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_DIRECTORIES</code> variable is defined for the current language. Its value is a JSON array of JSON strings where each string holds a path to an implicit link directory for the compiler.</p>
<dt><code>linkFrameworkDirectories</code></p>
<dd>Optional member that is present when the <code>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_FRAMEWORK_DIRECTORIES</code> variable is defined for the current language. Its value is a JSON array of JSON strings where each string holds a path to an implicit link framework directory for the compiler.</p>
<dt><code>linkLibraries</code></p>
<dd>Optional member that is present when the <code>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_LIBRARIES</code> variable is defined for the current language. Its value is a JSON array of JSON strings where each string holds a path to an implicit link library for the compiler.</p>
<dt><code>sourceFileExtensions</code></p>
<dd>Optional member that is present when the <code>CMAKE_&lt;LANG&gt;_SOURCE_FILE_EXTENSIONS</code> variable is defined for the current language. Its value is a JSON array of JSON strings where each each string holds a file extension (without the leading dot) for the language.</dl>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
