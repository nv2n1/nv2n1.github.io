---

title: "odb(1)"
name: "odb"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odb/"
description: "odb – object-relational mapping (ORM) compiler for C++"
---

<p> odb &#8211; object-relational mapping (ORM) compiler for C++</p>
<h2>SYNOPSIS</h2>
<p> <code>odb</code> <code>[</code> <i>options</i> <code>]</code> <i>file</i> <code>[</code> <i>file&#8230;</i> <code>]</code></p>
<h2>DESCRIPTION</h2>
<p> Given a set of C++ classes in a header file, <code>odb</code> generates C++ code that allows you to persist, query, and update objects of these classes in a relational database (RDBMS). The relational database that the generated code should target is specified with the required <code>&#8211;database</code> option (see below). </p>
<p> For an input file in the form <code>name.hxx</code> (other file extensions can be used instead of <code>.hxx</code>), in the single-database mode (the default), the generated C++ files by default have the following names: <code>name-odb.hxx</code> (header file), <code>name-odb.ixx</code> (inline file), and <code>name-odb.cxx</code> (source file). Additionally, if the <code>&#8211;generate-schema</code> option is specified and the <code>sql</code> schema format is requested (see <code>&#8211;schema-format</code>), the <code>name.sql</code> database schema file is generated. If the <code>separate</code> schema format is requested, the database creation code is generated into the separate <code>name-schema.cxx</code> file. </p>
<p> In the multi-database mode (see the <code>&#8211;multi-database</code> option below), the generated files corresponding to the <code>common</code> database have the same names as in the single-database mode. For other databases, the file names include the database name: <code>name-odb-</code><i>db</i><code>.hxx</code>, <code>name-odb-</code><i>db</i><code>.ixx</code>, <code>name-odb-</code><i>db</i><code>.cxx</code>, <code>name-</code><i>db</i><code>.sql</code>, and <code>name-schema-</code><i>db</i><code>.cxx</code> (where <i>db</i> is the database name).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Print usage information and exit. </dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version and exit. </dd>
<dt><code>-I</code> <i>dir</i></dt>
<dd> Add <i>dir</i> to the beginning of the list of directories to be searched for included header files. </dd>
<dt><code>-D</code> <i>name</i>[=<i>def</i>]</dt>
<dd> Define macro <i>name</i> with definition <i>def</i>. If definition is omitted, define <i>name</i> to be 1. </dd>
<dt><code>-U</code> <i>name</i></dt>
<dd> Cancel any previous definitions of macro <i>name</i>, either built-in or provided with the <code>-D</code> option. </dd>
<dt><code>&#8211;database</code>|<code>-d</code> <i>db</i></dt>
<dd> Generate code for the <i>db</i> database. Valid values are <code>mssql</code>, <code>mysql</code>, <code>oracle</code>, <code>pgsql</code>, <code>sqlite</code>, and <code>common</code> (multi-database mode only). </dd>
<dt><code>&#8211;multi-database</code>|<code>-m</code> <i>type</i></dt>
<dd> Enable multi-database support and specify its type. Valid values for this option are <code>static</code> and <code>dynamic</code>. </dd>
<p> In the multi-database mode, options that determine the kind (for example, <code>&#8211;schema-format</code>), names (for example, <code>&#8211;odb-file-suffix</code>), or content (for example, prologue and epilogue options) of the output files can be prefixed with the database name followed by a colon, for example, <code>mysql:value</code>. This restricts the value of such an option to only apply to generated files corresponding to this database. </p>
<dt><code>&#8211;default-database</code> <i>db</i></dt>
<dd> When static multi-database support is used, specify the database that should be made the default. When dynamic multi-database support is used, <code>common</code> is always made the default database. </dd>
<dt><code>&#8211;generate-query</code>|<code>-q</code></dt>
<dd> Generate query support code. Without this support you cannot use views and can only load objects via their ids. </dd>
<dt><code>&#8211;generate-prepared</code></dt>
<dd> Generate prepared query execution support code. </dd>
<dt><code>&#8211;omit-unprepared</code></dt>
<dd> Omit un-prepared (once-off) query execution support code. </dd>
<dt><code>&#8211;generate-session</code>|<code>-e</code></dt>
<dd> Generate session support code. With this option session support will be enabled by default for all the persistent classes except those for which it was explicitly disabled using the <code>db session</code> pragma. </dd>
<dt><code>&#8211;generate-schema</code>|<code>-s</code></dt>
<dd> Generate the database schema. The database schema contains SQL statements that create database tables necessary to store persistent classes defined in the file being compiled. Note that by applying this schema, all the existing information stored in such tables will be lost. </dd>
<p> Depending on the database being used (<code>&#8211;database</code> option), the schema is generated either as a standalone SQL file or embedded into the generated C++ code. By default the SQL file is generated for the MySQL, PostgreSQL, Oracle, and Microsoft SQL Server databases and the schema is embedded into the C++ code for the SQLite database. Use the <code>&#8211;schema-format</code> option to alter the default schema format. </p>
<p> If database schema evolution support is enabled (that is, the object model version is specified), then this option also triggers the generation of database schema migration statements, again either as standalong SQL files or embedded into the generated C++ code. You can suppress the generation of schema migration statements by specifying the <code>&#8211;suppress-migration</code> option. </p>
<dt><code>&#8211;generate-schema-only</code></dt>
<dd> Generate only the database schema. Note that this option is only valid when generating schema as a standalone SQL file (see <code>&#8211;schema-format</code> for details). </dd>
<dt><code>&#8211;suppress-migration</code></dt>
<dd> Suppress the generation of database schema migration statements. </dd>
<dt><code>&#8211;suppress-schema-version</code></dt>
<dd> Suppress the generation of schema version table. If you specify this option then you are also expected to manually specify the database schema version and migration state at runtime using the <code>odb::database::schema_version()</code> function. </dd>
<dt><code>&#8211;schema-version-table</code> <i>name</i></dt>
<dd> Specify the alternative schema version table name instead of the default <code>schema_version</code>. If you specify this option then you are also expected to manually specify the schema version table name at runtime using the <code>odb::database::schema_version_table()</code> function. The table name can be qualified. </dd>
<dt><code>&#8211;schema-format</code> <i>format</i></dt>
<dd> Generate the database schema in the specified format. Pass <code>sql</code> as <i>format</i> to generate the database schema as a standalone SQL file or pass <code>embedded</code> to embed the schema into the generated C++ code. The <code>separate</code> value is similar to <code>embedded</code> except the schema creation code is generated into a separate C++ file (<code>name-schema.cxx</code> by default). This value is primarily useful if you want to place the schema creation functionality into a separate program or library. Repeat this option to generate the same database schema in multiple formats. </dd>
<dt><code>&#8211;omit-drop</code></dt>
<dd> Omit <code>DROP</code> statements from the generated database schema. </dd>
<dt><code>&#8211;omit-create</code></dt>
<dd> Omit <code>CREATE</code> statements from the generated database schema. </dd>
<dt><code>&#8211;schema-name</code> <i>name</i></dt>
<dd> Use <i>name</i> as the database schema name. Schema names are primarily used to distinguish between multiple embedded schemas in the schema catalog. They are not to be confused with database schemas (database namespaces) which are specified with the <code>&#8211;schema</code> option. If this option is not specified, the empty name, which is the default schema name, is used. </dd>
<dt><code>&#8211;fkeys-deferrable-mode</code> <i>m</i></dt>
<dd> Use constraint checking mode <i>m</i> in foreign keys generated for object relationships. Valid values for this option are <code>not_deferrable</code>, <code>immediate</code>, and <code>deferred</code> (default). MySQL and SQL Server do not support deferrable foreign keys and for these databases such keys are generated commented out. Other foreign keys generated by the ODB compiler (such as the ones used to support containers and polymorphic hierarchies) are always generated as not deferrable. </dd>
<p> Note also that if you use either <code>not_deferrable</code> or <code>immediate</code> mode, then the order in which you persist, update, and erase objects within a transaction becomes important. </p>
<dt><code>&#8211;default-pointer</code> <i>ptr</i></dt>
<dd> Use <i>ptr</i> as the default pointer for persistent objects and views. Objects and views that do not have a pointer assigned with the <code>db pointer</code> pragma will use this pointer by default. The value of this option can be <code>*</code> which denotes the raw pointer and is the default, or qualified name of a smart pointer class template, for example, <code>std::auto_ptr</code>. In the latter case, the ODB compiler constructs the object or view pointer by adding a single template argument of the object or view type to the qualified name, for example <code>std::auto_ptr&lt;object&gt;</code>. The ODB runtime uses object and view pointers to return, and, in case of objects, pass and cache dynamically allocated instances of object and view types. </dd>
<p> Except for the raw pointer and the standard smart pointers defined in the <code>&lt;memory&gt;</code> header file, you are expected to include the definition of the default pointer at the beginning of the generated header file. There are two common ways to achieve this: you can either include the necessary header in the file being compiled or you can use the <code>&#8211;hxx-prologue</code> option to add the necessary <code>#include</code> directive to the generated code. </p>
<dt><code>&#8211;session-type</code> <i>type</i></dt>
<dd> Use <i>type</i> as the alternative session type instead of the default <code>odb::session</code>. This option can be used to specify a custom session implementation to be use by the persistent classes. Note that you will also need to include the definition of the custom session type into the generated header file. This is normally achieved with the <code>&#8211;hxx-prologue*</code> options. </dd>
<dt><code>&#8211;profile</code>|<code>-p</code> <i>name</i></dt>
<dd> Specify a profile that should be used during compilation. A profile is an options file. The ODB compiler first looks for a database-specific version with the name constructed by appending the <code>&#8211;</code><i>database</i><code>.options</code> suffix to <i>name</i>, where <i>database</i> is the database name as specified with the <code>&#8211;database</code> option. If this file is not found, then the ODB compiler looks for a database-independant version with the name constructed by appending just the <code>.options</code> suffix. </dd>
<p> The profile options files are searched for in the same set of directories as C++ headers included with the <code>#include &lt;&#8230;&gt;</code> directive (built-in paths plus those specified with the <code>-I</code> options). The options file is first searched for in the directory itself and then in its <code>odb/</code> subdirectory. </p>
<p> For the format of the options file refer to the <code>&#8211;options-file</code> option below. You can repeat this option to specify more than one profile. </p>
<dt><code>&#8211;at-once</code></dt>
<dd> Generate code for all the input files as well as for all the files that they include at once. The result is a single set of source/schema files that contain all the generated code. If more than one input file is specified together with this option, then the <code>&#8211;input-name</code> option must also be specified in order to provide the base name for the output files. In this case, the directory part of such a base name is used as the location of the combined file. This can be important for the <code>#include</code> directive resolution. </dd>
<dt><code>&#8211;schema</code> <i>schema</i></dt>
<dd> Specify a database schema (database namespace) that should be assigned to the persistent classes in the file being compiled. Database schemas are not to be confused with database schema names (schema catalog names) which are specified with the <code>&#8211;schema-name</code> option. </dd>
<dt><code>&#8211;export-symbol</code> <i>symbol</i></dt>
<dd> Insert <i>symbol</i> in places where DLL export/import control statements (<code>__declspec(dllexport/dllimport)</code>) are necessary. See also the <code>&#8211;extern-symbol</code> option below. </dd>
<dt><code>&#8211;extern-symbol</code> <i>symbol</i></dt>
<dd> If <i>symbol</i> is defined, insert it in places where a template instantiation must be declared <code>extern</code>. This option is normally used together with <code>&#8211;export-symbol</code> when both multi-database support and queries are enabled. </dd>
<dt><code>&#8211;std</code> <i>version</i></dt>
<dd> Specify the C++ standard that should be used during compilation. Valid values are <code>c++98</code> (default) and <code>c++11</code>. </dd>
<dt><code>&#8211;warn-hard-add</code></dt>
<dd> Warn about hard-added data members. </dd>
<dt><code>&#8211;warn-hard-delete</code></dt>
<dd> Warn about hard-deleted data members and persistent classes. </dd>
<dt><code>&#8211;warn-hard</code></dt>
<dd> Warn about both hard-added and hard-deleted data members and persistent classes. </dd>
<dt><code>&#8211;output-dir</code>|<code>-o</code> <i>dir</i></dt>
<dd> Write the generated files to <i>dir</i> instead of the current directory. </dd>
<dt><code>&#8211;input-name</code> <i>name</i></dt>
<dd> Use <i>name</i> instead of the input file to derive the names of the generated files. If the <code>&#8211;at-once</code> option is specified, then the directory part of <i>name</i> is used as the location of the combined file. Refer to the <code>&#8211;at-once</code> option for details. </dd>
<dt><code>&#8211;changelog</code> <i>file</i></dt>
<dd> Read/write changelog from/to <i>file</i> instead of the default changelog file. The default changelog file name is derived from the input file name and it is placed into the same directory as the input file. Note that the <code>&#8211;output-dir</code> option does not affect the changelog file location. In other words, by default, the changelog file is treated as another input rather than output even though the ODB compiler may modify it. Use the <code>&#8211;changelog-in</code> and <code>&#8211;changelog-out</code> options to specify different input and output chaneglog files. </dd>
<dt><code>&#8211;changelog-in</code> <i>file</i></dt>
<dd> Read changelog from <i>file</i> instead of the default changelog file. If this option is specified, then you must also specify the output chanegelog file with <code>&#8211;changelog-out</code>. </dd>
<dt><code>&#8211;changelog-out</code> <i>file</i></dt>
<dd> Write changelog to <i>file</i> instead of the default changelog file. If this option is specified, then you must also specify the input chanegelog file with <code>&#8211;changelog-in</code>. </dd>
<dt><code>&#8211;changelog-dir</code> <i>dir</i></dt>
<dd> Use <i>dir</i> instead of the input file directory as the changelog file directory. This directory is also added to changelog files specified with the <code>&#8211;changelog</code>, <code>&#8211;changelog-in</code>, and <code>&#8211;changelog-in</code> options unless they are absolute paths. </dd>
<dt><code>&#8211;init-changelog</code></dt>
<dd> Force re-initialization of the changelog even if one exists (all the existing change history will be lost). This option is primarily useful for automated testing. </dd>
<dt><code>&#8211;odb-file-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> to construct the names of the generated C++ files. In the single-database mode the default value for this option is <code>-odb</code>. In the multi-database mode it is <code>-odb</code> for the files corresponding to the <code>common</code> database and <code>-odb-</code><i>db</i> (where <i>db</i> is the database name) for other databases. </dd>
<dt><code>&#8211;sql-file-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> to construct the name of the generated schema SQL file. In the single-database mode by default no suffix is used. In the multi-database mode the default value for this option is <code>&#8211;</code><i>db</i> (where <i>db</i> is the database name). </dd>
<dt><code>&#8211;schema-file-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> to construct the name of the generated schema C++ source file. In the single-database mode the default value for this option is <code>-schema</code>. In the multi-database mode it is <code>-schema-</code><i>db</i> (where <i>db</i> is the database name). See the <code>&#8211;schema-format</code> option for details. </dd>
<dt><code>&#8211;changelog-file-suffix</code> <i>sfx</i></dt>
<dd> Use <i>sfx</i> to construct the name of the changelog file. In the single-database mode by default no suffix is used. In the multi-database mode the default value for this option is <code>&#8211;</code><i>db</i> (where <i>db</i> is the database name). </dd>
<dt><code>&#8211;hxx-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> instead of the default <code>.hxx</code> to construct the name of the generated C++ header file. </dd>
<dt><code>&#8211;ixx-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> instead of the default <code>.ixx</code> to construct the name of the generated C++ inline file. </dd>
<dt><code>&#8211;cxx-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> instead of the default <code>.cxx</code> to construct the name of the generated C++ source file. </dd>
<dt><code>&#8211;sql-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> instead of the default <code>.sql</code> to construct the name of the generated database schema file. </dd>
<dt><code>&#8211;changelog-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> instead of the default <code>.xml</code> to construct the name of the changelog file. </dd>
<dt><code>&#8211;hxx-prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of the generated C++ header file. </dd>
<dt><code>&#8211;ixx-prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of the generated C++ inline file. </dd>
<dt><code>&#8211;cxx-prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of the generated C++ source file. </dd>
<dt><code>&#8211;schema-prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of the generated schema C++ source file. </dd>
<dt><code>&#8211;sql-prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of the generated database schema file. </dd>
<dt><code>&#8211;migration-prologue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the beginning of the generated database migration file. </dd>
<dt><code>&#8211;sql-interlude</code> <i>text</i></dt>
<dd> Insert <i>text</i> after all the <code>DROP</code> and before any <code>CREATE</code> statements in the generated database schema file. </dd>
<dt><code>&#8211;hxx-epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of the generated C++ header file. </dd>
<dt><code>&#8211;ixx-epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of the generated C++ inline file. </dd>
<dt><code>&#8211;cxx-epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of the generated C++ source file. </dd>
<dt><code>&#8211;schema-epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of the generated schema C++ source file. </dd>
<dt><code>&#8211;sql-epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of the generated database schema file. </dd>
<dt><code>&#8211;migration-epilogue</code> <i>text</i></dt>
<dd> Insert <i>text</i> at the end of the generated database migration file. </dd>
<dt><code>&#8211;hxx-prologue-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> at the beginning of the generated C++ header file. </dd>
<dt><code>&#8211;ixx-prologue-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> at the beginning of the generated C++ inline file. </dd>
<dt><code>&#8211;cxx-prologue-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> at the beginning of the generated C++ source file. </dd>
<dt><code>&#8211;schema-prologue-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> at the beginning of the generated schema C++ source file. </dd>
<dt><code>&#8211;sql-prologue-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> at the beginning of the generated database schema file. </dd>
<dt><code>&#8211;migration-prologue-file</code> <i>f</i></dt>
<dd> Insert the content of file <i>f</i> at the beginning of the generated database migration file. </dd>
<dt><code>&#8211;sql-interlude-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> after all the <code>DROP</code> and before any <code>CREATE</code> statements in the generated database schema file. </dd>
<dt><code>&#8211;hxx-epilogue-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> at the end of the generated C++ header file. </dd>
<dt><code>&#8211;ixx-epilogue-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> at the end of the generated C++ inline file. </dd>
<dt><code>&#8211;cxx-epilogue-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> at the end of the generated C++ source file. </dd>
<dt><code>&#8211;schema-epilogue-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> at the end of the generated schema C++ source file. </dd>
<dt><code>&#8211;sql-epilogue-file</code> <i>file</i></dt>
<dd> Insert the content of <i>file</i> at the end of the generated database schema file. </dd>
<dt><code>&#8211;migration-epilogue-file</code> <i>f</i></dt>
<dd> Insert the content of file <i>f</i> at the end of the generated database migration file. </dd>
<dt><code>&#8211;odb-prologue</code> <i>text</i></dt>
<dd> Compile <i>text</i> before the input header file. This option allows you to add additional declarations, such as custom traits specializations, to the ODB compilation process. </dd>
<dt><code>&#8211;odb-prologue-file</code> <i>file</i></dt>
<dd> Compile <i>file</i> contents before the input header file. Prologue files are compiled after all the prologue text fragments (<code>&#8211;odb-prologue</code> option). </dd>
<dt><code>&#8211;odb-epilogue</code> <i>text</i></dt>
<dd> Compile <i>text</i> after the input header file. This option allows you to add additional declarations, such as custom traits specializations, to the ODB compilation process. </dd>
<dt><code>&#8211;odb-epilogue-file</code> <i>file</i></dt>
<dd> Compile <i>file</i> contents after the input header file. Epilogue files are compiled after all the epilogue text fragments (<code>&#8211;odb-epilogue</code> option). </dd>
<dt><code>&#8211;table-prefix</code> <i>prefix</i></dt>
<dd> Add <i>prefix</i> to table names and, for databases that have global index and/or foreign key names, to those names as well. The prefix is added to both names that were specified with the <code>db table</code> and <code>db index</code> pragmas and those that were automatically derived from class and data member names. If you require a separator, such as an underscore, between the prefix and the name, then you should include it into the prefix value. </dd>
<dt><code>&#8211;index-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> instead of the default <code>_i</code> to construct index names. The suffix is only added to names that were automatically derived from data member names. If you require a separator, such as an underscore, between the name and the suffix, then you should include it into the suffix value. </dd>
<dt><code>&#8211;fkey-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> instead of the default <code>_fk</code> to construct foreign key names. If you require a separator, such as an underscore, between the name and the suffix, then you should include it into the suffix value. </dd>
<dt><code>&#8211;sequence-suffix</code> <i>suffix</i></dt>
<dd> Use <i>suffix</i> instead of the default <code>_seq</code> to construct sequence names. If you require a separator, such as an underscore, between the name and the suffix, then you should include it into the suffix value. </dd>
<dt><code>&#8211;sql-name-case</code> <i>case</i></dt>
<dd> Convert all automatically-derived SQL names to upper or lower case. Valid values for this option are <code>upper</code> and <code>lower</code>. </dd>
<dt><code>&#8211;table-regex</code> <i>regex</i></dt>
<dd> Add <i>regex</i> to the list of regular expressions that is used to transform automatically-derived table names. See the SQL NAME TRANSFORMATIONS section below for details. </dd>
<dt><code>&#8211;column-regex</code> <i>regex</i></dt>
<dd> Add <i>regex</i> to the list of regular expressions that is used to transform automatically-derived column names. See the SQL NAME TRANSFORMATIONS section below for details. </dd>
<dt><code>&#8211;index-regex</code> <i>regex</i></dt>
<dd> Add <i>regex</i> to the list of regular expressions that is used to transform automatically-derived index names. See the SQL NAME TRANSFORMATIONS section below for details. </dd>
<dt><code>&#8211;fkey-regex</code> <i>regex</i></dt>
<dd> Add <i>regex</i> to the list of regular expressions that is used to transform automatically-derived foreign key names. See the SQL NAME TRANSFORMATIONS section below for details. </dd>
<dt><code>&#8211;sequence-regex</code> <i>regex</i></dt>
<dd> Add <i>regex</i> to the list of regular expressions that is used to transform automatically-derived sequence names. See the SQL NAME TRANSFORMATIONS section below for details. </dd>
<dt><code>&#8211;sql-name-regex</code> <i>regex</i></dt>
<dd> Add <i>regex</i> to the list of regular expressions that is used to transform all automatically-derived SQL names. See the SQL NAME TRANSFORMATIONS section below for details. </dd>
<dt><code>&#8211;sql-name-regex-trace</code></dt>
<dd> Trace the process of applying regular expressions specified with the SQL name <code>&#8211;*-regex</code> options. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </dd>
<dt><code>&#8211;accessor-regex</code> <i>regex</i></dt>
<dd> Add <i>regex</i> to the list of regular expressions used to transform data member names to function names when searching for a suitable accessor function. The argument to this option is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code> and the delimiter can be escaped inside <i>pattern</i> and <i>replacement</i> with a backslash (<code>\</code>). You can specify multiple regular expressions by repeating this option. </dd>
<p> All the regular expressions are tried in the order specified and the first expression that produces a suitable accessor function is used. Each expression is tried twice: first with the actual member name and then with the member&#8217;s <i>public name</i> which is obtained by removing the common member name decorations, such as leading and trailing underscores, the <code>m_</code> prefix, etc. The ODB compiler also includes a number of built-in expressions for commonly used accessor names, such as <code>get_foo</code>, <code>getFoo</code>, <code>getfoo</code>, and just <code>foo</code>. The built-in expressions are tried last. </p>
<p> As an example, the following expression transforms data members with public names in the form <code>foo</code> to accessor names in the form <code>GetFoo</code>: </p>
<p> <code>/(.+)/Get</code>\u$1/</code> </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
<dt><code>--accessor-regex-trace</code></dt>
<dd> <p> Trace the process of applying regular expressions specified with the <code>--accessor-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </p>
 </dd>
<dt><code>--modifier-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to transform data member names to function names when searching for a suitable modifier function. The argument to this option is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code> and the delimiter can be escaped inside <i>pattern</i> and <i>replacement</i> with a backslash (<code>\</code>). You can specify multiple regular expressions by repeating this option. </p>
<p> All the regular expressions are tried in the order specified and the first expression that produces a suitable modifier function is used. Each expression is tried twice: first with the actual member name and then with the member&#8217;s <i>public name</i> which is obtained by removing the common member name decorations, such as leading and trailing underscores, the <code>m_</code> prefix, etc. The ODB compiler also includes a number of built-in expressions for commonly used modifier names, such as <code>set_foo</code>, <code>setFoo</code>, <code>setfoo</code>, and just <code>foo</code>. The built-in expressions are tried last. </p>
<p> As an example, the following expression transforms data members with public names in the form <code>foo</code> to modifier names in the form <code>SetFoo</code>: </p>
<p> <code>/(.+)/Set\u$1/</code> </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
 </dd>
<dt><code>--modifier-regex-trace</code></dt>
<dd> <p> Trace the process of applying regular expressions specified with the <code>--modifier-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </p>
 </dd>
<dt><code>--include-with-brackets</code></dt>
<dd> <p> Use angle brackets (&lt;&gt;) instead of quotes (&quot;&quot;) in the generated <code>#include</code> directives. </p>
 </dd>
<dt><code>--include-prefix</code><i>prefix</i></dt>
<dd> <p> Add <i>prefix</i> to the generated <code>#include</code> directive paths. </p>
 </dd>
<dt><code>--include-regex</code><i>regex</i></dt>
<dd> <p> Add <i>regex</i> to the list of regular expressions used to transform generated <code>#include</code> directive paths. The argument to this option is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code> and the delimiter can be escaped inside <i>pattern</i> and <i>replacement</i> with a backslash (<code>\</code>). You can specify multiple regular expressions by repeating this option. All the regular expressions are tried in the order specified and the first expression that matches is used. </p>
<p> As an example, the following expression transforms include paths in the form <code>foo/bar-odb.h</code> to paths in the form <code>foo/generated/bar-odb.h</code>: </p>
<p> <code>%foo/(.+)-odb.h%foo/generated/$1-odb.h%</code> </p>
<p> See also the REGEX AND SHELL QUOTING section below. </p>
 </dd>
<dt><code>--include-regex-trace</code></dt>
<dd> <p> Trace the process of applying regular expressions specified with the <code>--include-regex</code> option. Use this option to find out why your regular expressions don&#8217;t do what you expected them to do. </p>
 </dd>
<dt><code>--guard-prefix</code><i>prefix</i></dt>
<dd> <p> Add <i>prefix</i> to the generated header inclusion guards. The prefix is transformed to upper case and characters that are illegal in a preprocessor macro name are replaced with underscores. </p>
 </dd>
<dt><code>--show-sloc</code></dt>
<dd> <p> Print the number of generated physical source lines of code (SLOC). </p>
 </dd>
<dt><code>--sloc-limit</code><i>num</i></dt>
<dd> <p> Check that the number of generated physical source lines of code (SLOC) does not exceed <i>num</i>. </p>
 </dd>
<dt><code>--options-file</code><i>file</i></dt>
<dd> <p> Read additional options from <i>file</i> with each option appearing on a separate line optionally followed by space and an option value. Empty lines and lines starting with <code>#</code> are ignored. Option values can be enclosed in double (<code>&quot;</code>) or single (<code>&#8216;</code>) quotes to preserve leading and trailing whitespaces as well as to specify empty values. If the value itself contains trailing or leading quotes, enclose it with an extra pair of quotes, for example <code>&#8216;&quot;x&quot;&#8216;</code>. Non-leading and non-trailing quotes are interpreted as being part of the option value. </p>
<p> The semantics of providing options in a file is equivalent to providing the same set of options in the same order on the command line at the point where the <code>--options-file</code> option is specified except that the shell escaping and quoting is not required. You can repeat this option to specify more than one options file. </p>
 </dd>
<dt><code>-x</code><i>option</i></dt>
<dd> <p> Pass <i>option</i> to the underlying C++ compiler (<code>g++</code>). The <i>option</i> value that doesn&#8217;t start with <code>-</code> is considered the <code>g++</code> executable name. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Print the commands executed to run the stages of compilation. </p>
 </dd>
<dt><code>--trace</code></dt>
<dd> <p> Trace the compilation process. </p>
 </dd>
<dt><code>--mysql-engine</code><i>engine</i></dt>
<dd> <p> Use <i>engine</i> instead of the default <code>InnoDB</code> in the generated database schema file. For more information on the storage engine options see the MySQL documentation. If you would like to use the database-default engine, pass <code>default</code> as the value for this option. </p>
 </dd>
<dt><code>--sqlite-override-null</code></dt>
<dd> <p> Make all columns in the generated database schema allow <code>NULL</code> values. This is primarily useful in schema migration since SQLite does not support dropping of columns. By making all columns <code>NULL</code> we can later &quot;delete&quot; them by setting their values to <code>NULL</code>. Note that this option overrides even the <code>not_null</code> pragma. </p>
 </dd>
<dt><code>--sqlite-lax-auto-id</code></dt>
<dd> <p> Do not force monotonically increasing automatically-assigned object ids. In this mode the generated database schema omits the <code>AUTOINCREMENT</code> keyword which results in faster object persistence but may lead to automatically-assigned ids not being in a strictly ascending order. Refer to the SQLite documentation for details. </p>
 </dd>
<dt><code>--pgsql-server-version</code><i>ver</i></dt>
<dd> <p> Specify the minimum PostgreSQL server version with which the generated C++ code and schema will be used. This information is used to enable version-specific optimizations and workarounds in the generated C++ code and schema. The version must be in the <i>major</i><code>.</code><i>minor</i> form, for example, <code>9.1</code>. If this option is not specified, then <code>7.4</code> or later is assumed. </p>
 </dd>
<dt><code>--oracle-client-version</code><i>ver</i></dt>
<dd> <p> Specify the minimum Oracle client library (OCI) version with which the generated C++ code will be linked. This information is used to enable version-specific optimizations and workarounds in the generated C++ code. The version must be in the <i>major</i><code>.</code><i>minor</i> form, for example, <code>11.2</code>. If this option is not specified, then <code>10.1</code> or later is assumed. </p>
 </dd>
<dt><code>--mssql-server-version</code><i>ver</i></dt>
<dd> <p> Specify the minimum SQL Server server version with which the generated C++ code and schema will be used. This information is used to enable version-specific optimizations and workarounds in the generated C++ code and schema. The version must be in the <i>major</i><code>.</code><i>minor</i> form, for example, <code>9.0</code> (SQL Server 2005), <code>10.5</code> (2008R2), or <code>11.0</code> (2012). If this option is not specified, then <code>10.0</code> (SQL Server 2008) or later is assumed. </p>
 </dd>
<dt><code>--mssql-short-limit</code><i>size</i></dt>
<dd> <p> Specify the short data size limit. If a character, national character, or binary data type has a maximum length (in bytes) less than or equal to this limit, then it is treated as <i>short data</i>, otherwise it is <i>long data</i>. For short data ODB pre-allocates an intermediate buffer of the maximum size and binds it directly to a parameter or result column. This way the underlying API (ODBC) can read/write directly from/to this buffer. In the case of long data, the data is read/written in chunks using the <code>SQLGetData()</code>/<code>SQLPutData()</code> ODBC functions. While the long data approach reduces the amount of memory used by the application, it may require greater CPU resources. The default short data limit is 1024 bytes. When setting a custom short data limit, make sure that it is sufficiently large so that no object id in the application is treated as long data. </p>
 </dd></dl>
<h2>SQL NAME TRANSFORMATIONS</h2>
<p> The ODB compiler provides a number of mechanisms for transforming automatically-derived SQL names, such as tables, columns, etc., to match a specific naming convention. At the higher level, we can add a prefix to global names (tables and, for some databases, indexes and/or foreign keys) with the <code>--table-prefix</code> option. Similarly, we can specify custom suffixes for automatically-derived index (<code>--index-suffix</code>; default is <code>_i</code>), foreign key (<code>--fkey-suffix</code>; default is <code>_fk</code>), and sequence (<code>--sequence-suffix</code>; default is <code>_seq</code>) names. Finally, we can also convert all the names to upper or lower case with the <code>--sql-name-case</code> option (valid values are <code>upper</code> and <code>lower</code>). </p>
<p> At the lower level we can specify a set of regular expressions to implement arbitrary transformations of the automatically-derived SQL names. If we want a particular regular expression only to apply to a specific name, for example, table or column, then we use one of the <code>--</code><i>kind</i><code>-regex</code> options, where <i>kind</i> can be <code>table</code>, <code>column</code>, <code>index</code>, <code>fkey</code>, or <code>sequence</code>. On the other hand, if we want our regular expressions to apply to all SQL names, then we use the <code>--sql-name-regex</code> option. </p>
<p> The interaction between the higher and lower level transformations is as follows. Prefixes and suffixes are added first. Then the regular expression transformations are applied. Finally, if requested, the name is converted to upper or lower case. Note also that all of these transformations except for <code>--table-prefix</code> only apply to automatically-derived names. In other words, if a table, column, etc., name was explicitly specified with a pragma, then it is used as is, without applying any (except for the table prefix) transformations. </p>
<p> The value for the <code>--*-regex</code> options is a Perl-like regular expression in the form <code>/</code><i>pattern</i><code>/</code><i>replacement</i><code>/</code>. Any character can be used as a delimiter instead of <code>/</code> and the delimiter can be escaped inside <i>pattern</i> and <i>replacement</i> with a backslash (<code>\</code>). You can also specify multiple regular expressions by repeating these options. </p>
<p> All the regular expressions are tried in the order specified with the name-specific expressions (for example, <code>--table-regex)</code> tried first followed by the generic expressions (<code>--sql-name-regex</code>). The first expression that matches is used. </p>
<p> As an example, consider a regular expression that transforms a class name in the form <code>CFoo</code> to a table name in the form <code>FOO:</code> </p>
<p> <code>--table-regex &#8216;/C(.+)/\U$1/&#8216;</code> </p>
<p> As a more interesting example, consider the transformation of class names that follow the upper camel case convention (for example, <code>FooBar</code>) to table names that follow the underscore-separated, all upper case convention (for example, <code>FOO_BAR</code>). For this case we have to use separate expressions to handle one-word, two-word, etc., names: </p>
<p> <code>--table-regex &#8216;/([A-z][a-z]+)/\U$1/&#8216;</code> </p>
<p> <code>--table-regex &#8216;/([A-z][a-z]+)([A-z][a-z]+)/\U$1_$2/&#8216;</code> </p>
<p> See also the REGEX AND SHELL QUOTING section below.  </p>
<h2>REGEX AND SHELL QUOTING</h2>
<p> When entering a regular expression argument in the shell command line it is often necessary to use quoting (enclosing the argument in &quot; &quot; or &#8216; &#8216;) in order to prevent the shell from interpreting certain characters, for example, spaces as argument separators and $ as variable expansions. </p>
<p> Unfortunately it is hard to achieve this in a manner that is portable across POSIX shells, such as those found on GNU/Linux and UNIX, and Windows shell. For example, if you use &quot; &quot; for quoting you will get a wrong result with POSIX shells if your expression contains $. The standard way of dealing with this on POSIX systems is to use &#8216; &#8216; instead. Unfortunately, Windows shell does not remove &#8216; &#8216; from arguments when they are passed to applications. As a result you may have to use &#8216; &#8216; for POSIX and &quot; &quot; for Windows ($ is not treated as a special character on Windows). </p>
<p> Alternatively, you can save regular expression options into a file, one option per line, and use this file with the <code>--options-file</code> option. With this approach you don&#8217;t need to worry about shell quoting.  </p>
<h2>DIAGNOSTICS</h2>
<p> If the input file is not valid C++, <code>odb</code> will issue diagnostic messages to STDERR and exit with non-zero exit code.  </p>
<h2>BUGS</h2>
<p> Send bug reports to the odb-users [at] codesynthesis.com mailing list.  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2009-2013 Code Synthesis Tools CC. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, version 1.2; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. Copy of the license can be obtained from <a rel="nofollow" href="http://www.codesynthesis.com/licenses/fdl-1.3.txt">http://www.codesynthesis.com/licenses/fdl-1.3.txt</a> </p>
