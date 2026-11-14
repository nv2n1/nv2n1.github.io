---
title: "mib2c(1)"
name: "mib2c"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mib2c/"
description: "mib2c — generate template code for extending the agent"
---

<h2>NAME</h2>
<p> mib2c &#8212; generate template code for extending the agent</p>
<h2>SYNOPSIS</h2>
<p> <code>mib2c</code> [-h] -c CONFIGFILE [-I PATH] [-f OUTNAME] [-i][-s][-q][-S VAR=VAL] MIBNODE</p>
<h2>DESCRIPTION</h2>
<p> The mib2c tool is designed to take a portion of the MIB tree (as defined by a MIB file) and generate the template C code necessary to implement the relevant management objects within it. </p>
<p> In order to implement a new MIB module, three files are necessary: </p>
<p> &#8211; MIB definition file<br />
 &#8211; C header file<br />
 &#8211; C implementation file. </p>
<p> The mib2c tool uses the MIB definition file to produce the two C code files. Thus, mib2c generates a template that you can edit to add logic necessary to obtain information from the operating system or application to complete the module. </p>
<p> MIBNODE is the top level mib node you want to generate code for. You must give mib2c a mib node (e.g. ifTable) on the command line, not a mib file. This is the single most common mistake. </p>
<p> The mib2c tool accepts both SMIv1 and SMIv2 MIBs. </p>
<p> mib2c needs to be able to find and load a MIB file in order to generate C code for the MIB. To enable mib2c to find the MIB file, set the MIBS environment variable to include the MIB file you are using. An example of setting this environment variable is: </p>
<p>MIBS=+NET-SNMP-TUTORIAL-MIB </p>
<p>or </p>
<p>MIBS=ALL </p>
<p> The first example ensures that mib2c finds the NET-SNMP-TUTORIAL-MIB mib, in addition to the default MIB modules. The default list of MIB modules is set when the suite is first configured and built and basically corresponds to the list of modules that the agent supports. The second example ensures that mib2c finds all MIBs in the search location for MIB files. The default search location for MIB files is /usr/share/snmp/mibs. This search location can be modified by the MIBDIRS environment variable. </p>
<p> Both the MIB files to be loaded and the MIB file search location can also be configured in the snmp.conf file. Please see <a href="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5) for more information. </p>
<p> The generated *.c and *.h files will be created in the current working directory.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display a help message.</p>
<dt><code>-c</code><i> CONFIGFILE</i></p>
<dd> Use CONFIGFILE when generating code. These files will be searched for first in the current directory and then in the /usr/share directory (which is where the default mib2c configuration files can be found). Running mib2c without the -c CONFIGFILE option will display a description of the valid values for CONFIGFILE, that is, the available config files, including new ones that you might author.</p>
<dt>
<dd> For example,</p>
<dt>
<dd> % mib2c ifTable</p>
<dt>
<dd> will display a description of the currently available values for CONFIGFILE.</p>
<dt>
<dd> The following values are supported for CONFIGFILE:</p>
<dt>
<dd> mib2c.mfd.conf<br />
 mib2c.scalar.conf<br />
 mib2c.int_watch.conf<br />
 mib2c.iterate.conf<br />
 mib2c.create-dataset.conf<br />
 mib2c.array-user.conf<br />
 mib2c.column_defines.conf<br />
 mib2c.column_enums.conf</p>
