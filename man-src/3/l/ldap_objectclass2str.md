---
title: "ldap_objectclass2str(3)"
name: "ldap_objectclass2str"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldap_objectclass2str/"
description: "ldap_str2syntax, ldap_syntax2str, ldap_syntax2name, ldap_syntax_free, ldap_str2matchingrule, ldap_matchingrule2str, ldap_matchingrule2name, ldap_matchingrule_free, ldap_str2attributetype, ldap_attr..."
---

<h2 class="name">NAME</h2>
<p> ldap_str2syntax, ldap_syntax2str, ldap_syntax2name, ldap_syntax_free, ldap_str2matchingrule, ldap_matchingrule2str, ldap_matchingrule2name, ldap_matchingrule_free, ldap_str2attributetype, ldap_attributetype2str, ldap_attributetype2name, ldap_attributetype_free, ldap_str2objectclass, ldap_objectclass2str, ldap_objectclass2name, ldap_objectclass_free, ldap_scherr2str &#8211; Schema definition handling routines </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LDAP (libldap, -lldap)</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ldap.h&gt;
#include &lt;ldap_schema.h&gt;
LDAPSyntax *ldap_str2syntax(s, code, errp, flags)
    const char *s;
int *code;
const char **errp;
const int flags;
char *ldap_syntax2str(syn)
    const LDAPSyntax *syn;
const char *ldap_syntax2name(syn)
LDAPSyntax *syn;
ldap_syntax_free(syn)
    LDAPSyntax *syn;
LDAPMatchingRule *ldap_str2matchingrule(s, code, errp, flags)
    const char *s;
int *code;
const char **errp;
const int flags;
char *ldap_matchingrule2str(mr);
const LDAPMatchingRule *mr;
const char *ldap_matchingrule2name(mr)
LDAPMatchingRule *mr;
ldap_matchingrule_free(mr)
    LDAPMatchingRule *mr;
LDAPAttributeType *ldap_str2attributetype(s, code, errp, flags)
    const char *s;
int *code;
const char **errp;
const int flags;
char *ldap_attributetype2str(at)
    const LDAPAttributeType *at;
const char *ldap_attributetype2name(at)
LDAPAttributeType *at;
ldap_attributetype_free(at)
    LDAPAttributeType *at;
LDAPObjectClass *ldap_str2objectclass(s, code, errp, flags)
    const char *s;
int *code;
const char **errp;
const int flags;
char *ldap_objectclass2str(oc)
    const LDAPObjectClass *oc;
const char *ldap_objectclass2name(oc)
LDAPObjectClass *oc;
ldap_objectclass_free(oc)
    LDAPObjectClass *oc;
