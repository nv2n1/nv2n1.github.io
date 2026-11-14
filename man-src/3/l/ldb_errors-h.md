---
title: "ldb_errors-h(3)"
name: "ldb_errors-h"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb_errors-h/"
description: "include/ldb_errors.h –"
---

<p>include/ldb_errors.h &#8211; </p>
<p> This header provides a set of result codes for LDB function calls.</p>
<h2>Synopsis</h2>
<h3>Macros</h3>
<p>#define <code>LDB_SUCCESS</code> 0<br />
 <i>The function call succeeded. </i><br />
 #define <code>LDB_ERR_OPERATIONS_ERROR</code> 1<br />
 <i>The function call failed for some non-specific reason. </i><br />
 #define <code>LDB_ERR_PROTOCOL_ERROR</code> 2<br />
 <i>The function call failed because of a protocol violation. </i><br />
 #define <code>LDB_ERR_TIME_LIMIT_EXCEEDED</code> 3<br />
 <i>The function call failed because a time limit was exceeded. </i><br />
 #define <code>LDB_ERR_SIZE_LIMIT_EXCEEDED</code> 4<br />
 <i>The function call failed because a size limit was exceeded. </i><br />
 #define <code>LDB_ERR_COMPARE_FALSE</code> 5<br />
 <i>The function was for value comparison, and the comparison operation returned false. </i><br />
 #define <code>LDB_ERR_COMPARE_TRUE</code> 6<br />
 <i>The function was for value comparison, and the comparison operation returned true. </i><br />
 #define <code>LDB_ERR_AUTH_METHOD_NOT_SUPPORTED</code> 7<br />
 <i>The function used an authentication method that is not supported by the database. </i><br />
 #define <code>LDB_ERR_STRONG_AUTH_REQUIRED</code> 8<br />
 <i>The function call required a underlying operation that required strong authentication. </i><br />
 #define <code>LDB_ERR_REFERRAL</code> 10<br />
 <i>The function resulted in a referral to another server. </i><br />
 #define <code>LDB_ERR_ADMIN_LIMIT_EXCEEDED</code> 11<br />
 <i>The function failed because an administrative / policy limit was exceeded. </i><br />
 #define <code>LDB_ERR_UNSUPPORTED_CRITICAL_EXTENSION</code> 12<br />
 <i>The function required an extension or capability that the database cannot provide. </i><br />
 #define <code>LDB_ERR_CONFIDENTIALITY_REQUIRED</code> 13<br />
 <i>The function involved a transaction or database operation that could not be performed without a secure link. </i><br />
 #define <code>LDB_ERR_SASL_BIND_IN_PROGRESS</code> 14<br />
 <i>This is an intermediate result code for SASL bind operations that have more than one step. </i><br />
 #define <code>LDB_ERR_NO_SUCH_ATTRIBUTE</code> 16<br />
 <i>The function referred to an attribute type that is not present in the entry. </i><br />
 #define <code>LDB_ERR_UNDEFINED_ATTRIBUTE_TYPE</code> 17<br />
 <i>The function referred to an attribute type that is invalid. </i><br />
 #define <code>LDB_ERR_INAPPROPRIATE_MATCHING</code> 18<br />
 <i>The function required a filter type that is not available for the specified attribute. </i><br />
 #define <code>LDB_ERR_CONSTRAINT_VIOLATION</code> 19<br />
 <i>The function would have violated an attribute constraint. </i><br />
 #define <code>LDB_ERR_ATTRIBUTE_OR_VALUE_EXISTS</code> 20<br />
 <i>The function involved an attribute type or attribute value that already exists in the entry. </i><br />
 #define <code>LDB_ERR_INVALID_ATTRIBUTE_SYNTAX</code> 21<br />
 <i>The function used an invalid (incorrect syntax) attribute value. </i><br />
 #define <code>LDB_ERR_NO_SUCH_OBJECT</code> 32<br />
 <i>The function referred to an object that does not exist in the database. </i><br />
 #define <code>LDB_ERR_ALIAS_PROBLEM</code> 33<br />
 <i>The function referred to an alias which points to a non-existent object in the database. </i><br />
 #define <code>LDB_ERR_INVALID_DN_SYNTAX</code> 34<br />
 <i>The function used a DN which was invalid (incorrect syntax). </i><br />
 #define <code>LDB_ERR_ALIAS_DEREFERENCING_PROBLEM</code> 36<br />
 <i>The function required dereferencing of an alias, and something went wrong during the dereferencing process. </i><br />
 #define <code>LDB_ERR_INAPPROPRIATE_AUTHENTICATION</code> 48<br />
 <i>The function passed in the wrong authentication method. </i><br />
 #define <code>LDB_ERR_INVALID_CREDENTIALS</code> 49<br />
 <i>The function passed in or referenced incorrect credentials during authentication. </i><br />
 #define <code>LDB_ERR_INSUFFICIENT_ACCESS_RIGHTS</code> 50<br />
 <i>The function required access permissions that the user does not possess. </i><br />
 #define <code>LDB_ERR_BUSY</code> 51<br />
 <i>The function required a transaction or call that the database could not perform because it is busy. </i><br />
 #define <code>LDB_ERR_UNAVAILABLE</code> 52<br />
 <i>The function required a transaction or call to a database that is not available. </i><br />
 #define <code>LDB_ERR_UNWILLING_TO_PERFORM</code> 53<br />
 <i>The function required a transaction or call to a database that the database declined to perform. </i><br />
 #define <code>LDB_ERR_LOOP_DETECT</code> 54<br />
 <i>The function failed because it resulted in a loop being detected. </i><br />
 #define <code>LDB_ERR_NAMING_VIOLATION</code> 64<br />
 <i>The function failed because it would have violated a naming rule. </i><br />
 #define <code>LDB_ERR_OBJECT_CLASS_VIOLATION</code> 65<br />
 <i>The function failed because it would have violated the schema. </i><br />
 #define <code>LDB_ERR_NOT_ALLOWED_ON_NON_LEAF</code> 66<br />
 <i>The function required an operation that is only allowed on leaf objects, but the object is not a leaf. </i><br />
 #define <code>LDB_ERR_NOT_ALLOWED_ON_RDN</code> 67<br />
 <i>The function required an operation that cannot be performed on a Relative DN, but the object is a Relative DN. </i><br />
 #define <code>LDB_ERR_ENTRY_ALREADY_EXISTS</code> 68<br />
 <i>The function failed because the entry already exists. </i><br />
 #define <code>LDB_ERR_OBJECT_CLASS_MODS_PROHIBITED</code> 69<br />
 <i>The function failed because modifications to an object class are not allowable. </i><br />
 #define <code>LDB_ERR_AFFECTS_MULTIPLE_DSAS</code> 71<br />
 <i>The function failed because it needed to be applied to multiple databases. </i><br />
 #define <code>LDB_ERR_OTHER</code> 80<br />
 <i>The function failed for unknown reasons. </i></p>
