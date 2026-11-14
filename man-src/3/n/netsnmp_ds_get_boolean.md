---
title: "netsnmp_ds_get_boolean(3)"
name: "netsnmp_ds_get_boolean"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_ds_get_boolean/"
description: "default_store – generic storage of global data."
---

<p>default_store &#8211; generic storage of global data.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/net-snmp-config.h&gt;

#include &lt;net-snmp/config_api.h&gt;
int netsnmp_ds_set_boolean(int store, int which, int val);

int netsnmp_ds_get_boolean(int store, int which);

int netsnmp_ds_set_int(int store, int which, int val);

int netsnmp_ds_get_int(int store, int which);

int netsnmp_ds_set_string(int store, int which,

                          const char *val);

char *netsnmp_ds_get_string(int store, int which);

int netsnmp_ds_register_config(u_char type,

                               const char *ftype,

                               const char *token,

                               int store, int which);

int netsnmp_ds_register_premib(u_char type,

                               const char *ftype,

                               const char *token,

                               int store, int which);

void netsnmp_ds_shutdown(void);</code></pre>
<h2>Description</h2>
<p>The purpose of the default storage is three-fold:</p>
<dl>
<dt>1)</p>
<dd>To create a global storage space without creating a whole bunch of globally accessible variables or a whole bunch of access functions to work with more privately restricted variables.</p>
<dt>2)</p>
<dd>To provide a single location where the thread locking needs to be implemented. At the time of this writing, however, thread locking is not yet in place.</p>
<dt>3)</p>
<dd>To reduce the number of cross dependencies between code pieces that may or may not be linked together in the long run. This provides for a single location in which configuration data, for example, can be stored for a separate section of code that may not be linked in to the application in question.</dl>
<p> The functions defined here implement these goals. Currently, three data types are supported: booleans, integers, and strings. Each of these data types have separate storage spaces. In addition, the storage space for each data type is divided further by the application level. Currently, there are two storage spaces. The first is reserved for the SNMP library itself. The second is intended for use in applications and is not modified or checked by the library, and, therefore, this is the space usable by you. You can think of these storage spaces as being 3 arrays, something like bool_storage[storeid][which], int_storage[storeid][which], and string_storage[storeid][which]. The data is then accessed through the functions defined below. For data you wish to store, you should use a <i>store</i> parameter of <code>NETSNMP_DS_APPLICATION_ID</code>. The storage space used by the library (for which the <i>store</i> parameter is <code>NETSNMP_DS_LIBRARY_ID</code>) is defined in the default_store.h file, which currently contains the following defines: </p>
<pre><code>*/
/**
* @def NETSNMP_DS_LIBRARY_ID These definitions correspond with the &quot;storid&quot; argument to the API
*/
#define NETSNMP_DS_LIBRARY_ID     0
#define NETSNMP_DS_APPLICATION_ID 1
#define NETSNMP_DS_TOKEN_ID       2

