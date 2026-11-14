---
title: "unregister_app_config_handler(3)"
name: "unregister_app_config_handler"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unregister_app_config_handler/"
description: "register_config_handler, register_const_config_handler, register_prenetsnmp_mib_handler, unregister_config_handler, register_mib_handlers, unregister_all_config_handlers, register_app_config_handle..."
---

<p>register_config_handler, register_const_config_handler, register_prenetsnmp_mib_handler, unregister_config_handler, register_mib_handlers, unregister_all_config_handlers, register_app_config_handler, register_app_prenetsnmp_mib_handler, unregister_app_config_handler, read_configs, read_premib_configs, read_config_print_usage, config_perror, config_pwarn &#8211; netsnmp_config_api functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/config_api.h&gt;

Config Handlers struct config_line *

register_config_handler(const char *filePrefix,

                        const char *token,

                        void (*parser)(const char *, char *),

                        void (*releaser)(void),

                        const char *usageLine);
struct config_line *

register_const_config_handler(const char *filePrefix,

                              const char *token,

                              void (*parser)(const char *, const char *),

                              void (*releaser)(void),

                              const char *usageLine);

struct config_line *

register_prenetsnmp_mib_handler(const char *filePrefix,

                                const char *token,

                                void (*parser)(const char *, char *),

                                void (*releaser)(void),

                                const char *usageLine);
void unregister_config_handler(const char *filePrefix,

                               const char *token);</code></pre>
<p> <code>void register_mib_handlers(void);</code><br />
 <code>void unregister_all_config_handlers(void);</code></p>
<h3>Application Handlers</h3>
<p>struct config_line *</p>
<p>register_app_config_handler(const char *token,</p>
<p>                            void (*parser)(const char *, char *),</p>
<p>                            void (*releaser)(void),</p>
<p>                            const char *usageLine);<br />
struct config_line *</p>
<p>register_app_prenetsnmp_mib_handler(const char *token,</p>
<p>                                    void (*parser)(const char *, char *),</p>
<p>                                    void (*releaser)(void),</p>
<p>                                    const char *usageLine); <code>void unregister_app_config_handler(const char *</code><i>token</i><code>);</code></p>
<h3>Reading Configuration Files</h3>
<p><code>void read_premib_configs(void);</code><br />
 <code>void read_configs(void);</code></p>
<h3>Help Strings and Errors</h3>
<pre><code>void read_config_print_usage(char *lead);

void config_pwarn(const char *string);

void config_perror(const char *string);
</code></pre>
<h2>Description</h2>
<p>The functions are a fairly extensible system of parsing various configuration files at the run time of an application. The configuration file flow is broken into the following phases:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Registration of handlers.</p>
<dt>2.</p>
<dd>Reading of the configuration files for pre-MIB parsing requirements.</p>
<dt>3.</p>
<dd>Reading and parsing of the textual MIB files.</p>
<dt>4.</p>
<dd>Reading of the configuration files for configuration directives.</p>
<dt>5.</p>
<dd>Optionally re-reading the configuration files at a future date.</dl>
</dl>
<p> The idea is that the calling application is able to register <i>handlers</i> for certain <i>tokens</i> specified in certain named <i>configuration files.</i> The <code>read_configs()</code> function can then be called to look for all relevant configuration files, match the first word on each line against the list of registered tokens and pass the remainder of the line to the appropriate registered handler.</p>
<h2>Registering A Handler</h2>
<dl>
<dt><code>register_config_handler()</code></p>
<dd>Registers a configuration handler routine, which should be called to process configuration directives starting with the specified token. For example:</dl>
<dl>
<dd>
<dl>
<dd>register_config_handler(&quot;snmp&quot;, &quot;exampleToken&quot;, example_handler, NULL, &quot;ARG1 [ARG2]&quot;);</dl>
</dl>
<dl>
<dd>would register the <code>example_handler()</code> function so that it will get called every time the first word of a line in the <i>snmp.conf</i> configuration file(s) matches &quot;exampleToken&quot;.<br />
 Calling the appropriate handlers to process the configuration file directives is the responsibility of <code>read_configs() </code> (see below).</p>
<dt><code>register_const_config_handler()</code></p>
<dd>Similar to the <code>register_config_handler()</code> function, but the parser routine is explicitly constrained to not modify the string being parsed.</p>
<dt><code>register_prenetsnmp_mib_handler()</code></p>
<dd>Similar to the <code>register_config_handler()</code> function, but the registered handler routine will be called <i>before</i> the textual MIBs are read in. This is typically used for tokens that will affect the configuration of the MIB parser, and will normally only be used within the SNMP library itself.</p>
<dt><code>register_mib_handlers()</code></p>
<dd>Initialisation routine to register the internal SNMP library configuration handlers.</p>
<dt><code>unregister_config_handler()</code></p>
<dd>Removes the registered configuration handler for the specified <i>filePrefix</i> and <i>token</i>.</p>
<dt><code>unregister_all_config_handlers()</code></p>
<dd>Removes all registered configuration handlers. </p>
</dl>
<h3>Token Handlers</h3>
<p>Handler functions should have the following signature: </p>
<dl>
<dd><code>void handler(const char *</code><i>token</i><code>, char *</code><i>line</i><code>);</code><br />
 or<br />
 <code>void handler(const char *</code><i>token</i><code>, const char *</code><i>line</i><code>);</code> br (if registered using <i>register_const_config_handler</i>)</dl>
