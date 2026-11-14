---
title: "register_premib_handler(3)"
name: "register_premib_handler"
section: "3"
letter: "r"
url: "/docs/linux/man/3-register_premib_handler/"
description: "register_config_handler, register_premib_handler unregister_config_handler, register_mib_handlers, read_configs, read_premib_configs, config_perror, config_pwarn – read_config functions"
---

<p>register_config_handler, register_premib_handler unregister_config_handler, register_mib_handlers, read_configs, read_premib_configs, config_perror, config_pwarn &#8211; read_config functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/config_api.h&gt;
struct config_line *

register_config_handler(const char *filePrefix,

                        const char *token,

                        void (*parser)(const char *, char *),

                        void (*releaser)(void),

                        const char *usageLine);
struct config_line *

register_premib_handler(const char *filePrefix,

                        const char *token,

                        void (*parser)(const char *, char *),

                        void (*releaser)(void),

                        const char *usageLine);
void unregister_config_handler(const char *filePrefix,

                               const char *token);
struct config_line *

register_app_config_handler(const char *token,

                            void (*parser)(const char *, char *),

                            void (*releaser)(void),

                            const char *usageLine);
struct config_line *

register_app_premib_handler(const char *token,

                            void (*parser)(const char *, char *),

                            void (*releaser)(void),

                            const char *usageLine);
void unregister_app_config_handler(const char *token);
void read_config_print_usage(char *lead);
void read_configs(void);
void read_premib_configs(void);
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
<p> The idea is that the calling application is able to register <i>handlers</i> for certain <i>tokens</i> specified in certain types of <i>files.</i> The <code>read_configs()</code> function can then be called to look for all the files that it has registrations for, find the first word on each line, and pass the remainder to the appropriately registered handler.</p>
<h2>Token Handlers</h2>
<p>Handler functions should have the following signature: </p>
<dl>
<dd><code>void handler(const char *</code><i>token</i><code>, char *</code><i>line</i><code>);</code></dl>
<p> The function will be called with two arguments, the first being the token that triggered the call to this function (which would be one of the tokens that the function had been registered for), and the second being the remainder of the configuration file line beyond the white space following the token.</p>
<h2>Resource Freeing Handlers</h2>
<p>If the parameter <i>releaser</i> passed to <code>register_config_handler</code> is non-NULL, then the function specified is called if and when the configuration files are re-read. This function should free any resources allocated by the token handler function and reset its notion of the configuration to its default. The token handler function will then be called again. No arguments are passed to the resource freeing handler.</p>
<h2>Registering A Handler</h2>
<dl>
<dt><code>register_config_handler()</code></p>
<dd>The <code>handler()</code> function above could be registered for the configuration file <i>snmp.conf,</i> with the token <i>genericToken</i> and the help string (discussed later) <i>ARG1 [ARG2]</i> using the following call to the <code>register_config_handler()</code> function:</dl>
<dl>
<dd>
<dl>
<dd>register_config_handler(&quot;snmp&quot;, &quot;genericToken&quot;, handler, NULL, &quot;ARG1 [ARG2]&quot;);</dl>
</dl>
<dl>
<dd>This would register the <code>handler()</code> function so that it will get called every time the first word of a line in the <i>snmp.conf</i> configuration file(s) matches &quot;genericToken&quot; (see <code>read_configs() </code> below).</p>
<dt><code>register_premib_handler()</code></p>
<dd>The <code>register_premib_handler()</code> function works identically to the <code>register_config_handler()</code> function but is intended for config file tokens that need to be read in before the textual MIBs are read in, probably because they will be used to configure the MIB parser. It is rarely the case that anything but the SNMP library itself should need to use this function.</p>
<dt><code>unregister_config_handler()</code></p>
<dd>Removes the registered configuration handler for the <i>filePrefix</i> and <i>token</i>. </p>
<dt><code>register_app_config_handler()</code></p>
<dd>
<dt><code>register_app_premib_handler()</code></p>
<dd>
<dt><code>unregister_app_config_handler()</code></p>
<dd>These functions are analagous to <code>register_config_handler()</code>, <code>register_premib_handler()</code> and <code>unregister_config_handler()</code> but don&#8217;t require the file type argument (which is filled in by the application). It is intended that MIB modules written for the agent use these functions to allow the agent to have more control over which configuration files are read (typically the <i>snmpd.conf</i> files).</dl>
<h2>Help Strings</h2>
<p>The <i>usageLine</i> parameter passed to <code>register_config_handler()</code> and similar calls, is used to display help information when the <code>read_config_print_usage()</code> function is called. This function is used by all of the applications when the <code>-H</code> flag is passed on the command line. It prints a summary of all of the configuration file lines, and the associated files, that the configuration system understands. The <i>usageLine</i> parameter should be a list of arguments expected after the token, and not a lengthy description (which should go into a manual page instead). The <i>lead</i> prefix will be prepended to each line that the function prints to stderr, where it displays its output. </p>
<p> The <code>init_snmp()</code> function should be called before the <code>read_config_print_usage()</code> function is called, so that the library can register its configuration file directives as well for the <code>read_config_print_usage()</code> function to display.</p>
<h2>Reading Configuration Files</h2>
<dl>
<dt><code>init_snmp()</code></p>
<dd>Once the relevant configuration token parsers have been registered, <code>init_snmp()</code> should be called. It will parse the configuration file tokens registered with <code>register_premib_handler(),</code> read in the textual MIB files using <code>init_mib(),</code> and finally parse the configuration file tokens registered with <code>register_config_handler()</code>.</dl>
<p> If the <code>init_snmp()</code> function is used, none of the following functions need to be called by the application:</p>
<dl>
<dt><code>register_mib_handlers()</code></p>
<dd>The SNMP library&#8217;s routine to register its configuration file handlers.</p>
<dt><code>read_premib_configs()</code></p>
<dd>The routine that parses the configuration files for tokens registered to be dealt with before the textual MIBs are read in. See <code>read_configs()</code> below.</p>
<dt><code>read_configs()</code></p>
<dd>Reads all the configuration files it can find in the <i>SNMPCONFPATH</i> environment variable (or its default value) for tokens and appropriately calls the handlers registered to it, or prints a &quot;Unknown token&quot; warning message. It looks for any file that it has previously received a registration request for.</dl>
<h2>Configuration Files Read</h2>
<p>The configuration files read are found by using the colon separated <i>SNMPCONFPATH</i> environment variable (or its default value, which will be /etc/snmp, followed by /usr/share/snmp, followed by /usr/lib/snmp (or /usr/lib64/snmp), followed by $HOME/.snmp) and reading in the files found that match both the prefix registered and the two suffixes <i>.conf</i> and <i>.local.conf.</i> The idea behind the two different suffixes is that the first file can be shared (via rdist or an NFS mount) across a large number of machines and the second file can be used to configure local settings for one particular machine. They do not need to be present, and will only be read if found.</p>
<h2>Error Handling Functions</h2>
<p>The two functions <code>config_pwarn()</code> and <code>config_perror()</code> both take an error string as an argument and print it to stderr along with the file and line number that caused the error. A call to the second function will also force <code>read_configs() </code> to eventually return with an error code indicating to it&#8217;s calling function that it should abort the operation of the application.</p>
<h2>Environment Variables</h2>
<dl>
<dt>SNMPCONFPATH</p>
<dd>A colon separated list of directories to search for configuration files in. Default: /etc/snmp:/usr/share/snmp:/usr/lib(64)/snmp:$HOME/.snmp</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mib_api/">mib_api</a></code>(3), <code><a href="/docs/linux/man/3-snmp_api/">snmp_api</a></code>(3) </p>