<h2>Detailed Description</h2>
<p>This header provides a set of result codes for LDB function calls. </p>
<p> Many LDB function calls return an integer value (int). As shown in the function documentation, those return values may indicate whether the function call worked correctly (in which case it returns LDB_SUCCESS) or some problem occurred (in which case some other value will be returned). As a special case, LDB_ERR_COMPARE_FALSE or LDB_ERR_COMPARE_TRUE may be returned, which does not indicate an error. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Not all error codes make sense for LDB, however they are based on the LDAP error codes, and are kept for reference and to avoid overlap. </p>
<p> Some of this documentation is based on information in the OpenLDAP documentation, as developed and maintained by the The OpenLDAP Project.</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define LDB_ERR_ADMIN_LIMIT_EXCEEDED 11</h3>
<p>The function failed because an administrative / policy limit was exceeded.</p>
<h3>#define LDB_ERR_AFFECTS_MULTIPLE_DSAS 71</h3>
<p>The function failed because it needed to be applied to multiple databases.</p>
<h3>#define LDB_ERR_ALIAS_DEREFERENCING_PROBLEM 36</h3>
<p>The function required dereferencing of an alias, and something went wrong during the dereferencing process.</p>
<h3>#define LDB_ERR_ALIAS_PROBLEM 33</h3>
<p>The function referred to an alias which points to a non-existent object in the database.</p>
<h3>#define LDB_ERR_ATTRIBUTE_OR_VALUE_EXISTS 20</h3>
<p>The function involved an attribute type or attribute value that already exists in the entry.</p>
<h3>#define LDB_ERR_AUTH_METHOD_NOT_SUPPORTED 7</h3>
<p>The function used an authentication method that is not supported by the database.</p>
<h3>#define LDB_ERR_BUSY 51</h3>
<p>The function required a transaction or call that the database could not perform because it is busy.</p>
<h3>#define LDB_ERR_COMPARE_FALSE 5</h3>
<p>The function was for value comparison, and the comparison operation returned false. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This is a status value, and doesn&#8217;t normally indicate an error.</dl>
<h3>#define LDB_ERR_COMPARE_TRUE 6</h3>
<p>The function was for value comparison, and the comparison operation returned true. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This is a status value, and doesn&#8217;t normally indicate an error.</dl>
<h3>#define LDB_ERR_CONFIDENTIALITY_REQUIRED 13</h3>
<p>The function involved a transaction or database operation that could not be performed without a secure link.</p>
<h3>#define LDB_ERR_CONSTRAINT_VIOLATION 19</h3>
<p>The function would have violated an attribute constraint.</p>
<h3>#define LDB_ERR_ENTRY_ALREADY_EXISTS 68</h3>
<p>The function failed because the entry already exists.</p>
<h3>#define LDB_ERR_INAPPROPRIATE_AUTHENTICATION 48</h3>
<p>The function passed in the wrong authentication method.</p>
<h3>#define LDB_ERR_INAPPROPRIATE_MATCHING 18</h3>
<p>The function required a filter type that is not available for the specified attribute.</p>
<h3>#define LDB_ERR_INSUFFICIENT_ACCESS_RIGHTS 50</h3>
<p>The function required access permissions that the user does not possess.</p>
<h3>#define LDB_ERR_INVALID_ATTRIBUTE_SYNTAX 21</h3>
<p>The function used an invalid (incorrect syntax) attribute value.</p>
<h3>#define LDB_ERR_INVALID_CREDENTIALS 49</h3>
<p>The function passed in or referenced incorrect credentials during authentication.</p>
<h3>#define LDB_ERR_INVALID_DN_SYNTAX 34</h3>
<p>The function used a DN which was invalid (incorrect syntax).</p>
<h3>#define LDB_ERR_LOOP_DETECT 54</h3>
<p>The function failed because it resulted in a loop being detected.</p>
<h3>#define LDB_ERR_NAMING_VIOLATION 64</h3>
<p>The function failed because it would have violated a naming rule.</p>
<h3>#define LDB_ERR_NO_SUCH_ATTRIBUTE 16</h3>
<p>The function referred to an attribute type that is not present in the entry.</p>
<h3>#define LDB_ERR_NO_SUCH_OBJECT 32</h3>
<p>The function referred to an object that does not exist in the database.</p>
<h3>#define LDB_ERR_NOT_ALLOWED_ON_NON_LEAF 66</h3>
<p>The function required an operation that is only allowed on leaf objects, but the object is not a leaf.</p>
<h3>#define LDB_ERR_NOT_ALLOWED_ON_RDN 67</h3>
<p>The function required an operation that cannot be performed on a Relative DN, but the object is a Relative DN.</p>
<h3>#define LDB_ERR_OBJECT_CLASS_MODS_PROHIBITED 69</h3>
<p>The function failed because modifications to an object class are not allowable.</p>
<h3>#define LDB_ERR_OBJECT_CLASS_VIOLATION 65</h3>
<p>The function failed because it would have violated the schema.</p>
<h3>#define LDB_ERR_OPERATIONS_ERROR 1</h3>
<p>The function call failed for some non-specific reason.</p>
<h3>#define LDB_ERR_OTHER 80</h3>
<p>The function failed for unknown reasons.</p>
<h3>#define LDB_ERR_PROTOCOL_ERROR 2</h3>
<p>The function call failed because of a protocol violation.</p>
<h3>#define LDB_ERR_REFERRAL 10</h3>
<p>The function resulted in a referral to another server.</p>
<h3>#define LDB_ERR_SASL_BIND_IN_PROGRESS 14</h3>
<p>This is an intermediate result code for SASL bind operations that have more than one step. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This is a result code that does not normally indicate an error has occurred.</dl>
<h3>#define LDB_ERR_SIZE_LIMIT_EXCEEDED 4</h3>
<p>The function call failed because a size limit was exceeded.</p>
<h3>#define LDB_ERR_STRONG_AUTH_REQUIRED 8</h3>
<p>The function call required a underlying operation that required strong authentication. This will normally only occur if you are using LDB with a LDAP backend.</p>
<h3>#define LDB_ERR_TIME_LIMIT_EXCEEDED 3</h3>
<p>The function call failed because a time limit was exceeded.</p>
<h3>#define LDB_ERR_UNAVAILABLE 52</h3>
<p>The function required a transaction or call to a database that is not available.</p>
<h3>#define LDB_ERR_UNDEFINED_ATTRIBUTE_TYPE 17</h3>
<p>The function referred to an attribute type that is invalid.</p>
<h3>#define LDB_ERR_UNSUPPORTED_CRITICAL_EXTENSION 12</h3>
<p>The function required an extension or capability that the database cannot provide.</p>
<h3>#define LDB_ERR_UNWILLING_TO_PERFORM 53</h3>
<p>The function required a transaction or call to a database that the database declined to perform.</p>
<h3>#define LDB_SUCCESS 0</h3>
<p>The function call succeeded. If a function returns LDB_SUCCESS, then that function, and the underlying transactions that may have been required, completed successfully. </p>
<p> <code>Examples: </code> <code>ldbreader.c</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LDB from the source code.</p>