/*
* These definitions correspond with the &quot;which&quot; argument to the API,
* when the storeid argument is NETSNMP_DS_LIBRARY_ID
*/
/*
* library booleans
*/
#define NETSNMP_DS_LIB_MIB_ERRORS          0
#define NETSNMP_DS_LIB_SAVE_MIB_DESCRS     1
#define NETSNMP_DS_LIB_MIB_COMMENT_TERM    2
#define NETSNMP_DS_LIB_MIB_PARSE_LABEL     3
#define NETSNMP_DS_LIB_DUMP_PACKET         4
#define NETSNMP_DS_LIB_LOG_TIMESTAMP       5
#define NETSNMP_DS_LIB_DONT_READ_CONFIGS   6    /* don't read normal config files */
#define NETSNMP_DS_LIB_DISABLE_CONFIG_LOAD      NETSNMP_DS_LIB_DONT_READ_CONFIGS
#define NETSNMP_DS_LIB_MIB_REPLACE         7    /* replace objects from latest module */
#define NETSNMP_DS_LIB_PRINT_NUMERIC_ENUM  8    /* print only numeric enum values */
#define NETSNMP_DS_LIB_PRINT_NUMERIC_OIDS  9    /* print only numeric enum values */
#define NETSNMP_DS_LIB_DONT_BREAKDOWN_OIDS 10   /* dont print oid indexes specially */
#define NETSNMP_DS_LIB_ALARM_DONT_USE_SIG  11   /* don't use the alarm() signal */
#define NETSNMP_DS_LIB_PRINT_FULL_OID      12   /* print fully qualified oids */
#define NETSNMP_DS_LIB_QUICK_PRINT         13   /* print very brief output for parsing */
#define NETSNMP_DS_LIB_RANDOM_ACCESS       14   /* random access to oid labels */
#define NETSNMP_DS_LIB_REGEX_ACCESS        15   /* regex matching to oid labels */
#define NETSNMP_DS_LIB_DONT_CHECK_RANGE    16   /* don't check values for ranges on send */
#define NETSNMP_DS_LIB_NO_TOKEN_WARNINGS   17   /* no warn about unknown config tokens */
#define NETSNMP_DS_LIB_NUMERIC_TIMETICKS   18   /* print timeticks as a number */
#define NETSNMP_DS_LIB_ESCAPE_QUOTES       19   /* shell escape quote marks in oids */
#define NETSNMP_DS_LIB_REVERSE_ENCODE      20   /* encode packets from back to front */
#define NETSNMP_DS_LIB_PRINT_BARE_VALUE    21   /* just print value (not OID = value) */
#define NETSNMP_DS_LIB_EXTENDED_INDEX      22   /* print extended index format [x1][x2] */
#define NETSNMP_DS_LIB_PRINT_HEX_TEXT      23   /* print ASCII text along with hex strings */
#define NETSNMP_DS_LIB_PRINT_UCD_STYLE_OID 24   /* print OID's using the UCD-style prefix suppression */
#define NETSNMP_DS_LIB_READ_UCD_STYLE_OID  25   /* require top-level OIDs to be prefixed with a dot */
#define NETSNMP_DS_LIB_HAVE_READ_PREMIB_CONFIG 26       /* have the pre-mib parsing config tokens been processed */
#define NETSNMP_DS_LIB_HAVE_READ_CONFIG    27   /* have the config tokens been processed */
#define NETSNMP_DS_LIB_QUICKE_PRINT        28
#define NETSNMP_DS_LIB_DONT_PRINT_UNITS    29 /* don't print UNITS suffix */
#define NETSNMP_DS_LIB_NO_DISPLAY_HINT     30 /* don't apply DISPLAY-HINTs */
#define NETSNMP_DS_LIB_16BIT_IDS           31   /* restrict requestIDs, etc to 16-bit values */
#define NETSNMP_DS_LIB_DONT_PERSIST_STATE  32   /* don't load config and don't load/save persistent file */
#define NETSNMP_DS_LIB_2DIGIT_HEX_OUTPUT   33   /* print a leading 0 on hex values &lt;= 'f' */
#define NETSNMP_DS_LIB_IGNORE_NO_COMMUNITY 34   /* don't complain if no community is specified in the command arguments */
#define NETSNMP_DS_LIB_DISABLE_PERSISTENT_LOAD  35 /* don't load persistent file */
#define NETSNMP_DS_LIB_DISABLE_PERSISTENT_SAVE  36 /* don't save persistent file */
#define NETSNMP_DS_LIB_APPEND_LOGFILES     37 /* append, don't overwrite, log files */