<p> The function will be called with two arguments, the first being the token that triggered the call to this function (i.e. the token used when registering the handler), and the second being the remainder of the configuration file line (i.e. everything following the white space following the matched token).</p>
<h3>Freeing Handlers</h3>
<p>If the token handler function dynamically allocates resources when processing a configuration entry, then these may need to be released before re-reading the configuration files. If the fourth parameter ( <i>releaser</i> ) passed to <code>register_config_handler</code> is non-NULL, then this specifies a function to be called before re-reading the configuration files. This function should free any resources allocated by the token handler function and reset its notion of the configuration to its default. The token handler function can then safely be called again. No arguments are passed to the resource freeing handler.<br />
 Note that this function is not called when the handler is unregistered individually (but <i>is</i> called as part of <code>unregister_all_config_handlers()</code> ).</p>
<h3>Application Handlers</h3>
<dl>
<dt><code>register_app_config_handler()</code></p>
<dd>
<dt><code>register_app_prenetsnmp_mib_handler()</code></p>
<dd>
<dt><code>unregister_app_config_handler()</code></p>
<dd>These functions are analagous to <code>register_config_handler()</code>, <code>register_prenetsnmp_mib_handler()</code> and <code>unregister_config_handler()</code> but do not require the file type argument (which is filled in by the application). It is intended that MIB modules written for the agent use these functions to allow the agent to have more control over which configuration files are read (typically the <i>snmpd.conf</i> files).</dl>
<h2>Reading Configuration Files</h2>
<dl>
<dt><code>read_premib_configs()</code></p>
<dd>
<dt><code>read_configs()</code></p>
<dd>These routines process the configuration files found in the configuration search path (see below). For each entry, the handler registered for that configuration token is called.</dl>
<p> <code>read_premib_configs()</code> is run before the MIB files are read in, and processes those configuration tokens registered using <code>register_prenetsnmp_mib_handler()</code> (or <code>register_app_prenetsnmp_mib_handler()</code> ). All other entries are ignored. </p>
<p> <code>read_configs()</code> is run after the MIB files have been read in, and processes those configuration tokens registered using <code>register_config_handler()</code> (or <code>register_app_config_handler()</code> ). If it encounters a configuration token for which no handler has been registered (either pre- or post-mib), then it will display a warning message, and continue processing with the next line of the configuration file.</p>
<h3>Configuration Search Path</h3>
<p>The configuration files to be read are found by searching a list of configuration directories for appropriately named files. In each such directory, the library will look for files named snmp.conf, snmp.local.conf, <i> app</i>.conf, <i> app</i>.local.conf,<br />
 (where <i>app</i> is the appication-specific filePrefix used to register configuration handlers). It is not necessary for any or all of these files to be present in each directory. Missing files will be silently skipped.<br />
 The idea behind the two different suffixes is that the first file can be shared (via rdist or an NFS mount) across a large number of machines and the second file can be used to configure local settings for one particular machine. </p>
<p> The default list of directories to search is /etc/snmp, followed by /usr/share/snmp, followed by /usr/lib(64)/snmp, followed by $HOME/.snmp. This list can be changed by setting the environmental variable <i>SNMPCONFPATH</i> to be a (colon separated) list of directories to search.</p>
<h3>init_snmp()</h3>
<p>The normal mode of operation would be to register the application-specific configuration handlers, and then invoke <code>init_snmp()</code>. This would call the routines listed above to register the internal library configuration handlers, process any configuration tokens registered with <code>register_prenetsnmp_mib_handler(),</code> read in the textual MIB files using <code>init_mib(),</code> and finally parse the configuration file tokens registered with <code>register_config_handler()</code>. </p>
<p> If the <code>init_snmp()</code> function is used, none of these functions need to be explicitly called by the application.</p>
<h2>Help Strings And Errors</h2>
<p>The <i>usageLine</i> parameter passed to <code>register_config_handler()</code> and similar calls, is used to display help information when the <code>read_config_print_usage()</code> function is called. This function is used by all of the applications when the <code>-H</code> flag is passed on the command line. It prints a summary of all of the configuration file lines, and the associated files, that the configuration system understands. The <i>usageLine</i> parameter should be a list of arguments expected after the token, and not a lengthy description (which should go into a manual page instead). The <i>lead</i> prefix will be prepended to each line that the function prints to stderr, where it displays its output. </p>
<p> The <code>init_snmp()</code> function should be called before the <code>read_config_print_usage()</code> function is called, so that the library can register its configuration file directives as well for the <code>read_config_print_usage()</code> function to display.</p>
<h3>Error Handling Functions</h3>
<p>The two functions <code>config_pwarn()</code> and <code>config_perror()</code> both take an error string as an argument and print it to stderr along with the file and line number that caused the error. A call to the second function will also force <code>read_configs() </code> to eventually return with an error code indicating to it&#8217;s calling function that it should abort the operation of the application.</p>
<h2>Environment Variables</h2>
<dl>
<dt>SNMPCONFPATH</p>
<dd>A colon separated list of directories to search for configuration files in. Default: /etc/snmp:/usr/share/snmp:/usr/lib(64)/snmp:$HOME/.snmp</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mib_api/">mib_api</a></code>(3), <code><a href="/docs/linux/man/3-snmp_api/">snmp_api</a></code>(3) </p>
