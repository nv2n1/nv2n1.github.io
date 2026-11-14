---
title: "ccache(1)"
name: "ccache"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ccache/"
description: "ccache – a fast C/C++ compiler cache"
---

<h2 class="name">NAME</h2>
<p> ccache &#8211; a fast C/C++ compiler cache </p>
<h2>SYNOPSIS</h2>
<pre><code>
ccache[options] ccache compiler[compiler options] compiler[compiler options](via symbolic link)
</code></pre>
<h2>DESCRIPTION</h2>
<p> ccache is a compiler cache. It speeds up recompilation by caching the result of previous compilations and detecting when the same compilation is being done again. Supported languages are C, C++, Objective-C and Objective-C++. </p>
<p> ccache has been carefully written to always produce exactly the same compiler output that you would get without the cache. The only way you should be able to tell that you are using ccache is the speed. Currently known exceptions to this goal are listed under BUGS. If you ever discover an undocumented case where ccache changes the output of your compiler, please let us know.</p>
<h3>Features</h3>
<dl>
<dt>
<dd> &bull; Keeps statistics on hits/misses.</dl>
<dl>
<dt>
<dd> &bull; Automatic cache size management.</dl>
<dl>
<dt>
<dd> &bull; Can cache compilations that generate warnings.</dl>
<dl>
<dt>
<dd> &bull; Easy installation.</dl>
<dl>
<dt>
<dd> &bull; Low overhead.</dl>
<dl>
<dt>
<dd> &bull; Optionally uses hard links where possible to avoid copies.</dl>
<dl>
<dt>
<dd> &bull; Optionally compresses files in the cache to reduce disk space.</dl>
<h3>Limitations</h3>
<dl>
<dt>
<dd> &bull; Only knows how to cache the compilation of a single C/C++/Objective-C/Objective-C++ file. Other types of compilations (multi-file compilation, linking, etc) will silently fall back to running the real compiler.</dl>
<dl>
<dt>
<dd> &bull; Only works with GCC and compilers that behave similar enough.</dl>
<dl>
<dt>
<dd> &bull; Some compiler flags are not supported. If such a flag is detected, ccache will silently fall back to running the real compiler.</dl>
<h2>RUN MODES</h2>
<p> There are two ways to use ccache. You can either prefix your compilation commands with <code>ccache</code> or you can let ccache masquerade as the compiler by creating a symbolic link (named as the compiler) to ccache. The first method is most convenient if you just want to try out ccache or wish to use it for some specific projects. The second method is most useful for when you wish to use ccache for all your compilations. </p>
<p> To use the first method, just make sure that <code>ccache</code> is in your <code>PATH</code>. </p>
<p> To use the symlinks method, do something like this: </p>
<dl>
<dt>
<dd>
<pre>
cp ccache /usr/local/bin/
ln -s ccache /usr/local/bin/gcc
ln -s ccache /usr/local/bin/g++
ln -s ccache /usr/local/bin/cc
ln -s ccache /usr/local/bin/c++
</pre>
</dl>
<p> And so forth. This will work as long as the directory with symlinks comes before the path to the compiler (which is usually in /usr/bin). After installing you may wish to run &#8220;which gcc&#8221; to make sure that the correct link is being used. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font> </p>
<p> The technique of letting ccache masquerade as the compiler works well, but currently doesn&#8217;t interact well with other tools that do the same thing. See USING CCACHE WITH OTHER COMPILER WRAPPERS. </p>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font> </p>
<p> Do not use a hard link, use a symbolic link. A hard link will cause &#8220;interesting&#8221; problems. </p>
</dl>
<h2>OPTIONS</h2>
<p> These options only apply when you invoke ccache as &#8220;ccache&#8221;. When invoked as a compiler (via a symlink as described in the previous section), the normal compiler options apply and you should refer to the compiler&#8217;s documentation. </p>
<p> <code>-c, &#8211;cleanup</code></p>
<dl>
<dt>
<dd> Clean up the cache by removing old cached files until the specified file number and cache size limits are not exceeded. This also recalculates the cache file count and size totals. Normally, there is no need to initiate cleanup manually as ccache keeps the cache below the specified limits at runtime and keeps statistics up to date on each compilation. Forcing a cleanup is mostly useful if you manually modify the cache contents or believe that the cache size statistics may be inaccurate.</dl>
<p> <code>-C, &#8211;clear</code></p>
<dl>
<dt>
<dd> Clear the entire cache, removing all cached files, but keeping the configuration file.</dl>
<p> <code>-F, &#8211;max-files</code>=<i>N</i></p>
<dl>
<dt>
<dd> Set the maximum number of files allowed in the cache. Use 0 for no limit. The value is stored in a configuration file in the cache directory and applies to all future compilations.</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Print an options summary page.</dl>
<p> <code>-M, &#8211;max-size</code>=<i>SIZE</i></p>
<dl>
<dt>
<dd> Set the maximum size of the files stored in the cache. <i>SIZE</i> should be a number followed by an optional suffix: k, M, G, T (decimal), Ki, Mi, Gi or Ti (binary). The default suffix is G. Use 0 for no limit. The value is stored in a configuration file in the cache directory and applies to all future compilations.</dl>
<p> <code>-o, &#8211;set-config</code>=<i>KEY=VALUE</i></p>
<dl>
<dt>
<dd> Set configuration <i>KEY</i> to <i>VALUE</i>. See CONFIGURATION for more information.</dl>
<p> <code>-p, &#8211;print-config</code></p>
<dl>
<dt>
<dd> Print current configuration options and from where they originate (environment variable, configuration file or compile-time default).</dl>
<p> <code>-s, &#8211;show-stats</code></p>
<dl>
<dt>
<dd> Print the current statistics summary for the cache.</dl>
<p> <code>-V, &#8211;version</code></p>
<dl>
<dt>
<dd> Print version and copyright information.</dl>
<p> <code>-z, &#8211;zero-stats</code></p>
<dl>
<dt>
<dd> Zero the cache statistics (but not the configuration options).</dl>
<h2>EXTRA OPTIONS</h2>
<p> When run as a compiler, ccache usually just takes the same command line options as the compiler you are using. The only exception to this is the option <code>&#8211;ccache-skip</code>. That option can be used to tell ccache to avoid interpreting the next option in any way and to pass it along to the compiler as-is. <code>Note</code>: <code>&#8211;ccache-skip</code> currently only tells ccache not to interpret the next option as a special compiler option &#8212; the option will still be included in the direct mode hash. </p>
<p> The reason this can be important is that ccache does need to parse the command line and determine what is an input filename and what is a compiler option, as it needs the input filename to determine the name of the resulting object file (among other things). The heuristic ccache uses when parsing the command line is that any argument that exists as a file is treated as an input file name. By using <code>&#8211;ccache-skip</code> you can force an option to not be treated as an input file name and instead be passed along to the compiler as a command line option. </p>
<p> Another case where <code>&#8211;ccache-skip</code> can be useful is if ccache interprets an option specially but shouldn&#8217;t, since the option has another meaning for your compiler than what ccache thinks.</p>
<h2>CONFIGURATION</h2>
<p> ccache&#8217;s default behavior can be overridden by configuration file settings, which in turn can be overridden by environment variables with names starting with <code>CCACHE_</code>. ccache normally reads configuration from two files: first a system-level configuration file and secondly a cache-specific configuration file. The priority of configuration settings is as follows (where 1 is highest): </p>
<dl>
<dt>
<dd> 1. Environment variables.</dl>
<dl>
<dt>
<dd> 2. The cache-specific configuration file <code>&lt;ccachedir&gt;/ccache.conf</code> (typically <code>$HOME/.ccache/ccache.conf</code>).</dl>
<dl>
<dt>
<dd> 3. The system-wide configuration file <code>&lt;sysconfdir&gt;/ccache.conf</code> (typically <code>/etc/ccache.conf</code> or <code>/usr/local/etc/ccache.conf</code>).</dl>
<dl>
<dt>
<dd> 4. Compile-time defaults.</dl>
<p> As a special case, if the environment variable <code>CCACHE_CONFIGPATH</code> is set, ccache reads configuration from the specified path instead of the default paths.</p>
<h3>Configuration file syntax</h3>
<p> Configuration files are in a simple &#8220;key = value&#8221; format, one setting per line. Lines starting with a hash sign are comments. Blank lines are ignored, as is whitespace surrounding keys and values. Example: </p>
<dl>
<dt>
<dd>
<pre>
# Set maximum cache size to 10 GB:
max_size = 10G
</pre>
</dl>
<h3>Boolean values</h3>
<p> Some settings are boolean values (i.e. truth values). In a configuration file, such values must be set to the string <code>true</code> or <code>false</code>. For the corresponding environment variables, the semantics are a bit different: a set environment variable means &#8220;true&#8221; regardless of the value (even if set to the empty string), and an unset environment variable means &#8220;false&#8221;. Each boolean environment variable also has a negated form starting with <code>CCACHE_NO</code>. For example, <code>CCACHE_COMPRESS</code> can be set to force compression and <code>CCACHE_NOCOMPRESS</code> can be set to force no compression.</p>
<h3>Configuration settings</h3>
<p> Below is a list of available configuration settings. The corresponding environment variable name is indicated in parentheses after each configuration setting key. </p>
<p> <code>base_dir</code> (<code>CCACHE_BASEDIR</code>)</p>
<dl>
<dt>
<dd> This setting should be an absolute path to a directory. ccache then rewrites absolute paths into relative paths before computing the hash that identifies the compilation, but only for paths under the specified directory. If set to the empty string (which is the default), no rewriting is done. See also the discussion under COMPILING IN DIFFERENT DIRECTORIES.</dl>
<p> <code>cache_dir</code> (<code>CCACHE_DIR</code>)</p>
<dl>
<dt>
<dd> This setting specifies where ccache will keep its cached compiler outputs. It will only take effect if set in the system-wide configuration file or as an environment variable. The default is <code>$HOME/.ccache</code>.</dl>
<p> <code>cache_dir_levels</code> (<code>CCACHE_NLEVELS</code>)</p>
<dl>
<dt>
<dd> This setting allows you to choose the number of directory levels in the cache directory. The default is 2. The minimum is 1 and the maximum is 8.</dl>
<p> <code>compiler</code> (<code>CCACHE_CC</code>)</p>
<dl>
<dt>
<dd> This setting can be used to force the name of the compiler to use. If set to the empty string (which is the default), ccache works it out from the command line.</dl>
<p> <code>compiler_check</code> (<code>CCACHE_COMPILERCHECK</code>)</p>
<dl>
<dt>
<dd> By default, ccache includes the modification time (&#8220;mtime&#8221;) and size of the compiler in the hash to ensure that results retrieved from the cache are accurate. This setting can be used to select another strategy. Possible values are: </p>
<p> <code>content</code></p>
<dl>
<dt>
<dd> Hash the content of the compiler binary. This makes ccache very slightly slower compared to the <code>mtime</code> setting, but makes it cope better with compiler upgrades during a build bootstrapping process.</dl>
<p> <code>mtime</code></p>
<dl>
<dt>
<dd> Hash the compiler&#8217;s mtime and size, which is fast. This is the default.</dl>
<p> <code>none</code></p>
<dl>
<dt>
<dd> Don&#8217;t hash anything. This may be good for situations where you can safely use the cached results even though the compiler&#8217;s mtime or size has changed (e.g. if the compiler is built as part of your build system and the compiler&#8217;s source has not changed, or if the compiler only has changes that don&#8217;t affect code generation). You should only use the <code>none</code> setting if you know what you are doing.</dl>
<p> <code>string:value</code></p>
<dl>
<dt>
<dd> Use <code>value</code> as the string to calculate hash from. This can be the compiler revision number you retrieved earlier and set here via environment variable.</dl>
<p> <i>a command string</i></p>
<dl>
<dt>
<dd> Hash the standard output and standard error output of the specified command. The string will be split on whitespace to find out the command and arguments to run. No other interpretation of the command string will be done, except that the special word <code>%compiler%</code> will be replaced with the path to the compiler. Several commands can be specified with semicolon as separator. Examples: </p>
<dl>
<dt>
<dd> &bull; %compiler% -v</dl>
<dl>
<dt>
<dd> &bull; %compiler% -dumpmachine; %compiler% -dumpversion</dl>
<p> You should make sure that the specified command is as fast as possible since it will be run once for each ccache invocation. </p>
<p> Identifying the compiler using a command is useful if you want to avoid cache misses when the compiler has been rebuilt but not changed. </p>
<p> Another case is when the compiler (as seen by ccache) actually isn&#8217;t the real compiler but another compiler wrapper &#8212; in that case, the default <code>mtime</code> method will hash the mtime and size of the other compiler wrapper, which means that ccache won&#8217;t be able to detect a compiler upgrade. Using a suitable command to identify the compiler is thus safer, but it&#8217;s also slower, so you should consider continue using the <code>mtime</code> method in combination with the <code>prefix_command</code> setting if possible. See USING CCACHE WITH OTHER COMPILER WRAPPERS.</dl>
</dl>
<p> <code>compression</code> (<code>CCACHE_COMPRESS</code> or <code>CCACHE_NOCOMPRESS</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> If true, ccache will compress object files and other compiler output it puts in the cache. However, this setting has no effect on how files are retrieved from the cache; compressed and uncompressed results will still be usable regardless of this setting. The default is false.</dl>
<p> <code>compression_level</code> (<code>CCACHE_COMPRESSLEVEL</code>)</p>
<dl>
<dt>
<dd> This setting determines the level at which ccache will compress object files. It only has effect if <code>compression</code> is enabled. The value defaults to 6, and must be no lower than 1 (fastest, worst compression) and no higher than 9 (slowest, best compression).</dl>
<p> <code>cpp_extension</code> (<code>CCACHE_EXTENSION</code>)</p>
<dl>
<dt>
<dd> This setting can be used to force a certain extension for the intermediate preprocessed file. The default is to automatically determine the extension to use for intermediate preprocessor files based on the type of file being compiled, but that sometimes doesn&#8217;t work. For example, when using the &#8220;aCC&#8221; compiler on HP-UX, set the cpp extension to <code>i</code>.</dl>
<p> <code>direct_mode</code> (<code>CCACHE_DIRECT</code> or <code>CCACHE_NODIRECT</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> If true, the direct mode will be used. The default is true. See THE DIRECT MODE.</dl>
<p> <code>disable</code> (<code>CCACHE_DISABLE</code> or <code>CCACHE_NODISABLE</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> When true, ccache will just call the real compiler, bypassing the cache completely. The default is false.</dl>
<p> <code>extra_files_to_hash</code> (<code>CCACHE_EXTRAFILES</code>)</p>
<dl>
<dt>
<dd> This setting is a list of paths to files that ccache will include in the the hash sum that idetifies the build. The list separator is semicolon on Windows systems and colon on other systems.</dl>
<p> <code>hard_link</code> (<code>CCACHE_HARDLINK</code> or <code>CCACHE_NOHARDLINK</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> If true, ccache will attempt to use hard links from the cache directory when creating the compiler output rather than using a file copy. Using hard links may be slightly faster in some situations, but can confuse programs like &#8220;make&#8221; that rely on modification times. Another thing to keep in mind is that if the resulting object file is modified in any way, this corrupts the cached object file as well. Hard links are never made for compressed cache files. This means that you should not enable compression if you want to use hard links. The default is false.</dl>
<p> <code>hash_dir</code> (<code>CCACHE_HASHDIR</code> or <code>CCACHE_NOHASHDIR</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> If true, ccache will include the current working directory in the hash that is used to distinguish two compilations. This prevents a problem with the storage of the current working directory in the debug info of an object file, which can lead ccache to give a cached object file that has the working directory in the debug info set incorrectly. This option is off by default as the incorrect setting of this debug info rarely causes problems. If you strike problems with GDB not using the correct directory then enable this option.</dl>
<p> <code>log_file</code> (<code>CCACHE_LOGFILE</code>)</p>
<dl>
<dt>
<dd> If set to a file path, ccache will write information on what it is doing to the specified file. This is useful for tracking down problems.</dl>
<p> <code>max_files</code> (<code>CCACHE_MAXFILES</code>)</p>
<dl>
<dt>
<dd> This option specifies the maximum number of files to keep in the cache. Use 0 for no limit (which is the default).</dl>
<p> <code>max_size</code> (<code>CCACHE_MAXSIZE</code>)</p>
<dl>
<dt>
<dd> This option specifies the maximum size of the cache. Use 0 for no limit. The default value is 5G. Available suffixes: k, M, G, T (decimal) and Ki, Mi, Gi, Ti (binary). The default suffix is &quot;G&quot;.</dl>
<p> <code>path</code> (<code>CCACHE_PATH</code>)</p>
<dl>
<dt>
<dd> If set, ccache will search directories in this list when looking for the real compiler. The list separator is semicolon on Windows systems and colon on other systems. If not set, ccache will look for the first executable matching the compiler name in the normal <code>PATH</code> that isn&#8217;t a symbolic link to ccache itself.</dl>
<p> <code>prefix_command</code> (<code>CCACHE_PREFIX</code>)</p>
<dl>
<dt>
<dd> This option adds a list of prefixes (separated by space) to the command line that ccache uses when invoking the compiler. See also USING CCACHE WITH OTHER COMPILER WRAPPERS.</dl>
<p> <code>read_only</code> (<code>CCACHE_READONLY</code> or <code>CCACHE_NOREADONLY</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> If true, ccache will attempt to use existing cached object files, but it will not to try to add anything new to the cache. If you are using this because your ccache directory is read-only, then you need to set <code>temporary_dir</code> as otherwise ccache will fail to create temporary files.</dl>
<p> <code>read_only_direct</code> (<code>CCACHE_READONLY_DIRECT</code> or <code>CCACHE_NOREADONLY_DIRECT</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> Just like <code>read_only</code> except that ccache will only try to retrieve results from the cache using the direct mode, not the preprocessor mode. See documentation for <code>read_only</code> regarding using a read-only ccache directory.</dl>
<p> <code>recache</code> (<code>CCACHE_RECACHE</code> or <code>CCACHE_NORECACHE</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> If true, ccache will not use any previously stored result. New results will still be cached, possibly overwriting any pre-existing results.</dl>
<p> <code>run_second_cpp</code> (<code>CCACHE_CPP2</code> or <code>CCACHE_NOCPP2</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> If true, ccache will not use the optimisation of avoiding the second call to the preprocessor by compiling the preprocessed output that was used for finding the hash in the case of a cache miss. This is primarily a debugging option, although it is possible that some unusual compilers will have problems with compiling the preprocessed output, in which case this option could allow ccache to be used anyway.</dl>
<p> <code>sloppiness</code> (<code>CCACHE_SLOPPINESS</code>)</p>
<dl>
<dt>
<dd> By default, ccache tries to give as few false cache hits as possible. However, in certain situations it&#8217;s possible that you know things that ccache can&#8217;t take for granted. This setting makes it possible to tell ccache to relax some checks in order to increase the hit rate. The value should be a comma-separated string with options. Available options are: </p>
<p> <code>file_macro</code></p>
<dl>
<dt>
<dd> Ignore <code>__FILE__</code> being present in the source.</dl>
<p> <code>file_stat_matches</code></p>
<dl>
<dt>
<dd> ccache normally examines a file&#8217;s contents to determine whether it matches the cached version. With this option set, ccache will consider a file as matching its cached version if the sizes, mtimes and ctimes match.</dl>
<p> <code>include_file_ctime</code></p>
<dl>
<dt>
<dd> By default, ccache also will not cache a file if it includes a header whose ctime is too new. This option disables that check.</dl>
<p> <code>include_file_mtime</code></p>
<dl>
<dt>
<dd> By default, ccache will not cache a file if it includes a header whose mtime is too new. This option disables that check.</dl>
<p> <code>pch_defines</code></p>
<dl>
<dt>
<dd> Be sloppy about #defines when precompiling a header file. See PRECOMPILED HEADERS for more information.</dl>
<p> <code>time_macros</code></p>
<dl>
<dt>
<dd> Ignore <code>__DATE__</code> and <code>__TIME__</code> being present in the source code.</dl>
<p> See the discussion under TROUBLESHOOTING for more information.</dl>
<p> <code>stats</code> (<code>CCACHE_STATS</code> or <code>CCACHE_NOSTATS</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> If true, ccache will update the statistics counters on each compilation. The default is true.</dl>
<p> <code>temporary_dir</code> (<code>CCACHE_TEMPDIR</code>)</p>
<dl>
<dt>
<dd> This setting specifies where ccache will put temporary files. The default is <code>&lt;cache_dir&gt;/tmp</code>. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 In previous versions of ccache, <code>CCACHE_TEMPDIR</code> had to be on the same filesystem as the <code>CCACHE_DIR</code> path, but this requirement has been relaxed.) </p>
</dl>
</dl>
<p> <code>umask</code> (<code>CCACHE_UMASK</code>)</p>
<dl>
<dt>
<dd> This setting specifies the umask for ccache and all child processes (such as the compiler). This is mostly useful when you wish to share your cache with other users. Note that this also affects the file permissions set on the object files created from your compilations.</dl>
<p> <code>unify</code> (<code>CCACHE_UNIFY</code> or <code>CCACHE_NOUNIFY</code>, see Boolean values above)</p>
<dl>
<dt>
<dd> If true, ccache will use a C/C++ unifier when hashing the preprocessor output if the <code>-g</code> option is not used. The unifier is slower than a normal hash, so setting this environment variable loses a little bit of speed, but it means that ccache can take advantage of not recompiling when the changes to the source code consist of reformatting only. Note that enabling the unifier changes the hash, so cached compilations produced when the unifier is enabled cannot be reused when the unifier is disabled, and vice versa. Enabling the unifier may result in incorrect line number information in compiler warning messages and expansions of the <code>__LINE__</code> macro. Also note that enabling the unifier implies turning off the direct mode.</dl>
<h2>CACHE SIZE MANAGEMENT</h2>
<p> By default, ccache has a five gigabyte limit on the total size of files in the cache and no maximum number of files. You can set different limits using the <code>-M</code>/<code>&#8211;max-size</code> and <code>-F</code>/<code>&#8211;max-files</code> options. Use <code>ccache -s/&#8211;show-stats</code> to see the cache size and the currently configured limits (in addition to other various statistics).</p>
<h2>CACHE COMPRESSION</h2>
<p> ccache can optionally compress all files it puts into the cache using the compression library zlib. While this may involve a tiny performance slowdown, it increases the number of files that fit in the cache. You can turn on compression with the <code>compression</code> configuration setting and you can also tweak the compression level with <code>compression_level</code>.</p>
<h2>HOW CCACHE WORKS</h2>
<p> The basic idea is to detect when you are compiling exactly the same code a second time and reuse the previously produced output. The detection is done by hashing different kinds of information that should be unique for the compilation and then using the hash sum to identify the cached output. ccache uses MD4, a very fast cryptographic hash algorithm, for the hashing. (MD4 is nowadays too weak to be useful in cryptographic contexts, but it should be safe enough to be used to identify recompilations.) On a cache hit, ccache is able to supply all of the correct compiler outputs (including all warnings, dependency file, etc) from the cache. </p>
<p> ccache has two ways of doing the detection: </p>
<dl>
<dt>
<dd> &bull; the <code>direct mode</code>, where ccache hashes the source code and include files directly</dl>
<dl>
<dt>
<dd> &bull; the <code>preprocessor mode</code>, where ccache runs the preprocessor on the source code and hashes the result</dl>
<p> The direct mode is generally faster since running the preprocessor has some overhead.</p>
<h3>Common hashed information</h3>
<p> For both modes, the following information is included in the hash: </p>
<dl>
<dt>
<dd> &bull; the extension used by the compiler for a file with preprocessor output (normally <code>.i</code> for C code and <code>.ii</code> for C++ code)</dl>
<dl>
<dt>
<dd> &bull; the compiler&#8217;s size and modification time (or other compiler-specific information specified by the <code>compiler_check</code> setting)</dl>
<dl>
<dt>
<dd> &bull; the name of the compiler</dl>
<dl>
<dt>
<dd> &bull; the current directory (if the <code>hash_dir</code> setting is enabled)</dl>
<dl>
<dt>
<dd> &bull; contents of files specified by the <code>extra_files_to_hash</code> setting (if any)</dl>
<h3>The direct mode</h3>
<p> In the direct mode, the hash is formed of the common information and: </p>
<dl>
<dt>
<dd> &bull; the input source file</dl>
<dl>
<dt>
<dd> &bull; the command line options</dl>
<p> Based on the hash, a data structure called &#8220;manifest&#8221; is looked up in the cache. The manifest contains: </p>
<dl>
<dt>
<dd> &bull; references to cached compilation results (object file, dependency file, etc) that were produced by previous compilations that matched the hash</dl>
<dl>
<dt>
<dd> &bull; paths to the include files that were read at the time the compilation results were stored in the cache</dl>
<dl>
<dt>
<dd> &bull; hash sums of the include files at the time the compilation results were stored in the cache</dl>
<p> The current contents of the include files are then hashed and compared to the information in the manifest. If there is a match, ccache knows the result of the compilation. If there is no match, ccache falls back to running the preprocessor. The output from the preprocessor is parsed to find the include files that were read. The paths and hash sums of those include files are then stored in the manifest along with information about the produced compilation result. </p>
<p> There is a catch with the direct mode: header files that were used by the compiler are recorded, but header files that were <code>not</code> used, but would have been used if they existed, are not. So, when ccache checks if a result can be taken from the cache, it currently can&#8217;t check if the existence of a new header file should invalidate the result. In practice, the direct mode is safe to use in the absolute majority of cases. </p>
<p> The direct mode will be disabled if any of the following holds: </p>
<dl>
<dt>
<dd> &bull; the configuration setting <code>direct_mode</code> is false</dl>
<dl>
<dt>
<dd> &bull; a modification time of one of the include files is too new (needed to avoid a race condition)</dl>
<dl>
<dt>
<dd> &bull; the unifier is enabled (the configuration setting <code>unify</code> is true)</dl>
<dl>
<dt>
<dd> &bull; a compiler option not supported by the direct mode is used: </p>
<dl>
<dt>
<dd> &bull; a <code>-Wp,</code><i>X</i> compiler option other than <code>-Wp,-MD,</code><i>path</i> and <code>-Wp,-MMD,</code><i>path</i></dl>
<dl>
<dt>
<dd> &bull; <code>-Xpreprocessor</code></dl>
</dl>
<dl>
<dt>
<dd> &bull; the string &#8220;__TIME__&#8221; is present in the source code</dl>
<h3>The preprocessor mode</h3>
<p> In the preprocessor mode, the hash is formed of the common information and: </p>
<dl>
<dt>
<dd> &bull; the preprocessor output from running the compiler with <code>-E</code></dl>
<dl>
<dt>
<dd> &bull; the command line options except options that affect include files (<code>-I</code>, <code>-include</code>, <code>-D</code>, etc; the theory is that these options will change the preprocessor output if they have any effect at all)</dl>
<dl>
<dt>
<dd> &bull; any standard error output generated by the preprocessor</dl>
<p> Based on the hash, the cached compilation result can be looked up directly in the cache.</p>
<h2>COMPILING IN DIFFERENT DIRECTORIES</h2>
<p> Some information included in the hash that identifies a unique compilation may contain absolute paths: </p>
<dl>
<dt>
<dd> &bull; The preprocessed source code may contain absolute paths to include files if the compiler option <code>-g</code> is used or if absolute paths are given to <code>-I</code> and similar compiler options.</dl>
<dl>
<dt>
<dd> &bull; Paths specified by compiler options (such as <code>-I</code>, <code>-MF</code>, etc) may be absolute.</dl>
<dl>
<dt>
<dd> &bull; The source code file path may be absolute, and that path may substituted for <code>__FILE__</code> macros in the source code or included in warnings emitted to standard error by the preprocessor.</dl>
<p> This means that if you compile the same code in different locations, you can&#8217;t share compilation results between the different build directories since you get cache misses because of the absolute build directory paths that are part of the hash. To mitigate this problem, you can specify a &#8220;base directory&#8221; in the configuration setting <code>base_dir</code> to an absolute path to the directory. ccache will then rewrite absolute paths that are under the base directory (i.e., paths that have the base directory as a prefix) to relative paths when constructing the hash. A typical path to use as the base directory is your home directory or another directory that is a parent of your build directories. (Don&#8217;t use / as the base directory since that will make ccache also rewrite paths to system header files, which doesn&#8217;t gain anything.) </p>
<p> The drawbacks of using a base directory are: </p>
<dl>
<dt>
<dd> &bull; If you specify an absolute path to the source code file, <code>__FILE__</code> macros will be expanded to a relative path instead.</dl>
<dl>
<dt>
<dd> &bull; If you specify an absolute path to the source code file and compile with <code>-g</code>, the source code path stored in the object file may point to the wrong directory, which may prevent debuggers like GDB from finding the source code. Sometimes, a work-around is to change the directory explicitly with the &#8220;cd&#8221; command in GDB.</dl>
<h2>PRECOMPILED HEADERS</h2>
<p> ccache has support for GCC&#8217;s precompiled headers. However, you have to do some things to make it work properly: </p>
<dl>
<dt>
<dd> &bull; You must set <code>sloppiness</code> to <code>pch_defines,time_macros</code>. The reason is that ccache can&#8217;t tell whether <code>__TIME__</code> or <code>__DATE__</code> is used when using a precompiled header. Further, it can&#8217;t detect changes in #defines in the source code because of how preprocessing works in combination with precompiled headers.</dl>
<dl>
<dt>
<dd> &bull; You must either: </p>
<dl>
<dt>
<dd> &bull; use the <code>-include</code> compiler option to include the precompiled header (i.e., don&#8217;t use <code>#include</code> in the source code to include the header); or</dl>
<dl>
<dt>
<dd> &bull; (for the Clang compiler) use the <code>-include-pch</code> compiler option to include the PCH file generated from the precompiled header; or</dl>
<dl>
<dt>
<dd> &bull; add the <code>-fpch-preprocess</code> compiler option when compiling.</dl>
<p> If you don&#8217;t do this, either the non-precompiled version of the header file will be used (if available) or ccache will fall back to running the real compiler and increase the statistics counter &#8220;preprocessor error&#8221; (if the non-precompiled header file is not available).</dl>
<h2>SHARING A CACHE</h2>
<p> A group of developers can increase the cache hit rate by sharing a cache directory. To share a cache without unpleasant side effects, the following conditions should to be met: </p>
<dl>
<dt>
<dd> &bull; Use the same cache directory.</dl>
<dl>
<dt>
<dd> &bull; Make sure that the configuration setting <code>hard_link</code> is false (which is the default).</dl>
<dl>
<dt>
<dd> &bull; Make sure that all users are in the same group.</dl>
<dl>
<dt>
<dd> &bull; Set the configuration setting <code>umask</code> to 002. This ensures that cached files are accessible to everyone in the group.</dl>
<dl>
<dt>
<dd> &bull; Make sure that all users have write permission in the entire cache directory (and that you trust all users of the shared cache).</dl>
<dl>
<dt>
<dd> &bull; Make sure that the setgid bit is set on all directories in the cache. This tells the filesystem to inherit group ownership for new directories. The command &#8220;find $CCACHE_DIR -type d | xargs chmod g+s&#8221; might be useful for this.</dl>
<p> The reason to avoid the hard link mode is that the hard links cause unwanted side effects, as all links to a cached file share the file&#8217;s modification timestamp. This results in false dependencies to be triggered by timestamp-based build systems whenever another user links to an existing file. Typically, users will see that their libraries and binaries are relinked without reason. </p>
<p> You may also want to make sure that a base directory is set appropriately, as discussed in a previous section.</p>
<h2>SHARING A CACHE ON NFS</h2>
<p> It is possible to put the cache directory on an NFS filesystem (or similar filesystems), but keep in mind that: </p>
<dl>
<dt>
<dd> &bull; Having the cache on NFS may slow down compilation. Make sure to do some benchmarking to see if it&#8217;s worth it.</dl>
<dl>
<dt>
<dd> &bull; ccache hasn&#8217;t been tested very thoroughly on NFS.</dl>
<p> A tip is to set <code>temporary_dir</code> to a directory on the local host to avoid NFS traffic for temporary files.</p>
<h2>USING CCACHE WITH OTHER COMPILER WRAPPERS</h2>
<p> The recommended way of combining ccache with another compiler wrapper (such as &#8220;distcc&#8221;) is by letting ccache execute the compiler wrapper. This is accomplished by defining the configuration setting <code>prefix_command</code>, for example by setting the environment variable <code>CCACHE_PREFIX</code> to the name of the wrapper (e.g. <code>distcc</code>). ccache will then prefix the command line with the specified command when running the compiler. To specify several prefix commands, set <code>prefix_command</code> to a colon-separated list of commands. </p>
<p> Unless you set <code>compiler_check</code> to a suitable command (see the description of that configuration option), it is not recommended to use the form <code>ccache anotherwrapper compiler args</code> as the compilation command. It&#8217;s also not recommended to use the masquerading technique for the other compiler wrapper. The reason is that by default, ccache will in both cases hash the mtime and size of the other wrapper instead of the real compiler, which means that: </p>
<dl>
<dt>
<dd> &bull; Compiler upgrades will not be detected properly.</dl>
<dl>
<dt>
<dd> &bull; The cached results will not be shared between compilations with and without the other wrapper.</dl>
<p> Another minor thing is that if <code>prefix_command</code> is used, ccache will not invoke the other wrapper when running the preprocessor, which increase performance.</p>
<h2>BUGS</h2>
<dl>
<dt>
<dd> &bull; ccache doesn&#8217;t handle the GNU Assembler&#8217;s <code>.incbin</code> directive correctly. This directive can be embedded in the source code inside an <i>asm</i> statement in order to include a file verbatim in the object file. If the included file is modified, ccache doesn&#8217;t pick up the change since the inclusion isn&#8217;t done by the preprocessor. A workaround of this problem is to set <code>extra_files_to_hash</code> to the path of the included file.</dl>
<dl>
<dt>
<dd> &bull; The direct mode fails to pick up new header files in some rare scenarios. See THE DIRECT MODE above.</dl>
<h2>TROUBLESHOOTING</h2>
<h3>General</h3>
<p> A general tip for getting information about what ccache is doing is to enable debug logging by setting <code>log_file</code>. The log contains executed commands, important decisions that ccache makes, read and written files, etc. Another way of keeping track of what is happening is to check the output of <code>ccache -s</code>.</p>
<h3>Performance</h3>
<p> ccache has been written to perform well out of the box, but sometimes you may have to do some adjustments of how you use the compiler and ccache in order to improve performance. </p>
<p> Since ccache works best when I/O is fast, put the cache directory on a fast storage device if possible. Having lots of free memory so that files in the cache directory stay in the disk cache is also preferrable. </p>
<p> A good way of monitoring how well ccache works is to run <code>ccache -s</code> before and after your build and then compare the statistics counters. Here are some common problems and what may be done to increase the hit rate: </p>
<dl>
<dt>
<dd> &bull; If &#8220;cache hit (preprocessed)&#8221; has been incremented instead of &#8220;cache hit (direct)&#8221;, ccache has fallen back to preprocessor mode, which is generally slower. Some possible reasons are: </p>
<dl>
<dt>
<dd> &bull; The source code has been modified in such a way that the preprocessor output is not affected.</dl>
<dl>
<dt>
<dd> &bull; Compiler arguments that are hashed in the direct mode but not in the preprocessor mode have changed (<code>-I</code>, <code>-include</code>, <code>-D</code>, etc) and they didn&#8217;t affect the preprocessor output.</dl>
<dl>
<dt>
<dd> &bull; The compiler option <code>-Xpreprocessor</code> or <code>-Wp,</code><i>X</i> (except <code>-Wp,-MD,</code><i>path</i> and <code>Wp,-MMD,</code><i>path</i>) is used.</dl>
<dl>
<dt>
<dd> &bull; This was the first compilation with a new value of the base directory setting.</dl>
<dl>
<dt>
<dd> &bull; A modification time of one of the include files is too new (created the same second as the compilation is being done). This check is made to avoid a race condition. To fix this, create the include file earlier in the build process, if possible, or set <code>sloppiness</code> to <code>include_file_mtime</code> if you are willing to take the risk. (The race condition consists of these events: the preprocessor is run; an include file is modified by someone; the new include file is hashed by ccache; the real compiler is run on the preprocessor&#8217;s output, which contains data from the old header file; the wrong object file is stored in the cache.)</dl>
<dl>
<dt>
<dd> &bull; The <code>__TIME__</code> preprocessor macro is (potentially) being used. ccache turns off direct mode if &#8220;__TIME__&#8221; is present in the source code. This is done as a safety measure since the string indicates that a <code>__TIME__</code> macro <i>may</i> affect the output. (To be sure, ccache would have to run the preprocessor, but the sole point of the direct mode is to avoid that.) If you know that <code>__TIME__</code> isn&#8217;t used in practise, or don&#8217;t care if ccache produces objects where <code>__TIME__</code> is expanded to something in the past, you can set <code>sloppiness</code> to <code>time_macros</code>.</dl>
<dl>
<dt>
<dd> &bull; The <code>__DATE__</code> preprocessor macro is (potentially) being used and the date has changed. This is similar to how <code>__TIME__</code> is handled. If &#8220;__DATE__&#8221; is present in the source code, ccache hashes the current date in order to be able to produce the correct object file if the <code>__DATE__</code> macro affects the output. If you know that <code>__DATE__</code> isn&#8217;t used in practise, or don&#8217;t care if ccache produces objects where <code>__DATE__</code> is expanded to something in the past, you can set <code>sloppiness</code> to <code>time_macros</code>.</dl>
<dl>
<dt>
<dd> &bull; The <code>__FILE__</code> preprocessor macro is (potentially) being used and the file path has changed. If &#8220;__FILE__&#8221; is present in the source code, ccache hashes the current input file path in order to be able to produce the correct object file if the <code>__FILE__</code> macro affects the output. If you know that <code>__FILE__</code> isn&#8217;t used in practise, or don&#8217;t care if ccache produces objects where <code>__FILE__</code> is expanded to the wrong path, you can set <code>sloppiness</code> to <code>file_macro</code>.</dl>
</dl>
<dl>
<dt>
<dd> &bull; If &#8220;cache miss&#8221; has been incremented even though the same code has been compiled and cached before, ccache has either detected that something has changed anyway or a cleanup has been performed (either explicitly or implicitly when a cache limit has been reached). Some perhaps unobvious things that may result in a cache miss are usage of <code>__TIME__</code> or <code>__DATE__</code> macros, or use of automatically generated code that contains a timestamp, build counter or other volatile information.</dl>
<dl>
<dt>
<dd> &bull; If &#8220;multiple source files&#8221; has been incremented, it&#8217;s an indication that the compiler has been invoked on several source code files at once. ccache doesn&#8217;t support that. Compile the source code files separately if possible.</dl>
<dl>
<dt>
<dd> &bull; If &#8220;unsupported compiler option&#8221; has been incremented, enable debug logging and check which option was rejected.</dl>
<dl>
<dt>
<dd> &bull; If &#8220;preprocessor error&#8221; has been incremented, one possible reason is that precompiled headers are being used. See PRECOMPILED HEADERS for how to remedy this.</dl>
<dl>
<dt>
<dd> &bull; If &#8220;can&#8217;t use precompiled header&#8221; has been incremented, see PRECOMPILED HEADERS.</dl>
<h3>Errors when compiling with ccache</h3>
<p> If compilation doesn&#8217;t work with ccache, but it works without it, one possible reason is that the compiler can&#8217;t compile preprocessed output correctly. A workaround that may work is to enable <code>run_second_cpp</code>*. This will make cache misses slower, though, so it is better to find and fix the root cause.</p>
<h3>Corrupt object files</h3>
<p> It should be noted that ccache is susceptible to general storage problems. If a bad object file sneaks into the cache for some reason, it will of course stay bad. Some possible reasons for erroneous object files are bad hardware (disk drive, disk controller, memory, etc), buggy drivers or file systems, a bad <code>prefix_command</code> or compiler wrapper. If this happens, the easiest way of fixing it is this: </p>
<dl>
<dt>
<dd> 1. Build so that the bad object file ends up in the build tree.</dl>
<dl>
<dt>
<dd> 2. Remove the bad object file from the build tree.</dl>
<dl>
<dt>
<dd> 3. Rebuild with <code>CCACHE_RECACHE</code> set.</dl>
<p> An alternative is to clear the whole cache with <code>ccache -C</code> if you don&#8217;t mind losing other cached results. </p>
<p> There are no reported issues about ccache producing broken object files reproducibly. That doesn&#8217;t mean it can&#8217;t happen, so if you find a repeatable case, please report it.</p>
<h2>MORE INFORMATION</h2>
<p> Credits, mailing list information, bug reporting instructions, source code, etc, can be found on ccache&#8217;s web site: <a rel="nofollow" href="http://ccache.samba.org.">http://ccache.samba.org.</a></p>
<h2>AUTHOR</h2>
<p> ccache was originally written by Andrew Tridgell and is currently developed and maintained by Joel Rosdahl. See AUTHORS.txt or AUTHORS.html and <a rel="nofollow" href="http://ccache.samba.org/credits.html">http://ccache.samba.org/credits.html</a> for a list of contributors. </p>
<h2>Index</h2>