<dt>
<dd> GENERATING CODE FOR SCALAR OBJECTS:</p>
<dt>
<dd> If you&#8217;re writing code for some scalars, run: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mib2c -c mib2c.scalar.conf MIBNODE</p>
<dt>
<dd> If you want to magically &quot;tie&quot; integer variables to integer scalars, use: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mib2c -c mib2c.int_watch.conf MIBNODE</p>
<dt>
<dd> GENERATING CODE FOR TABLES: </p>
<p> The recommended configuration file for tables is the MIBs for Dummies, or MFD, configuration file. It hides as much of the SNMP details as possible, generating small, easy to understand functions. It is also the most flexible and well documented configuration file. See the agent/mibgroup/if-mib/ifTable/ifTable*.c files for an example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>mib2c -c mib2c.mfd.conf MIBNODE </p>
<p> If your table data is kept somewhere else (e.g. it&#8217;s in the kernel and not in the memory of the agent itself) and you need to &quot;iterate&quot; over it to find the right data for the SNMP row being accessed. See the agent/mibgroup/mibII/vacm_context.c file for an example: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mib2c -c mib2c.iterate.conf MIBNODE</p>
<p> If your table data is kept in the agent (i.e. it&#8217;s not located in an external source) and is purely data driven (i.e. you do not need to perform any work when a set occurs). See the agent/mibgroup/examples/data_set.c file for an example of such a table: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mib2c -c mib2c.create-dataset.conf MIBNODE</p>
<p> If your table data is kept in the agent (i.e. it&#8217;s not located in an external source), and you can keep your data sorted by the table index but you do need to perform work when a set occurs: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mib2c -c mib2c.array-user.conf MIBNODE</p>
<p> GENERATING HEADER FILE DEFINITIONS </p>
<p> To generate just a header with a define for each column number in your table: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mib2c -c mib2c.column_defines.conf MIBNODE</p>
<p> To generate just a header with a define for each enum for any column containing enums: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mib2c -c mib2c.column_enums.conf MIBNODE</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>GENERATING CODE FOR THE 4.X LINE OF CODE (THE OLDER API)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>mib2c -c mib2c.old-api.conf MIBNODE</p>
<dt><code>-I</code><i>PATH</i></p>
<dd> Search for configuration files in PATH. Multiple paths can be specified using multiple -I switches or by using one with a comma separated list of paths in it.</p>
<dt><code>-f</code><i> OUTNAME</i></p>
<dd> Places the output code into OUTNAME.c and OUTNAME.h. Normally, mib2c will place the output code into files which correspond to the table names it is generating code for, which is probably what you want anyway.</p>
<dt><code>-i</code></p>
<dd> Do not run indent on the resulting code.</p>
<dt><code>-s</code></p>
<dd> Do not look for MIBNODE.sed and run sed on the resulting code. This is useful to shorten long mib variable names in the code.</p>
<dt><code>-q</code></p>
<dd> Run in &quot;quiet&quot; mode, which minimizes the status messages mib2c generates.</p>
<dt><code>-S</code><i>VAR=VAL</i></p>
<dd> Preset a variable VAR, in the mib2c.*.conf file, to the value VAL. None of the existing mib2c configuration files (mib2c.*.conf) currently makes use of this feature, however, so this option should be considered available only for future use.</dl>
<h2>EXAMPLES</h2>
<p> The following generates C template code for the header and implementation files to implement UCD-DEMO-MIB::ucdDemoPublic.</p>
<dl>
<dt>
<dd> % mib2c -c mib2c.scalar.conf ucdDemoPublic<br />
 writing to ucdDemoPublic.h<br />
 writing to ucdDemoPublic.c<br />
 running indent on ucdDemoPublic.h<br />
 running indent on ucdDemoPublic.c</dl>
<p> The resulting ucdDemoPublic.c and ucdDemoPublic.h files are generated the current working directory. </p>
<p> The following generates C template code for the header and implementation files for the module to implement TCP-MIB::tcpConnTable.</p>
<dl>
<dt>
<dd> % mib2c -c mib2c.iterate.conf tcpConnTable<br />
 writing to tcpConnTable.h<br />
 writing to tcpConnTable.c<br />
 running indent on tcpConnTable.h<br />
 running indent on tcpConnTable.c</dl>
<p> The resulting tcpConnTable.c and tcpConnTable.h files are generated in the current working directory. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5) </p>
<h2>Index</h2>