/*
* library integers
*/
#define NETSNMP_DS_LIB_MIB_WARNINGS  0
#define NETSNMP_DS_LIB_SECLEVEL      1
#define NETSNMP_DS_LIB_SNMPVERSION   2
#define NETSNMP_DS_LIB_DEFAULT_PORT  3
#define NETSNMP_DS_LIB_OID_OUTPUT_FORMAT  4
#define NETSNMP_DS_LIB_PRINT_SUFFIX_ONLY  NETSNMP_DS_LIB_OID_OUTPUT_FORMAT
#define NETSNMP_DS_LIB_STRING_OUTPUT_FORMAT 5
#define NETSNMP_DS_LIB_HEX_OUTPUT_LENGTH 6
#define NETSNMP_DS_LIB_SERVERSENDBUF   7 /* send buffer (server) */
#define NETSNMP_DS_LIB_SERVERRECVBUF   8 /* receive buffer (server) */
#define NETSNMP_DS_LIB_CLIENTSENDBUF   9 /* send buffer (client) */
#define NETSNMP_DS_LIB_CLIENTRECVBUF  10 /* receive buffer (client) */

/*
* special meanings for the default SNMP version slot (NETSNMP_DS_LIB_SNMPVERSION)
*/
#ifndef NETSNMP_DISABLE_SNMPV1
#define NETSNMP_DS_SNMP_VERSION_1    128        /* bogus */
#endif
#ifndef NETSNMP_DISABLE_SNMPV2C
#define NETSNMP_DS_SNMP_VERSION_2c   1  /* real */
#endif
#define NETSNMP_DS_SNMP_VERSION_3    3  /* real */


/*
* library strings
*/
#define NETSNMP_DS_LIB_SECNAME           0
#define NETSNMP_DS_LIB_CONTEXT           1
#define NETSNMP_DS_LIB_PASSPHRASE        2
#define NETSNMP_DS_LIB_AUTHPASSPHRASE    3
#define NETSNMP_DS_LIB_PRIVPASSPHRASE    4
#define NETSNMP_DS_LIB_OPTIONALCONFIG    5
#define NETSNMP_DS_LIB_APPTYPE           6
#define NETSNMP_DS_LIB_COMMUNITY         7
#define NETSNMP_DS_LIB_PERSISTENT_DIR    8
#define NETSNMP_DS_LIB_CONFIGURATION_DIR 9
#define NETSNMP_DS_LIB_SECMODEL          10
#define NETSNMP_DS_LIB_MIBDIRS           11
#define NETSNMP_DS_LIB_OIDSUFFIX         12
#define NETSNMP_DS_LIB_OIDPREFIX         13
#define NETSNMP_DS_LIB_CLIENT_ADDR       14
#define NETSNMP_DS_LIB_TEMP_FILE_PATTERN 15
#define NETSNMP_DS_LIB_AUTHMASTERKEY     16
#define NETSNMP_DS_LIB_PRIVMASTERKEY     17
#define NETSNMP_DS_LIB_AUTHLOCALIZEDKEY  18
#define NETSNMP_DS_LIB_PRIVLOCALIZEDKEY  19
#define NETSNMP_DS_LIB_APPTYPES          20
#define NETSNMP_DS_LIB_KSM_KEYTAB        21
#define NETSNMP_DS_LIB_KSM_SERVICE_NAME  22