char *ldap_scherr2str(code)
int code;
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines are used to parse schema definitions in the syntax defined in RFC 4512 into structs and handle these structs. These routines handle four kinds of definitions: syntaxes, matching rules, attribute types and object classes. For each definition kind, four routines are provided. </p>
<p> <code>ldap_str2xxx()</code> takes a definition in RFC 4512 format in argument <i>s</i> as a NUL-terminated string and returns, if possible, a pointer to a newly allocated struct of the appropriate kind. The caller is responsible for freeing the struct by calling <code>ldap_xxx_free()</code> when not needed any longer. The routine returns NULL if some problem happened. In this case, the integer pointed at by argument <i>code</i> will receive an error code (see below the description of <code>ldap_scherr2str()</code> for an explanation of the values) and a pointer to a NUL-terminated string will be placed where requested by argument <i>errp</i> , indicating where in argument <i>s</i> the error happened, so it must not be freed by the caller. Argument <i>flags</i> is a bit mask of parsing options controlling the relaxation of the syntax recognized. The following values are defined:</p>
<dl>
<dt><code>LDAP_SCHEMA_ALLOW_NONE</code></p>
<dd> strict parsing according to RFC 4512.</p>
<dt><code>LDAP_SCHEMA_ALLOW_NO_OID</code></p>
<dd> permit definitions that do not contain an initial OID.</p>
<dt><code>LDAP_SCHEMA_ALLOW_QUOTED</code></p>
<dd> permit quotes around some items that should not have them.</p>
<dt><code>LDAP_SCHEMA_ALLOW_DESCR</code></p>
<dd> permit a <code>descr</code> instead of a numeric OID in places where the syntax expect the latter.</p>
<dt><code>LDAP_SCHEMA_ALLOW_DESCR_PREFIX</code></p>
<dd> permit that the initial numeric OID contains a prefix in <code>descr</code> format.</p>
<dt><code>LDAP_SCHEMA_ALLOW_ALL</code></p>
<dd> be very liberal, include all options.</dl>
<p> The structures returned are as follows: </p>
<dl>
<dt>
<dd>
<pre><code>
typedef struct ldap_schema_extension_item {
    char *lsei_name;    /* Extension name */
    char **lsei_values; /* Extension values */
} LDAPSchemaExtensionItem;
typedef struct ldap_syntax {
    char *syn_oid;                            /* OID */
    char **syn_names;                         /* Names */
    char *syn_desc;                           /* Description */
    LDAPSchemaExtensionItem **syn_extensions; /* Extension */
} LDAPSyntax;
typedef struct ldap_matchingrule {
    char *mr_oid;                            /* OID */
    char **mr_names;                         /* Names */
    char *mr_desc;                           /* Description */
    int mr_obsolete;                         /* Is obsolete? */
    char *mr_syntax_oid;                     /* Syntax of asserted values */
    LDAPSchemaExtensionItem **mr_extensions; /* Extensions */
} LDAPMatchingRule;
typedef struct ldap_attributetype {
    char *at_oid;                            /* OID */
    char **at_names;                         /* Names */
    char *at_desc;                           /* Description */
    int at_obsolete;                         /* Is obsolete? */
    char *at_sup_oid;                        /* OID of superior type */
    char *at_equality_oid;                   /* OID of equality matching rule */
    char *at_ordering_oid;                   /* OID of ordering matching rule */
    char *at_substr_oid;                     /* OID of substrings matching rule */
    char *at_syntax_oid;                     /* OID of syntax of values */
    int at_syntax_len;                       /* Suggested minimum maximum length */
    int at_single_value;                     /* Is single-valued?  */
    int at_collective;                       /* Is collective? */
    int at_no_user_mod;                      /* Are changes forbidden through LDAP? */
    int at_usage;                            /* Usage, see below */
    LDAPSchemaExtensionItem **at_extensions; /* Extensions */
} LDAPAttributeType;
typedef struct ldap_objectclass {
    char *oc_oid;                            /* OID */
    char **oc_names;                         /* Names */
    char *oc_desc;                           /* Description */
    int oc_obsolete;                         /* Is obsolete? */
    char **oc_sup_oids;                      /* OIDs of superior classes */
    int oc_kind;                             /* Kind, see below */
    char **oc_at_oids_must;                  /* OIDs of required attribute types */
    char **oc_at_oids_may;                   /* OIDs of optional attribute types */
    LDAPSchemaExtensionItem **oc_extensions; /* Extensions */
} LDAPObjectClass;
</code></pre>
</dl>
<p> Some integer fields (those described with a question mark) have a truth value, for these fields the possible values are:</p>
<dl>
<dt><code>LDAP_SCHEMA_NO</code></p>
<dd> The answer to the question is no.</p>
<dt><code>LDAP_SCHEMA_YES</code></p>
<dd> The answer to the question is yes.</dl>
<p> For attribute types, the following usages are possible:</p>
<dl>
<dt><code>LDAP_SCHEMA_USER_APPLICATIONS</code></p>
<dd> the attribute type is non-operational.</p>
<dt><code>LDAP_SCHEMA_DIRECTORY_OPERATION</code></p>
<dd> the attribute type is operational and is pertinent to the directory itself, i.e. it has the same value on all servers that master the entry containing this attribute type.</p>
<dt><code>LDAP_SCHEMA_DISTRIBUTED_OPERATION</code></p>
<dd> the attribute type is operational and is pertinent to replication, shadowing or other distributed directory aspect. TBC.</p>
<dt><code>LDAP_SCHEMA_DSA_OPERATION</code></p>
<dd> the attribute type is operational and is pertinent to the directory server itself, i.e. it may have different values for the same entry when retrieved from different servers that master the entry.</dl>
<p> Object classes can be of three kinds:</p>
<dl>
<dt><code>LDAP_SCHEMA_ABSTRACT</code></p>
<dd> the object class is abstract, i.e. there cannot be entries of this class alone.</p>
<dt><code>LDAP_SCHEMA_STRUCTURAL</code></p>
<dd> the object class is structural, i.e. it describes the main role of the entry. On some servers, once the entry is created the set of structural object classes assigned cannot be changed: none of those present can be removed and none other can be added.</p>
<dt><code>LDAP_SCHEMA_AUXILIARY</code></p>
<dd> the object class is auxiliary, i.e. it is intended to go with other, structural, object classes. These can be added or removed at any time if attribute types are added or removed at the same time as needed by the set of object classes resulting from the operation.</dl>
<p> Routines <code>ldap_xxx2name()</code> return a canonical name for the definition. </p>
<p> Routines <code>ldap_xxx2str()</code> return a string representation in the format described by RFC 4512 of the struct passed in the argument. The string is a newly allocated string that must be freed by the caller. These routines may return NULL if no memory can be allocated for the string. </p>
<p> <code>ldap_scherr2str()</code> returns a NUL-terminated string with a text description of the error found. This is a pointer to a static area, so it must not be freed by the caller. The argument <i>code</i> comes from one of the parsing routines and can adopt the following values:</p>
<dl>
<dt><code>LDAP_SCHERR_OUTOFMEM</code></p>
<dd> Out of memory.</p>
<dt><code>LDAP_SCHERR_UNEXPTOKEN</code></p>
<dd> Unexpected token.</p>
<dt><code>LDAP_SCHERR_NOLEFTPAREN</code></p>
<dd> Missing opening parenthesis.</p>
<dt><code>LDAP_SCHERR_NORIGHTPAREN</code></p>
<dd> Missing closing parenthesis.</p>
<dt><code>LDAP_SCHERR_NODIGIT</code></p>
<dd> Expecting digit.</p>
<dt><code>LDAP_SCHERR_BADNAME</code></p>
<dd> Expecting a name.</p>
<dt><code>LDAP_SCHERR_BADDESC</code></p>
<dd> Bad description.</p>
<dt><code>LDAP_SCHERR_BADSUP</code></p>
<dd> Bad superiors.</p>
<dt><code>LDAP_SCHERR_DUPOPT</code></p>
<dd> Duplicate option.</p>
<dt><code>LDAP_SCHERR_EMPTY</code></p>
<dd> Unexpected end of data. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3)</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
