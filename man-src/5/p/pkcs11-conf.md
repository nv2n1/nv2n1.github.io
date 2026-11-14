---
title: "pkcs11-conf(5)"
name: "pkcs11-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pkcs11-conf/"
description: "pkcs11.conf – Configuration files for PKCS#11 modules"
---

<p>pkcs11.conf &#8211; Configuration files for PKCS#11 modules</p>
<h2>Description</h2>
<p>The <code>pkcs11.conf</code> configuration files are a standard way to configure PKCS#11 modules.</p>
<h2>File Format</h2>
<p>A complete configuration consists of several files. These files are text files. Since p11-kit is built to be used in all sorts of environments and at very low levels of the software stack, we cannot make use of high level configuration APIs that you may find on a modern desktop. </p>
<p> Each setting in the config file is specified consists of a name and a value. The name is a simple string consisting of characters and dashes. The name consists of alpha numeric characters, dot, hyphen and underscore. </p>
<p> The value is specified after the name on the same line, separated from it by a : (colon). White space between the name and value is ignored. </p>
<p> Blank lines are ignored. White space at the beginning or end of lines is stripped. Lines that begin with a # character are ignored as comments. Comments are not recognized when they come after a value on a line. </p>
<p> A fictitious module configuration file might look like: </p>
<dl>
<dd>
<pre>module: module.so
# Here is a comment
managed: true
setting.2: A long value with text.
x-custom : text</pre>
</dl>
<h2>Module Configuration</h2>
<p>Each configured PKCS#11 module has its own config file. These files can be placed in various locations. </p>
<p> The filename of the configuration file may consist of upper and lowercase letters underscore, comma, dash and dots. The first characters needs to be an alphanumeric, the filename should end with a .module extension. </p>
<p> Most importantly each config file specifies the path of the PKCS#11 module to load. A module config file has the following fields: </p>
<p> <code>module:</code></p>
<dl>
<dd>The filename of the PKCS#11 module to load. This should include an extension like .so </p>
<p> If this value is blank, then the module will be ignored. This can be used in the user configs to override loading of a module specified in the system configuration. </p>
<p> If this is a relative path, then the module will be loaded from the default module directory.</dl>
<p> <code>critical:</code></p>
<dl>
<dd>Set to yes if the module is critical and required to load. If a critical module fails to load or initialize, then the loading process for all registered modules will abort and return an error code. </p>
<p> This argument is optional and defaults to no.</dl>
<p> <code>enable-in:</code></p>
<dl>
<dd>A comma and/or space separated list of names of programs that this module should only be loaded in. The module will not be loaded for other programs using p11-kit. The base name of the process executable should be used here, for example seahorse, ssh. </p>
<p> This option can also be used to control whether the module will be loaded by the proxy module. To enable loading only from the proxy module, specify p11-kit-proxy as the value. </p>
<p> This is not a security feature. The argument is optional. If not present, then any process will load the module.</dl>
<p> <code>disable-in:</code></p>
<dl>
<dd>A comma and/or space separated list of names of programs that this module should not be loaded in. The module will be loaded for any other programs using p11-kit. The base name of the process executable should be used here, for example firefox, thunderbird-bin. </p>
<p> This option can also be used to control whether the module will be loaded by the proxy module. To disable loading from the proxy module, specify p11-kit-proxy as the value. </p>
<p> This is not a security feature. The argument is optional. If not present, then any process will load the module.</dl>
<p> <code>managed:</code></p>
<dl>
<dd>Set to no if the module is not to be managed by p11-kit. Making a module unmanaged is not recommended, and will cause problems if multiple callers in a single process share a PKCS#11 module. </p>
<p> This argument is optional and defaults to yes.</dl>
<p> <code>priority:</code></p>
<dl>
<dd>The value should be an integer. When lists of modules are returned to a caller of p11-kit, modules with a higher number are sorted first. When applications search modules for certificates, keys and trust policy information, this setting will affect what find first. </p>
<p> This argument is optional, and defaults to zero. Modules with the same <code>priority</code> option will be sorted alphabetically.</dl>
<p> <code>remote:</code></p>
<dl>
<dd>Instead of loading the PKCS#11 module locally, run the module remotely. </p>
<p> Specify a command to run, prefixed with | a pipe. The command must speak the p11-kit remoting protocol on its standard in and standard out. For example: </p>
<dl>
<dd>
<pre>remote: |ssh user [at] remote p11-kit remote /path/to/module.so</pre>
</dl>
<p> Other forms of remoting will appear in later p11-kit releases.</dl>
<p> <code>trust-policy:</code></p>
<dl>
<dd>Set to yes to use use this module as a source of trust policy information such as certificate anchors and black lists.</dl>
<p> <code>log-calls:</code></p>
<dl>
<dd>Set to yes to write a log to stderr of all the calls into the module. This is only supported for managed modules. </p>
<p> This argument is optional and defaults to no.</dl>
<p> Do not specify both enable-in and disable-in for the same module. </p>
<p> Other fields may be present, but it is recommended that field names that are not specified in this document start with a x- prefix.</p>
<h2>Global Configuration</h2>
<p>A global configuration may also be present. This file contains settings that are not related to a single PKCS#11 module. The location(s) of the global configuration are described below. The global configuration file can contain the following fields: </p>
<p> <code>user-config:</code></p>
<dl>
<dd>This will be equal to one of the following values: none, merge, only.</dl>
<p> <code>managed:</code></p>
<dl>
<dd>Set to yes or no to force all modules to be managed or unmanaged by p11-kit. Setting this setting in a global configuration file will override the managed setting in the individual module configuration files. Making modules unmanaged is not recommended, and will cause problems if multiple callers in a single process share a PKCS#11 module. </p>
<p> This argument is optional.</dl>
<p> <code>log-calls:</code></p>
<dl>
<dd>Set to yes to write a log to stderr of all the calls into all configured modules. This is only supported for managed modules. </p>
<p> This argument is optional.</dl>
<p> Other fields may be present, but it is recommended that field names that are not specified in this document start with a x- prefix.</p>
<h2>Configuration Files</h2>
<p>Each configured PKCS#11 module has its own config file. These files are placed in a directory. In addition a global config file exists. There is a system configuration consisting of the various module config files and a file for global configuration. Optionally each user can provide additional configuration or override the system configuration. </p>
<p> The system global configuration file is usually in /etc/pkcs11/pkcs11.conf and the user global configuration file is in ~/.config/pkcs11/pkcs11.conf in the user&#8217;s home directory. </p>
<p> The module config files are usually located in the /etc/pkcs11/modules directory, with one configuration file per module. In addition the ~/.config/pkcs11/modules directory can be used for modules installed by the user. </p>
<p> Note that user configuration files are not loaded from the home directory if running inside a setuid or setgid program. </p>
<p> The default system config file and module directory can be changed when building p11-kit. Always lookup these paths using pkg-config.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-p11-kit/">p11-kit</a></code>(8) Further details available in the p11-kit online documentation at m[blue]<code><a rel="nofollow" href="https://p11-glue.github.io/p11-glue/p11-kit/manual/">https://p11-glue.github.io/p11-glue/p11-kit/manual/</a></code>m[]. </p>