/*</code></pre>
<h2>Functions</h2>
<dl>
<dt><code>int netsnmp_ds_set_boolean(int </code><i>store</i><code>, int </code><i>which</i><code>, int </code><i>val</i><code>);</code></p>
<dd>Stores <i>TRUE</i> if <i>val</i> != 0 or else <i>FALSE</i> into the bool_storage[store][which] slot. Returns <code>SNMPERR_GENERR</code> if the <i>store</i> and <i>which</i> parameters do not correspond to a valid slot, or <code>SNMPERR_SUCCESS</code> otherwise.</p>
<dt><code>int netsnmp_ds_get_boolean(int </code><i>store</i><code>, int </code><i>which</i><code>);</code></p>
<dd>Returns 1 if bool_storage[store][which] is <i>TRUE</i> or 0 if not. May also return <code>SNMPERR_GENERR</code> if the <i>store</i> and <i>which</i> parameters do not correspond to a valid slot.</p>
<dt><code>int netsnmp_ds_set_string(int </code><i>store</i><code>, int </code><i>which</i><code>, const char *</code><i>val</i><code>);</code></p>
<dd>Stores <i>val</i> into the string_storage[store][which] slot. Returns <code>SNMPERR_SUCCESS</code> normally, or <code>SNMPERR_GENERR</code> if the <i>store</i> and <i>which</i> parameters do not correspond to a valid slot.</p>
<dt><code>char *netsnmp_ds_get_string(int </code><i>store</i><code>, int </code><i>which</i><code>);</code></p>
<dd>Returns the string which has been stored in the string_storage[store][which] slot, or <code>NULL</code> if the <i>store</i> and <i>which</i> parameters do not correspond to a valid slot.</p>
<dt><code>netsnmp_ds_set_int(int </code><i>store</i><code>, int </code><i>which</i><code>, int </code><i>val</i><code>);</code></p>
<dd>Stores <i>val</i> into the int_storage[store][which] slot. Returns <code>SNMPERR_GENERR</code> if the <i>store</i> and <i>which</i> parameters do not correspond to a valid slot, or <code>SNMPERR_SUCCESS</code> otherwise.</p>
<dt><code>int netsnmp_ds_get_int(int </code><i>store</i><code>, int </code><i>which</i><code>);</code></p>
<dd>Returns the integer which has been stored in the int_storage[store][which] slot, or <code>SNMPERR_GENERR</code> if the <i>store</i> and <i>which</i> parameters do not correspond to a valid slot.</p>
<dt><code>void netsnmp_ds_shutdown(void);</code></p>
<dd>Reclaims memory used to hold information gathered by <code>netsnmp_ds_register_config</code> and <code>netsnmp_ds_register_premib</code>.</p>
<dt><code>int netsnmp_ds_register_config(u_char </code><i>type</i><code>, const char *</code><i>ftype</i><code>, const char *</code><i>token</i><code>, int </code><i>store</i><code>, int </code><i>which</i><code>);</code></p>
<dd>Registers a configuration file directive <i>token</i> and attaches it to a default storage type and slot. Specifically, <i>store</i> and <i>which</i> indicate the storage slot in the data type indicated by <i>type,</i> where <i>type</i> is one of the following constants: <code>ASN_BOOLEAN</code>, <code>ASN_INTEGER</code>, or <code>ASN_OCTET_STR</code>. The <i>ftype</i> variable indicates the file name base string searched for the <i>token</i> keyword. For example, the following call:</p>
<dl>
<dd>
<dl>
<dd>netsnmp_ds_register_config(ASN_INTEGER, &quot;snmp&quot;, &quot;testtoken&quot;, DS_APPLICATION_ID, 5)</dl>
</dl>
<dd>would indicate that when the snmp.conf file(s) were found and parsed, that any line beginning with the word &quot;testtoken&quot; should be read and the value after &quot;testtoken&quot; should be stored into the int_storage[DS_APPLICATION_ID][5] slot. For example the following line in the configuration file:</p>
<dl>
<dd>
<dl>
<dd>testtoken 502</dl>
</dl>
<dd>would set int_storage[DS_APPLICATION_ID][5] = 502. This function returns <code>SNMPERR_SUCCESS</code> if the registration was made successfully, or <code>SNMPERR_GENERR</code> if the registration was not made (perhaps because the <i>store</i> and <i>which</i> parameters do not correspond to a valid slot, or because of a memory allocation failure).</p>
<dt><code>int netsnmp_ds_register_premib(u_char </code><i>type</i><code>, const char *</code><i>ftype</i><code>, const char *</code><i>token</i><code>, int </code><i>store</i><code>, int </code><i>which</i><code>);</code></p>
<dd>Analogous to the preceeding function, but the <i>token</i> is processed before MIBs are read (this is therefore useful for controlling MIB processing options).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-snmp_config/">snmp_config</a></code>(5), <code><a href="/docs/linux/man/3-read_config/">read_config</a></code>(3) </p>
