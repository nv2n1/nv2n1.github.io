---
title: "modutil(1)"
name: "modutil"
section: "1"
letter: "m"
url: "/docs/linux/man/1-modutil/"
description: "modutil – Manage PKCS #11 module information within the security module database."
---

<h2 class="name">NAME</h2>
<p> modutil &#8211; Manage PKCS #11 module information within the security module database. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>modutil</code> [<i>options</i>] [[<i>arguments</i>]]</dl>
<h2>STATUS</h2>
<dd>This documentation is still work in progress. Please contribute to the initial review in m[blue]<code>Mozilla NSS bug 836477</code>m[]<font SIZE="-2">[1]</font></p>
<h2>DESCRIPTION</h2>
<p> The Security Module Database Tool, <code>modutil</code>, is a command-line utility for managing PKCS #11 module information both within secmod.db files and within hardware tokens. <code>modutil</code> can add and delete PKCS #11 modules, change passwords on security databases, set defaults, list module contents, enable or disable slots, enable or disable FIPS 140-2 compliance, and assign default providers for cryptographic operations. This tool can also create certificate, key, and module security database files. </p>
<p> The tasks associated with security module database management are part of a process that typically also involves managing key databases and certificate databases.</p>
<h2>OPTIONS</h2>
<p> Running <code>modutil</code> always requires one (and only one) option to specify the type of module operation. Each option may take arguments, anywhere from none to multiple arguments. </p>
<p> <code>Options</code> </p>
<p> -add modulename</p>
<dl>
<dt>
<dd> Add the named PKCS #11 module to the database. Use this option with the <code>-libfile</code>, <code>-ciphers</code>, and <code>-mechanisms</code> arguments.</dl>
<p> -changepw tokenname</p>
<dl>
<dt>
<dd> Change the password on the named token. If the token has not been initialized, this option initializes the password. Use this option with the <code>-pwfile</code> and <code>-newpwfile</code> arguments. A <i>password</i> is equivalent to a personal identification number (PIN).</dl>
<p> -chkfips</p>
<dl>
<dt>
<dd> Verify whether the module is in the given FIPS mode. <code>true</code> means to verify that the module is in FIPS mode, while <code>false</code> means to verify that the module is not in FIPS mode.</dl>
<p> -create</p>
<dl>
<dt>
<dd> Create new certificate, key, and module databases. Use the <code>-dbdir</code> directory argument to specify a directory. If any of these databases already exist in a specified directory, <code>modutil</code> returns an error message.</dl>
<p> -default modulename</p>
<dl>
<dt>
<dd> Specify the security mechanisms for which the named module will be a default provider. The security mechanisms are specified with the <code>-mechanisms</code> argument.</dl>
<p> -delete modulename</p>
<dl>
<dt>
<dd> Delete the named module. The default NSS PKCS #11 module cannot be deleted.</dl>
<p> -disable modulename</p>
<dl>
<dt>
<dd> Disable all slots on the named module. Use the <code>-slot</code> argument to disable a specific slot. </p>
<p> The internal NSS PKCS #11 module cannot be disabled.</dl>
<p> -enable modulename</p>
<dl>
<dt>
<dd> Enable all slots on the named module. Use the <code>-slot</code> argument to enable a specific slot.</dl>
<p> -fips [true | false]</p>
<dl>
<dt>
<dd> Enable (true) or disable (false) FIPS 140-2 compliance for the default NSS module.</dl>
<p> -force</p>
<dl>
<dt>
<dd> Disable <code>modutil</code>&#8216;s interactive prompts so it can be run from a script. Use this option only after manually testing each planned operation to check for warnings and to ensure that bypassing the prompts will cause no security lapses or loss of database integrity.</dl>
<p> -jar JAR-file</p>
<dl>
<dt>
<dd> Add a new PKCS #11 module to the database using the named JAR file. Use this command with the <code>-installdir</code> and <code>-tempdir</code> arguments. The JAR file uses the NSS PKCS #11 JAR format to identify all the files to be installed, the module&#8217;s name, the mechanism flags, and the cipher flags, as well as any files to be installed on the target machine, including the PKCS #11 module library file and other files such as documentation. This is covered in the JAR installation file section in the man page, which details the special script needed to perform an installation through a server or with <code>modutil</code>.</dl>
<p> -list [modulename]</p>
<dl>
<dt>
<dd> Display basic information about the contents of the secmod.db file. Specifying a <i>modulename</i> displays detailed information about a particular module and its slots and tokens.</dl>
<p> -rawadd</p>
<dl>
<dt>
<dd> Add the module spec string to the secmod.db database.</dl>
<p> -rawlist</p>
<dl>
<dt>
<dd> Display the module specs for a specified module or for all loadable modules.</dl>
<p> -undefault modulename</p>
<dl>
<dt>
<dd> Specify the security mechanisms for which the named module will not be a default provider. The security mechanisms are specified with the <code>-mechanisms</code> argument.</dl>
<p> <code>Arguments</code> </p>
<p> MODULE</p>
<dl>
<dt>
<dd> Give the security module to access.</dl>
<p> MODULESPEC</p>
<dl>
<dt>
<dd> Give the security module spec to load into the security database.</dl>
<p> -ciphers cipher-enable-list</p>
<dl>
<dt>
<dd> Enable specific ciphers in a module that is being added to the database. The <i>cipher-enable-list</i> is a colon-delimited list of cipher names. Enclose this list in quotation marks if it contains spaces.</dl>
<p> -dbdir [sql:]directory</p>
<dl>
<dt>
<dd> Specify the database directory in which to access or create security module database files. </p>
<p> <code>modutil</code> supports two types of databases: the legacy security databases (cert8.db, key3.db, and secmod.db) and new SQLite databases (cert9.db, key4.db, and pkcs11.txt). If the prefix <code>sql:</code> is not used, then the tool assumes that the given databases are in the old format.</dl>
<p> &#8211;dbprefix prefix</p>
<dl>
<dt>
<dd> Specify the prefix used on the database files, such as my_ for my_cert8.db. This option is provided as a special case. Changing the names of the certificate and key databases is not recommended.</dl>
<p> -installdir root-installation-directory</p>
<dl>
<dt>
<dd> Specify the root installation directory relative to which files will be installed by the <code>-jar</code> option. This directory should be one below which it is appropriate to store dynamic library files, such as a server&#8217;s root directory.</dl>
<p> -libfile library-file</p>
<dl>
<dt>
<dd> Specify a path to a library file containing the implementation of the PKCS #11 interface module that is being added to the database.</dl>
<p> -mechanisms mechanism-list</p>
<dl>
<dt>
<dd> Specify the security mechanisms for which a particular module will be flagged as a default provider. The <i>mechanism-list</i> is a colon-delimited list of mechanism names. Enclose this list in quotation marks if it contains spaces. </p>
<p> The module becomes a default provider for the listed mechanisms when those mechanisms are enabled. If more than one module claims to be a particular mechanism&#8217;s default provider, that mechanism&#8217;s default provider is undefined. </p>
<p> <code>modutil</code> supports several mechanisms: RSA, DSA, RC2, RC4, RC5, AES, DES, DH, SHA1, SHA256, SHA512, SSL, TLS, MD5, MD2, RANDOM (for random number generation), and FRIENDLY (meaning certificates are publicly readable).</dl>
<p> -newpwfile new-password-file</p>
<dl>
<dt>
<dd> Specify a text file containing a token&#8217;s new or replacement password so that a password can be entered automatically with the <code>-changepw</code> option.</dl>
<p> -nocertdb</p>
<dl>
<dt>
<dd> Do not open the certificate or key databases. This has several effects: </p>
<dl>
<dt>
<dd> &bull; With the <code>-create</code> command, only a module security file is created; certificate and key databases are not created.</dl>
<dl>
<dt>
<dd> &bull; With the <code>-jar</code> command, signatures on the JAR file are not checked.</dl>
<dl>
<dt>
<dd> &bull; With the <code>-changepw</code> command, the password on the NSS internal module cannot be set or changed, since this password is stored in the key database.</dl>
</dl>
<p> -pwfile old-password-file</p>
<dl>
<dt>
<dd> Specify a text file containing a token&#8217;s existing password so that a password can be entered automatically when the <code>-changepw</code> option is used to change passwords.</dl>
<p> -secmod secmodname</p>
<dl>
<dt>
<dd> Give the name of the security module database (like secmod.db) to load.</dl>
<p> -slot slotname</p>
<dl>
<dt>
<dd> Specify a particular slot to be enabled or disabled with the <code>-enable</code> or <code>-disable</code> options.</dl>
<p> -string CONFIG_STRING</p>
<dl>
<dt>
<dd> Pass a configuration string for the module being added to the database.</dl>
<p> -tempdir temporary-directory</p>
<dl>
<dt>
<dd> Give a directory location where temporary files are created during the installation by the <code>-jar</code> option. If no temporary directory is specified, the current directory is used.</dl>
<h2>USAGE AND EXAMPLES</h2>
<p> <code>Creating Database Files</code> </p>
<p> Before any operations can be performed, there must be a set of security databases available. <code>modutil</code> can be used to create these files. The only required argument is the database that where the databases will be located. </p>
<dl>
<dt>
<dd>
<pre>
modutil -create -dbdir [sql:]directory
</pre>
</dl>
<p> <code>Adding a Cryptographic Module</code> </p>
<p> Adding a PKCS #11 module means submitting a supporting library file, enabling its ciphers, and setting default provider status for various security mechanisms. This can be done by supplying all of the information through <code>modutil</code> directly or by running a JAR file and install script. For the most basic case, simply upload the library: </p>
<dl>
<dt>
<dd>
<pre><code>
modutil - add modulename - libfile library - file[-ciphers cipher - enable - list][-mechanisms mechanism - list]
</code></pre>
</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
modutil -dbdir sql:/home/my/sharednssdb -add &quot;Example PKCS #11 Module&quot; -libfile &quot;/tmp/crypto.so&quot; -mechanisms RSA:DSA:RC2:RANDOM 
Using database directory ... 
Module &quot;Example PKCS #11 Module&quot; added to database.
</pre>
</dl>
<p> <code>Installing a Cryptographic Module from a JAR File</code> </p>
<p> PKCS #11 modules can also be loaded using a JAR file, which contains all of the required libraries and an installation script that describes how to install the module. The JAR install script is described in more detail in the section called &#8220;JAR INSTALLATION FILE FORMAT&#8221;. </p>
<p> The JAR installation script defines the setup information for each platform that the module can be installed on. For example: </p>
<dl>
<dt>
<dd>
Platforms<br />
{<br />
Linux:<br />
    5.4.08 : x86<br />
    {<br />
        ModuleName{&#8220;Example PKCS #11 Module&#8221;} ModuleFile{crypto.so} DefaultMechanismFlags{0x0000} CipherEnableFlags{0x0000} Files<br />
        {<br />
            crypto.so<br />
            {<br />
                Path<br />
                {<br />
                    / tmp / crypto.so<br />
                }<br />
            }<br />
            setup.sh<br />
            {<br />
                Executable<br />
                    Path<br />
                {<br />
                    / tmp / setup.sh<br />
                }<br />
            }<br />
        }<br />
    }<br />
Linux:<br />
    6.0.0 : x86<br />
    {<br />
        EquivalentPlatform<br />
        {<br />
        Linux:<br />
            5.4.08 : x86<br />
        }<br />
    }<br />
}
</dl>
<p> Both the install script and the required libraries must be bundled in a JAR file, which is specified with the <code>-jar</code> argument. </p>
<dl>
<dt>
<dd>
modutil -dbdir sql:/home/mt&#8221;jar-install-filey/sharednssdb -jar install.jar -installdir sql:/home/my/sharednssdb<br />
This installation JAR file was signed by:<br />
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
**SUBJECT NAME**<br />
C=US, ST=California, L=Mountain View, CN=Cryptorific Inc., OU=Digital ID<br />
Class 3 &#8211; Netscape Object Signing, OU=&#8221;www.verisign.com/repository/CPS<br />
Incorp. by Ref.,LIAB.LTD(c)9 6&#8243;, OU=www.verisign.com/CPS Incorp.by Ref<br />
. LIABILITY LTD.(c)97 VeriSign, OU=VeriSign Object Signing CA &#8211; Class 3<br />
Organization, OU=&#8221;VeriSign, Inc.&#8221;, O=VeriSign Trust Network **ISSUER<br />
NAME**, OU=www.verisign.com/CPS Incorp.by Ref. LIABILITY LTD.(c)97<br />
VeriSign, OU=VeriSign Object Signing CA &#8211; Class 3 Organization,<br />
OU=&#8221;VeriSign, Inc.&#8221;, O=VeriSign Trust Network<br />
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
Do you wish to continue this installation? (y/n) y<br />
Using installer script &#8220;installer_script&#8221;<br />
Successfully parsed installation script<br />
Current platform is Linux:5.4.08:x86<br />
Using installation parameters for platform Linux:5.4.08:x86<br />
Installed file crypto.so to /tmp/crypto.so<br />
Installed file setup.sh to ./pk11inst.dir/setup.sh<br />
Executing &#8220;./pk11inst.dir/setup.sh&#8221;&#8230;<br />
&#8220;./pk11inst.dir/setup.sh&#8221; executed successfully<br />
Installed module &#8220;Example PKCS #11 Module&#8221; into module database<br />
Installation completed successfully
</dl>
<p> <code>Adding Module Spec</code> </p>
<p> Each module has information stored in the security database about its configuration and parameters. These can be added or edited using the <code>-rawadd</code> command. For the current settings or to see the format of the module spec in the database, use the <code>-rawlist</code> option. </p>
<dl>
<dt>
<dd>
<pre>
modutil -rawadd modulespec
</pre>
</dl>
<p> <code>Deleting a Module</code> </p>
<p> A specific PKCS #11 module can be deleted from the secmod.db database: </p>
<dl>
<dt>
<dd>
<pre>
modutil -delete modulename -dbdir [sql:]directory 
</pre>
</dl>
<p> <code>Displaying Module Information</code> </p>
<p> The secmod.db database contains information about the PKCS #11 modules that are available to an application or server to use. The list of all modules, information about specific modules, and database configuration specs for modules can all be viewed. </p>
<p> To simply get a list of modules in the database, use the <code>-list</code> command. </p>
<dl>
<dt>
<dd>
modutil &#8211; list[modulename] &#8211; dbdir [sql:] directory
</dl>
<p> Listing the modules shows the module name, their status, and other associated security databases for certificates and keys. For example: </p>
<dl>
<dt>
<dd>
modutil &#8211; list &#8211; dbdir sql : / home / my / sharednssdb Listing of PKCS #11 Modules&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -1. NSS Internal PKCS #11 Module slots : 2 slots attached status : loaded slot : NSS Internal Cryptographic Services token : NSS Generic Crypto Services slot : NSS User Private Key and Certificate Services token : NSS Certificate DB&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;
</dl>
<p> Passing a specific module name with the <code>-list</code> returns details information about the module itself, like supported cipher mechanisms, version numbers, serial numbers, and other information about the module and the token it is loaded on. For example: </p>
<dl>
<dt>
<dd>
modutil &#8211; list &#8220;NSS Internal PKCS #11 Module&#8221; &#8211; dbdir sql : / home / my / sharednssdb&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -Name : NSS Internal PKCS #11 Module Library file : **Internal ONLY module **Manufacturer : Mozilla Foundation Description : NSS Internal Crypto Services PKCS #11 Version 2.20 Library Version : 3.11 Cipher Enable Flags : None Default Mechanism Flags : RSA : RC2 : RC4 : DES : DH : SHA1 : MD5 : MD2 : SSL : TLS : AES Slot : NSS Internal Cryptographic Services Slot Mechanism Flags : RSA : RC2 : RC4 : DES : DH : SHA1 : MD5 : MD2 : SSL : TLS : AES Manufacturer : Mozilla Foundation Type : Software Version Number : 3.11 Firmware Version : 0.0 Status : Enabled Token Name : NSS Generic Crypto Services Token Manufacturer : Mozilla Foundation Token Model : NSS 3 Token Serial Number : 0000000000000000 Token Version : 4.0 Token Firmware Version : 0.0 Access : Write Protected Login Type : Public(no login required) User Pin : NOT Initialized Slot : NSS User Private Key and Certificate Services Slot Mechanism Flags : None Manufacturer : Mozilla Foundation Type : Software Version Number : 3.11 Firmware Version : 0.0 Status : Enabled Token Name : NSS Certificate DB Token Manufacturer : Mozilla Foundation Token Model : NSS 3 Token Serial Number : 0000000000000000 Token Version : 8.3 Token Firmware Version : 0.0 Access : NOT Write Protected Login Type : Login required User Pin : Initialized
</dl>
<p> A related command, <code>-rawlist</code> returns information about the database configuration for the modules. (This information can be edited by loading new specs using the <code>-rawadd</code> command.) </p>
<dl>
<dt>
<dd>
modutil &#8211; rawlist &#8211; dbdir sql : / home / my / sharednssdb name = &#8220;NSS Internal PKCS #11 Module&#8221; parameters = &#8220;configdir=. certPrefix= keyPrefix= secmod=secmod.db flags=readOnly &#8221; NSS = &#8220;trustOrder=75 cipherOrder=100 slotParams={0x00000001=[slotFlags=RSA,RC4,RC2,DES,DH,SHA1,MD5,MD2,SSL,TLS,AES,RANDOM askpw=any timeout=30 ] }  Flags=internal,critical&#8221;
</dl>
<p> <code>Setting a Default Provider for Security Mechanisms</code> </p>
<p> Multiple security modules may provide support for the same security mechanisms. It is possible to set a specific security module as the default provider for a specific security mechanism (or, conversely, to prohibit a provider from supplying those mechanisms). </p>
<dl>
<dt>
<dd>
<pre>
modutil -default modulename -mechanisms mechanism-list 
</pre>
</dl>
<p> To set a module as the default provider for mechanisms, use the <code>-default</code> command with a colon-separated list of mechanisms. The available mechanisms depend on the module; NSS supplies almost all common mechanisms. For example: </p>
<dl>
<dt>
<dd>
<pre>
modutil -default &quot;NSS Internal PKCS #11 Module&quot; -dbdir -mechanisms RSA:DSA:RC2 
Using database directory c:\databases...
Successfully changed defaults.
</pre>
</dl>
<p> Clearing the default provider has the same format: </p>
<dl>
<dt>
<dd>
<pre>
modutil -undefault &quot;NSS Internal PKCS #11 Module&quot; -dbdir -mechanisms MD2:MD5
</pre>
</dl>
<p> <code>Enabling and Disabling Modules and Slots</code> </p>
<p> Modules, and specific slots on modules, can be selectively enabled or disabled using <code>modutil</code>. Both commands have the same format: </p>
<dl>
<dt>
<dd>
<pre>
modutil -enable|-disable modulename [-slot slotname] 
</pre>
</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
modutil -enable &quot;NSS Internal PKCS #11 Module&quot; -slot &quot;NSS Internal Cryptographic Services                            &quot; -dbdir .
Slot &quot;NSS Internal Cryptographic Services                            &quot; enabled.
</pre>
</dl>
<p> Be sure that the appropriate amount of trailing whitespace is after the slot name. Some slot names have a significant amount of whitespace that must be included, or the operation will fail. </p>
<p> <code>Enabling and Verifying FIPS Compliance</code> </p>
<p> The NSS modules can have FIPS 140-2 compliance enabled or disabled using <code>modutil</code> with the <code>-fips</code> option. For example: </p>
<dl>
<dt>
<dd>
<pre>
modutil -fips true -dbdir sql:/home/my/sharednssdb/
FIPS mode enabled.
</pre>
</dl>
<p> To verify that status of FIPS mode, run the <code>-chkfips</code> command with either a true or false flag (it doesn&#8217;t matter which). The tool returns the current FIPS setting. </p>
<dl>
<dt>
<dd>
<pre>
modutil -chkfips false -dbdir sql:/home/my/sharednssdb/
FIPS mode enabled.
</pre>
</dl>
<p> <code>Changing the Password on a Token</code> </p>
<p> Initializing or changing a token&#8217;s password: </p>
<dl>
<dt>
<dd>
modutil &#8211; changepw tokenname[-pwfile old &#8211; password &#8211; file][-newpwfile new &#8211; password &#8211; file]
</dl>
<dl>
<dt>
<dd>
<pre>
modutil -dbdir sql:/home/my/sharednssdb -changepw &quot;NSS Certificate DB&quot; 
Enter old password: 
Incorrect password, try again... 
Enter old password: 
Enter new password: 
Re-enter new password: 
Token &quot;Communicator Certificate DB&quot; password changed successfully.
</pre>
</dl>
<h2>JAR INSTALLATION FILE FORMAT</h2>
<p> When a JAR file is run by a server, by <code>modutil</code>, or by any program that does not interpret JavaScript, a special information file must be included to install the libraries. There are several things to keep in mind with this file: </p>
<dl>
<dt>
<dd> &bull; It must be declared in the JAR archive&#8217;s manifest file.</dl>
<dl>
<dt>
<dd> &bull; The script can have any name.</dl>
<dl>
<dt>
<dd> &bull; The metainfo tag for this is <code>Pkcs11_install_script</code>. To declare meta-information in the manifest file, put it in a file that is passed to <code>signtool</code>.</dl>
<p> <code>Sample Script</code> </p>
<p> For example, the PKCS #11 installer script could be in the file pk11install. If so, the metainfo file for <code>signtool</code> includes a line such as this: </p>
<dl>
<dt>
<dd>
<pre>
+ Pkcs11_install_script: pk11install
</pre>
</dl>
<p> The script must define the platform and version number, the module name and file, and any optional information like supported ciphers and mechanisms. Multiple platforms can be defined in a single install file. </p>
<dl>
<dt>
<dd>
ForwardCompatible{IRIX : 6.2 : mips SUNOS : 5.5.1 : sparc} Platforms<br />
{<br />
    WINNT::x86<br />
    {<br />
        ModuleName{&#8220;Example Module&#8221;} ModuleFile{win32 / fort32.dll} DefaultMechanismFlags{0x0001} DefaultCipherFlags{0x0001} Files<br />
        {<br />
            win32 / setup.exe<br />
            {<br />
                Executable<br />
                    RelativePath<br />
                {<br />
                    % temp % / setup.exe<br />
                }<br />
            }<br />
            win32 / setup.hlp<br />
            {<br />
                RelativePath<br />
                {<br />
                    % temp % / setup.hlp<br />
                }<br />
            }<br />
            win32 / setup.cab<br />
            {<br />
                RelativePath<br />
                {<br />
                    % temp % / setup.cab<br />
                }<br />
            }<br />
        }<br />
    }<br />
    WIN95::x86<br />
    {<br />
        EquivalentPlatform<br />
        {<br />
            WINNT::x86<br />
        }<br />
    }<br />
SUNOS:<br />
    5.5.1 : sparc<br />
    {<br />
        ModuleName{&#8220;Example UNIX Module&#8221;} ModuleFile{unix / fort.so} DefaultMechanismFlags{0x0001} CipherEnableFlags{0x0001} Files<br />
        {<br />
            unix / fort.so<br />
            {<br />
                RelativePath{ % root % / lib / fort.so} AbsolutePath{ / usr / local / netscape / lib / fort.so} FilePermissions<br />
                {<br />
                    555<br />
                }<br />
            }<br />
            xplat / instr.html<br />
            {<br />
                RelativePath{ % root % / docs / inst.html} AbsolutePath{ / usr / local / netscape / docs / inst.html} FilePermissions<br />
                {<br />
                    555<br />
                }<br />
            }<br />
        }<br />
    }<br />
IRIX:<br />
    6.2 : mips<br />
    {<br />
        EquivalentPlatform<br />
        {<br />
        SUNOS:<br />
            5.5.1 : sparc<br />
        }<br />
    }<br />
}
</dl>
<p> <code>Script Grammar</code> </p>
<p> The script is basic Java, allowing lists, key-value pairs, strings, and combinations of all of them. </p>
<dl>
<dt>
<dd>
<pre><code>
--&gt; valuelist
valuelist --&gt; value valuelist
               &lt;null&gt;
value ---&gt; key_value_pair
            string
key_value_pair --&gt; key { valuelist }
key --&gt; string
string --&gt; simple_string
            "complex_string"
simple_string --&gt; [^ 	
\""{
    ""}"]+ 
complex_string --&gt; ([^\"\
]|(\\")|(\\))+ 
</code></pre>
</dl>
<p> Quotes and backslashes must be escaped with a backslash. A complex string must not include newlines or carriage returns.Outside of complex strings, all white space (for example, spaces, tabs, and carriage returns) is considered equal and is used only to delimit tokens. </p>
<p> <code>Keys</code> </p>
<p> The Java install file uses keys to define the platform and module information. </p>
<p> <code>ForwardCompatible</code> gives a list of platforms that are forward compatible. If the current platform cannot be found in the list of supported platforms, then the <code>ForwardCompatible</code> list is checked for any platforms that have the same OS and architecture in an earlier version. If one is found, its attributes are used for the current platform. </p>
<p> <code>Platforms</code> (required) Gives a list of platforms. Each entry in the list is itself a key-value pair: the key is the name of the platform and the value list contains various attributes of the platform. The platform string is in the format <i>system name:OS release:architecture</i>. The installer obtains these values from NSPR. OS release is an empty string on non-Unix operating systems. NSPR supports these platforms: </p>
<dl>
<dt>
<dd> &bull; AIX (rs6000)</dl>
<dl>
<dt>
<dd> &bull; BSDI (x86)</dl>
<dl>
<dt>
<dd> &bull; FREEBSD (x86)</dl>
<dl>
<dt>
<dd> &bull; HPUX (hppa1.1)</dl>
<dl>
<dt>
<dd> &bull; IRIX (mips)</dl>
<dl>
<dt>
<dd> &bull; LINUX (ppc, alpha, x86)</dl>
<dl>
<dt>
<dd> &bull; MacOS (PowerPC)</dl>
<dl>
<dt>
<dd> &bull; NCR (x86)</dl>
<dl>
<dt>
<dd> &bull; NEC (mips)</dl>
<dl>
<dt>
<dd> &bull; OS2 (x86)</dl>
<dl>
<dt>
<dd> &bull; OSF (alpha)</dl>
<dl>
<dt>
<dd> &bull; ReliantUNIX (mips)</dl>
<dl>
<dt>
<dd> &bull; SCO (x86)</dl>
<dl>
<dt>
<dd> &bull; SOLARIS (sparc)</dl>
<dl>
<dt>
<dd> &bull; SONY (mips)</dl>
<dl>
<dt>
<dd> &bull; SUNOS (sparc)</dl>
<dl>
<dt>
<dd> &bull; UnixWare (x86)</dl>
<dl>
<dt>
<dd> &bull; WIN16 (x86)</dl>
<dl>
<dt>
<dd> &bull; WIN95 (x86)</dl>
<dl>
<dt>
<dd> &bull; WINNT (x86)</dl>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
IRIX:6.2:mips
SUNOS:5.5.1:sparc
Linux:2.0.32:x86
WIN95::x86
</pre>
</dl>
<p> The module information is defined independently for each platform in the <code>ModuleName</code>, <code>ModuleFile</code>, and <code>Files</code> attributes. These attributes must be given unless an <code>EquivalentPlatform</code> attribute is specified. </p>
<p> <code>Per-Platform Keys</code> </p>
<p> Per-platform keys have meaning only within the value list of an entry in the <code>Platforms</code> list. </p>
<p> <code>ModuleName</code> (required) gives the common name for the module. This name is used to reference the module by servers and by the <code>modutil</code> tool. </p>
<p> <code>ModuleFile</code> (required) names the PKCS #11 module file for this platform. The name is given as the relative path of the file within the JAR archive. </p>
<p> <code>Files</code> (required) lists the files that need to be installed for this module. Each entry in the file list is a key-value pair. The key is the path of the file in the JAR archive, and the value list contains attributes of the file. At least <code>RelativePath</code> or <code>AbsolutePath</code> must be specified for each file. </p>
<p> <code>DefaultMechanismFlags</code> specifies mechanisms for which this module is the default provider; this is equivalent to the <code>-mechanism</code> option with the <code>-add</code> command. This key-value pair is a bitstring specified in hexadecimal (0x) format. It is constructed as a bitwise OR. If the DefaultMechanismFlags entry is omitted, the value defaults to 0x0. </p>
<dl>
<dt>
<dd>
<pre>
RSA:                   0x00000001
DSA:                   0x00000002
RC2:                   0x00000004
RC4:                   0x00000008
DES:                   0x00000010
DH:                    0x00000020
FORTEZZA:              0x00000040
RC5:                   0x00000080
SHA1:                  0x00000100
MD5:                   0x00000200
MD2:                   0x00000400
RANDOM:                0x08000000
FRIENDLY:              0x10000000
OWN_PW_DEFAULTS:       0x20000000
DISABLE:               0x40000000
</pre>
</dl>
<p> <code>CipherEnableFlags</code> specifies ciphers that this module provides that NSS does not provide (so that the module enables those ciphers for NSS). This is equivalent to the <code>-cipher</code> argument with the <code>-add</code> command. This key is a bitstring specified in hexadecimal (0x) format. It is constructed as a bitwise OR. If the <code>CipherEnableFlags</code> entry is omitted, the value defaults to 0x0. </p>
<p> <code>EquivalentPlatform</code> specifies that the attributes of the named platform should also be used for the current platform. This makes it easier when more than one platform uses the same settings. </p>
<p> <code>Per-File Keys</code> </p>
<p> Some keys have meaning only within the value list of an entry in a <code>Files</code> list. </p>
<p> Each file requires a path key the identifies where the file is. Either <code>RelativePath</code> or <code>AbsolutePath</code> must be specified. If both are specified, the relative path is tried first, and the absolute path is used only if no relative root directory is provided by the installer program. </p>
<p> <code>RelativePath</code> specifies the destination directory of the file, relative to some directory decided at install time. Two variables can be used in the relative path: <code>%root%</code> and <code>%temp%</code>. <code>%root%</code> is replaced at run time with the directory relative to which files should be installed; for example, it may be the server&#8217;s root directory. The <code>%temp%</code> directory is created at the beginning of the installation and destroyed at the end. The purpose of <code>%temp%</code> is to hold executable files (such as setup programs) or files that are used by these programs. Files destined for the temporary directory are guaranteed to be in place before any executable file is run; they are not deleted until all executable files have finished. </p>
<p> <code>AbsolutePath</code> specifies the destination directory of the file as an absolute path. </p>
<p> <code>Executable</code> specifies that the file is to be executed during the course of the installation. Typically, this string is used for a setup program provided by a module vendor, such as a self-extracting setup executable. More than one file can be specified as executable, in which case the files are run in the order in which they are specified in the script file. </p>
<p> <code>FilePermissions</code> sets permissions on any referenced files in a string of octal digits, according to the standard Unix format. This string is a bitwise OR. </p>
<dl>
<dt>
<dd>
<pre>
user read:                0400
user write:               0200
user execute:             0100
group read:               0040
group write:              0020
group execute:            0010
other read:               0004
other write:              0002
other execute:            0001
</pre>
</dl>
<p> Some platforms may not understand these permissions. They are applied only insofar as they make sense for the current platform. If this attribute is omitted, a default of 777 is assumed.</p>
<h2>NSS DATABASE TYPES</h2>
<p> NSS originally used BerkeleyDB databases to store security information. The last versions of these <i>legacy</i> databases are: </p>
<dl>
<dt>
<dd> &bull; cert8.db for certificates</dl>
<dl>
<dt>
<dd> &bull; key3.db for keys</dl>
<dl>
<dt>
<dd> &bull; secmod.db for PKCS #11 module information</dl>
<p> BerkeleyDB has performance limitations, though, which prevent it from being easily used by multiple applications simultaneously. NSS has some flexibility that allows applications to use their own, independent database engine while keeping a shared database and working around the access issues. Still, NSS requires more flexibility to provide a truly shared security database. </p>
<p> In 2009, NSS introduced a new set of databases that are SQLite databases rather than BerkleyDB. These new databases provide more accessibility and performance: </p>
<dl>
<dt>
<dd> &bull; cert9.db for certificates</dl>
<dl>
<dt>
<dd> &bull; key4.db for keys</dl>
<dl>
<dt>
<dd> &bull; pkcs11.txt, which is listing of all of the PKCS #11 modules contained in a new subdirectory in the security databases directory</dl>
<p> Because the SQLite databases are designed to be shared, these are the <i>shared</i> database type. The shared database type is preferred; the legacy format is included for backward compatibility. </p>
<p> By default, the tools (<code>certutil</code>, <code>pk12util</code>, <code>modutil</code>) assume that the given security databases follow the more common legacy type. Using the SQLite databases must be manually specified by using the <code>sql:</code> prefix with the given security directory. For example: </p>
<dl>
<dt>
<dd>
<pre>
modutil -create -dbdir sql:/home/my/sharednssdb
</pre>
</dl>
<p> To set the shared database type as the default type for the tools, set the <code>NSS_DEFAULT_DB_TYPE</code> environment variable to <code>sql</code>: </p>
<dl>
<dt>
<dd>
<pre>
export NSS_DEFAULT_DB_TYPE=&quot;sql&quot;
</pre>
</dl>
<p> This line can be added to the ~/.bashrc file to make the change permanent for the user. </p>
<p> Most applications do not use the shared database by default, but they can be configured to use them. For example, this how-to article covers how to configure Firefox and Thunderbird to use the new shared NSS databases: </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB_Howto">https://wiki.mozilla.org/NSS_Shared_DB_Howto</a></dl>
<p> For an engineering draft on the changes in the shared NSS databases, see the NSS project wiki: </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB">https://wiki.mozilla.org/NSS_Shared_DB</a></dl>
<h2>SEE ALSO</h2>
<p> certutil (1) </p>
<p> pk12util (1) </p>
<p> signtool (1) </p>
<p> The NSS wiki has information on the new database design and how to configure applications to use it. </p>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB_Howto">https://wiki.mozilla.org/NSS_Shared_DB_Howto</a></dl>
<dl>
<dt>
<dd> &bull; <a rel="nofollow" href="https://wiki.mozilla.org/NSS_Shared_DB">https://wiki.mozilla.org/NSS_Shared_DB</a></dl>
<h2>ADDITIONAL RESOURCES</h2>
<p> For information about NSS and other tools related to NSS (like JSS), check out the NSS project wiki at m[blue]<code><a rel="nofollow" href="http://www.mozilla.org/projects/security/pki/nss/">http://www.mozilla.org/projects/security/pki/nss/</a></code>m[]. The NSS site relates directly to NSS code changes and releases. </p>
<p> Mailing lists: <a rel="nofollow" href="https://lists.mozilla.org/listinfo/dev-tech-crypto">https://lists.mozilla.org/listinfo/dev-tech-crypto</a> </p>
<p> IRC: Freenode at #dogtag-pki</p>
<h2>AUTHORS</h2>
<p> The NSS tools were written and maintained by developers with Netscape, Red Hat, Sun, Oracle, Mozilla, and Google. </p>
<p> Authors: Elio Maldonado &lt;emaldona [at] redhat.com&gt;, Deon Lackey &lt;dlackey [at] redhat.com&gt;.</p>
<h2>LICENSE</h2>
<p> Licensed under the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a rel="nofollow" href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a></p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Mozilla NSS bug 836477</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://bugzilla.mozilla.org/show_bug.cgi?id=836477">https://bugzilla.mozilla.org/show_bug.cgi?id=836477</a></dl>
</dl>
<h2>Index</h2>
