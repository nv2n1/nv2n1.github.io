---
title: "gccxml(1)"
name: "gccxml"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gccxml/"
---

<h2>NAME</h2>
<dl>
<dt><code>gccxml</code></p>
<dd> &#8211; Create an XML representation of C++ declarations.</dl>
<h2>SYNOPSIS</h2>
<p> gccxml [options] &lt;input-file&gt; -fxml=&lt;output-file&gt;</p>
<h2>DESCRIPTION</h2>
<p> GCC-XML parses a C++ source file as it is seen by the compiler when it is built. An easy-to-parse XML representation of the class, function, and namespace declarations is dumped to a specified file. Full C preprocessing transforms the file into a C++ translation unit as seen by the compiler. This means that GCC-XML should make use of the same standard library and other header files as the compiler. GCC-XML can be configured to simulate any of several popular compilers.</p>
<h2>OPTIONS</h2>
<p> The following options are available for running GCC-XML:</p>
<dl>
<dt><code>&#8211;copyright</code></p>
<dd> Print the GCC-XML copyright and exit.</p>
<dt><code>&#8211;debug</code></p>
<dd> Print extra debugging information. This option causes GCC-XML to print the executable name and command-line arguments used to execute the patched GCC C++ parser. This is useful when attempting to simulate an unsupported compiler.</p>
<dt><code>-fxml=&lt;output-file&gt;</code></p>
<dd> Specify the XML output file. This option is passed directly on to the patched GCC C++ parser. It enables the XML dump and specifies the output file name.</p>
<dt><code>-fxml-start=&lt;xxx&gt;[,&#8230;]</code></p>
<dd> Specify a list of starting declarations. This option is passed directly on to the patched GCC C++ parser. It is meaningful only if -fxml= is also specified. This specifies a comma-separated list of named starting declarations. GCC-XML will dump only the subset of the declarations in the translation unit that is reachable through a sequence of source references from one of the specified starting declarations.</p>
<dt><code>&#8211;gccxml-compiler &lt;xxx&gt;</code></p>
<dd> Set GCCXML_COMPILER to &quot;xxx&quot;.</p>
<dt><code>&#8211;gccxml-cxxflags &lt;xxx&gt;</code></p>
<dd> Set GCCXML_CXXFLAGS to &quot;xxx&quot;.</p>
<dt><code>&#8211;gccxml-executable &lt;xxx&gt;</code></p>
<dd> Set GCCXML_EXECUTABLE to &quot;xxx&quot;.</p>
<dt><code>&#8211;gccxml-cpp &lt;xxx&gt;</code></p>
<dd> Set GCCXML_CPP to &quot;xxx&quot;.</p>
<dt><code>&#8211;gccxml-config &lt;xxx&gt;</code></p>
<dd> Set GCCXML_CONFIG to &quot;xxx&quot;.</p>
<dt><code>&#8211;gccxml-root &lt;xxx&gt;</code></p>
<dd> Set GCCXML_ROOT to &quot;xxx&quot;.</p>
<dt><code>&#8211;gccxml-gcc-options &lt;xxx&gt;</code></p>
<dd> Read GCC options from file &quot;xxx&quot;. This option specifies a file from which to read options to pass to the patched GCC C++ parser. This is useful for specifying a long list of include directories. Each line in the file becomes one option. Empty lines and lines beginning in &#8216;#&#8217; are ignored.</p>
<dt><code>&#8211;help</code></p>
<dd> Print full help and exit. Full help displays most of the documentation provided by the UNIX man page. It is provided for use on non-UNIX platforms, but is also convenient if the man page is not installed.</p>
<dt><code>&#8211;help-html</code></p>
<dd> Print full help in HTML format. This option is used by GCC-XML authors to help produce web pages.</p>
<dt><code>&#8211;man</code></p>
<dd> Print a UNIX man page and exit. This option is used by GCC-XML authors to generate the UNIX man page.</p>
<dt><code>&#8211;print</code></p>
<dd> Print configuration settings and exit. GCC-XML has many configuration options to help it simulate another compiler. Using this option will cause GCC-XML to configure itself as if it were going to parse the C++ source, but stop and print the configuration found. This is useful for checking the configuration.</p>
<dt><code>&#8211;preprocess</code></p>
<dd> Preprocess the input and exit. GCC-XML simulates the proprocessor of another compiler. Using this option will cause GCC-XML to configure itself as if it were going to parse the C++ source, but stop after preprocessing. This is useful for debugging problems related to simulation of the other compiler.</p>
<dt><code>-E</code></p>
<dd> Alias for &#8211;preprocess.</p>
<dt><code>&#8211;version</code></p>
<dd> Show program name/version banner and exit.</dl>
<p> Other flags, such as -I and -D, are passed on to the patched GCC C++ parser executable.</p>
<h2>SETTINGS</h2>
<p> GCC-XML is designed to simulate a compiler&#8217;s parser while reading C++ source code. Some configuration settings are needed to determine how to simulate a particular compiler of the user&#8217;s choice. The following settings can be used to configure GCC-XML:</p>
<dl>
<dt><code>GCCXML_COMPILER</code></p>
<dd> The C++ compiler to be simulated. GCC-XML will attempt to automatically determine how to simulate the compiler specified by this setting. The compiler is specified by its executable name (such as &quot;g++&quot;). For Visual Studio, the compiler is specified by &quot;msvc6&quot;, &quot;msvc7&quot;, &quot;msvc71&quot;, or &quot;msvc8&quot; (if &quot;cl&quot; is given, GCC-XML attempts to guess which VS to use).</p>
<dt><code>GCCXML_CXXFLAGS</code></p>
<dd> The flags for the C++ compiler to be simulated. The behavior of most compilers can be adjusted by specifying flags on the command line. When GCC-XML attempts to automatically determine how to simulate a compiler, these flags are taken into consideration.</p>
<dt><code>GCCXML_CONFIG</code></p>
<dd> The configuration file for common settings. When non-default settings are often used, it is convenient to write a single file containing them. When such a file is specified, it will be read to configure any settings that are not yet known. Each line of the file consists of one assignment of the form KEY=&quot;VALUE&quot; (for example, GCCXML_COMPILER=&quot;g++&quot;).</p>
<dt><code>GCCXML_EXECUTABLE</code></p>
<dd> Specify the patched GCC C++ parser executable. The GCC-XML program as seen by the user is actually a front-end that determines the flags needed to configure the patched GCC C++ parser to simulate another compiler. This setting specifies the real executable to run once the flags have been determined. Users should rarely need to change this value from its default.</p>
<dt><code>GCCXML_CPP</code></p>
<dd> Specify the GCC C preprocessor executable. The GCC-XML program as seen by the user is actually a front-end that determines the flags needed to configure the patched GCC C++ parser to simulate another compiler. This setting specifies the preprocessor to run with the flags that have been determined for debugging purposes. Users should rarely need to change this value from its default.</p>
<dt><code>GCCXML_ROOT</code></p>
<dd> The GCC-XML support library directory. Since GCC-XML is only one C++ parser, it cannot exactly duplicate the functionality of every compiler it tries to simulate. Some compilers provide standard headers with code that GCC-XML cannot directly handle. To work around this limitation, a support library is provided for each compiler. This consists of a set of header files that are used in place of the compiler&#8217;s system headers. These files contain slight tweaks and then include the corresponding real header. The root of the directory tree containing these support library headers is specified by this setting. Users should rarely need to change this value from its default.</p>
<dt><code>GCCXML_FLAGS</code></p>
<dd> Flags used to simulate the other compiler. When GCC-XML runs the patched GCC C++ parser, these flags are passed to the program to tell it how to simulate a particular compiler. This setting is usually detected automatically from the other settings, but it can be specified directly by advanced users. Most users should not attempt to change this value from the automatic configuration.</p>
<dt><code>GCCXML_USER_FLAGS</code></p>
<dd> Additional user flags for compiler simulation. When GCC-XML runs the patched GCC C++ parser, these flags are passed in addition to those specified by GCCXML_FLAGS. This allows advanced users to tweak the compiler simulation while still using the automatic configuration of GCCXML_FLAGS. Users should rarely need to change this value from its default.</dl>
<p> There are several means by which these settings are configured. They are listed here in order of precedence (highest first):</p>
<dl>
<dt><code>Command-line Options</code></p>
<dd> Settings can be specified by their corresponding options. When a setting&#8217;s corresponding command-line option is provided, it is used in favor over any other means of configuration. If GCCXML_CONFIG is set on the command-line, settings are read from the file with precedence just slightly lower than other command-line options.</p>
<dt><code>Environment Variables</code></p>
<dd> Settings are configured by name in the environment. Each setting not already known is read from an environment variable with its name. If GCCXML_CONFIG is set by the environment, settings are read from the file with precedence just slightly lower than other environment variables.</p>
<dt><code>Configuration Files</code></p>
<dd> A search for GCCXML_CONFIG is performed. If GCCXML_CONFIG has not yet been set, an attempt is made to find a configuration file automatically. First, if the file $HOME/.gccxml/config exists, it will be used. Second, if GCC-XML is being executed from its build directory, a config file from that directory will be used. Finally, if a config file is found in the installation&#8217;s support library directory, it will be used. Once found, any unknown settings are read from the configuration file.</p>
<dt><code>Guessing</code></p>
<dd> Guesses are made based on other settings. Once GCCXML_COMPILER has been set, it is used to automatically find the setting for GCCXML_FLAGS. If it is not set, the &quot;CXX&quot; environment variable is checked as a last-resort to find the compiler setting and determine GCCXML_FLAGS.</dl>
<p> Most users should not have to adjust the defaults for these settings. There is a default GCCXML_CONFIG file provided in the support library directory after installation. It configures GCC-XML to simulate the compiler that was used to build it.</p>
<h2>COMPILERS</h2>
<p> GCC-XML can simulate any of the following compilers:</p>
<dl>
<dt><code>GCC</code></p>
<dd> Versions 4.2, 4.1, 4.0, 3.4, 3.3, 3.2, 2.95.x</p>
<dt><code>Visual C++</code></p>
<dd> Versions 8, 7.1, 7.0, and 6 (sp5)</p>
<dt><code>Borland, Intel, SGI</code></p>
<dd> formerly supported but no longer tested</dl>
<p> The following extra C preprocessor definitions are provided:</p>
<dl>
<dt><code>-D__GCCXML__=MMmmpp</code></p>
<dd> MM, mm, and pp are the major, minor, and patch versions of GCC-XML. This preprocessor symbol identifies GCC-XML to the source code as it is preprocessed. It can be used to enable GCC-XML-specific information.</p>
<dt><code>-D__GCCXML_GNUC__=M</code></p>
<dd> Defined to internal GCC parser major version.</p>
<dt><code>-D__GCCXML_GNUC_MINOR__=m</code></p>
<dd> Defined to internal GCC parser minor version.</p>
<dt><code>-D__GCCXML_GNUC_PATCHLEVEL__=p</code></p>
<dd> Defined to internal GCC parser patchlevel.</dl>
<p> Advanced users can simulate other compilers by manually configuring the GCCXML_FLAGS setting. Contact the mailing list for help.</p>
<h2>METAINFO</h2>
<p> GCC-XML has added a new attribute to the legal set of C/C++ attributes. The attribute is used to attach meta information to C/C++ source code, which will then appear in the XML output. The syntax for declaring an attribute is as follows:</p>
<dl>
<dt><code>__attribute((gccxml(&lt;string&gt;, &lt;string&gt;, &#8230;)))</code></p>
<dd> Here &lt;string&gt; is a quoted string. There must be at least one argument to the &#8216;gccxml&#8217; attribute, but there is no upper limit to the total number of arguments. Each argument is verified to be a string &#8211; if a non-string argument is found, the attribute is ignored.</dl>
<p> The XML output for the code element that is tagged with the attribute will then contain the following:</p>
<dl>
<dt><code>attributes= &#8230; gccxml(&lt;string&gt;,&lt;string&gt;,&lt;string&gt; &#8230;) &#8230; </code></p>
<dd> The &#8216;attributes&#8217; XML attribute contains all attributes applied to the code element. Each argument of the attribute is printed without enclosing quotes, so if an argument contains the &#8216;,&#8217; character, the argument will appear to be multiple arguments.</dl>
<p> The &#8216;gccxml&#8217; attribute can be applied to any declaration including structs, classes, fields, parameters, methods, functions, variables, and typedefs. The only exception is that GCC&#8217;s handling of the &#8216;__attribute&#8217; language element is currently broken for enumerations and constructors with an inlined body. The &#8216;gccxml&#8217; attribute can be used any number of times on a given declaration. </p>
<p> As an example of how this attribute can be used to attach meta information to C++ declarations, consider the following macro:</p>
<dl>
<dt><code>#define _out_ __attribute((gccxml(out)))</code></p>
<dd> Here &#8216;_out_&#8217; has been defined to be the gccxml attribute where the first argument is the string &quot;out&quot;. It is recommended that the first argument be used as a unique string name for the type of meta information begin applied.</dl>
<p> Now a method declaration can be written as follows:</p>
<dl>
<dt><code>void getInteger(_out_ int&amp; i);</code></p>
<dd> This will cause the XML output to contain meta information for the &#8216;_out_&#8217; attribute, in the form &quot;gccxml(out)&quot;.</dl>
<p> Using the &#8216;gccxml&#8217; attribute enables meta information to be included directly within C++ source code, without the need for a custom parser to extract the meta information. The &#8216;gccxml&#8217; attribute is provided for convenience only &#8211; there is no guarantee that future versions of GCC will accept the &#8216;__attribute&#8217; language element in a bug-free manner.</p>
<h2>COPYRIGHT</h2>
<p> GCC-XML &#8211; XML output for GCC </p>
<p> Copyright 2002-2012 Kitware, Inc., Insight Consortium </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<dl>
<dt><code>* </code></p>
<dd> Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. </p>
<dt><code>* </code></p>
<dd> Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. </p>
<dt><code>* </code></p>
<dd> Neither the names of Kitware, Inc., the Insight Software Consortium, nor the names of their contributors may be used to endorse or promote products derived from this software without specific prior written permission. </p>
</dl>
<p> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </p>
<p> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212; </p>
<p> gccxml_cc1plus &#8211; A GCC parser patched for XML dumps of translation units </p>
<p> Copyright 2002-2012 Kitware, Inc., Insight Consortium </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the<br />
&nbsp;<wbr>&nbsp;<wbr>Free Software Foundation, Inc.<br />
&nbsp;<wbr>&nbsp;<wbr>51 Franklin Street, Fifth Floor<br />
&nbsp;<wbr>&nbsp;<wbr>Boston, MA&nbsp;<wbr>&nbsp;<wbr>02110-1301&nbsp;<wbr>&nbsp;<wbr>USA </p>
<h2>AUTHOR</h2>
<p> This manual page was generated by &quot;gccxml &#8211;man&quot;. </p>
<h2>Index</h2>
